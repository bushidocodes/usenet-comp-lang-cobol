[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus DOS zero CPU overhead under WiN

_7 messages · 6 participants · 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus DOS zero CPU overhead under WiN

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7suoq2$q11$1@news4.svr.pol.co.uk>`

```
I need a way of releasing execution of my DOS applications under the Windows
based op.sys's
(including CITRIX). I'm using Micro Focus Workbench 2,4 & don't wish to
upgrade as newer versions have much larger execution overheads. Several of
my routines operate in the following way;

PERFORM Get-System-Time

PERFORM UNTIL 88-exit-true

    PERFORM Check-For-Key-Press

    IF  NOT keyboard-empty
       DO SOMETHING
    ELSE
       PERFORM Get-System-Time
    END-IF

END-PERFORM

Ideally I would like to CALL a .bin file which would wait for 0.5 sec's with
ZERO CPU overhead whilst returning the system time.

Any Idea's ? alister@specsoft.freeserve.co.uk
```

#### ↳ Re: Microfocus DOS zero CPU overhead under WiN

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t4e31$rii$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<7suoq2$q11$1@news4.svr.pol.co.uk>`

```
    If you use NT 4.0, you probably need do nothing.  It seems to be good at
squeezing dos programs down - I have written small test programs, and my
400MHz NT does fewer loops than my Win98 120MHz Pc in a tight loop checking
the time (without checking the keyboard).  Win98 is fairly good at choking a
program that sits in a tight loop on the keyboard if you set propertys
right.

    It is not so good at squeezing programs that loop on an accept T from
time.
I suppose that ignoreing the clock until a keystroke arrives would work.

    For win 3.1/95/98, either use Leif's suggestion (great job Leif!), of
try TAME out.  TAME seems to be a relic from DESQview, and has not been
changed in a while, but is highly tuneable and might work.  Of course, since
you have the source code ...

    Do NOT call the BBS if you have the number.  Some poor soul now has that
number.  I wonder how many 3AM calls he gets now.  It (TAME) can be found
at www.mindspring.com/~dgthomas/tame.htm




Alister Munro <alister@specsoft.freeserve.co.uk> wrote in message
news:7suoq2$q11$1@news4.svr.pol.co.uk...
> I need a way of releasing execution of my DOS applications under the
Windows
> based op.sys's
> (including CITRIX). I'm using Micro Focus Workbench 2,4 & don't wish to
…[17 more quoted lines elided]…
> Ideally I would like to CALL a .bin file which would wait for 0.5 sec's
with
> ZERO CPU overhead whilst returning the system time.
>
> Any Idea's ? alister@specsoft.freeserve.co.uk
>
```

#### ↳ Re: Microfocus DOS zero CPU overhead under WiN

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37f3596f_2@news3.prserv.net>`
- **References:** `<7suoq2$q11$1@news4.svr.pol.co.uk>`

```

Alister Munro <alister@specsoft.freeserve.co.uk> wrote in message
news:7suoq2$q11$1@news4.svr.pol.co.uk...
> I need a way of releasing execution of my DOS applications under the
Windows
> based op.sys's
> (including CITRIX). I'm using Micro Focus Workbench 2,4 & don't wish to
…[17 more quoted lines elided]…
> Ideally I would like to CALL a .bin file which would wait for 0.5 sec's
with
> ZERO CPU overhead whilst returning the system time.
>

The following does what you want. It is written for Realia that has a
different parameter convention from MF, but can easily be converted
to MF (ten minutes work). Then you can assemble the result and
you get an .obj file which you can link with your programs.

If this does it for you, I could make the conversion and post the obj
file. There might also be other people out there in the NG, can
would do this.

here goes:

TITLE   WAITMSEC
PAGE    55,132
.MODEL  SMALL
.486 ; .386 OK too

;-----------------------------------------------------.
;           Author:     Leif Svalgaard                :
;                                                     :
;           written:    95/11/22                      :
;           revised:    96/12/19                      :
;-----------------------------------------------------:
;           Cobol:      REALIA COBOL 2.x/3.x/4.x      :
;-----------------------------------------------------'

; structure of arguments

OPTION      PROC: PRIVATE, NOSCOPED
OPTION      OLDSTRUCTS
PARAM1      STRUCT
TASK_ID     DB  4 DUP(?)     ; task id  : used for debug purpose
OP          DB        ?      ; operation: (W)ait millisecs
KEY         DB        ?      ; key value: NUL if no key struck
MSECLO      DW        ?      ; wait time: wait this many milliseconds
MSECHI      DW        ?      ;   32 bit
PARAM1      ENDS             ;

WAITMSEC$ASM SEGMENT
            ASSUME      CS:WAITMSEC$ASM, DS:WAITMSEC$ASM
            PUBLIC      WAITMSEC
WAITMSEC    PROC        FAR
            JMP         BEGIN_PROG

STOP_MSECLO DW        0      ;
STOP_MSECHI DW        0      ;

; ES:[DI] points to param1

BEGIN_PROG:                              ; begin
            MOV         AL,ES:[DI].OP    ;   AL = operation
            CMP         AL,"W"           ;   if operation = W goto Wait
            JE          WAIT_OP          ;

NUL_RETURN:                              ; NUL Return:
            MOV         AL,00h           ;   key value = NUL
            JMP         RETURN           ;   return

; ----------------------------------------

WAIT_OP:                                 ; Wait:
            CALL        GET_MSEC         ;   get milliseconds now
            ADD         AX,ES:[DI].MSECLO;
            ADC         DX,ES:[DI].MSECHI;   add msecs_to_wait
            MOV         STOP_MSECLO,AX   ;   giving when to stop
            MOV         STOP_MSECHI,DX   ;
IDLE_LOOP:
            MOV         AH,0Bh           ;   DOS: interrupt check KBD status
            INT         21h              ;        also enables CTL+BREAK
            CMP         AL,0FFh          ;        if key struck
            JE          KEY_STRUCK       ;            goto Key Struck

            MOV         AH,86h           ;
            MOV         CX,0             ;   For OS/2:
            MOV         DX,5000          ;        BIOS: wait 5 msec
            INT         15h              ;

            MOV         AX,1680h         ;   For Windows:
            INT         2Fh              ;        Windows idle call

            CALL        GET_MSEC         ;   get millisecs
            SUB         AX,STOP_MSECLO   ;   compare to stop time
            SBB         DX,STOP_MSECHI   ;   if isn't there yet
            JS          IDLE_LOOP        ;       keep looping

            JMP         NUL_RETURN       ;   return NUL

KEY_STRUCK:                              ; Key Struck:
            MOV         AH,08h           ;   DOS: interrupt(Get key no echo)
            INT         21h              ;
            CMP         AL,00h           ;        if key = 00
            JNE         RETURN           ;
EXTENDED_KEY:                            ;            Extended key:
            MOV         AH,08h           ;            get key again
            INT         21h              ;            add 128 to key value
            ADD         AL,128           ;

RETURN:     MOV         ES:[DI].KEY,AL   ;    set key
            RET                          ;    return

GET_MSEC    PROC NEAR                    ; Get Millisecs:
            MOV         AH,2Ch           ;   DOS: interrupt(Get time)
            INT         21h              ;
            PUSH        DX               ;   save secs, hundredths
            MOV         BL,60            ;
            MOV         AL,CH            ;
            MUL         BL               ;   (CH) hours * 60
            ADD         AL,CL            ;              + (CL) mins
            ADC         AH,0             ;   AX = mins (hours,mins)
            MOV         BX,60000         ;
            MUL         BX               ;   DX,AX = millisecs (hours,mins)
            MOV         CX,AX            ;
            MOV         SI,DX            ;   SI,CX = millisecs (hours,mins)

            POP         DX               ;   get secs, hundredths
            MOV         BL,100           ;
            MOV         AL,DH            ;
            MUL         BL               ;   (DH) secs * 100
            ADD         AL,DL            ;             + (DL) hundredths
            ADC         AH,0             ;   AX = hundredths (secs,hund's)
            MOV         BX,10            ;
            MUL         BX               ;   DX,AX = millisecs (secs,hund's)
            ADD         AX,CX            ;
            ADC         DX,SI            ;   DX,AX = millisecs (total)
            RET                          ;
GET_MSEC    ENDP

WAITMSEC    ENDP
WAITMSEC$ASM ENDS
            END;
```

#### ↳ Re: Microfocus DOS zero CPU overhead under WiN

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7svqtn$69t$1@nntp3.atl.mindspring.net>`
- **References:** `<7suoq2$q11$1@news4.svr.pol.co.uk>`

```
Use the windows API 'Sleep'...

kenmullins

Alister Munro <alister@specsoft.freeserve.co.uk> wrote in message
news:7suoq2$q11$1@news4.svr.pol.co.uk...
> I need a way of releasing execution of my DOS applications under the
Windows
> based op.sys's
> (including CITRIX). I'm using Micro Focus Workbench 2,4 & don't wish to
…[17 more quoted lines elided]…
> Ideally I would like to CALL a .bin file which would wait for 0.5 sec's
with
> ZERO CPU overhead whilst returning the system time.
>
…[6 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Microfocus DOS zero CPU overhead under WiN

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t0613$a1b$1@hyperion.mfltd.co.uk>`
- **References:** `<7suoq2$q11$1@news4.svr.pol.co.uk> <7svqtn$69t$1@nntp3.atl.mindspring.net>`

```
Ken,

Alister's app is a 16-bit DOS program written using V2.4. Therefore it
cannot access 32-bit Windows APIs unfortunately. On the 32-bit Micro Focus
products the calls I referred to in my previous post call Sleep, so it
should not be neccesary to call the API directly unless you want an
application to sleep for a specific amout of time.

Ken Mullins wrote in message <7svqtn$69t$1@nntp3.atl.mindspring.net>...
>Use the windows API 'Sleep'...
>
>kenmullins
>
```

##### ↳ ↳ Re: Microfocus DOS zero CPU overhead under WiN

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7t0f3c$gvt$1@aklobs.kc.net.nz>`
- **References:** `<7suoq2$q11$1@news4.svr.pol.co.uk> <7svqtn$69t$1@nntp3.atl.mindspring.net>`

```
Ken Mullins <KenMullins@mindspring.com> wrote:
: Use the windows API 'Sleep'...

That's OK for Windows API programs, but not for DOS applications.

: kenmullins

: Alister Munro <alister@specsoft.freeserve.co.uk> wrote in message
: news:7suoq2$q11$1@news4.svr.pol.co.uk...
:> I need a way of releasing execution of my DOS applications under the
: Windows
:> based op.sys's
:> (including CITRIX). I'm using Micro Focus Workbench 2,4 & don't wish to
:> upgrade as newer versions have much larger execution overheads. Several of

You need to use the DOS/Windows MultiPlex interrupt 0x2F with
AX set to 0x1680.  This does not do a sleep but a despatch which
will release the current time-slice.

Use CALL X"84" with various flags and settings to do this.
```

#### ↳ Re: Microfocus DOS zero CPU overhead under WiN

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 1999-09-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7svan4$6nr$1@hyperion.mfltd.co.uk>`
- **References:** `<7suoq2$q11$1@news4.svr.pol.co.uk>`

```
Alister,

Have you tried calling CBL_YIELD_RUN_UNIT, or if that is not implemented in
2.4 (sorry, I can't remember when it was added), the call it superceded ie
_COYIELD ?


Alister Munro wrote in message <7suoq2$q11$1@news4.svr.pol.co.uk>...
>I need a way of releasing execution of my DOS applications under the
Windows
>based op.sys's
>(including CITRIX). I'm using Micro Focus Workbench 2,4 & don't wish to
>upgrade as newer versions have much larger execution overheads.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
