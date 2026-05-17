[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol2C-Converter

_2 messages · 2 participants · 1996-11_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Cobol2C-Converter

- **From:** "m..." <ua-author-17086883@usenetarchives.gap>
- **Date:** 1996-11-13T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56f0d9$1o8@actisl.actis.de>`

```

Hello,

I'searching for a Cobol to C Converter. Can anyone give me an adress or a company-name???

Thanx for your help!

Michael Stricker
Michael Stricker     Actis Berlin         E-Mail: m.··.@ac··s.de
Service und Support
** If I get a pence for every message  **
** in MS-Windows, I would be richer than Bill Gates!       **
```

#### ↳ Re: Cobol2C-Converter

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-11-14T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4b6f9fe17e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<56f0d9$1o8@actisl.actis.de>`
- **References:** `<56f0d9$1o8@actisl.actis.de>`

```

In message <<56f0d9$1.··.@act··s.de>> m.··.@ac··s.de writes:
›
› I'searching for a Cobol to C Converter. Can anyone give me an adress or a company-name???


In the cases that I have seen a code converter from Cobol to C
changes passable Cobol code into absolutely awful C code.

Many would think that one would wind up with a C program,
but in fact, the results are bound to be a Cobol program
implemented in bad C.

If you are wanting to do this because you think that C is
more easily maintained than Cobol, think again. It will
still be the Cobol form and structure.

If you think that converting it to C will improve performance,
think again. The Cobol code will cater for up to 18 numeric
digits. The converted code (to do the same job) will have to
use a numeric package based on decimal, packed decimal and
binary variable length fields. It will likely be slower.

If you think converting it to C will make it more portable,
think again. C is considerably less portable.

If you think C is more 'modern', well maybe, but why convert
from a 35 year old language to a 25 year old one ? The
rest of the world has moved from Pascal to C to C++ to Delphi
to Ada and now is in a stampede to Java.

Meanwhile Cobol is still Cobol and just carries on getting the
job done.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
