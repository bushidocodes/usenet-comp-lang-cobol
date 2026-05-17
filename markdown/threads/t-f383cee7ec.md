[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 88 Level Value clause...

_5 messages · 5 participants · 1998-04_

---

### 88 Level Value clause...

- **From:** "stephen sellars" <ua-author-17075261@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6hnfnc$b0e$1@news.ses.cio.eds.com>`

```

Hi,

Just a quick reality check on COBOL II syntax...can I do the following? I
don't have access to the mainframe compiler right now to confirm:

05 WS-DATE.
10 WS-YEAR PIC 9(02) VALUE 0.
88 VALID-YEAR VALUE 93 THRU 99,
00 THRU 49.

Do I need the comma after the 1st 'VALUE 93 THRU 99' ?

Thanks.

Stephen
```

#### ↳ Re: 88 Level Value clause...

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f383cee7ec-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6hnfnc$b0e$1@news.ses.cio.eds.com>`
- **References:** `<6hnfnc$b0e$1@news.ses.cio.eds.com>`

```

In article <6hnfnc$b0e$1.··.@new··s.com>,
Stephen Sellars wrote:
› Hi,
› 
…[8 more quoted lines elided]…
› Do I need the comma after the 1st 'VALUE 93 THRU 99' ?

I don't know about 'need' (I doubt it) but I always include one for
readability... I would also have used VALUES instead of VALUE for the same
reason.

DD
```

#### ↳ Re: 88 Level Value clause...

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f383cee7ec-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6hnfnc$b0e$1@news.ses.cio.eds.com>`
- **References:** `<6hnfnc$b0e$1@news.ses.cio.eds.com>`

```

I believe the current standard is that comma is never required, but in
all cases outside the PICTURE clause, comma is optional. Comma and
semicolon, immediately followed by a space, may be used anywhere a space
can be used as a separator.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove numbers from email id to respond)

Stephen Sellars wrote:
>Hi,
>
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: 88 Level Value clause...

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-04-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f383cee7ec-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f383cee7ec-p3@usenetarchives.gap>`
- **References:** `<6hnfnc$b0e$1@news.ses.cio.eds.com> <gap-f383cee7ec-p3@usenetarchives.gap>`

```

Judson McClendon wrote:
› 
› I believe the current standard is that comma is never required, but in
› all cases outside the PICTURE clause, comma is optional.  Comma and
› semicolon, immediately followed by a space, may be used anywhere a space
› can be used as a separator.

Not just the current standard, but all commas outside of PIC clauses
have been ignored since Cobol-68. Prior to that I believe commas were
ignored always, because there was no PIC clause.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net    Bar··.@wor··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \      Todd McCormick released after 12 day illegal incarceration
e    |\ for using Marinol w/ prescription: http://www.freecannabis.org
Y    |/     http://www.marijuanamagazine.com/toc/articles/toddfree.htm
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00  
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

#### ↳ Re: 88 Level Value clause...

- **From:** "vadim maslov" <ua-author-9434762@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f383cee7ec-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6hnfnc$b0e$1@news.ses.cio.eds.com>`
- **References:** `<6hnfnc$b0e$1@news.ses.cio.eds.com>`

```

Stephen Sellars wrote:
› 
› Hi,
…[9 more quoted lines elided]…
› Do I need the comma after the 1st 'VALUE 93 THRU 99' ?

You can put commas everywhere and nowhere.

That is, a compiler, the first thing it does is to break the program
text into character strings and separators. Comma is just another
space-like separator. It has no semantic or syntactic meaning
whatsoever.

Vadim Maslov
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
