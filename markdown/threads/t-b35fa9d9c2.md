[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ILBOWAT0 Information

_2 messages · 2 participants · 2001-01_

---

### ILBOWAT0 Information

- **From:** Dan Dirkse <iuvo@attglobal.net>
- **Date:** 2001-01-03T21:51:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A53E516.68F15E2B@attglobal.net>`

```
Hi:
I understand that the IBM supplied routine ILBOWAT0 can be called by a
program to go to 'sleep'.  Does anyone know where this module is
documented?
Thanks,
Dan Dirkse
Iuvo Technologies, Inc.
```

#### ↳ Re: ILBOWAT0 Information

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 2001-01-04T08:07:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<931avf$o8k$1@nnrp1.deja.com>`
- **References:** `<3A53E516.68F15E2B@attglobal.net>`

```
In article <3A53E516.68F15E2B@attglobal.net>,
  iuvo@attglobal.net wrote:
> Hi:
> I understand that the IBM supplied routine ILBOWAT0 can be called by a
…[5 more quoted lines elided]…
>

AFAIK, ILBOWAT0 dates back to old OS/VS COBOL days. You might find a
documentation in some 20 years old manuals. I never found descriptions
about ILBOWAT0 in the current IBM documentation. The module resides in
the COB2LIB as well as in the most current SCEERUN.

A disassembly of ILBOWAT0 shows SVC 47, so I would not use it in a CICS
environment. SVC 47 is the ASSEMBLER macro STIMER, you find it
documented in the manual 'OS/390 V2R10.0 MVS Assembler Services
Reference', Document Number GC28-1910-11, online at:
http://www.s390.ibm.com:80/bookmgr-cgi/bookmgr.cmd/BOOKS/IEA1A741


BTW, ILBOWAT0 is an ALIAS of ILBOWAT:

ILBOWAT  CSECT
         ENTRY ILBOWAT0
         DC    H'0'
ILBOWAT0 BC    15,4(0,R15)
         STM   R14,R12,96(R13)
...

If you call ILBOWAT instead of ILBOWAT0, you get an abend S0C1 because
of the invalid instruction H'0'!

I once wrote the following COBOL sample program (note the DATA(24)
compiler option, ILBOWAT0 has AMODE(24)):

       CBL DATA(24)
       IDENTIFICATION DIVISION.
       PROGRAM-ID. WAIT.
      ***
      *** DELAY IN COBOL VIA CALL TO ILBOWAT0
      ***
      *** USAGE:
      *** //S1 EXEC PGM=WAIT,PARM=NNNN
      *** NNNN IS A NUMBER IN THE RANGE OF 0001 TO 9999 SECONDS
      ***
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  DELAY-AMT               PIC S9(9) COMP.
       01  ILBOWAT0                PIC X(8) VALUE 'ILBOWAT0'.
       01  CURRENT-TIME            PIC 9(8).
       LINKAGE SECTION.
       01  PARAMETER-TO-MAIN.
         05 PARM-LENGTH PIC S9(4) COMP.
         05 PARM-TEXT   PIC X(100).
         05 PARM-REDEF REDEFINES PARM-TEXT.
          10 PARM-NUMERIC PIC 9999.
          10 FILLER       PIC X(94).
       PROCEDURE DIVISION USING PARAMETER-TO-MAIN.
       MAIN SECTION.
           MOVE PARM-NUMERIC TO DELAY-AMT
           ACCEPT CURRENT-TIME FROM TIME
           DISPLAY 'TIME OF DAY BEFORE ILBOWAT0: ', CURRENT-TIME
      *
           CALL ILBOWAT0 USING DELAY-AMT
      *
           ACCEPT CURRENT-TIME FROM TIME
           DISPLAY 'TIME OF DAY AFTER ILBOWAT0 : ', CURRENT-TIME
           GOBACK.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
