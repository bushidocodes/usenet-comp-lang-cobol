[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HOW: Does one code EXP in COBOL?

_45 messages · 15 participants · 2000-01_

---

### HOW: Does one code EXP in COBOL?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000111162141.29182.00000352@nso-ba.aol.com>`

```
I am trying to duplicate some PL/1 code in COBOL and there is 
this sticky little compute statement with an EXP function.
I found the general discussion of EXP returning the value of 'e'
raised to the power of 'x', but I just don't get it without a formula
drawn out using functions that I know exist in the realm of COBOL.

  EXP(x) = e**x

  e=LOG(?)

 Any math wizards out there got a handle on how to reduce this to 
 simpler terms.  

 Any and all assistance would be greatly appreciated.
```

#### ↳ Re: Does one code EXP in COBOL?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<85gfrf$cos$1@nntp9.atl.mindspring.net>`
- **References:** `<20000111162141.29182.00000352@nso-ba.aol.com>`

```
Are you using a COBOL with intrinsic functions?  If so, I think that
converting from PL/I to COBOL should be pretty straight forward.  If you
don't have use of the intrinsic functions, I will leave this to one of the
"mathematicians" in the group.
```

##### ↳ ↳ Re: Does one code EXP in COBOL?

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lnRe4.287$Rw3.5282149@news.netdirect.net>`
- **References:** `<20000111162141.29182.00000352@nso-ba.aol.com> <85gfrf$cos$1@nntp9.atl.mindspring.net>`

```
In article <85gfrf$cos$1@nntp9.atl.mindspring.net>, "William M. Klein" <wmklein@nospam.netcom.com> wrote:
>Are you using a COBOL with intrinsic functions?  If so, I think that
>converting from PL/I to COBOL should be pretty straight forward.  If you
>don't have use of the intrinsic functions, I will leave this to one of the
>"mathematicians" in the group.
>
I don't think there's an intrinsic function for e**x. However, a simple 
exponentiation operator should work, e.g.
***** WARNING ****   N O T   T E S T E D
 01 e PIC 9V9(17) COMP VALUE 2.71828182845904524.
..
 COMPUTE answer = e ** x
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VsRe4.288$Rw3.5282149@news.netdirect.net>`
- **References:** `<20000111162141.29182.00000352@nso-ba.aol.com> <85gfrf$cos$1@nntp9.atl.mindspring.net> <lnRe4.287$Rw3.5282149@news.netdirect.net>`

```
In article <lnRe4.287$Rw3.5282149@news.netdirect.net>, dxmixxer@netdirect.net (Douglas Miller) wrote:
>In article <85gfrf$cos$1@nntp9.atl.mindspring.net>, "William M. Klein"
> <wmklein@nospam.netcom.com> wrote:
…[11 more quoted lines elided]…
>
Another option would be to calculate e**x using the MacLaurin series 
expansion:

e**x = (x**0/0!) + (x**1/1!) + (x**2/2!) + (x**3/3!) + (x**4/4!) + ...
= 1 + x + x**2/2 + x**3/6 + x**4/24 + ...

By the time you get out to about the tenth term, you should have as much 
precision as a Cobol program is ever gonna need. If you need better precision 
than that, you probably ought to be writing in Fortran.
```

##### ↳ ↳ Re: Does one code EXP in COBOL?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000114153248.08829.00000653@nso-bd.aol.com>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net>`

```
In article <85gfrf$cos$1@nntp9.atl.mindspring.net>, "William M. Klein"
<wmklein@nospam.netcom.com> writes:

>
>Are you using a COBOL with intrinsic functions?  If so, I think that
…[3 more quoted lines elided]…
>

I am using COBOL for OS/390. an as far as I know the intrinsic functions
are available.  The problem is the use of FUNCTION LOG(n) to arrive at the
value of 'e' which can then be raised to the power of 'x'.

I did see a post providing a fixed value of 2.71828182845904524 for 'e'.
Using this , I was able to duplicate the sample values I was using for 
reference.  It would be nice to have another option that does does not 
require the hardcoded value of 'e'.

Thanks for your earlier responses.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bKRf4.373$Rw3.7347838@news.netdirect.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com>`

```
In article <20000114153248.08829.00000653@nso-bd.aol.com>, sff5ky@aol.comxxx123 (Sff5ky) wrote:
>In article <85gfrf$cos$1@nntp9.atl.mindspring.net>, "William M. Klein"
><wmklein@nospam.netcom.com> writes:
…[19 more quoted lines elided]…
>
Yeah, that would have been me. Perhaps you missed my followup, in which I gave 
the MacLaurin series expansion for e^x:

e^x = x^0/0! + x^1/1! + x^2/2! + x^3/3! + x^4/4! + x^5/5! + ...
= 1 + x + x^2/2 + x^3/6 + x^4/24 + x^5/120 + ...

(n! = 1 * 2 * 3 * 4 * ... * n; 0! = 1 by definition)

Computation of e^x using the MacLaurin series expansion can be implemented 
efficiently in a manner similar to this: (WARNING UNTESTED CODE FOLLOWS)

01 x      PIC S9(3)V9(6) COMP.
01 e-to-x PIC S9(6)V9(12) COMP.
01 n     PIC 99 COMP.
01 denominator PIC 9(9) COMP.
01 numerator    PIC S9(6)V9(12) COMP.
..
* assume that x already contains the desired value

COMPUTE e-to-x = 1
COMPUTE numerator = 1
COMPUTE denominator = 1
PERFORM VARYING n FROM 1 BY 1 UNTIL n > 10
    numerator = numerator * x
    denominator = denominator * n
    COMPUTE e-to-x = e-to-x + (numerator / denominator)
END-PERFORM
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-01-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000116120149.17310.00000226@ng-ci1.aol.com>`
- **References:** `<20000114153248.08829.00000653@nso-bd.aol.com>`

```
sff5ky@aol.comxxx123  (Sff5ky) writes...

[snip]

>
>I am using COBOL for OS/390. an as far as I know the intrinsic functions
…[6 more quoted lines elided]…
>require the hardcoded value of 'e'.

Since you are using the latest COBOL compiler, you have direct access to the LE
callable mathematical functions, which include the following:

CEESSEXP - return 'e' to the power of a single precision floating point number
(comp-1 in COBOL)

CEESDEXP - return 'e' to the power of a double precision floating point number
(comp-2 in COBOL)

CEESQEXP - return 'e' to the power of an extended precision floating point
number (although COBOL doesn't support this format of data item)

CEESTEXP, CEESEEXP, CEESREXP - which do the same thing for complex numbers,
which COBOL doesn't support


in your program...

CALL 'CEESxEXP' USING input-item, FC, output-item

where FC is declared as PIC x(12) value low-values. After your call, if FC is
still low-values then the result in output-itme is useful.

Hope this helps.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000120141330.01638.00000375@nso-fo.aol.com>`
- **References:** `<20000116120149.17310.00000226@ng-ci1.aol.com>`

```
I attempted using the CEESxEXP info from Steve Comstock and 
ran into a few problems.   Could I get a little more supporting information
to get me thru the rest of this little exercise?

Thanks in advance to all.


Having problems using the LE function

*
 01  WS-EXP-TEST-AREA.                           BLW=0002+450         0CL28
 03  WS-INPUT-VALUE PIC S9(9)V9(9) COMP VALUE 0. BLW=0002+450,0000000 8C
 03  WS-OUTPUT-VALUE PIC S9(9)V9(9) COMP VALUE 0.BLW=0002+458,0000008 8C
 03  WS-FUNCTION-RC PIC X(012).                  BLW=0002+460,0000010 12C
 COBOL FOR MVS & VM   1.2.2        CHKLIB    DATE 01/20/2000  TIME 08:06:50
 *************************************************************
 *
      MOVE 16      TO WS-INPUT-VALUE
      MOVE ZERO    TO WS-OUTPUT-VALUE
      MOVE LOW-VALUES TO WS-FUNCTION-RC
      CALL 'CEESDEXP' USING WS-INPUT-VALUE, WS-FUNCTION-RC,
                            WS-OUTPUT-VALUE
      IF WS-FUNCTION-RC = LOW-VALUES
          DISPLAY 'II - FUNCTION CALL SUCCESS!'
        ELSE
          DISPLAY 'FF - FUNCTION CALL FAILED!!'
          END-IF
      DISPLAY 'II - FUNCTION-RC =', WS-FUNCTION-RC
      DISPLAY 'II - INPUT-VALUE =', WS-INPUT-VALUE
      DISPLAY 'II -OUTPUT-VALUE =', WS-OUTPUT-VALUE
 *
 *************************************************************


3035 01 WS-EXP-TEST-AREA
                         AN-GR
3036  02 WS-INPUT-VALUE   S9(9)V9(9) COMP  +0000000016.000000000
3037  02 WS-OUTPUT-VALUE  S9(9)V9(9) COMP  +4688247212.092686336
3038  02 WS-FUNCTION-RC   X(12) DISP       '            '

II - BEGIN OF JOB
II - FUNCTION CALL SUCCESS!
II - FUNCTION-RC =
II - INPUT-VALUE =000000016000000000
CEE3209S The system detected a fixed-point divide exception.
         From compile unit CHKLIB at entry point CHKLIB at statement 3244 at
compile unit offset +0000250C at address
         16D03174.

Should I be using COMP-3? for the return value?
I was expecting a return value of  =8.88611E+6 or 8886110.520507872
which is the result of raising  2.71828182845904524 to the power of 16.

What might I be doing wrong?
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 5)_

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.12f101f3955de5139896a0@news.transport.com>`
- **References:** `<20000116120149.17310.00000226@ng-ci1.aol.com> <20000120141330.01638.00000375@nso-fo.aol.com>`

```
In article <20000120141330.01638.00000375@nso-fo.aol.com>, 
sff5ky@aol.comxxx123 says...
> I attempted using the CEESxEXP info from Steve Comstock and 
> ran into a few problems.   Could I get a little more supporting information
…[47 more quoted lines elided]…
> Should I be using COMP-3? for the return value?

Slap me silly if I'm off-target on this, 
but can't you just use this COBOL syntax?
   COMPUTE W-EXPONENT = FUNCTION LOG(W-PRODUCT)

(I posted this solution over a week ago, but didn't notice any responses 
to it)

Pete
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 6)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000120185108.02618.00000665@nso-fg.aol.com>`
- **References:** `<MPG.12f101f3955de5139896a0@news.transport.com>`

```
In article <MPG.12f101f3955de5139896a0@news.transport.com>, Pete Wirfs
<petwir@saif.com> writes:

>
>Slap me silly if I'm off-target on this, 
…[6 more quoted lines elided]…
>

I'm afraid that I might have missed your intent with this as 
I have already tested this as
  Compute W-EXP = Function LOG(16) **16
  Compute W-EXP = Function LOG(1)**16
and did not get the results I was expecting.
The only thing that has worked is 
  Compute W-EXP = 2.71828182845904524 ** 16

Even the CEESDEXP call does not return the value that 
I was expecting.

If you could enlighten me as to what was intended by W-PRODUCT,
maybe I could use this option over having a hardcoded value for 'e'.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 7)_

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.12f145ccaa6ff3b69896a3@news.transport.com>`
- **References:** `<MPG.12f101f3955de5139896a0@news.transport.com> <20000120185108.02618.00000665@nso-fg.aol.com>`

```
In article <20000120185108.02618.00000665@nso-fg.aol.com>, 
sff5ky@aol.comxxx123 says...
> In article <MPG.12f101f3955de5139896a0@news.transport.com>, Pete Wirfs
> <petwir@saif.com> writes:
…[25 more quoted lines elided]…
> 

In my sample production application code, W-EXPONENT and W-PRODUCT are 
both defined as COMP-2, and our actuary staff are satisfied that the the 
COBOL LOG function generated the result they were looking for with plenty 
of precision.  (the value of 'e' is built into the LOG function.)

I last worked on this application in 1997, so I'm not set up to dig into 
it further right now.  If it doesn't generate the desired result for you, 
then obviously you must look for other solutions!

Pete
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 6)_

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FAPh4.529$Rw3.11150144@news.netdirect.net>`
- **References:** `<20000116120149.17310.00000226@ng-ci1.aol.com> <20000120141330.01638.00000375@nso-fo.aol.com> <MPG.12f101f3955de5139896a0@news.transport.com>`

```
In article <MPG.12f101f3955de5139896a0@news.transport.com>, petwir@saif.com wrote:
[snip]
>
>Slap me silly if I'm off-target on this, 
>but can't you just use this COBOL syntax?
>   COMPUTE W-EXPONENT = FUNCTION LOG(W-PRODUCT)
>
No, he can't -- that function returns the natural logarithm of its argument. 
He's after the exponential function, which is the inverse of the logarithm 
function. To be specific:

if a = exp(b), then b = log(a)
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N%Kh4.529$nx5.15221@dfiatx1-snr1.gtei.net>`
- **References:** `<20000116120149.17310.00000226@ng-ci1.aol.com> <20000120141330.01638.00000375@nso-fo.aol.com>`

```
I think you have to use COMP-1 for both the argument and the return value.

Here's part of the original suggestion..
"....
PL/1 program used (back when I say any PL/1), then the routine to call is
CEESSEXP. It would look something like:

CALL CEESSEXP(WS-FLOAT-VALUE-INPUT,WS-FC,WS-FLOAT-VALUE-OUTPUT)

The COBOL declarations would look like:
77 WS-FLOAT-VALUE-INPUT COMP-1.
77 WS-FLOAT-VALUE-OUTPUT COMP-1.
77 WS-FC PIC X(12).

I hope this was of some help to you,
John McKown

.."


Sff5ky wrote in message <20000120141330.01638.00000375@nso-fo.aol.com>...
>I attempted using the CEESxEXP info from Steve Comstock and
>ran into a few problems         16D03174.
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 6)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000120185108.02618.00000666@nso-fg.aol.com>`
- **References:** `<N%Kh4.529$nx5.15221@dfiatx1-snr1.gtei.net>`

```
In article <N%Kh4.529$nx5.15221@dfiatx1-snr1.gtei.net>, "Michael Mattias"
<michael.mattias@gte.net> writes:

>
>I think you have to use COMP-1 for both the argument and the return value.
>
>

Imagine that!  I missed that one detail and it made all the 
difference in the world!  Thanks for the correction.
I knew that if I provided enough information from what I had 
been testing with, the solution would jump out with very little
trouble at all.

Thanks again.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3887e4e3.10198386@news.freewwweb.com>`
- **References:** `<20000116120149.17310.00000226@ng-ci1.aol.com> <20000120141330.01638.00000375@nso-fo.aol.com>`

```
On 20 Jan 2000 19:13:30 GMT, sff5ky@aol.comxxx123 (Sff5ky) wrote:

>I attempted using the CEESxEXP info from Steve Comstock and 
>ran into a few problems.   Could I get a little more supporting information
…[3 more quoted lines elided]…
>

I've been following this for some time, and I just finally have to
post this.  Maybe, just maybe I am missing something.  I know that the
initial post was about exponant and log (which can be obtained using
intrinsic functions) - but I have always used the following for
exponants:

Compute num = numb ** Exponant

For square roots and cube roots:

Compute root = numb ** 1/2 or compute root = numb ** 1/3

Seems to work fine all the time.  Here is a test program to try for
exponants:

 IDENTIFICATION DIVISION.
 PROGRAM-ID.  TEST01.
 ENVIRONMENT DIVISION.
 CONFIGURATION SECTION.
 DATA DIVISION.
 WORKING-STORAGE SECTION.
 01  FIRST-NUM PIC 9(9).
 01  RESULTANT PIC 9(9).
 01  EXPONANT PIC 99.
 PROCEDURE DIVISION.
 START-OF-PROGRAM.
     PERFORM VARYING FIRST-NUM FROM 1 BY 1 UNTIL FIRST-NUM > 5
       PERFORM VARYING EXPONANT FROM 1 BY 1 UNTIL EXPONANT > 4
	COMPUTE RESULTANT = FIRST-NUM ** EXPONANT
        DISPLAY "first " FIRST-NUM " exponant " EXPONANT
                " result " RESULTANT
       END-PERFORM
     END-PERFORM
     STOP RUN
     .

What am *I* missing?  Why wouldn't this work?
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 6)_

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k1%h4.535$Rw3.11469948@news.netdirect.net>`
- **References:** `<20000116120149.17310.00000226@ng-ci1.aol.com> <20000120141330.01638.00000375@nso-fo.aol.com> <3887e4e3.10198386@news.freewwweb.com>`

```
In article <3887e4e3.10198386@news.freewwweb.com>, thaneH@softwaresimple.com (Thane Hubbell) wrote:
>On 20 Jan 2000 19:13:30 GMT, sff5ky@aol.comxxx123 (Sff5ky) wrote:
>
…[14 more quoted lines elided]…
>
[snip]
>
>What am *I* missing?  Why wouldn't this work?

The only thing you missed was my first response to his post, in which 
I suggested doing exactly that, with 'e' defined as a constant in 
working-storage.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 6)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000121202330.01717.00000825@nso-fz.aol.com>`
- **References:** `<3887e4e3.10198386@news.freewwweb.com>`

```
In article <3887e4e3.10198386@news.freewwweb.com>, thaneH@softwaresimple.com
(Thane Hubbell) writes:

>I've been following this for some time, and I just finally have to
>post this.  Maybe, just maybe I am missing something.  I know that the
…[9 more quoted lines elided]…
>
   <<snip>>
>
>What am *I* missing?  Why wouldn't this work?
>
>

  It is not JUST Exponentiation.  the EXP function that I am trying
  to duplicate returns the value of 'e' raised to the power of 'x', where
  'e' is the value of the natural logarithm(?).
  I have since been given 2 options that DO work.

 The first option is using a fixed constant representing 'e' as 2.718.....
 and a compute statement similar to what you have suggested.

   WS-natural-log-e pic s9v9(17) comp-3 value 2.718.....
   WS-power-of-x pic s9(9)v9(9) comp-3.
   WS-exp-of-e pic s9(9)v9(9) comp-3.
   Move 16 to WS-power-of-x
   Compute WS-exp-of-e = ws-natural-log-e ** ws-power-of-x

 The second option is IBM LE specific (OS\390\LE).  (Which I mistakenly
 reported as not working , because of using the wrong usage syntax.)

  WS-power-of-x comp-1.
  WS-exp-of-e comp-1.
  WS-CEESDEXP-FC pic x(12).
  Move 16 to WS-power-of-x
  Move Low-values to WS-CEESDEXP-FC
  CALL 'CEESDEXP' USING WS-pwer-of-x, WS-CEESDEXP-FC, WS-exp-of-e
  IF WS-CEESDEXP-FC = Low-values
     ***Function returned good result
     Display ' EXP(', WS-power-of-x, ') = ', WS-exp-of-e
  Else
    ***Function failed
    Display'WW - Something went wrong - RC = ', WS-CEESDEXP-FC
    End-if
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000119195740.02746.00000241@nso-fp.aol.com>`
- **References:** `<20000116120149.17310.00000226@ng-ci1.aol.com>`

```
In article <20000116120149.17310.00000226@ng-ci1.aol.com>, scomstock@aol.com (S
Comstock) writes:

>
>Since you are using the latest COBOL compiler, you have direct access to the
…[14 more quoted lines elided]…
>

Thanks , Steve.

I was looking for something along the lines of this, just never worked
with calling the LE functions and how to validate the return items.
This is the 'ideal' solution to getting the equivalent function result to
calculations currently being done in PL/1.

Question:  Your response mentioned 'complex' numbers.  What might 
be the explanation of this term?  I think that the PL/1 routine is working
with values such as -1.0004375 and 0.93685 or some such range.
Is this valid in the COBOL/LE call scenario ?

Thanks again for your time.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

- **From:** John Grznar <jgrznar@earthlink.net>
- **Date:** 2000-01-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388B4FC6.2F4024AF@earthlink.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com>`

```
What you are trying to do is to calculate the value of e.  However, e = the sum
from n=0 to infinity of 1 / n! BY DEFINITION!  The 'by definition' is very
important here.  If e could be calculated by other means (which is what you are
trying to do) then e would not be defined by definition.  I am afraid you are
attempting the impossible.

John Grznar

Sff5ky wrote:

> In article <85gfrf$cos$1@nntp9.atl.mindspring.net>, "William M. Klein"
> <wmklein@nospam.netcom.com> writes:
…[17 more quoted lines elided]…
> Thanks for your earlier responses.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 4)_

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<baXi4.597$Rw3.13214370@news.netdirect.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net>`

```
In article <388B4FC6.2F4024AF@earthlink.net>, jgrznar@earthlink.net wrote:
>What you are trying to do is to calculate the value of e.  However, e = the sum
>from n=0 to infinity of 1 / n! BY DEFINITION!  The 'by definition' is very
…[4 more quoted lines elided]…
>John Grznar

Oh, my. Please gets your facts straight before you post.

(1) He's *not* trying to calculate the value of e, he's trying to evaluate the 
function e^x.

(2) It is certainly possible to compute the value of e, or of e^x, to any 
arbitrary degree of precision, simply by expanding the infinite series *far 
enough*. For most computing applications, six or eigth digits right of the 
decimal is sufficient precision, and this can be achieved by computing only 
about the first ten terms of the series. It is not necessary to expand the 
entire infinite series in order to obtain a usable approximation of its sum.

>
>Sff5ky wrote:
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 5)_

- **From:** "John Grznar" <jgrznar@earthlink.net>
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net>`

```

Douglas Miller <dxmixxer@netdirect.net> wrote in message
news:baXi4.597$Rw3.13214370@news.netdirect.net...
> In article <388B4FC6.2F4024AF@earthlink.net>, jgrznar@earthlink.net wrote:
> >What you are trying to do is to calculate the value of e.  However, e =
the sum
> >from n=0 to infinity of 1 / n! BY DEFINITION!  The 'by definition' is
very
> >important here.  If e could be calculated by other means (which is what
you are
> >trying to do) then e would not be defined by definition.  I am afraid you
are
> >attempting the impossible.
> >
…[4 more quoted lines elided]…
> (1) He's *not* trying to calculate the value of e, he's trying to evaluate
the
> function e^x.
>

  I know what he is trying to do.  Any high school algebra student should
know how to raise a number to a power.  Therefore, the problem boils down to
finding 'e'.  Once you have 'e' then finding e^x is trivial.

>
> (2) It is certainly possible to compute the value of e, or of e^x, to any
> arbitrary degree of precision, simply by expanding the infinite series
*far
> enough*. For most computing applications, six or eigth digits right of the
> decimal is sufficient precision, and this can be achieved by computing
only
> about the first ten terms of the series. It is not necessary to expand the
> entire infinite series in order to obtain a usable approximation of its
sum.
>

I know that, you know that, and the original poster knows that.  If you have
read the thread from the beginning then you should understand the problem.
He wants to compute e^16.  He first tried a function call but it didn't
work, he later found out why and is now using it.  However, in the
intervening time, he was looking for another way.  He knew he could just
hard code a value for e and use that, but he wanted a more elegant solution.
He also knew about the expansion series.  He said he didn't like using the
expansion series because it converges to slowly FOR HIM.  I, as you do, do
not understand why he feels that way because the series does converge
extremely fast.  But who are we to say?  So, what the problem boils down to
is finding e (or e^x if you insist)without:
   a:   hard coding a value for e or
   b:   using the expansion series.
This I claim is impossible!  If he is wants to compute e^16 then he is stuck
using either a or b or a function that uses a or b.

Now, what I would like to know, is why there isn't an EXP intrinsic function
in standard COBOL?

> >
> >> In article <85gfrf$cos$1@nntp9.atl.mindspring.net>, "William M. Klein"
…[4 more quoted lines elided]…
> >> >converting from PL/I to COBOL should be pretty straight forward.  If
you
> >> >don't have use of the intrinsic functions, I will leave this to one of
the
> >> >"mathematicians" in the group.
> >> >
> >>
> >> I am using COBOL for OS/390. an as far as I know the intrinsic
functions
> >> are available.  The problem is the use of FUNCTION LOG(n) to arrive at
the
> >> value of 'e' which can then be raised to the power of 'x'.
> >>
> >> I did see a post providing a fixed value of 2.71828182845904524 for
'e'.
> >> Using this , I was able to duplicate the sample values I was using for
> >> reference.  It would be nice to have another option that does does not
…[6 more quoted lines elided]…
> dlmiller/at/netdirect/dot/net
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 6)_

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dogj4.636$Rw3.13939218@news.netdirect.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net>`

```
In article <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net>, "John Grznar" <jgrznar@earthlink.net> wrote:
>
>
…[24 more quoted lines elided]…
>finding 'e'.  Once you have 'e' then finding e^x is trivial.

It certainly doesn't *appear* that you "know what he is trying to do" from the 
fact that the post asked how to implement e^x in a Cobol program, and you 
responded "What you are trying to do is calculate the value of e".

And that isn't a problem. The value of e is easily obtainable from any number 
of mathematical reference books. And several people, myself included, have 
posted that value earlier in the thread.
>>
>> (2) It is certainly possible to compute the value of e, or of e^x, to any
…[11 more quoted lines elided]…
>read the thread from the beginning then you should understand the problem.

I *have* read the thread from the beginning, and clearly you have not. If you 
had, you could hardly have missed the fact that I was one of the first people 
who responded to his post, supplying two different methods of doing what he 
asked for: calculating e^x in a Cobol program.

>He wants to compute e^16.  He first tried a function call but it didn't
>work, he later found out why and is now using it.  However, in the
>intervening time, he was looking for another way.  He knew he could just
>hard code a value for e and use that, but he wanted a more elegant solution.

Clearly you came into the thread somewhere in the middle. There is no evidence 
in the original post that he knew the precise value of e.

>He also knew about the expansion series. 

Nor is there any evidence of this in the original post, which is reproduced 
here for your reference (since you apparently have not seen it):

************************
I am trying to duplicate some PL/1 code in COBOL and there is 
 this sticky little compute statement with an EXP function.
 I found the general discussion of EXP returning the value of 'e' raised to 
the power of 'x', but I just don't get it without a formula drawn out using 
functions
 that I know exist in the realm of COBOL. 
  
   EXP(x) = e**x
  
   e=LOG(?)
  
 Any math wizards out there got a handle on how to reduce this to simpler 
terms.  
  
 Any and all assistance would be greatly appreciated.
************************
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 7)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hij4.142$K26.4250@dfiatx1-snr1.gtei.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net>`

```
Douglas Miller wrote in message ...

>And that isn't a problem. The value of e is easily obtainable from any
> number of mathematical reference books. And several people, myself
included, have posted that value earlier in the thread.
>>>
>>> (2) It is certainly possible to compute the value of e, or of e^x, to
any
>>> arbitrary degree of precision, simply by expanding the infinite series
>>*far
>>> enough*. For most computing applications, six or eigth digits right of
the
>>> decimal is sufficient precision, and this can be achieved by computing
>>only
>>> about the first ten terms of the series. It is not necessary to expand
the
>>> entire infinite series in order to obtain a usable approximation of its
>>sum.

Um, isn''t it easier to get the value of 'e' to the best precision available
on the current system by using the exponent function with a power of 1.0?
That is e**1 = e, doesn't it?

ref:
In article <20000116120149.17310.00000226@ng-ci1.aol.com>, scomstock@aol.com
(S
Comstock) writes:

>
>Since you are using the latest COBOL compiler, you have direct access to
the
>LE
>callable mathematical functions, which include the following:
…[3 more quoted lines elided]…
>

Seems to me, then, that 'e' may be obtained with:

77 INPUT-ITEM    COMP-1.
77 OUTPUT-ITEM COMP-1
77 E                    COMP-1
77 FC                  PIC X(12)

MOVE 1 TO INPUT-ITEM
MOVE LOW-VALUE TO FC
CALL 'CEESSEXP' USING input-item, FC, output-item
IF FC EQUAL LOW-VALUE THEN
  MOVE OUTPUT-ITEM TO E
ELSE
  DISPLAY 'OOPS!'
END-IF

MCM
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 8)_

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388db202_2@news3.prserv.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net>`

```
for people really obsessed by knowing the value of e, here it is:
e = 2.55760 52130 50535 51246 52773 42542 00741 72363 6166..(8)

Michael Mattias <michael.mattias@gte.net> wrote in message
news:9hij4.142$K26.4250@dfiatx1-snr1.gtei.net...
> Douglas Miller wrote in message ...
>
…[14 more quoted lines elided]…
> >>> entire infinite series in order to obtain a usable approximation of
its
> >>sum.
>
> Um, isn''t it easier to get the value of 'e' to the best precision
available
> on the current system by using the exponent function with a power of 1.0?
> That is e**1 = e, doesn't it?
>
> ref:
> In article <20000116120149.17310.00000226@ng-ci1.aol.com>,
scomstock@aol.com
> (S
> Comstock) writes:
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Real large numbers

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388DB6E2.DD743815@NOSPAMwebaccess.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net> <388db202_2@news3.prserv.net>`

```
Leif Svalgaard wrote:
> 
> for people really obsessed by knowing the value of e, here it is:
> e = 2.55760 52130 50535 51246 52773 42542 00741 72363 6166..(8)

Has anybody here used Real Large Numbers in Cobol for real programs (not
just playing around?)
```

###### ↳ ↳ ↳ Re: Real large numbers

_(reply depth: 10)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 2000-01-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86lfnt$lt1$1@news.igs.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net> <388db202_2@news3.prserv.net> <388DB6E2.DD743815@NOSPAMwebaccess.net>`

```
Well, I tried to add up my Amex once ...

Howard Brazee wrote in message <388DB6E2.DD743815@NOSPAMwebaccess.net>...
>Leif Svalgaard wrote:
>>
…[4 more quoted lines elided]…
>just playing around?)
```

###### ↳ ↳ ↳ Re: Real large numbers

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dgDj4.29646$wk.517704@news1.mia>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net> <388db202_2@news3.prserv.net> <388DB6E2.DD743815@NOSPAMwebaccess.net>`

