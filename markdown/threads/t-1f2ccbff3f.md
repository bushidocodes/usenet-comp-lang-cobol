[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading data from Com1

_2 messages · 2 participants · 1998-02_

---

### Reading data from Com1

- **From:** "tommy nilsen" <ua-author-17072129@usenetarchives.gap>
- **Date:** 1998-02-23T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34F2DE1A.1127A10@yahoo.com>`

```

I need to read data from Com1 into my cobol program, using Win32 API.

Does anyone know how to do this, or where I could find some sample
programs ??

Any help would be appreciated...

Tommy Nilsen
tom··.@ya··o.com
```

#### ↳ Re: Reading data from Com1

- **From:** "gael wilson" <ua-author-6589191@usenetarchives.gap>
- **Date:** 1998-02-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f2ccbff3f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34F2DE1A.1127A10@yahoo.com>`
- **References:** `<34F2DE1A.1127A10@yahoo.com>`

```

Tommy,

You should be able to do this by calling the CreateFile and ReadFile APIs.
You may also need to call SetCommState to set baud rate etc.

tommy nilsen wrote in article
<34F··.@ya··o.com>...
› I need to read data from Com1 into my cobol program, using Win32 API.
› 
…[11 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
