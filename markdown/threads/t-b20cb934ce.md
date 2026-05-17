[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Subject: COBOL standard and Re: report object

_1 message · 1 participant · 1994-11_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Subject: COBOL standard and Re: report object

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1994-11-22T20:48:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88106....@fox.nstn.ns.ca>`

```
My reaction to this post for a report object is that the
COBOL standards group needs to look at why proprietary
languages such as Sterling's DYL280 and Software AG's
Natural are so powerful. IM(rarely)HO it is in large part
because of the enhancements to the field definitions of
internal records. Both languages allow specification of a
default column heading and a default external display format
for all fields. Thus report writing functions for both
languages are relatively simple and straightforward. When I
used DYL280 4 years ago the handling of title lines was a
little awkward but overall the language made it simple to
create ad hoc reports. Much of that power centred on the
enriched capabilities of the field descriptions. The syntax
was the equivalent of:
05 FIELD-A PIC S9(7)V99 DISPLAY-PIC $,$$$,$0.00- COLUMN
HEADING "NET DOLLARS". Thus the printing of a detail
line consisted purely of a "LIST field_1 field_2 ... field_n
with all inter-field spacing and columnar headings taken
care of. I also could code INPUT_FILE.FIELD_1 instead of
the awkward FIELD-1 OF INPUT-FILE. Unfortunately they used
the less visually appealing underscore as a separator
character instead of the hyphen. DYL280 allows one to
describe a report as having a page n columns wide by m lines
per page with title line specifications. The title line
could include input fields, a number of system provided
fields such as current date and time, page number in
different formats, and literals. It was possible to take
control breaks, list the sum of fields at control breaks,
etc. Natural provided similar capabilities plus native
language access to the Adabas data base. My reaction to
both languages was feeling there was very little change
needed to give COBOL the same amount of power. Giving COBOL
a decent report writing function might not be as valuable as
it would have been in the eighties but it still would be
useful. Qualification in COBOL should allow writing the
equivalent of "Joe's car" instead of "car of Joe." This
would follow normal English usage and is only 25-30 years
overdue. This may seem a bit harsh but I have been angered
by the COBOL handling of qualification since I started using
it in the early 1960's. I have found it awkward to read and
people at my previous shop avoided using it because of the
awkwardness. This is despite the value of using the same
record description in every file the record is used. While
object-oriented programming is valuable in some areas, I
believe that a decent report writing facility (the existing
COBOL report writer was virtually unused at my previous shop
and IBM dropped it from VS COBOL II) would be a better
answer to Chris's need.

› Today I wrote for the 1,000th or so time the same COBOL
› report program.  This type of program reads a file of
…[3 more quoted lines elided]…
› the headers are written for the report.
 
› I have heard that C++ helps programmers by having the
› ability to reuse other's tested code.  Does anyone have
…[16 more quoted lines elided]…
› be?
 
 
› Chris Mason
› "The Unknown COBOL Programmer"

- -
Clark Morris, CFM Technical Programming Services
RR # 1, 1339 Clarence Road, Bridgetown, Nova Scotia, Canada B0S 1C0
902-665-4006 internet cmo··.@fox··s.ca
The opinions are those of my company, at least today
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
