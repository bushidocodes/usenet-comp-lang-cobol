[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# $ortparm in syncsort to override a Cobol sort for year 2000 question

_2 messages · 2 participants · 1997-02_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`VSAM, files, sorting`](../topics.md#files)

---

### $ortparm in syncsort to override a Cobol sort for year 2000 question

- **From:** "harol..." <ua-author-989315@usenetarchives.gap>
- **Date:** 1997-02-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970212031300.WAA00340@ladder01.news.aol.com>`

```

Hi Cobol gurus:

Has anybody used the $ORTPARM IN SYNCSORT (version 3.6) ) to override
Cobol internal sorts?? I am working on a year 2000 compliance project and
the client (an East coast insurance company) does not wish to make program
changes for 6 position years (YYMMDD). The Cobol program has three
internal sorts with three output procedures.

I was hoping that I could use the $ortparm in the batch Jcl to override
each sort. No matter how I code the JCL, each of the internal sorts gets
overriden with the first sort override I code. I have used three separate
$ortparm cards with Y2C offsets, but it always uses the first override.

Syncsort tech support was no help... They didnt think it couls be done.

Any suggestions.

Thanks....

Harold G.
```

#### ↳ Re: $ortparm in syncsort to override a Cobol sort for year 2000 question

- **From:** "john mckown" <ua-author-1779298@usenetarchives.gap>
- **Date:** 1997-02-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c2d1a59f9f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970212031300.WAA00340@ladder01.news.aol.com>`
- **References:** `<19970212031300.WAA00340@ladder01.news.aol.com>`

```

Harold,
I don't know if you tried this, but it might work. Use THREE $ORTPARM dd
statements similiar to the following:

//$ORTPARM DD DISP=SHR,DSN=PARMLIB(OVRRIDE1),FREE=CLOSE
//$ORTPARM DD DISP=SHR,DSN=PARMLIB(OVRRIDE2),FREE=CLOSE
//$ORTPARM DD DISP=SHR,DSN=PARMLIB(OVRRIDE3)

Using the FREE=CLOSE *should* allow the first SORT to get its overrides
from the first $ORTPARM dd statement. Since I believe that SYNCSORT will
then CLOSE its input files, the FREE=CLOSE should dynamically de-allocate
that dd statement. That would leave the second $ORTPARM for the second SORT
verb. The same thing would happen with the second SORT, leaving the last
$ORTPARM for the last SORT verb.

You did say that you had used three separate $ORTPARM dd statements, so
maybe you have already tried this. But I often forget things like the
FREE=CLOSE myself, so I thought maybe you had as well. Hope this helps
some.

Haroldrick wrote in article
<199··.@lad··l.com>...
› Hi Cobol gurus:
› 
…[22 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
