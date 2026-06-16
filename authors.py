"""Top-author profiles for the comp.lang.cobol archive.

Aggregates by *display name* when possible (so "Pete Dashwood" posting from
three different addresses over a decade is one entry, not three) and falls
back to per-email entries when the display name is empty/ambiguous.

Emits `markdown/authors.md`.
"""
from __future__ import annotations

import hashlib
import re
from collections import Counter, defaultdict

from archive import OUT, date_key, filter_msgs, parse_archive, thread_summaries
from utils import md_escape, trim

TOP_AUTHORS = 100
TOP_THREADS_PER_AUTHOR = 10

# Synthetic email minted by scrape_gap.py for UA.com-scraped authors.
UA_EMAIL_RE = re.compile(r"^ua-author-(\d+)@usenetarchives\.gap$")

# Curated bridge: UA.com author ID -> canonical display name (issue #28).
#
# UA.com strips emails and often truncates display names ("rtw...", "docd...",
# "dashwood"), so a long-running poster splits into a UA-gap entry and a
# separate Giganews entry. merge_key() can't reunite them — the truncated name
# normalizes to a different key than the real one. This map overrides the UA
# author's canonical name so it merges into the right group.
#
# The value MUST be a name whose merge_key() equals the target Giganews group's
# key (i.e. the name that group already canonicalizes to), or the merge won't
# happen. Each entry below was confirmed against the generated authors.md:
# matching email local-parts, overlapping active spans, and topic fingerprint.
UA_AUTHOR_NAMES = {
    # Pete Dashwood — dashwood@enternet.co.nz; the 2013-2022 COBOL-advocacy tail
    # (#27 "dashwood") split across four UA IDs.
    "14501808": "Pete Dashwood",
    "2154790": "Pete Dashwood",
    "6590328": "Pete Dashwood",
    "14256666": "Pete Dashwood",
    # docdwarf — docdwarf@erols.com; "docd..." (#55), 1996-1998, merges into #45.
    "514273": "docdwarf",
    # Bob Wolfe — rtwolfe@flexus.com; "rtw..." (#83), per issue #28, merges into #31.
    "6550399": "Bob Wolfe",
    # Randall Bart — "randallbart" (#80), 1997-1998, merges into #57 "Randall Bart".
    "464041": "Randall Bart",
    # William "Bill" Lynch — wblynch@att.net; "bill lynch" (#64), merges into #30.
    "92065": "William Lynch",
    # Richard Plinston — riplin@azonic.co.nz; "rip..." (#97), merges into #5 "Richard".
    "6589535": "Richard",
}


def bridge_name(email: str, fallback: str) -> str:
    """Map a synthetic UA.com author email to its curated canonical name.

    Returns ``fallback`` unchanged for non-UA emails and for UA author IDs
    that aren't in the bridge map. See ``UA_AUTHOR_NAMES`` and issue #28.
    """
    m = UA_EMAIL_RE.match(email)
    if m:
        return UA_AUTHOR_NAMES.get(m.group(1), fallback)
    return fallback


def best_display_name(name_counts: Counter) -> str:
    for name, _ in name_counts.most_common():
        if name and not name.startswith("<"):
            return name
    return ""


def merge_key(name: str) -> str:
    """Canonical key for matching the same author across multiple emails.

    Returns "" if the name is too short/empty to be a reliable identifier.
    """
    if not name:
        return ""
    n = re.sub(r"[^\w\s]", "", name.lower())
    n = re.sub(r"\s+", " ", n).strip()
    # Drop very short names; high false-merge risk
    if len(n) < 5:
        return ""
    return n


