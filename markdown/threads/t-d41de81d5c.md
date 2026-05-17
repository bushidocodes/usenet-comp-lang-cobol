[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# My "Not homework assignment that I'm not sure made it here"

_2 messages · 1 participant · 1997-03_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### My "Not homework assignment that I'm not sure made it here"

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-03-21T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5h2153$mhe@sjx-ixn8.ix.netcom.com>`

```

I am going to post this again forgive the duplication if it occured.

This is NOT a homework assignment, I just want to read other peoples solution to the same
problem.

The Problem: Using modulo 11 create from a customer_number a check digit and referance it
against a check digit provided for a data validation scheme.

Modulo 11 scheme : take a 5 digit number and calculate a check digit from it
the number 11111
1 1 1 1 1
multiply each number by these numbers 6 5 4 3 2
- - - - -
add the sums of the these together 6+5+4+3+2= 20 divide by 11 giving remainder 9

subtract the remainder from 11 giving the check digit 11-9 = 2

again this is not a homework assignment I just want to look at a number (hopefully :)
of experts solutions to this simple example.
Here is a data set including valid and invalid check digits

cust-num check-digit
---------------------------------begin data-----------------
11111 2
79200 4
01000 6
02340 0
02340 7
99999 7

---------------------------------end data-------------------
Again, Thanks and my solution will be added to this thread later tonight, I tried to find the
last first one and 4 hours after I posted it, it wasn't here.

Greg Amos
amo··.@ix.··m.com
```

#### ↳ Re: My "Not homework assignment that I'm not sure made it here"

- **From:** "gregory paul amos" <ua-author-17071352@usenetarchives.gap>
- **Date:** 1997-03-22T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d41de81d5c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5h2153$mhe@sjx-ixn8.ix.netcom.com>`
- **References:** `<5h2153$mhe@sjx-ixn8.ix.netcom.com>`

```

In article <5h2153$m.··.@sjx··m.com>,
Gregory Paul Amos wrote:

› I am  going to post this again forgive the duplication if it occured.
› 
…[33 more quoted lines elided]…
› amo··.@ix.··m.com  
Here's my program for the problem,I ask above. Please I'm not looking for help with mine IT
RUNS! :) Any constructive crticism welcomed but what I am really looking for is YOUR solutions
to this problem so I can read and compare several solutions and styles. Enjoy :)
Greg
amo··.@ix.··m.com

---------------Program Starts Here and uses data from above-- ---------------------------
IDENTIFICATION DIVISION.
PROGRAM-ID. CHKD.
ENVIRONMENT DIVISION.
FILE-CONTROL.

SELECT MYDATA ASSIGN TO DISK
* "C:¥VISOC¥SCHOOL¥DATA1.DAT"
* Rember to plug in your own compiler path here.
ORGANIZATION IS LINE SEQUENTIAL.
DATA DIVISION.
FILE SECTION.

FD MYDATA.
01 DATA-REC.
05 NUM1-KEY PIC 9(5).
05 FILLER PIC X(4).
05 CHK-DIGIT-1 PIC 9.



WORKING-STORAGE SECTION.
01 DAT-NUM-REC.
05 U-CUST-NUM1 PIC 9
OCCURS 5 TIMES INDEXED BY SUB.
05 F PIC X(3).
05 CHECK-DIGIT-1 PIC 9.
01 MISC.
05 EOF PIC X(3) VALUE 'NO '.
05 XX1 PIC 9(5) VALUE ZEROS.
05 XX2 PIC 9(5) VALUE ZEROS.
05 XX3 PIC 9(5) VALUE ZEROS.
05 XX4 PIC 9 VALUE ZEROS.
05 X PIC 9 VALUE ZEROS.
LINKAGE SECTION.
*01 U-CUST-NUM PIC 9
* OCCURS 5 TIMES INDEXED BY SUB.
*01 CHECK-DIGIT PIC 9.
*01 NUM-COMPARE-FLAG PIC X(4).

*PROCEDURE DIVISION USING U-CUST-NUM CHECK-DIGIT
* NUM-COMPARE-FLAG.
PROCEDURE DIVISION.

000-DRIVER-MAIN.
OPEN INPUT MYDATA
PERFORM 100-PROCESS-CHECK-DIGIT
UNTIL EOF = 'YES'
CLOSE MYDATA
GO TO 300-END-OF-PROG.

100-PROCESS-CHECK-DIGIT.
PERFORM 150-READ
MOVE ZEROS TO XX1
PERFORM VARYING X FROM 1 BY 1 UNTIL X > 5
COMPUTE XX1 = XX1 + ( U-CUST-NUM1(X) * (7 - X))
END-PERFORM
DIVIDE 11 INTO XX1 GIVING XX2 REMAINDER XX3 .
SUBTRACT XX3 FROM 11 GIVING XX4.
IF XX4 NOT EQUAL TO CHECK-DIGIT-1
* MOVE 'BAD ' TO NUM-COMPARE-FLAG.
DISPLAY 'BAD '
ELSE DISPLAY 'GOOD'
END-IF.
150-READ.
READ MYDATA INTO DAT-NUM-REC
AT END MOVE 'YES' TO EOF
END-READ.

300-END-OF-PROG.
EXIT PROGRAM.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
