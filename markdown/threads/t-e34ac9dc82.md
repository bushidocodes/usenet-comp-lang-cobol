[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Homework, Help

_2 messages · 2 participants · 1999-01_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning)

---

### Homework, Help

- **From:** Casey <sarvec@n-link.com>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36A55626.36B3@n-link.com>`

```
Please don't get on my rear for posting this code. Thane said "post the
code and maybe we can help" a while ago so now I am taking the
opportunity to post it. Is it a coincidence that college started again
today? :-)
Ok, we all know it is my homework and that I am having a hard time with
it. But you can also see that I have worked out a major portion of it on
my own.  I am putting in considerable effort but have decided to turn to
you experts.

The source is first, the input record data is next in [two files] , the
output data is listed last [in two files]. 
The object of the program is to load a table that contains the data for
a pay-table.
There is a hardcoded table that is in there somewhere near the middle.
Process is to read the input record for data, search the table for
corresponding data and if found process the record.
If the data in the input file is not valid [if type-role is not not A
through F] then write an error record and process the next record. There
is also a data check for non-numeric data. If data coming in is not
numeric then write the error record and process the next record
There are a few more calculations and moves to do but I have that
figured out, even though the below code doesn't reflect that.
My main problem is the program trying to read past end of file. 

The source:

IDENTIFICATION DIVISION.
 PROGRAM-ID.  PROGRAM8.
 AUTHOR.      CASEY.
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 
 SPECIAL-NAMES.
     C01 IS TOP-OF-PAGE.
 
 INPUT-OUTPUT SECTION.
 FILE-CONTROL.

     SELECT pay-file ASSIGN TO 'C:\PROGRAM8.DAT'
     organization is line sequential.

     SELECT input-file ASSIGN TO 'C:\xtra-file.DAT'
     ORGANIZATION IS LINE SEQUENTIAL.

     select output-file assign to 'c:\prog8out.dat'.
     select error-file assign to 'c:\error.dat'.

 DATA DIVISION.
 FILE SECTION.
 fd  error-file
     label records are omitted
     record contains 80 characters
     data record is error-record
     recording mode is f.

 01  error-record  pic x(80).
    

 FD  pay-file                                               
     LABEL RECORDS ARE OMITTED                                 
     RECORD CONTAINS 28 CHARACTERS
     DATA RECORD IS pay-record
     RECORDING MODE IS F.
 
 01 pay-record.
    05  filler    pic 99v99.

 fd  input-file
     label records are omitted
     record contains 40 characters
     data record is input-record
     recording mode is f.

  01  input-record.
     05  social-number    pic 9(9).
     05  xtras-name       pic x(20).
     05  experience       pic 99.
     05  type-role        pic x.
     05  regular-hours    pic 999v9.
     05  xpanded-role     pic xx.

 fd  output-file
     label records are omitted
     record contains 118 characters
     data record is output-record
     recording mode is f.

 01  output-record    pic x(118).
 
 
 
 working-storage section.
 01  no-more-records   pic xx value spaces.
 01  chart1-index      pic 9  value zero.
 01  chart2-index      pic 9  value zero.
 01  pay-chart-value   pic 9.
 01  movie-pay-file.
     05 pay-row occurs 6 times.
        10  pay-column occurs 7 times.
            15  pay-chart  pic 99v99.

 01  regular-pay       pic 9999v99.
 01  role-type         pic 9.
 01  pay-amount        pic 9999v99.
 01  extra-pay         pic 99V99.
 01  BONUS-INDEXER     pic 9         value zero.
 01  error-switch      pic 99.
 01  wk-regular-hours  pic 9999      value zero.
 01  pay-computer      pic 999v99    value zero.

 01  hard-code-table.
     05  filler        pic x(4)    value   'AA01'. 
     05  filler        pic x(4)    value   'AV01'.
     05  filler   	 pic x(4)    value   'BA03'.
     05  filler   	 pic x(4)    value   'BN05'.
     05  filler   	 pic x(4)    value   'CA05'.
     05  filler   	 pic x(4)    value   'CN04'.
     05  filler   	 pic x(4)    value   'DA08'.
     05  filler   	 pic x(4)    value   'DN08'.
     05  filler   	 pic x(4)    value   'DR09'.
     05  filler   	 pic x(4)    value   'EA14'.
     05  filler  	 pic x(4)    value   'EN03'.
     05  filler  	 pic x(4)    value   'ER03'.
     05  filler  	 pic x(4)    value   'FA01'.
     05  filler  	 pic x(4)    value   'FN06'.

 01  BONUS-TABLE REDEFINES HARD-CODE-TABLE.
     05  BONUS OCCURS 14 TIMES
         ASCENDING KEY IS BONUS-CODE
         INDEXED BY BONUS-INDEX.
         10  BONUS-CODE   pic XX.
         10  BONUS-HOURS  pic 99.
    
 01  HEADING-1.
     05  FILLER           PIC X(9)   VALUE 'SOC SEC #'.
     05  FILLER           PIC X(5)   VALUE SPACE.
     05  FILLER           PIC X(16)  VALUE 'MOVIE EXTRA NAME'.
     05  FILLER           PIC X(5)   VALUE SPACE.
     05  FILLER           PIC X(10)  VALUE 'EXPERIENCE'.
     05  FILLER           PIC X(5)   VALUE SPACE.
     05  FILLER           PIC X(9)   VALUE 'ROLE TYPE'.
     05  FILLER           PIC X(5)   VALUE SPACE.
     05  FILLER           PIC X(12)  VALUE 'HOURLY RATE'.
     05  FILLER           PIC X(5)   VALUE SPACE.
     05  FILLER           PIC X(10)  VALUE 'REG HOURS'.
     05  FILLER           PIC X(5)   VALUE SPACE.
     05  FILLER           PIC X(11)  VALUE 'EXTRA HOURS'.
     05  FILLER           PIC X(5)   VALUE SPACE.
     05  FILLER           PIC X(3)   VALUE 'PAY'.
     
 01  ws-output-record.
     05 ws-social-number  pic 9(9).
     05 filler            pic x(5).
     05 ws-xtras-name     pic x(20).
     05 filler            pic x(5).
     05 ws-experience     pic 99.
     05 filler            pic x(12).
     05 ws-type-role      pic x.
     05 filler            pic x(12).
     05 ws-pay-rate       pic 99.99.
     05 filler            pic x(11).
     05 ws-regular-hours  pic ZZ9.09.
     05 filler            pic x(12).
     05 ws-extra-hours    pic 99.
     05 filler            pic x(8).
     05 ws-pay-amount     pic $$$$$.99.

 01  ws-error-record.
     05 er-social-number  pic 9(9).
     05 filler            pic x(5).
     05 er-xtras-name     pic x(20).
     05 filler            pic x(5).
     05 er-experience     pic 99.
     05 filler            pic x(12).
     05 er-type-role      pic x.

 procedure division.
     open input pay-file input-file  
      output output-file error-file.
       perform load-table-process 
        varying chart1-index from 1 by 1 
         until chart1-index > 6
          after chart2-index from 1 by 1 
           until chart2-index > 7.

     WRITE OUTPUT-RECORD FROM HEADING-1
     AFTER ADVANCING TOP-OF-PAGE.
     read input-file.
     perform process-records until no-more-records = 'no'.

     close input-file error-file pay-file output-file.
     stop run.
 process-records.
     perform type-role-process.
     if type-role = 'G' then 
     perform write-error-records-process
     end-if.
     perform search-process.
     perform compute-hours-process.
     perform move-process.
     display regular-hours.
     move spaces to output-record.
     write output-record from ws-output-record.
     read input-file at end move 'no' to no-more-records.

 write-error-records-process.
     display 'Movie Role Type was not found'.
     display 'writing error record'.
     move social-number to er-social-number.
     move xtras-name to er-xtras-name.
     move experience to er-experience.
     move type-role to er-type-role.
     write error-record from ws-error-record
     after advancing 1 line.
     read input-file at end move 'no' to no-more-records.

 load-table-process. 
     
     read pay-file into pay-chart 
          (chart1-index, chart2-index).
     
     display pay-chart (chart1-index, chart2-index).
