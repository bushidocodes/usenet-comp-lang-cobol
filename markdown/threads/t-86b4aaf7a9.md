[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FUNCTION RANDOM.

_13 messages · 9 participants · 2010-11_

---

### FUNCTION RANDOM.

- **From:** "john@wexfordpress.com" <john@wexfordpress.com>
- **Date:** 2010-11-10T14:18:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com>`

```
When I use FUNCTION RANDOM the same value appears every time the
program is run. This is with OpenCobol. When I use TinyCobol a
different number appears  but again it is the same for each run of the
Tiny Cobol version.

I want a different number to be generated each time the program runs.

Here is my statement:
 COMPUTE RANDUM = FUNCTION RANDOM(8).

John Culleton
```

#### ↳ Re: FUNCTION RANDOM.

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-10T15:37:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<S8FCo.13859$z41.9323@newsfe05.iad>`
- **In-Reply-To:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com>`

```
On 11/10/2010 3:18 PM, john@wexfordpress.com wrote:
> When I use FUNCTION RANDOM the same value appears every time the
> program is run. This is with OpenCobol. When I use TinyCobol a
…[8 more quoted lines elided]…
> John Culleton

While both compilers return 'a same number', it suggests to me there is 
nothing wrong with the compilers. Looks like they are being consistent.

So it has to be you :-)

