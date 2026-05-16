[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DB2 CAF (call attach facility)

_4 messages · 4 participants · 2000-05_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### DB2 CAF (call attach facility)

- **From:** Charles Haatvedt Jr. <clastname@nospam.com>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.138cf0d15390ae349896c7@news>`

```

	I am interested in the relative performance differences between 
using the DB2 CAF (call attach facility) and TSO RUN DSN methods of 
executing COBOL II DB2 applications.

I would also be very interested in some skeleton code which utilizes the 
CAF facility. 
```

#### ↳ Re: DB2 CAF (call attach facility)

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7YQU4.564$pE3.17163@dfiatx1-snr1.gtei.net>`
- **References:** `<MPG.138cf0d15390ae349896c7@news>`

```
I didn't check if you did, but you might get more/faster/better responses
posting this question at http://www.mvshelp.com. All kinds of techie stuff
for the mainframer.
```

#### ↳ Re: DB2 CAF (call attach facility)

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 2000-05-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8g1nak$1h0v$1@wrath.news.nacamar.de>`
- **References:** `<MPG.138cf0d15390ae349896c7@news>`

```
CAF is faster because it does not initialize the TSO stuff.

Other advantages:
- Overriding SYSTSIN is a bit difficult for proc's
- You can wait in case DB2 is not active (there are two ECB). Minimize the
job-abends
- You can use a TSO call to invoke your program

We use an assembler program to initialize the CAF environment.
It's almost based on the one you can find in the DB2 books

BTW: there is also a DB2 ng available

Roland
```

#### ↳ Sample CAF Code.

- **From:** Bill <wfsent@bellatlantic.net>
- **Date:** 2000-05-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392535E5.27F97E6C@bellatlantic.net>`
- **References:** `<MPG.138cf0d15390ae349896c7@news>`

```
Hi Charles;
    This was written about 10 years ago, but it should still work...

    I'll be out of town for the next few weeks, so if you have any
questions, contact me after that...

Bill

====================================================================
caf routine - please change the names to protect the innocent..

         TITLE   'AB2CAF2 - DB2 CONNECT (OPEN AND CLOSE PLANS)'
         PRINT   NOGEN
         SPACE
*--------------------------------------------------------------------*
* AB2CAF2 TO PROVIDE DB2 CONNECTION FUNCTIONS
*
*
* PUBLIC DOMAIN SOFTWARE - PUBLISHED BY -   MAINFRAME JOURNAL
*                                           10935 ESTATE LANE
*                                           DALLAS , 75238.
*
*
*    FUNCTION
*    --------
*                1 - CONNECT TO DB2
*                2 - OPEN PLAN
*                3 - CLOSE PLAN
*                4 - DISCONNECT FROM DB2
*
*
*    LINKAGE.    (AS CALLED FROM COBOL)
*    --------
*
*        01  AB2CAF-PARAMS.
*          03  AB2CAF-FUNCTION      PIC  9.
*          03  AB2CAF-SSID          PIC  X(4).
*          03  AB2CAF-PLAN          PIC  X(8).
*          03  AB2CAF-TERMOP        PIC  X(4).
*          03  AB2CAF-RETCODE       PIC  S9(9) COMP.
*          03  AB2CAF-REASON        PIC  X(8).
*
*
*    RETURN-CODES
*    ------------
*
*        12  - UNDEFINED FUNCTION.  MUST BE 1 , 2 , 3 OR 4
*
*
*    MUST BE CALLED 'STATIC' AND MUST BE INCLUDED IN THE MAIN CSECT
*    * * * * * * * * * * * *
*
*    THE CALLING PROGRAM NEEDS TO USE THE ADDRESS FOR DSNHLI
*    AS SET UP BY THIS PROGRAM....
*--------------------------------------------------------------------*
         SPACE
AB2CAF2  CSECT                         * PROGRAM ID
         ENTRY DSNHLI                  * ENTRY POINT FOR SQL CALLS
         USING *,15                    * TEMPORARY ADDRESSABILITY
         B     BENCI18                 * GO AROUND SAVE ARES
         DC    17F'0'                  * SAVE AREA
         DC    CL8'AB2CAF2'            * PROGRAM NAME
*--------------------------------------------------------------------*
* REGISTER EQUATES                                                   *
*--------------------------------------------------------------------*
R0       EQU   0                       *
R1       EQU   1                       *
R2       EQU   2                       *
R3       EQU   3                       *
R4       EQU   4                       *
R5       EQU   5                       *
R6       EQU   6                       *
R7       EQU   7                       *
R8       EQU   8                       *
R9       EQU   9                       *
R10      EQU   10                      *
R11      EQU   11                      *
R12      EQU   12                      *
R13      EQU   13                      *
R14      EQU   14                      *
R15      EQU   15                      *
         SPACE
BENCI18  DS    0H
         STM   R14,R12,12(13)          * SAVE REGISTERS
         ST    R15,8(R13)              * SAVE CHAIN POINTER
         ST    R13,4(R15)              * LOCATE SAVE AREA
         LR    R13,R15                 * POINT TO CURRENT SAVE AREA
         DROP  R15                     * REMOVE TEMP BASE REG
         USING AB2CAF2,R13             * ESTABLISH BASE REGISTERS
         USING LINKAGE,R9              * PARM AREA
         L     R9,0(R1)                * SET PARM ADDRESS
         EJECT
*--------------------------------------------------------------------*
* MAIN LINE
*--------------------------------------------------------------------*
         SPACE
MAINLINE DS    0H
         BAL   R14,INITIAL             * INITIALIZE ROUTINE
         SPACE
MAIN0010 DS    0H
         CLI   FUNCTION,C'1'           * IF CONNECT REQUEST
         BNE   MAIN0020                *    NO - CONTINUE TEST
         BAL   R14,DB2CONN             *   YES - PERFORM CONNECT LOGIC
         B     MAINEXIT
         SPACE
MAIN0020 DS    0H
         CLI   FUNCTION,C'2'           * IF OPEN PLAN REQUEST
         BNE   MAIN0030                *    NO - CONTINUE TEST
         BAL   R14,OPENPLAN            *   YES - PERFORM OPEN LOGIC
         B     MAINEXIT
         SPACE
MAIN0030 DS    0H
         CLI   FUNCTION,C'3'           * IF CLOSE REQUEST
         BNE   MAIN0040                *    NO - CONTINUE TEST
         BAL   R14,CLOSPLAN            *   YES - PERFORM CLOSE LOGIC
         B     MAINEXIT
         SPACE
MAIN0040 DS    0H
         CLI   FUNCTION,C'4'           * IF DISCONNECT REQUEST
         BNE   MAIN0050                *    NO - CONTINUE TESTS
         BAL   R14,DB2DCON             *   YES - PERFORM CLOSE LOGIC
         B     MAINEXIT
         SPACE
MAIN0050 DS    0H
         LA    R15,12                  * UNKNOWN REQUEST , SET RC=12
         B     GOBACK
         SPACE
MAINEXIT DS    0H                      * RETURN
         LA    R15,0                   * SET RETURN CODE
         SPACE
GOBACK   DS    0H
         L     R13,4(R13)              * POINT TO SAVE AREA
         ST    R15,16(R13)             * POINT TO SAVE AREA
         LM    R14,R12,12(R13)         * RESTORE SAVED REGISTERS
         BR    R14                     * BRANCH TO RETURN
         EJECT
*--------------------------------------------------------------------*
* INITIAL LOAD OF CAF IF NEEDED                                      *
*--------------------------------------------------------------------*
INITR14  DS    F                       * RETURN ADDRESS
         SPACE
INITIAL  DS    0H
         ST    R14,INITR14             * SAVE REGISTERS
         CLC   VCONALI,HEXZERO         * IS DSNALI LOADED
         BNE   INIT0010                *  YES - LOADED CONTINUE
         LOAD  EP=DSNALI               *   NO - LOAD DSNALI
         ST    R0,VCONALI              *    STORE LOAD ADDRESS
         LOAD  EP=DSNHLI2              *    LOAD SDNHLI2
         ST    R0,VCONHLI2             *   STORE LOAD ADDRESS
         ST    R0,VCONXLI2             *   STORE LOAD ADDRESS
         SPACE
INIT0010 DS    0H
         SR    R4,R4                   * CLEAR THE WORK REGISTER
         SR    R5,R5
         SR    R6,R6
         SR    R7,R7
         SR    R8,R8
         SPACE
INITEXIT DS    0H
         L     R14,INITR14             * LOAD RETURN ADDRESS
         BR    R14                     * RETURN
         EJECT
*--------------------------------------------------------------------*
* CONNECT TO DB2 VIA CALL ATTACH
*--------------------------------------------------------------------*
CNNTR14  DS    F                       * RETURN ADDRESS
         SPACE
DB2CONN  DS    0H
         ST    R14,CNNTR14             * SAVE REGISTERS
         SPACE
CNNT0010 DS    0H
         LA    R5,SSID                 * SUBSYSTEM NAME
         LA    R6,TECB                 * START ECB
         LA    R7,SECB                 * TERMINATION ECB
         LA    R8,RIBPTR               * RELEASE INFORMATION BLOCK
         SPACE
CNNT0020 DS    0H
         MVC   DB2PARM1,=A(CONNECT)    * SET FUNCTION
         ST    R5,DB2PARM2             * SET SUBSYSTEM ID
         ST    R6,DB2PARM3             * TERMINATION ECB
         ST    R7,DB2PARM4             * START ECB ADDRESS
         ST    R8,DB2PARM5             * RELEASE INFO BLOCK
         OI    DB2PARM5,X'80'          * SET END OF PARM IND
         MVC   DB2PARM6,HEXZERO        * CLEAR REST
         LA    R1,DB2PARMS             * POINT TO PARMS
         L     R15,VCONALI             * LOAD DSNALI ADDRES
         BALR  R14,R15                 * CALL DSNALI
         ST    R15,RETCODE             * SAVE THE RETURN CODE
         BAL   R14,RSNCODE             * DETERMINE REASON CODE
CNNTEXIT DS    0H
         L     R14,CNNTR14             * LOAD RETURN ADDRESS
         BR    R14                     * RETURN
         EJECT
*--------------------------------------------------------------------*
* OPEN DB2 PLAN
*--------------------------------------------------------------------*
OPNPR14  DS    F                       * RETURN ADDRESS
         SPACE
OPENPLAN DS    0H
         ST    R14,OPNPR14             * SAVE REGISTER
         SPACE
OPNP0010 DS    0H
         LA    R5,SSID                 * SUBSYSTEM NAME
         LA    R6,PLAN                 * PLAN NAME
         MVC   DB2PARM1,=A(OPEN)       * SET FUNCTION
         ST    R5,DB2PARM2             * SET SUBSYSTEM ID
         ST    R6,DB2PARM3             * TERMINATION ECB
         OI    DB2PARM3,X'80'          * SET END OF PARM IND
         MVC   DB2PARM4,HEXZERO        * CLEAR REST
         MVC   DB2PARM5,HEXZERO
         MVC   DB2PARM6,HEXZERO
         LA    R1,DB2PARMS             * POINT TO PARMS
         L     R15,VCONALI             * LOAD DSNALI ADDRESS
         BALR  R14,R15                 * CALL DSNALI
         ST    R15,RETCODE             * SAVE THE RETURN CODE
         BAL   R14,RSNCODE             * DETERMINE REASON CODE
         SPACE
OPNPEXIT DS    0H
         L     R14,OPNPR14             * LOAD RETURN ADDRESS
         BR    R14                     * RETURN
         EJECT
*--------------------------------------------------------------------*
* CLOSE DB2 PLAN
*--------------------------------------------------------------------*
CLSPR14  DS    F                       * RETURN ADDRESS
         SPACE
CLOSPLAN DS    0H
         ST    R14,CLSPR14             * SAVE REGISTER
         SPACE
CLSO0010 DS    0H
         LA    R5,TERMOP               * TERMINATION OPTION
         MVC   DB2PARM1,=A(CLOSE)      * SET FUNCTION
         ST    R5,DB2PARM2             * SET SUBSYSTEM ID
         OI    DB2PARM2,X'80'          * SET END OF PARM IND
         MVC   DB2PARM3,HEXZERO        * CLEAR REST
         MVC   DB2PARM4,HEXZERO
         MVC   DB2PARM5,HEXZERO
         MVC   DB2PARM6,HEXZERO
         LA    R1,DB2PARMS             * POINT TO PARMS
         L     R15,VCONALI             * LOAD DSNALI ADDRESS
         BALR  R14,R15                 * CALL DSNALI
         ST    R15,RETCODE             * SAVE THE RETURN CODE
         BAL   R14,RSNCODE             * DETERMINE REASON CODE
         SPACE
CLSPEXIT DS    0H
         L     R14,CLSPR14             * LOAD RETURN ADDRESS
         BR    R14                     * RETURN
         EJECT
*--------------------------------------------------------------------*
* DISCONNECT FROM DB2
*--------------------------------------------------------------------*
DCNNR14  DS    F                       * RETURN ADDRESS
         SPACE
DB2DCON  DS    0H
         ST    R14,DCNNR14             * SAVE REGISTER
         SPACE
DCNN0010 DS    0H
         MVC   DB2PARM1,=A(DISC)       * SET FUNCTION
         OI    DB2PARM1,X'80'          * SET END OF PARM IND
         MVC   DB2PARM2,HEXZERO        * CLEAR REST
         MVC   DB2PARM3,HEXZERO
         MVC   DB2PARM4,HEXZERO
         MVC   DB2PARM5,HEXZERO
         MVC   DB2PARM6,HEXZERO
         LA    R1,DB2PARMS             * POINT TO PARMS
         L     R15,VCONALI             * LOAD DSNALI ADDRESS
         BALR  R14,R15                 * CALL DSNALI
         ST    R15,RETCODE             * SAVE THE RETURN CODE
         BAL   R14,RSNCODE             * DETERMINE REASON CODE
         SPACE
DCNNEXIT DS    0H
         L     R14,DCNNR14             * LOAD RETURN ADDRESS
         BR    R14                     * RETURN
         EJECT
*--------------------------------------------------------------------*
* HANDLE THE REASON CODE
*--------------------------------------------------------------------*
RSNCR14  DS    F                       * RETURN ADDRESS
         SPACE
RSNCODE  DS    0H
         ST    R14,RSNCR14             * SAVE RETURN CODE
         ST    R0,PACKCODE             * STORE THE REASON CODE
         UNPK  WSCHAR8(9),PACKCODE(5)
         TR    WSCHAR8(8),HEXTABLE
         MVC   REASCODE,WSCHAR8        * SET REASON CODE
RSNEXIT  DS    0H
         L     R14,RSNCR14             * LOAD RETURN ADDRESS
         BR    R14                     * RETURN
         EJECT
*-------------------------------------------------------------------
*  WORKING STORAGE
*-------------------------------------------------------------------
*-------------------------------------------------------------------
* CODE THIS WAY - IT CALLS TO DSNH.. ARE TO BE RESOLVED AT LINK TIME
*   VCONALI  DC    V(DSNALI)               * ACTIVATE VCON FOR STATIC
*   VCONXLI2 DC    V(DSNHALI)              * ACTIVATE VCON FOR STATIC
*-------------------------------------------------------------------
*-------------------------------------------------------------------
* CODE THIS WAY - IT CALLS TO DSNH.. ARE TO BE RESOLVED AT EXEC TIME
VCONALI  DC    F'0'                    * VCON FOR DSNALI
VCONXLI2 DC    F'0'                    * VCON FOR DSNHLI2
*-------------------------------------------------------------------
HEXZERO  DC    F'0'
DB2PARMS DS    0CL24
DB2PARM1 DS    F                       * GENERIC CALLING PARMS
DB2PARM2 DS    F                       *
DB2PARM3 DS    F                       *
DB2PARM4 DS    F                       *
DB2PARM5 DS    F                       *
DB2PARM6 DS    F                       *
PACKCODE DC    CL5'     '
         DC    CL8'        '
WSCHAR8  DC    CL8'        '
         DC    CL8'        '
RIBPTR   DS    F                       * RELEASE INFORMATION BLOCK
TECB     DS    F                       * TERMINATION ECB
SECB     DS    F                       * START ECB
HEXTABLE DC    XL240'00'               * TRANSLATE BINARY TO HEX
         DC    C'0123456789ABCDEF'
CONNECT  DC    CL12'CONNECT     '      * CONNECT TO DB2
OPEN     DC    CL12'OPEN        '
CLOSE    DC    CL12'CLOSE       '
DISC     DC    CL12'DISCONNECT  '
         LTORG
         EJECT
*--------------------------------------------------------------------*
*   SQL CALL ENTRY POINT             COBOL INTERFACE
*--------------------------------------------------------------------*
DSNHLI   DS    0H
         USING *,15                    * TEMP ADDRESSABILITY
         B     AB2CAF2X                * GO AROUND SAVE AREA
         DC    17F'0'                  * SAVE AREA
         DC    CL8'AB2CAF2'            * PROGRAM NAME
AB2CAF2X DS    0H
         STM   R14,R12,12(13)          * SAVE REGISTERS
         ST    R15,8(R13)              * SAVE CHAIN POINTER
         ST    R13,4(R15)              * LOCATE SAVE ARES
         LR    R13,R15                 * POINT TO CURRENT SAVE AREA
         DROP  R15                     * REMOVE TEMP BASE REG
*WFS ?
         USING DSNHLI,R13              * USING THE ADDRESS
         L     R15,VCONHLI2
         BALR  R14,R15                 * CALL CAF HANDLER
         SPACE
GOBACKX  DS    0H                      * RETURN
         L     R13,4(R13)              * POINT TO SAVE AREAS
         ST    R15,16(R13)
         LM    R14,R12,12(R13)         * RESTORE SAVE REGISTERS
         BR    R14                     * BRANCH TO RETURN
         SPACE
*---------------------------------------------------------------------
* IF CAF MODULES ARE LOADED DYNAMICALLY - CODE THIS WAY
VCONHLI2 DC    F'0'                    * CAF SQL ENTRY POINT
*---------------------------------------------------------------------
*---------------------------------------------------------------------
* IF CAF MODULES ARE INCLUDED WHEN AB2CAF2 IS LINKED - CODE THIS WAY
*    VCONHLI2 DC    V(DSNHLI2)
*---------------------------------------------------------------------
         EJECT
*---------------------------------------------------------------------
* PARM LINKAGE AREA FROM COBOL MODULE
*---------------------------------------------------------------------
LINKAGE  DSECT
FUNCTION DS    CL1
SSID     DS    CL4
PLAN     DS    CL8
TERMOP   DS    CL4
RETCODE  DS    F                       * READABLE RETURN CODE (HEX)
REASCODE DS    CL8                     * DB2'S REASON CODE
         END   AB2CAF2

=====================================================================
program that uses it...


       IDENTIFICATION DIVISION.

       PROGRAM-ID.    PROGRAM1.

       AUTHOR.        a programmer - not me - someone who used to work for
me...

           DATE-WRITTEN.  JUNE 1989.

           DATE-COMPILED.

           INSTALLATION.  a company.


      *--------------------------------------------------------------*
      * FUNCTION:  TO UNLOCK QA LOCKS                                *
      *--------------------------------------------------------------*

      *--------------------------------------------------------------*
      * UPDATED  |  BY  | REASON                                     *
      *----------+------+--------------------------------------------*
      * 03.23.89 | xxxx | FIRST VERSION                              *
      *----------+------+--------------------------------------------*


       ENVIRONMENT DIVISION.

       CONFIGURATION SECTION.

       INPUT-OUTPUT SECTION.

       FILE-CONTROL.

       SKIP3
       DATA DIVISION.

       FILE SECTION.

       EJECT
       WORKING-STORAGE SECTION.

       01  FILLER                       PIC  X(50)  VALUE
                               'PROGRAM1 WORKING STORAGE STARTS HERE'.

       01  W00-RETURN-CODE              PIC  9(5).
       01  W00-PROGRAM-NAME             PIC  X(8)  VALUE  'PROGRAM1'.
       01  W00-SECTION-NAME             PIC  X(72) VALUE  SPACES.
       01  W00-ZUSER                    PIC  X(7)  VALUE  SPACES.
       01  SUBA                         PIC  S9(4) COMP SYNC.
       01  SUBB                         PIC  S9(4) COMP SYNC.
       SKIP3
       01  ISP-VDEFINE                  PIC  X(8)  VALUE  'VDEFINE'.
       01  ISP-VDELETE                  PIC  X(8)  VALUE  'VDELETE'.
       01  ISP-VGET                     PIC  X(8)  VALUE  'VGET   '.
       01  ISP-DISPLAY                  PIC  X(8)  VALUE  'DISPLAY'.
       01  ISP-SETMSG                   PIC  X(8)  VALUE  'SETMSG '.
       01  ISP-COPY                     PIC  X(8)  VALUE  'COPY   '.
       01  ISP-FMT-CHAR                 PIC  X(8)  VALUE  'CHAR   '.
       01  ISP-FMT-FIXED                PIC  X(8)  VALUE  'FIXED  '.
       01  ISP-LEN-1                    PIC  S9(9) COMP   VALUE  +1.
       01  ISP-LEN-3                    PIC  S9(9) COMP   VALUE  +3.
       01  ISP-LEN-7                    PIC  S9(9) COMP   VALUE  +7.
       01  ISP-LEN-24                   PIC  S9(9) COMP   VALUE  +24.
       01  ISP-LEN-28                   PIC  S9(9) COMP   VALUE  +28.
       01  ISP-LEN-60                   PIC  S9(9) COMP   VALUE  +60.
       SKIP3
      *---------------------------------------------------------------*
      *  NAME LISTS AND IOS FOR ALL PANELS USED                       *
      *---------------------------------------------------------------*

       01  W100-NL-ALL                  PIC  X(3)  VALUE  '(*)'.

       01  W100-NL-FTMSG1               PIC  X(8)  VALUE  '(FTMSG1)'.
       01  W100-FTMSG1                  PIC  X(24).
       01  W100-NL-FTMSG2               PIC  X(8)  VALUE  '(FTMSG2)'.
       01  W100-FTMSG2                  PIC  X(60).
       01  W100-NL-ZUSER                PIC  X(7)  VALUE  '(ZUSER)'.
       01  W100-IO-ZUSER                PIC  X(7).

       01  W100-TABLE-A-NL-1.
         03  FILLER                     PIC  X(49) VALUE
              '(CNTL1 CNTL2 CNTL3 CNTL4 CNTL5 CNTL6 CNTL7 CNTL8 '.
         03  FILLER                     PIC  X(42) VALUE
              'CNTL9 CNTLA CNTLB CNTLC CNTLD CNTLE CNTLF)'.

       01  W100-TABLE-A-IO-1.
         03  FILLER                     OCCURS 15 TIMES.
           05  W100-CNTLNO              PIC  X(7).

       01  W100-TABLE-A-NL-2.
         03  FILLER                     PIC  X(25) VALUE
              '(L11 L12 L13 L14 L15 L16 '.
         03  FILLER                     PIC  X(24) VALUE
              'L17 L18 L19 L1A L1B L1C '.
         03  FILLER                     PIC  X(12) VALUE
              'L1D L1E L1F)'.                                           '.

       01  W100-TABLE-A-IO-2.
         03  W100-LOCKS-1               OCCURS 15 TIMES.
           05  W100-LOCK1               PIC  X(3).

       01  W100-TABLE-A-NL-3.
         03  FILLER                     PIC  X(25) VALUE
              '(L21 L22 L23 L24 L25 L26 '.
         03  FILLER                     PIC  X(24) VALUE
              'L27 L28 L29 L2A L2B L2C '.
         03  FILLER                     PIC  X(12) VALUE
              'L2D L2E L2F)'.                                           '.

       01  W100-TABLE-A-IO-3.
         03  W100-LOCKS-2               OCCURS 15 TIMES.
           05  W100-LOCK2               PIC  X(3).


       01  W100-TABLE-A-NL-4.
         03  FILLER                     PIC  X(25) VALUE
              '(CI1 CI2 CI3 CI4 CI5 CI6 '.
         03  FILLER                     PIC  X(24) VALUE
              'CI7 CI8 CI9 CIA CIB CIC '.
         03  FILLER                     PIC  X(12) VALUE
              'CID CIE CIF)'.                                           '.

       01  W100-TABLE-A-IO-4.
         03  W100-COMP-INDS             OCCURS 15 TIMES.
           05  W100-COMPIND            PIC  X(3).

       01  W100-TABLE-A-NL-6.
         03  FILLER                     PIC  X(49) VALUE
              '(MSGS1 MSGS2 MSGS3 MSGS4 MSGS5 MSGS6 MSGS7 MSGS8 '.
         03  FILLER                     PIC  X(42) VALUE
              'MSGS9 MSGSA MSGSB MSGSC MSGSD MSGSE MSGSF)'.

       01  W100-TABLE-A-IO-6.
         03  FILLER                     OCCURS 15 TIMES.
           05  W100-MSG                 PIC  X(28).

       01  W100-TABLE-A-NL-7.
         03  FILLER                     PIC  X(13) VALUE
              '(ATTR1 ATTR2)'.

       01  W100-TABLE-A-IO-7.
           05  W100-ATTR-L1             PIC  X.
           05  W100-ATTR-L2             PIC  X.
           05  W100-ATTR-CI             PIC  X.
       SKIP3
       01  W340-TRACE-FLAG              PIC  X       VALUE  'N'.
         88  TRACE-ON                                VALUE  'Y'.

       SKIP3
      *---------------------------------------------------------------*
      *  VARIABLES FOR ERROR PROCESSING AND PANEL DISPLAYING          *
      *---------------------------------------------------------------*

       01  W999-VALIDATION-ERROR        PIC  S9  COMP-3  VALUE ZERO.
           88  NO-VALIDATION-ERROR                       VALUE  +0.
           88  VALIDATION-ERROR                          VALUE  +1.

       01  W999-ABORT-REQUESTED         PIC  S9  COMP-3  VALUE ZERO.
           88  ABORT-NOT-REQUESTED                       VALUE  +0.
           88  ABORT-REQUESTED                           VALUE  +1.

       01  W999-PANEL-NAME              PIC  X(8)   VALUE  SPACES.
       01  W999-MSG-ID                  PIC  X(8)   VALUE  SPACES.
       01  W999-CURSOR                  PIC  X(8)   VALUE  SPACES.

       EJECT
       COPY  XZ2CNTLJ.
       COPY  AB2CAF.
       COPY  SQLREPLY.
       SKIP3
           EXEC SQL
                INCLUDE  TBCF020
           END-EXEC.
       EJECT
           EXEC SQL
                INCLUDE  TBUP010
           END-EXEC.
       EJECT
           EXEC SQL
                INCLUDE  SQLCA
           END-EXEC.
       EJECT

       LINKAGE SECTION.

       01  L-PARM.
         03  L-LENGTH                   PIC  S9(4)  COMP.
         03  L-DB2SYST                  PIC  X(4).

         03  L-CONNECT                  PIC  X.
           88  CONNECT-REQUIRED                     VALUE  'C'.
           88  ALREADY-CONNECTED                    VALUE  'X'.

         03  FILLER                     PIC  X(254).

       EJECT
       PROCEDURE DIVISION  USING  L-PARM.
       S10-CONTROL SECTION.
       P10-10.
           IF  TRACE-ON
               DISPLAY 'P10-10'.

           PERFORM  S20-CONNECT-DB2.

           PERFORM  S100-DEFINE-PANEL-FIELDS.

       P10-15.
           IF  TRACE-ON
               DISPLAY 'P10-15'
               DISPLAY 'TRACE FLAG = ', W340-TRACE-FLAG.

           PERFORM  S200-INITIALIZE.

       P10-20.
           IF  TRACE-ON
               DISPLAY 'P10-20'.

           PERFORM  S250-SET-ATTRIBUTES.

       P10-25.
           IF  TRACE-ON
               DISPLAY 'P10-25'.

           PERFORM  S300-PROCESS-PANEL-A.

           IF    ABORT-REQUESTED
               GO TO  P10-EXIT.

           GO TO  P10-25.

       P10-EXIT.
           IF  TRACE-ON
               DISPLAY 'P10-EXIT'.

           CALL  'ISPLINK'  USING  ISP-VDELETE
                                   W100-NL-ALL.

           PERFORM  S9999-DISCONNECT-DB2.

           STOP RUN.
           EJECT

      *--------------------------------------------------------------*
      *  CALLED BY: S10-CONTROL                                      *
      *                                                              *
      *  CALLS    : 'AB2CAF2'                                        *
      *                                                              *
      *  NOTE     : CONNECT TO DB2                                   *
      *--------------------------------------------------------------*
           SKIP3
       S20-CONNECT-DB2 SECTION.
       P20-10.
           IF  TRACE-ON
               DISPLAY 'P20-10'.

           IF       ALREADY-CONNECTED
                        GO TO  P20-20.

       P20-15.
           INITIALIZE AB2CAF-PARAMS.
           MOVE     AB2CAF-CONNECT     TO     AB2CAF-FUNCTION.
           MOVE     L-DB2SYST          TO     AB2CAF-SSID.
           CALL     'AB2CAF2'          USING  AB2CAF-PARAMS.

           IF       RETURN-CODE  NOT =  0
                        DISPLAY  'PROGRAM1 - P20-15  CONNECT ERROR'
                        DISPLAY  '  PARAMS  = ' AB2CAF-PARAMS
                        DISPLAY  '  RETCODE = ' AB2CAF-RETCODE
                        DISPLAY  '  REASON  = ' AB2CAF-REASON
                        GOBACK.
      *

       P20-20.
           INITIALIZE AB2CAF-PARAMS.
           MOVE     AB2CAF-OPEN         TO     AB2CAF-FUNCTION.
           MOVE     L-DB2SYST           TO     AB2CAF-SSID.
           MOVE     'PROGRAM1'          TO     AB2CAF-PLAN.
           MOVE     XZY-OPEN-PLAN-ERROR TO     SQLCODE.
           CALL     'AB2CAF2'           USING  AB2CAF-PARAMS.

           IF       RETURN-CODE  NOT =  0
                        DISPLAY  'PROGRAM1 - P20-15  OPEN ERROR'
                        DISPLAY  '  PARAMS  = ' AB2CAF-PARAMS
                        DISPLAY  '  RETCODE = ' AB2CAF-RETCODE
                        DISPLAY  '  REASON  = ' AB2CAF-REASON
                        GOBACK.
      *

       P20-EXIT.
           EXIT.
           EJECT

      *---------------------------------------------------------------*
      * CALLED BY  : S10-MAIN-CONTROL                                 *
      *                                                               *
      * CALLS      : NONE                                             *
      *                                                               *
      * NOTE       : DEFINES ALL ISPF PANEL FIELDS                    *
      *---------------------------------------------------------------*
       SKIP3
       S100-DEFINE-PANEL-FIELDS SECTION.
       P100-10.
           IF  TRACE-ON
               DISPLAY 'P100-10'.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-TABLE-A-NL-1
                                   W100-TABLE-A-IO-1
                                   ISP-FMT-CHAR
                                   ISP-LEN-7.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-TABLE-A-NL-2
                                   W100-TABLE-A-IO-2
                                   ISP-FMT-CHAR
                                   ISP-LEN-3.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-TABLE-A-NL-3
                                   W100-TABLE-A-IO-3
                                   ISP-FMT-CHAR
                                   ISP-LEN-3.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-TABLE-A-NL-4
                                   W100-TABLE-A-IO-4
                                   ISP-FMT-CHAR
                                   ISP-LEN-3.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-TABLE-A-NL-6
                                   W100-TABLE-A-IO-6
                                   ISP-FMT-CHAR
                                   ISP-LEN-28.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-TABLE-A-NL-7
                                   W100-TABLE-A-IO-7
                                   ISP-FMT-CHAR
                                   ISP-LEN-1.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-NL-ZUSER
                                   W100-IO-ZUSER
                                   ISP-FMT-CHAR
                                   ISP-LEN-7
                                   ISP-COPY.

           CALL  'ISPLINK'  USING  ISP-VGET
                                   W100-NL-ZUSER.

           MOVE  W100-IO-ZUSER TO       W00-ZUSER.

      *    ERROR PANELS

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-NL-FTMSG1
                                   W100-FTMSG1
                                   ISP-FMT-CHAR
                                   ISP-LEN-24.

           CALL  'ISPLINK'  USING  ISP-VDEFINE
                                   W100-NL-FTMSG2
                                   W100-FTMSG2
                                   ISP-FMT-CHAR
                                   ISP-LEN-60.

       P100-EXIT.
           EXIT.
       EJECT

      *---------------------------------------------------------------*
      * CALLED BY  : S10-MAIN-CONTROL                                 *
      *                                                               *
      * CALLS      : NONE                                             *
      *                                                               *
      * NOTE       : INITIALIZES VARIABLES                            *
      *---------------------------------------------------------------*
       SKIP3
       S200-INITIALIZE SECTION.
       P200-10.
           IF  TRACE-ON
               DISPLAY 'P200-10'.

           MOVE     SPACES     TO     W100-TABLE-A-IO-1
                                      W100-TABLE-A-IO-2
                                      W100-TABLE-A-IO-3
                                      W100-TABLE-A-IO-4
                                      W100-TABLE-A-IO-6.

           MOVE     ZEROES     TO     W999-VALIDATION-ERROR
                                      W999-ABORT-REQUESTED.

       P200-EXIT.
           EXIT.
       EJECT

       S250-SET-ATTRIBUTES SECTION.
       P250-10.
           IF  TRACE-ON
               DISPLAY 'P250-10'.

           MOVE     '0'        TO     W100-ATTR-L1
                                      W100-ATTR-L2
                                      W100-ATTR-CI.

           MOVE      W00-ZUSER  TO    UP010-TSOID.

       P250-20.
           EXEC SQL
               SELECT
                        UP010_XZYQA1
               INTO
                       :UP010-XZYQA1
               FROM
                        XZYTEC1.TBUP010
               WHERE
                        UP010_TSOID  = :UP010-TSOID
           END-EXEC.
      *
           IF       SQLCODE  =  ZERO
                        PERFORM  S1000-COMMIT
                        GO TO  P250-30.
      *
           IF       SQLCODE  =  SQL-ROW-NOT-FOUND
                        GO TO  P250-30.
      *
           IF     SQLCODE   NOT =   SQL-GOOD-RETURN-CODE
                     MOVE     'P250-20 SELECT USER ERROR'
                                             TO       W00-SECTION-NAME
                     CALL     'XZ2ERROR'     USING    SQLCA
                                                      W00-PROGRAM-NAME
                                                      W00-SECTION-NAME
                     PERFORM  S9999-DISCONNECT-DB2
                     STOP RUN.
      *
       P250-30.
           IF        TRACE-ON
                     DISPLAY 'UPDATE XZYQA1 ' UP010-XZYQA1.
      *
           IF     UP010-XZYQA1       = 'Y'
                     MOVE    '1' TO   W100-ATTR-L1
                                      W100-ATTR-L2
                                      W100-ATTR-CI.

       P250-EXIT.
           EXIT.
       EJECT

      *---------------------------------------------------------------*
      * CALLED BY  : S10-MAIN-CONTROL                                 *
      *                                                               *
      * CALLS      : S340-VALIDATE-PANEL-A                            *
      *                                                               *
      * NOTE       : DISPLAYS PANEL #1, AND CALLS VALIDATION ROUTINE  *
      *---------------------------------------------------------------*
       SKIP3
       S300-PROCESS-PANEL-A SECTION.
       P300-10.
           IF  TRACE-ON
                DISPLAY  'P300-10'.

           MOVE     'C2CF600A'     TO     W999-PANEL-NAME.
           PERFORM  S999-DISPLAY-PANEL.

           IF  ABORT-REQUESTED
               GO TO  P300-EXIT.

           IF  TRACE-ON
               DISPLAY  'P300-10'.

           MOVE     SPACES     TO     W100-TABLE-A-IO-6.

       P300-20.
           PERFORM  S340-VALIDATE-PANEL-A
               VARYING  SUBA  FROM 1 BY 1
                   UNTIL  SUBA  >  15
                   OR     W100-CNTLNO(SUBA)  =   SPACES.

           IF  VALIDATION-ERROR
                   GO TO  P300-10.

           PERFORM  S500-CLEAR-FIELDS
               VARYING  SUBB   FROM   SUBA BY 1
               UNTIL    SUBB   >   15.

       P300-EXIT.
           EXIT.
       EJECT

      *---------------------------------------------------------------*
      * CALLED BY  : S300-PROCESS-PANEL-A                             *
      *                                                               *
      * CALLS      : S400-CHECK-CNTLNO-EXISTS                         *
      *                                                               *
      * NOTE       : SELECTS RECORDS ACCORDING TO INPUT CRITERIA      *
      *---------------------------------------------------------------*
       SKIP3
       S340-VALIDATE-PANEL-A SECTION.
       P340-10.
           IF  TRACE-ON
                DISPLAY  'P340-10'.

           IF          W100-CNTLNO(SUBA) =  'TRACE'
               MOVE    'Y'             TO     W340-TRACE-FLAG
               MOVE    +1              TO     W999-VALIDATION-ERROR
               MOVE    SPACES          TO     W100-TABLE-A-IO-1
               GO TO  P340-EXIT.

           IF          W100-CNTLNO(SUBA) =  'NOTRACE'
               MOVE    'N'             TO     W340-TRACE-FLAG
               MOVE    +1              TO     W999-VALIDATION-ERROR
               MOVE    SPACES          TO     W100-TABLE-A-IO-1
               GO TO  P340-EXIT.

           MOVE     W100-CNTLNO(SUBA)  TO     XZ2CNTLJ-CNTLNO.

           CALL     'XZ2CNTLJ'         USING  XZ2CNTLJ.

           IF   NOT XZ2CNTLJ-REPLY-0
               MOVE  'INVALID CNTLNO'  TO        W100-MSG(SUBA)
               MOVE    +1              TO        W999-VALIDATION-ERROR
               GO TO  P340-EXIT
           ELSE
               MOVE  XZ2CNTLJ-CNTLNO   TO        W100-CNTLNO(SUBA)
                                                 CF020-CNTLNO.

           PERFORM  S400-GET-QA-LOCK-INFO.

       P340-EXIT.
           EXIT.
       EJECT

      *---------------------------------------------------------------*
      * CALLED BY  : S340-VALIDATE-PANEL-A                            *
      *                                                               *
      * CALLS      : NONE                                             *
      *                                                               *
      * NOTE       : GETS BA INFORMATION                              *
      *---------------------------------------------------------------*
       SKIP3
       S400-GET-QA-LOCK-INFO SECTION.
       P400-10.
           IF  TRACE-ON
               DISPLAY 'P400-10'.

           EXEC SQL
               SELECT
                        CF020_QA_LOCK1,
                        CF020_QA_LOCK2,
                        CF020_COMPLETE_IND
               INTO
                       :CF020-QA-LOCK1,
                       :CF020-QA-LOCK2,
                       :CF020-COMPLETE-IND
               FROM
                        XZYTEC1.TBCF020
               WHERE
                        CF020_CNTLNO = :CF020-CNTLNO
           END-EXEC.
      *
           IF       SQLCODE     =   ZERO
                     PERFORM  S1000-COMMIT
                     PERFORM  S450-UPDATE-QA-LOCKS
                     GO TO  P400-EXIT.
      *
           IF       SQLCODE     =   SQL-ROW-NOT-FOUND
               MOVE  'CTLNO NOT FOUND' TO        W100-MSG(SUBA)
               MOVE  SPACES            TO        W100-LOCK1(SUBA)
                                                 W100-LOCK2(SUBA)
                                                 W100-COMPIND(SUBA)
               MOVE    +1              TO        W999-VALIDATION-ERROR
               GO TO  P400-EXIT
      *
           IF     SQLCODE   NOT =   SQL-GOOD-RETURN-CODE
                     MOVE     'P400-20 SELECT ERROR'
                                             TO       W00-SECTION-NAME
                     CALL     'XZ2ERROR'     USING    SQLCA
                                                      W00-PROGRAM-NAME
                                                      W00-SECTION-NAME
                     PERFORM  S9999-DISCONNECT-DB2
                     STOP RUN.
      *

       P400-EXIT.
           EXIT.
           EJECT

      *---------------------------------------------------------------*
      * CALLED BY  : S340-PROCESS-PANEL-1                             *
      *                                                               *
      * CALLS      : NONE                                             *
      *                                                               *
      * NOTE       : UPDATE QA LOCKS                                  *
      *---------------------------------------------------------------*
       SKIP3
       S450-UPDATE-QA-LOCKS SECTION.
       P450-10.
           IF  TRACE-ON
                DISPLAY  'P450-10'
                DISPLAY  'ATTR1 = ', W100-ATTR-L1
                DISPLAY  'ATTR2 = ', W100-ATTR-L2
                DISPLAY  'ATTR3 = ', W100-ATTR-CI.

           MOVE   SPACES              TO   W100-MSG(SUBA).

           IF     W100-ATTR-L1        =    '0'
                  MOVE      'ACCESS DENIED'
                                      TO   W100-MSG(SUBA)
                  GO TO  P450-20-UPDATE.

       P450-15.
           IF  TRACE-ON
                DISPLAY  'P450-15'.

           IF  TRACE-ON
                DISPLAY  'LOCK1 = ', W100-LOCK1(SUBA)
                DISPLAY  'LOCK2 = ', W100-LOCK2(SUBA)
                DISPLAY  'COMPIND = ', W100-COMPIND(SUBA)
                DISPLAY  'CFLOCK1 = ', CF020-QA-LOCK1
                DISPLAY  'CFLOCK2 = ', CF020-QA-LOCK2
                DISPLAY  'CFCOMPIND = ', CF020-COMPLETE-IND.

           IF     W100-LOCK1(SUBA) NOT = SPACES
              AND W100-LOCK1(SUBA) NOT = CF020-QA-LOCK1
                  MOVE      W100-LOCK1(SUBA)
                                      TO   CF020-QA-LOCK1
                  STRING W100-MSG(SUBA)
                     'LOCK1 ' DELIMITED BY '  '
                     INTO W100-MSG(SUBA).

           IF     W100-LOCK2(SUBA) NOT = SPACES
              AND W100-LOCK2(SUBA) NOT = CF020-QA-LOCK2
                  MOVE      W100-LOCK2(SUBA)
                                      TO   CF020-QA-LOCK2
                  STRING W100-MSG(SUBA)
                     ' LOCK2' DELIMITED  BY '  '
                     INTO W100-MSG(SUBA).

           IF     W100-COMPIND(SUBA) NOT = SPACES
              AND W100-COMPIND(SUBA) NOT = CF020-COMPLETE-IND
                  MOVE      W100-COMPIND(SUBA)
                                      TO   CF020-COMPLETE-IND
                  STRING W100-MSG(SUBA)
                     ' COMP IND' DELIMITED  BY '  '
                     INTO W100-MSG(SUBA).

       P450-20-UPDATE.
           MOVE     CF020-QA-LOCK1     TO     W100-LOCK1(SUBA).
           MOVE     CF020-QA-LOCK2     TO     W100-LOCK2(SUBA).
           MOVE     CF020-COMPLETE-IND TO     W100-COMPIND(SUBA).

           IF     W100-MSG(SUBA) = SPACES OR
                  W100-MSG(SUBA) = 'ACCESS DENIED'
                   GO TO  P450-EXIT.

           STRING W100-MSG(SUBA) ' UPDATED.' DELIMITED  BY  '  '
                INTO W100-MSG(SUBA).

           EXEC SQL
              UPDATE  XZYTEC1.TBCF020
                SET CF020_LASTUPDT_BY  =  :W00-ZUSER,
                    CF020_QA_LOCK1     =  :CF020-QA-LOCK1,
                    CF020_QA_LOCK2     =  :CF020-QA-LOCK2,
                    CF020_COMPLETE_IND =  :CF020-COMPLETE-IND,
                    CF020_LASTUPDT     =  CURRENT TIMESTAMP
                WHERE
                    CF020_CNTLNO       =  :CF020-CNTLNO
           END-EXEC.

           IF     SQLCODE       =   ZERO
                     PERFORM  S1000-COMMIT
                     GO TO  P450-EXIT.

           IF     SQLCODE   =   SQL-DUPLICATE-ROW
                     MOVE      'NO CHANGE MADE'
                                      TO   W100-MSG(SUBA)
                     GO TO  P450-EXIT.

           IF     SQLCODE   =    SQL-ROW-NOT-FOUND
                     MOVE      'CNTLNO INVALID'
                                      TO   W100-MSG(SUBA)
                     GO TO  P450-EXIT.

           IF     SQLCODE   NOT =   ZERO
                     PERFORM  S9999-DISCONNECT-DB2
                     STOP RUN.


       P450-EXIT.
           EXIT.
           EJECT

      *---------------------------------------------------------------*
      * CALLED BY  : S10-CONTROL                                      *
      *                                                               *
      * CALLS      : NONE                                             *
      *                                                               *
      * NOTE       : CLEARS FIELDS                                    *
      *---------------------------------------------------------------*
       SKIP3
       S500-CLEAR-FIELDS SECTION.
       P500-10.
           IF  TRACE-ON
               DISPLAY 'P500-10'.

           MOVE     SPACES     TO     W100-LOCK1(SUBB)
                                      W100-LOCK2(SUBB)
                                      W100-COMPIND(SUBB).

       P500-EXIT.
           EXIT.
           EJECT


      *---------------------------------------------------------------*
      * CALLED BY  : S300-PROCESS-PANEL-A                             *
      *                                                               *
      * CALLS      : NONE                                             *
      *                                                               *
      * NOTE       : DISPLAYS PANELS                                  *
      *---------------------------------------------------------------*
       SKIP3
       S999-DISPLAY-PANEL SECTION.
       P999-10.
           IF  TRACE-ON
                DISPLAY  'P999-10'.

           CALL    'ISPLINK'  USING  ISP-DISPLAY
                                     W999-PANEL-NAME
                                     W999-MSG-ID
                                     W999-CURSOR.

           IF      RETURN-CODE  NOT =  ZERO
                       MOVE  +1   TO  W999-ABORT-REQUESTED.

           IF      TRACE-ON
                       MOVE     RETURN-CODE     TO     W00-RETURN-CODE
                       DISPLAY  'P999-10'
                       DISPLAY  'RETURN CODE = ', W00-RETURN-CODE.

           MOVE    SPACES   TO  W999-MSG-ID
                                W999-CURSOR.

           MOVE    ZERO     TO  W999-VALIDATION-ERROR.

       P999-EXIT.
           EXIT.
           EJECT

      *---------------------------------------------------------------*
      * CALLED BY  :                                                  *
      *                                                               *
      * CALLS      : NONE                                             *
      *                                                               *
      * NOTE       : COMMITS ALL DB2 TRANSACTIONS                     *
      *---------------------------------------------------------------*
       SKIP3
       S1000-COMMIT SECTION.
       P1000-10.
           IF  TRACE-ON
               DISPLAY  'P1000-10'.

           EXEC SQL
                COMMIT
           END-EXEC.

           IF     SQLCODE   NOT =   ZERO
                     MOVE    'P1000-10 - SQL COMMIT ERROR'
                                            TO       W00-SECTION-NAME
                     CALL    'XZ2ERROR'     USING    SQLCA
                                                     W00-PROGRAM-NAME
                                                     W00-SECTION-NAME
                     PERFORM  S9999-DISCONNECT-DB2
                     STOP RUN.

       P1000-EXIT.
           EXIT.
           EJECT

      *--------------------------------------------------------------*
      *  CALLED BY: S10-CONTROL                                      *
      *                                                              *
      *  CALLS    : 'AB2CAF2'                                        *
      *                                                              *
      *  NOTE     : DISCONNECT FROM DB2                              *
      *--------------------------------------------------------------*
           SKIP3
       S9999-DISCONNECT-DB2 SECTION.
       P9999-10.
           IF  TRACE-ON
                DISPLAY  'P9999-10'.

           INITIALIZE AB2CAF-PARAMS.
           MOVE     AB2CAF-CLOSE       TO     AB2CAF-FUNCTION.
           MOVE     L-DB2SYST          TO     AB2CAF-SSID.
           MOVE     'PROGRAM1'         TO     AB2CAF-PLAN.
           MOVE     'SYNC'             TO     AB2CAF-TERMOP.
           CALL     'AB2CAF2'          USING  AB2CAF-PARAMS.

           IF       RETURN-CODE  NOT =  0
                        DISPLAY  'PROGRAM1 - P9999-10 - CLOSE PLAN'
                        DISPLAY  '  PARAMS  = ' AB2CAF-PARAMS
                        DISPLAY  '  RETCODE = ' AB2CAF-RETCODE
                        DISPLAY  '  REASON  = ' AB2CAF-REASON
                        GOBACK.
      *

           IF       ALREADY-CONNECTED
                        GO TO  P9999-EXIT.

       P9999-20.

           INITIALIZE AB2CAF-PARAMS.
           MOVE     AB2CAF-DISCONNECT  TO     AB2CAF-FUNCTION.
           CALL     'AB2CAF2'          USING  AB2CAF-PARAMS.

           IF       RETURN-CODE  NOT =  0
                        DISPLAY  'PROGRAM1 - P9999-20  DISCONNECT ERR'
                        DISPLAY  '  PARAMS  = ' AB2CAF-PARAMS
                        DISPLAY  '  RETCODE = ' AB2CAF-RETCODE
                        DISPLAY  '  REASON  = ' AB2CAF-REASON.
      *
       P9999-EXIT.
           EXIT.
       EJECT

=====================================================================
copylib


      *---------------------------------------------------------*
      * TYPE  -  COPYLIB         LAST UPDATED - SEP 10 , 1991   *
      * NAME  -  AB2CAF          BY           - WFS             *
      *                                                         *
      * FUNCTION  1 - CONNECT                                   *
      *           2 - OPEN                                      *
      *           3 - CLOSE                                     *
      *           4 - DISCONNECT                                *
      *                                                         *
      * REPLY     0 - OK                                        *
      *         ï¿½ 0 - ERROR                                     *
      *---------------------------------------------------------*

       01  AB2CAF-PARAMS.
         03  AB2CAF-FUNCTION                 PIC  9.
         03  AB2CAF-SSID                     PIC  X(4).
         03  AB2CAF-PLAN                     PIC  X(8).
         03  AB2CAF-TERMOP                   PIC  X(4).
         03  AB2CAF-RETCODE                  PIC  S9(9) COMP.
         03  AB2CAF-REASON                   PIC  X(8).

       01  AB2CAF-CONNECT                    PIC  9     VALUE  1.
       01  AB2CAF-OPEN                       PIC  9     VALUE  2.
       01  AB2CAF-CLOSE                      PIC  9     VALUE  3.
       01  AB2CAF-DISCONNECT                 PIC  9     VALUE  4.


      *---------------------------------------------------------*
      * SET THE DB2 SYSTEM NAME - FOR THOSE FUNCTIONS THAT      *
      *                           DON'T RECEIVE THE DB2 SYSID   *
      *                           AS A PASSED PARM IN LINKAGE.  *
      *---------------------------------------------------------*
      * CUSTOMISE THE SYSTEM NAME AS REQUIRED..                 *
      *---------------------------------------------------------*


       01  DB2SYST                           PIC  X(4)  VALUE  'DB2F'.


      *---------------------------------------------------------*
      * THESE ARE XZY ERROR CODES, USED IN AN ATTEMPT TO STOP   *
      * CAF CONNECT ERRORS CAUSING THE PROGRAMS TO LOOP.        *
      *                                                         *
      * IF A PLAN FAILS TO OPEN CORRECTLY , ANY SUBSEQUENT SQL  *
      * CALL LEAVES THE SQL-STATUS-CODE UNCHANGED , SO THE      *
      * PROGRAM WILL LOOP INDEFINATELY.                         *
      *---------------------------------------------------------*


       01  XZY-CONNECT-ERROR             PIC  S9(4) COMP  VALUE  -9001.
       01  XZY-OPEN-PLAN-ERROR           PIC  S9(4) COMP  VALUE  -9002.
       01  XZY-CLOSE-PLAN-ERROR          PIC  S9(4) COMP  VALUE  -9003.
       01  XZY-DISCONNECT-ERROR          PIC  S9(4) COMP  VALUE  -9004.





=====================================================================


"Charles Haatvedt Jr." wrote:

          I am interested in the relative performance differences between
  using the DB2 CAF (call attach facility) and TSO RUN DSN methods of
  executing COBOL II DB2 applications.

  I would also be very interested in some skeleton code which utilizes the
  CAF facility.
  --

               Chuck Haatvedt

           email ===>> chaatvedt at home dot com

  remove space in email address....
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
