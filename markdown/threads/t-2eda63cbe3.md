[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I get DSN into COBOL Program

_18 messages · 10 participants · 2001-07 → 2001-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### How do I get DSN into COBOL Program

- **From:** jim.steelman@primerica.com (Jim Steelman)
- **Date:** 2001-07-24T10:02:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1743c876.0107240902.384b93f5@posting.google.com>`

```
A couple of years ago I was able to use the following COBOL subprogram
to return a list of DDnames and DSnames to a main program. This has
stopped working with the new release of OS/390. Can someone suggest
the alteration needed to this program or an alternative way for me to
get the DSN for a particular DD statement?

Thanks in advance.

Here is the old COBOL program

000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.  COBOLIIB.
000300 ENVIRONMENT DIVISION.
000400 INPUT-OUTPUT SECTION.
000500 FILE-CONTROL.
000600 DATA DIVISION.
000700 FILE SECTION.
000800 WORKING-STORAGE SECTION.
000900 01  TCB-ADDRESS-POINTER.
001000     05  TCB-ADDR-POINTER USAGE IS POINTER.
001100 01  TIOT-SEG-POINT.
001200     05  TIOT-SEG-POINTER USAGE IS POINTER.
001300     05  TIOT-SEG-PNT REDEFINES TIOT-SEG-POINTER
001400           PIC S9(9) COMP.
001500 01  JFCB-POINT.
001600     05  JFCB-POINTER USAGE IS POINTER.
001700     05  JFCB-POINT-RED REDEFINES JFCB-POINTER.
001800         10  FILLER PIC X.
001900         10  JFCB-LOW-3 PIC X(3).
002000 LINKAGE SECTION.
002100 01  DDNAME-DSN-ARRAY.
002200     05  DDNAME-DSN   OCCURS 100 TIMES INDEXED BY NDX1.
002300         10  DDA-DDNAME  PIC X(8).
002400         10  DDA-DSN     PIC X(44).
002500*
002600 01  TCB-POINTER USAGE IS POINTER.
002700 01  TCB.
002800     05  FILLER   PIC X(12).
002900     05  TIOT-POINTER USAGE IS POINTER.
003000 01  TIOT-START PIC X(24).
003100 01  TIOT-SEG.
003200     05  TIO-LEN PIC X.
003300     05  FILLER  PIC X(3).
003400     05  DD-NAME  PIC X(8).
003500     05  JFCB-ADDR PIC X(3).
003600 01  JFCB.
003700     05  FILLER PIC X(16).
003800     05  DS-NAME PIC X(44).
003900 PROCEDURE DIVISION USING DDNAME-DSN-ARRAY.
004000     MOVE LOW-VALUES TO JFCB-POINT.
004100     MOVE X'0000021C' TO TCB-ADDRESS-POINTER.
004200     SET ADDRESS OF TCB-POINTER TO TCB-ADDR-POINTER.
004300     SET ADDRESS OF TCB TO TCB-POINTER.
004400     SET ADDRESS OF TIOT-START TO TIOT-POINTER.
004500     SET TIOT-SEG-POINTER TO TIOT-POINTER.
004600     ADD 24 TO TIOT-SEG-PNT.
004700     SET ADDRESS OF TIOT-SEG TO TIOT-SEG-POINTER.
004800     SET NDX1 TO 1.
004900     PERFORM UNTIL TIO-LEN = LOW-VALUES OR NDX1 > 100
005000       MOVE DD-NAME TO DDA-DDNAME(NDX1)
005100       MOVE JFCB-ADDR TO JFCB-LOW-3
005200       SET ADDRESS OF JFCB TO JFCB-POINTER
005300       MOVE DS-NAME TO DDA-DSN(NDX1)
005400       ADD 20 TO TIOT-SEG-PNT
005500       SET ADDRESS OF TIOT-SEG TO TIOT-SEG-POINTER
005600       SET NDX1 UP BY 1
005700     END-PERFORM.
005800     GOBACK.
```

#### ↳ Re: How do I get DSN into COBOL Program

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-07-24T21:33:02+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pnfrltoq75rkmlksqkkfl15rboe556ho78@4ax.com>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com>`

```
On 24 Jul 2001 10:02:06 -0700 jim.steelman@primerica.com (Jim Steelman) wrote:

:>A couple of years ago I was able to use the following COBOL subprogram
:>to return a list of DDnames and DSnames to a main program. This has
:>stopped working with the new release of OS/390. Can someone suggest
:>the alteration needed to this program or an alternative way for me to
:>get the DSN for a particular DD statement?

Your system programmers changed to SWA above. You must use SWA access to get
to the JFCB.

I don't think that SWA access is available to COBOL.

You can always write an assembler program.

:>Thanks in advance.

:>Here is the old COBOL program

:>000100 IDENTIFICATION DIVISION.
:>000200 PROGRAM-ID.  COBOLIIB.
:>000300 ENVIRONMENT DIVISION.
:>000400 INPUT-OUTPUT SECTION.
:>000500 FILE-CONTROL.
:>000600 DATA DIVISION.
:>000700 FILE SECTION.
:>000800 WORKING-STORAGE SECTION.
:>000900 01  TCB-ADDRESS-POINTER.
:>001000     05  TCB-ADDR-POINTER USAGE IS POINTER.
:>001100 01  TIOT-SEG-POINT.
:>001200     05  TIOT-SEG-POINTER USAGE IS POINTER.
:>001300     05  TIOT-SEG-PNT REDEFINES TIOT-SEG-POINTER
:>001400           PIC S9(9) COMP.
:>001500 01  JFCB-POINT.
:>001600     05  JFCB-POINTER USAGE IS POINTER.
:>001700     05  JFCB-POINT-RED REDEFINES JFCB-POINTER.
:>001800         10  FILLER PIC X.
:>001900         10  JFCB-LOW-3 PIC X(3).
:>002000 LINKAGE SECTION.
:>002100 01  DDNAME-DSN-ARRAY.
:>002200     05  DDNAME-DSN   OCCURS 100 TIMES INDEXED BY NDX1.
:>002300         10  DDA-DDNAME  PIC X(8).
:>002400         10  DDA-DSN     PIC X(44).
:>002500*
:>002600 01  TCB-POINTER USAGE IS POINTER.
:>002700 01  TCB.
:>002800     05  FILLER   PIC X(12).
:>002900     05  TIOT-POINTER USAGE IS POINTER.
:>003000 01  TIOT-START PIC X(24).
:>003100 01  TIOT-SEG.
:>003200     05  TIO-LEN PIC X.
:>003300     05  FILLER  PIC X(3).
:>003400     05  DD-NAME  PIC X(8).
:>003500     05  JFCB-ADDR PIC X(3).
:>003600 01  JFCB.
:>003700     05  FILLER PIC X(16).
:>003800     05  DS-NAME PIC X(44).
:>003900 PROCEDURE DIVISION USING DDNAME-DSN-ARRAY.
:>004000     MOVE LOW-VALUES TO JFCB-POINT.
:>004100     MOVE X'0000021C' TO TCB-ADDRESS-POINTER.
:>004200     SET ADDRESS OF TCB-POINTER TO TCB-ADDR-POINTER.
:>004300     SET ADDRESS OF TCB TO TCB-POINTER.
:>004400     SET ADDRESS OF TIOT-START TO TIOT-POINTER.
:>004500     SET TIOT-SEG-POINTER TO TIOT-POINTER.
:>004600     ADD 24 TO TIOT-SEG-PNT.
:>004700     SET ADDRESS OF TIOT-SEG TO TIOT-SEG-POINTER.
:>004800     SET NDX1 TO 1.
:>004900     PERFORM UNTIL TIO-LEN = LOW-VALUES OR NDX1 > 100
:>005000       MOVE DD-NAME TO DDA-DDNAME(NDX1)
:>005100       MOVE JFCB-ADDR TO JFCB-LOW-3
:>005200       SET ADDRESS OF JFCB TO JFCB-POINTER
:>005300       MOVE DS-NAME TO DDA-DSN(NDX1)
:>005400       ADD 20 TO TIOT-SEG-PNT
:>005500       SET ADDRESS OF TIOT-SEG TO TIOT-SEG-POINTER
:>005600       SET NDX1 UP BY 1
:>005700     END-PERFORM.
:>005800     GOBACK.
```

##### ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-24T17:48:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jku3v$6vf$1@nntp9.atl.mindspring.net>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <pnfrltoq75rkmlksqkkfl15rboe556ho78@4ax.com>`

```
Gilbert Saint-Flour has indicated that he DOES have a (COBOL) program that
will handle SWA=ABOVE.

When/if he makes it available, I will post a reference to it.
```

###### ↳ ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-07-25T10:40:44+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cqtslt83tbmbuicmq1ajjrd214envo1q9j@4ax.com>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <pnfrltoq75rkmlksqkkfl15rboe556ho78@4ax.com> <9jku3v$6vf$1@nntp9.atl.mindspring.net>`

```
On Tue, 24 Jul 2001 17:48:32 -0500 "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

:>Gilbert Saint-Flour has indicated that he DOES have a (COBOL) program that
:>will handle SWA=ABOVE.

I didn't know that COBOL could do a call by address.

:>When/if he makes it available, I will post a reference to it.

Would be interesting.
```

###### ↳ ↳ ↳ Re: How do I get DSN into COBOL Program

_(reply depth: 4)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2001-07-25T12:29:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010725082938.08175.00000769@ng-fr1.aol.com>`
- **References:** `<cqtslt83tbmbuicmq1ajjrd214envo1q9j@4ax.com>`

```
Binyamin Dissen wrote...

>On Tue, 24 Jul 2001 17:48:32 -0500 "William M. Klein"
><wmklein@nospam.ix.netcom.com> wrote:
…[4 more quoted lines elided]…
>I didn't know that COBOL could do a call by address.

For any of the LE COBOL compilers:

      set procedure-ptr-item to entry 'subroutine'
      call procedure-ptr-item using ...

where "procedure-ptr-item" is declared something like:

     01  proceure-ptr-item procedure-pointer.

Or, in general, if you can get any entry point address into procedure-ptr-item
(passed as an argument, say), you can call specifying that name.


>
>:>When/if he makes it available, I will post a reference to it.
>
>Would be interesting.
>


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: How do I get DSN into COBOL Program

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-07-25T16:39:16+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7pitltgd143136npocqhh0rnm01mj7ob2v@4ax.com>`
- **References:** `<cqtslt83tbmbuicmq1ajjrd214envo1q9j@4ax.com> <20010725082938.08175.00000769@ng-fr1.aol.com>`

```
On 25 Jul 2001 12:29:38 GMT scomstock@aol.com (S Comstock) wrote:

:>Binyamin Dissen wrote...

:>>On Tue, 24 Jul 2001 17:48:32 -0500 "William M. Klein"
:>><wmklein@nospam.ix.netcom.com> wrote:

:>>:>Gilbert Saint-Flour has indicated that he DOES have a (COBOL) program that
:>>:>will handle SWA=ABOVE.

:>>I didn't know that COBOL could do a call by address.

:>For any of the LE COBOL compilers:

:>      set procedure-ptr-item to entry 'subroutine'
:>      call procedure-ptr-item using ...

:>where "procedure-ptr-item" is declared something like:

:>     01  proceure-ptr-item procedure-pointer.

:>Or, in general, if you can get any entry point address into procedure-ptr-item
:>(passed as an argument, say), you can call specifying that name.

So SWA access can be called by COBOL.
```

###### ↳ ↳ ↳ Re: How do I get DSN into COBOL Program

_(reply depth: 4)_

- **From:** Gilbert Saint-Flour <gsf@home.net>
- **Date:** 2001-07-26T12:36:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b600ee4$1$tfs$mr2ice@news>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <pnfrltoq75rkmlksqkkfl15rboe556ho78@4ax.com> <9jku3v$6vf$1@nntp9.atl.mindspring.net> <cqtslt83tbmbuicmq1ajjrd214envo1q9j@4ax.com>`

```
On 25 Jul 2001 at 10:40, Binyamin Dissen <postingid@dissensoftware.com> said:

>On Tue, 24 Jul 2001 17:48:32 -0500 "William M. Klein" wrote:

>:>Gilbert Saint-Flour has indicated that he DOES have a (COBOL) program
>:>that will handle SWA=ABOVE.

>I didn't know that COBOL could do a call by address.

You don't need to CALL anything to handle SWA=ABOVE.

>:>When/if he makes it available, I will post a reference to it.

>Would be interesting.

The COBOL code uses the same algorithm as the REXX function called SWAREQ which is available in the Tools&docs section of my Web page.  The algorithm hasn't changed since SWA=ABOVE was introduced in 1987.

 Gilbert Saint-flour
 Automated Migration Services
 http://members.home.net/gsf/
```

#### ↳ Re: How do I get DSN into COBOL Program

- **From:** Steve Thompson <sthompson_2@neo.rr.com>
- **Date:** 2001-07-24T21:53:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B5DEDD0.FE4AB17@neo.rr.com>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com>`

```
If you are using V2R10 AND you are on a machine that supports
z/Architecture, you will have to go back and revisit the control blocks
you are using.

Jim Steelman wrote:

> A couple of years ago I was able to use the following COBOL subprogram
> to return a list of DDnames and DSnames to a main program. This has
> stopped working with the new release of OS/390. Can someone suggest
> the alteration needed to this program or an alternative way for me to
> get the DSN for a particular DD statement?

<snip>

Regards,
Steve Thompson
OSP Consulting
330/335-9907
```

#### ↳ Re: How do I get DSN into COBOL Program

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-25T14:03:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B5ED1EC.C93FB5AC@cusys.edu>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com>`

```


Jim Steelman wrote:

> A couple of years ago I was able to use the following COBOL subprogram
> to return a list of DDnames and DSnames to a main program. This has
> stopped working with the new release of OS/390. Can someone suggest
> the alteration needed to this program or an alternative way for me to
> get the DSN for a particular DD statement?

I use the following, created by Gilbert Saint-Flour:    I just tested it
and it works (I use it to check my DD names to find out what database I am
running against).


000010  CBL XREF,MAP
000100 CBL NODYNAM,NOOPT,NOSSRANGE
000110*NODMLIST
000200 TITLE 'RETRIEVE JOB/STEP NAME PLUS DATASET INFO.'
000300 IDENTIFICATION DIVISION.
000400
000500 PROGRAM-ID.  DDNAME.
000600*---------------------------------------------------------------*
000700*                                                               *
000800*  USING POINTERS, RETRIEVE OPERATING-SYSTEM INFORMATION AND    *
000900*  RETURN IT TO THE CALLER.                                     *
001000*                                                               *
001010*  IT ONLY LOOKS AT THE DDNAME ASSOCIATED WITH THIS JOB STEP    *
001020*                                                               *
001030*  IT DOES NOT YET HANDLE CONCATENATED DATA SETS.               *
001040*                                                               *
001100*---------------------------------------------------------------*
001200     EJECT
001300 ENVIRONMENT DIVISION.
001400 CONFIGURATION SECTION.
001500
001600 INPUT-OUTPUT SECTION.
001700 FILE-CONTROL.
001800
001900 DATA DIVISION.
002000 FILE SECTION.
002100
002200*---------------------------------------------------------------*
002300* BEGINNING OF WORKING STORAGE
002400*---------------------------------------------------------------*
002500 WORKING-STORAGE SECTION.
002600
002700*---------------------------------------------------------------*
002800* DDN-SUBSCRIPTS-POINTERS
002900*---------------------------------------------------------------*
003000
003100 01  FILLER PIC X(016) VALUE 'DDN-SUBS-PNTRS**'.
003200
003300 01  DDN-SUBSCRIPTS-POINTERS.
003400     10  DDN-TCB-ADDR-POINTER-X.
003500         15  DDN-TCB-ADDR-POINTER       POINTER.
003600
003700     10  DDN-TIOT-SEG-POINTER           POINTER.
003800     10  DDN-TIOT-BINARY  REDEFINES  DDN-TIOT-SEG-POINTER
003900                                        PIC S9(09)  COMP.
004000
004100     10  DDN-JFCB-POINTER               POINTER.
004200     10  DDN-JFCB-X       REDEFINES  DDN-JFCB-POINTER.
004300         15  FILLER                     PIC X(01).
004400         15  DDN-JFCB-LOWER-3           PIC X(03).
004500     EJECT
004600
004700*---------------------------------------------------------------*
004800* WORK-MISCELLANEOUS
004900*---------------------------------------------------------------*
005000
005100 01  FILLER PIC X(016) VALUE '**WORK-MISC*****'.
005200
005300 01  WORK-MISCELLANEOUS.
005400     10  WORK-BINARY-2               PIC S9(04) COMP VALUE ZERO.
005500     10  FILLER  REDEFINES WORK-BINARY-2.
005600         15  WORK-BINARY-2L          PIC X(01).
005700         15  WORK-BINARY-2R          PIC X(01).
005710
005800 01  SWITCHES.
005810     05  SW-MAIN-SWITCH              PIC X(01)  VALUE 'N'.
005820     88  SW-MAIN                                VALUE 'Y'.
005900     EJECT
006000*---------------------------------------------------------------*
006100*  LINKAGE AREA
006200*---------------------------------------------------------------*
006300 LINKAGE SECTION.
006400
006500 01  LINK-COMM-AREA.
006600     10  LINK-JOB-NAME           PIC X(08).
006700     10  LINK-STEP-NAME          PIC X(08).
006800     10  LINK-DD-NAME            PIC X(08).
006900     10  LINK-DS-NAME            PIC X(44).
007000     10  LINK-GDG-OR-MEMBER      PIC X(08).
007100     10  LINK-CATALOG-IND        PIC X(01).
007200         88  LINK-FILE-IS-CATALOGED  VALUE 'Y'.
007300     10  LINK-FILE-TYPE          PIC X(01).
007400         88  LINK-FILE-IS-GDG        VALUE 'G'.
007500         88  LINK-FILE-IS-JES        VALUE 'J'.
007600         88  LINK-FILE-IS-PDS        VALUE 'P'.
007700         88  LINK-FILE-IS-REGULAR    VALUE 'R'.
007800     10  LINK-VOLUME-COUNT       PIC 9(01).
007900     10  LINK-VOLUMES            PIC X(30).
007910 01  PASSED-RECORD REDEFINES LINK-COMM-AREA.
007920     05  PASSED-LENGTH     PIC 9(4)  COMP.
007930     05  PASSED-UPDATE-PARM.
007940         10  PASSED-LABEL  PIC X(14).
007950***      10  FILLER        PIC X(14) VALUE 'PASSED DDNAME='
007960         10  PASSED-DDNAME PIC X(08) VALUE 'NAME=='.
007970     05  FILLER            PIC X(99).
008000
008100 01  L02-TCB-POINTER                 POINTER.
008200
008300 01  L03-TCB.
008400     10  FILLER                      PIC X(012).
008500     10  L03-TIOT-POINTER            POINTER.
008600
008700 01  L04-TIOT.
008800     10  L04-JOB-NAME                PIC X(08).
008900     10  L04-STEP-NAME               PIC X(08).
009000
009100 01  L04-TIOT-START                  PIC X(24).
009200
009300 01  L04-TIOT-SEGMENT.
009400     10  L04-TIOT-LENGTH             PIC X(01).
009500     10  FILLER                      PIC X(03).
009600     10  L04-DD-NAME                 PIC X(08).
009700     10  L04-JFCB-ADDRESS            PIC X(03).
009800
009900 01  L05-JFCB.
010000     10  FILLER                      PIC X(16).
010100     10  L05-DS-NAME                 PIC X(44).
010200     10  L05-GDG-OR-MEMBER           PIC X(08).
010300     10  L05-DMI-BYTE                PIC X(01).
010400     10  FILLER                      PIC X(33).
010500     10  L05-DSTYPE-BYTE             PIC X(01).
010600     10  FILLER                      PIC X(30).
010700     10  L05-VOLUME-COUNT-BYTE       PIC X(01).
010800     10  L05-VOLUME-LIST             PIC X(30).
010900     EJECT
011000 PROCEDURE DIVISION USING LINK-COMM-AREA.
011100
011120     IF  PASSED-LABEL  = 'PASSED DDNAME='
011121         MOVE SPACES                 TO PASSED-LABEL
011130         SET SW-MAIN                 TO TRUE
011140     END-IF
011200     MOVE X'0000021C'                TO DDN-TCB-ADDR-POINTER-X
011300     SET ADDRESS OF L02-TCB-POINTER  TO DDN-TCB-ADDR-POINTER.
011400     SET ADDRESS OF L03-TCB          TO L02-TCB-POINTER.
011500     SET ADDRESS OF L04-TIOT         TO L03-TIOT-POINTER.
011600
011700     MOVE L04-JOB-NAME               TO LINK-JOB-NAME.
011800     MOVE L04-STEP-NAME              TO LINK-STEP-NAME.
011900     INITIALIZE LINK-DS-NAME  LINK-GDG-OR-MEMBER LINK-CATALOG-IND
012000                LINK-FILE-TYPE LINK-VOLUME-COUNT LINK-VOLUMES.
012100
012200****  IF THEY DID NOT SUPPLY A DD NAME, EXIT STAGE LEFT.
012300
012400     IF LINK-DD-NAME < 'A'
012500        GOBACK
012600     END-IF.
012700
012800     MOVE LOW-VALUES TO DDN-JFCB-X.
012900     SET ADDRESS OF L04-TIOT-START   TO L03-TIOT-POINTER.
013000     SET DDN-TIOT-SEG-POINTER        TO L03-TIOT-POINTER.
013100     ADD 24                          TO DDN-TIOT-BINARY.
013200     SET ADDRESS OF L04-TIOT-SEGMENT TO DDN-TIOT-SEG-POINTER.
013300
013400****  LOOP THROUGH ALL POINTERS TO THE DD NAMES.
013500****  WHEN WE GET A MATCH, MOVE IN ALL THE FILE DATA AND EXIT.
013600
013610****  PERFORM UNTIL DD-NAME IS BLANK
013700     PERFORM UNTIL L04-TIOT-LENGTH = LOW-VALUES
013800        MOVE L04-JFCB-ADDRESS           TO DDN-JFCB-LOWER-3
013900        SET ADDRESS OF L05-JFCB         TO DDN-JFCB-POINTER
014000        IF L04-DD-NAME = LINK-DD-NAME
014100           MOVE L04-DD-NAME             TO LINK-DD-NAME
014200           MOVE L05-DS-NAME             TO LINK-DS-NAME
014300           MOVE L05-GDG-OR-MEMBER       TO LINK-GDG-OR-MEMBER
014400           IF L05-DMI-BYTE > X'79' AND < X'90'
014500              MOVE 'Y'                  TO LINK-CATALOG-IND
014600           ELSE
014700              MOVE 'N'                  TO LINK-CATALOG-IND
014800           END-IF
014900           IF L05-DMI-BYTE > X'19' AND < X'30'
015000              MOVE 'J'                  TO LINK-FILE-TYPE
015100           ELSE
015200              IF L05-DSTYPE-BYTE = X'00'
015300                 MOVE 'R'               TO LINK-FILE-TYPE
015400              ELSE
015500                 IF L05-DSTYPE-BYTE = X'01'
015600                    MOVE 'P'            TO LINK-FILE-TYPE
015700                 ELSE
015800                    IF L05-DSTYPE-BYTE = X'02'
015900                       MOVE 'G'         TO LINK-FILE-TYPE
016000                    ELSE
016100                       MOVE '?'         TO LINK-FILE-TYPE
016200                    END-IF
016300                 END-IF
016400              END-IF
016500           END-IF
016600           MOVE L05-VOLUME-COUNT-BYTE   TO WORK-BINARY-2R
016700           MOVE WORK-BINARY-2           TO LINK-VOLUME-COUNT
016800           MOVE L05-VOLUME-LIST         TO LINK-VOLUMES
016810           IF SW-MAIN
016811               DISPLAY
016812               'JJJJJJJJSSSSSSSSDDDDDDDDNNNNNNNNNNNNNNNNNNNNNNNN'
016813               'NNNNNNNNNNNNNNNNNNNNMMMMMMMMCTCVVVVVVVVVVVVVVV'
016814               'VVVVVVVVVVVVVVV'
016815               DISPLAY LINK-COMM-AREA
016820           END-IF
016900           GOBACK
017000        ELSE
017100           ADD 20                    TO DDN-TIOT-BINARY
017200           SET ADDRESS OF L04-TIOT-SEGMENT
017300                                     TO DDN-TIOT-SEG-POINTER
017400        END-IF
017500     END-PERFORM.
017501
017510     IF SW-MAIN
017520         DISPLAY
017530         'JJJJJJJJSSSSSSSSDDDDDDDDNNNNNNNNNNNNNNNNNNNNNNNN'
017540         'NNNNNNNNNNNNNNNNNNNNMMMMMMMMCTC'
017560         DISPLAY LINK-COMM-AREA
017570     END-IF.
017600
017700     GOBACK.
017800*------------ END OF SUBROUTINE DDNAME -------------------------*


Calling program is

000100*NODMLIST
000200 IDENTIFICATION DIVISION.
000300 PROGRAM-ID.    BRAZEE.
000400 ENVIRONMENT DIVISION.
000500
000600 INPUT-OUTPUT SECTION.
000700 IDMS-CONTROL SECTION.
000800 PROTOCOL.    MODE IS BATCH-AUTOSTATUS DEBUG
000900              IDMS-RECORDS MANUAL.
001000
001100 DATA DIVISION.
001200 FILE SECTION.
001300
001400
001500 SCHEMA SECTION.
001600
001700 DB     IASSS302 WITHIN IAZSC001.
001800
001900 WORKING-STORAGE SECTION.
002000
002100     COPY ABEND01.
002200
002300     COPY IDMS SUBSCHEMA-CONTROL.
002400
002500     COPY IDMS IASRCEM.
002510
002520 01  DISPLAY-LINE.
002530     10  FILLER       PIC X(13)   VALUE ', RUNNING IN '.
002540     10  DL-CV        PIC X(5)    VALUE ' CV '.
002550     10  FILLER       PIC X(6)    VALUE ' MODE.'.
002560 01  DDNAME           PIC x(8)    value 'DDNAME'.
002600
002610 01  FIND-COMM-AREA.
002620     10  FIND-JOB-NAME           PIC X(08).
002630     10  FIND-STEP-NAME          PIC X(08).
002640     10  FIND-DD-NAME            PIC X(08).
002650     10  FIND-DS-NAME            PIC X(44).
002660     10  FIND-GDG-OR-MEMBER.
002661         15  FIND-SI             PIC X(02).
002662         15  FIND-CV-NO          PIC X(02).
002663         15  FIND-CV-L1-L2       PIC X(04).
002670     10  FIND-CATALOG-IND        PIC X(01).
002680         88  FIND-FILE-IS-CATALOGED  VALUE 'Y'.
002690     10  FIND-FILE-TYPE          PIC X(01).
002691         88  FIND-FILE-IS-GDG        VALUE 'G'.
002692         88  FIND-FILE-IS-JES        VALUE 'J'.
002693         88  FIND-FILE-IS-PDS        VALUE 'P'.
002694         88  FIND-FILE-IS-REGULAR    VALUE 'R'.
002695     10  FIND-VOLUME-COUNT       PIC 9(01).
002696     10  FIND-VOLUMES            PIC X(30).
002697
005000
005091 PROCEDURE DIVISION.
005200
005300 000-MAIN-section    SECTION.
005301 000-MAIN.
005310     DISPLAY              ' STARTED ' FUNCTION CURRENT-DATE (5:2)
005320                          '/' FUNCTION CURRENT-DATE (7:2)
005330                          '/' FUNCTION CURRENT-DATE (1:4)
005340                          ' ' FUNCTION CURRENT-DATE (09:2)
005350                          ':' FUNCTION CURRENT-DATE (11:2)
005360                          ':' FUNCTION CURRENT-DATE (13:2)
005370
005400***  COPY    IDMS     SUBSCHEMA-BINDS.
005500
005600***  READY   IASAR101-REGION USAGE-MODE IS RETRIEVAL.
005800
005810     DISPLAY ' '
005900     MOVE 'SYSCTL'         TO FIND-DD-NAME.
006100     CALL DDNAME        USING FIND-COMM-AREA.
006101     IF FIND-DS-NAME = SPACES
006102         MOVE 'LOCAL'            TO DL-CV
006103     END-IF.
006104
006105     MOVE 'SYSIDMS'        TO FIND-DD-NAME.
006106     CALL DDNAME        USING FIND-COMM-AREA.
006107
006120     IF FIND-DS-NAME = SPACES
006130         DISPLAY ' THIS JOB IS NOT USING THE DATABASE'
006140         GOBACK
006150     END-IF.
006160
006200     IF FIND-CV-NO = '50'
006201         DISPLAY ' THIS JOB IS RUNNING AGAINST PRODUCTION'
006202         DISPLAY-LINE
006203         GOBACK
006204     END-IF.
006205
006214     IF   FIND-CV-NO = '60'
006215     AND (FIND-CV-L1-L2 = 'L1'
006216     OR   FIND-CV-L1-L2 = 'CV')
006217         DISPLAY ' THIS JOB IS RUNNING AGAINST DEVELOPMENT'
006218         DISPLAY-LINE
006219         GOBACK
006220     END-IF.
006221
006230     IF   FIND-CV-NO = '60'
006240     AND (FIND-CV-L1-L2 = 'L2'
006241     OR   FIND-CV-L1-L2 = 'CVT')
006250         DISPLAY ' THIS JOB IS RUNNING AGAINST TESTPROD'
006260         DISPLAY-LINE
006261         GOBACK
006262     END-IF.
006263
006280     DISPLAY " I DON'T RECOGNIZE " FIND-GDG-OR-MEMBER
006290
006400     GOBACK.
007770
007800 IDMS-ABORT.
007810     DISPLAY 'IDMS-ABORT'.
007900     COPY ABEND.
008000     COPY    IDMS IDMS-STATUS.
008100
008200*
:
```

##### ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** jim.steelman@primerica.com (Jim Steelman)
- **Date:** 2001-07-27T13:12:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1743c876.0107271212.6fba5efc@posting.google.com>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <3B5ED1EC.C93FB5AC@cusys.edu>`

```
Howard Brazee <howard.brazee@cusys.edu> wrote in message news:<3B5ED1EC.C93FB5AC@cusys.edu>...
> Jim Steelman wrote:
> 
…[11 more quoted lines elided]…
>-COBOL sample snipped to save space-

Well I tried this and got the same result as with my old program,
various binary values where the DSN should have been returned.

We are on OS/MVS 2.6. Could it be the amode/rmode of my calling
program?

Other suggestions please.
```

###### ↳ ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-07-27T15:36:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9jsjde$mdc$1@slb7.atl.mindspring.net>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <3B5ED1EC.C93FB5AC@cusys.edu> <1743c876.0107271212.6fba5efc@posting.google.com>`

```
As indicated before, this is probably a change to

   SWA=ABOVE

With this specified, none of the "old" techniques will work.
```

###### ↳ ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-27T20:39:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B61D1BE.A1AB7CA6@cusys.edu>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <3B5ED1EC.C93FB5AC@cusys.edu> <1743c876.0107271212.6fba5efc@posting.google.com>`

```
We are on OS/MVS 2.8.  I believe it worked when we were on 2.6.   My calling program is CoBOL for
MVS.

Jim Steelman wrote:

> Howard Brazee <howard.brazee@cusys.edu> wrote in message news:<3B5ED1EC.C93FB5AC@cusys.edu>...
> > Jim Steelman wrote:
…[20 more quoted lines elided]…
> Other suggestions please.
```

##### ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2001-07-31T13:33:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B66B3C6.C592D0A2@cusys.edu>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <3B5ED1EC.C93FB5AC@cusys.edu>`

```


Howard Brazee wrote:

> I use the following, created by Gilbert Saint-Flour:    I just tested it
> and it works (I use it to check my DD names to find out what database I am
> running against).

Gilbert e-mailed me asking "are you sure", as he doesn't remember writing
this.  I tried replying, but some how my e-mail fails someplace between me and
him.   I am not sure it was he who wrote this, I guess it was someone else,
but I don't know who.
```

#### ↳ Re: How do I get DSN into COBOL Program

- **From:** COBOLMAN <member@mainframeforum.com>
- **Date:** 2001-12-19T14:42:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c20fbb5_4@news.newzpig.com>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com>`

```
I have tried using this DDNAME program and we are at r2.9. It doesn't
seem pull the dsname. Should we be using a diffrent offset value?
```

##### ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-12-19T22:20:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jo8U7.2171$Cw3.232862@newsread2.prod.itd.earthlink.net>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <3c20fbb5_4@news.newzpig.com>`

```
Do you know if your system runs or doesn't run with SWA=ABOVE?  (Something
that normally only an "MVS" systems programmer knows).  So far, I have heard
that RDJFCB should work both places, but I don't know if the "sample
program" that you used does or does not use this correctly.
```

##### ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2001-12-19T23:06:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c188e1$c5bcfa00$5831e641@chottel>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <3c20fbb5_4@news.newzpig.com>`

```
Two programs were posted.  Which one are you trying?  The one I posted was
tested at work on z/OS.  I know our SWA is above the line because I had an
earlier version that was broken until I added a SWAREQ routine based upon
Gilbert St.-Flours REXX exec.

It is always possible that some control block offsets may be different on
your system.  The program I posted lists the assembler macros that I looked
at to determine my offsets.  If you can read assembler I can send you the
JCL and source to generate the DSECTS or you could extract the comments
from the posted program an with a little editing you could soon create your
own.  Contact me directly if you want


COBOLMAN <member@mainframeforum.com> wrote in article
<3c20fbb5_4@news.newzpig.com>...
> I have tried using this DDNAME program and we are at r2.9. It doesn't
> seem pull the dsname. Should we be using a diffrent offset value?
…[7 more quoted lines elided]…
>
```

#### ↳ Re: How do I get DSN into COBOL Program

- **From:** COBOLMAN <member@mainframeforum.com>
- **Date:** 2001-12-20T06:32:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c21da79$1_3@news.newzpig.com>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com>`

```
The program I am trying is the 'DDNAME' poested by Mr Brazee and others
in different groups. Does it make any diffference if the program is
compiled with DATA(24) or DATA(31)?

A seperate question. Some postings have had source code in the replies.
This source code in the reply is not in standard COBOL format ( each
line starts in col 1) but has multiple COBOL lines seperated by spaces
(see Brazee reply above). Does anyone have a parser to bring the code
into standard COBOL format?
```

##### ↳ ↳ Re: How do I get DSN into COBOL Program

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2001-12-21T01:44:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c189c1$093bec20$7834e641@chottel>`
- **References:** `<1743c876.0107240902.384b93f5@posting.google.com> <3c21da79$1_3@news.newzpig.com>`

```
Try selecting all of the program text and copying it to the clipboard. 
Startup a text editor e.g. Notepad and paste the text into it.  If it still
does not look right try Edit | Word Wrap.

COBOLMAN <member@mainframeforum.com> wrote in article
<3c21da79$1_3@news.newzpig.com>...
> The program I am trying is the 'DDNAME' poested by Mr Brazee and others
> in different groups. Does it make any diffference if the program is
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
