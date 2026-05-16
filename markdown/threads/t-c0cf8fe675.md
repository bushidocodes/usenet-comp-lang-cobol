[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# 32 Bit ASM from 32 Bit Windows COBOL

_6 messages · 2 participants · 2000-02_

---

### 32 Bit ASM from 32 Bit Windows COBOL

- **From:** thaneH@softwaresimple.com
- **Date:** 2000-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<88hrh7$pl9$1@nnrp1.deja.com>`

```
I need an assist.  I'm trying to convert a system from 16 to 32 bit
windows.  I have MASM 6.11, and a handful of called assembler
routines.  In need to convert these to 32 bit flat memory model for
Windows.

I have the following directives:

.386
.MODEL flat, c

for calling from Fujitsu COBOL. However if ANYONE with ANY 32 bit COBOL
is calling 32 bit ASM routines, I would like to hear from you.  My
problem is that while I get a clean assemble and link, I get a
protection exception when running.  I think I am missing something in
the addressability of the call parms.

I'm looking for example ASM code and the corresponding COBOL code that
calls the ASM.

One reason I think that I am missing something about parameter
addressability is that when I assemble these with STDCALL, I get
_MODULE@0 for an entry point, but the calling program is trying to call
_MODULE@8


Thanks in advance.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: 32 Bit ASM from 32 Bit Windows COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38acda8f.13194991@news.cox-internet.com>`
- **References:** `<88hrh7$pl9$1@nnrp1.deja.com>`

```
Here is a lot more info and some actual code.

Info:

     - The calling program sets the structure of passed parameters.
       In Realia, this was always ES:DI for 1st parm, DS:SI for 2nd,
       and the remaining passed on the stack.  Since I did not want
       to use the stack (since this has its own compatibility
problems)
       and since I wanted to make all my routines standard, all of
them
       are written with exactly two parameters.

     - Realia supplied the information as to the structure.  If
Fujitsu
       does not, you would have to see the assembler source listing
for
       a compiled program to see how it passes data parms during a
call.
       I would imagine, though, that even if it was not documented,
you
       could ask one of their programmers.  This is important to know
as
       it would relate what the new 'PROC USING' should contain.

     - As to LINK errors, I never really had to worry about them
because
       after the assembly, it created an .OBJ file, which was what was
used
       when I linked the COBOL program (e.g. LINK CBLPGM+ASMSUB).  If
there
       are any link errors during that, then it is probably because
the
       conventions (segment names or addresses) of the subroutine does
not
       match what the calling program is expecting.

     - I read through the manual and it seems as though what you did
was
       correct (the '.model flat, stdcall') in order to make it 32
bit.
       I don't know what else it could be unless it is automatically
       assuming 16 bit because of something in the program.

     - In reading through the manual, it says that referring to the
old
       register names (ES,DI,DS,SI,CS,SS,AX,BX,CX,DX) just causes
reference
       to the lower 16 bits of the 32 bit register.  Although for
address
       registers (ES,DI,DS,SI,CS,SS), it would probably want to
reference
       the entire 32 bits (I am guessing that EDI = expanded 32bit DI
reg).

     - The only other thing I noticed in the manual was OPTION EXPR32
to
       force 32 bit registers.	Maybe if you tried this, it would give
an
       error as to what is causing the (maybe) 16 bit assumption.

     - I am no expert assembler programmer.  I basically got one
program to
       work (with Realia's sample and help) and used it as a template
to
       write all the others.

     - I did have a problem with the routines (in 1990) when I started
writing
       DLL code instead of DOS EXE code (I think it was I had to name
all of
       the segments CODE instead of the program names I was using or
something
       stupid like that) in order for it to be called correctly from
Realia.
       In my experience in dealing with ASM calls, it was always one
little
       thing like that which changed it from non-working to working.

     - I hope some of this is helpful.

-------------
The orig code.  I know how to rewrite these two in COBOL, but these
are just simple test cases, there are some that are much more
complicated.

; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; * Compress a bit pattern into a byte.
*
; *     CALL "KBIT2C"                  USING W-BYTE K-KBIT-WORK.
*
; *		  PARAMETER 1	 1 byte
*
; *		  PARAMETER 2	 8 bytes
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; *    Bit Pattern field:
*
; *        Spaces, low-values, or 'N' is considered off.
*
; *	   Everything else is considered on.
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*

CODE	  SEGMENT PUBLIC
	  ASSUME CS:CODE
	  PUBLIC KBIT2C

KBIT2C	  PROC	 FAR
          MOV    BX,' N'               ;set constants  BH=N
BL=spaces
	  XOR	 DX,DX		       ;clear DL, set  DH=00

KB1:	  LODSW 		       ;get first two bytes of pattern
	  CMP	 AL,BL		       ;test for spaces or null
	  JE	 KB2
	  CMP	 AL,BH
	  JE	 KB2
	  CMP	 AL,DH
	  JE	 KB2
	  OR	 DL,10000000B
KB2:	  CMP	 AH,BL		       ;test for spaces or null
	  JE	 KB3
	  CMP	 AH,BH
	  JE	 KB3
	  CMP	 AH,DH
	  JE	 KB3
	  OR	 DL,01000000B
KB3:	  LODSW 		       ;get next two bytes
	  CMP	 AL,BL
	  JE	 KB4
	  CMP	 AL,BH
	  JE	 KB4
	  CMP	 AL,DH
	  JE	 KB4
	  OR	 DL,00100000B
KB4:	  CMP	 AH,BL
	  JE	 KB5
	  CMP	 AH,BH
	  JE	 KB5
	  CMP	 AH,DH
	  JE	 KB5
	  OR	 DL,00010000B
KB5:	  LODSW 		       ;get next two bytes
	  CMP	 AL,BL
	  JE	 KB6
	  CMP	 AL,BH
	  JE	 KB6
	  CMP	 AL,DH
	  JE	 KB6
	  OR	 DL,00001000B
KB6:	  CMP	 AH,BL
	  JE	 KB7
	  CMP	 AH,BH
	  JE	 KB7
	  CMP	 AH,DH
	  JE	 KB7
	  OR	 DL,00000100B
KB7:	  LODSW 		       ;get next two bytes
	  CMP	 AL,BL
	  JE	 KB8
	  CMP	 AL,BH
	  JE	 KB8
	  CMP	 AL,DH
	  JE	 KB8
	  OR	 DL,00000010B
KB8:	  CMP	 AH,BL
	  JE	 KRET
	  CMP	 AH,BH
	  JE	 KRET
	  CMP	 AH,DH
	  JE	 KRET
	  OR	 DL,00000001B

KRET:	  MOV	 ES:[DI],DL	       ;return formatted byte
	  RET
KBIT2C	  ENDP

CODE	  ENDS
	  END

------------
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; * Return the bit Pattern of a byte.
*
; *     CALL "KBIT2E"                  USING K-KBIT-WORK W-BYTE.
*
; *		  PARAMETER 1	 Eight bytes that will have either
*
; *                              a 'Y' or 'N' in them depending
*
; *				 on the value of Parameter 2.
*
; *		  PARAMETER 2	 Any one byte field.
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; *    01  K-KBIT-WORK		       PIC X(8).
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*

CODE	  SEGMENT PUBLIC
	  ASSUME CS:CODE
	  PUBLIC KBIT2E

KBIT2E	  PROC	 FAR
          MOV    AX,'NN'               ;clear pattern to all 'N'
	  MOV	 CX,4
	  REP	 STOSW		       ;DI now at end of pattern
          MOV    DH,'Y'                ;set DH to 'Y'
	  MOV	 AL,DS:[SI]	       ;move bit to test to al
	  CMP	 AL,0		       ;end if no values are on
	  JE	 KRET

KB8:	  TEST	 AL,001H
	  JZ	 KB7
	  MOV	 ES:[DI-1],DH
KB7:	  TEST	 AL,002H
	  JZ	 KB6
	  MOV	 ES:[DI-2],DH
KB6:	  TEST	 AL,004H
	  JZ	 KB5
	  MOV	 ES:[DI-3],DH
KB5:	  TEST	 AL,008H
	  JZ	 KB4
	  MOV	 ES:[DI-4],DH
KB4:	  TEST	 AL,010H
	  JZ	 KB3
	  MOV	 ES:[DI-5],DH
KB3:	  TEST	 AL,020H
	  JZ	 KB2
	  MOV	 ES:[DI-6],DH
KB2:	  TEST	 AL,040H
	  JZ	 KB1
	  MOV	 ES:[DI-7],DH
KB1:	  TEST	 AL,080H
	  JZ	 KRET
	  MOV	 ES:[DI-8],DH

KRET:	  RET
KBIT2E	  ENDP

CODE	  ENDS
	  END
------------

Now, here is my attempt.  Note, this DOES link and the entry point
shows the right number of bytes of call parms.  But I think I am doing
something fundamentally wrong.

; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; * Return the bit Pattern of a byte.
*
; *     CALL "KBIT2E"                  USING K-KBIT-WORK W-BYTE.
*
; *		  PARAMETER 1	 Eight bytes that will have either
*
; *                              a 'Y' or 'N' in them depending
*
; *				 on the value of Parameter 2.
*
; *		  PARAMETER 2	 Any one byte field.
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; *    01  K-KBIT-WORK		       PIC X(8).
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
.386                          ;tah
.MODEL flat, stdcall          ;tah

CODE	  SEGMENT PUBLIC
	  ASSUME CS:CODE
	  PUBLIC KBIT2E

PBYTE     TYPEDEF PTR BYTE      ;tah

KBIT2E    PROC   USES esi edi,  ;tah
          KBITWRK:PBYTE,        ;tah
          WBYTE:PBYTE           ;tah
          MOV    eSI,KBITWRK    ;tah
          MOV    edi,WBYTE      ;tah
          MOV    AX,'NN'               ;clear pattern to all 'N'
	  MOV	 CX,4
	  REP	 STOSW		       ;DI now at end of pattern
          MOV    DH,'Y'                ;set DH to 'Y'
          MOV    AL,DS:[eSI]            ;move bit to test to al
	  CMP	 AL,0		       ;end if no values are on
	  JE	 KRET

KB8:	  TEST	 AL,001H
	  JZ	 KB7
          MOV    ES:[eDI-1],DH
KB7:	  TEST	 AL,002H
	  JZ	 KB6
          MOV    ES:[eDI-2],DH
KB6:	  TEST	 AL,004H
	  JZ	 KB5
          MOV    ES:[eDI-3],DH
KB5:	  TEST	 AL,008H
	  JZ	 KB4
          MOV    ES:[eDI-4],DH
KB4:	  TEST	 AL,010H
	  JZ	 KB3
          MOV    ES:[eDI-5],DH
KB3:	  TEST	 AL,020H
	  JZ	 KB2
          MOV    ES:[eDI-6],DH
KB2:	  TEST	 AL,040H
	  JZ	 KB1
          MOV    ES:[eDI-7],DH
KB1:	  TEST	 AL,080H
	  JZ	 KRET
          MOV    ES:[eDI-8],DH

KRET:	  RET
KBIT2E	  ENDP

CODE	  ENDS
	  END

-----------------

I am calling using

    CALL "KBIT2E" with stdcall  USING W-OUTPUT W-FIELD1.

000150 01  W-MISC.
000160	   05  W-FIELD1 		   PIC X(2).
000170	   05  W-OUTPUT 		   PIC X(16).

When I run I get an invalid page fault.  Help!
```

##### ↳ ↳ Re: 32 Bit ASM from 32 Bit Windows COBOL

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.lang.asm
- **Message-ID:** `<2cm8bs89025f7734jnhnnbqocm3qpnt7p9@4ax.com>`
- **References:** `<88hrh7$pl9$1@nnrp1.deja.com> <38acda8f.13194991@news.cox-internet.com>`

```
anyone know a quick html link to an explanation of proc using?

thaneH@softwaresimple.com (Thane Hubbell) wrote:
>Here is a lot more info and some actual code.
>
…[21 more quoted lines elided]…
>       it would relate what the new 'PROC USING' should contain.

reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: 32 Bit ASM from 32 Bit Windows COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38b611f6.184711302@news.cox-internet.com>`
- **References:** `<88hrh7$pl9$1@nnrp1.deja.com>`

```
This was kind of a tedious journey - but I made it.

My thanks to Kevin Hansen, and Bob Wolfe, both of whom lent me
valuable insight into how to solve this - and my thanks too, to Tim
Robbins of the microsoft.public.masm news group (I thanked him there
already) for his help.

Here is a completed version of the example I posted earlier.

If anyone wants to call 32 bit ASM code from Fujitsu COBOL (This
should work with Realia too), please let me know.  I know the secret
code now.  Please please don't tell anyone I can do some PC assembler.
Not that I don't like it mind you - it's interesting, but not
something I want to do full time.  It would be like admitting that I
can code in RPG <G>.

BTW - the thing that finally pushed me over the hump was when Tim
explained what my attempt looked like in C - I had one too many levels
of indirection.  

; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; * Return the bit Pattern of a byte.
*
; *     CALL "KBIT2E"                  USING K-KBIT-WORK W-BYTE.
*
; *		  PARAMETER 1	 Eight bytes that will have either
*
; *                              a 'Y' or 'N' in them depending
*
; *				 on the value of Parameter 2.
*
; *		  PARAMETER 2	 Any one byte field.
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*
; *    01  K-KBIT-WORK		       PIC X(8).
*
; * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*

.386

_TEXT     SEGMENT PUBLIC PARA USE32 'CODE'
PUBLIC    _KBIT2E
;
;  Stack Frame for _KBIT2E
;
PARMDATA  STRUCT
 EBP_SAVE DD	 ?		       ;Saved EBP
 EDI_SAVE DD	 ?		       ;Saved EDI
 ESI_SAVE DD	 ?		       ;Saved ESI
 EBX_SAVE DD	 ?		       ;Saved EBX
 RA	  DD	 ?		       ;Return Address
 PARM1	  DD	 ?		       ;Address of PARAMETER-1
 PARM2	  DD	 ?		       ;Address of PARAMETER-2
PARMDATA  ENDS

_KBIT2E   PROC NEAR
	  PUSH	 EBX		       ;Preserve EBX register
	  PUSH	 ESI		       ;Preserve ESI register
	  PUSH	 EDI		       ;Preserve EDI register
	  PUSH	 EBP		       ;Preserve EBP
	  MOV	 EBP,ESP	       ;Point ESP to new stack frame

	  ASSUME EBP:PTR PARMDATA
;
;    Load parameter 1 (address) into EDI
;
           MOV    EDI,[EBP].PARM1

;
;    Load Parameter 2 (address) into ESI
;
           MOV    ESI,[EBP].PARM2

          MOV    EAX,'NN'              ;clear pattern to all 'N'
          MOV    ECX,4
	  REP	 STOSW		       ;DI now at end of pattern
          MOV    DH,'Y'                ;set DH to 'Y'
          MOV    AL,[ESI]              ;move bit to test to al
	  CMP	 AL,0		       ;end if no values are on
	  JE	 KRET

KB8:	  TEST	 AL,001H
	  JZ	 KB7
          MOV    [EDI-1],DH
KB7:	  TEST	 AL,002H
	  JZ	 KB6
          MOV    [EDI-2],DH
KB6:	  TEST	 AL,004H
	  JZ	 KB5
          MOV    [EDI-3],DH
KB5:	  TEST	 AL,008H
	  JZ	 KB4
          MOV    [EDI-4],DH
KB4:	  TEST	 AL,010H
	  JZ	 KB3
          MOV    [EDI-5],DH
KB3:	  TEST	 AL,020H
	  JZ	 KB2
          MOV    [EDI-6],DH
KB2:	  TEST	 AL,040H
	  JZ	 KB1
          MOV    [EDI-7],DH
KB1:	  TEST	 AL,080H
	  JZ	 KRET
          MOV    [EDI-8],DH

KRET:     
;
;    Return to COBOL, restoring preserved registers
;
	  MOV	 ESP,EBP	       ;Remove stack frame for
previous call

	  POP	 EBP		       ;Restore registers
	  POP	 EDI		       ;
	  POP	 ESI		       ;
	  POP	 EBX		       ;
	  RET			       ;And return

_KBIT2E   ENDP
_TEXT	  ENDS
	  END
```

##### ↳ ↳ Re: 32 Bit ASM from 32 Bit Windows COBOL

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tafcbss4kdi0mpc7ihi4coho9kere2ek03@4ax.com>`
- **References:** `<88hrh7$pl9$1@nnrp1.deja.com> <38b611f6.184711302@news.cox-internet.com>`

```
thaneH@softwaresimple.com (Thane Hubbell) wrote:

>BTW - the thing that finally pushed me over the hump was when Tim
>explained what my attempt looked like in C - I had one too many levels
>of indirection.  

umm, that was me. or at least i think it was.


reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

###### ↳ ↳ ↳ Re: 32 Bit ASM from 32 Bit Windows COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38b69c83.220186334@news.cox-internet.com>`
- **References:** `<88hrh7$pl9$1@nnrp1.deja.com> <38b611f6.184711302@news.cox-internet.com> <tafcbss4kdi0mpc7ihi4coho9kere2ek03@4ax.com>`

```
On Fri, 25 Feb 2000 03:32:42 -0500, G Moore
<gvwmoore@spam.ix.netcom.com> wrote:

>thaneH@softwaresimple.com (Thane Hubbell) wrote:
>
…[6 more quoted lines elided]…
>

I knew you mightthink that.  I should have explained further.  Tim
showed me what the call to my ASM would look like from C, and it was
obvious I had 2 levels of indirection instead of 1.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
