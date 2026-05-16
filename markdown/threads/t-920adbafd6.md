[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Confused with Two-Level Table Program

_4 messages · 3 participants · 2003-09_

---

### Confused with Two-Level Table Program

- **From:** mikey@mailbox.co.za (Michael)
- **Date:** 2003-09-01T03:31:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cddb7f2.0309010231.54e77e9d@posting.google.com>`

```
Hi, I was wondering if any of you could help me...I'm busy with a
crash-course in Cobol now after I failed the inital course

I'm completely confused with a two-level table program I have to
write...I don't know how to get the values out of the input file and
into the two-level table.  I know I have to do a search, but because
of the way the input file is structured I'm really confused....

I've included the program specifications, my code and the input
files...
My code is a mess..

If you could help in anway I'd really appreciate it..


Project 1
Description:
Write a program to determine whether a customer receives a discount
based on quantity ordered, and calculate the discounted unit price and
total discounted price. Create a report that prints each customer's
order, as well as the total quantity ordered and total sales for the
company. A summary must be included at the end of the report listing
the Item Series as well as the total discount for the series.
Input (Pr1Sales.dat):
01	IN-ORDER-TRANSACTION.
	05	IN-CUST-NUM		PIC 9(8).
	05	IN-QTY-ORDERED		PIC 9(3).
	05	IN-ITEM-NUMBER		PIC X(5).
	05	IN-UNIT-PRICE		PIC 9(3)V99.
Report Layout
Austin Retail Company

CUSTOMER	ITEM	QTY	UNIT	DISCOUNTED
NUMBER	NUMBER	ORDERED	PRICE	PRICE
				
XXXXXXXX	XXXXX	999	R999.99	R999.99
				

Summary

PRODUCT SERIES	TOTAL DISCOUNT
X	R9999999.99
	

 
Processing
1.	Read the file of order records.
2.	For every record read:
a.	Determine whether the customer will receive a discount. The
discounting of an item is based on the Item Series and Quantity
Ordered. The Item Series is the first character of the Item Number.
For example, Item Number 12345 is Item Series 1, and P3764 is Series
P, and so forth.
The discount is further determined by the quantity ordered. For
example, if a customer buys 0 - 10 units of Series 1, he/she will
receive 10% discount. For 11 - 50 units, he/she will receive 20%
discount.
A file is available (Pr1Disc.dat) containing the discount values in
the following format:
01	IN-DISCOUNT.
	05	DC-ITEM-SERIES		PIC X.
	05	DC-VALUES
		OCCURS 4 TIMES.
		10	NUM-ITEMS		PIC 999.
		10	DISCOUNT		PIC 99.	
This file needs to be read into a two-dimensional table at start-up,
and referred to during processing to get the discounts.
b.	Print the customer number, item number, quantity ordered, the
original unit price, and the discounted unit price.
c.	Update the summary by adding the Item Series (if it does not
already exist), and add the customer's discount to the total discount.
The summary table must be a variable length table with a maximum of 10
items.
d.	Update the Total Quantity Ordered and Total Discount for the
company.
3.	Print the company totals for Total Quantity Ordered and Total
Discount.
4.	Print the summary. 





000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID.  OP201SRT.
000030 AUTHOR.      MICHAEL.
000040 DATE-WRITTEN.  AUGUST 2003.
000050 ENVIRONMENT DIVISION.
000060 INPUT-OUTPUT SECTION.
000070 FILE-CONTROL.
000080     SELECT SALES-FILE ASSIGN TO DISK 'A:\PR1SALES.DAT'
000090            ORGANIZATION IS LINE SEQUENTIAL.
000100     SELECT DISCOUNT-FILE ASSIGN TO DISK 'A:\PR1DISC.DAT'
000110     SELECT PRINT-FILE  ASSIGN TO PRINTER 'CON'.
000120     
000130 DATA DIVISION.
000140 FILE SECTION.
000150
000160 
000170 FD  SALES-FILE
000180     RECORD CONTAINS 23 CHARACTERS
000190     DATA RECORD IS IN-ORDER-TRANSACTION.
000200     
000210 01  IN-ORDER-TRANSACTION
000220 
000230     05  IN-CUST-NUM	       PIC 9(8).
000240     05  IN-QTY-ORDERED	       PIC 9(3).
000250     05  IN-ITEM-NUMBER.
000260	       10  IN-SERIES	       PIC X.
000270	       10  IN-NUMBER	       PIC X(4).
000280	   05  IN-UNIT-PRICE	       PIC X(5).
000290
000300 
000310 FD  DISCOUNT-FILE
000320
000330     RECORD CONTAINS 20 CHARACTERS
000340	   DATA RECORD IS IN-DISCOUNT.
000350
000360 01  IN-DISCOUNT.
000370
000380	05	DC-ITEM-SERIES			PIC X.
000390	05	DC-VALUES OCCURS 4 TIMES.
000400  	10	NUM-ITEMS		PIC 999.
000410		10	DISCOUNT		PIC 99.
000420
000430   
000440   
000450                  
000460 FD  PRINT-FILE
000470     RECORD CONTAINS 80 CHARACTERS
000480     DATA RECORD IS PRINT-LINE.
000490     
000500 01  PRINT-LINE                PIC X(80).
000510 
000520    
000530 WORKING-STORAGE SECTION.    
000540
000550 
000560 01  PROGRAM-SWITCHES-AND-COUNTERS.
000570 
000580     05  PAUSE                   PIC X.
000590     05  END-OF-FILE             PIC X(3) VALUE 'NO'.
000600         88 END-FILE                      VALUE 'YES'.
000610     05  END-OF-DISCOUNT-FILE     PIC X(3) VALUE 'NO'.
000620         88 END-DISCOUNT-FILE              VALUE 'YES'.
000630    
000640  
000650
000660 
000670 01  DISCOUNT-TABLE.
000680 
000690     05  DISC-DETAILS OCCURS 8 TIMES INDEXED BY DISC-INDEX.
000700  	10  DISC-VALUES OCCURS 4 TIMES INDEXED BY VALUE-INDEX
000710  		15	D-NUM-ITEMS	PIC 999.
000720  		15 	D-DISCOUNT	PIC 99.
000730 
000740
000750 01  HDG-LINE-ONE		      
000760			      PIC X(15) VALUE SPACES.
000770			      PIC X(21) VALUE 'AUSTIN RETAIL COMPANY'
000780  
000790
000800       
000810 01  HDG-LINE-TWO.
000820 
000830     05                  PIC X(5)  VALUE SPACES.
000840     05                  PIC X(8)  VALUE 'CUSTOMER'. 
000850     05 			PIC X(5)  VALUE SPACES.
000860			       PIC X(4)  VALUE 'ITEM'.
000870			       PIC X(5)  VALUE SPACES.
000880			       PIC X(3)  VALUE 'QTY'.
000890			       PIC X(5)  VALUE SPACES.
000900			       PIC X(4)  VALUE 'UNIT'.
000910     05		               PIC X(10) VALUE 'DISCOUNTED'
000920         
000930 01  HDG-LINE-THREE.
000940 
000950     05                  PIC X(7)  VALUE SPACES.
000960     05                  PIC X(6)  VALUE 'NUMBER'.
000970     05                  PIC X(4)  VALUE SPACES.
000980     05  		       PIC X(6)  VALUE 'NUMBER'.
000990			       PIC X(3)  VALUE SPACES.
001000			       PIC X(7)  VALUE 'ORDERED'.
001010			       PIC X(3)  VALUE SPACES.
001020			       PIC X(5)  VALUE 'PRICE'
001030			       PIC X(8)  VALUE SPACES.
001040			       PIC X(5)  VALUE 'PRICE'.
001050
001060 
001070
001080     
001090 01  DETAIL-LINE.
001100 
001110     05                          PIC X(5)       VALUE SPACES.
001120     05 DET-CUST-NUMBER          PIC 9(8).
001130     05                          PIC X(3)       VALUE SPACES.
001140     05 DET-ITEM-NUMBER          PIC X(5).
001150     05 		               PIC X(3)       VALUE SPACES.
001160     05 DET-QTY-ORDERED	       PIC 999.
001170	   05			       PIC X(2)	      VALUE SPACES.
001180	   05 DET-UNIT-PRICE	       PIC $9(3)V99.
001190	   05 			       PIC X(3)       VALUE SPACES.
001200	   05 DET-DISC-PRICE	       PIC $9(3)V99
001210     
001220      
001230     
001240 PROCEDURE DIVISION.
001250 	   PERFORM INITIALIZATION.
001260     PERFORM PROCESS-RECORDS UNTIL END-FILE. 
001270     PERFORM TERMINATION.
001280     STOP RUN.
001290    
001300
001310****************
001320INITIALIZATION.     
001330     OPEN INPUT    SALES-FILE
001340			 DISCOUNT-FILE
001350          OUTPUT   PRINT-FILE.
001360     ACCEPT WS-DATE FROM DATE.
001370     PERFORM WRITE-HEADING-LINES.
001380     PERFORM LOAD-DISCOUNT-TABLE
001390	   CLOSE 	 DISCOUNT-FILE. 
001400
001410
001420AD-TABLE.
001430*************
001440
001450LOAD-DISCOUNT-TABLE.
001460     PERFORM Z-READ-DISCOUNT
001470     PERFORM LOAD-DISCOUNTS VARYING DISC-INDEX 
001480             FROM 1 BY 1 UNTIL DISC-INDEX > 8
001490             AFTER VALUE-INDEX FROM 1 BY 1 UNTIL VALUE-INDEX > 4
001500      	   OR END-DISCOUNT
001510     IF NOT END-DISCOUNT
001520        DISPLAY 'DISCOUNT TABLE TOO SMALL -RECOMPILE'
001530        DISPLAY 'RUN TERMINATING'
001540        STOP RUN.
001550        
001560 LOAD-DISCOUNTS.
001570     MOVE DC-VALUES TO DISC-VALUES(DISC-INDEX VALUE INDEX)
001580     PERFORM Z-READ-DISCOUNT.
001590
001600PROCESS-RECORDS.
001610     PERFORM SEARCH-DISCOUNT     
001620

001680 SEARCH-DISOUNT.
001690*****************
001700SET DISC-INDEX TO 1.
001710SET VALUE-INDEX TO 1
001720     SEARCH DISC-DETAILS
001730       AT END 
001740         MOVE 'UNKNOWN ' TO 
001750       WHEN DC-ITEM-SERIES = IN-SERIES
001760		PERFORM GET-DISCOUNT
001770		PERFORM CALCULATE-DISCOUNT      
001780		MOVE IN-CUST-NUM TO DET-CUST-NUM
001790 		MOVE IN-ITEM-NUMBER TO DET-ITEM-NUMBER
001800 		MOVE IN-QTY-ORDERED TO DET-QTY-ORDERED
001810 		MOVE IN-UNIT-PRICE TO DET-UNIT-PRICE
002760      
002770 READ-DISCOUNT.
002780**************
002790     READ DISCOUNT-FILE
002800       AT END 
002810         MOVE 'YES' TO END-OF-DISCOUNT-FILE.
002820     
002830                       
002840 PRINT-HEADINGS.
002850*****************
002860     WRITE PRINT-LINE FROM HDG-LINE-ONE AFTER 1.
002870     WRITE PRINT-LINE FROM HDG-LINE-TWO AFTER 2.
002880     WRITE PRINT-LINE FROM HDG-LINE-THREE.
002890     WRITE PRINT-LINE FROM HDG-LINE-FOUR.
002900     WRITE PRINT-LINE FROM HDG-LINE-FIVE.
002910     WRITE PRINT-LINE FROM SPACES.
002920        

INPUT FILES:

pr1sales.dat:

513472530501459312385
65543588055G265623536
453451050671156865239
45654654078P135816666
54654654420G456873331
232132151027265203600
879456450063663608700
546868750010666610500
54654666099P166635508
42686688169G730039912
546565480440365112609
878666783178166800999
876944440188933105899
133298970764554609977

pr1disc.dat:

102510100202503099940
G03010050201503099940
P00515020201003099945
706005100305003399937
310003300105004099955
025013500337503599937
800919090251804099945
450020750158002099950
```

#### ↳ Re: Confused with Two-Level Table Program

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-09-01T14:44:20+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2c6lv8m4td6l9et17rtsq5rni68rc3i3t@4ax.com>`
- **References:** `<5cddb7f2.0309010231.54e77e9d@posting.google.com>`

```
On 1 Sep 2003 03:31:55 -0700 mikey@mailbox.co.za (Michael) wrote:

:>Hi, I was wondering if any of you could help me...I'm busy with a
:>crash-course in Cobol now after I failed the inital course

:>I'm completely confused with a two-level table program I have to
:>write...I don't know how to get the values out of the input file and
:>into the two-level table.  I know I have to do a search, but because
:>of the way the input file is structured I'm really confused....

:>I've included the program specifications, my code and the input
:>files...
:>My code is a mess..

One would have greater belief of your effort if the code you supplied
compiled. That you should be able to do with little help, or have specific
questions about the compiler errors received.

Your load table will not work properly.

Should you manage to get a clean compile, it would be advisable to display the
table to confirm that the data was loaded properly.
```

##### ↳ ↳ Re: Confused with Two-Level Table Program

- **From:** mikey@mailbox.co.za (Michael)
- **Date:** 2003-09-21T09:33:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cddb7f2.0309210833.ff4d213@posting.google.com>`
- **References:** `<5cddb7f2.0309010231.54e77e9d@posting.google.com> <g2c6lv8m4td6l9et17rtsq5rni68rc3i3t@4ax.com>`

```
Hi, I compiled my code in Fujitsu 3.0, but I'm really not sure how to
accumulate the summary table and print from the summary table...



000010 IDENTIFICATION DIVISION.
000020 PROGRAM-ID.  OP201SRT.
000030 AUTHOR.      MICHAEL.
000040 DATE-WRITTEN.  AUGUST 2003.
000050 ENVIRONMENT DIVISION.
000060 INPUT-OUTPUT SECTION.
000070 FILE-CONTROL.
000080     SELECT SALES-FILE ASSIGN TO 'A:\PR1SALES.DAT'
000090            ORGANIZATION IS LINE SEQUENTIAL.
000100     SELECT DISCOUNT-FILE ASSIGN TO 'A:\PR1DISC.DAT'
000101		    ORGANIZATION IS LINE SEQUENTIAL.
000111	   SELECT PRINT-FILE  ASSIGN TO 'A:\REPORT.DOC'.
000120     
000130 DATA DIVISION.
000140 FILE SECTION.
000150
000160 
000170 FD  SALES-FILE
000180     RECORD CONTAINS 23 CHARACTERS
000190     DATA RECORD IS IN-ORDER-TRANSACTION.
000200     
000210 01  IN-ORDER-TRANSACTION.
000220 
000230     05  IN-CUST-NUM	       PIC 9(8).
000240     05  IN-QTY-ORDERED	       PIC 9(3).
000250     05  IN-ITEM-NUMBER.
000260	       10  IN-SERIES	       PIC X.
000270	       10  IN-NUMBER	       PIC X(4).
000280	   05  IN-UNIT-PRICE	       PIC 9(5).
000290
000300 
000310 FD  DISCOUNT-FILE
000320
000330     RECORD CONTAINS 21 CHARACTERS
000340	   DATA RECORD IS IN-DISCOUNT.
000350
000360 01  IN-DISCOUNT.
000370
000380	05	DC-ITEM-SERIES			PIC X.
000390	05	DC-VALUES OCCURS 4 TIMES.
000400  	10	NUM-ITEMS		PIC 999.
000410		10	DISCOUNT		PIC 99.
000420
000430   
000440   
000450                  
000460 FD  PRINT-FILE
000470     RECORD CONTAINS 80 CHARACTERS
000480     DATA RECORD IS PRINT-LINE.
000490     
000500 01  PRINT-LINE                PIC X(80).
000510 
000520    
000530 WORKING-STORAGE SECTION.    
000540
000550 
000560 01  PROGRAM-SWITCHES-AND-COUNTERS.
000570 
000580     05  PAUSE                   		 PIC X.
000590     05  END-OF-SALES-FILE             	 PIC X(3) VALUE 'NO'.
000600         88 END-SALES-FILE                      VALUE 'YES'.
000610     05  END-OF-DISCOUNT-FILE     	 PIC X(3) VALUE 'NO'.
000620         88 END-DISCOUNT-FILE              VALUE 'YES'.
000630     05  WS-DISCOUNTED-AMT		 PIC 9(6)V99.
000631	   05  WS-DISCOUNT			 PIC 99.
000640     05  WS-DISCOUNT-AMT			 PIC 9(6)V99.
000641	   05  WS-TOTAL-QTY-ORDERED		 PIC 9(6)V99.
000642	   05  WS-TOTAL-DISC-AMT		 PIC 9(6)V99.
000643     05  WS-DATE				 PIC 9(4).
000644	   05  SUM-NO				 PIC 9.
000650
000660 
000670 01  DISCOUNT-TABLE.
000680 
000690     05  DISC-DETAILS OCCURS 8 TIMES INDEXED BY DISC-INDEX.
000691          10  DISC-SERIES	                PIC X.
000700  	10  DISC-VALUES OCCURS 4 TIMES INDEXED BY VALUE-INDEX.
000710  		15	D-NUM-ITEMS	PIC 999.
000720  		15 	D-DISCOUNT	PIC 99.
000721
000722 01  SUMMARY-TABLE.
000723	  
000724	   05	SUMMARY-NO			PIC 9	VALUE ZERO.
000725	   05	SUMMARY-ENTITY OCCURS 0 TO 8 TIMES
000726		DEPENDING ON SUM-NO
000727		INDEXED BY SUM-INDEX.	
000728		10	SUM-SERIES		PIC X.
000729		10	SUM-DISCOUNT		PIC 99. 
000730
000731
000732 
000740
000750 01  HDG-LINE-ONE.		      
000760			      
000761	   05		      PIC X(15) VALUE SPACES.
000770	   05		      PIC X(21) VALUE 'AUSTIN RETAIL COMPANY'.
000780  
000790
000800       
000810 01  HDG-LINE-TWO.
000820 
000830     05                  PIC X(5)  VALUE SPACES.
000840     05                  PIC X(8)  VALUE 'CUSTOMER'. 
000850     05 		       PIC X(5)  VALUE SPACES.
000860	   05		       PIC X(4)  VALUE 'ITEM'.
000870	   05		       PIC X(5)  VALUE SPACES.
000880	   05		       PIC X(3)  VALUE 'QTY'.
000890	   05		       PIC X(5)  VALUE SPACES.
000900	   05		       PIC X(4)  VALUE 'UNIT'.
000910     05		       PIC X(10) VALUE 'DISCOUNTED'.
000920         
000930 01  HDG-LINE-THREE.
000940 
000950     05                  PIC X(7)  VALUE SPACES.
000960     05                  PIC X(6)  VALUE 'NUMBER'.
000970     05                  PIC X(4)  VALUE SPACES.
000980     05  		       PIC X(6)  VALUE 'NUMBER'.
000990	   05		       PIC X(3)  VALUE SPACES.
001000	   05		       PIC X(7)  VALUE 'ORDERED'.
001010     05		       PIC X(3)  VALUE SPACES.
001020	   05     	       PIC X(5)  VALUE 'PRICE'.
001030     05		       PIC X(8)  VALUE SPACES.
001040	   05		       PIC X(5)  VALUE 'PRICE'.
001050
001060 
001070
001080     
001090 01  DETAIL-LINE.
001100 
001110     05                          PIC X(5)       VALUE SPACES.
001120     05 DET-CUST-NUM             PIC 9(8).
001130     05                          PIC X(3)       VALUE SPACES.
001140     05 DET-ITEM-NUMBER          PIC X(5).
001150     05 		               PIC X(3)       VALUE SPACES.
001160     05 DET-QTY-ORDERED	       PIC 999.
001170	   05			       PIC X(2)	      VALUE SPACES.
001180	   05 DET-UNIT-PRICE	       PIC $9(3)V99.
001190	   05 			       PIC X(3)       VALUE SPACES.
001200	   05 DET-DISC-PRICE	       PIC $9(3)V99.
001210                             
001220      
001230     
001240 PROCEDURE DIVISION.
001250 	   PERFORM INITIALIZATION.
001260     PERFORM PROCESS-RECORDS UNTIL END-SALES-FILE. 
001280     STOP RUN.
001290    
001300
001310****************
001320 INITIALIZATION.     
001330     OPEN INPUT    SALES-FILE
001340			 DISCOUNT-FILE
001350          OUTPUT   PRINT-FILE.
001360     ACCEPT WS-DATE FROM DATE.
001370     PERFORM PRINT-HEADINGS.
001371	   PERFORM READ-DISCOUNT.
001380     PERFORM LOAD-DISCOUNTS
001381         VARYING DISC-INDEX FROM 1 BY 1
001382		UNTIL DISC-INDEX > 8 OR END-DISCOUNT-FILE. 
001390	   CLOSE 	 DISCOUNT-FILE. 
001400     PERFORM READ-SALES.
001410
001450        
001560 LOAD-DISCOUNTS.
001570     MOVE IN-DISCOUNT TO DISC-DETAILS(DISC-INDEX)
001580     PERFORM READ-DISCOUNT.
001590
001600 PROCESS-RECORDS.
001610     PERFORM SEARCH-DISCOUNT     
001620     MOVE IN-CUST-NUM TO DET-CUST-NUM.
001621 	   MOVE IN-ITEM-NUMBER TO DET-ITEM-NUMBER.
001622     MOVE IN-QTY-ORDERED TO DET-QTY-ORDERED.
001623 	   MOVE IN-UNIT-PRICE TO DET-UNIT-PRICE.
001630     MOVE WS-DISCOUNTED-AMT TO DET-DISC-PRICE.
001631     WRITE PRINT-LINE FROM DETAIL-LINE. 
001640     ADD IN-QTY-ORDERED TO WS-TOTAL-QTY-ORDERED.
001641	   ADD WS-DISCOUNTED-AMT TO WS-TOTAL-DISC-AMT.
001642	   PERFORM ADD-TO-SUMMARY.
001643	   PERFORM READ-SALES.
001660
001670		  
001680 SEARCH-DISCOUNT.
001690*****************
001700     SET DISC-INDEX TO 1.
001710     SEARCH DISC-DETAILS
001730       AT END 
001740         MOVE 0 TO WS-DISCOUNT 
001750       WHEN IN-SERIES = DISC-SERIES(DISC-INDEX)
001751          SET VALUE-INDEX TO 1
001752          SEARCH DISC-VALUES 
001753		  AT END 
001754		     MOVE 0 TO WS-DISCOUNT
001755		  WHEN IN-QTY-ORDERED <= D-NUM-ITEMS (DISC-INDEX VALUE-INDEX)
001756               COMPUTE WS-DISCOUNT-AMT = 
001757                        IN-QTY-ORDERED * IN-UNIT-PRICE *
WS-DISCOUNT / 100
001758               COMPUTE WS-DISCOUNTED-AMT = 
001759			      IN-QTY-ORDERED * IN-UNIT-PRICE * (100 - WS-DISCOUNT) /
100
001769          END-SEARCH
001779     END-SEARCH.
001780		
001830
001840		
002110 READ-SALES.
002751**************
002752     READ SALES-FILE
002753       AT END 
002754         MOVE 'YES' TO END-OF-SALES-FILE.
002760      
002770 READ-DISCOUNT.
002780**************
002790     READ DISCOUNT-FILE
002800       AT END 
002810         MOVE 'YES' TO END-OF-DISCOUNT-FILE.
002820     
002830                       
002840 PRINT-HEADINGS.
002850*****************
002860     WRITE PRINT-LINE FROM HDG-LINE-ONE AFTER 1.
002870     WRITE PRINT-LINE FROM HDG-LINE-TWO AFTER 2.
002880     WRITE PRINT-LINE FROM HDG-LINE-THREE.
002910     WRITE PRINT-LINE FROM SPACES.
002920        
002930 PRINT-DETAILS.
002940************************
002950     
002960 ADD-TO-SUMMARY.
002970***********************
002980     SET SUM-INDEX TO 1.
002990	   SEARCH SUMMARY-ENTITY 
003000	     AT END 
003010	        ADD 1 TO SUMMARY-NO
003020		MOVE IN-SERIES TO SUM-SERIES (SUM-NO)
003030		MOVE WS-DISCOUNT-AMT TO SUM-DISCOUNT (SUM-NO)
003040	     WHEN IN-SERIES = SUM-SERIES (SUM-INDEX)
003050		ADD WS-DISCOUNT TO SUM-DISCOUNT (SUM-INDEX)
003060
003070
```

###### ↳ ↳ ↳ Re: Confused with Two-Level Table Program

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-09-21T21:43:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0309212043.7c33a0f0@posting.google.com>`
- **References:** `<5cddb7f2.0309010231.54e77e9d@posting.google.com> <g2c6lv8m4td6l9et17rtsq5rni68rc3i3t@4ax.com> <5cddb7f2.0309210833.ff4d213@posting.google.com>`

```
Hi Mike,

Hang in there. You're almost home free. It looks to me like you've got
the summary tbl population ok. The only thing left is to print it.
What's the problem? Do you know where/when to write it? You should
know how many entries are in the table. And you should know who they
are and how much was accumed for each, right?

If not, set me straight. What don't you know? Maybe we can figure it
out.

Regards, Jack.



mikey@mailbox.co.za (Michael) wrote in message news:<5cddb7f2.0309210833.ff4d213@posting.google.com>...
> Hi, I compiled my code in Fujitsu 3.0, but I'm really not sure how to
> accumulate the summary table and print from the summary table...
…[241 more quoted lines elided]…
> 003070
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
