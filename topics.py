"""Build a topical index of comp.lang.cobol threads.

Loads the cached thread tree from `archive.py`, categorizes each thread by
subject-line keyword rules, and emits `markdown/topics.md`.
"""
from __future__ import annotations

import re
from collections import defaultdict

from archive import OUT, date_key, parse_archive, thread_summaries

MAX_THREADS_PER_TOPIC = 60
MIN_MESSAGES_FOR_UNCATEGORIZED = 4

# (display_name, slug, [regex_patterns]). Threads can match multiple topics.
TOPIC_RULES = [
    (
        "Y2K and Year-2000 remediation",
        "y2k",
        [
            r"\by2k\b",
            r"year\s*2[\s\-]*0?00",
            r"\by2 ?k\b",
            r"millennium",
            r"date\s*(problem|conversion|routine|expansion|window)",
            r"\b(2|two)[- ]digit\s*year",
            r"\b(4|four)[- ]digit\s*year",
            r"century\s*(roll|window|date)",
            r"end of the century",
            r"\bbug\b.*200?0",
            r"200?0\b.*\bbug",
        ],
    ),
    (
        "COBOL's future, legacy, and obsolescence",
        "future",
        [
            r"is\s*cobol\s*dead",
            r"cobol.{0,5}dy(ing|e)",
            r"future\s+of\s+cobol",
            r"\blegacy\b",
            r"dinosaur",
            r"obsolet",
            r"\breplace\s+cobol\b",
            r"will\s+cobol",
            r"cobol\s+(still|forever|alive)",
            r"history of cobol",
            r"why\s+cobol",
        ],
    ),
    (
        "Jobs, careers, recruiting, salary",
        "jobs",
        [
            r"\bjobs?\b",
            r"\bcareer",
            r"\bhir(ing|e)\b",
            r"\brecruit",
            r"\bresume\b",
            r"head ?hunter",
            r"\bsalary\b",
            r"contract(or|ing|s)?\b",
            r"\bmarket\b",
            r"opportunit",
            r"position",
            r"\blayoff",
            r"^\s*wanted",
            r"\bcv\b",
            r"available\b.*program",
            r"\bh-?1b\b",
            r"outsourc",
            r"offshor",
            r"\bw[- ]?2\b",
            r"\bc2c\b",
        ],
    ),
    (
        "Compilers and vendors",
        "compilers",
        [
            r"micro ?focus",
            r"fujitsu",
            r"acu ?cobol",
            r"rm[/\- ]?cobol",
            r"\brealia\b",
            r"\bisvr\b",
            r"\bibm cobol\b",
            r"\bvs\s*cobol\b",
            r"vendor",
            r"compiler",
            r"\bmf\b.*cobol",
            r"\bnetcobol\b",
            r"\bmerant\b",
            r"\bryan ?mcfarland\b",
            r"\bcobol[- ]?ii\b",
        ],
    ),
    (
        "Open-source COBOL (GnuCOBOL, OpenCOBOL, TinyCOBOL)",
        "open-source",
        [
            r"open\s*cobol",
            r"gnu\s*cobol",
            r"tiny\s*cobol",
            r"\bcobc\b",
            r"\bcobol-it\b",
        ],
    ),
    (
        "Object-oriented COBOL",
        "oo",
        [
            r"\boo\b",
            r"\boo[- ]?cobol\b",
            r"object[- ]?orient",
            r"\bclass(es)?\b",
            r"\binherit",
            r"polymorph",
            r"\bmethod\b",
            r"\bencapsulat",
        ],
    ),
    (
        "Language features and syntax",
        "syntax",
        [
            r"\bgo[- ]?to\b",
            r"\bperform\b",
            r"structured",
            r"spaghetti",
            r"\bevaluate\b",
            r"\bredefines\b",
            r"\bcopy\b",
            r"\busage\b",
            r"\bcomp-?\d\b",
            r"\bpic(ture)?\s+clause",
            r"\bsection",
            r"\bparagraph",
            r"\bend-?if\b",
            r"\binspect\b",
            r"\bstring\b",
            r"\bunstring\b",
            r"\baccept\b",
            r"\bsign\b",
            r"\bdisplay\b\s+statement",
            r"\bnext\s+sentence\b",
            r"\binitialize\b",
            r"\boccurs\b",
        ],
    ),
    (
        "COBOL standards (ANS, ISO, 74/85/2002/2014)",
        "standards",
        [
            r"\bans[i]?\s*[-/]?\s*cobol",
            r"\biso\s*cobol",
            r"cobol\s*(74|85|2002|2014)",
            r"\bansi\s*8[45]\b",
            r"\bstandard(s)?\b",
            r"\bx3j4\b",
            r"\bj4\b",
        ],
    ),
    (
        "Migration and conversion",
        "migration",
        [
            r"migrat(e|ion|ing|or)",
            r"convert(ing|ed|er|ion|s)?",
            r"port(ing|ed)\b",
            r"re[- ]?platform",
            r"modernization",
            r"transition",
            r"cobol\s*->\s*[a-z]",
            r"cobol\s*to\s*(c\b|c\+\+|java|\.net|python)",
            r"\brewrite\b",
        ],
    ),
    (
        "Mainframe, z/OS, JCL, CICS",
        "mainframe",
        [
            r"\bz[/\- ]?os\b",
            r"\bmvs\b",
            r"\bjcl\b",
            r"\bcics\b",
            r"mainframe",
            r"\bims\b",
            r"\btso\b",
            r"\bispf\b",
            r"\bos[/\- ]?390\b",
            r"\bs[/\- ]?390\b",
            r"\bracf\b",
            r"\babend\b",
            r"\b0c[0-9]\b",
            r"\bdsn\b",
            r"\bsysout\b",
            r"jes2",
        ],
    ),
    (
        "AS/400, iSeries, RPG",
        "as400",
        [
            r"as[/\- ]?400",
            r"iseries",
            r"system\s*i\b",
            r"\bibm\s*i\b",
            r"\brpg\b",
        ],
    ),
    (
        "Databases and SQL",
        "databases",
        [
            r"\bsql\b",
            r"database",
            r"\bdb2\b",
            r"oracle",
            r"\bodbc\b",
            r"\bjdbc\b",
            r"\bmysql\b",
            r"\bsybase\b",
            r"sql\s*server",
            r"embedded\s*sql",
            r"\besql\b",
            r"\bcursor\b",
            r"stored\s*proc",
        ],
    ),
    (
        "VSAM, files, sorting",
        "files",
        [
            r"\bvsam\b",
            r"\bisam\b",
            r"indexed\s*file",
            r"sequential\s*file",
            r"\bsort\b",
            r"\bmerge\b",
            r"\bfile\s*status\b",
            r"\bgdg\b",
            r"\bksds\b",
            r"\besds\b",
            r"\brrds\b",
            r"\bfd\b",
            r"variable\s*length",
        ],
    ),
    (
        "Date and calendar processing",
        "dates",
        [
            r"\bdate\b",
            r"\bcalendar\b",
            r"\bjulian\b",
            r"\btimestamp\b",
            r"current[- ]?date",
            r"day[- ]?of[- ]?(week|year)",
            r"\bleap\s*year\b",
        ],
    ),
    (
        "Web, XML, modern integration",
        "web",
        [
            r"\bweb\b",
            r"\bhtml\b",
            r"\bhttp\b",
            r"\binternet\b",
            r"\bbrowser\b",
            r"\bxml\b",
            r"\bjson\b",
            r"\bsoap\b",
            r"web\s*service",
            r"\brest\b",
            r"\bcgi\b",
            r"\b\.net\b",
            r"micro\s*service",
        ],
    ),
    (
        "Tutorials, books, learning",
        "learning",
        [
            r"\bbook(s)?\b",
            r"tutorial",
            r"newbie",
            r"begin(ner|ning)",
            r"\bstudent",
            r"homework",
            r"\btextbook",
            r"\blearn",
            r"reference",
            r"\bcourse\b",
            r"\bteach",
        ],
    ),
    (
        "Help requests and how-to",
        "help",
        [
            r"^\s*help\b",
            r"\bhow\s*to\b",
            r"\bhow\s*do\s*i\b",
            r"\bneed\s*help\b",
            r"\bsos\b",
            r"\bplease\s*help\b",
            r"\?\?+",
            r"^\s*urgent",
            r"newbie\s*question",
        ],
    ),
    (
        "Off-topic and spam",
        "spam",
        [
            r"viagra",
            r"\bcasino\b",
            r"\bpoker\b",
            r"\bpenis\b",
            r"\bporn\b",
            r"\bsex\b",
            r"earn\s*money",
            r"work\s*from\s*home",
            r"\bmlm\b",
            r"weight\s*loss",
            r"wholesale",
            r"\boff[- ]?topic\b",
            r"\bot:\s",
            r"^ot\s",
            r"replica\s*watch",
        ],
    ),
    (
        "Meta: FAQs, group policy, charter",
        "meta",
        [
            r"\bfaq\b",
            r"\bcharter\b",
            r"\bnetiquette\b",
            r"news\s*group",
            r"\bmoderat",
            r"\bspam\b",
            r"^test\b",
            r"\btroll\b",
            r"killfile",
        ],
    ),
]


