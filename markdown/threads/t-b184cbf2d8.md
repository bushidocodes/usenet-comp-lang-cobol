[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Request re COBOL program name.

_3 messages · 3 participants · 1995-09_

---

### Request re COBOL program name.

- **From:** "reg..." <ua-author-4631382@usenetarchives.gap>
- **Date:** 1995-09-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1995Sep14.094213.1@csc.canterbury.ac.nz>`

```
A simple request:
How can an executing VAX COBOL program determine the
directory and file title of its own .EXE file?

ie. If PAYJOB is a COBOL program and its .EXE file is
say [COMPANY.DAILY.TASK]PAYJOB.EXE then when the program
is running what particular routine can be called in
order to return the string
"[COMPANY.DAILY.TASK]PAYJOB.EXE".

Thankyou,
Brad Henry.
```

#### ↳ Re: Request re COBOL program name.

- **From:** "jhar..." <ua-author-1934101@usenetarchives.gap>
- **Date:** 1995-09-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b184cbf2d8-p2@usenetarchives.gap>`
- **In-Reply-To:** `<1995Sep14.094213.1@csc.canterbury.ac.nz>`
- **References:** `<1995Sep14.094213.1@csc.canterbury.ac.nz>`

```
Try using the GETJPI system service.

BUT.. VAX Cobol is a linked language and cannot CALL another .EXE, it can
only CALL another program that has been linked into the .EXE. You can use
LIB$DO_COMMAND to run another .EXE.

John Hartnett
```

#### ↳ Re: Request re COBOL program name.

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1995-09-14T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b184cbf2d8-p3@usenetarchives.gap>`
- **In-Reply-To:** `<1995Sep14.094213.1@csc.canterbury.ac.nz>`
- **References:** `<1995Sep14.094213.1@csc.canterbury.ac.nz>`

```
In article <199··.@csc··c.nz>,
reg··.@csc··c.nz wrote:
›
› How can an executing VAX COBOL program determine the directory and file title
› of its own .EXE file?

$ type demo.cob
IDENTIFICATION DIVISION.
PROGRAM-ID. DEMO.
ENVIRONMENT DIVISION.
* PARAMETER SECTION.
REPLACE
==IMAGNAME-MAX== BY ==255==
.
DATA DIVISION.
WORKING-STORAGE SECTION.


* Each item in the SYS$GETJPI item list is a data structure that makes one
* request to SYS$GETJPI. The first word is the length of the buffer that we
* are providing to SYS$GETJPI for its output. The second word is the item code,
* which specifies the operation that we wish SYS$GETJPI to perform. (In this
* case, we are asking SYS$GETJPI to return our image name.) Following these
* two words is a longword pointer to the buffer we are providing, and a longword
* pointer to a word in which SYS$GETJPI will write the length of whatever it
* wrote into the buffer we are providing. The item list is terminated by a
* longword of zero. (In this case, there is only one item on the item list.)

01 WS-SYS$GETJPI-ITMLST.

05 FILLER.
10 FILLER PIC S9(04) COMP VALUE IMAGNAME-MAX.
10 FILLER PIC S9(04) COMP VALUE EXTERNAL JPI$_IMAGNAME.
10 FILLER POINTER VALUE REFERENCE WS-IMAGNAME.
10 FILLER POINTER VALUE REFERENCE WS-IMAGNAME-LEN.

05 FILLER PIC S9(09) COMP VALUE ZERO.


01 FILLER.

05 WS-IMAGNAME-LEN PIC S9(04) COMP VALUE ZERO.
05 WS-IMAGNAME PIC X(IMAGNAME-MAX) VALUE SPACES.
05 FILLER PIC X(01) VALUE LOW-VALUE.


01 WS-SYS$PUTMSG-MSGVEC.
05 FILLER PIC S9(04) COMP VALUE +0001.
05 FILLER PIC X(02) VALUE X'000F'.
05 WS-VMS-COND PIC S9(09) COMP VALUE ZERO.


PROCEDURE DIVISION.

1000-MAIN.

CALL "SYS$GETJPIW"
USING OMITTED
OMITTED
OMITTED
BY REFERENCE WS-SYS$GETJPI-ITMLST
OMITTED
OMITTED
OMITTED
GIVING WS-VMS-COND.

IF WS-VMS-COND IS FAILURE
THEN CALL "SYS$PUTMSG"
USING BY REFERENCE WS-SYS$PUTMSG-MSGVEC
OMITTED
OMITTED
OMITTED
ELSE DISPLAY WS-IMAGNAME(1:WS-IMAGNAME-LEN)
END-IF.


9999-EXIT.
STOP RUN.
$ cobol demo.cob
$ link demo.obj
$ run demo.exe
$1$DUA0:[CWESTBURY.NEWS.COBOL]DEMO.EXE;1
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
