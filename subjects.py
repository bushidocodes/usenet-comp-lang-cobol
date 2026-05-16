"""Alphabetical concordance of every thread subject.

Useful for Ctrl-F / browser search across the entire archive.
Emits `markdown/subjects.md`.
"""
from __future__ import annotations

import string
from collections import defaultdict

from archive import OUT, parse_archive, thread_summaries


def md_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`").replace("|", "\\|")


def trim(text: str, n: int = 110) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def bucket_key(subject: str) -> str:
    """First-letter bucket for grouping. Non-alpha lumped under '#'."""
    if not subject:
        return "#"
    ch = subject[0].upper()
    return ch if ch in string.ascii_uppercase else "#"


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)

    buckets: dict[str, list] = defaultdict(list)
    for s in summaries:
        key = bucket_key(s["subject"])
        buckets[key].append(s)

    for key in buckets:
        buckets[key].sort(key=lambda s: (s["subject"].lower(), s["first_ym"]))

    out = OUT / "subjects.md"
    print(f"Writing {out}...")

    with out.open("w", encoding="utf-8") as f:
        f.write("[← README](README.md) · [Topics](topics.md) · [Years](years.md) · [Authors](authors.md) · [Stats](stats.md) · [Links](links.md)\n\n")
        f.write("# comp.lang.cobol — Subject Concordance\n\n")
        f.write(
            f"Every distinct thread subject in the archive ({len(summaries):,} threads), "
            "sorted alphabetically. Built for browser search — load this page and Ctrl-F "
            "for the term you want.\n\n"
        )

        # Alphabet jumplinks
        f.write("**Jump to:** ")
        letters = ["#"] + list(string.ascii_uppercase)
        present = [c for c in letters if buckets.get(c)]
        f.write(" · ".join(f"[{c}](#letter-{c.lower() if c != '#' else 'symbols'})" for c in present))
        f.write("\n\n")

        for letter in letters:
            entries = buckets.get(letter, [])
            if not entries:
                continue
            slug = "symbols" if letter == "#" else letter.lower()
            f.write(f"## {letter} <a id='letter-{slug}'></a>\n\n")
            f.write(f"_{len(entries):,} threads._\n\n")
            f.write("| Subject | Msgs | Span |\n|---|---:|---|\n")
            for s in entries:
                label = trim(s["subject"])
                ym = s["first_ym"]
                link = (
                    f"[{md_escape(label)}]({ym}.md#{s['anchor']})"
                    if ym != "undated"
                    else md_escape(label)
                )
                if s["months"] and s["months"][0] != s["months"][-1]:
                    span = f"{s['months'][0]} → {s['months'][-1]}"
                else:
                    span = s["months"][0] if s["months"] else "undated"
                f.write(f"| {link} | {s['count']} | {span} |\n")
            f.write("\n")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
