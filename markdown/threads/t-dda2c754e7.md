[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol question, please help

_6 messages · 6 participants · 1998-02_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Cobol question, please help

- **From:** "xinhong jin" <ua-author-4740557@usenetarchives.gap>
- **Date:** 1998-02-16T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`

```

Greetings,

I'm new to this newsgroup and hope this is the appropriate place to
post my Cobol questions:

I've just compiled a Cobol program without any error messages. When I
was trying to execute the program after linking and setting
SYSIN/SYSOUT, I got the following error message:

"RCL0002: File status 35 on C:sales.dat Error detected at offset 0046
in segment 00 of program sales".

I then tried to use the Cobol compiler RED to search for error
messages, but it says "no more error messages". Could anybody tell me
what's the problem please? Any suggestions/comments would be greatly
appreciated. Thanks for your time.

Attached below is the original program:

ID DIVISION.
PROGRAM-ID. SALES-SUMMARY.
AUTHOR. WISE OLD PROGRAMMER.
SECURITY. FOR STORE MANAGERS ONLY.
REMARKS. THIS PROGRAM WILL:
A) READ THE DAILY SALES OF A HARDWARE STORE
B) PRINT THE VALUE, PST & GST OF EACH ITEM
C) PRINT THE TOTAL FOR EACH "RECORD TYPE"
RECORD CODE 11 = HARDWARE
RECORD CODE 15 = LUMBER
D) PRINT THE GRAND TOTAL FOR SALES, PST & GST

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL. SELECT DAILY-SALES
ASSIGN TO UT-S-SYSIN.
SELECT SALES-REPORT
ASSIGN TO UT-S-SYSOUT.

DATA DIVISION.
FILE SECTION.
FD DAILY-SALES
RECORD CONTAINS 41 CHARACTERS.
01 SALES-RECORD.
05 RECORD-CODE PIC 99.
05 FILLER PIC X.
05 PART-NUMBER.
10 ALPHA-CODE PIC XX.
10 NUM-CODE PIC 9(4).
05 FILLER PIC X.
05 PART-DESCRIPTION PIC X(20).
05 FILLER PIC X.
05 NUMBER-SOLD PIC 9999.
05 FILLER PIC X.
05 UNIT-PRICE PIC 999V99.

FD SALES-REPORT
RECORD CONTAINS 132 CHARACTERS.
01 PRINT-LINE PIC X(132).

WORKING-STORAGE SECTION.
01 END-OF-FILE PIC XXX VALUE SPACES.

01 TAXATION-RATES.
05 GST-RATE PIC 99V99 VALUE 0.07.
05 PST-RATE PIC 99V99 VALUE 0.08.

01 ITEM-BY-ITEM-CALCULATIONS.
05 SALES-COUNT-CALC PIC 9(6) VALUE ZEROS.
05 SALES-AMOUNT-CALC PIC 99999V99 VALUE ZEROS.
05 PST-AMOUNT-CALC PIC 99999V99 VALUE ZEROS.
05 GST-AMOUNT-CALC PIC 99999V99 VALUE ZEROS.

01 CODE11-TOTALS.
05 TOTAL-CODE11-COUNT PIC 9(6) VALUE ZEROS.
05 TOTAL-CODE11-AMOUNT PIC 99999V99 VALUE ZEROS.
05 TOTAL-CODE11-PST PIC 99999V99 VALUE ZEROS.
05 TOTAL-CODE11-GST PIC 99999V99 VALUE ZEROS.

01 CODE15-TOTALS.
05 TOTAL-CODE15-COUNT PIC 9(6) VALUE ZEROS.
05 TOTAL-CODE15-AMOUNT PIC 99999V99 VALUE ZEROS.
05 TOTAL-CODE15-PST PIC 99999V99 VALUE ZEROS.
05 TOTAL-CODE15-GST PIC 99999V99 VALUE ZEROS.

01 DAILY-SALES-TOTALS.
05 TOTAL-AA-COUNTER PIC 9(6) VALUE ZEROS.
05 TOTAL-RANGE-COUNTER PIC 9(6) VALUE ZEROS.
05 TOTAL-SALES-COUNT PIC 9(6) VALUE ZEROS.
05 TOTAL-SALES-AMOUNT PIC 99999V99 VALUE ZEROS.
05 TOTAL-PST-AMOUNT PIC 99999V99 VALUE ZEROS.
05 TOTAL-GST-AMOUNT PIC 99999V99 VALUE ZEROS.

01 HEADING-LINE-1.
05 FILLER PIC X(57) VALUE SPACES.
05 FILLER PIC X(18) VALUE 'DAILY SALES REPORT'.
05 FILLER PIC X(57) VALUE SPACES.

