[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/370 vs. COBOL II TRUNC option

_1 message · 1 participant · 1996-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL/370 vs. COBOL II TRUNC option

- **From:** "gbr..." <ua-author-17086300@usenetarchives.gap>
- **Date:** 1996-02-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19960206142547.gbrooks@crystalball.com>`

```
We are switching from COBOL II to COBOL/370. The compiler options read
identically in the manuals, but one thing that worked properly in COBOL II
generates an S-level error with COBOL/370.

Using option TRUNC(OPT), COBOL II said the following statement was okay and
generated the proper code:

77 HEX-16384 COMP PIC S9(4) VALUE +16384.

This generates a halfword (2-byte) field that contains a hex value of
'4000'.

COBOL/370 flags that statement and says that a 5-digit value won't fit.

Is there another TRUNC option that won't generate the S-level error? Why is
this being flagged to begin with?
All replies appreciated.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
