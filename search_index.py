"""Static client-side search for the comp.lang.cobol archive.

Emits two files into `markdown/`:

- `search-index.json` — one compact record per surviving thread: anchor,
  subject, a short snippet of the root message's first original (non-quoted)
  text, message count, and date span.
- `search.html` — a single self-contained page that loads the JSON and does
  live full-text search in the browser, linking straight to `threads/t-*.md`.

The page ships **no external dependency** (no MiniSearch/Fuse CDN): the dataset
is small enough (~16K threads) that a ranked vanilla-JS token match over
subject + snippet is instant, and it keeps the page working offline with zero
supply-chain surface. Serve `markdown/` over http (GitHub Pages or
`python -m http.server`) so the page's `fetch()` of the JSON is allowed.

See issue #3.
"""
from __future__ import annotations

import json

from archive import OUT, _is_quote_line, date_key, parse_archive, thread_summaries
from utils import span_label

SNIPPET_LEN = 200

# Attribution lines like "On ... John wrote:" / "Fred Smith <x@y> wrote:" that
# introduce a quote block carry no original content — drop them from snippets.
_ATTRIBUTION_TAIL = ("wrote:", "writes:", "said:", "schrieb:", "a écrit:")


def _is_attribution(line: str) -> bool:
    s = line.strip().lower()
    return bool(s) and s.endswith(_ATTRIBUTION_TAIL)


def snippet(body: str, limit: int = SNIPPET_LEN) -> str:
    """First chunk of original (non-quoted, non-attribution) prose from a body.

    Skips quoted lines (``>``/``|``/``›``) and reply-attribution lines, then
    flows the remaining text into a single whitespace-collapsed string trimmed
    to *limit* characters.
    """
    if not body:
        return ""
    parts: list[str] = []
    total = 0
    for line in body.split("\n"):
        if _is_quote_line(line) or _is_attribution(line):
            continue
        line = line.strip()
        if not line:
            continue
        parts.append(line)
        total += len(line) + 1
        if total >= limit:
            break
    text = " ".join(parts)
    if len(text) > limit:
        text = text[: limit - 1].rstrip() + "…"
    return text


def root_entry(summary: dict, msgs: dict) -> dict | None:
    """The message a thread's snippet should come from: its root, else the
    earliest message (orphan threads whose root isn't in the archive)."""
    root = summary["root"]
    if root in msgs:
        return msgs[root]
    mids = summary.get("msg_ids") or []
    if not mids:
        return None
    first = min(mids, key=lambda x: date_key(msgs[x]["dt"]))
    return msgs.get(first)


def build_records(summaries: list[dict], msgs: dict) -> list[dict]:
    records = []
    for s in summaries:
        entry = root_entry(s, msgs)
        body = entry.get("body", "") if entry else ""
        records.append({
            "a": s["anchor"],
            "s": s["subject"],
            "b": snippet(body),
            "c": s["count"],
            "sp": span_label(s["months"]),
        })
    # Most-active threads first so an empty query shows something useful and
    # equal-scoring matches keep a sensible default order.
    records.sort(key=lambda r: -r["c"])
    return records


