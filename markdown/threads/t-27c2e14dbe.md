[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS ADDRESSABILITY TO DFHEIBLK IN DYNMIC CALL (NOT LINKED) PGM

_5 messages · 4 participants · 2003-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS ADDRESSABILITY TO DFHEIBLK IN DYNMIC CALL (NOT LINKED) PGM

- **From:** millsjay@aol.com (Jay Mills)
- **Date:** 2003-09-19T06:08:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5597693c.0309190508.60f4f5f1@posting.google.com>`

```
Is there a method of establishing addressability to the DFHEIBLK
without passing it in the CALL with USING DFHEIBLK.

Here is the problem

LEVEL 1 CICS

PROGRAM-A SEND A RECIEVE MAP

DYNAMICALLY CALLS PROGRAM-B WHICH DOES

MOVE DFHVALUE(UCTRAN) TO WS00-STATUS              
EXEC CICS                                         
     SET TERMINAL(EIBTRMID) UCTRANST(WS00-STATUS) 
END-EXEC

If I CALL PROGRAM-B USING DFHEIBLK there is no problem.  If I CALL
WITHOUT ANY USING I get the shown below.  However, due to vendor code
restrictions, I would like to CALL without the USING DFHEIBLK.  Is
there a solution (INQUIRE COMMAND DOES NOT WORK EITHER)using
ENTERPRISE COBOL?

 AEIK

    Explanation: TERMIDERR condition not handled.

    This is one of a number of abends issued by the EXEC interface
program.
    Because of their similar characteristics these abends are
described as a
    group.

    See the description of abend AEIA for further details.

    Module: DFHEIP
```

#### ↳ Re: CICS ADDRESSABILITY TO DFHEIBLK IN DYNMIC CALL (NOT LINKED) PGM

- **From:** godch01 <member30532@dbforums.com>
- **Date:** 2003-09-19T11:00:50-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3390905.1063983650@dbforums.com>`
- **References:** `<5597693c.0309190508.60f4f5f1@posting.google.com>`

```

Have you tried

EXEC CICS ADDRESS EIB(pointer-variable) END-EXEC

in the called program.
```

#### ↳ Re: CICS ADDRESSABILITY TO DFHEIBLK IN DYNMIC CALL (NOT LINKED) PGM

- **From:** millsjay@aol.com (Jay Mills)
- **Date:** 2003-09-19T13:03:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5597693c.0309191203.57e9e7e0@posting.google.com>`
- **References:** `<5597693c.0309190508.60f4f5f1@posting.google.com>`

```
The answer is:

EXEC CICS ADDRESS EIB(ADDRESS OF DFHEIBLK) END-EXEC

millsjay@aol.com (Jay Mills) wrote in message news:<5597693c.0309190508.60f4f5f1@posting.google.com>...
> Is there a method of establishing addressability to the DFHEIBLK
> without passing it in the CALL with USING DFHEIBLK.
…[32 more quoted lines elided]…
>     Module: DFHEIP
```

#### ↳ Re: CICS ADDRESSABILITY TO DFHEIBLK IN DYNMIC CALL (NOT LINKED) PGM

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-19T22:07:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U6Lab.39596$NM1.21303@newsread2.news.atl.earthlink.net>`
- **References:** `<5597693c.0309190508.60f4f5f1@posting.google.com>`

```
Thou SHALT pass the DFHEIBLK in a call to a separately compiled program.
See:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg10/3.1.1.4

which says, in part,

"If you are calling a separately compiled COBOL program that was processed
with either the separate CICS translator or the integrated CICS translator,
you must pass DFHEIBLK and DFHCOMMAREA as the first two parameters in the
CALL statement."
```

#### ↳ Re: CICS ADDRESSABILITY TO DFHEIBLK IN DYNMIC CALL (NOT LINKED) PGM

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-09-22T08:41:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-62DF9A.08414022092003@corp.supernews.com>`
- **References:** `<5597693c.0309190508.60f4f5f1@posting.google.com>`

```
For your first statement in the CALLed program, address the EIBLK and 
COMMAREA, e.g:

   EXEC CICS Address
      EIBLK( Address of DFHEIBLK )
      COMM( Address of DFHCOMMAREA )
   END-EXEC

That will allow you to operate with either style of parameter list as 
you prefer.




In article <5597693c.0309190508.60f4f5f1@posting.google.com>,
 millsjay@aol.com (Jay Mills) wrote:

> Is there a method of establishing addressability to the DFHEIBLK
> without passing it in the CALL with USING DFHEIBLK.
…[32 more quoted lines elided]…
>     Module: DFHEIP
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
