[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# C program call from COBOL

_11 messages · 8 participants · 1998-10_

---

### C program call from COBOL

- **From:** "Gerhard Bouma" <pmi@nl.aegon.nl>
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vva63$fst$1@newnews.nl.uu.net>`

```
Hi,

I have made a C program which calls a DLL (all on MVS), but now I want to
call this main C-program from a COBOL program. Everything goes well, except
the passing of parameters to the C-program.
Does anyone have some tips?

Gerhard
```

#### ↳ Re: C program call from COBOL

- **From:** Stuart Gaunt <stuartg@sequent.com>
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36233F32.5A841378@sequent.com>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net>`

```
I believe that COBOL passes all its parameters by reference, so your 'by
value' parameters will appear as addresses, not exactly what you want.

I've tried this on UNIX, and it works OK.  If you need a code fragment,
I should be able to dig one out.

Regards

Stuart
```

##### ↳ ↳ Re: C program call from COBOL

- **From:** aflinsch@njeb.att.com (Alex Flinsch)
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vvfuo$n0q@newsb.netnews.att.com>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net> <36233F32.5A841378@sequent.com>`

```
In article <36233F32.5A841378@sequent.com>, stuartg@sequent.com wrote:
>I believe that COBOL passes all its parameters by reference, so your 'by
>value' parameters will appear as addresses, not exactly what you want.
>

Unless you have coded your C proggie to accept a pointer to your 
parameters.
```

###### ↳ ↳ ↳ Re: C program call from COBOL

- **From:** bgwillia@vcu.edu (Boyce G. Williams, Jr.)
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36235107.3991841@usenet.acw.vcu.edu>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net> <36233F32.5A841378@sequent.com> <6vvfuo$n0q@newsb.netnews.att.com>`

```
aflinsch@njeb.att.com (Alex Flinsch) wrote:

>In article <36233F32.5A841378@sequent.com>, stuartg@sequent.com wrote:
>>I believe that COBOL passes all its parameters by reference, so your 'by
…[4 more quoted lines elided]…
>parameters.

I wrote a reply to a simular question regarding passing data between C
and COBOL programs.  Here it is from Deja News:

I'm not sure what platform you wish to perform this feat, so I'm
assuming you're doing this on a mainframe (MVS).  Linking
multi-language object files together can be done provided the venders
allowed means to this end via linkage cross-referencing (That's why
AFAIK Pascal can't be used as a subprogram to a COBOL call- one can't
pass data to it because one can't resolve cross-referencing issues).
I've written FORTRAN subprograms called from COBOL on MVS.

Examples used here are from James G. Janossy book: 'Advanced MVS JCL.'

The COBOL program fields to pass to C must be as follows:

C          COBOL             Size      Alignment
-----      ---------         -------   ---------
char       PIC X             1 byte    byte
signed int PIC S9(9) COMP    4 bytes   fullword
double     COMP-2            8 bytes   doubleword
struct     group item entry
array      OCCURS clause

BTW- C cannot directly handle packed decimal (COMP-3) type COBOL
fields.

COBOL uses the following to perform the call:

01  WS-VALUES.
    05  VALUE-1 PIC S9(09) COMP.
    05  VALUE-2 PIC S9(09) COMP.

PROCEDURE DIVISION.
000-CALL.
    CALL 'CSUB' USING WS-VALUES.

C uses the following to receive the call:

#pragma linkage( csub, COBOL )

struct bucket
{
    int int1;
    int int2;
};
void csub( struct bucket *parm )
{
  (*parm ).int2 = ( *parm ).int1 + 1;
}

One then compile the two programs seperately:

//STEP1 EXEC EDCCL,
//  CPARM='SOURCE,XREF',
//  INFILE='USER.SOURCE.LIB(CSUB'
//  OUTFILE='USER.LOAD.LIB(CSUB),DISP=SHR'
//STEP2 EXEC IGYWCL
//COBOL.SYSIN DD DSN=USER.SOURCE.LIB(COBMAIN),DISP=SHR
//LKED.SYSLMOD DD DSN=USER.LOAD.LIB(COBMAIN),DISP=SHR

The remainder of the programs and JCL are left as an excersize.

This will create (assuming compiler options are defaulted correct)
dynamically linked calls between the COBOL main and C subprogram.

I haven't done calls between COBOL and C, just between COBOL and
FORTRAN.  But the process is reasonable.

As always, just my two cents worth adjusted for inflation,

Boyce G. Williams, Jr.

 .--------------------------------------------------------------------.
 | "People should have two virtues:  purpose- the courage to envisage |
 | and pursue valued goals uninhibited by the defeat of infantile     |
 | fantasies, by guilt and the failing fear punishment;  and wisdom- a|
 | detached concern with life itself, in the face of death itself."   |
 |                                                     Norman F. Dixon|
 '--------------------------------------------------------------------'
```

###### ↳ ↳ ↳ Re: C program call from COBOL

_(reply depth: 4)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36242006.2EC9@swbell.net>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net> <36233F32.5A841378@sequent.com> <6vvfuo$n0q@newsb.netnews.att.com> <36235107.3991841@usenet.acw.vcu.edu>`

```
Boyce G. Williams, Jr. wrote, amid snippage:
> 
> aflinsch@njeb.att.com (Alex Flinsch) wrote:
…[4 more quoted lines elided]…
> >>

Depending on the dialect you may be able to pass a parameter "BY
VALUE," possibly with some restrictions on the size or type of
parameter so passed.  The C program receives the value rather than
a pointer to a value.  I've done this with MicroFocus under Unix; I
haven't tried it under MVS.

> I'm not sure what platform you wish to perform this feat, 

The original post specified MVS.

> so I'm
> assuming you're doing this on a mainframe (MVS).  Linking
…[4 more quoted lines elided]…
> I've written FORTRAN subprograms called from COBOL on MVS.

[snip -- examples from Janossy's book]

> BTW- C cannot directly handle packed decimal (COMP-3) type COBOL
> fields.

Standard C can't, at least not without a lot of bothersome bit
twiddling.  However, through an IBM extension, C for MVS can handle
packed decimal as a native datatype.

> COBOL uses the following to perform the call:
> 
…[10 more quoted lines elided]…
> #pragma linkage( csub, COBOL )

Note for the unwary: this pragma, like all pragmas in C, is
inherently compiler-specific.  Its presence here hints that COBOL
and C don't really get along very well under MVS without special 
tweaks from the compiler.

I don't know if this pragma is still necessary in the LE environment.

> struct bucket
> {
>     int int1;
>     int int2;
> };

Note that the C Standard permits the compiler to insert padding
bytes between structure members in order to maintain byte alignment.
Your options are:

   1. Pass elementary items rather than group items.  It's safest
      for the elementary items to be 01-levels; otherwise, depending
      on the platform, the byte alignment may not work right for
      the C program.

   2. Pass a group item which the C program expresses not as a
      struct but as an array of char, from which it plucks the
      members according to specified byte offsets.

   3. Pass a group item expressed by the C program as a struct;
      carefully make sure the byte alignment is correct for your
      environment and (where applicable) the set of compiler 
      options in use; remember to check again if you ever port to
      another environment or to another release of the C compiler.

[snip -- more sample code and JCL]

> I haven't done calls between COBOL and C, just between COBOL and
> FORTRAN.  But the process is reasonable.

I haven't done calls between COBOL and C under MVS, so I can't give
you the details for this platform, but I can suggest what to worry 
about:

1. COBOL passes parameters by reference, while C passes them by 
value.  Arrays are a special case which I won't go into here, but
any competent C programmer will know what I mean.

2. Compatible definitions of datatypes.

3. Byte alignment, especially in group items as noted above.

4. The order in which parameters are passed.  Due to differences in
calling conventions, in some environments you may have to reverse
the order.

5. How to handle a value which is returned by a C program.  MicroFocus
provides syntax for COBOL to receive the return value; I don't know
about MVS.

6. By convention, C usually uses nul-terminated character strings,
whereas COBOL defines fixed length fields and pads with blanks.

7. Possible interference between signal handlers in the C code and
whatever the COBOL runtime system does with exceptional conditions.


The ways to resolve these issues are highly platform-specific, so read
the manuals carefully.  Very likely, either your COBOL or your C will
have to be written differently in order to accommodate the quirks of
the other language.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: C program call from COBOL

_(reply depth: 5)_

- **From:** "Michael C. Kasten" <mck9@swbell.net>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36249800.3EBB@swbell.net>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net> <36233F32.5A841378@sequent.com> <6vvfuo$n0q@newsb.netnews.att.com> <36235107.3991841@usenet.acw.vcu.edu> <36242006.2EC9@swbell.net>`

```
Michael C. Kasten wrote:

[much snippage -- in particular, my list of things to consider when
 calling C modules from COBOL]

I just remembered another one, specific to the MVS environment:

8. In COBOL, the names of programs and entry points (other than
nested programs) must be no longer than eight characters.  Object
modules in normal libraries use eight-digit names for external
references.  However, names of functions and globals in C may be longer.
As a result, unless you confine your C external references to short 
names, you have to store your C object modules in a special funky 
library format which mangles the names to make them fit.

Michael C. Kasten	mck9@swbell.net
http://home.swbell.net/mck9/cobol/cobol.html
```

###### ↳ ↳ ↳ Re: C program call from COBOL

_(reply depth: 6)_

- **From:** "Gerhard Bouma" <pmi@nl.aegon.nl>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7026uh$r8v$1@newnews.nl.uu.net>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net> <36233F32.5A841378@sequent.com> <6vvfuo$n0q@newsb.netnews.att.com> <36235107.3991841@usenet.acw.vcu.edu> <36242006.2EC9@swbell.net> <36249800.3EBB@swbell.net>`

```
[snippage
>In COBOL, the names of programs and entry points (other than
>nested programs) must be no longer than eight characters.  Object
…[4 more quoted lines elided]…
>library format which mangles the names to make them fit.


Well yes, but to be complete, I use a development tool (Natstar by Nat
Systems) on my client to build (windows) applications, which generates C
coding. Also I can generate C for MVS and FTP it to the host to compile
there. So now I can build a function to be called on any platform. It also
takes care of the long names for me, so I can still just use them.

The final coding (for my experiment) now looks like this (sorry for some
dutch words):
COBOL:

WORKING-STORAGE SECTION.

01  PRPI                 PIC  9(2),9(7).
01  AANTAL-TERM          PIC  9(3).

01  WS-VALUES.
    05  VALUE-1          PIC S9(9)          VALUE ZERO.
    05  VALUE-2                     COMP-2  VALUE ZERO.

PROCEDURE DIVISION.
000-CALL.
    ACCEPT AANTAL-TERM.
    MOVE AANTAL-TERM TO VALUE-1.
    CALL "NSBMAIN" USING WS-VALUES.
    MOVE VALUE-2 TO PRPI.
    DISPLAY "AANTAL-TERM: " VALUE-1.
    DISPLAY "PI         : " PRPI.
    GOBACK.

If I don't want to use the #pragma pack in my following C, then I have to
use:
01  WS-VALUES SYNC.
in the COBOL source.

In C:  (NSBMAIN)

#pragma linkage( csub, COBOL )
#pragma pack(1)
#include "nslib.h"
#include "nsthform.h"
#include "nsthings.h"

_Packed struct bucket
{                                                      
    signed int   aant_term;                            
    double       pi;                                   
};                                                     
                                                       
void csub( struct bucket *parm )                       
{                                                      
    printf("NS-IN : %d\n",(*parm).aant_term);          
                                                       
    I_BEREKEN_PI ( (*parm).aant_term, &(*parm).pi);    
                                                       
    printf("NS-IN : %d\n",(*parm).aant_term);          
    printf("NS-UIT: %f\n",(*parm).pi);                 
}                                                      
                                         
This then calculates Pi. Notice the long instruction name! Of course I now have to make things more generic. 
My next problem (little project or maybe even opportunity) is that we also use CSP 4.1. (it generates COBOL to be compiled) CSP doesn't allow for very much data-types and alignment. The #pragma pack comes in handy, but as of now I don't see a way to pass double's. 

Thank you all for your reactions, I didn't expect this many.
Gerhard.
```

###### ↳ ↳ ↳ Re: C program call from COBOL

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<702snv$g@dfw-ixnews3.ix.netcom.com>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net> <36233F32.5A841378@sequent.com> <6vvfuo$n0q@newsb.netnews.att.com> <36235107.3991841@usenet.acw.vcu.edu> <36242006.2EC9@swbell.net> <36249800.3EBB@swbell.net>`

```

Michael C. Kasten wrote in message <36249800.3EBB@swbell.net>...
>Michael C. Kasten wrote:
>
…[14 more quoted lines elided]…
>http://home.swbell.net/mck9/cobol/cobol.html

This (limitation on COBOL program/entry-point names) is no longer true under
MVS (or Windows or AIX or OS/2) - check out the PGMNAME compiler option in
IBM COBOL for OS/390 & VM (or COBOL for MVS & VM).
```

###### ↳ ↳ ↳ Re: C program call from COBOL

_(reply depth: 5)_

- **From:** "Gerhard Bouma" <pmi@nl.aegon.nl>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<701jpq$86s$1@newnews.nl.uu.net>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net> <36233F32.5A841378@sequent.com> <6vvfuo$n0q@newsb.netnews.att.com> <36235107.3991841@usenet.acw.vcu.edu> <36242006.2EC9@swbell.net>`

```
I did what Boyce suggested, and it seems to work fine. However, I think I am
indeed experiencing byte alignment problems, since after my COMP-2
everything goes wrong. But I've now found a web page. For the interested:
http://boris.mfltd.co.uk/docs/infofax/0631.html
Gerhard.
```

#### ↳ Re: C program call from COBOL

- **From:** pduboisREMOVETHIS@enteract.com (PAL3000)
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3623683f.1971202@news.enteract.com>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net>`

```
If your using Microfocus, they have some excelent info and examples on
their web page.

Paul

On Tue, 13 Oct 1998 12:32:23 +0200, "Gerhard Bouma" <pmi@nl.aegon.nl>
wrote:

>Hi,
>
…[6 more quoted lines elided]…
>

--------------------------------------
To reply by email, please take out the
words REMOVETHIS from my email address
```

#### ↳ Re: C program call from COBOL

- **From:** Roland.Schiradin@t-online.de (Roland Schiradin)
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6vvv35$j2e$1@news00.btx.dtag.de>`
- **References:** `<6vva63$fst$1@newnews.nl.uu.net>`

```
Gerhard Bouma schrieb in Nachricht <6vva63$fst$1@newnews.nl.uu.net>...

use #pragma-option or

LINKAGE SECTION.
01 P1 PIC S9(9) USAGE IS BINARY
01 P2 PIC S9(9) USAGE IS BINARY
CALL 'CFUNC' USING BY VALUE P1
     RETURNING P2.

int CFUNC(int
{ 
  int p2;          
  p2=p1;           
  return p2;       
}                       
    
RTFM OS/390 V2R4.0 LANG ENV WRITING ILC APPLICATION 


Roland
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
