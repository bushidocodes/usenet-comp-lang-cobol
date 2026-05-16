"""Emit one Markdown file per conversation thread.

Each thread becomes `markdown/threads/<anchor>.md`, with the entire
message tree (DFS order, replies nested under parents) in one place
regardless of how long the conversation ran. Cross-reference indexes
(topics, years, authors, subjects, stats, links) link directly to the
per-thread file.
"""
from __future__ import annotations

import re
from collections import defaultdict

from archive import (
    OUT,
    THREADS_DIR,
    clean_body,
    date_key,
    parse_archive,
    thread_anchor,
    thread_summaries,
)
from topics import categorize


def md_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`")


def trim_subject(subject: str, max_len: int = 90) -> str:
    if len(subject) <= max_len:
        return subject
    return subject[: max_len - 1].rstrip() + "…"


def dfs_order(root, children, in_thread):
    """Depth-first traversal of a thread tree, returning IDs in display order.

    Falls back to date order for messages whose parent chain doesn't reach
    the root (orphaned replies, broken References headers).
    """
    order: list[str] = []
    visited: set = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node in in_thread:
            order.append(node)
        for child in reversed(children.get(node, ())):
            if child not in visited:
                stack.append(child)
    for mid in in_thread:
        if mid not in visited:
            order.append(mid)
    return order


def render_message(f, entry, depth_val):
    level = min(3 + depth_val, 6)
    hashes = "#" * level
    marker = ("↳ " * min(depth_val, 3)) if depth_val > 0 else ""
    f.write(f"{hashes} {marker}{md_escape(entry['subject'])}\n\n")
    if depth_val > 3:
        f.write(f"_(reply depth: {depth_val})_\n\n")
    f.write(f"- **From:** {md_escape(entry['sender'])}\n")
    f.write(f"- **Date:** {md_escape(entry['date_iso'])}\n")
    if entry["newsgroups"]:
        f.write(f"- **Newsgroups:** {md_escape(entry['newsgroups'])}\n")
    if entry["original_id"]:
        f.write(f"- **Message-ID:** `{entry['original_id']}`\n")
    if entry["in_reply_to_raw"]:
        irt_compact = re.sub(r"\s+", " ", entry["in_reply_to_raw"])
        f.write(f"- **In-Reply-To:** `{irt_compact}`\n")
    if entry["references"]:
        refs_compact = " ".join(entry["references"])
        f.write(f"- **References:** `{refs_compact}`\n")
    f.write("\n```\n")
    f.write(clean_body(entry["body"]))
    f.write("\n```\n\n")


def span_label(months: list[str]) -> str:
    if not months:
        return "undated"
    if months[0] == months[-1]:
        return months[0]
    return f"{months[0]} → {months[-1]}"


def write_thread(summary, msgs, children, depth):
    """Write one threads/<anchor>.md with the full conversation tree."""
    root = summary["root"]
    anchor = summary["anchor"]
    path = THREADS_DIR / f"{anchor}.md"

    in_thread = set(summary["msg_ids"])

    if root in msgs:
        order = dfs_order(root, children, in_thread)
    else:
        order = sorted(in_thread, key=lambda x: date_key(msgs[x]["dt"]))

    subject = summary["subject"] or "(no subject)"
    span = span_label(summary["months"])
    participants = len(summary["participants"])
    msg_count = summary["count"]
    topics = categorize(subject)

    with path.open("w", encoding="utf-8") as f:
        nav = [
            "[← Index](../README.md)",
            "[Topics](../topics.md)",
            "[Years](../years.md)",
            "[Subjects](../subjects.md)",
            "[Authors](../authors.md)",
        ]
        f.write(" · ".join(nav) + "\n\n")

        f.write(f"# {md_escape(subject)}\n\n")
        f.write(
            f"_{msg_count} message{'s' if msg_count != 1 else ''} · "
            f"{participants} participant{'s' if participants != 1 else ''} · "
            f"{span}_\n\n"
        )

        if topics:
            tag_str = " · ".join(
                f"[`{name}`](../topics.md#{slug})" for name, slug in topics
            )
            f.write(f"**Topics:** {tag_str}\n\n")

        f.write("---\n\n")

        for mid in order:
            render_message(f, msgs[mid], depth.get(mid, 0))

        f.write("---\n\n")
        f.write(" · ".join(nav) + "\n")


def main() -> int:
    msgs, children, root_cache, depth = parse_archive()
    summaries = thread_summaries(msgs, root_cache)

    THREADS_DIR.mkdir(parents=True, exist_ok=True)

    summaries.sort(key=lambda s: -s["count"])
    print(f"Writing {len(summaries):,} thread files to {THREADS_DIR}...")
    for i, s in enumerate(summaries, 1):
        write_thread(s, msgs, children, depth)
        if i % 2000 == 0:
            print(f"  ...{i:,} threads written")

    print(f"Done. {len(summaries):,} thread files written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
