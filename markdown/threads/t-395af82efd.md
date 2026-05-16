[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# debugging

_10 messages · 6 participants · 2006-02_

---

### debugging

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-02-27T18:39:00+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44033aaa$0$29469$ba620e4c@news.skynet.be>`

```
Could some people help me debugging the DATA DIVISION of that script that 
compute a Gaz Bill ?

       IDENTIFICATION DIVISION.
        PROGRAM-ID. FACTURE GAZ.
       ENVIRONMENT DIVISION.
        CONFIGURATION SECTION.
         SOURCE-COMPUTER. CPU1.
         OBJECT-COMPUTER. CPU1.
       DATA DIVISION.
        WORKING-STORAGE SECTION.
         77 NW-FACT PIC X.
            88 FOK VALUES "O", "o".
            88 FKO VALUES "N", "n".
         77 NM PIC X(16).
         77 CONS PIC 9(3)V99; COMP 3.
            88 T1 VALUES 1.00 THRU 19.99.
            88 T2 VALUES 20.00 THRU 49.99.
            88 T3 VALUES 50.00 THRU 999.00.
         01 VOL.
            02 C1 PIC 99V99.
            02 C2 PIC 99V99.
            02 C3 PIC 9(3)V99.
         77 TOT PIC 9(6)V9(3); COMP 3.
         77 TOT-ED PIC E(5)9.9(3).
         77 TVA PIC 9(5)V9(3); COMP 3.
         77 CONS-ED PIC *(5)9.99.
         77 CPT PIC 99; COMP 0; VALUE 30.

       PROCEDURE DIVISION.
      *structure
       PROG.
           PERFORM D-PROG.
           PERFORM FACT UNTIL FKO.
           PERFORM F-PROG.
       FACT.
           PERFORM D-FACT.
           PERFORM CONS UNTIL CONS > 0.
           PERFORM I-FACT.
           PERFORM A21.
           PERFORM A22.
           PERFORM A23.
           PERFORM F-FACT.

      *traitement
       D-PROG.
           DISPLAY "nom client ?".
           ACCEPT NW-FACT.
       F-FACT.
           DISPLAY "CONSOMMATION ?".
           ACCEPT CONS.
       CONS.
           DISPLAY "Reintro consommation".
           ACCEPT CONS.
       I-FACT.
           EXIT.
       A21.
           MOVE CONS TO C1.
       A22.
           MOVE 20 TO C1.
           SUBTRACT C1 FROM CONS GIVING C2.
       A23.
           MOVE 20 TO C1.
           MOVE 30 TO C2.
           SUBTRACT C1, C2 FROM CONS GIVING C3.
       F-FACT.
           MOVE CONS TO CONS-ED.
           DISPLAY (1,1) ERASE.
           DISPLAY "NOM : ", NW-FACT, "      CONSOMMATION : ", CONS-ED.
           DISPLAY (5,1) "LOCATION DU COMPTEUR".
           DISPLAY (5,20) CPT.
           DISPLAY (7,1) "TARIF 1 ", C1, " m3 . .45E".
           MULTIPLY .45 BY C1.
           DISPLAY (7,20) C1.
           DISPLAY (8,1) "TARIF 2 ", C2, " m3 . .55E".
           MULTIPLY .55 BY C2.
           DISPLAY (8,20) C2.
           MULTIPLY .7 BY C3.
           DISPLAY (9,1) "TARIF 3 ", C3, " m3 . .7E".
           DISPLAY (9,20) C3.
           ADD C1, C2, C3 TO TOT.
           MOVE TOT TO TOT-ED.
           DISPLAY (11,1) "TOTAL DES CONSOMMATIONS : ", TOT-ED.
           MULTIPLY .14 BY TOT GIVING TVA.
           MOVE TVA TO TOT-ED.
           DISPLAY (12,1) "TVA SUR LES CONSOMMATIONS : ", TOT-ED.
           DISPLAY (14,1) "A PAYER : ".
           ADD TVA TO TOT GIVING TOT-ED.
           DISPLAY (14,20) TOT-ED.
           DISPLAY (17,1) "NOUVELLE FACTURE (O/N) ?".
           ACCEPT (17,20) NW-FACT.
       F-PROG.
           EXIT.

** COMPILATION ERRORS

Object filename [FFACTURE.INT]: Listing filename [NUL.LST]:
** Scanning Environment Division...
** Scanning Data Division...
0013:/W/Terminal period assumed above.
0012:/W/Level 01 assumed.
0012:Group item,therefore PIC/JUST/BLANK/SYNC is ignored.
0014:Name omitted; entry bypassed. 88
  14              88 T1 VALUES 1.00 THRU 19.99.
0015:VALUE disallowed--OCCURS/REDEFINES/type/size conflict. 2000
  15              88 T2 VALUES 20.00 THRU 49.99.
0015:VALUE disallowed--OCCURS/REDEFINES/type/size conflict. 4999
0016:VALUE disallowed--OCCURS/REDEFINES/type/size conflict. 5000
  16              88 T3 VALUES 50.00 THRU 999.00.
0016:VALUE disallowed--OCCURS/REDEFINES/type/size conflict. 99900
  17           01 VOL.
0021:/W/Terminal period assumed above.
0020:/W/Level 01 assumed.
0020:Group item,therefore PIC/JUST/BLANK/SYNC is ignored.
0022:Name omitted; entry bypassed. 77
  22           77 TOT-ED PIC E(5)9.9(3).
0023:/W/Terminal period assumed above.
0022:/W/Level 01 assumed.
0022:Group item,therefore PIC/JUST/BLANK/SYNC is ignored.
0024:Name omitted; entry bypassed. 77
  24           77 CONS-ED PIC *(5)9.99.
0025:/W/Terminal period assumed above.
0025:Unrecognizable element is ignored.  0
0025:Unrecognizable element is ignored.  VALUE
  25           77 CPT PIC 99; COMP 0; VALUE 30.
0024:/W/Level 01 assumed.
0024:Group item,therefore PIC/JUST/BLANK/SYNC is ignored.
  26
0027:Name omitted; entry bypassed. PROCEDURE
  27         PROCEDURE DIVISION.
0029:Unrecognizable element is ignored.  PROG
0030:Unrecognizable element is ignored.  PERFORM
  30             PERFORM D-PROG.
0030:Unrecognizable element is ignored.  D-PROG
0031:Unrecognizable element is ignored.  PERFORM
0031:Unrecognizable element is ignored.  FACT
0031:Unrecognizable element is ignored.  UNTIL
  31             PERFORM FACT UNTIL FKO.
0031:Unrecognizable element is ignored.  FKO
0032:Unrecognizable element is ignored.  PERFORM
  32             PERFORM F-PROG.
0032:Unrecognizable element is ignored.  F-PROG
  33         FACT.
0033:Unrecognizable element is ignored.  FACT
0034:Unrecognizable element is ignored.  PERFORM
  34             PERFORM D-FACT.
0034:Unrecognizable element is ignored.  D-FACT
0035:Unrecognizable element is ignored.  PERFORM
0035:Unrecognizable element is ignored.  CONS
0035:Unrecognizable element is ignored.  UNTIL
0035:Unrecognizable element is ignored.  CONS
0035:Unrecognizable element is ignored.  >
  35             PERFORM CONS UNTIL CONS > 0.
0035:Unrecognizable element is ignored.  0
0036:Unrecognizable element is ignored.  PERFORM
  36             PERFORM I-FACT.
0036:Unrecognizable element is ignored.  I-FACT
0037:Unrecognizable element is ignored.  PERFORM
  37             PERFORM A21.
0037:Unrecognizable element is ignored.  A21
0038:Unrecognizable element is ignored.  PERFORM
  38             PERFORM A22.
0038:Unrecognizable element is ignored.  A22
0039:Unrecognizable element is ignored.  PERFORM
  39             PERFORM A23.
0039:Unrecognizable element is ignored.  A23
0040:Unrecognizable element is ignored.  PERFORM
  40             PERFORM F-FACT.
0040:Unrecognizable element is ignored.  F-FACT
  41
0043:Unrecognizable element is ignored.  D-PROG
0044:Unrecognizable element is ignored.  DISPLAY
  44             DISPLAY "nom client ?".
0044:Unrecognizable element is ignored.  nom client ?
0045:Unrecognizable element is ignored.  ACCEPT
  45             ACCEPT NW-FACT.
0045:Unrecognizable element is ignored.  NW-FACT
  46         F-FACT.
0046:Unrecognizable element is ignored.  F-FACT
0047:Unrecognizable element is ignored.  DISPLAY
  47             DISPLAY "CONSOMMATION ?".
0047:Unrecognizable element is ignored.  CONSOMMATION ?
0048:Unrecognizable element is ignored.  ACCEPT
  48             ACCEPT CONS.
0048:Unrecognizable element is ignored.  CONS
  49         CONS.
0049:Unrecognizable element is ignored.  CONS
0050:Unrecognizable element is ignored.  DISPLAY
  50             DISPLAY "Reintro consommation".
0050:Unrecognizable element is ignored.  Reintro consommation
0051:Unrecognizable element is ignored.  ACCEPT
  51             ACCEPT CONS.
0051:Unrecognizable element is ignored.  CONS
  52         I-FACT.
0052:Unrecognizable element is ignored.  I-FACT
  53             EXIT.
0053:Unrecognizable element is ignored.  EXIT
  54         A21.
0054:Unrecognizable element is ignored.  A21
0055:Unrecognizable element is ignored.  MOVE
0055:Unrecognizable element is ignored.  CONS
0055:Unrecognizable element is ignored.  TO
  55             MOVE CONS TO C1.
0055:Unrecognizable element is ignored.  C1
  56         A22.
0056:Unrecognizable element is ignored.  A22
0057:Unrecognizable element is ignored.  MOVE
0057:Name omitted; entry bypassed. TO
  57             MOVE 20 TO C1.
0058:Unrecognizable element is ignored.  SUBTRACT
0058:Unrecognizable element is ignored.  C1
0058:Unrecognizable element is ignored.  FROM
0058:Unrecognizable element is ignored.  CONS
0058:Unrecognizable element is ignored.  GIVING
0058:Unrecognizable element is ignored.  C2
  59         A23.
0059:Unrecognizable element is ignored.  A23
0060:Unrecognizable element is ignored.  MOVE
0060:Name omitted; entry bypassed. TO
  60             MOVE 20 TO C1.
0061:Unrecognizable element is ignored.  MOVE
0061:Name omitted; entry bypassed. TO
  61             MOVE 30 TO C2.
0062:Unrecognizable element is ignored.  SUBTRACT
0062:Unrecognizable element is ignored.  C1
0062:Unrecognizable element is ignored.  C2
0062:Unrecognizable element is ignored.  FROM
0062:Unrecognizable element is ignored.  CONS
0062:Unrecognizable element is ignored.  GIVING
  62             SUBTRACT C1, C2 FROM CONS GIVING C3.
0062:Unrecognizable element is ignored.  C3
  63         F-FACT.
0063:Unrecognizable element is ignored.  F-FACT
0064:Unrecognizable element is ignored.  MOVE
0064:Unrecognizable element is ignored.  CONS
0064:Unrecognizable element is ignored.  TO
  64             MOVE CONS TO CONS-ED.
0064:Unrecognizable element is ignored.  CONS-ED
0065:Unrecognizable element is ignored.  DISPLAY
0065:Unrecognizable element is ignored.  (
0065:Improper punctuation.
0065:Name omitted; entry bypassed. 1
  65             DISPLAY (1,1) ERASE.
0066:Unrecognizable element is ignored.  DISPLAY
0066:Unrecognizable element is ignored.  NOM :
0066:Unrecognizable element is ignored.  NW-FACT
0066:Unrecognizable element is ignored.        CONSOMMATION :
  66             DISPLAY "NOM : ", NW-FACT, "      CONSOMMATION : ", 
CONS-ED.
0066:Unrecognizable element is ignored.  CONS-ED
0067:Unrecognizable element is ignored.  DISPLAY
0067:Unrecognizable element is ignored.  (
0067:Improper punctuation.
0067:Name omitted; entry bypassed. 1
  67             DISPLAY (5,1) "LOCATION DU COMPTEUR".
0068:Unrecognizable element is ignored.  DISPLAY
0068:Unrecognizable element is ignored.  (
0068:Improper punctuation.
0068:Name omitted; entry bypassed. 20
  68             DISPLAY (5,20) CPT.
0069:Unrecognizable element is ignored.  DISPLAY
0069:Unrecognizable element is ignored.  (
0069:Improper punctuation.
0069:Name omitted; entry bypassed. 1
  69             DISPLAY (7,1) "TARIF 1 ", C1, " m3 . .45E".
0070:Unrecognizable element is ignored.  MULTIPLY
0070:Unrecognizable element is ignored.  45
0070:Unrecognizable element is ignored.  BY
  70             MULTIPLY .45 BY C1.
0070:Unrecognizable element is ignored.  C1
0071:Unrecognizable element is ignored.  DISPLAY
0071:Unrecognizable element is ignored.  (
0071:Improper punctuation.
0071:Name omitted; entry bypassed. 20
  71             DISPLAY (7,20) C1.
0072:Unrecognizable element is ignored.  DISPLAY
0072:Unrecognizable element is ignored.  (
0072:Improper punctuation.
0072:Name omitted; entry bypassed. 1
  72             DISPLAY (8,1) "TARIF 2 ", C2, " m3 . .55E".
0073:Unrecognizable element is ignored.  MULTIPLY
0073:Unrecognizable element is ignored.  55
0073:Unrecognizable element is ignored.  BY
  73             MULTIPLY .55 BY C2.
0073:Unrecognizable element is ignored.  C2
0074:Unrecognizable element is ignored.  DISPLAY
0074:Unrecognizable element is ignored.  (
0074:Improper punctuation.
0074:Name omitted; entry bypassed. 20
  74             DISPLAY (8,20) C2.
0075:Unrecognizable element is ignored.  MULTIPLY
0075:Unrecognizable element is ignored.  7
0075:Unrecognizable element is ignored.  BY
  75             MULTIPLY .7 BY C3.
0075:Unrecognizable element is ignored.  C3
0076:Unrecognizable element is ignored.  DISPLAY
0076:Unrecognizable element is ignored.  (
0076:Improper punctuation.
0076:Name omitted; entry bypassed. 1
  76             DISPLAY (9,1) "TARIF 3 ", C3, " m3 . .7E".
0077:Unrecognizable element is ignored.  DISPLAY
0077:Unrecognizable element is ignored.  (
0077:Improper punctuation.
0077:Name omitted; entry bypassed. 20
  77             DISPLAY (9,20) C3.
0078:Unrecognizable element is ignored.  ADD
0078:Unrecognizable element is ignored.  C1
0078:Unrecognizable element is ignored.  C2
0078:Unrecognizable element is ignored.  C3
0078:Unrecognizable element is ignored.  TO
  78             ADD C1, C2, C3 TO TOT.
0078:Unrecognizable element is ignored.  TOT
0079:Unrecognizable element is ignored.  MOVE
0079:Unrecognizable element is ignored.  TOT
0079:Unrecognizable element is ignored.  TO
  79             MOVE TOT TO TOT-ED.
0079:Unrecognizable element is ignored.  TOT-ED
0080:Unrecognizable element is ignored.  DISPLAY
0080:Unrecognizable element is ignored.  (
0080:Improper punctuation.
0080:Name omitted; entry bypassed. 1
  80             DISPLAY (11,1) "TOTAL DES CONSOMMATIONS : ", TOT-ED.
0081:Unrecognizable element is ignored.  MULTIPLY
0081:Unrecognizable element is ignored.  14
0081:Unrecognizable element is ignored.  BY
0081:Unrecognizable element is ignored.  TOT
0081:Unrecognizable element is ignored.  GIVING
  81             MULTIPLY .14 BY TOT GIVING TVA.
0081:Unrecognizable element is ignored.  TVA
0082:Unrecognizable element is ignored.  MOVE
0082:Unrecognizable element is ignored.  TVA
0082:Unrecognizable element is ignored.  TO
  82             MOVE TVA TO TOT-ED.
0082:Unrecognizable element is ignored.  TOT-ED
0083:Unrecognizable element is ignored.  DISPLAY
0083:Unrecognizable element is ignored.  (
0083:Improper punctuation.
0083:Name omitted; entry bypassed. 1
  83             DISPLAY (12,1) "TVA SUR LES CONSOMMATIONS : ", TOT-ED.
0084:Unrecognizable element is ignored.  DISPLAY
0084:Unrecognizable element is ignored.  (
0084:Improper punctuation.
0084:Name omitted; entry bypassed. 1
  84             DISPLAY (14,1) "A PAYER : ".
0085:Unrecognizable element is ignored.  ADD
0085:Unrecognizable element is ignored.  TVA
0085:Unrecognizable element is ignored.  TO
0085:Unrecognizable element is ignored.  TOT
0085:Unrecognizable element is ignored.  GIVING
  85             ADD TVA TO TOT GIVING TOT-ED.
0085:Unrecognizable element is ignored.  TOT-ED
0086:Unrecognizable element is ignored.  DISPLAY
0086:Unrecognizable element is ignored.  (
0086:Improper punctuation.
0086:Name omitted; entry bypassed. 20
  86             DISPLAY (14,20) TOT-ED.
0087:Unrecognizable element is ignored.  DISPLAY
0087:Unrecognizable element is ignored.  (
0087:Improper punctuation.
0087:Name omitted; entry bypassed. 1
  87             DISPLAY (17,1) "NOUVELLE FACTURE (O/N) ?".
0088:Unrecognizable element is ignored.  ACCEPT
0088:Unrecognizable element is ignored.  (
0088:Improper punctuation.
0088:Name omitted; entry bypassed. 20
  88             ACCEPT (17,20) NW-FACT.
0089:Unrecognizable element is ignored.  F-PROG
  90             EXIT.
0090:Unrecognizable element is ignored.  EXIT
** Compiling Procedure Division...
** Generating Object Code...

  203 errors or warnings

   Data area size =   238
   Code area size =     4
```

#### ↳ Re: debugging

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-27T10:58:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pte602lrhm5t0mn0uil4kkj1pmfoncfo3b@4ax.com>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be>`

```
On Mon, 27 Feb 2006 18:39:00 +0100, "gianluigi beuzard"
<gbeuzard@skynet.be> wrote:

What's a script and a Gaz Bill?

What is your environment?  OS & compiler.

It might help if you pasted the line numbers from the listing to cross
reference from the messages.

Some compilers require all 77 levels be after all 01 levels.   I don't
ever bother with 77 levels anymore, just use 01 levels.   I don't
believe I've ever tried an 88 after a 77 level.   See what happens
when you switch from 77 to 01.     Usually I do:

01    Work-fields.
     05 NW-FACT
     88  FOK values "O", "o".

The following is an interesting warning:
>  22           77 TOT-ED PIC E(5)9.9(3).
>0023:/W/Terminal period assumed above.

I assume it is because a period can be part of the picture, or the end
of the statement.   This is telling you what the compiler assumed, and
it appears to have assumed correctly.

It's not obvious to me what your compiler wants with:
>0027:Name omitted; entry bypassed. PROCEDURE
>  27         PROCEDURE DIVISION.

But until that is solved, the subsequent error messages have no hope.


>Could some people help me debugging the DATA DIVISION of that script that 
>compute a Gaz Bill ?
…[375 more quoted lines elided]…
>
```

##### ↳ ↳ Re: debugging

- **From:** "Oliver Wong" <owong@castortech.com>
- **Date:** 2006-02-27T18:36:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XEHMf.7097$M52.4776@edtnps89>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be> <pte602lrhm5t0mn0uil4kkj1pmfoncfo3b@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:pte602lrhm5t0mn0uil4kkj1pmfoncfo3b@4ax.com...

>
> Some compilers require all 77 levels be after all 01 levels.   I don't
…[6 more quoted lines elided]…
>     88  FOK values "O", "o".

    Fujitsu PowerCOBOL seems to allow 88s after 77s. They behave as you'd 
expect (the 88 evaluating to true or false depending on the value of the 
77).

>
> It's not obvious to me what your compiler wants with:
…[3 more quoted lines elided]…
> But until that is solved, the subsequent error messages have no hope.

    Could it have something to do with the semicolons showing up in the DATA 
DIVISION? I've never seen semicolons there before.

[snip]
>>       DATA DIVISION.
>>        WORKING-STORAGE SECTION.
[snip]
>>         77 TOT PIC 9(6)V9(3); COMP 3.
>>         77 TOT-ED PIC E(5)9.9(3).
…[4 more quoted lines elided]…
>>       PROCEDURE DIVISION.
[snip]

    - Oliver
```

###### ↳ ↳ ↳ Re: debugging

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-27T11:44:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j1i602dre4bgsmh7tck1c2kaaenecvaib4@4ax.com>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be> <pte602lrhm5t0mn0uil4kkj1pmfoncfo3b@4ax.com> <XEHMf.7097$M52.4776@edtnps89>`

```
On Mon, 27 Feb 2006 18:36:39 GMT, "Oliver Wong" <owong@castortech.com>
wrote:

>> But until that is solved, the subsequent error messages have no hope.
>
>    Could it have something to do with the semicolons showing up in the DATA 
>DIVISION? I've never seen semicolons there before.

I've had them there - but not with that compiler.   In olden dayze, I
used semi-colons instead of commas whenever possible because they
showed up better with impact printers (not confused with periods). But
either case, they were designed to look pretty, not to do anything.
```

###### ↳ ↳ ↳ Re: debugging

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-02-28T14:26:56+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44044fa3$0$26758$ba620e4c@news.skynet.be>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be> <pte602lrhm5t0mn0uil4kkj1pmfoncfo3b@4ax.com> <XEHMf.7097$M52.4776@edtnps89>`

```
The 88 name-condition works after the 77. The mistake was at COMP-3 that 
must receive a - in fact...

"Oliver Wong" <owong@castortech.com> a �crit dans le message de news: 
XEHMf.7097$M52.4776@edtnps89...
>
> "Howard Brazee" <howard@brazee.net> wrote in message 
…[39 more quoted lines elided]…
>    - Oliver
```

##### ↳ ↳ Re: debugging

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2006-02-28T13:36:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<du2fp3$16n0$1@si05.rsvl.unisys.com>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be> <pte602lrhm5t0mn0uil4kkj1pmfoncfo3b@4ax.com>`

```
"Howard Brazee" <howard@brazee.net> wrote in message 
news:pte602lrhm5t0mn0uil4kkj1pmfoncfo3b@4ax.com...

> Some compilers require all 77 levels be after all 01 levels.

The restriction that 77-level items must follow 01-level items was lifted by 
ANSI X3.23-1974.  Compilers that continue to enforce that restriction aren't 
in compliance with that standard or any subsequent one.

> I don't
> believe I've ever tried an 88 after a 77 level.

ANSI X3.23-1974 says that a condition-name can be associated with any data 
description entry that has a level number EXCEPT a 66, another 88, a group 
that has subordinate item with descriptions including JUSTIFIED, 
SYNCHRONIZED or non-DISPLAY USAGE, or an item declared USAGE INDEX.   I 
don't see any indication that this was a new feature of '74 COBOL, so I 
strongly suspect this has been "doable" all along.

> See what happens
> when you switch from 77 to 01.

For any standard COBOL of the last 32 years or so that has 88's at all (it's 
a feature of Level 2 Nucleus in '74 COBOL), it ought to work just fine 
either way ...

    -Chuck Stevens
```

#### ↳ Re: debugging

- **From:** docdwarf@panix.com ()
- **Date:** 2006-02-27T20:01:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtvlra$lu8$1@reader2.panix.com>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be>`

```
In article <44033aaa$0$29469$ba620e4c@news.skynet.be>,
gianluigi beuzard <gbeuzard@skynet.be> wrote:
>Could some people help me debugging the DATA DIVISION of that script that 
>compute a Gaz Bill ?

Please do your own homework.

DD
```

#### ↳ Re: debugging

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-27T21:08:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JTJMf.170681$K35.155748@fe05.news.easynews.com>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be>`

```
I see a BUNCH of
   COMP 3
where you probably mean
  COMP-3

I think that could explain several of the messages.

As others have pointed out, if you compare the message to the actual "line 
numbers" in your source code, the messages SHOULD help you.  If you don't 
understand a specific message for a specific line, show us the individual 
message and the line (with the line before and after).

Finally, some compilers are better than others on "recovering" after a message. 
Therefore, fix all the errors that you understand and then recompile and repeat 
until you are left with messages you don't understand.
```

#### ↳ Re: debugging

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-02-28T14:28:05+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44044fe6$0$13884$ba620e4c@news.skynet.be>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be>`

```
I fixed most if the bugs but I still get an error here :

77 TOT-ED PIC E(6).999.

 |0023:Improper PICTURE. PIC X assumed.
 |  23           77 TOT-ED PIC E(6).999.
…[5 more quoted lines elided]…
 |0083:Illegal MOVE or comparision is deleted.

Whats wrong with the currency ?

"gianluigi beuzard" <gbeuzard@skynet.be> a �crit dans le message de news: 
44033aaa$0$29469$ba620e4c@news.skynet.be...
> Could some people help me debugging the DATA DIVISION of that script that 
> compute a Gaz Bill ?
…[376 more quoted lines elided]…
>
```

##### ↳ ↳ Re: debugging

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-28T16:01:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kt_Mf.227508$AL5.220492@fe01.news.easynews.com>`
- **References:** `<44033aaa$0$29469$ba620e4c@news.skynet.be> <44044fe6$0$13884$ba620e4c@news.skynet.be>`

```
Where (and how) did you tell the compiler that "E" was the currency sign rather 
than the default "$".  There are several ways to do this, but I don't remember 
how you did this.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
