[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Unix System Problem

_2 messages · 2 participants · 1998-03_

---

### Unix System Problem

- **From:** "eric boatman" <ua-author-17074090@usenetarchives.gap>
- **Date:** 1998-03-23T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f8j02$ss2$0@208.207.70.226>`

```

We're running Unix (System V Release 4, if you care), we experience a lot of
file locks.
Thats when two or more people accessing the same file. Get locked out of the
record, they
tried to READ. The only solutions we have been able to come up with is to
either
WRITE the record after it has been READ or keep the file open as little as
possible, but
all this I/O slows down the code.

Any Ideas?

Thanx
Eric Boatman
Southern Missouri Containers, INC.
Be··.@Pc··s.net
```

#### ↳ Re: Unix System Problem

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-03-23T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-edf1cdb599-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6f8j02$ss2$0@208.207.70.226>`
- **References:** `<6f8j02$ss2$0@208.207.70.226>`

```

In message <<6f8j02$ss2$0.··.@208··0.226>> "Eric Boatman" writes:
› file locks.
› Thats when two or more people accessing the same file. Get locked out of the
…[7 more quoted lines elided]…
› Any Ideas?

I hope you meant REWRITE.

Does your compiler support UNLOCK ? or READ WITH NO LOCK ? or
LOCK MODE MANUAL plus READ WITH LOCK where actually required ?

It is usually necessary to supply the compiler make and version
with these questions because each compiler has its own variations
on how it does locking.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
