[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ANSI COBOL and ISO COBOL meetings this summer

_1 message · 1 participant · 1995-10_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### ANSI COBOL and ISO COBOL meetings this summer

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-10-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46rngk$bra@gazette.tandem.com>`

```
This is a bit late. I forgot to post it (I was on sabbatical for six
weeks just after the WG4 meeting).

Report on July 10-14, 1995 ANSI X3J4 COBOL Committee meeting,
Chicago, Illinois, USA, and the ISO/IEC JTC1/SC22/WG11 COBOL Working
Group meeting, San Francisco, California, USA, August 14-18, 1995.
When a vote is shown, the numbers are for, against, and abstain (f-a-
a).

Both meetings were primarily devoted to discussing the public review
comments on the working draft. There were several hundred of these
(about 25 responses with some of them having a large number of
comments).

The major topics/proposals we discussed were:

1. Most of the public review comments were addressed at both
meetings. There were so many that we could not get to them all.
Some topics brought up were: increase the number of digits of a
numeric item to something larger than 18 digits (the vote was 6-1-2),
but the number of digits was not agreed upon (31 and 38 are the two
candidates); a suggestion was made that the standard intermediate
data item should be > 1 + max digits (it is now 19, which is 1 + max
digits), and that was approved by 8-1; lots of other discussion about
standard arithmetic resulted in no major changes; some suggestions to
change the in-line invoke (object-name !! "method-name" ...) by
getting rid of "!!" and putting a reserved word in front (like
METHOD) did not succeed - some other graphic like "<-" will probably
be used; it was decided to change VALUE REPEATED to clear up an
ambiguity and make it easier to use; several comments complained
about the complexity of object-orientation, but no major changes were
made; boolean items were discussed at length (at the last meeting
some major changes were suggested) and it was decided that usage bit
was the default for boolean items, usage display would be kept for
boolean items, comparisons and moves with boolean and numeric would
require explicit type converting functions, boolean items are left-
aligned, and the concept that if everything in a group is usage bit
then the group is usage bit was not accepted (3-3-3 vote); a method
of defining implementor-defined compiler directives will be added (by
">>IMP"); there were lots of comments on exception handling but no
major changes other than to clarify the rules and change some
evaluation rules; it was decided that concatenation would be allowed
for data items as well as literals; it was decided that a method of
making ACCEPT return a 4-digit year (by changing the syntax like FROM
DATE-4) should be in the important category; and it was decided that
a function that takes a 2-digit year and returns a 4-digit year
should be in the important category.

There were a large number of suggestions for new facilities and
features. These were all added to our list of topics for future
revisions and will be discussed when the 1997 standard is complete.
We are no longer accepting new items for this revision.

2. As a result of the above discussions, many items were moved to
different priority order. The main ones that were moved to the
critical category (standard won't go out without them) were those
dealing with interlanguage calls - native binary, floating-point,
pointers to data and programs,and recursive programs.

2. The revised proposal on allowing text-name to be a literal for
COPY was reviewed and will be added to the base document.

3. The revised proposal on concatenated keys was reviewed. It allows
various non-contiguous fields in a record to be concatenated to
create one record key. It will be added to the base document.

4. A proposal on extending the CALL (allows user-defined functions,
calling other languages, omitted parameters, passing by values,
passing literals, passing variable-length strings, and so on) was
discussed. It was decided to remove the rule that allows only 01-
levels to be passed (exception handling can detect synchronization
problems). It was decided to add GOBACK (3-0-5).

5. There is some concern that the standard is too large. A copy
will probably cost around $300. There were suggestions that there be
no page breaks between statements/clauses, that the font be reduced
from 10 to 9 points, and that the composite skeleton be deleted.
Nothing was done, however.

The next X3J4 meeting will be in Lowell, Massachusetts, USA, on
October 9-13 1995, with a three-day editing ad-hoc meeting on the
October 5-7. The main topic will be the public review comments.

The next WG4 meeting will be in May 1996 in the Netherlands.

Don Nelson
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
