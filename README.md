# usenet-cobol

Pipeline that converts the comp.lang.cobol Usenet archive (1994–2013) from
mbox into a browsable Markdown tree under [`markdown/`](markdown/).
[`markdown/README.md`](markdown/README.md) is the landing page readers actually browse.

## Source data

[`comp.lang.cobol.mbox`](comp.lang.cobol.mbox) — 375 MB, every message from
comp.lang.cobol from 1994-11 to 2013-06 (with a 1995–mid-1998 gap inherited
from the Giganews tape archive). From
[archive.org/details/usenet-comp](https://archive.org/details/usenet-comp).

## Pipeline

```
comp.lang.cobol.mbox
     │
     │  archive.py   ──>  parse mbox, build thread tree, cache to disk
     ▼
.archive_cache.pickle  ──┐
                         │  thread_summaries()  ──> spam-filtered via spam.py
                         │
   ┌─────────────────────┴─────────────────────┐
   ▼                                           ▼
thread.py                       subjects.py / topics.py / years.py
   │                            authors.py / stats.py / links.py
   ▼                                           │
markdown/threads/t-*.md                        ▼
                                  markdown/{subjects,topics,years,
                                            authors,stats,links}.md
```

`spam.py` is consulted by `archive.thread_summaries()` so every downstream
generator automatically sees a spam-filtered view. Generators that walk
`msgs.values()` directly (`stats.py`, `authors.py`, `years.py`, `links.py`)
also call `archive.filter_msgs()` on the same set.

## How to run

```bash
# First run only — parses the 375 MB mbox (~60–90s). Subsequent generator
# runs hit the cached pickle (~1s).
python archive.py

# Per-thread files. Slow — writes 16,000+ files (~30s).
python thread.py

# Indexes. Independent of each other — run in any order or in parallel.
python subjects.py
python topics.py
python years.py
python authors.py
python stats.py
python links.py
```

After modifying `spam.py` (e.g. adding a new spam host), the cache stays
valid — just re-run the generators.

## Files

| File | Role |
|---|---|
| `comp.lang.cobol.mbox` | Source data (in repo; do not modify) |
| `archive.py` | Mbox parser, cache, `parse_archive()`, `thread_summaries()`, `filter_msgs()` |
| `spam.py` | Spam classifier — `SPAM_HOSTS`, `SPAM_HOST_SUFFIXES`, `message_is_spam`, `thread_is_spam` |
| `thread.py` | Generates `markdown/threads/t-*.md` |
| `subjects.py` | Alphabetical thread-subject concordance → `markdown/subjects.md` |
| `topics.py` | Topic-rule categorization → `markdown/topics.md` |
| `years.py` | Per-year overview → `markdown/years.md` |
| `authors.py` | Top-100 posters → `markdown/authors.md` |
| `stats.py` | Aggregate statistics → `markdown/stats.md` |
| `links.py` | External URLs cited → `markdown/links.md` |
| `markdown/README.md` | Archive viewer's landing page — **hand-maintained**, not generated |
| `convert.py` | Legacy monthly-format converter — not part of the per-thread pipeline |
| `.archive_cache.pickle` | Pickled parsed state (~320 MB, gitignored) |

## Adding new spam patterns

Edit [`spam.py`](spam.py):

- `SPAM_HOSTS` — exact host strings (`my-best-web.com`, `jaisahata.tk`).
  Matched as a substring against message body.
- `SPAM_HOST_SUFFIXES` — TLD/suffix patterns that turned out to be 100%
  spam in this archive (`.co.cc`, `.byethost`, `.50webs.com`).

Re-run the generators. Already-deleted thread `.md` files stay deleted;
`thread.py` only writes files for non-spam threads, never overwrites
into the spam set.
