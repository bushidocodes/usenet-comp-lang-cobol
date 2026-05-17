[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DOS/WINDOWS PRINTING

_2 messages · 2 participants · 1996-10_

---

### DOS/WINDOWS PRINTING

- **From:** "rigg..." <ua-author-1138336@usenetarchives.gap>
- **Date:** 1996-10-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<540b4i$dpl@newsbf02.news.aol.com>`

```

I'm new to DOS/Windows cobol. (UNIX only up to this point). I know how
to
print in UNIX, but how do I call a print routine (lp -d in UNIX) from Dos
or windows?
Right now I'm writing the file to disk, then having to use another program
to print
the file. Are there drivers available to use the laser printers? I'm
using the
MF Visual Cobol.

Thanks in advance

Bill Riggs
CONCO CEMENT CO.
It's real hard here!
```

#### ↳ Re: DOS/WINDOWS PRINTING

- **From:** "gbr..." <ua-author-17086232@usenetarchives.gap>
- **Date:** 1996-10-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5cdcc6d472-p2@usenetarchives.gap>`
- **In-Reply-To:** `<540b4i$dpl@newsbf02.news.aol.com>`
- **References:** `<540b4i$dpl@newsbf02.news.aol.com>`

```

In Article ,
RiggsBill wrote:
› how do I call a print routine (lp -d in UNIX) from Dos
› or windows?

In MS-DOS, there is a defined API for queueing print requests to the PRINT
command. I wrote one in C about 5 years ago, so I know it can be done. You
need to start the PRINT command before starting your program, and there are
limitations as to how many spool files you can put in the queue (max 10),
but your program can monitor what's in the queue and determine when another
request can be inserted. PRINT will only start to print a file after your
program has written and closed it, so you cannot just send print lines to
it via pipe. Thus, it is no where near as flexible as the UNIX lpr/lpd
approach, but then again, MS-DOS makes a crummy substitute for UNIX to
begin with.

In MS-Windows, it's more flexible, robust and complicated, and depending on
the level of control you want, it's different between Win3.x and Win95. You
should spend some time looking at how print support is implemented
(especially drivers and fonts) in some good book or perhaps the MSDN CD-ROM
library.

Good Luck,

Glynn
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
