"""Scrape comp.lang.cobol content missing from our Giganews mbox via UsenetArchives.com.

Output: one synthetic mbox `comp.lang.cobol.gap.mbox` that `archive.py` can
parse alongside the Giganews mbox. Resumable via `gap_state.json`.

Two regions of our existing archive are incomplete:

  1. Mid-1990s gap. We have:
       * One Nov 1994 message (Nov 30), 249 Dec 1994 messages (Dec 1–16).
       * Hard gap from 1994-12-17 through 1998-06-22.
       * Resumes 1998-06-23 (June through Jun 28; then July onward).
     UA.com fills this: 1994 (Nov 10 – Dec 31, 133 threads) through
     1998 (Jan 2 – Dec 31, 3,227 threads).

  2. Post-snapshot tail. Our mbox was captured 2013-06-11, so we have
     nothing after that date. UA.com has comp.lang.cobol activity through
     2022 — declining traffic and an increasing spam ratio in later years,
     but the spam filter handles that.

The default scope below covers both regions (1994–1998 + 2013–2022). We
dedupe by *root Message-ID* against our existing archive, so threads
already present (most of 1998-H2, most of 2013-H1) are skipped without
fetching. Pre-1994 is not available on UA.com (their earliest year for
this group is 1994); the only known pre-1994 source was the UTZOO Wiseman
archive, removed from the Internet Archive in 2020.

Key design choices:
- Root Message-IDs are real (base64-decoded from the `view.php?mid=` URL param).
- Reply Message-IDs are synthesized: <gap-{md5(root)[:10]}-p{N}@usenetarchives.gap>.
- Author "emails" are synthesized from stable UA.com author IDs:
  <ua-author-{id}@usenetarchives.gap>. Display name passes through.
- Within-day sort is preserved by adding the post number (in seconds) to the
  UA-supplied (hour-precision) timestamp.
- `X-Source: usenetarchives.com` marks scraped entries downstream.
- Polite: respects robots.txt `Crawl-delay: 10` for AI crawlers.
"""
from __future__ import annotations

import argparse
import base64
import calendar
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

from playwright.sync_api import Page, sync_playwright

PROJECT_DIR = Path(__file__).resolve().parent
STATE_FILE = PROJECT_DIR / "gap_state.json"
OUT_MBOX = PROJECT_DIR / "comp.lang.cobol.gap.mbox"

UA_BASE = "https://usenetarchives.com"
NEWSGROUP = "comp.lang.cobol"
CRAWL_DELAY = 10.0  # seconds, per UA robots.txt for AI crawlers

MONTH_NAME_TO_NUM = {m: i for i, m in enumerate(calendar.month_abbr) if m}


@dataclass
class IndexRow:
    mid_b64: str       # The URL-encoded base64 from the `mid=` param
    root_mid: str      # Decoded Message-ID (e.g., "<...@host>")
    subject: str
    post_count: int
    date_iso: str      # "YYYY-MM-DD" from the index listing


@dataclass
class Post:
    n: int             # 1-indexed post number
    depth: int
    author_id: str
    author_display: str
    timestamp_text: str  # "Jan 13, 1996 19:00 UTC" — raw
    body: str            # cleaned body text (paragraphs joined with \n)


def b64_decode_mid(mid_b64: str) -> str:
    """Decode UA's URL-base64 `mid` param back to a real Message-ID."""
    raw = mid_b64.replace("%3D", "=").replace("%2B", "+").replace("%2F", "/")
    # UA strips padding; restore it.
    pad = (-len(raw)) % 4
    return base64.b64decode(raw + "=" * pad).decode("utf-8", errors="replace")


def root_anchor(root_mid: str) -> str:
    return hashlib.md5(root_mid.encode("utf-8", errors="replace")).hexdigest()[:10]


def normalize_root_mid(raw: str) -> str:
    """Ensure a root MID is in <id@host> form so archive.py's MSGID_RE matches.

    UA.com sometimes returns a bare Google Groups conversation ID (e.g.,
    'WuGYNstiLCo') for threads where the original Message-ID was lost during
    their Giganews import. We wrap those so they parse as real MIDs and so
    references to them resolve during threading.
    """
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">") and "@" in raw:
        return raw
    # Strip stray angle brackets if only one side, then wrap.
    raw = raw.strip("<>")
    return f"<ua-fallback-{raw}@usenetarchives.gap>"


