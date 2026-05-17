[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microsoft COBOL Question

_1 message · 1 participant · 1995-02_

---

### Microsoft COBOL Question

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-02-07T14:15:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-zxYbMU53pDc@usenetarchives.gap>`

```
The following question came from a chap on Bix.
If you have an answer, please reply to a.··.@b··.com.

TITLE: linking with microfocus cobol and C

Hi I have specific question about linking a cobol (microfocus) obj
with a C obj, we have tried following the indications in the
microfocus manual and it blows up in our faces, if appropriate I can
post the basic code for everything in our "hello" test program and
perhaps someone can tell me what we are doing wrong, we are not at
the stage where we are linking to a production program but rather
just trying to find our way through, the cobol part is not of our
doing but rather a banking program into which we have to tye our
signature registration database, please advise as we have to deliver
by Monday.

Tks Ariel

cobol/general #552, from aft, 4686 chars, Thu Feb 2 16:06:10 1995
This is a comment to message 551.
There is/are comment(s) on this message.
--------------------------
This is what we are trying to do please look it over or tell us where to
post it if this is not the appropriate place.

. Product: Micro Focus COBOL/2 for use with DOS and OS/2 Operating
System
. Version : 1.2
. Computer: Olivetti 486
. Compaq contura 386/sx, 3/25, 120 MB HD, 4 Mb ram, single user
. Novell 3.11 en the Olivetti

. Config. sys
DEVICE=C:¥QEMM¥QEMM386.SYS RAM
BUFFERS=15,0
FILES=90
DOS=UMB
LASTDRIVE=E
FCBS=16,8
DEVICEHIGH /L:1,12192 =C:¥DOS¥SETVER.EXE
DEVICEHIGH /L:1,15872 =C:¥DOS¥DISPLAY.SYS CON=(EGA,,1)
COUNTRY=034,850,C:¥DOS¥COUNTRY.SYS
DOS=HIGH
STACKS=9,256

. Autoexec.bat
PATH
C:¥QEMM;C:¥WINWORD;C:¥CLARION;C:¥CPQDOS;C:¥;C:¥DOS;C:¥WINDOWS;C:¥MOUSE;C:
¥TOOLBOOK;C:¥PCLINK;C:¥WP51¥
PATH %PATH%;C:¥XTG;C:¥C600¥BIN;C:¥C600¥BINW;C:¥COMPEL;C:¥DATAFAX
SET PROMPT=$P$G
SET TEMP=C:¥WINDOWS¥TEMP
LH /L:1,7840 C:¥DOS¥NLSFUNC C:¥DOS¥COUNTRY.SYS
C:¥CPQDOS¥MODE CON CP PREP=((850,437) C:¥DOS¥EGA.CPI)
C:¥CPQDOS¥MODE CON CP SEL=850
C:¥CPQDOS¥KEYB us, 850, C:¥CPQDOS¥KEYBOARD.SYS
IF NOT EXIST C:¥CPQDOS¥SAVEDONE.CPQ CALL SAVEALL /A
LH /L:0;1,42896 /S C:¥DOS¥SMARTDRV.EXE
C:¥MOUSE¥MOUSE.COM
LH /L:1,6544 c:¥dos¥doskey
C:¥CPQDOS¥MODE.COM CO80
LH /L:1,14064 C:¥DOS¥SHARE.EXE

. Page & manual used as ref:

Operating Guide
Capitulos 10, 11, 13
Specifically interfacing With MSC v 6.0
page 13-2 as linking example

. Problem:

Given the following cobol source:
$SET ANS85 SPZERO noosvs mf nocsi
IDENTIFICATION DIVISION.
PROGRAM-ID. PRU.
ENVIRONMENT DIVISION.
CONFIGURATION SECTION.
SPECIAL-NAMES.
DECIMAL-POINT IS COMMA.
INPUT-OUTPUT SECTION.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 NRO-IMAGEN PIC 99 COMP-X.
01 ANCHO-IMAGEN PIC 9(4) COMP-X.
01 ALTO-IMAGEN PIC 9(4) COMP-X.
01 NADA PIC X.
01 RETORNO PIC 9(4) COMP-X.
01 RET-MUESTRO PIC Z(3)9.
*-----------------------------------------------------
PROCEDURE DIVISION.
0100-TRONCO SECTION.
0110-CARGO-PARAMETROS.
MOVE 1 TO NRO-IMAGEN.
MOVE 300 TO ANCHO-IMAGEN.
MOVE 100 TO ALTO-IMAGEN.
DISPLAY "ANTES DEL CALL:" AT 0310.
ACCEPT NADA AT 0325
* DISPLAY " " CLEAR SCREEN.
CALL "EDIBROU" USING "1" "100" "100".
* USING NRO-IMAGEN ANCHO-IMAGEN ALTO-IMAGEN
* GIVING RETORNO.
* DISPLAY " " CLEAR SCREEN.
MOVE RETORNO TO RET-MUESTRO.
DISPLAY "LUEGO DEL CALL:" AT 0510
DISPLAY RET-MUESTRO AT 0525
ACCEPT NADA AT 0325.
STOP-RUN.

and the folllowing C source

------------------------------------------------------------
#include
int edibrou()
{
printf("Hola, mundo");
return(0);
}
------------------------------------------------------------
Compiled with

------------------------------------------------------------
cl edibrou /Aulf
------------------------------------------------------------

Linkedited with
------------------------------------------------------------
2
LINK PRU+EDIBROU+MFC6INTF+C6DOSIF+C6DOSLB,,,COBLIB+COBAPI+LLIBCE/NOE
------------------------------------------------------------

you get
------------------------------------------------------------

Microsoft (R) Segmented-Executable Linker Version 5.03
Copyright (C) Microsoft Corp 1984-1989. All rights reserved.

Definitions File [NUL.DEF]:
LLIBCE.LIB(chkstk.asm) : error L2025: __chkstk : symbol defined
more than once
LLIBCE.LIB(output.asm) : warning L4004: possible fixup
overflow at 18 in segment _TEXT
target external '__CHKSTK'
LLIBCE.LIB(write.asm) : warning L4004: possible fixup
overflow at BE in segment _TEXT
target external '__CHKSTK'

There was 1 error detected

------------------------------------------------------------
If despite the mesg you try it, it hangs after showing the
"ANTES DEL CALL" text onscreen


Where we want to get to:


A MSC 6.0 Prog usign graphics and reserving memory dinamically
with
------------------------------------------------------------
#include
#include

imagen = (char _huge *) halloc (cimagen,1);
clip = (char _huge *) halloc (cclip,1);
pantalla = (char _huge *) halloc (cpantalla,1);
WorkBuff=(char far *)_fmalloc(35256U);
WorkBuff=(char far *) _fmalloc(12574);


All comments welcome.
Ariel

cobol/general #553, from pbpotter, 402 chars, Sat Feb 4 01:01:57 1995
This is a comment to message 552.
--------------------------
The __chkstk reference is to the stack probe the Microsoft compiler
inserts by default. Add the /Gs option to the compile to eliminate
it. As to the eccentricities of linking C modules with Cobol, I
haven't got a clue. My Microsoft manuals discuss linking with Basic,
Fortran, Pascal, but nothing about Cobol. I would have to know how
Cobol passes parameters and, quite possibly, a lot of other stuff.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
