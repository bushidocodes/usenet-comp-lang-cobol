[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# wait needed for mvs cobol II batch program

_4 messages · 4 participants · 1999-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### wait needed for mvs cobol II batch program

- **From:** Stefan Raabe <stefan.raabe@dresdner-bank.com>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37FC5399.9B258862@dresdner-bank.com>`

```
hi,

has anyone a wait routine (either an assembler subroutine) or something
similiar for an mvs cobol ii batch program? just want to wait a specific

ymount of time...

regards

stefan
```

#### ↳ Re: wait needed for mvs cobol II batch program

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ti3ua$eiq@netnews1.apci.com>`
- **References:** `<37FC5399.9B258862@dresdner-bank.com>`

```
Stefan Raabe wrote in message +ADw-37FC5399.9B258862+AEA-dresdner-bank.com+AD4-...
+AD4-hi,
+AD4-
+AD4-has anyone a wait routine (either an assembler subroutine) or something
+AD4-similiar for an mvs cobol ii batch program? just want to wait a specific
+AD4-
+AD4-ymount of time...
+AD4-
+AD4-regards
+AD4-
+AD4-stefan
+AD4-
+AD4-
Here's one I wrote several years ago.

G1F024   CSECT
+ACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAq-
+ACo-
+ACo-              AUTHOR: AL RUSSELL 8/14/90
+ACo-              PROGRAM TO WAIT FOR A CERTAIN NUMBER OF MINUTES
+ACo-
+ACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAq-
         SETUP SVAREA+AD0-SAVEREGS
         ST    R13,SAVE13
         USING SAVEREGS,R13
+ACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAq-
+ACo-
+ACo-              R1  POINTER TO PARM
+ACo-              R2  LENGTH OF PARM
+ACo-              R3  PARM
+ACo-              R4  WAIT TIME
+ACo-              R5  WORK FIELD
+ACo-
+ACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAqACoAKgAq-
         L     R1,0(,R1)               POINT TO PARM
         LH    R2,0(,R1)               GET PARM LENGTH
         LA    R3,2(,R1)               GET PARM DATA
         SR    R4,R4                   CLEAR WAIT TIME
         AH    R4,+AD0-H'1'                ASSUME 1 MINUTE
GETPARM  EQU   +ACo-
         CH    R2,+AD0-H'1'                SEE IF PARM NOT THERE
         BL    WAITLOOP                IF NOT ASSUME 1 MINUTE
         IC    R5,0(,R3)               GET PARM LENGTH
         N     R5,+AD0-X'0000000F'         CONVERT TO HEX
         LR    R4,R5                   MOVE TO LENGTH REGISTER
         CH    R2,+AD0-H'2'                SEE IF TWO BYTES LONG
         BL    WAITLOOP                DONE IF NOT
         IC    R5,1(,R3)               GET PARM BYTE 2
         N     R5,+AD0-X'0000000F'         CONVERT TO HEX
         MH    R4,+AD0-H'10'               SHIFT FIRST BYTE
         AR    R4,R5                   ADD TWO BYTES TOGETHER
WAITLOOP EQU   +ACo-
         STIMER WAIT,BINTVL+AD0-MINUTE  WAIT FOR ONE MINUTE
         BCT   R4,WAITLOOP
+ACo-
RETURN   GOBACK RC+AD0-0                   RETURN
+ACo-
SAVE13   DS    F
SAVEREGS DS    18F
MINUTE   DC    F'6000'     ONE MINUTE IN .01 SECONDS
         END

Alan Russell, PhD, CCP
Work - Russelah+AEA-apci.com
Home - AHRussell+AEA-computer.org
Home page - http://members.aol.com/ahrussell
-------------------------------------------------------
The views expressed are mine alone and do not necessarily reflect those of
my employer
```

#### ↳ Re: wait needed for mvs cobol II batch program

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ticfk$pn9@dfw-ixnews7.ix.netcom.com>`
- **References:** `<37FC5399.9B258862@dresdner-bank.com>`

```
IBM supplies one.  It is called ILBOWAT (but I think you need to call it by
the alias ILBOWAT0).  It requires that the parameter passed to it be "below
the line" and a full-word binary (I think - we had a discussion about this
quite a while ago in C.L.C.)  This routine should be in your "standard" IBM
COBOL run-time library.  (Try it with a small test program first, I think the
parameter tells you the "absolute" number of clock seconds to "wait" - but I
won't swear to that either)
```

#### ↳ Re: wait needed for mvs cobol II batch program

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7tk7ms$59j$1@nnrp1.deja.com>`
- **References:** `<37FC5399.9B258862@dresdner-bank.com>`

```
In article <37FC5399.9B258862@dresdner-bank.com>,
  stefan.raabe@dresdner-bank.com wrote:
> hi,
>
> has anyone a wait routine (either an assembler subroutine) or
> something similiar for an mvs cobol ii batch program?
>

Hi Stefan,

I wrote a routine in COBOL, based on Bill Klein's knowledge. Works with
all COBOL releases from OS/VS COBOL until the current COBOL for OS/390.
Here's the code (consider DATA(24) because ILBOWAT0 is AMODE(24)!):

       CBL DATA(24)
       IDENTIFICATION DIVISION.
       PROGRAM-ID. WAIT.
      ***
      *** DELAY IN COBOL VIA CALL TO ILBOWAT0
      ***
      *** USAGE:
      *** //S1 EXEC PGM=WAIT,PARM=NNNN
      *** NNNN IS A NUMBER IN THE RANGE OF 0001 TO 9999 SECONDS
      ***
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  DELAY-AMT               PIC S9(9) COMP.
       01  ILBOWAT0                PIC X(8) VALUE 'ILBOWAT0'.
       01  CURRENT-TIME            PIC 9(8).
       LINKAGE SECTION.
       01  PARAMETER-TO-MAIN.
         05 PARM-LENGTH PIC S9(4) COMP.
         05 PARM-TEXT   PIC X(100).
         05 PARM-REDEF REDEFINES PARM-TEXT.
          10 PARM-NUMERIC PIC 9999.
          10 FILLER       PIC X(94).
       PROCEDURE DIVISION USING PARAMETER-TO-MAIN.
       MAIN SECTION.
           MOVE PARM-NUMERIC TO DELAY-AMT
           ACCEPT CURRENT-TIME FROM TIME
           DISPLAY 'TIME OF DAY BEFORE ILBOWAT0: ', CURRENT-TIME
      *
           CALL ILBOWAT0 USING DELAY-AMT
      *
           ACCEPT CURRENT-TIME FROM TIME
           DISPLAY 'TIME OF DAY AFTER ILBOWAT0 : ', CURRENT-TIME
           GOBACK.

If you have installed a current version of OS/390 and your USS (unix) is
active, you can use the following piece of JCL (consider the
lowercase-character!):

//SLEEP EXEC PGM=BPXBATCH,PARM='SH sleep 30s'
//STDOUT DD PATH='/dev/null'
//STDIN DD PATH='/dev/null'
//STDERR DD PATH='/dev/null'

I saw this JCL in the newsgroup (mailing list) 'bit.listserv.ibm-main'.
Works in my shop. Seems to be an orinary unix-command, called from
batch.

Cheers

Daniel
------------------------------------------------------------
visit us at:
http://www.winterthur.com


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