```
Howard Brazee wrote:
>
>Has anybody here used Real Large Numbers in Cobol for real programs
>(not just playing around?)

How large do you mean by 'Real Large'?  Tens of digits, hundreds of
digits, thousands of digits, millions of digits?  I've done some work
on hundreds (over 1000) digits, though not much in COBOL.
```

###### ↳ ↳ ↳ Re: Real large numbers

_(reply depth: 11)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388F0AF0.44CF8596@NOSPAMwebaccess.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net> <388db202_2@news3.prserv.net> <388DB6E2.DD743815@NOSPAMwebaccess.net> <dgDj4.29646$wk.517704@news1.mia>`

```
Judson McClendon wrote:
> 
> Howard Brazee wrote:
…[6 more quoted lines elided]…
> on hundreds (over 1000) digits, though not much in COBOL.

Anything larger than what COBOL is designed to handle, where you have to
treat the number as an array of digits or some other alternative.  It
shouldn't make any difference after this to how to process these numbers
unless you get to table size maximums.
```

###### ↳ ↳ ↳ Re: Real large numbers

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O2Fj4.11006$1%2.196547@news3.mia>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net> <388db202_2@news3.prserv.net> <388DB6E2.DD743815@NOSPAMwebaccess.net> <dgDj4.29646$wk.517704@news1.mia> <388F0AF0.44CF8596@NOSPAMwebaccess.net>`

