[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF: S9(n) representation

_2 messages · 2 participants · 1999-03_

---

### MF: S9(n) representation

- **From:** Stephan Eichenlaub <stephan@uni-koblenz.de>
- **Date:** 1999-03-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E09095.425CB692@uni-koblenz.de>`

```
Hi out there,

I'm trying to convert data from the S9(n) respectively S9(n)V99 format.
The data is lying on an old HP-UX 3000 machine, the database TurboImage
and the program written with MicroFocus Cobol.

I found out so much:
- It is an ASCII format, one byte per decimal digit. '1' stands for 1 -
and so on.
- The number of decimals before and behind the dot is merely
interpretion by
  code, it is not contained in the data itself.
- The last byte represents both a number and the sign.

Question: How does that last byte work?

Thanks, Stephan
```

#### ↳ Re: MF: S9(n) representation

- **From:** Peter W. Smith <Peter_W._Smith@LNOTES3.bankofny.com>
- **Date:** 1999-03-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7c1n9h$14m$1@nnrp1.dejanews.com>`
- **References:** `<36E09095.425CB692@uni-koblenz.de>`

```
In article <36E09095.425CB692@uni-koblenz.de>,
  Stephan Eichenlaub <stephan@uni-koblenz.de> wrote:
> Hi out there,
>
…[15 more quoted lines elided]…
>
I'm not sure about the ASCII codes but generally speaking the high order half
byte is the number 0 - 9 and the low order half byte is the sign F unsigned or
D negative  C positive, at least that's how it works in EBCDIC

*************************************************************
*  He's thinking for himself, quick, hit him with a stick.  *
*************************************************************

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
