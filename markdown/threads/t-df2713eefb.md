[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol Quiz (for all of you who think you know what your doing.)

_10 messages · 10 participants · 2003-04_

---

### Cobol Quiz (for all of you who think you know what your doing.)

- **From:** "GoldenWing" <great1gw@hotmail.com>
- **Date:** 2003-04-20T16:53:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<va625659171pe7@corp.supernews.com>`

```
I need a little Help here guys....   Anything would be great...

1.  The A-margin covers ____________ in a line of COBOL code.
  a. columns  7 - 12
  b. columns 12 - 72
  c. columns  8 - 11
  d. columns  7 - 72
  e. none of these

2.   An alphanumeric field can contain ____________ .
  a. letters
  b. numbers
  c. blanks
  d. a and b
   e. a, b and c

3.  Which of the following symbols cannot be used in a picture clause of an
INPUT field?
  a. S
  b. X
  c. V
  d. Z
  e. all of the above can appear in an input field picture clause.

4.  Suppose the current date is January 2, 1999 and that FIELD-X has been
defined as a PIC 9(6).  What will be the contents of FIELD-X after execution
of the statement:
   ACCEPT FIELD-X FROM DATE.
  a. 010299
  b. 990102
  c. 020199
  d. 990201
  e. none of the above

5. The ASSIGN statement is found in the
 a.  IDENTIFICATION DIVISION
 b.  ENVIRONMENT DIVISION
 c.  DATA DIVISION
 d.  PROCEDURE DIVISION

6.   A group item:
 a.  Never has a PICTURE clause
 b.  Must be an 01 entry
 c.  May sometimes have both a  PICTURE and a VALUE clause

7. All of the following must begin in the B margin except:
 a.  SELECT statements
 b.  IF statements
 c.  01  level entries
 d.  PICTURE clause

8.  The ____________ statement can be used in place of numerous IF
statements when testing a field for multiple values.
  a. MOVE
  b. POSITIVE
  c. EVALUATE
  d. NEXT SENTENCE
  e. none of these

9.  A READ statement should be executed
  a. once for each input file
  b. once for each record to be input
  c. once for each field to be input
  d. after an EVALUATE statement

10. When a MOVE statement is executed
  a. the original value of the sending field is destroyed
  b. the original value of the receiving field is destroyed
  c. no data is destroyed


11. Examine the statement "MOVE  LNAME  TO  LNAME-OUT."  LNAME contains DOE
and LNAME-OUT has a picture of X(6).  The "b" below indicates a blank.  The
resulting value in LNAME-OUT will be:
 a. bbDOEb
 b. bbbDOE
 c. DOEbbb
 d. bbDOEb
 e. 000DOE


12. Given: SUBTRACT FIELD-A FROM FIELD-B.  Which of the following is/are
true?
 a. FIELD-A must be numeric
 b. FIELD-A may be either alphanumeric or numeric
 c. FIELD-A must be alphanumeric
 d. none of the above

13. Which of the following is not a valid COBOL math verb?
 a. ADD
 b. CALCULATE
 c. MULTIPLY
 d. DIVIDE
 e. all of the above are valid Cobol math verbs

14. What will be the value of A after execution of the statement:
 COMPUTE A = 2 * 3 ** 3 + 1.
 a. 19
 b. 217
 c. 1296
 d. 55
 e. none of the above


15.  An IF statement is used to implement the  ___________ structure.
  a. sequence
  b. selection
  c. iteration
  d. frame
  e. none of these


16. IF NPR-CUST-NUM < 0050 OR > 9900...        This is a _____________ test.
a. condition-name
 b. range
c. class
d. sign


17. To check to make sure that a field contains an entry, compare the
contents of the field to  ____________ .
  a. ZEROS
  b. SPACES


18.   Consider the following Cobol code segment:
 IF A = B
  IF C = D
   PERFORM W
  ELSE
   PERFORM X
 ELSE
   PERFORM Y.

Suppose A has a value of 2, B has a value of 3, C has a value of 4, and D
has a value of 4.  Which of
the following will be true?
 a.  Y will be executed
b.  W will be executed
c.  X will be executed
    d.  both W and Y will be executed


19. Given WA-FIELD-A contains 429847599, what happens when the statement
below executes?
 IF WA-FIELD-A NUMERIC
  MOVE "ERROR MESSAGE" TO DL-ERROR-OUT
  PERFORM B-300-ERRORS.

 a. B-300-ERRORS will be performed
 b. B-300-ERRORS will not be performed

20. Which of the following is NOT a valid sign test?
  a. NEGATIVE
  b. NUMERIC
  c. POSITIVE
  d. ZERO
  e. all of these are valid sign tests



21. A(n) ____________ PERFORM uses no paragraph name and is terminated with
an END-PERFORM.
  a. simple
  b. do-while
  c. in-line
  d. do-until
  e. complex


22. Consider the following instructions:  (Assume X has a PIC of 9)
  MOVE ZERO TO X.
  PERFORM A-MOD UNTIL X = 3.
  DISPLAY "HI".
  STOP RUN.
 A-MOD.
  ADD 1 TO X.
  DISPLAY X.

 What will appear on the monitor upon executing these instructions?  DISPLAY
allows you to print output on the monitor.
 a. HI.

 b.          0
             HI

 c.         1
             2
             3
             HI

 d.         3
             HI


Use the following code to answer the next question.

  WRITE REPORT-LINE-OUT FROM RH-1
AFTER ADVANCING 1 LINE.
  WRITE REPORT-LINE-OUT FROM RH-2
AFTER ADVANCING 2 LINES.
  WRITE REPORT-LINE-OUT FROM RH-3
AFTER ADVANCING 4 LINES.

23. How many blank lines appear between RH-2 and RH-3 in the printed output?
   a. 0
   b. 1
   c. 2
   d. 3
   e. 4

24. Suppose that FLDZ is described as PIC X(14) and contains the entry
"12#234#67#456#".  Suppose that FLDE, FLDF, FLDG, and FLDH are described as
PIC 999.  After exectution of the following statement, what value will be in
FLDF?

  UNSTRING FLDZ DELIMITED BY "#" INTO FLDE, FLDF, FLDG, FLDH.

  a. 12
  b. 456
  c. 67
  d. 234
  e. none of the above


25. A table whose data is contained in the DATA DIVISION is known as a(n)
____________ .
  a. loaded table
  b. key table
  c. input-loaded table
  d. linear table
  e. hard-coded table

26. A(n) ____________ is a numeric literal or field used to identify an
element within a table.
  a. buffer
  b. table limit
  c. delimiter
  d. subscript

27.   A subscript is enclosed in
 a. [   ]
 b. {   }
 c. (   )
 d. <  >
 e. none of the above


28. The ____________ clause specifies the number of times a field is
repeated in a table.
  a. INDEXED BY
  b. ASCENDING KEY
  c. VARYING
  d. OCCURS
  e. none of these


29. A SORT work file must be defined with a(n) ____________ entry in the
FILE SECTION.
  a. SELECT
  b. MD
  c. FD
  d. SD
  e. none of these




30. A control break occurs during processing when ____________ .
  a. the control field changes values
  b. the maximum number of lines on a page has been reached
  c. a READ statement is executed to retrieve the next record
  d. a file is closed in the wrap-up paragraph
e.   none of these

31  The LINKAGE Section occurs in a:
  a. sub-program
  b. main-program
  c. both the main-program and a sub-program
  d. none of the above

True or false:

    T      F 32.    VAR A  is a valid programmer-supplied name in COBOL.

    T      F    33. STOP-RUN is required to terminate a program.

    T      F 34. Division names and paragraph names must begin in the
B-margin.


    T      F 35.      Elementary items require a picture clause in their
definition.

    T      F 36.    A COBOL statement MULTIPLY A BY B will produce identical
results as
    COMPUTE A = A * B.

    T      F 37. A dollar sign ($) can be used as either a fixed or floating
character.

    T      F 38. When an AND is used in an IF statement, if one of the two
conditions is true, then the entire statement is true.

    T      F 39. When ELSE is used in an IF statement, the statement(s)
before the word ELSE are executed when the condition is false.

    T      F 40.    The WRITE statement contains a file name.

    T     F 41. Given:
            02  CUST-ACCT-NO  PIC X(10).
            Contents: 3334-AB7-6
            MOVE CUST-ACCT-NO (6:3) TO DL-ITEM-OUT.
           Moves "AB7" to DL-ITEM-OUT.  (true or false)

    T     F 42. When a PERFORM statement is used to transfer the flow of
logic to a paragraph, control returns to the statement following the PERFORM
once the end of the paragraph is encountered.

    T     F 43. The STRING command can be used to separate a single field
into multiple fields.


    T     F 44.    The INITIALIZE statement can be used to initialize a
group item that contains both numeric
    and alphanumeric fields.

    T     F 45. A sort-work file is a temporary file.

    T     F 46. An input file should be sorted before it is processed using
control breaks.

    T      F   47. A running total increments the value of a counter after
every record.

    T      F 48. In a subscript, at least one space is required between the
data name and the left parentheses.

    T      F 49. END-IF is an example of a scope-terminator.

    T      F 50. A rolling total increments the value of a counter after a
control break has occurred.


    T      F 51. For a COPY command to execute correctly, the file that is
copied into a program must be   compiled before the program that contains
the COPY command is compiled.

    T      F 52. When using a CALL statement, the data names specified must
be identical in both the called
    and calling programs.

    T      F 53. The name of the program specified in a CALL statement must
match exactly the program-id name of the sub-program.

    T      F 54. A COPY command can be used within the DATA DIVISION but not
within the
    PROCEDURE DIVISION.
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-04-21T00:08:01+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5v26avov14o5gn3lfsaq9eovis05ilf7uh@4ax.com>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```
On Sun, 20 Apr 2003 16:53:01 -0400 "GoldenWing" <great1gw@hotmail.com> wrote:

:>I need a little Help here guys....   Anything would be great...

These question seem quite trivial.

I would suggest making a more difficult quiz.

On the other hand, if you need help with a simple take home test ....
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-21T09:54:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea316fe_1@127.0.0.1>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```
ROFL!

This HAS to be the most blatant attempt to get homework done we have ever
seen in CLC.

"...a little help..."

So maybe you'd like a little help getting dressed in the morning, tying your
shoelaces, wiping your ass?

Get used to the fact there are some things you just have to do YOURSELF.

It is NOT a difficult test. If you bothered to spend even a few hours on the
subject you could pass it easily.

Grow up, and get with the program.

Pete.

<snipped beginner level COBOL test>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** docdwarf@panix.com
- **Date:** 2003-04-20T18:00:56-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7v5ao$s8p$1@panix1.panix.com>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```
In article <va625659171pe7@corp.supernews.com>,
GoldenWing <great1gw@hotmail.com> wrote:
>I need a little Help here guys....   Anything would be great...

Please do your own homework.

DD
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-04-20T17:29:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7v716$dfi$1@slb9.atl.mindspring.net>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```
A few answers that (while correct) will provide you *NO* help in doing
homework:
```

##### ↳ ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** LX-i <DanielJS@Knology.net>
- **Date:** 2003-04-20T19:49:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EA33FFF.1010908@Knology.net>`
- **References:** `<va625659171pe7@corp.supernews.com> <b7v716$dfi$1@slb9.atl.mindspring.net>`

```
William M. Klein wrote:
> A few answers that (while correct) will provide you *NO* help in doing
> homework:

dang...  :)  Thanks for a good laugh...

You know, I had been doing COBOL for about 2 1/2 years when I started 
learning VB and VBScript.  The guy who was training me would infuriate 
me - every question I asked him, his reply was "MSDN".  Finally, one 
time I asked him "how", and he took 2 minutes to show me around MSDN, 
and how to look things up myself.  I took off from there...

Searching manuals is a great skill to develop - I've picked up PHP very 
quickly, simply by searching the documentation for certain key words.  I 
wonder if they teach skills like that in college courses?  The only 
college programming course I had was ForTran (on a VAX), and they didn't 
teach it then...

I guess that's why "experience" is such an important part of a resume...


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~   /   \  /             Live from Montgomery, AL!   ~
~  /     \/       o                                  ~
~ /      /\   -   |       AIM:  LXi0007              ~
~ _____ /  \      |    E-mail:  DanielJS@Knology.net ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-21T01:54:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ea34071.182594904@news.optonline.net>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```
"GoldenWing" <great1gw@hotmail.com> wrote:

>I need a little Help here guys....   Anything would be great...

These questions are EASY for experienced COBOL programmers. If you did your
homework, you too might find them easy.
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-04-21T05:02:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yXKoa.213$_R3.17@newssvr19.news.prodigy.com>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```
Congratulate me -- I got zero wrong!  :)
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-21T22:13:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b7v66u$mnn$1@aklobs.kc.net.nz>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```
GoldenWing wrote:

> I need a little Help here guys....   Anything would be great...

I think that you have done an excellent job constructing this quiz, who 
will you be posing it to ?  

You could possibly put the correct number of END-IFs into this question as 
that is a preferred style, and the full stop on a separate line.

> 18.   Consider the following Cobol code segment:
>  IF A = B
…[5 more quoted lines elided]…
>    PERFORM Y.

Posting your quiz here may not have sensible though as some clueless 
students visit this site when they are failing and may think they can cheat 
by looking up the answers in a book and memorizing the sequence of the 
answers.

You wouldn't want that to happen, but then it is quite easy to detect who 
has actually paid attention in class, and who are failures.
```

#### ↳ Re: Cobol Quiz (for all of you who think you know what your doing.)

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-04-21T15:51:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b81416$2ae$1@peabody.colorado.edu>`
- **References:** `<va625659171pe7@corp.supernews.com>`

```

On 20-Apr-2003, "GoldenWing" <great1gw@hotmail.com> wrote:

> 1.  The A-margin covers ____________ in a line of COBOL code.
>   a. columns  7 - 12
…[3 more quoted lines elided]…
>   e. none of these

Who cares?   How many CoBOL programmers will be fired because they forgot what
an A-margin is?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
