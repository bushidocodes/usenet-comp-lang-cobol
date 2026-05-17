[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Tables - Help

_1 message · 1 participant · 1994-12_

---

### COBOL Tables - Help

- **From:** "karendb" <ua-author-17073982@usenetarchives.gap>
- **Date:** 1994-12-17T18:20:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-hvG1q8AD1Sc@usenetarchives.gap>`

```
I'm finding it necessary to relearn COBOL after working with C for a
long, long time. I'm trying to implement a three-level and reading the
data on disk. The data looks like this:

City1 Catagory1 015016017018
City1 Catagory2 011012013014 <-----This stuff is percentages, ie 011
City1 Catagory3 022023024025 is 11%, 12% for a total of 4
occurances.

I set up the table like this:

01 SALES-DATA.
05 LOCATION OCCURS 2 TIMES.
10 CITY PIC X(15).
10 CATAGORY OCCURS 3 TIMES.
15 CAT PIC X(10).
15 PERCENT-RATE OCCURS 4 TIMES PIC V999.


I know to use a PERFORM VARYING and a couple of AFTER clauses to load
this thing, but I'm having problems referencing the data items. I'm not
even sure if the thing will load correctly.

I'm reading each of the lines in the data into the table. Thanks for all
the help anyone can give me. The books I'm using aren't terribly helpful.

Karen
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
