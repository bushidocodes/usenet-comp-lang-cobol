[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# suppress leading zeroes

_3 messages · 3 participants · 1999-03_

---

### Re: suppress leading zeroes

- **From:** jraben19@mail.idt.net (Jeff Raben)
- **Date:** 1999-03-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36f90be3.9271174@news.idt.net>`
- **References:** `<36F8F167.E0645AA9@alcatel.be>`

```
steven <steven.vandenbosch@alcatel.be> wrote:

><!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
><HTML>
…[7 more quoted lines elided]…
><P>--

look at the picture clause  so that 0000010 will print as _____10.
pic ZZZZZZ9.

if the field is not numeric try the INSPECT verb. (old COBOL examine)

JR
and stir with a Runcible spoon...
```

#### ↳ Re: suppress leading zeroes

- **From:** matt <matt@500cc.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36F9A6D9.7F123057@500cc.com>`
- **References:** `<36F8F167.E0645AA9@alcatel.be> <36f90be3.9271174@news.idt.net>`

```
Or if you have a really old version of COBOL you could use the TRANSFORM verb

    EG

        TRANSFORM WS-DATA-NAME FROM ZERO TO SPACE.


Jeff Raben wrote:

> steven <steven.vandenbosch@alcatel.be> wrote:
>
…[17 more quoted lines elided]…
> and stir with a Runcible spoon...
```

##### ↳ ↳ Re: suppress leading zeroes

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-03-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36FA4AF7.FBDA7593@NOSPAMhome.com>`
- **References:** `<36F8F167.E0645AA9@alcatel.be> <36f90be3.9271174@news.idt.net> <36F9A6D9.7F123057@500cc.com>`

```
matt wrote:
> 
> Or if you have a really old version of COBOL you could use the TRANSFORM verb
…[3 more quoted lines elided]…
>         TRANSFORM WS-DATA-NAME FROM ZERO TO SPACE.

This was available for both ANSI 68 & ANSI 72, so in a shop which had
both, I didn't change EXAMINE to INSPECT, but instead changed EXAMINE to
TRANSFORM where I could.  I thought I was being smart, allowing the
programs to use the more stable verb!!!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
