[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compact Decimals

_4 messages · 4 participants · 1997-06_

---

### Compact Decimals

- **From:** "lisa cramer" <ua-author-17071453@usenetarchives.gap>
- **Date:** 1997-06-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33AAA772.16A4@access.ohio.gov>`

```

Currently in a conversion process. Can anyone let us know what the
packed decimal value for S9(6)V99 COMP -- the actual physical length of
this field. Another example we need to clarify would be S9(4).

Thanks,
Lisa

Please email cra··.@acc··o.gov
```

#### ↳ Re: Compact Decimals

- **From:** "jya..." <ua-author-6589456@usenetarchives.gap>
- **Date:** 1997-06-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-11eeb75ad9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33AAA772.16A4@access.ohio.gov>`
- **References:** `<33AAA772.16A4@access.ohio.gov>`

```

Lisa Cramer (cra··.@acc··o.gov) wrote:
: Currently in a conversion process. Can anyone let us know what the
: packed decimal value for S9(6)V99 COMP -- the actual physical length of
: this field. Another example we need to clarify would be S9(4).
: Thanks,
: Lisa
: Please email cra··.@acc··o.gov
-----------------------------------

In IBM Cobol:

The physical length of a packed decimal item is always:

Number of digits (rounded up to an odd number), then add 1 and
divide the answer by two. A decimal point in the picture has no
effect on this formula.

Packed decimal is COMP-3. The picture that you show is COMP, which
is pure binary and follows a different formula:

Number of digits in the Picture Bytes required

1-4 2
5-9 4
10-18 8

S9(4) uses 4 bytes (the sign part of the right-hand digit).
```

#### ↳ Re: Compact Decimals

- **From:** "ron schnatzmeyer" <ua-author-17073177@usenetarchives.gap>
- **Date:** 1997-06-19T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-11eeb75ad9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33AAA772.16A4@access.ohio.gov>`
- **References:** `<33AAA772.16A4@access.ohio.gov>`

```

› Currently in a conversion process. Can anyone let us know what the
› packed decimal value for S9(6)V99 COMP -- the actual physical length of
› this field. Another example we need to clarify would be S9(4).


Well first of all S9(6)V99 COMP is binary not packed. On an IBM mainframe
computer this would be a 4 byte field. Since you didn't specify any usage
for S9(4) it is impossible to tell how many bytes. No specified usage
defaults
to USAGE DISPLAY which would be 4 bytes.

Some basic rules:
A picture clause defines the number if digits NOT the number of bytes.
In the case of binary the trunc compiler options can modify this...look
up
the specifics in your manual.
Calculating bytes in numeric fields:
If the USAGE IS DISPLAY then digits = bytes.
If the USAGE IS COMP (binary) on IBM mainframes
then 1 to 4 digits is 2 bytes, 5 to 9 digits is 4 bytes, 10 to 18
digits is 8 bytes
If the USAGE IS COMP-3 (packed decimal)
then bytes = (number of digits / 2) + 1 and then drop the
remainder.
So if you had asked about S9(6)V99 COMP-3 this would be
an eight digit field with 2 decimal positions (8 / 2) + 1 = 5
bytes
Packed fields should always be defined as an odd number also. An
even number leaves an unused half-byte causing various
inefficiencies.
If this were S9(7)V99 it would be (9 / 2) + 1 = 5 bytes - drop the
remainder.

-Ron
```

#### ↳ Re: Compact Decimals

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-06-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-11eeb75ad9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<33AAA772.16A4@access.ohio.gov>`
- **References:** `<33AAA772.16A4@access.ohio.gov>`

```

Lisa Cramer wrote:
›
› Currently in a conversion process. Can anyone let us know what the
› packed decimal value for S9(6)V99 COMP -- the actual physical length of
› this field. Another example we need to clarify would be S9(4).
›

Lisa

What you have specified above is not packed decimal. I am making the
assumption here that you have a version of IBM aminframe COBOL. The
USAGE of COMP is for binary fields and four digits will give you the
halfword (2 bytes) while eight digits, or even some nine digit fields,
will be contained in the fullword (4 bytes).

Depending on the age and version of the program, these fields can also
be aligned on the halfword and fullword boundaries which means that the
halfword can actually take up three bytes with the slack
byte,
and the fullword could have as many as three slack bytes
leading it.

Generally speaking, don't worry about the slack bytes if you're only
interested in the source code. This consideration only comes into play
if you're getting into the execution code.

Charles

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