def categorize(subject: str):
    """Return list of (name, slug) tuples this subject matches."""
    matches = []
    for name, slug, patterns in TOPIC_RULES:
        for pat in patterns:
            if re.search(pat, subject, re.IGNORECASE):
                matches.append((name, slug))
                break
    return matches


def trim_label(s: str, n: int = 100) -> str:
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def thread_link(summary):
    return f"[{trim_label(summary['subject'])}](threads/{summary['anchor']}.md)"


def span_label(s):
    if not s["months"]:
        return "undated"
    if s["months"][0] == s["months"][-1]:
        return s["months"][0]
    return f"{s['months'][0]} → {s['months'][-1]}"


def write_topics(summaries, path):
    by_topic: dict[tuple, list] = defaultdict(list)
    uncategorized = []
    for s in summaries:
        topics = categorize(s["subject"])
        if topics:
            for t in topics:
                by_topic[t].append(s)
        else:
            uncategorized.append(s)

    for key in by_topic:
        by_topic[key].sort(key=lambda s: (-s["count"], s["first_ym"]))
    uncategorized.sort(key=lambda s: (-s["count"], s["first_ym"]))

    topic_order = [(name, slug) for name, slug, _ in TOPIC_RULES]
    total_threads = len(summaries)
    total_msgs = sum(s["count"] for s in summaries)

    with path.open("w", encoding="utf-8") as f:
        f.write("[← README](README.md) · [Years](years.md) · [Authors](authors.md) · [Subjects](subjects.md) · [Links](links.md) · [Stats](stats.md)\n\n")
        f.write("# comp.lang.cobol — Topic Index\n\n")
        f.write(
            f"Topical groupings of the {total_threads:,} threads ({total_msgs:,} messages) "
            "in this archive. Threads are matched by subject-line keyword rules and may "
            "appear under multiple topics.\n\n"
        )

        f.write("## Topics\n\n")
        for name, slug in topic_order:
            count = len(by_topic.get((name, slug), []))
            f.write(f"- [{name}](#{slug}) — {count:,} threads\n")
        f.write(
            f"- [Uncategorized (top by message count)](#uncategorized) — "
            f"{len(uncategorized):,} threads\n\n"
        )

        f.write("## Top threads overall (by message count)\n\n")
        top_overall = sorted(summaries, key=lambda s: -s["count"])[:30]
        for s in top_overall:
            f.write(f"- {thread_link(s)} — **{s['count']}** msgs · {span_label(s)}\n")
        f.write("\n")

        for name, slug in topic_order:
            threads_in_topic = by_topic.get((name, slug), [])
            f.write(f"## {name} <a id='{slug}'></a>\n\n")
            if not threads_in_topic:
                f.write("_No threads matched._\n\n")
                continue
            total_msgs_topic = sum(t["count"] for t in threads_in_topic)
            f.write(
                f"_{len(threads_in_topic):,} threads · {total_msgs_topic:,} messages._\n\n"
            )
            shown = threads_in_topic[:MAX_THREADS_PER_TOPIC]
            for s in shown:
                f.write(f"- {thread_link(s)} — **{s['count']}** msgs · {span_label(s)}\n")
            if len(threads_in_topic) > MAX_THREADS_PER_TOPIC:
                hidden = len(threads_in_topic) - MAX_THREADS_PER_TOPIC
                f.write(
                    f"- _…and {hidden:,} more threads (showing top {MAX_THREADS_PER_TOPIC} by message count)._\n"
                )
            f.write("\n")

        f.write("## Uncategorized (top by message count) <a id='uncategorized'></a>\n\n")
        big_uncat = [u for u in uncategorized if u["count"] >= MIN_MESSAGES_FOR_UNCATEGORIZED]
        f.write(
            f"_{len(uncategorized):,} threads didn't match any topic rule. "
            f"Showing the {min(MAX_THREADS_PER_TOPIC, len(big_uncat))} most active "
            f"(threads with ≥ {MIN_MESSAGES_FOR_UNCATEGORIZED} messages)._\n\n"
        )
        for s in big_uncat[:MAX_THREADS_PER_TOPIC]:
            f.write(f"- {thread_link(s)} — **{s['count']}** msgs · {span_label(s)}\n")


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)
    out = OUT / "topics.md"
    print(f"Writing {out}...")
    write_topics(summaries, out)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
