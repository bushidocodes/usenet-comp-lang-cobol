[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Address Of Object in Working Storage

_2 messages · 2 participants · 2001-09_

---

### Address Of Object in Working Storage

- **From:** NotACobolGuru@att.net (Alex S)
- **Date:** 2001-09-26T16:54:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c9e25266.0109261554.601e70c@posting.google.com>`

```
My apologies if this has been answered before.  I did search these
groups and did not find an answer to my specific issue, so here it
is...

MVS/OS-390 Cobol II on ESA-390   (Yes, not current, but what we use.)

I know that IBM states clearly, and the compiler enforces, that I can
not take the address of an object in working storage, that I can only
take the address of a level 1 or level 77 object in linkage section. 
We do this routinely, however, using an assembler routine designed
just for that purpose.  I have also seen other answers in these groups
explaining how.

My question/problem, on the other hand, is why?  Is this "limitation"
an oversight, or is there a technical reason for the restriction?  I
suspect that the reason might be that objects in working storage can
"move around" dynamically and/or they might not be contiguous.  If
true, then taking the address of such objects is just plain wrong,
even if it seems to work.

We have lots of "production code" that does this.  It works.  I am
concerned that we may have laid a trap for ourselves, but I have been
unable to find any positive reason in the manuals for the restriction.
 Can someone help, please?  Thank you.
```

#### ↳ Re: Address Of Object in Working Storage

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-26T21:18:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ou2au$4sf$1@nntp9.atl.mindspring.net>`
- **References:** `<c9e25266.0109261554.601e70c@posting.google.com>`

```
1) This restriction IS removed in the latest IBM compiler (IBM COBOL for
OS/390 & VM V2R2) - so no, there is no "technical/design" reason why it
shouldn't be allowed.

2) Doing this is REQUIRED to be supported in the draft of the next  COBOL
Standard. Therefore, assuming that IBM will "eventually" support the next
Standard, they will CONTINUE to include this support.

3)  Unless your shop is "heavy" into Assembler, I do recommend the "pass the
working-storage data item (not really an object) to a NESTED COBOL program -
and get the address there" technique - over an assembler subroutine to do
it.

4) The HISTORICAL reason that IBM did not (originally) allow this - when
they added support for ADDRESS OF syntax, was that it (by definition) would
stop some of their optimization.  If a linkage section item could be set to
an address (in a pointer data item)  that was also set to the address of a
Working-Storage item, this meant that you had "implicit" REDEFINES of items
in two different SECTIONS.  Once this is allowed, there is LOTS of
optimization that must be turned off.  (This same situation occurs whenever
a data item is passed BY REFERENCE in a CALL statement.  So the nested
program technique ALSO stops some optimization.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
