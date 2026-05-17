[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Please help me debug this *&% indexed file update program.

_7 messages · 6 participants · 1996-07 → 1996-08_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Please help me debug this *&% indexed file update program.

- **From:** "eric r. arnold" <ua-author-17086487@usenetarchives.gap>
- **Date:** 1996-07-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31FD097C.7DA6@flash.net>`

```
I always get an ERROR 018 whenever I run this program. I'm
trying to update an Indexed file with validated transactions. I've
included a listing of the valid transaction file. I step through the
program in MF Animator and it will step through the add record process
once and then it will READ, EVALUATE, and then PERFORM the ERROR RTN
about 5 times.
If any of the COBOL GURUS could help me on this I would greatly
appreciate it.
Please E-Mail or Post the Info to this Newsgroup.

Thanks'

Psyclops the Psynical
IDENTIFICATION DIVISION.
PROGRAM-ID. COBSHL01.
AUTHOR. ERIC R ARNOLD.
INSTALLATION. UTA.
DATE-WRITTEN.
DATE-COMPILED.
SECURITY. UNCLASSIFIED.
***************************************************************
* UPDATE MASTER FILE.
***************************************************************
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.

SOURCE-COMPUTER. IBM-PC.
OBJECT-COMPUTER. IBM-PC.

INPUT-OUTPUT SECTION.

FILE-CONTROL.
SELECT TRANSACTION-FILE
ASSIGN TO 'INKSTER3.TRN'.

SELECT INKSTER3-INDEXED
ASSIGN TO 'INKSTER3.MST'
ORGANIZATION IS INDEXED
ACCESS IS DYNAMIC
RECORD KEY IS IND-EMPLOYEE-ID.

DATA DIVISION.
FILE SECTION.

FD TRANSACTION-FILE
LABEL RECORDS ARE STANDARD
RECORD CONTAINS 127 CHARACTERS
DATA RECORD IS TRANSACTION-RECORD.
01 TRANSACTION-RECORD.
05 TRANS-CODE PIC X.
88 ADDITION VALUE 'A'.
88 CHANGE VALUE 'C'.
88 DELETION VALUE 'D'.
05 TRN-EMPL-ID PIC X(9).
05 TRN-LAST-NAME.
10 TRN-CHG-FIELD-NO PIC XX.
88 CHG-LAST VALUE '03'.
88 CHG-FIRST VALUE '04'.
88 CHG-POS VALUE '05'.
88 CHG-ADDRESS VALUE '06'.
88 CHG-CITY VALUE '07'.
88 CHG-STATE VALUE '08'.
88 CHG-ZIP VALUE '09'.
88 CHG-AREA-CD VALUE '10'.
88 CHG-PHONE VALUE '11'.
88 CHG-COVERAGE VALUE '12'.
88 CHG-DEPENDANTS VALUE '13'.
88 CHG-PAYRATE VALUE '14'.
88 CHG-SELF VALUE '15'.
88 CHG-SPOUSE VALUE '16'.
88 CHG-DEP VALUE '17'.
88 CHG-SYSTEM-ID VALUE '18'.
88 CHG-SYSTEM-PASS VALUE '19'.
88 VALID-FIELD-NUMBER
VALUES '03','04','05','06','07',
'08','09','10','11','12','13',
'14','15','16','17','18','19'.
10 TRN-CHG-INFO PIC X(13).
05 TRN-FIRST-NAME PIC X(10).
05 TRN-POS-CODE PIC X(2).
05 TRN-ADDRESS PIC X(25).
05 TRN-CITY PIC X(25).
05 TRN-STATE PIC X(2).
05 TRN-ZIP PIC X(5).
05 TRN-AREA-CD PIC X(3).
05 TRN-PHONE PIC X(7).
05 TRN-COVERAGE PIC X.
05 TRN-DEPENDANTS PIC XX.
05 TRN-PAYRATE PIC X(5).
05 TRN-LI-SELF PIC X.
05 TRN-LI-SPOUSE PIC X.
05 TRN-LI-DEP PIC X.
05 TRN-SYSTEM-ID PIC X(6).
05 TRN-SYSTEM-PASS PIC X(6).


FD INKSTER3-INDEXED
LABEL RECORDS ARE STANDARD
RECORD CONTAINS 126 CHARACTERS
DATA RECORD IS INKSTER3-MST-RECORD.
01 INKSTER3-MST-RECORD.
05 IND-EMPLOYEE-ID PIC X(9).
05 LAST-NAME PIC X(15).
05 FIRST-NAME PIC X(10).
05 POS-CODE PIC X(2).
05 EMP-ADDRESS PIC X(25).
05 EMP-CITY PIC X(25).
05 EMP-STATE PIC X(2).
05 EMP-ZIP PIC X(5).
05 EMP-AREA-CD PIC X(3).
05 EMP-PHONE PIC X(7).
05 EMP-COVERAGE PIC X.
05 EMP-DEPENDANTS PIC XX.
05 EMP-PAYRATE PIC X(5).
05 LI-SELF PIC X.
05 LI-SPOUSE PIC X.
05 LI-DEP PIC X.
05 SYSTEM-ID PIC X(6).
05 SYSTEM-PASS PIC X(6).


WORKING-STORAGE SECTION.

01 PROGRAM-SWITCHES.
05 END-OF-FILE-SWITCH PIC X(3) VALUE 'NO'.
05 RECORD-KEY-ALLOCATED-SWITCH PIC X(3) VALUE 'NO'.

PROCEDURE DIVISION.
PROGRAM-BEGIN.

0000-MAIN-MODULE.
OPEN INPUT TRANSACTION-FILE
I-O INKSTER3-INDEXED.
READ TRANSACTION-FILE NEXT RECORD
AT END
MOVE 'YES' TO END-OF-FILE-SWITCH
NOT AT END
PERFORM 0030-APPLY-TRANS-TO-MASTER
UNTIL END-OF-FILE-SWITCH = 'YES'
END-READ.
CLOSE TRANSACTION-FILE
INKSTER3-INDEXED.

EXIT PROGRAM.
STOP RUN.

0030-APPLY-TRANS-TO-MASTER.
EVALUATE TRUE
WHEN ADDITION
PERFORM 0090-ADD-NEW-RECORD
WHEN CHANGE
PERFORM 0100-CORRECT-EXISTING-RECORD
WHEN DELETION
PERFORM 0110-DELETE-EXISTING-RECORD
END-EVALUATE.
READ TRANSACTION-FILE NEXT RECORD
AT END MOVE 'YES'TO END-OF-FILE-SWITCH
END-READ.

0090-ADD-NEW-RECORD.
IF RECORD-KEY-ALLOCATED-SWITCH = 'YES'
DISPLAY ' ERROR DUPLICATE ADDITION: 'TRN-EMPL-ID
ELSE
MOVE TRN-EMPL-ID TO IND-EMPLOYEE-ID
MOVE TRN-LAST-NAME TO LAST-NAME
MOVE TRN-FIRST-NAME TO FIRST-NAME
MOVE TRN-POS-CODE TO POS-CODE
MOVE TRN-ADDRESS TO EMP-ADDRESS
MOVE TRN-CITY TO EMP-CITY
MOVE TRN-STATE TO EMP-STATE
MOVE TRN-ZIP TO EMP-ZIP
MOVE TRN-AREA-CD TO EMP-AREA-CD
MOVE TRN-PHONE TO EMP-PHONE
MOVE TRN-COVERAGE TO EMP-COVERAGE
MOVE TRN-DEPENDANTS TO EMP-DEPENDANTS
MOVE TRN-PAYRATE TO EMP-PAYRATE
MOVE TRN-LI-SELF TO LI-SELF
MOVE TRN-LI-SPOUSE TO LI-SPOUSE
MOVE TRN-LI-DEP TO LI-DEP
MOVE TRN-SYSTEM-ID TO SYSTEM-ID
MOVE TRN-SYSTEM-PASS TO SYSTEM-PASS.
WRITE INKSTER3-MST-RECORD
INVALID KEY PERFORM 1000-ERROR-RTN
END-WRITE.

0100-CORRECT-EXISTING-RECORD.
MOVE SPACES TO INKSTER3-MST-RECORD.
MOVE TRN-EMPL-ID TO IND-EMPLOYEE-ID.
READ INKSTER3-INDEXED
INVALID KEY PERFORM 1000-ERROR-RTN
NOT INVALID KEY PERFORM 0105-GET-CHG-FIELD-NO
END-READ.

0105-GET-CHG-FIELD-NO.
EVALUATE TRN-CHG-FIELD-NO
WHEN 3
MOVE TRN-CHG-INFO TO LAST-NAME
WHEN 4
MOVE TRN-CHG-INFO TO FIRST-NAME
WHEN 5
MOVE TRN-CHG-INFO TO POS-CODE
WHEN 6
MOVE TRN-CHG-INFO TO EMP-ADDRESS
WHEN 7
MOVE TRN-CHG-INFO TO EMP-CITY
WHEN 8
MOVE TRN-CHG-INFO TO EMP-STATE
WHEN 9
MOVE TRN-CHG-INFO TO EMP-ZIP
WHEN 10
MOVE TRN-CHG-INFO TO EMP-AREA-CD
WHEN 11
MOVE TRN-CHG-INFO TO EMP-PHONE
WHEN 12
MOVE TRN-CHG-INFO TO EMP-COVERAGE
WHEN 13
MOVE TRN-CHG-INFO TO EMP-DEPENDANTS
WHEN 14
MOVE TRN-CHG-INFO TO EMP-PAYRATE
WHEN 15
MOVE TRN-CHG-INFO TO LI-SELF
WHEN 16
MOVE TRN-CHG-INFO TO LI-SPOUSE
WHEN 17
MOVE TRN-CHG-INFO TO LI-DEP
WHEN 18
MOVE TRN-CHG-INFO TO SYSTEM-ID
WHEN 19
MOVE TRN-CHG-INFO TO SYSTEM-PASS
WHEN OTHER
DISPLAY 'INVALID CHANGE FIELD: 'TRN-EMPL-ID
END-EVALUATE.
REWRITE INKSTER3-MST-RECORD
INVALID KEY PERFORM 1000-ERROR-RTN
END-REWRITE.

0110-DELETE-EXISTING-RECORD.
MOVE TRN-EMPL-ID TO IND-EMPLOYEE-ID.
READ INKSTER3-INDEXED
INVALID KEY PERFORM 1000-ERROR-RTN
NOT INVALID KEY
DELETE INKSTER3-INDEXED
INVALID KEY PERFORM 1000-ERROR-RTN
END-DELETE
END-READ.

1000-ERROR-RTN.
DISPLAY 'ERROR: ' TRN-EMPL-ID.
A012553322MILLER AMANDA C26688 DISNEY CT IRVING TX762102148601654F02010004YY
A221992763PARKER JEFF SP1313 MOCKINGBIRD LN FT WORTH TX761108174612456F01048001YY
A333221111CLEMENTS KEVIN A1ONE WILL ROGERS PLAZA FT WORTH TX761108172744564F01014002YY
A623123842GULLEDGE KELLEY A3907 ALPHABETA DR MANSFIELD TX760018178299843S00024005NN
A666554444DRAKE JASON C39632 PIONEER PKY GRAND PRAIRIE TX751238172777890S00012003NN
A728374650ESPINOZA JUANITA C28273 INDIANAPOLIS DR DALLAS TX752228172654565F00010005YY
A777665555JACKSON AMY A43456 ARKANSAS APT B IRVING TX762108174595612S00025003NN
C07812354417Y
C27865163507BEDFORD
C2786516350976567
C27865163510214
C278651635112741651
C27865163503MONTGOMERIE
C278651635061509 TYLER
C27865163512F
C3245676211305
C54545422205C2
C65751657212F
C65751657217N
D357489319
D565487832
```

#### ↳ Re: Please help me debug this *&% indexed file update program.

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-07-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbcf0d8cbd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31FD097C.7DA6@flash.net>`
- **References:** `<31FD097C.7DA6@flash.net>`

```

In <31F··.@fl··h.net>, "Eric R. Arnold" writes:
› This is a multi-part message in MIME format.
› 
…[42 more quoted lines elided]…
›               END-WRITE.
The '??????' above points to what looks like a bug to me.
The WRITE statement is always executed, sometimes with
the previous contents of the record.
Here is another example why:
1) never use dots, except to terminate an IF statement
(and here it is better to use END-IF if your compiler
supports it)
2) if you use a dot (in violation of rule 1) put it on
a line by itself so it sticks out.

I don't know if this fixes your problem (I stopped looking
when I saw this one).
```

#### ↳ Re: Please help me debug this *&% indexed file update program.

- **From:** "f..." <ua-author-91703@usenetarchives.gap>
- **Date:** 1996-07-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbcf0d8cbd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<31FD097C.7DA6@flash.net>`
- **References:** `<31FD097C.7DA6@flash.net>`

```

"Eric R. Arnold" wrote:

› This is a multi-part message in MIME format.
 
› --------------59C14F59BED
› Content-Type: text/plain; charset=us-ascii
› Content-Transfer-Encoding: 7bit
 
› I always get an ERROR 018 whenever I run this program.  I'm 
› trying to update an Indexed file with validated transactions.  I've 
…[6 more quoted lines elided]…
› Please E-Mail or Post the Info to this Newsgroup.
 
› Thanks'
 
› Psyclops the Psynical

I've seen people make this mistake may times. An error 018 is a
premature end of file. The reason you are getting this is because MF
COBOL supports two kinds of fixed-length sequential files:

1) record sequential - where each record is n bytes long and the next
record begins at the n+1 byte. This is the default (and what yiu
specified.

3) line sequential - where each record is terminated by a CRLF - just
like most DOS based text files and your source program (and the input
file you supplied). MF space fills or truncates as necessary with
each READ.

