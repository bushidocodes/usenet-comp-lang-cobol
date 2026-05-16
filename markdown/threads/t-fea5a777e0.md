[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Translating character into hex for output

_5 messages · 5 participants · 2000-02_

---

### Translating character into hex for output

- **From:** "Troy Hoopes" <troy.hoopes@publicans.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88upfm$g1d$1@hornet.fibr.net>`

```
I am working in OS/VS COBOL and am trying to find a way to transfer the hex
value of a single character into a field for printout.  I have looked for
commands similar to other programming languages have, but find nothing in
COBOL.

Any suggestions besides building a table to be tested against?

Thanks,
```

#### ↳ Re: Translating character into hex for output

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88upvm$sv9$1@nntp4.atl.mindspring.net>`
- **References:** `<88upfm$g1d$1@hornet.fibr.net>`

```
OS/VS COBOL (which hasn't been supported by IBM for many, MANY years) does
not have "native language" support for this.  If your shop runs your OS/VS
COBOL programs under the LE run-time *and* if you have the current strategic
COBOL compiler (IBM COBOL for OS/390 & VM), then you can pass the hex data to
a new COBOL program and use the intrinsic functions ORD and CHAR to convert
hex to ordinal numbers and back.

Assuming this is NOT the way that you want to go, check out www.deja.com and
there are several "tricky" ways to do this in old-style COBOL (using tables
with hex values and/or using COMP redefinitions of fields).

P.S.  I really, REALLY, suggest that you get your COBOL programs converted to
a supported compiler.
```

#### ↳ Re: Translating character into hex for output

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2000-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88v94g$850$1@nntp4.atl.mindspring.net>`
- **References:** `<88upfm$g1d$1@hornet.fibr.net>`

```
Troy,

        Try the following:

           03  WS-TARGET-BYTE          PIC  X(001).
           03  WS-HEX-FIELD                PIC  X(002).
           03  FILLER              REDEFINES WS-HEX-FIELD.
               05  WS-HEX-BYTE-01       PIC  X(001).
               05  WS-HEX-BYTE-02       PIC  X(001).
           03  WS-HWORD                     PIC  9(004)      COMP.
           03  FILLER              REDEFINES WS-HWORD.
               05  WS-HWORD-UPPER  PIC  X(001).
               05  WS-HWORD-LOWER  PIC  X(001).

           MOVE 'F'                                        TO
WS-TARGET-BYTE.
           MOVE LOW-VALUE                    TO WS-HWORD-UPPER.
           MOVE WS-TARGET-BYTE         TO WS-HWORD-LOWER.
           COMPUTE WS-HWORD             = (WS-HWORD / 16).
      *
           IF  WS-HWORD > 9
               ADD  183                                  TO WS-HWORD
           ELSE
               ADD  240                                  TO WS-HWORD.
      *
           MOVE WS-HWORD-LOWER     TO WS-HEX-BYTE-01.
           MOVE WS-TARGET-BYTE         TO WS-HWORD-LOWER.
           COMPUTE WS-HWORD            = (WS-HWORD * 16).
           MOVE LOW-VALUE                   TO WS-HWORD-UPPER.
           COMPUTE WS-HWORD            = (WS-HWORD / 16).
      *
           IF  WS-HWORD >  9
               ADD  183                                 TO WS-HWORD
           ELSE
               ADD  240                                 TO WS-HWORD.
      *
           MOVE WS-HWORD-LOWER   TO WS-HEX-BYTE-02.
      ****
      **** AFTER COMPLETING THIS CODE, WS-HEX-FIELD CONTAINS A 'C6',
      **** WHICH (IN 01-BYTE HEX) IS X'C6', A CAPITAL 'F'.
      ****

        IMHO, your shop really needs to get off of OS/VS COBOL.

HTH....

WOB

Troy Hoopes <troy.hoopes@publicans.com> wrote in message news:88upfm$g1d$1@h
ornet.fibr.net...
> I am working in OS/VS COBOL and am trying to find a way to transfer the
hex
> value of a single character into a field for printout.  I have looked for
> commands similar to other programming languages have, but find nothing in
…[7 more quoted lines elided]…
>
```

#### ↳ Re: Translating character into hex for output

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Iixt4.35365$po2.362085@news1.mia>`
- **References:** `<88upfm$g1d$1@hornet.fibr.net>`

```
Troy Hoopes wrote:
>I am working in OS/VS COBOL and am trying to find a way to transfer the hex
>value of a single character into a field for printout.  I have looked for
>commands similar to other programming languages have, but find nothing in
>COBOL.

Use the FUNCTION ORD intrinsic to get the value of a byte, then use
DIVIDE ... REMAINDER to obtain the high and low half-byte values,
which you can use to subscript into a 16 character table 0-9,A-F.
```

##### ↳ ↳ Re: Translating character into hex for output

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<896dqa$vk0$1@nnrp1.deja.com>`
- **References:** `<88upfm$g1d$1@hornet.fibr.net> <Iixt4.35365$po2.362085@news1.mia>`

```
In article <Iixt4.35365$po2.362085@news1.mia>,
  "Judson McClendon" <judmc@bellsouth.net> wrote:
> Troy Hoopes wrote:
> >I am working in OS/VS COBOL and am trying to find a way to transfer
the hex
> >value of a single character into a field for printout.  I have
looked for
> >commands similar to other programming languages have, but find
nothing in
> >COBOL.
>
> Use the FUNCTION ORD intrinsic to get the value of a byte, then use

<Rest Snipped>

Judson,

Troy's environment is OS/VS COBOL. I don't believe FUNCTIONS existed.

Cheers,

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
