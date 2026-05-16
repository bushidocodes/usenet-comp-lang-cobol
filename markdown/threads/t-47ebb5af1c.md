[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# new programmer

_3 messages · 3 participants · 2004-03_

---

### new programmer

- **From:** davisb@njit.edu (Brenda)
- **Date:** 2004-03-29T08:45:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<82b1d610.0403290845.7f7a5955@posting.google.com>`

```
I am new to COBOL. I have never used COBOL before.  If I am correct, I
have a program which uses a presorted table by SSN.  I want to resort
by name.  I am having trouble identifying the fields. Where do I
begin?
I am providing the I-O section and the Working-Storage Section if that
will help.

*
INPUT-OUTPUT SECTION.
*
FILE-CONTROL.
    SELECT TIME-INPUT-FILE
        ASSIGN TO HRTIME
        FILE STATUS IS FSTAT
        ORGANIZATION IS SEQUENTIAL.
*
    SELECT CARD-FILE
        ASSIGN TO CARDFL
        ORGANIZATION IS SEQUENTIAL.
*
DATA DIVISION.
*
FILE SECTION.
*
FD  TIME-INPUT-FILE
*   BLOCK CONTAINS 0 RECORDS
    LABEL RECORD IS STANDARD
    DATA RECORD IS TR-RECORD.
01  TR-RECORD                   PIC X(300).
*
FD  CARD-FILE
*   BLOCK CONTAINS 0 RECORDS
    DATA RECORD IS CARD-RECORD.
01  CARD-RECORD                 PIC X(80).
/
*
*****************************************************************
*        W O R K I N G   S T O R A G E   S E C T I O N
*****************************************************************
*
WORKING-STORAGE SECTION.
*
*
01  WS-LIT                      PIC X(15)   VALUE
                                 "WORKING-STORAGE".
*
*
01  PROGRAM-CONTROL-DATA.
    03  PGM-ID                  PIC X(06)   VALUE "EBC311".
    03  PGM-VERSION             PIC X(02)   VALUE "01".
    03  PGM-LEVEL               PIC X(03)   VALUE "000".
    03  PGM-HEAD-TITLE          PIC X(50)   VALUE
            "                 TIME INPUT EXTRACT               ".
    03  PGM-SWITCHES.
        05  SW-EOTIF            PIC X(01)   VALUE "N".
    03  TOT-RCDS                PIC 9(09)   VALUE ZERO.
    03  TOT-PURGED              PIC 9(09)   VALUE ZERO.
    03  EMP-NO-HOLD             PIC X(09)   VALUE SPACES.
    03  HOLD-VER                PIC 9(05).
    03  CR-ERROR                PIC X(01)   VALUE "N".
    03  HOLD-PURGE-DATE         PIC X(08).
    03  LAST-ID                 PIC X(09)   VALUE SPACES.
    03  LAST-NAME               PIC X(30)   VALUE SPACES.
*
01  FISCAL-YEAR-DATE.
    03 FISCAL-CENT              PIC X(02)   VALUE SPACES.
    03 FISCAL-YEAR              PIC X(02)   VALUE SPACES.
*
*************************
*    HEADING LINES.    **
*************************
*
01  HEADINGS.
    03  H1                      PIC X(132)  VALUE SPACES.
    03  H2.
        05  FILLER              PIC X(50)   VALUE
        "EMPLOYEE ID  EMPLOYEE NAME                   FY PA".
        05  FILLER              PIC X(50)   VALUE
        "Y-ID ASSIGN TRN  OCC  E/C  DESCRIPTION     HOURS  ".
        05  FILLER              PIC X(32)   VALUE
        " START DATE   END DATE          ".
    03  H3                      PIC X(132)  VALUE SPACES.
*
01  HEADING-ARRAY  REDEFINES HEADINGS.
    03  HEADINGX                PIC X(132)  OCCURS 3 TIMES.
*
01  D1.
    03  D1-SSN                  PIC XXXBXXBXXXX.
    03  FILLER                  PIC X(02).
    03  D1-NAME                 PIC X(30).
    03  FILLER                  PIC X(02).
    03  D1-FY                   PIC X(02).
    03  FILLER                  PIC X(02).
    03  D1-PAYID                PIC X(04).
    03  FILLER                  PIC X(02).
    03  D1-JOB                  PIC X(01).
    03  FILLER                  PIC X(02).
    03  D1-ACODE                PIC X(03).
    03  FILLER                  PIC X(02).
    03  D1-TCODE                PIC X(02).
    03  FILLER                  PIC X(02).
    03  D1-OCC                  PIC X(03).
    03  FILLER                  PIC X(02).
    03  D1-ECODE                PIC X(03).
    03  FILLER                  PIC X(02).
    03  D1-ECODE-DESC           PIC X(10).
    03  FILLER                  PIC X(02).
    03  D1-HRS                  PIC ZZ,ZZZ.99.
    03  D1-SIGN                 PIC X(01).
    03  FILLER                  PIC X(02).
    03  D1-START                PIC X(10).
    03  FILLER                  PIC X(02).
    03  D1-END                  PIC X(10).
*
01  TOT-LINE.
    03  TOT-LIT                 PIC X(17).
    03  TL-RCD-CNT              PIC ZZZ,ZZZ,ZZ9.
*
*****************************************************************
*        FILE RECORD DESCRIPTIONS AND I/O PARM STRINGS.
*****************************************************************
*
*GM=EBC311,MM/DD/YYYY,CORP=XXX,PURGE=X,PURGE DATE=MM/DD/YYYY,
*       CREATE=X,PRINT=X
*
01  WS-CARD-REC.
    03  FILLER                  PIC X(04).
    03  WS-CC-PGM-ID            PIC X(06).
    03  FILLER                  PIC X(17).
    03  WS-CC-CORP              PIC X(03).
    03  FILLER                  PIC X(07).
    03  WS-CC-PURGE             PIC X(01).
    03  FILLER                  PIC X(12).
    03  WS-CC-PURGE-DATE.
        05  WS-PURGE-MM         PIC X(02).
        05  FILLER              PIC X(01).
        05  WS-PURGE-DD         PIC X(02).
        05  FILLER              PIC X(01).
        05  WS-PURGE-CC         PIC X(02).
        05  WS-PURGE-YY         PIC X(02).
    03  FILLER                  PIC X(08).
    03  WS-CC-CREATE            PIC X(01).
    03  FILLER                  PIC X(07).
    03  WS-CC-PRINT             PIC X(01).
    03  FILLER                  PIC X(03).
*
01  SEARCH-INFORMATION.
    03  SRCH-KEY.
        05  SRCH-LVL            PIC X(01).
        05  SRCH-CODE           PIC X(03).
    03  SRCH-IDX                PIC S9(3)   COMP SYNC.
    03  HIGH-LIMIT              PIC S9(3)   COMP SYNC.
    03  MID-POINT               PIC S9(3)   COMP SYNC.
    03  LOW-LIMIT               PIC S9(3)   COMP SYNC.
*
01  TCC-TABLE.
    03  TC-IDX                  PIC S9(3)   COMP SYNC VALUE +0.
    03  TC-TBL-MAX              PIC S9(3)   COMP SYNC VALUE +600.
    03  TC-TBL-CNT              PIC S9(3)   COMP SYNC VALUE +0.
    03  TC-TBL-ENTRY  OCCURS 600 TIMES.
        05  TC-TBL-KEY.
            07  TC-LVL          PIC X(01).
            07  TC-CODE         PIC X(03).
        05  TC-DESC             PIC X(10).
*
```

#### ↳ Re: new programmer

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-03-29T19:18:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c49sqf$251$1@peabody.colorado.edu>`
- **References:** `<82b1d610.0403290845.7f7a5955@posting.google.com>`

```
Looking at the supplied code, it is a safe bet that your instructor didn't want
you using the SORT command, but had a particular sort method in mind.   Probably
the method that he went over with in class.

Unfortunately, I wasn't at that class, so I don't know which of many different
ways to code a sort he wants.
```

#### ↳ Re: new programmer

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-03-29T20:21:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-EF7F7A.20212029032004@corp.supernews.com>`
- **References:** `<82b1d610.0403290845.7f7a5955@posting.google.com>`

```

Some time ago I posted a Cobol version of QuickSort here.  The example 
was, I believe, built for an 80-byte record.  You could Google that post 
to find an example of sorting a table.

Alternatively, you could use the SORT verb to sort your table.

Much depends upon the platform and compiler you are using?  Can you 
provide more details?



In article <82b1d610.0403290845.7f7a5955@posting.google.com>,
 davisb@njit.edu (Brenda) wrote:

> I am new to COBOL. I have never used COBOL before.  If I am correct, I
> have a program which uses a presorted table by SSN.  I want to resort
…[162 more quoted lines elided]…
> *
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
