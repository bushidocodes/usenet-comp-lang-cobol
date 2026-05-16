[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ANOTHER TOTAL-LINE QUESTION

_9 messages · 8 participants · 2000-12_

---

### ANOTHER TOTAL-LINE QUESTION

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-12-18T23:58:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001218185846.12040.00005458@ng-cj1.aol.com>`

```
i AM having quite a few problems here with my report.  I cannot get my total
line to print correct and I cannot get two of my columns to print the correct
information.  I have asked for help with this before and I majorly messed up my
program so I had to either fix a ton of problems or start fresh so i started
fresh.  I went back and re read the chapter but I must be missing something.  I
did find out one thing though about editing detal lines and not iventory
records;).  Please point me in the write direction with some explanation.

Deek

 IDENTIFICATION DIVISION.
 PROGRAM-ID. proj7.
 
*************************************************************************
* Purpose:  
* Class:    CIS160B - Structured Business Programming I.
* Author:   Derrick Pizur.
* Written:  09/18/00.
* Revised:  .
* Compiler: Fujitsu Cobol 4.0.
* Notes:    .
*************************************************************************

 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 SOURCE-COMPUTER. IBM-PC.
 OBJECT-COMPUTER. IBM-PC.

 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
     SELECT INVENTORY-FILE
 		ASSIGN TO "A:\COBOL\Proj7\PROJ7\Invntory.DAT"
		ORGANIZATION LINE SEQUENTIAL
		ACCESS	     SEQUENTIAL.
     SELECT PRINT-FILE
		ASSIGN TO "A:\COBOL\PROJ7\PROJ7\Report.txt"
          ORGANIZATION LINE SEQUENTIAL
		ACCESS	     SEQUENTIAL.
 DATA DIVISION.
 FILE SECTION.
 FD  INVENTORY-FILE
     RECORD CONTAINS 80 CHARACTERS.
 01 INVENTORY-RECORD.
	  05 IR-ITEM-NBR		PIC X(08).
	  05 IR-ITEM-DESCRIPTION	PIC X(30).
	  05 IR-QTY-ON-HAND             PIC S9(7)	 
                                  SIGN TRAILING SEPARATE.
    05 IR-QTY-TO-REORDER		PIC S9(3)
    				SIGN TRAILING SEPARATE.
    05 IR-REORDER-PT              PIC S9(3)
                                  SIGN TRAILING SEPARATE.
    05 IR-UNIT-COST		PIC S9(9)
                                  SIGN TRAILING SEPARATE.
    05 IR-UNIT-OF-MEASURE         PIC X(02).
	  05 IR-DOLLAR-VALUE		PIC S9(14).