01 HEADING-LINE-2.
05 FILLER PIC X VALUE SPACES.
05 FILLER PIC X(11) VALUE 'PART NUMBER'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(11) VALUE 'DESCRIPTION'.
05 FILLER PIC X(11) VALUE SPACES.
05 FILLER PIC X(11) VALUE 'NUMBER SOLD'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(10) VALUE 'UNIT PRICE'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(10) VALUE 'PST AMOUNT'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(10) VALUE 'GST AMOUNT'.
05 FILLER PIC X(5) VALUE SPACES.
05 FILLER PIC X(10) VALUE 'TOTAL SALE'.
05 FILLER PIC X(22) VALUE SPACES.

01 DASH-LINE.
05 FILLER PIC X(43) VALUE SPACES.
05 FILLER PIC X(5) VALUE ALL '-'.
05 FILLER PIC X(23) VALUE SPACES.
05 FILLER PIC X(8) VALUE ALL '-'.
05 FILLER PIC X(7) VALUE SPACES.
05 FILLER PIC X(8) VALUE ALL '-'.
05 FILLER PIC X(7) VALUE SPACES.
05 FILLER PIC X(8) VALUE ALL '-'.
05 FILLER PIC X(23) VALUE SPACES.

01 DETAIL-LINE.
05 FILLER PIC X(5) VALUE SPACES.
05 STOCK-NUMBER PIC X(6).
05 FILLER PIC X(5) VALUE SPACES.
05 PART-DETAILS PIC X(20).
05 FILLER PIC X(7) VALUE SPACES.
05 UNITS-SOLD PIC ZZZ9.
05 FILLER PIC X(10) VALUE SPACES.
05 PRICE-PER-UNIT PIC 999.99.
05 FILLER PIC X(7) VALUE SPACES.
05 CALC-PST PIC 99999.99.
05 FILLER PIC X(7) VALUE SPACES.
05 CALC-GST PIC 99999.99.
05 FILLER PIC X(7) VALUE SPACES.
05 TOTAL-SALE-AMT PIC $$$$$$9.99.
05 FILLER PIC X(23) VALUE SPACES.

01 SUMMARY-LINE.
05 FILLER PIC X(17) VALUE SPACES.
05 TOTAL-LABEL PIC X(23).
05 FILLER PIC X(2) VALUE SPACES.
05 TOTAL-UNITS-SOLD PIC ZZZZZ9.
05 FILLER PIC X(22) VALUE SPACES.
05 GRAND-TOTAL-PST PIC $$$$$9.99.
05 FILLER PIC X(6) VALUE SPACES.
05 GRAND-TOTAL-GST PIC $$$$$9.99.
05 FILLER PIC X(6) VALUE SPACES.
05 GRAND-TOTAL-SALE PIC $$$$$9.99.
05 FILLER PIC X(23) VALUE SPACES.

01 ASSIGN1-LINE.
05 FILLER PIC X(10) VALUE SPACES.
05 LABEL1 PIC X(20)
VALUE 'ASSIGNMENT #1 LINE:'.
05 FILLER PIC X(5) VALUE SPACES.
05 LABEL2 PIC X(25)
VALUE 'COUNT OF AA-CODE ITEMS'.
05 OUTPUT-AA-COUNT PIC 9(6).
05 FILLER PIC X(5) VALUE SPACES.
05 LABEL3 PIC X(25)
VALUE 'COUNT OF PART NUMBERS'.
05 LABEL4 PIC X(25)
VALUE 'BETWEEN 3000 AND 3999'.
05 OUTPUT-RANGE PIC 9(6).
05 FILLER PIC X(5) VALUE SPACES.

PROCEDURE DIVISION.
*****************************************************
* MAIN LINE OF THE PROGRAM BEGINS HERE
******************************************************
CALCULATE-SALES.
OPEN INPUT DAILY-SALES
OUTPUT SALES-REPORT.
PERFORM WRITE-HEADING-LINE.
PERFORM READ-DAILY-SALES.
PERFORM PROCESS-SALES-RECORD
UNTIL END-OF-FILE = 'YES'.
PERFORM WRITE-SALES-TOTALS.
CLOSE DAILY-SALES
SALES-REPORT.
STOP RUN.

*******************************************************
* MODULES CALLED FROM MAINLINE PROGRAM
********************************************************

WRITE-HEADING-LINE.
MOVE HEADING-LINE-1 TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING PAGE.
MOVE HEADING-LINE-2 TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING 1 LINE.
MOVE SPACES TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING 1 LINE.
READ-DAILY-SALES.
READ DAILY-SALES
AT END MOVE 'YES' TO END-OF-FILE
END-READ.

