[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL II with COBOL 370

_2 messages · 2 participants · 1999-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: COBOL II with COBOL 370

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<83gj1a$824$1@nntp4.atl.mindspring.net>`
- **References:** `<83evor$nnl$1@ssauraaa-i-1.production.compuserve.com>`

```
Yes,
  If you mean a user-written COBOL/370 (which is actually obsolete and
replaced by IBM COBOL for MVS & VM - or IBM COBOL for OS/390 & VM) program
which uses intrinsic functions, then you can statically call such
user-written programs from VS COBOL II.

HOWEVER, if your VS COBOL II program is compiled with the NORES compiler
option, you will need to use the LE library when you link-edit it.  If it is
compiled with RES, you shouldn't have any serious problem. (Read the COBOL
for this-and-that Migration Guide for general rules on mixing VS COBOL II and
COBOL for this-and-that routines.)

If you mean one of the LE routines (for doing "intrinsic functions") then the
answer is that you cannot call them (statically or dynamically) from a VS
COBOL II program.  Only the date/time routines can be directly called - and
the CALL must be dynamic - from a VS COBOL II program.

(CC'ing the reply to comp.lang.cobol - which is better than alt.cobol for
this type of question.)
```

#### ↳ Re: COBOL II with COBOL 370

- **From:** "Frank Lucivero" <nitesun@goes.com>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<386979c9@news.goes.com>`
- **References:** `<83evor$nnl$1@ssauraaa-i-1.production.compuserve.com> <83gj1a$824$1@nntp4.atl.mindspring.net>`

```
frankres@goes.com OUTSTANDING OPPORTUNITIES IN NY/NJ


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:83gj1a$824$1@nntp4.atl.mindspring.net...
> Yes,
>   If you mean a user-written COBOL/370 (which is actually obsolete and
…[5 more quoted lines elided]…
> option, you will need to use the LE library when you link-edit it.  If it
is
> compiled with RES, you shouldn't have any serious problem. (Read the COBOL
> for this-and-that Migration Guide for general rules on mixing VS COBOL II
and
> COBOL for this-and-that routines.)
>
> If you mean one of the LE routines (for doing "intrinsic functions") then
the
> answer is that you cannot call them (statically or dynamically) from a VS
> COBOL II program.  Only the date/time routines can be directly called -
and
> the CALL must be dynamic - from a VS COBOL II program.
>
…[17 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
