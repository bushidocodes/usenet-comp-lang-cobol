[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need JCL Return Code Help

_6 messages · 6 participants · 1999-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Need JCL Return Code Help

- **From:** "Lee Ann Simpson" <LSimpson@prodigy.net>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84f3gs$8dus$1@newssvr03-int.news.prodigy.com>`

```

I have a JCL/TSO problem that I cannot find an answer for.  Please refer to
the screen prints for clarification. I have checked our JCL code, as well as
the JCL people in my organization (I/S dept = 1000+) before coming here.
Our code does not use my proposed solution, and the people say this is over
their heads.  I have to believe that I am not the only one who has needed
this type of solution!
     1. Situation: I am running a JCL module that uses IEBGENER to run other
JCL modules in the same Librarian dataset. The SAS code forces an RC of 32,
which is used by the condition statement in the following steps. I am
getting ACF2 violation errors when I run the native SAS step (GWNCHECK Fig
1). The input file causes a violation, and when I use a file://LOGONID, I
get an ACF2 violation on the Librarian dataset (@CCCCCC.DDDDDDD.PULLSCH1).
     2. Attempted Correction: I have put the SAS code in a separate module
and call it with an IEBGENER step (GWN0ERR1 Fig 2). The SAS code still
forces an RC of 32 when the module runs. Although the SAS module functions
correctly, the RC of 32 is not returned to the calling program. Instead, the
program reads the IEBGENER return code, which is always 0 (because the step
executes w/o error). It has been suggested that I have the SAS module
produce a file that is read by the calling module, but I am back to ACF2
violations and a LOT more complexity than I really want! It is bad enough to
have to call a separate module for the SAS routine!
     3. Proposed Solution: At this point, it would seem logical to query the
TSO output of the SAS module (Fig 3) and return that rc to the calling
module.
     4. Problem:  Does anyone know how I can do this?  None of the MVSJCL
manuals I have searched handle return codes outside of the running module.
Will this require a combination of JCL and TSO?  Do I need to do something
in REXX and combine that with JCL?

You can respond to me here or at michaelsimpson@prodigy.net
Thanks,
     Michael

****** ***************************** Top of Data
******************************
000010 file://JOBNAME1 JOB (AAAA,1336),'SON',CLASS=7,
000020 //         MSGLEVEL=(1,1),MSGCLASS=1,REGION=3000K
000030 file://D OUTPUT DEFAULT=Y,JESDS=ALL
000040 /*ROUTE XEQ TSTMISC
000050 file://*LOGONID MMMM001
000060 file://*COM=CCCCCCCC
000070 file://UCC11RMS EXEC UCC11RMS,PARM=F
000080
file://*********************************************************************
*
000090 file://* GWNSASE2 CHECKS THE ERROR FILE OF GWN0. IF RC=32, THEN
PROCESS THE *
000100 file://* PCAI LOGIC. IF THERE WAS A PROBLEM WITH EDI3GWN0, PCAI AND
CCS NEED*
000110 file://* TO BE SKIPPED AND THE REPORT PROGRAM CALLED TO HANDLE THE
ERROR.   *
000120
file://*********************************************************************
*
000130 file://GWNCHECK EXEC SAS6,WORK='50,50'
000140 file://FILEIN   DD DSN=XXXXXXX.YYYYYYYY.EDIGWN01(+0),DISP=SHR
000150 file://SYSIN    DD *
000160 DATA _NULL_;
000170   INFILE FILEIN;
000180     INPUT
000190      @1    COND_IND            $007. ;
000200   IF COND_IND = 'SUCCESS' THEN ABORT RETURN 32;
000210 file://******
000220 file://* IF GWN0 RAN OK (RC=32) THEN PROCESS THE PCAI LOGIC AND
FOLLOW WITH
000230 file://* EDI3CCS. IF NOT, JUMP TO THE REPORTS SCHEDULER (PCAIDOIT
ELSE)
000240 file://******
000250 file://*---------------------------------------
000260 file://RUNPCAI  IF (GWNCHECK.SAS.RC = 32) THEN
000270 file://*---------------------------------------
000330 file://CHKPCAI2 EXEC PGM=ZC77
000340 file://SYSUT1   DD DSN= XXXXXXX.YYYYYYYY.PCAI(+0),DISP=SHR
000350 file://SYSUT2   DD DUMMY
000360 file://SYSPRINT DD SYSOUT=*
000370 file://SYSIN    DD DUMMY
000380 file://*-----------------------------------
000390 file://RUNPCAI2 IF (CHKPCAI2.RC = 0) THEN
000400 file://*-----------------------------------
000410 file://CALLPCAI EXEC PGM=IEBGENER
000420 file://SYSPRINT DD SYSOUT=*
000430 file://SYSIN    DD DUMMY
000440 file://SYSUT1   DD DSN=@CCCCCC.DDDDDDD.PULLSCH1(abcdPCAI),
000450 //            DISP=SHR,SUBSYS=LAM
000460 file://SYSUT2   DD SYSOUT=(,INTRDR)
000470 file://*******
000480 file://WAITPCAI EXEC CATEND,PARM='%WAIT4JOB @abcPCAI'
                                                            Fig 1

000070
file://*********************************************************************
*
000080 file://* GWNSASE1 CHECKS THE ERROR FILE OF GWN0. IF RC=32, THEN
PROCESS THE *
000090 file://* PCAI LOGIC. IF THERE WAS A PROBLEM WITH EDI3GWN0, PCAI AND
CCS NEED*
000100 file://* TO BE SKIPPED AND THE REPORT PROGRAM CALLED TO HANDLE THE
ERROR.   *
000110
file://*********************************************************************
*
000120 file://GWN0ERR1 EXEC PGM=IEBGENER
000130 file://SYSPRINT DD SYSOUT=*
000140 file://SYSIN    DD DUMMY
000150 file://SYSUT1   DD DSN=@CCCCCC.DDDDDDD.PULLSCH1(@abcPCER),
000160 //            DISP=SHR,SUBSYS=LAM
000170 file://SYSUT2   DD SYSOUT=(,INTRDR)
000180 file://******
000190 file://* IF GWN0 RAN OK (RC=32) THEN PROCESS THE PCAI LOGIC AND
FOLLOW WITH
000200 file://* EDI3CCS. IF NOT, JUMP TO THE REPORTS SCHEDULER (PCAIDOIT
ELSE)
000210 file://******
000220 file://*---------------------------------------
000230 file://PCAIDOIT IF (GWN0ERR1.RC = 32) THEN
000240 file://*---------------------------------------
                                                            Fig 2

-------JOBNAME--JOBID--ACT-STAT-OWNER----DEST/DEVICE--------RECS-HELD-DAY--T
IME
_    1 @abcPCER J00000 MOV   32 mmmm001  USMUO003                 263 363
12:08
                                                            Fig 3
```

#### ↳ Re: Need JCL Return Code Help

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O72#2RwU$GA.319@cpmsnbbsa02>`
- **References:** `<84f3gs$8dus$1@newssvr03-int.news.prodigy.com>`

```
Could you please provide the appropriate portions of sysout from your job
runs (the parts with the error messages)?

The only thing I notice right away is that in both IEBGENER, the SYSUT1
names a partioned dataset that appears to be spelled with smallcase
characters.  Is this generic naming for the purposes of this post?  The last
time I ran JCL, it wouldn't take smallcase characters.


If I read the rest of what you're saying correctly, then the "return 32:" in
the SAS code does not seem to be sending the value 32 out to the JCL?  Yes?
I always thought "return" was a statement strictly internal to SAS,
something about controlling the flow of logic . . .   Umm, try looking
around in the SAS Companion to the MVS Environment for a statement that will
explicitly send a return code to MVS (unless I'm wrong about "return").


Sincerely,
      Chris Osborne



Lee Ann Simpson <LSimpson@prodigy.net> wrote in message
news:84f3gs$8dus$1@newssvr03-int.news.prodigy.com...
>
> I have a JCL/TSO problem that I cannot find an answer for.  Please refer
to
> the screen prints for clarification. I have checked our JCL code, as well
as
> the JCL people in my organization (I/S dept = 1000+) before coming here.
> Our code does not use my proposed solution, and the people say this is
over
> their heads.  I have to believe that I am not the only one who has needed
> this type of solution!
>      1. Situation: I am running a JCL module that uses IEBGENER to run
other
> JCL modules in the same Librarian dataset. The SAS code forces an RC of
32,
> which is used by the condition statement in the following steps. I am
> getting ACF2 violation errors when I run the native SAS step (GWNCHECK Fig
…[5 more quoted lines elided]…
> correctly, the RC of 32 is not returned to the calling program. Instead,
the
> program reads the IEBGENER return code, which is always 0 (because the
step
> executes w/o error). It has been suggested that I have the SAS module
> produce a file that is read by the calling module, but I am back to ACF2
> violations and a LOT more complexity than I really want! It is bad enough
to
> have to call a separate module for the SAS routine!
>      3. Proposed Solution: At this point, it would seem logical to query
the
> TSO output of the SAS module (Fig 3) and return that rc to the calling
> module.
…[19 more quoted lines elided]…
>
//**********************************************************************
> 000090 //* GWNSASE2 CHECKS THE ERROR FILE OF GWN0. IF RC=32, THEN
> PROCESS THE *
…[5 more quoted lines elided]…
>
//*********************************************************************
> *
> 000130 //GWNCHECK EXEC SAS6,WORK='50,50'
…[34 more quoted lines elided]…
>
//*********************************************************************
> *
> 000080 //* GWNSASE1 CHECKS THE ERROR FILE OF GWN0. IF RC=32, THEN
…[6 more quoted lines elided]…
>
//*********************************************************************
> *
> 000120 //GWN0ERR1 EXEC PGM=IEBGENER
…[16 more quoted lines elided]…
> -------JOBNAME--JOBID--ACT-STAT-OWNER----DEST/DEVICE--------RECS-HELD-DAY-
-T
> IME
> _    1 @abcPCER J00000 MOV   32 mmmm001  USMUO003                 263 363
…[3 more quoted lines elided]…
>
```

#### ↳ Re: Need JCL Return Code Help

- **From:** bberman@netbox.com (B Berman)
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386bf7fd.5115216@news.ntplx.net>`
- **References:** `<84f3gs$8dus$1@newssvr03-int.news.prodigy.com>`

```
On Thu, 30 Dec 1999 02:00:19 -0600, "Lee Ann Simpson"
<LSimpson@prodigy.net> wrote:

>
>I have a JCL/TSO problem that I cannot find an answer for.  (snip...)

> The SAS code forces an RC of 32,
>which is used by the condition statement in the following steps. 
…[3 more quoted lines elided]…
>executes w/o error). 

Although I know nothing of SAS, I have had a similar experience, I
think, with an FTP job step, that runs correctly and downloads a file
to a server, but somehow does not return a good condition code to MVS.
Although the SYSOUT shows a 0000 cond code, the subsequent step which
forces an abend if the FTP fails always seems to execute anyhow.  We
have been unable to figure it out despite everyone's agreement that
the cond parameter is coded correctly, so have been forced to turn it
over to IBM Global for debugging.

----------------------------------------------------------------------
                  Bob Berman   -    West Hartford, CT                 
 mailto:bberman@netbox.com    website: http://www.ntplx.net/~bberman  
                                                                      
                  THE TRUE TERRORISTS IN AMERICA ARE                  
          THE PEOPLE WHO DEMAND TO SEE THE STORE MANAGER !            
----+----+----+----+----+----+----+----+----+----+----+----+----+----+
```

##### ↳ ↳ Re: Need JCL Return Code Help

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386C34E6.AA8FF096@zip.com.au>`
- **References:** `<84f3gs$8dus$1@newssvr03-int.news.prodigy.com> <386bf7fd.5115216@news.ntplx.net>`

```
B Berman wrote:
> 
> Although the SYSOUT shows a 0000 cond code, the subsequent step which
…[3 more quoted lines elided]…
> over to IBM Global for debugging.

COND is no longer recommended by IBM.  use:

// IF STEP.RC = 000
//....
// ENDIF

(Look it up I do not have my manuals or samples handy).

I have found Cond a weird beast and I always get it wrong if I code
from scratch.  It appears to reverse meaning in the JOB statement as
well.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Need JCL Return Code Help

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386CB9DE.E4A106E1@NOSPAMwebaccess.net>`
- **References:** `<84f3gs$8dus$1@newssvr03-int.news.prodigy.com> <386bf7fd.5115216@news.ntplx.net>`

```
Can you create a user error from within your SAS code?

If your JCL education is as old as mine, you may wish to look at
http://www.objectz.com/cobolreport/TCR_jcl.htm to see how JCL error
checking has simplified and become more powerful in recent years.  It
can look for specific system and user codes.
```

#### ↳ Re: Need JCL Return Code Help

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991231004313.24912.00000189@ng-fc1.aol.com>`
- **References:** `<84f3gs$8dus$1@newssvr03-int.news.prodigy.com>`

```
> I am
>getting ACF2 violation errors when I run the native SAS step

Isn't ACF2 a security package?  Do you have the appropriate security to the
files you're trying to access?  

Eileen (being a bit dense and abtuse tonight)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