PROCESS-SALES-RECORD.
PERFORM CALC-SALES-TOTALS.
PERFORM SUM-UP-DAILY-SALES-TOTALS
PERFORM WRITE-DETAIL-LINE.
PERFORM READ-DAILY-SALES.

CALC-SALES-TOTALS.
PERFORM CALCULATE-PST.
PERFORM CALCULATE-GST.
PERFORM CALCULATE-TOTAL-SALE.

CALCULATE-PST.
COMPUTE PST-AMOUNT-CALC =
NUMBER-SOLD * UNIT-PRICE * PST-RATE.

CALCULATE-GST.
COMPUTE GST-AMOUNT-CALC =
NUMBER-SOLD * UNIT-PRICE * GST-RATE.

CALCULATE-TOTAL-SALE.
COMPUTE SALES-COUNT-CALC = NUMBER-SOLD OF SALES-RECORD.
COMPUTE SALES-AMOUNT-CALC =
NUMBER-SOLD * UNIT-PRICE +
PST-AMOUNT-CALC +
GST-AMOUNT-CALC.

SUM-UP-DAILY-SALES-TOTALS.
ADD SALES-COUNT-CALC TO TOTAL-SALES-COUNT.
ADD SALES-AMOUNT-CALC TO TOTAL-SALES-AMOUNT.
ADD PST-AMOUNT-CALC TO TOTAL-PST-AMOUNT.
ADD GST-AMOUNT-CALC TO TOTAL-GST-AMOUNT.
IF RECORD-CODE = 11 PERFORM SUM-UP-CODE11.
IF RECORD-CODE = 15 PERFORM SUM-UP-CODE15.
IF ALPHA-CODE = 'AA'
ADD 1 TO TOTAL-AA-COUNTER
IF NUM-CODE >= 3000 AND NUM-CODE <= 3999
ADD 1 TO TOTAL-RANGE-COUNTER.

SUM-UP-CODE11.
ADD SALES-COUNT-CALC TO TOTAL-CODE11-COUNT.
ADD SALES-AMOUNT-CALC TO TOTAL-CODE11-AMOUNT.
ADD PST-AMOUNT-CALC TO TOTAL-CODE11-PST.
ADD GST-AMOUNT-CALC TO TOTAL-CODE11-GST.

SUM-UP-CODE15.
ADD SALES-COUNT-CALC TO TOTAL-CODE15-COUNT.
ADD SALES-AMOUNT-CALC TO TOTAL-CODE15-AMOUNT.
ADD PST-AMOUNT-CALC TO TOTAL-CODE15-PST.
ADD GST-AMOUNT-CALC TO TOTAL-CODE15-GST.

WRITE-DETAIL-LINE.
MOVE PART-NUMBER TO STOCK-NUMBER.
MOVE PART-DESCRIPTION TO PART-DETAILS.
MOVE NUMBER-SOLD TO UNITS-SOLD.
MOVE UNIT-PRICE TO PRICE-PER-UNIT.
MOVE PST-AMOUNT-CALC TO CALC-PST.
MOVE GST-AMOUNT-CALC TO CALC-GST.
MOVE SALES-AMOUNT-CALC TO TOTAL-SALE-AMT.
MOVE DETAIL-LINE TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING 1 LINE.

WRITE-SALES-TOTALS.
MOVE DASH-LINE TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING 1 LINE.

MOVE 'TOTAL:HARDWARE RECORDS' TO TOTAL-LABEL.
MOVE TOTAL-CODE11-COUNT TO TOTAL-UNITS-SOLD.
MOVE TOTAL-CODE11-PST TO GRAND-TOTAL-PST.
MOVE TOTAL-CODE11-GST TO GRAND-TOTAL-GST.
MOVE TOTAL-CODE11-AMOUNT TO GRAND-TOTAL-SALE.
MOVE SUMMARY-LINE TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING 2 LINES.

MOVE 'TOTAL:LUMBER RECORDS' TO TOTAL-LABEL.
MOVE TOTAL-CODE15-COUNT TO TOTAL-UNITS-SOLD.
MOVE TOTAL-CODE15-PST TO GRAND-TOTAL-PST.
MOVE TOTAL-CODE15-GST TO GRAND-TOTAL-GST.
MOVE TOTAL-CODE15-AMOUNT TO GRAND-TOTAL-SALE.
MOVE SUMMARY-LINE TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING 2 LINES.

