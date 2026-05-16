[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# need basic y2k source code.

_3 messages · 3 participants · 1998-12_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### need basic y2k source code.

- **From:** "netone" <netone@pacbell.net>
- **Date:** 1998-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eoke2.480$Mk.2047@typhoon-sf.snfc21.pbi.net>`

```
If anybody could supply me a generic set of how a COBOL Y2K problem look
like in a source code. Doesn't have to be complete, only what the problem
looks like in code. Thanks.
```

#### ↳ Re: need basic y2k source code.

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Hpqe2.239$bJ4.454855@news2.mia>`
- **References:** `<eoke2.480$Mk.2047@typhoon-sf.snfc21.pbi.net>`

```
netone wrote:
>If anybody could supply me a generic set of how a COBOL Y2K problem look
>like in a source code. Doesn't have to be complete, only what the problem
>looks like in code. Thanks.

Your question is too simplistic.  The Y2K 'problem' could be expressed
in code a truly infinite number of ways.  I could post 500 pages here,
and not scratch the surface.  This sounds like a homework assignment,
but I'll give you some examples.

Example 1:

  Data Division:

           03  MAST-TRAN-DATE.
               05  MAST-TRAN-YY      PIC  9(02).
               05  MAST-TRAN-MM      PIC  9(02).
               05  MAST-TRAN-DD      PIC  9(02).

           03  WORK-TRAN-DATE.
               05  WORK-TRAN-YY      PIC  9(02).
               05  WORK-TRAN-MM      PIC  9(02).
               05  WORK-TRAN-DD      PIC  9(02).

  Procedure Division:

           IF (WORK-TRAN-DATE < MAST-TRAN-DATE)
               ...

As you can see, the date only allows for a 2 digit year.  As soon
as the year reaches 2000, the If statement in the Procedure Division
will no longer be valid, because 00 < 99.  To correct this problem,
both dates must be expanded like this:

           03  MAST-TRAN-DATE.
               05  MAST-TRAN-CC      PIC  9(02).
               05  MAST-TRAN-YY      PIC  9(02).
               05  MAST-TRAN-MM      PIC  9(02).
               05  MAST-TRAN-DD      PIC  9(02).

           03  WORK-TRAN-DATE.
               05  WORK-TRAN-CC      PIC  9(02).
               05  WORK-TRAN-YY      PIC  9(02).
               05  WORK-TRAN-MM      PIC  9(02).
               05  WORK-TRAN-DD      PIC  9(02).

Or you could expand them like this:

           03  MAST-TRAN-DATE.
               05  MAST-TRAN-YYYY    PIC  9(04).
               05  MAST-TRAN-MM      PIC  9(02).
               05  MAST-TRAN-DD      PIC  9(02).

           03  WORK-TRAN-DATE.
               05  WORK-TRAN-YYYY    PIC  9(04).
               05  WORK-TRAN-MM      PIC  9(02).
               05  WORK-TRAN-DD      PIC  9(02).

Of course, every reference to these two date fields must be examined
and changed if necessary to accommodate the new format.  A typical
program may have from none, one or two date references to literally
hundreds, perhaps thousands, of date references.  Each of them must
be carefully examined, analyzed, and corrected.  The above example
was very simple.  A more complex situation is when the dates are used
in calculations, say to compute the number of days since a payment
has been made on a loan.  Calculating the number of days between two
dates is very common, and the algorithms are different between dates
with two and four digit years.  And if the year only has two digits,
both dates are assumed to be in the same century.  Another common use
of dates is to calculate the day of the week on which the date falls.
The pattern of weekdays is different between the 20th century and
the 21st century.  Once the year reaches 2000, all those routines
will fail, giving the wrong day of the week.
```

#### ↳ Re: need basic y2k source code.

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<367CA565.5BB3@sprynet.com>`
- **References:** `<eoke2.480$Mk.2047@typhoon-sf.snfc21.pbi.net>`

```
netone wrote:
> 
> If anybody could supply me a generic set of how a COBOL Y2K problem look
> like in a source code. Doesn't have to be complete, only what the problem
> looks like in code. Thanks.

DATA DIVISION.
WORKING-STORAGE SECTION.
01  DATES.
    05  DATE-1             PIC 999999.
    05  FILLER             REDEFINES DATE-1.
        10  DATE-1-YY      PIC 99.
        10  DATE-1-MM      PIC 99.
        10  DATE-1-DD      PIC 99.
    05  DATE-2             PIC 999999.
    05  FILLER             REDEFINES DATE-2.
        10  DATE-2-YY      PIC 99.
        10  DATE-2-MM      PIC 99.
        10  DATE-2-DD      PIC 99.

PROCEDURE DIVISION.
     IF DATE-1 IS GREATER THAN DATE-2
         DISPLAY 'DATE 1 IS MORE THAN DATE 2'
     ELSE
     IF DATE-1 IS EQUAL TO DATE-2
         DISPLAY 'DATE 1 IS THE SAME AS DATE 2'
     ELSE
         DISPLAY 'DATE 2 IS MORE THAN DATE 1'.

I'll let you figure out the results if one of the dates is December 31, 1999
and the other is January 1, 2000.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
