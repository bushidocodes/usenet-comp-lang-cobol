[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Working-Storage Initialization

_1 message · 1 participant · 1995-07_

---

### Working-Storage Initialization

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-07-31T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3vlnh7$hd8@gazette.tandem.com>`

```
There seem to be a few people confused about initialization of the
Working-Stroage Section. Some seem to think that initial programs do
it only once and so on.

Here are the facts:

1. The Working-Storage Section for all programs is initialized the
first time the program is called in the run unit. Initialized means
that everything that has a VALUE clause is set to that value and the
contents of anything without a VALUE clause are undefined. I know
that some compilers set everything without a VALUE to spaces or
something else, but you should never count on that.

2. When any program is cancelled (with a CANCEL statement),
Working-Storage is initialized on the next call to the program.

3. If a program is an initial program (INITIAL is specified in the
PROGRAM-ID paragraph), it is initialized every time it is called.

Those are the rules in the standard. There is nothing about
re-entrant programs (everybody has a different definition of what this
means anyhow) or anything else. Simple and straightforward.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
