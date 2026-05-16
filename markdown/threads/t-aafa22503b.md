[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# error message with mf cob -x and sco OD5

_1 message · 1 participant · 2000-04_

---

### error message with mf cob -x and sco OD5

- **From:** Jean-michel Bain-cornu <jean-michel.bain-cornu@libertysurf.fr>
- **Date:** 2000-04-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38E9AFB5.CB46ABC1@libertysurf.fr>`

```
This action works correctly on unix sco 4.2
With mfcobol 3.2 on SCO 5.0.5, i obtain:

$ cat tst.cbl
       working-storage section.
       procedure division.
       display "hello"
$ cob -x tst.cbl
i386ld libcrtn.a: can't find library libsocket.a

My unix is:
$ uname -X
System = SCO_SV
Node = archexx5
Release = 3.2v5.0.5
KernelID = 98/07/02
Machine = Pentium
BusType = EISA
Serial = 4FI005643
Users = 16-user
OEM# = 0
Origin# = 1
NumCPU = 1

and my cobol (toolbox 3.2.37) is:
$ cob -V
version @(#)cob.c       1.47
PRN=2XCGG/ZZC:7a.1a.11.06b
PTI=NLS

Any idea ?
Thanks in advance
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
