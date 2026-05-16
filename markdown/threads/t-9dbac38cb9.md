[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol ii - mainframe question

_6 messages · 6 participants · 2000-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### cobol ii - mainframe question

- **From:** "john weathers" <flairn@starpower.net>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<897rmo$qbb$1@bob.news.rcn.net>`

```
CICS field edit question...

SITUATION:    I am parsing a "free form" entry, 13-byte character field on a
CICS screen -  for example, the user could input  "123334.5", and I parse
this entry into character format "00000123334.50.

QUESTION:  What is the easiest way to convert this character field -
'00000123334.56' - into numeric format pic 9(11)v99.  ..Do I need to move
each side of the decimal into separate character fields - redefined to
numeric - (e.g., left side "field-dollars",  right side "field-cents") and
then add them together?

I tried various ways of moving the character field - "00000123334.56" -
into a same size numeric field defined as 9(11)v99, but get a s0c7 error.
I seemed to me that there should be a simple way to accomlish this.

i.e.,      FIELD-CHAR   PIC X(13) VALUE '0000012334.56'.
            FIELD-NUMB PIC 9(11)V99 VALUE 0.
            -
            -
            -
           MOVE FIELD FIELD-CHAR TO FIELD-NUMB  <---s0c7 error

Thanks,

jw
```

#### ↳ Re: cobol ii - mainframe question

- **From:** "RUSSELL STYLES" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89eoa0$jj$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<897rmo$qbb$1@bob.news.rcn.net>`

```
    Your text example should work, but the source is a 9(10).99, not a
9(11).99.  If doing a direct move
from pic x to pic 9, pics should work.  Use some other method (ie unstring,
etc).  Or new intrinsic function.


john weathers <flairn@starpower.net> wrote in message
news:897rmo$qbb$1@bob.news.rcn.net...
> CICS field edit question...
>
> SITUATION:    I am parsing a "free form" entry, 13-byte character field on
a
> CICS screen -  for example, the user could input  "123334.5", and I parse
> this entry into character format "00000123334.50.
…[22 more quoted lines elided]…
>
```

#### ↳ Re: cobol ii - mainframe question

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B7B75F.B88920BE@worldnet.att.net>`
- **References:** `<897rmo$qbb$1@bob.news.rcn.net>`

```
john weathers wrote:
> 
> CICS field edit question...
…[24 more quoted lines elided]…
> jw

You get a S0C7 error because you are moving a non-numeric character (the
decimal point) into a numeric field.

If you can guarantee that the decimal point will always be in the
eleventh position of FIELD-CHAR, then I think you could try:

FIELD-CHAR-R  REDEFINES FIELD-CHAR PIC 9(10).99.

Then you should be able to MOVE FIELD-CHAR-R TO FIELD-NUMB, because
COBOL II supports numeric de-editing.  

Try this test program with COBOL II:

000012 IDENTIFICATION DIVISION.
000020     PROGRAM-ID. DEEEDIT.
000030 ENVIRONMENT DIVISION.
000040 DATA DIVISION.
000050 WORKING-STORAGE SECTION.
000060 01  MY-DATA.
000070     05  FIELD-CHAR       PIC  X(13)  VALUE '0000012334.56'.
000071     05  FIELD-CHAR-R     REDEFINES FIELD-CHAR PIC 9(10).99.
000072     05  FIELD-NUMB       PIC 9(11)V99.
000120 PROCEDURE DIVISION.
000150 INIT.
000160     MOVE FIELD-CHAR-R TO FIELD-NUMB.
000170     DISPLAY 'FIELD-CHAR   = ' FIELD-CHAR.
000171     DISPLAY 'FIELD-CHAR-R = ' FIELD-CHAR-R.
000172     DISPLAY 'FIELD-NUMB   = ' FIELD-NUMB.
000190     STOP RUN.

It compiled cleanly and the execution results were:

FIELD-CHAR   = 0000012334.56
FIELD-CHAR-R = 0000012334.56
FIELD-NUMB   = 0000001233456

So I think numeric de-editing in COBOL II should solve your problem.
```

##### ↳ ↳ Re: cobol ii - mainframe question

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89965s$2ne$1@nntp6.atl.mindspring.net>`
- **References:** `<897rmo$qbb$1@bob.news.rcn.net> <38B7B75F.B88920BE@worldnet.att.net>`

```
Besides being certain that your input field always has the decimal point in
the same place, you ALSO need to make certain that your "leading zeroes" are
always present - and never represented by spaces.

Note to readers:
   VS COBOL II does *not* support intrinsic functions.  If it did (as IBM
COBOL for this-and-that does) then the programmer could use the NUMVAL
intrinsic function and NOT worry about where the decimal point was or whether
or not their were leading spaces or leading zeros.  HENCE this is yet another
reason to upgrade your IBM COBOL to a current "strategic" IBM compiler.  Also
of interest (now that 1/1/00 is past), IBM has announced that VS COBOL II
will "lose support" come March of *next* year, i.e. March 2001.
```

#### ↳ Re: cobol ii - mainframe question

- **From:** "Mark L. Bartlett" <mbartlet@sound.net>
- **Date:** 2000-02-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38B7EB84.E84EBFD2@sound.net>`
- **References:** `<897rmo$qbb$1@bob.news.rcn.net>`

```
As I understand it, if you move from a numeric edited field to a numeric field,
the data will be de-edited.

ex.: 01 field-1 pic 999,999,999.99 value 1234.56.
       01 field-2 pic 9(9)v99.
---
     move field-1 to field-2


john weathers wrote:

> CICS field edit question...
>
…[23 more quoted lines elided]…
> jw
```

#### ↳ Re: cobol ii - mainframe question

- **From:** "Donald Bauer" <dwbauer@attglobal.net>
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38bc5974_3@news1.prserv.net>`
- **References:** `<897rmo$qbb$1@bob.news.rcn.net>`

```
If you are interested this is some sample code that edits character input
data and depending on what was input it will create a numeric data element
of
the type 9(10)v99 as output.  It is now set up to input an array of
different numbers for a test to see how it all works.  You will note the
CICS code for error attributes have been commented out as I was running this
in batch.  I think this is good code and will work to edit about any amount,
even negatives.

Take a look:
000100 IDENTIFICATION DIVISION.
000200 PROGRAM-ID.  BPB00TSL.
000300 DATE-WRITTEN.MARCH 1998.
000400*PRODUCTION DATE.???????????????.
000500 ENVIRONMENT DIVISION.
000600 CONFIGURATION SECTION.
000700 DATA DIVISION.
000800 WORKING-STORAGE SECTION.
000900 01  WS-DECIMALS PIC S9(2) COMP-3.
001000 01  WS-COUNT    PIC S9(2) COMP-3.
001100 01  WS-AMOUNT-OUT.
001200     05  WS-AMTOUT-1POS PIC X OCCURS 13 TIMES
001300          INDEXED BY AMTOUT.
001400 01  FILLER REDEFINES WS-AMOUNT-OUT.
001500     05  WS-EDITED-AMOUNT  PIC 9(12).
001600     05  FILLER            PIC X(01).
001700 01  WS-NUMERIC-TEST REDEFINES WS-AMOUNT-OUT PIC 9(13).
001800
001900 01  WS-AMOUNT-TEST REDEFINES WS-AMOUNT-OUT PIC 9(13).
002000 01  WS-AMOUNT-IN.
002100     05  WS-AMTIN-1POS PIC X OCCURS 13 TIMES
002110           INDEXED BY AMTIN.
002500 01  WBM-DATA.
002600     05  FILLER PIC X(2) VALUE '02'.
002700     05  FILLER PIC X(12) VALUE '  83456.92  '.
002800     05  FILLER PIC X(2) VALUE '02'.
002900     05  FILLER PIC X(12) VALUE ' 1234.5     '.
003000     05  FILLER PIC X(2) VALUE '02'.
003100     05  FILLER PIC X(12) VALUE '  12345678  '.
003200     05  FILLER PIC X(2) VALUE '02'.
003300     05  FILLER PIC X(12) VALUE '  8439872.88'.
003400     05  FILLER PIC X(2) VALUE '02'.
003500     05  FILLER PIC X(12) VALUE '1234.5      '.
003600     05  FILLER PIC X(2) VALUE '02'.
003700     05  FILLER PIC X(12) VALUE '827.757     '.
003800     05  FILLER PIC X(2) VALUE '02'.
003810     05  FILLER PIC X(12) VALUE '827X75712345'.
003820     05  FILLER PIC X(2) VALUE '02'.
003830     05  FILLER PIC X(12) VALUE '827175712345'.
003840     05  FILLER PIC X(2) VALUE '02'.
003850     05  FILLER PIC X(12) VALUE '8271757123  '.
004100     05  FILLER PIC X(14) VALUE SPACE.
004200     05  FILLER PIC X(14) VALUE SPACE.
004300     05  FILLER PIC X(14) VALUE SPACE.
004400 01  WBM-TABLE REDEFINES WBM-DATA.
004500     05  WBM-DATA OCCURS 12 TIMES INDEXED BY SCRINX.
004600       10 WBM-AMOUNT-LEN     PIC X(2).
004700       10 WBM-AMOUNT         PIC X(12).
004800 01  PROGRAM-ERROR-IND PIC X(01).
004900     88 PROGRAM-ERROR    VALUE 'Y'.
005000     88 NOT-PROGRAM-ERROR VALUE 'N'.
005100 01  AMOUNT-ERROR-IND PIC X(01).
005200     88 AMOUNT-ERROR     VALUE 'Y'.
005300     88 NOT-AMOUNT-ERROR VALUE 'N'.
005400 PROCEDURE DIVISION.
005500     SET NOT-PROGRAM-ERROR TO TRUE
005600     SET NOT-AMOUNT-ERROR  TO TRUE
005610     PERFORM 4800-EDIT-AMOUNTS THRU 4800-EXIT
005620     STOP RUN.
005700     .
005800  4800-EDIT-AMOUNTS.
005900     PERFORM VARYING SCRINX
006000        FROM 1 BY 1 UNTIL SCRINX > 11
006010          OR WBM-AMOUNT-LEN         (SCRINX) = SPACE
006100* **     IF WBM-AMOUNT-LEN         (SCRINX) > ZERO
006200          IF WBM-AMOUNT-LEN         (SCRINX) > SPACE
006300              MOVE WBM-AMOUNT             (SCRINX)
006400                TO WS-AMOUNT-IN
006500              PERFORM XXXX-KEYED-AMOUNT-EDITOR
006600                 THRU XXXX-EXIT
006700              IF AMOUNT-ERROR
006800*                 MOVE ATTR-UNP-MDT-ON
006900*                   TO WBM-AMOUNT-ATTR (SCRINX)
007000*                 MOVE COLOR-ERROR-FIELD
007100*                   TO WBM-AMOUNT-C    (SCRINX)
007200*                 MOVE -1 TO WBM-AMOUNT-LEN  (SCRINX)
007300                  SET PROGRAM-ERROR TO TRUE
007400              END-IF
007500          END-IF
007600*
007700*         IF WBM-ADJ-AMOUNT-LEN     (SCRINX) > ZERO
007800*             MOVE WBM-ADJ-AMOUNT         (SCRINX)
007900*               TO WS-AMOUNT-IN
008000*             PERFORM XXXX-KEYED-AMOUNT-EDITOR
008100*                THRU XXXX-EXIT
008200*             IF AMOUNT-ERROR
008300*                 MOVE ATTR-UNP-MDT-ON
008400*                   TO WBM-ADJ-AMOUNT-ATTR (SCRINX)
008500*                 MOVE COLOR-ERROR-FIELD
008600*                   TO WBM-ADJ-AMOUNT-C (SCRINX)
008700*                 MOVE -1 TO WBM-ADJ-AMOUNT-LEN (SCRINX)
008800*                 SET PROGRAM-ERROR TO TRUE
008900*             END-IF
009000*         END-IF
009100*
009200*         IF WBM-CAPPED-AMOUNT-LEN  (SCRINX) > ZERO
009300*             MOVE WBM-CAPPED-ADJ-AMOUNT  (SCRINX)
009400*               TO WS-AMOUNT-IN
009500*             PERFORM XXXX-KEYED-AMOUNT-EDITOR
009600*                THRU XXXX-EXIT
009700*             IF AMOUNT-ERROR
009800*                 MOVE ATTR-UNP-MDT-ON
009900*                   TO WBM-ADJ-CAPPED-AMOUNT-ATTR (SCRINX)
010000*                 MOVE COLOR-ERROR-FIELD
010100*                   TO WBM-ADJ-CAPPED-AMOUNT-C (SCRINX)
010200*                 MOVE -1 TO WBM-ADJ-CAPPED-AMOUNT-LEN
(SCRINX)
010300*                 SET PROGRAM-ERROR TO TRUE
010400*             END-IF
010500*         END-IF
010600     IF PROGRAM-ERROR DISPLAY 'INVALID AMOUNT '
010700        WS-AMOUNT-OUT ' ' WS-EDITED-AMOUNT
010800        SET NOT-PROGRAM-ERROR TO TRUE
010900     ELSE
011000       DISPLAY 'GOOD AMOUNT ' WS-EDITED-AMOUNT
011100     END-IF
011200     END-PERFORM
011300*    IF PROGRAM-ERROR
011400*        MOVE 'INVALID AMOUNT'     TO ERRMSG1O
011500*        MOVE COLOR-ERROR-FIELD    TO ERRMSG1A
011600*    END-IF
011700     .
011800  4800-EXIT. EXIT.
011900  XXXX-KEYED-AMOUNT-EDITOR.
012000     SET NOT-AMOUNT-ERROR TO TRUE
012100     MOVE +50  TO WS-DECIMALS
012200     MOVE ZERO TO WS-COUNT
012300     PERFORM VARYING AMTIN FROM 1 BY 1
012400       UNTIL AMTIN > 12
012500       IF WS-AMTIN-1POS (AMTIN) > SPACE
012600           ADD +1 TO WS-COUNT
012700       END-IF
012800       IF WS-AMTIN-1POS (AMTIN) = '.'
012900           MOVE ZERO TO WS-DECIMALS
013000       END-IF
013100       IF WS-AMTIN-1POS (AMTIN) NOT < '0' AND
013200          WS-AMTIN-1POS (AMTIN) NOT > '9'
013300           ADD +1    TO WS-DECIMALS
013400       END-IF
013500     END-PERFORM
013510     IF WS-DECIMALS > +50
013520         MOVE ZERO TO WS-DECIMALS
013530     END-IF
013600     IF WS-DECIMALS < 3
013700* MOVE ONLY NUMERICS RIGHT JUSTIFIED ZERO FILL *
013800         SET AMTOUT TO 12
014000         MOVE ZERO TO WS-AMOUNT-OUT
014100         PERFORM WITH TEST AFTER
014200           VARYING AMTIN FROM 12 BY -1
014300             UNTIL AMTIN NOT > 1
014400           IF WS-AMTIN-1POS (AMTIN) NOT = '.' AND
014500              WS-AMTIN-1POS (AMTIN) NOT = SPACE
014600              MOVE WS-AMTIN-1POS (AMTIN)
014700                TO WS-AMTOUT-1POS (AMTOUT)
014800              SET AMTOUT DOWN BY 1
015000           END-IF
015100         END-PERFORM
015200         EVALUATE TRUE
015300           WHEN WS-DECIMALS = 1
015400             MOVE WS-AMOUNT-OUT TO WS-AMOUNT-IN
015500             MOVE ZERO TO WS-AMOUNT-OUT
015600             SET AMTOUT TO 11
015700             PERFORM WITH TEST AFTER
015800               VARYING AMTIN FROM 12 BY -1
015900                 UNTIL AMTIN NOT > 1
016000              MOVE WS-AMTIN-1POS (AMTIN)
016100                TO WS-AMTOUT-1POS (AMTOUT)
016200              SET AMTOUT DOWN BY 1
016400             END-PERFORM
016500           WHEN WS-DECIMALS = ZERO
016600             MOVE WS-AMOUNT-OUT TO WS-AMOUNT-IN
016700             MOVE ZERO TO WS-AMOUNT-OUT
016800             SET AMTOUT TO 10
016900             PERFORM WITH TEST AFTER
017000               VARYING AMTIN FROM 12 BY -1
017100                 UNTIL AMTIN NOT > 1
017200              MOVE WS-AMTIN-1POS (AMTIN)
017300                TO WS-AMTOUT-1POS (AMTOUT)
017400              SET AMTOUT DOWN BY 1
017510             END-PERFORM
017700         END-EVALUATE
017800     ELSE
017900       DISPLAY '> 3 DECIMALS ' WS-AMOUNT-OUT
018000       SET AMOUNT-ERROR  TO TRUE
018100       SET PROGRAM-ERROR TO TRUE
018200     END-IF
018210     IF WS-COUNT > +10
018220       DISPLAY '> 10 DECIMALS ' WS-AMOUNT-OUT
018230       SET AMOUNT-ERROR  TO TRUE
018240       SET PROGRAM-ERROR TO TRUE
018250     END-IF
018300     IF NOT-AMOUNT-ERROR AND
018400        WS-NUMERIC-TEST NOT NUMERIC
018500         DISPLAY ' NOT NUMERIC ' WS-AMOUNT-OUT
018600         SET AMOUNT-ERROR  TO TRUE
018700         SET PROGRAM-ERROR TO TRUE
018800     END-IF
018900     .
019000   XXXX-EXIT.
019100     EXIT.
019110   GOBACK-PARA.
019200     GOBACK.

----- Original Message -----
From: "Mark L. Bartlett" <mbartlet@sound.net>
Newsgroups: comp.lang.cobol
Sent: Saturday, February 26, 2000 10:04 AM
Subject: Re: cobol ii - mainframe question


> As I understand it, if you move from a numeric edited field to a numeric
field,
> the data will be de-edited.
>
…[10 more quoted lines elided]…
> > SITUATION:    I am parsing a "free form" entry, 13-byte character field
on a
> > CICS screen -  for example, the user could input  "123334.5", and I
parse
> > this entry into character format "00000123334.50.
> >
> > QUESTION:  What is the easiest way to convert this character field -
> > '00000123334.56' - into numeric format pic 9(11)v99.  ..Do I need to
move
> > each side of the decimal into separate character fields - redefined to
> > numeric - (e.g., left side "field-dollars",  right side "field-cents")
and
> > then add them together?
> >
> > I tried various ways of moving the character field - "00000123334.56" -
> > into a same size numeric field defined as 9(11)v99, but get a s0c7
error.
> > I seemed to me that there should be a simple way to accomlish this.
> >
…[10 more quoted lines elided]…
>

"john weathers" <flairn@starpower.net> wrote in message
news:897rmo$qbb$1@bob.news.rcn.net...
> CICS field edit question...
>
> SITUATION:    I am parsing a "free form" entry, 13-byte character field on
a
> CICS screen -  for example, the user could input  "123334.5", and I parse
> this entry into character format "00000123334.50.
…[22 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
