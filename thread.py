"""Reorganize the comp.lang.cobol mbox into threaded monthly Markdown files.

Within each month: messages grouped by conversation (using References /
In-Reply-To headers), rendered as a tree — replies nested under their parents
in depth-first order. Each file also gets:
  - prev/next month navigation
  - a mini-TOC of every thread in the month
  - message counts in thread headings (this-month and total)
  - stable in-page anchors derived from each thread's root message-id
"""
from __future__ import annotations

import re
from collections import defaultdict

from archive import (
    OUT,
    clean_body,
    date_key,
    parse_archive,
    thread_anchor,
)
from topics import categorize


def md_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`")


def trim_subject(subject: str, max_len: int = 90) -> str:
    if len(subject) <= max_len:
        return subject
    return subject[: max_len - 1].rstrip() + "…"


def dfs_order(root, children, in_month):
    """Iterative DFS from root, returning message IDs in this month in tree order."""
    order = []
    visited = set()
    stack = [root]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node in in_month:
            order.append(node)
        for child in reversed(children.get(node, ())):
            if child not in visited:
                stack.append(child)
    for mid in in_month:
        if mid not in visited:
            order.append(mid)
    return order


def render_message(f, entry, depth_val, msgs):
    level = min(3 + depth_val, 6)
    hashes = "#" * level
    marker = ("↳ " * min(depth_val, 3)) if depth_val > 0 else ""
    f.write(f"{hashes} {marker}{md_escape(entry['subject'])}\n\n")
    if depth_val > 3:
        f.write(f"_(thread depth: {depth_val})_\n\n")
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


def write_month(ym, threads_in_month, msgs, children, depth, root_cache, prev_ym, next_ym, total_count_by_root):
    """Write one YYYY-MM.md with mini-TOC + threaded message tree."""
    path = OUT / f"{ym}.md"
    thread_roots = sorted(
        threads_in_month.keys(),
        key=lambda r: date_key(msgs[min(threads_in_month[r], key=lambda x: date_key(msgs[x]["dt"]))]["dt"]),
    )
    msg_count = sum(len(threads_in_month[r]) for r in thread_roots)

    with path.open("w", encoding="utf-8") as f:
        # Nav bar
        nav = []
        if prev_ym:
            nav.append(f"[← {prev_ym}]({prev_ym}.md)")
        nav.append("[Index](README.md)")
        nav.append("[Topics](topics.md)")
        if next_ym:
            nav.append(f"[{next_ym} →]({next_ym}.md)")
        f.write(" · ".join(nav) + "\n\n")

        f.write(f"# comp.lang.cobol — {ym}\n\n")
        f.write(f"_{msg_count} messages in {len(thread_roots)} threads_\n\n")

        # Mini-TOC of threads in this month
        f.write("## Threads this month\n\n")
        for root in thread_roots:
            in_month_count = len(threads_in_month[root])
            total_count = total_count_by_root.get(root, in_month_count)
            anchor = thread_anchor(root)
            # Resolve a subject for the TOC line
            if root in msgs:
                subj = msgs[root]["norm_subject"] or msgs[root]["subject"]
            else:
                first_mid = min(threads_in_month[root], key=lambda x: date_key(msgs[x]["dt"]))
                subj = msgs[first_mid]["norm_subject"] or msgs[first_mid]["subject"]
            subj = subj or "(no subject)"
            label = trim_subject(subj)
            if total_count == in_month_count:
                count_label = f"{in_month_count} msg{'s' if in_month_count != 1 else ''}"
            else:
                count_label = f"{in_month_count}/{total_count} msgs this month"
            f.write(f"- [{md_escape(label)}](#{anchor}) — {count_label}\n")
        f.write("\n---\n\n")

        # Each thread
        for root in thread_roots:
            in_month_ids = set(threads_in_month[root])
            in_month_count = len(in_month_ids)
            total_count = total_count_by_root.get(root, in_month_count)
            anchor = thread_anchor(root)

            if root in msgs:
                thread_subject = msgs[root]["norm_subject"] or msgs[root]["subject"]
            else:
                first_mid = min(in_month_ids, key=lambda x: date_key(msgs[x]["dt"]))
                thread_subject = (
                    msgs[first_mid]["norm_subject"] or msgs[first_mid]["subject"]
                )

            # Anchor + heading
            f.write(f'<a id="{anchor}"></a>\n')
            count_suffix = (
                f"— {in_month_count} msgs"
                if total_count == in_month_count
                else f"— {in_month_count} this month / {total_count} total"
            )
            f.write(f"## Thread: {md_escape(thread_subject)} {count_suffix}\n\n")

            # Topic tags
            topics = categorize(thread_subject)
            if topics:
                tag_str = " · ".join(
                    f"[`{name}`](topics.md#{slug})" for name, slug in topics
                )
                f.write(f"_Topics: {tag_str}_\n\n")

            if root in msgs and msgs[root]["ym"] != ym:
                root_ym = msgs[root]["ym"]
                f.write(f"_Thread started [{root_ym}]({root_ym}.md#{anchor})._\n\n")

            if root in msgs:
                order = dfs_order(root, children, in_month_ids)
            else:
                order = sorted(in_month_ids, key=lambda x: date_key(msgs[x]["dt"]))

            for mid in order:
                render_message(f, msgs[mid], depth.get(mid, 0), msgs)

            f.write("---\n\n")

        # Footer nav
        f.write("\n")
        if prev_ym or next_ym:
            footer = []
            if prev_ym:
                footer.append(f"[← {prev_ym}]({prev_ym}.md)")
            footer.append("[Index](README.md)")
            if next_ym:
                footer.append(f"[{next_ym} →]({next_ym}.md)")
            f.write(" · ".join(footer) + "\n")


def main() -> int:
    msgs, children, root_cache, depth = parse_archive()

    by_month: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    total_count_by_root: dict[str, int] = defaultdict(int)
    for mid, entry in msgs.items():
        ym = entry["ym"]
        root = root_cache[mid]
        by_month[ym][root].append(mid)
        total_count_by_root[root] += 1

    for ym in by_month:
        for root in by_month[ym]:
            by_month[ym][root].sort(key=lambda x: date_key(msgs[x]["dt"]))

    sorted_months = sorted(by_month)
    print(f"Writing {len(sorted_months)} monthly files...")

    for i, ym in enumerate(sorted_months):
        prev_ym = sorted_months[i - 1] if i > 0 else None
        next_ym = sorted_months[i + 1] if i + 1 < len(sorted_months) else None
        write_month(
            ym, by_month[ym], msgs, children, depth, root_cache, prev_ym, next_ym, total_count_by_root
        )

    print(f"Done. {len(sorted_months)} months written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