```
Howard Brazee wrote:
>Judson McClendon wrote:
>> Howard Brazee wrote:
…[11 more quoted lines elided]…
>unless you get to table size maximums.

Not necessarily.  For hundreds or thousands of digits, yes.  But if
all you want is, say 30 digit integers, you can handle that fairly
easily by making each number two 15 digit data items, and handle
accordingly.  In many cases this would be simpler and more efficient
than resorting to tables of digits.  And if you need floating point
numbers, the table of digits would be better, though you can gain
some significant calculation efficiency by storing several digits in
one element.  If you want to see some well commented algorithms (but
in C), download BIGCALC.ZIP from my website below.  The algorithms
should map fairly well to COBOL, as far as the math is concerned.
For efficiency, the divide routine is in as tightly written C as I
could manage, and may not be as easily understood as the rest of the
code.  I have done a bit of this in COBOL, but many years ago, and I
don't have any of the source code.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 8)_

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WNtj4.661$Rw3.14424051@news.netdirect.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net>`

```
In article <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net>, "Michael Mattias" <michael.mattias@gte.net> wrote:
>Douglas Miller wrote in message ...
>
…[20 more quoted lines elided]…
>
Not if you don't have an intrinsic function to calculate it.
<snip>

>CALL 'CEESSEXP' USING input-item, FC, output-item

This is, of course, highly platform-dependent.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 8)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000125223427.01352.00000120@nso-fn.aol.com>`
- **References:** `<9hij4.142$K26.4250@dfiatx1-snr1.gtei.net>`