*    05 FILLER			PIC X(06).
  FD PRINT-FILE.
  01 PRINT-RECORD			PIC X(80).  
 WORKING-STORAGE SECTION.

 01 SYSTEM-DATE-AND-TIME.
    05 SYSTEM-DATE.
	     
	     10 SYS-DATE-CCYY           PIC 9(4).
	     10 SYS-DATE-MM             PIC 9(2).
	     10 SYS-DATE-DD             PIC 9(2).
	  05 SYSTEM-TIME.
	     10 SYS-TIME-HOURS          PIC 9(2).
	     10 SYS-TIME-MINUTES        PIC 9(2).
	     10 SYS-TIME-SECONDS        PIC 9(2).
	     10 SYS-TIME-HUNDREDTHS     PIC 9(2).
	  05 FILLER			PIC X(05).
 01 HEAD-1.                   
	  05 H1-DATE.
	  	10 H1-MONTH-LIT		PIC X(3).
		10 FILLER	        PIC X .
		10 H1-DATE-DD		PIC 99.
          10 FILLER		PIC X .
		10 H1-DATE-CCYY		PIC 9(4).
		
	  05 FILLER 			PIC X(13) VALUE SPACES.
    05 FILLER			PIC X(40)
		VALUE "CIS160 Structured Business Programming".
    05 FILLER			PIC X(10) VALUE SPACES.
	  05 FILLER			PIC X(5)  VALUE "PAGE ".
	  05 H1-PAGE-NUM		PIC 9.
 01 HEAD-2.
	  05 H2-TIME.
		10 H2-DOW		PIC X(3).
		10 FILLER		PIC XX VALUE SPACE.
		10 H2-TIME-HOURS-LIT    PIC 9(2).
	 	10 FILLER		PIC X VALUE ":".
		10 H2-TIME-MINUTES	PIC 99.
		10 FILLER		PIC X VALUE ":".
		10 H2-TIME-SECONDS      PIC 99.
	  05 FILLER			PIC X(13) VALUE SPACES.
	  05 FILLER			PIC X(61)
		VALUE "List of Inventory Items to Reorder".
 01 TITLE-LINE-1.
    05 FILLER     		PIC X(40)  VALUE SPACES.
	  05 FILLER			PIC X(8)   VALUE 'Quantity'.
	  05 FILLER		   	PIC X(4)   VALUE SPACES.
	  05 FILLER  			PIC X(7)   VALUE SPACES.
    05 FILLER			PIC X(6)   VALUE SPACES.
	  05 FILLER			PIC X(8)   VALUE SPACES.
 01 TITLE-LINE-2.
    05 FILLER                     PIC X(12)  VALUE 'Item Nbr'.
	  05 FILLER			PIC X(2)   VALUE SPACES.
	  05 FILLER			PIC X(16)  VALUE 
						 'Item Description'.
	  05 FILLER    			PIC X(10) VALUE SPACES.
	  05 FILLER			PIC X(7)  VALUE 'On Hand'.
	  05 FILLER  			PIC X(5)  VALUE SPACES.
	  05 FILLER			PIC X(9)  VALUE 'UNIT COST'.
    05 FILLER			PIC X(7)  VALUE SPACES.
	  05 FILLER			PIC X(12) VALUE 'DOLLAR VALUE'.
 01 DETAIL-LINE.
    05 DL-ITEM-NUM	        PIC  X(08)        VALUE SPACES.
    05 FILLER   		        PIC  X(01)        VALUE SPACES.
    05 DL-ITEM-DESC		PIC  X(30)        VALUE SPACES.
	  05 FILLER			PIC  X(1)         VALUE SPACES. 
	  05 DL-QTY-ON-HAND    	  	PIC  Z,ZZZ,ZZ9-   VALUE ZEROS.
    05 FILLER			PIC  X(1)         VALUE SPACES.
    05 DL-UNIT-COST		PIC  ZZ,ZZ9.9999- VALUE ZEROS.
    05 FILLER			PIC  X(1)         VALUE SPACES.
*    05 DL-REORDER-PT		PIC  Z(6)9-       VALUE ZEROS.
    05 FILLER			PIC  X(1)         VALUE SPACES.
    05 DL-DOLLAR-VALUE		PIC  ZZZ,ZZZ,ZZ9.99- VALUE ZEROS.
*    05 DL-QTY-TO-REORDER		PIC  Z(6)9-       VALUE ZEROS.
	  
	  05 DL-DOLLAR-VALUE		PIC  ZZZ,ZZZ,ZZ9.99- VALUE ZEROS.
 01 WS-ACCUMULATORS.
    05 WS-QTY-TO-REORDER-TOT      PIC  S9(7)   VALUE ZEROS.
    05 WS-QTY-ON-HAND-TOT		PIC  S9(7)   VALUE ZEROS.
    05 WS-REORDER-PT-TOT 		PIC  S9(7)   VALUE ZEROS.
	  05 WS-DOLLAR-VALUE-TOT	PIC  S9(7)   VALUE ZEROS.
 01 TOTAL-LINE.
    05 FILLER 			PIC  X(10)   VALUE SPACES.
    05 FILLER			PIC  X(5)    VALUE 'Total'.
	  05 FILLER			PIC  X(1)    VALUE SPACES.
	  05 FILLER			PIC  X(10)   VALUE 'Quantities'.
    05 FILLER			PIC  X(15)   VALUE SPACES.
    05 TL-QTY-ON-HAND-TOT	        PIC  Z,ZZZ,ZZ9-.
    05 FILLER                     PIC  X(4)    VALUE SPACES.
    05 TL-UNIT-COST-TOT           PIC  Z(6)9-.
    05 FILLER                     PIC  X(7)    VALUE SPACES.
    05 TL-DOLLAR-VALUE-TOT        PIC  Z(6)9-.

