[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Subroutines

_11 messages · 7 participants · 2001-02_

---

### Re: Subroutines

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-02-07T09:26:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95rlp2$5nr$1@news.igs.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com>`

```

"Stefan Meyer" <meyerst@my-deja.com> wrote in message
news:95r0op$tbl$1@nnrp1.deja.com...
> Donald,
> I'll comment inline...
…[8 more quoted lines elided]…
>
<SNIP REST>

I am using Fujitsu, so the code might vary a bit, but here is a sample OOP
subroutine.  I just typed this in as a sample, but it should show you the
basics.  I am going to presume that you know how to do the same sorts of
things with subroutines, and I am sure that someone here can show you yhe
differences for MF.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. "USER-CODE".
       AUTHOR. D. L. Tees.
       SECURITY.
           Copyright (C), 2001, Donald L Tees.
      * Notes:
      * SAMPLE "calling" PROGRAM FOR OOP.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       REPOSITORY.
           CLASS DISP2005.
       SOURCE-COMPUTER. IBM-PC.
       OBJECT-COMPUTER. IBM-PC.
       SPECIAL-NAMES.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       77 OBJECT-INSTANCE-ONE      USAGE OBJECT REFERENCE DISP2005.
       77 OBJECT-INSTANCE-TWO      USAGE OBJECT REFERENCE DISP2005.
       PROCEDURE DIVISION.
       MAIN-LINE.
      * FIRST, YOU HAVE TO CREATE THE OBJECTS
           INVOKE DISP2005 "NEW" RETURNING OBJECT-INSTANCE-ONE.
           INVOKE DISP2005 "NEW" RETURNING OBJECT-INSTANCE-TWO.
      * USING THE INSTANCE IS THE SAME AS A SUBROUTINE
           INVOKE OBJECT-INSTANCE-ONE "HELLO-WORLD".
           INVOKE OBJECT-INSTANCE-ONE "HELLO-SOMEONE"
                USING "DONALD".
      * HOWEVER, YOU CAN ALSO SET PROPERTIES
      * THIS CALL WILL LOOK THE SAME AS THE "hello-someone" using
           MOVE "DONALD" TO PERSON-NAME OF OBJECT-INSTANCE-TWO.
           INVOKE OBJECT-INSTANCE-TWO "HELLO-WORLD".
      * AFTER USING THEM, YOU HAVE TO DESTROY THEM
           SET OBJECT-INSTANCE-ONE TO NULL.
           SET OBJECT-INSTANCE-TWO TO NULL.
           GOBACK.


THIS IS THE OBJECT PROGRAM.

        CLASS-ID. DISP2005 INHERITS FJBASE.
        ENVIRONMENT DIVISION.
        CONFIGURATION SECTION.
        REPOSITORY.
                CLASS FJBASE.
        OBJECT.
        ENVIRONMENT DIVISION.
        INPUT-OUTPUT SECTION.
 FILE-CONTROL.
        DATA DIVISION.
 FILE SECTION.
        WORKING-STORAGE SECTION.
       * DATA COMMON TO ALL METHODS
        01 PERSON-NAME          PICTURE X(10) VALUE
                                SPACE PROPERTY.
        PROCEDURE DIVISION.
       * THE METHODS GO HERE.
*********************************************************
        METHOD-ID. HELLO-WORLD.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        LINKAGE SECTION.
        PROCEDURE DIVISION.
        MAINLINE.
                IF PERSON-NAME IS EQUAL TO SPACE
                        DISPLAY "HELLO WORLD"
                ELSE
                        DISPLAY "HELLO " PERSON-NAME.
                EXIT METHOD.
        END METHOD HELLO-WORLD.

*********************************************************
        METHOD-ID. HELLO-SOMEONE.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
        LINKAGE SECTION.
        77 NAME-INPUT           PICTURE X(10).
        PROCEDURE DIVISION USING NAME-INPUT.
        MAINLINE.
                MOVE NAME-INPUT TO PERSON-NAME.
                INVOKE SELF "HELLO-WORLD".
                EXIT METHOD.
        END METHOD HELLO-SOMEONE.
        END OBJECT.
        END CLASS DISP2005.

That should give you the basic structure.  I have some actual code that is
in beta test right now.  Here is the "file object" code for one of the
files. Notice that the file stuff is all at the top so is global to all
methods.

******* File level objects
*******************************************************************
       CLASS-ID. DISP2010 INHERITS FJBASE.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       REPOSITORY.
           CLASS DISP2005
           CLASS FJBASE.
       OBJECT.
       ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
           SELECT PRODUCT-FILE ASSIGN TO DPROD-ID
               ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               LOCK MODE IS EXCLUSIVE
               FILE STATUS IS DPROD-STATUS
               RECORD KEY IS DPROD-NUMBER.
           SELECT CONTROL-FILE ASSIGN TO CONTROL-ID
               ORGANIZATION IS RELATIVE
               LOCK MODE IS EXCLUSIVE
               ACCESS IS RANDOM
               RELATIVE KEY IS CONTROL-KEY
               FILE STATUS IS CONTROL-STATUS.
           SELECT CUSTOMER-FILE ASSIGN TO DCUST-ID
               ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               LOCK MODE IS EXCLUSIVE
               FILE STATUS IS DCUST-STATUS
               RECORD KEY IS DCUST-KEY
               ALTERNATE RECORD KEY IS DCUST-ALPHA
                   WITH DUPLICATES.
           SELECT TRUCK-TYPE-FILE ASSIGN TO TTYPE-ID
               ORGANIZATION IS RELATIVE
               FILE STATUS TTYPE-STATUS
               RELATIVE KEY IS TTYPE-KEY
               LOCK MODE EXCLUSIVE
               ACCESS IS DYNAMIC.
           SELECT OLD-TRUCK-TYPE-FILE ASSIGN TO OLD-TTYPE-ID
               ORGANIZATION IS RELATIVE
               FILE STATUS OLD-TTYPE-STATUS
               RELATIVE KEY IS OLD-TTYPE-KEY
               LOCK MODE EXCLUSIVE
               ACCESS IS DYNAMIC.
           SELECT DTRK-FILE ASSIGN TO DTRK-IDENT
               ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               LOCK MODE IS EXCLUSIVE
               FILE STATUS IS DTRK-STATUS
               RECORD KEY IS DTRK-KEY
               ALTERNATE KEY IS
                   DTRK-SHOW, DTRK-DATE
                   DTRK-IN, DTRK-KEY
               ALTERNATE RECORD KEY IS DTRK-DISPATCH-KEY
                   WITH DUPLICATES.
           SELECT CARD-FILE ASSIGN TO CARD-IDENT
              ORGANIZATION IS INDEXED
               ACCESS MODE IS DYNAMIC
               FILE STATUS IS CARD-STATUS
               RECORD KEY IS CARD-NUMBER OF CARD-RECORD
               ALTERNATE RECORD KEY IS CARD-TRUCK WITH DUPLICATES
               ALTERNATE RECORD KEY IS CARD-CUSTOMER WITH DUPLICATES.
           SELECT TICKET-FILE ASSIGN TO TICKET-IDENT
               ORGANIZATION IS INDEXED
               ACCESS IS DYNAMIC
               FILE STATUS IS TICKET-STATUS
               RECORD KEY IS T-TICKET-NUMBER.
       DATA DIVISION.
 FILE SECTION.
       FD PRODUCT-FILE.
       01 PRODUCT-RECORD.
           COPY "\LIBRARY\COPIES\PRODUCT.COBOL".
       FD CONTROL-FILE.
       01 CONTROL-RECORD.
           COPY "\LIBRARY\COPIES\CONTROL.COBOL".
       FD CUSTOMER-FILE.
       01 CUSTOMER-RECORD.
           COPY "\LIBRARY\COPIES\CUSTOMER.COBOL".
       FD TRUCK-TYPE-FILE.
       01 TRUCK-TYPE-RECORD.
           COPY "\LIBRARY\COPIES\TTYPE.COBOL".
       FD OLD-TRUCK-TYPE-FILE.
       01 OLD-TRUCK-TYPE-RECORD.
           02 TRUCK-TYPE-ENTRY     OCCURS 20 TIMES.
              04 TRUCK-TYPE-DESC PICTURE X(5).
       FD DTRK-FILE.
       01 TRUCK-RECORD.
           COPY "\LIBRARY\COPIES\TRUCK.COBOL".
       FD CARD-FILE.
       01 CARD-RECORD.
           COPY "\LIBRARY\COPIES\CARD.COBOL".
       FD TICKET-FILE.
       01 TICKET-RECORD.
           COPY "\LIBRARY\COPIES\TICKET.COBOL".
       WORKING-STORAGE SECTION.
       77 PROGRAM-NAME-ABORT   PICTURE X(8) VALUE SPACE PROPERTY.
       77 VERSION-A                            PICTURE 9 VALUE ZERO
PROPERTY.
       77 VERSION-B                            PICTURE 99 VALUE ZERO
PROPERTY.
       77 SOURCE-MODULE               PICTURE X(45) VALUE SPACE PROPERTY.
       77 DPROD-STATUS                   PICTURE XX VALUE SPACE.
       77 DPROD-ID                             PICTURE X(80) VALUE SPACE.
       77 CONTROL-STATUS           PICTURE XX VALUE SPACE.
       77 CONTROL-KEY              PICTURE 9(5) VALUE ZERO.
       77 CONTROL-ID               PICTURE X(80) VALUE SPACE.
       77 DCUST-STATUS           PICTURE XX VALUE SPACE.
       77 DCUST-ID                 PICTURE X(80) VALUE SPACE.
       77 TTYPE-STATUS           PICTURE XX VALUE SPACE.
       77 TTYPE-ID               PICTURE X(80) VALUE SPACE.
       77 TTYPE-KEY                PICTURE 99.
       77 OLD-TTYPE-STATUS         PICTURE XX VALUE SPACE.
       77 OLD-TTYPE-ID             PICTURE X(80) VALUE SPACE.
       77 OLD-TTYPE-KEY            PICTURE 99.
       77 DTRK-STATUS           PICTURE XX VALUE SPACE.
       77 DTRK-IDENT               PICTURE X(80) VALUE SPACE.
       77 CARD-IDENT               PICTURE X(80) VALUE SPACE.
       77 CARD-STATUS           PICTURE XX VALUE SPACE.
       77 WINDOW-NAME              PICTURE X(8) VALUE SPACE.
       77 TICKET-STATUS           PICTURE XX VALUE SPACE.
       77 TICKET-IDENT             PICTURE X(80) VALUE SPACE.
       01 WINDOW-RECORD-DATA.
           COPY "\LIBRARY\COPIES\WINDOW.COBOL".
           COPY "\LIBRARY\COPIES\COBF-INF.COBOL".
       01 MISCSE02-PARAMETERS.
           COPY "\LIBRARY\COPIES\MISCSE02.COBOL".
       PROCEDURE DIVISION.
*******************************************************************
       METHOD-ID. ABORT-METHOD.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 BASE-OBJECT          USAGE OBJECT REFERENCE DISP2005.
       LINKAGE SECTION.
       PROCEDURE DIVISION.
       MAINLINE.
           INVOKE DISP2005 "NEW" RETURNING BASE-OBJECT.
           MOVE "DISPATCH" TO THIS-SYSTEM-NAME OF BASE-OBJECT.
           MOVE PROGRAM-NAME-ABORT TO PROGRAM-NAME OF BASE-OBJECT.
           MOVE VERSION-A OF SELF TO VERSION-A OF BASE-OBJECT.
           MOVE VERSION-B OF SELF TO VERSION-B OF BASE-OBJECT.
           MOVE SOURCE-MODULE OF SELF TO SOURCE-MODULE OF BASE-OBJECT.
           INVOKE BASE-OBJECT "ABORT-METHOD".
           SET BASE-OBJECT TO NULL.
           EXIT METHOD.
       END METHOD ABORT-METHOD.
*******************************************************************
           COPY "\LIBRARY\COPIES\PRODFILE.CBL".
           COPY "\LIBRARY\COPIES\CONTFILE.CBL".
           COPY "\LIBRARY\COPIES\CUSTFILE.CBL".
           COPY "\LIBRARY\COPIES\TTYPFILE.CBL".
           COPY "\LIBRARY\COPIES\TRKFILE.CBL".
           COPY "\LIBRARY\COPIES\CARDFILE.CBL".
           COPY "\LIBRARY\COPIES\TICKET.CBL".
*******************************************************************
       END OBJECT.
       END CLASS DISP2010.


And one of the copy libraries for one of the files.

       METHOD-ID. OPEN-LOCK-DPROD.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 BASE-OBJECT              USAGE OBJECT REFERENCE DISP2005.
       01 SCREEN-OBJECT            USAGE OBJECT REFERENCE DISP2005.
       01 LOCAL-KEYSTROKE          PICTURE S999.
       01 LOCK-TIME                PICTURE 99.
       01 FILE-ID-AREA             PICTURE X(80).
       01 BADFILE-AREA             PICTURE X(80).
       01 MESSAGE-AREA.
           02 DISPLAY-PART         PICTURE X(40).
           02 FILLER               PICTURE X(512).
       LINKAGE SECTION.
       PROCEDURE DIVISION.
       DECLARATIVES.
       TROUBLE SECTION.
           USE AFTER ERROR PROCEDURE ON PRODUCT-FILE.
       CHECK-STATUS.
           CONTINUE.
       END DECLARATIVES.
       MAINLINE.
           IF DPROD-ID IS EQUAL TO SPACE
               INVOKE DISP2005 "NEW" RETURNING BASE-OBJECT
               MOVE "DISPATCH" TO THIS-SYSTEM-NAME OF BASE-OBJECT
               MOVE "G" TO PARAMETER-TYPE OF BASE-OBJECT
               MOVE "DPRODID" TO PARAMETER-NAME OF BASE-OBJECT
               MOVE SYSTEM-PARAMETER OF BASE-OBJECT TO DPROD-ID
               SET BASE-OBJECT TO NULL.
           MOVE ZERO TO LOCK-TIME.
           MOVE "99" TO DPROD-STATUS.
           PERFORM OPEN-THE-FILE UNTIL
               DPROD-STATUS IS EQUAL TO "00".
           IF SCREEN-OBJECT IS NOT EQUAL TO NULL
               INVOKE SCREEN-OBJECT "CLOSE-ERROR-MESSAGE"
               SET SCREEN-OBJECT TO NULL.
           EXIT METHOD.

       OPEN-THE-FILE.
           OPEN I-O PRODUCT-FILE.
           IF DPROD-STATUS IS EQUAL TO "35"
               PERFORM CREATE-NEW-FILE.
           IF DPROD-STATUS IS EQUAL TO "39"
               PERFORM ATTEMPT-TO-RECOVER
           ELSE
           IF DPROD-STATUS IS EQUAL TO "93"
               PERFORM SHOW-THE-LOCK
           ELSE
           IF DPROD-STATUS IS EQUAL TO "41"
               DISPLAY "PRODUCT status --> " DPROD-STATUS
                       " (Open attempt on open file)"
               INVOKE SELF "ABORT-METHOD"
           ELSE
           IF DPROD-STATUS IS NOT EQUAL TO "00"
               DISPLAY "Open PRODUCT status --> " DPROD-STATUS
               INVOKE SELF "ABORT-METHOD".

       SHOW-THE-LOCK.
           IF LOCK-TIME IS EQUAL TO ZERO
               INVOKE DISP2005 "NEW" RETURNING SCREEN-OBJECT
               MOVE "DPRODID" TO LOCK-CODE OF SCREEN-OBJECT
               MOVE "Product file" TO LOCK-NAME OF SCREEN-OBJECT
               MOVE DPROD-STATUS TO LOCK-STATUS OF SCREEN-OBJECT
               INVOKE SCREEN-OBJECT "SHOW-LOCK"
               ADD 1 TO LOCK-TIME
           ELSE
           IF LOCK-TIME IS LESS THAN 60
               MOVE DPROD-STATUS TO LOCK-STATUS OF SCREEN-OBJECT
               INVOKE SCREEN-OBJECT "SHOW-LOCK"
               ADD 1 TO LOCK-TIME
           ELSE
               DISPLAY "Product file lock time exceeded"
               INVOKE SELF "ABORT-METHOD".

       ATTEMPT-TO-RECOVER.
           INVOKE DISP2005 "NEW" RETURNING SCREEN-OBJECT.
           MOVE "Product file" TO LOCK-NAME OF SCREEN-OBJECT.
           MOVE DPROD-STATUS TO LOCK-STATUS OF SCREEN-OBJECT.
           INVOKE SCREEN-OBJECT "ASK-RECOVER".
           MOVE SCREEN-KEYCODE OF SCREEN-OBJECT
               TO LOCAL-KEYSTROKE.
           IF LOCAL-KEYSTROKE IS EQUAL TO 500
               PERFORM ATTEMPT-TO-RECOVER-TWO
           ELSE
           IF LOCAL-KEYSTROKE IS EQUAL TO 501
               SET SCREEN-OBJECT TO NULL
               PERFORM CREATE-NEW-FILE
           ELSE
               SET SCREEN-OBJECT TO NULL
               INVOKE SELF "ABORT-METHOD".

       ATTEMPT-TO-RECOVER-TWO.
           MOVE LOW-VALUES TO COBF-INF.
           MOVE "C:\WILLMACK\PRODUCT.ERROR" TO COBF-INPUT-FILENAME.
           DISPLAY "Deleting old error file C:\WILLMACK\PRODUCT.ERROR".
           CALL "COB_FILE_DELETE" USING BY REFERENCE COBF-INF.
           MOVE "C:\WILLMACK\PRODUCT.ERROR" TO COBF-INPUT-FILENAME.
           MOVE "C:\WILLMACK\PRODUCT.ERROR" TO BADFILE-AREA.
           MOVE DPROD-ID TO FILE-ID-AREA.
           DISPLAY "File id " FILE-ID-AREA.
           DISPLAY "Error file " BADFILE-AREA.
           DISPLAY "Starting recover".
           CALL "CFURCOV" USING BY REFERENCE FILE-ID-AREA
                                BY REFERENCE BADFILE-AREA
                                BY REFERENCE MESSAGE-AREA.
           INSPECT MESSAGE-AREA REPLACING ALL X'00' BY " ".
           DISPLAY DISPLAY-PART.
           DISPLAY "Doing reorganize".
           MOVE LOW-VALUES TO COBF-INF.
           MOVE "C:\WILLMACK\PRODUCT.ERROR1" TO COBF-INPUT-FILENAME.
           DISPLAY "Deleting old error file C:\WILLMACK\PRODUCT.ERROR1".
           CALL "COB_FILE_DELETE" USING BY REFERENCE COBF-INF.
           MOVE LOW-VALUES TO COBF-INF.
           MOVE DPROD-ID TO COBF-INPUT-FILENAME.
           MOVE "C:\WILLMACK\PRODUCT.ERROR1" TO COBF-OUTPUT-FILENAME.
           CALL "COB_FILE_REORGANIZE" USING BY REFERENCE COBF-INF.
           INSPECT MESSAGE-AREA REPLACING ALL X'00' BY " ".
           DISPLAY DISPLAY-PART.
           SET SCREEN-OBJECT TO NULL.

       CREATE-NEW-FILE.
           OPEN OUTPUT PRODUCT-FILE.
           CLOSE PRODUCT-FILE.
           OPEN I-O PRODUCT-FILE.

       END METHOD OPEN-LOCK-DPROD.
*******************************************************************
       METHOD-ID. CLOSE-DPROD.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       LINKAGE SECTION.
       PROCEDURE DIVISION.
       MAINLINE.
           CLOSE PRODUCT-FILE.
           EXIT METHOD.
       END METHOD CLOSE-DPROD.
*******************************************************************
       METHOD-ID. PRODUCT-RECORD-UPDATE.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 BASE-OBJECT              USAGE OBJECT REFERENCE DISP2005.
       LINKAGE SECTION.
       77 REQUEST-TYPE             PICTURE X.
       01 PRODUCT-RECORD-IN.
           COPY "\LIBRARY\COPIES\PRODUCT.COBOL".
       77 ERROR-CODE               PICTURE 9.
       77 READ-WRITE-FLAG          PICTURE X.
       PROCEDURE DIVISION USING REQUEST-TYPE
                             PRODUCT-RECORD-IN
                             ERROR-CODE
                             READ-WRITE-FLAG.
       MAINLINE.
           IF DPROD-ID IS EQUAL TO SPACE
               INVOKE DISP2005 "NEW" RETURNING BASE-OBJECT
               MOVE "DISPATCH" TO THIS-SYSTEM-NAME OF BASE-OBJECT
               MOVE "G" TO PARAMETER-TYPE OF BASE-OBJECT
               MOVE "DPRODID" TO PARAMETER-NAME OF BASE-OBJECT
               MOVE SYSTEM-PARAMETER OF BASE-OBJECT TO DPROD-ID
               SET BASE-OBJECT TO NULL.
           MOVE ZERO TO ERROR-CODE.
           MOVE "Y" TO READ-WRITE-FLAG.
           IF (REQUEST-TYPE IS NOT EQUAL TO "1"
               AND
               REQUEST-TYPE IS NOT EQUAL TO "2"
               AND
               REQUEST-TYPE IS NOT EQUAL TO "4"
               AND
               REQUEST-TYPE IS NOT EQUAL TO "3")
                   INVOKE SELF "OPEN-LOCK-DPROD".
           IF REQUEST-TYPE = "R" PERFORM DPROD-READ
           ELSE
           IF REQUEST-TYPE = "4" PERFORM DPROD-READ
           ELSE
           IF REQUEST-TYPE = "D" PERFORM DPROD-DELETE
           ELSE
           IF REQUEST-TYPE = "U" PERFORM DPROD-REWRITE
           ELSE
           IF REQUEST-TYPE = "X" PERFORM DPROD-X-DESC
           ELSE
           IF REQUEST-TYPE = "Y" PERFORM DPROD-Y-TONS-ORDER
           ELSE
           IF REQUEST-TYPE = "Z" PERFORM DPROD-Z-TONS-ORDER
           ELSE
           IF REQUEST-TYPE = "L" PERFORM DPROD-OVER-UNDER-LOADS
           ELSE
           IF REQUEST-TYPE = "C" PERFORM DPROD-CHANGE
           ELSE
           IF REQUEST-TYPE = "V" PERFORM DPROD-REVERSE-CHANGE
           ELSE
           IF REQUEST-TYPE = "N" PERFORM DPROD-CREATE-NEW
           ELSE
           IF REQUEST-TYPE = "S" PERFORM DPROD-SET-ZERO
           ELSE
           IF REQUEST-TYPE = "3" PERFORM DPROD-SET-ZERO
           ELSE
           IF REQUEST-TYPE = "1" PERFORM DPROD-START-READ1
           ELSE
           IF REQUEST-TYPE = "2" PERFORM DPROD-READ-SEQUENTIAL
           ELSE
               DISPLAY "PRODDATA --> Illegal call"
               INVOKE SELF "ABORT-METHOD".
           MOVE PRODUCT-RECORD TO PRODUCT-RECORD-IN.
           IF (REQUEST-TYPE IS NOT EQUAL TO "1"
               AND
               REQUEST-TYPE IS NOT EQUAL TO "2"
               AND
               REQUEST-TYPE IS NOT EQUAL TO "4"
               AND
               REQUEST-TYPE IS NOT EQUAL TO "3")
                   INVOKE SELF "CLOSE-DPROD".
           EXIT METHOD.

       DPROD-READ.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           READ PRODUCT-FILE INVALID KEY
              MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG IS EQUAL TO "N"
               MOVE 3 TO ERROR-CODE.

       DPROD-DELETE.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           READ PRODUCT-FILE INVALID KEY
               MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "Y"
               PERFORM DPROD-DELETE-CONTINUE
           ELSE
               MOVE 5 TO ERROR-CODE.

       DPROD-DELETE-CONTINUE.
           DELETE PRODUCT-FILE RECORD INVALID KEY
               MOVE 5 TO ERROR-CODE.

       DPROD-REWRITE.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "N"
               MOVE 6 TO ERROR-CODE.

       DPROD-X-DESC.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           READ PRODUCT-FILE INVALID KEY
              MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "Y"
              PERFORM DPROD-X-DESC-CONTINUE
           ELSE
               MOVE 3 TO ERROR-CODE.

       DPROD-X-DESC-CONTINUE.
           MOVE DPROD-DESC OF PRODUCT-RECORD-IN
               TO DPROD-DESC OF PRODUCT-RECORD.
           MOVE DPROD-PLANT-NUMBER OF PRODUCT-RECORD-IN
               TO DPROD-PLANT-NUMBER OF PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE 6 TO ERROR-CODE.

       DPROD-Y-TONS-ORDER.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           MOVE "Y" TO READ-WRITE-FLAG.
           READ PRODUCT-FILE INVALID KEY
               MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "Y"
              PERFORM DPROD-Y-TONS-ORDER-CONTINUE
           ELSE
               MOVE 6 TO ERROR-CODE.

       DPROD-Y-TONS-ORDER-CONTINUE.
           ADD DPROD-TONS-ORDER OF PRODUCT-RECORD-IN
               TO DPROD-TONS-ORDER OF PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE 6 TO ERROR-CODE.

       DPROD-Z-TONS-ORDER.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           READ PRODUCT-FILE INVALID KEY
              MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "Y"
              PERFORM DPROD-Z-TONS-ORDER-CONTINUE
           ELSE
               MOVE 3 TO ERROR-CODE.

       DPROD-Z-TONS-ORDER-CONTINUE.
           SUBTRACT DPROD-TONS-ORDER OF PRODUCT-RECORD-IN
               FROM DPROD-TONS-ORDER OF PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE 6 TO ERROR-CODE.

       DPROD-OVER-UNDER-LOADS.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           MOVE "Y" TO READ-WRITE-FLAG.
           READ PRODUCT-FILE INVALID KEY
              MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "Y"
              PERFORM DPROD-OVER-UNDER-LOADS-CONT
           ELSE
               MOVE 6 TO ERROR-CODE.

       DPROD-OVER-UNDER-LOADS-CONT.
           ADD DPROD-OVERLOADS OF PRODUCT-RECORD-IN
               TO DPROD-OVERLOADS OF PRODUCT-RECORD.
           ADD DPROD-UNDERLOADS OF PRODUCT-RECORD-IN
               TO DPROD-UNDERLOADS OF PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE 6 TO ERROR-CODE.

       DPROD-CHANGE.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           READ PRODUCT-FILE INVALID KEY
                MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "Y"
               PERFORM DPROD-CHANGE-CONTINUE
           ELSE
               MOVE 3 TO ERROR-CODE.

       DPROD-CHANGE-CONTINUE.
           IF DPROD-LOADS-TODAY OF PRODUCT-RECORD IS EQUAL TO ZERO
               ADD 1 TO DPROD-LOADS-TODAY OF PRODUCT-RECORD
               MOVE DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD-IN
                  TO DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD
           ELSE
               MULTIPLY DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD BY
                   DPROD-LOADS-TODAY OF PRODUCT-RECORD
                       GIVING DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD
               ADD DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD-IN
                   TO DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD
               ADD 1 TO DPROD-LOADS-TODAY OF PRODUCT-RECORD
               DIVIDE DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD
                 BY DPROD-LOADS-TODAY OF PRODUCT-RECORD
                 GIVING DPROD-AVE-LOAD-TIME OF PRODUCT-RECORD ROUNDED.
           ADD DPROD-UNDERLOADS OF PRODUCT-RECORD-IN
               TO DPROD-UNDERLOADS OF PRODUCT-RECORD.
           ADD DPROD-OVERLOADS OF PRODUCT-RECORD-IN
               TO DPROD-OVERLOADS OF PRODUCT-RECORD.
           ADD DPROD-TONS-FOB OF PRODUCT-RECORD-IN
               TO DPROD-TONS-FOB OF PRODUCT-RECORD.
           ADD DPROD-TONS-DELIVER OF PRODUCT-RECORD-IN
               TO DPROD-TONS-DELIVER OF PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE 6 TO ERROR-CODE.

       DPROD-REVERSE-CHANGE.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           READ PRODUCT-FILE INVALID KEY
               MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "Y"
               PERFORM DPROD-REVERSE-CHANGE-CONT
           ELSE
               MOVE 3 TO ERROR-CODE.

       DPROD-REVERSE-CHANGE-CONT.
           SUBTRACT 1 FROM DPROD-LOADS-TODAY OF PRODUCT-RECORD.
           SUBTRACT DPROD-TONS-FOB OF PRODUCT-RECORD-IN
               FROM DPROD-TONS-FOB OF PRODUCT-RECORD.
           SUBTRACT DPROD-TONS-DELIVER OF PRODUCT-RECORD-IN
               FROM DPROD-TONS-DELIVER OF PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE 6 TO ERROR-CODE.

       DPROD-CREATE-NEW.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           WRITE PRODUCT-RECORD INVALID KEY
               MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG = "N"
               MOVE 6 TO ERROR-CODE.

       DPROD-SET-ZERO.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           READ PRODUCT-FILE INVALID KEY
              MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG IS EQUAL TO "Y"
               PERFORM DPROD-SET-ZERO-CONTINUE.

       DPROD-SET-ZERO-CONTINUE.
           MOVE ALL "0" TO DPROD-DATA OF PRODUCT-RECORD.
           REWRITE PRODUCT-RECORD INVALID KEY
               MOVE 6 TO ERROR-CODE.

       DPROD-START-READ1.
           MOVE PRODUCT-RECORD-IN TO PRODUCT-RECORD.
           START PRODUCT-FILE
               KEY GREATER THAN DPROD-NUMBER OF PRODUCT-RECORD
                   INVALID KEY
                       MOVE 3 TO ERROR-CODE
                       MOVE "N" TO READ-WRITE-FLAG.
           IF READ-WRITE-FLAG IS EQUAL TO "Y"
               READ PRODUCT-FILE NEXT RECORD
                   AT END
                       MOVE 3 TO ERROR-CODE
                       MOVE "N" TO READ-WRITE-FLAG.

       DPROD-READ-SEQUENTIAL.
           READ PRODUCT-FILE NEXT RECORD
               AT END MOVE "N" TO READ-WRITE-FLAG.

       END METHOD PRODUCT-RECORD-UPDATE.
```

#### ↳ Re: Subroutines

- **From:** Stefan Meyer <meyerst@my-deja.com>
- **Date:** 2001-02-07T16:30:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95rt7u$kk3$1@nnrp1.deja.com>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net>`

```
  "donald tees" <donald@willmack.com> wrote:
>
> I am using Fujitsu, so the code might vary a bit, but here is a
sample OOP
> subroutine.  I just typed this in as a sample, but it should show you
the
> basics.  I am going to presume that you know how to do the same sorts
of
> things with subroutines, and I am sure that someone here can show you
yhe
> differences for MF.

Donald,

first of all: "Big Thank You" for spending your time and posting the
source.

I should have known that OOP is that easy in COBOL..."Damned".

That's the way I like programing/developping. Everything goes.

Well if I find the time I'll try to do more in OO-COBOL.

...and for my originated question: OO is the best answer.

Thanks everybody giving me some usefull hints. This NG is a great place
to find usefull COBOL information.

Bye - Stefan Meyer

To Donald: May I send you the code to take a look on it?


Sent via Deja.com
http://www.deja.com/
```

##### ↳ ↳ Re: Subroutines

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-02-07T14:29:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95s7bi$e9q$1@news.igs.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com>`

```
Sure.  No problem.  It may take a day ...

"Stefan Meyer" <meyerst@my-deja.com> wrote in message
news:95rt7u$kk3$1@nnrp1.deja.com...
>   "donald tees" <donald@willmack.com> wrote:
> >
…[32 more quoted lines elided]…
> http://www.deja.com/
```

##### ↳ ↳ Re: Subroutines

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2001-02-07T15:12:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95s9to$f0s$1@news.igs.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com>`

```
P.S. to that last.

"Stefan Meyer" <meyerst@my-deja.com> wrote in message

> I should have known that OOP is that easy in COBOL..."Damned".
>

OOP is *very* easy in Cobol, and even if you only use it to replace
subroutines, it has huge advantages.  Wilson Price has published a book on
OOP Cobol(and he was kind enough to send me a free copy)(Elements of Object
Oriented Cobol, www.objectz.com ) that is MF oriented rather than Fujitsu,
and there are some differences.  The new standard is now in final review,
and so that should be cleared up quite soon.

I love it.  The "abort-routine" is very typical of the type of thing it is
almost impossible to do with subroutines.  Not only does it provide a nice
simple way to crash and find out where it happened, but that base object
gives me a "What's this" window for every screen that tells me the source
code library that is currently running.  When projects get huge, that sort
of thing is invaluable to finding your way around in the code.

OOP also provides seamless component based structure; the components can be
written in Cobol or any other language.  PowerCobol will create a COM
object, while Fujitsu also provide a "wrapper" to make regular Cobol code
COM/CORBA compliant.  I have just gotten started on this stuff, and am
starting to get the feel of it.  My next step is to take something like a
customer master system, and wrap it up as a COM object.  In theory, I should
then be able to add a customer database to a system by simply dropping it
into my project.  Certainly, others are using the component model big time,
right now.  Most of those objects can be purchased ... stuff like mailers
and weird-devices.  Peter Dashwood has done a large amount of work using
that approach.  Jimmy Gavan is doing a lot of base module work in MF.  I
would like to see a lot more sharing of code using the OOP approach. I am
convinced that is where the future is.
```

###### ↳ ↳ ↳ Re: Subroutines

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-07T14:43:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A81C195.85EEF9AD@brazee.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com> <95s9to$f0s$1@news.igs.net>`

```
donald tees wrote:

>  I would like to see a lot more sharing of code using the OOP approach. I am
> convinced that is where the future is.

I am convinced that that is where "a" future is.   But what we will see are more
than one future for CoBOL.   In enterprise environments sharing code can cause
more cost than benefit.  If you have 75% maintenance, you don't want to unit
test, user test, and system test every thing your module touches.   If you have
75% maintenance, you need to easily and quickly browse all of the code for a
program.    If you have tons of existing non OO code, the thought of a mixed
code environment doesn't look like a good investment.

Also, how much does a good OO shop save in code reusability in real life?   With
GUIs, I bet quite a bit.  With business rules, I bet not much.   Polymorphing
business rules can also obfuscate them.

Different tools are designed for different needs.  OO is not a tool which is
best for all needs.  Neither is CoBOL.
```

###### ↳ ↳ ↳ Re: Subroutines

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-02-11T16:42:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a86c089.4432262@news1.attglobal.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com> <95s9to$f0s$1@news.igs.net> <3A81C195.85EEF9AD@brazee.net>`

```
There is another benefit to OO we have not touched upon.  Refactoring.
I have used this with OO to enahnce performance - reengineering a
process without having to change the underlying objects.  It's pretty
interesting how well it works.  Refactoring an OO system is MUCH
easier that refactoring a structured system.

On Wed, 07 Feb 2001 14:43:49 -0700, Howard Brazee <howard@brazee.net>
wrote:

>donald tees wrote:
>
…[17 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Subroutines

_(reply depth: 5)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-02-11T18:46:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x6Bh6.7844$Nj5.435469@bgtnsc07-news.ops.worldnet.att.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com> <95s9to$f0s$1@news.igs.net> <3A81C195.85EEF9AD@brazee.net> <3a86c089.4432262@news1.attglobal.net>`

```
REFACTORING AN OO OBJECT

Slowly, the concepts of OO creep into my mind. The jargon not withstanding.
Would someone of you OO people please devise an illustration to KIS(S) this
term?

I'd be grateful, and many others might better grasp the subject better.
Every day, I try to get better and better. Reading CLC is like attending a
life long seminar, enjoyable, but slow learning (which I can handle.)

Warren Simmons
"Thane Hubbell" <thaneH@softwaresimple.com> wrote in message
news:3a86c089.4432262@news1.attglobal.net...
> There is another benefit to OO we have not touched upon.  Refactoring.
> I have used this with OO to enahnce performance - reengineering a
…[9 more quoted lines elided]…
> >>  I would like to see a lot more sharing of code using the OOP approach.
I am
> >> convinced that is where the future is.
> >
> >I am convinced that that is where "a" future is.   But what we will see
are more
> >than one future for CoBOL.   In enterprise environments sharing code can
cause
> >more cost than benefit.  If you have 75% maintenance, you don't want to
unit
> >test, user test, and system test every thing your module touches.   If
you have
> >75% maintenance, you need to easily and quickly browse all of the code
for a
> >program.    If you have tons of existing non OO code, the thought of a
mixed
> >code environment doesn't look like a good investment.
> >
> >Also, how much does a good OO shop save in code reusability in real life?
With
> >GUIs, I bet quite a bit.  With business rules, I bet not much.
Polymorphing
> >business rules can also obfuscate them.
> >
> >Different tools are designed for different needs.  OO is not a tool which
is
> >best for all needs.  Neither is CoBOL.
> >
…[3 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ OO : Refactoring WAS : Subroutines

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-02-16T05:50:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A8CC139.4FD6F5D@home.com>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com> <95s9to$f0s$1@news.igs.net> <3A81C195.85EEF9AD@brazee.net> <3a86c089.4432262@news1.attglobal.net> <x6Bh6.7844$Nj5.435469@bgtnsc07-news.ops.worldnet.att.net>`

```
For : Warren and Howard

Warren Simmons wrote:

> REFACTORING AN OO OBJECT

Ah Ha ! Thane has used one of those $10 words <G> I checked out the few books I
have, plus Net Express on-Line help and Mr. Gates' 'Computer Dictionary' -
zilch. Wanna blame someone - Thane probably picked it up from Ken Foskey, great
OO advocate but spends most of his time currently in C++ - that pays his
mortgage !

It's one of the new buzz phrases, along with Extreme Programming. Refactoring
itself is getting the edge on converting/updating application code, specifically
in an OO environment. One of the gurus is James Fowler. He has a site, starts
"I'll now describe my basic premise, but if you really want the detail, you'll
have to buy my book" GOTCHA !

Go to google.com and search on "refactoring programming" or the other way
around.

I could be way off track but it is another way of saying reusability, and that's
how I interpreted Thane's use of the word. So let's try and keep this KISS.

(1) In an earlier message I illustrated ONE PROGRAM (Class) could have as many
instances as you have files. You subsequently find this File Class program
doesn't do it all for you. You need a new method of access, (a) invent a new
method name which you are going to use from calling programs and add that new
method to the File Class - one change/one compile - the class file, only and
test it with just one program accessing the new method.

Another way would be to create a sub-class containing this specific stuff, so
sub-class B accesses super class A. Now if both Class A and B contain an
identical method name "xyz-do-it", by invoking Class B you are going to get it
actioned as it reads in Class B rather than as it appears in Class A. That's
kind of the reverse order we think in, because Structured Program A tends to
call B, rather than the other way around.

(2) I'll illustrate with GUIs, (although these are not part of the COBOL
standard and never will be - see below about Component Generators). This is
somewhat parallel to what I've mentioned above. In my own design, rather than
laboriously keep on typing source for GUIs, I've put all the GUI actions into a
separate program MyDialog.cbl. (Thane tells me this is not dissimilar to the
approach taken by Flexus with SP2). At the current time MyDialog.cbl handles
only what I need :-

- entry fields
- pushbuttons
- lisboxes/droplists
- radio buttons

and it creates those controls as a result of my using the Merant Dialog Editor
(screen builder tool) or where necessary, dynamically creating controls using
GUI methods.
(Why dynamically ? - the Dialog Editor isn't worth tiddly-squat when I want a
table of 10 x 24 entryfiedls - alternatives being use Activex or Java).

So MyDialog has a whole bunch of method names to do different things,
"hide-object", "show-object", "set-enableEmpty", "set-disable" "get-events"
etc......
and it could grow like Topsy to accommodate anything new I come up with, e.g.,
I could have a new need for a Multiple Line Entry field required for making
notes to attach to a record...

MyDialog.cbl works beautifully. But, getting a bit confused trying to remember
which parameters were required for which method, ( or rather the control being
actioned), I decided I would pass a standard set in a copy file
Dialog-Params.cpy. (Details are irrelevant but it contains x,y,w,h for dynamic
rectangles, and other properties etc.).

So first time I ran MyDialog with the new Dialog-Params it went belly-up !
Here's the original code :-

A Business Logic Class which calls MyDialog
*>------------------------------------------------------------
Method-id. "display-new-record".
*>-----------------------------------------------------------
Procedure Division.

 set NoStressValues    to true
 set ControlCollection to true
 set field-PrimeKey    to true
 move Field            to Dialog-Field
 invoke os-Dialog "set-disable" using Dialog-Params  *>  in Working-Storage
 set Field-SpecNo to true
 move Field       to Dialog-Field
 invoke os-Dialog "set-nextfocus-empty" using Dialog-Params  <<<<--------

Exit Method
End Method "display-new-record".
*>------------------------------------------------------------

MyDialog.cbl
---------------
Note - the following method is accessed from my Business Program above
*>-------------------------------------------------------------
Method-id. "set-nextfocus-empty".
*>--------------------------------------------------------------

*> This method sets the entryfield "setEmpty" for fresh user
*> input.

Local-storage section.
01 ls-object                         object reference.
Linkage section.
copy "dilogprm.cpy" replacing ==(tag)== by ==lnk==.

Procedure Division using lnk-Params.

  invoke os-Collection(2) "at"
         using lnk-field returning ls-object
  set os-CurrentObject to ls-object
  invoke os-CurrentObject "enable"
  invoke os-CurrentObject "setempty"
  invoke os-CurrentObject "setfocus"
  invoke super            "show"

End Method "set-nextfocus-empty".
*>--------------------------------------------------------------

The following method in MyDialog is initial 'housekeeping: :-

Method-id. "z-create-Entryfield".
*>-------------------------------------------------------------
Local-storage section.
01 ls-event                      pic x(4) comp-5.
01 ls-object                     object reference.
01 ls-size                       pic x(4) comp-5.
01 ls-capacity                   pic x(4) comp-5.
Linkage section.
copy "dilogprm.cpy" replacing ==(tag)== by ==lnk==.

Procedure Division using lnk-Params.

 invoke self "getObjectFromId"
        using lnk-ID returning ls-object

 *** etc.... , more stuff, but I've pared down  to illustrate the problem

 if   lnk-length <> zeroes
      invoke ls-object "setLength" using lnk-length
      invoke ls-object "accessSystemEvents"
      move Button1Down to ls-event

      Evaluate true
       when EmptyField
         invoke ls-object "setEventto" using
           ls-event, self, "z-set-nextfocus-empty ", lnk-Field
       when other
         invoke ls-object "setEventto" using
           ls-event, self, "z-set-nextfocus-insert ", lnk-Field
      End-evaluate

*** more stuff................

End Method "z-create-Entryfield".
*>--------------------------------------------------------------

Now look at the above. My Business Program calling MyDialog for
"set-nextfocus-empty" will give the correct results. But now look at the method
"z-create-entryfield", as originally worded. It will go belly up because of
incorrect parameters. Sod it ! It doesn't work.

Now - revised code to handle the above problem :-

*>--------------------------------------------------------------
Method-id. "z-create-Entryfield".
*>-------------------------------------------------------------
Local-storage section.
01 ls-event                      pic x(4) comp-5.
01 ls-object                     object reference.
01 ls-size                       pic x(4) comp-5.
01 ls-capacity                   pic x(4) comp-5.
Linkage section.
copy "dilogprm.cpy" replacing ==(tag)== by ==lnk==.

Procedure Division using lnk-Params.

 invoke self "getObjectFromId"
        using lnk-ID returning ls-object

 *** etc.... ......

 if   lnk-length <> zeroes
      invoke ls-object "setLength" using lnk-length
      invoke ls-object "accessSystemEvents"
      move Button1Down to ls-event

      Evaluate true
       when EmptyField
         invoke ls-object "setEventto" using
           ls-event, self, "z-set-nextfocus-empty ", lnk-Field   <<< new method
name
       when other
         invoke ls-object "setEventto" using
           ls-event, self, "z-set-nextfocus-insert ", lnk-Field     <<< new
method name
      End-evaluate

**** some more code

End Method "z-create-Entryfield".
*>--------------------------------------------------------------
Following new method added - and only occurs in MyDialog.cbl - so you can
consider it to be a 'Private' method.
*>------------------------------------------------------------
Method-id. "z-set-nextfocus-empty".
*>------------------------------------------------------------
Local-storage section.
copy "dilogprm.cpy" replacing ==(tag)== by ==ls==.
Linkage section.
01 lnk-field                         pic x(4) comp-5.
Procedure Division using lnk-field.
  initialize ls-Params
  move 2 to ls-number
  move lnk-field to ls-Field
  invoke self "set-nextfocus-empty" using ls-Params

End Method "z-set-nextfocus-empty".
*>------------------------------------------------------------

 Problem solved - and only one compile and one test !

(3) Example 3

Big American Corp Inc., trades only in the Americas. They have a class which
handles all date functions, plus formatting. They now move into Europe, so they
are confronted with German, Dutch, French, Italian etc.( But wait, they've
probably already covered this scenario because in dealing with Canada they had
to allow for French in Quebec, Spanish in Mexico; chances are they are trading
in S. America, so throw in Portuguese as well).

The date problem - no big deal. Having deftly designed a class to handle all
date problems, intrinsic functions, difference between two dates etc., now we
come up against the various 'human' languages - formatting in the 'local' tongue
for display/printing. The various languages are 'sub classed' to Class Date, the
correct terminology being Classes FrenchDates or GermanDates invoke the Class
"super" Dates.

OK. So there's nothing really to stop you paralleling this in Structured. Based
on any given set of tools, it's up to us to become individually innovative.
Warren, like you, I'm much too old in the tooth to be taken in by a modern
gimmick - for me OO COBOL is ELEGANT and an absolute PLEASURE to use. Now the
kicker - the proof of the pudding is in the eating - at the current time you can
only 'prove' it with Fujitsu and Net Express.

Howard's comments

Well I know he's got his violin out to play the 'maintenance' theme, and it is a
genuine concern. I know you wont buy it, but you don't have to goddam test
everything, if you've got it isolated like I've tried to illustrate above. When
was the last time you tested COBOL intrinsic functions against every program in
your installation that uses them.

Savings on reusability - might be figures from other languages, but I don't
accept them as being applicable to COBOL. Until we see a growth in OO COBOL  we
wont know. Yes you are right about the effectiveness with GUIs, as my quotes
above indicate.

Reusability with Business problems - yes and know - I'll go 50% with you that
the business problem is unique. Take Walmart and Montgomery Ward - success and
disaster - it was the application of business(marketing) rules/philosphy that
puts them at the respective ends of the spectrum. Business philosophy and
resulting rules will be the driving force.

But the other 50 % for our two retailers - they have so much in common.

Take a hypothetical example - Payroll. (I know nothing of this topic ensuring we
used an ICL package when I was a Systems Manager <G>). Let's say you are in
Quebec and had a method to calculate overtime which is a standard 1.5. Then the
Quebecers decide that if you work on St. Jean Baptiste day, (whenever that is),
that by law you get double-time, or maybe even triple-time. Ouch ! Your PayCalc
Class doesn't handle it. Solution - add a new method :-

Business Class
-------------
invoke PayCalc "get-overtime" using Rate, Hours returning Dollars - OR -

if StJeanBaptitsteDay
   invoke PayCalc "get-StJean" using Rate, Hours returning Dollars
End-if

Class - PayCalc
----------------
method-id. "get-overtime".
Linkage Rate, Hours, Dollars.
Procedure Division using Rate Hours returning Dollars.
   compute Dollars =  etc....

method-id. "get-StJean".
Linkage Rate, Hours, Dollars2.
Procedure Division using Rate Hours returning Dollars2.
    invoke self "get-overtime" using Rate Hours returning Dollars1
   compute Dollars2 =  etc.......

Maybe a lousy example, but it does illustrate the concept of 'flexibility', and
the same approach is universal in OO to all business rules that break the mode.
OO hardly represents a 'business tool', it is a methodology -  No, a methodical
approach to system design related to business problems, breaking them down into
itsy bitsy methods to cover a variety of possibilities(rules).

Let me stress again - you can parallel it in Structured - I just have the gut
feeling that OO is to an nth degree more flexible. (Well, actually it's more
than a gut feeling - I KNOW it works for me <G>)

> >I am convinced that that is where "a" future is.   But what we will see
>> are more than one future for CoBOL....

Where does the future that you forsee fit in. Here's a sobering thought for the
non-OO'ers. Just heard from Mike Sheehan that Limerick Tech (in Eire) which is
one of the mainstays in the republic for teaching COBOL, is calling it quits in
two years time for our language. If this continues, it wont really matter what
your preference is, whether Structured or OO - unless you are one of the lucky
ones, already retired before COBOL gets buried..

Component Maker

Warren - Knowing your interest in keeping up to snuff, even though in your
twilight years, write to Pete Dashwood who will explain the following more
eloquently than I can. I know he will be delighted to respond to you.

GUIs are not part of COBOL; perhaps they could have been, had they been given
some serious thought 20 years ago when the "Mickey Mouse" Apples, Radio Shacks
and then PCs were first touted. Smalltalk had GUI classes in the '70s. But again
- GUIs designed by a committee !!!!??????  Smalltalk, Jobs, Gates, Java -
single-minded designers/entrepreneurs  pushed the envelope.

It's got to be some four months or more ago that somebody jumped in here
promoting his use of POWERCOBOL - he was such an asshole that most of us ignored
him; ignoring the messenger we also ignored the message. Now Pete is on the same
tack - more diplomatically <G>. The way to go for UI(User Interface) or GUI-ing
is to treat it as being outside of COBOL. (Now being one of the 'originals' in
introducing DB for COBOL, I think you will appreciate the similarity).

Pete's contention is that UI must stand independent of ANY language - and that
includes Java. You use the appropriate tools/languages  to build a 'window',
clicking, dropping and dragging, getting 'shapes', properties AND method code
related to the control. Plus he also adds, drag and drop in a database if
necessary. The finished component then becomes usable with ANY language.. Take
an extension of this UI approach - I doubt any of us would suggest COBOL should
be used for light pens, voice recognition etc. It makes sense to build these
features in using a general purpose Component Generator.

Chances are component generators will come and go as they beat one another out
of the market, but the payola is that we ALL finish up with an even better
designing tool. (Hope our friends at Flexus and Norcom are keeping 'alert').

Jimmy, Calgary AB

>
> Slowly, the concepts of OO creep into my mind. The jargon not withstanding.
…[52 more quoted lines elided]…
> > My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Subroutines

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-12T07:40:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A87F5E8.E1A7C3BB@brazee.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com> <95s9to$f0s$1@news.igs.net> <3A81C195.85EEF9AD@brazee.net> <3a86c089.4432262@news1.attglobal.net>`

```


Thane Hubbell wrote:

> There is another benefit to OO we have not touched upon.  Refactoring.
> I have used this with OO to enahnce performance - reengineering a
> process without having to change the underlying objects.  It's pretty
> interesting how well it works.  Refactoring an OO system is MUCH
> easier that refactoring a structured system.

Please define refactoring.
```

###### ↳ ↳ ↳ Re: Subroutines

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2001-02-15T21:38:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96i42e$n51$2@news.hitter.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com> <95s9to$f0s$1@news.igs.net> <3A81C195.85EEF9AD@brazee.net> <3a86c089.4432262@news1.attglobal.net> <3A87F5E8.E1A7C3BB@brazee.net>`

```

Howard Brazee wrote in message <3A87F5E8.E1A7C3BB@brazee.net>...
>
>
…[8 more quoted lines elided]…
>Please define refactoring.

I'll give it a try.

Refactoring is factoring after the code has been written. :-)