def bypass_age_gate(page: Page) -> None:
    """Submit the age verification form so subsequent requests work."""
    page.evaluate(
        """() => {
          document.getElementById('dobMonth').value = '1';
          document.getElementById('dobDay').value = '1';
          document.getElementById('dobYear').value = '1990';
          document.getElementById('ageForm').submit();
        }"""
    )
    page.wait_for_load_state("networkidle")


def _wait_for_threads_table(page: Page) -> bool:
    """Wait until the DataTables-rendered thread list is populated."""
    try:
        page.wait_for_load_state("networkidle", timeout=15000)
    except Exception:
        pass
    try:
        page.wait_for_selector('a[href^="view.php"]', timeout=15000)
        return True
    except Exception:
        return False


def fetch_index_page(page: Page, year: int, page_n: int) -> tuple[list[IndexRow], bool]:
    """Return (rows, has_next_page). Rows in display order."""
    url = f"{UA_BASE}/threads.php?id={NEWSGROUP}&y={year}&r=0&p={page_n}"
    page.goto(url, wait_until="domcontentloaded")
    # Age gate appears on first request only.
    if "Age Verification" in (page.title() or ""):
        bypass_age_gate(page)
        page.goto(url, wait_until="domcontentloaded")
    if not _wait_for_threads_table(page):
        # Empty page (past the last) — no thread links will appear.
        return [], False

    data = page.evaluate(
        """() => {
          // The thread index is a table-ish layout. Each thread row has a
          // link to view.php?mid=..., plus columns for post count and date.
          // We find the date by looking at the row's text content.
          const links = Array.from(document.querySelectorAll('a[href^="view.php"]'));
          const seen = new Set();
          const rows = [];
          for (const a of links) {
            const href = a.getAttribute('href');
            const m = href.match(/mid=([^&]+)/);
            if (!m) continue;
            const mid_b64 = m[1];
            if (seen.has(mid_b64)) continue;  // dedupe (subject + count both link to thread)
            seen.add(mid_b64);
            // Walk up to the row containing this anchor.
            let row = a.closest('tr, .thread-row, .thread-item, li, div');
            // Find the next sibling cells/spans for posts and date.
            let rowText = '';
            if (row) rowText = row.innerText || '';
            else rowText = a.parentElement?.innerText || '';
            rows.push({ mid_b64, subject: a.textContent.trim(), rowText });
          }
          return rows;
        }"""
    )

    out: list[IndexRow] = []
    for r in data:
        text = r["rowText"]
        # Extract post count and date from the row's text.
        # Layout: "<subject>\t<count>\t<YYYY-MM-DD>" (tabs OR runs of spaces).
        date_m = re.search(r"(\d{4}-\d{2}-\d{2})", text)
        count_m = re.search(r"\b(\d+)\b\s*\d{4}-\d{2}-\d{2}", text)
        if not date_m:
            continue
        try:
            root_mid = normalize_root_mid(b64_decode_mid(r["mid_b64"]))
        except Exception:
            continue
        out.append(IndexRow(
            mid_b64=r["mid_b64"],
            root_mid=root_mid,
            subject=r["subject"],
            post_count=int(count_m.group(1)) if count_m else 0,
            date_iso=date_m.group(1),
        ))

    # Has-next-page heuristic: 100 rows means likely more to come.
    has_next = len(out) >= 100
    return out, has_next


def fetch_thread(page: Page, mid_b64: str) -> list[Post]:
    url = f"{UA_BASE}/view.php?id={NEWSGROUP}&mid={mid_b64}"
    page.goto(url, wait_until="domcontentloaded")
    if "Age Verification" in (page.title() or ""):
        bypass_age_gate(page)
        page.goto(url, wait_until="domcontentloaded")
    try:
        page.wait_for_selector(".post-card", timeout=15000)
    except Exception:
        return []

    posts_data = page.evaluate(
        """() => {
          return Array.from(document.querySelectorAll('.post-card')).map((card, idx) => {
            const depth = parseInt(card.getAttribute('data-depth') || '0', 10);
            const authorAnchor = card.querySelector('.post-author a');
            const authorId = authorAnchor ?
              (authorAnchor.getAttribute('href').match(/id=(\\d+)/) || [])[1] || '' : '';
            const authorDisplay = authorAnchor ? authorAnchor.textContent.trim() :
              (card.querySelector('.post-author')?.textContent?.trim() || '');
            const timestamp = card.querySelector('.post-timestamp')?.textContent?.trim() || '';
            // Body: join paragraphs with newlines. UA wraps each text run in <p>.
            const body = Array.from(card.querySelectorAll('.post-body p'))
              .map(p => p.innerText.replace(/\\n+$/, ''))
              .join('\\n');
            return { idx, depth, authorId, authorDisplay, timestamp, body };
          });
        }"""
    )
    return [
        Post(
            n=p["idx"] + 1,
            depth=p["depth"],
            author_id=p["authorId"] or "unknown",
            author_display=p["authorDisplay"],
            timestamp_text=p["timestamp"],
            body=p["body"],
        )
        for p in posts_data
    ]


