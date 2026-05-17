[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# THIS IS NOT HOMEWORK !!! I would like to read some experts code

_3 messages · 2 participants · 1997-03_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### THIS IS NOT HOMEWORK !!! I would like to read some experts code

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-03-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5h1nre$nre@sjx-ixn4.ix.netcom.com>`

```

This is an exersize for me to get a chance to read (hopefully :) several versions of code to
solve the same problem.

First: This is NOT homework, It was but that was a while ago and I got it done without an
problems.

The Problem : A customer number 5 digits and a check digit of 1 digit.
use modulo 11 to figure the check digit then compare. return valid/invalid response.

modulo 11 is figured as follows multiply each of the digits of the customer num. from left to
right by the numbers 6,5,4,3,2 add the results divide by 11 with remainder, subtract remainder
from 11 giving check digit.


Ok, so your all confused now real example:
cust-num 11111 check digit 2
65432
= 20 divided by 11 giving remainder = 9
subtract 9 from 11 = 2
check digit = 2


Ther following data set contains both valid and invalid check digits

11111 2
79200 4
01000 6
02340 2
02340 0
99999 7

I will post my solution later this evening and Thanks for "Playing" :)

Greg Amos
amo··.@ix.··m.com
```

#### ↳ Re: THIS IS NOT HOMEWORK !!! I would like to read some experts code

- **From:** "pdu..." <ua-author-1262469@usenetarchives.gap>
- **Date:** 1997-03-22T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1c522bae8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5h1nre$nre@sjx-ixn4.ix.netcom.com>`
- **References:** `<5h1nre$nre@sjx-ixn4.ix.netcom.com>`

```

Gregory,

The problem was interesting, but I found a flaw in the concept. You
are looking for a check DIGIT, which I take to mean a single number.
Using Modulo 11, your remainder could be 0 thru 10. This means that
your check DIGIT might be 11 or 10 which aren't single Digits.

Just thought I would HELP,

Paul



Gregory Paul Amos wrote:

› This is an exersize for me to get a chance to read (hopefully :) several versions of code to
› solve the same problem.
…[32 more quoted lines elided]…
› amo··.@ix.··m.com
```

##### ↳ ↳ Re: THIS IS NOT HOMEWORK !!! I would like to read some experts code

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-03-22T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1c522bae8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1c522bae8-p2@usenetarchives.gap>`
- **References:** `<5h1nre$nre@sjx-ixn4.ix.netcom.com> <gap-e1c522bae8-p2@usenetarchives.gap>`

```

In article <3334da57.16610277@news>,
pdu··.@w··.com (Paul DuBois) wrote:

› Gregory,
› 
…[8 more quoted lines elided]…
› 

Paul, Thanks for the flaw, this question was a call program for a larger lab that passed the
cust_num, check_digit,and a message flag to be used for a valid or invalid response. I looked at
the 10 or 11 problem but it was handled by truncating to a single digit. Why? Don't ask me this
was the instructors requirements and in his example ( really 1/2 of the calling program the
check_digit was in fact just 1 digit.
Greg

› 
› 
…[39 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