* 01 WS-QTY-TO-REORDER               PIC  S9(7).
 01 WS-DOW 			PIC  9 	     VALUE ZERO.
 01 WS-REORDER-PT			PIC  9(6).
 01 WS-QTY-ON-HAND		PIC  9(6).
 01 EOF-FLAG		        PIC  X(01)   VALUE SPACE.  
 
 
 01 WS-QTY-TO-REORDER	        PIC S9(7)  
					SIGN TRAILING SEPARATE.
 01 WS-PAGE-CNT			PIC 9(3) VALUE ZERO.
 01 WS-LINE-CNT			PIC 9(3) VALUE 56.
 01 WS-PAGE-SIZE			PIC 9(3) VALUE 54.
 PROCEDURE DIVISION.
 MAINLINE.
     PERFORM 100-INITIALIZATION
     
     PERFORM 200-PROCESSING

     PERFORM 300-TERMINATION

	   STOP RUN.
 100-INITIALIZATION.
     OPEN INPUT INVENTORY-FILE
		OUTPUT PRINT-FILE.
 110-WRITE-HEADINGS.
     ADD 1 TO WS-PAGE-CNT
	   MOVE WS-PAGE-CNT TO H1-PAGE-NUM
     MOVE FUNCTION CURRENT-DATE TO SYSTEM-DATE-AND-TIME

	   EVALUATE SYS-DATE-MM
		WHEN 01 MOVE "JAN" TO H1-MONTH-LIT
		WHEN 02 MOVE "FEB" TO H1-MONTH-LIT
		WHEN 03 MOVE "MAR" TO H1-MONTH-LIT
		WHEN 04 MOVE "APR" TO H1-MONTH-LIT
		WHEN 05 MOVE "MAY" TO H1-MONTH-LIT
		WHEN 06 MOVE "JUN" TO H1-MONTH-LIT
		WHEN 07 MOVE "JUL" TO H1-MONTH-LIT
		WHEN 08 MOVE "AUG" TO H1-MONTH-LIT
		WHEN 09 MOVE "SEP" TO H1-MONTH-LIT
		WHEN 10 MOVE "OCT" TO H1-MONTH-LIT
		WHEN 11 MOVE "NOV" TO H1-MONTH-LIT
		WHEN 12 MOVE "DEC" TO H1-MONTH-LIT
	   END-EVALUATE.
	   
	   EVALUATE SYS-TIME-HOURS
		WHEN 00 MOVE "12" TO  H2-TIME-HOURS-LIT
		WHEN 01 MOVE "01" TO  H2-TIME-HOURS-LIT
		WHEN 02 MOVE "02" TO  H2-TIME-HOURS-LIT
		WHEN 03 MOVE "03" TO  H2-TIME-HOURS-LIT
		WHEN 04 MOVE "04" TO  H2-TIME-HOURS-LIT
 		WHEN 05 MOVE "05" TO  H2-TIME-HOURS-LIT
		WHEN 06 MOVE "06" TO  H2-TIME-HOURS-LIT
		WHEN 07 MOVE "07" TO  H2-TIME-HOURS-LIT
          WHEN 08 MOVE "08" TO  H2-TIME-HOURS-LIT
		WHEN 09 MOVE "09" TO  H2-TIME-HOURS-LIT
          WHEN 10 MOVE "10" TO  H2-TIME-HOURS-LIT
 		WHEN 11 MOVE "11" TO  H2-TIME-HOURS-LIT
		WHEN 12 MOVE "12" TO  H2-TIME-HOURS-LIT
		WHEN 13 MOVE "01" TO  H2-TIME-HOURS-LIT
		WHEN 14 MOVE "02" TO  H2-TIME-HOURS-LIT
		WHEN 15 MOVE "03" TO  H2-TIME-HOURS-LIT
		WHEN 16 MOVE "04" TO  H2-TIME-HOURS-LIT
		WHEN 17 MOVE "05" TO  H2-TIME-HOURS-LIT
		WHEN 18 MOVE "06" TO  H2-TIME-HOURS-LIT
		WHEN 19 MOVE "07" TO  H2-TIME-HOURS-LIT
		WHEN 20 MOVE "08" TO  H2-TIME-HOURS-LIT
 		WHEN 21 MOVE "09" TO  H2-TIME-HOURS-LIT
		WHEN 22 MOVE "10" TO  H2-TIME-HOURS-LIT
		WHEN 23 MOVE "11" TO  H2-TIME-HOURS-LIT
		WHEN 24 MOVE "12" TO  H2-TIME-HOURS-LIT
	   END-EVALUATE.
	   ACCEPT WS-DOW FROM DAY-OF-WEEK 
	       EVALUATE WS-DOW 
		    WHEN 1 MOVE "MON" TO H2-DOW
		    WHEN 2 MOVE "TUE" TO H2-DOW
		    WHEN 3 MOVE "WED" TO H2-DOW
		    WHEN 4 MOVE "THU" TO H2-DOW
		    WHEN 5 MOVE "FRI" TO H2-DOW
		    WHEN 6 MOVE "SAT" TO H2-DOW
		    WHEN 7 MOVE "SUN" TO H2-DOW
	       END-EVALUATE.
		MOVE SYS-TIME-MINUTES TO H2-TIME-MINUTES.
          MOVE SYS-TIME-SECONDS TO H2-TIME-SECONDS.
		WRITE PRINT-RECORD    FROM HEAD-2 AFTER PAGE.
		MOVE SYS-DATE-CCYY    TO H1-DATE-CCYY.
 		MOVE SYS-DATE-DD      TO H1-DATE-DD.
          WRITE PRINT-RECORD    FROM HEAD-1 AFTER 1.
	   MOVE SPACES                TO PRINT-RECORD
		WRITE PRINT-RECORD    AFTER 1.
	   MOVE TITLE-LINE-1          TO PRINT-RECORD
		WRITE PRINT-RECORD    AFTER ADVANCING 1.
	   MOVE TITLE-LINE-2          TO PRINT-RECORD
		WRITE PRINT-RECORD    AFTER ADVANCING 1.	 	
     MOVE SPACES                TO PRINT-RECORD
		WRITE PRINT-RECORD    AFTER 1.
     MOVE 6 TO WS-LINE-CNT.
 200-PROCESSING.
     PERFORM UNTIL EOF-FLAG = 'Y'
         READ INVENTORY-FILE
	       AT END
		   MOVE 'Y' TO EOF-FLAG
         NOT AT END   
                PERFORM 205-PROCESS-A-RECORD 	       
	       END-READ 
	   END-PERFORM.
 205-PROCESS-A-RECORD.
     IF WS-LINE-CNT > WS-PAGE-SIZE
		PERFORM 110-WRITE-HEADINGS
	   END-IF.
	   COMPUTE IR-DOLLAR-VALUE ROUNDED = IR-QTY-ON-HAND * IR-UNIT-COST
	   END-COMPUTE.
     PERFORM 210-DISPLAY-A-LINE.
     ADD 1 TO WS-LINE-CNT.
  
 210-DISPLAY-A-LINE.     
 		 MOVE IR-ITEM-NBR 
		     TO DL-ITEM-NUM
	         MOVE IR-ITEM-DESCRIPTION
 		     TO DL-ITEM-DESC
	         MOVE IR-QTY-ON-HAND
		     TO DL-QTY-ON-HAND
