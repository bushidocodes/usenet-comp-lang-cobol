[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to submit job using CICS COBOL under MVS ?

_9 messages · 8 participants · 1998-07 → 1998-08_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### How to submit job using CICS COBOL under MVS ?

- **From:** "ppp" <ua-author-842015@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35C17AD9.D3C@ddd.ddd.com>`

```
If you know to method, please post to newsgroup.

Thanks in advance.
```

#### ↳ Re: How to submit job using CICS COBOL under MVS ?

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-07-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35C17AD9.D3C@ddd.ddd.com>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com>`

```
PPP wrote:
›
› If you know to method, please post to newsgroup.
›
› Thanks in advance.

Please do your own job/homework.

DD
```

##### ↳ ↳ Re: How to submit job using CICS COBOL under MVS ?

- **From:** "alan brown" <ua-author-25618@usenetarchives.gap>
- **Date:** 1998-07-31T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5d49c7bfb-p2@usenetarchives.gap>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com> <gap-f5d49c7bfb-p2@usenetarchives.gap>`

```


The Goobers wrote in article
<35C··.@er··s.com>...
› PPP wrote:
›› 
…[7 more quoted lines elided]…
› 
CHARTER

This newsgroup is for discussion of all aspects of the use of the COBOL
programming language. Examples of relevant topics are :

o Good books to learn from
o Requests for algorithms
o Discussions of coding problems
o Comparisons of different COBOL products
o The COBOL standards, past, present and future
o Object Oriented COBOL
o Portability between COBOL on mainframes, UNIX and DOS

The group should not be used for discussions or flame wars of the ``my
language is better than your language because...'' variety which more
properly belong in /dev/null.
```

###### ↳ ↳ ↳ Re: How to submit job using CICS COBOL under MVS ?

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-08-01T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5d49c7bfb-p3@usenetarchives.gap>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com> <gap-f5d49c7bfb-p2@usenetarchives.gap> <gap-f5d49c7bfb-p3@usenetarchives.gap>`

```
In article <01bdbce5$0ef5e2d0$3368e288@ato-10098>,
Alan Brown wrote:
› 
› 
…[15 more quoted lines elided]…
› programming language.  Examples of relevant topics are :

You see, Mr Brown?... *nothing* in the Charter about requests for doing
one's homework or job; thanks for your support!

DD
```

###### ↳ ↳ ↳ Re: How to submit job using CICS COBOL under MVS ?

_(reply depth: 4)_

- **From:** "laxmi..." <ua-author-17075221@usenetarchives.gap>
- **Date:** 1998-08-03T11:56:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5d49c7bfb-p4@usenetarchives.gap>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com> <gap-f5d49c7bfb-p2@usenetarchives.gap> <gap-f5d49c7bfb-p3@usenetarchives.gap> <gap-f5d49c7bfb-p4@usenetarchives.gap>`

```
Use the following steps in the program to submit a JCL from CICS program.

WORKING STORAGE SECTION
-----------------------

In the working storage, include this JCL steps.

01 WS-SUB PIC 9(2) VALUE ZERO .
01 WS-TOKEN PIC X(8) .
01 WS-USER PIC X(8) VALUE 'INTRDR ' .
01 WS-NODE PIC X(8) VALUE 'NODE1 ' .
*
01 WS-JCL-CARDS .
10 DUMMY1 .
20 FILLER PIC XX
VALUE '//' .
20 JCL1-USERID PIC X(6) .
20 FILLER PIC X(16)
VALUE 'SP JOB (CTB,CTB,' .
20 JCL2-USERID PIC X(6) .
20 FILLER PIC X(50)
VALUE ',D2,DT99X),' .
10 FILLER PIC X(80)
VALUE '// ''REPORT'',CLASS=B,MSGLEVEL=(1,1),MSGCLASS=X,' .
10 DUMMY2 .
20 FILLER PIC X(10)
VALUE '// NOTIFY=' .
20 NOTIFY-USERID PIC X(6) .
20 FILLER PIC X(64)
VALUE SPACES .
10 FILLER PIC X(80)
VALUE '//STEP1 EXEC PGM=FXR003 ' .
10 FILLER PIC X(80)
VALUE '//STEPLIB DD DSN=PROD.CICS.LOAD,DISP=SHR ' .
10 FILLER PIC X(80)
VALUE '//SYSOUT DD SYSOUT=* ' .
10 FILLER PIC X(80)
VALUE '//SYSABOUT DD SYSOUT=* ' .
10 FILLER PIC X(80)
VALUE '//SYSDUMP DD SYSOUT=* ' .
*
01 WS-JCL-ARR REDEFINES WS-JCL-CARDS .
05 WS-JCL-ARRAY OCCURS 8 TIMES PIC X(80) .
*

PROCEDURE DIVISION
------------------


In the program, include the following steps to direct the above mentioned JCL
to the input
queue

MOVE WP-USER TO JCL1-USERID
MOVE WP-USER TO JCL2-USERID
MOVE WP-USER TO NOTIFY-USERID

EXEC CICS SPOOLOPEN OUTPUT
USERID ( WS-USER )
TOKEN ( WS-TOKEN )
NODE ( WS-NODE )
NOHANDLE
END-EXEC

* Perform 8 times because there are 8 lines in the JCL step.

PERFORM VARYING WS-SUB FROM 1 BY 1 UNTIL WS-SUB > 8

EXEC CICS SPOOLWRITE
FROM (WS-JCL-ARRAY ( WS-SUB ) )
FLENGTH ( 80 )
TOKEN ( WS-TOKEN )
NOHANDLE
END-EXEC

END-PERFORM

EXEC CICS SPOOLCLOSE
TOKEN ( WS-TOKEN )
NOHANDLE
END-EXEC

The JCL submitted will look like this :-

//WP-USER SP JOB (OTB,OTB,WP-USER,D2,DT99X),
// ''REPORT'',CLASS=B,MSGLEVEL=(1,1),MSGCLASS=X,
// NOTIFY=WP-USER
//STEP1 EXEC PGM=FXR003
//STEPLIB DD DSN=PROD.CICS.LOAD,DISP=SHR
//SYSOUT DD SYSOUT=*
//SYSABOUT DD SYSOUT=*
//SYSDUMP DD SYSOUT=*





In article <6q2192$3rd$1.··.@cla··k.net>,
doc··.@cl··k.net () wrote:
› In article <01bdbce5$0ef5e2d0$3368e288@ato-10098>,
› Alan Brown  wrote:
…[24 more quoted lines elided]…
› 

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: How to submit job using CICS COBOL under MVS ?

_(reply depth: 5)_

- **From:** "ppp" <ua-author-842015@usenetarchives.gap>
- **Date:** 1998-08-05T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5d49c7bfb-p5@usenetarchives.gap>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com> <gap-f5d49c7bfb-p2@usenetarchives.gap> <gap-f5d49c7bfb-p3@usenetarchives.gap> <gap-f5d49c7bfb-p4@usenetarchives.gap> <gap-f5d49c7bfb-p5@usenetarchives.gap>`

```
Thanks a lot, the method you provided is very useful to me !
```

#### ↳ Re: How to submit job using CICS COBOL under MVS ?

- **From:** "ken foskey" <ua-author-3204800@usenetarchives.gap>
- **Date:** 1998-07-31T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p7@usenetarchives.gap>`
- **In-Reply-To:** `<35C17AD9.D3C@ddd.ddd.com>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com>`

```
setup tdque outputing to sysout=(,INTRDR)

Write to the tdque the complete job statements.

close it.

Check the syslog carefully when your job does not appear.

I have not done this in a long time but that is the method.

Good luck
Ken

PPP wrote:
›
› If you know to method, please post to newsgroup.
›
› Thanks in advance.
```

#### ↳ Re: How to submit job using CICS COBOL under MVS ?

- **From:** "izaguir..." <ua-author-17084362@usenetarchives.gap>
- **Date:** 1998-08-04T10:22:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p8@usenetarchives.gap>`
- **In-Reply-To:** `<35C17AD9.D3C@ddd.ddd.com>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com>`

```
In article <35C··.@ddd··d.com>,
PPP wrote:
› 1) define the resource READER on CICS startup and DCT define ... for example for cics 2.1.2

reader dd sysout=(A,INTRDR),dcb=(recfm=fb,lrecl=80,blksize=80) and reader
dfhdct type=sdsci( or extra) dscname=reader 2) the cics program write the job
on this device. 3) make attention on attribute of class of internal reader
(no replay on console) bye Ruggero Ruggeri

›
›
›

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

##### ↳ ↳ Re: How to submit job using CICS COBOL under MVS ?

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-08-04T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f5d49c7bfb-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f5d49c7bfb-p8@usenetarchives.gap>`
- **References:** `<35C17AD9.D3C@ddd.ddd.com> <gap-f5d49c7bfb-p8@usenetarchives.gap>`

```
iza··.@my-··s.com wrote:
› 
› In article <35C··.@ddd··d.com>,
…[7 more quoted lines elided]…
› 
It's also a good idea to end your JCL stream with a "/*EOF" statement,
which causes JES (JES2, anyway, no experience with JES3) to regard your
JCL as a complete job, meaning it won't wait for another JOB card. This
is much better than repetitive OPENs & CLOSEs of the extrapartition
destination (OPENs & CLOSEs = SVCs, a bad thing in a CICS region).

There was a discussion of this several months ago, you might try
DejaNews to insure you don't miss any details.

Bill Lynch
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
