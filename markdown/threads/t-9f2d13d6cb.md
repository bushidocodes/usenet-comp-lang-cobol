[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DEC COBOL FMS - Negative Decimal Point Numbers

_3 messages · 3 participants · 1997-10_

---

### DEC COBOL FMS - Negative Decimal Point Numbers

- **From:** "jimmy sugrue" <ua-author-12763052@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bcdee3$d9e46e20$d42d7dc2@default>`

```

How do you get FMS to accept negative decimal point numbers?

I have used the form field specification of 'NNNNNN.NNNNN' to
accept a pic field of 9(6)V9(4)-.

This works OK if the last character entered is '-'. eg 124.3456-

However, if you enter the minus any where else in the field the form
does not reject the data entered and generates a spurious value.

The field is required to accept both plus and minus values.

I would be greatful to anyone who can answer the above or point me
to somewhere I can get support on FMS.
```

#### ↳ Re: DEC COBOL FMS - Negative Decimal Point Numbers

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-10-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9f2d13d6cb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdee3$d9e46e20$d42d7dc2@default>`
- **References:** `<01bcdee3$d9e46e20$d42d7dc2@default>`

```

In article <01bcdee3$d9e46e20$d42d7dc2@default>,
"Jimmy Sugrue" wrote:
› 
› How do you get FMS to accept negative decimal point numbers?
› [...]
› I would be grateful to anyone who can answer the above or point me to
› somewhere I can get support on FMS.

There might be someone who knows VAX FMS on comp.os.vms.

The only manual I have on FMS is "How to Convert VAX FMS to DECForms",
and it does not answer your question.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: DEC COBOL FMS - Negative Decimal Point Numbers

- **From:** "wr..." <ua-author-17072575@usenetarchives.gap>
- **Date:** 1997-10-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9f2d13d6cb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bcdee3$d9e46e20$d42d7dc2@default>`
- **References:** `<01bcdee3$d9e46e20$d42d7dc2@default>`

```

"Jimmy Sugrue" muttered:

__How do you get FMS to accept negative decimal point numbers?
__
__I have used the form field specification of 'NNNNNN.NNNNN' to
__accept a pic field of 9(6)V9(4)-.

The trick is to declare the FMS field as a string, then
parse it in a UAR. You have to check and measure the string
and bounce a success or failure condition back to your program
"Daddy, what does 'formatting drive C:' mean"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
