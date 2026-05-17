[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# BCD

_1 message · 1 participant · 1995-02_

---

### BCD

- **From:** "colin..." <ua-author-5711152@usenetarchives.gap>
- **Date:** 1995-02-21T17:33:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8A3F585.09D200061F.uuout@almac.co.uk>`

```
JP> What I am asking is if BCD is BCD is BCD or are there other flavors

You've already had some answers. Here's another way of looking at it.

Packed numbers are IBM's implementation of BCD on 360 architecture
machines. Each quartet is indeed BCD but the least significant quartet
is reserved for a coded sign. The way IBM's firmware converts unsigned,
unpacked to packed leaves an 'F' in it. After arithmetic it will be
converted to a 'C' for + or 'D' for -. Assembler programmers then have
to convert it back to an 'F' if they need it unsigned; high-level
programmers get it done for them by the compiler.

Unpacked numbers are the EBCDIC printable character codes. Here each
byte is a sign quartet 'F' and a zone quartet which just happens to be
the same as the BCD. A little quirk allows the rightmost digit to have
coded an 'overpunch' sign [I'll explain the 12-row codes on 80-column
cards another time if you like] which is the 'C' or 'D' as above.

A side effect of this is on utilities like sorts. You can't just use the
plain value - you have to tell the sort it's packed decimal otherwise
the results are in the wrong order. On IBM X'0F' and X'0C' are,
therefore, the same. On HP3000 they used to be different.
---
* RM 1.3 00712 * Watership Down, Read the book, seen film, now eat the pie..
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
