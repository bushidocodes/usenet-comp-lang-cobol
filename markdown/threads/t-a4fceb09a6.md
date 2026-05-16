[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Check new one and please correct it and send to me, please!=)

_1 message · 1 participant · 2001-04_

---

### Re: Check new one and please correct it and send to me, please!=)

- **From:** "Kevin Solomon" <kjsolo@home.com>
- **Date:** 2001-04-09T10:20:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w1gA6.186866$A6.42171561@news4.rdc1.on.home.com>`
- **References:** `<0Yyy6.15$AX2.990@read2.inet.fi> <3acb0f45_1@my.newsfeeds.com> <2D713F5028C5113F.C640D91E22085D00.E58BDCCEB6256DD0@lp.airnews.net> <SyWy6.75$Td4.3755@read2.inet.fi> <3ACC730C.15742143@brazee.net> <GTez6.66$qw5.2787@read2.inet.fi> <usFz6.12065$Kr1.1067948@newsread1.prod.itd.earthlink.net> <uIdA6.39$P22.911@read2.inet.fi>`

```
Here's your completely debugged source.  Compare it with what you had.  Note
especially that the Environment Division comes before the Data Division.
Read up on the use of Section and scope terminators.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. FRIENDS2NUM.
       AUTHOR.     JARKKO

       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.

       SELECT FRIENDS-FILE ASSIGN TO "C:\FRIENDS.DAT"
       ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.

       FILE SECTION.

       FD FRIENDS-FILE

       RECORD CONTAINS 82 CHARACTERS.

       01 FF-FRIENDS-FILE.
          05 FRIENDS-NAME PIC X(17).
          05 FRIENDS-EMAIL-ADDRESS PIC X(39).
          05 FRIENDS-GSM-NUMBER PIC X(14).
          05 FRIENDS-ADDRESS PIC X(12).

       WORKING-STORAGE SECTION.
       01   OWNSTRING               PIC X(82).
       01   END-OF-FRIENDS-FILE     PIC 9       VALUE ZERO.


       PROCEDURE DIVISION.

       000-PROGRAM-BODY.

       DISPLAY "!Reading friends.dat line by line!"
       OPEN INPUT FRIENDS-FILE.
       PERFORM 100-READ-MY-DATA-FILE UNTIL END-OF-FRIENDS-FILE = 1
       DISPLAY OWNSTRING

       CLOSE FRIENDS-FILE.
       DISPLAY "cool, eh?=)"

       STOP RUN.

       100-READ-MY-DATA-FILE.

       READ FRIENDS-FILE NEXT INTO OWNSTRING
       AT END MOVE 1 TO END-OF-FRIENDS-FILE
       END-READ.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