def parse_ua_timestamp(text: str, post_n: int) -> datetime:
    """Parse 'Jan 13, 1996 19:00 UTC' → datetime; add post_n seconds for tiebreak."""
    # Pattern: Mon D, YYYY H:MM UTC
    m = re.match(r"([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})\s+(\d{1,2}):(\d{2})\s*UTC", text.strip())
    if not m:
        # Fallback: epoch zero plus post number for stable sort
        return datetime(1970, 1, 1, tzinfo=timezone.utc).replace(second=min(post_n, 59))
    mon = MONTH_NAME_TO_NUM.get(m.group(1)[:3].title(), 1)
    return datetime(
        year=int(m.group(3)),
        month=mon,
        day=int(m.group(2)),
        hour=int(m.group(4)),
        minute=int(m.group(5)),
        second=min(post_n, 59),
        tzinfo=timezone.utc,
    )


def synth_reply_mid(root_anchor_str: str, post_n: int) -> str:
    return f"<gap-{root_anchor_str}-p{post_n}@usenetarchives.gap>"


def synth_author_email(author_id: str) -> str:
    return f"ua-author-{author_id}@usenetarchives.gap"


def build_references(posts: list[Post], target_idx: int) -> list[str]:
    """Walk back through posts to construct References (root → ... → parent)."""
    refs: list[str] = []
    target_depth = posts[target_idx].depth
    if target_depth == 0:
        return refs
    # Walk backwards finding ancestor at each decreasing depth.
    wanted_depth = target_depth - 1
    chain: list[int] = []
    i = target_idx - 1
    while i >= 0 and wanted_depth >= 0:
        if posts[i].depth == wanted_depth:
            chain.append(i)
            wanted_depth -= 1
        i -= 1
    # chain has ancestors from immediate-parent to root; References is root-first.
    return list(reversed(chain))


def render_message(
    post: Post,
    posts: list[Post],
    post_idx: int,
    root_mid: str,
    subject: str,
) -> str:
    """Render one Post as an RFC822-ish message body suitable for our mbox."""
    root_anc = root_anchor(root_mid)
    is_root = post.depth == 0 and post.n == 1

    if is_root:
        msg_id = root_mid
    else:
        msg_id = synth_reply_mid(root_anc, post.n)

    dt = parse_ua_timestamp(post.timestamp_text, post.n)
    # Subject: roots get the literal subject; replies get "Re: <subject>"
    # if it doesn't already start with Re:.
    subj = subject if is_root else (
        subject if re.match(r"^\s*Re:", subject, re.I) else f"Re: {subject}"
    )

    author_email = synth_author_email(post.author_id)
    # Display name might be truncated like "im..." — keep as-is for fidelity.
    from_header = f'"{post.author_display}" <{author_email}>'

    # Build References / In-Reply-To from depth-walk.
    ancestor_indices = build_references(posts, post_idx)
    references: list[str] = []
    for anc_idx in ancestor_indices:
        anc = posts[anc_idx]
        if anc.depth == 0 and anc.n == 1:
            references.append(root_mid)
        else:
            references.append(synth_reply_mid(root_anc, anc.n))
    in_reply_to = references[-1] if references else ""

    headers = [
        f"From: {from_header}",
        f"Subject: {subj}",
        f"Date: {dt.strftime('%a, %d %b %Y %H:%M:%S +0000')}",
        f"Newsgroups: {NEWSGROUP}",
        f"Message-ID: {msg_id}",
    ]
    if in_reply_to:
        headers.append(f"In-Reply-To: {in_reply_to}")
    if references:
        headers.append(f"References: {' '.join(references)}")
    headers.append("X-Source: usenetarchives.com")
    headers.append(f"X-UA-PostNum: {post.n}")
    headers.append(f"X-UA-Depth: {post.depth}")
    headers.append(f"X-UA-AuthorId: {post.author_id}")
    headers.append("Content-Type: text/plain; charset=utf-8")
    headers.append("")  # blank line between headers and body

    body = post.body.rstrip()
    # mbox-quote any line starting with "From " in the body.
    body = re.sub(r"^(From )", r">\1", body, flags=re.MULTILINE)

    return "\n".join(headers) + "\n" + body + "\n"


