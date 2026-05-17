[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM VS-COBOL II & DBCS

_2 messages · 2 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM VS-COBOL II & DBCS

- **From:** "dw..." <ua-author-514328@usenetarchives.gap>
- **Date:** 1998-07-27T07:41:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6php0h$1gf$1@nnrp1.dejanews.com>`

```
I was wondering if someone could answer this simple question for me. With IBM
VS-COBOL II, it supports DBCS characters by defining the PICTURE clause with
PIC G(xx). I was wondering whether you can interchange SBCS and DBCS types
like the following:

10 FOO PIC G(5).
10 BAR PIC X(10).
10 FOOBAR PIC G(5).

MOVE FOO TO BAR.
MOVE BAR TO FOOBAR.

(FOO = FOOBAR in value)

Would this actually work with BAR being an intermediate data item or would I
get a compiler error?

Please respond by posting or emailing to dw··.@my-··s.com.

Thanks,

Daniel S. Wong

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

#### ↳ Re: IBM VS-COBOL II & DBCS

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-07-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e3e9f1d9df-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6php0h$1gf$1@nnrp1.dejanews.com>`
- **References:** `<6php0h$1gf$1@nnrp1.dejanews.com>`

```
Look in the COBOL programming guide for some callable routines.for doing
this conversion. (I can't remember their names off the top of my head and
don't have the documentation handy.) They do, however, do exactly the
conversion that you want.

P.S. With VS COBOL II, I think you need to say Display-1 with a PIC
G item. With the newer COBOL for this-and-that compilers, you do NOT need
to specify any special USAGE when you use the PIC N replacements for PIC G
(PIC N is also what the next COBOL Standard uses).

Let me know if you have any trouble finding the conversion routines and I'll
try and get their exact IGZ.... names for you.

dw··.@my-··s.com wrote in message <6php0h$1gf$1.··.@nnr··s.com>...
› I was wondering if someone could answer this simple question for me.  With
› IBM
…[25 more quoted lines elided]…
› http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
