[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Same Record Key and FD for multiple VSAM files (of same structure)

_1 message · 1 participant · 2007-09_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Same Record Key and FD for multiple VSAM files (of same structure)

- **From:** dividby0 <mithhilarora@gmail.com>
- **Date:** 2007-09-23T03:59:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1190545150.006181.323230@n39g2000hsh.googlegroups.com>`

```
Hi,

I'm writing a COBOL program which accepts 5 KSDS files and extract
data into a single file. All the files are of the same type and have
same data fields with values from different sources.

I am able to do this for 1 input file. But I'm having problems with
the Record Key Clause and FD for 5 files.

Since the files have same struction I'm using"

RECORD KEY IS NCB-D100

How can I do this for 5 files?

And, I'm using a copybook for the FD:

FD INP-FIL.
COPY BCBSECR.

I want to use the same copybook for all the 5 files.

Help required.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
