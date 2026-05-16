[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Accessing MQ Series queue from MF Cobol on Solaris Client

_6 messages · 4 participants · 2004-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Accessing MQ Series queue from MF Cobol on Solaris Client

- **From:** mkbobba@yahoo.com (Bob)
- **Date:** 2004-02-10T09:24:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64713ce9.0402100924.495d4bea@posting.google.com>`

```
Hi,

We have trying to code a MF Cobol program on a Solaris MQ Client to
access messages on a MQ series message queue. The MQ Server is a
mainframe.

We could compile fine but getting the following error message during
run time:

Load error : file 'mqconn'
error code: 173, pc=0, call=1, seg=0
173 Called program file not found in the drive/directory

We tried to use COMPILE DIRECTIVE "LITLINK" without much help.

The program:

==================
      *$set callfh"ctecfh"

       IDENTIFICATION DIVISION.
       PROGRAM-ID. 
                         YYYYT000.
       *DATE-WRITTEN. 10/12/2003.
      *********************************************************************
      *   Program-Id:  YYYYT000
      *  Description:  THIS IS A SAMPLE PROGRAM TO READ           
      *                PUBLISHED DATA OFF OF A PUBLISH QUEUE.
      *                AN 80 BYTE INPUT FILE IS OPENED AND READ TO
      *                OBTAIN THE QUEUE MANAGER NAME TO CONNECT TO
      *                AND THE QUEUE NAME TO BE USED BY THE PROGRAM.
      *
      *                THE PROGRAM OPENS THE QUEUE AND LOOPS GETTING
      *                ALL OF THE MESSAGES OFF OF THE QUEUE.  EACH
      *                MESSAGE IS WRITTEN TO A FILE.
      *
      *    Input Files:  1)  WFINPUT  - QUEUE NAME & MANAGER NAME
      *
      *   Output Files:  1)  YYYYT100 - PUBLISHED PERSON FILE RECORDS
      *
      *********************************************************************
      * Note:  "REPLACING COMP-3 BY COMP-5" Was Included To Override
The
      *        Datatype Defined In The Existing Copybook.  COMP-5
Provides
      *        Improved Effeciency.  When The Existing Copybook Is
Changed,
      *        The REPLACING Clause Will Have No Effect Or Can Be
Removed.
      **************************Change
Log*********************************
      *12/10/03       New Program For YYYY_lookup            
      *********************************************************************

       ENVIRONMENT DIVISION.

       CONFIGURATION SECTION.

       SOURCE-COMPUTER.
           SUN-SOLARIS.

       OBJECT-COMPUTER.
           SUN-SOLARIS.

      *
       INPUT-OUTPUT SECTION.
      *
       FILE-CONTROL.

      *    Option File
      *$SET FILETYPE"61"
           SELECT WFINPUT-FILE
               FILE STATUS IS FILE-STATUS
               ASSIGN TO UT-S-YYYYTWFINPUT.

      *    PUBLISHED PERSON File
      *$SET FILETYPE"60"
           SELECT YYYYT100-FILE
               FILE STATUS IS FILE-STATUS
               ORGANIZATION IS LINE SEQUENTIAL
               ASSIGN TO UT-S-YYYYT100.


      *$SET FILETYPE"60"
           SELECT SUMMARY-REPORT
               FILE STATUS IS FILE-STATUS
               ORGANIZATION IS LINE SEQUENTIAL
               ASSIGN TO UT-S-SUMMARY.

      *$SET FILETYPE"60"
           SELECT SUMMARY-FILE
               FILE STATUS IS FILE-STATUS
               ORGANIZATION IS LINE SEQUENTIAL
               ASSIGN TO UT-S-SUMFILE.

       DATA DIVISION.

       FILE SECTION.

       FD  WFINPUT-FILE
           RECORDING MODE              IS  F
           BLOCK   CONTAINS            0  RECORDS
           LABEL  RECORDS              ARE  OMITTED
           DATA   RECORD               IS  WFINPUT-RECORD.
       01  WFINPUT-RECORD.
           05  OPTION-QUEUE-MANAGER    PIC  X(08).
           05  OPTION-SUBCRIBER-QNAME  PIC  X(048).
           05  OPTION-FILLER           PIC  X(24).

       FD  YYYYT100-FILE
           RECORDING MODE              IS  F
           BLOCK   CONTAINS            0   RECORDS
           LABEL  RECORDS              ARE OMITTED
           DATA   RECORD               IS  YYYYT100-RECORD.

       01  YYYYT100-RECORD.
           COPY YYYYT100.

      *    REPORT FILES
       FD  SUMMARY-REPORT
           RECORDING MODE IS F
           BLOCK CONTAINS 0 RECORDS.
       01  SUMMARY-REC                      PIC X(132).

       FD  SUMMARY-FILE
           RECORDING MODE IS F
           BLOCK CONTAINS 0 RECORDS.
       01  SUMFILE-REC.
           COPY WFINFOFF.



       WORKING-STORAGE SECTION.
 
       01  WS-AREA.
           05  PROGRAM-NAME                 PIC X(08)
               VALUE 'YYYYT000'.
           05  FILLER                       PIC X(33)
               VALUE ' WORKING STORAGE AREA START HERE>'.


       01  WS-FOUND-PERSON-REC              PIC X(01) VALUE SPACES.

       01  WS-INSERTED-RECORDS              PIC 9(05) VALUE ZERO.
       01  WS-UPDATED-RECORDS               PIC 9(05) VALUE ZERO.
       01  WS-DELETED-RECORDS               PIC 9(05) VALUE ZERO.
       01  WS-TOTAL-RECORDS                 PIC 9(05) VALUE ZERO.
       01  WS-PROCESSED-RECORDS             PIC 9(05) VALUE ZERO.

      *****************************************************************
      *    WS  - GENERAL WORK FIELDS                                 