Some initializing problem perhaps ? Are you calling a sub-program that 
uses the Random function. The glitch is in all probability staring you 
in the face. (You will kick yourself if you find that to be the case - 
we've all been there !). Care to post snippets of code of what you are 
doing. Don't give us what you THINK WE NEED - give us the COMPLETE CODE 
that is doing this.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: FUNCTION RANDOM.

- **From:** "john@wexfordpress.com" <john@wexfordpress.com>
- **Date:** 2010-11-10T14:41:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4f195c9e-8571-4297-837e-886523965a01@r14g2000yqa.googlegroups.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com> <S8FCo.13859$z41.9323@newsfe05.iad>`

```
On Nov 10, 5:37 pm, James Gavan <jga...@shaw.ca> wrote:
> On 11/10/2010 3:18 PM, j...@wexfordpress.com wrote:
>
…[24 more quoted lines elided]…
> Jimmy, Calgary AB

OK here is a test program, including irrelevant matter:
000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID. TEMPLATE.
000030 AUTHOR. JOHN CULLETON.
000040 INSTALLATION. WEXFORDPRESS
000045               Eldersburg MD.
000050*REMARKS.
000060*    THIS IS A TEMPLATE FOR OPEN COBOL AND HTCOBL.
000070 ENVIRONMENT DIVISION.
000080
000090 CONFIGURATION SECTION.
000100 SOURCE-COMPUTER.
000110      Linux.
000120 OBJECT-COMPUTER.
000230      Linux.
000140
000150 INPUT-OUTPUT SECTION.
000160 FILE-CONTROL.
000170    SELECT INFILE ASSIGN TO "SIGFILE"
           ORGANIZATION IS INDEXED ACCESS IS
           DYNAMIC RECORD KEY IS KEYREC.
000180 DATA DIVISION.
000190
000200 FILE SECTION.
       FD  INFILE.
       01  MAIN-REC.
               05 KEYREC PIC 99.
               05 LINE-REC PICTURE X(72) OCCURS 6 TIMES.
000220 WORKING-STORAGE SECTION.
       77  RANDUM PICTURE S9V9(10).
000240 PROCEDURE DIVISION.
000250 001-MAIN-PROCEDURE.
      *    OPEN I-O INFILE.
           COMPUTE RANDUM = FUNCTION RANDOM(8).
           COMPUTE KEYREC = RANDUM * 100.
           DISPLAY KEYREC.
           DISPLAY RANDUM.
      *    CLOSE INFILE.
           STOP RUN.

See?
```

###### ↳ ↳ ↳ Re: FUNCTION RANDOM.

- **From:** James Gavan <jgavan@shaw.ca>
- **Date:** 2010-11-10T16:52:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KeGCo.20826$NM2.2619@newsfe22.iad>`
- **In-Reply-To:** `<4f195c9e-8571-4297-837e-886523965a01@r14g2000yqa.googlegroups.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com> <S8FCo.13859$z41.9323@newsfe05.iad> <4f195c9e-8571-4297-837e-886523965a01@r14g2000yqa.googlegroups.com>`

```
On 11/10/2010 3:41 PM, john@wexfordpress.com wrote:
> On Nov 10, 5:37 pm, James Gavan<jga...@shaw.ca>  wrote:
>> On 11/10/2010 3:18 PM, j...@wexfordpress.com wrote:
…[67 more quoted lines elided]…
> See?

Yep ! That was a real quick response :-) But what actually is in that 
file. I've never used Randomizing.

Can't post the whole damn thing here, it's much too large. Written by 
Jerome Garfunkel using M/F Net Express. He, many moons ago, used to be 
on J4 and he's the brother of the singer. (His total example is 
screaming for a GUI Dialog).

I've extracted what he did for Random. The source is followed by the DOS 
screen results. If you are interested in getting his source for ALL 
functions then e-mail me and I'll send a zipfile.

Jimmy

*****************************************************************
* The Following program "Random" is nested in "Cobol89         *
*****************************************************************
*****************************************************************
* This program uses the following intrinsic functions.          *
*    RANDOM      CURRENT-DATE     NUMVAL        SQRT            *
*                                                               *
* The RANDOM functions has two formats - one with and argument  *
* and one without an argument.  When using the RANDOM function  *
* with an argument ("seed value") the same seed value will      *
* cause the RANDOM function to return the same random value.    *
* This is particularly useful for "regression testing" during   *
* program development.                                          *
*****************************************************************
  IDENTIFICATION DIVISION.
  PROGRAM-ID. Random-JG.      *> That's Jerome not me :-) !
*AUTHOR.  Jerome Garfunkel.
  ENVIRONMENT DIVISION.
  DATA DIVISION.
  WORKING-STORAGE SECTION.
  1   random-return-values.
      3  first-in-random-sequence PIC 9(6)V9(12).
      3  next-in-random-sequence  PIC 9(6)V9(12).

  1   seed-value                  PIC 9(6)    VALUE 32767.

  1   square-root-of-seed         PIC  Z(6).9(6).

  1   repeat-response             PIC XXX.
      88  the-user-wants-another-demo  VALUE "Y" "y" "YES" "yes".

  1   current-date-and-time       PIC  x(21).

  PROCEDURE DIVISION.
*****************************************************************
* All program functions are controled from this procedure       *
*****************************************************************
  Program-Functions.

      PERFORM Random-Function-With-Seed
      PERFORM Random-Function-Without-Seed
      PERFORM Random-Function-With-Time-Seed
      PERFORM Repeat-Demo-Question

      IF the-user-wants-another-demo GO TO Program-Functions.

      EXIT PROGRAM.
      STOP RUN.
*****************************************************************
* The next procedure returns a Random value based on the seed-  *
* value (argument).  The same seed value causes the RANDOM      *
* function to return the same "random" value. This is           *
* particularly useful while regression testing                  *
* a program during development.                                 *
*****************************************************************
  Random-Function-With-Seed.

      INITIALIZE random-return-values.

      COMPUTE first-in-random-sequence
            = FUNCTION RANDOM (seed-value)
      END-COMPUTE.

      DISPLAY "The random value returned is "
              first-in-random-sequence.

*****************************************************************
* The next procedure returns a Random value with no seed-value  *
* (argument).  The next "random" number in sequence is returned *
* by the RANDOM function.                                       *
*****************************************************************
  Random-Function-Without-Seed.

      COMPUTE next-in-random-sequence
            = FUNCTION RANDOM
      END-COMPUTE.

      DISPLAY "The random value returned is "
               next-in-random-sequence.

*****************************************************************
* The next procedure is a more realistic version of the Random  *
* function that  might be used in applications.                 *
* The seed value that is used here is the "hundreth-of-seconds" *
* postions of the Current-Date function (positions 15, 16).     *
* Note the use of Reference Modification to reference the 15th  *
* and 16th positions from the 21 total positions of date/time   *
* information returned by the Current Date Function.  Also note *
* the Random function, when used with a "seed" value must       *
* provide an "integer" value for the argument.  The NUMVAL      *
* Function is used to convert the two positions of Current-date *
* into an integer for use in the Random Function .  Furthermore *
* the CURRENT-DATE function is "nested" in the NUMVAL function -*
* that is, the returned value of the CURRENT-DATE function      *
* serves as the argument for the NUMVAL function.               *
*****************************************************************
  Random-Function-With-Time-Seed.

      INITIALIZE random-return-values.

      COMPUTE seed-value
           =  FUNCTION NUMVAL (FUNCTION CURRENT-DATE (15 : 2))
           *  FUNCTION NUMVAL (FUNCTION CURRENT-DATE (15 : 2))

      COMPUTE square-root-of-seed
         =    FUNCTION SQRT (seed-value)

      COMPUTE first-in-random-sequence
           =  FUNCTION RANDOM (seed-value)

      END-COMPUTE.

      DISPLAY "The seed value used is "
              seed-value

      DISPLAY "The random value returned is "
              first-in-random-sequence.

*****************************************************************
* The next procedure determines if demo is to be run again.     *
* "y" or "Y" or "yes" or "YES" will re-run demo.  Anything else *
* will end the demo program.                                    *
*****************************************************************
  Repeat-Demo-Question.

      Display "Do you want to repeat demo for: "
              "function-to-demo - yes/no? "
              WITH NO ADVANCING

      ACCEPT  repeat-response.
  END PROGRAM Random-JG.

*****************************************
These are the results I got from runs :-
*****************************************
The random value returned is 000000288687194742
The random value returned is 000000085899342787
The seed value used is 000001
The random value returned is 000000476382794811
Do you want to repeat demo for: function-to-demo - yes/no? y
The random value returned is 000000476382794811
The random value returned is 000000547849351424
The seed value used is 003600
The random value returned is 000000874462619487
Do you want to repeat demo for: function-to-demo - yes/no? y
The random value returned is 000000874462619487
The random value returned is 000000307827435990
The seed value used is 009216
The random value returned is 000000264742223651
Do you want to repeat demo for: function-to-demo - yes/no? y
The random value returned is 000000264742223651
The random value returned is 000000092777956393
The seed value used is 005625
The random value returned is 000000914226899835
Do you want to repeat demo for: function-to-demo - yes/no?
```

###### ↳ ↳ ↳ Re: FUNCTION RANDOM.

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-11-11T12:12:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cceod6hccg30s2hfhe8f641ij1vs1uj3j5@4ax.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com> <S8FCo.13859$z41.9323@newsfe05.iad> <4f195c9e-8571-4297-837e-886523965a01@r14g2000yqa.googlegroups.com>`

```
On Wed, 10 Nov 2010 14:41:12 -0800 (PST), "john@wexfordpress.com"
<john@wexfordpress.com> wrote:

>000250 001-MAIN-PROCEDURE.
>      *    OPEN I-O INFILE.
…[7 more quoted lines elided]…
>See?

For a given seed, RANDOM will pull up a given value.   Typically you
use the most random seed you can for the first iteration, then use
your result as the next input.

e.g.:
MOVE FUNCTION CURRENT-DATE TO SYSTEM-DATE.             
MOVE SYSTEM-TIME-CC     TO SEED-VALUE                  
PERFORM 20 TIMES                                       
    COMPUTE MY-NUM     = FUNCTION RANDOM (SEED-VALUE)  
    COMPUTE SEED-VALUE = MY-NUM * 100000               
    DISPLAY 'SEED-VALUE"' SEED-VALUE '"'               
           
END-PERFORM                                            
```

###### ↳ ↳ ↳ Re: FUNCTION RANDOM.

_(reply depth: 4)_

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-12T04:40:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c000ec77-cb2d-45d8-ac30-3526569924f8@r6g2000vbf.googlegroups.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com> <S8FCo.13859$z41.9323@newsfe05.iad> <4f195c9e-8571-4297-837e-886523965a01@r14g2000yqa.googlegroups.com> <cceod6hccg30s2hfhe8f641ij1vs1uj3j5@4ax.com>`

```
On Nov 11, 7:12 pm, Howard Brazee <how...@brazee.net> wrote:
> On Wed, 10 Nov 2010 14:41:12 -0800 (PST), "j...@wexfordpress.com"
>
…[31 more quoted lines elided]…
> - James Madison

Good for testing but better is to use the time seed with a new current
time each invocation of the random function.
```

##### ↳ ↳ Re: FUNCTION RANDOM.

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-11-10T17:20:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FMFCo.371145$pX3.45199@en-nntp-11.dc1.easynews.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com> <S8FCo.13859$z41.9323@newsfe05.iad>`

```
The rules for COBOL *require* that if you give the same "seed" number, then 
you MUST get the same "series" of returned values for the RANDOM function. 
The compilers are working "as required".

In order to get DIFFERENT numberts, you need to use different seed numbers. 
This is often done by using the time of day (seconds - for example) as the 
seed value. The more digits you use as the seed value, the more likely it is 
to get "unique" returned values.

See (for example), the statement at:

 http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/IGY3LR50/7.1.38

"For a given seed value, the sequence of pseudorandom numbers is always the 
same. "

If you check the "language reference" (or ANSI/ISO Standards) you will see 
the same text.

"James Gavan" <jgavan@shaw.ca> wrote in message 
news:S8FCo.13859$z41.9323@newsfe05.iad...
> On 11/10/2010 3:18 PM, john@wexfordpress.com wrote:
>> When I use FUNCTION RANDOM the same value appears every time the
…[23 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: FUNCTION RANDOM.

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2010-11-11T00:11:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1dadnWy35ZSXFEbRnZ2dnUVZ5uKdnZ2d@giganews.com>`
- **In-Reply-To:** `<FMFCo.371145$pX3.45199@en-nntp-11.dc1.easynews.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com> <S8FCo.13859$z41.9323@newsfe05.iad> <FMFCo.371145$pX3.45199@en-nntp-11.dc1.easynews.com>`

```
On 11/10/2010 5:20 PM, Bill Klein wrote:
> The rules for COBOL *require* that if you give the same "seed" number, then
> you MUST get the same "series" of returned values for the RANDOM function.
…[17 more quoted lines elided]…
> (snip)

In order to get a series of pseudo random numbers, the first instance of 
FUNCTION RANDOM must have a seed argument, and every subsequent 
invocation must omit the seed argument:

COMPUTE MY-RANDOM-NUMBER = FUNCTION RANDOM(SEED-VALUE)   <== first time

COMPUTE MY-RANDOM-NUMBER = FUNCTION RANDOM  <== every other time

If you're building a simulation and you need to test with the same 
series of pseudo random numbers, then always start with the same seed 
argument.  If you need a less predictable series of pseudo random 
numbers, then use something like time of day in milliseconds as your 
seed argument.

Don't forget that the pseudo random number returned is always a value 
between zero and one.
```

###### ↳ ↳ ↳ Re: FUNCTION RANDOM.

- **From:** Anonymous <cripto@ecn.org>
- **Date:** 2010-11-11T16:09:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20101111150934.466411A7925@www.ecn.org>`
- **References:** `<FMFCo.371145$pX3.45199@en-nntp-11.dc1.easynews.com>`

```
> The rules for COBOL *require* that if you give the same "seed" number,
> then you MUST get the same "series" of returned values for the RANDOM
> function.
> The compilers are working "as required".

I would add, this is true of every standard pseudo-random number generator.
They all work on the principle. You must provide (or use a default) seed and
given the same seed they will always produce the same sequence. This is how
pseudo-random number generators work. COBOL isn't unique in this, although
if there is some standard that specifies it, it's really just documenting
(also good!) the restriction/behavior of the underlying PRNG, not
introducing anything new.
```

#### ↳ Re: FUNCTION RANDOM.

- **From:** Alistair Maclean <alistair.j.l.maclean@googlemail.com>
- **Date:** 2010-11-11T03:51:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4048f3ed-e292-4c86-a8a6-a691b43ed4f7@z9g2000yqz.googlegroups.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com>`

```
On Nov 10, 10:18 pm, "j...@wexfordpress.com" <j...@wexfordpress.com>
wrote:
> When I use FUNCTION RANDOM the same value appears every time the
> program is run. This is with OpenCobol. When I use TinyCobol a
…[8 more quoted lines elided]…
> John Culleton

You may also like to check to see if the random function returns a
random number or a pseudo-random number. There is an algorithm
available to do that (but I can't remember where to get it).
```

##### ↳ ↳ Re: FUNCTION RANDOM.

- **From:** abrsvc <dansabrservices@yahoo.com>
- **Date:** 2010-11-11T06:02:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0fa7d58e-0ac7-4294-881a-90f38075f04f@s11g2000prs.googlegroups.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com> <4048f3ed-e292-4c86-a8a6-a691b43ed4f7@z9g2000yqz.googlegroups.com>`

```
On Nov 11, 6:51 am, Alistair Maclean
<alistair.j.l.macl...@googlemail.com> wrote:
> On Nov 10, 10:18 pm, "j...@wexfordpress.com" <j...@wexfordpress.com>
> wrote:
…[15 more quoted lines elided]…
> available to do that (but I can't remember where to get it).

Please note that ALL values returned by any "random number generator"
are pseudo random.  Since these numbers are "generated", by definition
they are not truely random.  Different algorithms will generate longer
strings of non-repeatable values which appear to be somewhat random.
The longer the "repeat" interval, the more random the numbers.  There
are whole studies on differing generators.  The formula used by most
"random" functions is rather simple and has a relatively short repeat
string (in other words, the same pattern of values will be repeated
relatievly quickly).  For most applications this is sufficient.

As others have stated, in order to be able to debug the functions of a
program, most start with a fixed seed.  This will insure the same
sequence of random numbers be generated each run.  Once the debug
phase has completed, using a time value is the most common way of
seeding or starting the random number sequence that won't typically be
a repeatable sequence.

Dan
```

#### ↳ Re: FUNCTION RANDOM.

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2010-11-11T11:40:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33eod6dh6dglehpf7ubiq64kkfbs0i4klf@4ax.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com>`

```
On Wed, 10 Nov 2010 14:18:49 -0800 (PST), "john@wexfordpress.com"
<john@wexfordpress.com> wrote:

>Here is my statement:
> COMPUTE RANDUM = FUNCTION RANDOM(8).

You might try starting off with a time-date stamp seed value.
```

#### ↳ Re: FUNCTION RANDOM.

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2010-11-11T16:35:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SIidnen2c9k48kHRnZ2dnUVZ_sGdnZ2d@earthlink.com>`
- **References:** `<8ebd5cc6-869e-4d81-b376-6737853d79c3@l17g2000yqe.googlegroups.com>`

```
john@wexfordpress.com wrote:
> When I use FUNCTION RANDOM the same value appears every time the
> program is run. This is with OpenCobol. When I use TinyCobol a
…[7 more quoted lines elided]…
>

Dilbert is being given a tour of the accounting department by the head 
accounting troll:

"This is our random number generator"

"NINE, NINE, NINE, NINE,..." says another troll.

"Doesn't sound random to me," observes Dilbert.

"Ah, but with random numbers, you can't be sure!"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
