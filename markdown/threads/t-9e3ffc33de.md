[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Problem with cobol cics program calling assembler module

_24 messages · 13 participants · 1998-06_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Problem with cobol cics program calling assembler module

- **From:** "erich quant" <ua-author-17075175@usenetarchives.gap>
- **Date:** 1998-06-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`

```

I have a big problem and hope you could give me a hint: We have CICS
COBOL/COBOL2 application system that is using several assembler modules
that are called from the cobol programs (call "xxx" using ... not exec
cicsl ink "xxx"). For a while we used MVS SP and CICS 1.7 as development
environment without probles. For some time now we have MVS ESA and CICS 4.1
and now I get big problems trying to use this application.

I simplyfied the problem to "I cann't call my assembler modules under CICS"
- if I do so I get an AEXZ abend code. I cann't find a solution for the
problem.

I hope that you can help me because I couldn't find a solution - even tried
with IBM and other people I know - their hint is to just use cobol modules
or assembler programs called with "EXEC CICS LINK" - yes I know this works
but I need a solution for "call "XXX" using ..." assembler modules.

Thanks in advance

Erich
(eri··.@opt··a.at)

The assembler modules are all very simple and are looking like the
following example:

PRINT NOGEN
ASSTSTP AMODE 31
ASSTSTP RMODE ANY
ASSTSTP CSECT
ENTRY ASSTST
DC CL8'ASSTST ' PROGRAMM-NAME
DC CL2'01' VERSIONSNUMMER
DC CL6'100690' UMWANDLUNGSDATUM
*
* STANDARDSAVEBEREICH FUER DIE REGISTER 0-12,14 UND 15
*
SAVEAREA DC X'00' INT. PROGRAMM-SCHALTER
DC AL3(ASSTSTE-ASSTST) PROGRAMM-LAENGE
DC A(0) ADR. VORGELAGERTE SAVEAREA
DC A(0) ADR. NACHGELAGERTE SAVEAREA
DC 15F'0' SAVEBEREICH D. REGISTER
*
* +------------------------------------------------------+
* I CALL "ASSTST" USING NACH, LAENGE, VON I
* I ==================================================== I
* I VARIABLES UEBERTRAGEN AUS COBOL-PROGRAMMEN I
* +------------------------------------------------------+
*
EJECT
*
* REGISTER SICHERN UND PARAMETER UEBERNEHMEN
*
CNOP 0,4
USING ASSTST,R3 R3 = BASISREGISTER
ASSTST EQU *
STM R14,R12,12(R13) REGISTER SICHERN
LR R3,R15 BASISREGISTER LADEN
L R14,=A(SAVEAREA) R14 = A(NEUE SAVEAREA)
MVI 0(R14),X'F1' KZ. MODUL IN VERWENDUNG
ST R13,4(,R14) ADR. VORGELAGERTE SV-AREA SAV
ST R14,8(,R13) ADR. NACHGELAGERTE SV-AREA SA
LR R13,R14 R13 = A(NEUE SAVEAREA)
LR R4,R1 R4 = A(PARAMETER)
*
* PARAMETER LADEN
*
LR R14,R4 R14 = A(PARAMETER)
*
L R5,0(,R4) R5 = A(ERGEBNIS-BEREICH)
L R6,4(,R4) R6 = A(LAENGE)
LH R6,0(,R6) R6 = LAENGE
SH R6,=H'1' LAENGE - 1 FUER BEFEHLSFORMAT
L R7,8(,R4) R7 = A(AUSGANGS-BEREICH)
*
EX R6,ASSTSTEX MOVE IN GEWUENSCHTER LAENGE
*
* RUECKSPRUNG ZUM ANWENDER
*
MVI 0(R13),1 KZ. MODUL WAR BEREITS IN VERW.
L R13,4(,R13) R13 = A(ALTE SAVEAREA)
LM R14,R12,12(R13) REGISTER 14-12 LADEN
BR R14 RETURN TO USER
*
EJECT
*
LTORG
*
* +------------------------------------------------------+
* I MOVE-BEFEHL FUER DIE BEFEHLS-MODIFIKATION I
* +------------------------------------------------------+
*
DS 0H
ASSTSTEX MVC 0(0,R5),0(7) UEBERTRAGEN IN DER GEW. LAENGE
*
ASSTSTE DS 0D
*
* REGISTER EQUATES
*
R0 EQU 0
R1 EQU 1
R2 EQU 2
R3 EQU 3
R4 EQU 4
R5 EQU 5
R6 EQU 6
R7 EQU 7
R8 EQU 8
R9 EQU 9
R10 EQU 10
R11 EQU 11
R12 EQU 12
R13 EQU 13
R14 EQU 14
R15 EQU 15
END ASSTST
```

#### ↳ Re: Problem with cobol cics program calling assembler module

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-06-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`

```

I have some bad news for you. This is from the LE ILC book (in the section
on ILC under CICS). It sounds like you are not yet at LE (just using VS
COBOL II) but not only is this the "wave of the future" but my guess is the
real answer for today.

>From the URL (all on 1 line - if only it would fit)

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/CEEA404/14.1.6
..1

"Static and dynamic calls are allowed in VS COBOL II, COBOL/370, COBOL for
MVS & VM, and COBOL for OS/390 & VM *to* but *not from( routines written in
non-Language Environment-conforming assembler routines. "
```

#### ↳ Re: Problem with cobol cics program calling assembler module

- **From:** "roland...." <ua-author-6589193@usenetarchives.gap>
- **Date:** 1998-06-21T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p3@usenetarchives.gap>`
- **In-Reply-To:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`

```

Erich,

Erich Quant schrieb in Nachricht <01bd9dbe$09ffd470$3303a8c0@pcqu>...
› I have a big problem and hope you could give me a hint: We have CICS
› COBOL/COBOL2 application system that is using several assembler modules
…[8 more quoted lines elided]…
› problem.
I think this come because the entry point for you cobol-programm is wrong so
cics gets confused. Check the trace table entries in the transaction dump.

Also note your assembler program is NOT reentrent!!! This is a NO-NO for
CICS and I
think every program should be reentrent. I know that CICS is smart enough to
run the
program, but it requires some storage for the ESDSA/SDSA.

Regards

Rol··.@Sch··n.de or Rol··.@t-o··e.de
```

#### ↳ Re: Problem with cobol cics program calling assembler module

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-06-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`

```

Please IGNORE my other post. I just reread your question and realized that
you in COBOL calling Assembler (which is supported) and not vice versa
(which is not). You still may want to check out the URL that I pointed to
for ILC information on COBOL and Assembler under CICS - It might give you
some help on your problem.
```

#### ↳ Re: Problem with cobol cics program calling assembler module

- **From:** "bal oberoi" <ua-author-13993379@usenetarchives.gap>
- **Date:** 1998-06-23T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`

```

Erich Quant wrote:

› I have a big problem and hope you could give me a hint: We have CICS
› COBOL/COBOL2 application system that is using several assembler 
…[4 more quoted lines elided]…
› application.

I seem to remember reading somewhere that a called program in CICS
environment should not have an alternate entry point, i.e. ENTRY point
of the module should be same as the CSECT name. I have looked but have
not yet located where I read this; can anyone else confirm this?

Another thing to check: Your ASSTSTP module is set to use AMODE=31
and RMODE=ANY. What about the calling program?
"If you are passing control between programs executing in different
addressing modes, you must change the AMODE indicator in the PSW".
(MVS Assembler Services Reference, GC28-1910).

Module ASSTSTP does not issue any CICS commands, so it does not
have to be processed by CICS Translator, nor do you need an entry
for it in the PPT. That being so, all CALLs to ASSTSTP *have* to
be static; neither dynamic CALLs nor a CICS LINK is possible.

Hope this is of some help!
MfG,
Bal
obe··.@i··.net
http://www.geocities.com/~oberoi/mainfrme.html
-----
"The universe is full of magical things, 
patiently waiting for our wits to grow sharper." - Eden Phillpotts
```

##### ↳ ↳ Re: Problem with cobol cics program calling assembler module

- **From:** "danie..." <ua-author-6589640@usenetarchives.gap>
- **Date:** 1998-06-25T05:25:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p5@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap>`

```

In article <359··.@i··.net>,
obe··.@i··.net wrote:
› 
› Erich Quant wrote:
…[13 more quoted lines elided]…
› 

I have never tried to use an alternate entry in such a program, but I can't
imagine that this should cause any problem at all.

› Another thing to check: Your ASSTSTP module is set to use AMODE=31
› and RMODE=ANY. What about the calling program?

Another question which seems much more important: Is your assembler-module
linked reentrant? And is it really reentrant?

› "If you are passing control between programs executing in different
› addressing modes, you must change the AMODE indicator in the PSW".
› (MVS Assembler Services Reference, GC28-1910).
› 
 
› The dynamic COBOL-call does this automatically for you!
 
› Module ASSTSTP does not issue any CICS commands, so it does not
› have to be processed by CICS Translator, nor do you need an entry
› for it in the PPT.  That being so, all CALLs to ASSTSTP *have* to
› be static; neither dynamic CALLs nor a CICS LINK is possible.
› 

I am shure that you have to define your ASSEMBLER in the PPT when called
dynamically from COBOL. And via COBOL, you don't load the module from the
STEPLIB but rather from the DFHRPL. Only ASSEMBLER-ASSEMBLER via the LINK- or
LOAD-macro works directly without CICS between (and with poor performance for
the whole CICS)! Both dynamic calls and CICS LINK work fine. I wrote a little
ASSEMBLER which is used in production via dynamic call since one year and I
use CICS LINK with several different ASSEMBLER routines.

› Hope this is of some help!
› MfG,
…[8 more quoted lines elided]…
› 

Cheers

Daniel


"Murpy was an optimist!"

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

- **From:** "bal oberoi" <ua-author-13993379@usenetarchives.gap>
- **Date:** 1998-06-25T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p6@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap>`

```

dan··.@win··r.ch wrote:


› 
›› "If you are passing control between programs executing in different
…[4 more quoted lines elided]…
› The dynamic COBOL-call does this automatically for you!

Agreed. However, unless Erich has the time and inclination to make
changes to his Assembler programs, dynamic CALLs are not an option.
For a program to be called dynamically it has to satisfy several
requirements. A couple I can think of are:
1. It must be CICS-aware, i.e. it must be coded to expect
EIB and CommArea as the first two among the parameters that the
calling program passes to it.
2. The subprogram should be passed through the Translator prior to
assembly, and it should have an entry in the PPT.

› 
›› Another thing to check:  Your ASSTSTP module is set to use 
…[3 more quoted lines elided]…
› assembler-module linked reentrant? And is it really reentrant?

If the CALL to the subprogram is static (i.e. it is linkedited as
part of *each* calling COBOL load module) then reentrancy is not a
requirement; it's enough if it's serially reuseable, or
"quasi-reentrant".

Regards,
Bal
-----
obe··.@i··.net
http://www.geocities.com/~oberoi/mainfrme.html
-----
"The universe is full of magical things,
patiently waiting for our wits to grow sharper." - Eden Phillpotts
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 4)_

