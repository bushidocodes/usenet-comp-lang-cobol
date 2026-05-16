[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DELAY COMMAND or whatever

_13 messages · 10 participants · 1998-12 → 1999-01_

---

### DELAY COMMAND or whatever

- **From:** insane_o@hotmail.com (Gil)
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368052f1.9329575@news.inter.net.il>`

```
Hey,
 Is there a command to make a DELAY during the run? like pause or whatever?
```

#### ↳ Re: DELAY COMMAND or whatever

- **From:** mixxerdw@eye_eye_echs.com
- **Date:** 1998-12-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com>`
- **References:** `<368052f1.9329575@news.inter.net.il>`

```
On Wed, 23 Dec 1998 02:18:53, insane_o@hotmail.com (Gil) wrote:

> Hey,
>  Is there a command to make a DELAY during the run? like pause or whatever?
>  
>  
You mean a COBOL command?  Probably several ways to do it with 
date/time calls, but if you want a JCL invoked waiter for pauses 
between job steps:

         TITLE 'WAIT FOR PARAMETER TIME'
WAITERX  BEGIN 12,SAVE               JCL CALL VERSION
         SPACE 2
         L     R1,0(R1)                GET PARM AREA
         ST    R1,SAVPARM               SAVE FOR FUN
         MVC   INTV2,2(R1)             BUT THIS IS FOR REAL
         STIMER WAIT,DINTVL=INTV6
         B     GOBYE
GOBYE    L     R13,SAVE+4
         RETURN (14,12),RC=0
          DC    C'INTV1 STARTS HERE---'
         DS    2F
INTV6    DC    C'000'        THIS IS CONSTANT
INTV2    DC    CL4'0'          FROM THE PARM
         DC    X'C0'         DO NOT CHANGE
SAVPARM  DC  A(0)           PARM ADDRESS
         DC    C'END OF WAITERX'
         END   WAITERX
```

##### ↳ ↳ Re: DELAY COMMAND or whatever

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76bcc5$ft1@sjx-ixn6.ix.netcom.com>`
- **References:** `<368052f1.9329575@news.inter.net.il> <1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com>`

```
In case you don't LIKE coding in Assembler (and you are talking about IBM
mainframes - which I think you are), see bellow

mixxerdw@eye_eye_echs.com wrote in message
<1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com>...
>On Wed, 23 Dec 1998 02:18:53, insane_o@hotmail.com (Gil) wrote:
>
>> Hey,
>>  Is there a command to make a DELAY during the run? like pause or
whatever?
>>
>>


In all versions of MVS COBOL from OS/VS COBOL on, you can simply call

  "ILBOWAT"

passing it (below the 16M line, i.e. with DATA(24) if you are using a
current COBOL compiler) the time for which you want to "pause". (I can't
remember, with some of the more recent run-time libraries - you might need
to call the entry point ILBOWAT0.)

This is a little known (but documented in the old OS/VS COBOL logic manual)
feature that has been maintained with both the VS COBOL II and LE run-time
libraries.

P.S.  Mark Young -- is there an ILBDWAT (or similar) VSE module?
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76betq$60t$1@news.igs.net>`
- **References:** `<368052f1.9329575@news.inter.net.il> <1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com> <76bcc5$ft1@sjx-ixn6.ix.netcom.com>`

```

William M. Klein wrote in message <76bcc5$ft1@sjx-ixn6.ix.netcom.com>...

>P.S.  Mark Young -- is there an ILBDWAT (or similar) VSE module?


Don't know about VSE, but the PC has a "sleep/dispatch" that
can be called by subroutine.  The only Cobol I know that does
not is DOS, but there it is easy to just loop and look at the clock.
Since it is single user anyway, that is sufficient for most purposes.
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

_(reply depth: 4)_

- **From:** Albert Ratzlaff <albert@conexion.com.py>
- **Date:** 1998-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3689F318.A83999B3@conexion.com.py>`
- **References:** `<368052f1.9329575@news.inter.net.il> <1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com> <76bcc5$ft1@sjx-ixn6.ix.netcom.com> <76betq$60t$1@news.igs.net>`

```


