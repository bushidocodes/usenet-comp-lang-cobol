[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The Universal Tool

_1 message · 1 participant · 2000-04_

---

### The Universal Tool

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39048D23.46F4D2FD@cusys.edu>`

```
The "Swiss Army Knife" theory of language development has been tried in
the past.  PL/I did pretty well at it.  But I am not sold on the
concept.

But I very much like enhancements to Cobol which are Cobol-like.  The
following is an example which I took out of IEEE Software March/April
2000:

01  birthdate.  *> month, day, year: mmddyyyy
 03 month pic 99 valid values 1 thru 12.
    valid value 1 thru 32 when month =
      1 or 3 or 5 or 7 or 8 or 10 or 12
    valid value 1 thru 29 when month = 2
    valid value 1 thru 30 when month =
      4 or 6 or 9 or 11
 03 year pic 9(4) invalid when year >
    function current-date (1:4)
01  error-message pic x(80)
  error "date is not numeric" on format for month,
     day-of-month, year
  error "month must be <= 12" on content for month
  error "day not valid in that month" on content for day-of-month
  error "invalid birth year" on relation for year.

...
validate birthdate


This is data and business rules centric evolution of the language. 
Furthermore, it is obvious what the above code does - to maintain that
code do you need to pull out a manual to look at those unfamiliar
commands?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