*	         MOVE IR-REORDER-PT
*		     TO DL-REORDER-PT
*	         MOVE WS-QTY-TO-REORDER
*		     TO DL-QTY-TO-REORDER
		 MOVE IR-UNIT-COST TO
			DL-UNIT-COST.
*		 MOVE IR-DOLLAR-VALUE TO
*			DL-DOLLAR-VALUE
       MOVE DETAIL-LINE    TO PRINT-RECORD
		 WRITE PRINT-RECORD AFTER 1.
	   ADD IR-QTY-ON-HAND    TO WS-QTY-ON-HAND-TOT.
*     ADD IR-REORDER-PT     TO WS-REORDER-PT-TOT.
*     COMPUTE WS-QTY-TO-REORDER-TOT = WS-REORDER-PT-TOT - WS-QTY-ON-HAND-TOT
*     END-COMPUTE.
	   ADD 1 TO WS-LINE-CNT. 
 300-TERMINATION.
     MOVE SPACES TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER 1.
	   MOVE WS-QTY-ON-HAND-TOT    TO TL-QTY-ON-HAND-TOT.
	   MOVE WS-DOLLAR-VALUE-TOT   TO TL-DOLLAR-VALUE-TOT.
*	   MOVE WS-REORDER-PT-TOT     TO TL-REORDER-PT-TOT.
*	   MOVE WS-QTY-TO-REORDER-TOT TO TL-QTY-TO-REORDER-TOT.
     MOVE TOTAL-LINE TO PRINT-RECORD.
       WRITE PRINT-RECORD AFTER ADVANCING 1.
     CLOSE INVENTORY-FILE
           PRINT-FILE
	   .
