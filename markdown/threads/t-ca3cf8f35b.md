[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Follow up: Question for CICS gurus -- CICS CALL statements]

_1 message · 1 participant · 1998-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Follow up: Question for CICS gurus -- CICS CALL statements]

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-07-03T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<6nhmbp$gq0@bgtnsc03.worldnet.att.net>`
- **References:** `<359BB445.FA569E2A@earthlink.com> <6ngt57$4fn$1@heliodor.xara.net> <6ngtik$cgk@bgtnsc01.worldnet.att.net>`

```

Ramone wrote:
> 
(snip)
> No.  This merely bypasses the load from //STEPLIB.  You would never be
> allowed to do this in my shop, but if you insist, then you must have
> your program in a //STEPLIB library, not a //DFHRPL library.

No, it's a static call. On completion of the link edit (or Binder) step,
the load module will contain the module called "PROGRAM". The CICS
region's STEPLIB and/or DFHRPL don't enter into it. What matters is the
SYSLIB concatenation for the link edit (or Binder) step, meaning
"PROGRAM" had better be found there. This is true in an MVS 5.2. &
CICS/ESA 4.1 environment. If you believe otherwise please describe your
operating environment's attributes.

Also, if you would not permit a static call, what did you do regarding
calling subroutines from OS/VS COBOL programs (assuming, of course, that
you had OS/VS COBOL programs)?

Bill Lynch

> >
> >    Would appreciate any feed back.  I promise to post any updates or solutions to this problem.
…[12 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
