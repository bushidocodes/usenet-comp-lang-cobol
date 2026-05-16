[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACCEPT / Y2K

_1 message · 1 participant · 1999-02_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Language features and syntax`](../topics.md#syntax)

---

### Re: ACCEPT / Y2K

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-02-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36BE4605.8BEAD7D4@acm.org>`
- **References:** `<36B9F4CE.1E4@club-internet.fr> <19990205013208.28378.00000993@ng-fb1.aol.com>`

```
Theo DP wrote:
> 
> >Subject: ACCEPT / Y2K
…[15 more quoted lines elided]…
> will get you an 8 digit date.

And I believe this function definition is part of the formal ISO/ANSI
COBOL Extensions, so the complete current COBOL standard does include
4-digit year support if you are running on a compiler that is current
enough to support the functional extensions.  Although there are some
ACCEPT syntax extensions implemented by some compilers, the old ACCEPT
syntax should not have its semantics arbitrarily changed for 4-digit
years, as this would break existing programs (including those programs
that are Y2K compliant despite the 2-digit year from ACCEPT because they
use windowing or some other technique as required to interpret the
date)  
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
