[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PerformVarying - Tables

_8 messages · 6 participants · 1999-11_

---

### PerformVarying - Tables

- **From:** dc606@my-deja.com
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vp65o$lar$1@nnrp1.deja.com>`

```
I think the problem is with PERFORM VARYING statement.  Output is not
correct.

1.  First LOCATION VALUE for first record is a blank space.

2.  When values are moved from tables (Title, Location and Education)
to Detail line, the value moved is the value one(1) line before correct
value defined in table.

Any idea why?


 01  TITLE-VALUE.
           05 PIC X(18) VALUE '010PRESIDENT'.
           05 PIC X(18) VALUE '020VICE PRES'.
           05 PIC X(18) VALUE '030MKT VP'.
           05 PIC X(18) VALUE '040MKT MGR'.
           05 PIC X(18) VALUE '050MKT REP'.
           05 PIC X(18) VALUE '060DP VP'.
           05 PIC X(18) VALUE '070DP MGR'.
           05 PIC X(18) VALUE '080DP PROG'.
           05 PIC X(18) VALUE '090CLERK'.
           05 PIC X(18) VALUE '010ADM ASST'.


       01  TITLE-TABLE REDEFINES TITLE-VALUE.
           05  TITLES OCCURS 10 TIMES.
               10  TITLE-CODE          PIC X(3).
               10  EXP-TITLE           PIC X(15).

           05  REPORT-TITLE            PIC X(10).




       01 LOCATION-VALUE.
          05   PIC X(14)   VALUE 'MIAMIAMI'.
          05   PIC X(14)   VALUE 'CHICHICAGO'.
          05   PIC X(14)   VALUE 'LA LOS ANGELES'.
          05   PIC X(14)   VALUE 'NY NEW YORK'.
          05   PIC X(14)   VALUE 'ATLATLANTA'.

       01 LOCATION-TABLE REDEFINES LOCATION-VALUE.
          05   LOCATIONS OCCURS 5 TIMES.
               10  LOCATION-CODE       PIC X(3).
               10  EXP-LOCATION        PIC X(11).

           05  REPORT-LOCATION         PIC X(14).




       01 EDUCATION-VALUE.
          05  PIC X(15)   VALUE '1GRADE SCHOOL'.
          05  PIC X(15)   VALUE '2HIGH SCHOOL'.
          05  PIC X(15)   VALUE '3ASSOCIATES'.
          05  PIC X(15)   VALUE '4BACHELORS'.
          05  PIC X(15)   VALUE '5MASTERS'.
          05  PIC X(15)   VALUE '6DOCTORATE'.

       01 EDUCATION-TABLE REDEFINES EDUCATION-VALUE.
          05   EDUCATION OCCURS 6 TIMES.
               10  EDUCATION-CODE      PIC 9.
               10  EXP-EDUCATION       PIC X(14).

          05   REPORT-EDUCATION        PIC X(15).


       PROCEDURE DIVISION.


           PERFORM UNTIL WS-END-OF-FILE-SWITCH='YES'
               READ SALARY-FILE
                   AT END
                       MOVE 'YES' TO WS-END-OF-FILE-SWITCH
                   NOT AT END
                       PERFORM 400-CREATE-SALARY-REPORT
                       PERFORM 900-WRITE-DETAIL-LINE
                   END-READ
          END-PERFORM.
          CLOSE SALARY-FILE
                SALARY-REPORT.
          STOP RUN.




          400-CREATE-SALARY-REPORT.
          PERFORM 500-FIND-TITLE
           VARYING WS-TITLE-SUB FROM 1 BY 1
               UNTIL WS-TITLE-SUB > 10
               OR SAL-TITLE-CODE=TITLE-CODE(WS-TITLE-SUB).

          PERFORM 600-FIND-LOCATION
           VARYING WS-LOCATION-SUB FROM 1 BY 1
               UNTIL WS-LOCATION-SUB > 5
                   OR SAL-LOCATION-CODE=LOCATION-CODE(WS-LOCATION-SUB).


           PERFORM 700-FIND-EDUCATION
            VARYING WS-EDUCATION-SUB FROM 1 BY 1
               UNTIL WS-EDUCATION-SUB > 6
                   OR
                   SAL-EDUCATION-CODE=EDUCATION-CODE(WS-EDUCATION-SUB).




           500-FIND-TITLE.
               IF (WS-TITLE-SUB) NOT=10
                   MOVE EXP-TITLE(WS-TITLE-SUB) TO REPORT-TITLE

               END-IF.


           600-FIND-LOCATION.
               IF (WS-LOCATION-SUB) NOT=5
                  MOVE EXP-LOCATION (WS-LOCATION-SUB) TO
                        REPORT-LOCATION
               END-IF.




           700-FIND-EDUCATION.
               IF (WS-EDUCATION-SUB) NOT=6
                  MOVE EXP-EDUCATION (WS-EDUCATION-SUB) TO
                        REPORT-EDUCATION
               END-IF.




           900-WRITE-DETAIL-LINE.
               MOVE SAL-SOC-SEC-NO TO DET-SSN
               MOVE SAL-NAME-AND-INITIALS TO DET-NAME
               MOVE REPORT-TITLE TO DET-TITLE
               MOVE REPORT-LOCATION TO DET-LOCATION
               MOVE REPORT-EDUCATION TO DET-EDUCATION
               MOVE SAL-RATING TO DET-RATING
               MOVE SAL-SALARY TO DET-SALARY
               WRITE PRINT-LINE FROM DETAIL-LINE


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: PerformVarying - Tables

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4B33E7A1C94A603F.82DE4253412820EF.89F739B9C7CC59F7@lp.airnews.net>`
- **References:** `<7vp65o$lar$1@nnrp1.deja.com>`

```
On Wed, 03 Nov 1999 11:26:48 GMT, dc606@my-deja.com enlightened us:

>I think the problem is with PERFORM VARYING statement.  Output is not
>correct.
…[143 more quoted lines elided]…
>Before you buy.

Maybe this will help.  Given the format of:

PERFORM procedure-name VARYING identifier-1 FROM literal-2 BY
literal-3 UNTIL condition-1 OR condition-2

The logic flow if the PERFORM verb with VARYING and UNTIL options is:

A.  First time, identifier-1 is set equal to literal-2;

B.  Check condition-1 if true exit procedure-name

C.  Check condition-2 if true exit procedure-name

D.  Execute statements in procedure-name

E.  identifier-1 is incremented by literal-3

F.  Loop back to B.

Regards,
  
          ////
         (o o)
-oOO--(_)--OOo-

Whenever I find myself in a difficult situation, I ask myself "What
Would Jesus Do?"  The mental image of my opposition being cast into
pits of hellfire for all eternity *is* comforting, but probably not
what the inventors of the phrase had in mind.


Remove nospam to email me.

 Steve
```

#### ↳ Re: PerformVarying - Tables

- **From:** "Alan Russell" <RUSSELAH@apci.com>
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vpa1n$kcf@netnews1.apci.com>`
- **References:** `<7vp65o$lar$1@nnrp1.deja.com>`

```
The UNTIL clause on the PERFORM is tested BEFORE the paragraph is performed.
So if the correct entry is in position 5 of the table the paragraph is
performed with subscripts of 1,2,3,4 but not 5.  There are a number of
correct solutions to this problem which I'm sure others will be happy to
supply (SEARCH ALL, etc.).  But since your code seems to expect to always
find a match, the easiest way to fix your program without rewriting much of
it is to change the equal compare to greater than as well as eliminate the
IF...END-IF construct inside paragraphs 500, 600, and 700 since they are
essentially worthless.

Alan Russell, PhD, CCP
Work - Russelah@apci.com
Home - AHRussell@computer.org
Home page - http://members.aol.com/ahrussell
-------------------------------------------------------
The views expressed are mine alone and do not necessarily reflect those of
my employer

dc606@my-deja.com wrote in message <7vp65o$lar$1@nnrp1.deja.com>...
>I think the problem is with PERFORM VARYING statement.  Output is not
>correct.
…[143 more quoted lines elided]…
>Before you buy.
```

##### ↳ ↳ Re: PerformVarying - Tables

- **From:** "Anton Rusbach" <a.rusbach@coss.nl>
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vpc8j$724$1@news1.xs4all.nl>`
- **References:** `<7vp65o$lar$1@nnrp1.deja.com> <7vpa1n$kcf@netnews1.apci.com>`

```
> The UNTIL clause on the PERFORM is tested BEFORE the paragraph is
performed.

correct, unless you PERFORM WITH TEST AFTER UNTIL (Cobol85)


grtx,
Anton
```

#### ↳ Re: PerformVarying - Tables

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991103093302.14508.00001129@ngol04.aol.com>`
- **References:** `<7vp65o$lar$1@nnrp1.deja.com>`

```
In article <7vp65o$lar$1@nnrp1.deja.com>, dc606@my-deja.com writes:

>
>I think the problem is with PERFORM VARYING statement.  Output is not
…[8 more quoted lines elided]…
>Any idea why?

     <snip>

>
>          400-CREATE-SALARY-REPORT.
…[4 more quoted lines elided]…
>
           <snip>

            Each of these PERFORMs are doing a sequential/linear search
            of your table and moving EVERY entry to the print line EXCEPT
            the one you want.   This is because of the UNTIL condition that 
            is by default tested AFTER the procedures and subscript increment.
            You could just as easily remove the paragraph name from the
           perform and move the If test in the paragraph immediately after
           the perform.
```

#### ↳ Re: PerformVarying - Tables

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3822C9AE.BDB29B9A@zip.com.au>`
- **References:** `<7vp65o$lar$1@nnrp1.deja.com>`

```
dc606@my-deja.com wrote:
>  01  TITLE-VALUE.
>            05 PIC X(18) VALUE '010PRESIDENT'.
.. 8 lines snipped..
>            05 PIC X(18) VALUE '010ADM ASST'.
> 
…[5 more quoted lines elided]…
>            05  REPORT-TITLE            PIC X(10).

Over and above your problem did you notice that you redefined an extra
10 bytes.  Surprised this compiled.

Ken
```

##### ↳ ↳ Re: PerformVarying - Tables

- **From:** dc606@my-deja.com
- **Date:** 1999-11-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<801pk8$ok9$1@nnrp1.deja.com>`
- **References:** `<7vp65o$lar$1@nnrp1.deja.com> <3822C9AE.BDB29B9A@zip.com.au>`

```
Thanks for your comment.
Looking at my program again, just wondering is it considered "better"
coding if I put my Report-Title, Report-Location and Report-Education
together in working storage, i.e.

01  Reports.
    05 Report-Title         PIC X
    05 Report-Location      PIC
    05 Report-Education     PIC


Rather than putting them as follows:

       01  TITLE-TABLE REDEFINES TITLE-VALUE.
           05  TITLES OCCURS 10 TIMES.
               10  TITLE-CODE          PIC X(3).
               10  EXP-TITLE           PIC X(15).

           05  REPORT-TITLE            PIC X(10).


       01  LOCATION-TABLE REDEFINES LOCATION-VALUE.
           05   LOCATIONS OCCURS 5 TIMES.
                10  LOCATION-CODE       PIC X(3).
                10  EXP-LOCATION        PIC X(11).

           05  REPORT-LOCATION         PIC X(14).



       01  EDUCATION-TABLE REDEFINES EDUCATION-VALUE.
           05   EDUCATION OCCURS 6 TIMES.
                10  EDUCATION-CODE      PIC 9.
                10  EXP-EDUCATION       PIC X(14).

           05   REPORT-EDUCATION        PIC X(15).




In article <3822C9AE.BDB29B9A@zip.com.au>,
  Ken Foskey <waratah@zip.com.au> wrote:
> dc606@my-deja.com wrote:
> >  01  TITLE-VALUE.
…[16 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: PerformVarying - Tables

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38255C30.EF2A2BC@zip.com.au>`
- **References:** `<7vp65o$lar$1@nnrp1.deja.com> <3822C9AE.BDB29B9A@zip.com.au> <801pk8$ok9$1@nnrp1.deja.com>`

```
dc606@my-deja.com wrote:
> 
> Thanks for your comment.
…[31 more quoted lines elided]…
> 

Neither.. We really are heading into personal opinion here.

I prefer the layouts to be totally separate.  Memory is not a major
issue and a really smart compiler would eliminate the unused storage
(I don't think any would today).  This fulfils the 'least surprise'
rule.

Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