```
In article <9hij4.142$K26.4250@dfiatx1-snr1.gtei.net>, "Michael Mattias"
<michael.mattias@gte.net> writes:

>
>Seems to me, then, that 'e' may be obtained with:
…[14 more quoted lines elided]…
>

This is all perfectly valid, but the object of getting the value of 'e' was to 
be able to use strictly COBOL code in a non-IBM environment.  I have 
resorted to the use of the OC/390 LE Function call CEESDEXP to obtain
the result of EXP(x) or e**x as an interim solution.
For my non-IBM platform development I will continue to use 
2.7182818205492 ** x.

My earlier request for an alternative solution for a hard-coded value for e
had to do with wanting a COBOL function or formula other than the iterative
division / exponentiation progression that would supply the value of e for 
use in exponentiation to the power of x.

Since it has been stated several times that it can't be done without the 
progression expansion or the hard-coded vaue, I have settled on the use
of the hard-coded value as it does not involve additional cpu cycles to
determine
'e'.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 9)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ixCj4.82$ag.3560@dfiatx1-snr1.gtei.net>`
- **References:** `<9hij4.142$K26.4250@dfiatx1-snr1.gtei.net> <20000125223427.01352.00000120@nso-fn.aol.com>`

```
Save clock cycles? Um, just how many times in any one program do you need to
calculate this? I thought COBOL allowed you to calculate a value once and
re-use it. Damn, I better re-read the manual.

Ok, so that's not very nice of me to say that. But you have managed to hit
one of my 'hot buttons' - pinching pennies while wasting pounds of clocks.
I've just seen too many programs where those pounds are available with a
small investment in restructuring loops, storing commonly-used values in
working-storage rather than re-calculating several times, changing from
unsorted to sorted tables, etc., etc. etc.

Just as Willie Sutton robbed banks "because that's where they keep the
money,"  programmers should focus performance tuning on those sections of
code using the most clocks the most number of times rather than on one-shot
computations.

While your point is valid in the non-LE environment, MVS/LE was a 'condition
of contest'.

MCM

Sff5ky wrote in message <20000125223427.01352.00000120@nso->This is all
>Since it has been stated several times that it can't be done without the
>progression expansion or the hard-coded vaue, I have settled on the use
>of the hard-coded value as it does not involve additional cpu cycles to
>determine 'e'.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 10)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000126113302.05636.00000270@nso-fv.aol.com>`
- **References:** `<ixCj4.82$ag.3560@dfiatx1-snr1.gtei.net>`

