[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help!

_11 messages · 4 participants · 2002-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help!

- **From:** "Dan J" <dali@cogeco.ca>
- **Date:** 2002-12-04T12:06:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GvqH9.32785$L47.3775200@read2.cgocable.net>`

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

#### ↳ Re: Help!

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-12-05T08:12:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<25Ccneb6Wekxw3KgXTWcpw@giganews.com>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net>`

```

"Dan J" <dali@cogeco.ca> wrote in message
news:GvqH9.32785$L47.3775200@read2.cgocable.net...
>
> "Dan J" <dali@cogeco.ca> wrote in message news:...
…[346 more quoted lines elided]…
>            MOVE 5                  TO WS-LINE-COUNT.

It would help if you told us what these compiler errors were!

I bet if you fix the first two errors - having to do with redefinition of
your tables - the rest would go away.

Here's a hint: Add up the bytes in a table. Add up the bytes in the
redefinition of that table. They should be (except for very advanced
techniques) the same. Yours are not.

Also, you can lose the RECORD CONTAINS and DATA RECORD IS clauses. They're
comments.
```

##### ↳ ↳ Re: Help!

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-05T16:02:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212051602.2770b083@posting.google.com>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> I bet if you fix the first two errors - having to do with redefinition of
> your tables - the rest would go away.
…[3 more quoted lines elided]…
> techniques) the same. Yours are not.

One table has an obvious missing line of data, the other adds up correctly.

Neither will generate an error, nor will 'fixing' this make other errors go away.
```

###### ↳ ↳ ↳ Re: Help!

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-12-05T21:55:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MmmdnQePH9wygm2gXTWcrg@giganews.com>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com> <217e491a.0212051602.2770b083@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0212051602.2770b083@posting.google.com...
> "JerryMouse" <nospam@bisusa.com> wrote
>
> > I bet if you fix the first two errors - having to do with redefinition
of
> > your tables - the rest would go away.
> >
…[4 more quoted lines elided]…
> One table has an obvious missing line of data, the other adds up
correctly.
>
> Neither will generate an error, nor will 'fixing' this make other errors
go away.

>        01  RATE-TABLES.
>            05  TAB-RATE-DATA.
…[11 more quoted lines elided]…
>                10 TAB-RATE         PIC 9V99.

Generates an error.
```

###### ↳ ↳ ↳ Re: Help!

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-06T18:20:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF0EA72.BD177AA8@Azonic.co.nz>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com> <217e491a.0212051602.2770b083@posting.google.com> <MmmdnQePH9wygm2gXTWcrg@giganews.com>`

```
JerryMouse wrote:
 
> >        01  RATE-TABLES.
> >            05  TAB-RATE-DATA.
…[13 more quoted lines elided]…
> Generates an error.

'Generating an error' depends on compiler used and options selected.  It
may well generate an error on your system, but you are stating it as if
it were an absolute.

It need not generate an error with my compilers.
```

###### ↳ ↳ ↳ Re: Help!

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-12-06T12:09:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<69-cnYZGsJZRem2gXTWcoQ@giganews.com>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com> <217e491a.0212051602.2770b083@posting.google.com> <MmmdnQePH9wygm2gXTWcrg@giganews.com> <3DF0EA72.BD177AA8@Azonic.co.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3DF0EA72.BD177AA8@Azonic.co.nz...
> JerryMouse wrote:
>
…[21 more quoted lines elided]…
> It need not generate an error with my compilers.

Then you got shit for compilers.
```

###### ↳ ↳ ↳ Re: Help!

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-06T12:47:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<asqrb9$9g2$1@slb9.atl.mindspring.net>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com> <217e491a.0212051602.2770b083@posting.google.com> <MmmdnQePH9wygm2gXTWcrg@giganews.com> <3DF0EA72.BD177AA8@Azonic.co.nz> <69-cnYZGsJZRem2gXTWcoQ@giganews.com>`

```
Jerry,
  I don't quite agree with you on this one.

I think that it is entirely "reasonable" for a compiler to REQUIRE (as the
ANSI/ISO Standards do, have, and probably always will) that the LARGEST
"variation" of redefined storage be defined first.

