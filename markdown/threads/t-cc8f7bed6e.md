[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can't sort variable length records using mfsort

_4 messages · 2 participants · 2007-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Can't sort variable length records using mfsort

- **From:** "ari" <unikoski@yahoo.com>
- **Date:** 2007-01-16T08:28:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1168964899.292481.225690@s34g2000cwa.googlegroups.com>`

```
I am evaluating the use of microfocus' mfsort under linux.

I created a variable length file with a cobol program as follows:

       IDENTIFICATION DIVISION.
       PROGRAM-ID. TESTER.

*=================================================================
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT  TEST-FILE
           ORGANIZATION SEQUENTIAL
           ASSIGN TO EXTERNAL VBFILE.
       DATA DIVISION.
       FILE SECTION.
       FD  TEST-FILE
           DATA RECORD IS TST-REC
           RECORDING MODE V
           RECORD IS VARYING IN SIZE FROM 1 TO 32760
           DEPENDING ON LRECL
           BLOCK CONTAINS 0.
       01  TST-REC.
           05 TST-DATA        PIC X(32760).
       WORKING-STORAGE SECTION.
       01 KUKU PIC X(10).
       01 DISP-TEST.
          05 PS99C            PIC S9(9) COMP.
          05 PS94             PIC S9(4).
          05 PCOMP-2          COMP-2.
       01 MISC.
          05 LRECL            PIC 9(5)    comp    value 0.
          05 II               PIC 9(4) COMP.
       01 TTT.
          05 TEST-DATA-R.
             10 FILLER PIC X(20) VALUE 'ABRA'.
             10 FILLER PIC X(20) VALUE 'CADABRA'.
             10 FILLER PIC X(20) VALUE 'BILLY'.
             10 FILLER PIC X(20) VALUE 'ZULU'.
             10 FILLER PIC X(20) VALUE 'AAA'.
          05 TEST-DATA REDEFINES TEST-DATA-R.
             10 TEST-DATA-DATA PIC X(20) OCCURS 5 TIMES.
          05 TEST-LEN-R.
             10 FILLER PIC 9(4) COMP VALUE 4.
             10 FILLER PIC 9(4) COMP VALUE 7.
             10 FILLER PIC 9(4) COMP VALUE 5.
             10 FILLER PIC 9(4) COMP VALUE 4.
             10 FILLER PIC 9(4) COMP VALUE 3.
          05 FILLER REDEFINES TEST-LEN-R.
             10 TEST-LEN PIC 9(4) COMP OCCURS 5 TIMES.
      **************************************************************
       PROCEDURE DIVISION.
      **************************************************************
       A-PROGRAM-CONTROL             SECTION.
      *----------------------------------------------------------------
           OPEN OUTPUT TEST-FILE.
           MOVE "ABCDEFGHIJKLMNOPQRSTUVWXYZ" TO  TST-DATA.
           PERFORM VARYING II FROM 1 BY 1 UNTIL II > 20
               MOVE II TO LRECL
               WRITE TST-REC
           END-PERFORM


           PERFORM VARYING II FROM 1 BY 1 UNTIL II > 5
              MOVE TEST-DATA-DATA(II) TO TST-DATA
              MOVE TEST-LEN(II) TO LRECL
              WRITE TST-REC
           END-PERFORM

           CLOSE TEST-FILE.
       .

The programs runs happily, and creates a file called VBFILE with the
128 byte header as described in microfocus documentation.

I then try and sort the file using mfsort - I tried doing:

mfsort use VBFILE ORG SQ RECORD V,1,100 GIVE out.out RECORD V,1,100

and got the following error message:

SORT013U: I/O error on dataset 'VBFILE'
SORT014U: Status = 9/139
SORT020U: SORT(EXTSM) failed - sort engine status = 9/139

I have tried lots of variations on the command, but to no avail - all I
ever get is the above message. What am I doing wrong?
```

#### ↳ Re: Can't sort variable length records using mfsort

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-01-16T12:30:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12qq33lb39cn745@corp.supernews.com>`
- **References:** `<1168964899.292481.225690@s34g2000cwa.googlegroups.com>`

```

"ari" <unikoski@yahoo.com> wrote in message
news:1168964899.292481.225690@s34g2000cwa.googlegroups.com...
> I am evaluating the use of microfocus' mfsort under linux.
>
> I created a variable length file with a cobol program as follows:

[snip]
>            RECORD IS VARYING IN SIZE FROM 1 TO 32760
[snip]

> The programs runs happily, and creates a file called VBFILE with the
> 128 byte header as described in microfocus documentation.
…[12 more quoted lines elided]…
> ever get is the above message. What am I doing wrong?

The record size doesn't match the file.

I ran it using MFSORT under DOS and, while
I got it to run the results were confusing, because
the output file was shorter than the input.

I broke it into three parts:
    USE VBFILE RECORD (V,1,32760)
    GIVE OUT
    SORT FIELDS (1,100,CH,A)
```

##### ↳ ↳ Re: Can't sort variable length records using mfsort

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-01-16T14:45:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12qqavff1vht10@corp.supernews.com>`
- **References:** `<1168964899.292481.225690@s34g2000cwa.googlegroups.com> <12qq33lb39cn745@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:12qq33lb39cn745@corp.supernews.com...
>
> "ari" <unikoski@yahoo.com> wrote in message
…[34 more quoted lines elided]…
>     SORT FIELDS (1,100,CH,A)

I corrected the file size problem by giving MFSORT
more memory; but the records were not properly
sequenced. This may be because the sort key includes
areas to do not exist in any record.

When I changed the files to line sequential (program and
sort), everything worked as expected.
```

###### ↳ ↳ ↳ Re: Can't sort variable length records using mfsort

- **From:** "ari" <unikoski@yahoo.com>
- **Date:** 2007-01-17T02:23:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1169029398.206134.67810@38g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<12qqavff1vht10@corp.supernews.com>`
- **References:** `<1168956852.973313.98780@11g2000cwr.googlegroups.com> <1168958596.394741.280240@51g2000cwl.googlegroups.com> <3r-dnTjbsJ-V6DDYnZ2dnUVZ_q6vnZ2d@centurytel.net>`

```
Thanks Rick - you found my error!
The unix command line that gave perfect results was:


mfsort use VBFILE ORG SQ RECORD V,1,32760 GIVE out.out SORT
'FIELDS=(1,100,CH,A)' RECORD V,1,32760

It never occurred to me that it would care that the definition of the
maximum record length would need to be exactly the same as in the cobol
- I thought it only needed the maximum record length that there
physically was in the file. A silly assumption on my part.

Ari
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
