[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migrating to AIX IBM Cobol

_2 messages · 2 participants · 2000-01 → 2000-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Migrating to AIX IBM Cobol

- **From:** "Charles Handy" <charles_handy@hotmail.com>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#$ndAJ5Z$GA.201@cpmsnbbsa03>`

```
We are migrating a COBOLII/DB2 application from OS390 to AIX/DB2 UDB5 and
recompiling
with the standard AIX IBM COBOL compiler.  A DB2 pre-compile error "DB2
product not found" is being triggered by the lack of an "EXEC SQL BEGIN
DECLARE SECTION" before the working storage host variable declarations.
This statement is not required in COBOLII under OS390/DB2.  Can we set a
compile option in AIX Cobol or do we need to change our source?
```

#### ↳ Re: Migrating to AIX IBM Cobol

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<877thv$jse$1@nntp1.atl.mindspring.net>`
- **References:** `<#$ndAJ5Z$GA.201@cpmsnbbsa03>`

```
Here is the (3rd hand) reply that I received from one of my "usually reliable
sources",

"The customer is getting the DB2 not found message most likely because he
does not have db2lib installed in usr/lib.   The user does not have to
specify BEGIN DECLARE and END DECLARE around his host variables
declarations.  But we know that Workstation DB2 and S/390 DB2 have some
incompatibilities.  So this migration may or may not be easy depending on
how many S/390 DB2 extensions they have in their code.  We eliminated a lot
of incompatibilities with the co-processors, but we did not eliminate all
of them."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
