[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Even negitive dollar comp-3 fields loosing sign byte in acucobol.

_3 messages · 2 participants · 1997-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Language features and syntax`](../topics.md#syntax)

---

### Even negitive dollar comp-3 fields loosing sign byte in acucobol.

- **From:** "h. blakely williford" <ua-author-9633586@usenetarchives.gap>
- **Date:** 1997-04-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3360BFA8.105EF4FD@fuller.com>`

```


This is a multi-part message in MIME format.

--------------7DB14A3217810F0F3E40B73D
Content-Type: text/plain; charset=us-ascii
Content-Transfer-Encoding: 7bit

Hello World!

we are running ACUCOBOL-85 runtime version 2.4.2 on digital
unix 4.0.

On the following code the values of gf-gv-growth and gf-pgv-growth
are looseing the negitive value in the .dat file.

The signed byte is lost and the first byte of next field "writes"
over it. for example if ...

field 1 = (hex) 123d
field 2 = (hex) 456d

on a hex dump after the write the fields look ok, but on the
read ...

field 1 = (hex) 1245
field 2 = (hex) 6dxx (where xx is the next byte of the record)

this seems to happen on negitive even dollar amount.

Note: we just came off of an MVS main-frame cobol please be
nice :) The programer's e-mail address is kar··.@ful··h.com

--------------7DB14A3217810F0F3E40B73D
Content-Type: text/plain; charset=us-ascii; name="sortck2.s"
Content-Transfer-Encoding: 7bit
Content-Disposition: inline; filename="sortck2.s"

IDENTIFICATION DIVISION.
*
PROGRAM-ID. SORTCHCK.
AUTHOR. Karla Essmiller.
INSTALLATION. The Fuller Brush Co, Great Bend, KS.
DATE-WRITTEN. April 1997.
DATE-COMPILED.
**
** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
** FBHH049 **
**-------------------------------------------------------------**
** Prints the HH distributor GV and PGV growth report. **
** **
** Data Base Files : micusmf customer master **
** Input Files : mlmpayfl pay file **
** Output Files : report1 GV/PGV growth report **
** **
** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
**
*
ENVIRONMENT DIVISION.
*
INPUT-OUTPUT SECTION.
*
FILE-CONTROL.
*
SELECT GROWTH-FILE
ASSIGN TO RANDOM GROWTH
ORGANIZATION IS LINE SEQUENTIAL
FILE STATUS IS FILESTAT.
*
SELECT REPORT1-FILE
ASSIGN TO RANDOM REPORT1
ORGANIZATION IS LINE SEQUENTIAL
FILE STATUS IS FILESTAT.
/
DATA DIVISION.
*
FILE SECTION.
*
FD GROWTH-FILE.
01 GROWTH-REC.
05 GF-ACCT PIC 9(7) VALUE ZEROES.
05 GF-NAME PIC X(25) VALUE SPACES.
05 GF-GV-GROWTH PIC S9(7)V99 VALUE ZEROES USAGE COMP-3.
05 GF-PGV-GROWTH PIC S9(7)V99 VALUE ZEROES USAGE COMP-3.
05 GF-TOT-RET PIC S9(7)V99 VALUE ZEROES.
05 GF-ENC-RET PIC S9(7)V99 VALUE ZEROES.
05 GF-PGV PIC S9(7)V99 VALUE ZEROES.
05 GF-TITLE PIC XX VALUE SPACES.
05 GF-PAID-AS PIC XX VALUE SPACES.
05 GF-BV PIC S9(5)V99 VALUE ZEROES.
05 GF-TOTAL-DL PIC S9(5) VALUE ZEROES.
05 GF-TOT-RET1 PIC S9(7)V99 VALUE ZEROES.
05 GF-ENC-RET1 PIC S9(7)V99 VALUE ZEROES.
05 GF-PGV1 PIC S9(7)V99 VALUE ZEROES.
05 GF-TITLE1 PIC XX VALUE SPACES.
05 GF-PAID-AS1 PIC XX VALUE SPACES.
05 GF-BV1 PIC S9(5)V99 VALUE ZEROES.
05 GF-TOTAL-DL1 PIC S9(5) VALUE ZEROES.
05 FILLER PIC XX VALUE SPACES.
*
FD REPORT1-FILE
LABEL RECORDS ARE STANDARD
RECORD CONTAINS 133 CHARACTERS
DATA RECORD IS REPORT1-REC.
01 REPORT1-REC PIC X(133).
/
WORKING-STORAGE SECTION.
*----------------------------------------------------------------------*
* Paths for input/output files stored here in open routines. *
*----------------------------------------------------------------------*
01 GROWTH PIC X(40) VALUE
'-F /usr/users/control2/sortchck.dat '.
01 REPORT1 PIC X(40) VALUE
'-F /usr/users/control2/sortchck.rpt '.
*----------------------------------------------------------------------*
*
01 FILESTAT PIC XX VALUE SPACES.
/
01 REPORT1-LINE.
05 R1-ACCT PIC 9(7) VALUE ZEROES.
05 FILLER PIC X VALUE SPACES.
05 R1-NAME PIC X(25) VALUE ZEROES.
05 FILLER PIC X VALUE SPACES.
05 R1-GV-GROWTH PIC ZZZZZZ9.99-.
05 FILLER PIC X VALUE SPACES.
05 R1-PGV-GROWTH PIC ZZZZZZ9.99-.
05 FILLER PIC X VALUE SPACES.
05 R1-TOT-RET PIC ZZZZZZ9.99-.
05 FILLER PIC X VALUE SPACES.
05 R1-ENC-RET PIC ZZZZZZ9.99-.
05 FILLER PIC X VALUE SPACES.
05 R1-PGV PIC ZZZZZZ9.99-.
05 FILLER PIC X VALUE SPACES.
05 R1-TITLE PIC XX VALUE SPACES.
05 FILLER PIC X VALUE SPACES.
05 R1-PAID-AS PIC XX VALUE SPACES.
05 FILLER PIC X VALUE SPACES.
05 R1-BV PIC ZZZZ9.99-.
05 FILLER PIC X VALUE SPACES.
05 R1-TOTAL-DL PIC ZZZZ9 VALUE ZEROES.
05 FILLER PIC X(18) VALUE SPACES.
/
PROCEDURE DIVISION.
*---------------------------------------------------------------------*
* This is the main logic module of the program. *
*---------------------------------------------------------------------*
000-OPEN-FILES.
*
PERFORM 2000-CREATE-FILE THRU 2000-EXIT.
PERFORM 3000-PRINT-REPORT THRU 3000-EXIT.
GO TO 1999-STOP-RUN.
*
1999-STOP-RUN.
STOP RUN.
1999-EXIT.
EXIT.
*
/
2000-CREATE-FILE.
OPEN OUTPUT GROWTH-FILE.
*
MOVE 'KARLA ESSMILLER ' TO GF-NAME.
MOVE 1100002 TO GF-ACCT.
MOVE 1.00 TO GF-GV-GROWTH.
MOVE 1.00 TO GF-PGV-GROWTH.
MOVE 30273.57 TO GF-TOT-RET.
MOVE 60834.31 TO GF-ENC-RET.
MOVE -30560.74 TO GF-PGV.
MOVE 'M ' TO GF-TITLE.
MOVE ' ' TO GF-PAID-AS.
MOVE 903 TO GF-TOTAL-DL
MOVE 123.45 TO GF-BV.
MOVE 28020.76 TO GF-TOT-RET1.
MOVE 48435.57 TO GF-ENC-RET1.
MOVE -20414.81 TO GF-PGV1.
MOVE ' ' TO GF-TITLE1.
MOVE ' ' TO GF-PAID-AS1.
MOVE 123 TO GF-TOTAL-DL1.
MOVE 234.56 TO GF-BV1.
WRITE GROWTH-REC.
*
MOVE 'TEST NEGATIVES ' TO GF-NAME.
MOVE 1100001 TO GF-ACCT.
MOVE -1.00 TO GF-GV-GROWTH.
MOVE -1.00 TO GF-PGV-GROWTH.
MOVE 30273.57 TO GF-TOT-RET.
MOVE 60834.31 TO GF-ENC-RET.
MOVE -30560.74 TO GF-PGV.
MOVE 'M ' TO GF-TITLE.
MOVE ' ' TO GF-PAID-AS.
MOVE 903 TO GF-TOTAL-DL
MOVE 123.45 TO GF-BV.
MOVE 28020.76 TO GF-TOT-RET1.
MOVE 48435.57 TO GF-ENC-RET1.
MOVE -20414.81 TO GF-PGV1.
MOVE ' ' TO GF-TITLE1.
MOVE ' ' TO GF-PAID-AS1.
MOVE 123 TO GF-TOTAL-DL1.
MOVE 234.56 TO GF-BV1.
WRITE GROWTH-REC.
*
CLOSE GROWTH-FILE.
2000-EXIT.
EXIT.
*
3000-PRINT-REPORT.
*
OPEN INPUT GROWTH-FILE
OUTPUT REPORT1-FILE.
*
3000-READ-NEXT.
*---------------------------------------------------------------------*
* Read sort file and print reports. *
*---------------------------------------------------------------------*
READ GROWTH-FILE
AT END
GO TO 3000-CLOSE-FILES.
*
MOVE SPACES TO REPORT1-LINE.
MOVE GF-ACCT TO R1-ACCT.
MOVE GF-NAME TO R1-NAME.
MOVE GF-GV-GROWTH TO R1-GV-GROWTH.
MOVE GF-PGV-GROWTH TO R1-PGV-GROWTH.
MOVE GF-TOT-RET TO R1-TOT-RET.
MOVE GF-ENC-RET TO R1-ENC-RET.
MOVE GF-PGV TO R1-PGV.
MOVE GF-TITLE TO R1-TITLE.
MOVE GF-PAID-AS TO R1-PAID-AS.
MOVE GF-BV TO R1-BV.
MOVE GF-TOTAL-DL TO R1-TOTAL-DL.
WRITE REPORT1-REC FROM REPORT1-LINE AFTER 2.
*
MOVE SPACES TO REPORT1-LINE.
MOVE GF-TOT-RET1 TO R1-TOT-RET.
MOVE GF-ENC-RET1 TO R1-ENC-RET.
MOVE GF-PGV1 TO R1-PGV.
MOVE GF-TITLE1 TO R1-TITLE.
MOVE GF-PAID-AS1 TO R1-PAID-AS.
MOVE GF-BV1 TO R1-BV.
MOVE GF-TOTAL-DL1 TO R1-TOTAL-DL.
WRITE REPORT1-REC FROM REPORT1-LINE.
*
GO TO 3000-READ-NEXT.
*
3000-CLOSE-FILES.
CLOSE GROWTH-FILE
REPORT1-FILE.
*
3000-EXIT.
EXIT.
/

--------------7DB14A3217810F0F3E40B73D--
```

#### ↳ Re: Even negitive dollar comp-3 fields loosing sign byte in acucobol.

- **From:** "clifford lane" <ua-author-2820384@usenetarchives.gap>
- **Date:** 1997-04-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a639b5beac-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3360BFA8.105EF4FD@fuller.com>`
- **References:** `<3360BFA8.105EF4FD@fuller.com>`

```

This may be a stretch but I ran into a similar problem on an old no name
compiler that had a compile time flag that caused packed numbers to start
on word boundaries. Check your compile time options for a flag that may be
causing the problem.

Cliff Lane
```

#### ↳ Re: Even negitive dollar comp-3 fields loosing sign byte in acucobol.

- **From:** "h. blakely williford" <ua-author-9633586@usenetarchives.gap>
- **Date:** 1997-04-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a639b5beac-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3360BFA8.105EF4FD@fuller.com>`
- **References:** `<3360BFA8.105EF4FD@fuller.com>`

```

H. Blakely Williford wrote:

We ran this code on two other machines running VMS and MVS; both
worked fine. The problem we found was that accucobol want/needs
is binary sequential organization, not line sequential. After
that change was made the code worked, but produced a file that
was unusable on both VMS and MVS systems.

Is thes some new standared in COBOL that passed us by?

> ENVIRONMENT DIVISION.
> *
…[5 more quoted lines elided]…
> ASSIGN TO RANDOM GROWTH
--> ORGANIZATION IS LINE SEQUENTIAL
> FILE STATUS IS FILESTAT.
> *

changed to

> ENVIRONMENT DIVISION.
> *
…[5 more quoted lines elided]…
> ASSIGN TO RANDOM GROWTH
**> ORGANIZATION IS BINARY SEQUENTIAL
> FILE STATUS IS FILESTAT.
> *

thank-you for your time.

H. Blakely Williford          Men never do evil so completely and
Systems Administrator         cheerfully as when they do it from 
The Fuller Brush Company      religious conviction. (Pascal)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
