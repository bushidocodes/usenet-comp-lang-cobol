[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WorkBench V3.4 Problem

_2 messages · 1 participant · 2000-01_

---

### WorkBench V3.4 Problem

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86js7o$2b3$1@nnrp1.deja.com>`

```
Hi,

since I changed my machine I'm having a configuration problem when
compiling using WorkBench V3.4.

Situation:
MainPath for sources: q:\cobol\pptawis
COBCPY=q:\cobol\pptawis
COBDIR=q:\cobol\pptawis

When editing a program within a subdir lets say q:\cobol\pptawis\upd3
I'm able to expand and to maintain copy-files stored in
q:\cobol\pptawis.

So far so good.

But when I try to compile I get: ERROR: Missing Copy file on exactly
those copyfiles stored in q:\cobol\pptawis.

Does anyone know, what I forgot the configure?

Any hints are gratefully appreciated.

TIA- Stefan Meyer





Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: WorkBench V3.4 Problem

- **From:** Stefan.Meyer@Triumph-international.de
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86kgjq$ggl$1@nnrp1.deja.com>`
- **References:** `<86js7o$2b3$1@nnrp1.deja.com>`

```
So sorry....got it. The COBCPY was pointing to a wrong path...I forgot
the ';' to enhance the existing COBCPY


Bye - Stefan Meyer


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
