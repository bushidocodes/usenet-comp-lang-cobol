[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Student - packed decimal - Net Express

_1 message · 1 participant · 1999-10_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Re: Student - packed decimal - Net Express

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bf1041$724c60b0$0100007f@vaagshaugen>`
- **References:** `<37fbaf89.8279142@nntp.xsite.net> <1kIK3.1773$eM4.147804@typ11.nn.bcandid.com> <37fd8c11.693046@nntp.xsite.net>`

```
zennmaster <zenn@master.net> wrote in article
<37fd8c11.693046@nntp.xsite.net>...
> Thanks all, for your insights and answers. 
> 
…[21 more quoted lines elided]…
> remarkable - byte count remains the same.       Any ideas?

Ken Foskey's posting should point you in the right direction.  Here is a
more detailed explanation.  I am sure it has been covered numerous times in
various news groups.

The file transfer programs between MVS and the PC world can either transfer
in binary mode (each byte transfers unaltered) or in text mode (each byte
is translated to/from ASCII/EBCDIC code).  The trouble is the PIC 9(5)V99
COMP-3 fields.  These are in packed decimal representation, i.e. each byte
contains 2 decimal digits in BCD code, the last byte contains 1 digit and
the sign.  If your field has the value 12345.67 it is represented as 4
bytes with hex values 12 34 56 7F.  If transferred as text from MVS to PC,
each byte is translated (the translate table depends on the character set
used on each side).  Certain values may cause particular trouble, for
example being confused with control characters like CarriageReturn,
LineFeed, Tab, and others.  The result is generally unusable.  You have two
alternatives. 1: transfer in binary mode.  No translation takes place, you
must interpret all data as is (text fields are still in EBCDIC code).  Or
2: convert packed decimal fields to numeric display fields (unpacked) on
the MVS side before transferring, and transfer as text.  All data (also
numeric fields) will come through as ASCII coded text.  If you have defined
binary fields, they must be treated in a similar way.

Hope this helps.

Gunnar.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
