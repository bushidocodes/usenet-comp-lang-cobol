[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Please help me!!!!

_6 messages · 6 participants · 1999-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Please help me!!!!

- **From:** "Sally Hall" <Hallsframpton@btinternet.com>
- **Date:** 1999-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77ium4$6nc$1@plutonium.btinternet.com>`

```
Hello Guys!

 I've been given this procedure in Pascal to put into a proper program.

 It's designed for a salesman who wants to know how much commission he can
earn on selling different products. If the product is in category A, he
charges 0.5% commission. If it's in category B, he can charge 1% commission.
If it's in category C, he can charge 2% commission. If it's in category D,
he can charge 2.5% commission.

Here's the procedure code:

PROCEDURE DIVISION.
SALES-SEG.
    ACCEPT PRODUCT=CODE.
    ACCEPT SALE=VALUE.
COMM-SEL.
    IF PRODUCT-CODE NOT = "A" GO TO COMM-OR-2.
      MUTLIPLY 0.005 BY SALE-VALUE GIVING COMMISSION,
    GO TC COMM-END.
COMM-OR-2.
    IF PRODUCT-CODE NOT = "B" GO TO COMM-OR-3.
      MULTIPLY 0.01 BY SALE-VALUE GIVING COMMISSION,
    GO TO COMM-END.
COMM-OR-3.
    IF PRODUCT-CODE NOT = "C" GO TO COMM-OR-4.
      MULTIPLY 0.02 BY SALE-VALUE GIVING COMMISSION.
    GO TO COMM-END.
COMM-OR-4.
      MULTIPLY 0.025 BY SALE-VALUE GIVING COMMISSION.
COMM-END.
    DISPLAY CONFIRMATION. STOP RUN.
SALES-END.

Thanks ever so much!!!!



Tony Hall

(please send your reply to 056540@gloscat.ac.uk as well as
tonyhall@btinternet.com)
```

#### ↳ Re: Please help me!!!!

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369d3e39.80018208@news1.ibm.net>`
- **References:** `<77ium4$6nc$1@plutonium.btinternet.com>`

```
On Wed, 13 Jan 1999 20:15:39 -0000, "Sally Hall"
<Hallsframpton@btinternet.com> wrote:

>Hello Guys!
>
…[36 more quoted lines elided]…
>Tony Hall


Tony!  PLEASE consider a more structured approach!!!  How about an
Evaluate 

ie

Evaluate Product-Code
   When "A"
       Multiply........
   When "B"
       Multiply .......
   When "C"
       Multiply .......
End-Evaluate
```

##### ↳ ↳ Re: Please help me!!!!

- **From:** "Jerry Peacock" <bismail@bisusa.com>
- **Date:** 1999-01-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77jl8m$pq7$1@holly.prod.itd.earthlink.net>`
- **References:** `<77ium4$6nc$1@plutonium.btinternet.com> <369d3e39.80018208@news1.ibm.net>`

```

Thane Hubbell wrote in message <369d3e39.80018208@news1.ibm.net>...

>Tony!  PLEASE consider a more structured approach!!!  How about an
>Evaluate
…[11 more quoted lines elided]…
>

Or even (shudder)
IF PRODUCT-CODE = "A"
    MULTIPLY....
ELSE
    IF PRODUCT-CODE = "B"
        MULTIPLY...
    ELSE
        IF PRODUCT-CODE = "C"
            MULTIPLY...
>
```

#### ↳ Re: Please help me!!!!

- **From:** Alex Romaniuk <ales.romaniuk@zag.si>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369E28E5.7D91@zag.si>`
- **References:** `<77ium4$6nc$1@plutonium.btinternet.com>`

```
Sally Hall wrote:
> PROCEDURE DIVISION.
> SALES-SEG.
…[25 more quoted lines elided]…
> tonyhall@btinternet.com)

There could be more efficient code like:

 PROCEDURE DIVISION.
 SALES-SEG.
     ACCEPT PRODUCT-CODE.
     ACCEPT SALE-VALUE.
     EVALUATE PRODUCT-CODE
        WHEN  "A"    MULTIPLY 0.005 BY SALE-VALUE GIVING COMMISSION
        WHEN  "B"    MULTIPLY 0.01  BY SALE-VALUE GIVING COMMISSION
        WHEN  "C"    MULTIPLY 0.02  BY SALE-VALUE GIVING COMMISSION
        WHEN  "D"    MULTIPLY 0.025 BY SALE-VALUE GIVING COMMISSION
        WHEN OTHER DISPLAY "WHAT IS WRONG ???"
     END-EVALUATE
     DISPLAY CONFIRMATION. STOP RUN.
 SALES-END.

or in Pascal

   READLN(PRODUCT-CODE);
   READLN(SALE-VALUE);
   CASE PRODUCT-CODE OF
      'A': COMMISSION := SALE-VALUE * 0.005 ;
      'B': COMMISSION := SALE-VALUE * 0.01 ;
      'C': COMMISSION := SALE-VALUE * 0.02 ;
      'D': COMMISSION := SALE-VALUE * 0.025 ;
      else
         WRITELN('WHAT IS WRONG ???');
   END ;
   WRITELN(CONFIRMATION);
```

#### ↳ Re: Please help me!!!!

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5Tvn2.3243$hE2.20528302@storm.twcol.com>`
- **References:** `<77ium4$6nc$1@plutonium.btinternet.com>`

```
>PROCEDURE DIVISION.
>SALES-SEG.
…[18 more quoted lines elided]…
>SALES-END.


First, for a little criticism...never ever use GO TO statements.

But maybe try this:

WORKING-STORAGE SECTION.
01  COMMISSION-RATE-DATA.
    05 FILLER       PIC X(22)
       VALUE '0005  0010  0020  0025'.
01  FILLER REDEFINES COMMISSION-RATE-DATA.
    05 COMMISSION-RATE OCCURS 4 TIMES
                    PIC 9V999.
01  COMMISSION-SUB  PIC 999.

PROCEDURE DIVISION.
SALES-SEG.
     ACCEPT PRODUCT-CODE
     ACCEPT SALE-VALUE
     COMPUTE COMMISSION-SUB = FUNCTION ORD(PRODUCT-CODE)
                              - ORD('A') +1
     IF COMMISSION-SUB > 0 AND < 5 THEN
        MULTIPLY COMMISSION-RATE(COMMISSION-SUB)
              BY SALE-VALUE
          GIVING COMMISSION
     ELSE
        DISPLAY "WHAT IS WRONG ???"
     END-IF
     DISPLAY CONFIRMATION
     STOP RUN
     .
```

##### ↳ ↳ Re: Please help me!!!!

- **From:** e=mc^3@netcom.com (Richard Anderson)
- **Date:** 1999-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77o5mk$lr4@dfw-ixnews8.ix.netcom.com>`
- **References:** `<77ium4$6nc$1@plutonium.btinternet.com> <5Tvn2.3243$hE2.20528302@storm.twcol.com>`

```
On Thu, 14 Jan 1999 19:22:32 -0500, "Jeff" <a@a.com> wrote:

>>PROCEDURE DIVISION.
>>SALES-SEG.
…[51 more quoted lines elided]…
>
You have GOT to be kidding!  Know thee not the EVALUATE construct?

Rick Anderson
Seattle
anderson  ï¿½atï¿½  pobox  ï¿½fullstopï¿½  com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
