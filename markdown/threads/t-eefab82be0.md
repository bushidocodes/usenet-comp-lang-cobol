[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# quick help question

_11 messages · 5 participants · 2001-02_

---

### quick help question

- **From:** deek40@aol.com (Deek40)
- **Date:** 2001-02-19T16:07:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010219110735.02143.00000021@ng-cm1.aol.com>`

```
Hello once again, I am a student and trying to learn cobol, when i compile my
program i got like 50 errors ok np i fixed all the ones i could but there are a
few i cant get rid of.  Please help because i have put so much time into this
and it would kill me to lose 2 out of the 10 points for these minor errors. 
Thanks for your time.

here are the errors:
1)user word 'Detail  Desc' is multidefined
here is the code it points to:
PERFORM VARYING A-SUB FROM 1 BY 1
		UNTIL A-SUB > 3
	#######	MOVE  DETAIL-DESC (A-SUB)  TO DESC-PR########
		MOVE  PROD-UNITS (A-SUB)   TO UNITS-PR
		MOVE  PROD-REVENUE (A-SUB) TO REVENUE-PR
		WRITE PRINT-RECORD FROM DETAIL-LINE AFTER 1
     END-PERFORM.
2) user word 'summary-line' is multi defined
here is the code it points to:
 PERFORM VARYING S-SUB FROM 1 BY 1
          UNTIL S-SUB > 6
         MOVE PRODUCT-LINE (S-SUB) TO SUM-PROD-LINE         
           PERFORM VARYING A-SUB FROM 1 BY 1
             UNTIL A-SUB > 3
                MOVE LINE-REVENUE (S-SUB  A-SUB) TO SUM-REV-PR (S-SUB)   
           END-PERFORM
##### WRITE PRINT-RECORD FROM SUMMARY-LINE AFTER 1####### 
      END-PERFORM.
--------------------------------------------------------------------------
--------------------
here is my full code please help me because i have put countless hours into
this program and i need the 2 points that i get for no errors in compilation.  

 IDENTIFICATION DIVISION.
 PROGRAM-ID. projone.
