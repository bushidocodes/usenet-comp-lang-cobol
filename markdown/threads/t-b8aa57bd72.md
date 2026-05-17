[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sort-input & output procedure-RM/85 v2.00+

_6 messages · 6 participants · 1996-10_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Sort-input & output procedure-RM/85 v2.00+

- **From:** "m..." <ua-author-467978@usenetarchives.gap>
- **Date:** 1996-10-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32743ac1.6121281@news.mindspring.com>`

```

Hello. I'm having a problem with this program. It has no errors in it,
yet when I run it, I get an error message telling me that a RELEASE or
RETURN statement was attempted and no sort or merge was active in line
195. The object of the sort is that I wish to sort after the
calculations and to sort the report in order by territory, and within
territory, by take home pay.
T.I.A., I racked my brain for hours...
Guy Woodard, Essex Community College
(m.··.@min··g.com)

IDENTIFICATION DIVISION.
PROGRAM-ID. PROGRAM3.
AUTHOR. GUY WOODARD.
*
ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT PAYROLL-DATA-IN ASSIGN TO DISK 'A:¥DATA¥PAYROLL.DAT'
ORGANIZATION IS LINE SEQUENTIAL.
SELECT TAX-TABLE-FILE ASSIGN TO DISK 'A:¥DATA¥TAX.DAT'.
SELECT SORT-FILE ASSIGN TO DISK 'A:¥SORT.DAT'.
SELECT PAYROLL-DATA-OUT ASSIGN TO DISK 'A:¥OUT.TXT'.
DATA DIVISION.
FILE SECTION.
FD PAYROLL-DATA-IN
LABEL RECORDS ARE STANDARD.
01 INPUT-REC.
05 FILLER PIC X(5).
05 IN-NAME PIC X(20).
05 IN-TERR PIC 99.
05 FILLER PIC 99.
05 IN-SALARY PIC 9(6).
05 FILLER PIC 9(9).
05 IN-DEP PIC 99.
FD TAX-TABLE-FILE
LABEL RECORDS ARE STANDARD.
01 TAX-REC.
05 T-TAX-INC PIC 9(5).
05 T-FED-RATE PIC V999.
05 T-STATE-RATE PIC V999.
SD SORT-FILE
RECORD CONTAINS 80 CHARACTERS.
01 SORT-REC.
05 FILLER PIC X(5).
05 SO-NAME PIC X(20).
05 SO-TERR PIC 99.
05 FILLER PIC 99.
05 SO-SALARY PIC 9(6).
05 FILLER PIC 9(9).
05 SO-DEP PIC 99.
05 SO-ATAKE-HOME PIC 999999.
FD PAYROLL-DATA-OUT
LABEL RECORDS ARE OMITTED.
01 OUT-REC PIC X(132).
WORKING-STORAGE SECTION.
01 STORED-AREAS.
05 WS-DEP PIC 99 VALUE ZERO.
05 WS-SALARY PIC 999999 VALUE ZERO.
05 WS-DEP-DED PIC 99999 VALUE ZERO.
05 WS-TAX-INC PIC 999999 VALUE ZERO.
05 WS-FICA-AMT PIC 99999 VALUE ZERO.
05 WS-ATAKE-HOME PIC 999999 VALUE ZERO.
05 WS-MTAKE-HOME PIC 999999 VALUE ZERO.
05 WS-FED-TAX PIC 999999 VALUE ZERO.
05 WS-STATE-TAX PIC 999999 VALUE ZERO.
05 WS-FED-RATE PIC V999 VALUE ZERO.
05 WS-STATE-RATE PIC V999 VALUE ZERO.
01 CONS-AREA.
05 ARE-THERE-MORE-RECORDS PIC X(3) VALUE 'YES'.
88 NO-RECORDS VALUE 'NO '.
05 WS-STD-DED PIC 9999 VALUE 1000.
01 TAX-TABLE.
05 TAX-ENTRIES OCCURS 6 TIMES
ASCENDING KEY TAX-INC
INDEXED BY TAX-IND.
10 TAX-INC PIC 9(5).
10 FED-RATE PIC V999.
10 STATE-RATE PIC V999.
01 HDG-LINE-1.
05 FILLER PIC X(29) VALUE SPACES.
05 FILLER PIC X(16) VALUE 'Employee
Listing'.
05 FILLER PIC X(14) VALUE SPACES.
05 FILLER PIC X(11) VALUE 'Guy Woodard'.
01 HDG-LINE-2.
05 FILLER PIC X(47) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Annual'.
05 FILLER PIC X(6) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Annual'.
05 FILLER PIC X(17) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Annual'.
05 FILLER PIC X(6) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Annual'.
05 FILLER PIC X(6) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Annual'.
05 FILLER PIC X(6) VALUE SPACES.
05 FILLER PIC X(7) VALUE 'Monthly'.
01 HDG-LINE-3.
05 FILLER PIC X(25) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Annual'.
05 FILLER PIC X(14) VALUE SPACES.
05 FILLER PIC X(10) VALUE 'Dependents'.
05 FILLER PIC X(4) VALUE SPACES.
05 FILLER PIC X(7) VALUE 'Taxable'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Annual'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(5) VALUE 'State'.
05 FILLER PIC X(6) VALUE SPACES.
05 FILLER PIC X(7) VALUE 'Federal'.
05 FILLER PIC X(7) VALUE SPACES.
05 FILLER PIC X(3) VALUE 'Net'.
05 FILLER PIC X(9) VALUE SPACES.
05 FILLER PIC X(3) VALUE 'Net'.
01 HDG-LINE-4.
05 FILLER PIC X(8) VALUE SPACES.
05 FILLER PIC X(4) VALUE 'Name'.
05 FILLER PIC X(13) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Salary'.
05 FILLER PIC X(2) VALUE SPACES.
05 FILLER PIC X(10) VALUE 'Dependents'.
05 FILLER PIC X(2) VALUE SPACES.
05 FILLER PIC X(9) VALUE 'Deduction'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(6) VALUE 'Income'.
05 FILLER PIC X(7) VALUE SPACES.
05 FILLER PIC X(4) VALUE 'FICA'.
05 FILLER PIC X(7) VALUE SPACES.
05 FILLER PIC X(3) VALUE 'Tax'.
05 FILLER PIC X(10) VALUE SPACES.
05 FILLER PIC X(3) VALUE 'Tax'.
05 FILLER PIC X(9) VALUE SPACES.
05 FILLER PIC X(3) VALUE 'Pay'.
05 FILLER PIC X(9) VALUE SPACES.
05 FILLER PIC X(3) VALUE 'Pay'.
01 DETAIL-LINE.
05 OUT-NAME PIC X(20).
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-ANN-SALARY PIC ZZZ,ZZ9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-DEP PIC Z9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-DEP-DED PIC ZZZ,ZZ9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-TAX-INC PIC ZZZ,ZZ9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-FICA PIC ZZ,ZZ9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-ST-TAX PIC ZZZ,ZZ9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-FED-TAX PIC ZZZ,ZZ9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-ATAKE-HOME PIC ZZZ,ZZ9.
05 FILLER PIC X(5) VALUE SPACES.
05 OUT-MTAKE-HOME PIC ZZZ,ZZ9.
*
PROCEDURE DIVISION.
100-MAIN.
OPEN INPUT PAYROLL-DATA-IN
TAX-TABLE-FILE.
MOVE 'YES' TO ARE-THERE-MORE-RECORDS.
PERFORM VARYING TAX-IND FROM 1 BY 1
UNTIL NO-RECORDS
READ TAX-TABLE-FILE
AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS
END-READ
MOVE TAX-REC TO TAX-ENTRIES (TAX-IND)
END-PERFORM.
MOVE ZEROES TO STORED-AREAS.
READ PAYROLL-DATA-IN
AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS.
PERFORM 200-CALC-RTN.
PERFORM 300-MOV-IN-RTN.
PERFORM 400-SRT-RTN.
CLOSE PAYROLL-DATA-IN
TAX-TABLE-FILE.
200-CALC-RTN.
MOVE IN-DEP TO WS-DEP.
MOVE IN-SALARY TO WS-SALARY.
COMPUTE WS-DEP-DED = 2000 * WS-DEP.
COMPUTE WS-TAX-INC = WS-SALARY - WS-STD-DED - WS-DEP-DED.
IF WS-SALARY < 57600
COMPUTE WS-FICA-AMT = 0.0765 * WS-SALARY
ELSE
COMPUTE WS-FICA-AMT = 0.0765 * 57600
END-IF.
SET TAX-IND TO 1.
SEARCH TAX-ENTRIES
AT END MOVE ZEROES TO WS-ATAKE-HOME
MOVE ZEROES TO WS-MTAKE-HOME
WHEN WS-SALARY >= TAX-INC (TAX-IND)
MOVE FED-RATE (TAX-IND) TO WS-FED-RATE
MOVE STATE-RATE (TAX-IND) TO WS-STATE-RATE
END-SEARCH.
COMPUTE WS-STATE-TAX = WS-SALARY * WS-STATE-RATE.
COMPUTE WS-FED-TAX = WS-SALARY * WS-FED-RATE.
COMPUTE WS-ATAKE-HOME = WS-SALARY -
(WS-STATE-TAX + WS-FED-TAX + WS-FICA-AMT).
COMPUTE WS-MTAKE-HOME = WS-ATAKE-HOME / 12.
300-MOV-IN-RTN.
MOVE IN-NAME TO SO-NAME.
MOVE IN-TERR TO SO-TERR.
MOVE IN-SALARY TO SO-SALARY.
MOVE IN-DEP TO SO-DEP.
MOVE WS-ATAKE-HOME TO SO-ATAKE-HOME.
Line 195-->RELEASE SORT-REC.
READ PAYROLL-DATA-IN
AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS.
400-SRT-RTN.
SORT SORT-FILE
ASCENDING KEY SO-TERR
ASCENDING KEY SO-ATAKE-HOME
INPUT PROCEDURE IS 300-MOV-IN-RTN
OUTPUT PROCEDURE IS 500-OUT-RTN.
500-OUT-RTN.
OPEN OUTPUT PAYROLL-DATA-OUT.
WRITE OUT-REC FROM HDG-LINE-1.
WRITE OUT-REC FROM HDG-LINE-2 AFTER ADVANCING 2 LINES.
WRITE OUT-REC FROM HDG-LINE-3 AFTER ADVANCING 1 LINE.
WRITE OUT-REC FROM HDG-LINE-4 AFTER ADVANCING 1 LINE.
MOVE 'YES' TO ARE-THERE-MORE-RECORDS.
PERFORM 600-MOV-OUT-RTN
UNTIL NO-RECORDS.
CLOSE PAYROLL-DATA-OUT.
600-MOV-OUT-RTN.
MOVE SO-NAME TO OUT-NAME.
MOVE SO-SALARY TO OUT-ANN-SALARY.
MOVE SO-DEP TO OUT-DEP.
MOVE WS-DEP-DED TO OUT-DEP-DED.
MOVE WS-TAX-INC TO OUT-TAX-INC.
MOVE WS-FICA-AMT TO OUT-FICA.
MOVE WS-STATE-TAX TO OUT-ST-TAX.
MOVE WS-FED-TAX TO OUT-FED-TAX.
MOVE SO-ATAKE-HOME TO OUT-ATAKE-HOME.
MOVE WS-MTAKE-HOME TO OUT-MTAKE-HOME.
WRITE OUT-REC FROM SORT-REC.
RETURN SORT-FILE
AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS
END-RETURN.
```

#### ↳ Re: Sort-input & output procedure-RM/85 v2.00+

- **From:** "spam.f..." <ua-author-17086140@usenetarchives.gap>
- **Date:** 1996-10-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8aa57bd72-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32743ac1.6121281@news.mindspring.com>`
- **References:** `<32743ac1.6121281@news.mindspring.com>`

```

m.··.@min··g.com (Guy J. Woodard, Jr.) wrote:
› Hello. I'm having a problem with this program. It has no errors in it,

Well, no *compile* errors anyway. Obviously, there's at least *one*
error in it or you wouldn't get the run-time diagnostic. :-)

› yet when I run it, I get an error message telling me that a RELEASE or
› RETURN statement was attempted and no sort or merge was active in line
…[26 more quoted lines elided]…
›           PERFORM 200-CALC-RTN.
 
› Problem is right here...
›           PERFORM 300-MOV-IN-RTN.
In 400-SRT-RTN, you have specified 300-MOV-IN-RTN as your input procedure.
Therefore, it should not be PERFORMed here. RELEASE and RETURN are
indeed valid only within the scope of a SORT verb. By performing this paragraph
before invoking the SORT verb, you attempt to RELEASE outside the scope
of a SORT, hence the error message.

BTW, there are some other logic errors in the program.
Hint: look more closely at your output procedure.

› PERFORM 400-SRT-RTN.
› CLOSE PAYROLL-DATA-IN
› TAX-TABLE-FILE.


Doug Miller
dlm··.@ine··t.net ('from' field rigged to foil e-mail spammers)
views expressed are mine and not those of
Hospital Health Plan Corp. "all health care is local"
```

#### ↳ Re: Sort-input & output procedure-RM/85 v2.00+

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1996-10-27T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8aa57bd72-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32743ac1.6121281@news.mindspring.com>`
- **References:** `<32743ac1.6121281@news.mindspring.com>`

```

In article <327··.@new··g.com>,
m.··.@min··g.com (Guy J. Woodard, Jr.) wrote:
› 
›     PROCEDURE DIVISION.
…[12 more quoted lines elided]…
›              AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS.
 
› This statement is not in a loop and it reads only one record.
 
 
›         PERFORM 200-CALC-RTN.
›         PERFORM 300-MOV-IN-RTN.
›         PERFORM 400-SRT-RTN.
›         CLOSE PAYROLL-DATA-IN
›               TAX-TABLE-FILE.

The proximate cause of the error you reported is the absence of a STOP
RUN statement here to prevent control from falling through into the
subroutines.

› 200-CALC-RTN.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

##### ↳ ↳ Re: Sort-input & output procedure-RM/85 v2.00+

- **From:** "dlmi..." <ua-author-1050936@usenetarchives.gap>
- **Date:** 1996-10-28T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8aa57bd72-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b8aa57bd72-p3@usenetarchives.gap>`
- **References:** `<32743ac1.6121281@news.mindspring.com> <gap-b8aa57bd72-p3@usenetarchives.gap>`

```

cwe··.@gia··t.com (Chris Westbury) wrote:
+In article <327··.@new··g.com>,
+m.··.@min··g.com (Guy J. Woodard, Jr.) wrote:
+>
+> PROCEDURE DIVISION.
+> 100-MAIN.
+> OPEN INPUT PAYROLL-DATA-IN
+> TAX-TABLE-FILE.
+> MOVE 'YES' TO ARE-THERE-MORE-RECORDS.
+> PERFORM VARYING TAX-IND FROM 1 BY 1 UNTIL NO-RECORDS
+> READ TAX-TABLE-FILE
+> AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS
+> END-READ
+> MOVE TAX-REC TO TAX-ENTRIES (TAX-IND)
+> END-PERFORM.
+> MOVE ZEROES TO STORED-AREAS.
+> READ PAYROLL-DATA-IN
+> AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS.
+
+This statement is not in a loop and it reads only one record.
+
+
+> PERFORM 200-CALC-RTN.
+> PERFORM 300-MOV-IN-RTN.
+> PERFORM 400-SRT-RTN.
+> CLOSE PAYROLL-DATA-IN
+> TAX-TABLE-FILE.
+
+The proximate cause of the error you reported is the absence of a STOP
+RUN statement here to prevent control from falling through into the
+subroutines.

No, it's not, although that will cause problems too. The proximate cause of
the error he reported is that he performs his input procedure (300-mov-in-rtn)
before executing the sort verb in 400-srt-rtn.

+
+> 200-CALC-RTN.
+
+
+--
+Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: Sort-input & output procedure-RM/85 v2.00+

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1996-10-28T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8aa57bd72-p5@usenetarchives.gap>`
- **In-Reply-To:** `<32743ac1.6121281@news.mindspring.com>`
- **References:** `<32743ac1.6121281@news.mindspring.com>`

```

m.··.@min··g.com (Guy J. Woodard, Jr.) wrote:

› Hello. I'm having a problem with this program. It has no errors in it,
› yet when I run it, I get an error message telling me that a RELEASE or
…[6 more quoted lines elided]…
› 			(m.··.@min··g.com)


Close but no sort.

Think of the sort verb a a producer and then a consumer of data
(release / return)

You must first envoke the sort indicating the production. You did
that AFTER the actual production....NO NO

SORT .....INPUT PROCEDURE .... OUTPUT PROCEDURE..


INPUT PROCEDURE
...READ....RELEASE

OUTPUT PROCEDURE
....RETURN.....WRITE

a little simple....but

JR
```

#### ↳ Re: Sort-input & output procedure-RM/85 v2.00+

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-10-28T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b8aa57bd72-p6@usenetarchives.gap>`
- **In-Reply-To:** `<32743ac1.6121281@news.mindspring.com>`
- **References:** `<32743ac1.6121281@news.mindspring.com>`

```

m.··.@min··g.com (Guy J. Woodard, Jr.) wrote:

› Hello. I'm having a problem with this program. It has no errors in it,
› yet when I run it, I get an error message telling me that a RELEASE or
…[6 more quoted lines elided]…
› 			(m.··.@min··g.com)
 
› IDENTIFICATION DIVISION.
›       PROGRAM-ID.   PROGRAM3.
…[8 more quoted lines elided]…
›           END-PERFORM.

This loop above will not process your last record correctly. I think
it should read as follows:

move 'yes' to are-there-more-records.
perform varying tax-ind from 1 by 1 until no-records
read tax-table-file
at end
move 'no' to are-there-more-records
not at end
move tax-rec to tax-entries (tax-ind)
end-read
end-perform.

›           MOVE ZEROES TO STORED-AREAS.
›           READ PAYROLL-DATA-IN
›                AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS.
›           PERFORM 200-CALC-RTN.
›           PERFORM 300-MOV-IN-RTN.

As Doug Miller pointed out, you should omit the previous line, because
300-move-in-rtn is the input procedure named in 400-srt-rtn.

› PERFORM 400-SRT-RTN.
› CLOSE PAYROLL-DATA-IN
› TAX-TABLE-FILE.

As someone else pointed out, you should place a STOP RUN statement
here.

›       200-CALC-RTN.
›           MOVE IN-DEP TO WS-DEP.
…[29 more quoted lines elided]…
›                AT END MOVE 'NO ' TO ARE-THERE-MORE-RECORDS.

Generally, when I use an internal sort, I make the input procedure
come farther down in the program than the routine which contains the
sort statement. Your way should still work, but I think it shows an
incorrect heirarchy.

›       400-SRT-RTN.
›           SORT SORT-FILE
…[10 more quoted lines elided]…
›           MOVE 'YES' TO ARE-THERE-MORE-RECORDS.
 
› Somewhere in here you need to RETURN the first record from the sort.
 
›           PERFORM 600-MOV-OUT-RTN
›                UNTIL NO-RECORDS.
…[15 more quoted lines elided]…
›           END-RETURN.

I haven't tried to test these suggestions, so take them with a grain
of salt. I hope they help!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