def write_mbox_chunk(out_f, posts: list[Post], root_mid: str, subject: str) -> None:
    for idx, post in enumerate(posts):
        # mbox separator. archive.py only checks ^From -?\d+\s*\n.
        out_f.write(f"From 0\n")
        out_f.write(render_message(post, posts, idx, root_mid, subject))
        out_f.write("\n")


def load_state() -> dict:
    if STATE_FILE.exists():
        with STATE_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {"done": {}}


def save_state(state: dict) -> None:
    tmp = STATE_FILE.with_suffix(".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        json.dump(state, f, indent=2)
    tmp.replace(STATE_FILE)


def filter_rows_by_month(rows: list[IndexRow], year: int, month: int) -> list[IndexRow]:
    prefix = f"{year:04d}-{month:02d}"
    return [r for r in rows if r.date_iso.startswith(prefix)]


def load_existing_mids() -> set[str]:
    """Return the set of Message-IDs in our existing archive.

    Used to skip threads we already have. We compare against thread *root*
    Message-IDs that UA.com exposes in its URL `mid=` param. If our archive
    has any message with that ID, we already have the thread (since our
    threading is keyed on Message-ID).
    """
    try:
        import archive
        msgs, _, _, _ = archive.parse_archive(use_cache=True)
        return set(msgs.keys())
    except Exception as e:
        print(f"[warn] could not load existing MIDs: {e}", flush=True)
        return set()


# Year range covering the mid-90s gap (1994–1998) and the post-snapshot
# tail (2013–2022, since our Giganews mbox was captured 2013-06-11).
# Dedup-by-MID skips threads already in our archive (overwhelmingly in
# 1998-H2 and 2013-H1). UA.com has nothing pre-1994 or post-2022.
DEFAULT_YEARS = (1994, 1995, 1996, 1997, 1998,
                 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022)


def parse_years(spec: str) -> list[int]:
    out: list[int] = []
    for tok in spec.split(","):
        tok = tok.strip()
        if not tok:
            continue
        if "-" in tok:
            a, b = tok.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(tok))
    return sorted(set(out))


