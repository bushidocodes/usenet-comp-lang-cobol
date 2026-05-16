[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# end of the century

_1 message · 1 participant · 1994-12_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Re: end of the century

- **From:** walterm@hprctbs3.rose.hp.com (Walter Murray)
- **Date:** 1994-12-01T18:11:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bl3k2$slk@hpchase.rose.hp.com>`
- **References:** `<CzztHF.LFB@Belgium.EU.net> <3bdm45$2qb@hpchase.rose.hp.com> <3be3qq$8k@ns1.computek.net> <3bgfcl$bdh@ohsun01.sumitomo-chem.co.jp>`

```
Senri (meyer@ohsun01.sumitomo-chem.co.jp) wrote:
: 1) Am I correct in understanding that Julian dating is the system in which
:    dates are represented by the number of days between the date in question
:    and a standard reference date?

The term "Julian date" has been used over the years to mean different
things.  Since this is comp.lang.cobol, I'd suggest using the terminology
used in the COBOL standard.

What you are describing is called "integer date form".  In standard COBOL
the starting date is January 1, 1601.  The term "Julian date form"
means the form YYYYDDD, where YYYY is a year and DDD is the day of
that year.  Finally, "standard date form" means YYYYMMDD.

: 2) If my understanding is correct, can someone provide some references to
:    their usage in application systems.  I would like to know such things as:
:    algorithms for converting regular dates to and from Julian dates; date
:    arithmetic; actual experience in applying Julian dates in business/
:    accounting applications.  If we were to use Julian dates here, we would
:    probably be forced to build the whole system from scratch.

Standard COBOL provides functions for date conversion:

     DATE-OF-INTEGER --> integer date to standard date
     DAY-OF-INTEGER  --> integer date to Julian date
     INTEGER-OF-DATE --> standard date to integer date
     INTEGER-OF-DAY  --> Julian date to integer date

To do date arithmetic, simply use addition and subtraction on dates
represented in integer date form.

Walter
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