*
      *****************************************************************
       01  WS-WORK-FIELDS.
           05  WS-RECORD-LENGTH        PIC  9(05) VALUE ZERO.
           05  BLOW-UP                 PIC S9(1) VALUE ZEROS.
           05  WS-WHEN-COMPILED        PIC X(16) VALUE SPACES.
           05  WS-TIME                 PIC 9(08) VALUE ZERO.
           05  WS-GETS                 PIC 9(07) VALUE ZERO.
           05  WS-GETS-COMMIT          PIC 9(07) VALUE ZERO.
           05  WS-GETS-COMMIT-LIMIT    PIC 9(07) VALUE 5000.
           05  WS-RECS-OUT             PIC 9(07) VALUE ZERO.
           05  ABEND-MSG               PIC X(70).

           05  WMQ-QMGR                PIC X(48) VALUE SPACES.

       01  WS-MESSAGE-RECEIVED-SW      PIC X   VALUE '0'.
           88  MESSAGE-RECEIVED-OK             VALUE '1'.
           88  NO-MESSAGE-RECEIVED             VALUE '0'.

       01  WS-REPLY-BUFFER.
           05  WS-REPLY-DATA           PIC X(32600).

       01  WMQ-HCONN                   PIC S9(9) BINARY VALUE ZERO.
       01  WMQ-HOBJ-SUBSCRIBER         PIC S9(9) BINARY.
       01  WMQ-COMPCODE                PIC S9(9) BINARY.
       01  WMQ-OPTIONS                 PIC S9(9) BINARY.
       01  WMQ-REASON                  PIC S9(9) BINARY.
       01  WMQ-BUFFLEN                 PIC S9(9) BINARY.
       01  WMQ-DATALEN                 PIC S9(9) BINARY.

      *  THIS COPYBOOK IS HARDCODED IN THE PROGRAM TO ALLOW IT'S   **
      *  USE ACROSS PDM LINES.                                     **
      *                                                            **
      **-----------------------------------------------------------**

       01  WMQ2-XXSB-HEADER-LAYOUT.
           05  WMQ2-XXSB-HDR-SVC-VERS  PIC X(002) VALUE '01'.
           05  WMQ2-XXSB-HDR-SVC-RLS   PIC X(002) VALUE '01'.
           05  WMQ2-XXSB-HDR-ACCT-1    PIC X(006) VALUE 'DHRCCI'.
           05  WMQ2-XXSB-HDR-ACCT-2    PIC X(024) VALUE SPACES.
           05  FILLER                  PIC X(056) VALUE SPACES.
           05  WMQ2-XXSB-HDR-COMP-CD   PIC S9(05) VALUE +0.
           05  WMQ2-XXSB-HDR-REAS-CD   PIC S9(05) VALUE +0.


       01  WMQ2-YYYY-HEADER-LAYOUT.
           05  WMQ2-YYYY-HDR-TYPE      PIC X(001) VALUE SPACES.
               88  WMQ2-REQUEST-IS-BATCH          VALUE 'B'.
               88  WMQ2-REQUEST-IS-ONLINE         VALUE 'O'.
               88  WMQ2-REQUEST-IS-PUBLISH        VALUE 'P'.
               88  WMQ2-REQUEST-IS-HEARTBEAT      VALUE 'H'.
               88  WMQ2-REQUEST-IS-SYNC           VALUE 'S'.

           05  WMQ2-YYYY-HDR-SERVICE   PIC X(008) VALUE SPACES.

           05  FILLER REDEFINES WMQ2-YYYY-HDR-SERVICE.
               10  WMQ2-YYYY-HDR-TABLE     PIC X(004).
                   88  WMQ2-TABLE-IS-PERSON           VALUE 'PERS'.
                   88  WMQ2-TABLE-IS-XREF             VALUE 'XREF'.
               10  WMQ2-YYYY-HDR-ACTION    PIC X(004).
                   88  WMQ2-UPDATE-IS-ADD             VALUE 'ADD '.
                   88  WMQ2-UPDATE-IS-CHG             VALUE 'CHG '.
                   88  WMQ2-UPDATE-IS-DEL             VALUE 'DEL '.
                   88  WMQ2-UPDATE-IS-COMB            VALUE 'COMB'.

           05  WMQ2-YYYY-HDR-VERSION   PIC X(002) VALUE SPACES.
           05  WMQ2-YYYY-HDR-APPLIC    PIC X(004) VALUE SPACES.
           05  WMQ2-FILLER             PIC X(005) VALUE SPACES.

       01  WMQ2-PUBLISHING-HEADER.
           05  FILLER                  PIC X(203) VALUE SPACES.

       01  WMQ2-PERS-PUBLISHED-DATA.
           05  WMQ2-PPUB-PERSON-ID-CK-DIG.
               10  WMQ2-PPUB-PERSON-ID            PIC 9(09).
               10  WMQ2-PPUB-CHECK-DIGIT          PIC X(01).
           05  WMQ2-PPUB-STATUS-CODE              PIC X(01).
           05  WMQ2-PPUB-SOUNDEX-ID               PIC X(18).
           05  WMQ2-PPUB-LAST-NAME                PIC X(40).
           05  WMQ2-PPUB-FIRST-NAME               PIC X(12).
           05  WMQ2-PPUB-MIDDLE-INITIAL           PIC X(01).
           05  WMQ2-PPUB-NAME-SUFFIX              PIC X(03).
           05  WMQ2-PPUB-SSN                      PIC X(09).
           05  WMQ2-PPUB-DATE-OF-BIRTH            PIC X(08).
           05  FILLER REDEFINES  WMQ2-PPUB-DATE-OF-BIRTH.
               10  WMQ2-PPUB-DOB-CCYY             PIC X(04).
               10  WMQ2-PPUB-DOB-MM               PIC X(02).
               10  WMQ2-PPUB-DOB-DD               PIC X(02).
           05  WMQ2-PPUB-RACE                     PIC X(01).
           05  WMQ2-PPUB-SEX                      PIC X(01).
           05  WMQ2-PPUB-BIOMETRICS-CODE          PIC X(01).
           05  WMQ2-PPUB-SSI-INDICATOR            PIC X(01).
           05  WMQ2-PPUB-ACTS-MPI-NUMBER          PIC X(10).
           05  WMQ2-PPUB-LAST-EIS-CTY             PIC X(03).
           05  WMQ2-PPUB-LAST-FSIS-CTY            PIC X(03).
           05  WMQ2-PPUB-LAST-CHG-TS              PIC X(20).
           05  WMQ2-PPUB-LAST-CHG-PROG            PIC X(08).
           05  WMQ2-PPUB-LAST-CHG-USER            PIC X(08).

       01  WMQ2-XREF-PUBLISHED-DATA.
           05  WMQ2-PXRF-PERSON-ID                PIC 9(09).
           05  WMQ2-PXRF-CHECK-DIGIT              PIC X(01).
           05  WMQ2-PXRF-APP-SYS-ID               PIC X(30).
           05  WMQ2-PXRF-REFERENCE-TYPE           PIC X(01).
           05  WMQ2-PXRF-RECORD-TYPE              PIC X(04).
           05  WMQ2-PXRF-COMBINE-TS               PIC X(20).
           05  WMQ2-PXRF-LAST-CHG-USER            PIC X(08).
           05  WMQ2-PXRF-LAST-CHG-PROG            PIC X(08).
           05  WMQ2-PXRF-LAST-CHG-TS              PIC X(20).

      *
      ****************************************************************
      *   IBM MQSERIES API COPY BOOKS.                               *
      ****************************************************************
       01  MQM-OBJECT-DESCRIPTOR.
           COPY CMQODV.
       01  MQM-MESSAGE-DESCRIPTOR.
           COPY CMQMDV.
       01  MQM-PUT-MESSAGE-OPTIONS.
           COPY CMQPMOV.
       01  MQM-GET-MESSAGE-OPTIONS.
           COPY CMQGMOV.
       01  MQM-TRIGGER-MESSAGE.
           COPY CMQTML.
       01  MQM-LITERALS.
           COPY CMQV.

      *    Common Working Storage Area.
      *    Contains File Status And WS Areas For Other Common Routines
           COPY WFCOMMON.

      *    Date Checking Area.
      *    Contains Working Storage For The Date Checking Routine
           COPY WFDATE.

      *    Lookup Table Area.
      *    Contains Working Storage For Lookup Table
           COPY SHLUPTBL.

      *    Report Summary Area
      *    Contains Report Layouts For The Process Summary
           COPY WFDSSSUM.

      *    WFDSSCTL Linkage Area
      *    Will Contain DateTime Stamp And If Needed A Control Date
           COPY WFDSSLNK.

      *    Info
      *    Contains Summary Information About All The Files
      *    Can Be Referenced By DD Name Or File Number
      *    Should Be 1 Occurrance For Each Input And Output File.
       01  FILE-NO-MAX                      PIC 9(03) COMP-5 VALUE 2.
       01  FILE-SUMMARY.
           03  FILE-I OCCURS 2 TIMES INDEXED BY FILE-NO.
               COPY WFINFO  REPLACING COMP-3 BY COMP-5.
               COPY WFINFOF REPLACING COMP-3 BY COMP-5.

       01  WFINPUT-INFO.
           05  WFINPUT                      PIC 9(02) COMP-5 VALUE 01.

       01  YYYYT100-INFO.
           05  YYYYT100                     PIC 9(02) COMP-5 VALUE 02.
           COPY YYYYT10I.

      *    This Is Defintion Used By PDSCAN To Replace Input Data Less
      *    Than X'40' (Space) By Space.
       LINKAGE SECTION.
       01  WS-SCAN-L.
           05 WS-SCAN                       PIC X(1) OCCURS 100 TIMES
                                            INDEXED BY SX.

      *
       PROCEDURE DIVISION.

       0000-BEGIN.

           PERFORM 0100-INITIALIZE-RTN
              THRU 0100-EXIT.
      *
           PERFORM 1000-MAIN-PROCESS
              THRU 1000-EXIT.
      *
           PERFORM 0900-TERMINATION-RTN
              THRU 0900-EXIT.
      *
       0000-EXIT.
            STOP RUN.
      *
      ***-----------------------------------------------------------***
      *    OPEN FILES, READ RUN TIME PARMS.  VERIFY THAT VALUES      
