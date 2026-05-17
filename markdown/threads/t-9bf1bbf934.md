[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compatible text editor for UNIX vi editor

_6 messages · 6 participants · 1997-07_

---

### Compatible text editor for UNIX vi editor

- **From:** "jlewi..." <ua-author-4847145@usenetarchives.gap>
- **Date:** 1997-07-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970720001100.UAA23207@ladder02.news.aol.com>`

```

Warmest Salutations to this group,

I am looking for a text editor I can use at home on my PC to write COBOL
source code and take it to class and FTP it to a UNIX vi editor.
Everything I have tried has been adding control characters to the source
code. Please help.

I am new to this newsgroup and programming. I hope you won't mind if I
post some rather novice questions from time to time. Any help will be
greatly appreciated. You can e-mail your reply or I will check the
newsgroup.

John W. Lewis
```

#### ↳ Re: Compatible text editor for UNIX vi editor

- **From:** "steve wolfe" <ua-author-733217@usenetarchives.gap>
- **Date:** 1997-07-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bf1bbf934-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970720001100.UAA23207@ladder02.news.aol.com>`
- **References:** `<19970720001100.UAA23207@ladder02.news.aol.com>`

```

JLewis8756 wrote:
› 
› Warmest Salutations to this group,
…[11 more quoted lines elided]…
› John W. Lewis

You also might want to look into Mortice Kern Systems. They produce a
product called MKS Toolkit that gives you access to over 190 unix
programs under dos/windows, os2, win95, nt 3.51 and 4.0. Great product.
Includes VI, cpio, grep, tar, ps, perl, awk, the korn shell, you get the
point. You can get more info at
http://www.mks.com/solution/tk/spec_52.htm

Good luck.

Steve
*****************************************************************

            Support the Western Bigfoot Research effort
                         for information:
             http://www.teleport.com/‾caveman/wbs.html

prg··.@ep··x.net
url http://www.epix.net/‾prgsdw
*****************************************************************
```

##### ↳ ↳ Re: Compatible text editor for UNIX vi editor

- **From:** "bill h." <ua-author-1252963@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bf1bbf934-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9bf1bbf934-p2@usenetarchives.gap>`
- **References:** `<19970720001100.UAA23207@ladder02.news.aol.com> <gap-9bf1bbf934-p2@usenetarchives.gap>`

```

› JLewis8756 wrote:
›› 
…[5 more quoted lines elided]…
›› John W. Lewis

Hi John,

I'm not sure what it is your mean by control characters.
Are you refering to tabs, carriage returns and line feeds,
or something in front of each line?
If you e-mail me and clarify this, I may have something
that can help.

Bill H.
```

#### ↳ Re: Compatible text editor for UNIX vi editor

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-07-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bf1bbf934-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19970720001100.UAA23207@ladder02.news.aol.com>`
- **References:** `<19970720001100.UAA23207@ladder02.news.aol.com>`

```

JLewis8756 wrote in article
<199··.@lad··l.com>...
› Warmest Salutations to this group,
› 
…[10 more quoted lines elided]…
› John W. Lewis

Try VEDIT from Greenview Data. (313) 996-1300.

Email to sup··.@ve··t.com or http://www.vedit.com

Remove the '-' from orion-data for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.
```

#### ↳ Re: Compatible text editor for UNIX vi editor

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bf1bbf934-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19970720001100.UAA23207@ladder02.news.aol.com>`
- **References:** `<19970720001100.UAA23207@ladder02.news.aol.com>`

```

JLewis8756 wrote:
› 
› I am looking for a text editor I can use at home on my PC to write COBOL
› source code and take it to class and FTP it to a UNIX vi editor.
› Everything I have tried has been adding control characters to the source
› code.  Please help.

I believe Watcom produces a vi editor for the PC that does not have this
problem.


Del.
```

#### ↳ Re: Compatible text editor for UNIX vi editor

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1997-07-20T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9bf1bbf934-p6@usenetarchives.gap>`
- **In-Reply-To:** `<19970720001100.UAA23207@ladder02.news.aol.com>`
- **References:** `<19970720001100.UAA23207@ladder02.news.aol.com>`

```

JLewis8756 wrote:
› 
› Warmest Salutations to this group,
…[4 more quoted lines elided]…
› code.  Please help.

John - if you're FTP'ing from a PC to the Unix machine, just ensure
that you FTP in "Text" mode (use the "ascii" command to FTP before
the "put" command). This will get FTP to automatically do the
translation for you.

Alternatively, when in "vi", type:

:1,$ s/.$//

This will get 'vi' to strip the last character in each line. A
slightly safer version is to type where that period
is - this will make sure that only ctrl-M's at the end of a line are
stripped.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
