[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL dynamic allocation (putenv) of output-file won't release extra space when closed

_4 messages · 4 participants · 2007-03 → 2007-05_

---

### COBOL dynamic allocation (putenv) of output-file won't release extra space when closed

- **From:** miggeman@gmail.com
- **Date:** 2007-03-12T03:06:34-07:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<1173693994.200977.61730@30g2000cwc.googlegroups.com>`

```

This is my first post and I hope you can bear with me since english is
not my
native language. Thank you in advance!

Cheers,
Miguel

Background info:
   z/OS version 01.07.01
   IBM Enterprise COBOL for z/OS version 3.4.0

   Enterprise COBOL for z/OS, Version 3 Release 4 Publications
        http://www-306.ibm.com/software/awdtools/cobol/zos/library/
   Language Reference Manual
        http://publibfp.boulder.ibm.com/epubs/pdf/igy3lr31.pdf


This is regarding file allocation from a COBOL program using a an
environmental
variable in the SELECT ... ASSIGN TO clause. That is, input and/or
output
from a COBOL program to a data set whose name has been dynamically
obtained.

I do not have any problem at all making the actual dynamic connection
between
my COBOL program and the reference to a physical file for reading or
writing.
I have so far with success managed to dynamically allocate files for
splitting
a large file into many several smaller files, all having the same
characteristics,
without any problems at all. Works like a charm.

I've used a normal COBOL program and called setenv for setting an
environmental
variable to contain a "DSN(...)" with all file attributes stated.



My problem lies in the allocation and the non-release of space
afterwards when the
file is closed in the program.

Normally when a file is created and written to from a cobol program,
the file
characteristics and attributes are defined in the COBOL program and in
the
JCL / procedure used to run the program.

Typically this is how a normal case would be solved without using an
environmental
variable in the SELECT ASSIGN -clause. The name in the ASSIGN is
stated with
the DD-statement:

//DYNAM    DD  DSN=P210.DEL1.TEST,
//             DISP=(NEW,CATLG,KEEP),
//             DCB=(RECFM=FB,LRECL=32),
//             SPACE=(CYL,(50,10),RLSE)

The definition above would see to that the file P210.DEL1.TEST is
created with
the possibility to accomodate one record or up to the limit of
SPACE=(CYL,(50,10,RLSE).
The RLSE parameter attached to the SPACE keyword makes sure that all
superflous,
unused space is "returned" to the system when the file is closed or
the program ended.
The quantity CYL, 50 and 10 extents was picked to show my problem but
one would think
that it should not be a problem in the scenario of not knowing in
advance if the resulting
output file will accomodate 10 records or hundreds of thousands of
them. A mechanism
corresponding to the JCL and space-keyword and the attribute "RLSE
would take care of that,
if I'm correct.



The corresponding solution using a COBOL program but instead
explicitly *not* defining
a corresponding DD-card to the SELECT ... ASSIGN defintion in the
program works fine, but
with the quirk that the created file's remaining / superflous space is
never released.

In my test COBOL program the environvent-variable DYNAM is set by
calling the PUTENV program
with the null-terminated string DYNAM=DSN(P210.DEL1.TEST) NEW CYL
SPACE(50,10) KEEP.

Nowhere have I found any mentioning of RLSE as a valid parameter to
use in the dynamic
allocation / use of QSAM files.

In the Language Reference Manual, I've read and re-read the sections

"4.2.3.1 Assignment name for environment variable"

where it says "[...]The contents of the environment variable are
checked at each OPEN
statement. If a file was dynamically allocated by a previous OPEN
statement and the
contents of the environment variable have changed since the previous
OPEN, then the
previous allocation is dynamically deallocated prior to dynamically
reallocating the
file using the options currently set in the environment variable."

Doesn't that include releasing the allocated, unused space?



"4.2.3.2 Environment variable contents for a QSAM file" does not
mention any specifics
about the release.





Results and examples of output
------------------------------

This is the result showing how much space the testfile has allocated
but not released.
Each record is 32 characters and the file contains 10 records. The 750
tracks
should be a much smaller number

  Menu  Options  View  Utilities  Compilers
Help
------------------------------------------------------------------------------
DSLIST - Data Sets Matching P210.DEL1.T*
Row 1 of 1
Command ===>                                                  Scroll
===> CSR

Command - Enter "/" to select action                  Tracks %Used XT
Device
-------------------------------------------------------------------------------
         P210.DEL1.TEST                                  750    1   1
3390
***************************** End of Data Set list
****************************




This is the result after issueing the FREE command on the file,
releasing the
unused but previously allocated space.

   Menu  Options  View  Utilities  Compilers
Help
 
------------------------------------------------------------------------------
 DSLIST - Data Sets Matching P210.DEL1.T*                        Free
completed
 Command ===>                                                  Scroll
===> CSR

 Command - Enter "/" to select action                  Tracks %Used
XT  Device
 
-------------------------------------------------------------------------------
          P210.DEL1.TEST                                   15    6
1  3390
 ***************************** End of Data Set list
****************************



This is the result after running the testprogram with the testfile
specifically
defined with DD-card and other attributes in the JCL:

//DYNAM    DD  DSN=P210.DEL1.TEST,
//             DISP=(NEW,CATLG,KEEP),
//             DCB=(RECFM=FB,LRECL=32),
//             SPACE=(CYL,(50,10),RLSE)


 DSLIST - Data Sets Matching P210.DEL1.TEST2
Row 1 of 1
 Command ===>                                                  Scroll
===> CSR

 Command - Enter "/" to select action                  Tracks %Used
XT  Device
 
-------------------------------------------------------------------------------
          P210.DEL1.TEST2                                  15    6
1  3390
 ***************************** End of Data Set list
****************************





The simple testprogram used to create the testfile with PUTENV and
directly with JCL
DD-card.

        IDENTIFICATION DIVISION.
        PROGRAM-ID. TESTALLC.
        ENVIRONMENT DIVISION.
        CONFIGURATION SECTION.
        SOURCE-COMPUTER. IBM-370.
        OBJECT-COMPUTER. IBM-370.
        INPUT-OUTPUT SECTION.
        FILE-CONTROL.
            SELECT  TESTFILE  ASSIGN DYNAM
                              FILE STATUS ST-DYNAMFILE.
        I-O-CONTROL.
        DATA DIVISION.
        FILE SECTION.
        FD  TESTFILE
            RECORDING MODE F.
        01  TEST-RECORD                 PIC X(32).

        WORKING-STORAGE SECTION.
        01  WORK-AREA.
            03  ST-DYNAMFILE            PIC 9(2).
            03  WS-TEST-RECORD          PIC X(32).

        01  SETENV-AREA.
            03  SETENV-RC               PIC S9(9) BINARY.
                88  SETENV-RC-OK                          VALUE 0.
            03  SETENV-POINTER          POINTER.
            03  SETENV-DATA             PIC X(64).
 
*-----------------------------------------------------------------
        PROCEDURE DIVISION.
 
*-----------------------------------------------------------------
            INITIALIZE WORK-AREA

            PERFORM SET-DYNAM-ENVAR
            PERFORM WRITE-TEST-FILE
            GOBACK.
 
*-----------------------------------------------------------------
        SET-DYNAM-ENVAR SECTION.
 
*-----------------------------------------------------------------

            INITIALIZE SETENV-AREA
            STRING
              'DYNAM=DSN(P210.DEL1.TEST) NEW CYL SPACE(50,10) KEEP'
              X'00'
              DELIMITED SIZE INTO SETENV-DATA

            SET SETENV-POINTER TO ADDRESS OF SETENV-DATA
            CALL 'PUTENV' USING BY VALUE SETENV-POINTER
                               RETURNING SETENV-RC

            EVALUATE TRUE
              WHEN SETENV-RC-OK
                CONTINUE
              WHEN OTHER
              DISPLAY "PUTENV FAILED"
              DISPLAY "RC=" SETENV-RC
              GOBACK
            END-EVALUATE
            EXIT.
 
*-----------------------------------------------------------------
        WRITE-TEST-FILE SECTION.
 
*-----------------------------------------------------------------
            OPEN OUTPUT TESTFILE
            DISPLAY 'OPEN FILESTATUS=' ST-DYNAMFILE

            PERFORM 10 TIMES
              MOVE FUNCTION CURRENT-DATE TO WS-TEST-RECORD
              WRITE TEST-RECORD FROM WS-TEST-RECORD
              DISPLAY 'WRITE FILESTATUS=' ST-DYNAMFILE
            END-PERFORM

            CLOSE TESTFILE
            DISPLAY 'CLOSE FILESTATUS=' ST-DYNAMFILE

            EXIT.
```

#### ↳ Re: COBOL dynamic allocation (putenv) of output-file won't release extra space when closed

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-03-12T16:08:36+00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<8WeJh.285631$gM1.135263@fe04.news.easynews.com>`
- **References:** `<1173693994.200977.61730@30g2000cwc.googlegroups.com>`

```
I am checking with some IBM sources on this, but one POSSIBLE solution would be 
to use an SMS storage class that automatically does what you want.  (I think SMS 
can handle RLSE - but I *know* it can put your dataset on "temporary" storage)
```

##### ↳ ↳ Re: COBOL dynamic allocation (putenv) of output-file won't release extra space when closed

- **From:** miguel.laiz@gmail.com
- **Date:** 2007-04-24T05:56:13-07:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<1177419373.768114.211630@t39g2000prd.googlegroups.com>`
- **In-Reply-To:** `<8WeJh.285631$gM1.135263@fe04.news.easynews.com>`
- **References:** `<1173693994.200977.61730@30g2000cwc.googlegroups.com> <8WeJh.285631$gM1.135263@fe04.news.easynews.com>`

```
On 12 Mar, 18:08, "William M. Klein" <wmkl...@nospam.netcom.com>
wrote:
> I am checking with some IBM sources on this, but one POSSIBLE solution would be
> to use an SMS storage class that automatically does what you want.  (I think SMS
…[3 more quoted lines elided]…
> Bill Klein

Hi Bill K,

first of all, my apologies for taking so long to comment on your
feedback. Long overdue vacation and trying deadlines came between my
initial question.

So far, I've managed to get the file I create to be BLOCKED by adding
the BLOCK CONTAINS 0 CHARACTERS clause in the program to the FD
descriptor.

I know that all the file attributes could probably be managed through
SMS and STORCLAS, MGMTCLAS and DATACLAS keywords. The documentation
says that they are supported. And that is what your answer, Bill, also
mentions. My problem is that the client I'm currently working for has
added a coupling between the second level in the DSN-name and a
MANAGEMENT class. So for example P211.DEL1.ABCD would create a file
that expires after 31 days and is deleted. In this example could be
DELx where x represents different expiry dates. I fully understand
that this is shop dependant.

The problem is that I can't seem to specify a DSN-name and also a
DATACLAS attribute in the string used as data with my environment-
variable to create a file. It is totally ignored. I thought that
DATACLAS would override it somehow. In the long run if I want to play
by the shop rules the only way might be to create a new set of DSN-
name levels (as
DEL in the example) but all have the BLOCKING set and the RELEASE of
unused allocated space.



I'm thinking of maybe calling using IKJTSOEV and then IKJEFTSR with a
ALLOC and FREE would be another way to go. I think there is BLOCK and
RLSE keywords that would let me save a lot of space when creating
small and large datasets.

Any thoughts, anyone?

Cheers
Miguel
```

#### ↳ Re: COBOL dynamic allocation (putenv) of output-file won't release extra space when closed

- **From:** Anne - Marie Jensen <anne-marie@husetjensen.dk>
- **Date:** 2007-05-03T09:31:48-07:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<1178209908.592119.280780@q75g2000hsh.googlegroups.com>`
- **In-Reply-To:** `<1173693994.200977.61730@30g2000cwc.googlegroups.com>`
- **References:** `<1173693994.200977.61730@30g2000cwc.googlegroups.com>`

```
On 12 Mar., 12:06, migge...@gmail.com wrote:
> This is my first post and I hope you can bear with me since english is
> not my
…[20 more quoted lines elided]…
>

Hej.
Sorry to be so late with an answer.

In Zos there is a built in module, that you can call called BPXWDYN.
I have used it a lot, and it is wery easy.

Look here: http://www.google.dk/search?hl=da&q=bpxwdyn&meta=lr%3Dlang_da%7Clang_en%7Clang_no%7Clang_sv

Just be sertain, that the input parameter you send to this module, is
null terminated (x('00')).

If you want, i can send you som examples of how to use it.

Best regards
Anne - Marie
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
