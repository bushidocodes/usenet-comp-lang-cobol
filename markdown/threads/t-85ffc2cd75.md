[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP : INTRINSIC Functions MVS COBOL II

_2 messages · 2 participants · 1996-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### HELP : INTRINSIC Functions MVS COBOL II

- **From:** "david osborne" <ua-author-2107636@usenetarchives.gap>
- **Date:** 1996-02-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4g8qo7$6pi@cdn_news.telecom.com.au>`

```
Is anyone using intrinsic functions (eg SIN,TAN) in a Batch MVS COBOL II (Rel 4.0)
environment. Are you using inhouse routines or some 3rd Party Product ?

TIA

David.
```

#### ↳ Re: HELP : INTRINSIC Functions MVS COBOL II

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-02-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-85ffc2cd75-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4g8qo7$6pi@cdn_news.telecom.com.au>`
- **References:** `<4g8qo7$6pi@cdn_news.telecom.com.au>`

```
Per-se, the COBOL intrinsic functions are not available in VS COBOL II
R4.0 In particular, the VS COBOL II compiler does not recognize or
compile the FUNCTION syntax, and library does not support the functions
(if compiled with a compiler - COBOL/370 or COBOL for MVS and VM that does
recognize them).

The Edge "Bridge to the Next Century" routines provide transparent, work
alikes for the 5 date related intrinsics for OS/VS COBOL and VS COBOL II -
INTEGER OF DATE, INTEGER OF DAY, DAY OF INTEGER, DATE OF INTEGER and
CURRENT -DATE.

If you have LE/370, reference to the LE/370 functions ( different than the
COBOL intrinsic functions ) is reported to be possible under special
circumstances, but you are likely on your own.

We have used nearly all of the intrinsics here, but only with COBOL/370
and LE/370 platforms.

I have also developed SIN and COS routines for OS/VS and VS COBOL II
environments which are exclusively in the language available in those
compilers. Taylor / McLauren series were used to perform the calculation
- straight out of a 1960's School of Mines and Misery Math 21 (calculus)
text book. These provided the SIN and COS function for a client who could
not get to COBOL/370. These routines were never developed to the extent
that the Bridge to the Next Century routines were ( not made coding
transparent ), but they do generate the "right" answers.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
