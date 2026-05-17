[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Inline performs and ifs

_8 messages · 8 participants · 1996-09 → 1996-10_

---

### Inline performs and ifs

- **From:** "sosh..." <ua-author-15564211@usenetarchives.gap>
- **Date:** 1996-09-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<52qglp$5qr@granny.mac.co.nz>`

```

When I run the code below, if the condition TITLE-MR is true control
jumps straight to the END-PERFORM causing an infinite loop.
Can anyone tell me why?.
There is only one full stop and that is after the END-PERFORM.

DD-PROCESS-LABELS SECTION.
*Read up to 5 records from the ip file into a table then
*call the print routine
PERFORM VARYING WA-LABEL-NUMBER FROM 1 BY 1
UNTIL WA-LABEL-NUMBER > 5

IF TITLE-MR
MOVE WC-MR TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
IF TITLE-MRS
MOVE WC-MRS TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
MOVE FI-TITLE TO WT-TITLE(WA-LABEL-NUMBER)
END-IF

MOVE FI-INITIAL1 TO WT-INITIAL1(WA-LABEL-NUMBER)
MOVE FI-INITIAL2 TO WT-INITIAL2(WA-LABEL-NUMBER)
MOVE FI-SURNAME TO WT-SURNAME(WA-LABEL-NUMBER)
MOVE FI-STREET-ADDRESS TO
WT-STREET-ADDRESS(WA-LABEL-NUMBER)
MOVE FI-CITY TO WT-CITY(WA-LABEL-NUMBER)

PERFORM ZA-READ-INPUT-FILE

IF NO-MORE-RECORDS
MOVE 6 TO WA-LABEL-NUMBER
END-IF
END-PERFORM.
```

#### ↳ Re: Inline performs and ifs

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1996-09-29T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58ff8ee6bd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<52qglp$5qr@granny.mac.co.nz>`
- **References:** `<52qglp$5qr@granny.mac.co.nz>`

```

Stephen OShaughnessy wrote:
› 
› When I run the code below,  if the condition TITLE-MR is true control
…[18 more quoted lines elided]…
›                  ^                   |
+------------+
|
This END-IF is paired with the IF TITLE-MRS...ELSE construct, forcing the IF TITLE-MR
to be paired with the END-IF just before the END-PERFORM.


Del.
```

#### ↳ Re: Inline performs and ifs

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-09-29T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58ff8ee6bd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<52qglp$5qr@granny.mac.co.nz>`
- **References:** `<52qglp$5qr@granny.mac.co.nz>`

```

In message <<52qglp$5.··.@gra··o.nz>> sos··.@net··o.nz writes:
› jumps straight to the END-PERFORM causing an infinite loop. 
› Can anyone tell me why?.
…[11 more quoted lines elided]…
› 
You need an END-IF for each and every IF.

IF Title-MR
....
ELSE
IF Title-MRS
....
ELSE
.....
END-IF
END-IF

Without the 2nd END-IF the whole of the rest of the PERFORM is
part of the ELSE to IF Title-MR
```

#### ↳ Re: Inline performs and ifs

- **From:** "emi..." <ua-author-17086441@usenetarchives.gap>
- **Date:** 1996-09-30T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58ff8ee6bd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<52qglp$5qr@granny.mac.co.nz>`
- **References:** `<52qglp$5qr@granny.mac.co.nz>`

```

In article <52qglp$5.··.@gra··o.nz>, sos··.@net··o.nz says...
› 
› When I run the code below,  if the condition TITLE-MR is true control
…[31 more quoted lines elided]…
›           END-PERFORM.	

===============================================================
Add a second END-IF after the first in Your section.
A good habbit is count the number of your if-statements.
The number of end-if-statements must be equal.
hlj, Helsinki
===============================================================
```

#### ↳ Re: Inline performs and ifs

- **From:** "guyf..." <ua-author-17071752@usenetarchives.gap>
- **Date:** 1996-09-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58ff8ee6bd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<52qglp$5qr@granny.mac.co.nz>`
- **References:** `<52qglp$5qr@granny.mac.co.nz>`

```

sos··.@net··o.nz (Stephen OShaughnessy) wrote:

› When I run the code below,  if the condition TITLE-MR is true control
› jumps straight to the END-PERFORM causing an infinite loop. 
› Can anyone tell me why?.
› There is only one full stop and that is after the END-PERFORM.
 
›  DD-PROCESS-LABELS SECTION.
›      *Read up to 5 records from the ip file into a table then
›      *call the print routine
›           PERFORM VARYING WA-LABEL-NUMBER FROM 1 BY 1
›                   UNTIL WA-LABEL-NUMBER > 5
 
›                IF TITLE-MR
›                   MOVE WC-MR TO WT-TITLE(WA-LABEL-NUMBER)
…[5 more quoted lines elided]…
›                END-IF
 
›               MOVE FI-INITIAL1 TO WT-INITIAL1(WA-LABEL-NUMBER)
›               MOVE FI-INITIAL2 TO WT-INITIAL2(WA-LABEL-NUMBER)
…[3 more quoted lines elided]…
›               MOVE FI-CITY     TO WT-CITY(WA-LABEL-NUMBER)
 
›               PERFORM ZA-READ-INPUT-FILE
›           
…[3 more quoted lines elided]…
›           END-PERFORM.

IF TITLE-MR
MOVE WC-MR TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
IF TITLE-MRS
MOVE WC-MRS TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
MOVE FI-TITLE TO WT-TITLE(WA-LABEL-NUMBER)
END-IF

Try adding the following line here:
END-IF

All of the code following the first else statement would be treated as a
continuation of that statement. I believe that if you use END-IF with one
IF, nested IF's will also require END-IF. When I use nested IF statements
I do the following:

IF

END-IF

I then fill in the condition following the IF and then code between the IF
and the END-IF and do the same again if there is a nested IF.

I prefer the EVALUATE method. Try the following alternative

EVALUATE variable-name
WHEN TITLE-MR
MOVE WC-MR TO WT-TITLE(WA-LABEL-NUMBER)
WHEN TITLE-MRS
MOVE WC-MRS TO WT-TITLE(WA-LABEL-NUMBER)
WHEN OTHER
MOVE FI-TITLE TO WT-TITLE(WA-LABEL-NUMBER)
END-EVALUATE


MOVE FI-INITIAL1 TO WT-INITIAL1(WA-LABEL-NUMBER)
MOVE FI-INITIAL2 TO WT-INITIAL2(WA-LABEL-NUMBER)
MOVE FI-SURNAME TO WT-SURNAME(WA-LABEL-NUMBER)
MOVE FI-STREET-ADDRESS TO
WT-STREET-ADDRESS(WA-LABEL-NUMBER)
MOVE FI-CITY TO WT-CITY(WA-LABEL-NUMBER)
PERFORM ZA-READ-INPUT-FILE

IF NO-MORE-RECORDS
MOVE 6 TO WA-LABEL-NUMBER
END-IF
END-PERFORM.

Either way you go should work. By the way, I'm glad to see that I'm not
the only one that still uses all upper case (most of the time anyway) when
coding.
```

#### ↳ Re: Inline performs and ifs

- **From:** "lsv..." <ua-author-13441627@usenetarchives.gap>
- **Date:** 1996-10-01T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58ff8ee6bd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<52qglp$5qr@granny.mac.co.nz>`
- **References:** `<52qglp$5qr@granny.mac.co.nz>`

```

In <52qglp$5.··.@gra··o.nz>, sos··.@net··o.nz (Stephen OShaughnessy) writes:
› When I run the code below,  if the condition TITLE-MR is true control
› jumps straight to the END-PERFORM causing an infinite loop. 
…[15 more quoted lines elided]…
› 
It is poor style to monkey with the control variable in a PERFORM.
You mislead the reader as to what is going on. If you must change
WA-LABEL-NUMBER inside the loop do it only there:

MOVE 1 TO WA-LABEL-NUMBER
PERFORM UNTIL WA-LABEL-NUMBER > 5
...
IF NO-MORE-RECORDS
MOVE 6 TO WA-LABEL-NUMBER
ELSE
ADD 1 TO WA-LABEL-NUMBER
END-IF
END-PERFORM
```

#### ↳ Re: Inline performs and ifs

- **From:** "glenn amy" <ua-author-17071700@usenetarchives.gap>
- **Date:** 1996-10-03T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58ff8ee6bd-p7@usenetarchives.gap>`
- **In-Reply-To:** `<52qglp$5qr@granny.mac.co.nz>`
- **References:** `<52qglp$5qr@granny.mac.co.nz>`

```

Stephen OShaughnessy wrote:
› 
› When I run the code below,  if the condition TITLE-MR is true control
…[21 more quoted lines elided]…
›            END-PERFORM.

You are missing an end-if. The move statements that follow become
conditional under the 'else'. The else is not terminated until the
implicit scope terminator (the period) is found on the end-perform.

Try this:

IF TITLE-MR
MOVE WC-MR TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
IF TITLE-MRS
MOVE WC-MRS TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
MOVE FI-TITLE TO WT-TITLE(WA-LABEL-NUMBER)
add -> END-IF
END-IF

Good luck!
Glenn Amy                | If you need something but do not buy it,
EDS CA-XIX               | you will pay for it without getting it. 
sac··.@e··.com  | H. Ford
```

#### ↳ Re: Inline performs and ifs

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-10-06T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-58ff8ee6bd-p8@usenetarchives.gap>`
- **In-Reply-To:** `<52qglp$5qr@granny.mac.co.nz>`
- **References:** `<52qglp$5qr@granny.mac.co.nz>`

```

sos··.@net··o.nz (Stephen OShaughnessy) wrote:

› When I run the code below,  if the condition TITLE-MR is true control
› jumps straight to the END-PERFORM causing an infinite loop. 
› Can anyone tell me why?.
› There is only one full stop and that is after the END-PERFORM.
 
›  DD-PROCESS-LABELS SECTION.
›      *Read up to 5 records from the ip file into a table then
›      *call the print routine
›           PERFORM VARYING WA-LABEL-NUMBER FROM 1 BY 1
›                   UNTIL WA-LABEL-NUMBER > 5
 
›                IF TITLE-MR
›                   MOVE WC-MR TO WT-TITLE(WA-LABEL-NUMBER)
…[5 more quoted lines elided]…
›                END-IF
 
›               MOVE FI-INITIAL1 TO WT-INITIAL1(WA-LABEL-NUMBER)
›               MOVE FI-INITIAL2 TO WT-INITIAL2(WA-LABEL-NUMBER)
…[3 more quoted lines elided]…
›               MOVE FI-CITY     TO WT-CITY(WA-LABEL-NUMBER)
 
›               PERFORM ZA-READ-INPUT-FILE
›           
…[3 more quoted lines elided]…
›           END-PERFORM.

I reformated your code through my editor (removing blank lines within
the PERFORM). Is this what the computer is seeing:

PERFORM VARYING WA-LABEL-NUMBER FROM 1 BY 1
UNTIL WA-LABEL-NUMBER > 5
IF TITLE-MR
MOVE WC-MR TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
IF TITLE-MRS
MOVE WC-MRS TO WT-TITLE(WA-LABEL-NUMBER)
ELSE
MOVE FI-TITLE TO WT-TITLE(WA-LABEL-NUMBER)
END-IF
MOVE FI-INITIAL1 TO WT-INITIAL1(WA-LABEL-NUMBER)
MOVE FI-INITIAL2 TO WT-INITIAL2(WA-LABEL-NUMBER)
MOVE FI-SURNAME TO WT-SURNAME(WA-LABEL-NUMBER)
MOVE FI-STREET-ADDRESS
TO WT-STREET-ADDRESS(WA-LABEL-NUMBER)
MOVE FI-CITY TO WT-CITY(WA-LABEL-NUMBER)
PERFORM ZA-READ-INPUT-FILE
IF NO-MORE-RECORDS
MOVE 6 TO WA-LABEL-NUMBER
END-IF
(An implied END-IF here)
END-PERFORM
.

You might want to check where to put the missing END-IF statement
(always match your END-IFs to your IFs).

Boyce Williams
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