```

#### ↳ Re: ANOTHER TOTAL-LINE QUESTION

- **From:** mike__c@my-deja.com
- **Date:** 2000-12-19T09:33:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91na0f$egd$1@nnrp1.deja.com>`
- **References:** `<20001218185846.12040.00005458@ng-cj1.aol.com>`

```
In article <20001218185846.12040.00005458@ng-cj1.aol.com>,
  deek40@aol.com (Deek40) wrote:
> i AM having quite a few problems here with my report.  I cannot get my
total
> line to print correct and I cannot get two of my columns to print the
correct
> information.  I have asked for help with this before and I majorly
messed up my
> program so I had to either fix a ton of problems or start fresh so i
started
> fresh.  I went back and re read the chapter but I must be missing
something.  I
> did find out one thing though about editing detal lines and not
iventory
> records;).  Please point me in the write direction with some
explanation.
>
> Deek

You haven't said which fields you are having trouble with, but as
someone suggested in a reply to your original post, put lots of DISPLAYs
in your program to see what values your problem fields have.

Put the DISPLAYs in whenever a field you are having trouble with is
being moved or changing to verify that it's happening correctly - you
what to trace the journey of a field from the input file through working
storage to the output file.

>
> 	   ACCEPT WS-DOW FROM DAY-OF-WEEK
…[8 more quoted lines elided]…
> 	       END-EVALUATE.

Don't know if you are having trouble with any of your EVALUATE
statements, but it's always advisable to code the WHEN OTHER bit even if
you think it'll never happen, e.g. WHEN OTHER DISPLAY "WS-DOW not
between 1 and 7 " WS-DOW


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: ANOTHER TOTAL-LINE QUESTION

- **From:** lcccpiasabird@my-deja.com
- **Date:** 2000-12-19T16:43:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91o37g$2qr$1@nnrp1.deja.com>`
- **References:** `<20001218185846.12040.00005458@ng-cj1.aol.com>`

