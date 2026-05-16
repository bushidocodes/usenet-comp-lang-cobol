[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Checking a number for uniqueness (Student Program)

_3 messages · 3 participants · 2001-04_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Checking a number for uniqueness (Student Program)

- **From:** "J. Reis" <jreis26@hotmail.com>
- **Date:** 2001-04-03T14:56:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SXpy6.1243$wG4.317255@news.uswest.net>`

```
Greetings.

Working again on my COBOL class final project.  I have created a lottery
program that randomly draws six numbers.  It also allows people to input
their guesses. There are two things left I would like it to do and need to
get pointed in the right direction.  First, I would like it to make the
numbers it draws for the first five random numbers unique.  I assume that an
IF...OR....THEN...GOTO statement would need to be used.  I separated the
sections in my code to give each random number its own section of the
Procedure Division.  I have tried using these section titles as the
identifiers for performing the check against numbers but I dont think that
is the appropriate way to procede.  The other part of this project which I
would like the program to perform is the matching of guessed numbers to
drawn numbers.  Once again, an IF...OR....THEN....GOTO statement of some
variety needs to be used, but I am not sure how to implement this one.

For my first problem, I think inserting the lines at Line No. 001520
containing -

IF random-number-1 = random-number-2 OR random-number-1 = random-number-3 OR
random-number-1 = random-number-4 OR random-number-1 = random-number-5
THEN GO TO randnum-1
END-IF

should do the work, but will it loop properly if the same number is drawn
twice?  Can I also assume the same type of line comparing the
random-number-x to an entry in the Working Storage section for the user
inputted number would work for detereming a winning combination?
The program code that I have thus far follows this message.  Any help on
this is greatly appreciated.

Justin Reis

@OPTIONS MAIN
000020 IDENTIFICATION DIVISION.
000030 PROGRAM-ID.   LOTTERY.
000040 AUTHOR.       JUSTIN REIS.
000050 ENVIRONMENT DIVISION.
000060 CONFIGURATION SECTION.
000070 SPECIAL-NAMES.
000080       CRT STATUS IS KEYBOARD-STATUS
000090       CURSOR IS CURSOR-POSITION.
000100 SOURCE-COMPUTER.  IBM-PC.
000110 OBJECT-COMPUTER.  IBM-PC.
000120 DATA DIVISION.
000130 WORKING-STORAGE SECTION.
000140 01  KEYBOARD-STATUS.
000150     03 ACCEPT-STATUS   PIC 9.
000160     03 FUNCTION-KEY    PIC X.
000170     03 SYSTEM-USE      PIC X.
000180 01  CURSOR-POSITION.
000190     03 CURSOR-ROW      PIC 9(2)     VALUE 1.
000200     03 CURSOR-COLUMN   PIC 9(2)     VALUE 1.
000210 01  RANDOM-SEED        PIC 9(8)     VALUE ZEROS.
000220 01  RANDOM-NUMBER-1    PIC 99       VALUE ZEROS.
000230 01  RANDOM-NUMBER-2    PIC 99       VALUE ZEROS.
000231 01  RANDOM-NUMBER-3    PIC 99       VALUE ZEROS.
000232 01  RANDOM-NUMBER-4    PIC 99       VALUE ZEROS.
000233 01  RANDOM-NUMBER-5    PIC 99       VALUE ZEROS.
000234 01  RANDOM-NUMBER-6    PIC 99       VALUE ZEROS.
000236 01  RANDOM-GENERATE    PIC V9(2)    VALUE ZEROS.
000240 01  SHOW-NEXT-SCREEN   PIC X        VALUE "Y".
000241 01  PROCESS-FLAG       PIC X        VALUE SPACES.
000242     88  END-PROCESS    VALUE "Y".
000243 01  SCREEN-ITEMS.
000250     03  LOTTO-BALL-1   PIC 9(2)     VALUE 1.
000260     03  LOTTO-BALL-2   PIC 9(2)     VALUE 2.
000270     03  LOTTO-BALL-3   PIC 9(2)     VALUE 3.
000280     03  LOTTO-BALL-4   PIC 9(2)     VALUE 4.
000290     03  LOTTO-BALL-5   PIC 9(2)     VALUE 5.
000300     03  JUSTIN-BALL-6  PIC 9(2)     VALUE 1.
000310     03  ACTUAL-NUM-1   PIC 9(2)     VALUE ZEROS.
000320     03  ACTUAL-NUM-2   PIC 9(2)     VALUE ZEROS.
000330     03  ACTUAL-NUM-3   PIC 9(2)     VALUE ZEROS.
000340     03  ACTUAL-NUM-4   PIC 9(2)     VALUE ZEROS.
000350     03  ACTUAL-NUM-5   PIC 9(2)     VALUE ZEROS.
000360     03  ACTUAL-NUM-6   PIC 9(2)     VALUE ZEROS.
000370 SCREEN SECTION.
000380 01  DATA-ENTRY-SCREEN
000390     BLANK SCREEN, AUTO,
000400     FOREGROUND-COLOR IS 7,
000410     BACKGROUND-COLOR IS 4.
000420     03  LINE 1 COLUMN 7  VALUE "Welcome to Justin's Lottery"
000430         HIGHLIGHT FOREGROUND-COLOR 7 BACKGROUND-COLOR 4.
000440     03  LINE 4 COLUMN 5  VALUE "To play, simply enter 5 unique ".
000450     03  LINE 5 COLUMN 4  VALUE "numbers and the lucky JustinBall".
000460     03  LINE 6 COLUMN 5  VALUE " Numbers must be between 1 and ".
000470     03  LINE 7 COLUMN 7  VALUE " 50 and use two digits.".
000480     03  LINE 9  COLUMN 1  VALUE "Lotto".
000490     03  LINE 9  COLUMN 9  VALUE "Lotto".
000500     03  LINE 9  COLUMN 17 VALUE "Lotto".
000510     03  LINE 9  COLUMN 25 VALUE "Lotto".
000520     03  LINE 9  COLUMN 33 VALUE "Lotto".
000530     03  LINE 9  COLUMN 41 VALUE "POWER".
000540     03  LINE 10 COLUMN 1  VALUE "Ball".
000550     03  LINE 10 COLUMN 9  VALUE "Ball".
000560     03  LINE 10 COLUMN 17 VALUE "Ball".
000570     03  LINE 10 COLUMN 25 VALUE "Ball".
000580     03  LINE 10 COLUMN 33 VALUE "Ball".
000590     03  LINE 10 COLUMN 41 VALUE "BALL".
000600     03  LINE 11 COLUMN 1  VALUE "No. 1".
000610     03  LINE 11 COLUMN 9  VALUE "No. 2".
000620     03  LINE 11 COLUMN 17 VALUE "No. 3".
000630     03  LINE 11 COLUMN 25 VALUE "No. 4".
000640     03  LINE 11 COLUMN 33 VALUE "No. 5".
000650     03  LINE 11 COLUMN 41 VALUE "  |  ".
000660     03  LINE 12 COLUMN 3  PIC 9(2) USING LOTTO-BALL-1
000670         REVERSE-VIDEO REQUIRED.
000680     03  LINE 12 COLUMN 11 PIC 9(2) USING LOTTO-BALL-2
000690         REVERSE-VIDEO REQUIRED.
000700     03  LINE 12 COLUMN 19 PIC 9(2) USING LOTTO-BALL-3
000710         REVERSE-VIDEO REQUIRED.
000720     03  LINE 12 COLUMN 27 PIC 9(2) USING LOTTO-BALL-4
000730         REVERSE-VIDEO REQUIRED.
000740     03  LINE 12 COLUMN 35 PIC 9(2) USING LOTTO-BALL-5
000750         REVERSE-VIDEO REQUIRED.
000760     03  LINE 12 COLUMN 43 PIC 9(2) USING JUSTIN-BALL-6
000770         REVERSE-VIDEO REQUIRED.
000780 01  CONFIRMATION-SCREEN-1.
000781     03  LINE 14 COLUMN 5  VALUE "ARE YOU READY TO PLAY? (Y/N): ".
000782     03  LINE 14 COLUMN 29 PIC X USING SHOW-NEXT-SCREEN.
000783 01  LOTTERY-DRAWING-SCREEN.
000784     03  LINE 17 COLUMN 5  VALUE "Here are today's lucky".
000790     03  LINE 18 COLUMN 6  VALUE "JUSTIN-BALL numbers!".
000800     03  LINE 20 COLUMN 1  VALUE "Lotto".
000810     03  LINE 20 COLUMN 9  VALUE "Lotto".
000820     03  LINE 20 COLUMN 17 VALUE "Lotto".
000830     03  LINE 20 COLUMN 25 VALUE "Lotto".
000840     03  LINE 20 COLUMN 33 VALUE "Lotto".
000850     03  LINE 20 COLUMN 41 VALUE "POWER".
000860     03  LINE 21 COLUMN 1  VALUE "Ball".
000870     03  LINE 21 COLUMN 9  VALUE "Ball".
000880     03  LINE 21 COLUMN 17 VALUE "Ball".
000890     03  LINE 21 COLUMN 25 VALUE "Ball".
000900     03  LINE 21 COLUMN 33 VALUE "Ball".
000910     03  LINE 21 COLUMN 41 VALUE "BALL".
000920     03  LINE 22 COLUMN 1  VALUE "No. 1".
000930     03  LINE 22 COLUMN 9  VALUE "No. 2".
000940     03  LINE 22 COLUMN 17 VALUE "No. 3".
000950     03  LINE 22 COLUMN 25 VALUE "No. 4".
000960     03  LINE 22 COLUMN 33 VALUE "No. 5".
000970     03  LINE 22 COLUMN 43 VALUE "|".
000980     03  LINE 23 COLUMN 3  PIC 9(2) USING RANDOM-NUMBER-1
000990         REVERSE-VIDEO REQUIRED.
001000     03  LINE 23 COLUMN 11 PIC 9(2) USING RANDOM-NUMBER-2
001010         REVERSE-VIDEO REQUIRED.
001020     03  LINE 23 COLUMN 19 PIC 9(2) USING RANDOM-NUMBER-3
001030         REVERSE-VIDEO REQUIRED.
001040     03  LINE 23 COLUMN 27 PIC 9(2) USING RANDOM-NUMBER-4
001050         REVERSE-VIDEO REQUIRED.
001060     03  LINE 23 COLUMN 35 PIC 9(2) USING RANDOM-NUMBER-5
001070         REVERSE-VIDEO REQUIRED.
001080     03  LINE 23 COLUMN 43 PIC 9(2) USING RANDOM-NUMBER-6
001090         REVERSE-VIDEO REQUIRED.
001100 PROCEDURE DIVISION.
001110 JUSTIN-BALL-START.
001111     PERFORM PROCESS-SCREEN
001112 PROCESS-SCREEN.
001113     DISPLAY DATA-ENTRY-SCREEN.
001120     ACCEPT  DATA-ENTRY-SCREEN.
001121     DISPLAY CONFIRMATION-SCREEN-1.
001122     ACCEPT  CONFIRMATION-SCREEN-1.
001130 LOTTERY-START.
001140     MOVE FUNCTION CURRENT-DATE (9:8) TO RANDOM-SEED
001150     PERFORM RANDNUM-1 THRU RANDNUM-6.
001160 RANDNUM-1.
001180     PERFORM 1 TIMES
001190         COMPUTE RANDOM-GENERATE = FUNCTION RANDOM
001200         COMPUTE RANDOM-NUMBER-1 = (RANDOM-GENERATE * 50) + 1
001210     END-PERFORM.
001230 RANDNUM-2.
001240     PERFORM 1 TIMES
001250         COMPUTE RANDOM-GENERATE = FUNCTION RANDOM
001260         COMPUTE RANDOM-NUMBER-2  = (RANDOM-GENERATE * 50) + 1
001270     END-PERFORM.
001290 RANDNUM-3.
001300     PERFORM 1 TIMES
001310         COMPUTE RANDOM-GENERATE = FUNCTION RANDOM
001320         COMPUTE RANDOM-NUMBER-3 = (RANDOM-GENERATE * 50) + 1
001330     END-PERFORM.
001350 RANDNUM-4.
001360     PERFORM 1 TIMES
001370         COMPUTE RANDOM-GENERATE = FUNCTION RANDOM
001380         COMPUTE RANDOM-NUMBER-4 = (RANDOM-GENERATE * 50) + 1
001390     END-PERFORM.
001410 RANDNUM-5.
001420     PERFORM 1 TIMES
001430         COMPUTE RANDOM-GENERATE = FUNCTION RANDOM
001440         COMPUTE RANDOM-NUMBER-5 = (RANDOM-GENERATE * 50) + 1
001450     END-PERFORM.
001470 RANDNUM-6.
001480     PERFORM 1 TIMES
001490         COMPUTE RANDOM-GENERATE = FUNCTION RANDOM
001500         COMPUTE RANDOM-NUMBER-6 = (RANDOM-GENERATE * 50) + 1
001510     END-PERFORM.
001530     DISPLAY LOTTERY-DRAWING-SCREEN.
001531     STOP RUN.
001540
```

#### ↳ Re: Checking a number for uniqueness (Student Program)

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-04-03T20:48:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ACA36E6.477F0B72@home.com>`
- **References:** `<SXpy6.1243$wG4.317255@news.uswest.net>`

```


"J. Reis" wrote:

> Greetings.
>
…[195 more quoted lines elided]…
> 001540

Justin,

I'm not going to get into random numbers, because that's not my scene. I suspect
some of the math whiz kids will tell you 'there aint no such animal as a random
number' <G>.

My comments are more to do with shorthand. You've got it nicely structured, but
as soon as you find yourself saying, "Hey - I just coded that before", look to
see if you can introduce a shortcut - more concise and less chance of errors -
what we call in OO 'Reusability", although the term is just as legit in
Structured programming..

So taking your source :--

000220 01  RANDOM-NUMBER-1    PIC 99       VALUE ZEROS.
000230 01  RANDOM-NUMBER-2    PIC 99       VALUE ZEROS.
000231 01  RANDOM-NUMBER-3    PIC 99       VALUE ZEROS.
000232 01  RANDOM-NUMBER-4    PIC 99       VALUE ZEROS.
000233 01  RANDOM-NUMBER-5    PIC 99       VALUE ZEROS.
000234 01  RANDOM-NUMBER-6    PIC 99       VALUE ZEROS.

Change this to :-

01 RandomTable
    05  RandomNumber occurs 6                        pic 9(02).

Procedure....

initialize RandomTable
perform RANDOM-CALC varying n from 1 by 1 until n > 6

RANDOM-CALC.

    compute RandomGenerate = function Random
    compute RandomNumber(n) = (RandomGenerate * 50) + 1.

That's the general idea, and you should be able to alter it to do any additional
perform you might want, even segregating to two paragraphs if you were using a
different Multiplying factor for certain of the numbers.

Perform RANDOM-CALC
    varying n from x by y until n > z

Jimmy, Calgary AB
```

#### ↳ Re: Checking a number for uniqueness (Student Program)

- **From:** "Thomas Meehan" <erwin24@worldnet.att.net>
- **Date:** 2001-04-03T23:26:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n_sy6.7196$IJ1.609390@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<SXpy6.1243$wG4.317255@news.uswest.net>`

```
First thing that popped into my mind was tabling up the numbers as you draw
them.  Each time you draw a new number you check if it's in the table.  If
it is go back to the paragraph for drawing the number.  If it's not in the
table store it, and see if you have enough numbers.  Either go back to the
drawing paragraph or exit the loop when you have them all selected.


J. Reis <jreis26@hotmail.com> wrote in message
news:SXpy6.1243$wG4.317255@news.uswest.net...
> Greetings.
>
…[4 more quoted lines elided]…
> numbers it draws for the first five random numbers unique.  I assume that
an
> IF...OR....THEN...GOTO statement would need to be used.  I separated the
> sections in my code to give each random number its own section of the
…[10 more quoted lines elided]…
> IF random-number-1 = random-number-2 OR random-number-1 = random-number-3
OR
> random-number-1 = random-number-4 OR random-number-1 = random-number-5
> THEN GO TO randnum-1
…[181 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
