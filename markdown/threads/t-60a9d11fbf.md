[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# *Code for sequential updates

_4 messages · 3 participants · 1999-11_

---

### *Code for sequential updates

- **From:** Bill <dc606@my-deja.com>
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8192bp$910$1@nnrp1.deja.com>`

```
I am struggling with figuring out code for sequential updates. Can I see
some examples?

Thanks


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: *Code for sequential updates

- **From:** dxmixxer@netdirect.net (Doug Miller)
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8194or$bk_001@news.netdirect.net>`
- **References:** `<8192bp$910$1@nnrp1.deja.com>`

```
In article <8192bp$910$1@nnrp1.deja.com>, Bill <dc606@my-deja.com> wrote:
+I am struggling with figuring out code for sequential updates. Can I see
+some examples?
+
I'll bet your textbook has some.

Post what you have tried so far, and many people here will be happy to help 
you out. But don't expect us to do your homework for you.
```

##### ↳ ↳ Re: *Code for sequential updates

- **From:** Bill <dc606@my-deja.com>
- **Date:** 1999-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<819cgv$fjr$1@nnrp1.deja.com>`
- **References:** `<8192bp$910$1@nnrp1.deja.com> <8194or$bk_001@news.netdirect.net>`

```
My text book has an example for a NONsequential update.

1.Do I use the
same statements for a SEQUENTIAL lookup, i.e. VALID KEY, NOT VALID KEY?

2.   I didn't define Record key as numeric because I am not doing any
calculations with it.  Should it be numeric for updates though?

3.    Is there any way I can view an index file that I created.  When I
try to view it in Notepad, it is one big long line.


Thank you
***********************************************************************
ERRORS
LINE	171
A:\3BB.CBL                                                       �000171
027: * 368-S Exception phrase inappropriate

.
LINE 175
A:\3BB.CBL                                                       �000175
019: * 564-S A scope-delimiter did not have a matching verb and was
discarded.


LINE 208
A:\3BB.CBL                                                        000208
017: * 564-S A scope-delimiter did not have a matching verb and was
discarded.


LINE 214
A:\3BB.CBL                                                        000214
034: *  34-S Operand WS-TRANS-RECORD should be numeric


LINES 230-232
A:\3BB.CBL                                                       �000230
038: * 330-S Not a record name
A:\3BB.CBL                                                        000231
040: * 330-S Not a record name
A:\3BB.CBL                                                        000232
028: * 330-S Not a record name


LINES 238-240
A:\3BB.CBL                                                        000238
038: * 330-S Not a record name
A:\3BB.CBL                                                        000239
040: * 330-S Not a record name
A:\3BB.CBL                                                        000240
032: * 330-S Not a record name

LINES 245-247
A:\3BB.CBL                                                        000245
038: * 330-S Not a record name
A:\3BB.CBL                                                       �000246
040: * 330-S Not a record name
A:\3BB.CBL                                                        000247
031: * 330-S Not a record name
A:\3BB.CBL                                                       �000255
032: * 348-S Procedure name

LINE 177
400-APPLY-TRANS-TO-MASTER undeclared, line 155 (first usage)

************************************************************************
      ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

           SELECT TRANSACTION-FILE ASSIGN TO 'A:\TRANS.DAT'
               ORGANIZATION IS LINE SEQUENTIAL.

           SELECT INDEXED-FILE ASSIGN TO 'A:\VALIDX.DAT'
               ORGANIZATION IS INDEXED
               ACCESS IS SEQUENTIAL
               RECORD KEY IS IND-SOC-SEC-NUM.

           SELECT ERROR-FILE ASSIGN TO 'A:\ERROR.DAT'
               ORGANIZATION IS LINE SEQUENTIAL.



       DATA DIVISION.
       FILE SECTION.

       FD  TRANSACTION-FILE
           RECORD CONTAINS 46 CHARACTERS
           DATA RECORD IS TRANSACTION-RECORD.
           01  TRANSACTION-RECORD      PIC X(47).


       FD  INDEXED-FILE
           RECORD CONTAINS 47 CHARACTERS
           DATA RECORD IS INDEXED-RECORD.
       01  INDEXED-RECORD.
           05 IND-SOC-SEC-NUM          PIC X(9).
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
           05 INDEXED-STATUS-BYTES     PIC X.


       01  HEADING-ERROR-LINE-ONE.
       05  FILLER                      PIC X(26) VALUE SPACES.

       05  FILLER                      PIC X(25)
           VALUE 'MASTER FILE UPDATE REPORT'.


       01  HEADING-ERROR-LINE-TWO.
       05  FILLER                      PIC X(13)
           VALUE 'SOC. SEC. NO.'.

       05  FILLER                      PIC X(4) VALUE SPACES.

       05  FILLER                      PIC X(10)
           VALUE 'TRANS CODE'.

       05  FILLER                      PIC X(2) VALUE SPACES.

       05  FILLER                      PIC X(13)
           VALUE 'ERROR MESSAGE'.


       01  ERROR-LINE.
           05 ERR-SOC-SEC              PIC X(9).
           05 FILLER                   PIC X(2).

           05 ERR-TRANS-CODE           PIC X(1).
           05 FILLER                   PIC X(2).

           05 ERROR-MESSAGE            PIC X(32).
           05 FILLER                   PIC X(2).


  PROCEDURE DIVISION.
       100-PROCESS-TRANSACTION-FILE.
           OPEN INPUT TRANSACTION-FILE
                I-O INDEXED-FILE
                ERROR-FILE.
           PERFORM 200-WRITE-ERROR-HEADINGS.

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
                 INDEXED-FILE.
           STOP RUN.

       200-WRITE-ERROR-HEADINGS.
           MOVE HEADING-ERROR-LINE-ONE TO ERROR-RECORD.
           WRITE ERROR-RECORD.
           MOVE HEADING-ERROR-LINE-TWO TO ERROR-RECORD.
           WRITE ERROR-RECORD.

       300-READ-INDEXED-FILE.
           MOVE TR-SOC-SEC-NUMBER TO IND-SOC-SEC-NUM.
           READ INDEXED-FILE INTO WS-MASTER-RECORD
               INVALID KEY
                   MOVE 'NO' TO RECORD-KEY-ALLOCATED-SWITCH
               NOT INVALID KEY
                   MOVE 'YES' TO RECORD-KEY-ALLOCATED-SWITCH
           END-READ.

       400-APPLY-TRANS-T0-MASTER.
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
               PERFORM 800-WRITE-ADD-MSG-LINE
           ELSE
               MOVE SPACES TO WS-MASTER-RECORD
               MOVE TR-SOC-SEC-NUMBER TO MA-SOC-SEC-NUMBER
               MOVE TR-NAME-AND-INITIALS TO MA-NAME-AND-INITIALS
               MOVE TR-BIRTH-DATE TO MA-BIRTH-DATE.
               MOVE TR-LOCATION-CODE TO MA-LOCATION-CODE
               MOVE TR-EDUCATION-CODE TO MA-EDUCATION-CODE
               MOVE TR-TITLE-DATA TO MA-TITLE-DATA
               MOVE TR-RATING TO MA-RATING
               MOVE TR-SALARY TO MA-SALARY
               WRITE INDEXED-RECORD FROM WS-MASTER-RECORD
           END-IF.



       600-CORRECT-EXISTING-RECORD.
           IF RECORD-KEY-ALLOCATED-SWITCH = 'YES'
               ADD WS-TRANS-RECORD TO WS-MASTER-RECORD
               REWRITE INDEXED-RECORD FROM WS-MASTER-RECORD
           ELSE
               PERFORM 900-WRITE-CORRECT-MSG-LINE
           END-IF.


       700-DELETE-EXISTING-RECORD.
           IF RECORD-KEY-ALLOCATED-SWITCH= 'YES'
               DELETE INDEXED-FILE
           ELSE
               PERFORM 1000-WRITE-DELETE-MSG-LINE
           END-IF.


       800-WRITE-ADD-MSG-LINE.
               WRITE TR-SOC-SEC-NUMBER TO ERR-SOC-SEC.
               WRITE TR-TRANSACTION-CODE TO ERR-TRANS-CODE.
               WRITE ADD-MSG TO ERROR-MESSAGE.
               MOVE ERROR-LINE TO ERROR-RECORD.
               WRITE ERROR-RECORD.


       900-WRITE-CORRECT-MSG-LINE.
               WRITE TR-SOC-SEC-NUMBER TO ERR-SOC-SEC.
               WRITE TR-TRANSACTION-CODE TO ERR-TRANS-CODE.
               WRITE CORRECT-MSG TO ERROR-MESSAGE.
               MOVE ERROR-LINE TO ERROR-RECORD.
               WRITE ERROR-RECORD.

       1000-WRITE-DELETE-MSG-LINE.
               WRITE TR-SOC-SEC-NUMBER TO ERR-SOC-SEC.
               WRITE TR-TRANSACTION-CODE TO ERR-TRANS-CODE.
               WRITE DELETE-MSG TO ERROR-MESSAGE.
               MOVE ERROR-LINE TO ERROR-RECORD.
               WRITE ERROR-RECORD.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: *Code for sequential updates

- **From:** "ChrisOsborne" <chris_n_osborne@msn.com>
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ejwrKMRN$GA.211@cpmsnbbsa03>`
- **References:** `<8192bp$910$1@nnrp1.deja.com> <8194or$bk_001@news.netdirect.net> <819cgv$fjr$1@nnrp1.deja.com>`

```
There are sequential and non-sequential updates of indexed files, and
sequential updates of non-indexed files.

If you are doing a SEQUENTIAL update of an indexed file (say VSAM on an MVS
platform) I'd define it as . . .

ORGANIZATION IS INDEXED and
ACCESS IS SEQUENTIAL

. . . and use ordinary READS and WRITES to do my updates, with no VALID KEY
or NOT VALID KEY.
You could use ACCESS IS RANDOM and VALID KEY and NOT VALID KEY, however, at
least on an MVS platform, even with 200 index and 200 data buffers
specified, randomly processing your way through each record of a VSAM
dataset takes a long, long time.  ACCESS IS SEQUENTIAL and normal READS
(with AT END and NOT AT END) and WRITES are much better.

And I'll ask again:

What platform?
What compiler?
What type of source file?
What type of target file?
What does your code look like?
What errors are you getting (reprint them here)?
Are you just looking for an algorithm that does sequential updating?  Of
indexed or non-indexed files?
In-place updating, or creation of an entirely new file with deletion of the
old (or GDG processing for MVS and related environments)?

What?



Bill <dc606@my-deja.com> wrote in message
news:819cgv$fjr$1@nnrp1.deja.com...
> My text book has an example for a NONsequential update.
>
…[312 more quoted lines elided]…
> Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