*
      *    WERE ENTERED.                                             
*
      *    PERFORM CONNECT PARAGRAPH FOR THE MQCONNECT CALL.         
*
      ***-----------------------------------------------------------***
       0100-INITIALIZE-RTN.

           ACCEPT WS-TIME FROM TIME.
           MOVE WHEN-COMPILED  TO WS-WHEN-COMPILED.

           DISPLAY '** YYYYT000 EXECUTION BEGINNING **'.
           DISPLAY ' '.
           DISPLAY '** TIME        =', WS-TIME.
           DISPLAY '** COMPILE DATE=', WS-WHEN-COMPILED.
           DISPLAY ' '.

           OPEN INPUT  WFINPUT-FILE.
           OPEN OUTPUT YYYYT100-FILE.
      *
           READ WFINPUT-FILE
             AT END
               DISPLAY '**** WFINPUT FILE EMPTY ***'
               DISPLAY '**** WFINPUT FILE EMPTY ***'
               DIVIDE 0 INTO BLOW-UP.


           IF  OPTION-QUEUE-MANAGER   > SPACES
               DISPLAY 'USING QUEUE MANAGER    =',
                        OPTION-QUEUE-MANAGER
           ELSE
               DISPLAY '*******ERROR************'
               DISPLAY 'MISSING QUEUE MANAGER NAME'
               DISPLAY '*******ERROR************'
               DIVIDE 0 INTO BLOW-UP
           END-IF.

           IF  OPTION-SUBCRIBER-QNAME > SPACES
               DISPLAY 'USING SUBSCRIBER QUEUE =',
                        OPTION-SUBCRIBER-QNAME
           ELSE
               DISPLAY '*******ERROR************'
               DISPLAY 'MISSING  QUEUE NAME'
               DISPLAY '*******ERROR************'
               DIVIDE 0 INTO BLOW-UP
           END-IF.


           MOVE OPTION-QUEUE-MANAGER   TO WMQ-QMGR.

           PERFORM 0500-MQCONN-QMGR
              THRU 0500-EXIT.

       0100-EXIT.
            EXIT.
      *
      *
       0500-MQCONN-QMGR.
      *
      ***-----------------------------------------------------------***
      *    CONNECT TO THE SPECIFIED QUEUE MANAGER.                   
