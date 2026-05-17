[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# VS COBOL II vs. COBOL/370

_3 messages · 3 participants · 1995-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### VS COBOL II vs. COBOL/370

- **From:** "be..." <ua-author-40317@usenetarchives.gap>
- **Date:** 1995-10-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<461h4g$1cn@ixnews7.ix.netcom.com>`

```
We are looking to improve speed performance of a number of
cpu-intensive VS COBOL II programs. I understand that the COBOL/370
compiler (now known as COBOL for MVS and VM) and also a version of
COBOL 85 contains a number of intrinsic functions which may very well
provide speed improvements in such things as string manipulation and
character handling.

I would very much appreciate hearing from COBOL programmers who have
used the COBOL/370 intrinsics and can advise on their relative speed,
as well as their ease of use.

Thanks in advance for your help.

Beryl Blickstein
Group 1 Software
Lanham MD
```

#### ↳ Re: VS COBOL II vs. COBOL/370

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-10-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcac66bf77-p2@usenetarchives.gap>`
- **In-Reply-To:** `<461h4g$1cn@ixnews7.ix.netcom.com>`
- **References:** `<461h4g$1cn@ixnews7.ix.netcom.com>`

```
In article <464ja9$i.··.@new··l.com> RWidmer, rwi··.@a··.com
writes:

...

› As for ease of use, the big headache with the current Intrinsic Function
› implementation is a problem inherited from the standard.  Error
…[4 more quoted lines elided]…
› these routines.

That is indeed a fault. CODASYL had resolved this by defining an error
return. ANSI did not like that (some returns could be legitimate values
for such things as TAN) and rejected it. In the next standard, the
common
exception procesing facility provides a capability of checking for errors
(after executing the function, that is).
Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

#### ↳ Re: VS COBOL II vs. COBOL/370

- **From:** "wein..." <ua-author-17087683@usenetarchives.gap>
- **Date:** 1995-10-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bcac66bf77-p3@usenetarchives.gap>`
- **In-Reply-To:** `<461h4g$1cn@ixnews7.ix.netcom.com>`
- **References:** `<461h4g$1cn@ixnews7.ix.netcom.com>`

```
Just how more efficient the new intrinsic functions prove to be depends on how slow your current
ones happen to be. The intrinsic functions in COBOL/370 are the same string functions available
throughout the LE/370 environment. For people with C/370 experience, the routines are the same.
You'll need to benchmark.

Howard Weiner
The Number Company, Inc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