- **From:** "frank swarbrick" <ua-author-4445237@usenetarchives.gap>
- **Date:** 1998-06-25T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p7@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap> <gap-9e3ffc33de-p7@usenetarchives.gap>`

```

Bal Oberoi wrote:
› 
›› unknown person wrote:
…[15 more quoted lines elided]…
›    assembly, and it should have an entry in the PPT.

I believe this is not true. I have a completely batch program called CHKALPHA.PHASE.
As long as it is in the PPT, I can call it the following way from a CICS program:

working-storage section.
01 CHKALPHA PIC X(8) VALUE 'CHKALPHA'.

procedure division.
CALL CHKALPHA USING [parameters].

Because I am calling it, not LINKing to it, the EIB and COMMAREAs are not
required in the called program.

Now, CHKALPHA is a COBOL II program, not an assembler program, but I can't
imagine why assembler programs could not be called the same way.

Note that we use VSE, not MVS, but I doubt this makes a difference.
Frank Swarbrick
home: inf··.@spr··t.com
work: fra··.@1st··k.com
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 5)_

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-06-26T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p8@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap> <gap-9e3ffc33de-p7@usenetarchives.gap> <gap-9e3ffc33de-p8@usenetarchives.gap>`

```

On Fri, 26 Jun 1998 18:59:37 -0700, Frank Swarbrick
was insane enough to write:

› Bal Oberoi wrote:
›› 
…[37 more quoted lines elided]…
› work: fra··.@1st··k.com

You are correct. This is a static call. The object of CHKALPHA is
embedded in the object of the calling program at linkedit time and,
therefore, doesn't need a PPT entry nor needs to be aware of the EIB
and COMMAREA. However, if the program was called using EXEC CICS LINK
or EXEC CICS XCTL, it would have to be CICS eligible.

Regards,


////
(o o)
-oOO--(_)--OOo-
Ambition is a poor excuse for not having enough sense to be lazy.
Steve
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 6)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-06-26T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p9@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap> <gap-9e3ffc33de-p7@usenetarchives.gap> <gap-9e3ffc33de-p8@usenetarchives.gap> <gap-9e3ffc33de-p9@usenetarchives.gap>`

```

SkippyPB wrote:
› 
› (snip)
…[25 more quoted lines elided]…
› or EXEC CICS XCTL, it would have to be CICS eligible.

No, no, calling a data_name is *always* a dynamic call, even with the
NODYNAM compiler option. If you're calling an Asm pgm and it doesn't
issue CICS commands, you needn't pass the EIB & Commarea; but you
*always* need a PPT entry for a dynamic call (that's inherent in it's
being dynamic). In the above case the called module (CHKALPHA) will not
be made part of the load module by the linkage editor/Binder.

