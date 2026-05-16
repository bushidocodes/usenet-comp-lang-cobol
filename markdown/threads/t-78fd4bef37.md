[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File formatting.

_3 messages · 3 participants · 1999-05_

---

### File formatting.

- **From:** "John" <nospam@nospam-please.com>
- **Date:** 1999-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DoEZ2.3184$%x.2654@wards>`

```
I am writing a program in Cobol to convert an ASCII file into a formatted
file so that I can import the files into a database.

The original file has different length fields with fields in different
places - eg. NAME[Neil Capel]AGE[21]ADD1[------- etc.

I want to read a line at a time and then look at each character for [ and ].
Do I have to move the read line into, say -
 1 conv-line.
     3 1char  x.
     3 2char  x.
     3 3char  x.

etc.

and then look at each character?  Is there a better way?  PLEASE HELP.

Also I will need to search and replace - is it possible to replace end of
line chars with spaces?  How do I look for end of line chars.

Please e-mail me:

neilc@1sitedesigns.net
```

#### ↳ Re: File formatting.

- **From:** "Warren Porter" <warrenp123@netdoor123.com>
- **Date:** 1999-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<udFZ2.102$r14.11510@axe.netdoor.com>`
- **References:** `<DoEZ2.3184$%x.2654@wards>`

```

John wrote in message ...
>I am writing a program in Cobol to convert an ASCII file into a formatted
>file so that I can import the files into a database.
…[4 more quoted lines elided]…
>I want to read a line at a time and then look at each character for
[ and ].
>  Is there a better way?  PLEASE HELP.

Yes.  Try the UNSTRING statement.  First define a numeric field to help with
this statment:   01  WS-POINT    PIC 999.    I also assume you would define
FIELD-NAME and FIELD-DATA there as well. Then in the procedure division:

MOVE 1 TO WS-POINT.

And within a loop or PERFORM statement:

IF IN-REC(WS-POINT:1) NOT = SPACE
  UNSTRING IN-REC DELIMITED BY "[" INTO FIELD-NAME POINTER WS-POINT
  UNSTRING IN-REC DELIMITED BY "]" INTO FIELD-DATA POINTER WS-POINT
   ... Code to process each field would go here.

>
>Also I will need to search and replace - is it possible to replace end of
>line chars with spaces?  How do I look for end of line chars.

Define your input file ORGANIZATION LINE SEQUENTIAL and you won't have to.
Short lines will be padded out with spaces.  The IF statement checks to see
if you have reached the end.


Warren Porter -- Remove numbers to reply.
```

#### ↳ Re: File formatting.

- **From:** Ed Milne <emilne@my-dejanews.com>
- **Date:** 1999-05-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7h7gcl$ir5$1@nnrp1.deja.com>`
- **References:** `<DoEZ2.3184$%x.2654@wards>`

```
In article <DoEZ2.3184$%x.2654@wards>,
  "John" <nospam@nospam-please.com> wrote:
> The original file has different length fields with fields in different
> places - eg. NAME[Neil Capel]AGE[21]ADD1[------- etc.
>
> I want to read a line at a time and then look at each character for [
and ].

Here's another way to use the UNSTRING statement to analys=ze the
contents of the line.

 77  sub1                        VALUE ZERO   COMP   PIC S9(4).
 01  work-line                                       PIC X(100).
 01  my-table.
     05 my-item    OCCURS 3.
       10 my-word                                    PIC X(10).
       10 my-data                                    PIC X(50).
 01  myrec-rec.
     05 myrec-name                                   PIC X(15).
     05 myrec-age                                    PIC X(02).
     05 myrec-add1                                   PIC X(25).
*
 PROCEDURE DIVISION.
     MOVE 'NAME[Neil Capel]AGE[21]ADD1[---]'
       TO work-line
     UNSTRING work-line
       DELIMITED BY '[' OR ']'
       INTO my-word(1)
            my-data(1)
            my-word(2)
            my-data(2)
            my-word(3)
            my-data(3)
     PERFORM
       VARYING sub1 FROM 1 BY 1
       UNTIL sub1 > 3 OR
             my-word(sub1) = SPACE
       EVALUATE my-word(sub1)
       WHEN 'NAME'
         MOVE my-data(sub1)          TO myrec-name
       WHEN 'AGE'
         MOVE my-data(sub1)          TO myrec-age
       WHEN 'ADD1'
         MOVE my-data(sub1)          TO myrec-add1
       END-EVALUATE
     END-PERFORM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