*
      ***-----------------------------------------------------------***
      *
           CALL 'MQCONN' USING WMQ-QMGR
                               WMQ-HCONN
                               WMQ-COMPCODE
                               WMQ-REASON.

           IF (WMQ-COMPCODE NOT = MQCC-OK) THEN
              MOVE 'UNEXPECTED COMPCODE ON MQCONN CALL'
                                           TO ABEND-MSG
              DISPLAY 'ABEND-MSG:' ABEND-MSG
              DISPLAY 'WMQ-COMPCODE:' WMQ-COMPCODE
              DISPLAY 'WMQ-REASON  :' WMQ-REASON
              DIVIDE 0 INTO BLOW-UP
           END-IF.

           PERFORM 0510-OPEN-SUBSCRIBE-Q
              THRU 0510-EXIT.

       0500-EXIT.
            EXIT.
      *
      *
       0510-OPEN-SUBSCRIBE-Q.

      ***----------------------------------------------------------***
      ***  OPEN THE REQUESTED QUEUE.                               ***
      ***----------------------------------------------------------***
           MOVE MQOT-Q                     TO MQOD-OBJECTTYPE.
           MOVE OPTION-SUBCRIBER-QNAME     TO MQOD-OBJECTNAME.

      ***----------------------------------------------------------***
      ***  GET THE MESSAGES WITH THE QUEUE DEFAULT OPTIONS.        ***
      ***  FAIL IF THE THE QUEUE MANAGER IS TRYING TO SHUT DOWN.   ***
      ***----------------------------------------------------------***
           COMPUTE WMQ-OPTIONS = MQOO-INPUT-AS-Q-DEF  +
                                 MQOO-FAIL-IF-QUIESCING
           END-COMPUTE.

           CALL 'MQOPEN' USING WMQ-HCONN
                               MQOD
                               WMQ-OPTIONS
                               WMQ-HOBJ-SUBSCRIBER
                               WMQ-COMPCODE
                               WMQ-REASON.

           IF (WMQ-COMPCODE NOT = MQCC-OK)
              MOVE 'UNEXPECTED COMPCODE ON MQOPEN SUBSCRIBER'
                                           TO ABEND-MSG
              DISPLAY 'ABEND-MSG:' ABEND-MSG
              DISPLAY 'WMQ-COMPCODE:' WMQ-COMPCODE
              DISPLAY 'WMQ-REASON  :' WMQ-REASON
              DIVIDE 0 INTO BLOW-UP
           END-IF.
      *
       0510-EXIT.
            EXIT.
      *
       0900-TERMINATION-RTN.

      *
      ***----------------------------------------------------------***
      ***  CLOSE THE SUBSCRIBER QUEUE.                             ***
      ***----------------------------------------------------------***
           CALL 'MQCLOSE' USING WMQ-HCONN
                                WMQ-HOBJ-SUBSCRIBER
                                MQCO-NONE
                                WMQ-COMPCODE
                                WMQ-REASON.

           IF (WMQ-COMPCODE NOT = MQCC-OK) THEN
              MOVE 'UNEXPECTED COMPCODE ON MQCLOSE CALL'
                                           TO ABEND-MSG
              DISPLAY 'ABEND-MSG:' ABEND-MSG
              DISPLAY 'WMQ-COMPCODE:' WMQ-COMPCODE
              DISPLAY 'WMQ-REASON  :' WMQ-REASON
              DIVIDE 0 INTO BLOW-UP
           END-IF.
      ***----------------------------------------------------------***
      ***  CLOSE THE FLAT FILES AND WE'RE DONE DUDE.               ***
      ***----------------------------------------------------------***

           CLOSE WFINPUT-FILE.
           CLOSE YYYYT100-FILE.

           DISPLAY '** YYYYT000 TERMINATING OKAY **'.
           DISPLAY ' '.
           DISPLAY '** MSGS READ    =', WS-GETS.
           DISPLAY '** RECS WRITTEN =', WS-RECS-OUT.
           DISPLAY ' '.

       0900-EXIT.
            EXIT.
      *

      ***----------------------------------------------------------***
      ***  THIS IS A SIMPLE MAINLINE PARAGRAPH.                    ***
      ***----------------------------------------------------------***
       1000-MAIN-PROCESS.

           MOVE ZERO TO WS-GETS.
           MOVE ZERO TO WS-GETS-COMMIT.
           SET MESSAGE-RECEIVED-OK  TO TRUE.
           PERFORM 1100-MQGET-MESSAGES
              THRU 1100-EXIT
             UNTIL NO-MESSAGE-RECEIVED.

      *
       1000-EXIT.
            EXIT.
      *
      ***----------------------------------------------------------***
      ***  THIS PARAGRAPH GETS EACH MESSAGE OFF OF THE INPUT QUEUE ***
      ***  AND DETERMINES IF THE PUBLISHED DATA IS PERSON OR       ***
      ***  CROSS REFERENCE DATA.                                   ***
      ***----------------------------------------------------------***
       1100-MQGET-MESSAGES.

      ***----------------------------------------------------------***
      ***  CALCULATE THE GET MESSAGE OPTIONS.                      ***
      ***----------------------------------------------------------***
           COMPUTE MQGMO-OPTIONS      =  MQGMO-SYNCPOINT +
                                         MQGMO-CONVERT      +
                                         MQGMO-ACCEPT-TRUNCATED-MSG +
                                         MQGMO-WAIT
           END-COMPUTE.

      ***----------------------------------------------------------***
      ***  WAIT 10 SECONDS FOR ANY MORE MESSAGES ON THE QUEUE.     ***
      ***----------------------------------------------------------***
           MOVE  01000                    TO MQGMO-WAITINTERVAL.

      ***----------------------------------------------------------***
      ***  WE DON'T CARE ABOUT A SPECIFIC MESSAGE, JUST GET THEM   ***
      ***  ALL.                                                    ***
      ***----------------------------------------------------------***
           MOVE ZERO                      TO MQMD-CODEDCHARSETID.
           MOVE MQMI-NONE                 TO MQMD-MSGID.
           MOVE MQCI-NONE                 TO MQMD-CORRELID.
           MOVE LENGTH OF WS-REPLY-BUFFER TO WMQ-BUFFLEN.
      *
      ***----------------------------------------------------------***
      ***  ISSUE THE MQGET CALL.                                   ***
      ***----------------------------------------------------------***
           CALL 'MQGET' USING WMQ-HCONN,
                              WMQ-HOBJ-SUBSCRIBER,
                              MQMD,
                              MQGMO,
                              WMQ-BUFFLEN,
                              WS-REPLY-BUFFER,
                              WMQ-DATALEN,
                              WMQ-COMPCODE,
                              WMQ-REASON.
      ***----------------------------------------------------------***
      ***  CHECK THE COMPLETION AND REASON CODES FOR SUCCESSFUL OR ***
      ***  NO MESSAGES LEFT ON THE INPUT QUEUE.                    ***
      ***----------------------------------------------------------***
           EVALUATE TRUE
               WHEN (WMQ-COMPCODE       = MQCC-OK AND
                     WMQ-REASON         = MQRC-NONE)
                    SET MESSAGE-RECEIVED-OK TO TRUE
                    ADD 1 TO WS-GETS

               WHEN (WMQ-COMPCODE       = MQCC-FAILED AND
                     WMQ-REASON         = MQRC-NO-MSG-AVAILABLE)

                    SET NO-MESSAGE-RECEIVED TO TRUE

               WHEN OTHER
                    MOVE 'UNEXPECTED COMPCODE ON MQGET OF SUBQ'
                                                 TO ABEND-MSG
                    DISPLAY 'ABEND-MSG:' ABEND-MSG
                    DISPLAY 'WMQ-COMPCODE:' WMQ-COMPCODE
                    DISPLAY 'WMQ-REASON  :' WMQ-REASON
                    DIVIDE 0 INTO BLOW-UP
           END-EVALUATE.
      *
      ***----------------------------------------------------------***
      ***  IF A MESSAGE WAS RETRIEVED OKAY, PERFORM A PARAGRAPH TO ***
      ***  PROCESS IT.                                             ***
      ***----------------------------------------------------------***
           IF  MESSAGE-RECEIVED-OK
               PERFORM 1150-BREAK-APART-MESSAGE
                  THRU 1150-EXIT
           END-IF.

       1100-EXIT.
            EXIT.
      *
       1150-BREAK-APART-MESSAGE.
      ***----------------------------------------------------------***
      ***  IF A MESSAGE WAS RETRIEVED OKAY, UNSTRING IT INTO BOTH  ***
      ***  THE PERSON AND CROSS REFERENCE LAYOUTS.  THEN, LOOK AT  ***
      ***  YYYY HEADER INFORMATION TO DETERMINE WHICH TYPE OF      ***
      ***  PUBLISHED DATA IT IS.                                   ***
      ***----------------------------------------------------------***

                ADD +1 TO WS-TOTAL-RECORDS.

           UNSTRING WS-REPLY-BUFFER
               INTO WMQ2-PUBLISHING-HEADER
                    WMQ2-XXSB-HEADER-LAYOUT
                    WMQ2-YYYY-HEADER-LAYOUT
                    WMQ2-PERS-PUBLISHED-DATA
                 ON OVERFLOW CONTINUE
           END-UNSTRING.

           UNSTRING WS-REPLY-BUFFER
               INTO WMQ2-PUBLISHING-HEADER
                    WMQ2-XXSB-HEADER-LAYOUT
                    WMQ2-YYYY-HEADER-LAYOUT
                    WMQ2-XREF-PUBLISHED-DATA
                 ON OVERFLOW CONTINUE
           END-UNSTRING.

           IF WMQ2-TABLE-IS-PERSON
                   ADD +1 TO WS-PROCESSED-RECORDS
                   PERFORM 1200-PROCESS-PERSON-DATA
                      THRU 1200-EXIT
           END-IF.

           IF WMQ2-TABLE-IS-XREF
                   PERFORM 1250-PROCESS-XREF-DATA
                      THRU 1250-EXIT
           END-IF.

      ***----------------------------------------------------------***
      ***  COMMIT THE MESSAGES EVERY 5000 OR SO.                   ***
      ***----------------------------------------------------------***
           ADD +1 TO WS-GETS-COMMIT.

           IF  WS-GETS-COMMIT  > WS-GETS-COMMIT-LIMIT
               PERFORM 1300-COMMIT-MESSAGES
                  THRU 1300-EXIT
               MOVE +0 TO WS-GETS-COMMIT
           END-IF.

       1150-EXIT.
            EXIT.

       1200-PROCESS-PERSON-DATA.
      ***----------------------------------------------------------***
      ***  ADD LOGIC                                               ***
      ***----------------------------------------------------------***


       1200-EXIT.
            EXIT.

      *

       1250-PROCESS-XREF-DATA.

      ***----------------------------------------------------------***
      ***  COMBINE LOGIC  (ADD)                                    ***
      ***----------------------------------------------------------***

       1250-EXIT.
            EXIT.

       1300-COMMIT-MESSAGES.

           CALL 'MQCMIT' USING WMQ-HCONN,
                               WMQ-COMPCODE,
                               WMQ-REASON.
           EVALUATE TRUE
               WHEN (WMQ-COMPCODE       = MQCC-OK AND
                     WMQ-REASON         = MQRC-NONE)
                    CONTINUE

               WHEN OTHER
                    MOVE 'UNEXPECTED COMPCODE ON MQCMIT CALL'
                                                 TO ABEND-MSG
                    DISPLAY 'ABEND-MSG:' ABEND-MSG
                    DISPLAY 'WMQ-COMPCODE:' WMQ-COMPCODE
                    DISPLAY 'WMQ-REASON  :' WMQ-REASON
                    DIVIDE 0 INTO BLOW-UP
           END-EVALUATE.
       1300-EXIT.
            EXIT.
      ***----------------------------------------------------------***
      ***  END OF PROGRAM YYYYT000                                 ***
      ***----------------------------------------------------------***
