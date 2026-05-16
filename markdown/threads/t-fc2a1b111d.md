[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# confused

_3 messages · 3 participants · 2000-10_

---

### confused

- **From:** deek40@aol.com (Deek40)
- **Date:** 2000-10-31T04:20:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20001030232037.02372.00000624@ng-fh1.aol.com>`

```
I am so discouraged with COBOL right now i cant get this program to work right
i have been working on it for like 2 months now and i just hit a brick wall,
this is for a class and it should display 9 records , the title line and end of
proj 4 well i got the title line and proj 4 part but i cant get the records to
display please help.  here is my code.
thanks deek
 IDENTIFICATION DIVISION.
 PROGRAM-ID. proj4.
 
*************************************************************************
* Purpose:  Enhance Project 3 by defining display lines in WORKING-STORAGE 
*            and editing the numeric inventory quantities. 
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
 		ASSIGN TO "A:\Proj2\Invntory.DAT"
		ORGANIZATION LINE SEQUENTIAL
		ACCESS	     SEQUENTIAL.

 DATA DIVISION.
 FILE SECTION.
 FD  INVENTORY-FILE
     RECORD CONTAINS 80 CHARACTERS.
 01 INVENTORY-RECORD.
	  03 IR-ITEM-NBR		PIC X(08).
	  03 IR-ITEM-DESCRIPTION	PIC X(30).
	  03 IR-QTY-ON-HAND             PIC S9(7)	 
                                  SIGN TRAILING SEPARATE.
    03 IR-QTY-ON-ORDER		PIC S9(7)
    				SIGN TRAILING SEPARATE.
    03 IR-REORDER-POINT           PIC S9(7)
                                  SIGN TRAILING SEPARATE.
    03 IR-UNIT-COST		PIC S9(5)V9(4)
                                  SIGN TRAILING SEPARATE.
    03 IR-UNIT-OF-MEASURE         PIC X(02).
    03 FILLER			PIC X(06).
    
 WORKING-STORAGE SECTION.
 01 TITLE-LINE			PIC X(79)
	   VALUE 'PROJECT 4 - Display Inventory Items to Reorder'.
 01 DETAIL-LINE.
 	  03 DL-ITEM-NUM	        PIC  X(08)  VALUE SPACES.
    03 FILLER   		        PIC  X(02)  VALUE SPACES.
    03 DL-ITEM-DESC		PIC  X(30)  VALUE SPACES.
	  03 FILLER			PIC  X(6)   VALUE SPACES. 
	  03 DL-QTY-ON-HAND    	  	PIC  Z(6)9- VALUE ZEROS.
    03 FILLER			PIC  X(4)   VALUE SPACES.
    03 DL-REORDER-PT		PIC  Z(6)9- VALUE ZEROS.
    03 FILLER			PIC  X(7)   VALUE SPACES.
    03 DL-QTY-TO-REORDER		PIC  Z(6)9- VALUE ZEROS.  
 01 EOF-FLAG		        PIC  X(01)  VALUE SPACE.  
 
 
 01 WS-QTY-TO-REORDER	        PIC S9(7)  
					SIGN TRAILING SEPARATE.
 PROCEDURE DIVISION.
 MAINLINE.
     PERFORM 100-INITIALIZATION

     PERFORM 200-PROCESSING

     PERFORM 300-TERMINATION

	   STOP RUN.

 100-INITIALIZATION.
     DISPLAY TITLE-LINE.
 
 200-PROCESSING.
     
   
     OPEN INPUT INVENTORY-FILE
     MOVE IR-ITEM-NBR
			TO DL-ITEM-NUM
	   MOVE IR-ITEM-DESCRIPTION
 			TO DL-ITEM-DESC
	   MOVE IR-QTY-ON-HAND
			TO DL-QTY-ON-HAND
	   MOVE IR-REORDER-POINT
			TO DL-REORDER-PT
	   MOVE IR-QTY-ON-ORDER
			TO DL-QTY-TO-REORDER.
     DISPLAY DETAIL-LINE
     PERFORM UNTIL EOF-FLAG = 'Y'
         READ INVENTORY-FILE
	       AT END
		   MOVE 'Y' TO EOF-FLAG
         NOT AT END
             IF IR-QTY-ON-HAND < IR-REORDER-POINT
		      COMPUTE IR-QTY-ON-ORDER  =
			IR-REORDER-POINT - IR-QTY-ON-HAND  
             END-IF
	       END-READ
	   END-PERFORM.

 300-TERMINATION.
	   
     CLOSE INVENTORY-FILE

	   DISPLAY ' '
	   DISPLAY 'End of program Project 4.'
	   .
```

#### ↳ Re: confused

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-31T05:11:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39fe5419.35935218@207.126.101.100>`
- **References:** `<20001030232037.02372.00000624@ng-fh1.aol.com>`

```
Let me share my quick observations.

Look down in the code below.

On 31 Oct 2000 04:20:37 GMT, deek40@aol.com (Deek40) wrote:

>I am so discouraged with COBOL right now i cant get this program to work right
>i have been working on it for like 2 months now and i just hit a brick wall,
…[82 more quoted lines elided]…
>     OPEN INPUT INVENTORY-FILE

---> There won't be any data here because you have not read a record
yet.

>     MOVE IR-ITEM-NBR
>			TO DL-ITEM-NUM
…[8 more quoted lines elided]…
>     DISPLAY DETAIL-LINE

--- The above display will show nothing, nothing has been read.

>     PERFORM UNTIL EOF-FLAG = 'Y'
>         READ INVENTORY-FILE
>	       AT END
>		   MOVE 'Y' TO EOF-FLAG
>         NOT AT END

---> now we are in the read loop, but no move and display!

--->> move your move and display logic to here, and I think you will
have a better shot at it working.

>             IF IR-QTY-ON-HAND < IR-REORDER-POINT
>		      COMPUTE IR-QTY-ON-ORDER  =
…[15 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: confused

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-31T07:17:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FED472.44BCEFB5@brazee.net>`
- **References:** `<20001030232037.02372.00000624@ng-fh1.aol.com>`

```
Two months?

Usually OPEN commands go in the initialization, just as you have your CLOSE in your
termination.

Then usually we perform the main routine until EOF.  You actually have your perform
loop within your main routine - but you display your output BEFORE you enter that
loop.  You haven't read anything yet.  Then when and after you read your records,
you never display anything.  Why bother reading all of those records if you never
display anything from them?

When you are not getting results, take a pencil and paper and pretend you are a
computer.  Do everything the CoBOL tells the computer to do.  When it says READ,
write the read results next to the fields you read into.  When it says compute, put
the computed result next to the field name you computed.  You should get the same
results the computer does - but with a better understanding of why, and what you
should change.

Deek40 wrote:

> I am so discouraged with COBOL right now i cant get this program to work right
> i have been working on it for like 2 months now and i just hit a brick wall,
…[114 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