***********************************
*PURPOSE: SOFTWARE COST ANALYSIS  *
*AUTHOR: DERRICK PIZUR            *
*WRITTEN: 02/02/01.               *
*REVISED:.                        *
*COMPILER: FUJITSU COBOL 4.0      *
*NOTES:.                          *
***********************************
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 SOURCE-COMPUTER. IBM-PC.
 OBJECT-COMPUTER. IBM-PC.
 
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
	   SELECT SOFTWARE-FILE
		ASSIGN TO "A:\PROJ11-6\SOFT.DAT"
		ORGANIZATION LINE SEQUENTIAL.
	   SELECT PRINT-FILE
		ASSIGN TO "A:\PROJ11-6\REPORT.TXT"
		ORGANIZATION LINE SEQUENTIAL.
 DATA DIVISION.
 FILE SECTION.
 FD SOFTWARE-FILE
	   RECORD CONTAINS 80 CHARACTERS.
 01 SOFTWARE-RECORD.
    05 SOFT-PROGRAM-INFO.
	    10 SOFT-PRODUCT-LINE         PIC X.
      10 SOFT-PRODUCT-NO           PIC 9(4).
      10 SOFT-PROGRAM-NAME         PIC X(18).
    05 SOFT-VARIABLE-COSTS.
	    10 SOFT-PREP-COSTS.
		15 SOFT-LOADING-PER-DISK PIC 9V99.
    	15 SOFT-NO-DISKS-USED    PIC 99.
      10 SOFT-MANUAL-PRINTING      PIC 99V99.
      10 SOFT-SHIPPING-N-HANDLING  PIC 99V99.
    05 SOFT-SELL-PRICE		 PIC 999V99.
    05 SOFT-FIXED-COST       	 PIC 9(5).
 FD PRINT-FILE.
 01 PRINT-RECORD PIC X(80).
 WORKING-STORAGE SECTION.
 01 subscripts.
     05 A-SUB   PIC 99  VALUE ZERO.
     05 S-SUB PIC 99  VALUE ZERO.
 01 TITLE-LINE-1.
     05 FILLER      PIC X(15) VALUE SPACES.
	   05 FILLER      PIC X(5)  VALUE "Nexus".
     05 FILLER	  PIC X(1)  VALUE SPACE.
     05 FILLER	  PIC X(8)  VALUE "Software".
     05 FILLER	  PIC X(1)  VALUE SPACE.
     05 FILLER      PIC X(4)  VALUE "INC.".
 01 TITLE-LINE-2.
     05 FILLER      PIC X(15) VALUE SPACES.
     05 FILLER      PIC X(13) VALUE "Product Cost ".
     05 FILLER      PIC X(9)  VALUE "Analysis ".
     05 FILLER	  PIC X(6)  VALUE "as of "  .
     05 FILLER	  PIC 9(2)  VALUE 02.
     05 FILLER      PIC X(1)  VALUE "/".
     05 FILLER      PIC 9(2)  VALUE 14.
     05 FILLER      PIC X(1)  VALUE "/".
     05 FILLER      PIC 9(2)  VALUE 01.
 01 TITLE-LINE-3.
     05 FILLER      PIC X(9)  VALUE "based on ".
     05 FILLER	  PIC X(6)  VALUE "Total ".
     05 FILLER	  PIC X(6)  VALUE "Fixed ".
     05 FILLER	  PIC x(6)  VALUE "Costs:".
     05 TOT-FIXED-COSTS PIC $ZZ,ZZ9.
 01 TITLE-LINE-SUM-2.
     05 FILLER      PIC X(21) VALUE "Product Cost Analysis".
 01 TITLE-LINE-SUM-3.
     05 FILLER	  PIC X(36) VALUE "Summary Report by Product Line as of".
     
 01 TITLE-LINE-SUM-4.
     05 FILLER     PIC X(7) VALUE "Product".
     05 FILLER     PIC X(2) VALUE SPACES.
     05 FILLER     PIC X(9) VALUE "Breakeven".
     05 FILLER	 PIC X(4) VALUE SPACES.
     05 FILLER     PIC X(7) VALUE "Profit:".
     05 FILLER	 PIC X(6) VALUE SPACES.
     05 FILLER	 PIC X(5) VALUE "Price".
 01 TITLE-LINE-SUM-5.
     05 FILLER     PIC X(2) VALUE SPACES.
     05 FILLER	 PIC X(4) VALUE "Line".
     05 FILLER	 PIC X(26) VALUE SPACES.
     05 FILLER	 PIC X(8) VALUE "Decline:".
        
 01 ANALYSIS-TABLE.
     05 PRODUCT-INFORMATION OCCURS 3 TIMES.
        10 PROD-UNITS   PIC 9(5).
        10 PROD-REVENUE PIC 9(8).
 01 SUMMARY-TABLE.
      05 SUMMARY-LINE OCCURS 6 TIMES.
        10  PRODUCT-LINE          PIC X .
        10  PRODUCT-INFO                OCCURS 3 TIMES. 
        	    15  LINE-REVENUE          PIC 9(5).

 01 DETAIL-TABLE.
      05  FILLER          PIC X(20) VALUE 'Breakeven'.
	    05  FILLER          PIC X(20) VALUE 'Profit $50,000'.
      05  FILLER          PIC X(20) VALUE 'Price Decline 25%'.
