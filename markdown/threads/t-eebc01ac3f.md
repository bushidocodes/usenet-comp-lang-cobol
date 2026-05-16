[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File owner

_2 messages · 2 participants · 2000-01_

---

### File owner

- **From:** "Bill Wood" <beavis27@bigfoot.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OuUlbGcX$GA.112@cpmsnbbsa05>`

```
I'm using NetExpress 3.0 on NT 4.0 and I'm trying to find the owner of a
given file.  If I look at the properties of the file I can find the owner so
there must be some way to get it.  Does anyone know how to get this through
COBOL (preferable) or a WinAPI call (more realistic)?  Any help would be
appreciated.

bill
```

#### ↳ Re: File owner

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2000-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56nf4.34339$g12.1033331@news2.rdc1.on.home.com>`
- **References:** `<OuUlbGcX$GA.112@cpmsnbbsa05>`

```
Take a look at GetFileSecurity(). It might be what you want.

Karl Wagner

"Bill Wood" <beavis27@bigfoot.com> wrote in message
news:OuUlbGcX$GA.112@cpmsnbbsa05...
> I'm using NetExpress 3.0 on NT 4.0 and I'm trying to find the owner of a
> given file.  If I look at the properties of the file I can find the owner
so
> there must be some way to get it.  Does anyone know how to get this
through
> COBOL (preferable) or a WinAPI call (more realistic)?  Any help would be
> appreciated.
…[4 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
