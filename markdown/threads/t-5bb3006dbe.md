[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Unresolved external symbal error in fujitsu cobol.

_23 messages · 10 participants · 2003-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Unresolved external symbal error in fujitsu cobol.

- **From:** manga <member43127@dbforums.com>
- **Date:** 2003-11-04T19:08:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3560214.1067990880@dbforums.com>`

```

I am calling one program from another using call stmt.



Calling program

___________________



WORKING-STORAGE SECTION.

 01  BUF         PIC S9(9) BINARY VALUE 99.

 01  RESULT      PIC S9(9) BINARY VALUE -99.

 PROCEDURE DIVISION.

 START-IT.

     CALL 'SUB-MAIN-ENTRY' USING BUF.

     DISPLAY "RESULT".

     CALL 'SECOND-ENTRY'.

 END PROGRAM RETURN-CODE-TEST.



Called Program

_____________



LINKAGE SECTION.

 01  BUF PIC S9(9).

 PROCEDURE DIVISION USING BUF.

 PARA-01.

     ADD 1 TO BUF GIVING RETURN-CODE.

     EXIT PROGRAM.

 PARA-02.

     ENTRY "SECOND-ENTRY".

     MOVE -5000 TO RETURN-CODE.



it is compiling fine..but when I am linking, I am getting error as



obj : error LNK2001: unresolved external symbol _SECOND-ENTRY

OBJ: error  LNK2001: unresolved external symbol _SUB-MAIN-ENTRY

.\.exe : fatal error LNK1120: 2 unresolved externals

NMAKE : fatal error U1077: '...PCOBOL32\LINK' : return code '0x19'

Stop.



Linking files failed.

Please close the window.



*********************************************



I used Main and NOALPHAL as the compiler options.



Is there anything I have to do , to make this work?

Can anyone help please?



-manga
```

#### ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-04T20:06:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xaidnf3_uf6IxjWiU-KYuA@giganews.com>`
- **References:** `<3560214.1067990880@dbforums.com>`

```
manga wrote:
> I am calling one program from another using call stmt.
>
…[86 more quoted lines elided]…
> Can anyone help please?

With the information provided here, I don't see enough to help on the
linkage question. Note that "BUF" is defined differently in the calling and
called programs. This will cause all manner of unfortunate results. In the
calling program, BUF is 4 bytes long; in the called program, BUF is 7 bytes
long.
```

#### ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** manga <member43127@dbforums.com>
- **Date:** 2003-11-05T13:59:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3563730.1068058752@dbforums.com>`
- **References:** `<3560214.1067990880@dbforums.com>`

```

OK...let me simplify the code..I have changed the code and copied
below...and again I am getting the same linking error..it says it cannot
find the sub program...Can u please help? I am using fujistsu cobol V3.



CALLING PROG:(RT1.COB)

-------------------



 IDENTIFICATION DIVISION.

 PROGRAM-ID. RETURN-CODE-TEST.

 DATA DIVISION.

 WORKING-STORAGE SECTION.

 01  BUF         PIC S9(9) VALUE 99.

 01  RESULT      PIC S9(9) VALUE -99.

 PROCEDURE DIVISION.

 START-IT.

     CALL 'SUB-MAIN-ENTRY' USING BUF.

     DISPLAY "RESULT".

 END PROGRAM RETURN-CODE-TEST.

********************************************************



CALLED PROGRAM :(SM1.COB)

---------------------



 IDENTIFICATION DIVISION.

 PROGRAM-ID. SUB-MAIN-ENTRY.

 DATA DIVISION.

 LINKAGE SECTION.

 01  BUF PIC 99.

 PROCEDURE DIVISION USING BUF.

 PARA-01.

     ADD 1 TO BUF.

     DISPLAY BUF.

     EXIT PROGRAM.
```

##### ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** Donald Tees <Donald_Tees@sympatico.ca>
- **Date:** 2003-11-05T16:22:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3Zdqb.7469$fg4.274907@news20.bellglobal.com>`
- **In-Reply-To:** `<3563730.1068058752@dbforums.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com>`

```
manga wrote:
> OK...let me simplify the code..I have changed the code and copied
> below...and again I am getting the same linking error..it says it cannot
…[64 more quoted lines elided]…
> Posted via http://dbforums.com

Either stick to 8 character names and make the file name the same, or 
place the program id in quotes.

Donald


Donald
```

##### ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-05T16:34:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311051634.7b40c9a2@posting.google.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com>`

```
manga <member43127@dbforums.com> wrote 

> OK...let me simplify the code..I have changed the code and copied
> below...and again I am getting the same linking error..it says it cannot
…[27 more quoted lines elided]…
>      EXIT PROGRAM.

When passing parameters from one program to another they must be
defined exactly the same.  PIC S9(9) is 9 bytes long and PIC 99 is two
bytes long.  Adding 1 in the subroutine will change  000000099  to 
010000099.

You seem to want to have some sort of 'return'. FJ3 does not support
returning a value to the CALL. By default, parameters are passed by
reference you can change the contents as you are doing.

As to the failed linker, you probably need to read the manual a bit
closer.  You need to compile SM1 without a MAIN and then add SM1.LIB
to the link of RT1.  RT1 must be compiled with compiler option MAIN.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-11-06T19:24:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UeKdnSjCG-WiaTeiU-KYiA@giganews.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com>`

```
Richard wrote:
>
> You seem to want to have some sort of 'return'. FJ3 does not support
> returning a value to the CALL. By default, parameters are passed by
> reference you can change the contents as you are doing.

Yes it does, although not by the RETURNING clause. You may set whatever
numeric value you want in the special register RETURN-CODE in the called
program. The calling program can then test RETURN-CODE (be careful you don't
do anything to screw with RETURN-CODE - such as another subroutine call -
between regaining control from the subprogram and the test).
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-11-07T21:35:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<acsjeKCdABr$EwP3@ld50macca.demon.co.uk>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com>`

```
In message <217e491a.0311051634.7b40c9a2@posting.google.com>, Richard 
<riplin@Azonic.co.nz> writes
>When passing parameters from one program to another they must be
>defined exactly the same.

As an adjunct to this, Richard/anyone, as a general principle does a 
program calling several programs using the same parameters need those 
parameters to be specified in the same sequence for each called program? 
I suspect IBM does not and I know that Fujitsu does.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-11-07T14:31:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<boh6gt$e68$1@si05.rsvl.unisys.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk>`

```
Alistair MacLean queried:

<< ... as a general principle does a program calling several programs using
the same parameters need those parameters to be specified in the same
sequence for each called program?  I suspect IBM does not and I know that
Fujitsu does.>>

Yes, I think they do.

ANSI X3.23-1985, page X-29, 5.2.4, CALL statement, General Rule 10:

"The sequence of appearance of the data-names of the USING phrase of the
CALL statement and in the corresponding USING phrase in the called program's
Procedure Division header determines the correspondence between the
data-names used by the calling and called programs.  This correspondence is
positional and not by name equivalence; the first data-name in one USING
phrase corresponds to the first data-name in the other, the second to the
second, etc."

In standard COBOL, then, if Program A calls programs B, C and D, using the
parameters X, Y and Z,  X corresponds to the first parameter, Y to the
second, Z to the third, in each of the three programs B, C and D.  It
doesn't matter what B, C or D calls those parameters.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 5)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-11-08T07:41:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0311080741.40f34aa8@posting.google.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <boh6gt$e68$1@si05.rsvl.unisys.com>`

```
Chuck - 

With some compilers I have used the order of the items listed in the
LINKAGE SECTION mattered as well.  With others - it does not.


"Chuck Stevens" <charles.stevens@unisys.com> wrote in message news:<boh6gt$e68$1@si05.rsvl.unisys.com>...
> Alistair MacLean queried:
> 
…[22 more quoted lines elided]…
>     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 6)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-11-08T22:03:31+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nuiqqvcppfdjd8ok1bs15va0aemalde8pv@4ax.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <boh6gt$e68$1@si05.rsvl.unisys.com> <bfdfc3e8.0311080741.40f34aa8@posting.google.com>`

```
On 8 Nov 2003 07:41:46 -0800 thaneh@softwaresimple.com (Thane Hubbell) wrote:

:>With some compilers I have used the order of the items listed in the
:>LINKAGE SECTION mattered as well.  With others - it does not.

Which ones operated differently based on the LINKAGE SECTION order?

Sounds like they didn't do COBOL.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-08T23:26:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6Zerb.2963$nz.686@newsread2.news.pas.earthlink.net>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <boh6gt$e68$1@si05.rsvl.unisys.com> <bfdfc3e8.0311080741.40f34aa8@posting.google.com>`

```
Thane,
  If so, they were NOT conforming to any ANSI/ISO COBOL Standard that I know
of.  The order of parameters in the USING phrases of CALL / Procedure
Division is *supposed* to be the only thing that impacts "matching".

P.S.  I have never run into one that didn't work this way - but that doesn't
mean that there has never been one.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-11-09T13:52:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7J277kB2akr$EwaO@ld50macca.demon.co.uk>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <boh6gt$e68$1@si05.rsvl.unisys.com>`

```
Chuck, the quote applies to the relationship between the calling and 
called programs. My question relates to three called programs within one 
parent program, utilising a different sequence of the same parameters 
for each called program.

I suspect the situation I have experienced constitutes a 'feature' of 
Fujitsu Cobol.

In message <boh6gt$e68$1@si05.rsvl.unisys.com>, Chuck Stevens 
<charles.stevens@unisys.com> writes
>Alistair MacLean queried:
>
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-07T18:33:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311071833.2f2d76be@posting.google.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk>`

```
Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote

> As an adjunct to this, Richard/anyone, as a general principle does a 
> program calling several programs using the same parameters need those 
> parameters to be specified in the same sequence for each called program? 

No.  The sequence of parameters required is determined by the called
program alone and is determined for each called program individually.

In the called program it is the 'PROCEDURE DIVISION USING ..' (or
'ENTRY USING') that specifies the order that the CALL parameters are
to be in.  There is nothing that can enforce writing one PD USING
clause to match some other program's PD USING, except arbitrary
standards and some sensible consideration of uniformity.

> I suspect IBM does not and I know that Fujitsu does.

In what way does Fujitsu 'need' the parameter sequence to be the same
for calling different programs ?

There is nothing to prevent having:

           CALL "prog1" USING A B
           CALL "prog2" USING B A

as long as these are the required order for those programs.

In fact if A and B have the same definition one may say:

            CALL "prog3" USING A B
            CALL "prog3" USING B A

depending on what prog3 may be doing with those parameters.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-11-09T13:49:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<z575nPBBYkr$EwY0@ld50macca.demon.co.uk>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com>`

```
In message <217e491a.0311071833.2f2d76be@posting.google.com>, Richard 
<riplin@Azonic.co.nz> writes
>In what way does Fujitsu 'need' the parameter sequence to be the same
>for calling different programs ?
…[13 more quoted lines elided]…
>depending on what prog3 may be doing with those parameters.

I recently wrote a Fujitsu Cobol program which called in sequence three 
other programs passing the same parameters to each program. 
Unfortunately, I did not use the same sequence of parameters for calling 
the second and third programs as was used to call the first program. 
Although the sequences for the CALLs matched the LINKAGE SECTION in the 
called programs perfectly, the program kept abending. Only after 
changing the three calls to use the same sequence of parameters did the 
program function correctly.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-11T10:24:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fb0020d_5@news.athenanews.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com> <z575nPBBYkr$EwY0@ld50macca.demon.co.uk>`

```

"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
news:z575nPBBYkr$EwY0@ld50macca.demon.co.uk...
> In message <217e491a.0311071833.2f2d76be@posting.google.com>, Richard
> <riplin@Azonic.co.nz> writes
…[25 more quoted lines elided]…
>
Gleep!

Code sample please, Alistair.

I can't believe this. There has to be a discrepancy between the Linkage and
Procedure Division headers, in terms of the parameter definitions.

To my knowledge, this is NOT a requirement of Fujitsu COBOL. The fact that
it worked when you changed it would be purely coincidental.

Really need to see the code...

Pete.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-11-11T12:50:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QAPhpSAMsNs$Ew2v@ld50macca.demon.co.uk>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com> <z575nPBBYkr$EwY0@ld50macca.demon.co.uk> <3fb0020d_5@news.athenanews.com>`

```
Typical bloody project manager! Wants to see the code AFTER it's been 
corrected. Sorry can not supply code. Hence my original question.

In message <3fb0020d_5@news.athenanews.com>, Peter E.C. Dashwood 
<dashwood@enternet.co.nz> writes
>
>"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
…[43 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-11-12T11:39:30+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fb16536_5@news.athenanews.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com> <z575nPBBYkr$EwY0@ld50macca.demon.co.uk> <3fb0020d_5@news.athenanews.com> <QAPhpSAMsNs$Ew2v@ld50macca.demon.co.uk>`

```

"Alistair Maclean" <alistair@ld50macca.demon.co.uk> wrote in message
news:QAPhpSAMsNs$Ew2v@ld50macca.demon.co.uk...
> Typical bloody project manager! Wants to see the code AFTER it's been
> corrected. Sorry can not supply code. Hence my original question.
>

Hahaha! Fair comment...

If you cover your tracks then you can't expect sympathy <G> (or help...)

Pete.


> In message <3fb0020d_5@news.athenanews.com>, Peter E.C. Dashwood
> <dashwood@enternet.co.nz> writes
…[24 more quoted lines elided]…
> >> Unfortunately, I did not use the same sequence of parameters for
calling
> >> the second and third programs as was used to call the first program.
> >> Although the sequences for the CALLs matched the LINKAGE SECTION in the
…[8 more quoted lines elided]…
> >I can't believe this. There has to be a discrepancy between the Linkage
and
> >Procedure Division headers, in terms of the parameter definitions.
> >
> >To my knowledge, this is NOT a requirement of Fujitsu COBOL. The fact
that
> >it worked when you changed it would be purely coincidental.
> >
…[13 more quoted lines elided]…
>             Don't you need any IT support?"
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-11-10T14:01:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0311101401.1941b712@posting.google.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com> <z575nPBBYkr$EwY0@ld50macca.demon.co.uk>`

```
Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote 

> I recently wrote a Fujitsu Cobol program 

Which version of Fujitsu was that ?

> which called in sequence three 
> other programs passing the same parameters to each program. 
…[5 more quoted lines elided]…
> program function correctly.

What was the order in the PROCEDURE DIVISION USING clauses ?  Did you
change these when you changed the CALLs.

The LINKAGE SECTION may contain entries which are not part of a CALL
of this program, so matching order should be irrelevant.

I suspect that something else was also changed that actually made the
program work correctly and the order of parameters in the 3 CALLs was
not the fix that you attribute it to.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-11-11T12:52:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FQTktBB9tNs$EwVg@ld50macca.demon.co.uk>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com> <z575nPBBYkr$EwY0@ld50macca.demon.co.uk> <217e491a.0311101401.1941b712@posting.google.com>`

```
Version 3 Fujitsu. I changed the PROC DIV USING at the time of effecting 
the correction. However, as I no longer have the errant source you could 
have a point.

In message <217e491a.0311101401.1941b712@posting.google.com>, Richard 
<riplin@Azonic.co.nz> writes
>Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote
>
…[21 more quoted lines elided]…
>not the fix that you attribute it to.
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-11-10T22:21:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tbUrb.6575$nz.5400@newsread2.news.pas.earthlink.net>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com> <z575nPBBYkr$EwY0@ld50macca.demon.co.uk>`

```
Alistar,
  Either you found a "bug" in the Fujitsu product, or there is something you
aren't telling us about the situation.

Certainly if EITHER the size/definitions of the CALLing parameter or the
CALLed (linkage section) parameters are "different" - then a run-time error
would be "reasonable". Another "problem" can occur when you aren't passing
ALL the parameters in the Procedure Division USING phrase every time.
Otherwise,  I just don't see this being "likely".

The following is an "example" (outline only) of where I would expect
run-time problems:

  Program-ID.  CALLing.
     ...
   01   Big-Field  Pic X(100).
   01   Big-Field2  Pic X(100).
   01  Medium-Field  Pic X(50).
   01  Small-Field   Pic X.
       ...
     Call "CALLed" using  Big-Field Big-Field2 Medium-Field Small-Field
       ...
    Display  "Next Call should work OK in any ANSI conforming compiler"
     Call "CALLed" using Big-Field2   Big-Field  Medium-Field  Small-field
       ***
    Display "Next two calls *may* fail"
    Call "CALLed" using Small-Field Big-Field Medium-Field Big-Field2
       ...
    Call "CALLed" using  Big-Field  Big-Field2  Medium-Field
       ...
  Program-ID.  CALLed
  Linkage Section.
* note that the ORDER that fields are defined in LS is not important
  01  LS-Small-Field   Pic X.
  01  LS-Medium-Field  Pic  X(50).
  01  LS-Big-Field2  Pic X(100).
  01  LS-Big-Field   Pic X(100).
 Procedure Division Using LS-Big-Field Big-Field2  LS-Medium-Field
LS-Small-Field.
*  The next statement may fail if 4 parameters aren't passed
   Move "X" to LS-Small-Field
* The next statement may fail if the 1st parameter passed isn't 100
characters long
   Move "Y" to Big-Field (99:2)
   Exit Program
     .
```

###### ↳ ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-11-11T12:58:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QgNhByBG0Ns$Ew0r@ld50macca.demon.co.uk>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com> <217e491a.0311051634.7b40c9a2@posting.google.com> <acsjeKCdABr$EwP3@ld50macca.demon.co.uk> <217e491a.0311071833.2f2d76be@posting.google.com> <z575nPBBYkr$EwY0@ld50macca.demon.co.uk> <tbUrb.6575$nz.5400@newsread2.news.pas.earthlink.net>`

```
As I no longer have the original errant source I can not be 110% certain 
of the code. However, my memory recalls each program used three tables 
listed in various sequences. I took some care to ensure that the 
parameters were correctly sequenced and that the calling code and the 
called code contained the same definitions. The most likely error may be 
the sequence on the PROC DIV USING statement. But I can not prove it 
either way (and currently my Fujitsu v3 compiler is dead).

Judging by the response, I must have be in error, as no-one else seems 
to have suffered from the same 'feature'.

In message <tbUrb.6575$nz.5400@newsread2.news.pas.earthlink.net>, 
William M. Klein <wmklein@nospam.netcom.com> writes
>Alistar,
>  Either you found a "bug" in the Fujitsu product, or there is something you
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-11-05T17:34:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0311051734.2a2875c9@posting.google.com>`
- **References:** `<3560214.1067990880@dbforums.com> <3563730.1068058752@dbforums.com>`

```
Try changing your called program's name.  V3 only supports 8 character
names beginning with a letter.


manga <member43127@dbforums.com> wrote in message news:<3563730.1068058752@dbforums.com>...
> OK...let me simplify the code..I have changed the code and copied
> below...and again I am getting the same linking error..it says it cannot
…[60 more quoted lines elided]…
>      EXIT PROGRAM.
```

#### ↳ Re: Unresolved external symbal error in fujitsu cobol.

- **From:** manga <member43127@dbforums.com>
- **Date:** 2003-11-06T15:32:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3569110.1068150770@dbforums.com>`
- **References:** `<3560214.1067990880@dbforums.com>`

```

It worked. Thanks for all ur help.



I had to add SM1.obj(sub pgm) to Rt1.obj(main pgm) while linking....



-manga
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
