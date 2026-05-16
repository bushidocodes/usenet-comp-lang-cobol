[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CONVERTION DECIMAL IN PACKED NUMBERS

_3 messages · 3 participants · 1999-01_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### CONVERTION DECIMAL IN PACKED NUMBERS

- **From:** amonaci@protec.it (Andrea Monaci)
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** alt.cobol,alt.lang.awk,comp.lang.awk,comp.lang.cobol,fj.lang.awk,fj.lang.cobol,fj.lang.misc
- **Message-ID:** `<36b18fda.1215819@news.interbusiness.it>`

```
HI

How does you become to convert  by hand a decimal number in a Packed decimal
or BCD (Binary Coded Decimal) number?

THANKS

BYE



Andrea Monaci

My address is:

Via A.Gramsci N. 96
C.A.P.: 35010 Cadoneghe (Padova) (Italy)
Tel/Fax: 0039-049700637
E-Mail: amonaci@protec.it
```

#### ↳ Re: CONVERTION DECIMAL IN PACKED NUMBERS

- **From:** Warren Porter <warrenp@ASPMnetdoor.com>
- **Date:** 1999-01-29T00:00:00
- **Newsgroups:** alt.cobol,alt.lang.awk,comp.lang.awk,comp.lang.cobol,fj.lang.awk,fj.lang.cobol,fj.lang.misc
- **Message-ID:** `<36B1C768.710F2840@ASPMnetdoor.com>`
- **References:** `<36b18fda.1215819@news.interbusiness.it>`

```
Andrea Monaci wrote:

> How does you become to convert  by hand a decimal number in a Packed decimal
> or BCD (Binary Coded Decimal) number?

I assume you will be doing this in something other than COBOL.  Each byte
(except possibly the last) contains two digits while the low order byte last 4
bit positions may contain a sign.  In general, to get the first digit, divide
the byte by 16 or shift to the right by 4 bits.  To get the low order digit, AND
the byte by 15 (x'0F') or mod the byte by 16.  HTH.

If the field is signed, the sign will be in the rightmost 4 bits.  On some
machines 15 is unsigned (or positive), 12 is positive, and 13 is negative, but,
"Your milage may vary".
```

#### ↳ Re: CONVERTION DECIMAL IN PACKED NUMBERS

- **From:** "stcheong" <stcheong@mbox2.singnet.com.sg>
- **Date:** 1999-01-30T00:00:00
- **Newsgroups:** alt.cobol,alt.lang.awk,comp.lang.awk,comp.lang.cobol,fj.lang.awk,fj.lang.cobol,fj.lang.misc
- **Message-ID:** `<78u9c2$slm$1@mawar.singnet.com.sg>`
- **References:** `<36b18fda.1215819@news.interbusiness.it>`

```
How about dropping the first 4 bytes of both numeric values and joining them
back together.
Hope it works.

Andrea Monaci wrote in message <36b18fda.1215819@news.interbusiness.it>...
>HI
>
>How does you become to convert  by hand a decimal number in a Packed
decimal
>or BCD (Binary Coded Decimal) number?
>
…[13 more quoted lines elided]…
>E-Mail: amonaci@protec.it
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
