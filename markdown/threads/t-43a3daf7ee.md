[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with a Sort Routine

_3 messages · 3 participants · 1999-02_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Problem with a Sort Routine

- **From:** "Jim" <jimyt@REMOVEMEyahoo.com>
- **Date:** 1999-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%%_v2.1121$QK4.1234@news2.giganews.com>`

```
Compiler : Microfocus Personal Cobol for Windows
OS : Win98

I have a problem with a Sort Routine in my program. All the literature I
have on Cobol doesn't say much about sorting variable length records, could
this be where the problem is? It will not Compile. It keeps coming up with
the message:

"C:\Coding\Mt25p2.cbl 49: JMN2896I-S  SORT-MERGE FILE CAN ONLY SPECIFY
FILE-IDENTIFIER IN ASSIGN CLAUSE."

Here are the relevant sections of code :
**********************************************************************
IDENTIFICATION DIVISION.
 PROGRAM-ID. MT25P2.
 ENVIRONMENT DIVISION.
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
     SELECT VALID-FILE ASSIGN TO "MT25VF.DAT"
         ORGANIZATION IS LINE SEQUENTIAL.
     SELECT PRINT-FILE ASSIGN TO PRINTER.
     SELECT SORTED-FILE ASSIGN TO "MT25SD.DAT"
         ORGANIZATION IS LINE SEQUENTIAL.
     SELECT WORK-FILE ASSIGN TO "WORKFILE.DAT".

 DATA DIVISION.
 FILE SECTION.

FD  VALID-FILE.
 01  VAL-IR-REC.
     03  V-IR-REC-TYPE         PIC X.
     03  V-IR-CUST-CODE       PIC X(5).
     03  V-IR-PART-NUM          PIC X(6).
     03  V-IR-QUANTITY           PIC 9(4).

01  VAL-D-REC.
     03  V-D-REC-TYPE             PIC X.
     03  V-D-CUST-CODE          PIC X(5).

01  VAL-C-REC.
     03  V-C-REC-TYPE             PIC X.
     03  V-C-CUST-CODE           PIC X(5).
     03  V-C-CUST-NAME           PIC X(20).
     03  V-C-CUST-ADDRESS     PIC X(60).
     03  V-C-CUST-BALANCE      PIC 9(7)V99.
     03  V-C-CRED-LIMIT             PIC 9(7).

 FD  SORTED-FILE.
 01  SORT-IR-REC.
     03  S-IR-REC-TYPE           PIC X.
     03  S-IR-CUST-CODE         PIC X(5).
     03  S-IR-PART-NUM            PIC X(6).
     03  S-IR-QUANTITY             PIC 9(4).

01  SORT-D-REC.
     03  S-D-REC-TYPE              PIC X.
     03  S-D-CUST-CODE            PIC X(5).

 01  SORT-C-REC.
     03  S-C-REC-TYPE               PIC X.
     03  S-C-CUST-CODE             PIC X(5).
     03  S-C-CUST-NAME             PIC X(20).
     03  S-C-CUST-ADDRESS       PIC X(60).
     03  S-C-CUST-BALANCE        PIC 9(7)V99.
     03  S-C-CRED-LIMIT               PIC 9(7).

 SD  WORK-FILE.
 01  WORK-REC.
     03     REC-TYPE                PIC X.
     03     CUST-CODE-KEY      PIC X(5).
     03                                     PIC X(96).
**************************************************************************
SORT-ROUTINE.
     SORT WORK-FILE
     ON ASCENDING KEY CUST-CODE-KEY
     USING VALID-FILE
     GIVING SORTED-FILE.
**************************************************************************
```

#### ↳ Re: Problem with a Sort Routine

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-02-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79qg9g$b0k@dfw-ixnews4.ix.netcom.com>`
- **References:** `<%%_v2.1121$QK4.1234@news2.giganews.com>`

```
You may THINK you are using a Micro Focus compiler - but you aren't.  You
are using the Fujitsu one - where this problem is reported about once a
month. Change the Select/Assign clause for the file specified in your SD
from a literal to an identifier and the message will go away (as it has
every other time this STUPID error on Fujitsu's part was reported).

NOTE: As I also state monthly, this means that the Fujitsu compiler is NOT
ANSI conforming and you should demand a "refund" from their false
advertising on this - until they fix it.
```

#### ↳ Re: Problem with a Sort Routine

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-02-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c18423@news3.us.ibm.net>`
- **References:** `<%%_v2.1121$QK4.1234@news2.giganews.com>`

```
as the message clearly states, you cannot use a filename (such as
workfile.dat) in the
assign clause. Only an identifier (no quotes) is allowed. Try to use simply
SORTFILE.
The assign clause is for documentation only anyway.

Jim wrote in message
>Compiler : Microfocus Personal Cobol for Windows
>OS : Win98
…[79 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
