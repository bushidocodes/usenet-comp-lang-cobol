[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu 6.0; Using german special-chars in alphabetic-test

_2 messages · 2 participants · 2002-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu 6.0; Using german special-chars in alphabetic-test

- **From:** "Spectra" <Spectra.Soft@t-online.de>
- **Date:** 2002-06-02T12:18:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<adcrd1$30i$01$1@news.t-online.com>`

```
Hi!

Is it possible do define an alphabet which includes german special
characters like "ï¿½" "ï¿½" and others so that the condition "IF .... IS
ALPHABETIC " becomes true even if these characters are included in the
string being examined?

Are special compiler-options required?

Do You have an example?

Thanks a lot in advance!
Hans Jakschik
```

#### ↳ Re: Fujitsu 6.0; Using german special-chars in alphabetic-test

- **From:** Carlos Lages <clages@attglobal.net>
- **Date:** 2002-06-11T08:49:25-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D05E3C5.75DEEE31@attglobal.net>`
- **References:** `<adcrd1$30i$01$1@news.t-online.com>`

```
Hans Jakschik
try this

in Special names paragraph
section
Special-names

ALPHABET clause

find this in you PDF manual tha comes in Power cobol CD

Carlos lages


Spectra gravada:

> Hi!
>
…[10 more quoted lines elided]…
> Hans Jakschik
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
