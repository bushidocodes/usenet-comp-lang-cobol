[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF-cobol and shared libraries on Sun

_1 message · 1 participant · 1996-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF-cobol and shared libraries on Sun

- **From:** "joan schepens" <ua-author-17086521@usenetarchives.gap>
- **Date:** 1996-01-09T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<30F3824A.2DAD@denkart.be>`

```
Language : Micro Focus 3.2
Platform : Sun SPARC 20
OS : SunOS 5.4


I'm using a lot of shared libraries in my application. These shared
libraries contain only Micro Focus object code. For creating the
Micro Focus object code, I use "cob -cx -k cob1.mfcbl". For creating
the shared libraries, I use for example "ld -G -z text -o -libxxx.so
cob1.o". Because of the "-z text" option, I can see a lot of relocations
that remain against allocatable but non-writable sections. The symbols
that I see on my screen all start with _mF (_mFg2star,_mFerr,_mF9910,
_mF9923, ...).

What must I do to avoid these relocations?

Do I have to create position independent object code ?
If yes, how do I do this in Micro Focus ( which compiler option) ?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