* I READ AHREAD IN THE TEXT TO THE NEXT CHAPTER AND USED
* TEACH YOURSELF COBOL IN 21 DAYS AS REFERENCE FOR THE REDEFINES 
* USEAGE.
 01  FILLER REDEFINES DETAIL-TABLE.
	    05  DETAIL-DESC PIC X(20) OCCURS 3 TIMES.
 
 01 WS-ACCUMULATORS.
     05 WS-VARIABLE-COSTS     PIC 9(5) VALUE ZERO.
     05 WS-PROFIT-PER-SALE    PIC 9(8) VALUE ZERO.
     05 WS-REVENUE	    PIC 9(8) VALUE ZERO.
	   05 WS-UNITS     	    PIC 9(5) VALUE ZERO.
     05  WS-SUM-TOTALS OCCURS 3 TIMES.
          10  WS-TOTAL             PIC 9(6).
     05 WS-DECLINE	    PIC 9(5) VALUE ZERO.
 01 DETAIL-LINE.
    05  DETAIL-DESC           PIC X(20).
    05  UNITS-PR              PIC ZZZ9.
    05  REVENUE-PR            PIC ZZ,ZZZ,ZZ9.
* CHANGE PICS LENGTH
 01  SUMMARY-LINE.
      05  SUM-PROD-LINE          PIC X.
      05  SUM-REVENUE OCCURS 3 TIMES.
            10  FILLER                   PIC XXX.
             10  SUM-REV-PR        PIC $$$$,$$9.
 01 DETAIL-LINES.
   05 PRODUCT-DL. 
      10 FILLER	              PIC X(13) VALUE "Product Line:".
      10 FILLER 	              PIC X(1)  VALUE SPACE.
      10 DL-SOFT-PRODUCT-LINE   PIC X     VALUE SPACE.
   05 PROGRAM-NAME-DL.
      10 FILLER		      PIC X(14) VALUE "Product Name: ". 
      10 DL-SOFT-PROGRAM-NAME   PIC X(18) VALUE SPACES.
   05 SELL-PRICE-DL.
      10 FILLER     	      PIC X(12) VALUE "Sell Price: ".
      10 DL-SOFT-SELL-PRICE     PIC $$$,$$9.99.
      10 FILLER                 PIC X(21) VALUE "Total Variable Cost: ". 
      10 DL-SOFT-VARIABLE-COST  PIC ZZ9.99.
 PROCEDURE DIVISION.
 MAINLINE.
 	   PERFORM 100-INITIALIZATION.
     PERFORM 200-MAIN-PROCESS 
     PERFORM 600-PRINT-DETAIL-SUM.
     CLOSE SOFTWARE-FILE.
     CLOSE PRINT-FILE.   	
	   	 STOP RUN.
 100-INITIALIZATION.
* INSERT DATE LOGIC
     OPEN INPUT SOFTWARE-FILE
          OUTPUT PRINT-FILE.

     
     PERFORM VARYING S-SUB FROM 1 BY 1
          UNTIL S-SUB > 6
         MOVE SPACES TO PRODUCT-LINE (S-SUB)
         PERFORM VARYING A-SUB FROM 1 BY 1
            UNTIL A-SUB > 3
                 MOVE 0 TO WS-TOTAL (A-SUB)        
         END-PERFORM
     END-PERFORM.



	   PERFORM 400-CLEAR-ANALYSIS.
     READ SOFTWARE-FILE. 
     PERFORM 300-LINE-BREAK.
 200-MAIN-PROCESS.
      
      IF SOFT-PRODUCT-LINE NOT = PRODUCT-LINE (S-SUB)
			PERFORM 300-LINE-BREAK
	   	END-IF.

	    MOVE 0 TO A-SUB.

      PERFORM 201-VARIABLE-COST-CALC.
      PERFORM 202-BREAKEVEN-CALC.
 	    PERFORM 203-REVENUE-CALC.
      PERFORM 204-MOVE-TO-TABLES.

      PERFORM 205-PROFIT-UNITS.
      PERFORM 203-REVENUE-CALC.
      PERFORM 204-MOVE-TO-TABLES.

      PERFORM 206-DECLINE-CALC.
      PERFORM 203-REVENUE-CALC.
      PERFORM 204-MOVE-TO-TABLES.

      PERFORM 500-PRINT-DETAIL.
      

 201-VARIABLE-COST-CALC.
     COMPUTE WS-VARIABLE-COSTS = ((SOFT-LOADING-PER-DISK + 1) * 
             SOFT-NO-DISKS-USED) + SOFT-MANUAL-PRINTING +
		   SOFT-SHIPPING-N-HANDLING
     END-COMPUTE.

 202-BREAKEVEN-CALC.
     COMPUTE WS-UNITS = (SOFT-SELL-PRICE - 
    	   WS-VARIABLE-COSTS) / SOFT-FIXED-COST
     END-COMPUTE.

 203-REVENUE-CALC.
     COMPUTE WS-REVENUE = (WS-UNITS * 
             SOFT-SELL-PRICE)
     END-COMPUTE.
     
 204-MOVE-TO-TABLES.
     ADD 1 TO A-SUB.
     MOVE WS-UNITS TO PROD-UNITS (A-SUB).
     MOVE WS-REVENUE TO PROD-REVENUE (A-SUB).
	   ADD WS-REVENUE TO LINE-REVENUE (S-SUB A-SUB).
     ADD WS-REVENUE TO WS-TOTAL (A-SUB).
 205-PROFIT-UNITS.
     COMPUTE WS-UNITS = (50000 + SOFT-FIXED-COST) /
	     (SOFT-SELL-PRICE - WS-VARIABLE-COSTS)
	   END-COMPUTE.

 206-DECLINE-CALC.
     COMPUTE WS-DECLINE = (SOFT-SELL-PRICE * .75)
	   END-COMPUTE.

 300-LINE-BREAK.
     ADD 1 TO S-SUB.
