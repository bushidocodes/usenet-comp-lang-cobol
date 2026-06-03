"""Extract URLs cited in the comp.lang.cobol archive.

Walks every message body, pulls out HTTP(S) URLs, groups by domain, and
emits `markdown/links.md` — useful for finding what external resources
(papers, tools, vendor sites, news stories) people linked to over 20 years.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from urllib.parse import urlparse

from archive import OUT, filter_msgs, parse_archive, thread_anchor, thread_summaries

URL_RE = re.compile(
    r"""(?xi)
    \b(?:https?://|ftp://|www\.)
    [^\s<>"'(){}\[\]]+
    """,
)

# Trim trailing punctuation that's almost always sentence-context, not URL
TRAIL_TRIM = ".,;:!?)]}>\""

TOP_DOMAINS_SHOWN = 75
TOP_URLS_SHOWN = 1000
MIN_DOMAIN_MENTIONS = 3


def md_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("`", "\\`").replace("|", "\\|")


def trim(text: str, n: int = 80) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def normalize_url(raw: str) -> str:
    url = raw.rstrip(TRAIL_TRIM)
    # `www.foo.com/x` (no scheme) — prepend http:// so urlparse works
    if url.startswith("www."):
        url = "http://" + url
    return url


def get_domain(url: str) -> str:
    try:
        host = urlparse(url).hostname or ""
    except Exception:
        return ""
    host = host.lower().lstrip(".")
    if host.startswith("www."):
        host = host[4:]
    return host


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)
    msgs = filter_msgs(msgs, summaries)

    print("Scanning bodies for URLs...")
    domain_count: Counter = Counter()
    url_count: Counter = Counter()
    domain_threads: dict[str, set] = defaultdict(set)
    url_first_msg: dict[str, str] = {}
    url_year_count: dict[str, Counter] = defaultdict(Counter)

    scanned = 0
    for mid, entry in msgs.items():
        scanned += 1
        if scanned % 20000 == 0:
            print(f"  ...{scanned} scanned")
        body = entry.get("body") or ""
        if not body:
            continue
        for raw in URL_RE.findall(body):
            url = normalize_url(raw)
            domain = get_domain(url)
            if not domain or "." not in domain:
                continue
            domain_count[domain] += 1
            url_count[url] += 1
            domain_threads[domain].add(root_cache[mid])
            if url not in url_first_msg:
                url_first_msg[url] = mid
            if entry["dt"]:
                url_year_count[domain][entry["dt"].year] += 1

    total_urls = sum(url_count.values())
    unique_urls = len(url_count)
    unique_domains = len(domain_count)

    out = OUT / "links.md"
    print(f"Writing {out} ({total_urls:,} URL mentions, {unique_domains:,} domains)...")

    with out.open("w", encoding="utf-8") as f:
        f.write("[← README](README.md) · [Topics](topics.md) · [Years](years.md) · [Authors](authors.md) · [Stats](stats.md) · [Subjects](subjects.md)\n\n")
        f.write("# comp.lang.cobol — External Links\n\n")
        f.write(
            f"URLs extracted from {scanned:,} message bodies. "
            f"**{total_urls:,} total mentions** across **{unique_urls:,} unique URLs** "
            f"and **{unique_domains:,} domains**. "
            "Useful for tracking what tools, vendors, papers, and news stories "
            "the community pointed at over two decades.\n\n"
        )

        # Top domains
        f.write(f"## Top {TOP_DOMAINS_SHOWN} domains by mention count\n\n")
        f.write("| Domain | Mentions | Threads | Peak year |\n|---|---:|---:|---|\n")
        for domain, count in domain_count.most_common(TOP_DOMAINS_SHOWN):
            if count < MIN_DOMAIN_MENTIONS:
                break
            tcount = len(domain_threads[domain])
            year_counts = url_year_count[domain]
            peak = (
                f"{year_counts.most_common(1)[0][0]} ({year_counts.most_common(1)[0][1]})"
                if year_counts
                else "—"
            )
            f.write(f"| `{md_escape(domain)}` | {count:,} | {tcount:,} | {peak} |\n")
        f.write("\n")

        # Top individual URLs
        f.write(f"## Top {TOP_URLS_SHOWN} individual URLs (≥2 mentions)\n\n")
        shown = 0
        for url, count in url_count.most_common():
            if count < 2:
                break
            if shown >= TOP_URLS_SHOWN:
                break
            first_mid = url_first_msg[url]
            first_entry = msgs[first_mid]
            ym = first_entry["ym"]
            root = root_cache.get(first_mid)
            if root and ym != "undated":
                anchor = thread_anchor(root)
                first_link = f"[first cited {ym}](threads/{anchor}.md)"
            elif ym != "undated":
                first_link = f"first cited {ym}"
            else:
                first_link = "undated"
            display = trim(url, 100)
            f.write(f"- [{md_escape(display)}]({url}) — **{count}** mentions · {first_link}\n")
            shown += 1
        f.write("\n")

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
