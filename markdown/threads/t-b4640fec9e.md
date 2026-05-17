[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VS COBOL II - CICS on IBM ESA question(s)

_6 messages · 6 participants · 1997-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### VS COBOL II - CICS on IBM ESA question(s)

- **From:** "cal..." <ua-author-584395@usenetarchives.gap>
- **Date:** 1997-02-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970213031200.WAA26128@ladder01.news.aol.com>`

```

I'm trying to write a COBOL driver for a COBOL program that receives
pointers via a CICS COMMAREA to a Request Data Area, and uses a CICS
GETMAIN to assign an output area with a SET to a pointer in the COMMAREA
to give the response to its caller. Only thing is, its a C language
caller.

If I try to drive it with a COBOL program, I need to be able to SET
ADDRESS OF (data-area) to a pointer-value. As far as the I can tell from
the manuals, this is only possible if the data-area is in LINKAGE. But, as
a driver, my program may have no LINKAGE... or may it?

I doubt this is clear enough for intelligent response, but if the puzzle
is interesting ask me what you will. I'll try a LINKAGE SECTION, and this
may work, but if you've been down this path, or if you know (or intuit)
more about COBOL than its manual writers, let's talk. I love a good
puzzle, but my timeframes are short...
```

#### ↳ Re: VS COBOL II - CICS on IBM ESA question(s)

- **From:** "mikehutchinson" <ua-author-17071774@usenetarchives.gap>
- **Date:** 1997-02-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b4640fec9e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970213031200.WAA26128@ladder01.news.aol.com>`
- **References:** `<19970213031200.WAA26128@ladder01.news.aol.com>`

```

Calpox3 wrote:
› 
› I'm trying to write a COBOL driver for a COBOL program that receives
…[14 more quoted lines elided]…
› puzzle, but my timeframes are short...
On an IBM mainframe, you can avoid the linkage section restriction as
follows by creating a perverse little subprogram:
IDENTIFICATION DIVISION.
PROGRAM-ID. OUTRMOST.
...
WORKING STORAGE.
01 FIELD-NEEDING-ADDRESSABILITY pic x(...).
01 PNTR-TO-FIELD-NEEDING-ADDRBIL pointer.
PROCEDURE DIVISION.
1000-MAINLINE.
call 'setaddr' using FIELD-NEEDING-ADDRESSABILITY
PNTR-TO-FIELD-NEEDING-ADDRBIL.
...
IDENTIFICATION DIVISION.
PROGRAM-ID. SETADDR.
DATA DIVISION.
LINKAGE SECTION.
01 data-area pic x.
01 data-area-pntr pointer.
PROCEDURE DIVISION USING DATA-AREA DATA-AREA-PNTR.
SET DATA-AREA-PNTR to ADDRESS of DATA-AREA.
END program setaddr.
END program outrmost.

This works for us. Thanks to Stephen Thomas, one of the sharpest
coworkers I've ever had the pleasure to work with...
```

##### ↳ ↳ Re: VS COBOL II - CICS on IBM ESA question(s)

- **From:** "ron voyles" <ua-author-17072685@usenetarchives.gap>
- **Date:** 1997-02-12T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b4640fec9e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b4640fec9e-p2@usenetarchives.gap>`
- **References:** `<19970213031200.WAA26128@ladder01.news.aol.com> <gap-b4640fec9e-p2@usenetarchives.gap>`

```

MikeHutchinson wrote:
› 
› Calpox3 wrote:
…[42 more quoted lines elided]…
› coworkers I've ever had the pleasure to work with...

A related question. Has anyone ever heard an explaination as to why the
SET TO ADDRESS OF construct does not allow us to set the
pointer to the address of an item in Working-Storage? This seems to only
be a restriction on IBM COBOL II. MicroFocus's PC and unix compilers
allow this to happen.

Regards,

Ron Voyles
```

#### ↳ Re: VS COBOL II - CICS on IBM ESA question(s)

- **From:** "aa..." <ua-author-462541@usenetarchives.gap>
- **Date:** 1997-02-12T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b4640fec9e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19970213031200.WAA26128@ladder01.news.aol.com>`
- **References:** `<19970213031200.WAA26128@ladder01.news.aol.com>`

```


Calpox3 (cal··.@a··.com) writes:
› I'm trying to write a COBOL driver for a COBOL program that receives
› pointers via a CICS COMMAREA to a Request Data Area, and uses a CICS
…[8 more quoted lines elided]…
› 
Not initially (I don't think so anyhow). But if you do a return tranid with a LINKAGE section
as soon as you come into the program (and are sure you're supposed to be there), you can build
yourself a LINKAGE section.

› I doubt this is clear enough for intelligent response, but if the puzzle
› is interesting ask me what you will. I'll try a LINKAGE SECTION, and this
› may work, but if you've been down this path, or if you know (or intuit)
› more about COBOL than its manual writers, let's talk. I love a good
› puzzle, but my timeframes are short...

Let me know how it goes...

Mike Wolff
```

#### ↳ Re: VS COBOL II - CICS on IBM ESA question(s)

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-02-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b4640fec9e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19970213031200.WAA26128@ladder01.news.aol.com>`
- **References:** `<19970213031200.WAA26128@ladder01.news.aol.com>`

```

Calpox3 wrote:
› 
› I'm trying to write a COBOL driver for a COBOL program that receives
…[14 more quoted lines elided]…
› puzzle, but my timeframes are short...

Any CICS COBOL program can have a linkage section. If your program receives
the address of a piece of storage from another program, the only way you can
access that area is to define it as a Linkage section record in your program,
and SET ADDRESS OF linkage-section-record TO pointer. You will need to know
the length of that area ahead of time, so you don't walk over the end of it
and create a storage violation. It would help if the program that
calls your program passes the length of the storage area in the DFHCOMMAREA
as well as the pointer to it. Or you could design the application so it uses
a fixed-size area and always expects it to be that size.

Your program can do a CICS GETMAIN to allocate another piece of storage. You
can pass a pointer to that area back to your calling program through the
COMMAREA. You do not need to establish addressability to the GETMAIN'ed area
in your program, unless you need to actually read or modify it. If you do
need to establish addressability to the area you GETMAIN'ed, you have to
define it as a linkage section record and do the SET ADDRESS command.

You may already be aware that when your CICS task terminates, CICS will
FREEMAIN all the storage areas associated with your task. If you're trying
to share memory between two tasks, the storage could get freed by the
terminating task while the other task is still trying to use it. That can
cause some problems. On the other hand, if you have a long-running task and
you GETMAIN in a loop without doing FREEMAIN, you can eventually kill CICS by
going short-on-storage.

I don't know if this helps you. Managing memory in CICS can get a little
tricky at times. I know several techniques that work well, but the specific
choice will depend on exactly what you want to do, and I'm not sure that I
have understood your requirements.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: VS COBOL II - CICS on IBM ESA question(s)

- **From:** "fr..." <ua-author-16633589@usenetarchives.gap>
- **Date:** 1997-02-14T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b4640fec9e-p6@usenetarchives.gap>`
- **In-Reply-To:** `<19970213031200.WAA26128@ladder01.news.aol.com>`
- **References:** `<19970213031200.WAA26128@ladder01.news.aol.com>`

```

In article <199··.@lad··l.com>, cal··.@a··.com (Calpox3) writes:
› I'm trying to write a COBOL driver for a COBOL program that receives
› pointers via a CICS COMMAREA to a Request Data Area, and uses a CICS
…[13 more quoted lines elided]…
› puzzle, but my timeframes are short...

The linkage section is essentially a "dummy section" - it describes relative
offsets between data items within each 01 data item. The compiler expects
01 linkage section items to have their address resolved at run time -- normally
this is done in subprograms with the "Procedure Division Using
linkage-data-item-1, linkage-data-item-2, ..." statement. When this happens
each linkage 01 item refers to an argument passed by the caller. The caller
actually only passes the address (of "by reference" items), which is why
discrepancies between callers and subprograms view of the arguments sometimes
differ.

Sooo... no reason (in Cobol II) that the address of a 01 linkage section data
item can't be set by the statement "SET ADDRESS OF data-item TO
pointer-data-item". And this will work fine, as long as references to the
data-item happen after this statement, and if the pointer-data-item actually
points to the expected structure. In fact there is an example in the IBM Cobol
Set AIX Programmer Guide, I assume a similar example is in the MVS version of
the book -- but I'm sure it will work fine. (In fact I think the assembles or C
type "usage pointer" variable were added to Cobol II for CICS getmains).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
