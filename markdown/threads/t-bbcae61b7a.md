[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RANDOM Generator

_7 messages · 7 participants · 1998-03_

---

### RANDOM Generator

- **From:** "peter van den wildenbergh" <ua-author-17075080@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6eu3vp$7kj$1@news1.skynet.be>`

```

Does somebody have a good procedure to generate my own random figures in
COBOL.
The Deskware compiler I'am using doesn't support RANDOM...
```

#### ↳ Re: RANDOM Generator

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bbcae61b7a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6eu3vp$7kj$1@news1.skynet.be>`
- **References:** `<6eu3vp$7kj$1@news1.skynet.be>`

```

Van den Wildenbergh wrote in message <6eu3vp$7kj$1.··.@new··t.be>...
› Does somebody have a good procedure to generate my own random figures in
› COBOL.
› The Deskware compiler I'am using doesn't support RANDOM...
›
›

Get a compiler that supports current ANSI COBOL syntax, then you can use
the RANDOM intrinsic function. (Depending on exactly what you want to do,
you might want to pass the time-of-day - from FUNCTION CURRENT-DATE to it as
a seed value.)
```

##### ↳ ↳ Re: RANDOM Generator

- **From:** "ross klatte" <ua-author-8441791@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bbcae61b7a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bbcae61b7a-p2@usenetarchives.gap>`
- **References:** `<6eu3vp$7kj$1@news1.skynet.be> <gap-bbcae61b7a-p2@usenetarchives.gap>`

```

William M. Klein wrote in article
<6euaim$q.··.@sjx··m.com>...
› Van den Wildenbergh wrote in message <6eu3vp$7kj$1.··.@new··t.be>...
›› Does somebody have a good procedure to generate my own random figures in
…[23 more quoted lines elided]…
› 
In general the procedure is as follows:
Declare a variable Big Number, say, a 9 digit integer.
Declare a constant Multiplierï¿½say, a 5 digit integer.
Enter a Random Seedï¿½time of day measured in seconds is usually okay.
Move the Random Seed to the Big Number.
RNG:
Multiply the Big Number by the Multiplier, storing the result in Big
Number. (Note that different makers treat Integer Overflow errors
differentlyï¿½you may have to program around that.)
Move the middle digitsï¿½for example, digits 3-7 of a 9-digit numberï¿½
to, say, a 5 digit field, Percentage.
Divide Percentage by 100000.
Percentage can now contain any probability from 0 to 100.
If you are looking for a specific range of integers, just divide
Percentage by the number of items in the range.
If you need another, go to RNG.

Be careful choosing the Multiplierï¿½some of them are not very helpful.
For example, using 00001 as the Multiplier would be a particularly
bad choice. Other Multipliers can react with the Random Seed to
produce an undesirable repeated sequence very quickly.

Another more reliable but less efficient Random Number Generator is
to ask three computer programmers to spell "Mississippi" and then
count the total number of s's.

Ross

http://www.geocities.com/Hollywood/Set/7185/
```

##### ↳ ↳ Re: RANDOM Generator

- **From:** "bstr..." <ua-author-7882617@usenetarchives.gap>
- **Date:** 1998-03-28T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bbcae61b7a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bbcae61b7a-p2@usenetarchives.gap>`
- **References:** `<6eu3vp$7kj$1@news1.skynet.be> <gap-bbcae61b7a-p2@usenetarchives.gap>`

```

On Fri, 20 Mar 1998 09:55:14 -0800, "William M. Klein"
wrote:

› Van den Wildenbergh wrote in message <6eu3vp$7kj$1.··.@new··t.be>...
›› Does somebody have a good procedure to generate my own random figures in
…[8 more quoted lines elided]…
› a seed value.)

Bill is right, but if you really insist... I make no warrantees or
guarantees on this code. It's IBM VC COBOL II r3 (pre intrinsic
functions). I used it for a project a number of years ago, and it
worked good enough. It's based on the algorithm from Knuth's book, so
if I implemented it right it should be pretty fair.

You're welcome to it - provided:

1) you don't use it for outright commercial gain (i.e. sell it by
itself without substantial added value),
2) it's totally at your own risk, and
3) you probably should give credit, (i.e. "Based on KPMG Peat Marwick
LLP's PCHLRAND routine, used by permission")

-----Burton


IDENTIFICATION DIVISION.

PROGRAM-ID. PCHLRAND.

AUTHOR. KPMG PEAT MARWICK.

DATE-WRITTEN. April 1995.

DATE-COMPILED.

*REMARKS. Random number generation

*

* This generator 'shuffles' a sequence of characters

*

* On entry:

* LS-PCHLRAND-DATA contains the data

* LS-PCHLRAND-LIMIT set to the number of data items

*

* On exit:

* LS-PCHLRAND-DATA contains data in a random

* ordering

*

* Basic generator is Knuth's Algorithm M (V2 pg 31)

*

*
*
SOM95 * 04/ /95 B.STRAUSS Initial version
*
*
*

*---------------------------------------------------------------*



ENVIRONMENT DIVISION.

EJECT

DATA DIVISION.

WORKING-STORAGE SECTION.



01 WS-CONSTANTS.

05 WS-GEN-X-A PIC S9(11) COMP-3 VALUE 3141592653.

05 WS-GEN-X-C PIC S9(11) COMP-3 VALUE 2718281829.

05 WS-GEN-Y-A PIC S9(11) COMP-3 VALUE 2718281829.

05 WS-GEN-Y-C PIC S9(11) COMP-3 VALUE 3141592653.

05 WS-2E35 PIC S9(11) COMP-3 VALUE 34359738368.



01 WS-WORK.

05 WS-WORK-X PIC S9(15) COMP-3.

05 WS-WORK-Y PIC S9(15) COMP-3.

05 WS-GEN-X PIC S9(11) COMP-3.

05 WS-GEN-Y PIC S9(11) COMP-3.

05 WS-RANDOM PIC S9(11) COMP-3.

05 WS-QUOTIENT PIC S9(11) COMP-3.

05 WS-REMAINDER PIC S9(11) COMP-3.

05 WS-GEN-K PIC S9(4) COMP VALUE +100.

05 WS-GEN-J PIC S9(4) COMP.

05 WS-SUB PIC S9(4) COMP.

05 WS-SWAP-A PIC S9(4) COMP.

05 WS-SWAP-B PIC S9(4) COMP.

05 WS-TIME PIC 9(8).

05 WS-DATE PIC 9(6).

05 FILLER REDEFINES WS-DATE.

10 WS-DATE-123 PIC 9(3).

10 WS-DATE-456 PIC 9(3).

05 WS-DISPLAY PIC ---,---,---,--9.



01 WS-HOLD.

05 WS-HOLD-DATA OCCURS 100.

10 WS-HOLD-ENTRY PIC S9(11) COMP-3.

05 WS-HOLD-PCHLPARM-ITEM PIC X(9).



LINKAGE SECTION.

01 LS-PCHLRAND-PARMS.

05 LS-PCHLRAND-LIMIT PIC S9(5) COMP-3.

05 LS-PCHLRAND-DATA.

10 LS-PCHLRAND-ENTRY OCCURS 1 TO 99999

DEPENDING ON LS-PCHLRAND-LIMIT.

15 LS-PCHLRAND-ITEM PIC X(9).



PROCEDURE DIVISION USING LS-PCHLRAND-PARMS.

0000-MAIN-LINE.



PERFORM 1000-INITIALIZE

PERFORM 2000-SHUFFLE

GOBACK

.



1000-INITIALIZE.

* X0

ACCEPT WS-TIME FROM TIME

MOVE WS-TIME TO WS-GEN-X



* Y0

ACCEPT WS-DATE FROM DATE

COMPUTE WS-GEN-Y =

99999999999 -

(WS-DATE-456 * 100000000) -

WS-DATE-123

PERFORM

VARYING WS-SUB

FROM 1

BY 1

UNTIL WS-SUB > WS-GEN-K

PERFORM 4000-GEN-X

MOVE WS-GEN-X TO

WS-HOLD-ENTRY (WS-SUB)



END-PERFORM

.



2000-SHUFFLE.

PERFORM

VARYING WS-SUB

FROM 1

BY 1

UNTIL WS-SUB > LS-PCHLRAND-LIMIT

PERFORM 3000-ALGO-M

COMPUTE WS-SWAP-A =

(LS-PCHLRAND-LIMIT * WS-RANDOM) /

WS-2E35 + 1

PERFORM 3000-ALGO-M

COMPUTE WS-SWAP-B =

(LS-PCHLRAND-LIMIT * WS-RANDOM) /

WS-2E35 + 1

MOVE LS-PCHLRAND-ITEM (WS-SWAP-A)

TO WS-HOLD-PCHLPARM-ITEM

MOVE LS-PCHLRAND-ITEM (WS-SWAP-B)

TO LS-PCHLRAND-ITEM (WS-SWAP-A)

MOVE WS-HOLD-PCHLPARM-ITEM

TO LS-PCHLRAND-ITEM (WS-SWAP-B)



END-PERFORM

.



3000-ALGO-M.

PERFORM 4000-GEN-X

PERFORM 5000-GEN-Y

COMPUTE WS-GEN-J =

(WS-GEN-K * WS-GEN-Y) /

WS-2E35 + 1

* 1<=J<=K

MOVE WS-HOLD-ENTRY (WS-GEN-J) TO WS-RANDOM

MOVE WS-GEN-X TO WS-HOLD-ENTRY (WS-GEN-J)

.



4000-GEN-X.

COMPUTE WS-WORK-X =

WS-GEN-X *

WS-GEN-X-A +

WS-GEN-X-C

DIVIDE WS-WORK-X

BY WS-2E35

GIVING WS-QUOTIENT

REMAINDER WS-GEN-X

.



5000-GEN-Y.

COMPUTE WS-WORK-Y =

WS-GEN-Y *

WS-GEN-Y-A +

WS-GEN-Y-C

DIVIDE WS-WORK-Y

BY WS-2E35

GIVING WS-QUOTIENT

REMAINDER WS-GEN-Y
```

###### ↳ ↳ ↳ Re: RANDOM Generator

- **From:** "fernando sevilla fdez." <ua-author-6588958@usenetarchives.gap>
- **Date:** 1998-03-28T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bbcae61b7a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bbcae61b7a-p4@usenetarchives.gap>`
- **References:** `<6eu3vp$7kj$1@news1.skynet.be> <gap-bbcae61b7a-p2@usenetarchives.gap> <gap-bbcae61b7a-p4@usenetarchives.gap>`

```

Sabe alguien por que no funciona las rutinas internas de rmcobol v6.08
para windows c$mbar

Saludos
```

###### ↳ ↳ ↳ Re: RANDOM Generator

_(reply depth: 4)_

- **From:** "nop0..." <ua-author-471015@usenetarchives.gap>
- **Date:** 1998-03-28T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bbcae61b7a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bbcae61b7a-p5@usenetarchives.gap>`
- **References:** `<6eu3vp$7kj$1@news1.skynet.be> <gap-bbcae61b7a-p2@usenetarchives.gap> <gap-bbcae61b7a-p4@usenetarchives.gap> <gap-bbcae61b7a-p5@usenetarchives.gap>`

```

On Sun, 29 Mar 1998 17:24:58 +0100, "Fernando Sevilla Fdez."
wrote:

› Sabe alguien por que no funciona las rutinas internas de rmcobol v6.08
› para windows c$mbar
›
› Saludos

Si io lo se. Pero Cercosoft lo sabe tambiem. Habla con tus compadres.

Saludos.

Frederico Fonseca
```

#### ↳ Re: RANDOM Generator

- **From:** "Anonymous" <ua-author-9618@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bbcae61b7a-p7@usenetarchives.gap>`
- **In-Reply-To:** `<6eu3vp$7kj$1@news1.skynet.be>`
- **References:** `<6eu3vp$7kj$1@news1.skynet.be>`

```


Peter Van den Wildenbergh wrote in message
› Does somebody have a good procedure to generate my own random figures in
› COBOL.


Go to http://www.etk.com and download the ETKPK subroutine library.
It has a random number generator.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
