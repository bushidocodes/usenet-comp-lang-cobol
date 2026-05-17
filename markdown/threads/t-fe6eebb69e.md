[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol for MVS or Cobol/370?

_4 messages · 4 participants · 1997-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Cobol for MVS or Cobol/370?

- **From:** "mc4..." <ua-author-2196104@usenetarchives.gap>
- **Date:** 1997-02-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32f8e946.10803167@news.mclink.it>`

```

Could anybody tell me the main differences and opportunities of these
two languages?
I keep programming in the good old Cobol-II (but also in Cobol/VS,
Assembler, Rexx, ...) but I know that in a short time I've to
understand wich Cobol is the right one for me and for my Company (MVS
env.)
TIA to everybody


<100··.@com··e.com>
```

#### ↳ Re: Cobol for MVS or Cobol/370?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-02-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe6eebb69e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32f8e946.10803167@news.mclink.it>`
- **References:** `<32f8e946.10803167@news.mclink.it>`

```

COBOL / 370 - released in the 1991 time frame.

Essentialially the next release of VS COBOL II, with Intrinsic Functions
from the 1985 standard addendum added. Requires LE/370 for operation.

COBOL for MVS and VM - released in late 1995. A renamed release 2 of
COBOL / 370. Everything that was in COBOL / 370 plus IBM's flavor of OO
COBOL (as vendor extension) and better interfaces with 'c'. Requires
LE/370 1.5. No migration headaches unless you are dealing with assembler
subroutines, or third party products that are very dependant on the
generated code structures.

The COBOL language supported by COBOL for MVS and VM is a proper superset
of that supported by COBOL / 370 - the OO stuff was added cleanly (well
maybe a new reserved word or two, but I seem to recall they were marked
reserved in COBOL / 370).

Here we have every IBM MVS COBOL compiler installed from OS/VS COBOL, thru
all releases of VS COBOL II, COBOL/370 and COBOL for MVS and VM. One
should be cautious about staying on COBOL/370 for too long, not sure where
it stands in termns of support cut-off. Of course, mega dittos for VS
COBOL II - only R4 is supported now.... Transition from COBOL/370 to
COBOL for MVS and VM is trivial. Of course that's our business, doing the
transitions, and providing hand holding and training support.

Most of the issues going forward from VS COBOL II are not language, but
are run-time confgiuration and mixed technology (i.e. assembler subs)
issues.



Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: Cobol for MVS or Cobol/370?

- **From:** "ar..." <ua-author-89056@usenetarchives.gap>
- **Date:** 1997-02-05T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe6eebb69e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32f8e946.10803167@news.mclink.it>`
- **References:** `<32f8e946.10803167@news.mclink.it>`

```


Sergio Sardo - Italy (mc4··.@mcl··k.it) writes:
› Could anybody tell me the main differences and opportunities of these
› two languages?
…[3 more quoted lines elided]…
› env.)

In 1995 our shop moved to VS COBOL II Release 4. We had previously
eliminated all OS/VS COBOL. The only snags we encountered were coding
errors that previous releases let you get away with. In COBOL II rel 4 we
found:
(a) you could not SET an INDEX value to zero - but you could SET it
to 1, then SET DOWN by 1
(b) "dead code," or code which will never be executed, is flagged by the
compiler
In 1996 we skipped COBOL/370 Rel 1 and went directly to COBOL for MVS & VM
Rel 2. We found only one instance where code had to be corrected:

Programmers were coding a single line with a period in area A (cols 8 thru
11). They called this a "structured period." COBOL II allowed this but
COBOL for MVS & VM wouldn't. All the periods had to be moved to area B.
```

#### ↳ Re: Cobol for MVS or Cobol/370?

- **From:** "john mckown" <ua-author-1779298@usenetarchives.gap>
- **Date:** 1997-02-05T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fe6eebb69e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32f8e946.10803167@news.mclink.it>`
- **References:** `<32f8e946.10803167@news.mclink.it>`

```

Sergio,
I do not know all the differences between COBOL II and COBOL/370. We do not
yet have COBOL/370. We just ordered it. However, I have been reading some
of the books. The single, biggest difference that I can see is that
COBOL/370 has object-oriented extentions. Another big difference that I can
see is that you can more easily mix different languages (C/370, ADA/370,
Fortran, PL/I). Also, if you use SOM (System Object Model), you can create
object oriented programs that can be in mixed languages as well. In fact,
using SOM, you can write a class in PL/I and then a subclass in COBOL, or
ASM and COBOL, or ???? and ?????. I have not seen anything in the manuals
that COBOL II can do that COBOL/370 cannot do. There are some syntax
differences when COBOL 2 allows you to "get away with" what I think should
be errors. From what I can see, COBOL/370 is closer to the ANSI/ISO
standard with fewer "holes" (aka IBM proprietary extentions). Another BIG
difference is the COST! COBOL/370 costs more than COBOL II. Oh, COBOL/370
has some new facilities in regards to four digit years (year 2000
processing). COBOL 2 does not have a "builtin" way to get a four digit
year. COBOL/370 does. COBOL/370 has a LOT of date manipulation functions. I
don't remember the syntax off hand, but you can take todays date (in year,
month, & day), convert it to an integer, add or subtract some value, then
convert it back to a year, month, day. All using "standard" COBOL, no
non-standard or in-house written subroutines.

Hope that's some help.

Sergio Sardo - Italy wrote in article
<32f··.@new··k.it>...
› Could anybody tell me the main differences and opportunities of these
› two languages?
…[8 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
