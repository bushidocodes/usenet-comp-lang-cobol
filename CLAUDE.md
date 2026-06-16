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

## Author identity grouping

`authors.group_authors(msgs)` is the **single source of truth** for collapsing
one person's many email addresses into one entry. Both `authors.py` (Markdown
profiles) and `export_json.py` (website data) call it, so they can't drift.
It returns `(groups, email_to_group, email_to_canonical)`. Two layers:

1. **Primary** — group by `merge_key(canonical_display_name)`, with the
   `UA_AUTHOR_NAMES` bridge applied first (issue #28). Names too short/empty
   to key on fall back to a per-email group.
2. **Reconciliation** (`_reconcile`, issue #8) — merge primary groups that
   share a **distinctive email local-part** *and* a **compatible name**.
   Both signals are required: `distinctive_localpart()` drops generic/role/
   first-name/synthetic-UA local-parts, and `_names_compatible()` requires a
   surname+first-name match (with a `NICKNAMES` map) for full names. Neither
   shared-domain nor name-alone is ever trusted — both over-merge unrelated
   people (there's more than one "John Smith").

When tuning the merge, regenerate `authors.md` and eyeball the diff on the
top ~200 groups; false merges show up as one group with two surnames.

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
2. Re-run `python build.py`. The pickle cache stays valid since filtering
   happens at summary time, not at parse time. Orphaned thread files are
   swept automatically at the end of the run.

## Running the pipeline

```bash
python build.py              # rebuild only stale outputs (recommended)
python build.py --force      # rebuild everything unconditionally
python build.py --dry-run    # preview what would run without running it
```

`build.py` runs `thread.py` first (indexes link to its output), then runs
the six index generators in parallel. It skips any generator whose output
is newer than `archive.py`, `spam.py`, and the generator's own source file.

To run generators individually:

```bash
python thread.py             # ~30s, writes 16K+ files
python subjects.py           # ~5s
python topics.py
python years.py
python authors.py
python stats.py
python links.py
```

## Cache invalidation

Bump `archive.CACHE_VERSION` if you change parser semantics (the `entry`
dict schema, `_build_threads()` behavior, etc.). The pickle is keyed on
this constant and will re-parse on version mismatch.

## Watch out for

- **`markdown/README.md` is hand-maintained**, not generated. It contains
  the gap-year research and layout description; it has no counts that drift
  with spam changes (those live in the generated `stats.md`).
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
3. Add an entry to `INDEX_SPECS` in `build.py`.
4. Add to the README's pipeline diagram and the "How to run" list.
