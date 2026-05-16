[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New to the cobol world!! Newbie Question.

_3 messages · 3 participants · 2001-01_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### New to the cobol world!! Newbie Question.

- **From:** "MadG" <patrick4133@hotmail.com>
- **Date:** 2001-01-27T16:18:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lxCc6.879$KP3.391438@news3.rdc1.on.home.com>`

```
Hi, I am just learning cobol and I mean JUST learning cobol!

Anyway I have a problem and can't seem to get it working.

This is the error message I get:.

COBOL I/O error 48,02 on DOGG-FILE file DOGG.TXT.
COBOL I/O error  at line 67 in DOG-LICENSE (C:\WINDOWS\DESKTOP\C.COB)
compiled
01/01/27 11:06:44.

I can't seem to get what's wrong, I am hoping someone can help me out?

I've posted the whole program code below, If this isn't ok etiquette for the
form then please accept my apologies.

To any help, Thanks in advance!

Pat :)




    IDENTIFICATION DIVISION.

 PROGRAM-ID. DOG-LICENSE.

 ENVIRONMENT DIVISION.

 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
  SELECT DOGG-FILE
   ASSIGN TO "DOGG.TXT"
   ORGANIZATION IS LINE SEQUENTIAL.

 DATA DIVISION.
 FILE SECTION.

 FD DOGG-FILE
  RECORD CONTAINS 44 CHARACTERS.

 01 DOGG-RECORD.
    05 LICENSENO.
       10 PROV  PIC X(2).
       10 FOUR-DIGIT PIC 9(4).
    05 NAME  PIC X(20).
    05 BANK  PIC X(3).
    05 BREED  PIC X(13).
    05 FEE  PIC X(2).

 WORKING-STORAGE SECTION.
 01 WORK-SPACE.
    05 LAST-NUM  PIC 9(4).
    05 CONTIN  PIC X(1).
    05 START-PROG  PIC X(1).
    05 KOUNT  PIC 9(3).


 PROCEDURE DIVISION.

 PRODUCE-DOG-FILE.
  PERFORM 101-OPTION-TO-START
  IF START-PROG = "y" OR "Y"
   PERFORM 105-START-UP-JOB
   PERFORM 240-CONTINUE-ENTRY
   PERFORM UNTIL CONTIN = "n" OR "N"
    PERFORM 110-PROCESSING-JOB
    PERFORM 120-WRAP-UP-JOB
   END-PERFORM
   PERFORM 270-REPORT-SUMMARY
  END-IF
  STOP RUN.

 105-START-UP-JOB.
  PERFORM 205-ANNOUNCE-JOB
  OPEN OUTPUT DOGG-FILE
  PERFORM 220-CALL-LAST-NUMBER
  PERFORM 230-INITIALIZE-DATA.

 110-PROCESSING-JOB.
  PERFORM 250-INCREMENT-DIGIT
  PERFORM 260-ACCEPT-INPUT-FIELDS
  WRITE DOGG-RECORD
  PERFORM 240-CONTINUE-ENTRY.

 120-WRAP-UP-JOB.
  CLOSE DOGG-FILE.


 205-ANNOUNCE-JOB.
  DISPLAY " " ERASE
  DISPLAY " This program will create a file containing".

 101-OPTION-TO-START.
  Display " YOU KNOW HAVE THE OPTION TO BEGIN THE"
  Display " PLEASE ENTER y FOR YES, n FOR NO. "
  ACCEPT START-PROG.

 220-CALL-LAST-NUMBER.
  DISPLAY " "
  Display " PLEASE ENTER THE LAST 4 DIGIT NUMBER ENTERED"
  ACCEPT LAST-NUM NO BEEP PROMPT.


 230-INITIALIZE-DATA.
  MOVE LAST-NUM TO FOUR-DIGIT
  MOVE ZERO TO BANK
  MOVE ZERO TO KOUNT
  MOVE ZERO TO START-PROG.



 240-CONTINUE-ENTRY.
  DISPLAY " WOULD YOU LIKE TO CONTINUE ENTERING DATA?"
  Display " PLEASE ENTER y FOR YES, n FOR NO. "
  ACCEPT CONTIN NO BEEP PROMPT.

 250-INCREMENT-DIGIT.
  ADD 1 TO FOUR-DIGIT
  ADD 1 TO KOUNT.

 260-ACCEPT-INPUT-FIELDS.
  DISPLAY " "
  DISPLAY " PLEASE ENTER A TWO (2) CHARACTER"
  DISPLAY " PROVINCE CODE AND PRESS ENTER."
  ACCEPT PROV NO BEEP PROMPT
  DISPLAY " "
  DISPLAY " PLEASE ENTER THE OWNER'S NAME. "
  ACCEPT NAME NO BEEP PROMPT
  DISPLAY " "
  DISPLAY " PLEASE ENTER THE BREED OF DOG."
  ACCEPT BREED NO BEEP PROMPT
  DISPLAY " "
  DISPLAY " PLEASE ENTER THE FEE."
  ACCEPT FEE NO BEEP PROMPT.

 270-REPORT-SUMMARY.
  DISPLAY " " ERASE
  DISPLAY " YOU BEGAN THIS PROGRAM WITH THE NUMBER: "
  DISPLAY LAST-NUM
  DISPLAY " "
  DISPLAY " YOU HAVE PROCESSED " KOUNT " RECORDS."
  DISPLAY "  "
  DISPLAY " YOU WILL NEED TO WRITE DOWN THIS NUMBER "
  DISPLAY "NEXT TIME YOU RUN THIS PROGRAM: " FOUR-DIGIT.
```

#### ↳ Re: New to the cobol world!! Newbie Question.

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-01-27T19:43:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OxFc6.1244$KP3.714640@news3.rdc1.on.home.com>`
- **References:** `<lxCc6.879$KP3.391438@news3.rdc1.on.home.com>`

```
Assuming your compiler is returning ANSI file status codes, then a 48 means
an attempt was made to write to a file that was not opened, or opened in the
wrong mode.

If you look carefully at your code you will see something unintended is
happening to your file in your processing loop. You'll probably smack
yourself in the forehead when you see what it is.

- Karl

"MadG" <patrick4133@hotmail.com> wrote in message
news:lxCc6.879$KP3.391438@news3.rdc1.on.home.com...
> Hi, I am just learning cobol and I mean JUST learning cobol!
>
…[11 more quoted lines elided]…
> I've posted the whole program code below, If this isn't ok etiquette for
the
> form then please accept my apologies.
>
…[130 more quoted lines elided]…
>
```

#### ↳ Re: New to the cobol world!! Newbie Question.

- **From:** "Rob" <RHeady1@Flash.net>
- **Date:** 2001-01-28T05:50:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0rOc6.4330$467.181256@news.flash.net>`
- **References:** `<lxCc6.879$KP3.391438@news3.rdc1.on.home.com>`

```
Hey MadG,

Welcome to the wonderful world of COBOL!

A COBOL I/O error 48,02 is a WRITE operation was attempted on an unopend
file.

It looks like you are using RM/COBOL.  There are many sample and diagnostic
COBOL programs included in the development system.  Since you are just
learning, it may be helpful to use an existing program as a guide to writing
a new program.  Look for a program called filetest.cbl or pacetest.cbl.

-Rob

MadG wrote in message ...
>Hi, I am just learning cobol and I mean JUST learning cobol!
>
…[11 more quoted lines elided]…
>I've posted the whole program code below, If this isn't ok etiquette for
the
>form then please accept my apologies.
>
…[130 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
