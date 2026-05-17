[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Century Aware Date From VS COBOL II

_1 message · 1 participant · 1997-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Date and calendar processing`](../topics.md#dates)

---

### Century Aware Date From VS COBOL II

- **From:** "ar..." <ua-author-89056@usenetarchives.gap>
- **Date:** 1997-01-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cichs$kuu@freenet-news.carleton.ca>`

```


Although our shop now has COBOL for MVS & VM and LE 1.5, some groups are
reluctant to migrate to the new compiler and are staying with VS COBOL
II 1.4.0

The IBM literature I have read states that the ACCEPT identifier FROM DATE
directive will not be changed to return a date in the form YYYYMMDD. To
accomodate the Year 2000 effort I have 2 options:

Via APAR PN79703, LE date/time services can be DYNAMICALLY called from VS
COBOL II. They cannot be called statically from COBOL II, and other LE
services cannot be called at all from COBOL II.

The same groups will not use LE date/time services, claiming that they are
too resource (CPU) intensive. My other choice is to apply PN76666 to get
the callable module IGZEDT4. I have applied this in a test environment but
I get an ABEND U1015 when I code the following:

01 YYYYMMDD PIC 9(8).

CALL "IGZEDT4" USING BY REFERENCE YYYYMMDD.

U1015 is a recursive call error. This also happens when I call IGZEDT4
dynamically. There was a HOLDSYS(ACTION) on the PTF to re-apply any
usermod that customises the COBPACKs. I did not do any customisation, so
the HOLD was bypassed.

Has anyone been able to successfully call IGZEDT4? Any information will be
much appreciated. TIA.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
