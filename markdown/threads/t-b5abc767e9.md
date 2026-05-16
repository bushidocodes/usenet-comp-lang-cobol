[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MVS Cobol help needed

_5 messages · 5 participants · 1999-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### MVS Cobol help needed

- **From:** mfeinshtein@my-dejanews.com
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78k49s$ee9$1@nnrp1.dejanews.com>`

```
Dear sirs,

I'm just new to Cobol.I have some problems with running a very simple COBOL
program on MVS(OS/390).

Listed are the Cobol program and the JCL. Together they produce the
listed dump

000001 IDENTIFICATION DIVISION.
000002 PROGRAM-ID. SeqWrite.
000003 ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT OPTIONAL TestFile
               ASSIGN TO PHONLST
               ACCESS MODE  IS SEQUENTIAL
               ORGANIZATION IS SEQUENTIAL
               FILE STATUS  IS PhoneFileStatus.
000004 DATA DIVISION.
       FILE SECTION.
       FD TestFile
           RECORDING MODE IS F
           BLOCK CONTAINS   5 RECORDS
           RECORD CONTAINS 30 CHARACTERS.
       01  PhoneData.
           05  FirstName   PIC X(10).
           05  LastName    PIC X(10).
           05  AreaCode    PIC 999.
           05  PhoneNumber PIC 9(7).
       WORKING-STORAGE SECTION.
       77  PhoneFileStatus PIC XX VALUE "00".
       01  FredsPhone.
           05  FirstName   PIC X(10) VALUE "Fred".
           05  LastName    PIC X(10) VALUE "Anonymous".
           05  AreaCode    PIC 999   VALUE 711.
           05  PhoneNumber PIC 9(7)  VALUE  5559438.
000005 PROCEDURE DIVISION.
000006 Mainline.
           OPEN OUTPUT TestFile.
           PERFORM WriteFourRecords.
           CLOSE TestFile.
           STOP RUN.

       WriteFourRecords.
           MOVE "Billy Bob" TO FirstName   OF PhoneData.
           MOVE "Hamhock"   TO LastName    OF PhoneData.
           MOVE 817         TO AreaCode    OF PhoneData.
           MOVE 5558016     TO PhoneNumber OF PhoneData.
           WRITE PhoneData.
           MOVE "Tim       Shane     2055550918" TO PhoneData.
           WRITE PhoneData.
           MOVE "Fanny     Brice     9725558381" TO PhoneData.
           WRITE PhoneData.
           WRITE PhoneData FROM FredsPhone.
           STOP RUN.

This is the JCL:
========================
//COBTST1  JOB  'MMM / DDD',CLASS=A,MSGCLASS=X,
//             NOTIFY=&SYSUID
//*
//COBOL  EXEC PGM=IGYCRCTL,REGION=2048K,
//            PARM=TEST(ALL,SYM)
//SYSIN    DD DSN=MAXIM.COBOL(SEQWRITE),DISP=SHR
//STEPLIB  DD  DSNAME=IGY.V1R2M0.SIGYCOMP,DISP=SHR
//SYSPRINT DD  SYSOUT=*
//SYSLIN   DD  DSNAME=&&LOADSET,UNIT=SYSDA,
//             DISP=(MOD,PASS),SPACE=(TRK,(3,3)),
//             DCB=(BLKSIZE=3200)
//SYSUT1   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT2   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT3   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT4   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT5   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT6   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
//SYSUT7   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
//LKED   EXEC PGM=HEWL,PARM=TEST,COND=(8,LT,COBOL),REGION=1024K
//SYSLIB   DD  DSNAME=CEE.SCEELKED,DISP=SHR
//SYSPRINT DD  SYSOUT=*
//SYSLIN   DD  DSNAME=&&LOADSET,DISP=(OLD,DELETE)
//         DD  DDNAME=SYSIN
//SYSLMOD  DD  DSNAME=MAXIM.LOAD(COBTEST),DISP=OLD
//SYSUT1   DD  UNIT=SYSDA,SPACE=(TRK,(10,10))
//GO     EXEC  PGM=COBTEST,
//             COND=((8,LT,COBOL),(4,LT,LKED)),
//             REGION=2048K
//STEPLIB  DD  DSNAME=SYS1.SCEERUN,DISP=SHR
//         DD  DSNAME=MAXIM.LOAD,DISP=SHR
//****  DEFINITION OF QSAM FILE TO MVS ******
//*PHONLST  DD  DSNAME=MAXIM.PHONES,DISP=SHR
//PHONLST  DD  DSNAME=MAXIM.PHONES,UNIT=SYSDA,VOL=SER=NAV003,
//             SPACE=(TRK,(20,5,1)),DISP=(MOD,PASS,CATLG),
//             DCB=(BLKSIZE=400),RECFM=F
//*
//SYSPRINT DD  SYSOUT=*
//CEEDUMP  DD  SYSOUT=*
//SYSUDUMP DD  SYSOUT=*



When I am running the program with the following line, I get

IGZ0011C MODULE IGZEINI  WAS NOT A PROPER MODULE FOR THIS SYSTEM
         ENVIRONMENT.
IEA995I SYMPTOM DUMP OUTPUT
   USER COMPLETION CODE=4093 REASON CODE=00000034
  TIME=11.35.57  SEQ=00073  CPU=0000  ASID=0047
  PSW AT TIME OF ERROR  078D1000   84CE2138  ILC 2  INTC 0D
    NO ACTIVE MODULE FOUND
    NAME=UNKNOWN
    DATA AT PSW  04CE2132 - 00181610  0A0D47F0  B0E41811
    GPR  0-3  84000000  84000FFD  00000034  00000003
    GPR  4-7  866A3B18  06693988  00000000  00000000
    GPR  8-11 00000005  0668F1C4  00000004  04CE2090
    GPR 12-15 06693010  0668F2A8  84CDB838  00000034
  END OF SYMPTOM DUMP
 User abend 4,093 dec occurred processing command 'CALL    '.
 CMD abended - 'DEBUG' terminated abnormally.

I've carefully read the explanation on IGZ0011C, but it didn't help me.

Any help will be greatly appropriated.

Kind regards,
Maxim Feinshtein,
Software engineer

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: MVS Cobol help needed

- **From:** daniel.jacot@winterthur.ch
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78kk8j$r1b$1@nnrp1.dejanews.com>`
- **References:** `<78k49s$ee9$1@nnrp1.dejanews.com>`

```
In article <78k49s$ee9$1@nnrp1.dejanews.com>,
  mfeinshtein@my-dejanews.com wrote:
> Dear sirs,
>
> I'm just new to Cobol.I have some problems with running a very simple COBOL
> program on MVS(OS/390).
>
<snip>
>        FD TestFile
>            RECORDING MODE IS F
>            BLOCK CONTAINS   5 RECORDS
>            RECORD CONTAINS 30 CHARACTERS.
<snip>
>            OPEN OUTPUT TestFile.
>            PERFORM WriteFourRecords.
<snip>
> //PHONLST  DD  DSNAME=MAXIM.PHONES,UNIT=SYSDA,VOL=SER=NAV003,
> //             SPACE=(TRK,(20,5,1)),DISP=(MOD,PASS,CATLG),
> //             DCB=(BLKSIZE=400),RECFM=F

I think that you rather get a System Abend 0C4 than anything else. Look at
SYSOUT and CEEDUMP, not at the Console!

First of all, it's a JCL-Problem: Do not try to write in a library without a
member-name! Do not try to write blocked in an unblocked file!

And before all: ALWAYS ask the file-status before you try to write in a file!

So change your code the following way:

BLOCK CONTAINS 0 RECORDS
...
OPEN OUTPUT TESTFILE
IF PHONEFILESTATUS NOT = 00
 THEN DISPLAY PHONEFILESTATUS
 ELSE
   PERFORM
   ....
END-IF
GOBACK.
//             SPACE=(TRK,(20,5)),DISP=(MOD,PASS,CATLG),
//             DCB=(LRECL=30,BLKSIZE=300),RECFM=FB

Delete your existing file first! If it still does not work (I tried it, it
worked at my installation) repost your problem and show us your entire SYSOUT!

Cheers

Daniel

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: MVS Cobol help needed

- **From:** Joseph Kohler <joe_kohler@yahoo.com>
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36AE1444.CA9BBC95@yahoo.com>`
- **References:** `<78k49s$ee9$1@nnrp1.dejanews.com>`

```


mfeinshtein@my-dejanews.com wrote:


> ---------------8<--------------snippage-----------8<

> 000001 IDENTIFICATION DIVISION.
> 000002 PROGRAM-ID. SeqWrite.

.
.  snipped stuff
.

>

>
>
…[70 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own

For one thing you compile a program names SEQWRITE and link-edit it to a module
names COBTEST.  I don't think you can do that and this MAY be causing your
problem.
```

##### ↳ ↳ Re: MVS Cobol help needed

- **From:** "Gunnar Opheim" <gunnar.opheim@eunet.no>
- **Date:** 1999-01-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01be4d5a$bab2fbc0$0100007f@vaagshaugen>`
- **References:** `<78k49s$ee9$1@nnrp1.dejanews.com> <36AE1444.CA9BBC95@yahoo.com>`

```
Joseph Kohler <joe_kohler@yahoo.com> wrote in article
<36AE1444.CA9BBC95@yahoo.com>...
> 
> For one thing you compile a program names SEQWRITE and link-edit it to a
module
> names COBTEST.  I don't think you can do that and this MAY be causing
your
> problem.

No, that is OK and not the cause of the problem.  As others has pointed out
the messages given refers to an environment incompatibility, which leads to
the U4083 abend in LE.  Have the system programmer check the content of
CEE.SCEELKED and SYS1.SCEERUN.  When this has been resolved there is still
the error with RECFM and BLKSIZE which is incompatible between the program
and the JCL.  This must be resolved otherwise the file will not open
(status key 39), and the WRITE will not work (status key 48).

Gunnar.
```

#### ↳ Re: MVS Cobol help needed

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78l33h$i8g@dfw-ixnews3.ix.netcom.com>`
- **References:** `<78k49s$ee9$1@nnrp1.dejanews.com>`

```
There have been several other replies to your question - all of which MAY be
real problems. HOWEVER, from the message you are getting, let me point out
the following problems:

A)  Do not name a "user" program "COBTEST".  This is the name of an (older)
IBM supplied utility - and you may run into some conflicts.

B) In your link-edit step, you have
   CEE.SCEELKED
but in your "go" step you have,
   SYS1.SCEERUN
Where one starts with "CEE" and the other starts with "SYS1", it is possible
(in fact likely) that they are not a "matching" set of libraries.  Verify
that they do match or try finding a SYS1.SCEELKED or a CEE.SCEERUN and see
if this helps.

C) The message that you are getting indicates that the "run-time"
environment support that you are using (SCEERUN) doesn't match the
environment where you are actually running.  My guess is that this is caused
by the absence of the "correct" boot-strap module (see above) but it COULD
also be caused by your shop's SCEERUN actually being the CICS run-time
library rather than the batch one.  I doubt this strongly, but if everything
else fails, ask whether this might be the case in your shop.

D) Finally, you mention "MVS(OS/39)".  Can you confirm that you are REALLY
running under OS/390 rather than MVS.  There are some (minor) differences in
how you should be specifying LE - if you are actually still using MVS rather
than OS/390.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
