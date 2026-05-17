[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question on the use of the GLOBAL attribute

_1 message · 1 participant · 1995-03_

---

### Question on the use of the GLOBAL attribute

- **From:** "obr..." <ua-author-17087775@usenetarchives.gap>
- **Date:** 1995-03-06T17:05:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-iIJEoxqTbrQ@usenetarchives.gap>`

```
Hi,

I am using MF COBOL version 3.0 on a Unix

If I declare a data item in a program with the GLOBAL clause as follows

01 DATA-VAR GLOBAL.
02 COPIES PIC 99.

and a second data item in a directly contained subprogram

01 VAR.
02 COPIES PIC 99.

In the subprogram I want to assign a value to the GLOBAL data item COPIES
from the local data item COPIES. That is

MOVE COPIES TO COPIES OF DATA-VAR.

This MOVE works fine.

However if I use the CORRESPONDING phrase, that is

MOVE CORRESPONDING VAR TO DATA-VAR

The value in the GLOBAL data item COPIES (COPIES OF DATA_VAR) is not changed.

Has anyone come across this problem before? Am I missing something?

One may ask why no use the single MOVE. I am analysing other people's code to
separate some parts into subprograms and if they have used the MOVE
CORRESPONDING I do not want to change it.

Any help would be appreciated.

Liam.


==============================================================================
Liam O' Brien           |email: obr··.@u··.ie  | "Every word is like an
Dept. C.S.I.S,          |voice: +353-61-202710 |    unnecessary stain on
University of Limerick, |                      |      silence and nothingness"
Limerick,               |fax:   +353-61-330876 |     
Ireland.                |                      |          -  Beckett
------------------------|----------------------|------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
