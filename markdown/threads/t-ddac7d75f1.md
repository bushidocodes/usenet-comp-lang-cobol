[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What's the right IBM MVS compiler option?

_4 messages · 4 participants · 1996-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### What's the right IBM MVS compiler option?

- **From:** "gbr..." <ua-author-17086300@usenetarchives.gap>
- **Date:** 1996-01-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19960109142858.gbrooks@crystalball.com>`

```
In older versions of the IBM MVS COBOL compiler, I used to use the NOTRUNC
option. It was used to control how the compiler treated USAGE COMPUTATIONAL
data items. For example, when I coded

77 BINARY-HALFWORD PIC S9999 COMP.

the compiler generated a two-byte binary data item which could contain a
decimal value in the range -32767 (hex 8000) to +32768 (hex 7FFF).

With the default compiler option TRUNC, the compiler generated extra code
whenever the data item was changed. The extra code was there to assure that
no decimal value greater than +9999 or less than -9999 was ever stored in
the data item even though much larger values were possible. Using the
NOTRUNC option, the compiler did not generate this extra code.

We have switched to using COBOL II now, and I get a W-level warning when I
use the NOTRUNC option. It says that NOTRUNC is not supported and it is
using TRUNC(OPT) instead. My questions are: what other suboptions are
available for the TRUNC() directive? What does OPT do? Will it do what the
old NOTRUNC option does?
```

#### ↳ Re: What's the right IBM MVS compiler option?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-01-09T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddac7d75f1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19960109142858.gbrooks@crystalball.com>`
- **References:** `<19960109142858.gbrooks@crystalball.com>`

```
For recent VS COBOL II, COBOL/370 and COBOL for MVS and VM IBM mainframe
compilers - the closest match to OS/VS COBOL's (and even earlier IBM
mainframe COBOL's) NOTRUNC option is TRUNC(OPT).

Another optioin which exists in all but the earliest VS COBOL II products
is TRUNC(BIN).

TRUNC(BIN) was recommended for cases where values between 10,000 and
32,767 as well as -10,000 and -32,768 need to be accurately handed in
these late compilers.

TRUNC(OPT) has a rather soft definition - essentially that truncation
behavior is not standard, nor is it rigorously "full binary field size".


Generally speaking, TRUNC(BIN) is more expensive in CPU time and code
size. TRUNC(OPT) is usually acceptable for migrating applications from
OS/VS COBOL.

For a long time IBM recommended TRUNC(BIN) for all programs dealing with
CICS, DB2, FORTRAN, etc, etc, etc. Lately, the recommendation is that
TRUNC(OPT) should do and will provide better performance.

NOTRUNC became TRUNC(OPT) with VS COBOL II R3, when the option became
trinary instead of binary (as I recall... this was about 1986/7).

Hope this helps. More details can be found in the VS COBOL II R3 or later
Programmer's Guide, or the equivalent pubs for COBOL/370 or COBOL for MVS
and VM.
```

#### ↳ Re: What's the right IBM MVS compiler option?

- **From:** "mor..." <ua-author-4892761@usenetarchives.gap>
- **Date:** 1996-01-09T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddac7d75f1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19960109142858.gbrooks@crystalball.com>`
- **References:** `<19960109142858.gbrooks@crystalball.com>`

```
In response to your questions on the TRUNC options they are as
follows:
TRUNC(STD) - equivalent of TRUNC and follows the COBOL standard.
TRUNC(BIN) - despite the manual this should always be avoided since
it generates conversion to decimal for all binary
arithmetic operations. The newer manuals indicate
that in some circumstances it gives different results
from TRUNC(OPT) but normally you should use TRUNC(OPT)
The clearest difference in terms of actual result is
that if you display a PIC S9(8) BINARY/COMP field
TRUNC(BIN) will display 10 digits while TRUNC(OPT)
will only display 8 digits. Tests I have run with
both show that if you compute FIELD-BINARY = 900
million + 900 million + 900 million you get a
negative result with both TRUNC(OPT) and
TRUNC(BIN).
TRUNC(OPT) - Does arithmetic in Binary on BINARY/COMP fields and
doesn't truncate to picture. However the turkeys will
many times generate double precision adds when the
code adds two PIC S9(9) fields. I use TRUNC(OPT).

Clark F. Morris, Jr. - CFM Technical Programming Services.
Bridgetown, Nova Scotia Canada
cmo··.@fox··n.ca
on assignment in New Brunswick at
mor··.@nbn··b.ca
› In older versions of the IBM MVS COBOL compiler, I used to use the NOTRUNC
› option. It was used to control how the compiler treated USAGE COMPUTATIONAL
…[17 more quoted lines elided]…
› old NOTRUNC option does?
```

#### ↳ Re: What's the right IBM MVS compiler option?

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1996-01-10T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddac7d75f1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19960109142858.gbrooks@crystalball.com>`
- **References:** `<19960109142858.gbrooks@crystalball.com>`

```
The variations of TRUNC in VS COBOL II (Release 3.0 and higher),
COBOL/370, and COBOL for MVS & VM are:

TRUNC(STD) - exactly like old "TRUNC", i.e. truncation
always conforms to the PICTURE clause

TRUNC(BIN) - similar but not identical to old NOTRUNC. This
always allows for a data item to include any value that will fit
in the allocated storage. This has *lots* of run-time overhead
and should be avoided if possible - but does work with some CICS,
SQL, and PL/I "data" where the values are based on storage size
rather than PICTURE.

TRUNC(OPT) - "proprietary" (i.e., undocumented) rules for when
truncation does or does not occur. If your application only
supports data that matches the picture clause, then you REALLY
want to use this option which gives the best run-time
performance. This option is "medium-similar" to the OS/VS COBOL
"notrunc" option, but there are some down differences.

* * * * * * * *

I suggest that you get one of the IBM "migration guides" (there
are different ones depending on which COBOL you are going from
and which you are going to) - and look at the topic "TRUNC".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
