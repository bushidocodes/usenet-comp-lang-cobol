[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# TOTAL-LINE QUESTION

_18 messages · 10 participants · 2000-12_

---

### TOTAL-LINE QUESTION

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-12-14T01:08:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001213200806.12046.00004824@ng-cj1.aol.com>`

```
I KEEP GETTING A SYNTAX ERROR WS-DOLLAR-VALUE-TOT IN A ARITHMATIC EXPRESSION
MUST BE A NUMERIC ITEM.  i CANNOT FIND MY ERROR IN MY CODE I WOULD APPRECIATE
IT IF SOMEONE COULD PLEASE TAKE A LOOK.

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
 		ASSIGN TO "A:\COBOL\Proj7\Invntory.DAT"
		ORGANIZATION LINE SEQUENTIAL
		ACCESS	     SEQUENTIAL.
     SELECT PRINT-FILE
		ASSIGN TO "A:\COBOL\PROJ7\Report.txt"
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
    05 IR-QTY-TO-REORDER		PIC S9(7)
    				SIGN TRAILING SEPARATE.
    05 IR-REORDER-PT              PIC S9(7)
                                  SIGN TRAILING SEPARATE.
    05 IR-UNIT-COST		PIC S9(5)V9(4)
                                  SIGN TRAILING SEPARATE.
    05 IR-UNIT-OF-MEASURE         PIC X(02).
    05 FILLER			PIC X(06).
  FD PRINT-FILE.
  01 PRINT-RECORD			PIC X(80).  
 WORKING-STORAGE SECTION.

 01 SYSTEM-DATE-AND-TIME.
    05 SYSTEM-DATE.
	     
	     10 SYS-DATE-CCYY             PIC 9(4).
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
	  05 FILLER 			PIC X(10) VALUE SPACES.
	  05 FILLER			PIC X(5)  VALUE "Page ".
	  05 H1-PAGE-NUM		PIC 9.
 01 HEAD-2.
	  05 H2-TIME.
		10 H2-DOW		PIC X(3).
		10 FILLER		PIC X VALUE SPACE.
		10 H2-TIME-HOURS-LIT        PIC X(2).
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
	  05 FILLER  			PIC X(4)   VALUE SPACES.
    05 FILLER			PIC X(6)   VALUE SPACES.
	  05 FILLER			PIC X(8)   VALUE SPACES.
 01 TITLE-LINE-2.
    05 FILLER                     PIC X(8)  VALUE 'Item Nbr'.
	  05 FILLER			PIC X(2)   VALUE SPACES.
	  05 FILLER			PIC X(16)  VALUE 
						 'Item Description'.
	  05 FILLER    			PIC X(14) VALUE SPACES.
	  05 FILLER			PIC X(7)  VALUE 'On Hand'.
	  05 FILLER  			PIC X(7)  VALUE SPACES.
	  05 FILLER			PIC X(9)  VALUE 'Unit Cost'.
    05 FILLER			PIC X(5)  VALUE SPACES.
	  05 FILLER			PIC X(12) VALUE 'Dollar Value'.
 01 DETAIL-LINE.
    05 DL-ITEM-NUM	        PIC  X(08)   VALUE SPACES.
    05 FILLER   		        PIC  X(01)   VALUE SPACES.
    05 DL-ITEM-DESC		PIC  X(30)   VALUE SPACES.
	  05 FILLER			PIC  X(1)    VALUE SPACES. 
	  05 DL-QTY-ON-HAND    	  	PIC  Z(6)9-  VALUE ZEROS.
    05 FILLER			PIC  X(4)    VALUE SPACES.
    05 DL-UNIT-COST		PIC  ZZ,ZZ9.9999-  .
    05 FILLER			PIC  X(1)    VALUE SPACES.
    05 DL-DOLLAR-VALUE		PIC  ZZZ,ZZZ,ZZ9.99-  .
 01 WS-ACCUMULATORS.

     05 WS-QTY-ON-HAND-TOT		PIC  S9(7)   VALUE ZEROS.

	  05 WS-UNIT-COST-TOT		PIC  ZZZ,ZZZ,ZZ9.99 VALUE ZEROS.
	  05 WS-DOLLAR-VALUE-TOT	PIC  999,999,999.99 VALUE ZEROS.
 01 TOTAL-LINE.
    05 FILLER 			PIC  X(10)   VALUE SPACES.
    05 FILLER			PIC  X(5)    VALUE 'Total'.
	  05 FILLER			PIC  X(1)    VALUE SPACES.
	  05 FILLER			PIC  X(10)   VALUE 'Quantities'.
    05 FILLER			PIC  X(15)   VALUE SPACES.
    05 TL-QTY-ON-HAND-TOT	        PIC  Z(6)9-.
    05 FILLER                     PIC  X(4)    VALUE SPACES.
    05 TL-UNIT-COST-TOT           PIC  ZZZ,ZZZ,ZZ9.99.
    05 FILLER                     PIC  X(7)    VALUE SPACES.
    05 TL-DOLLAR-VALUE-TOT        PIC  999,999,999.99.

* 01 WS-QTY-TO-REORDER               PIC  S9(7).
 01 WS-DOW 			PIC 9 	     VALUE ZERO.
 01 WS-REORDER-PT			PIC  9(6).
 01 WS-QTY-ON-HAND		PIC  9(6).
 01 EOF-FLAG		        PIC  X(01)   VALUE SPACE.  
 
 
 01 WS-DOLLAR-VALUE	        PIC S9(14)V99  
					SIGN TRAILING SEPARATE.
 01 WS-PAGE-CNT 			PIC  9(3) VALUE 0.
 01 WS-LINE-CNT			PIC  9(3) VALUE 0.
 01 PAGE-SIZE			PIC  9(3) VALUE 54.
 PROCEDURE DIVISION.
 MAINLINE.
     PERFORM 100-INITIALIZATION
     PERFORM 110-WRITE-HEADINGS
     PERFORM 200-PROCESSING
     PERFORM 300-TERMINATION

	   STOP RUN.
 100-INITIALIZATION.
     OPEN INPUT INVENTORY-FILE
		OUTPUT PRINT-FILE.
*     PERFORM 110-WRITE-HEADINGS
 110-WRITE-HEADINGS.
	   ADD 1 TO WS-PAGE-CNT
	   MOVE WS-PAGE-CNT TO H1-PAGE-NUM.
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
*		MOVE SYS-TIME-HOURS   TO H2-TIME-HOURS.
		MOVE SYS-TIME-MINUTES TO H2-TIME-MINUTES.
          MOVE SYS-TIME-SECONDS TO H2-TIME-SECONDS.
		WRITE PRINT-RECORD    FROM HEAD-2 AFTER 1
		MOVE SYS-DATE-CCYY    TO H1-DATE-CCYY.
 		
*   	MOVE SYS-DATE-MM   TO H1-DATE-MM.
 		MOVE SYS-DATE-DD   TO H1-DATE-DD.
          WRITE PRINT-RECORD FROM HEAD-1 AFTER 1
	   MOVE SPACES             TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER 1.
	   MOVE TITLE-LINE-1       TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER ADVANCING 1.
	   MOVE TITLE-LINE-2       TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER ADVANCING 1.	 	
     MOVE SPACES             TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER 1.
	   MOVE 6 TO WS-LINE-CNT.
 200-PROCESSING.
     PERFORM UNTIL EOF-FLAG = 'Y'
         READ INVENTORY-FILE
	       AT END
		   MOVE 'Y' TO EOF-FLAG
         NOT AT END  
*             IF IR-QTY-ON-HAND < IR-REORDER-PT  
             PERFORM 205-PROCESS-A-RECORD    	       
*	         END-IF
	       END-READ 
	   END-PERFORM.
 205-PROCESS-A-RECORD.
	   IF WS-LINE-CNT > PAGE-SIZE
		 PERFORM 110-WRITE-HEADINGS
	   END-IF
     PERFORM 210-DISPLAY-A-LINE
*	   WRITE PRINT-RECORD FROM DETAIL-LINE AFTER 1.
	   ADD 1 TO WS-LINE-CNT.
 210-DISPLAY-A-LINE.
     	   COMPUTE WS-DOLLAR-VALUE 
			ROUNDED = IR-QTY-ON-HAND  *  IR-UNIT-COST  
	           END-COMPUTE
		           
 		 MOVE IR-ITEM-NBR 
		     TO DL-ITEM-NUM
	         MOVE IR-ITEM-DESCRIPTION
 		     TO DL-ITEM-DESC
	         MOVE IR-QTY-ON-HAND
		     TO DL-QTY-ON-HAND
	         MOVE IR-UNIT-COST
		     TO DL-UNIT-COST
		 MOVE WS-DOLLAR-VALUE 
		     TO DL-DOLLAR-VALUE
           MOVE DETAIL-LINE    TO PRINT-RECORD
		 WRITE PRINT-RECORD AFTER 1.
*	   ADD IR-QTY-ON-HAND    TO WS-QTY-ON-HAND-TOT.
*     ADD IR-REORDER-PT     TO WS-REORDER-PT-TOT.
     COMPUTE WS-UNIT-COST-TOT ROUNDED = WS-DOLLAR-VALUE-TOT / 
				  WS-QTY-ON-HAND-TOT
     END-COMPUTE.
     ADD 1 TO WS-LINE-CNT.
 300-TERMINATION.
     MOVE SPACES TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER 1.
	   MOVE WS-QTY-ON-HAND-TOT    TO TL-QTY-ON-HAND-TOT.
	   MOVE WS-UNIT-COST-TOT     TO TL-UNIT-COST-TOT.
*	   MOVE WS-QTY-TO-REORDER-TOT TO TL-DOLLAR-VALUE-TOT.
     MOVE TOTAL-LINE TO PRINT-RECORD.
       WRITE PRINT-RECORD AFTER ADVANCING 1.
     CLOSE INVENTORY-FILE
           PRINT-FILE
```

#### ↳ Re: TOTAL-LINE QUESTION

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-14T01:58:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wPVZ5.5194$Sl.264192@iad-read.news.verio.net>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com>`

```
In article <20001213200806.12046.00004824@ng-cj1.aol.com>,
Deek40 <deek40@aol.com> wrote:
>I KEEP GETTING A SYNTAX ERROR WS-DOLLAR-VALUE-TOT IN A ARITHMATIC EXPRESSION
>MUST BE A NUMERIC ITEM.  i CANNOT FIND MY ERROR IN MY CODE I WOULD APPRECIATE
>IT IF SOMEONE COULD PLEASE TAKE A LOOK.

[snippage]

>	  05 WS-DOLLAR-VALUE-TOT	PIC  999,999,999.99 VALUE ZEROS.

PIC 999,999,999.99 is not numeric... it is an edited-numeric.  It might be
interesting to change the specified decimal to an implied one.

DD
```

##### ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-12-14T13:25:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001214082544.01956.00002594@ng-fk1.aol.com>`
- **References:** `<wPVZ5.5194$Sl.264192@iad-read.news.verio.net>`

```
so something similar to 99V99?
```

###### ↳ ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-12-14T13:52:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gg4_5.5224$Sl.266965@iad-read.news.verio.net>`
- **References:** `<wPVZ5.5194$Sl.264192@iad-read.news.verio.net> <20001214082544.01956.00002594@ng-fk1.aol.com>`

```
In article <20001214082544.01956.00002594@ng-fk1.aol.com>,
Deek40 <deek40@aol.com> wrote:
>so something similar to 99V99?

Ummmmm... this falls under the heading of doing your own homework; perhaps
some experimentation is in order.

DD
```

###### ↳ ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-12-15T03:47:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001214224728.12681.00004462@ng-ce1.aol.com>`
- **References:** `<20001214082544.01956.00002594@ng-fk1.aol.com>`

```
>From: deek40@aol.com  (Deek40)
>Date: 12/14/00 8:25 AM Eastern Standard Time
>Message-id: <20001214082544.01956.00002594@ng-fk1.aol.com>
>
>so something similar to 99V99?

Yup - you're catching on.
```

###### ↳ ↳ ↳ Re: TOTAL-LINE QUESTION

_(reply depth: 4)_

- **From:** "Searcher" <Searcher_mctell@hotmail.com>
- **Date:** 2000-12-15T17:32:54+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a3a3bc0$0$232@hades.is.co.za>`
- **References:** `<20001214082544.01956.00002594@ng-fk1.aol.com> <20001214224728.12681.00004462@ng-ce1.aol.com>`

```

YukonMama <yukonmama@aol.com> wrote in message
news:20001214224728.12681.00004462@ng-ce1.aol.com...
> >From: deek40@aol.com  (Deek40)
> >Date: 12/14/00 8:25 AM Eastern Standard Time
…[4 more quoted lines elided]…
> Yup - you're catching on.


05 WS-UNIT-COST-TOT PIC  ZZZ,ZZZ,ZZ9.99 VALUE ZEROS

Can this be computed? Hell I dont remember ??
```

###### ↳ ↳ ↳ Re: TOTAL-LINE QUESTION

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-12-15T09:33:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A3A47D3.1DD30038@brazee.net>`
- **References:** `<20001214082544.01956.00002594@ng-fk1.aol.com> <20001214224728.12681.00004462@ng-ce1.aol.com> <3a3a3bc0$0$232@hades.is.co.za>`

```
Searcher wrote:

> 05 WS-UNIT-COST-TOT PIC  ZZZ,ZZZ,ZZ9.99 VALUE ZEROS
>
> Can this be computed? Hell I dont remember ??

Fortunately, you don't have to remember.  You can look it up.
```

###### ↳ ↳ ↳ Re: TOTAL-LINE QUESTION

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-12-20T12:53:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a40aba2.1830399@news1.attglobal.net>`
- **References:** `<20001214082544.01956.00002594@ng-fk1.aol.com> <20001214224728.12681.00004462@ng-ce1.aol.com> <3a3a3bc0$0$232@hades.is.co.za>`

```
I think you will be suprised to find that your field as defined below
does not contain 0.00 but rather contains 000000000000000 

On Fri, 15 Dec 2000 17:32:54 +0200, "Searcher"
<Searcher_mctell@hotmail.com> wrote:

>
>YukonMama <yukonmama@aol.com> wrote in message
…[14 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: TOTAL-LINE QUESTION

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-14T00:16:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<919oia$5nt$1@slb1.atl.mindspring.net>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com>`

```
The topics to look up (to solve this yourself <G>) are:

 - Numeric vs Numeric-Edited items (possibly under a discussion of CATEGORY
and CLASS of data-items)
 - Arithmetic statements and their "operands" (restrictions on both sending
and receiving items)

If you understand these concepts, I think you will be able to understand -
and CORRECT - your syntax error
```

#### ↳ Re: TOTAL-LINE QUESTION

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-12-14T07:22:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A38D792.F777797A@brazee.net>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com>`

```


Deek40 wrote:

> I KEEP GETTING A SYNTAX ERROR WS-DOLLAR-VALUE-TOT IN A ARITHMATIC EXPRESSION
> MUST BE A NUMERIC ITEM.  i CANNOT FIND MY ERROR IN MY CODE I WOULD APPRECIATE
> IT IF SOMEONE COULD PLEASE TAKE A LOOK.

I bet all of the programmers looked at the above question and knew what we would
find in the code.  This is an error we never get though, it is a beginner's only
error.

When a field has a picture such as 999,999,999.99  it no longer is a number.
Numbers can be moved to such a field.  That move puts commas and decimals in the
right place to make a display.  But commas, periods, spaces, dollar signs, plus,
minus, etc. are not numeric.

Only use such pictures in your output.  If you have to have them in your input,
you need to convert these alphanumeric strings to real numbers before you can do
arithmetic with them.  Real numbers do not have commas nor periods in them (the
computer uses the "V" to tell where the decimal is, and "S" to tell if it is
signed)
```

#### ↳ Re: TOTAL-LINE QUESTION

- **From:** lcccpiasabird@my-deja.com
- **Date:** 2000-12-14T16:25:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91asa1$vd5$1@nnrp1.deja.com>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com>`

```


NOTE:
Any numeric value with a pic clause with a comma, a dolloa sign, a
decimal point blanks (ZZZ), etc is an edited field and can not be used
in a calculation because it has non-numeric data in it for printing
purposes.

You need an accumulator or counter to put the data into in other words
the calculation field must be strictly like (PIC 9(10).)  Your compiler
may be able to unedit the number somehow if you look it up!

In article <20001213200806.12046.00004824@ng-cj1.aol.com>,
  deek40@aol.com (Deek40) wrote:
> I KEEP GETTING A SYNTAX ERROR WS-DOLLAR-VALUE-TOT IN A ARITHMATIC
EXPRESSION
> MUST BE A NUMERIC ITEM.  i CANNOT FIND MY ERROR IN MY CODE I WOULD
APPRECIATE
> IT IF SOMEONE COULD PLEASE TAKE A LOOK.
>
…[3 more quoted lines elided]…
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
…[256 more quoted lines elided]…
>


Sent via Deja.com
http://www.deja.com/
```

##### ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-14T12:35:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91b3sr$li5$1@slb0.atl.mindspring.net>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com> <91asa1$vd5$1@nnrp1.deja.com>`

```
Probably not the answer that Derrick should use in his first semester of
COBOL - but there is another alternative which CAN accomplish this without
keeping both a numeric and a numeric-edited version of the field. Consider
the statement:

      COMPUTE WS-UNIT-COST-TOT ROUNDED =
            (Function NumVal (WS-DOLLAR-VALUE-TOT)) / WS-QTY-ON-HAND-TOT
                On Size Error
                       Display "Consider the possibility that QTY-ON-HAND is
zero"
      END-COMPUTE

P.S. notice my removal of the period after the END-COMPUTE statement and the
addition of the ON SIZE ERROR phrase.

   ***

I think that in *most* "real-world" applications, it is BETTER to have both
a numeric and numeric-edited version of such fields - but it isn't required
the the language (since the Intrinsic Function amendment)
```

#### ↳ Re: TOTAL-LINE QUESTION

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-12-15T15:12:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001215101248.23511.00004987@ng-fv1.aol.com>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com>`

```
OK I fixed the syntax error, but i dug a bigger hole.  Now i get a succesful
compile and build, but when i try to run it I get and error and the program
terminates. 
could it be i am still moving a numeric to a edited or alpanum feild?  I
checked for it but i may have missed something.
Here is my code:
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
 		ASSIGN TO "A:\COBOL\Proj7\Invntory.DAT"
		ORGANIZATION LINE SEQUENTIAL
		ACCESS	     SEQUENTIAL.
     SELECT PRINT-FILE
		ASSIGN TO "A:\COBOL\PROJ7\Report.txt"
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
    05 IR-QTY-TO-REORDER		PIC S9(7)
    				SIGN TRAILING SEPARATE.
    05 IR-REORDER-PT              PIC S9(7)
                                  SIGN TRAILING SEPARATE.
    05 IR-UNIT-COST		PIC S9(5)V9(4)
                                  SIGN TRAILING SEPARATE.
    05 IR-UNIT-OF-MEASURE         PIC X(02).
    05 FILLER			PIC X(06).
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
	  05 FILLER 			PIC X(10) VALUE SPACES.
	  05 FILLER			PIC X(5)  VALUE "Page ".
	  05 H1-PAGE-NUM		PIC 9.
 01 HEAD-2.
	  05 H2-TIME.
		10 H2-DOW		PIC X(3).
		10 FILLER		PIC X VALUE SPACE.
		10 H2-TIME-HOURS-LIT        PIC X(2).
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
	  05 FILLER  			PIC X(4)   VALUE SPACES.
    05 FILLER			PIC X(6)   VALUE SPACES.
	  05 FILLER			PIC X(8)   VALUE SPACES.
 01 TITLE-LINE-2.
    05 FILLER                     PIC X(8)  VALUE 'Item Nbr'.
	  05 FILLER			PIC X(2)   VALUE SPACES.
	  05 FILLER			PIC X(16)  VALUE 
						 'Item Description'.
	  05 FILLER    			PIC X(14) VALUE SPACES.
	  05 FILLER			PIC X(7)  VALUE 'On Hand'.
	  05 FILLER  			PIC X(7)  VALUE SPACES.
	  05 FILLER			PIC X(9)  VALUE 'Unit Cost'.
    05 FILLER			PIC X(5)  VALUE SPACES.
	  05 FILLER			PIC X(12) VALUE 'Dollar Value'.
 01 DETAIL-LINE.
    05 DL-ITEM-NUM	        PIC  X(08)   VALUE SPACES.
    05 FILLER   		        PIC  X(01)   VALUE SPACES.
    05 DL-ITEM-DESC		PIC  X(30)   VALUE SPACES.
	  05 FILLER			PIC  X(1)    VALUE SPACES. 
	  05 DL-QTY-ON-HAND    	  	PIC  Z(6)9-  VALUE ZEROS.
    05 FILLER			PIC  X(4)    VALUE SPACES.
    05 DL-UNIT-COST		PIC  S9(11)V999 VALUE ZEROS  .
    05 FILLER			PIC  X(1)    VALUE SPACES.
    05 DL-DOLLAR-VALUE		PIC  S9(11)V999 VALUE ZEROS  .
 01 WS-ACCUMULATORS.

     05 WS-QTY-ON-HAND-TOT	PIC  S9(7)   VALUE ZEROS.

	  05 WS-UNIT-COST-TOT		PIC  S9(11)V999 VALUE ZEROS.
	  05 WS-DOLLAR-VALUE-TOT	PIC  S9(11)V999 VALUE ZEROS.
 01 TOTAL-LINE.
    05 FILLER 			PIC  X(10)   VALUE SPACES.
    05 FILLER			PIC  X(5)    VALUE 'Total'.
	  05 FILLER			PIC  X(1)    VALUE SPACES.
	  05 FILLER			PIC  X(10)   VALUE 'Quantities'.
    05 FILLER			PIC  X(15)   VALUE SPACES.
    05 TL-QTY-ON-HAND-TOT	        PIC  S9(7).
    05 FILLER                     PIC  X(4)    VALUE SPACES.
    05 TL-UNIT-COST-TOT           PIC  S9(11)V999.
    05 FILLER                     PIC  X(7)    VALUE SPACES.
    05 TL-DOLLAR-VALUE-TOT        PIC  S9(11)V999.

 01 WS-DOW 			PIC 9 	     VALUE ZERO.
 01 WS-REORDER-PT			PIC  9(6).
 01 WS-QTY-ON-HAND		PIC  9(6).
 01 EOF-FLAG		        PIC  X(01)   VALUE SPACE.  
 
 
 01 WS-DOLLAR-VALUE	        PIC S9(14)V99  
					SIGN TRAILING SEPARATE.
 01 WS-PAGE-CNT 			PIC  9(3) VALUE 0.
 01 WS-LINE-CNT			PIC  9(3) VALUE 0.
 01 PAGE-SIZE			PIC  9(3) VALUE 54.
 PROCEDURE DIVISION.
 MAINLINE.
     PERFORM 100-INITIALIZATION
     PERFORM 110-WRITE-HEADINGS
     PERFORM 200-PROCESSING
     PERFORM 300-TERMINATION

	   STOP RUN.
 100-INITIALIZATION.
     OPEN INPUT INVENTORY-FILE
		OUTPUT PRINT-FILE.
 110-WRITE-HEADINGS.
	   ADD 1 TO WS-PAGE-CNT
	   MOVE WS-PAGE-CNT TO H1-PAGE-NUM.
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
*		MOVE SYS-TIME-HOURS   TO H2-TIME-HOURS.
		MOVE SYS-TIME-MINUTES TO H2-TIME-MINUTES.
          MOVE SYS-TIME-SECONDS TO H2-TIME-SECONDS.
		WRITE PRINT-RECORD    FROM HEAD-2 AFTER 1
		MOVE SYS-DATE-CCYY    TO H1-DATE-CCYY.
 		
*   	MOVE SYS-DATE-MM   TO H1-DATE-MM.
 		MOVE SYS-DATE-DD   TO H1-DATE-DD.
          WRITE PRINT-RECORD FROM HEAD-1 AFTER 1
	   MOVE SPACES             TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER 1.
	   MOVE TITLE-LINE-1       TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER ADVANCING 1.
	   MOVE TITLE-LINE-2       TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER ADVANCING 1.	 	
     MOVE SPACES             TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER 1.
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
	   IF WS-LINE-CNT > PAGE-SIZE
		 PERFORM 110-WRITE-HEADINGS
	   END-IF
     PERFORM 210-DISPLAY-A-LINE
*	   WRITE PRINT-RECORD FROM DETAIL-LINE AFTER 1.
	   ADD 1 TO WS-LINE-CNT.
 210-DISPLAY-A-LINE.
     	   COMPUTE WS-DOLLAR-VALUE 
			ROUNDED = IR-QTY-ON-HAND  *  IR-UNIT-COST  
	           END-COMPUTE
		           
 		 MOVE IR-ITEM-NBR 
		     TO DL-ITEM-NUM
	         MOVE IR-ITEM-DESCRIPTION
 		     TO DL-ITEM-DESC
	         MOVE IR-QTY-ON-HAND
		     TO DL-QTY-ON-HAND
	         MOVE IR-UNIT-COST
		     TO DL-UNIT-COST
		 MOVE WS-DOLLAR-VALUE 
		     TO DL-DOLLAR-VALUE
           MOVE DETAIL-LINE    TO PRINT-RECORD
		 WRITE PRINT-RECORD AFTER 1.
*	   ADD IR-QTY-ON-HAND    TO WS-QTY-ON-HAND-TOT.
*     ADD IR-REORDER-PT     TO WS-REORDER-PT-TOT.
     COMPUTE WS-UNIT-COST-TOT ROUNDED = WS-DOLLAR-VALUE-TOT / 
				  WS-QTY-ON-HAND-TOT
     END-COMPUTE.
     ADD 1 TO WS-LINE-CNT.
 300-TERMINATION.
     MOVE SPACES TO PRINT-RECORD
		WRITE PRINT-RECORD AFTER 1.
	   MOVE WS-QTY-ON-HAND-TOT   TO TL-QTY-ON-HAND-TOT.
	   MOVE WS-UNIT-COST-TOT     TO TL-UNIT-COST-TOT.
     MOVE WS-DOLLAR-VALUE-TOT TO TL-DOLLAR-VALUE-TOT.
     MOVE TOTAL-LINE TO PRINT-RECORD.
       WRITE PRINT-RECORD AFTER ADVANCING 1.
     CLOSE INVENTORY-FILE
           PRINT-FILE
```

##### ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-12-15T09:32:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A3A47A3.E2C4FD1D@brazee.net>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com> <20001215101248.23511.00004987@ng-fv1.aol.com>`

```


Deek40 wrote:

> OK I fixed the syntax error, but i dug a bigger hole.  Now i get a succesful
> compile and build, but when i try to run it I get and error and the program
…[3 more quoted lines elided]…
> Here is my code:

I did not look at your code, not wanting to do your homework.  Find out which
statement is your problem.  Either run a debugger or put displays in the code.
If one command works and the next one fails, you will know which command is
faulty.
```

##### ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-12-15T12:29:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0951F46610F0EC61.9098583B0D415BF8.68C349212FA8B736@lp.airnews.net>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com> <20001215101248.23511.00004987@ng-fv1.aol.com>`

```


Scroll down to see where I found your error.


On 15 Dec 2000 15:12:48 GMT, deek40@aol.com (Deek40) enlightened us:

>OK I fixed the syntax error, but i dug a bigger hole.  Now i get a succesful
>compile and build, but when i try to run it I get and error and the program
…[255 more quoted lines elided]…
>		 WRITE PRINT-RECORD AFTER 1.


>*	   ADD IR-QTY-ON-HAND    TO WS-QTY-ON-HAND-TOT.
>*     ADD IR-REORDER-PT     TO WS-REORDER-PT-TOT.
>     COMPUTE WS-UNIT-COST-TOT ROUNDED = WS-DOLLAR-VALUE-TOT / 
>				  WS-QTY-ON-HAND-TOT
>     END-COMPUTE.

In the above statement you are performing a divide using
WS-QTY-ON-HAND-TOT as your divisor.  However, it contains zero
(initial value) because the statement that would add something to it
is commented out!  Dividing by zero causes black holes to appear in
the universe and computer programs to crash!!



>     ADD 1 TO WS-LINE-CNT.
> 300-TERMINATION.
…[8 more quoted lines elided]…
>           PRINT-FILE

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

An optimist thinks that this is the best possible world.
A pessimist fears that this is true.

Help Save The Rainforest
For more info, please see:  
http://www.ran.org/ran/

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** "Searcher" <Searcher_mctell@hotmail.com>
- **Date:** 2000-12-15T19:50:15+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a3a5bf6$0$226@helios.is.co.za>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com> <20001215101248.23511.00004987@ng-fv1.aol.com> <0951F46610F0EC61.9098583B0D415BF8.68C349212FA8B736@lp.airnews.net>`

```
Skippy you make things to easy man.!
```

#### ↳ Re: TOTAL-LINE QUESTION

- **From:** "John P Fife" <jfife1@home.com>
- **Date:** 2000-12-16T01:06:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Oez_5.70734$15.15304406@news1.rdc1.az.home.com>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com>`

```
From what I can see the only thing that you did with ws-dollar-value-tot is
have it initialized at zeros. So when you divide ws-dollar-value-tot which
is 00 by another value you have an error.
It also looks like WS-QTY-ON-HAND-TOT could be zeros I could not tell
whether your add to WS-QTY-ON-HAND-TOT was commented out.

"Deek40" <deek40@aol.com> wrote in message
news:20001213200806.12046.00004824@ng-cj1.aol.com...
> I KEEP GETTING A SYNTAX ERROR WS-DOLLAR-VALUE-TOT IN A ARITHMATIC
EXPRESSION
> MUST BE A NUMERIC ITEM.  i CANNOT FIND MY ERROR IN MY CODE I WOULD
APPRECIATE
> IT IF SOMEONE COULD PLEASE TAKE A LOOK.
>
…[270 more quoted lines elided]…
>            PRINT-FILE
```

##### ↳ ↳ Re: TOTAL-LINE QUESTION

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-12-15T20:45:44-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91ekvp$ng0$1@nntp9.atl.mindspring.net>`
- **References:** `<20001213200806.12046.00004824@ng-cj1.aol.com> <Oez_5.70734$15.15304406@news1.rdc1.az.home.com>`

```
I may be "overly cautious" - but *in general* - when I code a DIVIDE
statement (either via COMPUTE or DIVIDE) - I either

1) Code an ON SIZE ERROR phrase

2) Code it within an "IF" statement checking for zero

  ***

Some threads in CLC talk about giving the customer what they want, but I
(almost) never believe someone when they tell me a field can't EVER be zero.
(I also am EXTREMELY dubious when a "designer/analyst" tell me that I
specific field can NEVER be greater than some specific value.)  Unless you
are in a "really tight loop," the performance disadvantages of an explicit
ON SIZE ERROR phrase are rarely more significant that "protective coding".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
