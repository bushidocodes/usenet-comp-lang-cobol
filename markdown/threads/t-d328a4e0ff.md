[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question about sort error in microfocus

_2 messages · 2 participants · 1996-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Question about sort error in microfocus

- **From:** "bert duerinck" <ua-author-17072731@usenetarchives.gap>
- **Date:** 1996-12-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32AEC765.7611@denkart.be>`

```

Hello,

I get a run-time error called "attempt to access item beyond bounds of
memory" error-code 114 and i get this error on a release statement.

I have compiled the program with the following command:

cob -x -C IBMCOMP -C LINKCOUNT=1500 -C NOMFCOMMENT -C
SEQUENTIAL="LINE" -C DEFAULTBYTE=0 -C OSVS -C LINKCOUNT=350 -C TRACE
-k Z26063.mfcbl

The COBSW +s contains the default value (3M of sort memory)
The input file 0321710.0 is about 5,5 M and it is a line-sequential file
and the records are of variable record length.
What happens is that i read a lot of records and release them to the
sort(what you see in the source code), when i have released +/- 4,5 M of
data to the sort i'll get the run-time error 114 on the release
statement.

Does anybody know what goes wrong with this program???????
e-mail: b.··.@den··t.be

thanks

This is the code of the program:

INPUT-OUTPUT SECTION.
FILE-CONTROL.
SELECT O0321710 ASSIGN TO "0321710.0".
SELECT O0321711 ASSIGN TO DISK.
SELECT XA ASSIGN TO DISK.

DATA DIVISION.
*
FILE SECTION.
FD O0321710
LABEL RECORD IS STANDARD
BLOCK CONTAINS 20 RECORDS.
01 REC-710-1.
03 710-EJERAFD PIC 9(4).
03 710-AFD PIC 9(4).
03 710-ORDRE PIC 9(9).
03 710-AKTBEGREB.
05 710-HOVEDAKT PIC 9.
05 710-AKTIVITET PIC 99.
05 710-BRANCHE PIC 99.
05 710-HR PIC 9.
03 710-REC-TYPE PIC 9.
03 FILLER PIC X(32).
03 710-234-PER-COUNT PIC 99.
03 710-234-MAX-COUNT PIC 99.
03 710-234-PER-FORBRUG OCCURS 1 TO 99 DEPENDING ON
710-234-PER-COUNT.
05 710-234-PERIODE PIC 9(4).
05 710-234-TIMER PIC S9(7)V9.
01 REC-710-2.
03 FILLER PIC X(24).
03 710-233-FOERSTE-PLAN PIC S9(7)V9.
03 710-233-RESTTID PIC S9(7)V9.
03 710-233-PLANNING-REPORT PIC S9(7)V9.
03 710-233-DEL-GEN-TID PIC S9(7)V9.
03 FILLER PIC X(4).
*
FD O0321711
LABEL RECORD IS STANDARD
BLOCK CONTAINS 20 RECORDS
VALUE OF FILE-ID IS "0321711".
01 REC-711-1.
03 711-EJERAFD PIC 9(4).
03 711-AFD PIC 9(4).
03 711-ORDRE PIC 9(9).
03 711-AKTBEGREB.
05 711-HOVEDAKT PIC 9.
05 711-AKTIVITET PIC 99.
05 711-BRANCHE PIC 99.
05 711-HR PIC 9.
03 711-REC-TYPE PIC 9.
03 FILLER PIC X(32).
03 711-234-PER-COUNT PIC 99.
03 711-234-MAX-COUNT PIC 99.
03 711-234-PER-FORBRUG OCCURS 1 TO 99 DEPENDING ON
711-234-PER-COUNT.
05 711-234-PERIODE PIC 9(4).
05 711-234-TIMER PIC S9(7)V9.
01 REC-711-2.
03 FILLER PIC X(24).
03 711-233-FOERSTE-PLAN PIC S9(7)V9.
03 711-233-RESTTID PIC S9(7)V9.
03 711-233-PLANNING-REPORT PIC S9(7)V9.
03 711-233-DEL-GEN-TID PIC S9(7)V9.
03 FILLER PIC X(4).
*
SD XA
RECORD IS VARYING IN SIZE.
01 SORT-REC-1.
03 XA-EJERAFD PIC 9(4).
03 XA-AFD PIC 9(4).
03 XA-ORDRE PIC 9(9).
03 XA-AKTBEGREB.
05 XA-HOVEDAKT PIC 9.
05 XA-AKTIVITET PIC 99.
05 XA-BRANCHE PIC 99.
05 XA-HR PIC 9.
03 XA-REC-TYPE PIC 9.
03 FILLER PIC X(32).
03 XA-PER-COUNT PIC 99.
03 FILLER PIC 99.
03 XA-ELEM-1 OCCURS 1 TO 99 DEPENDING ON XA-PER-COUNT.
05 FILLER PIC 9(4).
05 FILLER PIC S9(7)V9.
01 SORT-REC-2.
03 FILLER PIC X(60).
PROCEDURE DIVISION.

BEGYND SECTION.

BS-PAR1.
OPEN INPUT O0321710.
OPEN OUTPUT O0321711.
PERFORM SORTER-AFD-ORD-AKT.
STOP RUN.
SR-EXIT.
EXIT.
*

SORTER-AFD-ORD-AKT SECTION.

SAOA-PAR1.
SORT XA
ON ASCENDING KEY XA-AFD XA-ORDRE XA-AKTBEGREB XA-REC-TYPE
INPUT PROCEDURE IS KO-SORT-IN THRU KO-SORT-IN-EXIT
OUTPUT PROCEDURE IS KO-SORT-OUT THRU KO-SORT-OUT-EXIT.


KO-SORT-IN SECTION.

KSI-PAR1.
READ O0321710
AT END
GO TO KO-SORT-IN-EXIT.
IF 710-REC-TYPE = 1 OR 3
MOVE REC-710-2 TO SORT-REC-2
RELEASE SORT-REC-2
MOVE SPACES TO SORT-REC-2
GO TO KSI-PAR1.
MOVE REC-710-1 TO SORT-REC-1.
RELEASE SORT-REC-1.
MOVE SPACES TO SORT-REC-1.
GO TO KSI-PAR1.

KO-SORT-IN-EXIT SECTION.

KSIE-PAR1.
CLOSE O0321710.

KSIE-EXIT.
EXIT.
*

KO-SORT-OUT SECTION.

KSO-PAR1.
MOVE SPACES TO SORT-REC-1.
RETURN XA
AT END
GO TO KO-SORT-OUT-EXIT.
IF XA-REC-TYPE = 1 OR 3
MOVE SORT-REC-2 TO REC-711-2
WRITE REC-711-2
END-WRITE
MOVE SPACES TO REC-711-2
ELSE
MOVE SORT-REC-1 TO REC-711-1
WRITE REC-711-1
END-WRITE
MOVE SPACES TO REC-711-1.
GO TO KSO-PAR1.

KO-SORT-OUT-EXIT SECTION.

KSOE-PAR1.
CLOSE O0321711.

KSOE-EXIT.
EXIT.
```

#### ↳ Re: Question about sort error in microfocus

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-12-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d328a4e0ff-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32AEC765.7611@denkart.be>`
- **References:** `<32AEC765.7611@denkart.be>`

```

Bert Duerinck wrote:
›
› Hello,
›
› I get a run-time error called "attempt to access item beyond bounds of
› memory" error-code 114 and i get this error on a release statement.

[snip]

Hello Bert -
This looks like it might be an internal error in the SORT. I suggest
that
you get in touch with your Technical Support representative. They will
request the full version numbers/platform details and also, if the
problem
is not reproducable with a smaller set of input data, the large data
file
you are trying to sort.

Cheers,
Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