```

#### ↳ Re: Accessing MQ Series queue from MF Cobol on Solaris Client

- **From:** mkbobba@yahoo.com (Bob)
- **Date:** 2004-02-11T06:22:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64713ce9.0402110622.555b8ff7@posting.google.com>`
- **References:** `<64713ce9.0402100924.495d4bea@posting.google.com>`

```
We even tried using Call '_mqconn' as suggested by some earlier poster
with out much help. Any ideas to make this program working.

Thans much!.

Bob
```

##### ↳ ↳ Re: Accessing MQ Series queue from MF Cobol on Solaris Client

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-02-14T16:43:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C8FBDB.16432914022004@corp.supernews.com>`
- **References:** `<64713ce9.0402100924.495d4bea@posting.google.com> <64713ce9.0402110622.555b8ff7@posting.google.com>`

```
In article <64713ce9.0402110622.555b8ff7@posting.google.com>,
 mkbobba@yahoo.com (Bob) wrote:

> We even tried using Call '_mqconn' as suggested by some earlier poster
> with out much help. Any ideas to make this program working.
…[3 more quoted lines elided]…
> Bob

Have you checked you path?
```

##### ↳ ↳ Re: Accessing MQ Series queue from MF Cobol on Solaris Client

- **From:** Wiggy <wignomore@nospam.btopenworld.com>
- **Date:** 2004-02-15T10:27:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c0nhj9$jjt$1@hercules.btinternet.com>`
- **In-Reply-To:** `<64713ce9.0402110622.555b8ff7@posting.google.com>`
- **References:** `<64713ce9.0402100924.495d4bea@posting.google.com> <64713ce9.0402110622.555b8ff7@posting.google.com>`