Your program was reading fixed length chunks of the data file
including the CRLF's, so that when you got to those short "C" records
at the end you were reading two or three at a time. The last read was
a little short hence the 018


Solution: add ORGANIZATION IS LINE SEQUENTIAL to the select statement
for your input file.



Good Luck,

Lee Unterreiner
COBOL Research Group
415.568.1522
```

##### ↳ ↳ Re: Please help me debug this *&% indexed file update program.

- **From:** "eric r arnold" <ua-author-17086626@usenetarchives.gap>
- **Date:** 1996-07-30T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbcf0d8cbd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cbcf0d8cbd-p3@usenetarchives.gap>`
- **References:** `<31FD097C.7DA6@flash.net> <gap-cbcf0d8cbd-p3@usenetarchives.gap>`

```

I want to thank all for pointing out the errors in my program. I
corrected the SELECT statement and added ORGANIZATION IS LINE
SEQUENTIAL. I no longer received an error message. I corrected the
premature period in the MOVE paragraph and that took care of moving
records. I worked out the rest of the bugs and the program works
wonderfully.
Again, thanks. I was able to complete the rest of my class
assignment and turn it in on time.

Psyclops the psynical.
```

###### ↳ ↳ ↳ Re: Please help me debug this *&% indexed file update program.

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-08-01T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbcf0d8cbd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cbcf0d8cbd-p4@usenetarchives.gap>`
- **References:** `<31FD097C.7DA6@flash.net> <gap-cbcf0d8cbd-p3@usenetarchives.gap> <gap-cbcf0d8cbd-p4@usenetarchives.gap>`

```

