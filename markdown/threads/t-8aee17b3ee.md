[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Realia & ansii.sys

_5 messages · 4 participants · 1997-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Realia & ansii.sys

- **From:** "bill h." <ua-author-1252963@usenetarchives.gap>
- **Date:** 1997-08-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33E99A2D.60A0@tht.net>`

```

I'm using an old(circa 1985) version of Realia COBOL
that required the ansii.sys file for screen handling.
Do the newer versions still require it & what version
do you have? Is it Win 3.1 and/or Win 95 compatible?
Thanks,
Bill H.
```

#### ↳ Re: Realia & ansii.sys

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1997-08-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8aee17b3ee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33E99A2D.60A0@tht.net>`
- **References:** `<33E99A2D.60A0@tht.net>`

```

Bill H. wrote:
› 
› I'm using an old(circa 1985) version of Realia COBOL
…[4 more quoted lines elided]…
› Bill H.


CA-Realia COBOL requires ANSI.SYS only if you wish to display output at
the DOS-level. It does not require ANSI.SYS when displaying at the
faster BIOS and memory-mapped levels. These options have existed since
at least version 3.0 and exist in the current versions. Refere to
DISPLAY-CONTROL and "alternate link modulse (DISPDOS) for more
information.

Version 4.2 and higher support WIN 3.1 applications. I believe the
version which supports WIN '95 and NT are still in beta, but may be
close for general availability. Note that none of the screen handling
questions have any relevance to Windows applications, only DOS
applications.

Hope this helps a bit,

Mike Dodas

(Remove NOSPAM! for e-mail replies)
```

#### ↳ Re: Realia & ansii.sys

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-08-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8aee17b3ee-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33E99A2D.60A0@tht.net>`
- **References:** `<33E99A2D.60A0@tht.net>`

```

"Bill H." wrote:

› I'm using an old(circa 1985) version of Realia COBOL
› that required the ansii.sys file for screen handling.
…[4 more quoted lines elided]…
› 
You can use ansi.sys, dos-calls, or machine level
Take your pick.

JR



and stir with a Runcible spoon...
```

##### ↳ ↳ Re: Realia & ansii.sys

- **From:** "bill h." <ua-author-1252963@usenetarchives.gap>
- **Date:** 1997-08-07T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8aee17b3ee-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8aee17b3ee-p3@usenetarchives.gap>`
- **References:** `<33E99A2D.60A0@tht.net> <gap-8aee17b3ee-p3@usenetarchives.gap>`

```

Jeff Raben wrote:
› 
› "Bill H."  wrote:
…[13 more quoted lines elided]…
› and stir with a Runcible spoon...

That's the problem J.R. I don't want to HAVE to use ansii.sys
just to send and receive data from the screen. I want to get
away from using it.
It always meant any apps I sold, I had to make sure that the
buyer had it in the path. Besides ansii.sys I think is owned
by MS not Realia, so it's not something you should ship with
your apps.
Bill H.
```

#### ↳ Re: Realia & ansii.sys

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1997-08-06T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8aee17b3ee-p5@usenetarchives.gap>`
- **In-Reply-To:** `<33E99A2D.60A0@tht.net>`
- **References:** `<33E99A2D.60A0@tht.net>`

```

"Bill H." wrote:

› I'm using an old(circa 1985) version of Realia COBOL
› that required the ansii.sys file for screen handling.
…[4 more quoted lines elided]…
› 

Bill:

What version of Realia COBOL do you have? Is it version 4.2 or later?
I believe that the compiler first supported the Windows 16 bit
environment with version 4.2.

We have also successfully executed version 4.2 16 bit Realia programs
in the 32 bit Windows environments, but they are running as 16 bit
programs, not 32 bit programs.


Bob Wolfe, flexus, rtw··.@FIL··s.com
Delete FILTER from my e-mail address to reply
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