* Displays have confirmed that table is properly loaded.     
* display ' '.

 type-role-process.

     move 0 to error-switch.
     move 0 to chart1-index.
      evaluate type-role
      when 'A' move 1 to chart1-index
      when 'B' move 2 to chart1-index
      when 'C' move 3 to chart1-index
      when 'D' move 4 to chart1-index
      when 'E' move 5 to chart1-index
      when 'F' move 6 to chart1-index
     end-evaluate.
     

 experience-process.
     move 0 to chart2-index.
     move 0 to pay-computer.
     evaluate experience
      when 0 move 1 to chart2-index
      when 1 move 2 to chart2-index
      when 2 move 3 to chart2-index
      when 3 move 4 to chart2-index
      when 4 move 5 to chart2-index
      when 5 through 7 move 6 to chart2-index
      when 8 through 15 move 7 to chart2-index
     end-evaluate.
     if experience is not numeric 
     perform write-error-records-process
     end-if.     

     display 'pay chart ' pay-chart (chart1-index, 
       chart2-index).
     
     move pay-chart (chart1-index, chart2-index) to 
      pay-computer ws-pay-rate.

     display ws-pay-rate.
     
 move-process.    
*     add regular-hours to wk-regular-hours.
    

     move social-number to ws-social-number.
     move xtras-name to ws-xtras-name.
     move experience to ws-experience.
     move type-role to ws-type-role.
    

 search-process.
     set bonus-index to 0.
     search all BONUS
      at end move 99 to error-switch
       when BONUS-CODE (BONUS-INDEX) equals xpanded-role
        add bonus-hours (bonus-index) to  wk-regular-hours.
         move bonus-hours (bonus-index) to ws-extra-hours.
     if bonus-code (bonus-index) not equal xpanded-role
      move 00 to ws-extra-hours
     end-if.

 compute-hours-process.
     display 'regular hours: '  regular-hours.
     display 'pay-computer: '  pay-computer.
     move regular-hours to ws-regular-hours.
     add ws-extra-hours to regular-hours.
     compute pay-amount = regular-hours * pay-computer.
     move pay-amount to ws-pay-amount.
     
