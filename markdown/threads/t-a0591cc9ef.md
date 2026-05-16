[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# REPRO VS DFSORT

_10 messages · 8 participants · 2003-09_

---

### REPRO VS DFSORT

- **From:** "KK" <KK@KK.com>
- **Date:** 2003-09-04T01:00:29+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f561e2d$1@shknews01>`

```
Could anyone tell me, what's the difference between them if I just want to
merge some QSAM files into one without doing any sorting? Thx.
```

#### ↳ Re: REPRO VS DFSORT

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-09-03T19:44:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bj5gaj$c8t$1@peabody.colorado.edu>`
- **References:** `<3f561e2d$1@shknews01>`

```

On  3-Sep-2003, "KK" <KK@KK.com> wrote:

> Could anyone tell me, what's the difference between them if I just want to
> merge some QSAM files into one without doing any sorting? Thx.

Merge or concatenate?
```

#### ↳ Re: REPRO VS DFSORT

- **From:** "Gonzo" <ckhamel1961@yahoo.com>
- **Date:** 2003-09-03T21:25:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p%s5b.1081$o57.424@newssvr24.news.prodigy.com>`
- **References:** `<3f561e2d$1@shknews01>`

```

"KK" <KK@KK.com> wrote:
> Could anyone tell me, what's the difference between them if I just want to
> merge some QSAM files into one without doing any sorting? Thx.

Strictly speaking, REPRO does not perform a "merge" process that I am aware
of. Merge would be a SORT function.

If you want to "concatenate" a bunch of QSAM files into a single file, then
I suppose either would do. My own personal preference is SORT, but that's
only because I have occasion to use it more. I don't have anything against
REPRO. Others might have some other preferences, or qualms about
performance.

Gonzo
```

##### ↳ ↳ Re: REPRO VS DFSORT

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-09-03T22:06:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com>`
- **References:** `<3f561e2d$1@shknews01> <p%s5b.1081$o57.424@newssvr24.news.prodigy.com>`

```
"Gonzo" <ckhamel1961@yahoo.com> wrote in message
news:p%s5b.1081$o57.424@newssvr24.news.prodigy.com...
>
> If you want to "concatenate" a bunch of QSAM files into a single file,
then
> I suppose either would do.

Well, if IDCAMS (REPRO) is 'a' and DFSORT/SYNCSORT is 'b' then

C) IEBGENER
D) Don't even bother, just concatenate 'em in the DD statement for the using
program (as you would for SYSUT1 with  IEBGENER)

MCM
```

###### ↳ ↳ ↳ Re: REPRO VS DFSORT

- **From:** "jce" <defaultuser@hotmail.com>
- **Date:** 2003-09-05T02:56:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QXS5b.9822$Mb2.383258@twister.tampabay.rr.com>`
- **References:** `<3f561e2d$1@shknews01> <p%s5b.1081$o57.424@newssvr24.news.prodigy.com> <hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com...
> "Gonzo" <ckhamel1961@yahoo.com> wrote in message
> news:p%s5b.1081$o57.424@newssvr24.news.prodigy.com...
> >

> C) IEBGENER
> D) Don't even bother, just concatenate 'em in the DD statement for the
using
> program (as you would for SYSUT1 with  IEBGENER)
Or ICEGENER which is part of dfsort and in cases where it is not setup will
default to IEBGENER
At least that is what I recall.

JCE
```

###### ↳ ↳ ↳ Re: REPRO VS DFSORT

_(reply depth: 4)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-09-05T13:04:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JR%5b.129990$3o3.9130571@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f561e2d$1@shknews01> <p%s5b.1081$o57.424@newssvr24.news.prodigy.com> <hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com> <QXS5b.9822$Mb2.383258@twister.tampabay.rr.com>`

```

"jce" <defaultuser@hotmail.com> wrote in message
news:QXS5b.9822$Mb2.383258@twister.tampabay.rr.com...
|
| "Michael Mattias" <michael.mattias@gte.net> wrote in message
…[9 more quoted lines elided]…
| Or ICEGENER which is part of dfsort and in cases where it is not setup
will
| default to IEBGENER
| At least that is what I recall.

I think it's the other way around: IEBGENER invokes ICEGENER.
```

###### ↳ ↳ ↳ Re: REPRO VS DFSORT

_(reply depth: 5)_

- **From:** Frank Yaeger <yaeger@us.ibm.com>
- **Date:** 2003-09-15T09:10:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F65E48F.2090902@us.ibm.com>`
- **References:** `<3f561e2d$1@shknews01> <p%s5b.1081$o57.424@newssvr24.news.prodigy.com> <hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com> <QXS5b.9822$Mb2.383258@twister.tampabay.rr.com> <JR%5b.129990$3o3.9130571@bgtnsc05-news.ops.worldnet.att.net>`

```
Harley wrote:

