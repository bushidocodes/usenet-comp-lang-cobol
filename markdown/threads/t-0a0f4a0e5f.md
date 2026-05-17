[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IMS DB/DC Question#2?

_2 messages · 2 participants · 1995-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IMS DB/DC Question#2?

- **From:** "ca..." <ua-author-5306861@usenetarchives.gap>
- **Date:** 1995-04-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3nmq7g$dsq$2@heifetz.msen.com>`

```
Hi!



I have manage to come up with some COBOL code of my own based on
the specifications I provided earlier. Please evaluate and
comment on the logic used in order to accomplish the task based
on those specifications:



Below the ENTRY statement under the PROCEDURE DIVISION I have
this:



Perform 0100-UNQUAL-GN-ZP010SSA

UNTIL EOF-FLAG-SW = HIGH-VALUE



0100-UNQUAL-GN-ZP010SSA.

Move Spaces to ZP010ssa-LPAREN

Call "CBLTDLI" Using GN

ZPARTPCB

IO-AREA

ZP010SSA

Move "(" to ZP010SSA-LPAREN

IF ZPART-PCB-STATUS = BB

MOVE IO_AREA TO ZPAR010D

Perform 0200-ZP070-UNQ-GNP-CALL

ELSE

If Zpart-pcb-status = GE or GB

Move High-Value to Eof-Flag-Sw

Else

Call "COREDUMP".

0200-ZP070-UNQ-GNP-CALL.

Move Spaces to Zp070SSA-LPAREN

CALL "CBLTDLI" USING GNP

ZPARTPCB

IO-AREA

ZP070SSA

Move "(" to ZP070SSA-LPAREN.

IF Zpart-pcb-status = BB

Move IO-AREA to ZPAR070D

Perform 0400-CHK-ZPAR070D

If ZP070-IND-SORS = "N" or (ZP070-IND-SORS = "C"

AND ZP070-SPCL-NEW = "N")

PERFORM 0800-GU-ZPAR090D-PCB2.

0300-ZP010SSA-UNQ-GNP-CALL.

Move Spadces to Zp010ssa-Lparen

Call "CBLTDLI" Using GNP

ZPARTPCB

IO-AREA

ZP070SSA

Move "(" To ZP070SSA-Lparen

If Zpart-pcb-status = BB

Move IO-AREA to ZPAR070D

Perform 0400-CHK-ZPAR070D.

0400-CHK-ZPAR070D.

If Zp070-InD-SORS - "N" Or (ZP070-IND-SORS = "C"

And ZP070-SPCL-NEW = "N")

Perform 0800-GU-ZPAR090D-PCB2

If ZP090-DATE > "930601"

Perform 0500-GU-ZPAR050D.

0500-GU-ZPAR050D.

Move Zp050-Key to Zp050ssa-Keyval

Move Zp070-Prime-Supplier-Code to Zp040SSa-Supplier

Move Zp070-Year to Zp050ssa-Year, Zp040ssa-year

Move "64" to Zp050ssa-Date-Type

Call "CBLTDLI" Using GU

ZPARTPCB

ZP010SSA

ZP040SSA

ZP050SSA.

0600-ZPAR050.

If Zpart-pcb-status = BB or GE or GB

Move Io-area to Zp050SSA

Else

Call "COREDUMP"

If Zp090ssa-date-type = "02"

Move spaces to zp090-vehicle.

0800-GU-ZPAR090D-PCB2.

Move Zp090-key to Zp090ssa-keyval

Move Zp090-year to Zp090ssa-year

Move Spaces to Zp090-Vehicle

Move Zp090-yr2-year to ws-model-year

Move "02" to Zp090-DATE-TYPE

Call "CBLTDLI" Using GU

ZPARTPCB

IO-AREA

ZP010SSA

ZP090SSA

Move Zp070-YEAR To Zp070SSA-YEAR.

Detail-Line-mv-out.

String Zp010-Part-Pref Delimited by " "

" " Delimited by Size

ZP010-Part-Base Delimited by " "

" " Delimited by Size

ZP010-PART-SUFF Delimited by " "

" " Delimited by Size

Into WS-part-num

Move Zp070-Year to ws-model-year

Move zp070-ps-supp to ws-prim-suppl

Move zp090-date-mm to ws-part-added-date-mm

Move zp090-date-dd to ws-part-added-date-dd

Move zp090-date-yy to ws-part-added-date-yy

If Line-count < Lines-per-page

ADD 1 to Line-count

Else

Move Zero to Line-count.

EJECT

Copy MDLYEDRT.

EJECT


```

#### ↳ Re: IMS DB/DC Question#2?

- **From:** "marty..." <ua-author-17073867@usenetarchives.gap>
- **Date:** 1995-04-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0a0f4a0e5f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3nmq7g$dsq$2@heifetz.msen.com>`
- **References:** `<3nmq7g$dsq$2@heifetz.msen.com>`

```

For a variety of reasons [simplicity, auto-magic multi-file update
processing ], I set up the WS seg-area as follows (in pseudo-code):
01 seg name.
05 seg key.
10 seg key details (multiple).
05 FILLER REDEFINES
seg key.
10 FILLER PIC X(01).
88 NO-MORE-pcbname value high-value.
05 seg data.
10 seg data details (multiple).

Yeh, it _does_ assume that high-value is *not* a valid key value.
A reasonable assumption in the _real_ business world of alphamerics.

This allows me to code such statements as (in pseudo-code):
Get a seg
DOUntil no more PCBname
Process a seg
Get a seg
ENDdo


PS: Why, yes, being a DBA _does_ tend to spoil one.
---
* SLMR 2.1a * Real programmers use Patch Wires
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
