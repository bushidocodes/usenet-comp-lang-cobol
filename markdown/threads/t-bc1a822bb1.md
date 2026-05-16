[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORT-RETURN values

_1 message · 1 participant · 2001-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Re: SORT-RETURN values

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-04-09T13:38:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9asviv$rd1$1@slb6.atl.mindspring.net>`
- **References:** `<3AD1DE83.CC9CC17F@brazee.net>`

```
Short answer - NOT VERY EASILY.

Medium answer - if all you want to know is whether it succeeded or not,
check out:
 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igypg205/1.11.12

Long Answer (and I have *not* tried this).
Use the SORT-MESSAGE special register to set the output DDname for your sort
messages to a "known" file - that you allocate in your run-time JCL. *also*
allocate that same file with a Select/Assign statement, an FD - but do NOT
open it before your SORT.

In the example (pointed to above), after you have determined that the
SORT-RETURN special register is not zero, THEN open the file with the sort
diagnostics (pointed to by your Select/Assign - FD) and "read" those
messages and DISPLAY them on the console.

  ***

Probably the BEST way (IMHO) is to simply test for SORT-RETURN not being
zero.  In that case send a message to your console operator to read the
diagnostics in the SORT sysout file (which can be "modified" by the use of
the SORT-MESSAGE special register).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
