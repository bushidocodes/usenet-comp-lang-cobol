[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help Desperately Needed in Student Cobol Project

_1 message · 1 participant · 2001-05_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Help Desperately Needed in Student Cobol Project

- **From:** markyoung01@home.com (Mark Young)
- **Date:** 2001-05-17T00:09:55+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol,fj.comp.lang.cobol
- **Message-ID:** `<3b030ca9.15876552@news.rdc1.tx.home.com>`
- **References:** `<6wxM6.4098$6j3.356899@www.newsranger.com>`

```
On Wed, 16 May 2001 16:02:10 GMT, Michael <nospam@newsranger.com>
wrote:

>Hi, My name is Michael Lorenc, I am 21 years old from Cape Town, South Africa.
>I am currently doing a course in Cobol, but have run into some problems in a
…[18 more quoted lines elided]…
>
Try this kind of layout....

01 AGENT-RECORD.
	10 AGENT-EMPLOYEE-NUMBER        PIC 9(6).
	10 AGENT-SURNAME                            PIC  X(15).
	10 AGENT-INITIALS                                PIC  X(3).
	10 AGENT-COMPANY-CODE              PIC 99.
	10 AGENT-SALES-TABLE OCCURS 5 INDEXED BY SALES-INDEX.
	    15 AGENT-POLICY-TYPE                  PIC 99.
                  15 AGENT-AMT-SOLD                      PIC  9(4)V99.


Makes it cleaner....

Also... "more than 2 policy types"?  Do you mean the agent has to make
more than two sales or he has to have sales in two different types of
policies?

You are handling for two or more sales but keep in mind the customer
may mean for you to track agents who are making more than one policy
type sale...  (I think you are on the right track in this case)

>Read the records in... subscript across bump a counter on 
>
…[186 more quoted lines elided]…
>

1. Use Indentions liberally to make it more readable and
maintainable... The advantage that COBOL has over other languages is
the maintainability in the long run.   That works only if the program
is well written.

2. Number your paragraphs as a prefix.

>PROCEDURE DIVISION.
>SORT-EMPLOYEE-RECORDS.
…[6 more quoted lines elided]…
>
3. Try having one Write and performing it...  There are arguements
both ways...

move space to print-line
perform 600-printline thru 600-exit.

>WRITE PRINT-LINE FROM SPACES.   
>DISPLAY "PRESS ANY KEY TO CONTINUE".                   
>ACCEPT PAUSE

What is this running on?  not OS390.


>DISPLAY SPACES ERASE.
>STOP RUN. 

4. This is your mainline paragraph....  010-mainline or 010-Driver
would be a good name...

>CALC-AND-EXTRACT.
>OPEN INPUT EMPLOYEE-FILE
>                        COMPANY-FILE
>OUTPUT PRINT-FILE
>PERFORM READ-EMPLOYEE

5. Perform THRU allows you to say exactly what you mean and if future
paragraphs are added, then the logic is not changed accidently.

>PERFORM PROCESS-EMPLOYEE-RECORDS UNTIL NO-DATA-REMAINS
>CLOSE EMPLOYEE-FILE
…[17 more quoted lines elided]…
>PERFORM PROCESS-ONE-COMPANY 
      UNTIL NO-DATA-REMAINS 
           OR HEADING-COMPANY NOT EQUAL PREV-COMPANY.


try that way....
>
>
…[10 more quoted lines elided]…
>    RELEASE SORT-RECORD

Don't ya want to wait to reset Policy-Counter with each new record?
Also if you try initializing it before the read of a new record, you
won't SOC7 the first time you add 1 to Policy-counter...
>
>INITIALISE-COMPANY.
…[17 more quoted lines elided]…
>      ADD 1 TO POLICY-COUNTER.

Boom right here first time thru if you don't set it to zero before
reading a record....


>READ EMPLOYEE-FILE
>     AT END MOVE 'NO' TO DATA-REMAINS-SWITCH
>END-READ.


If you have carriage control defined in the first print line then you
would just move the heading-line-one in and
perform the Write print-line

How about 

900-Print-Headers.
>
>WRITE-HEADING-LINES.
…[6 more quoted lines elided]…
>
900-exit. 
        exit.

950-Print-detail.
>WRITE-DETAIL-LINE.
>MOVE SRT-EMPLOYEE-NUMBER TO DET-EMPLOYEE-NUMBER.
…[3 more quoted lines elided]…
>WRITE PRINT-LINE FROM DETAIL-LINE.

950-exit.
        exit.




>

   Line up your moves and To to make it more readable...

Cheers!
Mark Young


>
>Input Files - 
…[35 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
