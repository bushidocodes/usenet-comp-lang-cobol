[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Moving variable

_8 messages · 8 participants · 1997-05_

---

### Moving variable

- **From:** "kwok-ho" <ua-author-7158421@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<338C4856.3EC1@netvigator.com>`

```

Hi,

I want to move an alphanumeric variable X(6) which read
from a seauential file to a non-integer numeric field 9(4)V99.
The alphanumeric variable is checked before moved, but it
doesn't work.

Would you help me to solve this problem? Thanks!

Regards
=================================
            Kwok-ho
 E-mail: kwo··.@net··r.com
=================================
```

#### ↳ Re: Moving variable

- **From:** "dbryant" <ua-author-575626@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a77efe68e5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<338C4856.3EC1@netvigator.com>`
- **References:** `<338C4856.3EC1@netvigator.com>`

```

Kwok-ho writes:

› I want to move an alphanumeric variable X(6) which read
› from a seauential file to a non-integer numeric field 9(4)V99.
› The alphanumeric variable is checked before moved, but it
› doesn't work.


In Wang COBOL this would be done with one of their nifty
language extentions...

MOVE WITH CONVERSION alpha-var TO numeric-var.

In your case you would probably have to do it thru a REDEFINES

01 alpha-var PIC X(6).
01 numeric-var REDEFINES alpha-var
PIC 9(04)V99.

MOVE alpha-var TO numeric-var.
```

#### ↳ Re: Moving variable

- **From:** "jt..." <ua-author-17073095@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a77efe68e5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<338C4856.3EC1@netvigator.com>`
- **References:** `<338C4856.3EC1@netvigator.com>`

```

In , dbr··.@net··m.com (David K. Bryant) writes:
› Kwok-ho  writes:
› 
…[18 more quoted lines elided]…
› 
A redefines simply gives to different definitions to the same storage location. In your example the move statement would produce wierd results, the move statement would be moving an integer to a decimal field so that the results would be in effect multiplied by 100. The fact that your sending and receiving fields are the same could possibly result in changing the sending field as the move progressed.

The redefines gives you the ability to access data in either of two formats. If the field coming in from the sequential file contains a decimal point you would have to write a routine to parse the field. If the decimal place simply implied then a redefines is all that is necessary.
```

#### ↳ Re: Moving variable

- **From:** "h..." <ua-author-16374103@usenetarchives.gap>
- **Date:** 1997-05-28T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a77efe68e5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<338C4856.3EC1@netvigator.com>`
- **References:** `<338C4856.3EC1@netvigator.com>`

```

On Wed, 28 May 1997 22:59:34 +0800, Kwok-ho
wrote:

› Hi,
› 
…[3 more quoted lines elided]…
› doesn't work.

move x(6) to 9(6)
move 9(6) to 9999v99, but beware of overrun.
perhaps move 9(6) to 9(6)v99 and divide by 100?

If there is a decimal point in your x(6) string, it gets more
complicated.

H
```

#### ↳ Re: Moving variable

- **From:** "charles goodman" <ua-author-901347@usenetarchives.gap>
- **Date:** 1997-05-28T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a77efe68e5-p5@usenetarchives.gap>`
- **In-Reply-To:** `<338C4856.3EC1@netvigator.com>`
- **References:** `<338C4856.3EC1@netvigator.com>`

```

Kwok-ho wrote:
› 
› Hi,
…[5 more quoted lines elided]…
› 

01 IN-FIELD PIC X(6).

01 OUT-FIELD.
05 OUT-NUMERIC PIC 9(4)V99.

MOVE IN-FIELD TO OUT-FIELD.

This tells the compiler to move the six bytes. You then refer to
OUT-NUMERIC to treat the result as a numeric field.

Charlie Goodman
```

#### ↳ Re: Moving variable

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-05-28T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a77efe68e5-p6@usenetarchives.gap>`
- **In-Reply-To:** `<338C4856.3EC1@netvigator.com>`
- **References:** `<338C4856.3EC1@netvigator.com>`

```

In message <<338··.@net··r.com>> Kwok-ho writes:
› 
› I want to move an alphanumeric variable X(6) which read
› from a seauential file to a non-integer numeric field 9(4)V99.
› The alphanumeric variable is checked before moved, but it
› doesn't work.

MicroFocus has supported de-editing moves for decades.

01 Source-Edited PIC --9.99.
01 Destination-Numeric PIC S9(4)V99.

MOVE Source-Edited TO Destination-Numeric

You may need to use a $SET DE-EDIT"1" compiler option.
```

##### ↳ ↳ Re: Moving variable

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-05-28T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a77efe68e5-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a77efe68e5-p6@usenetarchives.gap>`
- **References:** `<338C4856.3EC1@netvigator.com> <gap-a77efe68e5-p6@usenetarchives.gap>`

```

Richard Plinston wrote:
› 
› In message <<338··.@net··r.com>> Kwok-ho  writes:
…[13 more quoted lines elided]…
› You may need to use a $SET DE-EDIT"1" compiler option.

A de-edited MOVE was made part of the standard in 1985 (maybe not
decades, but at least one decade). There is no need for any compiler
options and it works on almost every compiler there is. However, I
don't think his input corresponds quite to what you stated. Perhaps
he has random decimal points and whatnot in his sender. Or, it might
be something like PIC -----9. That is, no decimal. The safest way is
to use the NUMVAL function (like COMPUTE destination-numeric =
FUNCTION NUMVAL (source-field)). I did a COMPUTE instead of a MOVE
because of the dumb rule in the standard that you can use a numeric
function only in an arithmetic expression (that rule is gone from the
next standard, whatever number it will be).

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: Moving variable

- **From:** "flashback" <ua-author-6590555@usenetarchives.gap>
- **Date:** 1997-05-29T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a77efe68e5-p8@usenetarchives.gap>`
- **In-Reply-To:** `<338C4856.3EC1@netvigator.com>`
- **References:** `<338C4856.3EC1@netvigator.com>`

```


On 28.05.97 kwo··4@net··r.com wrote some lines reffering to
"Moving variable":

howdy,
› 
› 
…[8 more quoted lines elided]…
› 
1. please post the definitions of the two fields and the code-fragment,
where you check the x-field and move it into the num-field

2. take a look at the REDEFINES-clause

regards

gregor

public key available

what's puzzlin' you, is the nature of my game......


## CrossPoint v4.00 R ##
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
