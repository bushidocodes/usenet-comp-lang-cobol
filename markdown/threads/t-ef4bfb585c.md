[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# **Update-Index-File

_1 message · 1 participant · 1999-11_

---

### **Update-Index-File

- **From:** Bill <dc606@my-deja.com>
- **Date:** 1999-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81p3k8$a9j$1@nnrp1.deja.com>`

```
Purpose of Program:  To update index file
I am getting errors that I expect to get in my error report, therefore,
I assume other transactions were added, deleted or corrected.

Is there another way to confirm that transactions were added, deleted or
corrected?

Is there any way that I can view Validx.Dat in a readable format?

Can I confirm somehow through Indexed-Status-Bytes that update was done
correctly?



Miscellaneous Question
Should Indexed-Status-Bytes be used for every program that includes an
index file?
Of course, Index-Status-Bytes should be used only for programs that
include an indexed file right?

Thank you.


************************************************************************

     ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

           SELECT TRANSACTION-FILE ASSIGN TO 'A:\TRANS.DAT'
               ORGANIZATION IS LINE SEQUENTIAL.
           SELECT INDEXED-FILE ASSIGN TO 'A:\VALIDX.DAT'
               ORGANIZATION IS INDEXED
               ACCESS IS RANDOM
               RECORD KEY IS IND-SOC-SEC-NUM
               FILE STATUS IS INDEXED-STATUS-BYTES.
           SELECT ERROR-FILE ASSIGN TO 'A:\ERROR.DAT'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD  TRANSACTION-FILE
           RECORD CONTAINS 47 CHARACTERS
           DATA RECORD IS TRANSACTION-RECORD.
           01  TRANSACTION-RECORD      PIC X(47).


       FD  INDEXED-FILE
           RECORD CONTAINS 46 CHARACTERS
           DATA RECORD IS INDEXED-RECORD.
       01  INDEXED-RECORD.
           05 IND-SOC-SEC-NUM           PIC X(9).
           05 IND-SSN-NUMERIC
              REDEFINES IND-SOC-SEC-NUM PIC 9(9).
           05 IND-REST-OF-RECORD       PIC X(37).

       FD  ERROR-FILE
           RECORD CONTAINS 132 CHARACTERS
           DATA RECORD IS ERROR-RECORD.
       01  ERROR-RECORD                PIC X(132).


       WORKING-STORAGE SECTION.
       01  FILLER                      PIC X(14)
               VALUE 'WS BEGINS HERE'.
       01  WS-TRANS-RECORD.
           05  TR-SOC-SEC-NUMBER       PIC X(9).
           05  TR-TRANSACTION-CODE     PIC X.
               88  ADDITION    VALUE 'A'.
               88  CORRECTION  VALUE 'C'.
               88  DELETION    VALUE 'D'.
           05  TR-NAME-AND-INITIALS    PIC X(15).
           05  TR-BIRTH-DATE.
               10  TR-BIRTH-MONTH     PIC 9(2).
               10  TR-BIRTH-YEAR      PIC 9(2).
           05  TR-LOCATION-CODE        PIC X(3).
           05  TR-EDUCATION-CODE       PIC 9.
           05  TR-TITLE-DATA.
               10  TR-TITLE-CODE       PIC X(3).
               10  TR-TITLE-DATE.
                   15  TR-TITLE-MONTH  PIC 9(2).
                   15  TR-TITLE-YEAR   PIC 9(2).
           05  TR-RATING               PIC X.
           05  TR-SALARY               PIC X(6).
       01  WS-MASTER-RECORD.
           05  MA-SOC-SEC-NUMBER       PIC X(9).
           05  MA-NAME-AND-INITIALS    PIC X(15).
           05  MA-BIRTH-DATE.
               10  MA-BIRTH-MONTH      PIC 9(2).
               10  MA-BIRTH-YEAR       PIC 9(2).
           05  MA-LOCATION-CODE        PIC X(3).
           05  MA-EDUCATION-CODE       PIC 9.
           05  MA-TITLE-DATA.
               10  MA-TITLE-CODE       PIC X(3).
               10  MA-TITLE-DATE.
                   15  MA-TITLE-MONTH  PIC 9(2).
                   15  MA-TITLE-YEAR   PIC 9(2).
           05  MA-RATING               PIC X.
           05  MA-SALARY               PIC X(6).
       01  ERROR-REASONS.
           05  ADD-MSG                 PIC X(40)
               VALUE 'DUPLICATE RECORD'.
           05  CORRECT-MSG             PIC X(50)
               VALUE 'KEY DOES NOT EXIST ON MASTER FILE-CORRECT-MSG'.
           05  DELETE-MSG              PIC X(50)
               VALUE 'KEY DOES NOT EXIST ON MASTER-FILE-DELETE-MSG'.

       01  PROGRAM-SWITCHES.
           05 END-OF-FILE-SWITCH       PIC X(3)     VALUE 'NO'.
           05 RECORD-KEY-ALLOCATED-SWITCH  PIC X(3) VALUE 'NO'.
           05 INDEXED-STATUS-BYTES     PIC 99.

       01  ERROR-LINE.
           05 ERR-SOC-SEC              PIC X(9).
           05 FILLER                   PIC X(13).

           05 ERR-TRANS-CODE           PIC X(1).
           05 FILLER                   PIC X(6).

           05 ERROR-MESSAGE            PIC X(47).
           05 FILLER                   PIC X(2).
       PROCEDURE DIVISION.
       100-PROCESS-TRANSACTION-FILE.
           OPEN INPUT TRANSACTION-FILE
                I-O INDEXED-FILE
                OUTPUT  ERROR-FILE.
           DISPLAY 'OPEN STATEMENT EXECUTED'.
           DISPLAY ' FILE STATUS BYTES = ', INDEXED-STATUS-BYTES.
           DISPLAY ' '.

           PERFORM UNTIL END-OF-FILE-SWITCH='YES'
               READ TRANSACTION-FILE INTO WS-TRANS-RECORD
                   AT END
                       MOVE 'YES' TO END-OF-FILE-SWITCH
                   NOT AT END
                       PERFORM 300-READ-INDEXED-FILE
                       PERFORM 400-APPLY-TRANS-TO-MASTER
               END-READ
           END-PERFORM.
           CLOSE TRANSACTION-FILE
                 INDEXED-FILE
                 ERROR-FILE.
           DISPLAY 'CLOSE STATEMENT EXECUTED '.
           DISPLAY ' FILE STATUS BYTES = ', INDEXED-STATUS-BYTES.
           DISPLAY ' ' .
           STOP RUN.

       300-READ-INDEXED-FILE.
           MOVE TR-SOC-SEC-NUMBER TO IND-SSN-NUMERIC.
           READ INDEXED-FILE INTO WS-MASTER-RECORD
               INVALID KEY
                   MOVE 'NO' TO RECORD-KEY-ALLOCATED-SWITCH
               NOT INVALID KEY
                   MOVE 'YES' TO RECORD-KEY-ALLOCATED-SWITCH
           END-READ.

       400-APPLY-TRANS-TO-MASTER.
           EVALUATE TRUE
               WHEN ADDITION
                   PERFORM 500-ADD-NEW-RECORD
               WHEN CORRECTION
                   PERFORM 600-CORRECT-EXISTING-RECORD
               WHEN DELETION
                   PERFORM 700-DELETE-EXISTING-RECORD
               WHEN OTHER
                   DISPLAY 'INVALID TRANSACTION CODE'
           END-EVALUATE.

       500-ADD-NEW-RECORD.
           IF RECORD-KEY-ALLOCATED-SWITCH='YES'
               PERFORM 800-MOVE-ADD-MSG-LINE
           ELSE
               MOVE SPACES TO WS-MASTER-RECORD
               MOVE TR-SOC-SEC-NUMBER TO MA-SOC-SEC-NUMBER
               MOVE TR-NAME-AND-INITIALS TO MA-NAME-AND-INITIALS
               MOVE TR-BIRTH-DATE TO MA-BIRTH-DATE
               MOVE TR-LOCATION-CODE TO MA-LOCATION-CODE
               MOVE TR-EDUCATION-CODE TO MA-EDUCATION-CODE
               MOVE TR-TITLE-DATA TO MA-TITLE-DATA
               MOVE TR-RATING TO MA-RATING
               MOVE TR-SALARY TO MA-SALARY
               WRITE INDEXED-RECORD FROM WS-MASTER-RECORD
           END-IF.

       600-CORRECT-EXISTING-RECORD.
           IF RECORD-KEY-ALLOCATED-SWITCH = 'YES'
               MOVE SPACES TO WS-MASTER-RECORD
               MOVE TR-SOC-SEC-NUMBER TO MA-SOC-SEC-NUMBER
               MOVE TR-NAME-AND-INITIALS TO MA-NAME-AND-INITIALS
               MOVE TR-BIRTH-DATE TO MA-BIRTH-DATE
               MOVE TR-LOCATION-CODE TO MA-LOCATION-CODE
               MOVE TR-EDUCATION-CODE TO MA-EDUCATION-CODE
               MOVE TR-TITLE-DATA TO MA-TITLE-DATA
               MOVE TR-RATING TO MA-RATING
               MOVE TR-SALARY TO MA-SALARY
               REWRITE INDEXED-RECORD FROM WS-MASTER-RECORD
           ELSE
               PERFORM 900-MOVE-CORRECT-MSG-LINE
           END-IF.

       700-DELETE-EXISTING-RECORD.
           IF RECORD-KEY-ALLOCATED-SWITCH= 'YES'
               DELETE INDEXED-FILE
           ELSE
               PERFORM 1000-MOVE-DELETE-MSG-LINE
           END-IF.


       800-MOVE-ADD-MSG-LINE.
               MOVE TR-SOC-SEC-NUMBER TO ERR-SOC-SEC.
               MOVE TR-TRANSACTION-CODE TO ERR-TRANS-CODE.
               MOVE ADD-MSG TO ERROR-MESSAGE.
               MOVE ERROR-LINE TO ERROR-RECORD.
               WRITE ERROR-RECORD.


       900-MOVE-CORRECT-MSG-LINE.
               MOVE TR-SOC-SEC-NUMBER TO ERR-SOC-SEC.
               MOVE TR-TRANSACTION-CODE TO ERR-TRANS-CODE.
               MOVE CORRECT-MSG TO ERROR-MESSAGE.
               MOVE ERROR-LINE TO ERROR-RECORD.
               WRITE ERROR-RECORD.

       1000-MOVE-DELETE-MSG-LINE.
               MOVE TR-SOC-SEC-NUMBER TO ERR-SOC-SEC.
               MOVE TR-TRANSACTION-CODE TO ERR-TRANS-CODE.
               MOVE DELETE-MSG TO ERROR-MESSAGE.
               MOVE ERROR-LINE TO ERROR-RECORD.
               WRITE ERROR-RECORD.




Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
