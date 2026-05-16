[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Print to file in Rm/Cobol...

_2 messages · 2 participants · 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Print to file in Rm/Cobol...

- **From:** "R���jean Carrier" <rejean.carrier@informatiquell.ca>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w9OK3.2183$jC3.78491@wagner.videotron.net>`

```
Hello, I am running R/M Cobol 85.

I would like to print in a file that will be loaded by Wordpad but i don't
know what code force a form feed.

Any help would be greatly appreciated.

Thanks in advance for your help.
```

#### ↳ Re: Print to file in Rm/Cobol...

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqOK3.10$iN6.971@news2.mia>`
- **References:** `<w9OK3.2183$jC3.78491@wagner.videotron.net>`

```
R�jean Carrier wrote:
>Hello, I am running R/M Cobol 85.
>
>I would like to print in a file that will be loaded by Wordpad but i don't
>know what code force a form feed.


WRITE print-record BEFORE/AFTER PAGE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
