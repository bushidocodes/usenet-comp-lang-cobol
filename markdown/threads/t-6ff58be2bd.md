[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORT

_6 messages · 5 participants · 1998-03_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### SORT

- **From:** "a..." <ua-author-17071896@usenetarchives.gap>
- **Date:** 1998-03-23T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f7cps$j3p@pellew.ntu.edu.au>`

```



G'day,


The program below converts a field in the input file, sort the records and
then re-writes them back into file.

The program compiles OK, and does the sort and return code is 00. No problems
but if I take out the DISPLAY statement, the program still compiles with 00
return code when I run it but it doesn't do the sort. I get a message
something like SORT-REGISTER not used.............

I work in MVS-TSO environment and using COBOL II compiler. Your help would be
appreciated.





IDENTIFICATION DIVISION.
PROGRAM-ID. GLCB9069.
DATE-WRITTEN. MARCH 1998.
REMARKS. THIS PROGRAM CONVERTS THE ORG FIELD FOR
ORG 94, 96, 97 & 98 TO ORG 11 BEFORE
RE-SORTING THE RECORDS.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT INPUT-FL ASSIGN TO UT-S-INPUT.
SELECT SORT-FL ASSIGN TO UT-DA-SORT.

DATA DIVISION.
FILE SECTION.
FD INPUT-FL
LABEL RECORDS ARE STANDARD
RECORDING MODE F
BLOCK CONTAINS 0 RECORDS.
01 INPUT-RECORD PIC X(130).

SD SORT-FL.
01 SORT-RECORD.
05 SORT-ORG PIC X(06).
05 SORT-ACC PIC X(45).
05 FILLER PIC X(79).

WORKING-STORAGE SECTION.
01 INPUT-AREA.
05 INP-ORG-ID.
07 INP-ORG-ID-1 PIC X(01).
07 INP-ORG-ID-2 PIC X(01).
07 INP-ORG-ID-3 PIC X(01).
07 INP-ORG-ID-4 PIC X(01).
07 INP-ORG-ID-5 PIC X(01).
07 INP-ORG-ID-6 PIC X(01).
05 INP-PROG-CODE PIC X(45).
05 INP-POST-STD-CLASS PIC X(6).
05 INP-PAY-PERIOD.
07 FILLER PIC X(2).
07 INP-PAY-YR PIC X(2).
07 INP-PAY-PD PIC X(2).
05 INP-CAT-NO PIC X(2).
05 INP-AMOUNT-SIGN PIC X.
05 INP-AMOUNT PIC 9(9)V9(2).
05 FILLER PIC X(55).

77 FILLER PIC X VALUE 'N'.
88 INPUT-EOF VALUE 'Y'.
77 FILLER PIC X VALUE 'N'.
88 RETURN-EOF VALUE 'Y'.

PROCEDURE DIVISION.
000-MAIN.

DISPLAY ' START '

SORT SORT-FL
ON ASCENDING KEY SORT-ORG
ASCENDING KEY SORT-ACC
INPUT PROCEDURE 100-RELEASE
OUTPUT PROCEDURE 100-RETURN

DISPLAY 'PROGRAM GLCB9069: TERMINATED SUCCESSFULLY.'

STOP RUN.


100-RELEASE.
OPEN INPUT INPUT-FL
PERFORM UNTIL INPUT-EOF
READ INPUT-FL INTO INPUT-AREA
AT END
SET INPUT-EOF TO TRUE
NOT AT END
IF INP-ORG-ID = '94 ' OR '96 ' OR
'97 ' OR '98 '
MOVE '11 ' TO INP-ORG-ID
END-IF

RELEASE SORT-RECORD FROM INPUT-AREA
END-READ
END-PERFORM
CLOSE INPUT-FL.

100-RETURN.
OPEN OUTPUT INPUT-FL
PERFORM UNTIL RETURN-EOF
RETURN SORT-FL INTO INPUT-AREA
AT END
SET RETURN-EOF TO TRUE
NOT AT END
WRITE INPUT-RECORD FROM INPUT-AREA
END-RETURN
END-PERFORM
CLOSE INPUT-FL.
```

#### ↳ Re: SORT

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-23T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ff58be2bd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6f7cps$j3p@pellew.ntu.edu.au>`
- **References:** `<6f7cps$j3p@pellew.ntu.edu.au>`

```

Can you post/send the full message that you are getting? At a quick look
the code looks reasonable. You don't take into account the possibility of a
BAD "open" in either your input or output procedures and similarly you loop
until end-of-file even if an I/O error occurred. HOWEVER, since you are
using the IBM extension of not putting in either a File-Status or a
Declarative, then I would expect the program to ABEND if there were any I/O
problems.

P.S. For future development, I suggest that you comment (put an asterisk in
column 7) the "remarks" paragraph. You may not know this but the compiler
doesn't support this anymore. Your code works because the compiler thinks
it is actually a part of the Date-Written paragraph (because IBM has an
extension that allows comment-entries in the A-margin).
```

#### ↳ Re: SORT

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ff58be2bd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6f7cps$j3p@pellew.ntu.edu.au>`
- **References:** `<6f7cps$j3p@pellew.ntu.edu.au>`

```

Alvin,

I see some possible enhancements, which I cant resist to tell you, but no error,
nothing that explains your problem. Please report more runtime info, f.e. the
exact error msgs you get.

The cobol Frog.

Alvin Teo wrote:

8< [I snipped the problem descr]

›        IDENTIFICATION DIVISION.
›        PROGRAM-ID.    GLCB9069.
…[3 more quoted lines elided]…
›                       RE-SORTING THE RECORDS.
 
› Get rid of this no longer supported paragraph.
 
›        ENVIRONMENT DIVISION.
›        INPUT-OUTPUT SECTION.
›        FILE-CONTROL.
›             SELECT INPUT-FL ASSIGN TO UT-S-INPUT.
 
› I would use something like UPDATE i.s.o INPUT. To prevent misleaded JCL-writers.
 
›             SELECT SORT-FL  ASSIGN TO UT-DA-SORT.
› 
…[5 more quoted lines elided]…
›            BLOCK CONTAINS 0 RECORDS.
 
› Recording mode is a no longer needed IBM extension.
 
›        01  INPUT-RECORD                PIC X(130).
› 
›        SD  SORT-FL.
›        01  SORT-RECORD.
 
› Add a group above sort-og and -acc, f.e. 05  SORTKEY. See sort stmnt below.
 
›            05  SORT-ORG                PIC X(06).
›            05  SORT-ACC                PIC X(45).
…[20 more quoted lines elided]…
›            05  FILLER                 PIC X(55).
 
› This filler is two bytes too long.
 
›        77  FILLER                         PIC X VALUE 'N'.
›             88  INPUT-EOF                       VALUE 'Y'.
…[10 more quoted lines elided]…
›               ASCENDING KEY SORT-ACC

The addition off a group SORTKEY now makes it possible to code ON
ASCENDING KEY SORTKEY
i.s.o. two keys. This executes slightly faster. (The sort does one clc machine
instruction i.s.o. two, which is faster even if the amount of bytes to compare is
the same).

› INPUT PROCEDURE 100-RELEASE
› OUTPUT PROCEDURE 100-RETURN

Either the input or the output procedure could be used for the change of ORG-ID
codes. since you choose the input pocedure, I propose to change the OUTPUT line:
Make this GIVING INPUT-FL

› 
› 
…[19 more quoted lines elided]…
›            CLOSE INPUT-FL.
 
› Start omission. (See below)
 
›        100-RETURN.
›            OPEN OUTPUT INPUT-FL
…[8 more quoted lines elided]…
›            CLOSE INPUT-FL.

Because of the GIVING, the whole 100-RETURN paragraph can be omitted now.
```

#### ↳ Re: SORT

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1998-03-27T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ff58be2bd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6f7cps$j3p@pellew.ntu.edu.au>`
- **References:** `<6f7cps$j3p@pellew.ntu.edu.au>`

```

Input and Output Procedures need to be in Sections.

Code the paragraph names as:
100-RELEASE SECTION.
100-RETURN SECTION.

The SORT statement remains the same.
```

##### ↳ ↳ Re: SORT

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-27T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ff58be2bd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6ff58be2bd-p4@usenetarchives.gap>`
- **References:** `<6f7cps$j3p@pellew.ntu.edu.au> <gap-6ff58be2bd-p4@usenetarchives.gap>`

```


Cit··.@Cr··s.Com [Ron] wrote in message
<6fj4oe$l.··.@exa··c.net>...
› Input and Output Procedures need to be in Sections.
› 
…[5 more quoted lines elided]…
› 


It won't hurt, but this hasn't been required since the ANSI '74 Standard (or
compilers that tried to conform to it).
```

##### ↳ ↳ Re: SORT

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-03-30T08:20:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ff58be2bd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-6ff58be2bd-p4@usenetarchives.gap>`
- **References:** `<6f7cps$j3p@pellew.ntu.edu.au> <gap-6ff58be2bd-p4@usenetarchives.gap>`

```

In article <6fj4oe$l.··.@exa··c.net>,
Cit··.@Cr··s.Com [Ron] wrote:
› Input and Output Procedures need to be in Sections.
›
Not in Cobol-85 they don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