```



  In article <20001218185846.12040.00005458@ng-cj1.aol.com>,
  deek40@aol.com (Deek40) wrote:

When you round numbers you can get bad results.
I noticed you were rounding.
There are much easier ways to handle the time.  like subtracting 12
based on an if condition!!!!

You can also put the months in one field and then redefining the field
to occur 12 times and then subscripting them out.  I hope your teacher
is teaching you how to use subscripting, if not don't mess with that
part.

I suggest you read your book.  Totals are easy.  You compute the
result, move it to the total and then move it to the total counter.

Important!
If you are computing a rounded amount you need to compute it unrounded,
move it to the total field and then compute it rounded and move it to
the printline, so you don't lose anything in the rounding process. Then
you can round it at the bottom if you want.  The rounded values may not
add up so you can not check it that way.  I suggest making the report
without rounding and then you can check it and then add in the rounding
as an extra step.  When facing a complex problem slve it one step at a
time use an extra field that you can comment out in the printline to
test your results.


> i AM having quite a few problems here with my report.  I cannot get
my total
> line to print correct and I cannot get two of my columns to print the
correct
> information.  I have asked for help with this before and I majorly
messed up my
> program so I had to either fix a ton of problems or start fresh so i
started
> fresh.  I went back and re read the chapter but I must be missing
something.  I
> did find out one thing though about editing detal lines and not
iventory
> records;).  Please point me in the write direction with some
explanation.
>
> Deek
…[4 more quoted lines elided]…
>
************************************************************************
*
> * Purpose:
> * Class:    CIS160B - Structured Business Programming I.
…[5 more quoted lines elided]…
>
************************************************************************
*
>
>  ENVIRONMENT DIVISION.
…[103 more quoted lines elided]…
>     05 DL-DOLLAR-VALUE		PIC  ZZZ,ZZZ,ZZ9.99- VALUE
ZEROS.
> *    05 DL-QTY-TO-REORDER		PIC  Z(6)9-       VALUE ZEROS.
>
> 	  05 DL-DOLLAR-VALUE		PIC  ZZZ,ZZZ,ZZ9.99- VALUE
ZEROS.
>  01 WS-ACCUMULATORS.
>     05 WS-QTY-TO-REORDER-TOT      PIC  S9(7)   VALUE ZEROS.
…[123 more quoted lines elided]…
> 	   COMPUTE IR-DOLLAR-VALUE ROUNDED = IR-QTY-ON-HAND * IR-UNIT-
COST
> 	   END-COMPUTE.
>      PERFORM 210-DISPLAY-A-LINE.
…[21 more quoted lines elided]…
> *     COMPUTE WS-QTY-TO-REORDER-TOT = WS-REORDER-PT-TOT - WS-QTY-ON-
HAND-TOT
> *     END-COMPUTE.
> 	   ADD 1 TO WS-LINE-CNT.
…[13 more quoted lines elided]…
>


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: ANOTHER TOTAL-LINE QUESTION

- **From:** rjones1005@aol.com (RJones1005)
- **Date:** 2000-12-23T04:50:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001222235018.03963.00006061@ng-ct1.aol.com>`
- **References:** `<20001218185846.12040.00005458@ng-cj1.aol.com>`

```
>205-PROCESS-A-RECORD.
>     IF WS-LINE-CNT > WS-PAGE-SIZE
…[11 more quoted lines elided]…
> 		     TO D


Deek, don't mix scope terminatores (END-IF, END-<whatever>) and periods.  You
will eventually run into trouble.  I'm not saying this is the problem with your
program however.  Either use periods or use scope terminators, but not both.
```

##### ↳ ↳ Re: ANOTHER TOTAL-LINE QUESTION

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-12-23T06:42:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001223014246.12056.00003636@ng-mn1.aol.com>`
- **References:** `<20001222235018.03963.00006061@ng-ct1.aol.com>`

```
ok, the strangest thing i have learned with programming so far is that everyone
has a different opinion or tells me a different thing to do or not to do.
```

###### ↳ ↳ ↳ Re: ANOTHER TOTAL-LINE QUESTION

- **From:** "Willem Clements" <willem@horizontes-informatica.com>
- **Date:** 2000-12-23T11:22:25+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jvyyrzubevmbagrfvasbezngvpnpbz.g6145d0.pminews@news.wanadoo.es>`
- **References:** `<20001222235018.03963.00006061@ng-ct1.aol.com> <20001223014246.12056.00003636@ng-mn1.aol.com>`

