[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RANDOM function?

_2 messages · 2 participants · 2000-02_

---

### RANDOM function?

- **From:** Ray Guerette <rguerett@earthlink.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3899C538.876066E3@earthlink.net>`

```
Has anyone used the RANDOM function?  If so, how exactly does it work?
What is meant by "sequence" of pseudo-random numbers? How is/are the
value(s) returned?  If you have a coding example, PLEASE send it my way.

Thanks.
```

#### ↳ Re: RANDOM function?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87ci99$c7r$1@nntp9.atl.mindspring.net>`
- **References:** `<3899C538.876066E3@earthlink.net>`

```
A few things to understand about the COBOL Random Intrinsic Function:

1) It returns a value between 0 and 1 (with lots of decimal points, actually
zero is possible but it is always less than 1)

2) It can be invoked (referenced) with or without a "seed-value".  The
statement about a "series" of numbers replies to the fact that if you
reference it in a loop WITHOUT a seed-value, it will return a "random" (see
below) series of numbers.

3) The actual series of numbers is called "pseudo-random".  This is because
*if* you start with the same seed value followed by the same number of
references without seed-values, then you will get the identical series of
numbers.  (Lots of people "hate" this - but it is done intentionally - to
allow for "testing" and "audit-trails".)  However, see below ...

4) It is "customary" to use a relatively random seed-value - if what you
really want is an "un-reproducible" random series of numbers.  Often using a
portion of the CURRENT-DATE function works well for this (either seconds - or
hundredths of a second - depending on what your computer supports).

5) If what you really want is a random integer between 0 and n, then multiply
the results of the intrinsic function random by "n" - and you will get what
you want.  If you want an integer between 1 and n, then multiply the results
by "n - 1" - and then add 1 to the results.

6) Like all numeric intrinsic functions, this can only be used (in ANSI
conforming source code) where an arithmetic expression can be used (i.e.
COMPUTE works, but MOVE doesn't).  (This will be "fixed" in the next
revision - and some compilers don't enforce it today).

  ***

If this isn't enough information to get you started, let us (the NG) know
what your remaining problems are (and show us what you have tried).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
