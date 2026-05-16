[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Multi-threaded programing in MF COBOL

_3 messages · 2 participants · 2000-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Multi-threaded programing in MF COBOL

- **From:** "e-GOista" <kenka@polbox.com>
- **Date:** 2000-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iT865.60970$DC.1411255@news.tpnet.pl>`

```
How organize access to file from threads?

Any remarks and advises.

Wieslaw Sawicki
kenka@polbox.com
```

#### ↳ Re: Multi-threaded programing in MF COBOL

- **From:** "Ken Mullins" <**Ken**Mullins**@**mindspring.com** remove **'s>
- **Date:** 2000-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jb8hg$h5f$1@nntp9.atl.mindspring.net>`
- **References:** `<iT865.60970$DC.1411255@news.tpnet.pl>`

```
mutexes, semaphore, etc

kenmullins

"e-GOista" <kenka@polbox.com> wrote in message
news:iT865.60970$DC.1411255@news.tpnet.pl...
> How organize access to file from threads?
>
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Multi-threaded programing in MF COBOL

- **From:** Stephen Gennard <stephen.gennard@merant.com>
- **Date:** 2000-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3959B603.24063623@merant.com>`
- **References:** `<iT865.60970$DC.1411255@news.tpnet.pl> <8jb8hg$h5f$1@nntp9.atl.mindspring.net>`

```
Ken Mullins wrote:

> mutexes, semaphore, etc
>
…[12 more quoted lines elided]…
> >

You should also have a read of the multi-threading section in the documentation,
especially the bits on "reentrant programs/Using Data Attributes/Using
Synchronization Primitives".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
