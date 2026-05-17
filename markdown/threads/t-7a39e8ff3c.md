[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL on HP3000 & KSAMXL file

_2 messages · 2 participants · 1997-05_

---

### COBOL on HP3000 & KSAMXL file

- **From:** "yong..." <ua-author-17073148@usenetarchives.gap>
- **Date:** 1997-05-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970523215001.RAA25780@ladder01.news.aol.com>`

```

Fellow COBOL programmers,

I just started a job requiring COBOL knowledge, so I am learning a lot.
Can someone please e-mail me a program showing how they are accessing a
KSAMXL file using COBOL on an HP3000 setup? We are running MPE 5.5.

Specifically, I would like to see examples of the intrinsics at work,
FOPEN, FCLOSE, FREAD etc etc. My KSAMXL file has only one key. Including
code from the working-storage section showing the variables used would
also be very helpful. Thanks very very very much!!

yon··.@pac··l.net
(Eben Yong)
```

#### ↳ Re: COBOL on HP3000 & KSAMXL file

- **From:** "paul krikorian" <ua-author-6589542@usenetarchives.gap>
- **Date:** 1997-05-26T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7a39e8ff3c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970523215001.RAA25780@ladder01.news.aol.com>`
- **References:** `<19970523215001.RAA25780@ladder01.news.aol.com>`

```

YongLove wrote:
› 
› Fellow COBOL programmers,
…[8 more quoted lines elided]…
› also be very helpful.  Thanks very very very much!!

Eben,

You do not need to use the FOPEN, FCLOSE, etc intrinsics in order to
access
a KSAMXL file, in fact, I would not recommend it. Just stay with the
standard
COBOL file access syntax and you will be able to read and write to the
file
with no problems. Below is some simple COBOL to access a KSAM file:

INPUT-OUTPUT SECTION.
FILE-CONTROL.

SELECT OBJECT-CONV-FILE
ASSIGN TO 'OBJFL'
ORGANIZATION IS INDEXED
ACCESS MODE IS DYNAMIC
RECORD KEY IS OLD-OBJ-KEY
FILE STATUS IS IO-STATUS.

DATA DIVISION.
FILE SECTION.

FD OBJECT-CONV-FILE.
01 OBJECT-CONV-REC.
05 FILLER PIC X.
05 OLD-OBJ-KEY PIC X(4).
05 FILLER PIC X.
05 NEW-OBJ-CODE PIC X(4).

01 IO-STATUS.
05 STATUS-KEY-1 PIC X.
88 EOF-STATUS VALUE '1'.
88 NOT-FOUND VALUE '2'.
88 CKERROR VALUE '9'.
05 STATUS-KEY-2 PIC X.
88 DUPLICATE-KEY VALUE '2'.
01 IO-STAT REDEFINES IO-STATUS PIC XX.
88 IO-SUCCESSFUL VALUE '00'.

PROCEDURE DIVISION.

OPEN INPUT OBJECT-CONV-FILE.
...
MOVE '00' TO IO-STATUS.
MOVE '1234' TO OLD-OBJ-KEY.
READ OBJECT-CONV-FILE.
IF IO-SUCCESSFUL THEN
...
ELSE
...
END-IF.

CLOSE OBJECT-CONV-FILE.
STOP RUN.

Hope this helps.
Paul Krikorian                   | Internet: pa··.@uhu··d.edu
Coast Community College District |           (or pa··.@cc··d.edu)
1370 Adams Ave.                  |    Voice: (714) 438-4621     
Costa Mesa, CA 92626, USA        |      Fax: (714) 432-5062
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
