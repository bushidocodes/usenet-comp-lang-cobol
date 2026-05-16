[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Comparing time in microfocus Cobol

_2 messages · 2 participants · 2002-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Comparing time in microfocus Cobol

- **From:** samhunt90@hotmail.com (Sam)
- **Date:** 2002-10-10T14:58:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e20518e0.0210101358.1b206a24@posting.google.com>`

```
Hi

What's the best way to compare times in cobol?  For example, the
program should only initiate a process if the time of day is before a
certain "cutoff" time.  That "cutoff" time is retrieved from an oracle
database, where it is stored as a date field.  The date (mm/dd/yy)
will be ignored, only the time (hh:mm) will be compared to the current
system time.

Thanks,
Sam90
```

#### ↳ Re: Comparing time in microfocus Cobol

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-10-11T18:31:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021011143151.29550.00010951@mb-ml.aol.com>`
- **References:** `<e20518e0.0210101358.1b206a24@posting.google.com>`

```
Hi Sam,

If your compiler supports intrinsic functions, you can try this:

move function current-date(9:4) to curr-hh-mm

if curr-hh-mm >= oracle-hh-mm ....

The current-date function returns a 21 pos A/N field  that contains the
date/time to 100ths fo a sec as well as  +/- offeset data relative to GMT. The
example above just uses the hhmm of the time substring.

HTH, Jack.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
