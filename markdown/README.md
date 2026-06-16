# comp.lang.cobol Usenet Archive

Converted from mbox to Markdown. One file per conversation. See [Stats](stats.md) for current totals.

## Browse

- **[Topics](topics.md)** — threads grouped by subject (Y2K, careers, compilers, mainframe, OO COBOL, language debates, etc.).
- **[Years](years.md)** — yearly overview with top threads and dominant topics per year.
- **[Authors](authors.md)** — top 100 posters (merged across email aliases) with their most-active conversations.
- **[Subjects](subjects.md)** — alphabetical concordance of every thread subject (built for Ctrl-F).
- **[Links](links.md)** — external URLs cited in the archive, grouped by domain.
- **[Stats](stats.md)** — activity timeline, longest threads, busiest months, posting patterns, first-mentions of key terms.
- **[Threads](threads/)** — full thread tree, one file per conversation. Reach individual threads via the indexes above.

Source: [archive.org/details/usenet-comp](https://archive.org/details/usenet-comp) — `comp.lang.cobol.mbox.zip` (94.8 MB compressed, 375 MB raw). Contributed by Giganews, captured ~2013-08.

## The 1995–mid-1998 gap

Coverage jumps from **December 1994 → June 1998** with no messages in between. This is a property of the source archive, not the conversion. The Internet Archive's Usenet collection is built from Giganews' tape archives, which have well-known gaps in the mid-1990s — DejaNews started indexing in 1995, Google acquired DejaNews in 2001, and Giganews was never the canonical record for that era.

### Sources investigated

| Source | Coverage | Verdict |
|---|---|---|
| `archive.org/usenet-comp/comp.lang.cobol.mbox.zip` | 1994-11 to 2013-06 (with gap) | The archive used here |
| `archive.org/usenet-comp.lang/comp.lang.cobol.20140612.mbox.gz` | 2003-06 onward | Different snapshot but starts later — wider gap |
| `archive.org/usenet-dejanews` | "comm.*" community forums only | No `comp.*` content |
| [UTZOO Wiseman archive](https://archive.org/details/utzoo-wiseman-usenet-archive) | 1981–1991 | Ends before our gap |
| Eternal September (free NNTP) | 90 days retention for non-Big8 | Far too short |
| NewsDemon / Easynews (paid NNTP) | ~17–20 years | Reaches back to ~2005, not 1995 |
| [Narkive](https://comp.lang.cobol.narkive.com/) | Unverified (503 on probe) | Likely mirrors current Usenet |
| [Google Groups](https://groups.google.com/g/comp.lang.cobol) | 1995+ verified | Full content but no enumeration API |
| **[UsenetArchives.com](https://usenetarchives.com/threads.php?id=comp.lang.cobol&y=1996&r=0&p=1)** | **1994+ complete** | **Best fill source** |

### UsenetArchives.com coverage and dedupe yield

Walked all index pages and matched root Message-IDs against our existing archive:

| Year | UA threads | New after dedupe |
|---|---:|---:|
| 1994 (Nov 10 – Dec 31) | 133 | 107 (pre-Nov-30 + post-Dec-16 gap) |
| 1995 | 1,285 | 1,285 |
| 1996 | 1,953 | 1,953 |
| 1997 | 2,707 | 2,707 |
| 1998 | 3,227 | 2,025 (Jan 2 – Jun 22 + boundary) |
| 2013 | 131 | 59 (post-snapshot tail, Jun 12 onward) |
| 2014–2022 | 378 | 378 |
| **Total** | **9,814** | **8,514** |

UA.com has nothing pre-1994 (their earliest year for this group) and nothing post-2022. The mid-1990s gap and the post-snapshot tail are filled by [`scrape_gap.py`](../scrape_gap.py); fetched threads carry `X-Source: usenetarchives.com` in the mbox so downstream code can tell them apart.

Thread URL: `view.php?id=comp.lang.cobol&mid=<urlsafe-base64-message-id>`. JS-rendered (DataTables), requires Playwright. Age gate bypasses via a JS form submit. Robots.txt allows `view.php` with `Crawl-delay: 10` for AI crawlers; at that rate the full run is ~24 h wall-clock, ~7 h at a polite 3 s delay.

### Data fidelity caveats in UA-sourced threads

UA.com publishes a curated, privacy-munged view of historical Usenet — not a raw mbox dump. The 8,500 supplementary threads have several known gaps relative to the Giganews source. For comparison, any post-1998 [thread](threads/) shows what full-fidelity records look like.

**Authorship — stripped or truncated.**

| Field | Giganews source | UA.com source |
|---|---|---|
| Author email | preserved (`john@wexfordpress.com`) | stripped — replaced with synthetic `ua-author-{id}@usenetarchives.gap` |
| Author display name | preserved | truncated email-local-part forms (`im...`, `rtw...`); multi-word real names kept verbatim (`david m. martin`) |

UA's `X-UA-AuthorId` carries a stable numeric ID, so an author's posts merge correctly *within* the gap period. Bridging those UA-gap entries to the same person's Giganews-period entry is harder, since the truncated names normalize differently. A curated map (`UA_AUTHOR_NAMES` in [authors.py](../authors.py)) reunites the highest-traffic posters: Pete Dashwood, Bob Wolfe, Richard Plinston, Randall Bart, and William "Bill" Lynch now appear as single entries spanning both eras. Authors whose Giganews identity is *itself* fragmented can't be fully reunited this way — DocDwarf, for instance, posted with an empty display name from `panix.com` and `clark.net` (so those entries are keyed by email, not name) and as "the goobers" from `erols.com`; the bridge only consolidates his UA-gap entries with each other. Lower-traffic UA authors not yet in the map may still show as two separate entries.

**Message bodies — partial obfuscation.**

Inline emails and Message-IDs quoted in reply bodies are masked with `··` (U+00B7 MIDDLE DOT, twice):

```
original:  In article <4dan6v$t8p@usenet.kornet.nm.kr>, imuk@sobun.kornet.nm.kr says...
UA shows:  In article <4dan6v$t.··.@use··m.kr>, im··.@sob··m.kr says...
```

Subject lines, prose, signatures, sign-offs, and external URLs are unmunged. Names inside quoted attribution lines — `(Bob Wolfe)`, `(Phil Paxton)`, `Lim Uk (kornet) wrote:` — survive verbatim and often reveal real names the `From:` header has hidden.

**Threading — reconstructed, not preserved.**

| Header | Giganews source | UA.com source |
|---|---|---|
| Thread-root Message-ID | real | real (base64-decoded from URL `mid=` param) |
| Reply Message-ID | real | synthesized `<gap-{md5(root)}-pN@usenetarchives.gap>` |
| References / In-Reply-To | real headers | reconstructed from UA's per-post `data-depth` and display order |

Parent/child relationships are correct in shape; reply Message-IDs are local to this archive and never match the wider Usenet record.

**Timestamps — date precision for pre-2000.**

Gap-era UA posts arrive with `HH:00 UTC` regardless of real time. The scraper adds the post number as a seconds offset (`19:00:01`, `19:00:02`, …) so within-thread reply order survives sorting. Post-2000 UA timestamps have real `HH:MM` precision.

**Other artifacts.**

- UA's quote-prefix character is `›` (U+203A), not `>`. Quote-elision in `clean_body()` and the spam filter's `_non_quoted()` key on `>` only, so UA-sourced replies render with longer visible quote blocks. Cosmetic.
- Some old messages show double-encoded Unicode in UA's stored copy (`Zürich` → `ZÃ¼rich`, `who'll` → `whoï¿½ll`). Passed through unmodified.
- A handful of threads use a Google-Groups-style 11-char conversation ID in place of a real Message-ID (their original was lost during UA's import). The scraper wraps these as `<ua-fallback-{id}@usenetarchives.gap>` to keep them addressable.

## Layout

- One file per thread under [`threads/`](threads/) — filename is `<anchor>.md` where the anchor is `t-<10-hex>` (md5 of the root Message-ID, truncated).
- Each thread file contains the entire conversation in depth-first reply order, with sender / date / Message-ID / In-Reply-To / References preserved per message.
- The indexes above are the entry points — they cross-reference every thread by topic, year, author, and subject.
