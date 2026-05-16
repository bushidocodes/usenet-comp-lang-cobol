[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# dubbuging that script

_7 messages · 6 participants · 2006-02_

---

### dubbuging that script

- **From:** "gianluigi beuzard" <gbeuzard@skynet.be>
- **Date:** 2006-02-27T18:49:44+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<44033bbb$0$3811$ba620e4c@news.skynet.be>`

```
## Could some people help me debbuging the DATA DIVISION  of that gaz bill ?

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



** COMPILATION ERROR

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

#### ↳ Re: dubbuging that script

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-02-27T10:52:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141066377.242862.325740@i39g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<44033bbb$0$3811$ba620e4c@news.skynet.be>`
- **References:** `<44033bbb$0$3811$ba620e4c@news.skynet.be>`

```

> 203 errors or warnings

You could start by removing the semicolons (;) that are not part of the
language and getting the COMP-3 spelt correctly with a hyphen.  You
should be able to get it to  point where it is telling you the real
erors, such as 'D-Fact' is undefined.

Also check the format of the ACCEPT / DISPLAY in your _Cobol_ manual,
you may be reading  a Basi book by mistake.
```

##### ↳ ↳ Re: dubbuging that script

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-02-27T21:18:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_0KMf.170785$K35.57814@fe05.news.easynews.com>`
- **References:** `<44033bbb$0$3811$ba620e4c@news.skynet.be> <1141066377.242862.325740@i39g2000cwa.googlegroups.com>`

```
Actually a semi-colon followed by a space IS allowed in every Standard of COBOL 
(at least since the 74 Standard) wherever a comma followed by a space may be 
used, which is also where a space by itself may be used, e.g. the following is 
valid 85-Standard code (but NOT something that I would recommend!)

 05;   This-field, Pic, ; 9.
```

###### ↳ ↳ ↳ Re: dubbuging that script

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-02-27T14:25:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4gr602hb2i0f2iue0r40aa3l9ti5bih5ij@4ax.com>`
- **References:** `<44033bbb$0$3811$ba620e4c@news.skynet.be> <1141066377.242862.325740@i39g2000cwa.googlegroups.com> <_0KMf.170785$K35.57814@fe05.news.easynews.com>`

```
On Mon, 27 Feb 2006 21:18:50 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Actually a semi-colon followed by a space IS allowed in every Standard of COBOL 
>(at least since the 74 Standard) wherever a comma followed by a space may be 
…[3 more quoted lines elided]…
> 05;   This-field, Pic, ; 9.


I wonder what the clearest way of writing the following is:

    05   This-field     PIC 9..
```

###### ↳ ↳ ↳ Re: dubbuging that script

_(reply depth: 4)_

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-02-28T06:18:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141136338.517586.155470@i40g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<4gr602hb2i0f2iue0r40aa3l9ti5bih5ij@4ax.com>`
- **References:** `<44033bbb$0$3811$ba620e4c@news.skynet.be> <1141066377.242862.325740@i39g2000cwa.googlegroups.com> <_0KMf.170785$K35.57814@fe05.news.easynews.com> <4gr602hb2i0f2iue0r40aa3l9ti5bih5ij@4ax.com>`

```

Howard Brazee wrote:
> On Mon, 27 Feb 2006 21:18:50 GMT, "William M. Klein"
> <wmklein@nospam.netcom.com> wrote:
…[11 more quoted lines elided]…
>     05   This-field     PIC 9..

I wonder if the overuse of semicolons is a tab marker forcing alignment
in the editor?
```

#### ↳ Re: dubbuging that script

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2006-02-27T11:58:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141070286.065063.184830@v46g2000cwv.googlegroups.com>`
- **In-Reply-To:** `<44033bbb$0$3811$ba620e4c@news.skynet.be>`
- **References:** `<44033bbb$0$3811$ba620e4c@news.skynet.be>`

```
>        77 CONS PIC 9(3)V99; COMP 3.

Actually when one works out what the compiler is doing it is not too
strange.

It is taking the '3' as being the next level number, therefore there is
a missing full stop on the previous declaration and you can't have a
level 3 after a 77.

It all goes downhill from there. Note that CONS is also used as a
paragaph name causing more confusion.

You should also study what 'EXIT' does and ask why you are using it.
You may also want to consider what happens after it has executed the
line PERFORM F-PROG.
```

#### ↳ Re: dubbuging that script

- **From:** epc8@juno.com
- **Date:** 2006-02-27T15:57:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1141084632.692524.245850@v46g2000cwv.googlegroups.com>`
- **References:** `<44033bbb$0$3811$ba620e4c@news.skynet.be>`

```

gianluigi beuzard wrote:
> ## Could some people help me debbuging the DATA DIVISION  of that gaz bill ?
>
>       IDENTIFICATION DIVISION.
>         PROGRAM-ID. FACTURE GAZ.

FACTURE-GAZ is safer here

>        ENVIRONMENT DIVISION.
>         CONFIGURATION SECTION.
>          SOURCE-COMPUTER. CPU1.
>          OBJECT-COMPUTER. CPU1.

you may need

            SPECIAL-NAMES.
                 CURRENCY SIGN IS "E".

here to match your PIC below


>        DATA DIVISION.
>         WORKING-STORAGE SECTION.
…[4 more quoted lines elided]…
>          77 CONS PIC 9(3)V99; COMP 3.

COMP-3

>             88 T1 VALUES 1.00 THRU 19.99.
>             88 T2 VALUES 20.00 THRU 49.99.
>             88 T3 VALUES 50.00 THRU 999.00.

What good does T1 through T3 do?????

>          01 VOL.
>             02 C1 PIC 99V99.
>             02 C2 PIC 99V99.
>             02 C3 PIC 9(3)V99.

>          77 TOT PIC 9(6)V9(3); COMP 3.

COMP-3

>          77 TOT-ED PIC E(5)9.9(3).
>          77 TVA PIC 9(5)V9(3); COMP 3.

COMP-3

>          77 CONS-ED PIC *(5)9.99.
>          77 CPT PIC 99; COMP 0; VALUE 30.

even if you change it to COMP-0 that serves no purpose.
just make it DISPLAY.

>
>        PROCEDURE DIVISION.
…[4 more quoted lines elided]…
>            PERFORM F-PROG.

why not

              STOP RUN.

>        FACT.
>            PERFORM D-FACT.

unknown label

>            PERFORM CONS UNTIL CONS > 0.
>            PERFORM I-FACT.

WHY???????????

>            PERFORM A21.
>            PERFORM A22.
…[7 more quoted lines elided]…
>        F-FACT.

duplicate label, maybe you want

          D-FACT.

>            DISPLAY "CONSOMMATION ?".
>            ACCEPT CONS.
…[9 more quoted lines elided]…
>            SUBTRACT C1 FROM CONS GIVING C2.

and what if C2 goes negative?

>        A23.
>            MOVE 20 TO C1.
>            MOVE 30 TO C2.
>            SUBTRACT C1, C2 FROM CONS GIVING C3.

and what if C3 goes negative?

>        F-FACT.
>            MOVE CONS TO CONS-ED.
…[6 more quoted lines elided]…
>            DISPLAY (7,20) C1.

  C1 is not an EDITED field

>            DISPLAY (8,1) "TARIF 2 ", C2, " m3 . .55E".
>            MULTIPLY .55 BY C2.
>            DISPLAY (8,20) C2.

  C2 is not an EDITED field

>            MULTIPLY .7 BY C3.
>            DISPLAY (9,1) "TARIF 3 ", C3, " m3 . .7E".
>            DISPLAY (9,20) C3.

  C3 is not an EDITED field

>            ADD C1, C2, C3 TO TOT.

TOT is unintialized. Do you want to set it to ZERO first????

>            MOVE TOT TO TOT-ED.
>            DISPLAY (11,1) "TOTAL DES CONSOMMATIONS : ", TOT-ED.
…[4 more quoted lines elided]…
>            ADD TVA TO TOT GIVING TOT-ED.

Do you really want to do this? I am not sure you can do arithmetic on
an EDITED field.
So how about
             ADD TVA TO TOT.
            MOVE TOT TO TOT-ED.

>            DISPLAY (14,20) TOT-ED.
>            DISPLAY (17,1) "NOUVELLE FACTURE (O/N) ?".
>            ACCEPT (17,20) NW-FACT.
>        F-PROG.
>            EXIT.

[horrible error casecade snipped]

-- Elliot

note: The student still has plenty of work to do here. I've just
applied a dose of the old red pencil.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
