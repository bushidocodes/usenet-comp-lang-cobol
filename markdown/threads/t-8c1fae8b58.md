[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read versus Read Into the diffinitive answer...

_1 message · 1 participant · 1999-11_

---

### Read versus Read Into the diffinitive answer...

- **From:** Bill Thompson <wthompson@my-deja.com>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81e4qe$qln$1@nnrp1.deja.com>`

```
Dang!!! I am really getting to hate these Deja delays and omissions!!!!

No!  The routine in the generated COBOL code did not get called upon a
READ!  That code only got called when the elementary field that was the
object of "occurs depending on" phrase got altered, that included a
change to any group level to which that elementary field was a part of.

That was why any intelligent programmer would identify which of those
01s in the FD was the proper record just read in and then before
referring to any variable field in that record would "MOVE RCD-CNTR-
(whichever) TO RCD-CNTR-(itself)".  This then caused the compiler to
set the length of THAT 01 to the correct length.

READ INTOs always used max record as the from length and the length of
the to area as the to length.  This could result in either truncation
or padding as will any move of dissimilar length areas.

As a note, to avoid the constant recalculation of variable length
areas, the ODO object was often redefined with a slightly different
name and then could be referenced without the compiler doing a
recalculation.

With all this clamor about READ versus READ INTO of variable length
records, I now am understanding why some interviewers in the past were
so concerned with variable length record I/O skills - while I never
thought much about them....

I learned in a shop that had many variable length KSDS files,
synchronized to each other (SQL was a long ways away).  Many of those
files had multiple ODO phrases and one had four.  To modify there
records did require a READ INTO but mere input only reads did not.

Learning a few simple "rules" that were required to avoid clobbering
storage was all that was needed, and these rules are still valid to
this day.

Bill
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
