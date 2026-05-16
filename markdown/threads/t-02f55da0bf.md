[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Arithmetic operations using DFSORT

_2 messages · 2 participants · 2006-01_

---

### Arithmetic operations using DFSORT

- **From:** "mftips@gmail.com" <mftips@gmail.com>
- **Date:** 2006-01-24T21:20:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1138166439.379334.206290@f14g2000cwb.googlegroups.com>`

```
Using DFOSRT, we can perform arithmetic operations on input fields.

OUTFIL OUTREC now allows you to combine fields, decimal constants (+n
and -n), operators (MIN, MAX, MUL, DIV, MOD, ADD, SUB) and parentheses
to form arithmetic expressions, and place the results in your records
as BI, FI, PD, ZD, FS or edited CH values.

Syntax:
term,operator,term<,operator,...>

Where:
Term is a field (Start position, Number of characters, Format) or a
decimal constant (+n or -n). You can use BI, FI, PD, PD0, ZD, FS, DTn
and

Operator is MIN (minimum), MAX (maximum), MUL (multiplication), DIV
(division), MOD (modulus), ADD (addition) or SUB (subtraction).

The order of evaluation precedence for the operators is as follows
unless it is changed by parentheses:
1. MIN and MAX
2. MUL, DIV and MOD
3. ADD and SUB

The intermediate or final result of a DIV operation is rounded down to
the nearest integer. The intermediate or final result of a MOD
operation is an integer remainder with the same sign as the dividend.
If an intermediate or final result of an arithmetic expression
overflows 15 digits, the overflowing intermediate or final result will
be truncated to 15 digits. If an intermediate or final result of an
arithmetic expression requires division or modulus by 0, the
intermediate or final result will be set to 0.

Example 1: [(First 2 digits) * (-10)] + 10, and the output is formatted
by edit mask (M0 - M26), and is truncated to a length of 5

//SYSIN DD *
SORT FIELDS=(1,2,CH,A)
OUTREC FIELDS=(1,3,
(1,2,ZD,MUL,-10,ADD,+10),M6,LENGTH=5,
15X)
//*

Example 2, Divide the first field (positions 1, 2) by the second field
(position 3), and the output is converted to packed decimal format

//SYSIN DD *
SORT FIELDS=(1,2,CH,A)
OUTREC FIELDS=(1,3,
(1,2,ZD,DIV,3,1,ZD),TO=PD,
15X) 
//*
 
Thanks,
MFTIPS
http://mftips.blogspot.com/
```

#### ↳ Re: Arithmetic operations using DFSORT

- **From:** Colin Campbell <cmcampb@adelphia.net>
- **Date:** 2006-01-25T22:29:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D9idnfUuubSu8UXenZ2dnUVZ_t-dnZ2d@adelphia.com>`
- **In-Reply-To:** `<1138166439.379334.206290@f14g2000cwb.googlegroups.com>`
- **References:** `<1138166439.379334.206290@f14g2000cwb.googlegroups.com>`

```
Wow!  I guess we don't need (mainframe) COBOL any more, do we?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
