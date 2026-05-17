[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Inspecting file structures

_2 messages · 2 participants · 1997-11_

---

### Inspecting file structures

- **From:** "fr..." <ua-author-17072884@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<65h2c3$8i@flumux.hamburg.netsurf.de>`

```

We try to build some kind of generic file conversion tool which is able
to determine automatically the structure of a given file and convert all
numeric values to display format. Because we don't want to specify for
each input file the record description manually the tool have to be smart
enough to analyze the record type by itself.
Our current approach is to let the tool parse a source file containing
an appropriate record description and deduce the type of a read record
from this parsing. This should work fine for us as long as the record
description doesn't contain any redefines clause. But, how could we handle
this kind of files? Any solution ideas? Does anyone know a tool for
this kind of file conversion?

Any suggestions are appreciated.

- Frank

Fra··.@Ham··f.de
```

#### ↳ Re: Inspecting file structures

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-11-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d12d2b1a1c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<65h2c3$8i@flumux.hamburg.netsurf.de>`
- **References:** `<65h2c3$8i@flumux.hamburg.netsurf.de>`

```



Frank Froese wrote in article
<65h2c3$8.··.@flu··f.de>...
› We try to build some kind of generic file conversion tool which is able
› to determine automatically the structure of a given file and convert all
…[12 more quoted lines elided]…
›  

Without the FD you cannot do this. A field with spaces in it might be a
comp field with 2020 in it. (4040 in ebcdic).

You can't do this with any reliability.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
