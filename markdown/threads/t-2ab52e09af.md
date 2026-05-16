[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# To See Whats Happen - Cobol Call Statistik

_9 messages · 5 participants · 2001-09_

---

### To See Whats Happen - Cobol Call Statistik

- **From:** Andreas Lerch <andreaslerch@t-online.de>
- **Date:** 2001-09-08T12:05:46+00:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<20010908.12054669@04307839700-0001.dialin.t-online>`

```
Hallo,

system: OS-390-2.10 with COBOL for MVS and COBOL-II

I have this idea: In my LE-370 Environment (test and development) i 
want to see which programm is calling other programms.

	Call from - Call to - Call Count
	PGM1		PGM2		500
	PGM3		PGM2		200
and so on

To do this i modify IGZCLNK to get control on each LE-Call.

My applikation design is fixed. Very early i can get control. The 
first call in each mainprogramm is a initial-call to build instorage 
tables for variable data.

When i replace IGZCLNK with my programm i got system abends 0C1,0C4. 
Therefore i must do this:

	ICM R15,B'1111',R15+6
	BSM 0,R15
	DS 2H		her is the adress of my module

to modify IGZCLNK i am building a Loadmodule with my litte programm 
including IGZCLNK as statik CALL (V-Const) and BINDER ALIAS. I can not 
modify the module in storage, because it is linked with the options: 
RES,RENT,REUSE and storage protected

Then i move the first 4 bytes in my programm and modify the first 10 
bytes of the IGZ-Module with my little code.

When IGZCLNK gets control, my code is invoked and works fine. After my 
work i restore the register and execute the saved small 4 byte code 
(X'47F0F028')

First i want to get the name of the calling programm. To get this i 
point over register 13 and register 15 to the entrypoint, twice if 
ENTRY DLITCBL is coded. On fixed positions there are some eye-catcher 
to position to the right position in the module. Differences between 
COBOL-II and CEE and my assembler routines. I coded this some time ago 
and it works fine too.

Here my litte problem.

IGZCLNK is call with:

	Reg 13: positioning to dynamic storage - savearea
	Reg 14: Return in calling programm
	Reg 15: EPA-Adress of IGZCLNK
	REG 1: is positioning in the Literal-Pool

In front of invoking IGZCLNK the cobol code says something like this:

	MVC TS=1,@parm1
	MVC TS=2,@parm2
	MVC TS=3,='Name of Subprogram'
	LA R1,PGMLIT+3882
	LA R15,=V(IGZCLNK)
	BALR R14,R15

how can i positioning into the cobol-areas to get the name of the 
called programm. I think its very easy because there are some 
performance hints to call programms but i can not see how easy it is.

Yesterday i am testing with XPEDITER and COBOL compile LIST NOOFFSET 
to get all this informations. Can anybody help me...

some weeks ago i have build a DL1 and DB2 interface to get the counter 
of this calls. This works very fine and helps a lot to get potential 
run/time problems.

thank you all

Andreas
```

#### ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2001-09-11T18:29:13+00:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<20010911.18291337@04307839700-0001.dialin.t-online>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 08.09.01, 12:05:46, schrieb Andreas Lerch <andreaslerch@t-online.de> 
zum Thema To See Whats Happen - Cobol Call Statistik:


> Hallo,

> system: OS-390-2.10 with COBOL for MVS and COBOL-II

> I have this idea: In my LE-370 Environment (test and development) i
> want to see which programm is calling other programms.


I think i got it:

its very simple i think:

First i do this to modify IGZCLNKL:

(I am soory about the german comments!)

*--------------------------------------------------------------------
-*
*--- DIE ERSTEN 4 BYTES DES PROGRAMMES IGZCLNK WERDEN IN DAS FELD  
---*
*--- SS22IGZ GEBRACHT -> VOM SS22 ZUM IGZCLNK                      ---*
*--- DANN WERDEN DIE ERSTEN BYTES VOM IGZK                         
---*
*--------------------------------------------------------------------
-*
IGZMOVE1 B     24(R15)
IGZMOVE  MVC   24(0,R1),IGZHDR
IGZHDRL  DC    AL1(IGZHDRE-IGZHDR)
         DS    0F                  VOLLWORTGRENZE
         DS    H                   EIN HALBWORT WEITER
IGZHDR   EQU   *
         ICM   R15,B'1111',30(R15) 4 BYTES ICM START AUF 
HALBWORTGRENZE
         BSM   0,R15               2 BYTES BSM
IGZSS22  DS    0A                  4 BYTES ADRESSE
PUQSS22K DS    A
IGZHDRE  EQU   *
PIGZCLNK DC    V(IGZCLNK)          IGZCLNK ORIGINALADRESSE

Then, when i got control the first time, i modify line this:

*------- MODIFY IGZLNK HDR
         L     R1,PIGZCLNK         ADRESSIEREN IGZCLNK
         MVC   SS22IGZ(4),0(R1)    SICHERN DER ERSTEN 4 BYTES
         IC    R14,IGZHDRL         LAENGE ZAP
         EX    R14,IGZMOVE         IGZCLNK AENDERN
         MVC   00(4,R1),IGZMOVE1   IGZCLNK AENDERN


The following is what i want, Register 1 points to an area inside the 
Literal-Pool which indicates the style of the call and the offset of 
the clear name on the calling program:

there are differences between static and dynamic link also cancel-call


*------- ANALYSE CALLING
         MVC   STABTPRG,=CL8'??'   PROGRAMMNAME
         L     R14,4(R13)          VORHERIGE SAVEAREA
         L     R5,PARAM            REGISTER 1
         XR    R6,R6               LOESCHEN REGISTER 5
         ICM   R6,B'0111',5(R5)    LADEN OFFSET
         AR    R14,R6              PLUS BASIS
         MVI   STABIDNT,STAB_UNBE  SETZEN INDIKATOR UNBEKANNT
         IF    (CLI,0(R5),EQ,X'A6'), ? CALL INDIKATOR MIT PARAMETER
               OR,
               (CLI,0(R5),EQ,X'A2') ? CALL INDIKATOR OHNE PARAMETER
          MVI  STABIDNT,STAB_CALL  SETZEN CALL
         ENDIF
         IF    (CLI,0(R5),EQ,X'62') ? CALL INDIKATOR
          MVI  STABIDNT,STAB_CANC  SETZEN CANCEL
         ENDIF
         IF    (CLI,0(R5),EQ,X'96') ? CALL INDIKATOR STATISCHER CALL
          MVI  STABIDNT,STAB_STAT  SETZEN STATISCH
          LA   R14,KSTATIK
         ENDIF
         MVC   STABTPRG,0(R14)     UEBERTRAGEN PGMNAMEN

i get all my information i want. Including an internal table i can 
count all:

Callfrom-Type-Callto - so i can get the full volume of calls anf can 
tell my - sorry - softwarespecialist, where they are wrong, and keep 
clear resources by imlementation of a small part of instructions (i.e. 
IF THEN ELSE....)

This is the output of my little pProgram:

UQSS22K 14:10:56.361430: CallVon   CallNach  Anzahl Calls
UQSS22K 14:10:56.361455: TQAS05K   IEFBR14              6
UQSS22K 14:10:56.361480:           UQAS05K             15
UQSS22K 14:10:56.361504:           UQSS14K              1
UQSS22K 14:10:56.361527:           UQTA05K7             1
UQSS22K 14:10:56.361556:           UQAS05K              8  Cancel
UQSS22K 14:10:56.361586: UQAS05K   CEELOCT              9  Get Current 
Local Dat
UQSS22K 14:10:56.361610:           UQAS08K             24
UQSS22K 14:10:56.361635:           UQTA05K2            19
UQSS22K 14:10:56.361659: Summe                         83

i hope this is a interesting work - it is xp - experimantal - and: If 
you 
have it, you miss it in the past. If you dont know about this, you 
never miss it :-)

thanks - Andreas Lerch -
```

##### ↳ ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** Max <petteno@generali.it>
- **Date:** 2001-09-13T10:36:52+02:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<3BA07024.2596702B@generali.it>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online> <20010911.18291337@04307839700-0001.dialin.t-online>`

```
Where did you find IGZCLNK source code?

TIA
Max
```

###### ↳ ↳ ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2001-09-13T17:54:07+00:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<20010913.17540783@04307839700-0001.dialin.t-online>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online> <20010911.18291337@04307839700-0001.dialin.t-online> <3BA07024.2596702B@generali.it>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 13.09.01, 08:36:52, schrieb Max <petteno@generali.it> zum Thema Re: 
To See Whats Happen - Cobol Call Statistik:


> Where did you find IGZCLNK source code?

Hello

I learn assembler in the late 70th early 80th, yes more than 20 years 
ago - i'm 41 year old - some times, long time ago, i must read dumps 
and interpret COBOL generation of Assembler code. Some times i can 
'disassembler in mind' some code forward and backward of a 
dump-position. Its - in german sorry - 'Erfahrung' (experience) and 
'Neugierde' (searching for ..) and some litte code which is generated 
by the cobol-compiler LA..ST..BALR..

then i code a small programm to dump the area passe by register 1 - 
and -and -and 

the rest: investing of time.....

i never change the original module IGZCLNK (now IGZCFCC too), i only 
modify the storage in the loaded program :-) Zap-Inflight

have a nice day

i think, i do the right work for which i want.

Andreas
```

#### ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2001-09-11T18:51:02+00:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<20010911.18510220@04307839700-0001.dialin.t-online>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 08.09.01, 12:05:46, schrieb Andreas Lerch <andreaslerch@t-online.de> 
zum Thema To See Whats Happen - Cobol Call Statistik:


> Hallo,

> system: OS-390-2.10 with COBOL for MVS and COBOL-II

> I have this idea: In my LE-370 Environment (test and development) i
> want to see which programm is calling other programms.



One final word:

if you do this and you are an systemprogrammer (SMP and Installation) 
you can control it - Usermodification.

If you are a small programme - like me - you must hurry every time a 
stupid systemprogrammer changes cobol.

Sorry - i know both jobs - i am a application programmer and in the 
past i do the smp-work with the mask of a systemprogrammer - both, 
appl and sys, must work togehter, to make a good and efficient work.

If i kick off anybody - sorry
if not - smile

hallo world

Andreas
```

##### ↳ ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-09-13T14:52:28+12:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<3ba0200a_6@news.newsgroups.com>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online> <20010911.18510220@04307839700-0001.dialin.t-online>`

```
Well, you made ME smile, Andreas...<G>

(Especially the bit about XORing Register 6 with itself to clear it, when
the comment (translated) says "Clear Register 5"....)

MORAL: Don't put comments in Assembler code unless you intend to maintain
them...<G>


Pete.
"Andreas Lerch" <andreas@andreas-lerch.de> wrote in message
news:20010911.18510220@04307839700-0001.dialin.t-online...


>>>>>>>>>>>>>>>>>> Ursprï¿½ngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 08.09.01, 12:05:46, schrieb Andreas Lerch <andreaslerch@t-online.de>
zum Thema To See Whats Happen - Cobol Call Statistik:


> Hallo,

> system: OS-390-2.10 with COBOL for MVS and COBOL-II

> I have this idea: In my LE-370 Environment (test and development) i
> want to see which programm is calling other programms.



One final word:

if you do this and you are an systemprogrammer (SMP and Installation)
you can control it - Usermodification.

If you are a small programme - like me - you must hurry every time a
stupid systemprogrammer changes cobol.

Sorry - i know both jobs - i am a application programmer and in the
past i do the smp-work with the mask of a systemprogrammer - both,
appl and sys, must work togehter, to make a good and efficient work.

If i kick off anybody - sorry
if not - smile

hallo world

Andreas






-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2001-09-13T17:37:36+00:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<20010913.17373686@04307839700-0001.dialin.t-online>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online> <20010911.18510220@04307839700-0001.dialin.t-online> <3ba0200a_6@news.newsgroups.com>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 13.09.01, 02:52:28, schrieb "Peter E. C. Dashwood" 
<dashwood@nospam.enternet.co.nz> zum Thema Re: To See Whats Happen - 
Cobol Call Statistik:


> Well, you made ME smile, Andreas...<G>

> (Especially the bit about XORing Register 6 with itself to clear it, 
when
> the comment (translated) says "Clear Register 5"....)

> MORAL: Don't put comments in Assembler code unless you intend to 
maintain
> them...<G>


My comments are not for me, my comments are for 
nonreadingassembleryoungpeopelwhoonlyknowcobolorc - i correct it! ;-)

Andreas
```

###### ↳ ↳ ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** Wild Bill <nospam@today.thanks>
- **Date:** 2001-09-19T08:58:41-07:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<B7CE0EC1.18DF6%nospam@today.thanks>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online> <20010911.18510220@04307839700-0001.dialin.t-online> <3ba0200a_6@news.newsgroups.com>`

```
I used to work with some Japanese microcoders. While they couldn't read
English, per se', they did have a thorough grasp of the storage controller
microcode assembler. On several instances, they'd change the coded
instruction, but neglect to change the comments.

The four letter words that flowed forth from this one "Good 'ol boy" were
truly astounding after he figured out what had happened to his recovery
routine...

in article 3ba0200a_6@news.newsgroups.com, Peter E. C. Dashwood at
dashwood@nospam.enternet.co.nz wrote on 09/12/2001 19:52:

> Well, you made ME smile, Andreas...<G>
> 
…[54 more quoted lines elided]…
> -----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

#### ↳ Re: To See Whats Happen - Cobol Call Statistik

- **From:** Andreas Lerch <andreas@andreas-lerch.de>
- **Date:** 2001-09-14T14:06:08+00:00
- **Newsgroups:** comp.lang.asm370,comp.lang.cobol
- **Message-ID:** `<20010914.14060834@04307839700-0001.dialin.t-online>`
- **References:** `<20010908.12054669@04307839700-0001.dialin.t-online>`

```


>>>>>>>>>>>>>>>>>> Ursprüngliche Nachricht <<<<<<<<<<<<<<<<<<

Am 08.09.01, 12:05:46, schrieb Andreas Lerch <andreaslerch@t-online.de> 
zum Thema To See Whats Happen - Cobol Call Statistik:


> Hallo,

> system: OS-390-2.10 with COBOL for MVS and COBOL-II

Here is my solution - sorry about the 6k attached file - it shows what 
i have done

there are 4 different Programms:

UQTA05K* - central manager
UQSS20K  - IMS (CBLTDLI/ASMTDLI) Interface
UQSS21K* - DB2 (DSNHLI) Interface
UQSS22K  - COBOL-II Cobol for MVS Interface

the first call initialized tables, at Termination (normal and 
abnormal) the tables are printet

i can see which type of DB-Call is done and where the modules located 
in which version.

The details of UQSS2* are only in test the other lines are also in 
production.

It saves a lot of time to analyse potetial problems.

I think I do a nice work! (selfpraise <G>)

Thank you to notice me

freundliche gruesse

Andreas
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
