[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File Locking - NT Server 4.0 - Windows95 - VB 3.0 - MsCobol Dll's & Index Sequential File System

_1 message · 1 participant · 1997-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### File Locking - NT Server 4.0 - Windows95 - VB 3.0 - MsCobol Dll's & Index Sequential File System

- **From:** "richard" <ua-author-11605@usenetarchives.gap>
- **Date:** 1997-02-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc1682$fab72f40$2b371bc4@richardpentium>`

```

Hi,
I am having a problem with msWindows 95 reporting:-

"System Error - File in use by another application
........."

I am using an application using Visual Basic 3.0 Prof. as the front end
calling multi-entry point msCobol 5.0 progammes complied to .dll's. The
Select
statement contains "locking manual" and "not optional". All files are
opened
I/O and closed again before leaving the cobol dll. The only locking done is
within the cobol and that is "record locking" when updating a record.

The VB exe's and the cobol dll's are all loaded onto the client PC,s
(6 x pentium 100mhz with 32mb ram and ethernet UTP). The files are loaded
onto a NT server 4.0 (pentium 100mhz with 32mb ram and ethernet UTP).
The disk and directory concerned are shared with "full control". The
"clients"
are mapped to this directory and the application working directory pathed
to
the mapped drive.

The same application with the same settings run without a
problem
under the Novell 3.12 environment using msWindows for Work Groups 3.11.

Browsing through files in the multi user environment works well and is very
fast. As soon as there is a mixture of updating and browsing the "system
error"
messages begin to occur. The first client to display this message seems to
cause a number of the others to also display the same message.

After "clicking" on "OK" on the PC that first displayed the message, the
others
can then also successfully "click" on "OK" and continue working.

This looks as if msWindows is not allowing the "record locked" condition
through to the cobol programme (which would wait for 2 seconds before
retrying the instruction), although I cannot be sure.

Are there any of you that have any suggestions as to solve this problem???

Best wishes

Richard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
