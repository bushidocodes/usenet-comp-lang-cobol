"""Per-year index of the comp.lang.cobol archive.

For each year, shows: total messages/threads, monthly drill-down, top threads,
and dominant topics. Emits `markdown/years.md`.
"""
from __future__ import annotations

from collections import Counter, defaultdict

from archive import OUT, date_key, parse_archive, thread_summaries
from topics import TOPIC_RULES, categorize

TOP_THREADS_PER_YEAR = 15


def md_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`")


def trim(text: str, n: int = 90) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def thread_link(s):
    ym = s["first_ym"]
    if ym == "undated":
        return md_escape(trim(s["subject"]))
    return f"[{md_escape(trim(s['subject']))}]({ym}.md#{s['anchor']})"


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)

    # Group threads by year. A thread is "in" a year if its first message is in that year.
    by_year_threads: dict[int, list] = defaultdict(list)
    for s in summaries:
        if s["first_dt"]:
            by_year_threads[s["first_dt"].year].append(s)

    # Per-year thread starters: who initiated the most conversations that year.
    starters_per_year: dict[int, Counter] = defaultdict(Counter)
    starter_names: dict[str, str] = {}
    for s in summaries:
        root = s["root"]
        if root not in msgs or not s["first_dt"]:
            continue
        starter = msgs[root]["email"]
        if not starter:
            continue
        starters_per_year[s["first_dt"].year][starter] += 1
        if msgs[root]["display_name"]:
            starter_names[starter] = msgs[root]["display_name"]

    # Threads that continued into the next year (carryovers / lasting conversations).
    carryover_per_year: dict[int, list] = defaultdict(list)
    for s in summaries:
        if not s["first_dt"]:
            continue
        y = s["first_dt"].year
        if s["months"] and s["months"][-1][:4] != str(y):
            carryover_per_year[y].append(s)

    # Messages per year and per month
    msgs_per_year: Counter = Counter()
    msgs_per_ym: dict[str, int] = Counter()
    months_per_year: dict[int, set] = defaultdict(set)
    for entry in msgs.values():
        if entry["dt"]:
            y = entry["dt"].year
            msgs_per_year[y] += 1
            msgs_per_ym[entry["ym"]] += 1
            months_per_year[y].add(entry["ym"])

    years = sorted(by_year_threads)
    out = OUT / "years.md"
    print(f"Writing {out}...")

    with out.open("w", encoding="utf-8") as f:
        f.write("[← README](README.md) · [Topics](topics.md) · [Authors](authors.md) · [Subjects](subjects.md) · [Links](links.md) · [Stats](stats.md)\n\n")
        f.write("# comp.lang.cobol — Yearly Index\n\n")
        f.write(
            "Each year links to its monthly files and lists the top conversations and "
            "dominant topics of that year.\n\n"
        )

        f.write("## Years\n\n")
        f.write("| Year | Messages | Threads | Months |\n|---|---:|---:|---:|\n")
        for y in years:
            f.write(
                f"| [{y}](#y{y}) | {msgs_per_year[y]:,} | "
                f"{len(by_year_threads[y]):,} | {len(months_per_year[y])} |\n"
            )
        f.write("\n")

        for y in years:
            threads = by_year_threads[y]
            months = sorted(months_per_year[y])
            total_msgs = msgs_per_year[y]
            total_threads = len(threads)

            f.write(f"## {y} <a id='y{y}'></a>\n\n")
            f.write(
                f"**{total_msgs:,} messages in {total_threads:,} threads** · "
                f"active {months[0]} → {months[-1]}\n\n"
            )

            # Monthly drill-down
            f.write("### Months\n\n")
            for ym in months:
                count = msgs_per_ym[ym]
                f.write(f"- [{ym}]({ym}.md) — {count:,} msgs\n")
            f.write("\n")

            # Top threads
            f.write(f"### Top {min(TOP_THREADS_PER_YEAR, total_threads)} threads\n\n")
            top = sorted(threads, key=lambda s: -s["count"])[:TOP_THREADS_PER_YEAR]
            for s in top:
                span_extra = ""
                if s["months"] and s["months"][-1][:4] != str(y):
                    span_extra = f" (continues into {s['months'][-1][:4]})"
                f.write(f"- {thread_link(s)} — **{s['count']}** msgs{span_extra}\n")
            f.write("\n")

            # Topic breakdown
            topic_counter: Counter = Counter()
            for s in threads:
                for name, _slug in categorize(s["subject"]):
                    topic_counter[name] += 1
            if topic_counter:
                f.write("### Dominant topics\n\n")
                for name, cnt in topic_counter.most_common(10):
                    f.write(f"- {name} — {cnt:,} threads\n")
                f.write("\n")

            # Top thread starters
            top_starters = starters_per_year[y].most_common(10)
            if top_starters:
                f.write("### Most active thread starters\n\n")
                f.write("(People who started the most distinct conversations this year.)\n\n")
                for email, count in top_starters:
                    name = starter_names.get(email, "")
                    label = f"{name} `{email}`" if name else f"`{email}`"
                    f.write(f"- {md_escape(label)} — **{count}** new threads\n")
                f.write("\n")

            # Carryovers — threads continuing into the next year
            cos = sorted(carryover_per_year[y], key=lambda s: -s["count"])[:8]
            if cos:
                f.write("### Threads that escaped the year\n\n")
                f.write("(Started this year, but conversation continued into the next.)\n\n")
                for s in cos:
                    f.write(
                        f"- {thread_link(s)} — **{s['count']}** msgs, into {s['months'][-1]}\n"
                    )
                f.write("\n")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
