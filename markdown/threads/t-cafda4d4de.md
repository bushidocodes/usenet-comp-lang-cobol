[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The Best to Calculate The Day Of Week

_2 messages · 2 participants · 1995-11_

**Topics:** [`Date and calendar processing`](../topics.md#dates)

---

### The Best to Calculate The Day Of Week

- **From:** "zear..." <ua-author-17087838@usenetarchives.gap>
- **Date:** 1995-11-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<482up0$aa2@news.puug.pt>`

```
This routine is dedicated to my wife Amelia and my little baby Joana.
It calculates the day of the week for a given date in the format:
YYYYMMDD.

*=================================================================*
* DAY-OF-WEEK.ROT : Calculates de day of the week for a given
*
* : date in the format YYYYMMDD
*
* : where YYYY - is the year (any one)
*
* : MM - is the month (must be
valid)*
* : DD - is the day (must exist)
*

*-----------------------------------------------------------------*
* Writer / Author...: Jose Araujo
*
* : E-mail: zea··.@ind··g.pt
*
* Date last modifyed: 1989 - Fev - 03
*

*=================================================================*
*
*
*INPUT: This variaveles must exist and must have the right
values (the date must be on SDT-YMD in the format YYYYMMDD)
*
*01 SDT-YMD PIC 9(08).
*01 SDT-YMD-X REDEFINES SDT-YMD.
* 03 SDT-Y PIC 9(04).
* 03 SDT-M PIC 9(02).
* 03 SDT-D PIC 9(02).
*
*
*WORKING: This are auxiliar (used in calculations)
*
*01 WK-DAT-VAR.
* 03 WK-DWK PIC 9(0001).
* 03 WK-DT1 PIC 9(0002).
* 03 WK-DT2 PIC 9(0001).
* 03 WK-DT3 PIC 9V9.
* 03 WK-DT4 PIC 9(0012).
* 03 WK-DT5 PIC 9(0012).
*
*
*OUTPUT: The result is WK-DWK
* (a number that coul be: 1 - Saturday
* 2 - Sunday
* 3 - Monday
* 4 - Tuesday
* 5 - Wednesday
* 6 - Thursday
* 7 - Friday
*
*------------------- +++ +++ +++ +++ +++ +++
---------------------
*
*
DAY-OF-WEEK SECTION.
*===================

IF SDT-M < 3

COMPUTE WK-DT4 = 365 * SDT-Y + SDT-D
+ 31 * ( SDT-M - 1 )
+ ( ( SDT-Y - 1 ) / 4 )

ELSE

COMPUTE WK-DT4 = 365 * SDT-Y + SDT-D
+ 31 * ( SDT-M - 1 )

COMPUTE WK-DT3 = 0.4 * SDT-M + 2.3

MOVE WK-DT3 TO WK-DT2

SUBTRACT WK-DT2 FROM WK-DT4

COMPUTE WK-DT4 = WK-DT4 + ( SDT-Y / 4 ).

COMPUTE WK-DT1 = SDT-Y / 100 + 1.

COMPUTE WK-DT1 = WK-DT1 * 0.75.

SUBTRACT WK-DT1 FROM WK-DT4.

COMPUTE WK-DT5 = WK-DT4 / 7.

COMPUTE WK-DT5 = WK-DT5 * 7.

COMPUTE WK-DWK = WK-DT4 - WK-DT5 + 1.

EXIT.
*
*
*-------------------( End of the routine )
*
*
Enjoy it. I assure this is the "best"
Jose Araujo
E-mail: zea··.@ind··g.pt
```

#### ↳ Re: The Best to Calculate The Day Of Week

- **From:** "j..." <ua-author-13889168@usenetarchives.gap>
- **Date:** 1995-11-12T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cafda4d4de-p2@usenetarchives.gap>`
- **In-Reply-To:** `<482up0$aa2@news.puug.pt>`
- **References:** `<482up0$aa2@news.puug.pt>`

```
Jose Manuel Araujo (zea··.@ind··g.pt) wrote:

: This routine is dedicated to my wife Amelia and my little baby Joana.
: It calculates the day of the week for a given date in the format:
: YYYYMMDD.

This looks like a COBOL adaptation of Zeller's Congruence...is it?

Jim

*-------------------------------------------------------------------------*
* James H. McCullars I Phone: (205) 895-6347 x238 *
* Director of Systems & Operations I Fax: (205) 895-6643 *
* Information Services I Internet: mcc··.@ema··h.edu *
* The University of Alabama I -----------------------------------*
* in Huntsville I *
* Huntsville, AL 35899 I This space for rent - CHEAP! *
*-------------------------------------------------------------------------*
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
