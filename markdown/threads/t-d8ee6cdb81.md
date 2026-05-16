[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# sample program(s) to get to OS/390 "control blocks"

_1 message · 1 participant · 2002-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### sample program(s) to get to OS/390 "control blocks"

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-03-05T13:37:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a636ps$ata$1@slb0.atl.mindspring.net>`

```
As pointed out recently, Gilbert Saint-flour's web-page has moved.  I will
update the FAQ with the new address, but if anyone is interested in this
files before that:

    http://mywebpages.comcast.net/gsf/tools/cob2job.txt

has a program with the following comments:

"      *----------------------------------------------------------------
      *
      *    This program retrieves specific job-related data from MVS
      *    control blocks and moves it to Working-storage.
      *
      *    The name of the control-block is indicated in pos 1-6 of
      *    the Procedure Division lines.
      *    The layout of the MVS control blocks is described in the
      *    MVS Data Areas manuals, which can be found on any MVS or
      *    OS/390 CD collection or viewed on-line by going to:
      *        http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/library
      *    and searching for:
      *        MVS DATA AREAS
      *----------------------------------------------------------------*

while

    http://mywebpages.comcast.net/gsf/tools/cob2sys.txt

has a program with the following comments:

      *----------------------------------------------------------------
      *
      *    This program retrieves specific system-related data from
      *    MVS control blocks and moves it to Working-storage.
      *
      *    The name of the control-block is indicated in pos 1-6 of
      *    the Procedure Division lines.
      *    The layout of the MVS control blocks is described in the
      *    MVS Data Areas manuals, which can be found on any MVS or
      *    OS/390 CD collection or viewed on-line by going to:
      *        http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/library
      *    and searching for:
      *        MVS DATA AREAS
      *
      *----------------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