```
Bob wrote:
> We even tried using Call '_mqconn' as suggested by some earlier poster
> with out much help. Any ideas to make this program working.

Hi Bob,

Not sure if this helps, but I took this from the IBM Application 
Programming Guide. Note the COBCPY setting and the link command-line -- 
I suspect that you've not pulled in all the MQ libraries?

Precompiled COBOL programs are supplied in the /opt/mqm/samp/bin 
directory. Use the Micro Focus compiler from the directory /opt/bin to 
build a sample from source code.

To compile, for example, the sample program amq0put0:

    1. Ensure that the environment is set:

   export COBDIR=/opt/lib/cobol
   export PATH=/opt/bin:$PATH
   export LD_LIBRARY_PATH=$COBDIR/coblib:$LD_LIBRARY_PATH

       Note:
           The above assumes that COBOL is installed in the default 
directories.

    2. Define the location of the copybooks which declare the MQI 
structures:

   export COBCPY="/opt/mqm/inc"

    3. Link your program with one of the following libraries when 
building the application:
       Library file 	Program/exit type
       libmqmcb.so 	Server for COBOL
       libmqicb.so 	Client for COBOL
    4. Compile the program:

   cob -vxP amq0put0.cbl -lmqmcb -lmqm -lmqmcs -lmqmzse

Wiggy.
```

