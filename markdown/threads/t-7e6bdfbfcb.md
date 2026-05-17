[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie question re: DEC Alpha Compilition

_2 messages · 2 participants · 1998-02_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Newbie question re: DEC Alpha Compilition

- **From:** "gypsy" <ua-author-45425@usenetarchives.gap>
- **Date:** 1998-02-13T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd39a3$83b0daa0$08b4ced0@planet10>`

```

arrrghh...

Would anyone happen to know the system specific commands for assignment in
the File-Control section for system input and output commands on a DEC
Alpha System V Unix machine?

I am presently doing an "independent study" intro to COBOL at a University
which uses the DEC Alpha, and there isn't any documentation regarding the
COBOL compiler thereon. While the CA-Relia compiler I am using on my
windows box at home is "really nifty" I would prefer to stay in a UNIX
environment and can't seem to get these assignment commands for file input
and output.

Any help would be greatly appreciated.

Additionally: nice newsgroup y'all... I plan on perusing it often now that
I've found it :)

Lucretia M. Pruitt
gy··.@pla··l.com or
pru··.@cle··d.edu
```

#### ↳ Re: Newbie question re: DEC Alpha Compilition

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1998-02-14T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7e6bdfbfcb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd39a3$83b0daa0$08b4ced0@planet10>`
- **References:** `<01bd39a3$83b0daa0$08b4ced0@planet10>`

```

Not sure whether this will answer your question (it probably won't), but...

Under VMS, sys$input and sys$output (and also sys$command) are special
logicals that point to the source of input, output, and the next DCL
command. So, if you do something like...

SELECT SYS-INP ASSIGN TO SYS$INPUT.
SELECT SYS-OUT ASSIGN TO SYS$OUTPUT.
.
.
.
FD SYS-INP.
01 SYS-INP-REC.
05 FILLER PIC X(256).
FD SYS-OUT.
01 SYS-OUT-REC.
05 FILLER PIC X(256).

This should enable you to read and write to these standard devices (wherever
they happen to be pointing to at the moment).

Mind you, this is working under VMS. I'm not sure whether this is valid
under UNIX or Ultrix.

Good luck!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
