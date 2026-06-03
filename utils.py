"""Shared utilities used across the Markdown and JSON generators."""
from __future__ import annotations


def md_escape(text: str) -> str:
    """Escape backslashes, backticks, and pipes for Markdown output."""
    return text.replace("\\", "\\\\").replace("`", "\\`").replace("|", "\\|")


def trim(text: str, n: int = 80) -> str:
    """Truncate *text* to at most *n* characters, appending … if cut."""
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def span_label(months: list[str]) -> str:
    """Return a human-readable date-span string from a sorted months list."""
    if not months:
        return "undated"
    return months[0] if months[0] == months[-1] else f"{months[0]} → {months[-1]}"


def dfs_order(root: str, children: dict, in_thread: set) -> list[str]:
    """Depth-first traversal of a thread tree, returning IDs in display order.

    Falls back to append-at-end for messages whose parent chain doesn't
    reach the root (orphaned replies, broken References headers).
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
