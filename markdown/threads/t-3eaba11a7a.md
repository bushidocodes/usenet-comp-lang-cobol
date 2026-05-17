[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NetExpress Distribution

_2 messages · 2 participants · 1998-02_

---

### NetExpress Distribution

- **From:** "bob..." <ua-author-47816@usenetarchives.gap>
- **Date:** 1998-02-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980220012400.UAA12975@ladder03.news.aol.com>`

```

Hi,

I am trying to move my program that i built with NetExpress from the computer
that has the NetExpress IDE to another computer that does not have the IDE. I
copy my program SPEDCHEK.EXE which is five OBJ files linked into an .EXE with
the shared runtime system. I also copy the CBLRTSS.DLL and MSVCRT.DLL files to
the second computer. On my NetExpress computer the program run fine. But when
i try to run the program on the second computer the program does not run. Are
there other files that need to be copied over ? On my NetExpress computer
these three files are the only files i have in the directory and the program
runs fine.

Thanks in advance for any help,

Bob Hennessey.
```

#### ↳ Re: NetExpress Distribution

- **From:** "gael wilson" <ua-author-6589191@usenetarchives.gap>
- **Date:** 1998-02-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3eaba11a7a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980220012400.UAA12975@ladder03.news.aol.com>`
- **References:** `<19980220012400.UAA12975@ladder03.news.aol.com>`

```

Bob,

When the NetExpress product is installed, various entries are created in
the registry to indicate where to look for files etc. It would appear that
something your app needs that is normally found in one of the NetExpress
directories is missing. I believe that the product documentation contains
information on which files and programs are required for different
functionality so the best thing would probably be to check through that.

One possibility that immediately springs to mind is that if your
application does character screen I/O you will also need CBLVIOS.DLL (or
CBLDWINS.DLL if the EXE was linked as graphical).

Bob7536 wrote in article
<199··.@lad··l.com>...
› Hi,
› 
…[21 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
