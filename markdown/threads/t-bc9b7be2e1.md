[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol help please

_8 messages · 6 participants · 2001-05_

---

### cobol help please

- **From:** deek163@aol.com (Deek163)
- **Date:** 2001-05-11T15:22:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010511112231.13807.00003452@ng-cj1.aol.com>`

```
This is what i have done so far could somebody please scan for major errors, i
have a few that i cant seem to solve here is my code. BTW i know its far from
done.

 IDENTIFICATION DIVISION.
 PROGRAM-ID.    PROJ5.

****************************************
* Purpose:                             *
* Class: CIS260A.                      *
* Author: Derrick.                     *
* Written: 04/25/01.                   *
* Compiler: Fujitsu Cobol 4.0.         *
****************************************

 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 SOURCE-COMPUTER. IBM-PC.
 OBJECT-COMPUTER. IBM-PC.

 INPUT-OUTPUT SECTION.
 FILE-CONTROL.
     SELECT TRANSACTION-FILE
         ASSIGN TO "A:\STOKTRAN.DAT".
     SELECT SORT-FILE
         ASSIGN TO SORTWORK.
     SELECT AUDIT-REPORT
	       ASSIGN TO "A:\ADUIT.TXT".
     SELECT MASTER-FILE
	       ASSIGN TO "A:\STOCKMAST"
	       ORGANIZATION IS INDEXED
	       ACCESS IS RANDOM
	       RECORD KEY IS MAST-KEY.
 DATA DIVISION.
 FILE SECTION.
 FD TRANSACTION-FILE.
 01 TRANSACTION-REC.          
       05 TRANS-NAME   PIC X(10).
       05 TRANS-CODE   PIC X(10).
 SD SORT-FILE.
 01 SORT-RECORD.
     05 SORT-KEY.
         10 SK-NAME          PIC X(8).
         10 SK-CODE          PIC X(1).
     05 SORT-DATA            PIC X(35).              
 FD AUDIT-REPORT.
    01 AUDIT-RECORD		   PIC X(80).
 FD MASTER-FILE.
    01 MAST-KEY.
       05 STOK-NAME       PIC X(8).
       05 MASTER-RECORD   PIC X(26).
 WORKING-STORAGE SECTION.
 COPY FDTRAN.
 COPY FDMAST.
 01 END-OF-FILE              PIC X VALUE SPACE.
    88 EOF-FLAG           VALUE "Y".
 01 HEADING-1.
	  05 FILLER  PIC X(80) VALUE "PROJECT 5 AUDIT REPORT".
 01 HEADING-2.
    05 FILLER  PIC X(80) VALUE "HEADING-2".
 01 DETAIL-LINE.
    05         PIC X(80) VALUE "DETAIL".
 01 TOTAL-LINE.
    05	     PIC X(80) VALUE "TOTAL".
 01 PROGRAM-SWITCHES.
	  05   RECORD-FOUND-SW   PIC X VALUE SPACE.   
 PROCEDURE DIVISION.
 MAINLINE.

     PERFORM 100-INITIALIZATION.
     PERFORM 200-PROCESSING.
     PERFORM 300-TERMINATION.

     STOP RUN.

 100-INITIALIZATION.
     DISPLAY "Project 5 start".
 110-ADD-A-RECORD.
 120-CHANGE-A-RECORD.
 130-DELETE-A-RECORD.
 200-PROCESSING.
     DISPLAY "Project 5 in progress".
     SORT SORT-FILE
         ASCENDING KEY SORT-KEY
         INPUT PROCEDURE 210-SORT-INPUT
         OUTPUT PROCEDURE 220-SORT-OUTPUT
         .
 210-SORT-INPUT.
     OPEN INPUT TRANSACTION-FILE
         PERFORM UNTIL EOF-FLAG
             READ TRANSACTION-FILE
                 INTO WS-TRANSACTION-RECORD
             AT END
                 SET EOF-FLAG TO TRUE
             NOT AT END
              	MOVE TRANS-NAME TO SK-NAME 
                  MOVE TRANS-CODE TO SK-CODE
  		MOVE TRANSACTION-REC TO SORT-DATA
             END-READ
         END-PERFORM
         CLOSE TRANSACTION-FILE
         .
 
 220-SORT-OUTPUT.
      MOVE N TO EOF-FLAG
      OPEN  OUTPUT AUDIT-REPORT
* format and write audit headings
      WRITE AUDIT-RECORD FROM HEADING-1 AFTER PAGE
      WRITE AUDIT-RECORD FROM HEADING-2 AFTER 2
      PERFORM UNTIL END-OF-FILE
      RETURN SORT-FILE
       AT END
       SET EOF-FLAG TO TRUE
       NOT AT END
       	MOVE SORT-DATA TO WS-TRANSACTION-RECORD
		MOVE TR-NAME TO MAST-KEY
		READ SORT-KEY
			INTO WS-MASTER-RECORD
		INVALID KEY
		    MOVE 'N' TO RECORD-FOUND-SW
		NOT INVALID KEY
		    MOVE 'Y' TO RECORD-FOUND-SW
          END-READ
       	EVALUATE TR-TRANS-CODE
		    WHEN "A" 
			IF RECORD-FOUND DISPLAY 'ERROR'
                  ELSE
			PERFORM 110-ADD-A-RECORD
		  WRITE MASTER-RECORD
			  FROM WS-MASTER-RECORD
			INVALID KEY
			MOVE 'N' TO RECORD-FOUND-SW
			NOT INVALID KEY
			MOVE 'Y' TO RECORD-FOUND-SW
		   END-WRITE
			END-IF.
*  ADD NOTES HERE
			WHEN "C" PERFORM 120-CHANGE-A-RECORD
*  HERE	
			WHEN "D" PERFORM 130-DELETE-A-RECORD
* HERE
			END-EVALUATE
			END-PERFORM
		      DISPLAY DETAIL-LINE
             CLOSE AUDIT-REPORT.
 300-TERMINATION.
     DISPLAY "Project 5 complete".
```

#### ↳ Re: cobol help please

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-05-11T22:24:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eEZK6.29688$ho6.1640437@news5.aus1.giganews.com>`
- **References:** `<20010511112231.13807.00003452@ng-cj1.aol.com>`

```
Made a couple of corrections.

In my view, nested read-write-return-rewrite-etc., code is not much
different from nested IF statements; hard to read, hard to fix.

For example, your snippet:

>       RETURN SORT-FILE
>        AT END
…[23 more quoted lines elided]…
> END-IF.

Could be rewritten as:

PERFORM MYSORT-RETURN UNTIL END-OF-FILE.

MYSORT-RETURN.
   RETURN SORT-FILE
      AT END MOVE 'Y' TO END-OF-FILE
      NOT AT END
         PERFORM MYSORT-IN.
MYSORT-IN.
   MOVE SORT-DATA TO WS-TRANSACTION-RECORD.
   MOVE TR-NAME TO MAST-KEY.
   PERFORM MYGET-MASTER.
MYGET-MASTER.
   READ MASTER-FILE
      INVALID KEY PERFORM MYGET-MASTER-NOJOY
      NOT INVALID KEY PERFORM MYGET-MASTER-JOY
      END-READ.
MYGET-MASTER-NOJOY.
   DISPLAY 'ERROR'.
MYGET-MASTER-JOY.
   etc.

This technique, in my experience, is easier to understand and easier
to add processing statments such as formatting a screen instead of
DISPLAY "ERROR"

Just my three cents.

"Deek163" <deek163@aol.com> wrote in message
news:20010511112231.13807.00003452@ng-cj1.aol.com...
> This is what i have done so far could somebody please scan for major
errors, i
> have a few that i cant seem to solve here is my code. BTW i know its
far from
> done.
>
…[89 more quoted lines elided]…
>                  SET EOF-FLAG TO TRUE        *** MOVE 'Y' TO
END-OF-FILE
>              NOT AT END
>               MOVE TRANS-NAME TO SK-NAME
…[52 more quoted lines elided]…
>
```

#### ↳ Re: cobol help please

- **From:** Stephen J Spiro <donotreply@interbulletin.bogus>
- **Date:** 2001-05-12T02:01:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AFC998E.7274B51A@interbulletin.com>`
- **References:** `<20010511112231.13807.00003452@ng-cj1.aol.com>`

```
deek163@aol.com (Deek163) wrote: 
>This is what i have done so far could somebody please scan for major errors, i
>have a few that i cant seem to solve here is my code. BTW i know its far from
…[98 more quoted lines elided]…
>         CLOSE TRANSACTION-FILE.
------------------------------------

First, you are moving the TRANSACTION-FILE record to WORKING-STORAGE, (presumably in FDTRAN). Nevertheless, you use the data names in the FD as the source of your MOVE instructions.
Second, these fields are each 10 bytes long in the source, but 8 and 1 bytes in the target record. Is this correct?
Third, having moved truncated values into the sort key, you then take the same 20 bytes, and move it into the 35 byte data area of the sort key. Is this correct?  It is inefficient to build a sort record larger than you need.
Fourth, you need a RELEASE SORT-RECORD statement before the END-PERFORM.
Fifth, I recommend against AT END ... NOT AT END.  If you use File Statuses (and you CAN use File Statuses with sequential files), you can do a structured test. Not only that, you do not need a separate end-of-file flag; the file status IS the end-of-file flag! And you do not have to test explicitly for end-of-file, the PERFORM statement will do that for you!:

     PERFORM UNTIL EOF-FLAG
*       If you make this an 88-level on the TRAN-RETURN-CODE, otherwise
     PERFORM UNTIL TRAN-RETURN-CODE IS EQUAL TO '10' 
     -
     - 
     IF TRAN-RETURN-CODE IS EQUAL TO ZERO
	 MOVE TRANS-NAME TO SK-NAME 
         MOVE TRANS-CODE TO SK-CODE 
  	 MOVE TRANSACTION-REC TO SORT-DATA
     ELSE
     IF TRAN-RETURN-CODE IS NOT EQUAL TO '10'
         PERFORM ERROR-ROUTINE
     -
     -
     END-PERFORM.

One of the reasons I do not like AT END .... NOT AT END is because, in a production environment, you will be expected to check for a bad READ. NOT AT END assumes a good READ.  If you get a return code of '04' or something, you will fall thru and corrupt everything until you (possibly) ABEND.

------------------------------------------
 
> 220-SORT-OUTPUT.
>      MOVE N TO EOF-FLAG
…[42 more quoted lines elided]…
>
---------------------

There are other problems with the program; you should try to resolve all of your error messages before you ask for help.  You should not ask for help until all of your syntax errors have been resolved.  THEN, we can help you with the logic errors.
-----------------------

Stephen J Spiro
Member, J4


_______________________________________________
Submitted via WebNewsReader of http://www.interbulletin.com
```

#### ↳ Re: cobol help please

- **From:** foodman123 <nospam@newsranger.com>
- **Date:** 2001-05-12T13:32:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dYaL6.2684$j65.209964@www.newsranger.com>`
- **References:** `<20010511112231.13807.00003452@ng-cj1.aol.com>`

```
In article <20010511112231.13807.00003452@ng-cj1.aol.com>, Deek163 says...
>
>This is what i have done so far could somebody please scan for major errors, i
>have a few that i cant seem to solve here is my code. BTW i know its far from
>done.

Hi:

Your messages, as above, seem to always disregard conventions regarding
grammar, punctuation, capitalization and composition. This undesirable
trait may carry over into your programming. . .

For example:

>     SELECT AUDIT-REPORT
>	       ASSIGN TO "A:\ADUIT.TXT".


Convention would dictate that a level 01 in an FD would be a record name.
I would hope that a key to a file would not be the entire record. It is 
illogical that a record would be part of a key.

> FD MASTER-FILE.
>    01 MAST-KEY.
>       05 STOK-NAME       PIC X(8).
>       05 MASTER-RECORD   PIC X(26).

If you are going to be a COBOL programmer, you must strive for uncompromising
accuracy and clarity in the DATA DIVISION. Poorly designed records and W-S
items will lead to poorly coded and misleading code in the PROCEDURE DIVISION.

Since I despise structured programming, I will not comment on the rest of it.

Thanks

Tony Dilworth
```

##### ↳ ↳ Re: cobol help please

- **From:** deek40@aol.com (Deek40)
- **Date:** 2001-05-14T04:23:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010514002322.03354.00003372@ng-mp1.aol.com>`
- **References:** `<dYaL6.2684$j65.209964@www.newsranger.com>`

```
SORRY ABOUT THE GRAMMER ERRORS, BUT I AM WORKING A FULL TIME JOB AND TRYING TO
DO THIS PROGRAM ITS NOT EASY WORKING 40 HOURS A WEEK, BEING A FULL TIME STUDENT
AND TRYING TO WRITE A PROGRAM ON TOP OF TRYING TO GET MORE THAN 3 HOURS OF
SLEEP A NIGHT.  THANKS FOR YOUR ADVICE THOUGH.  JUST ONE QUESTION HOW DO U
PROGRAM COBOL WITH OUT STRUCTURE AND WHY WOULD TEACHERS STRESS STRUCTURED
PROGRAMMING IF ITS NOT IMPORTANT WITH COBOL?

DeEk
```

###### ↳ ↳ ↳ Re: cobol help please

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2001-05-14T05:35:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-FHGSdGd1qhiW@24-108-102-82.ivideon.com>`
- **References:** `<dYaL6.2684$j65.209964@www.newsranger.com> <20010514002322.03354.00003372@ng-mp1.aol.com>`

```
On Mon, 14 May 2001 04:23:22, deek40@aol.com (Deek40) wrote:

> SORRY ABOUT THE GRAMMER ERRORS, BUT I AM WORKING A FULL TIME JOB AND TRYING TO
> DO THIS PROGRAM ITS NOT EASY WORKING 40 HOURS A WEEK, BEING A FULL TIME STUDENT
…[5 more quoted lines elided]…
> DeEk

Use lots of little paragraphs in your procedure division and use
condition tests to GO TO a paragraph to do some small piece
of work... and then GO TO some other  paragraph to do another
small bit .............. skipping around all over the place.

Structured programming is always important in any programming 
language. 
```

###### ↳ ↳ ↳ Re: cobol help please

- **From:** Stephen J Spiro <donotreply@interbulletin.bogus>
- **Date:** 2001-05-15T05:37:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B00C084.3EB9474B@interbulletin.com>`
- **References:** `<dYaL6.2684$j65.209964@www.newsranger.com> <20010514002322.03354.00003372@ng-mp1.aol.com>`

```
deek40@aol.com (Deek40) wrote in article 
<SORRY ABOUT THE GRAMMER ERRORS, BUT I AM WORKING A FULL TIME JOB AND TRYING TO
>DO THIS PROGRAM ITS NOT EASY WORKING 40 HOURS A WEEK, BEING A FULL TIME STUDENT
>AND TRYING TO WRITE A PROGRAM ON TOP OF TRYING TO GET MORE THAN 3 HOURS OF
…[4 more quoted lines elided]…
>DeEk

If you don't write very carefully structured, modular programs, I will not hire you.  And neither will any other manager worth his salary.

Stephen J Spiro
Wizard Systems

_______________________________________________
Submitted via WebNewsReader of http://www.interbulletin.com
```

###### ↳ ↳ ↳ Re: cobol help please

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-05-15T16:19:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rGcM6.61840$ho6.3789899@news5.aus1.giganews.com>`
- **References:** `<dYaL6.2684$j65.209964@www.newsranger.com> <20010514002322.03354.00003372@ng-mp1.aol.com>`

```
Keyboards fixed: $12
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
