[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Please!

_2 messages · 2 participants · 2002-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Re: Help Please!

- **From:** "Dan J" <dali@cogeco.ca>
- **Date:** 2002-12-03T23:19:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GjfH9.40728$lj.837513@read1.cgocable.net>`

```

"Dan J" <dali@cogeco.ca> wrote in message news:...
> I'm a student. I've got 6 comliation errors that I can not solve for the
> life of me. Can anybody help? Please, Please!!!
…[24 more quoted lines elided]…
>

       IDENTIFICATION DIVISION.
       PROGRAM-ID. SALES.
      **********************************************
      * BY:DALIBOR JOVASEVIC 313578                *
      * ASSIGNMENT 4                               *
      * INPUT - READ CM2002S                       *
      * SALES COMMISSION REPORT                    *
      **********************************************

       ENVIRONMENT DIVISION.

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

           SELECT  SALES-FILE  ASSIGN TO DISK "D:\COBOL\CM2002S.DAT"
                               ORGANIZATION IS LINE SEQUENTIAL.

           SELECT  PRINT-FILE  ASSIGN TO PRINTER "D:\COBOL\A4.RPT"
                               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.

       FILE SECTION.

       FD SALES-FILE
           RECORD  CONTAINS    80 CHARACTERS
           DATA    RECORD      IS SALES-REC.

       01  SALES-REC.
           05  SR-STORE-NUMBER     PIC XX.
           05  SR-DEPT-NUMBER      PIC XX.
           05  SR-EMPL-NUMBER      PIC XXX.
           05  SR-EMPL-NAME        PIC X(20).
           05  SR-YTD-SALES        PIC 9(5)V99.
           05  SR-CUR-SALES        PIC 9(5)V99.
           05  SR-COMM             PIC 99.
           05  SR-EMPL-CODE        PIC XX.
           05  SR-YTD-RETURNS      PIC 9(4)V99.
           05  SR-CUR-RECORDS      PIC 9(4)V99.
           05  FILLER              PIC X(23).

       FD  PRINT-FILE
           RECORD  CONTAINS    132 CHARACTERS
           DATA    RECORDS     IS  PRINT-REC.

       01  PRINT-REC               PIC X(132).

       WORKING-STORAGE SECTION.
       01  WS-SWITCHERS.
           05  WS-MORE-RECORDS     PIC XXX             VALUE "YES".
           05  WS-FOUND            PIC XXX             VALUE "NO".
           05  WS-NEW-COMM-RATE    PIC 99V99           VALUE 0.
           05  WS-OLD-COMM         PIC 9999V99         VALUE 0.
           05  WS-NEW-COMM         PIC 9999V99         VALUE 0.
           05  WS-NEW-COMM-INCREASE PIC 9V99           VALUE 0.

       01  WS-COUNTERS             COMP-3.
           05  WS-RECORD-COUNT     PIC S99             VALUE +0.
           05  WS-PAGE-COUNT       PIC S99             VALUE +0.
           05  WS-LINE-COUNT       PIC S99             VALUE +60.

       01  WS-TOTAL-COMMISSION     COMP-3.
           05  WS-OLD-COMMISSION   PIC S9(6)V99        VALUE 0.
           05  WS-NEW-COMMISSION   PIC S9(6)V99        VALUE 0.
           05  WS-COUNTER          PIC 999V99          VALUE 0.

       01  WS-ACCUMULATIONS.
           05  WS-TOT-YTD-SALES    PIC S9(7)V99   COMP-3   VALUE +0.
       01  HDG1.
           05  FILLER              PIC X(5)            VALUE SPACES.
           05  H1-DATE             PIC 99/99/99.
           05                      PIC X(50)           VALUE SPACES.
           05                      PIC X(35)
                                   VALUE "ABC COMPANY".

           05                      PIC X(11)           VALUE SPACES.
           05                      PIC X(5)            VALUE "PAGE".
           05  H1-PAGE             PIC ZZ9.

       01  HDG2.
           05  FILLER      PIC X(60)   VALUE SPACES.
           05  FILLER      PIC X(62)   VALUE "COMMISSION SUMMARY".

       01  HDG3.
           05  FILLER      PIC X(5)    VALUE SPACES.
           05  FILLER      PIC X(5)    VALUE "STORE".
           05  FILLER      PIC X(5)    VALUE SPACES.
           05  FILLER      PIC X(10)   VALUE "DEPARTMENT".
           05  FILLER      PIC X(9)    VALUE SPACES.
           05  FILLER      PIC X(12)   VALUE "EMPLOYEE".
           05  FILLER      PIC X(16)   VALUE SPACES.
           05  FILLER      PIC X(3)    VALUE "YTD".
           05  FILLER      PIC X(8)    VALUE SPACES.
           05  FILLER      PIC X(3)    VALUE "OLD".
           05  FILLER      PIC X(5)    VALUE SPACES.
           05  FILLER      PIC X(8)    VALUE "OLD COMM".
           05  FILLER      PIC X(9)    VALUE SPACES.
           05  FILLER      PIC X(3)    VALUE "NEW".
           05  FILLER      PIC X(10)   VALUE SPACES.
           05  FILLER      PIC X(3)    VALUE "NEW".

       01  HDG4.
           05  FILLER      PIC X(5)    VALUE SPACES.
           05  FILLER      PIC X(6)    VALUE "NUMBER".
           05  FILLER      PIC X(4)    VALUE SPACES.
           05  FILLER      PIC X(4)    VALUE "NAME".
           05  FILLER      PIC X(15)   VALUE SPACES.
           05  FILLER      PIC X(4)    VALUE "NAME".
           05  FILLER      PIC X(23)   VALUE SPACES.
           05  FILLER      PIC X(7)    VALUE "SALES".
           05  FILLER      PIC X(5)    VALUE SPACES.
           05  FILLER      PIC X(4)    VALUE "COMM".
           05  FILLER      PIC X(6)    VALUE SPACES.
           05  FILLER      PIC X(4)    VALUE "RATE".
           05  FILLER      PIC X(11)   VALUE SPACES.
           05  FILLER      PIC X(4)    VALUE "COMM".
           05  FILLER      PIC X(9)    VALUE SPACES.
           05  FILLER      PIC X(4)    VALUE "RATE".

       01  DETAIL-LINE.
           05  FILLER           PIC X(7)   VALUE SPACES.
           05  DTL-STORE-NUMBER PIC XX.
           05  FILLER           PIC X(6)   VALUE SPACES.
           05  DTL-DEPT-NAME    PIC X(15).
           05  FILLER           PIC X(4)   VALUE SPACES.
           05  DTL-EMPL-NAME    PIC X(20).
           05  FILLER           PIC X(5)   VALUE SPACES.
           05  DTL-YTD-SALES    PIC $Z,ZZZ.99.
           05  FILLER           PIC X      VALUE SPACES.
           05  DTL-COMM         PIC $$,$$$.99.
           05  FILLER           PIC X      VALUE SPACES.
           05  DTL-NEW-COMM-RATE PIC $$,$$$.99.
           05  FILLER           PIC X(6)   VALUE SPACES.
           05  DTL-NEW-COMM     PIC $$,$$$.99.
           05  FILLER           PIC X(5).
           05  DTL-OLD-COMM     PIC $$,$$$.99.

       01  TOTAL-LINE1.
           05  FILLER      PIC X(27)   VALUE SPACES.
           05  FILLER      PIC X(33)
           VALUE "*** TOTAL OLD COMMISSION PAID WAS".
           05  FILLER      PIC X(2)    VALUE SPACES.
           05  TOC-PAID    PIC $,$$$,$$$.99.

       01  TOTAL-LINE2.
           05  FILLER      PIC X(27)   VALUE SPACES.
           05  FILLER      PIC X(33)
           VALUE "*** TOTAL NEW COMMISSION PAID WAS".
           05  FILLER      PIC X(2)    VALUE SPACES.
           05  TNC-PAID    PIC $,$$$,$$$.99.

       01 TOTAL-LINE3.
           05  FILLER      PIC X(31)   VALUE SPACES.
           05  FILLER      PIC X(30)
           VALUE "AVERAGE PERCENTAGE INCREASE OF".
           05  FILLER      PIC X(7)    VALUE SPACES.
           05  AVERAGE     PIC ZZ9.99.
           05  FILLER      PIC X       VALUE SPACES.
           05  FILLER      PIC X(3)    VALUE "%".

       01  RATE-TABLES.
           05  TAB-RATE-DATA.
               10 FILLER           PIC 9(5) VALUE 15000.
               10 FILLER           PIC 9V99 VALUE 2.50.
               10 FILLER           PIC 9(5) VALUE 10000.
               10 FILLER           PIC 9V99 VALUE 1.75.
               10 FILLER           PIC 9(5) VALUE 1.00.
               10 FILLER           PIC 9(5) VALUE 00000.
               10 FILLER           PIC 9V99 VALUE 0.50.
               10 FILLER           PIC 9(5) VALUE 00000.
               10 FILLER           PIC 9V99 VALUE 0.00.
           05  TAB-RATE-TABLE REDEFINES TAB-RATE-DATA OCCURS 5 TIMES.
               10 TAB-SALES        PIC 9(5).
               10 TAB-RATE         PIC 9V99.

       01  SUB-COMMISSION.
           05  SUB-COMM            PIC 9.
           05  SUB-RATE            PIC 9.

       01  DEPARTMENT-TABLE.
           05  DEPARTMENT-TABLE-WS.
               10      PIC X(17)   VALUE "01WOMENS DEPART".
               10      PIC X(17)   VALUE "01HOSEHOLD DEP".
               10      PIC X(17)   VALUE "03SPORTING GOODS".
               10      PIC X(17)   VALUE "04AUTOM. GOODS".
               10      PIC X(17)   VALUE "05HARDWARE".
               10      PIC X(17)   VALUE "06SIGHT & SOUND".
               10      PIC X(17)   VALUE "07MENS DEPART".
               10      PIC X(17)   VALUE "08PETS".
               10      PIC X(17)   VALUE "09TOYLAND".
           05  DEPT-TABLE-RED  REDEFINES DEPARTMENT-TABLE-WS
                   OCCURS 9 TIMES.
                   10 DEPT-NUMBER      PIC XX.
                   10 DEPT-NAME        PIC X(15).

       01  SUB-DEPARTMENT-NAME.
           05  SUB-DEPT-NAME           PIC 99  VALUE 1.

       PROCEDURE DIVISION.

       1000-MAIN.
           PERFORM 1100-START-UP.
           PERFORM 1200-PROCESS
                           UNTIL WS-MORE-RECORDS = "NO".
           PERFORM 1300-FINISH-UP.
           STOP RUN.

       1100-START-UP.
           OPEN INPUT  SALES-FILE.
           OPEN OUTPUT PRINT-FILE.

           ACCEPT H1-DATE FROM DATE.

           PERFORM 1110-READ.
           IF WS-MORE-RECORDS = "YES"
           NEXT SENTENCE.

       1200-PROCESS.

           MOVE "NO" TO WS-FOUND.
           PERFORM 1210-DEPARTMENT-NAME
               VARYING SUB-DEPT-NAME
                   FROM 1 BY 1 UNTIL
                       SUB-DEPT-NAME > 9
                       OR
                   WS-FOUND = "YES"

           MOVE "NO" TO WS-FOUND.
           PERFORM 1220-COMMISSION-PERCENTAGE
               VARYING SUB-COMM
                   FROM 1 BY 1 UNTIL
                       SUB-COMM > 4
                   OR
                       WS-FOUND = "YES".

           PERFORM 1230-COMPUTE-SECTION.
           PERFORM 1240-WRITE-SALES-LINE.
           PERFORM 1110-READ.

       1300-FINISH-UP.
           PERFORM 1310-TOTALS.
           CLOSE SALES-FILE.
           CLOSE PRINT-FILE.

       1110-READ.
           READ SALES-FILE
           AT END
           MOVE "NO" TO WS-MORE-RECORDS.

       1210-DEPARTMENT-NAME.
           IF SR-DEPT-NUMBER = DEPT-NUMBER (SUB-DEPT-NAME)
           MOVE DEPT-NAME (SUB-DEPT-NAME) TO DTL-DEPT-NAME
           MOVE 10 TO SUB-DEPT-NAME
           MOVE "YES" TO WS-FOUND
           ELSE
           NEXT SENTENCE.

       1220-COMMISSION-PERCENTAGE.
           IF SR-YTD-SALES > TAB-SALES (SUB-COMM)

           MOVE TAB-RATE (SUB-COMM) TO WS-NEW-COMM-INCREASE
           MOVE 5 TO SUB-COMM
           MOVE "YES" TO WS-FOUND
           ELSE
           NEXT SENTENCE.

       1230-COMPUTE-SECTION.

           COMPUTE WS-NEW-COMM-RATE = SR-COMM + WS-NEW-COMM-INCREASE.
           COMPUTE
               WS-NEW-COMM = (SR-YTD-SALES * WS-NEW-COMM-RATE) / 100.
           COMPUTE WS-OLD-COMM = ( SR-YTD-SALES * SR-COMM) / 100.

           ADD WS-NEW-COMM-INCREASE TO WS-AVERAGE-INCREASE.
           ADD 1 TO WS-COUNTER.
           ADD WS-OLD-COMM TO WS-OLD-COMMISSION.
           ADD WS-NEW-COMM TO WS-NEW-COMMISSION.

       1240-WRITE-SALES-LINE.

           IF WS-LINE-COUNT > 40
               PERFORM 1241-WROTE-HEADINGS
           ELSE
           NEXT SENTENCE.

           MOVE SR-STORE-NUMBER        TO DTL-STORE-NUMBER
           MOVE SR-EMPL-NAME           TO DTL-EMPL-NAME
           MOVE SR-YTD-SALES           TO DTL-YTD-SALES
           MOVE SR-COMM                TO DTL-COMM
           MOVE WS-NEW-COMM-RATE       TO DTL-NEW-COMM-RATE
           MOVE WS-NEW-COMM            TO DTL-NEW-COMM
           MOVE WS-OLD-COMM            TO DTL-OLD-COMM

           WRITE PRINT-REC FROM DETAIL-LINE AFTER ADVANCING 1 LINES

           ADD 1                       TO WS-LINE-COUNT.

       1310-TOTALS.

           MOVE WS-OLD-COMMISSION  TO TOC-PAID
           MOVE WS-NEW-COMMISSION  TO TNC-PAID

           COMPUTE AVERAGE = WS-AVERAGE-INCREASE / WS-COUNTER
           WRITE PRINT-REC     FROM TOTAL-LINE1 AFTER ADVANCING 3 LINE.

           WRITE PRINT-REC     FROM TOTAL-LINE2 AFTER ADVANCING 1 LINE.

           WRITE PRINT-REC     FROM TOTAL-LINE3 AFTER ADVANCING 3 LINE.

       1241-WRITE-HEADINGS.

           ADD 1               TO WS-PAGE-COUNT.
           MOVE WS-PAGE-COUNT  TO H1-PAGE

           WRITE PRINT-REC FROM HDG1 AFTER ADVANCING PAGE
           WRITE PRINT-REC FROM HDG2 AFTER ADVANCING 1 LINE.
           WRITE PRINT-REC FROM HDG3 AFTER ADVANCING 2 LINE.
           WRITE PRINT-REC FROM HDG4 AFTER ADVANCING 1 LINES.
           MOVE 5                  TO WS-LINE-COUNT.
```

#### ↳ Re: Help Please!

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-12-05T02:19:51+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sr6tuuguq25l46idncsueb65q1asap669b@4ax.com>`
- **References:** `<GjfH9.40728$lj.837513@read1.cgocable.net>`

```
On Tue, 3 Dec 2002 23:19:29 -0500 "Dan J" <dali@cogeco.ca> wrote:

:>"Dan J" <dali@cogeco.ca> wrote in message news:...
:>> I'm a student. I've got 6 comliation errors that I can not solve for the
:>> life of me. Can anybody help? Please, Please!!!

What are the errors.

How did you try to solve them?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
