[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with Microfocus COBOL Ver 3.1

_1 message · 1 participant · 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: Problem with Microfocus COBOL Ver 3.1

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-23T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<7seera$5bs@dfw-ixnews3.ix.netcom.com>`
- **References:** `<7sduos$2eaj$1@news.inc.net>`

```
(In the future, you might find better replies in comp.lang.cobol - rather
than alt.cobol), but

If you print out the REDEFINED filed (the one that's all PIC X), then I
would be very surprised if you actually got commas and periods in the
output.  However, when you print out the numeric-edited version, you have
"incompatible data" - (because the actual storage doesn't match the PIC),
therefore, the compiler can do whatever it wants.  In this case, the
compiler is BELIEVING the PIC rather than the  storage - and not even
"looking at" what's in storage for those bytes, but printing out what SHOULD
be there.

Besides the solution of printing the all PIC X version - AND depending on
what you really want to do, another possible solution would be to look at
adding the "BLANK WHEN ZERO" clause to your numeric-edited definition.  I
think (but haven't tried it) that this might also solve your problem.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
