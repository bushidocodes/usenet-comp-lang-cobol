[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Examine vs Inspect

_2 messages · 2 participants · 2007-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Examine vs Inspect

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-10-08T18:54:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T1vOi.297113$1o1.291213@fe12.news.easynews.com>`

```
I asked in J4 and here is the information that I received back.
    ***

ANSI X3.23-1974, Appendix A, The History of COBOL, has the following:

Page XIV-11,  2.3.2, Overview of the Revised Module under 2.3, Differences 
between X3.23-1968 and the Revised Standard:  "The EXAMINE statement has been 
deleted in favor of the more general and powerful INSPECT statement.  The 
INSPECT statement provides the ability to count (Format 1), replace (Format 2) 
or count and replace (Format 3) occurrences of single characters or groups of 
characters in a data item."

Page XIV-29, 2.3.3, Substantive changes, item 49:  "EXAMINE statement and the 
special register TALLY were deleted."  This entry carries the indication that 
existing programs may be affected and the remark "Function was replaced by the 
INSPECT statement."   Item 50 contains a "condensed" version of the description 
of INSPECT from 2.3.2.

EXAMINE is listed among items deleted from the revised standard on page XIV-31 
under 2.3.4, simply indicating that it is replaced by the more powerful INSPECT.

I suspect one of the reasons for using a different verb (INSPECT vs. EXAMINE) 
was to eliminate any possible ambiguity arising from the fact that EXAMINE ... 
TALLYING affected a special register (TALLY) in '68; this register was 
eliminated in favor of user-specified data items in the TALLYING forms of 
INSPECT.  Also, EXAMINE tallied everything into TALLY as I recall, which means 
that doing multiple tallies in a given EXAMINE was, if not impossible, at least 
no more than marginally useful.  Allowing separate data items with INSPECT 
eliminated that restriction.  This is in addition to the ability to combine 
TALLYING and REPLACING, or both, in a single INSPECT, which the '74 standard 
indicates wasn't legal in '68.

   ***

FYI, as long as I have been following COBOL there has been a "direction" to get 
rid of (and avoid adding) special registers (and figurative constants).  For 
example, in those implementations that first introduced "length of" it created a 
special register, but this was NOT how it was added in Standard COBOL.  (Same 
for ADDRESS OF and NULLS figurative constant)
```

#### ↳ Re: Examine vs Inspect

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-10-08T18:08:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JZKdnezzCIvtW5fanZ2dnUVZ_vyinZ2d@comcast.com>`
- **In-Reply-To:** `<T1vOi.297113$1o1.291213@fe12.news.easynews.com>`
- **References:** `<T1vOi.297113$1o1.291213@fe12.news.easynews.com>`

```
William M. Klein wrote:
> I asked in J4 and here is the information that I received back.

[snip]

> I suspect one of the reasons for using a different verb (INSPECT vs. EXAMINE) 
> was to eliminate any possible ambiguity arising from the fact that EXAMINE ... 
…[7 more quoted lines elided]…
> indicates wasn't legal in '68.

Ah - that makes sense.  There were a few programs that still had 
references to registers in them when I got to my first shop, and I never 
did figure out what that was for - that must be what one of them was.  :)

> FYI, as long as I have been following COBOL there has been a "direction" to get 
> rid of (and avoid adding) special registers (and figurative constants).  For 
> example, in those implementations that first introduced "length of" it created a 
> special register, but this was NOT how it was added in Standard COBOL.  (Same 
> for ADDRESS OF and NULLS figurative constant)

That's a good thing, IMO.  With user defined data names, you know 
exactly what you've got.

I really appreciate this detailed information.  :)  Thanks!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