*     MOVE SOFT-PRODUCT-LINE TO (S-SUB).

 400-CLEAR-ANALYSIS.
	   PERFORM VARYING A-SUB FROM 1 BY 1
     	UNTIL A-SUB > 3
	 	   MOVE 0 TO PROD-UNITS (A-SUB)
		   MOVE 0 TO PROD-REVENUE (A-SUB)
     END-PERFORM.

 500-PRINT-DETAIL.
     MOVE SOFT-FIXED-COST  TO TOT-FIXED-COSTS.
     MOVE SOFT-PRODUCT-LINE TO DL-SOFT-PRODUCT-LINE.
     MOVE SOFT-PROGRAM-NAME TO DL-SOFT-PROGRAM-NAME.
     MOVE SOFT-SELL-PRICE   TO DL-SOFT-SELL-PRICE.
     MOVE WS-VARIABLE-COSTS TO DL-SOFT-VARIABLE-COST.
     WRITE PRINT-RECORD FROM TITLE-LINE-1 AFTER PAGE.
	   WRITE PRINT-RECORD FROM TITLE-LINE-2 AFTER 1.
     WRITE PRINT-RECORD FROM TITLE-LINE-3 AFTER 1.
     WRITE PRINT-RECORD FROM TOT-FIXED-COSTS AFTER 1.
     WRITE PRINT-RECORD FROM DL-SOFT-PRODUCT-LINE AFTER 1.
     WRITE PRINT-RECORD FROM DL-SOFT-PROGRAM-NAME AFTER 1.
     WRITE PRINT-RECORD FROM DL-SOFT-SELL-PRICE  AFTER 1.
     WRITE PRINT-RECORD FROM DL-SOFT-VARIABLE-COST AFTER 1.
     PERFORM VARYING A-SUB FROM 1 BY 1
		UNTIL A-SUB > 3
		MOVE  DETAIL-DESC (A-SUB)  TO DESC-PR
		MOVE  PROD-UNITS (A-SUB)   TO UNITS-PR
		MOVE  PROD-REVENUE (A-SUB) TO REVENUE-PR
		WRITE PRINT-RECORD FROM DETAIL-LINE AFTER 1
     END-PERFORM.
     PERFORM 400-CLEAR-ANALYSIS.
 600-PRINT-DETAIL-SUM.
     WRITE PRINT-RECORD FROM TITLE-LINE-1     AFTER PAGE.
     WRITE PRINT-RECORD FROM TITLE-LINE-SUM-2 AFTER 1. 
     WRITE PRINT-RECORD FROM TITLE-LINE-SUM-3 AFTER 1.
     WRITE PRINT-RECORD FROM TITLE-LINE-SUM-4 AFTER 1.
     WRITE PRINT-RECORD FROM TITLE-LINE-SUM-5 AFTER 1.
      PERFORM VARYING S-SUB FROM 1 BY 1
          UNTIL S-SUB > 6
         MOVE PRODUCT-LINE (S-SUB) TO SUM-PROD-LINE         
           PERFORM VARYING A-SUB FROM 1 BY 1
             UNTIL A-SUB > 3
                MOVE LINE-REVENUE (S-SUB  A-SUB) TO SUM-REV-PR (S-SUB)   
           END-PERFORM
       WRITE PRINT-RECORD FROM SUMMARY-LINE AFTER 1 
      END-PERFORM.

     MOVE 'TOTAL' TO SUM-PROD-LINE   
     PERFORM VARYING A-SUB FROM 1 BY 1
      UNTIL A-SUB > 3
         MOVE WS-TOTAL (A-SUB) TO SUM-REV-PR (A-SUB)
     END-PERFORM.