I think you're mixing the notions of dynamic vs. static with the ability
to issue CICS commands or not.

Bill Lynch

(snipped)
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 7)_

- **From:** "frank swarbrick" <ua-author-4445237@usenetarchives.gap>
- **Date:** 1998-06-26T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p10@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap> <gap-9e3ffc33de-p7@usenetarchives.gap> <gap-9e3ffc33de-p8@usenetarchives.gap> <gap-9e3ffc33de-p9@usenetarchives.gap> <gap-9e3ffc33de-p10@usenetarchives.gap>`

```

Bill Lynch wrote:
› 
› SkippyPB wrote:
…[37 more quoted lines elided]…
› to issue CICS commands or not.

I didn't get SkippyPB's reply to my message, but thanks for coming to my
defense! You are exactly correct. And I can prove it because I never compiled
a CHKALPHA.OBJ, and therefore there's no possible way it could have linked into
my program!
Frank Swarbrick
home: inf··.@spr··t.com
work: fra··.@1st··k.com
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 7)_

- **From:** "stev..." <ua-author-6589195@usenetarchives.gap>
- **Date:** 1998-06-27T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p10@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap> <gap-9e3ffc33de-p7@usenetarchives.gap> <gap-9e3ffc33de-p8@usenetarchives.gap> <gap-9e3ffc33de-p9@usenetarchives.gap> <gap-9e3ffc33de-p10@usenetarchives.gap>`

```

On Sat, 27 Jun 1998 20:05:02 -0400, Bill Lynch
was insane enough to write:

› SkippyPB wrote:
›› 
…[40 more quoted lines elided]…
› (snipped)

Bill, you are absolutely correct. I missed seeing that he was calling
the program using a data name. Got confused because the data name
value and the actual phase name were the same.

Sorry about that!

Regards,


////
(o o)
-oOO--(_)--OOo-
Everyone has a photographic memory. Some don't have film.
Steve
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 8)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-06-27T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p12@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap> <gap-9e3ffc33de-p7@usenetarchives.gap> <gap-9e3ffc33de-p8@usenetarchives.gap> <gap-9e3ffc33de-p9@usenetarchives.gap> <gap-9e3ffc33de-p10@usenetarchives.gap> <gap-9e3ffc33de-p12@usenetarchives.gap>`

```

SkippyPB wrote:
› 
› (snip)
…[17 more quoted lines elided]…
› value and the actual phase name were the same.

Not to worry - I do that all the time, too!

Bill Lynch :-)

(snipped)
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 5)_

- **From:** "bal oberoi" <ua-author-13993379@usenetarchives.gap>
- **Date:** 1998-06-26T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-9e3ffc33de-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-9e3ffc33de-p8@usenetarchives.gap>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <gap-9e3ffc33de-p5@usenetarchives.gap> <gap-9e3ffc33de-p6@usenetarchives.gap> <gap-9e3ffc33de-p7@usenetarchives.gap> <gap-9e3ffc33de-p8@usenetarchives.gap>`

```

Frank Swarbrick wrote:

›››› "If you are passing control between programs executing in 
›››› different addressing modes, you must change the AMODE indicator 
›››› in the PSW".  (MVS Assembler Services Reference, GC28-1910).
 
