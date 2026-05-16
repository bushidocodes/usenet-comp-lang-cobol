[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error while installing Fujitsu COBOL 3.0 -COBOLV3-

_3 messages · 3 participants · 2006-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Error while installing Fujitsu COBOL 3.0 -COBOLV3-

- **From:** ehabaziz2001@gmail.com
- **Date:** 2006-09-23T10:45:52-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1159033551.935864.189050@d34g2000cwd.googlegroups.com>`

```
I tried many installations of
String variable is not large enough for string.
check the string decalrations.
Error 401

When executing I found not found file :
f3biprct.dll
```

#### ↳ Re: Error while installing Fujitsu COBOL 3.0 -COBOLV3-

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-09-24T12:44:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1159127079.317531.250670@m7g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<1159033551.935864.189050@d34g2000cwd.googlegroups.com>`
- **References:** `<1159033551.935864.189050@d34g2000cwd.googlegroups.com>`

```

ehabaziz2001@gmail.com wrote:
> I tried many installations of
> String variable is not large enough for string.
…[4 more quoted lines elided]…
> f3biprct.dll

I can find no mention of Error 401 (there is a 410 referring to the
STOP statement). The text you quote would indicate that an attempt is
being made to move a string into a field that is too small to hold the
result.

I do not understand why you have looked for and found missing the
f3biprct.dll.
```

##### ↳ ↳ Re: Error while installing Fujitsu COBOL 3.0 -COBOLV3-

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-09-24T20:52:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2eCRg.36707$Ua3.6067@fe06.news.easynews.com>`
- **References:** `<1159033551.935864.189050@d34g2000cwd.googlegroups.com> <1159127079.317531.250670@m7g2000cwm.googlegroups.com>`

```
Isn't the error on a "LIBPATH" or "PATH" type commend (seating up the 
environment for Fujitsu - not within a COBOL program)?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
