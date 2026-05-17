[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Take the COMPUTE challenge

_8 messages · 5 participants · 1995-07 → 1995-08_

---

### Take the COMPUTE challenge

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1995-07-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3uf16m$hia@hpchase.rose.hp.com>`

```
We've seen several arguments about the COMPUTE statement in COBOL.

1. COMPUTE is [good/bad] because it is [faster/slower] than the
other arithmetic statements. I would expect this to depend a
lot on the particular compiler, and I doubt there would be a
measurable difference for the typical COBOL application.

2. COMPUTE is [good/bad] because it is [more/less] readable. This
is pretty subjective and depends on who is doing the reading.

3. COMPUTE is bad because the rules of COBOL don't define how the
intermediate results will be handled. Precision, rounding, etc.,
are left up to the compiler implementor. I see this as the
biggest potential problem.

I propose the following experiment to help us gauge just how much of
a portability problem there is with the COMPUTE statement today.
Consider the following program.

IDENTIFICATION DIVISION.
PROGRAM-ID. COMPUTE-TEST.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 A PIC 9(10)V9 VALUE 10.
01 B PIC 9(10)V9 VALUE 3.
01 C PIC 9(5).999.
PROCEDURE DIVISION.
BEGIN.
COMPUTE C = (A / B) * 10000
DISPLAY C
STOP RUN.
END PROGRAM COMPUTE-TEST.

Predict the results of this program. (Hint: There is no right answer,
according to the current COBOL standard.) Does your compiler's
documentation give you enough information to define the results?
Now run the program on as many compilers as you have access to, and
post the results. Were you surprised?

For the ambitious, experiment with different values, different PICTURE
clauses, different USAGE clauses, the ROUNDED phrase, etc.

Walter
```

#### ↳ Re: Take the COMPUTE challenge

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1995-07-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8d409f9cf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3uf16m$hia@hpchase.rose.hp.com>`
- **References:** `<3uf16m$hia@hpchase.rose.hp.com>`

```
wc··.@adp··e.edu wrote:

: The problem with this computation series is not COMPUTE vs. a series of DVIDE
: and MULTIPLY. I expect the COMPUTE will get exactly the same results as if you
: did the following:
: DIVIDE A BY B GIVING D.
: MULTIPLY D BY 10000 GIVING C.

: And you can define D with however many decimal places you wish.

You may expect this to give the same results, but you didn't try it,
did you?

And the number of decimal places you define for D certainly does affect
the result. That's the whole point. Using separate DIVIDE and MULTIPLY
statements gives you a degree of control and portability that you
sacrifice when you use COMPUTE.

Several people have actually executed the code that I posted and have
mailed the results to me. No two have gotten the same answer! I'll
post a summary when a few more people have gotten a chance to try it.

Walter
```

#### ↳ Re: Take the COMPUTE challenge

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1995-07-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8d409f9cf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3uf16m$hia@hpchase.rose.hp.com>`
- **References:** `<3uf16m$hia@hpchase.rose.hp.com>`

```
I wrote:

: I propose the following experiment to help us gauge just how much of
: a portability problem there is with the COMPUTE statement today.
: Consider the following program.

: IDENTIFICATION DIVISION.
: PROGRAM-ID. COMPUTE-TEST.
: DATA DIVISION.
: WORKING-STORAGE SECTION.
: 01 A PIC 9(10)V9 VALUE 10.
: 01 B PIC 9(10)V9 VALUE 3.
: 01 C PIC 9(5).999.
: PROCEDURE DIVISION.
: BEGIN.
: COMPUTE C = (A / B) * 10000
: DISPLAY C
: STOP RUN.
: END PROGRAM COMPUTE-TEST.

: Predict the results of this program. (Hint: There is no right answer,
: according to the current COBOL standard.) Does your compiler's
: documentation give you enough information to define the results?
: Now run the program on as many compilers as you have access to, and
: post the results. Were you surprised?

Not many people took the challenge, but a few souls did mail me
their results. I take no responsibility for the accuracy of
this data.

VAX COBOL: 33333.333
IBM 3090-400E with IBM OS/VS COBOL RELEASE 2.3: 33330.000
Tandem COBOL85: 33333.000
An old CDC implementation: 33333.333
HP 3000 with HP COBOL II: 33330.000

Bottom line: Simple COMPUTE statement on five compilers gives three
different results.

If DIVIDE and MULTIPLY statements had been used instead, I am confident
all five compilers would have produced identical results.

Walter
```

##### ↳ ↳ Re: Take the COMPUTE challenge

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1995-07-26T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8d409f9cf-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8d409f9cf-p3@usenetarchives.gap>`
- **References:** `<3uf16m$hia@hpchase.rose.hp.com> <gap-a8d409f9cf-p3@usenetarchives.gap>`

```
I wrote:

: : 01 A PIC 9(10)V9 VALUE 10.
: : 01 B PIC 9(10)V9 VALUE 3.
: : 01 C PIC 9(5).999.
: : COMPUTE C = (A / B) * 10000
: : DISPLAY C

: VAX COBOL: 33333.333
: IBM 3090-400E with IBM OS/VS COBOL RELEASE 2.3: 33330.000
: Tandem COBOL85: 33333.000
: An old CDC implementation: 33333.333
: HP 3000 with HP COBOL II: 33330.000

Here is one more data point.

MicroFocus v3.2 under IBM's AIX 3.2.5: 33333.333

Thanks to those who took the time to try the code and send me their
results. If anyone else wants to try it on a different implementation,
please post your results here.

Walter
```

###### ↳ ↳ ↳ Re: Take the COMPUTE challenge

- **From:** "ac..." <ua-author-6281289@usenetarchives.gap>
- **Date:** 1995-08-01T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8d409f9cf-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8d409f9cf-p4@usenetarchives.gap>`
- **References:** `<3uf16m$hia@hpchase.rose.hp.com> <gap-a8d409f9cf-p3@usenetarchives.gap> <gap-a8d409f9cf-p4@usenetarchives.gap>`

```
Using CA-Realia II Workbench with the Realia-4 dialect
the program gave me 33333.333, so add that to your list Walter.

Aron Cox
CU&C Health Services Society
Vancouver
Canada.
```

##### ↳ ↳ Re: Take the COMPUTE challenge

- **From:** "mark gray" <ua-author-1833039@usenetarchives.gap>
- **Date:** 1995-07-26T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8d409f9cf-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8d409f9cf-p3@usenetarchives.gap>`
- **References:** `<3uf16m$hia@hpchase.rose.hp.com> <gap-a8d409f9cf-p3@usenetarchives.gap>`

```
[snip]
›     VAX COBOL:                                       33333.333
›     IBM 3090-400E with IBM OS/VS COBOL RELEASE 2.3:  33330.000
›     Tandem COBOL85:                                  33333.000
›     An old CDC implementation:                       33333.333
›     HP 3000 with HP COBOL II:                        33330.000

Micro Focus COBOL 3.2 on PC 33333.333

Mark Gray
```

###### ↳ ↳ ↳ Re: Take the COMPUTE challenge

- **From:** "gordon...." <ua-author-10958913@usenetarchives.gap>
- **Date:** 1995-07-26T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8d409f9cf-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8d409f9cf-p6@usenetarchives.gap>`
- **References:** `<3uf16m$hia@hpchase.rose.hp.com> <gap-a8d409f9cf-p3@usenetarchives.gap> <gap-a8d409f9cf-p6@usenetarchives.gap>`

```
Mark Gray wrote:

ÿ¢§[snip]
ÿ¢§> VAX COBOL: 33333.333
ÿ¢§> IBM 3090-400E with IBM OS/VS COBOL RELEASE 2.3: 33330.000
ÿ¢§> Tandem COBOL85: 33333.000
ÿ¢§> An old CDC implementation: 33333.333
ÿ¢§> HP 3000 with HP COBOL II: 33330.000

ÿ¢§ Micro Focus COBOL 3.2 on PC 33333.333

ÿ¢§Mark Gray


I tried a Unisys A17 system using the COBOL85 compiler.

Unisys A17 COBOL85 v41.2 33333.333

I believe we have not had much problems with the compute statement. This used to
be a problem with the older compilers, but the new ones seem to do the right
things with computes.
```

##### ↳ ↳ Re: Take the COMPUTE challenge

- **From:** "hel..." <ua-author-12786417@usenetarchives.gap>
- **Date:** 1995-07-27T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a8d409f9cf-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a8d409f9cf-p3@usenetarchives.gap>`
- **References:** `<3uf16m$hia@hpchase.rose.hp.com> <gap-a8d409f9cf-p3@usenetarchives.gap>`

```
wal··.@hpr··p.com (Walter Murray) wrote:
› : Predict the results of this program. (Hint: There is no right answer,
› : according to the current COBOL standard.) Does your compiler's
› : documentation give you enough information to define the results?

Why isn't there a right answer? Shouldn't all compilers keep
intermeadiate results in floating point at some level of precision?
I've used several compilers on a few CPU (PC to mainframe) and they
all keep intermeadate results at 18 significant digits. I don't know
if this is part of the 'standards' but it seems unlikely that 18
significant digits would be chosen by 4 separate compiler vendors.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
