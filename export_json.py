"""Export archive data to static JSON files for the web frontend.

Run once (or after rebuilding the archive) to populate web/data/.
The Node.js server then serves these files statically.

Usage:
    # Normal (script and data in same directory):
    python export_json.py

    # Git worktree: data files live in main project, output goes to worktree:
    python export_json.py --data-dir "C:\\path\\to\\main\\project"
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_DIR))

import archive as _archive_mod
from archive import clean_body, date_key, parse_archive, thread_anchor, thread_summaries
from authors import best_display_name, bridge_name, merge_key
from topics import TOPIC_RULES, categorize
from utils import dfs_order

# email -> group id, populated in main() before any card() is built so that
# thread/message author links resolve to the merged-person author page rather
# than to one of the person's many raw emails. Populated by the author-index
# grouping in main(). See issue #28.
_EMAIL_TO_GID: dict[str, str] = {}

OUT = PROJECT_DIR / "web" / "data"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def mkdirs():
    OUT.mkdir(parents=True, exist_ok=True)
    # Wipe per-item subdirs so a re-export with a changed thread/author set
    # doesn't leave orphaned files behind (e.g. anchors that no longer exist).
    for sub in ("threads", "year", "topic", "author"):
        d = OUT / sub
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)


def dump(path: Path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))


def span(s: dict) -> str:
    months = s.get("months", [])
    if not months:
        return "undated"
    return months[0] if months[0] == months[-1] else f"{months[0]} → {months[-1]}"


def author_id(group_key: str) -> str:
    """Stable filesystem-safe ID for an author *group* (MD5 of its merge key).

    The group key is a person's canonical merge_key() (shared across all their
    emails), or ``__email__<addr>`` for emails with no reliable display name.
    """
    return hashlib.md5(group_key.encode()).hexdigest()


def card(s: dict, msgs: dict) -> dict:
    """Compact thread summary for list views."""
    root = s["root"]
    entry = msgs.get(root)
    sender = ""
    email = ""
    if entry:
        sender = entry.get("display_name") or entry.get("email", "")
        email = entry.get("email", "")
    return {
        "a": s["anchor"],
        "s": s["subject"],
        "c": s["count"],
        "p": len(s["participants"]),
        "f": s.get("first_ym", ""),
        "l": s.get("last_ym", ""),
        "sp": span(s),
        "t": s["topics"],
        "by": sender,
        "em": _EMAIL_TO_GID.get(email, ""),
    }



# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Export archive to JSON for the web frontend.")
    parser.add_argument(
        "--data-dir",
        metavar="DIR",
        default=None,
        help="Directory containing comp.lang.cobol.mbox and the pickle cache "
             "(defaults to the same directory as this script).",
    )
    args = parser.parse_args()

    data_dir = Path(args.data_dir).resolve() if args.data_dir else PROJECT_DIR

    # Monkey-patch archive module paths before calling parse_archive() so it
    # finds the mbox and cache in data_dir when running from a git worktree.
    _archive_mod.SRC = data_dir / "comp.lang.cobol.mbox"
    _archive_mod.EXTRA_SRCS = [data_dir / "comp.lang.cobol.gap.mbox"]
    _archive_mod.CACHE = data_dir / ".archive_cache.pickle"

    print("Loading archive...")
    msgs, children, root_cache, depth = parse_archive()
    print(f"  {len(msgs):,} messages loaded")

    summaries = thread_summaries(msgs, root_cache)
    print(f"  {len(summaries):,} threads after spam filter")

    for s in summaries:
        s["topics"] = categorize(s["subject"])

    mkdirs()

    # Pre-sort
    by_hot = sorted(summaries, key=lambda s: -s["count"])
    by_new = sorted(
        summaries,
        key=lambda s: (date_key(s.get("first_dt")), 0),
        reverse=True,
    )

    # Year index
    by_year: dict[str, list] = defaultdict(list)
    for s in summaries:
        ym = s.get("first_ym", "")
        if ym and ym != "undated" and len(ym) >= 4:
            by_year[ym[:4]].append(s)

    years_data = sorted(
        [
            {"year": y, "threads": len(ss), "messages": sum(x["count"] for x in ss)}
            for y, ss in by_year.items()
        ],
        key=lambda x: x["year"],
    )

    # Topic index
    by_topic: dict[str, list] = defaultdict(list)
    for s in summaries:
        for _name, slug in s["topics"]:
            by_topic[slug].append(s)

    topics_data = [
        {
            "name": name,
            "slug": slug,
            "threads": len(by_topic.get(slug, [])),
            "messages": sum(t["count"] for t in by_topic.get(slug, [])),
        }
        for name, slug, _ in TOPIC_RULES
    ]

    # Author index — aggregated per *person*, not per raw email. The same
    # display-name merge + UA.com bridge that authors.py uses (issue #28), so
    # the website matches markdown/authors.md instead of splitting a poster
    # across every address they ever used.
    print("Building author index...")
    root_anchor_map = {s["root"]: s["anchor"] for s in summaries}
    anchor_set = {s["anchor"] for s in summaries}

    # Per-email canonical display name (UA-bridged), then group emails by person.
    email_names: dict[str, Counter] = defaultdict(Counter)
    for entry in msgs.values():
        email = entry.get("email", "")
        if not email:
            continue
        email_names[email][entry.get("display_name", "")] += 1
    email_to_canonical = {
        e: bridge_name(e, best_display_name(c)) for e, c in email_names.items()
    }
    groups: dict[str, list[str]] = defaultdict(list)
    for email, name in email_to_canonical.items():
        groups[merge_key(name) or f"__email__{email}"].append(email)
    email_to_group = {e: gk for gk, emails in groups.items() for e in emails}
    # Publish the email -> group-id map that card() reads for author links.
    _EMAIL_TO_GID.update({e: author_id(gk) for e, gk in email_to_group.items()})

    author_threads: dict[str, set] = defaultdict(set)
    author_msg_count: dict[str, int] = defaultdict(int)
    group_name_counts: dict[str, Counter] = defaultdict(Counter)
    group_email_counts: dict[str, Counter] = defaultdict(Counter)
    for mid, entry in msgs.items():
        email = entry.get("email", "")
        if not email:
            continue
        gk = email_to_group[email]
        root = root_cache.get(mid)
        if root:
            anc = root_anchor_map.get(root)
            if anc and anc in anchor_set:
                author_threads[gk].add(anc)
        author_msg_count[gk] += 1
        group_name_counts[gk][entry.get("display_name", "")] += 1
        group_email_counts[gk][email] += 1

    # Display name and primary email (most-used) per group.
    author_name = {
        gk: best_display_name(c) or group_email_counts[gk].most_common(1)[0][0]
        for gk, c in group_name_counts.items()
    }
    author_email = {
        gk: group_email_counts[gk].most_common(1)[0][0] for gk in author_msg_count
    }

    top_authors = sorted(author_msg_count, key=lambda gk: -author_msg_count[gk])
    anchor_map = {s["anchor"]: s for s in summaries}

    # ---- index.json ----
    print("Writing index.json...")
    dump(OUT / "index.json", {
        "messages": sum(s["count"] for s in summaries),
        "threads": len(summaries),
        "authors": len(top_authors),
        "date_start": years_data[0]["year"] if years_data else "",
        "date_end": years_data[-1]["year"] if years_data else "",
        "years": years_data,
        "topics": topics_data,
    })

    # ---- hot.json / new.json ----
    print("Writing hot.json...")
    dump(OUT / "hot.json", [card(s, msgs) for s in by_hot])
    print("Writing new.json...")
    dump(OUT / "new.json", [card(s, msgs) for s in by_new])

    # ---- years.json / topics.json ----
    dump(OUT / "years.json", years_data)
    dump(OUT / "topics.json", topics_data)

    # ---- per-year ----
    print(f"Writing {len(by_year)} year files...")
    for year, ss in by_year.items():
        ss_sorted = sorted(ss, key=lambda s: -s["count"])
        dump(OUT / "year" / f"{year}.json", [card(s, msgs) for s in ss_sorted])

    # ---- per-topic ----
    print(f"Writing {len(TOPIC_RULES)} topic files...")
    for name, slug, _ in TOPIC_RULES:
        ts = sorted(by_topic.get(slug, []), key=lambda s: -s["count"])
        dump(OUT / "topic" / f"{slug}.json", [card(s, msgs) for s in ts])

    # ---- authors.json ----
    print("Writing authors.json...")
    dump(OUT / "authors.json", [
        {
            "id": author_id(gk),
            "email": author_email[gk],
            "name": author_name.get(gk, author_email[gk]),
            "messages": author_msg_count[gk],
            "threads": len(author_threads[gk]),
        }
        for gk in top_authors[:1000]
    ])

    # ---- per-author JSON (top 500) ----
    print("Writing per-author files (top 500)...")
    for gk in top_authors[:500]:
        anchors = list(author_threads[gk])
        author_sums = sorted(
            [anchor_map[a] for a in anchors if a in anchor_map],
            key=lambda s: -s["count"],
        )
        dump(OUT / "author" / f"{author_id(gk)}.json", {
            "id": author_id(gk),
            "email": author_email[gk],
            "name": author_name.get(gk, author_email[gk]),
            "messages": author_msg_count[gk],
            "thread_count": len(author_sums),
            "threads": [card(s, msgs) for s in author_sums[:100]],
        })

    # ---- per-thread JSON ----
    n = len(summaries)
    print(f"Writing {n:,} thread JSON files...")
    t0 = time.perf_counter()

    for i, s in enumerate(summaries, 1):
        if i % 5000 == 0:
            elapsed = time.perf_counter() - t0
            print(f"  {i:,} / {n:,}  ({elapsed:.0f}s elapsed)")

        in_thread = set(s["msg_ids"])
        root = s["root"]
        if root in msgs:
            order = dfs_order(root, children, in_thread)
        else:
            order = sorted(in_thread, key=lambda x: date_key(msgs[x]["dt"]))

        messages = []
        for mid in order:
            entry = msgs.get(mid)
            if not entry:
                continue
            messages.append({
                "id": mid,
                "s": entry.get("subject", ""),
                "by": entry.get("display_name") or entry.get("email", ""),
                "em": _EMAIL_TO_GID.get(entry.get("email", ""), ""),
                "d": entry.get("date_iso", ""),
                "ym": entry.get("ym", ""),
                "body": clean_body(entry.get("body", "")),
                "dep": depth.get(mid, 0),
                "par": entry.get("parent", ""),
            })

        months = s.get("months", [])
        sp = (
            months[0]
            if (months and months[0] == months[-1])
            else (f"{months[0]} → {months[-1]}" if months else "undated")
        )
        dump(OUT / "threads" / f"{s['anchor']}.json", {
            "anchor": s["anchor"],
            "subject": s["subject"],
            "count": s["count"],
            "participants": len(s["participants"]),
            "span": sp,
            "topics": s["topics"],
            "messages": messages,
        })

    elapsed = time.perf_counter() - t0
    print(f"\nDone! {n:,} thread files written in {elapsed:.0f}s.")
    print(f"Data directory: {OUT}")
    print("\nNext: node server.js")


if __name__ == "__main__":
    main()