Donald Tees wrote:

> Don't know about VSE, but the PC has a "sleep/dispatch" that
> can be called by subroutine.  The only Cobol I know that does
> not is DOS, but there it is easy to just loop and look at the clock.
> Since it is single user anyway, that is sufficient for most purposes.

"Used to be" single user. One of the nice things about Windows is that now
you have a multi-user DOS.

Regards
Albert Ratzlaff
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

_(reply depth: 5)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298364.19792.10092@kcbbs.gen.nz>`
- **References:** `<3689F318.A83999B3@conexion.com.py>`

```
In message <<3689F318.A83999B3@conexion.com.py>> Albert Ratzlaff <albert@conexion.com.py> writes:
> 
> Donald Tees wrote:
…[7 more quoted lines elided]…
> you have a multi-user DOS.

I think you mean 'multi-tasking', multi-user is something different
though NT TSE (Terminal Server Edition) does finally achieve
multi-user, it does it rather poorly because underneath it
is still inherently a single user design.

Given that I have used a multi-user DOS (but not from MS)
for a dozen years or more that also supported multi-tasking
at each terminal then the best that MS can claim is that
they have at last caught up.

MS-DOS and Windows do actually have a despatch OS function
using the multiplex interrupt INT 0x2F with AX=0x1680.
This should be called in each loop waiting for time:  ie

        ACCEPT Time-Now FROM TIME
        ADD 100 Time-Now GIVING Time-Out
        PERFORM UNTIL Time-Now > Time-Out
            ACCEPT Time-Now  FROM TIME
            CALL x"84"
                USING Interrupt-2F
                      etc
         END-PERFORM
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36899A6D.121FBDB8@att.net>`
- **References:** `<368052f1.9329575@news.inter.net.il> <1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com> <76bcc5$ft1@sjx-ixn6.ix.netcom.com>`

```
"William M. Klein" wrote:
>
(snip)
> >>  Is there a command to make a DELAY during the run? like pause or
> whatever?
…[8 more quoted lines elided]…
> to call the entry point ILBOWAT0.)

What does the time field passed to ILBOWAT look like?

Bill Lynch
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76cb85$qb5@sjx-ixn4.ix.netcom.com>`
- **References:** `<368052f1.9329575@news.inter.net.il> <1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com> <76bcc5$ft1@sjx-ixn6.ix.netcom.com> <36899A6D.121FBDB8@att.net>`

```

William Lynch wrote in message <36899A6D.121FBDB8@att.net>...
>"William M. Klein" wrote:
>>
…[10 more quoted lines elided]…
>> remember, with some of the more recent run-time libraries - you might
need
>> to call the entry point ILBOWAT0.)
>
>What does the time field passed to ILBOWAT look like?
>
>Bill Lynch

My memory is that it is a half-word binary (i.e. Pic S9(04)) - what I can't
remember is exactly what it means, i.e. does "1" mean a second or
one-hundredths of a second.  I think it is the latter.

