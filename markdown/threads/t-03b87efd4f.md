[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Urgently needed with Printing from A Two-Level Table

_10 messages · 4 participants · 2003-06_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help Urgently needed with Printing from A Two-Level Table

- **From:** mikey@mailbox.co.za (Michael)
- **Date:** 2003-06-05T06:29:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cddb7f2.0306050529.24493935@posting.google.com>`

```
Hi, in this program I need to accumulate the profits and losses for
each town and each quarter of the year in a 2-dimesional table and
then to print these results from the two-dimesional table.

I can't get the program to run, it gets stuck somewhere on the search.
If anyone could help me, i'd really appreciate it, it's quite
urgent...

Thanks,

Michael

IDENTIFICATION DIVISION.
       PROGRAM-ID.  OP203003.
       AUTHOR.      MICHAEL LORENC.
       DATE-WRITTEN.  MAY 2003.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT SALES-FILE  ASSIGN TO DISK 'H:\OP2QTR03.DAT'
                  ORGANIZATION IS LINE SEQUENTIAL.
           SELECT PRINT-FILE  ASSIGN TO PRINTER 'CON'.
           
       DATA DIVISION.
       FILE SECTION.
       FD  SALES-FILE
           RECORD CONTAINS 21 CHARACTERS
           DATA RECORD IS SALES-RECORD.
       
       01  SALES-RECORD.
           05  SALES-TOWN-CODE      PIC 9(4).
           05  SALES-QUARTER        PIC 9.
           05  SALES-AMOUNT         PIC S9(5)V99 SIGN TRAILING
SEPARATE.
           05  PURCHASE-AMOUNT      PIC S9(5)V99 SIGN TRAILING
SEPARATE.
           
       
       FD  PRINT-FILE
           RECORD CONTAINS 80 CHARACTERS
           DATA RECORD IS PRINT-LINE.
           
       01  PRINT-LINE               PIC X(80).               
       
       WORKING-STORAGE SECTION.
     
       01  WAREHOUSE-VALUES.
           05  SALES OCCURS 14 TIMES
               INDEXED BY TOWNS-INDEX.
               10  QUARTERS OCCURS 5 TIMES
                   INDEXED BY QUARTER-INDEX.
                   15  PURCHASE      PIC S9999999V99.
       
       
       
            
       01  MONTH-NAMES.
       
           05                    PIC X(9)   VALUE 'JANUARY'.
           05                    PIC X(9)   VALUE 'FEBRUARY'.
           05                    PIC X(9)   VALUE 'MARCH'.
           05                    PIC X(9)   VALUE 'APRIL'.
           05                    PIC X(9)   VALUE 'MAY'.
           05                    PIC X(9)   VALUE 'JUNE'.
           05                    PIC X(9)   VALUE 'JULY'.
           05                    PIC X(9)   VALUE 'AUGUST'.
           05                    PIC X(9)   VALUE 'SEPTEMBER'.
           05                    PIC X(9)   VALUE 'OCTOBER'.
           05                    PIC X(9)   VALUE 'NOVEMBER'.
           05                    PIC X(9)   VALUE 'DECEMBER'.  
           
       01  MONTHS-TABLE REDEFINES MONTH-NAMES.   
           05  MONTHS OCCURS 12 TIMES
               INDEXED BY MONTH-INDEX.
               10  MONTH-NAME     PIC X(9).
               
       01  TOWN-NAMES.
       
           05                   PIC X(20) VALUE "CT  CAPE TOWN".
           05                   PIC X(20) VALUE "BE  BELLVILLE".
           05                   PIC X(20) VALUE "ST  STELLENBOSCH".
           05                   PIC X(20) VALUE "PE  PORT ELIZABETH".
           05                   PIC X(20) VALUE "EL  EASTLONDON".
           05                   PIC X(20) VALUE "GHT GRAHAMSTOWN".
           05                   PIC X(20) VALUE "DBN DURBAN".
           05                   PIC X(20) VALUE
"PTMBPIETERMARITZBURG".
           05                   PIC X(20) VALUE "BLM BLOEMFONTEIN".
           05                   PIC X(20) VALUE "JHB JOHANNESBURG".
           05                   PIC X(20) VALUE "PTCHPOTCHEFSTROOM".
           05                   PIC X(20) VALUE "POL POLOKWANE".
           05                   PIC X(20) VALUE '    UNKNOWN'.       
           05                   PIC X(20) VALUE "QTT QUARTER TOTAL".
       
       01  TOWN-TABLE REDEFINES TOWN-NAMES.
           05  TOWN-VALUES OCCURS 14 TIMES INDEXED BY TOWN-INDEX.
               10  TOWN-CODE         PIC X(4).
               10  TOWN-NAME         PIC X(16).

       
       01  PROGRAM-SWITCHES-AND-COUNTERS.
       
           05  PAUSE                   PIC X.
           05  DATA-REMAINS-SWITCH     PIC X(3) VALUE 'YES'.
               88 NO-DATA-REMAINS               VALUE 'NO'.
           05  PAGE-COUNT              PIC 9(2) VALUE 0.
           
       01  WS-DATE.
           05   WS-YEAR                     PIC 99.
           05   WS-MONTH                    PIC 99.
           05   WS-DAY                      PIC 99.
       
           
       01  HEADING-LINE-ONE.
       
           05                          PIC X(27)  VALUE SPACES.
           05                          PIC X(26)  VALUE 
               'THE MCWIMPY BURGER COMPANY'.
           05                          PIC X(11)  VALUE SPACES.
           05                          PIC X(14)  VALUE
               'MAY 2003'.
               
       01  HEADING-LINE-TWO.
       
           05                          PIC X(23) VALUE SPACES.
           05                          PIC X(3)  VALUE '1ST'.
           05                          PIC X(9)  VALUE SPACES.
           05                          PIC X(3)  VALUE '2ND'.
           05                          PIC X(9)  VALUE SPACES.
           05                          PIC X(3)  VALUE '3RD'.
           05                          PIC X(9)  VALUE SPACES.
           05                          PIC X(3)  VALUE '4TH'.
           05                          PIC X(8)  VALUE SPACES.
           05                          PIC X(4)  VALUE 'TOWN'.
               
       01  HEADING-LINE-THREE.
       
           05                          PIC X(7)    VALUE SPACES.
           05                          PIC X(4)    VALUE 'TOWN'.
           05                          PIC X(10)   VALUE SPACES.
           05                          PIC X(7)    VALUE 'QUARTER'.
           05                          PIC X(5)    VALUE SPACES.
           05                          PIC X(7)    VALUE 'QUARTER'.
           05                          PIC X(5)    VALUE SPACES.
           05                          PIC X(7)    VALUE 'QUARTER'.
           05                          PIC X(5)    VALUE SPACES.
           05                          PIC X(7)    VALUE 'QUARTER'.
           05                          PIC X(6)    VALUE SPACES.
           05                          PIC X(5)    VALUE 'TOTAL'.
           

       
       01  DETAIL-LINE.
       
           05                          PIC X     VALUE SPACES.
           05 DET-TOWN-NAME            PIC X(16).
           05                          PIC X(3) VALUE SPACES.
           05 DET-FIRST OCCURS 5 TIMES INDEXED BY DETAIL-INDEX.
              10 DET-AMOUNT              PIC ZZZZZZZ9.99-.
              10 DET-AMOUNTX REDEFINES DET-AMOUNT
                                       PIC X(12).
           
       PROCEDURE DIVISION.
       PREPARE-EMPLOYEE.
           
           PERFORM INITIALIZATION.
           PERFORM PROCESS-RECORDS UNTILEND OF FILE    
           PERFORM TERMINATION.
           STOP RUN.
           
       INITIALIZATION.     
           OPEN INPUT    SALES-FILE
                OUTPUT   PRINT-FILE.
           ACCEPT WS-DATE FROM DATE.
           PERFORM WRITE-HEADING-LINES.
           
           READ SALES-FILE
                 AT END MOVE 'NO' TO DATA-REMAINS-SWITCH
           END-READ.
           
           
       TERMINATION.
       
           CLOSE SALES-FILE
                 PRINT-FILE.
       
       PROCESS-RECORDS.
           SUBTRACT PURCH  
           PERFORM SEARCH-TOWNS.
            READ SALES-FILE
                 AT END MOVE 'NO' TO DATA-REMAINS-SWITCH
           END-READ.
           
       SEARCH-TOWNS.
            
            SET TOWNS-INDEX TO 1.   
            SEARCH TOWN-VALUES
            AT END
                ADD SALES-AMOUNT TO SALES(13 QUARTER-INDEX)
                ADD SALES-AMOUNT TO SALES(13 5)
                ADD SALES-AMOUNT TO SALES(14 QUARTER-INDEX)
                ADD SALES-AMOUNT TO SALES(14 5)
            WHEN SALES-TOWN-CODE = TOWN-CODE (TOWN-INDEX)
                SET TOWNS-INDEX TO TOWN-INDEX
                SET QUARTER-INDEX TO SALES-QUARTER
                ADD SALES-AMOUNT TO SALES(TOWNS-INDEX QUARTER-INDEX)
                ADD SALES-AMOUNT TO SALES(TOWNS-INDEX 5)
                ADD SALES-AMOUNT TO SALES(14 QUARTER-INDEX)
                ADD SALES-AMOUNT TO SALES(14 5)
            END-SEARCH.
           
       PERORM PRINT-TOWN-TABLE VARYING TOWN-INDEX FROM 1 BY 1
                 UNTIL TOWN-INDEX > 14.
            
       PRINT-TOWN-TABLE.
           MOVE TOWN-NAME (TOWN-INDEX) TO DET-TOWN-NAME.
           SET TOWNS-INDEX TO TOWN-INDEX
           PERFORM PROCESS-QUARTER VARYING QUARTER-INDEX
               FROM 1 BY 1 UNTIL QUARTER-INDEX > 5
            PERFORM WRITE-DETAIL-LINE.
            
       PROCESS-QUARTER.
           SET DETAIL-INDEX TO QUARTER-INDEX.
           IF SALES(TOWN-INDEX, QUARTER-INDEX ) = ZERO
              MOVE ALL '*' TO DET-AMOUNTX(DETAIL-INDEX)
           ELSE   
           MOVE SALES( TOWNS-INDEX QUARTER-INDEX)
                       TO DET-AMOUNT(DETAIL-INDEX).        
           
                  
       WRITE-HEADING-LINES.
           WRITE PRINT-LINE FROM HEADING-LINE-ONE AFTER PAGE.
           WRITE PRINT-LINE FROM HEADING-LINE-TWO AFTER 2.
           WRITE PRINT-LINE FROM HEADING-LINE-THREE.
           WRITE PRINT-LINE FROM SPACES.
              
       WRITE-DETAIL-LINE.
           WRITE PRINT-LINE FROM DETAIL-LINE.
```

#### ↳ Re: Help Urgently needed with Printing from A Two-Level Table

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-05T19:17:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_GMDa.188415$ja4.9946964@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com>`

```
Check your search index.
It seems your set  Towns-index to 1, rather than town-index.

"Michael" <mikey@mailbox.co.za> wrote in message
news:5cddb7f2.0306050529.24493935@posting.google.com...
| Hi, in this program I need to accumulate the profits and losses for
| each town and each quarter of the year in a 2-dimesional table and
…[235 more quoted lines elided]…
|            WRITE PRINT-LINE FROM DETAIL-LINE.
```

#### ↳ Re: Help Urgently needed with Printing from A Two-Level Table

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-06T00:10:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3edfd8fc.616248957@news.optonline.net>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com>`

```
The error is obvious. You are initializing towns-index rather than town-index
before the search. 

What is:

   PERFORM PROCESS-RECORDS UNTILEND OF FILE    

That will not compile. It should be:

   perform process-records until no-data-remains

-----------------------------------------------------------------------------------------------

mikey@mailbox.co.za (Michael) wrote:

>Hi, in this program I need to accumulate the profits and losses for
>each town and each quarter of the year in a 2-dimesional table and
…[235 more quoted lines elided]…
>           WRITE PRINT-LINE FROM DETAIL-LINE.
```

##### ↳ ↳ Re: Help Urgently needed with Printing from A Two-Level Table

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-06T01:08:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VPRDa.111910$cO3.8152743@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com> <3edfd8fc.616248957@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3edfd8fc.616248957@news.optonline.net...
| The error is obvious. You are initializing towns-index rather than
town-index
| before the search.
|
…[6 more quoted lines elided]…
|    perform process-records until no-data-remains

There are more errors, can you find them all?
```

#### ↳ Re: Help Urgently needed with Printing from A Two-Level Table

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-06-05T21:14:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0306052014.6cf67bfa@posting.google.com>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com>`

```
Hi Mike,

Looks like you're hell bent in the wrong direction. This is the 2nd
control break problem youï¿½ve presented here. Success in handling these
problems start with understanding how to order your input file. That's
usually spelled S-O-R-T.

Creating a table of amounts by town /by quarter can lead to a
solution, but it can also lead to the kind of mess you got yourself
into.

So you have to create a report that produces a line of data for each
town on the Sales file. That line contains a total of sales for each
quarter and a yearly total. How would you order (sort) the Sales file
to accomplish that? Think CONTROL BREAKS and the answer should emerge.

As I've mentioned above, this is the 2nd control break problem you've
encountered in as many weeks. It behooves you to sit down and 
establish a thorough understanding of the topic before proceeding.
There will be many control breaks in your future, if youï¿½re lucky. <G>

BTW,I noticed some syntax errors in your code. You should try to
present cleanly compiled code. It prevents misunderstandings. You are
cut & pasting, I hope.
 
Regards, Jack.

        


mikey@mailbox.co.za (Michael) wrote in message news:<5cddb7f2.0306050529.24493935@posting.google.com>...
> Hi, in this program I need to accumulate the profits and losses for
> each town and each quarter of the year in a 2-dimesional table and
…[235 more quoted lines elided]…
>            WRITE PRINT-LINE FROM DETAIL-LINE.
```

##### ↳ ↳ Re: Help Urgently needed with Printing from A Two-Level Table

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-06T23:17:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ii9Ea.189923$ja4.10079959@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com> <8a2d426e.0306052014.6cf67bfa@posting.google.com>`

```

"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0306052014.6cf67bfa@posting.google.com...
| Hi Mike,
|
…[3 more quoted lines elided]…
| usually spelled S-O-R-T.

I think he's a student working on a class problem.
Probably getting into 2 dimension tables.

Your proposal is OK, but I think he woulkd get an F on the assignment.

|
| Creating a table of amounts by town /by quarter can lead to a
…[15 more quoted lines elided]…
| cut & pasting, I hope.

There are more than syntax errors.

|
| Regards, Jack.
|
```

###### ↳ ↳ ↳ Re: Help Urgently needed with Printing from A Two-Level Table

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-06-06T22:04:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0306062104.8fd2778@posting.google.com>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com> <8a2d426e.0306052014.6cf67bfa@posting.google.com> <ii9Ea.189923$ja4.10079959@bgtnsc05-news.ops.worldnet.att.net>`

```
"Harley" <dennis.harley@worldnet.att.net> wrote in message news:<ii9Ea.189923$ja4.10079959@bgtnsc05-news.ops.worldnet.att.net>...
> "Jack Sleight" <jacksleight@hotmail.com> wrote in message
> news:8a2d426e.0306052014.6cf67bfa@posting.google.com...
…[8 more quoted lines elided]…
> Probably getting into 2 dimension tables.

The world is full of problems requiring a solution using 2 dimension
tables, but I doubt this is one.

> Your proposal is OK, but I think he woulkd get an F on the assignment.

I think the instructor should get the F for imposing that methodology.
> 

> |
> | Creating a table of amounts by town /by quarter can lead to a
…[17 more quoted lines elided]…
> There are more than syntax errors.

Logic errors are expected at this stage of debugging. Syntax errors
should be long gone.
> 
> |
> | Regards, Jack.
> |
```

###### ↳ ↳ ↳ Re: Help Urgently needed with Printing from A Two-Level Table

_(reply depth: 4)_

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-07T13:16:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6BlEa.113656$cO3.8324388@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com> <8a2d426e.0306052014.6cf67bfa@posting.google.com> <ii9Ea.189923$ja4.10079959@bgtnsc05-news.ops.worldnet.att.net> <8a2d426e.0306062104.8fd2778@posting.google.com>`

```

"Jack Sleight" <jacksleight@hotmail.com> wrote in message
news:8a2d426e.0306062104.8fd2778@posting.google.com...
| "Harley" <dennis.harley@worldnet.att.net> wrote in message
news:<ii9Ea.189923$ja4.10079959@bgtnsc05-news.ops.worldnet.att.net>...
| > "Jack Sleight" <jacksleight@hotmail.com> wrote in message
| > news:8a2d426e.0306052014.6cf67bfa@posting.google.com...
…[11 more quoted lines elided]…
| tables, but I doubt this is one.

I Agree, in part.
I can't remember the last time I used more than 1 dimension.
As you said S-O-R-T.

|
| > Your proposal is OK, but I think he woulkd get an F on the assignment.
|
| I think the instructor should get the F for imposing that methodology.

I have a low opinion of instructors in general.
Partly because I've found they teach based on state-of-the-art methods that
are 20 years old.
```

###### ↳ ↳ ↳ Re: Help Urgently needed with Printing from A Two-Level Table

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-06-07T20:21:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ee1fb5b.106164753@news.optonline.net>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com> <8a2d426e.0306052014.6cf67bfa@posting.google.com> <ii9Ea.189923$ja4.10079959@bgtnsc05-news.ops.worldnet.att.net> <8a2d426e.0306062104.8fd2778@posting.google.com> <6BlEa.113656$cO3.8324388@bgtnsc04-news.ops.worldnet.att.net>`

```
Student code posted here uses upper case, prefixes on data and paragraph names,
and a period at the end of every statement.  It looks like COBOL from the 70s. 

"Harley" <dennis.harley@worldnet.att.net> wrote:

>| I think the instructor should get the F for imposing that methodology.
>
>I have a low opinion of instructors in general.
>Partly because I've found they teach based on state-of-the-art methods that
>are 20 years old.
```

###### ↳ ↳ ↳ Re: Help Urgently needed with Printing from A Two-Level Table

_(reply depth: 6)_

- **From:** "Harley" <dennis.harley@worldnet.att.net>
- **Date:** 2003-06-08T14:47:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r0IEa.115184$cO3.8443822@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<5cddb7f2.0306050529.24493935@posting.google.com> <8a2d426e.0306052014.6cf67bfa@posting.google.com> <ii9Ea.189923$ja4.10079959@bgtnsc05-news.ops.worldnet.att.net> <8a2d426e.0306062104.8fd2778@posting.google.com> <6BlEa.113656$cO3.8324388@bgtnsc04-news.ops.worldnet.att.net> <3ee1fb5b.106164753@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3ee1fb5b.106164753@news.optonline.net...
| Student code posted here uses upper case, prefixes on data and paragraph
names,
| and a period at the end of every statement.  It looks like COBOL from the
70s.

Except for the absence of FILLER.

01  TOWN-NAMES.

           05                   PIC X(20) VALUE "CT  CAPE TOWN".
           05                   PIC X(20) VALUE "BE  BELLVILLE".


|
| "Harley" <dennis.harley@worldnet.att.net> wrote:
…[4 more quoted lines elided]…
| >Partly because I've found they teach based on state-of-the-art methods
that
| >are 20 years old.
|
|
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
