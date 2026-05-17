[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL VS COBOLII

_3 messages · 3 participants · 1996-08 → 1996-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL VS COBOLII

- **From:** "jl..." <ua-author-17072453@usenetarchives.gap>
- **Date:** 1996-08-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0_0/0_0_227350b0@fidonet.org>`

```

Hello !

I am enrolled in a COBOLII class at the local
college, using Xedit on a VM-ESA mainframe. I
have seen many references to COBOL, but not
COBOLII. What is the difference?

Also, does anyone know of an inexpensive COBOLII
compiler/run time for a pc? I can get the
Visual Cobol for OS/2, but that is far more
than I need, both in pc requirements and price.


Have a nice day,
Joe
---
* Origin: (0:0/0)
```

#### ↳ Re: COBOL VS COBOLII

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-08-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dccb20159c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<0_0/0_0_227350b0@fidonet.org>`
- **References:** `<0_0/0_0_227350b0@fidonet.org>`

```

jl··.@pro··g.net wrote:
› Hello !
› 
…[14 more quoted lines elided]…
› * Origin:  (0:0/0)

COBOL II is just IBM's name for their ANSI-85 compliant COBOL compiler.
The COBOL II name was used just to distinguish it from their earlier
compiler, which was compatible with the 1968 and 1974 standard. For the
MVS operating system the old name was OS/VS COBOL for the old one, and
VS COBOL II for the ANSI-85 compatible compiler. It has now been
superseded by COBOL for MVS and VM (formerly called COBOL/370). COBOL
for for MVS and VM is identical to COBOL II, but includes the new
intrinsic functions and uses LE/370 (Language Environment 370), which is
a common set of runtime libraries for COBOL, PL/I, C, and assembler.

I got a nice COBOL compiler for PC DOS by buying a textbook titled
"COBOL: From Micro to Mainframe", by Robert T. Grauer and Carol Vazquez
Villar, and published by Prentice Hall in 1991, ISBN 0-13-140179-3. The
price was about $60. I used to have a 1-800 number to order it direct,
but I can't find it right now. The compiler, with examples, came on two
5-1/4" floppies, non-copy protected. You need to supply your own linkage
editor -- I used one from Microsoft QuickBasic 4.5 and it worked fine.

The compiler has some limitations. No program can have more than 500
lines of code, excluding comment lines. No file can be bigger than 64K
bytes. You can get around the first limitation by linking multiple
programs together, and you can get around the second limitation by using
the doscall library. Unfortunately, the only way to get documentation
on the doscall library is to get manuals for the full-blown Realia COBOL
compiler (that compiler costs about $800). The student compiler that
comes with the textbook is a smaller version of the full Realia compiler
and it supports both ANSI-74 and ANSI-85 COBOL dialects.

You can also get MicroFocus Personal COBOL, which is pretty inexpensive.
I think you can find it for less than $100. I don't have any personal
experience with it, but I hear it's a good product. If you look at other
posts in comp.lang.cobol you will see their address for their web page,
or just search for MicroFocus.

Good Luck!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: COBOL VS COBOLII

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-09-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dccb20159c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<0_0/0_0_227350b0@fidonet.org>`
- **References:** `<0_0/0_0_227350b0@fidonet.org>`

```

COBOL II - more preciesly VS COBOL II is a specific IBM implementation of
COBOL for the mainframe environment.

Depending on the release and compiler option setting, either a very
extended 1974 standard COBOL or a extended 1985 standard COBOL
implementation is provided.

The visual age COBOL is essentially the same compiler, ported to OS/2 (and
a win NT / win 95 version may also be out).

Micro Focus COBOL implements about the same variants of COBOL for various
platforms. The "student edition" of the MF product is available at a
quite low cost, and would probably be suitable. Note that MF has a large
number of compiler directives, many of which set up the product to match
the behavior of various IBM mainframe compiler / option combinations.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