(Easy way to test it - but I don't have a compiler and run-time handy) is to
display time-of-day (or equivalent), call with a value of 100, then display
the time again.  That should give a fairly accurate answer.
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

_(reply depth: 5)_

- **From:** daniel.jacot@winterthur.ch
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76qjnc$tcf$1@nnrp1.dejanews.com>`
- **References:** `<368052f1.9329575@news.inter.net.il> <1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com> <76bcc5$ft1@sjx-ixn6.ix.netcom.com> <36899A6D.121FBDB8@att.net> <76cb85$qb5@sjx-ixn4.ix.netcom.com>`

```
In article <76cb85$qb5@sjx-ixn4.ix.netcom.com>,
  "William M. Klein" <wmklein@ix.netcom.com> wrote:

<snip>

> >
> >What does the time field passed to ILBOWAT look like?
…[10 more quoted lines elided]…
>

Don't try PIC S9(04)! You'll get a returncode of 8 and no delay at all. It
has to be a fullword binary, not a halfword. I tested the following little
programm, compiled with COBOL for MVS & VM V1R2M1 and LE/370 Version 1.8
(OS/390 V2.4):

CBL DATA(24)
       IDENTIFICATION DIVISION.
       PROGRAM-ID. I49804.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  DELAY-AMT               PIC S9(9) COMP.
       01  ILBOWAT0                PIC X(8) VALUE 'ILBOWAT0'.
       01  CURRENT-TIME            PIC 9(8).
       PROCEDURE DIVISION.
           MOVE 100 TO DELAY-AMT
           ACCEPT CURRENT-TIME FROM TIME
           DISPLAY CURRENT-TIME
           CALL ILBOWAT0 USING DELAY-AMT
           ACCEPT CURRENT-TIME FROM TIME
           DISPLAY CURRENT-TIME
           GOBACK.

With the following result:
13590982
14004985

So 100 means 100 seconds. By the way, there is no documentation at all in the
COBOL for MVS & VM manual. And: don't try to call ILBOWAT instead of ILBOWAT0!
The CSECT starts with a "DC H'0'" at displacement 0, so you'll get a ABEND
S0C1. ILBOWAT0 is an ALIAS of ILBOWAT, but with entry point at displacement 2.

Cheers

Daniel

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76rgdj$8b4@dfw-ixnews6.ix.netcom.com>`
- **References:** `<368052f1.9329575@news.inter.net.il> <1tGZ16mMk7i4-pn2-fnCSn9dutg0m@dsm4merlin.iix.com> <76bcc5$ft1@sjx-ixn6.ix.netcom.com> <36899A6D.121FBDB8@att.net> <76cb85$qb5@sjx-ixn4.ix.netcom.com> <76qjnc$tcf$1@nnrp1.dejanews.com>`

```
Thank you for the corrections.  It has been years since I worked with it
(and was providing information from a dim memory only).  By the way, the
ONLY place that I know that this module is/was ever documented was in the LY
(licencensed) "run-time logic" manual for OS/VS COBOL.

daniel.jacot@winterthur.ch wrote in message
<76qjnc$tcf$1@nnrp1.dejanews.com>...
>In article <76cb85$qb5@sjx-ixn4.ix.netcom.com>,
>  "William M. Klein" <wmklein@ix.netcom.com> wrote:
…[8 more quoted lines elided]…
>> My memory is that it is a half-word binary (i.e. Pic S9(04)) - what I
can't
>> remember is exactly what it means, i.e. does "1" mean a second or
>> one-hundredths of a second.  I think it is the latter.
>>
>> (Easy way to test it - but I don't have a compiler and run-time handy) is
to
>> display time-of-day (or equivalent), call with a value of 100, then
display
>> the time again.  That should give a fairly accurate answer.
>>
…[27 more quoted lines elided]…
>So 100 means 100 seconds. By the way, there is no documentation at all in
the
>COBOL for MVS & VM manual. And: don't try to call ILBOWAT instead of
ILBOWAT0!
>The CSECT starts with a "DC H'0'" at displacement 0, so you'll get a ABEND
>S0C1. ILBOWAT0 is an ALIAS of ILBOWAT, but with entry point at displacement
2.
>
>Cheers
…[4 more quoted lines elided]…
>http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1998-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981230012818.25321.00001260@ngol02.aol.com>`
- **References:** `<76bcc5$ft1@sjx-ixn6.ix.netcom.com>`

```

In article <76bcc5$ft1@sjx-ixn6.ix.netcom.com>, "William M. Klein"
<wmklein@ix.netcom.com> writes:

>P.S.  Mark Young -- is there an ILBDWAT (or similar) VSE module?

I had never heard of ILBDWAT--I'll have to look into it.


Mark A. Young
```

###### ↳ ↳ ↳ Re: DELAY COMMAND or whatever

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990103212334.23737.00002189@ngol04.aol.com>`
- **References:** `<76bcc5$ft1@sjx-ixn6.ix.netcom.com>`

```

In article <76bcc5$ft1@sjx-ixn6.ix.netcom.com>, "William M. Klein"
<wmklein@ix.netcom.com> writes:

>P.S.  Mark Young -- is there an ILBDWAT (or similar) VSE module?

I checked the DOS/VS COBOL 1.3.1 Compiler and Library Reference and did not see
anything about WAIT in its description of the ILBD modules.


Mark A. Young
```

#### ↳ Re: DELAY COMMAND or whatever

- **From:** WOB@my-dejanews.com
- **Date:** 1998-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<769i2d$nvr$1@nnrp1.dejanews.com>`
- **References:** `<368052f1.9329575@news.inter.net.il>`

```
In article <368052f1.9329575@news.inter.net.il>,
  insane_o@hotmail.com wrote:
> Hey,
>  Is there a command to make a DELAY during the run? like pause or whatever?
>
>

Below is another variation of the STIMER macro in a sub-program named
SNOOZER. It's called by COBOL and passes a 7-Byte Display-Numeric parameter,
defined as PIC 9(05)V99. The label MAXINTVL is USER defined. It's set to
300.00 seconds (5 minutes) in the sub-program.

Syntax specifying a WAIT of 3.57 Seconds (a favorite number of mine) ===>

03    WS-SNOOZER     PIC X(08)       VALUE 'SNOOZER'.
03    WS-INTERVAL    PIC 9(05)V99    VALUE 3.57.

CALL WS-SNOOZER USING WS-INTERVAL.

HTH....

Happy Holidays,

WOB,
Atlanta

SNOOZER  CSECT	00000100  USING *,R12  R12 IS OUR BASE-REGISTER  00000200 
PRINT GEN  ACTIVATE MACRO-EXPANSION  00000300 SNOOZER  AMODE 31  SHOULD
ALWAYS BE '31'	00000400 SNOOZER  RMODE ANY  SHOULD ALWAYS BE 'ANY'  00000500
 YREGS	MVS REGISTER-MACRO  00000600  SAVE  (14,12)  SAVE ALL REGISTERS 
00000700  LR  R12,R15  ESTABLISH ADDRESSABILITY  00000800  B  GETPARM  BRANCH
AROUND EYECATCHER  00000900  DC  CL19' PROGRAM NAME ===>'  00001000 PROGNAME
DC  CL8'SNOOZER'  00001100  DC	CL21', LAST ASSEMBLY ===>'  00001200  DC 
CL8'&SYSDATE'  00001300  DC  CL2','  00001400  DC  CL5'&SYSTIME'  00001500 
DC  CL22', ASSEMBLER USED ===>'  00001600  DC  CL21'&SYSASM'  00001700
MAXINTVL DC  PL4'0030000'  MAX-INTERVAL FOR 'STIMER'  00001800 TWNTY4HR DC 
PL4'8640000'  24-HOUR MAX-INTERVAL  00001900  EJECT  00002000 GETPARM  DS  0H
 00002100  L  R9,0(,R1)  PARAMETER ADDRESSABILITY  00002200  PACK 
DWORD,0(7,R9)  PACK AS P'00000000SSSSSTH'  00002300  OI  DWORD+7,X'0F' 
ENSURE 'F' SIGN-NIBBLE	00002400  LA  R15,4  SET TO F'4' (RETURN-CODE) 
00002500  MVC  MSGAREA,=CL69'SNOOZER ===> SLEEP-INTERVAL IS <INVALID>,
X00002600  RETURN-CODE 004'  00002700  NC  MSGAREA+14(4),=7X'BF'  CONVERT TO
LOWER-CASE  00002800  NC  MSGAREA+20(7),=7X'BF'  DITTO-DITTO-DITTO-DITTO 
00002900  NC  MSGAREA+28(2),=7X'BF'  DITTO-DITTO-DITTO-DITTO  00003000	NC 
MSGAREA+43(5),=7X'BF'  DITTO-DITTO-DITTO-DITTO	00003100  NC 
MSGAREA+50(3),=7X'BF'  DITTO-DITTO-DITTO-DITTO	00003200  LA  R6,RTN2CLLR 
POINT R6 AT RETURN-LABEL  00003300  CP	DWORD,TWNTY4HR	PARAMETER EXCEEDS
24-HOURS?  00003400  BH  PUT2CNSL  YES, THANKS FOR PLAYING  00003500  SLL 
R15,1  RESET TO F'8'  00003600	MVI  MSGAREA+56,C'8'  INSERT INTO MSGAREA 
00003700  CP  DWORD,MAXINTVL  PARAMETER EXCEEDS MAX INTERVAL?  00003800  BH 
PUT2CNSL  YES, THANKS FOR PLAYING  00003900  SLL  R15,1  RESET TO F'16' 
00004000  MVC  MSGAREA+55(2),=C'16'  INSERT INTO MSGAREA  00004100  CVB 
R7,DWORD  CONVERT TO BINARY  00004200  LTR  R7,R7  PARAMETER ZERO?  00004300 
BZ  PUT2CNSL  YES, THANKS FOR PLAYING  00004400  ST  R7,DWORD+4  POPULATE
'STIMER' INTERVAL  00004500  MVC  MSGAREA+13(53),=CL53'BEGIN 00000.00 SECOND
SLEEP-INTERVAX00004600	L, PLEASE WAIT....'  00004700  MVC 
MSGAREA+19(5),0(R9)  INSERT WHOLE-SECONDS  00004800  MVC  MSGAREA+25(2),5(R9)
 INSERT TENTH/HUNDRETHS  00004900  NC  MSGAREA+14(4),=7X'BF'  CONVERT TO
LOWER-CASE  00005000  NC  MSGAREA+29(5),=7X'BF'  DITTO-DITTO-DITTO-DITTO 
00005100  NC  MSGAREA+36(4),=7X'BF'  DITTO-DITTO-DITTO-DITTO  00005200	NC 
MSGAREA+42(7),=7X'BF'  DITTO-DITTO-DITTO-DITTO	00005300  NC 
MSGAREA+52(5),=7X'BF'  DITTO-DITTO-DITTO-DITTO	00005400  NC 
MSGAREA+59(3),=7X'BF'  DITTO-DITTO-DITTO-DITTO	00005500  BAL  R6,PUT2CNSL 
ISSUE 'WTO'  00005600  STIMER WAIT,BINTVL=DWORD+4  ISSUE 'STIMER'  00005700 
MVC  MSGAREA+13(5),=CL5'END' INDICATE END OF SLEEP-INTERVAL  00005800  NC 
MSGAREA+14(2),=7X'BF'  CONVERT TO LOWER-CASE  00005900	MVC 
MSGAREA+51(15),=CL15'RETURN-CODE 000'  00006000  NC  MSGAREA+52(5),=7X'BF' 
CONVERT TO LOWER-CASE  00006100  NC  MSGAREA+59(3),=7X'BF' 
DITTO-DITTO-DITTO-DITTO  00006200  BAL	R6,PUT2CNSL  ISSUE 'WTO'  00006300 
XR  R15,R15  RETURN-CODE IS NORMAL  00006400  EJECT  00006500 RTN2CLLR DS  0H
 00006600  RETURN (14,12),RC=(15)  RESTORE REGISTERS AND RETURN  00006700
PUT2CNSL DS  0H  00006800  BAL	R1,WRT2OPER  ISSUE SVC 35  00006900  DC 
Y(L'MSGAREA+4)	MESSAGE-LGTH PLUS 4  00007000  DC  X'8000'  MCS-FLAGS 
00007100 MSGAREA  DS  CL69  WTO MESSAGE-AREA  00007200	DC  H'0' 
DESCRIPTOR-CODES  00007300  DC	X'0024'  ROUTING-CODES	00007400 WRT2OPER DS 
0H  00007500  SVC  35  ISSUE 'WTO'  00007600  BR  R6  RETURN TO THE 'NSI' 
00007700 DWORD	DS  D  ALIGNED DOUBLEWORD WORKAREA  00007800  END  00007900

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
