[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cannot open file oldnames.lib??

_2 messages · 2 participants · 2001-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### cannot open file oldnames.lib??

- **From:** KNeddy@home.com
- **Date:** 2001-11-03T03:26:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3be36b2b.49084748@NEWS>`

```
I purchased Teach yourself cobol in 24 hours.
I created a cobol program that makes use of the cgisetup, cgiread and
cgiwritr  prog's. I got a clean compile and attempted to link and
received an error that said "3 unresolved externals". I read further
on down through the cgi guide and noticed it said I have to link the
file cgiwin32.obj.  I thought to myself, this must be where the three
externals reside. I took the cgiwin32.obj file and moved it into the
folder where my program resided (for convenience mostly) and attempted
to link. It seemed to correct the unresolved externals error, but I
get the following error.

cannot open file oldnames.lib.

I looked for a file named oldnames.lib on my PC and I am unable to
locate it. I'm guessing that the cgiwin32.obj file makes use of this
lib, however I don't know where it is and I'm stuck.  Any suggestions?

Kevin.
```

#### ↳ Re: cannot open file oldnames.lib??

- **From:** chris.glazier@microfocus.com (Chris Glazier)
- **Date:** 2001-11-05T08:56:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<260cd566.0111050856.175dce5e@posting.google.com>`
- **References:** `<3be36b2b.49084748@NEWS>`

```
This is a file which is included with the Microsoft Visual C/C++
product. It is a library which maps older function names (16-bit) to
the new function names of Visual C/C++ 6.0.


KNeddy@home.com wrote in message news:<3be36b2b.49084748@NEWS>...
> I purchased Teach yourself cobol in 24 hours.
> I created a cobol program that makes use of the cgisetup, cgiread and
…[15 more quoted lines elided]…
> Kevin.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