MOVE ' ** GRAND TOTAL **' TO TOTAL-LABEL.
MOVE TOTAL-SALES-COUNT TO TOTAL-UNITS-SOLD.
MOVE TOTAL-PST-AMOUNT TO GRAND-TOTAL-PST.
MOVE TOTAL-GST-AMOUNT TO GRAND-TOTAL-GST.
MOVE TOTAL-SALES-AMOUNT TO GRAND-TOTAL-SALE.
MOVE SUMMARY-LINE TO PRINT-LINE.
WRITE PRINT-LINE
AFTER ADVANCING 2 LINES.

MOVE TOTAL-AA-COUNTER TO OUTPUT-AA-COUNT.
MOVE TOTAL-RANGE-COUNTER TO OUTPUT-RANGE.
MOVE ASSIGN1-LINE TO PRINT-LINE.
WRITE PRINT-LINE
AfTER ADVANCING 3 LINES.
```

#### ↳ Re: Cobol question, please help

- **From:** "michael dodas" <ua-author-6589016@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dda2c754e7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`
- **References:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`

```

Xinhong Jin wrote:
› 
› Greetings,
…[15 more quoted lines elided]…
› 

The CA-Realia run-time issuing the File Status 35 indicates the input
was not found.

Make sure you include the full path name for the file, for example:

Set SYSIN=C:\Pathname\Sales.dat


Mike Dodas

(Remove cutthejunk for e-mail replies)
```

#### ↳ Re: Cobol question, please help

- **From:** "helmut leininger" <ua-author-7651185@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dda2c754e7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`
- **References:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`

```



Xinhong Jin wrote:

› Greetings,
› 
…[9 more quoted lines elided]…
› 

...

Hi,

The error happens at the OPEN statement at the beginning of your PROCEDURE
DIVISION. File status 35 means you want to open a file in input or update
that is not present.
For your case it means that C:sales.dat does not exist (or cannot be
found). As you did not specify an absolute path you should verify the file
exists in your current directory.

Regards

Helmut Leininger
Bull AG Vienna
Unix Support
Email: Hel··.@bu··l.net
```

#### ↳ Re: Cobol question, please help

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dda2c754e7-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`
- **References:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`

```

Xinhong Jin wrote:
› 
› Greetings,
…[15 more quoted lines elided]…
› 

Xinhong,

On what platform you are working on and which compiler you are using?

Rgds,
Chip Ling
chi··.@sym··o.ca
```

#### ↳ Re: Cobol question, please help

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1998-02-18T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dda2c754e7-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`
- **References:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`

```

Xinhong Jin wrote:

snip>
› "RCL0002: File status 35 on C:sales.dat  Error detected at offset 0046
›  in segment 00 of program sales".
…[18 more quoted lines elided]…
› 

snip

you are confusing compile time errors with run time errors.

using RED you are looking at ascii text source/listing files.

you are using EXTERNAL names SYSIN and SYSOUT.......
what did you set them to?
the setting may not be matching your real file names

error 35 (run time) means FILE NOT FOUND.

jr

and stir with a Runcible spoon...
```

#### ↳ Re: Cobol question, please help

- **From:** "jerry peacock" <ua-author-36061@usenetarchives.gap>
- **Date:** 1998-02-18T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-dda2c754e7-p6@usenetarchives.gap>`
- **In-Reply-To:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`
- **References:** `<6cd394$kmf$1@bertrand.ccs.carleton.ca>`

```


If this is a REALIA COBOL compiler (clues: "RCL" error message, RED (Realia
Editor), the
problem is SELECT DAILY-SALES ASSIGN TO UT-S-SYSIN which the compiler
believes to
be an external name. You basically have three choices:
1. SELECT ... ASSIGN TO external-name
where external-name is defined at execution time via SET
external-name=C:\DIR1\FILE1
2. SELECT ... ASSIGN TO VARYING internal-name
where internal-name is defined in Working Storage as
01 internal-name PIC X(79) VALUE 'C:\DIR1\FILE1'
or
01 internal-name PIC X(79).
followed by
MOVE 'C:\DIR1\FILE1' TO internal-name.
3. SELECT ... ASSIGN TO literal
as in SELECT MY-FILE ASSIGN TO 'C:\DIR1\FILE1'

It gets a tad more complicated. As part of the file definition, REALIA
expects parameters
which define the physical file included in brackets at the end of the file
name. For example,
'FILE1.DAT[N]' means a text file which, on output, trailing blanks are
discarded. Other
possibilities are [X] = indexed, [C]=compressed, [T]=Tabbed text,
[V]=variable length, etc.
Further, each of these file types has sub-parameters unique to the type.
Again for example,
[X:Bnn:Rnnn:Dnn:Inn:Hnn:Wnn:Knn] for an indexed file where Bnn specifies the
block size
in kilobytes, Rnnn specifies the packing factor when the file is created,
Dnn controls the
number of data blocks held in memory, and so forth.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
