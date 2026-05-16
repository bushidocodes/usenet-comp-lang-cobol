[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Find Mainline name

_3 messages · 2 participants · 2000-02_

---

### Find Mainline name

- **From:** Jim Ferguson <"Jim Ferguson">
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3899F2F3.1265@notes.ntrs.com>`

```
I'm running mainframe COBOL/MVS.   I need to find the name of the
mainline (first cobol program in the run unit).  I wrote an assembler
routine to extract it from the RUNCOM control block, but I would prefer
and IBM supported method.  Any  suggestions?

Jim Ferguson jwf1@notes.ntrs.com
Northern Trust
```

#### ↳ Re: Find Mainline name

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<87d9jg$9j5$1@nntp2.atl.mindspring.net>`
- **References:** `<3899F2F3.1265@notes.ntrs.com>`

```
Assuming that by the name "COBOL/MVS" that you mean "IBM COBOL for MVS & VM"
(or even "IBM COBOL for OS/390 & VM"), then you might look at the

  CEE3GRN--Get Name of Routine that Incurred Condition

LE callable service.  I am not certain exactly how this will/could work for
your specific problem, but it is documented (including a COBOL example) at:

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/CEEA306/3%2e5%2e6
```

#### ↳ Re: Find Mainline name

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 2000-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Saqm4.1762$Sx.30936@news4.mia>`
- **References:** `<3899F2F3.1265@notes.ntrs.com>`

```
No such creature exists for COBOL.
The IBM supported method would be to use the EXTRACT macros and xTCBx macros
to retrieve it from the system.

Jim Ferguson <"Jim Ferguson"> wrote in message
news:3899F2F3.1265@notes.ntrs.com...
> I'm running mainframe COBOL/MVS.   I need to find the name of the
> mainline (first cobol program in the run unit).  I wrote an assembler
…[4 more quoted lines elided]…
> Northern Trust
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
