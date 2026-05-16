[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL performance

_1 message · 1 participant · 1999-09_

---

### Re: COBOL performance

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fGrmN78MyKKUWxsNLZoBqR94SN7R@4ax.com>`
- **References:** `<7rut5q$ivi@netaxs.com> <37E346F3.9B763BED@att.net>`

```
On Sat, 18 Sep 1999 04:01:55 -0400 William Lynch <WBLynch@att.net> wrote:

   [ snipped ]

:>1. while you're making all your subscripts BINARY, add a SYNC, as well.
:>COBOL (from COBOL II, on, anyway) will generate a Load instruction);

And use the compiler option TRUNC(OPT) and use the ON SIZE ERROR clause for
the cases where you are concerned that number might be too large.

   [ snipped ]
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
