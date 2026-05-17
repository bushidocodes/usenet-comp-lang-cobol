[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Book on SQL in COBOL ???

_3 messages · 3 participants · 1996-01_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Book on SQL in COBOL ???

- **From:** "stev..." <ua-author-565738@usenetarchives.gap>
- **Date:** 1996-01-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4d2ckc$ko4@newsbf02.news.aol.com>`

```
Looking for a recommendation on a book on coding SQL in Mainframe COBOL
programs (mixed environment, IMS, DB2, CICS, IMS-DC, etc). What I need is
a "how-to" with pratical examples of using SQL. Any and all information
about the books out there is appreciated.

TIA
Steven L. Newton
Milwaukee, WI
Asimov, Heinlein, and Zappa are still the best
```

#### ↳ Re: Book on SQL in COBOL ???

- **From:** "chris mason" <ua-author-1350352@usenetarchives.gap>
- **Date:** 1996-01-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ce5da84e6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4d2ckc$ko4@newsbf02.news.aol.com>`
- **References:** `<4d2ckc$ko4@newsbf02.news.aol.com>`

```
Steven asked about SQL on the mainframe...

I recommend DB2 for the COBOL programmer written by Mr. Steve Eckols.
I met Steve at a trade show and I bought those two volumes (Part 1
and Part 2). It is published by Mike Murach in *lovely* Fresno
California. Mike Murach & Associates, Inc. 4697 West Jacquelyn
Avenue, Fresno, California 93722, phone = (209) 275-3335.

This publisher also has titles on other Mainframe Topics. Unfortunately,
you will find that you need other books on the topics you mentioned.
Every one of these subsystems have their own details to learn...

These books can be pricey, but they are worth their weight in gold...

Personally, I prefer these books to some competing publishers books
with titles such as "COBOL for Gardeners". Or "How to make more
money implementing unix on your hotdog stand using a COBOL to C
translator". 8-> (ha, ha, yuk, yuk, tee hee) (laugh track required
due to humor quality cut back)

Although "COBOL for pasta connosiuers" helped me deal with sphaghetti
code...

But seriously...DB2 is executed/compiled/linked DIFFERENTLY depending on
wether IMS
is involved or if it is "pure" DB2 which involves TSO...
We experience the joy of having to compile TWO versions of the same
DB2 subprogram depending on wether the calling program has IMS or
not...

We find Fileaid for DB/2 to be nice. SPUFI is spify. DB/2 security
with such concepts as plans, groups and so-on is a royal pain in
the you-know-what. Open up the data with SQL and then clamp down
on security more then in IMS days so that any gains seem diminished...???

It's like the management/users don't trust us poor COBOL programmers
with the data. Will, mistakes are made, I admit it. But mistakes
are NOT prevented with these elaborate "protect the data from the
programmers" policies...

I spend more time filling out security forms then coding the actual
SQL...

Here is some sample JCL for "pure DB2 cobol program" L94L1
Notice the jobparm that forces it to run on a specific mainframe,
since DB2 regions here are on one specific node...

EDIT ----- CG42P1.JCL.CNTL(L94L1NEW) - 01.04 ---------------- COLUMNS
001 072
COMMAND ===> SCROLL
===> HALF
000005 /*JOBPARM SYSAFF=0027
000006 //JOBLIB DD DISP=SHR,DSN=DB2.DB2T.SDSNLOAD
000007 // DD DISP=SHR,DSN=DB2.DB2T.SDSNEXIT
000008 // DD DISP=SHR,DSN=DB2TEST.DB2.LOAD
000009 // DD DISP=SHR,DSN=DB2TEST.DBRM.DATA
000010 // DD DISP=SHR,DSN=MVS1.COBOL2.COB2LIB
0000
000011 //STEP01 EXEC PGM=IKJEFT01,
000012 // DYNAMNBR=20
000013 //DBRMLIB DD DISP=SHR,DSN=DB2TEST.DBRM.DATA
000014 //SYSTSPRT DD SYSOUT=*
000015 //SYSOUT DD SYSOUT=*
000016 //SYSPRINT DD SYSOUT=*
000017 //PRINTDD DD SYSOUT=*
000018 //SYSUDUMP DD SYSOUT=*
000019 //SYSABOUT DD SYSOUT=*
000020 //SYSDBOUT DD SYSOUT=*
000021 //STANDAT5 DD DISP=SHR,DSN=SYS1.STANDAT5
000022 //L94LD DD DISP=SHR,DSN=CG42P1.L94LD.OCT19
000023 //MESSAGE DD DISP=SHR,DSN=CG42P1.MESSAGE
000024 //L94MG DD DISP=SHR,DSN=CG42P1.L94MG.MSTR
000025 //L94WI DD DISP=SHR,DSN=CG42P1.L94WI.MSTR
000026 //SYSTSIN DD *
000027 PROFILE PREFIX(CG42P1)
000028 DSN SYSTEM(DB2T) RETRY(0) TEST(1)
000029 RUN PROG(L94L1) -
000030 PLAN(L94L1) -
000031 LIB('DB2TEST.DB2.LOAD')
000032 END
The DB2 system is named db2t here (test environment) and
the program name is L94L1, and the plan name is L94L1.
The load module executable is in DB2test.db2.load...

I would paste in IMS with DB/2 JCL, but in summary, just
say it is WAY different than the above, because IMS is running
the show while the above had TSO connecting DB2 to the cobol
program...
Here is a PARTIAL fragment of IMS/DB2 JCL:

000010 //JOBLIB DD DISP=SHR,DSN=DB2.TEST.SDSNLOAD
000011 // DD DISP=SHR,DSN=DB2.TEST.SDSNEXIT
000012 // DD DISP=SHR,DSN=DB2TEST.DB2.LOAD
000013 // DD DISP=SHR,DSN=MVS1.COBOL2.COB2LIB
000014 // DD DISP=SHR,DSN=MVS1.IMSTEST.RESLIB
000015 // DD DISP=SHR,DSN=LRTS.CIAO.TRANLIB
000016 //*
Notice that here the batch IMS DFSRRC00 is in the drivers seat
and the IMS/DB2 utility DSNMTV01 is being executed with PSB
L77AA. Fun huh?
000017 //STEP01 EXEC PGM=DFSRRC00,PARM='DLI,DSNMTV01,L77AA',
000018 // REGION=4096K
000019 //DDITV02 DD *
000020 DB2T,,DSNMIN10,,R,-,Q450100,L77AA,L77AA
000021 //*
000022 //DDOTV02 DD DSN=&&INFO,DISP=(,PASS),
000023 // UNIT=SYSDA,SPACE=(CYL,(1,1),RLSE),
000024 // DCB=(RECFM=VB,LRECL=4092,BLKSIZE=4096)
000025 //*------------------------------------------------
000026 //*-- IMS DATA ---
000027 //*------------------------------------------------
000028 //DFSRESLB DD DSN=MVS1.IMSTEST.RESLIB,DISP=SHR +I IMS RESLIB
000029 //DFSESL DD DSN=MVS1.IMSTEST.RESLIB,DISP=SHR +I IMS RESLIB
000030 //IMS DD DSN=IMSAIMS.PSBLIB,DISP=SHR IMS PSBLIB
000031 // DD DSN=IMSAIMS.DBDLIB,DISP=SHR IMS DBDLIB
Chris Mason                                                              
       
"The Unknown COBOL Programmer"                                           
       
The opinions expressed are mine, not my Employers.                       
       
cma··.@lms··d.com or HCM··.@ix.··m.com
```

#### ↳ Re: Book on SQL in COBOL ???

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1996-01-11T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-4ce5da84e6-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4d2ckc$ko4@newsbf02.news.aol.com>`
- **References:** `<4d2ckc$ko4@newsbf02.news.aol.com>`

```
In article <4d2ckc$k.··.@new··l.com>, ste··.@a··.com says...
› 
› Looking for a recommendation on a book on coding SQL in Mainframe COBOL
› programs (mixed environment, IMS, DB2, CICS, IMS-DC, etc).  What I need is
› a "how-to" with pratical examples of using SQL.  Any and all information
› about the books out there is appreciated.

The COBOL FAQ has a number of books listed. You can get to the FAQ through
a link from The Flexus COBOL Page http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
