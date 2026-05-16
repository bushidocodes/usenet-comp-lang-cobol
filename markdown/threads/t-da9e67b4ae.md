[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Elementary 0C4

_1 message · 1 participant · 1999-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Elementary 0C4

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37879611.1790228C@acm.org>`
- **References:** `<7m4jdh$prr@dfw-ixnews13.ix.netcom.com>`

```


R Teutsch wrote:
> Code
> SORT SORT-WORK ASCENDING KEY WORK-ITEM
…[15 more quoted lines elided]…
> given the sort msgs.
...

Surprised none of the other replies seems to have mentioned the obvious:

Barring some unusual inter-language interfacing problems, the most
common ways (without compiler or run-time library bugs) that an MVS
COBOL program can ever produce a S0C4 ABEND are:
(1)Table subscripts out of range; or
(2)Attempt to do input or output to a file that it not currently in OPEN
status (the address of the I/O access method routine is "null" at that
point).
(3)Use of static subroutine linking with an unresolved reference at
linkedit time (resulting in a run-time attempt to branch to 00000000).

Look for violations in these areas in your INPUT-PROC and OUTPUT-PROC,
although the code fragment you show is actually suggestive of (3), and
could suggest either a missing SYSLIB at program linkedit time or
possibly even some error in the way the SORT product was installed. 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
