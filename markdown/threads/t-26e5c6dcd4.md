[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Checking Bits

_5 messages · 5 participants · 1999-04_

---

### Checking Bits

- **From:** joehans@cris.com (Joe Hans)
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3711d6c4.24339164@news.cris.com>`

```
Does anyone know how to test the value of the bits of an alphanumeric
field?

I have a PIC X, and need to find out which bits are on (i.e. set to
1).  So I want to return 8 answers.  Any ideas?

Thanks in advance.
```

#### ↳ Re: Checking Bits

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370efec3@news3.us.ibm.net>`
- **References:** `<3711d6c4.24339164@news.cris.com>`

```
http://www.etk.com then download then etkpak.
Look at the BITPK routine to see how to extract
bits in Cobol.

Joe Hans <joehans@cris.com> wrote in message
news:3711d6c4.24339164@news.cris.com...
> Does anyone know how to test the value of the bits of an alphanumeric
> field?
…[4 more quoted lines elided]…
> Thanks in advance.
```

##### ↳ ↳ Re: Checking Bits

- **From:** joehans@email.com (Joe Hans)
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<371281a3.3568698@news.cris.com>`
- **References:** `<3711d6c4.24339164@news.cris.com> <370efec3@news3.us.ibm.net>`

```
Leif - Thank you very much.  I will put it to use Monday.  It is very
nice of you to make these subroutines available to us.

Joe
------------------------
On Sat, 10 Apr 1999 02:33:37 -0500, "Leif Svalgaard" <lsvalg@ibm.net>
wrote:

>http://www.etk.com then download then etkpak.
>Look at the BITPK routine to see how to extract
…[11 more quoted lines elided]…
>
```

#### ↳ Re: Checking Bits

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7env4k$c46$1@juliana.sprynet.com>`
- **References:** `<3711d6c4.24339164@news.cris.com>`

```
Joe,

        This is my tried and true method I use on the IBM Mainframe ===>

        03    WS-BYTE                 PIC    X(01).
        03    WS-BIT-RSLT          PIC    X(08).
        03    WS-HWORD-X.
                05    WS-HWORD    PIC   S9(04)    BINARY.
        03    WS-SUB                   PIC   S9(04)    BINARY.

        MOVE 'A'                          TO WS-BYTE.
        MOVE ZERO                    TO WS-BIT-RSLT.
        MOVE +1                          TO WS-SUB.
        MOVE LOW-VALUE       TO WS-HWORD-X (1:1).
        MOVE WS-BYTE             TO WS-HWORD-X (2:1).

        PERFORM UNTIL WS-SUB IS GREATER THAN +8
                IF     WS-HWORD-X (2:1) IS GREATER THAN X'7F'
                        MOVE '1'           TO WS-BIT-RSLT (WS-SUB:1)
                        END-IF
                ADD WS-HWORD   TO WS-HWORD
                ADD +1                      TO WS-SUB
                END-PERFORM.

        When the PERFORM falls through, WS-BIT-RSLT will equal '11000001',
which is the bit-pattern of an upper-case EBCDIC 'A' (B'11000001'). You can
then use Reference Modification to test if a bit is present ('1')or not
('0').

        HTH....

Cheers,

WOB,
Atlanta

Joe Hans wrote in message <3711d6c4.24339164@news.cris.com>...
>Does anyone know how to test the value of the bits of an alphanumeric
>field?
…[4 more quoted lines elided]…
>Thanks in advance.
```

#### ↳ Re: Checking Bits

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WBMP2.7056$w6.1883561@news4.mia>`
- **References:** `<3711d6c4.24339164@news.cris.com>`

```
Joe Hans wrote:
>Does anyone know how to test the value of the bits of an alphanumeric
>field?
>
>I have a PIC X, and need to find out which bits are on (i.e. set to
>1).  So I want to return 8 answers.  Any ideas?


       01  BIT-WORK.
           03  BW-BYTE         PIC X(01)      VALUE SPACE.
           03  BW-ORD          PIC 9(04) COMP VALUE 0.
           03  BW-BITS.
               05  BW-BIT128   PIC  9(01).
               05  BW-BIT64    PIC  9(01).
               05  BW-BIT32    PIC  9(01).
               05  BW-BIT16    PIC  9(01).
               05  BW-BIT8     PIC  9(01).
               05  BW-BIT4     PIC  9(01).
               05  BW-BIT2     PIC  9(01).
               05  BW-BIT1     PIC  9(01).
           03  BW-BIT          REDEFINES BW-BITS
                               OCCURS 8 TIMES
                               INDEXED BY BW-X
                                   PIC  9(01).

       SPLIT-BYTE-INTO-BITS.
           COMPUTE BW-ORD = FUNCTION ORD(BW-BYTE) - 1.
           PERFORM VARYING BW-X FROM 8 BY -1 UNTIL BW-X < 1
               DIVIDE 2 INTO BW-ORD
                   GIVING BW-ORD REMAINDER BW-BIT(BW-X)
           END-PERFORM.

       MERGE-BITS-INTO-BYTE.
           MOVE 0 TO BW-ORD.
           PERFORM VARYING BW-X FROM 1 BY 1 UNTIL BW-X > 8
               COMPUTE BW-ORD = BW-ORD + BW-ORD + BW-BIT(BW-X)
           END-PERFORM.
           MOVE FUNCTION CHAR(BW-ORD + 1) TO BW-BYTE.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
