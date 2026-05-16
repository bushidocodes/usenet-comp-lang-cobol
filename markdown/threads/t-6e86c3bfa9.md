[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# problems compiling cobol-files

_2 messages · 2 participants · 1998-07_

---

### problems compiling cobol-files

- **From:** werth@mailer.scm.de
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6og6kq$ft3$1@surz18.HRZ.Uni-Marburg.DE>`

```


helo there!

I am programming with MS-COBOL version 4.
I have the following problem:

If I have compiled and linked a COBOL-program it will run only depending
from files like ADIS.EXE ... and so on.

How can I make the program run independend from COBOL-files like ADIS.EXE?

If you know the answere please send it to:

WERTH@MAILER.SCM.DE

Thank you.

Viele Gruesse
Carsten.

Net-Tamer V 1.11 - Test Drive
```

#### ↳ Re: problems compiling cobol-files

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-07-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ogrr1$61o$1@news.igs.net>`
- **References:** `<6og6kq$ft3$1@surz18.HRZ.Uni-Marburg.DE>`

```
>If I have compiled and linked a COBOL-program it will run only >depending
>from files like ADIS.EXE ... and so on.

You can link them in at link time.  For ADIS, for example, find
ADIS.OBJ (comes with the compiler), and link myprog+ADIS
rather than just myprog.  Here is a standard link file that I use
as link @filename.

\LIBRARY\RIR\RIRO\RIR+\LIBRARY\RIR\RIRO\RIR001+
\NCOBOL\ADIS+\NCOBOL\ADISINIT+\NCOBOL\ADISKEY+\NCOBOL\IXSIO
RIR
RIR
\LIBRARY\RIR\RIRO\RIR
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
