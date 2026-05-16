[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol - Deleted Records

_2 messages · 2 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol - Deleted Records

- **From:** Joan Thompson <Joant@csionline.net>
- **Date:** 1999-11-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383B4680.784498F2@csionline.net>`

```
I'm using DataJunction to export MF Cobol data files to Fixed ASCII.
How do I determine which records are deleted in the source (MF Cobol)
files so I can skip exporting them?
```

#### ↳ Re: MF Cobol - Deleted Records

- **From:** "Glen Johnson" <glen@csisoft.com>
- **Date:** 1999-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hcT%3.2233$SO.115257@typhoon2.austin.rr.com>`
- **References:** `<383B4680.784498F2@csionline.net>`

```

Joan Thompson wrote in message <383B4680.784498F2@csionline.net>...
>I'm using DataJunction to export MF Cobol data files to Fixed ASCII.
>How do I determine which records are deleted in the source (MF Cobol)
>files so I can skip exporting them?
>


In I0 formated files, the record will be zeroed out.  In compressed formats,
the 0x20 bit of the first byte indicates the record is free.  For
uncompressed
I3 and I4 formats the first byte being 0x40 means used and 0x20 free.

                                                                        If I
remember right
                                                                        Glen
Johnson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
