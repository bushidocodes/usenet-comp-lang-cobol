# Project notes for Claude

Python pipeline that converts `comp.lang.cobol.mbox` (375 MB, ~140K messages
from 1994–2013) into a per-thread Markdown index under `markdown/`. See
[README.md](README.md) for the user-facing overview.

## Architecture

`archive.py` is the foundation. It parses the mbox once, pickles the parsed
state to `.archive_cache.pickle` (~320 MB), and exposes:

- `parse_archive(use_cache=True)` → `(msgs, children, root_cache, depth)`
- `thread_summaries(msgs, root_cache, include_spam=False)` → list of summary
  dicts, one per surviving thread. **Filters spam by default** via `spam.thread_is_spam`.
- `filter_msgs(msgs, summaries)` → subset dict for generators that iterate
  over raw messages.
- `thread_anchor(root_id)` → `t-<10-hex>` anchor (md5 of root Message-ID).

Every generator (`thread.py`, `subjects.py`, `topics.py`, `years.py`,
`authors.py`, `stats.py`, `links.py`) calls `parse_archive()` and
`thread_summaries()`. The generators that also walk `msgs.values()` directly
(`stats`, `authors`, `years`, `links`) must additionally call `filter_msgs()`
so they don't tally spam content — this is easy to miss when adding new
generators.

## Spam filter

`spam.py` classifies messages by **URL host** in the non-quoted portion of
the body. A thread is spam only if the root message is spam **and** no
other message has substantive original content beyond auto-quote-headers —
human replies (even one-line jokes) keep a thread alive.

Two knobs:

- `SPAM_HOSTS` — exact host strings, substring-matched against the body.
- `SPAM_HOST_SUFFIXES` — domain suffixes that turned out to be 100% spam
  in this archive (`.co.cc`, `.byethost`, `.50webs.com`, `.blogspot.in`, …).
  Substring-matched, which also catches URLs that some mail clients wrap
  across newlines.

The source mbox is **not** modified. Spam stays in the archive — only the
generated Markdown is filtered.

When adding a new spam pattern:

1. Append to `SPAM_HOSTS` or `SPAM_HOST_SUFFIXES`.
2. Re-run the generators. The pickle cache stays valid since filtering
   happens at summary time, not at parse time.
3. Delete the now-orphaned `markdown/threads/t-*.md` files manually —
   `thread.py` only creates files, it doesn't sweep obsolete ones.

## Running the pipeline

```bash
python thread.py             # ~30s, writes 16K+ files
python subjects.py           # ~5s
python topics.py
python years.py
python authors.py
python stats.py
python links.py
```

Indexes are independent and can run in parallel. `thread.py` should be
first since the indexes link to its output, but nothing crashes if it's
out of date.

## Cache invalidation

Bump `archive.CACHE_VERSION` if you change parser semantics (the `entry`
dict schema, `_build_threads()` behavior, etc.). The pickle is keyed on
this constant and will re-parse on version mismatch.

## Watch out for

- **`markdown/README.md` is hand-maintained**, not generated. Its totals
  (`140,279 messages` / `16,371 thread files`) drift when spam patterns
  change; update by hand. Anything else there (the gap-year research,
  the layout description) is human-written.
- **`convert.py` is legacy.** It writes `markdown/YYYY-MM.md` monthly
  files (the old flat layout) **and overwrites `markdown/README.md`**.
  Do not run it as part of the per-thread pipeline.
- **The 1995-01 → 1998-05 gap is real**, baked into the source mbox.
  Generators handle it fine; don't try to "fix" missing months.
- **Quote-line detection** in `spam._non_quoted` requires `>` at column 0.
  Spam decoration like `   >>> http://… <<<` has leading whitespace and is
  treated as original content (correctly). Don't reintroduce `lstrip()`
  before the quote check.

## Adding a new generator

1. Import `parse_archive`, `thread_summaries` (and `filter_msgs` if you
   also iterate over raw `msgs.values()`).
2. Write output to `markdown/<name>.md` via `OUT / "<name>.md"`.
3. Add to the README's pipeline diagram and the "How to run" list.