```
In article <ixCj4.82$ag.3560@dfiatx1-snr1.gtei.net>, "Michael Mattias"
<michael.mattias@gte.net> writes:

>
>Save clock cycles? Um, just how many times in any one program do you need to
…[9 more quoted lines elided]…
>

You are right that I could put the calculation procedure somewhere in an 
initialization process and store the value for use in later computations.
I suppose that I could throw this into some kind of arithmetic functions DLL 
and use a CALL to it in order to keep from having to duplicate the logic into
any future programs that might need this kind of function.
These days we are seeing more of the external Marketing Modelers using
packages that require this type of function.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 7)_

- **From:** John Grznar <jgrznar@earthlink.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388E7842.9AC7A34C@earthlink.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net>`

```


Douglas Miller wrote:

> In article <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net>, "John Grznar" <jgrznar@earthlink.net> wrote:
> >
> >

<snip> <snif>

  I stand corrected as to the intent of the original poster.  But, I stand by the gist of my messages, that if you
want to find the value of e (or e^x, if you prefer) you must either hard code a (approximate) value for e, use the
expansion series to find the value of e, or use a function that uses one of those two.  There just isn't any other
way to do it.

  Now I know an n-th Taylor polynomial can be used to find the value of e^x; however, that series is but the series
for e with each term multiplied by x^n.  So by using the series for e^x, you are but using a function of the series
for e.

John Grznar
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<388F02FF.9644C583@NOSPAMwebaccess.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <388E7842.9AC7A34C@earthlink.net>`

