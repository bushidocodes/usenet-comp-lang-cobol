[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Difference between COBOL II and COBOL/370

_3 messages · 3 participants · 1996-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Difference between COBOL II and COBOL/370

- **From:** "jason antonitis" <ua-author-17086614@usenetarchives.gap>
- **Date:** 1996-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<317C464F.60F7@cs.niu.edu>`

```
I have been programming in LE/370 here at school for about 3 years
and I have and intership this summer programming in COBOL II. Are these
two versions the same except for intrinsic functions in LE/370? Or, what
are the differences?

- Jason
```

#### ↳ Re: Difference between COBOL II and COBOL/370

- **From:** "liz krofka" <ua-author-8741652@usenetarchives.gap>
- **Date:** 1996-04-23T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f94a73aaf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<317C464F.60F7@cs.niu.edu>`
- **References:** `<317C464F.60F7@cs.niu.edu>`

```
Jason Antonitis wrote:
› 
› I have been programming in LE/370 here at school for about 3 years
…[4 more quoted lines elided]…
› - JasonYes, as far as the COBOL code is concerned the only difference is the 
functions available in COBOL/370 and not in COBOL II.
Liz Krofka	GMAC Information Warehouse - EDS
		Plano, TX	
================================================
Is there life out there?
```

#### ↳ Re: Difference between COBOL II and COBOL/370

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-04-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f94a73aaf-p3@usenetarchives.gap>`
- **In-Reply-To:** `<317C464F.60F7@cs.niu.edu>`
- **References:** `<317C464F.60F7@cs.niu.edu>`

```
Jason Antonitis wrote:
› I have been programming in LE/370 here at school for about 3 years
› and I have and intership this summer programming in COBOL II.  Are these 
…[3 more quoted lines elided]…
› - Jason

IBM publications state that a COBOL II program (release 3 or better) will
compile without changes under the LE370 compiler, variously called COBOL
370 or COBOL/MVS. The primary differences are the presence of functions
in LE370, and that all LE370 compilers for MVS (PL/1, Fortran, COBOL, C)
share the same runtime libraries. This is supposed to improve
interoperability between these languages.

IBM VS COBOL II came out first. IBM wants all their customers
to migrate to LE370 compilers eventually.

So if you exclude intrinsic functions and runtime libraries, IBM COBOL II
and COBOL 370 are essentially the same to the programmer.

My shop hasn't gotten COBOL 370 yet. I've got a book on COBOL 370, and I
would be interested in using some of those intrinsic functions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
