[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Utility Program

_2 messages · 1 participant · 2001-01_

---

### Cobol Utility Program

- **From:** "David P. Bretz" <DBretz@mescoma.com>
- **Date:** 2001-01-30T18:52:53-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3A7753D5.C7A43537@mescoma.com>`

```
Just curious if anyone might be interested in a little COBOL program
that reads a CICS BMS layout and generates a printed report of the
screen layout with data fields defined, etc.    Saves having to assemble
the BMS, new it to the region and CECI it, just to look at it.

It sorta looks like this


1----1----2----2----3----3----4----4----5----5----6----6----7----7----8

1---5----0----5----0----5----0----5----0----5----0----5----0----5----0----5----0

           01 -  RR9S                     STATE TAX WITHHOLDING
TABLE            OPERATOR aaaa   - 01
           02
-
- 02
           03 -  STATE CODE      uu#
uuuuuuuuuuuuuuuuuuuuuuuuuuuuuu#   STATE NUMBER  uu#    - 03
           04
-
- 04
           05 -  HAS INCOME TAX?
u#                                             - 05
           06 -  HAS TAX DEFAULT?
u#                                             - 06
           07 -  FOLLOWS FED.GUIDE?
u#                                             - 07
           08
-
- 08
           09 -  DEFAULT PERCENT
nnnnnnn#                                         - 09
           10 -  MAXIMUM PERCENT
nnnnnnn#                                         - 10
           11 -  THRESHOLD AMOUNT
nnnnnnnnn#                                         - 11
           12
-
- 12
           13 -  HAS DISCLOSURE FORM?
u#                                             - 13
           14 -  DISCLOSURE FORM NUMBER
uuuuuuuuuu#                                    - 14
           15 -  EFFECTIVE DATE
uuuuuu#                                    - 15
           16
-
- 16
           17 -  LAST MAINT          aaaaaaaaaa
aaaaaaaa                                       - 17
           18 -  BY (RRS ID)         aaaa#
SYSTEM DATE/TIME STAMP   - 18
           19 -    (FUNB ID)         uuuuuuuu#
aaaaaaaaaaaaaaaaaaaaaaaaaa   - 19
           20
-
- 20
           21 -
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- 21
           22 -
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
- 22
           23 -  7-PREV.STATE   8-NEXT STATE: u#   DEL:
uuu#                                     - 23
           24 -
PRESS PA1 FOR SYS MENU  - 24

1----1----2----2----3----3----4----4----5----5----6----6----7----7----8

1---5----0----5----0----5----0----5----0----5----0----5----0----5----0----5----0

                u = Unprotected Alpha
                o = Protected Alpha
                a = Askipped Alpha

                U = Bright Unprotected Alpha
                O = Bright Protected Alpha
                A = Bright Askipped Alpha

                * = Dark Alpha

                n = Unprotected Numeric
                z = Protected Numeric
                s = Askipped Numeric

                N = Bright Unprotected numeric
                Z = Bright Protected Numeric
                S = Bright Askipped Numeric

                - = Dark Numeric

                # = Skip Byte

Two assumptions the program makes............the syntax of the BMS is
correct, and there is only one map per mapset.

Please respond privately if interested.

Dave
```

#### ↳ Re: Cobol Utility Program

- **From:** "David P. Bretz" <DBretz@mescoma.com>
- **Date:** 2001-01-30T18:54:52-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3A77544C.4608D3CA@mescoma.com>`
- **References:** `<3A7753D5.C7A43537@mescoma.com>`

```
sorry.............the formatting didn't work right.      looked good before I sent
it.

"David P. Bretz" wrote:

> Just curious if anyone might be interested in a little COBOL program
> that reads a CICS BMS layout and generates a printed report of the
…[97 more quoted lines elided]…
> Dave
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
