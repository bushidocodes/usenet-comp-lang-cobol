[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error 196-S on MF COBOL 4.1

_2 messages · 2 participants · 1998-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Error 196-S on MF COBOL 4.1

- **From:** "mathew" <ua-author-18567@usenetarchives.gap>
- **Date:** 1998-08-11T05:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6qp1pt$dr$1@osprey.global.co.za>`

```
Hi

Perhaps someone can help me out here.

When compiling the following code on HP-UX 10.01 with Microfocus COBOL 3.2
I get no errors and the program compiles clean. I use the following
directives:

DG, ANS85, BOUND, DEFAULTBYTE"00", SPZERO, NOALTER, XREF, COPYLIST,
OPTIONAL-FILE, OLDBLANKLINE, SOURCEFORMAT"FREE", NODETECTLOCK,
ACCEPTREFTESH.

****************************************************************************
* Temporary area for building up a group of fields
03 ds-d pic x(260) value low-value.
03 ds-data redefines ds-d pic x(01) occurs 260.
03 ds-array redefines ds-data.
05 ds-fld-id pic x(02) comp-x.
05 ds-fld-lth pic x(02) comp-x.
05 ds-field pic x(256).
==> 05 ds-fld-data redefines ds-field
==> pic x(01)
==> occurs 1 to 256
==> depending on ds-fld-lth.
==> 05 ds-fld-data9 redefines ds-field
==> pic x(02) comp-x
==> occurs 1 to 128
==> depending on ds-fld-lth.
****************************************************************************
*

When compiling on HP-UX 10.20 with Microfocus COBOL 4.1 with the identical
directives as above I get an error 196-S which according to the manual is

0196 Redefinition of item containing an 'OCCURS DEPENDING ON' clause
Your selected flagging dialect does not support this.

Recode your program.

I know I could recode the OCCURS clause without the DEPENDING clause
but that would only be done as a last resort.

The manuals are a bit cryptic when trying to work out how to solve this.

Any help will be greatly appreciated.

Regards
Mathew

P.S remove the "1" from "msevitz1" for e-mail.
```

#### ↳ Re: Error 196-S on MF COBOL 4.1

- **From:** "as-..." <ua-author-17074031@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9b9ef72b1b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6qp1pt$dr$1@osprey.global.co.za>`
- **References:** `<6qp1pt$dr$1@osprey.global.co.za>`

```
Mathew schrieb:


› ****************************************************************************
› 
…[3 more quoted lines elided]…
›      03  ds-array redefines ds-data.

first error, should be

03 ds-array redefines ds-d.


› 05 ds-fld-id pic x(02) comp-x.
› 05 ds-fld-lth pic x(02) comp-x.
› 05 ds-field pic x(256).

next change: 05 ds-field.
10 ds-fld-data PIC X occurs 256 times.
05 ds-field2 redefines ds-field.
10 ds-fld-data9 PIC XX COMP-X occurs 128 times.


that should be worked fine!

Greatings

AS
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