##### ↳ ↳ Re: Accessing MQ Series queue from MF Cobol on Solaris Client

- **From:** wignomore@btopenworld.com (Wiggy)
- **Date:** 2004-02-15T02:33:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9badd74.0402150233.31fe4e89@posting.google.com>`
- **References:** `<64713ce9.0402100924.495d4bea@posting.google.com> <64713ce9.0402110622.555b8ff7@posting.google.com>`

```
mkbobba@yahoo.com (Bob) wrote in message news:<64713ce9.0402110622.555b8ff7@posting.google.com>...
> We even tried using Call '_mqconn' as suggested by some earlier poster
> with out much help. Any ideas to make this program working.
…[3 more quoted lines elided]…
> Bob

Hi Bob,

Not sure if this helps, but I took this from the IBM Application
Programming Guide (http://publibfp.boulder.ibm.com/epubs/html/csqzal09/csqzal09tfrm.htm
, chapter 30). Note the COBCPY setting and the link command-line -- I
suspect that you've not pulled in all the MQ libraries?

Precompiled COBOL programs are supplied in the /opt/mqm/samp/bin
directory. Use the Micro Focus compiler from the directory /opt/bin to
build a sample from source code.

To compile, for example, the sample program amq0put0:

   1. Ensure that the environment is set:

  export COBDIR=/opt/lib/cobol
  export PATH=/opt/bin:$PATH
  export LD_LIBRARY_PATH=$COBDIR/coblib:$LD_LIBRARY_PATH

      Note:
          The above assumes that COBOL is installed in the default
directories.

   2. Define the location of the copybooks which declare the MQI
structures:

  export COBCPY="/opt/mqm/inc"

   3. Link your program with one of the following libraries when
building the application:
      Library file     Program/exit type
      libmqmcb.so     Server for COBOL
      libmqicb.so     Client for COBOL
   4. Compile the program:

  cob -vxP amq0put0.cbl -lmqmcb -lmqm -lmqmcs -lmqmzse

Wiggy.
```

###### ↳ ↳ ↳ Re: Accessing MQ Series queue from MF Cobol on Solaris Client

- **From:** mkbobba@yahoo.com (Bob)
- **Date:** 2004-02-17T10:55:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64713ce9.0402171055.2e6cda63@posting.google.com>`
- **References:** `<64713ce9.0402100924.495d4bea@posting.google.com> <64713ce9.0402110622.555b8ff7@posting.google.com> <f9badd74.0402150233.31fe4e89@posting.google.com>`

```
Thank you all for your responses. I have COBCPY in my path defined as
"/opt/mqm/inc" and all the other PATH variables are also set properly.

But the reason form distress seems to be the following reason:
I was told that the Sun Solaris version 5.6 doesn't support dynamic
linking and this is the reason why I am not able to link these
libraries.

Thanks again.

Bob
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
