[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL compilers.

_3 messages · 2 participants · 2002-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL compilers.

- **From:** Simon Jenkins <seaslug.mk2@btopenworld.com>
- **Date:** 2002-10-15T22:02:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DAC90CF.8158C9A0@btopenworld.com>`

```
After many years of not programming I'd like to get back into cobol, and
need a compiler.  I'm not specifically looking for a free one, but I
don't want one that needs run-time licences.  It looks like the best is
Fujitsu; can anyone tell me if it supports dynamic file access on a PC?
Fujitsu's website doesn't make this clear (to me at least).

Thanks in advance,

Simon        seaslug.mk2 (at) btopenworld.com
```

#### ↳ Re: COBOL compilers.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-10-15T17:18:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itucnbkcHPfMCTGgXTWc3Q@News.GigaNews.Com>`
- **References:** `<3DAC90CF.8158C9A0@btopenworld.com>`

```

"Simon Jenkins" <seaslug.mk2@btopenworld.com> wrote in message
news:3DAC90CF.8158C9A0@btopenworld.com...
> After many years of not programming I'd like to get back into cobol, and
> need a compiler.  I'm not specifically looking for a free one, but I
…[6 more quoted lines elided]…
> Simon        seaslug.mk2 (at) btopenworld.com

There's no need to make it clear - it should be a given.

If you mean
    SELECT MYFILE ASSIGN TO FILENAME
        ORGANIZATION IS INDEXED
        ACCESS IS DYNAMIC
        ...

The answer is: (wait for it now....) Yes.

Fujitsu's compiler is fully COBOL-85 compliant. It is not 'stripped-down' or
'crippled' or 'limited' in any way.
```

##### ↳ ↳ Re: COBOL compilers.

- **From:** Simon Jenkins <seaslug.mk2@btopenworld.com>
- **Date:** 2002-10-15T22:42:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DAC9A3A.A39A6E8E@btopenworld.com>`
- **References:** `<3DAC90CF.8158C9A0@btopenworld.com> <itucnbkcHPfMCTGgXTWc3Q@News.GigaNews.Com>`

```


JerryMouse wrote:

>
>
…[3 more quoted lines elided]…
> 'crippled' or 'limited' in any way.

Many Thanks.

Simon       seaslug.mk2 (at) btopenworld.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
