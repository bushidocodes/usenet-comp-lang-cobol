[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# aging dates in COBOL

_4 messages · 4 participants · 1998-10_

---

### aging dates in COBOL

- **From:** Martin P McDonald <mpmcd@ix.netcom.com>
- **Date:** 1998-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vogq1$71o@dfw-ixnews6.ix.netcom.com>`

```
As part of Y2K testing, we're trying to develop a program that could warp file dates forward or
backward any number of days or months.  I can use the CEE services only if I consider a month to
be equal to 30 days or 31 days etc.  I could use a series of loops, simulating a kind of internal
"calendar odometer", but I'd like to use mathematical computations instead of loops.
I know that the remainder of (month + warpvalue / 12) yields the new month portion of the date, I
know that the integer portion of (month + warpvalue / 12) yields how many years need to be added
to the year portion of the date.  I even know that to warp backwards, one could use the preceeding
logic as long as the numbers are inverted MM = 13 - 1, and warpvalue = warpvalue * -1.  This works
when warping forward and backward, except when warping backward by a warpvalue evenly divisible by
12; an extra year is subtracted that shouldn't be.  If anyone knows the bug in the preceeding
logic or has any other ways of doing this, please pass it on!
Thanks very much!
Marty McDonald
mpmcd@ix.netcom.com
```

#### ↳ Re: aging dates in COBOL

- **From:** The Goobers <docdwarf@erols.com>
- **Date:** 1998-10-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36200B0B.3E4E@erols.com>`
- **References:** `<6vogq1$71o@dfw-ixnews6.ix.netcom.com>`

```
Martin P McDonald wrote:
> 
> As part of Y2K testing, we're trying to develop a program that could warp file dates > forward or backward any number of days or months. 

If my porous memory serves correctly there is something in Mr
Svalgaard's ETKPAK.ZIP which takes care of this rather nicely... no need
to reinvent the wheel.

DD
```

#### ↳ Re: aging dates in COBOL

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<271U1.913$ce.1130687@news4.mia.bellsouth.net>`
- **References:** `<6vogq1$71o@dfw-ixnews6.ix.netcom.com>`

```
Martin P McDonald wrote:
>As part of Y2K testing, we're trying to develop a program that could
>warp file dates forward or backward any number of days or months.

You can download routines to add or subtract days, months or years, plus
a number of other date functions, from my web page below.  Download file
DATE.ZIP under 'COBOL Source Files'.  Works for all dates in the Gregorian
Calendar (1583 - 9999).
```

#### ↳ Re: aging dates in COBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vtrci$4s2@sjx-ixn5.ix.netcom.com>`
- **References:** `<6vogq1$71o@dfw-ixnews6.ix.netcom.com>`

```
(Sorry for leaving the entire original post, but it will help understand the
reply - and it is old enough that some may not have saved it.  My reply is
at the end)

Martin P McDonald wrote in message <6vogq1$71o@dfw-ixnews6.ix.netcom.com>...
>As part of Y2K testing, we're trying to develop a program that could warp
file dates forward or
>backward any number of days or months.  I can use the CEE services only if
I consider a month to
>be equal to 30 days or 31 days etc.  I could use a series of loops,
simulating a kind of internal
>"calendar odometer", but I'd like to use mathematical computations instead
of loops.
>I know that the remainder of (month + warpvalue / 12) yields the new month
portion of the date, I
>know that the integer portion of (month + warpvalue / 12) yields how many
years need to be added
>to the year portion of the date.  I even know that to warp backwards, one
could use the preceeding
>logic as long as the numbers are inverted MM = 13 - 1, and warpvalue =
warpvalue * -1.  This works
>when warping forward and backward, except when warping backward by a
warpvalue evenly divisible by
>12; an extra year is subtracted that shouldn't be.  If anyone knows the bug
in the preceeding
>logic or has any other ways of doing this, please pass it on!
>Thanks very much!
>Marty McDonald
>mpmcd@ix.netcom.com

I received the following note from one of my "usually reliable sources" who
works with the CEE routines and Y2K stuff, (I hope this helps)

"It's probably pretty obvious, but the questions I have to ask are:  Does
the
customer want to change the date forward or backward relative to a specific
date, say change all dates the same number of days represented by the span
from today to  3/15/2000?  Or, do they want to change the date a set number
days (or months), say 120 days or 4 months from now?  Use all signed numbers
so that you can go forwards or backwards without having different
calculations.   Here are some possible solutions:

To warp dates relative to a specific calendar date range, e.g. span all
dates
the same number of days represented by changing 10/12/1998 to 3/15/2000:

01  date-to-span  pic 9(08).
01  warp-date  pic 9(08) value 20000315.
.. . .
Compute date-to-span = (function date-of-integer (function integer-of-date
(date-to-span) + function integer-of-date (function current-date (1:8)) -
function integer-of-date (warp-date)))


To warp the date a specific number of days:

01  date-to-span  pic 9(08).
01  warp-days  pic s9(05).
.. . .
Compute date-to-span = function date-of-integer (function
integer-of-date(date-to-span) + warp-days)


To warp the date a specific number of months do the following.  I don't have
a good way of playing with leap years here without going into MANY more
steps. I'd recommend using one of the previous methods instead:

01  date-to-span.
 05  date-to-span-days pic 9(02).
 05  date-to-span-months pic 9(02).
 05  date-to-span-years pic 9(04).
01  number-of-warp-months pic s9(03).
01  number-of-warp-years pic s9(03).
01  left-over-months  pic s9(03).
.. . .
Divide number-of-warp-months by 12 giving number-of-warp-years remainder
left-over-months
Evaluate (date-to-span-month + left-over-months)
When > 12
Subtract 12 from left-over-months
Add 1 to number-of-warp-years
End-evaluate
Compute date-to-span-year =  number-of-warp-years + date-to-span-year
Compute date-span-month = lef-over-months + date-to-span-month



You could also use the LE Callable Services, CEEDAYS and CEEDATE instead of
the Intrinsic Functions above."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
