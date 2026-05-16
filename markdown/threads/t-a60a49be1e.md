[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# open input afile

_11 messages · 8 participants · 2002-12_

---

### open input afile

- **From:** klaus.duttle@online.de (m8java)
- **Date:** 2002-12-20T07:03:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba4d0b76.0212200703.2808eda4@posting.google.com>`

```
Hi Cobol cracks,

I want to port and run a cobol host programm under AIX with
Cobol Set for AIX 1.1. Many modifikations and corrections
I have already done. On the host platform the program runs
without any problem but under AIX there are some trouble
with the statement "open input afile"

I've tried many variants in the select clause of the
FILE-CONTROL area and in the FILE-SECTION of the DATA DIVISION.

The original host code looks like

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT  SAP  ASSIGN    TO  AFILE
                FILE STATUS IS STATUS-BYTES.
       ...
       DATA DIVISION.
       FILE SECTION.
       FD  AFILE
           LABEL    RECORD   STANDARD
               RECORDING MODE    IS F.
       ...
           OPEN  OUTPUT LISTE1
           DISPLAY 'Status-Bytes is: ' STATUS-BYTES


All my efforts result in an error-code 35 or 95
in STATUS-BYTES.

Help and comments are welcome.
```

#### ↳ Re: open input afile

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2002-12-20T15:18:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fdrUCAAXTzA+EwTh@ld50macca.demon.co.uk>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com>`

```
In article <ba4d0b76.0212200703.2808eda4@posting.google.com>, m8java
<klaus.duttle@online.de> writes
>Hi Cobol cracks,
>
…[29 more quoted lines elided]…
>Help and comments are welcome.
This should be:

SELECT AFILE ASSIGN TO 'file-name-of-your-choice'.
```

#### ↳ Re: open input afile

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-20T09:36:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atvdec$fkl$1@slb6.atl.mindspring.net>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com>`

```
What have you done to "associate" the pseudo-DDName
    AFILE
with your physical file?  Just as JCL does this on the mainframe, there are
a variety of ways to do this under AIX.
```

##### ↳ ↳ Re: open input afile

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-12-20T09:38:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atvdh5$9q1$1@slb6.atl.mindspring.net>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com> <atvdec$fkl$1@slb6.atl.mindspring.net>`

```
Also, the subject of your note says "input afile" - while your code snippet
says "OPEN OUTPUT".  If it is an input file, you may need to check its
permission level.
```

#### ↳ Re: open input afile

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2002-12-20T21:26:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021220162604.03151.00000508@mb-mq.aol.com>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com>`

```
I'd say that you have several associations confused.

In article <ba4d0b76.0212200703.2808eda4@posting.google.com>,
klaus.duttle@online.de (m8java) writes:

>I want to port and run a cobol host programm under AIX with
>Cobol Set for AIX 1.1. Many modifikations and corrections
…[12 more quoted lines elided]…
>                FILE STATUS IS STATUS-BYTES.

You are SELECTing SAP, this should be your FD name.
The ASSIGN to AFILE is providing the JCL DD-Name to link.
>       ...
>       DATA DIVISION.
>       FILE SECTION.

Should this be SAP ? or do you change your SELECT Statement.

>       FD  AFILE
>           LABEL    RECORD   STANDARD
>               RECORDING MODE    IS F.
>       ...

Where is this file Defined?  Where is the FD for LISTE1?
Or should this be the FD you have shown SAP 
or the name you referenced in your message  - AFILE


>           OPEN  OUTPUT LISTE1
>           DISPLAY 'Status-Bytes is: ' STATUS-BYTES
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: open input afile

- **From:** klaus.duttle@online.de (m8java)
- **Date:** 2002-12-22T03:25:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ba4d0b76.0212220325.35d15667@posting.google.com>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com> <20021220162604.03151.00000508@mb-mq.aol.com>`

```
sff5ky@aol.comxxx123 (Sff5ky) wrote in message news:<20021220162604.03151.00000508@mb-mq.aol.com>...
> I'd say that you have several associations confused.
 
This is correct. I'm sorry but I have modified and confused
the original Cobol code. My physical file is a data file
from a SAP-application running on the same AIX machine.
In the SELECT clause the real assignment name is SAP and
not AFILE. I choose AFILE because this name isn't linked
to a famous german campany. I hate spam and commercials
in newsgroups.

How I can read the data saved in "/usr/cobol/SAP" in
the AIX filesystem. I believe the file contains several
thousand records with fixed length. The File Description
Entry in the DATA DIVISION follows a data group for the
definition of the record structure in the data file.
Here is correct code snippet:

       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT  AFILE  ASSIGN    TO  SAP
                FILE STATUS IS STATUS-BYTES.
       ...
       DATA DIVISION.
       FILE SECTION.
       FD  AFILE
           LABEL    RECORD   STANDARD
               RECORDING MODE    IS F.
       01  SAP-SATZ.
           05                    PIC X(001).
           05 SAP-SATZ1.
              10                    PIC X(006).
              10 SAP-KENNUNG        PIC X(004).
              10 SAP-PROGNAME       PIC X(008).
              10 SAP-HDLNR          PIC X(005).
              10 SAP-BELNR          PIC X(006).
       ...
           OPEN  INPUT AFILE
           DISPLAY 'Status-Bytes is: ' STATUS-BYTES

After "OPEN INPUT AFILE" the STATUS-BYTES always shows
an error code 35 or 95. In the IBM documentation for
AIX-Cobol (Cobol Language Reference) these error codes
are defined as:

       35 An OPEN statement with the INPUT, I-O, or
          EXTEND phrase was attempted on a non-optional
          file that was not present.
       95 For all files, except QSAM:
          Invalid or incomplete file information.

Thanks for your help.
```

###### ↳ ↳ ↳ Re: open input afile

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-12-22T08:26:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E05E7AB.9040002@Sympatico.ca>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com> <20021220162604.03151.00000508@mb-mq.aol.com> <ba4d0b76.0212220325.35d15667@posting.google.com>`

```
I do not know the AIX file system, but on most machines, the code below 
uses SAP as a data name.  In effect, you would either re-write the 
select clause as

           SELECT  AFILE  ASSIGN    TO  "/usr/cobol/SAP"
                FILE STATUS IS STATUS-BYTES.

or define the word SAP in working storage

           SELECT  AFILE  ASSIGN    TO  SAP
                FILE STATUS IS STATUS-BYTES.
and in working storage:
	01 SAP			PICTURE X(25) VALUE "/USR/COBOL/SAP".

Since your program is compiling, I suspect that the data name SAP is defined, but defined wrong.  You may have to put a drive name or computer name on the beginning of the literal if the drive your program is on is not the same drive as the drive your data is on (IE: "A:\user ...  or \\machinename\user\ ...).

As I say, I am not familiar with your specific platform, so I may be out to lunch here, but it is what I would check first.

Donald


   
m8java wrote:

>sff5ky@aol.comxxx123 (Sff5ky) wrote in message news:<20021220162604.03151.00000508@mb-mq.aol.com>...
>  
…[56 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: open input afile

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-22T16:36:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0SlN9.37254$6H6.1089618@twister.austin.rr.com>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com> <20021220162604.03151.00000508@mb-mq.aol.com> <ba4d0b76.0212220325.35d15667@posting.google.com>`

```
Could easily be a coupe of things;

(1) Whatever environment variable you are using to define SAP could be pointing to the wrong place. The way you have "SAP" defined
in your SELECT clause will cause the runtime to find an environment variable named "SAP" and substitute the value for that into the
OPEN. Try hardcoding the file in the select, using something like ... ASSIGN TO "/usr1/SAP/files/afile"  (using the real path and
file name of course.)

(2) The file you are trying to open may not be one of the types that COBOL recognizes, though it looks to be pretty much a flat file
(i.e. Sequential) from your definition. If it *is* a sequential file, it has to have particular headers on it that the COBOL
compiler runtime inserts. If, as is more likely, it is an AIX sequential file, define the file as LINE SEQUENTIAL and I expect it
will start working.

Just a personal idiosyncrasy, but I always fully define files in the SELECT. If you had fully defined it, we would probably be able
to tell you more exactly what the problem is. :)

-Paul

"m8java" <klaus.duttle@online.de> wrote in message news:ba4d0b76.0212220325.35d15667@posting.google.com...
> sff5ky@aol.comxxx123 (Sff5ky) wrote in message news:<20021220162604.03151.00000508@mb-mq.aol.com>...
> > I'd say that you have several associations confused.
…[50 more quoted lines elided]…
> .
```

###### ↳ ↳ ↳ Re: open input afile

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2002-12-22T18:29:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20021222132929.17913.00000603@mb-mv.aol.com>`
- **References:** `<ba4d0b76.0212220325.35d15667@posting.google.com>`

```
In article <ba4d0b76.0212220325.35d15667@posting.google.com>,
klaus.duttle@online.de (m8java) writes:

>
>After "OPEN INPUT AFILE" the STATUS-BYTES always shows
…[9 more quoted lines elided]…
>

This would then be pointing to the connector in your JCL or whatever
acts as your Job Control Language in AIX.
In JCL you would have a DDname that points to the actual SAP file.
//SAP  DD DSN=usr.cobol.sap, <all the other related attributes>
In PC COBOL you would define in the FD an ATTRIBUTE TITLE IS "/usr/cobol/sap"
or TITLE is WS-FILENAME
and WS-FILENAME PICx(nn) value "/usr/cobol/sap"
or in the ASSIGN statement as ASSIGN TO "/usr/cobol/sap".
```

###### ↳ ↳ ↳ Re: open input afile

- **From:** ctimmer@gci.net (Curt Timmerman)
- **Date:** 2002-12-23T20:01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns92ED70123D1Ectimmermanacsalaskac@10.136.100.32>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com> <20021220162604.03151.00000508@mb-mq.aol.com> <ba4d0b76.0212220325.35d15667@posting.google.com>`

```
klaus.duttle@online.de (m8java) wrote in
<ba4d0b76.0212220325.35d15667@posting.google.com>: 

>sff5ky@aol.comxxx123 (Sff5ky) wrote in message
>news:<20021220162604.03151.00000508@mb-mq.aol.com>... 
…[51 more quoted lines elided]…
>.

IF 'SAP' is a reference to a data field use (note USING key word):
SELECT  AFILE  ASSIGN    USING  SAP

Otherwise, prior to executing you application set the 'SAP' environment 
variable:
export SAP="/usr/cobol/SAP"

These are both AIX Cobol constructs.
```

#### ↳ Re: open input afile

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-12-21T07:21:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E04167B.28996C7F@Azonic.co.nz>`
- **References:** `<ba4d0b76.0212200703.2808eda4@posting.google.com>`

```
m8java wrote:

> without any problem but under AIX there are some trouble
> with the statement "open input afile"
…[18 more quoted lines elided]…
> in STATUS-BYTES.

I think that this is not what the original code looks like, the SELECT
is probably:

        SELECT AFILE ASSIGN SAP

then this will match with 'FD AFILE' and 'OPEN INPUT AFILE'.

The file status indicates that it can't find the file.  This is because
you haven't told it what the actual name of the file is.  On the
mainframe there will be a run-card that specifies the actual filename to
use for 'AFILE'.  You need to find out how to specify this in AIX,
either externally in some configuration file or environment entry, or
within the program such as:

       SELECT AFILE ASSIGN "/livedata/host/AFILE.DAT"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