››› The dynamic COBOL-call does this automatically for you!
 
›› 
›› Agreed. However, unless Erich has the time and inclination to make
…[7 more quoted lines elided]…
››    assembly, and it should have an entry in the PPT.
 
› 
› I believe this is not true.  I have a completely batch program called 
…[15 more quoted lines elided]…
› Note that we use VSE, not MVS, but I doubt this makes a difference.

Well, I stand corrected! I have never seen it done, but the manual,
(COBOL for MVS/VM, Prog. Gde.), certainly backs you up:

* CALL identifier can be used with the NODYNAM compiler option to
dynamically call a program. Called programs can contain any
function supported by CICS for the language. Dynamically called
programs have to be defined in the CICS program processing table
(PPT).
* If you are calling a COBOL program that has been translated, you
must pass DFHEIBLK and DFHCOMMAREA as the first two parameters in
the CALL statement.

It's a tad ambiguous. But based on your experience it would appear
that:
If a subprogram, called dynamically, does not use any CICS
functions, it does not have to be translated.
And if the Translator did not stick any CICS-related stuff into the
code, it does not have to be passed pointers to EIB and CommArea.
In any event, for a dynamic CALL to work, the called program must
have an entry in the PPT.

Thanks for sharing your experience, Frank.

Best of regards,
Bal
-----
obe··.@i··.net
http://www.geocities.com/~oberoi/mainfrme.html
-----
"The universe is full of magical things,
patiently waiting for our wits to grow sharper." - Eden Phillpotts
```

#### ↳ Re: Problem with cobol cics program calling assembler module

- **From:** Bal Oberoi <oberoi@ibm.net>
- **Date:** 1998-06-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35910C96.5082@ibm.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu>`

```

Erich Quant wrote:
 
> I have a big problem and hope you could give me a hint: We have CICS
> COBOL/COBOL2 application system that is using several assembler 
…[4 more quoted lines elided]…
> application.
 
I seem to remember reading somewhere that a called program in CICS 
environment should not have an alternate entry point, i.e. ENTRY point 
of the module should be same as the CSECT name. I have looked but have 
not yet located where I read this; can anyone else confirm this?

Another thing to check:  Your ASSTSTP module is set to use AMODE=31 
and RMODE=ANY.  What about the calling program? 
"If you are passing control between programs executing in different 
addressing modes, you must change the AMODE indicator in the PSW". 
(MVS Assembler Services Reference, GC28-1910).

Module ASSTSTP does not issue any CICS commands, so it does not 
have to be processed by CICS Translator, nor do you need an entry 
for it in the PPT.  That being so, all CALLs to ASSTSTP *have* to 
be static; neither dynamic CALLs nor a CICS LINK is possible.

Hope this is of some help!
MfG, 
Bal
```

##### ↳ ↳ Re: Problem with cobol cics program calling assembler module

- **From:** daniel.jacot@winterthur.ch
- **Date:** 1998-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mt51o$f41$1@nnrp1.dejanews.com>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net>`

```

In article <35910C96.5082@ibm.net>,
  oberoi@ibm.net wrote:
>
> Erich Quant wrote:
…[13 more quoted lines elided]…
>

I have never tried to use an alternate entry in such a program, but I can't
imagine that this should cause any problem at all.

> Another thing to check:  Your ASSTSTP module is set to use AMODE=31
> and RMODE=ANY.  What about the calling program?

Another question which seems much more important: Is your assembler-module
linked reentrant? And is it really reentrant?

> "If you are passing control between programs executing in different
> addressing modes, you must change the AMODE indicator in the PSW".
> (MVS Assembler Services Reference, GC28-1910).
>

The dynamic COBOL-call does this automatically for you!

> Module ASSTSTP does not issue any CICS commands, so it does not
> have to be processed by CICS Translator, nor do you need an entry
> for it in the PPT.  That being so, all CALLs to ASSTSTP *have* to
> be static; neither dynamic CALLs nor a CICS LINK is possible.
>

I am shure that you have to define your ASSEMBLER in the PPT when called
dynamically from COBOL. And via COBOL, you don't load the module from the
STEPLIB but rather from the DFHRPL. Only ASSEMBLER-ASSEMBLER via the LINK- or
LOAD-macro works directly without CICS between (and with poor performance for
the whole CICS)! Both dynamic calls and CICS LINK work fine. I wrote a little
ASSEMBLER which is used in production via dynamic call since one year and I
use CICS LINK with several different ASSEMBLER routines.