```
It appears that the writers of COBOL didn't figure that EXP would be a
priority for COBOL.  IBM mainframes have it via the Language Environment
which was written for multiple languages.

Is it used for some financial functions, or are we talking about using
the tool at hand (COBOL), for some non-business needs?
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 9)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000126113301.05636.00000269@nso-fv.aol.com>`
- **References:** `<388F02FF.9644C583@NOSPAMwebaccess.net>`

```
In article <388F02FF.9644C583@NOSPAMwebaccess.net>, Howard Brazee
<brazee@NOSPAMwebaccess.net> writes:

>It appears that the writers of COBOL didn't figure that EXP would be a
>priority for COBOL.  IBM mainframes have it via the Language Environment
…[5 more quoted lines elided]…
>

I have an application/program that needs this function in doing some funky
statistical calculations for mortality or client stratification based on
demographics.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 10)_

- **From:** bwpent@my-deja.com
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86vrqe$mhn$1@nnrp1.deja.com>`
- **References:** `<388F02FF.9644C583@NOSPAMwebaccess.net> <20000126113301.05636.00000269@nso-fv.aol.com>`

```
Okay, IBMs COBOL has always had the EXPONENT functionality, it just was
not called EXP except in LE370. As you know LE370 routines can be
dynamically called from COBOL390.

Here is what you do... Its documented in the COBOL manuals...

Two asterisks causes EXP to be used during arithmetic operations.

COMPUTE NUM1 = NUM2 ** NUM3

Basically NUM2 is be multiplied by itself the number of times indicated
in NUM3 and the result is be stored in NUM1.

So the conclusion is OS/VS COBOL, COBOL2 and COBOL390 (LE370) have the
same funtionality.

I have 25 years of COBOL experience.

Brett


In article <20000126113301.05636.00000269@nso-fv.aol.com>,
  sff5ky@aol.comxxx123 (Sff5ky) wrote:
> In article <388F02FF.9644C583@NOSPAMwebaccess.net>, Howard Brazee
> <brazee@NOSPAMwebaccess.net> writes:
>
> >It appears that the writers of COBOL didn't figure that EXP would be
a
> >priority for COBOL.  IBM mainframes have it via the Language
Environment
> >which was written for multiple languages.
> >
> >Is it used for some financial functions, or are we talking about
using
> >the tool at hand (COBOL), for some non-business needs?
> >
> >
>
> I have an application/program that needs this function in doing some
funky
> statistical calculations for mortality or client stratification based
on
> demographics.
>
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86vtl2$2s$1@nntp9.atl.mindspring.net>`
- **References:** `<388F02FF.9644C583@NOSPAMwebaccess.net> <20000126113301.05636.00000269@nso-fv.aol.com> <86vrqe$mhn$1@nnrp1.deja.com>`

