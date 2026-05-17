[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OPTLINK with CA-Realia II

_1 message · 1 participant · 1995-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### OPTLINK with CA-Realia II

- **From:** "nor..." <ua-author-17087514@usenetarchives.gap>
- **Date:** 1995-08-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40vt1l$5gf@hudson.lm.com>`

```

I'm having problems with INCLUDE statements in DEF files for the OPTLINK
compiler version 2.60.

My def file looks like this:

LIBRARY ....
STUB ....
STACKSIZE ...
INCLUDE c_code.def
INCLUDE sms_code.def

Then, c_code.def and sms_code.def look like this:

IMPORTS
...

OPTLINK returns an error "Unexpected End of File" #26. If I don;t use INCLUDE
statements, it works fine. Anyone else encounter this error?

StorminNormin


nor··.@gen··s.com People generally fear what they dont understand.
Norman E. Gottschalk III
Manager of MIS
General American Credits, Inc.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