```
On 23 Dec 2000 06:42:46 GMT, Deek40 wrote:

>ok, the strangest thing i have learned with programming so far is that everyone
>has a different opinion or tells me a different thing to do or not to do.


Yes, but no.

If you read all the opinions, you'll find that they all boil down to the
same, Think carefully before doing anything. Adopt a standard way of doing
things and be consequent. Also make things easy for the people who have to
modify your program (it might be you).

Willem Clements
Brainbench MVP for COBOL II
http://www.brainbench.com
```

###### ↳ ↳ ↳ Re: ANOTHER TOTAL-LINE QUESTION

_(reply depth: 4)_

- **From:** "Russell Styles" <RWSTYLES01@CS.COM>
- **Date:** 2000-12-23T22:46:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<923t25$pq8$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<20001222235018.03963.00006061@ng-ct1.aol.com> <20001223014246.12056.00003636@ng-mn1.aol.com> <jvyyrzubevmbagrfvasbezngvpnpbz.g6145d0.pminews@news.wanadoo.es>`

```

"Willem Clements" <willem@horizontes-informatica.com> wrote in
message
news:jvyyrzubevmbagrfvasbezngvpnpbz.g6145d0.pminews@news.wanadoo.
es...
> On 23 Dec 2000 06:42:46 GMT, Deek40 wrote:
>
> >ok, the strangest thing i have learned with programming so far
is that everyone
> >has a different opinion or tells me a different thing to do or
not to do.
>
>
> Yes, but no.
>
> If you read all the opinions, you'll find that they all boil
down to the
> same, Think carefully before doing anything. Adopt a standard
way of doing
> things and be consequent. Also make things easy for the people
who have to
> modify your program (it might be you).
>
…[5 more quoted lines elided]…
>
    Just because 2 people have the exact opposite opinion does
not mean that
they both cannot be correct (sometimes).  Ie, avoid periods or
use a period everywhere
humanly possible.  See above.

    Before someone complains, yes, some things are wrong (Ie
alters).
```

###### ↳ ↳ ↳ Re: ANOTHER TOTAL-LINE QUESTION

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-23T15:35:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zD316.6393$Sl.326911@iad-read.news.verio.net>`
- **References:** `<20001222235018.03963.00006061@ng-ct1.aol.com> <20001223014246.12056.00003636@ng-mn1.aol.com>`

```
In article <20001223014246.12056.00003636@ng-mn1.aol.com>,
Deek40 <deek40@aol.com> wrote:
>ok, the strangest thing i have learned with programming so far is that everyone
>has a different opinion or tells me a different thing to do or not to do.

Hmmmmmm... I'm not sure I agree with that; permit me to present you with
an alternate view...

(joking aside, old boy, what was the name of Knuth's work which might
explain your confusion?)

DD
```

###### ↳ ↳ ↳ Re: ANOTHER TOTAL-LINE QUESTION

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-12-27T07:04:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A49F6F3.DF839FFC@brazee.net>`
- **References:** `<20001222235018.03963.00006061@ng-ct1.aol.com> <20001223014246.12056.00003636@ng-mn1.aol.com>`

```


Deek40 wrote:

> ok, the strangest thing i have learned with programming so far is that everyone
> has a different opinion or tells me a different thing to do or not to do.

There is no single right method - otherwise we could automate the process.  But
figure out where we are all coming from, and remember even contradictory
suggestions for when you are working with real world problems.  If you know why we
make certain suggestions, you can use them, or variations of them to help you (and
use your employers standards as well)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
