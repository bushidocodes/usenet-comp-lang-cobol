[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COMP-2, Floating Point Help needed!!

_6 messages · 6 participants · 1997-08_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### COMP-2, Floating Point Help needed!!

- **From:** "dta..." <ua-author-17073385@usenetarchives.gap>
- **Date:** 1997-08-12T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5sqvug$es7$1@venus.ConnectI.com>`

```

I am in serious need of some help in converting parameter input data
from text format to COMP-2, floating point decimal.
Here is how it looks:
Input a parameter in a 10 byte field:
05 INPUT-PARM PIC X(10) VALUE '523.123456'.
The value or decimal point position can change from time to time. It
will actuallu be read from a file. The input parameter needs to be
moved into field for computation.
05 CALCULATE-FIELD COMP-2.
I am using mainframe, MVS, COBOL/370, and when I try to move the
INPUT-PARM to the COMP-2 field I get an error stating that the input
field contained an invalid character. This is probably the decimal
point, but I do not know how to define the data such that the decimal
point has meaning without having to modify the progam. The idea is to
have the parameter change decimal positions without having to change
the program.
I have read about mantissas and exponents and do not really understand
what this means in terms of inputting floating point literals.
Any help or directions to sites, etc. will be grreatly appreciated.

Many Thanks!
dt
```

#### ↳ Re: COMP-2, Floating Point Help needed!!

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-08-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc0cea817-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5sqvug$es7$1@venus.ConnectI.com>`
- **References:** `<5sqvug$es7$1@venus.ConnectI.com>`

```

dta··.@con··i.com wrote:
› 
› I am in serious need of some help in converting parameter input data
…[20 more quoted lines elided]…
› dt
You can't move a USAGE DISPLAY (implied usage with PIC X) to a numeric
field with any certainty. Since your input parm is pretty much 'free
format', I'd suggest the following:

05 INPUT-PARM PIC X(10).
05 NUMERIC-FIELD PIC 9(5)v9(5).
05 FILLER REDEFINES NUMERIC-FIELD.
10 UNITS PIC X(5) JUSTIFIED RIGHT.
10 DECIMALS PIC X(5).
05 CALCULATE-FIELD PIC 9(?) COMP-2.

MOVE ZERO TO NUMERIC-FIELD.
UNSTRING INPUT-PARM DELIMITED BY '.' INTO UNITS DECIMALS.
MOVE NUMERIC-FIELD TO CALCULATE-FIELD.

Good luck :-)
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: COMP-2, Floating Point Help needed!!

- **From:** "joe kohler" <ua-author-6589073@usenetarchives.gap>
- **Date:** 1997-08-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc0cea817-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5sqvug$es7$1@venus.ConnectI.com>`
- **References:** `<5sqvug$es7$1@venus.ConnectI.com>`

```

dta··.@con··i.com wrote:
› 
› I am in serious need of some help in converting parameter input data
…[10 more quoted lines elided]…
› 

---8<----minor snip---
dt, you first need to get your alphabetic data field into a
numeric-edited format (PIC S9(x)v9(x)) and thn you can move it to the
COMP-2 field. Alternatively you could format your input into External
Floating point and accomplish much the same thing. Check out your COBOL
manual under MOVE and FLOATING POINT.

Joe.
```

#### ↳ Re: COMP-2, Floating Point Help needed!!

- **From:** "le..." <ua-author-651022@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc0cea817-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5sqvug$es7$1@venus.ConnectI.com>`
- **References:** `<5sqvug$es7$1@venus.ConnectI.com>`

```

Dear dt:

You are treating the field as alphanumeric so you get none of the niceties
of numeric. You can define it as pic "9(03).9(06)". Now it knows how to
handle the decimal point (the . becomes a numeric editing character).

You say that the decimal point shifts from time to time. This will
require more work - redefinitions to locate the decimal point so you know
which view to use (i.e. 9(02).9(07), etc).

As a last resort you could make it a 10 character table and do it like
grade school. Find and remember the subscript of the decimal point.
Then add/move the value at (sub -1) to the comp-2 field, add (10 * sub -
2), (100 * sub-3) and so on to sub = 1. Then add (sub +1)/10, (sub
+2)/100 and so on to sub = 10.

Hope this helps point the way (it was a bit difficult to explain).
```

#### ↳ Re: COMP-2, Floating Point Help needed!!

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-08-13T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc0cea817-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5sqvug$es7$1@venus.ConnectI.com>`
- **References:** `<5sqvug$es7$1@venus.ConnectI.com>`

```

dta··.@con··i.com () wrote:

› I am in serious need of some help in converting parameter input data
› from text format to COMP-2, floating point decimal.  
…[6 more quoted lines elided]…
› 05 CALCULATE-FIELD COMP-2.
snip
You are confusing edited data 9(?).9(?) with scientific notation.

If you use a recent compiler you must used an intrinsic function
to automatically PARSE the ALPHANUMERIC data which results in a
NUMERIC field.

Or you can scan and count the relative position of the "." and then
parse the number and put the pieces back together.

It all depends on what you have to work with.

What compiler are you using (and what version).

JR


and stir with a Runcible spoon...
```

#### ↳ Re: COMP-2, Floating Point Help needed!!

- **From:** "charles f hankel" <ua-author-1885209@usenetarchives.gap>
- **Date:** 1997-08-14T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6cc0cea817-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5sqvug$es7$1@venus.ConnectI.com>`
- **References:** `<5sqvug$es7$1@venus.ConnectI.com>`

```

dta··.@con··i.com wrote:
› 
› I am in serious need of some help in converting parameter input data
…[10 more quoted lines elided]…
› field contained an invalid character.


Hello, dt

I am a little unclear about your motive. Are you getting an input field
that could have a decimal point in any position or not at all; or do you
have a fixed location for the decimal point on your input; or are you
getting a field that is expressed in floating point notation such as
5.23E100?

If it's the first, you can parse your input for the decimal point and,
once its location is determined, move the other digits to a workfield
and then into your floating point area. This is a bit old-fashioned and
long-winded, but it works.
Or you can use STRING/UNSTRING.

If it's the last, I don't know. If it's the middle one, then move each
part of the number to a work field and then move the workfield into the
COMP-2 field.

I must admit that I'm answering this from a position of comparative
weakness because I have only used floating-point in two COBOL programs
and that was about twenty years ago, to store an actuarial index as an
extended double-precision fp item. It's not usually acceptable in
business applications to use floating point because of its inherent
inaccuracy.

=====================================================
Thus writes the virtual quill pen of Charles F Hankel
Dat veniam corvis, vexat censura columbas - Juvenal
=====================================================
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
