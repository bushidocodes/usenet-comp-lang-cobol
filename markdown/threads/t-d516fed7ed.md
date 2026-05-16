[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL/VSE and ICCF batch partitions

_1 message · 1 participant · 2001-01_

---

### COBOL/VSE and ICCF batch partitions

- **From:** "Leon" <Leon.in.Newport.News@att.net>
- **Date:** 2001-01-18T01:39:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uPr96.439$Mu1.17281@bgtnsc06-news.ops.worldnet.att.net>`

```
I have a few programs written in DOS/COBOL that were intended to be run in
an ICCF batch partition.

When I converted one of the programs to COBOL/VSE I discovered that it would
not run because the ICCF batch partition was loading run-time phases from
the SCEECICS library instead of the SCEEBASE library.

Is there a way to do the equivalent of a LIBDEF in an ICCF batch partition
to force the loading of run-time phases from the SCEEBASE library?

Leon
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
