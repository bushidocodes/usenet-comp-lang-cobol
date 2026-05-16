[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rmcobol & Pervasive file problem

_1 message · 1 participant · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Rmcobol & Pervasive file problem

- **From:** Mario Gauci <mgauci@hotmail.com>
- **Date:** 1999-11-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QqkhOEDJ7nyIBGQfk5nuNxMCL3Jp@4ax.com>`

```
We are using own written RM/Cobol programs to access files under
Pervasive SQL ver.7. We are using the BEGIN/END/ABORT Transaction in
C$BTRV.DLL. When an update transaction is complete the first file
which was originally locked with the READ statement is not being
unlocked notwithstanding that we have issued the UNLOCK command. The
only time the record is released is when the file is CLOSED.

If anybody can help, please let us know.


Many Thanks


Mario


mgauci@hotmail.com or dwallbank@gasan.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