def slug(s: str) -> str:
    h = hashlib.md5(s.encode("utf-8")).hexdigest()[:10]
    return f"a-{h}"


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)
    summary_by_root = {s["root"]: s for s in summaries}
    msgs = filter_msgs(msgs, summaries)

    # Per-email display name distribution → pick canonical per email
    email_names: dict[str, Counter] = defaultdict(Counter)
    for entry in msgs.values():
        email = entry["email"]
        if not email:
            continue
        email_names[email][entry["display_name"]] += 1
    email_to_canonical: dict[str, str] = {
        e: bridge_name(e, best_display_name(c)) for e, c in email_names.items()
    }

    # Group emails by merge_key of canonical name. Emails with unmergeable
    # names go in their own group keyed by email.
    groups: dict[str, list[str]] = defaultdict(list)
    for email, name in email_to_canonical.items():
        key = merge_key(name) or f"__email__{email}"
        groups[key].append(email)

    # Aggregate stats per group
    group_msgs: dict[str, int] = defaultdict(int)
    group_threads: dict[str, set] = defaultdict(set)
    group_started: dict[str, set] = defaultdict(set)
    group_first: dict[str, tuple] = {}
    group_last: dict[str, tuple] = {}
    group_emails: dict[str, set] = defaultdict(set)
    group_name_counts: dict[str, Counter] = defaultdict(Counter)

    # Reverse lookup: email -> group_key
    email_to_group: dict[str, str] = {}
    for key, emails in groups.items():
        for e in emails:
            email_to_group[e] = key
        group_emails[key].update(emails)

    for mid, entry in msgs.items():
        email = entry["email"]
        if not email:
            continue
        gk = email_to_group[email]
        group_msgs[gk] += 1
        root = root_cache[mid]
        group_threads[gk].add(root)
        group_name_counts[gk][entry["display_name"]] += 1
        if root in msgs and msgs[root]["email"] == email and msgs[root]["id"] == root:
            group_started[gk].add(root)
        dt = entry["dt"]
        if dt is not None:
            sk = date_key(dt)
            if gk not in group_first or sk < group_first[gk][0]:
                group_first[gk] = (sk, entry["ym"])
            if gk not in group_last or sk > group_last[gk][0]:
                group_last[gk] = (sk, entry["ym"])

    # Per-group, per-thread message counts (for "top threads")
    group_thread_msgs: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    group_email_msgs: dict[str, Counter] = defaultdict(Counter)
    for mid, entry in msgs.items():
        email = entry["email"]
        if not email:
            continue
        gk = email_to_group[email]
        group_thread_msgs[gk][root_cache[mid]] += 1
        group_email_msgs[gk][email] += 1

    # Rank groups by message count
    ranked = sorted(group_msgs.items(), key=lambda kv: -kv[1])
    top = ranked[:TOP_AUTHORS]

    print(f"Writing top {len(top)} authors (after display-name merging)...")
    out = OUT / "authors.md"
    with out.open("w", encoding="utf-8") as f:
        f.write("[← README](README.md) · [Topics](topics.md) · [Years](years.md) · [Stats](stats.md) · [Subjects](subjects.md) · [Links](links.md)\n\n")
        f.write("# comp.lang.cobol — Top Authors\n\n")
        f.write(
            f"The {len(top)} most prolific posters by message count. "
            "Aggregated by display name across email addresses where possible "
            "(so the same person posting from multiple accounts merges into one entry). "
            "Bot/recruiter accounts will still appear — heavy raw count doesn't imply signal.\n\n"
        )

        # Quick reference
        f.write("## Quick reference\n\n")
        f.write(
            "| # | Author | Msgs | Threads | Started | Aliases | Active |\n"
            "|---:|---|---:|---:|---:|---:|---|\n"
        )
        for rank, (gk, _msg_count) in enumerate(top, 1):
            name = best_display_name(group_name_counts[gk]) or "—"
            tcount = len(group_threads[gk])
            scount = len(group_started[gk])
            aliases = len(group_emails[gk])
            first_ym = group_first.get(gk, (None, "?"))[1]
            last_ym = group_last.get(gk, (None, "?"))[1]
            span = first_ym if first_ym == last_ym else f"{first_ym} → {last_ym}"
            anchor = slug(gk)
            f.write(
                f"| {rank} | [{md_escape(trim(name, 40))}](#{anchor}) | "
                f"{_msg_count:,} | {tcount:,} | {scount:,} | {aliases} | {span} |\n"
            )
        f.write("\n")

        # Per-author detail
        for rank, (gk, msg_count) in enumerate(top, 1):
            name = best_display_name(group_name_counts[gk]) or gk
            tcount = len(group_threads[gk])
            scount = len(group_started[gk])
            first_ym = group_first.get(gk, (None, "?"))[1]
            last_ym = group_last.get(gk, (None, "?"))[1]
            span = first_ym if first_ym == last_ym else f"{first_ym} → {last_ym}"
            anchor = slug(gk)

            f.write(f"## #{rank}. {md_escape(name)} <a id='{anchor}'></a>\n\n")

            # Aliases (sorted by message count under each email)
            alias_list = ", ".join(
                f"`{md_escape(e)}` ({c:,})"
                for e, c in group_email_msgs[gk].most_common()
            )
            f.write(f"{alias_list}\n\n")

            f.write(
                f"**{msg_count:,} messages** in **{tcount:,} threads** "
                f"({scount:,} started) · active **{span}**\n\n"
            )

            # Other display names this person used
            other_names = [
                n for n, _ in group_name_counts[gk].most_common(5)
                if n and n != name
            ]
            if other_names:
                trimmed = ", ".join(md_escape(trim(n, 50)) for n in other_names[:3])
                f.write(f"_Also posted as: {trimmed}._\n\n")

            top_thread_roots = sorted(
                group_thread_msgs[gk].items(),
                key=lambda kv: -kv[1],
            )[:TOP_THREADS_PER_AUTHOR]
            if top_thread_roots:
                f.write("**Top threads:**\n\n")
                for root, n in top_thread_roots:
                    s = summary_by_root.get(root)
                    if not s:
                        continue
                    label = trim(s["subject"])
                    link = f"[{md_escape(label)}](threads/{s['anchor']}.md)"
                    started_marker = " · _started_" if root in group_started[gk] else ""
                    f.write(f"- {link} — **{n}** of {s['count']} msgs{started_marker}\n")
                f.write("\n")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
