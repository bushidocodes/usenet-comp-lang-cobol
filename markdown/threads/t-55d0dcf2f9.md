[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Moving variable

_3 messages · 3 participants · 1997-05_

---

### Moving variable

- **From:** "kwok-ho" <ua-author-7158421@usenetarchives.gap>
- **Date:** 1997-05-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<338C4837.7812@netvigator.com>`

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

- **From:** "kevin p corkery" <ua-author-17071571@usenetarchives.gap>
- **Date:** 1997-05-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-55d0dcf2f9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<338C4837.7812@netvigator.com>`
- **References:** `<338C4837.7812@netvigator.com>`

```



Kwok-ho wrote in article
<338··.@net··r.com>...
› Hi,
› 
…[12 more quoted lines elided]…
› =================================
Try the following .....

01 ALPHA-SOURCE.
05 NUMERIC-SOURCE PIC 9(4)V99.

01 NUMERIC-TARGET PIC 9(4)V9(2).

IF ALPHA-SOURCE IS NUMERIC
MOVE NUMERIC-SOURCE TO NUMERIC-TARGET
ELSE
< something appropriate >
ENDIF.

Some compilers will attempt to permit the move (IBM for instance) of the
"X" pictured field to the numeric pictured filed. As long as the source
field is truly numeric, no problem, if not then and error will occur (IBM
)C& for instance). Redefining the alpha definition as a numeric will
permit the move to work.


›
```

##### ↳ ↳ Re: Moving variable

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-05-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-55d0dcf2f9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-55d0dcf2f9-p2@usenetarchives.gap>`
- **References:** `<338C4837.7812@netvigator.com> <gap-55d0dcf2f9-p2@usenetarchives.gap>`

```

Kevin P Corkery wrote:
› Some compilers will attempt to permit the move (IBM for instance) of the
› "X" pictured field to the numeric pictured filed.  As long as the source
› field is truly numeric, no problem, if not then and error will occur (IBM
› )C& for instance).  Redefining the alpha definition as a numeric will
› permit the move to work.

All compilers allow you to move alphanumeric to an integer numeric.
The alphanumeric item is treated as an integer. This is part of the
standard. Of course the contents must be all numeric - no decimal
point and no sign and such. What is not allowed in the standard is
moving such an item to a non-integer numeric. Some do as an extension
and some don't because they conform to the standard.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