# A single-file page. The JSON is fetched at runtime (kept separate so it can be
# cached independently and inspected on its own). {THREAD_COUNT} is filled in.
HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>comp.lang.cobol — Search</title>
<style>
  :root {{ color-scheme: light dark; }}
  body {{
    font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    max-width: 860px; margin: 0 auto; padding: 1.5rem 1rem 4rem;
  }}
  h1 {{ font-size: 1.5rem; margin: 0 0 .25rem; }}
  .sub {{ color: #888; margin: 0 0 1rem; font-size: .9rem; }}
  .sub a {{ color: inherit; }}
  #q {{
    width: 100%; box-sizing: border-box; padding: .65rem .8rem; font-size: 1.1rem;
    border: 1px solid #999; border-radius: 8px; background: Canvas; color: CanvasText;
  }}
  #status {{ color: #888; font-size: .85rem; margin: .6rem 0 1rem; }}
  ol {{ list-style: none; padding: 0; margin: 0; }}
  li {{ padding: .7rem 0; border-top: 1px solid rgba(128,128,128,.25); }}
  li a {{ font-size: 1.05rem; text-decoration: none; color: #06c; }}
  li a:hover {{ text-decoration: underline; }}
  .meta {{ color: #888; font-size: .82rem; margin-top: .15rem; }}
  .snip {{ color: #555; font-size: .9rem; margin-top: .25rem; }}
  @media (prefers-color-scheme: dark) {{
    li a {{ color: #6cf; }} .snip {{ color: #aaa; }}
  }}
  mark {{ background: #fe8; color: #000; padding: 0 1px; border-radius: 2px; }}
</style>
</head>
<body>
<h1>comp.lang.cobol — Search</h1>
<p class="sub">Full-text search across {THREAD_COUNT} threads ·
  <a href="README.md">archive home</a> ·
  <a href="subjects.md">subjects</a> ·
  <a href="topics.md">topics</a></p>
<input id="q" type="search" placeholder="Search subjects and first posts…" autofocus
       autocomplete="off" spellcheck="false">
<p id="status">Loading search index…</p>
<ol id="results"></ol>
<script>
const MAX_RESULTS = 200;
let DOCS = [];

const qEl = document.getElementById('q');
const statusEl = document.getElementById('status');
const resultsEl = document.getElementById('results');

function tokenize(s) {{
  return (s.toLowerCase().match(/[a-z0-9]+/g) || []);
}}

// Pre-tokenize once at load so each keystroke is a cheap scan.
function prepare(docs) {{
  for (const d of docs) {{
    d._s = ' ' + tokenize(d.s).join(' ') + ' ';
    d._b = ' ' + tokenize(d.b).join(' ') + ' ';
  }}
  return docs;
}}

// Score: every query term must hit subject or snippet (AND). Subject hits and
// whole-word hits rank above snippet/prefix hits; more messages breaks ties.
function score(doc, terms) {{
  let total = 0;
  for (const t of terms) {{
    const word = ' ' + t + ' ';
    let s = 0;
    if (doc._s.includes(word)) s = 10;
    else if (doc._s.includes(' ' + t)) s = 6;
    else if (doc._b.includes(word)) s = 3;
    else if (doc._b.includes(' ' + t)) s = 1;
    if (s === 0) return -1;           // a term matched nothing — drop the doc
    total += s;
  }}
  return total;
}}

function esc(s) {{
  return s.replace(/[&<>"]/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]));
}}

function highlight(text, terms) {{
  let out = esc(text);
  for (const t of terms) {{
    if (!t) continue;
    const re = new RegExp('(' + t.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&') + ')', 'gi');
    out = out.replace(re, '<mark>$1</mark>');
  }}
  return out;
}}

function render(matches, terms) {{
  resultsEl.innerHTML = '';
  const frag = document.createDocumentFragment();
  for (const d of matches) {{
    const li = document.createElement('li');
    li.innerHTML =
      '<a href="threads/' + d.a + '.md">' + highlight(d.s, terms) + '</a>' +
      '<div class="meta">' + d.c + ' msg' + (d.c === 1 ? '' : 's') + ' · ' + esc(d.sp) + '</div>' +
      (d.b ? '<div class="snip">' + highlight(d.b, terms) + '</div>' : '');
    frag.appendChild(li);
  }}
  resultsEl.appendChild(frag);
}}

function run() {{
  const terms = tokenize(qEl.value);
  if (!terms.length) {{
    statusEl.textContent = DOCS.length.toLocaleString() + ' threads. Type to search.';
    render(DOCS.slice(0, MAX_RESULTS), []);
    return;
  }}
  const scored = [];
  for (const d of DOCS) {{
    const sc = score(d, terms);
    if (sc >= 0) scored.push([sc, d]);
  }}
  scored.sort((a, b) => b[0] - a[0] || b[1].c - a[1].c);
  const shown = scored.slice(0, MAX_RESULTS).map(x => x[1]);
  statusEl.textContent =
    scored.length.toLocaleString() + ' match' + (scored.length === 1 ? '' : 'es') +
    (scored.length > MAX_RESULTS ? ' (showing top ' + MAX_RESULTS + ')' : '');
  render(shown, terms);
}}

fetch('search-index.json')
  .then(r => {{ if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); }})
  .then(data => {{
    DOCS = prepare(data);
    qEl.addEventListener('input', run);
    run();
    if (qEl.value) run();
  }})
  .catch(err => {{
    statusEl.innerHTML = 'Could not load <code>search-index.json</code> (' + esc(String(err)) +
      ').<br>Open this page over http — e.g. <code>python -m http.server</code> from the ' +
      '<code>markdown/</code> directory, or via GitHub Pages — rather than a <code>file://</code> URL.';
  }});
</script>
</body>
</html>
"""


def main() -> int:
    msgs, _, root_cache, _ = parse_archive()
    summaries = thread_summaries(msgs, root_cache)

    records = build_records(summaries, msgs)

    json_out = OUT / "search-index.json"
    html_out = OUT / "search.html"
    print(f"Writing {json_out}...")
    with json_out.open("w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, separators=(",", ":"))

    size_mb = json_out.stat().st_size / 1e6
    print(f"  {len(records):,} records, {size_mb:.1f} MB")

    print(f"Writing {html_out}...")
    with html_out.open("w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(THREAD_COUNT=f"{len(records):,}"))

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
