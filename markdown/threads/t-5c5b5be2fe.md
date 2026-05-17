[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Unix Data files vs DOS data files

_6 messages · 5 participants · 1996-12_

---

### Unix Data files vs DOS data files

- **From:** "byro..." <ua-author-17087254@usenetarchives.gap>
- **Date:** 1996-12-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59aice$qm1$1@perth.DIALix.oz.au>`

```

Help!
I have taken my Unix Microfocus Cobol programs and have them running
successfully under Windows 95 MF Cobol. However, when I copy my data
files from Unix to Windows 95, I can't read them.

Can someone educate me on the differences between the data file formats
and suggest a really easy way to just copy my data?

Grovelling in appreciation!
Jim
```

#### ↳ Re: Unix Data files vs DOS data files

- **From:** "tony heffner" <ua-author-6589464@usenetarchives.gap>
- **Date:** 1996-12-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c5b5be2fe-p2@usenetarchives.gap>`
- **In-Reply-To:** `<59aice$qm1$1@perth.DIALix.oz.au>`
- **References:** `<59aice$qm1$1@perth.DIALix.oz.au>`

```

Dave Parker wrote:
› 
› In article <59aice$qm1$1.··.@per··z.au> byr··.@per··z.au (Byronics Pty Ltd) writes:
…[13 more quoted lines elided]…
› Dave Parker                             dlp··.@dlp··0.com

On at least hp-ux tr will only substiture an equal number of characters,
not one
character for two. There are usually commands to do this, though. ON
SCO, I think
it is dos2unix (may be wrong on that). I know on hp, it is dos2ux.

Regards,

Tony Heffner
```

##### ↳ ↳ Re: Unix Data files vs DOS data files

- **From:** "jerr..." <ua-author-2158094@usenetarchives.gap>
- **Date:** 1996-12-18T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c5b5be2fe-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c5b5be2fe-p2@usenetarchives.gap>`
- **References:** `<59aice$qm1$1@perth.DIALix.oz.au> <gap-5c5b5be2fe-p2@usenetarchives.gap>`

```

We transfer files from SunOS to Windows95 to run on MF Cobol programs
all the time. When I'm on the SUN I run gunzip to do a UNIX unzip
of the selected file (example gunzip whatever.dat.gz), then run
zip -l whatever.zip whatever.dat while on UNIX. Then transfer the
files over to my WIN95 machine (the -l is critical). hope this helps.


On Thu, 19 Dec 1996 17:33:48 -0500, Tony Heffner
wrote:

› Dave Parker wrote:
›› 
…[24 more quoted lines elided]…
› Tony Heffner
```

##### ↳ ↳ Re: Unix Data files vs DOS data files

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1996-12-26T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c5b5be2fe-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5c5b5be2fe-p2@usenetarchives.gap>`
- **References:** `<59aice$qm1$1@perth.DIALix.oz.au> <gap-5c5b5be2fe-p2@usenetarchives.gap>`

```

Tony Heffner wrote:
› 
› Dave Parker wrote:
…[25 more quoted lines elided]…
› Tony Heffner

I don't have the manual here, but *believe* SCO unix is dtox (dos to
unix).

****************************************************************************
email  : prg··.@ep··x.net
url    : http://www.epix.net/~prgsdw
****************************************************************************
```

#### ↳ Re: Unix Data files vs DOS data files

- **From:** "tds..." <ua-author-12498061@usenetarchives.gap>
- **Date:** 1996-12-19T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c5b5be2fe-p5@usenetarchives.gap>`
- **In-Reply-To:** `<59aice$qm1$1@perth.DIALix.oz.au>`
- **References:** `<59aice$qm1$1@perth.DIALix.oz.au>`

```

In article , dlp··.@dlp··0.com (Dave Parker)
writes:

› In article <59aice$qm1$1.··.@per··z.au> byr··.@per··z.au 
› (Byronics Pty Ltd) 
…[12 more quoted lines elided]…
› delimiter (newline/carriage-return).

If you have PFE 0.06.002 (Programmer's File Editor) installed on the
Windows box, it can read/write both Unix and DOS formats. It's a nice
editor and is completely free (always a nice bonus).

Troy Smith
```

#### ↳ Re: Unix Data files vs DOS data files

- **From:** "tony heffner" <ua-author-6589464@usenetarchives.gap>
- **Date:** 1996-12-19T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5c5b5be2fe-p6@usenetarchives.gap>`
- **In-Reply-To:** `<59aice$qm1$1@perth.DIALix.oz.au>`
- **References:** `<59aice$qm1$1@perth.DIALix.oz.au>`

```

Byronics Pty Ltd wrote:
› 
› Help!
…[8 more quoted lines elided]…
› Jim

oh, something else. At least on HP-UX, there is a file named file.1
that contains the information about the different file types and how
data is stored internally for the UNIX platform. on hp-ux, it's either
/usr/lib/cobol/docs/file.1 or /opt/cobol/cobdir/docs/file.1

Regards,

Tony Heffner
hef··.@m··.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
