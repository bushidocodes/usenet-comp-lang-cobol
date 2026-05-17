[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RTS 170/230

_3 messages · 3 participants · 1998-07_

---

### RTS 170/230

- **From:** "map..." <ua-author-2578618@usenetarchives.gap>
- **Date:** 1998-07-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998071703001300.XAA02507@ladder01.news.aol.com>`

```
I am getting two run time error while running people soft programs in
a windows environment. (not a good idea, but that's the setup)
How can I track down these problems? Thank you.

1) RTS Load failure error.
Error Number: 170 (can't find program)
filename : ADIS (just like the example in the book)
Segment: Root

2) RTS Run Time Error
Error Number: 230 (floating point support module not found)
Segment: Root
```

#### ↳ Re: RTS 170/230

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-07-16T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8f1c6f3d6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1998071703001300.XAA02507@ladder01.news.aol.com>`
- **References:** `<1998071703001300.XAA02507@ladder01.news.aol.com>`

```
1) RTS Load failure error.
Error Number: 170 (can't find program)
filename : ADIS (just like the example in the book)
Segment: Root

This one is easy. ADIS is the accept/display module, and either
needs to be available (on path) or linked. Find ADIS.EXE and
put it on the path, or find ADIS.OBJ and link it in.
```

#### ↳ Re: RTS 170/230

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-07-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e8f1c6f3d6-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1998071703001300.XAA02507@ladder01.news.aol.com>`
- **References:** `<1998071703001300.XAA02507@ladder01.news.aol.com>`

```
In article <199··.@lad··l.com>, map··.@a··.com
says...
› 
›  1)  RTS Load failure error.
›       Error Number:   170   (can't find program)
›       filename : ADIS  (just like the example in the book)
›       Segment: Root

Easy. Can't find ADIS (the Accept/DISplay module). Depending on how the
application was built you'll need to have a UTILS.LBR in the same directory as
the application or pointed at by the COBDIR environment variable. eg. SET
COBDIR=C:\fred where c:\fred is a directory containing UTILS.LBR.

Potentially, the application could have had ADIS built into another library or
into an EXE, .DLE or .DLL. That may be trickier to find.

›
› 2) RTS Run Time Error
› Error Number: 230 (floating point support module not found)
› Segment: Root

Can't find COBFP87.DLE or .DLL. Similar problem to the above.

Shaun
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
