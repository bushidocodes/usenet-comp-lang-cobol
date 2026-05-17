[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error handler in MF Cobol 4.0

_2 messages · 2 participants · 1998-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Error handler in MF Cobol 4.0

- **From:** "priem..." <ua-author-17084430@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34DEF111.1FFBFD2C@sni.de>`

```

Hi,

does anyone know if it's possible to define or overwrite a error
handler,
e.g. to handle out of boundary errors, file errors, ... in MF Cobol 4.0.

In know there exists something like Exceptions in MF Object Cobol, but
we don't write new programs so this is not a solution for us. The main
purpose of this error handler would be to log this error to a log file.
The Cobol program must not just exit if a serious error occurs.

Regards


Karsten Priemer


--------------------------------------------------------------------------------------

Karsten Priemer
Siemens Nixdorf Informationssysteme AG
email: pri··.@s··.de phone: 00495251 815583
--------------------------------------------------------------------------------------
```

#### ↳ Re: Error handler in MF Cobol 4.0

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d5a5cad11d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34DEF111.1FFBFD2C@sni.de>`
- **References:** `<34DEF111.1FFBFD2C@sni.de>`

```

pri··.@s··.de wrote:
› 
› Hi,
…[3 more quoted lines elided]…
› e.g. to handle out of boundary errors, file errors, ... in MF Cobol 4.0.

I am not sure what you mean by 'boundary errors' (subscript overflows?)
but file errors are usually dealt with by a FILE STATUS declaration.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