The input data:
000000001JONES, J            00G0800GN
000000002JONES, ROY          02F0450FA
000000003WILLIAMS, JOHN      01E0450FA
000000004FOSTER, RAYMOND     11B0425BN
000000005HIGH, LUCY          08A0450AR
000000006HJARDING, HOWARD    04A0450AV
000000007ZHE, KEVIN          05D0450DN
000000008JENNINGS, VIVIAN      D0200DA
000000009ROOSEVELT, TIMOTHY  07E0230XX
000000010TRUELOVE, BILL      09G0450EN

The pay chart that is loaded into the table:

2000250030003200340038004000
1400170018001900210023002400
1700175018001800185018501900
1400150015501550155016001600
1375145015001500152515501550
1350135013501375137513751400

The output record:

SOC SEC# MOVIE EXTRA NAME EXPERIENCE ROLE TYPE HOURLY RATE REG HOURS
EXTRA HOURS PAY   
000000002 JONES, ROY       02            F       45.00       
01            $.00
000000003 WILLIAMS, JOHN   01            E       45.00       
01            $.00
000000004 FOSTER, RAYMOND  11            B       42.05       
05            $.00
000000005 HIGH, LUCY       08            A       45.00       
00            $.00
000000006 HJARDING, HOWARD 04            A       45.00       
01            $.00
000000007 ZHE, KEVIN       05            D       45.00       
08            $.00
000000008 JENNINGS, VIVIAN  0            D       20.00       
08            $.00
000000009 ROOSEVELT, TIMOT 07            E       23.00       
00            $.00
000000010 TRUELOVE, BILL   09            G       45.00       
03            $.00


In the above record the G shouldn't be there, the program should have
written it to the error file and ended.


The error record:


000000001 JONES, J                 00           
G                          
000000010  TRUELOVE, BILL           09            G
```

#### ↳ Re: Homework, Help

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<783nej$n8j@dfw-ixnews10.ix.netcom.com>`
- **References:** `<36A55626.36B3@n-link.com>`

```
You'll may get lots of comments on this, but a few things to say:

On your "reading past file" question,
    look at your
         process-records
paragraph, and follow the logic *IF* the very last record that you read in
HAPPENS to end up with a type-role = G.

HINT: always be "wary" if your application reads the same file in more than
one place.

   ****

Now having said that (which I think may be your real problem) let me mention
a few other related hints.

When reading a file, NEVER believe the people who have told you how many
records it will have.  You don't have an "AT END" on your first read of the
"input-file" and NONE on your reads of the "pay-file".  Related to this,
when you are loading your pay-table, you do a PERFORM VARYING that doesn't
allow for any "get out" - just in case it doesn't have all the required
records in it.

I hope this helps.

FYI - in the future, if you can "cut your program down" a little to
demonstrate the problem, or provide it as an attachment (2nd choice) or give
an email address (or web page) where everyone can download it, that probably
will work better than posting the whole code.  HOWEVER, we really do respond
better with too much code than with too little.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
