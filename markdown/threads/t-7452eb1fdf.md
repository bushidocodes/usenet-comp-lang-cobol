[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Belated report on December X3J4 meeting

_2 messages · 2 participants · 1997-03_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Belated report on December X3J4 meeting

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-03-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33270DC0.5E93@tandem.com>`

```

Report on December 9-13, 1996 ANSI X3J4 COBOL Committee meeting,
Carmel, California, USA and the December 6-8, 1996 Object-Oriented
COBOL ad hoc group in the same location. When a vote is shown, the
numbers are for, against, and abstain (f-a-a).

Membership stands at 11. The primary topic at this meeting was action
for the CD (committee draft) review at ISO. We received about 30 sets
of comments (18 from IBM) and went through all of them.

The major topics/proposals we discussed were:

1. The object-oriented COBOL ad hoc committee met for three days and
made some significant changes. The main ones were: remove simple
classes; remove the INVARIANT attribute for a method; remove the class
library except for a minimal base class and a null object; remove
presistence; and lots of other changes. The class library will
probably be removed from the standard and published as a technical
report, which will provide guidelines to implementors but will allow
for more refinement in subsequent publications. Some portability will
probably be lost, however.

2. The public review comments (almost all of the meeting was spent on
this). Most of the comments resulted in editorial or other minor
changes. No other real changes were made, but direction was given to
make several changes. This may be overridden by WG4 (the
international group) in March, so I won't detail them here.

3. During public review comment discussion we discussed many topics
at length. One was to have a concept of "staging", where implementors
would have a basic set of features in the beginning and a year or so
later would have another set and so on. This did not go over (it was
rejected by 9-1-1). There is concern over the size of the standard
(rightfully so). There were some attempts to delete features in order
to simplify the standard (both IBM and MF suggested this), but there
did not seem to be much support. See below.

Another topic discussed at length was the method of handling complex
collating sequences that require multiple characters (like accents and
such). This is done in the draft by using locales. However, there is
no way to use this for SORT, MERGE, regular comparisons (functions
must be used), SEARCH, indexed files, and so on. Nothing much was
done except stating that perhaps SORT should work with such locales.

The attempt by Micro Focus to remove boolean and bit support failed by
a 8-1 vote.

The attempt by Micro Focus to remove the VALIDATE feature failed by a
9-1 vote.

The attempt by Micro Focus to make the report writer obsolete failed
by a 8-1 vote.

The attempt by Micro Focus to remove the exception handling facility
failed by a 9-1 vote.

The next X3J4 meeting will be in, Chelmsford, Massachusetts, USA, on
February 24-28, 1997. The main topic will be addressing comments on
the CD review of the base document and the above proposals that were
rewritten. There will also be an object-oriented ad hoc meeting in
Chelmsford on February 17-21, 1997.

Don Nelson
Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: Belated report on December X3J4 meeting

- **From:** "r..." <ua-author-43843@usenetarchives.gap>
- **Date:** 1997-03-14T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7452eb1fdf-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33270DC0.5E93@tandem.com>`
- **References:** `<33270DC0.5E93@tandem.com>`

```

In article <332··.@tan··m.com>
› nel··.@tan··m.com "Don Nelson" writes:
› The attempt by Micro Focus to
…[3 more quoted lines elided]…
›   remove the exception handling facility failed by a 9-1 vote.

Would someone explain why Micro Focus, an acknowledged leader in
COBOL compiler writing, was alone in wanting to do these things?
For example, is it MF elegance versus MS bloat?

Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