There is no problem (in any ANSI/ISO conforming compiler) with putting the
largest variation first and redefining it as SMALLER variations - but if you
put a smaller one first, you aren't really "redefining" existing storage -
but allocating MORE storage and redefining it.  Certainly a compiler COULD
be "forced to" (and I know some do) "read ahead" to find the largest
redefinition in a series of redefinitions, but the COBOL "standard" language
definition is explicitly set up to insure that this isn't REQUIRED.
```

###### ↳ ↳ ↳ Re: Help!

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-07T09:08:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DF1BAA6.6089B86@Azonic.co.nz>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com> <217e491a.0212051602.2770b083@posting.google.com> <MmmdnQePH9wygm2gXTWcrg@giganews.com> <3DF0EA72.BD177AA8@Azonic.co.nz> <69-cnYZGsJZRem2gXTWcoQ@giganews.com> <asqrb9$9g2$1@slb9.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> Certainly a compiler COULD
> be "forced to" (and I know some do) "read ahead" to find the largest
> redefinition in a series of redefinitions, 

It doesn't need to 'read ahead'.  It only needs to keep a total size
which is updated if required as it proceeds.  It only needs to commit
this size when it meets a new area that is not a redefinition, at which
point there cannot be a further redefines that could change it.

Whether it is sensible or not to allow larger sizes to redefine depends
on what the areas are used for.
```

###### ↳ ↳ ↳ Re: Help!

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-06T14:18:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<asr0nj$u1q$1@slb9.atl.mindspring.net>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com> <217e491a.0212051602.2770b083@posting.google.com> <MmmdnQePH9wygm2gXTWcrg@giganews.com> <3DF0EA72.BD177AA8@Azonic.co.nz> <69-cnYZGsJZRem2gXTWcoQ@giganews.com> <asqrb9$9g2$1@slb9.atl.mindspring.net> <3DF1BAA6.6089B86@Azonic.co.nz>`

```
Can you give me an example of where it is "better" to put a smaller
definition before a larger one?  I am not saying that there aren't some, but
it seems to me (but that may because I am USED to this restriction) that
there is never a time that it is BETTER to put the smaller item first.

I think that everyone is agreed that you always CAN structure your data
definition with the largest first (as REDEFINES don't really "matter" what
order they appear in) - but I do think that there MAY be reasons why putting
one definition "first" is easier to maintain (without errors).
```

###### ↳ ↳ ↳ Re: Help!

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-07T14:58:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212071458.3d2f8b38@posting.google.com>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net> <25Ccneb6Wekxw3KgXTWcpw@giganews.com> <217e491a.0212051602.2770b083@posting.google.com> <MmmdnQePH9wygm2gXTWcrg@giganews.com> <3DF0EA72.BD177AA8@Azonic.co.nz> <69-cnYZGsJZRem2gXTWcoQ@giganews.com> <asqrb9$9g2$1@slb9.atl.mindspring.net> <3DF1BAA6.6089B86@Azonic.co.nz> <asr0nj$u1q$1@slb9.atl.mindspring.net>`

```
"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote 

> Can you give me an example of where it is "better" 

I don't think that I ever claimed that it was 'better' to do it any
specific way (in fact I am certain that I did not make any such
statement), I only said that it need not give an error and may, or may
not, be sensible.

> I think that everyone is agreed that you always CAN structure your data
> definition with the largest first (as REDEFINES don't really "matter" what
> order they appear in) - but I do think that there MAY be reasons why putting
> one definition "first" is easier to maintain (without errors).

Well, 'maintain' is the operative word.

In changing a program it may be that one particular redefinition may
become larger (where this is irrelevant to the other definitions). 
Would it then be 'better' to reorder the definitions just to make the
largest first ?  Or would this just be 'if you don't know what you are
doing, do it neatly' ?

Is it 'better' to define different record types under a variable
record FD in descending order of size ? or increasing record type ? or
in some order they may be expected in the file ?
```

#### ↳ Re: Help!

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-05T16:11:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212051611.57466627@posting.google.com>`
- **References:** `<GvqH9.32785$L47.3775200@read2.cgocable.net>`

```
"Dan J" <dali@cogeco.ca> wrote

>            IF WS-MORE-RECORDS = "YES"
>            NEXT SENTENCE.

You are being taught to use an obsolete version of the language that
was superceeded [probably] before you were born.

Apart from 'NEXT SENTENCE' being incompatible with modern techniques
it is also pointless in this particular case.

>            IF SR-DEPT-NUMBER = DEPT-NUMBER (SUB-DEPT-NAME)
>            MOVE DEPT-NAME (SUB-DEPT-NAME) TO DTL-DEPT-NAME
…[3 more quoted lines elided]…
>            NEXT SENTENCE.

You should learn to indent, it makes the code easier to see what is
supposed to happen.  The 'ELSE NEXT SENTENCE' is redundant (as well as
being archaic usage).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
