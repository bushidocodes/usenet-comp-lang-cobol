[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Lilian Dates Code needed.

_6 messages · 4 participants · 1997-03_

---

### Lilian Dates Code needed.

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-03-10T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>`

```

I need some code.

My compiler doesn't have integer of date. I need some code to take
YYYYMMDD dates and convert them to and from an integer. Anyone have
anything they would like to share?
```

#### ↳ Re: Lilian Dates Code needed.

- **From:** "ni..." <ua-author-15612150@usenetarchives.gap>
- **Date:** 1997-03-10T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-802fe9cad1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>`
- **References:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>`

```

On 11 Mar 1997 16:59:38 GMT, "Thane Hubbell" wrote:

› I need some code.  
› 
…[3 more quoted lines elided]…
› 


If your date format can be redefined as (for example) :-

01 WSAA-STRING-DATE PIC X(08).
01 WSAA-NUMERIC-DATE PIC 9(08) REDEFINES WSAA-STRING-DATE.

You can convert to a binary field :

01 WSAA-BINARY-DATE PIC 9(08) COMP.

This produces a relatively compact (4 byte) version of the date. There are
various ways that you could reduce the size further, but this will enable your
applications to be year 2000 compliant, will have little effect on speed and
saves on disk space.

Hope this helps.

Nigel Benson
```

##### ↳ ↳ Re: Lilian Dates Code needed.

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-03-11T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-802fe9cad1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-802fe9cad1-p2@usenetarchives.gap>`
- **References:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell> <gap-802fe9cad1-p2@usenetarchives.gap>`

```



N Benson wrote in article
<332··.@new··o.uk>...
› On 11 Mar 1997 16:59:38 GMT, "Thane Hubbell"  wrote:
› 
…[23 more quoted lines elided]…
› saves on disk space.

Thanks Nigel, you jumped to the Logical assumption here, that I am seeking
Y2K compliance. My applicaiton is already compliant. What I need the
routines for is so that I can compute the lilian dates from 2 gregorian
dates and determine the days elapsed, and to use a gregorian date along
with a number of days to elapse, and then produce a second date.

My compiler version does not support he intrinsic functions, so I'm looking
to do this on my own in COBOL.
```

#### ↳ Re: Lilian Dates Code needed.

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-03-11T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-802fe9cad1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>`
- **References:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>`

```

What I think you may be asking for is an emulation of INTEGER OF DATE and DATE OF INTEGER....

If so, such a beast does exist, along with emulations of the other 3 date related intrinsic functions - DAY OF INTEGER, INTEGER OF DAY, and CURRENT-DATE.

Unfortunately its a product.

Fortunately cheap (by some standards).

Called Bridge to the Next Century.

If this is the type of beastie you are seeking, advise. Please also advise compiler / environment.

Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

#### ↳ Re: Lilian Dates Code needed.

- **From:** "john mckown" <ua-author-1779298@usenetarchives.gap>
- **Date:** 1997-03-13T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-802fe9cad1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>`
- **References:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>`

```

Thane,
The following COBOL program should do what you want. I have tested the code
on my PC using the Fujitsu COBOL compiler. However, the usual disclaimers
apply. Actually, I only did ONE test and the test is self-contained. The
final display should be 148138 which, according to my book, is the Lilian
date for 16 May 1988. That's the result that I got. Hope this helps you
some! Oh, yea, the original code I wrote in IBM S/370 assembler. It convert
it to PC COBOL, I scribbled the algorithm into Excel then into COBOL.
Please be kind about my weird way of writing COBOL, I'm an MVS Systems
Programmer, not a real COBOL programmer (for good or ill ).

ID DIVISION.
PROGRAM-ID. DATELIL.
AUTHOR. JOHN MCKOWN.
INSTALLATION. UICI LIFE INSURANCE CENTER.
DATE-WRITTEN.
DATE-COMPILED.
SECURITY. NONE.

ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SOURCE-COMPUTER. IBM-370.
OBJECT-COMPUTER. IBM-370.
INPUT-OUTPUT SECTION.
FILE-CONTROL.
I-O-CONTROL.
DATA DIVISION.
FILE SECTION.
*
WORKING-STORAGE SECTION.
01 CONSTANTS.
05 CONST-DAYS-PER-400-YEARS PIC S9(8) VALUE +146097.
05 CONST-DAYS-PER-4-YEARS PIC S9(8) VALUE +1461.
05 CONST-DAYS-PER-5-MONTHS PIC S9(8) VALUE +153.
05 CONST-BASE-JULIAN PIC S9(8) VALUE +1721119.
05 CONST-JAN-01-1900 PIC S9(8) VALUE +2415020.
05 CONST-BASE-LILIAN PIC S9(15) VALUE +2299160.
01 TEST-DATE.
05 TEST-MONTH PIC 99 VALUE 5.
05 TEST-DAY PIC 99 VALUE 16.
05 TEST-YEAR PIC 9999 VALUE 1988.
77 WS-MONTH PIC S9(15).
77 WS-YEAR PIC S9(15).
77 WS-CENTURY PIC S9(15).
77 WS-YEAR-IN-CENTURY PIC S9(15).
77 WS-DAYS-IN-CENTURY PIC S9(15).
77 WS-DAYS-IN-YEAR PIC S9(15).
77 WS-DAY-JULIAN PIC S9(15).
77 WS-DATE-JULIAN PIC S9(15).
77 WS-DATE-LILIAN PIC S9(15).

* ACCORDING TO MY BOOK 16 MAY 1988 IS LILIAN DATE 148138. USED TO
CHECK LOGIC.

LINKAGE SECTION.
PROCEDURE DIVISION.
START-UP.
IF TEST-MONTH < 3 THEN
ADD +9 TO TEST-MONTH GIVING WS-MONTH
SUBTRACT +1 FROM TEST-YEAR GIVING WS-YEAR
ELSE
SUBTRACT +3 FROM TEST-MONTH GIVING WS-MONTH
MOVE TEST-YEAR TO WS-YEAR
END-IF
DIVIDE WS-YEAR BY 100
GIVING WS-CENTURY
REMAINDER WS-YEAR-IN-CENTURY
DISPLAY 'WS-CENTURY ' WS-CENTURY
DISPLAY 'WS-YEAR-IN-CENTURY ' WS-YEAR-IN-CENTURY
COMPUTE WS-DAYS-IN-CENTURY = TEST-DAY +
WS-CENTURY * CONST-DAYS-PER-400-YEARS / 4
DISPLAY 'WS-DAYS-IN-CENTURY ' WS-DAYS-IN-CENTURY
COMPUTE WS-DAYS-IN-YEAR = WS-DAYS-IN-CENTURY +
WS-YEAR-IN-CENTURY * CONST-DAYS-PER-4-YEARS / 4
DISPLAY 'WS-DAYS-IN-YEAR ' WS-DAYS-IN-YEAR
ADD CONST-BASE-JULIAN TO WS-DAYS-IN-YEAR
GIVING WS-DAY-JULIAN
DISPLAY 'WS-DAY-JULIAN ' WS-DAY-JULIAN
COMPUTE WS-DATE-JULIAN = WS-DAY-JULIAN +
( WS-MONTH * CONST-DAYS-PER-5-MONTHS + 2 ) / 5
DISPLAY 'WS-DATE-JULIAN ' WS-DATE-JULIAN
SUBTRACT CONST-BASE-LILIAN FROM WS-DATE-JULIAN
GIVING WS-DATE-LILIAN
DISPLAY 'WS-DATE-LILIAN ' WS-DATE-LILIAN
.
END PROGRAM DATELIL.



Thane Hubbell wrote in article
<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell>...
› I need some code.  
› 
…[4 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Lilian Dates Code needed.

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-03-16T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-802fe9cad1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-802fe9cad1-p5@usenetarchives.gap>`
- **References:** `<01bc2e3e$7ccb9ca0$e6f548a6@thane-hubbell> <gap-802fe9cad1-p5@usenetarchives.gap>`

```



John McKown wrote in article
<01bc302f$b32d0700$1610edcc@743441631>...
› Thane,
› The following COBOL program should do what you want. I have tested the
…[9 more quoted lines elided]…
› Programmer, not a real COBOL programmer (for good or ill ).


Thanks for posting your program John! I appreciate it. I really enjoy the
exchange of coding practices and methods that happens here. I wish there
was more of it! (Especially as related to different algorithms). Thanks!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