```

#### ↳ Re: quick help question

- **From:** Jeff Farkas <tazberjef@naxs.nospam.net>
- **Date:** 2001-02-19T11:16:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.14fb10da9ade5c4998968a@news.naxs.com>`
- **References:** `<20010219110735.02143.00000021@ng-cm1.aol.com>`

```
In article <20010219110735.02143.00000021@ng-cm1.aol.com>, deek40@aol.com 
says...
> Hello once again, I am a student and trying to learn cobol, when i compile my
> program i got like 50 errors ok np i fixed all the ones i could but there are a
…[13 more quoted lines elided]…
>      END-PERFORM.
Where do you have DESC-PR Defined?? In the DETAIL-LINE you have 
DETAIL-DESC.. maybe that's where you would want to put DESC-PR??

Jeff...

> 2) user word 'summary-line' is multi defined
> here is the code it points to:
…[31 more quoted lines elided]…
> 	   SELECT SOFTWARE-FILE
```

#### ↳ Re: quick help question

- **From:** Jeff Farkas <tazberjef@naxs.nospam.net>
- **Date:** 2001-02-19T11:22:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.14fb12577bdf363d98968b@news.naxs.com>`
- **References:** `<20010219110735.02143.00000021@ng-cm1.aol.com>`

```
In article <20010219110735.02143.00000021@ng-cm1.aol.com>, deek40@aol.com 
says...
Hi..

 The problem I can see is that you defining the same item twice.. it's 
not going to work with COBOL,IMO. Use a unique name for these items and 
try to compile again. I think you will get the results you're looking 
for.

Jeff...........

"I calculated the odds of this thing succeeding versus the odds of it 
doing something incredibly stupid.....and......I went ahead anyway"
{Crow from MST3K}


> Hello once again, I am a student and trying to learn cobol, when i compile my
> program i got like 50 errors ok np i fixed all the ones i could but there are a
…[309 more quoted lines elided]…
>
```

##### ↳ ↳ Re: quick help question

- **From:** deek40@aol.com (Deek40)
- **Date:** 2001-02-19T17:09:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010219120937.04305.00000464@ng-ck1.aol.com>`
- **References:** `<MPG.14fb12577bdf363d98968b@news.naxs.com>`

```
I got rid of the detail-desc one but i still cant get rid of the summary-line
one:(
```

###### ↳ ↳ ↳ Re: quick help question

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-19T11:00:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A915F3A.56064B5E@brazee.net>`
- **References:** `<MPG.14fb12577bdf363d98968b@news.naxs.com> <20010219120937.04305.00000464@ng-ck1.aol.com>`

```


Deek40 wrote:

> I got rid of the detail-desc one but i still cant get rid of the summary-line
> one:(

Do the same thing.   Look for "SUMMARY-LINE" and see how often it occurs.  If it
happens more than once, CoBOL needs to know which one you are using.
```

###### ↳ ↳ ↳ Re: quick help question

- **From:** Jeff Farkas <tazberjef@naxs.nospam.net>
- **Date:** 2001-02-19T13:01:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.14fb2964c55223ff989690@news.naxs.com>`
- **References:** `<MPG.14fb12577bdf363d98968b@news.naxs.com> <20010219120937.04305.00000464@ng-ck1.aol.com>`

```
In article <20010219120937.04305.00000464@ng-ck1.aol.com>, deek40@aol.com 
says...
> I got rid of the detail-desc one but i still cant get rid of the summary-line
> one:(
> 

I would just change the 01 SUMMARY-LINE to SUMM-LINE. Or something like 
that and the code in the procedure division as well. 

Try that out and see what happens...

Jeff....
Remove nospam from email address.
```

#### ↳ Re: quick help question

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-19T10:57:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A915E97.D351FBE0@brazee.net>`
- **References:** `<20010219110735.02143.00000021@ng-cm1.aol.com>`

```


Deek40 wrote:

> Hello once again, I am a student and trying to learn cobol, when i compile my
> program i got like 50 errors ok np i fixed all the ones i could but there are a
…[13 more quoted lines elided]…
>      END-PERFORM.

But that's not where it is defined.  Even though one of your DETAIL-DESC is within
an occurs, and the other was not, CoBOL won't make any assumptions on what you
want.  It needs an unambiguous definition.  If you have more than one DETAIL-DESC
(a practice which is frowned upon in many shops), you need to qualify your
statement with an OF or IN.
```

##### ↳ ↳ Re: quick help question

- **From:** deek40@aol.com (Deek40)
- **Date:** 2001-02-19T18:39:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010219133945.04298.00000507@ng-ck1.aol.com>`
- **References:** `<3A915E97.D351FBE0@brazee.net>`

```
thanks howard, i didnt know that since i am fairly new to cobol.  Thanks again
for the help.
```

#### ↳ Re: quick help question

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-19T22:04:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GLgk6.6$rX4.980@newsread1.prod.itd.earthlink.net>`
- **References:** `<20010219110735.02143.00000021@ng-cm1.aol.com>`

```

"Deek40" <deek40@aol.com>

> 1)user word 'Detail  Desc' is multidefined

Silly compiler!

It doesn't point to the multiple definitions (in the Data Division)
but tries to confuse you by pointing to where these multiple
definitions are used (the Procedure Division).

But, then again, just as a falling tree makes no sound if there's no
one to hear (according to some), there is no error with multiple
definitions unless you try to use one.

Anyway, look in the data-forest, not the procedure-forest.
```

##### ↳ ↳ Re: quick help question

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-19T17:33:53-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<96sah0$oud$1@slb4.atl.mindspring.net>`
- **References:** `<20010219110735.02143.00000021@ng-cm1.aol.com> <GLgk6.6$rX4.980@newsread1.prod.itd.earthlink.net>`

```
There is nothing "illegal" with having multiple definitions of the same
items in the data division - so it can't issue a message there.  These are
legal for two reasons:

1) (most common) you use "qualification" ("OF/IN" phrase) when referencing a
data item in the procedure division.  Very COMMON if you define your record
layouts in "copy books".

2) (less common - but has its reason)  If you do NOT reference a data item
in the procedure division, it is "totally legal" (but not usually useful) to
have as many multiple definitions - even at the 01-level - or unable to be
qualified - in the data division.  (FYI - this was a change between the '74
and '85 Standards, so those of you still using '74 compilers may not have
this "feature" <G>)
```

##### ↳ ↳ Re: quick help question

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-02-20T08:11:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A928927.B26C69D0@brazee.net>`
- **References:** `<20010219110735.02143.00000021@ng-cm1.aol.com> <GLgk6.6$rX4.980@newsread1.prod.itd.earthlink.net>`

```
Jerry P wrote:

> "Deek40" <deek40@aol.com>
>
…[10 more quoted lines elided]…
> definitions unless you try to use one.

Unless you try to use one incorrectly (ambiguously).  You can still use
them with qualifiers.

> Anyway, look in the data-forest, not the procedure-forest.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