> Hope this is of some help!
> MfG,
…[8 more quoted lines elided]…
>

Cheers

Daniel


"Murpy was an optimist!"

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/   Now offering spam-free web-based newsreading
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

- **From:** Bal Oberoi <oberoi@ibm.net>
- **Date:** 1998-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3593AA30.704E@ibm.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com>`

```

daniel.jacot@winterthur.ch wrote:


> 
> > "If you are passing control between programs executing in different
…[4 more quoted lines elided]…
> The dynamic COBOL-call does this automatically for you!

Agreed. However, unless Erich has the time and inclination to make 
changes to his Assembler programs, dynamic CALLs are not an option.
For a program to be called dynamically it has to satisfy several 
requirements.  A couple I can think of are:
1. It must be CICS-aware, i.e. it must be coded to expect 
   EIB and CommArea as the first two among the parameters that the 
   calling program passes to it.
2. The subprogram should be passed through the Translator prior to 
   assembly, and it should have an entry in the PPT. 

> 
> > Another thing to check:  Your ASSTSTP module is set to use 
…[3 more quoted lines elided]…
> assembler-module linked reentrant? And is it really reentrant?

If the CALL to the subprogram is static (i.e. it is linkedited as 
part of *each* calling COBOL load module) then reentrancy is not a 
requirement; it's enough if it's serially reuseable, or 
"quasi-reentrant". 

Regards,
Bal
----- 
oberoi@ibm.net
http://www.geocities.com/~oberoi/mainfrme.html
-----
"The universe is full of magical things, 
patiently waiting for our wits to grow sharper." - Eden Phillpotts
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 4)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-06-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35945209.79B9@sprynet.com>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net>`

```

Bal Oberoi wrote:
> 
> > unknown person wrote:
…[15 more quoted lines elided]…
>    assembly, and it should have an entry in the PPT.

I believe this is not true.  I have a completely batch program called CHKALPHA.PHASE.
As long as it is in the PPT, I can call it the following way from a CICS program:

working-storage section.
  01  CHKALPHA    PIC X(8)   VALUE 'CHKALPHA'.

procedure division.
  CALL CHKALPHA USING [parameters].

Because I am calling it, not LINKing to it, the EIB and COMMAREAs are not
required in the called program.

Now, CHKALPHA is a COBOL II program, not an assembler program, but I can't
imagine why assembler programs could not be called the same way.

Note that we use VSE, not MVS, but I doubt this makes a difference.
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 5)_

- **From:** stevewie@apk.dot.net (SkippyPB)
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<359523ca.3949052@news.apk.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com>`

```

On Fri, 26 Jun 1998 18:59:37 -0700, Frank Swarbrick
<infocat@sprynet.com> was insane enough to write:

>Bal Oberoi wrote:
>> 
…[37 more quoted lines elided]…
>work: frank.swarbrick@1stbank.com

You are correct.  This is a static call.  The object of CHKALPHA is
embedded in the object of the calling program at linkedit time and,
therefore, doesn't need a PPT entry nor needs to be aware of the EIB
and COMMAREA.  However, if the program was called using EXEC CICS LINK
or EXEC CICS XCTL, it would have to be CICS eligible.

Regards,


          ////
         (o o)
-oOO--(_)--OOo-
Ambition is a poor excuse for not having enough sense to be lazy.
 Steve
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 6)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6n41at$5lg@bgtnsc03.worldnet.att.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net>`

```

SkippyPB wrote:
> 
(snip)
> >I believe this is not true.  I have a completely batch program called CHKALPHA.PHASE.
> >As long as it is in the PPT, I can call it the following way from a CICS program:
…[23 more quoted lines elided]…
> or EXEC CICS XCTL, it would have to be CICS eligible.

No, no, calling a data_name is *always* a dynamic call, even with the
NODYNAM compiler option. If you're calling an Asm pgm and it doesn't
issue CICS commands, you needn't pass the EIB & Commarea; but you
*always* need a PPT entry for a dynamic call (that's inherent in it's
being dynamic). In the above case the called module (CHKALPHA) will not
be made part of the load module by the linkage editor/Binder.

