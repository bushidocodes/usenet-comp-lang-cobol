[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Code Question

_8 messages · 8 participants · 2002-11 → 2002-12_

---

### Code Question

- **From:** "Dali J" <dali@cogeco.ca>
- **Date:** 2002-11-08T11:45:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MMRy9.4778$L47.762264@read2.cgocable.net>`

```
I'm new at COBOL. And I'm confused writing a piece of code that does the
following:(maximum the window for viewing) I am especially confused with
Control Breaks.

WRITE A PROGRAM TO PRODUCE A REPORT THAT WILL INCLUDE CONTROL BREAKS, AS
WELL AS FINAL TOTALS.
USE THE CM2002S FILE AND RECORD LAYOUT FROM THE PREVIOUS ASSIGNMENT.

A MINOR TOTAL BREAK WILL OCCUR WHEN THE DEPARTMENT NUMBER
CHANGES, AND A MAJOR CONTROL BREAK WILL OCCUR WHEN THE STORE
NUMBER CHANGES.  FINAL TOTALS WILL BE PRINTED AT THE END OF THE
JOB.

YOU MAY DESIGN YOUR OWN REPORT LAYOUT, HOWEVER, USE THE ATTRIBUTES
FROM THE EXAMPLE.
NOTE: ZERO SUPPRESSION, AMOUNT FIELDS AND LINE SPACING.

** NOTE **     ALL FIELDS SHOWN MUST BE INCLUDED ON YOUR REPORT
               AND ABOVE ALL, YOUR REPORT MUST BE AESTHETICALLY
               PLEASING (I.E. REPORT AND COLUMNS CENTERED, SPACING
               HEADINGS CENTERED ETC).




ASSIGNMENT DUE: ___________________

YY/MM/DD                           STORE ANALYSIS REPORT
PAGE X
                                                                   BY
                                            DEPARTMENT WITHIN STORE

     STORE      DEPARTMENT   SALESMAN                         YTD
CURRENT
     NUMBER     NUMBER       NAME                            SALES
SALES        COMM

      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
               * TOTAL FOR DEPARTMENT  XX                 XXXXXX0.00
XXXXXX0.00


      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
               * TOTAL FOR DEPARTMENT  XX                 XXXXXX0.00
XXXXXX0.00

              ** TOTAL FOR STORE       XX               XXXXXXXX0.00
XXXXXXXX0.00


      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
      XX         XX          XXX---------------------XX    XXXXX0.00
XXXXX0.00      XX
               * TOTAL FOR DEPARTMENT  XX                 XXXXXX0.00
XXXXXX0.00

              ** TOTAL FOR STORE       XX               XXXXXXXX0.00
XXXXXXXX0.00

             *** FINAL TOTALS                           XXXXXXXX0.00
XXXXXXXX0.00


This is the CM2002S file:
1001004ACHER, WILLIAM C.   019072600575241003000850000000
2
1001185DONNEMAN, THOMAS M. 065042300900191007006700001020
1
1001730REEDE, OWEN W.      090055501051441008010520002310
2
1001960WINGLAND, KEITH E.  005000000350001002000000000000
2
1002111CARTOLER, VIOLET B. 028099800750061204003020001140
1
1002304FROMM, STEVE V.     065000001200001205006090001823
2
1003030ALLOREN, RUTH W.    213202000000001510114000020933
2
1003181DELBERT,EDWARD D.   125065901305541509037540000000
2
1003487KING, MILDRED J.    185089601804291510038260005322
1
1004027ALHOUER, ELAINE E.  011257300220661205001880000400
1
1004171COSTA, NAN S.       058035600560021210013020000903
2
1005308GLEASON, JAMES E.   014500000390001004000925000000
3
1005568LYNNE, GERALD H.    092448701333111007016530001428
1
1005909UDSON, DORIS M.     015449900303251004000780000000
2
1006292EVERLEY, DONNA M.   033200001775000502000322000322
2
1006409ICK, MICK W.        041012201950800502000590000590
2
1006607ODELLE, NICHOLAS P. 058250701875070503006220006220
3
1006825TILLMAN, DON M.     123044401995090505019230004665
1
1007214EDMONSON, RICK T.   007906700330571003000290000000
2
1007310GORMALLY, MARIE N.  038902200640551006007320000866
1
1008322HARLETON, JEAN H.   078089901200891506010180000000
2
1008505LAMBERT, JERRY O.   015400100407451504002840000000
5
1008921ULL, GEORGE A.      180200002000001509034090012080
1
1009105BOYLE, RALPH P.     087804401430551206016070007787
2
1009215EDSON, WILBUR S.    060705000820051207011885001575
2
1009574MELTZ,FRANK K.      075436600590301210015760000000
1
1009820TELLER, STEPHEN U.  195704401770091210051920032222
3
2001300FELDMAN, MIKE R.    025000000300001009000600000000
2
2001325HATFIELD, MARK I.   015112200205391007001840000220
1
2002590NEIL,CLARENCE N.    075006500950231208014000002324
2
2002801SCHEIBER, HARRY T.  009523700325081203000520000520
3
2002958WANGLEY, THEO. A.   012000000150001207001720000275
1
2003311GROLER, GRACE B.    230064302054201510260480048369
1
2003318HANEY, CAROL S.     097500001450001505012020006019
3
2003834TRAWLEY, HARRIS T.  057732600550001510011000001329
2
2004317HANBEE, ALETA O.    038500000395001210007530001180
2
2004721RASSMUSEN, JOHN J.  081000001000001208017680002346
1
2004739RIDEL, ROBERT R.    055750400825711207033303007224
3
2004806STOCKTON, NORMAN Q. 067250700725881209013380013380
2
2005122CENNA, DICK L.      035577700440011008003270000000
1
2005207EBERHARDT,RON G.    056400700940091006006300000980
2
2006100BATES, TONY F.      081906602076450504088340005170
1
2006179DAMSON, ERIC C.     035250201808880502000223000223
2
2007332HELD, ANNA J.       024400000295001009005115000926
3
2007689OWNEY, REED M.      043778800530661009008635001132
2
2007802SHEA, MICHAEL H.    064203300820091008012920004680
1
2008102BELLSLEY, ARTHUR A. 088300000990001509019033002762
1
3008282ESTABAN, JUAN L.    198405500000001510040505005050
2
3009315HALE, ALAN A.       127400001680001208025954003829
2
3009740RIDGEFIELD, SUZY S. 180417801905061210033024002310
1


Any help with this would be grealty appricated,
Dali
```

#### ↳ Re: Code Question

- **From:** docdwarf@panix.com
- **Date:** 2002-11-08T12:06:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqgquu$sjb$1@panix1.panix.com>`
- **References:** `<MMRy9.4778$L47.762264@read2.cgocable.net>`

```
In article <MMRy9.4778$L47.762264@read2.cgocable.net>,
Dali J <dali@cogeco.ca> wrote:
>I'm new at COBOL. And I'm confused writing a piece of code that does the
>following:(maximum the window for viewing) I am especially confused with
…[4 more quoted lines elided]…
>USE THE CM2002S FILE AND RECORD LAYOUT FROM THE PREVIOUS ASSIGNMENT.

Please do your own homework.

DD
```

#### ↳ Re: Code Question

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2002-11-08T17:50:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aqgti6$514$1@peabody.colorado.edu>`
- **References:** `<MMRy9.4778$L47.762264@read2.cgocable.net>`

```

On  8-Nov-2002, "Dali J" <dali@cogeco.ca> wrote:

> I'm new at COBOL. And I'm confused writing a piece of code that does the
> following:(maximum the window for viewing) I am especially confused with
> Control Breaks.

We don't have enough detail to determine where you need help.   Please include
the code you have written, the compiler you have used, and the results you have
achieved so far.

If you haven't started coding yet, code your INPUT-OUTPUT & WORKING-STORAGE. 
Then code enough to read all records and display them.  When you get done with
this, modify your code to print the output without control breaks.   When you
get done with this include the control breaks.  If you get stuck somewhere then
ask for help and show us the alternatives you have tried.   Start now, as lots
of us won't be on this forum during the weekend.

A control break is the term used to mean - when something changes, you must do
something, such as start printing a new page, or show totals for that person, or
something different.

IF DEPARTMENT-NUMBER = OLD-DEPARTMENT-NUMBER
     CONTINUE
ELSE
     PERFORM MINOR-CONTROL-BREAK
END-IF.
```

#### ↳ Re: Code Question

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-11-08T18:34:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<itTy9.1406$NB6.928015606@newssvr11.news.prodigy.com>`
- **References:** `<MMRy9.4778$L47.762264@read2.cgocable.net>`

```
There is an excellent example of how to code control breaks on
www.tek-tips.com

Go to that web site and search for the:
COBOL General Discussion Forum

Once you are in the COBOL General Discussion Forum, click on the "FAQs" tab
(Frequently Asked Questions).  Topic 1d is titled "How to code control
breaks."  I recommend that this is a good starting point for understanding
this basic programming concept.  (While you are in Tek-Tips, be sure to
register.  THEN, if you find the FAQ helpful, be sure to give it a good
rating; you will find the rating question at the bottom of the FAQ.)
```

#### ↳ Re: Code Question

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2002-11-08T12:29:18-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DCC1E9E.8060206@Sympatico.ca>`
- **References:** `<MMRy9.4778$L47.762264@read2.cgocable.net>`

```
Which part of the code confuses you?  If you post what you have written, 
then you
will probably get some help.  If you expect someone to do your homework 
for you,
then you are in the wrong newsgroup.

Donald

Dali J wrote:

>I'm new at COBOL. And I'm confused writing a piece of code that does the
>following:(maximum the window for viewing) I am especially confused with
…[186 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Code Question

- **From:** "Gordon McIntosh" <mcintg@ntlworld.com>
- **Date:** 2002-11-09T20:30:13
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Z7ez9.1369$2j7.82082@newsfep3-gui.server.ntli.net>`
- **References:** `<MMRy9.4778$L47.762264@read2.cgocable.net> <3DCC1E9E.8060206@Sympatico.ca>`

```
Can't help thinking that if you rely on others to show you how to do this
you will miss out on actually learning anything yourself.


"Donald Tees" <Donald_Tees@Sympatico.ca> wrote in message
news:3DCC1E9E.8060206@Sympatico.ca...
> Which part of the code confuses you?  If you post what you have written,
> then you
…[197 more quoted lines elided]…
>
```

#### ↳ Re: Code Question

- **From:** monkeycat <mensa@iname.com>
- **Date:** 2002-11-11T20:23:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3DD01216.1060200@iname.com>`
- **References:** `<MMRy9.4778$L47.762264@read2.cgocable.net>`

```

I note you included records but did not include the record format; 
However, I shall assume you know it (if not, you must obtain it).  I 
also assume the file is already in store, dept order (if not, include a 
sort).
My experience is that beginning programmers (and even many experienced 
programmers) get into trouble with control breaks by not following a 
simple rule: test for the control breaks immediately after reading the 
record - it should be done before doing anything with the current 
record.  If you don't do that, it's highly probable you will wind up 
with a program that's extremely difficult to debug.
The following outline will give you the basic structure of the program.
If you are just starting out, concentrate on getting the program 
structure right and hang onto that like grim death.  The details can 
then be attacked one by one without having to think of the details and 
the structure at the same time.
I've made no attempt to code basics of how to print a line, how to open 
files, etc.  You should have been trained in those details already; but 
if you are shaky in those areas, find somebody else's print program and 
study it.  Also don't forget to check your end of page line counter each 
time you print.

Good Luck!!

001-Main-routine.
	Perform 002-Housekeep-routine.
	Perform 003-Open-files-routine.
	Perform 005-Read-record-routine until EOF-switch = "E".
	Perform 007-Final-print-routine.
	Perform 004-Close-files-routine.
	Stop Run.
002-Housekeep-routine.
	Whatever.
	Exit.
003-Open-files-routine.
	Open input and output files (incl printer).
	Exit.
004-Close-files-routine.
	Close input and output files (incl printer).
	Exit.
005-Read-record-routine.
	Read the input file at end move "E" to EOF-switch.
		Check for read errors
	If EOF-switch not = "E" perform 006-Process-record.	
	Exit.
006-Process-record.
	If store#<>saved store# and not first-rec perform 008-Major.
	If dept#<>saved dept# and not first-rec perform 009-Minor.
	Add sales in record to Minor-Accum.	
	Save dept# and store# of this record.
	Perform 010-Print-deail-line.
	Exit.
007-Final-print-routine.
	Perform 008-Major.
	Perform 011-Final-total-routine.
	Exit.
008-Major.
	Perform 009-Minor-routine.
	Print major totals for the saved store#.
	Add Major-Accum to Final-Accum
	Zero Major-Accum.
	Exit.
009-Minor-routine.
	Print minor totals for the saved dept#.
	Add Minor-Accum to Major-Accum
	Zero Minor-Accum.
	Exit.
010-Print-detail-line.
	Print the detail line from the data in the current record.
	Exit
011-Final-total-routine.
	Print final totals.
	Exit.



Dali J wrote:
> I'm new at COBOL. And I'm confused writing a piece of code that does the
> following:(maximum the window for viewing) I am especially confused with
…[184 more quoted lines elided]…
>
```

#### ↳ Re: Code Question

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2002-12-23T04:38:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NtidnV_vF94BepujXTWcrg@comcast.com>`
- **References:** `<MMRy9.4778$L47.762264@read2.cgocable.net>`

```
In article <MMRy9.4778$L47.762264@read2.cgocable.net>, dali@cogeco.ca 
wrote:

>I'm new at COBOL. And I'm confused writing a piece of code that does the
>following:(maximum the window for viewing) I am especially confused with
>Control Breaks.

We're not here to do your homework for you, Dali.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
