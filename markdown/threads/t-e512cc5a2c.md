[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus

_2 messages · 2 participants · 1998-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus

- **From:** "frank osner" <ua-author-17074707@usenetarchives.gap>
- **Date:** 1998-08-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6rbq7a$d4h$1@ts-mail.roka.net>`

```
When I run a Cobol-Program in a DOS-BOX
every DISPLAY Statement appears on the Screen,
but if I turn the output into a File by ">", "2>" or ">&",
I see nothing of them.
How can I get them, if I turn the output into a file?

I use MicroFocus V4.0.32 under WinNT 4.0 SP3
```

#### ↳ Re: MicroFocus

- **From:** "karl wagner" <ua-author-12514286@usenetarchives.gap>
- **Date:** 1998-08-18T17:28:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e512cc5a2c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6rbq7a$d4h$1@ts-mail.roka.net>`
- **References:** `<6rbq7a$d4h$1@ts-mail.roka.net>`

```
Frank Osner wrote:
› 
› When I run a Cobol-Program in a DOS-BOX
…[5 more quoted lines elided]…
› I use MicroFocus V4.0.32 under WinNT 4.0 SP3

Set the environment variable COBSW to use ANSI console I/O then try
again.

SET COBSW=+S5
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