> I think it's the other way around: IEBGENER invokes ICEGENER.

No.  DFSORT's ICEGENER invokes IEBGENER when DFSORT copy can't be used.
For more information on DFSORT's ICEGENER, see:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ICECA109/9.2.18?SHELF=&DT=20020722140254
```

###### ↳ ↳ ↳ Re: REPRO VS DFSORT

_(reply depth: 6)_

- **From:** "Joel C. Ewing" <jREMOVEcCAPSewing@acm.org>
- **Date:** 2003-09-20T05:46:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SQRab.10735$BS5.9876@newsread4.news.pas.earthlink.net>`
- **In-Reply-To:** `<3F65E48F.2090902@us.ibm.com>`
- **References:** `<3f561e2d$1@shknews01> <p%s5b.1081$o57.424@newssvr24.news.prodigy.com> <hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com> <QXS5b.9822$Mb2.383258@twister.tampabay.rr.com> <JR%5b.129990$3o3.9130571@bgtnsc05-news.ops.worldnet.att.net> <3F65E48F.2090902@us.ibm.com>`

```
Frank Yaeger wrote:
> Harley wrote:
> 
…[7 more quoted lines elided]…
> 

Perhaps merely semantic confusion.

Assuming it's similar to Syncsort interfaces, a JCL reference to 
IEBGENER really invokes a "sort" module, which decides whether the real 
IBM IEBGENER must be used, and if so transfers control by some means to 
the "real" IEBGENER module/CSECT.  The crucial point from the 
application programmers viewpoint is that the JCL does still reference 
PGM=IEBGENER, so that use of the sort program for improved Copy 
performance is transparent to the JCL writer.  So, perhaps both answers 
are correct.  Invoking IEBGENER in JCL invokes a program in linklist 
known as IEBGENER, which really invokes some "sort" code, which 
conditionally transfers to the code previously (without sort in the 
picture) known as IEBGENER.

On our system IEBGENER is an alias for Syncsort's BetterGener module and 
is in a linklist library concatenated ahead of SYS1.LINKLIST, so it is 
invoked by default by JCL references to IEBGENER.  If necessary it calls 
IEBGENR, which is an alias for IBM's IEBGENER in SYS1.LINKLIST.
```

###### ↳ ↳ ↳ Re: REPRO VS DFSORT

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-09-20T11:40:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a1Xab.1039$Hd6.816385@newssvr28.news.prodigy.com>`
- **References:** `<3f561e2d$1@shknews01> <p%s5b.1081$o57.424@newssvr24.news.prodigy.com> <hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com> <QXS5b.9822$Mb2.383258@twister.tampabay.rr.com> <JR%5b.129990$3o3.9130571@bgtnsc05-news.ops.worldnet.att.net> <3F65E48F.2090902@us.ibm.com> <SQRab.10735$BS5.9876@newsread4.news.pas.earthlink.net>`

```
"Joel C. Ewing" <jREMOVEcCAPSewing@acm.org> wrote in message
news:SQRab.10735$BS5.9876@newsread4.news.pas.earthlink.net...
> Frank Yaeger wrote:
> > Harley wrote:
…[3 more quoted lines elided]…
> > For more information on DFSORT's ICEGENER, see:

Yes, but who's first?

MCM
```

###### ↳ ↳ ↳ Re: REPRO VS DFSORT

_(reply depth: 7)_

- **From:** Frank Yaeger <yaeger@us.ibm.com>
- **Date:** 2003-09-22T13:19:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F6F5950.7070605@us.ibm.com>`
- **References:** `<3f561e2d$1@shknews01> <p%s5b.1081$o57.424@newssvr24.news.prodigy.com> <hBt5b.18416$Ih1.7258087@newssrv26.news.prodigy.com> <QXS5b.9822$Mb2.383258@twister.tampabay.rr.com> <JR%5b.129990$3o3.9130571@bgtnsc05-news.ops.worldnet.att.net> <3F65E48F.2090902@us.ibm.com> <SQRab.10735$BS5.9876@newsread4.news.pas.earthlink.net>`

```
Joel C. Ewing wrote:
> Perhaps merely semantic confusion.
> 
…[15 more quoted lines elided]…
> IEBGENR, which is an alias for IBM's IEBGENER in SYS1.LINKLIST.

Yes, just semantic confusion.  For DFSORT, ICEGENER is called first 
either directly by PGM=ICEGENER, or by PGM=IEBGENER if the site has 
installed ICEGENER as a "replacement" for IEBGENER.  ICEGENER then usess 
DFSORT copy if possible, otherwise it calls IEBGENR which is an alias 
for the real IEBGENER.

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com
Specialties: ICETOOL, OUTFIL, Symbols, Migration
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