I think you're mixing the notions of dynamic vs. static with the ability
to issue CICS commands or not.

Bill Lynch

(snipped)
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 7)_

- **From:** Frank Swarbrick <infocat@sprynet.com>
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3595B520.3A01@sprynet.com>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net> <6n41at$5lg@bgtnsc03.worldnet.att.net>`

```

Bill Lynch wrote:
> 
> SkippyPB wrote:
…[37 more quoted lines elided]…
> to issue CICS commands or not.

I didn't get SkippyPB's reply to my message, but thanks for coming to my
defense!  You are exactly correct.  And I can prove it because I never compiled
a CHKALPHA.OBJ, and therefore there's no possible way it could have linked into
my program!
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 7)_

- **From:** stevewie@apk.dot.net (SkippyPB)
- **Date:** 1998-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35986d71.3026751@news.apk.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net> <6n41at$5lg@bgtnsc03.worldnet.att.net>`

```

On Sat, 27 Jun 1998 20:05:02 -0400, Bill Lynch
<wblynch@worldnet.att.net> was insane enough to write:

>SkippyPB wrote:
>> 
…[40 more quoted lines elided]…
>(snipped)

Bill, you are absolutely correct.  I missed seeing that he was calling
the program using a data name.  Got confused because the data name
value and the actual phase name were the same.  

Sorry about that!

Regards,


          ////
         (o o)
-oOO--(_)--OOo-
Everyone has a photographic memory. Some don't have film.
 Steve
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 8)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1998-06-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6n693c$7o8@bgtnsc03.worldnet.att.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com> <359523ca.3949052@news.apk.net> <6n41at$5lg@bgtnsc03.worldnet.att.net> <35986d71.3026751@news.apk.net>`

```

SkippyPB wrote:
> 
(snip)
> >
> >No, no, calling a data_name is *always* a dynamic call, even with the
…[15 more quoted lines elided]…
> value and the actual phase name were the same.

Not to worry - I do that all the time, too!

Bill Lynch :-)

(snipped)
```

###### ↳ ↳ ↳ Re: Problem with cobol cics program calling assembler module

_(reply depth: 5)_

- **From:** Bal Oberoi <oberoi@ibm.net>
- **Date:** 1998-06-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3595300F.66C2@ibm.net>`
- **References:** `<01bd9dbe$09ffd470$3303a8c0@pcqu> <35910C96.5082@ibm.net> <6mt51o$f41$1@nnrp1.dejanews.com> <3593AA30.704E@ibm.net> <35945209.79B9@sprynet.com>`

```

Frank Swarbrick wrote:

> > > > "If you are passing control between programs executing in 
> > > > different addressing modes, you must change the AMODE indicator 
> > > > in the PSW".  (MVS Assembler Services Reference, GC28-1910).

> > > The dynamic COBOL-call does this automatically for you!

> >
> > Agreed. However, unless Erich has the time and inclination to make
…[7 more quoted lines elided]…
> >    assembly, and it should have an entry in the PPT.

> 
> I believe this is not true.  I have a completely batch program called 
…[15 more quoted lines elided]…
> Note that we use VSE, not MVS, but I doubt this makes a difference.

Well, I stand corrected! I have never seen it done, but the manual, 
(COBOL for MVS/VM, Prog. Gde.), certainly backs you up:

* CALL identifier can be used with the NODYNAM compiler option to 
  dynamically call a program.  Called programs can contain any 
  function supported by CICS for the language.  Dynamically called 
  programs have to be defined in the CICS program processing table 
  (PPT).
* If you are calling a COBOL program that has been translated, you 
  must pass DFHEIBLK and DFHCOMMAREA as the first two parameters in 
  the CALL statement.

It's a tad ambiguous. But based on your experience it would appear 
that: 
  If a subprogram, called dynamically, does not use any CICS 
  functions, it does not have to be translated. 
  And if the Translator did not stick any CICS-related stuff into the 
  code, it does not have to be passed pointers to EIB and CommArea.
  In any event, for a dynamic CALL to work, the called program must 
  have an entry in the PPT.

Thanks for sharing your experience, Frank.  

Best of regards,
Bal
----- 
oberoi@ibm.net
http://www.geocities.com/~oberoi/mainfrme.html
-----
"The universe is full of magical things, 
patiently waiting for our wits to grow sharper." - Eden Phillpotts
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