Factoring is accomplished during design.

Factoring is the process of removing common elements
from two or more classes. These common elements are
placed into a superclass. The original classes are then
changed to inherit from that superclass.

The primary reason for (re)factoring is that, if there is a
common element between two classes, there is a
possibility that more new classes might use that common
element.(1)

1. Robert C. Martin, "Designing Object-Oriented C++
    Applications," Prentice-Hall, 1995.
------------------
Rick Smith
```

###### ↳ ↳ ↳ Re: Subroutines

_(reply depth: 7)_

- **From:** "Warren Simmons" <warren.simmons@worldnet.att.net>
- **Date:** 2001-02-16T15:06:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5mbj6.12566$Nj5.824982@bgtnsc07-news.ops.worldnet.att.net>`
- **References:** `<95ebmb$qr6$1@nnrp1.deja.com> <3A7B99ED.AD0ADAF@optonline.net> <95gdnb$jp6$1@nnrp1.deja.com> <95h24b$ltn$1@slb0.atl.mindspring.net> <95lnv6$9fm$1@nnrp1.deja.com> <95qmnc$k5g$1@news.igs.net> <95r0op$tbl$1@nnrp1.deja.com> <95rlp2$5nr$1@news.igs.net> <95rt7u$kk3$1@nnrp1.deja.com> <95s9to$f0s$1@news.igs.net> <3A81C195.85EEF9AD@brazee.net> <3a86c089.4432262@news1.attglobal.net> <3A87F5E8.E1A7C3BB@brazee.net> <96i42e$n51$2@news.hitter.net>`

```
Great, Rick.... Set theory... I get it.

Thanks, Warren Simmons
"Rick Smith" <ricksmith@aiservices.com> wrote in message
news:96i42e$n51$2@news.hitter.net...
>
> Howard Brazee wrote in message <3A87F5E8.E1A7C3BB@brazee.net>...
…[33 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
