[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol II

_8 messages · 7 participants · 1998-07 → 1998-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Cobol II

- **From:** "l..." <ua-author-907007@usenetarchives.gap>
- **Date:** 1998-07-23T23:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35B7FB10.3A4C0773@nac.net>`

```
An old timer who is interested in Y2K stuff has a strange question.

What makes Cobol II different than "regular" Cobol?

LB
```

#### ↳ Re: Cobol II

- **From:** "chris" <ua-author-10487@usenetarchives.gap>
- **Date:** 1998-07-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-670deb9b4c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35B7FB10.3A4C0773@nac.net>`
- **References:** `<35B7FB10.3A4C0773@nac.net>`

```
There are very considerable differences between the COBOL 1974 and COBOL
1985 compilers. Lots of new options, some of them with far reaching
effects.


My experience being with MVS, this is restricted to information about IBM
platforms:
Math, strangely enough, is slower (based on changes made to the way
object code is built from assembly language).
Variable length files are different (in COBOL II, the JCL LRECL has to
account for the RDW, but the code can't; in COBOL, the figures in JCL and
code must be the same).
You can use seven dimensional arrays, instead of just three.
The list goes on and on.
Get a book about the COBOL II compiler and language differences, and
read it.
One good option is COBOL II: Programming Techniques, Efficiency
Considerations, and Debugging Techniques. From the J. Ranade IBM Series
published by McGraw-Hill. ISBN 0-07-006522-0 (again, this deals with MVS
platforms exclusively).


l.··.@bou··t.net wrote in message <35B··.@n··.net>...
› An old timer who is interested in Y2K stuff has a strange question.
›
› What makes Cobol II different than "regular" Cobol?
›
› LB
```

#### ↳ Re: Cobol II

- **From:** "sba..." <ua-author-1103371@usenetarchives.gap>
- **Date:** 1998-07-24T10:16:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-670deb9b4c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35B7FB10.3A4C0773@nac.net>`
- **References:** `<35B7FB10.3A4C0773@nac.net>`

```
In article <35B··.@n··.net>,
l.··.@bou··t.net wrote:
› An old timer who is interested in Y2K stuff has a strange question.
›
…[3 more quoted lines elided]…
›

Several new features such as: inline performs, evaluate clause, ability to
move a string within a field, disabling of "READY TRACE" and "EXHIBIT NAMED"
staements, and others I can't think of right now.

Oh yeah,
something about "above the line" vs "below the line processing.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

##### ↳ ↳ Re: Cobol II

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-07-24T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-670deb9b4c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-670deb9b4c-p3@usenetarchives.gap>`
- **References:** `<35B7FB10.3A4C0773@nac.net> <gap-670deb9b4c-p3@usenetarchives.gap>`

```
sba··.@my-··s.com wrote:
› 
› In article <35B··.@n··.net>,
…[13 more quoted lines elided]…
›  something about "above the line" vs "below the line processing.

And the lovely & talented "RENT" - lest we forget (i.e., it can generate
reentrant code).

Bill Lynch
```

###### ↳ ↳ ↳ Re: Cobol II

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-07-24T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-670deb9b4c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-670deb9b4c-p4@usenetarchives.gap>`
- **References:** `<35B7FB10.3A4C0773@nac.net> <gap-670deb9b4c-p3@usenetarchives.gap> <gap-670deb9b4c-p4@usenetarchives.gap>`

```
On Sat, 25 Jul 1998 00:40:39 -0400, Bill Lynch
wrote:

› sba··.@my-··s.com wrote:
›› 
…[19 more quoted lines elided]…
› Bill Lynch

Just to jump in briefly... the foundation of the difference is ANSI
85, whereas 'old cobol' was ANSI 74 -- and many using 'old cobol', aka
VS/COBOL, were using it at the ANSI 68 level. A lot happened in
software from 68 to 85 --

a reminder: cobol ii is considered out-of-date. if you're looking for
new reference material, look for cobol/370, cobol for mvs, or cobol
for os/390. these include the interim ansi standards on intrinsic
functions and also provide Y2K tools in the compiler.

also, that 'above the line' stuff is important. with many mainframes
now at the 2 gig memory level, it makes little sense to be generating
load modules that can access less than 1% of memory. 31-bit addressing
buys a lot for an application.

hope this helps.
david

David d.s··.@ix.··m.com
____________________________________
```

###### ↳ ↳ ↳ Re: Cobol II

_(reply depth: 4)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-07-24T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-670deb9b4c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-670deb9b4c-p5@usenetarchives.gap>`
- **References:** `<35B7FB10.3A4C0773@nac.net> <gap-670deb9b4c-p3@usenetarchives.gap> <gap-670deb9b4c-p4@usenetarchives.gap> <gap-670deb9b4c-p5@usenetarchives.gap>`

```
David wrote:
› 
› (snip)
…[23 more quoted lines elided]…
› david

Quite true, the current COBOL compiler for the MVS platform is IBM COBOL
for MVS & VM (I'm just starting to play with it). For my application the
benefits of 31-bit addressability & RENT were needed and apparent in our
CICS applications. However, it didn't make much difference in batch
because we aren't constrained by the 16 MB limit of 24-bit
addressability in batch. The default for COBOL II batch programs is
DATA(24) to maintain compatibility with the remaining OS/VS COBOL
programs and a few old Asm subroutines (which haven't been upgraded to
AMODE(31) & RMODE(ANY)). COBOL II called programs are compiled with
AMODE(31), as they might be called (dynamically) online as well as in
batch.

At first we didn't compile batch COBOL II programs with the RENT option,
but we switched about 2 years ago because the load modules are smaller
(sometimes a *lot*) so it saves us load library space (probably also a
little load time - probably not enough for anyone to care about). From
COBOL II and up you get the scope delimiters (no trivial change, IMHO),
plus from COBOL/370 & up you get the intrinsic functions.

My $0.02,
Bill Lynch
```

##### ↳ ↳ Re: Cobol II

- **From:** "ejon7" <ua-author-17074383@usenetarchives.gap>
- **Date:** 1998-08-07T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-670deb9b4c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-670deb9b4c-p3@usenetarchives.gap>`
- **References:** `<35B7FB10.3A4C0773@nac.net> <gap-670deb9b4c-p3@usenetarchives.gap>`

```
sba··.@my-··s.com wrote:
› 
› In article <35B··.@n··.net>,
…[13 more quoted lines elided]…
›  something about "above the line" vs "below the line processing.

COBOL II (aka the dress rehearsal for the OOP-debut of Great-grandson
of FLOW*MATIC(tm)...OO Cobol)

C2 puts forth the common constructs of other procedural and structured
languages, such as ALGOL, JOVIAL, Ada, Pascal, PL/1, etc. with
scope-terminators, inline procedure blocks (PERFORM/END-PERFORM),
and a nifty "case selector" (EVALUATE/END-EVALUATE), modified
referencing
allows pseudo-function equivalents of "Substring".

===============================================
Church of Orthdox, Latter-day Testifiers, Reformed
& Reorganized, Universal & Triumphant, Apocalyptic,
Modern-day Mysticism and Mythology
(services to be announced)
===============================================
```

#### ↳ Re: Cobol II

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-07-24T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-670deb9b4c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<35B7FB10.3A4C0773@nac.net>`
- **References:** `<35B7FB10.3A4C0773@nac.net>`

```
In article <35B··.@n··.net>, l.··.@bou··t.net writes:

› What makes Cobol II different than "regular" Cobol?

That depends on whose COBOL II you are referring to. If it is IBM's COBOL II,
it follows the '85 standard but without intrinsic functions. COBOL for MVS/VM
and COBOL for VSE are more recent ventages that also include the optional
intrinsic functions.

Mark A. Young
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