```
The "EXP" intrinsic function is NOT the same as "exponentiation".  It is
certainly true that COBOL has always (well as long as I know of) supported
exponentiation via the "**" arithmetic operand.  The following is the
"summary" of what the "EXP" intrinsic function does in the draft standard:

"The EXP function returns an approximation of the value of e raised to the
power of the argument."

Sorry if I wasn't clear about what this (new) function does (and why it is
related to ALSO adding the intrinsic function "E").

"OBVIOUSLY" - if you are willing to hard-code the value of "E" in your
program (or to calculate it to whatever level of precision you want), then
you don't need this new intrinsic function at all. However, it is used in
some mathematical calculations which is why both functions are being added to
the next COBOL.
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86u06n$sta$1@nntp5.atl.mindspring.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net> <baXi4.597$Rw3.13214370@news.netdirect.net> <KC7j4.4780$bp2.220016@newsread2.prod.itd.earthlink.net> <Dogj4.636$Rw3.13939218@news.netdirect.net> <388E7842.9AC7A34C@earthlink.net> <388F02FF.9644C583@NOSPAMwebaccess.net>`

```
As stated elsewhere, both "E" and "EXP" are being added as intrinsic function
in the next revision.  (Ask your "vendor of choice" for an early
implementation - if you are willing to pay for it. <G>)
```

