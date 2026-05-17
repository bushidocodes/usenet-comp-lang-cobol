[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Hex

_6 messages · 5 participants · 1996-07_

---

### Hex

- **From:** "dbret..." <ua-author-6588809@usenetarchives.gap>
- **Date:** 1996-07-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4sqtoo$3ja@newsbf02.news.aol.com>`

```

Is there a way to display the hex value of a character (for instance "C1"
for the letter "A") in cobol?

Dave
```

#### ↳ Re: Hex

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-07-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-90fea7c95a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4sqtoo$3ja@newsbf02.news.aol.com>`
- **References:** `<4sqtoo$3ja@newsbf02.news.aol.com>`

```

In <4sqtoo$3.··.@new··l.com>, dbr··.@a··.com (DBretz0727) writes:
› Is there a way to display the hex value of a character (for instance "C1"
› for the letter "A") in cobol?
›
› Dave

Yes, there are many. Here is one:
000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID. THEX.
000300
000400 AUTHOR. LEIF SVALGAARD.
000500 DATE-WRITTEN. 96/07/20
000600 -REVISED: 96/07/20.
000700
000800 ENVIRONMENT DIVISION.
000900
001000 CONFIGURATION SECTION.
001100 SOURCE-COMPUTER. IBM-370.
001200 OBJECT-COMPUTER. IBM-370.
001300
001400 DATA DIVISION.
001500
001600 WORKING-STORAGE SECTION.
001700
001800 01 HEX-CONVERSION.
001900 02 THE-INDEX PIC S9(4) COMP.
002000 02 THE-CHAR-VALUE PIC S9(4) COMP-4 VALUE ZEROES.
002100 02 FILLER REDEFINES THE-CHAR-VALUE.
002200 03 FILLER PIC X.
002300 03 THE-CHAR PIC X.
002400 02 HEX-DIGITS PIC X(16) VALUE "0123456789ABCDEF".
002500 02 FILLER REDEFINES HEX-DIGITS.
002600 03 HEX-DIGIT PIC X OCCURS 16 TIMES.
002700 02 THE-RESULT PIC X.
002800
002900 PROCEDURE DIVISION.
003000 BEGIN-PROGRAM.
003100 MOVE "A" TO THE-CHAR
003200 PERFORM SHOW-ME-HEX
003300
003400 MOVE 129 TO THE-CHAR-VALUE
003500 PERFORM SHOW-ME-HEX
003600
003700 STOP RUN
003800 .
003900
004000 SHOW-ME-HEX.
004100 COMPUTE THE-INDEX = THE-CHAR-VALUE / 16 + 1
004200 MOVE HEX-DIGIT (THE-INDEX) TO THE-RESULT
004300 DISPLAY THE-RESULT NO ADVANCING
004400
004500 COMPUTE THE-INDEX = THE-CHAR-VALUE / 16
004600 COMPUTE THE-INDEX = THE-CHAR-VALUE - 16 * THE-INDEX + 1
004700 MOVE HEX-DIGIT (THE-INDEX) TO THE-RESULT
004800 DISPLAY THE-RESULT
004900 .

Leif Svalgaard
```

#### ↳ Re: Hex

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1996-07-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-90fea7c95a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4sqtoo$3ja@newsbf02.news.aol.com>`
- **References:** `<4sqtoo$3ja@newsbf02.news.aol.com>`

```

DBretz0727 (dbr··.@a··.com) wrote:
: Is there a way to display the hex value of a character (for instance "C1"
: for the letter "A") in cobol?

The following should show how to do what you want. It's standard
COBOL and should be fairly portable.

IDENTIFICATION DIVISION.
PROGRAM-ID. COBTEST.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 TEST-CHAR PIC X.
01 TEST-HEX PIC XX.
PROCEDURE DIVISION.
BEGIN.
MOVE "A" TO TEST-CHAR
CALL "CHAR-TO-HEX" USING TEST-CHAR, TEST-HEX
DISPLAY TEST-CHAR, " ==> ", TEST-HEX
STOP RUN.
END PROGRAM COBTEST.
IDENTIFICATION DIVISION.
PROGRAM-ID. CHAR-TO-HEX.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 NUM PIC 999 COMP.
01 HIGH PIC 99 COMP.
01 LOW PIC 99 COMP.
01 HEX-DIGITS PIC X(16) VALUE "0123456789ABCDEF".
LINKAGE SECTION.
01 CHAR PIC X.
01 HEX PIC XX.
PROCEDURE DIVISION USING CHAR, HEX.
BEGIN.
COMPUTE NUM = FUNCTION ORD (CHAR), SUBTRACT 1 FROM NUM
DIVIDE NUM BY 16 GIVING HIGH REMAINDER LOW
ADD 1 TO HIGH, LOW
MOVE HEX-DIGITS (HIGH:1) TO HEX (1:1)
MOVE HEX-DIGITS (LOW:1) TO HEX (2:1)
EXIT PROGRAM.
END PROGRAM CHAR-TO-HEX.

No warranties, of course!

Walter Murray
Hewlett-Packard
Support Technology Lab
```

#### ↳ Re: Hex

- **From:** "ken mackenzie" <ua-author-4360810@usenetarchives.gap>
- **Date:** 1996-07-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-90fea7c95a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<4sqtoo$3ja@newsbf02.news.aol.com>`
- **References:** `<4sqtoo$3ja@newsbf02.news.aol.com>`

```

DBretz0727 wrote:
›
› Is there a way to display the hex value of a character (for instance "C1"
› for the letter "A") in cobol?Dave,
Try the following. Of course it works for all codes (not just "A").
Also, you can use it for longer strings by making From-Char and To-Char
longer. To-Char is always twice the length of From-Char
------------------------------------------------------------------------
Id Division.
Program-Id. HexDisp.
Author. Ken Mackenzie
Environment Division.
Data Division.
Working-Storage Section.
01.
05 From-Packed Pic S9(03) Packed-Decimal Value +0.
05 Redefines From-Packed.
10 From-Char Pic X(01).
10 Pic X(01).
05 To-Unpacked Pic 9(03).
05 Redefines To-Unpacked.
10 To-Char Pic X(02).
10 Pic X(01).
05 Hex-Table-1 Pic X(16) Value
X'FAFBFCFDFEFF'.
05 Hex-Table-2 Pic X(16) Value
X'C1C2C3C4C5C6'.
05 Ws-Sub Pic S9(04) Binary.
05 Redefines Ws-Sub.
10 Pic X.
10 Ws-Sub-X Pic X.
Procedure Division.
Move 'A' To From-Char
Move From-Packed To To-Unpacked
Inspect To-Char Converting Hex-Table-1
To Hex-Table-2
Display To-Char
Goback.
--------------------------------------------------------------------
```

##### ↳ ↳ Re: Hex

- **From:** "ken mackenzie" <ua-author-4360810@usenetarchives.gap>
- **Date:** 1996-07-21T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-90fea7c95a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-90fea7c95a-p4@usenetarchives.gap>`
- **References:** `<4sqtoo$3ja@newsbf02.news.aol.com> <gap-90fea7c95a-p4@usenetarchives.gap>`

```

Ken MacKenzie wrote:

›            05  Hex-Table-1          Pic X(16)                 Value
›                X'FAFBFCFDFEFF'.
›            05  Hex-Table-2          Pic X(16)                 Value
›                X'C1C2C3C4C5C6'.
› --------------------------------------------------------------------These two items should be PIC X(06) - it would still work though
but you'd get a run-time error message.
```

#### ↳ Re: Hex

- **From:** "arn trembley" <ua-author-9756949@usenetarchives.gap>
- **Date:** 1996-07-22T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-90fea7c95a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<4sqtoo$3ja@newsbf02.news.aol.com>`
- **References:** `<4sqtoo$3ja@newsbf02.news.aol.com>`

```

dbr··.@a··.com (DBretz0727) wrote:
› Is there a way to display the hex value of a character (for instance "C1"
› for the letter "A") in cobol?
›
› Dave

I built a routine to do this, and have used it in several programs.
Unfortunately, it is somewhat longer than the elegant solutions already
posted here, so I will outline it briefly:

First, build a 512-byte table of the displayable hex values, something
like this:

01 HEX-TABLE-DATA.
05 FILLER PIC X(32) VALUE '000102030405060708090A0B0C0D0E0F'.
omitting 14 lines until ending with...
05 FILLER PIC X(32) VALUE 'F0F1F2F3F4F5F6F7F8F9FAFBFCFDFEFF'.

01 HEX-TABLE REDEFINES HEX-TABLE-DATA.
05 HEX-VALUE OCCURS 256 TIMES PIC X(02).

Now, set up a work area to convert your single character byte into a
subscript into the table:

01 HEX-SUB PIC S9(4) COMP VALUE ZERO.
01 HEX-SUB-R REDEFINES HEX-SUB.
05 FILLER PIC X(01).
05 HEX-SUB-CHAR PIC X(01).

Now, any byte you need to convert to displayable hex would be converted
like this:

MOVE ZERO TO HEX-SUB
MOVE 'A' TO HEX-SUB-CHAR
ADD +1 TO HEX-SUB
DISPLAY 'THE HEXADECIMAL VALUE OF "A" = ' HEX-VALUE (HEX-SUB).

Using Realia COBOL on the PC I have had to reverse the order of the
bytes in HEX-SUB-R because intel is little-endian while system 370 is
big-endian, but the technique still works.

I have used a similar technique for converting ebcdic to ascii or
vice-versa, but it takes a little more work to build the translation
tables.

Good luck!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri




_
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
