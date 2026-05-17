# comp.lang.cobol Usenet Archive

Converted from mbox to Markdown. **140,279 messages** across **16,371 thread files**, one file per conversation.

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

### UsenetArchives.com gap-year coverage

| Year | Threads available |
|---|---|
| 1994 | 133 |
| 1995 | 1,285 |
| 1996 | 1,953 |
| 1997 | 2,707 |
| 1998 | 3,227 (we have Jun–Dec) |

Thread URL pattern: `view.php?id=comp.lang.cobol&mid=<base64-message-id>`. JS-rendered, requires browser automation (Playwright) to scrape. Site has an age gate that's trivially bypassed via JS form submit. Caveats: email addresses are spam-munged (`rbr··.@uv··g.com`); `Message-ID`/`References` headers are not reliably exposed, so threading metadata won't fully match this archive's existing structure.

Estimated scrape effort to fill 1995, 1996, 1997, and Jan–May 1998: ~7,200 threads at `Crawl-delay: 10` per their robots.txt → ~25 hours polite, several hours aggressive.

## Layout

- One file per thread under [`threads/`](threads/) — filename is `<anchor>.md` where the anchor is `t-<10-hex>` (md5 of the root Message-ID, truncated).
- Each thread file contains the entire conversation in depth-first reply order, with sender / date / Message-ID / In-Reply-To / References preserved per message.
- The indexes above are the entry points — they cross-reference every thread by topic, year, author, and subject.