###### ↳ ↳ ↳ Re: Does one code EXP in COBOL?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<86tvvt$quj$1@nntp5.atl.mindspring.net>`
- **References:** `<85gfrf$cos$1@nntp9.atl.mindspring.net> <20000114153248.08829.00000653@nso-bd.aol.com> <388B4FC6.2F4024AF@earthlink.net>`

```
I can't believe how long this thread has continued.  Makes me (almost) glad
that the next revision actually will add the "E" and "EXP" intrinsic
functions.  (Sorry about my much earlier post where I thought they were
already in the '89 Standard.)
```

#### ↳ Re: HOW: Does one code EXP in COBOL?

- **From:** joarmc@linux2.johnmckown.net (John McKown)
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<slrn87nkl5.35v.joarmc@linux2.johnmckown.net>`
- **References:** `<20000111162141.29182.00000352@nso-ba.aol.com>`

```

On 11 Jan 2000 21:21:41 GMT, Sff5ky <sff5ky@aol.comxxx123> wrote:
>I am trying to duplicate some PL/1 code in COBOL and there is
>this sticky little compute statement with an EXP function.
…[9 more quoted lines elided]…
> simpler terms.

Well, in "pure" COBOL, I would even hazard a guess. However, if you are
running VS COBOL II or the current COBOL For OS/390 & VM, and you are
running LE/370 (which you must with the latter compiler), then you can
use the LE/370 callable routine, CEESxEXP. The lower case x is replaced
by a specific character indicating the parameters. This routine is explained
in the manual "OS/390: Language Environment for OS/390 & VM Programming
Reference", manual number SC28-1940, book name CEEA305. If you want to
get EXP(x) where x is a 32 bit floating point number, which I think most
PL/1 program used (back when I say any PL/1), then the routine to call is
CEESSEXP. It would look something like:

CALL CEESSEXP(WS-FLOAT-VALUE-INPUT,WS-FC,WS-FLOAT-VALUE-OUTPUT)

The COBOL declarations would look like:
77 WS-FLOAT-VALUE-INPUT COMP-1.
77 WS-FLOAT-VALUE-OUTPUT COMP-1.
77 WS-FC PIC X(12).

I hope this was of some help to you,
John McKown
HealthAxis.com
```

##### ↳ ↳ Re: HOW: Does one code EXP in COBOL?

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-01-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000115100839.23039.00001265@nso-ck.aol.com>`
- **References:** `<slrn87nkl5.35v.joarmc@linux2.johnmckown.net>`

```
In article <slrn87nkl5.35v.joarmc@linux2.johnmckown.net>,
joarmc@linux2.johnmckown.net (John McKown) writes:

>get EXP(x) where x is a 32 bit floating point number, which I think most
>PL/1 program used (back when I say any PL/1), then the routine to call is
…[8 more quoted lines elided]…
>

This is exactly what I was looking for!  I saw some information in the LE
portion of the Online manual, but still was uncertain of how the syntax
and field definitons should be handled.

Thanks ever so much!
```

#### ↳ Re: Does one code EXP in COBOL?

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 2000-01-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<387befdc_3@news3.prserv.net>`
- **References:** `<20000111162141.29182.00000352@nso-ba.aol.com>`

```

Sff5ky <sff5ky@aol.comxxx123> wrote in message
news:20000111162141.29182.00000352@nso-ba.aol.com...
> I am trying to duplicate some PL/1 code in COBOL and there is
> this sticky little compute statement with an EXP function.
…[9 more quoted lines elided]…
>  simpler terms.

If you don't have the ** function or other suitable thing to call,
go to http://www.etk.com/download/etkpak/etkpak.htm#MATHPK
go get a routine (MATHPK) that you can use on ANY system.
```

#### ↳ Re: HOW: Does one code EXP in COBOL?

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 2000-01-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.12e580cdf824c98b989698@news.transport.com>`
- **References:** `<20000111162141.29182.00000352@nso-ba.aol.com>`

```
In article <20000111162141.29182.00000352@nso-ba.aol.com>, 
sff5ky@aol.comxxx123 says...
> I am trying to duplicate some PL/1 code in COBOL and there is 
> this sticky little compute statement with an EXP function.
…[14 more quoted lines elided]…
> 

On our OS/390 platform, I have used:
 COMPUTE WA-EXPONENT = FUNCTION LOG(WA-PRODUCT)

Is this what you are looking for?
```

#### ↳ Re: HOW: Does one code EXP in COBOL?

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2000-01-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000113225914.12140.00000195@ng-cr1.aol.com>`
- **References:** `<20000111162141.29182.00000352@nso-ba.aol.com>`

```

An '85 compiler with '89 extensions should have the functions you need: see

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYLR201/CONTENTS?SHELF=


In chapter 7.0 Part 7. Intrinsic Functions

see 
7.1.20        LOG
http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYLR201/7%2e1%2e20

and
7.1.21        LOG10

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/BOOKS/IGYLR201/7%2e1%2e21?
SHELF=



Robert Rayhawk
RKRayhawk@aol.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
