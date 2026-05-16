"""Statistical overview of the comp.lang.cobol archive.

Emits `markdown/stats.md` — totals, activity timeline (ASCII bar chart), top
authors, top threads, top months, thread-size distribution.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from datetime import datetime

from archive import OUT, date_key, parse_archive, thread_summaries

# Terms whose first appearance in the archive is interesting to surface.
# Order roughly chronological by expected first-mention to make the table read well.
TIMELINE_TERMS = [
    "COBOL 85", "ANSI 85", "Y2K", "year 2000", "millennium bug",
    "Visual Basic", "Delphi", "OS/2", "Windows 95", "Windows 98", "Windows NT",
    "Linux", "Solaris", "AIX", "HP-UX",
    "Micro Focus", "Fujitsu", "Acucobol", "RM/COBOL",
    "AS/400", "iSeries", "z/OS", "OS/390",
    "Java", "Perl", "Python", "Ruby on Rails", "PHP",
    "Servlet", "Tomcat", "Apache",
    "object-oriented", "OO COBOL", "COBOL 2002",
    "XML", "SOAP", "JSON", "web service",
    ".NET", "C#",
    "NetBeans",
    "OpenCOBOL", "TinyCOBOL", "GnuCOBOL",
    "Wikipedia", "GitHub", "Facebook",
    "iPad",
    "Hadoop", "MapReduce",
    "Y2K38", "COBOL 2014",
]

BAR_WIDTH = 50
# 9 levels of fill (0/8 through 8/8) for sub-cell bar resolution
BLOCKS = " ▏▎▍▌▋▊▉█"


def bar(value: int, max_value: int, width: int = BAR_WIDTH) -> str:
    if max_value <= 0 or value <= 0:
        return ""
    units = value / max_value * width
    full = int(units)
    frac_idx = int((units - full) * (len(BLOCKS) - 1))
    return "█" * full + (BLOCKS[frac_idx] if frac_idx > 0 else "")


def md_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`")


def trim(text: str, n: int = 80) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def best_display_name(name_counts: Counter) -> str:
    """Pick the most common non-empty display name for an author."""
    for name, _ in name_counts.most_common():
        if name and not name.startswith("<"):
            return name
    return ""


def first_mention_timeline(msgs, terms):
    """For each term, find the earliest message that mentions it (subject or body).

    Uses non-word lookaround so "Eclipse" doesn't match "eclipsed" and ".NET"
    doesn't match ".NETwork".
    """
    name_to_term = {}
    parts = []
    for i, t in enumerate(terms):
        name = f"T{i}"
        name_to_term[name] = t
        parts.append(f"(?P<{name}>(?<![\\w]){re.escape(t)}(?![\\w]))")
    pattern = re.compile("|".join(parts), re.IGNORECASE)

    first: dict[str, dict] = {}
    chronological = sorted(
        (m for m in msgs.values() if m["dt"] is not None),
        key=lambda m: date_key(m["dt"]),
    )
    for entry in chronological:
        if len(first) == len(terms):
            break
        haystack = (entry.get("subject") or "") + "\n" + (entry.get("body") or "")
        for m in pattern.finditer(haystack):
            for name, val in m.groupdict().items():
                if val and name_to_term[name] not in first:
                    first[name_to_term[name]] = entry
    return first


def write_stats(msgs, summaries, path):
    total_msgs = len(msgs)
    total_threads = len(summaries)

    by_year = Counter()
    by_ym = Counter()
    by_dow = Counter()
    by_hour = Counter()
    undated = 0
    for entry in msgs.values():
        dt = entry["dt"]
        if dt is None:
            undated += 1
            continue
        by_year[dt.year] += 1
        by_ym[entry["ym"]] += 1
        by_dow[dt.weekday()] += 1
        by_hour[dt.hour] += 1

    dated = [m["dt"] for m in msgs.values() if m["dt"]]
    if dated:
        first_dt = min(dated, key=date_key)
        last_dt = max(dated, key=date_key)
    else:
        first_dt = last_dt = None

    # Author aggregation by lowercased email; pick the most common display name
    by_email_msgs: dict[str, int] = Counter()
    by_email_names: dict[str, Counter] = defaultdict(Counter)
    by_email_threads: dict[str, set] = defaultdict(set)
    for entry in msgs.values():
        email = entry["email"] or "(no email)"
        by_email_msgs[email] += 1
        by_email_names[email][entry["display_name"]] += 1
    # Threads per author
    msg_to_root = {mid: s["root"] for s in summaries for mid in s["msg_ids"]}
    for mid, entry in msgs.items():
        email = entry["email"] or "(no email)"
        by_email_threads[email].add(msg_to_root[mid])

    # Thread metrics
    thread_sizes = sorted((s["count"] for s in summaries), reverse=True)
    singleton_threads = sum(1 for c in thread_sizes if c == 1)
    median_size = thread_sizes[len(thread_sizes) // 2] if thread_sizes else 0
    max_size = thread_sizes[0] if thread_sizes else 0
    p95 = thread_sizes[int(len(thread_sizes) * 0.05)] if thread_sizes else 0
    p99 = thread_sizes[int(len(thread_sizes) * 0.01)] if thread_sizes else 0

    with path.open("w", encoding="utf-8") as f:
        f.write("[← README](README.md) · [Topics](topics.md) · [Years](years.md) · [Authors](authors.md) · [Subjects](subjects.md) · [Links](links.md)\n\n")
        f.write("# comp.lang.cobol — Statistics\n\n")

        # Header
        if first_dt and last_dt:
            f.write(
                f"**{total_msgs:,} messages** in **{total_threads:,} threads** from "
                f"**{first_dt.date()}** to **{last_dt.date()}** "
                f"({len(by_ym):,} active months).\n\n"
            )
        else:
            f.write(f"**{total_msgs:,} messages** in **{total_threads:,} threads**.\n\n")

        unique_authors = len([e for e in by_email_msgs if e != "(no email)"])
        f.write(
            f"**{unique_authors:,} unique email senders** "
            f"({by_email_msgs.get('(no email)', 0):,} messages had no parseable email).\n\n"
        )

        # Activity by year
        f.write("## Messages per year\n\n")
        f.write("```\n")
        max_y = max(by_year.values(), default=1)
        for year in sorted(by_year):
            count = by_year[year]
            f.write(f"{year}  {bar(count, max_y):<{BAR_WIDTH}}  {count:>6,}\n")
        f.write("```\n\n")

        # Activity by month
        f.write("## Messages per month\n\n")
        f.write("```\n")
        max_m = max(by_ym.values(), default=1)
        for ym in sorted(by_ym):
            count = by_ym[ym]
            f.write(f"{ym}  {bar(count, max_m):<{BAR_WIDTH}}  {count:>5,}\n")
        f.write("```\n\n")

        # Day of week
        f.write("## Posting by day of week\n\n")
        f.write("```\n")
        dows = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        max_d = max(by_dow.values(), default=1)
        for i, name in enumerate(dows):
            count = by_dow.get(i, 0)
            f.write(f"{name}  {bar(count, max_d, 40):<40}  {count:>6,}\n")
        f.write("```\n\n")

        # Hour of day (UTC after normalization)
        f.write("## Posting by hour\n\n")
        f.write("```\n")
        max_h = max(by_hour.values(), default=1)
        for h in range(24):
            count = by_hour.get(h, 0)
            f.write(f"{h:02d}:00  {bar(count, max_h, 40):<40}  {count:>6,}\n")
        f.write("```\n\n")

        # Top months
        f.write("## Busiest 25 months\n\n")
        f.write("| Month | Messages |\n|---|---:|\n")
        for ym, count in by_ym.most_common(25):
            f.write(f"| [{ym}]({ym}.md) | {count:,} |\n")
        f.write("\n")

        # Thread size distribution
        f.write("## Thread size distribution\n\n")
        f.write(
            f"- **Largest thread:** {max_size:,} messages\n"
            f"- **Top 1% threshold (p99):** {p99:,} messages\n"
            f"- **Top 5% threshold (p95):** {p95:,} messages\n"
            f"- **Median thread size:** {median_size:,} messages\n"
            f"- **Single-message threads:** {singleton_threads:,} "
            f"({singleton_threads / total_threads:.0%} of all threads)\n\n"
        )

        # Top threads by message count
        f.write("## Top 30 longest threads ever\n\n")
        top_threads = sorted(summaries, key=lambda s: -s["count"])[:30]
        f.write("| Thread | Messages | Participants | Span |\n|---|---:|---:|---|\n")
        for s in top_threads:
            label = trim(s["subject"])
            span = (
                f"{s['months'][0]} → {s['months'][-1]}"
                if s["months"] and s["months"][0] != s["months"][-1]
                else (s["months"][0] if s["months"] else "undated")
            )
            ym = s["first_ym"] if s["first_ym"] != "undated" else None
            link = f"[{md_escape(label)}]({ym}.md#{s['anchor']})" if ym else md_escape(label)
            f.write(f"| {link} | {s['count']:,} | {len(s['participants'])} | {span} |\n")
        f.write("\n")

        # Most participatory threads
        f.write("## Top 30 threads by participant count\n\n")
        f.write("(Threads with the most distinct email senders.)\n\n")
        top_part = sorted(summaries, key=lambda s: -len(s["participants"]))[:30]
        f.write("| Thread | Participants | Messages | Span |\n|---|---:|---:|---|\n")
        for s in top_part:
            label = trim(s["subject"])
            span = (
                f"{s['months'][0]} → {s['months'][-1]}"
                if s["months"] and s["months"][0] != s["months"][-1]
                else (s["months"][0] if s["months"] else "undated")
            )
            ym = s["first_ym"] if s["first_ym"] != "undated" else None
            link = f"[{md_escape(label)}]({ym}.md#{s['anchor']})" if ym else md_escape(label)
            f.write(f"| {link} | {len(s['participants'])} | {s['count']:,} | {span} |\n")
        f.write("\n")

        # Top authors by message count
        f.write("## Top 50 authors by message count\n\n")
        f.write("| Author | Email | Messages | Threads |\n|---|---|---:|---:|\n")
        for email, count in by_email_msgs.most_common(50):
            if email == "(no email)":
                continue
            name = best_display_name(by_email_names[email]) or "—"
            tcount = len(by_email_threads[email])
            f.write(
                f"| {md_escape(name)} | `{md_escape(email)}` | {count:,} | {tcount:,} |\n"
            )
        f.write("\n")

        # Evergreen threads — widest span between first and last activity
        f.write("## Top 20 evergreen threads (longest active span)\n\n")
        f.write(
            "Threads whose conversation kept going (or kept getting revived) over the widest stretch of time.\n\n"
        )
        def span_months(s):
            if not s["months"] or len(s["months"]) < 2:
                return 0
            a = s["months"][0]
            b = s["months"][-1]
            return (int(b[:4]) - int(a[:4])) * 12 + (int(b[5:7]) - int(a[5:7]))
        evergreen = sorted(summaries, key=lambda s: (-span_months(s), -s["count"]))[:20]
        f.write("| Thread | Span | Months | Messages |\n|---|---:|---:|---:|\n")
        for s in evergreen:
            sm = span_months(s)
            if sm < 1:
                continue
            label = trim(s["subject"])
            ym = s["first_ym"]
            link = f"[{md_escape(label)}]({ym}.md#{s['anchor']})" if ym != "undated" else md_escape(label)
            f.write(
                f"| {link} | {sm} mo | {s['months'][0]} → {s['months'][-1]} | {s['count']:,} |\n"
            )
        f.write("\n")

        # Hottest threads — most messages in any single calendar day
        f.write("## Top 20 hottest threads (peak day velocity)\n\n")
        f.write(
            "Threads with the most messages posted on a single calendar day — proxy for "
            "conversations that went viral within the group.\n\n"
        )
        peak_per_thread: dict = {}
        for s in summaries:
            day_counts: Counter = Counter()
            for mid in s["msg_ids"]:
                dt = msgs[mid]["dt"]
                if dt is None:
                    continue
                day_counts[dt.date().isoformat()] += 1
            if day_counts:
                peak_day, peak_count = day_counts.most_common(1)[0]
                peak_per_thread[s["root"]] = (peak_day, peak_count, s)
        hottest = sorted(peak_per_thread.values(), key=lambda x: -x[1])[:20]
        f.write("| Thread | Peak day | Peak msgs | Total | Span |\n|---|---|---:|---:|---|\n")
        for peak_day, peak_count, s in hottest:
            label = trim(s["subject"])
            ym = s["first_ym"]
            link = f"[{md_escape(label)}]({ym}.md#{s['anchor']})" if ym != "undated" else md_escape(label)
            span = (
                f"{s['months'][0]} → {s['months'][-1]}"
                if s["months"] and s["months"][0] != s["months"][-1]
                else (s["months"][0] if s["months"] else "—")
            )
            f.write(f"| {link} | {peak_day} | {peak_count} | {s['count']:,} | {span} |\n")
        f.write("\n")

        # First-mention timeline
        f.write("## First mentions of key terms\n\n")
        f.write(
            "Earliest message in the archive (subject or body) containing each term. "
            "Useful for spotting when new technologies first cracked the conversation.\n\n"
        )
        first_mentions = first_mention_timeline(msgs, TIMELINE_TERMS)
        rows = []
        for term, entry in first_mentions.items():
            rows.append((entry["dt"], term, entry))
        rows.sort(key=lambda r: date_key(r[0]))
        f.write("| Term | First mention | Thread |\n|---|---|---|\n")
        for dt, term, entry in rows:
            ym = entry["ym"]
            subj = entry.get("subject") or "(no subject)"
            if len(subj) > 70:
                subj = subj[:69].rstrip() + "…"
            link = f"[{md_escape(subj)}]({ym}.md)" if ym != "undated" else md_escape(subj)
            f.write(f"| **{md_escape(term)}** | {dt.date()} | {link} |\n")
        f.write("\n")

        if undated:
            f.write(f"\n_{undated:,} messages had unparseable dates and are omitted from time-based charts._\n")


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)
    out = OUT / "stats.md"
    print(f"Writing {out}...")
    write_stats(msgs, summaries, out)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
