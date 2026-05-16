[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL pgm accessing ORACLE (AIX platform)

_3 messages · 2 participants · 1998-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### COBOL pgm accessing ORACLE (AIX platform)

- **From:** glemol@aol.com (GLEMOL)
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980917184313.29603.00000735@ng143.aol.com>`

```

Hi, 
I am a Mainframe COBOL programmer that started new project on RS/6000.
I deal with CICS program accessing DB2 tables. DBAs decided to remove one of
the tables and substitute it by ORACLE. So that pgm would has to access both
databases. I decided to split pgm on 2 modules:
1 Main pgm that access only DB2
2 Subprogram that access ORACLE
My problem :  What is the most appropriate way to invoke subprogram - 
CALL(static or dynamic) or LINK?
And, because I am not good in AIX scripts (so far) I need help on modifying
MAKE-file in order to compile COBOL - ORACLE pgm
I would really appreciate if some gurus send me examples of the script with
short descriptions and guidelines.

Alex
glemol@aol.com
```

#### ↳ Re: COBOL pgm accessing ORACLE (AIX platform)

- **From:** WOB@my-dejanews.com
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tsgc2$et1$1@nnrp1.dejanews.com>`
- **References:** `<19980917184313.29603.00000735@ng143.aol.com>`

```
In article <19980917184313.29603.00000735@ng143.aol.com>,
  glemol@aol.com (GLEMOL) wrote:
>
> Hi,
…[15 more quoted lines elided]…
>
Alex,

Speaking only from a Mainframe-CICS point of view, let's begin:

1) Static Calls are the quickest. However, the Called Program's Object Module
is merged with the Caller's Object Module. This could create a rather large
Load Module after Link-Edit. If many other DIFFERENT Caller's Statically Call
the Called Program, when modifications are made to the Called Program, the
Calling Program(s) will need to Link-Edit the new Called Program's Object
Module.

2) Dynamic Calls are next and are slower than Static calls. They require a
PPT entry (Statically Called Programs do not). When modifications are made to
the Called Program, only a CEMT NEWCOPY is required (or CICS Recycle) and all
Caller's will execute the updated version. However, Dynamically Called
Programs should be small and quick (in my opinion, 16K and under). This is
because storage that is allocated in the called program REMAINS allocated
UNTIL Task Termination. If the Caller issues a 'CALL' to a Dynamically Called
Program more than once prior to returning control (XCTL or RETURN), execution
time will be reduced significantly as opposed to a LINKED-TO Program, which
is next. BTW, Dynamic Calls CANNOT use DPL (Distributed Program Link), one of
the basics of a CICS SYSPLEX environment.

3) Using the LINK-API is the slowest. Like the Dynamically Called Program,
they also require a PPT entry. Unlike the Dynamic Call, storage allocated is
freed upon return to the Linker. However, subsequent LINKS to this same
Program by the same Linker prior to returning control (as noted above)
require significantly more execution time and overhead than the Dynamic Call.
CEMT would be used to NEWCOPY an updated version of the program while CICS is
executing.

I can't tell you which method to use, only the pro's and con's which I've run
into over the years.

HTH....

Cheers,

WOB,
Atlanta

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

##### ↳ ↳ Re: COBOL pgm accessing ORACLE (AIX platform)

- **From:** glemol@aol.com (GLEMOL)
- **Date:** 1998-09-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980918220916.24150.00001502@ng13.aol.com>`
- **References:** `<6tsgc2$et1$1@nnrp1.dejanews.com>`

```

Thank you very much for the detailed explanation of the differences between
CALLs and LINK in the mainframe environment, but I did dive into this field
about 14 years ago and still feel comfortable enough other there.

I am really need an answer from  RS/6000 - CICS/DB2/ORACLE point of view. I got
an exposure to this environment 1 month ago. Oh, boyï¿½

Actually second question  is more important for me because  I am new to the AIX
scripts and have problems with modifying MAKE-files.

Anyway thanks for your effort to help me.

Alex
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