Eric R Arnold wrote:

› I want to thank all for pointing out the errors in my program.  I 
› corrected the SELECT statement and added ORGANIZATION IS LINE 
…[5 more quoted lines elided]…
› assignment and turn it in on time.
 
› Psyclops the psynical.

Well, this looks like the first case of a world-wide desk-check of a
student assignment.
```

#### ↳ Re: Please help me debug this *&% indexed file update program.

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-07-29T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbcf0d8cbd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<31FD097C.7DA6@flash.net>`
- **References:** `<31FD097C.7DA6@flash.net>`

```

"Eric R. Arnold" wrote:


›       0090-ADD-NEW-RECORD.
›           IF RECORD-KEY-ALLOCATED-SWITCH = 'YES'
…[22 more quoted lines elided]…
›               END-WRITE.

Just a question: did you intend to put the period after "MOVE
TRN-SYSTEM-PASS TO SYSTEM-PASS." and have "WRITE INKSTER3-MST-RECORD"
perform its duty no matter what the conditional does?
```

#### ↳ Re: Please help me debug this *&% indexed file update program.

- **From:** "jra..." <ua-author-1103086@usenetarchives.gap>
- **Date:** 1996-07-29T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbcf0d8cbd-p7@usenetarchives.gap>`
- **In-Reply-To:** `<31FD097C.7DA6@flash.net>`
- **References:** `<31FD097C.7DA6@flash.net>`

```

"Eric R. Arnold" wrote:

›               MOVE TRN-SYSTEM-ID TO SYSTEM-ID
›               MOVE TRN-SYSTEM-PASS TO SYSTEM-PASS.
 
›                 is this a typeo                  ^^^^^
 
›               WRITE INKSTER3-MST-RECORD
›                   INVALID KEY PERFORM 1000-ERROR-RTN
›               END-WRITE.

JR


and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
