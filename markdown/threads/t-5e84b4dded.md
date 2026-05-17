[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL programs compiling & running slower on CMOS processor?

_7 messages · 5 participants · 1997-03_

---

### COBOL programs compiling & running slower on CMOS processor?

- **From:** "tus..." <ua-author-17073394@usenetarchives.gap>
- **Date:** 1997-03-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3339a648.1805124@news.mindspring.com>`

```

Has anyone heard anything about COBOL programs compiling and/or
running slower on the new CMOS processor? Is this true, and if so,
maybe someone can enlighten me?

We are currently in the process of installing a new Enterprise 2000
CMOS processor, and one of IBM's competitors made this statement to
our VP of I/S.

Is this fact or fiction?

Whatch a know?



Brian R. Tusler
Martin Marietta Materials ~~~
2710 Wycliff RD. \\~ ~//
Raleigh, NC 27607 "Hang in there!" ( @ @ )
|--oOOo-(_)-oOOo--|
Tus··.@min··g.com
VM/ESA 1.2-2.2
VSE/ESA 1.3.5-2.2
```

#### ↳ Re: COBOL programs compiling & running slower on CMOS processor?

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-03-26T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5e84b4dded-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3339a648.1805124@news.mindspring.com>`
- **References:** `<3339a648.1805124@news.mindspring.com>`

```



Brian R. Tusler wrote in article
<333··.@new··g.com>...
› Has anyone heard anything about COBOL programs compiling and/or
› running slower on the new CMOS processor? Is this true, and if so,
› maybe someone can enlighten me?
Brian .... This is not a COBOL question at all, it's a question of single
.vs. multi-processor capability .... At the simplest level assume that your
have a uni-processor running at 20MIPS, if one only one program is running
then that program (I don't care what it's programmed in) basically gets the
full 20MIPS of processor cycles ... Now let's say you replace the 20MIPs
uni-processor with a 30MIPS 3-way CMOS processor and run the same
program...guess what, that program only has about 10MIPS available for its
processing (i.e. 30MIPS / 3processors) ... Any one program can only exploit
the services of the fastest single engine available ... Where the
multi-engines come into benefit is if your running concurrent processes
which can simultaneously exploit individual engines ... In your
environment, your VSE guest could exploit and engine, while your CMS users
exploit others ... Bottom line is that for sequentially dependent workloads
you need each engine to be at least as fast as your current engine and
possible then some .... Please reference IBM's VSE homepage for more
information.
```

#### ↳ Re: COBOL programs compiling & running slower on CMOS processor?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-03-26T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5e84b4dded-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3339a648.1805124@news.mindspring.com>`
- **References:** `<3339a648.1805124@news.mindspring.com>`

```

"It Depends".....

IBM has at least 4 different CMOS based systems on the street.

The slowest engine is the P/390, then the original CMOS /390, then the next CMOS/390 then the most current CMOS/390. Sorry, no model numbers in front of me.

Bipolar 308x, 309x, 902x, etc,etc, machines have individual engines which may (especially the later machines) be faster than individual engines in CMOS technology. The latest CMOS systems probably about equal the best of the bipolar technology in raw speed.

But..... the maximum number of engines has increased. Biggest 902x was an 8 engine machine (as I recall). CMOS allows up to 12 ways (as I recall), with sysplex allowing many more within a sysplex. So.... the realistic capacity of the sysplex is much larger than a single machine could accomplish before.

As for COBOL programs compiling and running slower on CMOS processor... yes and no... Yup on my OS/390 P/390 system the billed out (by SMF) CPU time is perhaps double what it is on a 3090 600J. But the latest CMOS (3rd version) processor engine will likely bill significantly less CPU time for running the same program even on a 9021 based system.

Generic problem of "COBOL is Slower" NOPE. Could it hapen - yup, especially when going from a highly tuned to an untuned system, but realistically NOPE.

Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

#### ↳ Re: COBOL programs compiling & running slower on CMOS processor?

- **From:** "tus..." <ua-author-17073394@usenetarchives.gap>
- **Date:** 1997-03-26T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5e84b4dded-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3339a648.1805124@news.mindspring.com>`
- **References:** `<3339a648.1805124@news.mindspring.com>`

```


Has anyone heard anything about COBOL programs compiling and/or
running slower on the new CMOS processor? Is this true, and if so,
maybe someone can enlighten me?

We are currently in the process of installing a new Enterprise 2000
CMOS processor, and one of IBM's competitors made this statement to
our VP of I/S.

Is this fact or fiction?

This question is based upon the migration from a single (non CMOS)
processor (BARE BONE), to one of IBM's new Multiprise 2003 CMOS single
engine box (BARE BONE), with the exact same mip rating. Forget about
the tuning factor.

The question is not a "What IF" question.

"Just the facts please", if there are any!





Brian R. Tusler
Martin Marietta Materials ~~~
2710 Wycliff RD. \\~ ~//
Raleigh, NC 27607 "Hang in there!" ( @ @ )
|--oOOo-(_)-oOOo--|
Tus··.@min··g.com
VM/ESA 1.2-2.2
VSE/ESA 1.3.5-2.2
```

##### ↳ ↳ Re: COBOL programs compiling & running slower on CMOS processor?

- **From:** "john mckown" <ua-author-1779298@usenetarchives.gap>
- **Date:** 1997-03-27T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5e84b4dded-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5e84b4dded-p4@usenetarchives.gap>`
- **References:** `<3339a648.1805124@news.mindspring.com> <gap-5e84b4dded-p4@usenetarchives.gap>`

```

Brian,
There is a Washington System Center flash (WSC Flash 9608) that details
some of the performance degradation experienced by people using COBOL on
the CMOS processors. In IBMLink, this is Item G023604. I cannot attach the
article because it plainly says that it is copyrighted. It does reference a
Web page: http://www.software.ibm.com/ad/cobol/cobol.htm , but I looked
there and it doesn't say anything.

The basic info is that COBOL program that use Subscripting (instead of
Indexing), or do a lot of data type conversions, may not run as fast as
expected. They recommend using the TRUNC(STD) or TRUNC(OPT) instead of
TRUNC(BIN). Also use indexes instead of subscripts for tables. From other
things that I vaguely remember hearing, the CVB (convert PACKED to BINARY)
and the CVD (convert BINARY to PACKED) instructions on the CMOS processors
are VERY slow. The following shows some of the results posted in the flash:

Table using subscripts

ES/9000-972 ES/9672-E04

TRUNC=BIN 6 seconds 45 seconds
TRUNC=STD 4 seconds 18 seconds
TRUNC=OPT 3 seconds 15 seconds

Table using indexes

ES/9000-972 ES/9672-E04

TRUNC=BIN 2 seconds 11 seconds
TRUNC=STD 2 seconds 11 seconds
TRUNC=OPT 2 seconds 11 seconds

Hope this helps - get hold of the WSC flash for more info.

Brian R. Tusler wrote in article
<333··.@new··g.com>...
› 
› Has anyone heard anything about COBOL programs compiling and/or
…[30 more quoted lines elided]…
›
```

#### ↳ Re: COBOL programs compiling & running slower on CMOS processor?

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1997-03-27T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5e84b4dded-p6@usenetarchives.gap>`
- **In-Reply-To:** `<3339a648.1805124@news.mindspring.com>`
- **References:** `<3339a648.1805124@news.mindspring.com>`

```

The first thing to check is the assumed MIP rate of each CMOS engine versus
each processor in your current box. If the CMOS processor is as fast as the
previous processor or faster, the compiles should take roughly the same
amount of time or be faster depending on the relative MIP rate (and a few
other arcane factors). COBOL II and COBOL for MVS and VM programs compiled
using the TRUNC(BIN) option that do a noticeable amount of binary arithmetic
(Add 1 to BINARY-FIELD, etc. where BINARY-FIELD is PIC S9(4) BINARY or COMP)
will be slower because the field is converted to decimal for arithmetic and
back. Its even worse with multiple BINARY operands. The CVB and CVD
instructions are much slower. Packed arithmetic in general may also take
more cycles than on your current box although not as badly. I think that the
CVB and CVD instructions were assumed to be infrequently used so they lost
out in the optimization process to others presumed more important.

› Has anyone heard anything about COBOL programs compiling and/or  
› running slower on the new CMOS processor?  Is this true, and if so,  
…[20 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at mor··.@nbn··b.ca
```

#### ↳ Re: COBOL programs compiling & running slower on CMOS processor?

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1997-03-27T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5e84b4dded-p7@usenetarchives.gap>`
- **In-Reply-To:** `<3339a648.1805124@news.mindspring.com>`
- **References:** `<3339a648.1805124@news.mindspring.com>`

```

The first thing to check is the assumed MIP rate of each CMOS engine versus
each processor in your current box. If the CMOS processor is as fast as the
previous processor or faster, the compiles should take roughly the same
amount of time or be faster depending on the relative MIP rate (and a few
other arcane factors). COBOL II and COBOL for MVS and VM programs compiled
using the TRUNC(BIN) option that do a noticeable amount of binary arithmetic
(Add 1 to BINARY-FIELD, etc. where BINARY-FIELD is PIC S9(4) BINARY or COMP)
will be slower because the field is converted to decimal for arithmetic and
back. Its even worse with multiple BINARY operands. The CVB and CVD
instructions are much slower. Packed arithmetic in general may also take
more cycles than on your current box although not as badly. I think that the
CVB and CVD instructions were assumed to be infrequently used so they lost
out in the optimization process to others presumed more important.

› Has anyone heard anything about COBOL programs compiling and/or 
› running slower on the new CMOS processor?  Is this true, and if so, 
…[20 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at mor··.@nbn··b.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
