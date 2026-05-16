[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question on Data Validation

_3 messages · 2 participants · 2000-05_

---

### Question on Data Validation

- **From:** "Masood Saiyed" <masood@lancashire77.freeserve.co.uk>
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fpu1f$l9n$1@news6.svr.pol.co.uk>`

```
Hi

I just wanted to ask a question on Data Validation.

For example,If I have got an INPUT file on disk which
needs to be validated:

 FD  INPUT-FILE.
 01  INPUT-RECORD.
     03  IN-PART-NUMBER          PIC X(6).
     03  IN-QUANTITY             PIC ?(4).

 My detail line for printing looks something like:

 01  P-DETAIL-LINE.
     03  P-PART-NUMBER           PIC X(6).
     03  FILLER                  PIC X(5).
     03  P-QUANTITY              PIC ??(4).

     Now the REQUIREMENT is IN-PART-NUMBER is alphanumeric and
     IN-QUANTITY is numeric to be a valid value.


          PROCEDURE DIVISION.
          .
          .
          IF IN-QUANTITY NOT NUMERIC THEN
line 100     MOVE IN-QUANTITY TO P-QUANTITY
          END-IF
          .
          .

 Now I have tried using PIC "9" at the first "?" and
                        PIC "X" at the second "??"......is this a usual
practise ?
or does it depend on the compiler used.

 Well the program runs PERFECT with me on my compiler Fujitsu v3..Now my
problem is
when I sent it to my teacher it came up with an ERROR:
     "Non-numeric data at line 100"  (They use MICRO FOCUS compiler)

 Please any one tell me what shall I do to overcome this error. Do I need to
move IN-QUANTITY to a working storage first and then check for numeric
?..just guessing...
or am I doing something else wrong here ? please advise.


Best Regards
MS
```

#### ↳ Re: Question on Data Validation

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2000-05-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39207db0.27458262@news.transport.com>`
- **References:** `<8fpu1f$l9n$1@news6.svr.pol.co.uk>`

```
Here is a trick you might want to consider:


03  IN-QUANTITY-X.
    04 IN-QUANTITY-9  PIC 9(4).

03  P-QUANTITY-X.
    04  P-QUANTITY-9 PIC 9(4).


IF IN-QUANTITY-9 NUMERIC
   MOVE IN-QUANTITY-9 TO P-QUANTITY-9
ELSE
   MOVE IN-QUANTITY-X TO P-QUANTITY-X
END-IF




On Mon, 15 May 2000 23:36:47 +0100, "Masood Saiyed"
<masood@lancashire77.freeserve.co.uk> wrote:

>Hi
>
…[49 more quoted lines elided]…
>
```

#### ↳ Re: Question on Data Validation

- **From:** "Masood Saiyed" <masood@lancashire77.freeserve.co.uk>
- **Date:** 2000-05-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fq0cu$n6d$1@news6.svr.pol.co.uk>`
- **References:** `<8fpu1f$l9n$1@news6.svr.pol.co.uk>`

```
Sorry pete,I didn't mention the whole INPUT-FILE FD in my
origional question,and the detail line was also partial only.

There are other various fields that needs validating - so if any
of the field is INVALID, I move 'Invalid Message' to
WS-MESSAGE-FIELD.
Then..

              IF IN-QUANTITY NOT NUMERIC THEN
                 MOVE 'Invalid Message' TO WS-MESSAGE-FIELD
              END-IF
              IF IN-FIELD-1 NOT NUMERIC THEN
                 MOVE 'Invalid Message' TO WS-MESSAGE-FIELD
              END-IF
              IF IN-FIELD-2 NOT NUMERIC THEN
                 MOVE 'Invalid Message' TO WS-MESSAGE-FIELD
              END-IF


              IF WS-MESSAGE-FIELD NOT EQUAL TO SPACES THEN
                 MOVE IN-QUANTITY TO P-QUANTITY
                 MOVE IN-FIELD-1  TO P-FIELD-1
                 MOVE IN-FIELD-2  TO P-FIELD-2
                 WRITE P-DETAIL-LINE FROM PRINT-REC
              END-IF

Sorry for any inconvenience..

Regards
MS.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