def main() -> int:
    ap = argparse.ArgumentParser(description="Scrape gap-period threads from UsenetArchives.com")
    ap.add_argument("--years", default=",".join(str(y) for y in DEFAULT_YEARS),
                    help="Years to scrape, e.g. '1995,1996,1997' or '1994-1998'. "
                         "Default covers the full gap + boundary years.")
    ap.add_argument("--month", type=int,
                    help="If set, restrict to this month (only valid with single --years).")
    ap.add_argument("--limit", type=int, default=0,
                    help="Cap on threads per year (0 = no cap). Useful for probing.")
    ap.add_argument("--delay", type=float, default=CRAWL_DELAY,
                    help=f"Initial crawl delay in seconds (default {CRAWL_DELAY}).")
    ap.add_argument("--max-delay", type=float, default=60.0,
                    help="Cap on adaptive backoff delay (default 60s).")
    ap.add_argument("--abort-after-failures", type=int, default=15,
                    help="Abort if this many consecutive errors/empties occur (default 15).")
    ap.add_argument("--out", default=str(OUT_MBOX), help="Output mbox path.")
    ap.add_argument("--resume", action="store_true",
                    help="Skip threads already in state file (auto-on if state file exists).")
    ap.add_argument("--append", action="store_true",
                    help="Append to output mbox instead of overwriting.")
    ap.add_argument("--no-dedup", action="store_true",
                    help="Skip Message-ID dedup against existing archive (debug only).")
    args = ap.parse_args()

    years = parse_years(args.years)
    if args.month and len(years) != 1:
        ap.error("--month requires exactly one year in --years")

    # Auto-resume if state file exists.
    resume = args.resume or STATE_FILE.exists()
    state = load_state() if resume else {"done": {}}
    if resume:
        print(f"Resuming from {STATE_FILE.name} ({sum(1 for v in state['done'].values() if v == 'ok')} threads already done)", flush=True)

    existing_mids: set[str] = set() if args.no_dedup else load_existing_mids()
    if existing_mids:
        print(f"Loaded {len(existing_mids):,} existing Message-IDs for dedup", flush=True)

    out_path = Path(args.out)
    mode = "a" if (args.append or resume) else "w"

    total_new = 0
    total_skipped_overlap = 0
    total_skipped_state = 0

    # Adaptive backoff state.
    base_delay = args.delay
    current_delay = base_delay
    consecutive_failures = 0
    consecutive_ok_since_backoff = 0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context()
        page = ctx.new_page()

        for year in years:
            all_rows: list[IndexRow] = []
            page_n = 1
            while True:
                print(f"Index page {page_n} for year {year}...", flush=True)
                rows, has_next = fetch_index_page(page, year, page_n)
                print(f"  got {len(rows)} thread rows", flush=True)
                all_rows.extend(rows)
                if not has_next:
                    break
                page_n += 1
                time.sleep(args.delay)

            if args.month:
                target = filter_rows_by_month(all_rows, year, args.month)
                print(f"Filtered to {year}-{args.month:02d}: {len(target)} threads", flush=True)
            else:
                target = all_rows

            # Dedup: drop threads whose root MID is already in our archive.
            if existing_mids:
                before = len(target)
                target = [r for r in target if r.root_mid not in existing_mids]
                overlap = before - len(target)
                total_skipped_overlap += overlap
                print(f"Dedup: skipped {overlap} of {before} threads "
                      f"already in our archive; {len(target)} remain.", flush=True)

            if args.limit:
                target = target[: args.limit]
                print(f"Limited to first {args.limit} threads", flush=True)

            with out_path.open(mode, encoding="utf-8", newline="\n") as out_f:
                # After the first year's writes we should always append.
                mode = "a"
                for i, row in enumerate(target, 1):
                    if state["done"].get(row.mid_b64) == "ok":
                        total_skipped_state += 1
                        if i % 100 == 0:
                            print(f"[{year} {i}/{len(target)}] SKIP (cached): {row.subject[:50]}", flush=True)
                        continue
                    print(f"[{year} {i}/{len(target)}] {row.date_iso} "
                          f"{row.subject[:55]!r} ({row.post_count} posts) "
                          f"(delay={current_delay:.1f}s)", flush=True)
                    fetch_ok = False
                    try:
                        posts = fetch_thread(page, row.mid_b64)
                        if not posts:
                            print(f"  [warn] no posts parsed", flush=True)
                            state["done"][row.mid_b64] = "empty"
                            # Empty likely means UA returned an error page; count as failure.
                        else:
                            write_mbox_chunk(out_f, posts, row.root_mid, row.subject)
                            out_f.flush()
                            state["done"][row.mid_b64] = "ok"
                            total_new += 1
                            fetch_ok = True
                        save_state(state)
                    except Exception as e:
                        print(f"  [error] {e}", flush=True)
                        state["done"][row.mid_b64] = f"error: {repr(e)[:200]}"
                        save_state(state)

                    # Adaptive backoff: ramp delay up on consecutive failures,
                    # ramp back down after a stretch of successes.
                    if fetch_ok:
                        consecutive_failures = 0
                        if current_delay > base_delay:
                            consecutive_ok_since_backoff += 1
                            if consecutive_ok_since_backoff >= 5:
                                old = current_delay
                                current_delay = max(base_delay, current_delay / 2)
                                consecutive_ok_since_backoff = 0
                                print(f"  [backoff] {consecutive_ok_since_backoff}+ recoveries, "
                                      f"reducing delay {old:.1f}s -> {current_delay:.1f}s", flush=True)
                    else:
                        consecutive_failures += 1
                        consecutive_ok_since_backoff = 0
                        if consecutive_failures >= args.abort_after_failures:
                            print(f"\n[abort] {consecutive_failures} consecutive failures — "
                                  f"UA.com may be rate-limiting or down. "
                                  f"State saved; rerun to resume.", flush=True)
                            browser.close()
                            return 2
                        if consecutive_failures >= 3 and current_delay < args.max_delay:
                            old = current_delay
                            current_delay = min(args.max_delay, current_delay * 2)
                            print(f"  [backoff] {consecutive_failures} consecutive failures, "
                                  f"raising delay {old:.1f}s -> {current_delay:.1f}s", flush=True)

                    if i < len(target):
                        time.sleep(current_delay)

        browser.close()

    print(f"\n=== Done ===", flush=True)
    print(f"New threads scraped: {total_new:,}", flush=True)
    print(f"Skipped (overlap with existing archive): {total_skipped_overlap:,}", flush=True)
    print(f"Skipped (already in state file): {total_skipped_state:,}", flush=True)
    print(f"Output: {out_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
