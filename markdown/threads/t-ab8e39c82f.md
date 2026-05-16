[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OS/390 Now getting open error on VSAM

_3 messages · 2 participants · 2002-11_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`VSAM, files, sorting`](../topics.md#files)

---

### OS/390 Now getting open error on VSAM

- **From:** P Goodwin <member@dbforums.com>
- **Date:** 2002-11-12T21:15:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2039454.1037135715@dbforums.com>`

```

We just converted to OS/390 and started getting a status code 35 when
trying to open an empty VSAM file for I-O.  With COBOL II it worked
fine.  We now have to put a dummy record in it and code around the dummy
record.   Has anyone else had this problem?
```

#### ↳ Re: OS/390 Now getting open error on VSAM

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-12T16:48:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqs0uc$8ka$1@slb3.atl.mindspring.net>`
- **References:** `<2039454.1037135715@dbforums.com>`

```
See the discussion of "available and unavailable" VSAM files at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/1.10.6

What exactly did you change?  From VS COBOL II run-time to LE? VS COBOL II
compiler to Enterprise COBOL compiler? CMPR2 compiler option to NOCMPR2?

Each/any of these COULD be the cause of your problem.  (Obviously, the "fix"
is initialize the VSAM file *or* to add the "optional" phrase)
```

##### ↳ ↳ Re: OS/390 Now getting open error on VSAM

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-11-12T17:01:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqs35q$4op$1@slb6.atl.mindspring.net>`
- **References:** `<2039454.1037135715@dbforums.com> <aqs0uc$8ka$1@slb3.atl.mindspring.net>`

```
I just thought that I would add that this is NOT a change in the definition
of "available VSAM" files from VS COBOL II.  For the older definition, see:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igya1101/4.1.1.2

My GUESS is that you have changed from CMPR2 to NOCMPR2 - which is BOUND to
have a variety of run-time differences.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
