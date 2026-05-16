[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# array

_6 messages · 5 participants · 1999-02 → 1999-03_

---

### array

- **From:** "Arlene B. Call" <abcall@sisna.com>
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cedcf0.0@news.sisna.com>`

```
Can anyone give me an example of a simply array using Cobol. I'm trying to
learn this language and it would help to see an example,
thanks
abcall@sisna.com
```

#### ↳ Re: array

- **From:** terrywin.nospam@spectra.net (Terry Winchester)
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cf0589.22563528@supernews.spectra.net>`
- **References:** `<36cedcf0.0@news.sisna.com>`

```
On Sat, 20 Feb 1999 09:09:54 -0700, "Arlene B. Call"
<abcall@sisna.com> wrote:

>Can anyone give me an example of a simply array using Cobol. I'm trying to
>learn this language and it would help to see an example,
>thanks
>abcall@sisna.com
>

Working-Storage..........
01  Idx                    Pic S9(3)  Value +0    Comp-3.
01  Nbr                    Pic  9(2)  Value 0.

01  The-Table.
    05  An-Array   occurs 10 times.
        10  An-Element     Pic  9(2). 

Procedure Division.......
Move Zeros to The-Table.

Perform Varying Idx from 1 by 1
Until Idx Greater Than 10
    Add 1 to Nbr
    Move Nbr to An-Element (Idx)
End-Perform.

Perform Varying Idx from 1 by 1
Until Idx Greater Than 10
    Display An-Element (Idx)
End-Perform.

HTH
Terry
```

#### ↳ Re: array

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36cfdc99.69351402@news3.ibm.net>`
- **References:** `<36cedcf0.0@news.sisna.com>`

```
On Sat, 20 Feb 1999 09:09:54 -0700, "Arlene B. Call" <abcall@sisna.com> wrote:

>Can anyone give me an example of a simply array using Cobol. I'm trying to
>learn this language and it would help to see an example,
>thanks
>abcall@sisna.com
>
Data Division.

01 German-Weekday-Table.
	05 PIC X(10) VALUE 'Montag'.
	05 PIC X(10) VALUE 'Dienstag'.
	05 PIC X(10) VALUE 'Mittwoch.
	05 PIC X(10) VALUE 'Donnerstag'.
	05 PIC X(10) VALUE 'Freitag'.
	05 PIC X(10) VALUE 'Sonnabend'.
	05 PIC X(10) VALUE 'Sonntag'.
01 REDEFINES German-Weekday-Table.
	05 G-Weekday PIC X(10) Occurs 7 TIMES.
77	DOW	PIC 9.

PROCEDURE DIVISION.
	ACCEPT DOW From Day-Of-Week
	DISPLAY 'The German weekday today is' G-Weekday(DOW)
	GOBACK
	.


HTH

Volker Bandke

(BSP GmbH)

with kind regards

Volker Bandke
(BSP GmbH)
```

#### ↳ Re: array

- **From:** Atta <vdbank@bigfoot.com>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E2693C.93F3AA51@hotmail.com>`
- **References:** `<36cedcf0.0@news.sisna.com>`

```
I'm not exactly sure of the full syntax as I have just started with tables
(called so in Cobol). I hope this will help you somewhat:

Variables
Table occurs 10 times : Num [4]   {So there are 10 fields in the array which
can hold 4 numeric characters each)
T-Sub : Num [2]

Now, every field in the array is written as Table(T-Sub).

"Arlene B. Call" wrote:

> Can anyone give me an example of a simply array using Cobol. I'm trying to
> learn this language and it would help to see an example,
> thanks
> abcall@sisna.com
```

#### ↳ Re: array

- **From:** Atta <vdbank@bigfoot.com>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E26CD3.A95F81B6@hotmail.com>`
- **References:** `<36cedcf0.0@news.sisna.com>`

```
I'm not exactly sure of the full syntax as I have just started with tables
(called so in Cobol). I hope this will help you somewhat:

Variables
Table occurs 10 times : Num [4]   {So there are 10 fields in the array which
can hold 4 numeric characters each)
T-Sub : Num [2]

Now, every field in the array is written as Table(T-Sub).

"Arlene B. Call" wrote:

> Can anyone give me an example of a simply array using Cobol. I'm trying to
> learn this language and it would help to see an example,
> thanks
> abcall@sisna.com
```

##### ↳ ↳ Re: array

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1999-03-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36E27815.E2EFA79D@ix.netcom.com>`
- **References:** `<36cedcf0.0@news.sisna.com> <36E26CD3.A95F81B6@hotmail.com>`

```
This example demonstrates assign values to a table by using a
REDEFINES.  ("FILLER" is optional and has been left out.)

01  ws-end-of-month-list.
     02          PIC X(24)  VALUE '312831303130313130313031'.
01              REDEFINES ws-end-of-month-list.
     02          OCCURS 12 TIMES.
         03 ws-eom-dd            PIC XX.

******************************************************************

This is a example of using a SEARCH verb against a one-dimensional
table. Note that the table elements have values assigned when the
program starts to execute, and that you will need to write code to load
data into the table

 01  Suspense-table.
     02  suspense-element           OCCURS 48 TIMES
                                                INDEXED  susp-index.
         03 suspense-code            PIC X        VALUE HIGH-VALUES.
         03  suspense-key             PIC X(27) VALUE SPACES.
..
..
..

SET susp-index TO 1.
SEARCH suspense-element
        AT END
            MOVE ZEROS TO file-key
        WHEN vjs-index NOT < ws-limit
             MOVE ZEROS TO file-key
         WHEN suspense-code  (susp-index) = some-field
             MOVE suspense-key (vjs-index) TO file-key.

Atta wrote:

> I'm not exactly sure of the full syntax as I have just started with
> tables (called so in Cobol). I hope this will help you somewhat:
…[15 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
