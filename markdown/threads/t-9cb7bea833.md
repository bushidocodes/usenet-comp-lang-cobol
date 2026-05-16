[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

_35 messages · 11 participants · 2003-09 → 2003-10_

---

### The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-26T14:42:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl24r10a9o@enews1.newsguy.com>`

```
Steve Thompson mention the "Indian Problem" -- How much would
12.00 be today if it was put in the bank in 1626, when
Manhattan was purchased?

Benchmarking this simple logic likely proves nothing, but it is
yield some interesting results:

mpb Visual COBOL 3.6.0.8
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31674824.8227
  Elapsed:               52850

Borland Delphi 5.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677245.6417
  Elapsed:                1783

Microsoft Visual Basic 6.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677245.6417
  Elapsed:                3505

I'll post the code if anyone is interested.
```

#### ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-26T15:46:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl28if0ji6@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com>`

```
Here's another one:

Microsoft C#.net 1.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677446.1774
  Year:                  13830

The difference in resultant principle is pretty interesting.

31674824.8227 (mbp COBOL)
31677245.6417 (VB)
31677245.6417 (Delphi)
31677446.1774 (C#)

A tentative explanation:

mbp COBOL -- truncates digits beyond those defined in the PIC.
(Is that right?)

VB, Delphi -- rounds digits beyond the 4th digit after the
decimal (Currency types are 64-bit integers with a presumed
numeric scale of 4.)

C#.net -- I used the "decimal" type which a 128-bit integer
scale by 10, but it keeps more digits past the decimal point
than 1.  It has a precision of about 28, but it's unclear to me
how it determines numeric scale.  It coerces to and from
integer types implicitly, so it's apparently not a floating
point type.
```

##### ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** Howard Hess <hmhess1@yahoo.com>
- **Date:** 2003-09-28T04:17:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b2ocnvo4n8nttt96n70jc5c0ujivpca511@4ax.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com>`

```
On Fri, 26 Sep 2003 15:46:06 -0500, "Grinder"
<grinder@no.spam.maam.com> wrote:

>Here's another one:
>
…[33 more quoted lines elided]…
>
FWIW, here's a REXX program and its result to a ridiculous number of
decimal places.

/* REXX */
Numeric digits 1000
Amount = 12
Rate = 1.04
do i = 1627 to 2003
   Amount = Amount * Rate
end
say Amount
exit


31677446.1774342288922841877664856146636484384464847468309094416987301114925357384612428149183625963293479201550634284472249750735808412628650705475158690203814462404683557797805693987206823775116898183839905392551153457097454200720367653556557064869642326979656270511650099450147867841847415280620933593132886827337636885351553546741269778099970476529040421927405325721582091424222372237861744291729069212226681520912808443470347973664564044851169935356098322720814579888592047410210202662634148948118449792137270703240033533478265344867300315542846323621365165553736603328583667592468117238679618745123741998409905573621028702253453767915783981167254513088709436544314033090449023037421491594431500146233751465587831408587481640660182758741882166821096372830208
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T04:02:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl682b028ec@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <b2ocnvo4n8nttt96n70jc5c0ujivpca511@4ax.com>`

```
> FWIW, here's a REXX program and its result to a ridiculous
number of
> decimal places.
>
…[11 more quoted lines elided]…
>
31677446.177434228892284187766485614663648438446484746830909441
698730111492535738461242814918362596329347920155063428447224975
073580841262865070547515869020381446240468355779780569398720682
377511689818383990539255115345709745420072036765355655706486964
232697965627051165009945014786784184741528062093359313288682733
763688535155354674126977809997047652904042192740532572158209142
422237223786174429172906921222668152091280844347034797366456404
485116993535609832272081457988859204741021020266263414894811844
979213727070324003353347826534486730031554284632362136516555373
660332858366759246811723867961874512374199840990557362102870225
345376791578398116725451308870943654431403309044902303742149159
443150014623375146558783140858748164066018275874188216682109637
2830208

Thanks, I'll take the opportunity to install a REXX
interpreter/compiler? and get a timing to compare with the
others.
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T17:26:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl7n6901nlr@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <b2ocnvo4n8nttt96n70jc5c0ujivpca511@4ax.com>`

```
I added to you code in an attempt to match the other
implementation -- it's attached at the end.  I hope I haven't
introduced any idiocy in the process.

Here's some output:

Regina REXX 3.2
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677446.1785
  Elapsed (ms):          75000 +/- 1000

From what I've learned of REXX in the last 10 seconds, it
appears to be doing string-based long arithmetic.  This is
reasonable given its goals, but that and probably the
interpretation, adds a lot to the elapsed time.  In particular,
using "12.00" and "0.04" for principle and rate respectively,
takes off about 10 seconds.

I see there are ways to store numerics as binaries, so I'll
investigate that.  Also, there's probably some way to compile
REXX.

_____________

/* REXX */
Numeric digits 12

TestCount     = 100000
InitPrinciple = 12.0000
InitYear      = 1626
Rate          = 0.0400

Multiplier    = 1 + Rate
ThisYear      = 2003

say
say "Regina REXX 3.2"
say "  Test Count:          " TestCount
say "Init -------------------------"
say "  Year:                  " InitYear
say "  Principle:          " InitPrinciple
say "  Rate:                " Rate

/* start the clock */
/* Any ideas on how to get fractional seconds? */
Elapsed = DATE("T")

do Test = 1 to TestCount
  Principle = InitPrinciple
  do Year = InitYear to ThisYear - 1
    Principle = Principle * Multiplier
  end
end

/* stop the clock */
/* Any ideas on how to get fractional seconds? */
Elapsed = 1000 * (DATE("T") - Elapsed)

say "Results ----------------------"
say "  Principle:    " Principle
say "  Elapsed (ms):         " Elapsed "+/- 1000"

exit
```

##### ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** Alfred Cleve <alfred.cleve@t-online.de>
- **Date:** 2003-09-28T12:40:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl6dec$fvg$05$1@news.t-online.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com>`

```
Hello Grinder,

> The difference in resultant principle is pretty interesting.
> 
…[3 more quoted lines elided]…
> 31677446.1774 (C#)

there are nice differents... i coded the problem with tiny-cobol and my 
result is 31677446,1747764224

The working-variable of Amount was pic 9(8)v9(10).

Have fun !
Alfred
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T15:46:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl7hc3013mr@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <bl6dec$fvg$05$1@news.t-online.com>`

```

"Alfred Cleve" <alfred.cleve@t-online.de> wrote in message
news:bl6dec$fvg$05$1@news.t-online.com...
> Hello Grinder,
>
> > The difference in resultant principle is pretty
interesting.
> >
> > 31674824.8227 (mbp COBOL)
…[4 more quoted lines elided]…
> there are nice differents... i coded the problem with
tiny-cobol and my
> result is 31677446,1747764224
>
> The working-variable of Amount was pic 9(8)v9(10).

If you have it -- Can I have a Win32 executable to get a
comparative time test?
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

_(reply depth: 4)_

- **From:** Alfred Cleve <alfred.cleve@t-online.de>
- **Date:** 2003-09-28T23:26:37+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl7j9j$4gf$07$1@news.t-online.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <bl6dec$fvg$05$1@news.t-online.com> <bl7hc3013mr@enews1.newsguy.com>`

```
Hi,

> If you have it -- Can I have a Win32 executable to get a
> comparative time test?

i will ask in the mailing-list of tinycobol, if anybody can build a 
win32-executable for you. My system is Linux... :-)

have fun !
Alfred
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

_(reply depth: 5)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T17:27:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl7n8601nsc@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <bl6dec$fvg$05$1@news.t-online.com> <bl7hc3013mr@enews1.newsguy.com> <bl7j9j$4gf$07$1@news.t-online.com>`

```

"Alfred Cleve" <alfred.cleve@t-online.de> wrote in message
news:bl7j9j$4gf$07$1@news.t-online.com...
> Hi,
>
…[3 more quoted lines elided]…
> i will ask in the mailing-list of tinycobol, if anybody can
build a
> win32-executable for you. My system is Linux... :-)
>
> have fun !
> Alfred

Thanks and I am.
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

_(reply depth: 4)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-28T18:56:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1HJdb.1117$op2.142741@news20.bellglobal.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <bl6dec$fvg$05$1@news.t-online.com> <bl7hc3013mr@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:bl7hc3013mr@enews1.newsguy.com...
>
> "Alfred Cleve" <alfred.cleve@t-online.de> wrote in message
…[19 more quoted lines elided]…
>
It would be interesting to see if how a cobol program that gave the correct
answer using bussiness rules, and how fast the other languages gave the
correct answer each benchmarked.  To find out, just change your picture
clause to 9(8)v9(2) rounded. That will give the correct answer.  Then adjust
the other routines to fit.

To check the answers and debug, just print a balance sheet for each year.
Three or four columns will do. It is only going to be a dozen pages long,
and you can compare the entire thing in each of the languages as a test.

Progressive errors should be very easy to spot.

Donald
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

_(reply depth: 5)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T20:20:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl81d702glv@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <bl6dec$fvg$05$1@news.t-online.com> <bl7hc3013mr@enews1.newsguy.com> <1HJdb.1117$op2.142741@news20.bellglobal.com>`

```
> It would be interesting to see if how a cobol program that
gave the correct
> answer using bussiness rules, and how fast the other
languages gave the
> correct answer each benchmarked.  To find out, just change
your picture
> clause to 9(8)v9(2) rounded. That will give the correct
answer.  Then adjust
> the other routines to fit.

The ROUNDED clause go on to the MULTIPLY statement?
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

_(reply depth: 6)_

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-09-29T08:50:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LUVdb.1812$op2.274167@news20.bellglobal.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com> <bl6dec$fvg$05$1@news.t-online.com> <bl7hc3013mr@enews1.newsguy.com> <1HJdb.1117$op2.142741@news20.bellglobal.com> <bl81d702glv@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:bl81d702glv@enews1.newsguy.com...
> > It would be interesting to see if how a cobol program that
> gave the correct
…[9 more quoted lines elided]…
>

Yes.

Donald


>
```

##### ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-09-28T21:01:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0309281924.74ebb968@posting.google.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl28if0ji6@enews1.newsguy.com>`

```
Can you email me (thane at softwaresimple.com - not to the address I
am posting from) your source?


"Grinder" <grinder@no.spam.maam.com> wrote in message news:<bl28if0ji6@enews1.newsguy.com>...
> Here's another one:
> 
…[31 more quoted lines elided]…
> point type.
```

##### ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-10-04T21:08:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031004170810.15309.00000218@mb-m23.aol.com>`
- **References:** `<bl28if0ji6@enews1.newsguy.com>`

```

A number of posts back in time ...

 "Grinder" grinder@no.spam.maam.com 
Date: 9/26/03 3:46 PM EST
Message-id: <bl28if0ji6@enews1.newsguy.com>


posted what were then preliminary results from
a comparison test across a number of languages. In a portion of the post
commenting ...

(snips)
<<
C#.net -- I used the "decimal" type which a 128-bit integer
scale by 10, but it keeps more digits past the decimal point
than 1.  It has a precision of about 28, but it's unclear to me
how it determines numeric scale.  It coerces to and from
integer types implicitly, so it's apparently not a floating
point type.
>>

There is some guidance at

http://www2.hursley.ibm.com/decimal/

"General Decimal Arithmetic"

and at
http://www2.hursley.ibm.com/decimal/decarith.html

"General Decimal Arithmetic 
Specification 
Version 1.37 – 2 Oct 2003 "

This is front line action and material there is subject to change. But you can
get a sense of what the C# decimal type is albout. 

And according to the vocabulary newly established, you _are_ dealing with
floating point ...

(from the cited page)

"IEEE 854 and the earlier IEEE 754 (Binary Floating-Point) 
standards are being merged in the ongoing IEEE 754 revision 
which is expected to become the new IEEE 754 Standard for 
Floating-Point Arithmetic in due course. The current draft 
includes decimal floating-point formats (as described above) 
and arithmetic on those formats (also described above) "

So we are learning the term "decimal floating-point".

That site has a lot of interesting stuff including test cases and lots of
downloadable documentation.

Apropo one of my meager posts in this thread consider these new vocabulary
words

round-down 
round-half-up 
round-half-even 
round-ceiling 
round-floor 
round-half-down 
round-up 

Got that? Now, ... which shell is it under?

Perhaps as major business apps are taken onto the more economical platforms the
decimal will be decimal floating-point and not binary coded decimal. 

Conversion project anyone? Stated more bluntly we will need competent
programmers to get the data into these encoding devices, and right now the
field is wide open!

I have seen some discussions of the Strawman style of decimal storage that
allow for, and I mean this literally, a billion decimal places if you need it.
Sounds just like COBOL to me. Get your keyboards warmed up.

Seriously, in addition to a very special and useful encoding, some variations
are permitting a field level extensibility.  Keep in mind all subject to change
before it arrives at your local Walmart. But this new stuff has pizzaz AND
manages numbers the way humans do!

The Valkids might grow up any day now.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ New decimal types was Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-10-14T21:16:14-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F8C91CE.5895EA8C@istar.ca>`
- **References:** `<bl28if0ji6@enews1.newsguy.com> <20031004170810.15309.00000218@mb-m23.aol.com>`

```
My comments are triggered by the posting below on the proposed new
decimal data types.  I strongly urge all regulars on this list to go to
www2.hursley.ibm.com/decimal/ and read the various pages at that site. 
Pay special attention to the proposed decimal floating point.  In order
to get the most accuracy, the proposal is to encode 0 - 999 into 10 bits
so that all numbers would be composed of the number part in groups of 10
bits and the exponent would be in binary (I forget the formal terms for
the parts of the floating point number).  While I agree with almost
everything else at the site, my belief is that saving bits in this day
and age is not worth the complexity.  On the other hand if this is only
for the floating point decimal it may be moot.  It will depend on how
much conversion to and from display mode (with or without editing)
relative to arithmetic operations and whether the fixed point arithmetic
would also use the special encoding.  I can see the display form of the
numbers being carried in Unicode (16 bit characters) where the circuitry
does the arithmetic ignoring all but 4 bits of each character. 
Currently the only hardware decimal arithmetic left on any computer in
general business use seems to be that on the z series and that is only
fixed point with not enough precision to handle multiplication and
division for the new COBOL standard (and IBM extensions to the 85
standard) with single instructions as opposed to a multi-precision
routine.  Given the floating point proposals and the Java proposals, I
think that changes are coming and since this has been in the works for
over 2 years, IEEE may be close to a decision.  Note the creator of the
site, Mike Cowlishaw is the inventor of the Rexx language (Regina is the
implementation in Linux) among other achievements and is an IBM
Fellow.   

RKRayhawk wrote:
> 
> A number of posts back in time ...
…[85 more quoted lines elided]…
> RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: New decimal types was Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-10-15T03:24:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<763jb.1462$7a4.394@newsread4.news.pas.earthlink.net>`
- **References:** `<bl28if0ji6@enews1.newsguy.com> <20031004170810.15309.00000218@mb-m23.aol.com> <3F8C91CE.5895EA8C@istar.ca>`

```
Actually, this sounds remarkably similar to (but not quite identical) to the
"Standard Intermediate Data Item" *required* by the 2002 ISO COBOL Standard.
The following information gives you an idea of what that is:

"8.8.1.3 Standard arithmetic

Standard arithmetic is a standard method of evaluating an arithmetic
expression, an arithmetic statement, the SUM clause, and certain integer and
numeric functions as specified in 15.3.1, Numeric and integer functions. The
rules for standard arithmetic are defined in 8.8.1.3.1, Standard
intermediate data item through 8.8.1.3.8, Unary minus.

Standard arithmetic is in effect when the ARITHMETIC IS STANDARD clause is
specified in the OPTIONS paragraph. When a data item described with a usage
of binary-char, binary-short, binary-long, binary-double, floatshort,
float-long, or float-extended is an operand in an arithmetic expression, an
arithmetic statement, the SUM clause, or certain integer and numeric
functions, the techniques used shall be those specified for native
arithmetic.

When standard arithmetic has been specified or implied for the source unit
and the FLAG-NATIVE-ARITHMETIC directive is enabled, any arithmetic
operation that uses native arithmetic shall be flagged.

8.8.1.3.1 Standard intermediate data item

A standard intermediate data item is of the class numeric and the category
numeric. It is the unique value zero or an abstract, signed, normalized
decimal floating-point temporary data item. The internal representation
shall be defined by the implementor. Implementors may use whatever method or
methods they wish as long as the results conform to the rules for standard
intermediate data items.

NOTE The internal representation of a standard intermediate data item is
permitted to vary so that implementors can choose the most efficient
implementation for the circumstances.

When standard arithmetic is in effect the following rules apply:

1) Any operand of an arithmetic expression that is not already contained in
a standard intermediate data item shall be converted into a standard
intermediate data item.

NOTE This rule covers such cases as an arithmetic expression that contains
only one operand and no operator. For
example, IF (A = 1) and COMPUTE A = B.

2) The size error condition is raised and the EC-SIZE-OVERFLOW or
EC-SIZE-UNDERFLOW exception condition is
set to exist if the value is too large or too small, respectively, to be
contained in a standard intermediate data item. (See 14.6.4, SIZE ERROR
phrase and size error condition.)

NOTE Underflow is treated as a SIZE ERROR and is not rounded to zero.

8.8.1.3.1.1 Precision and allowable magnitude

A standard intermediate data item has the unique value of zero or a value
whose magnitude is in the range of
    10-999 (1.000 000 000 000 000 000 000 000 000 000 0E-999)
        through
    101000 - 10968 (9.999 999 999 999 999 999 999 999 999 999 9E+999)

inclusive, with a precision of 32 decimal digits. A standard intermediate
data item shall be truncated or rounded to fewer than 32 digits only as
explicitly specified.

8.8.1.3.1.2 Normalized values

When the value of a standard intermediate data item is not zero, the
significand shall contain exactly one non-zero digit to the left of the
decimal point.

8.8.1.3.1.3 Rounding rules

A standard intermediate data item shall be rounded to 31 digits in the
situations listed below and the rounding shall occur as described for the
ROUNDED phrase.

1) When a standard intermediate data item is compared except when the
comparison is among the arguments of an intrinsic function, in which case it
shall not be rounded and all 32 digits shall be used.

2) When a standard intermediate data item is the argument of a function and
there is no equivalent arithmetic expression defined for the rules of the
function, unless otherwise specified in the rules for a function or unless
situation 1, above, applies.

3) When a standard intermediate data item is being moved to a
resultant-identifier for which the ROUNDED phrase has not been specified.
Rounding of a standard intermediate data item may cause the size error
condition to be raised or the EC-SIZE-OVERFLOW exception condition to exist.

NOTE These rules are intended to eliminate excessive rounding and to ensure
that rounding occurs once at the end of the evaluation of nested arithmetic
expressions.

When a standard intermediate data item is being moved to a
resultant-identifier for which the ROUNDED phrase is specified, the number
of digits to which rounding occurs is as specified in 14.6.3, ROUNDED
phrase. ..."
```

#### ↳ Sleightly improved mbp Visual COBOL results

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-26T21:39:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl2t8r022c0@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com>`

```
mbp Visual COBOL 3.6.0.8
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31674824.8227
  Elapsed:               36610
  Time Zero:  200309262133579500000
  Time Final: 200309262134345600000

Microsoft C#.net 1.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677446.1774
  Year:                  13629

Microsoft Visual Basic 6.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677245.6417
  Elapsed:                3508

Borland Delphi 5.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677245.6417
  Elapsed:                1772

____

I guess I'll start going through whatever orphaned
compilers/interpreters are lying around...
```

##### ↳ ↳ Re: Sleightly improved mbp Visual COBOL results

- **From:** Harald.Cordes@microfocus.com (Harald Cordes)
- **Date:** 2003-10-09T09:07:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1fabdc0d.0310090807.30a14928@posting.google.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl2t8r022c0@enews1.newsguy.com>`

```
Try
   01  WS-MULTIPLIER  comp-2   VALUE ZEROS.
   01  WS-PRINCIPLE   comp-2   VALUE ZEROS.

compile it as
VISCOB32 manhattan.cob /FLOAT

---------------

The default for COMP-2 in mbp Visual COBOL has a 20 bytes unpacked
decimal mantissa, a display sign and a one byte exponent.

With /FLOAT you can switch it to a 64bit float with at least 16 digits
precission.
With /XFLOAT you can switch it to a 80bit float with at least 19
digits precission.

---------------

Your original code contains:
01  WS-MULTIPLIER            PIC 9V9999        VALUE ZEROS.
01  WS-PRINCIPLE             PIC 9(12)V9999    VALUE ZEROS.

improved to
01  WS-MULTIPLIER    comp    PIC 9V9999        VALUE ZEROS.
01  WS-PRINCIPLE     comp    PIC 9(12)V9999    VALUE ZEROS.

the statement
MULTIPLY WS-MULTIPLIER BY WS-PRINCIPLE.

results in an intermediate result like 9(13)V9(8).
The scaling move of the ...V9(8) to ...V9(4) causes the performance
gap.

If performance is very important for an mbp Visual COBOL program,
please try to avoid scaling moves on binary values. Also the multiply
from the original coding result in binary intermediate values.
```

##### ↳ ↳ Re: Sleightly improved mbp Visual COBOL results

- **From:** David Essex <dessex@nobloodyspam.nospam.net>
- **Date:** 2003-10-10T00:38:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lMqhb.23852$lz5.2870@nntp-post.primus.ca>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl2t8r022c0@enews1.newsguy.com>`

```
Grinder wrote:

  > I guess I'll start going through whatever orphaned
  > compilers/interpreters are lying around...

It would be interesting to try some of the open source COBOL compilers
such as TinyCOBOL, OpenCOBOL, to see how the compare.
```

#### ↳ Re: New Comparison

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T17:34:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl7nll01omi@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com>`

```
Summarized:

Environment                    Principle    Elapsed
Regina REXX 3.2              31677446.1785   75000
mbp Visual COBOL 3.6.0.8     31674824.8227   36520
Microsoft C#.net 1.0         31677446.1774   13589
Microsoft Visual Basic 6.0   31677245.6417    3504
Borland Delphi 5.0           31677245.6417    1773

Run report:

Interpreted ==================

Regina REXX 3.2
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677446.1785
  Elapsed (ms):          75000 +/- 1000

Compiled =====================

mbp Visual COBOL 3.6.0.8
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31674824.8227
  Elapsed (ms):          36520

Microsoft C#.net 1.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677446.1774
  Elapsed (ms):          13589

Microsoft Visual Basic 6.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677245.6417
  Elapsed (ms):           3504

Borland Delphi 5.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:           12.0000
  Rate:                 0.0400
Results ----------------------
  Principle:     31677245.6417
  Elapsed (ms):           1773
```

#### ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T21:34:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl85od02pj3@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com>`

```
I've taken Donald Tees' advice, and now the resultant principle
values are in agreement.  This generally increased computation
time, but that has been offset by cutting the size of the local
variables -- slightly for REXX and COBOL, but significantly for
the others.

REXX gets pounded by the 40 million rounding operations it must
now make, but that may be because I don't know the optimal
path -- are there any rexxperts who can assist?  (That code
posted as a reply to this note.)

Summary:

Compiler/Interpreter          Principle    Elapsed
--------------------------   -----------   -------
Regina REXX 3.2              31658845.52    164000
mbp Visual COBOL 3.6.0.8     31658845.52     46380
Borland Delphi 5.0           31658845.52      3846
Microsoft C#.net 1.0         31658845.52      3615
Microsoft Visual Basic 6.0   31658845.52      2534

Run report:

Compiled =====================

Borland Delphi 5.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31658845.52
  Elapsed (ms):           3846

mbp Visual COBOL 3.6.0.8
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31658845.52
  Elapsed (ms):          46380

Microsoft C#.net 1.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31658845.52
  Elapsed (ms):           3615

Microsoft Visual Basic 6.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31658845.52
  Elapsed (ms):           2534

Interpreted ==================

Regina REXX 3.2
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31658845.52
  Elapsed (ms):         164000 +/- 1000
```

##### ↳ ↳ Latest REXX code

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-28T21:45:17-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl86bu02qc7@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl85od02pj3@enews1.newsguy.com>`

```
/* REXX */
Numeric digits 12

TestCount     = 100000
InitPrinciple = 12.00
InitYear      = 1626
Rate          = 0.04

Multiplier    = 1 + Rate
ThisYear      = 2003

say
say "Regina REXX 3.2"
say "  Test Count:        " FORMAT(TestCount, 8, 0)
say "Init -------------------------"
say "  Year:                  " FORMAT(InitYear, 4, 0)
say "  Principle:  " FORMAT(InitPrinciple, 12, 2)
say "  Rate:                " FORMAT(Rate, 3, 2)

/* start the clock */
/* Any ideas on how to get fractional seconds? */
Elapsed = DATE("T")

do Test = 1 to TestCount
  Principle = InitPrinciple
  do Year = InitYear to ThisYear - 1
    Principle = FORMAT(Principle * Multiplier, , 2)
  end
end

/* stop the clock */
/* Any ideas on how to get fractional seconds? */
Elapsed = 1000 * (DATE("T") - Elapsed)

say "Results ----------------------"
say "  Principle:  " FORMAT(Principle, 12, 2)
say "  Elapsed (ms):        " FORMAT(Elapsed, 6) "+/- 1000"


exit
```

##### ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-09-29T05:13:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qcPdb.7546$RW4.2514@newsread4.news.pas.earthlink.net>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl85od02pj3@enews1.newsguy.com>`

```
Do you have a compiler with a full set of COBOL '89 Intrinsic Functions?  If
so, I know it wouldn't be a "fair" test of the compiler (itself), but I
would be interested in the RESULTS obtained using the FUNCTION Annuity
feature (if that is the right function).
```

###### ↳ ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-29T13:28:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bl9tl101398@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bl85od02pj3@enews1.newsguy.com> <qcPdb.7546$RW4.2514@newsread4.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:qcPdb.7546$RW4.2514@newsread4.news.pas.earthlink.net...
> Do you have a compiler with a full set of COBOL '89 Intrinsic
Functions?  If
> so, I know it wouldn't be a "fair" test of the compiler
(itself), but I
> would be interested in the RESULTS obtained using the
FUNCTION Annuity
> feature (if that is the right function).

If you show me where and how it should be applied, I'll run it
through a compile and test.  Here's the current COBOL code:

       IDENTIFICATION DIVISION.
       PROGRAM-ID. MANHAT.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
      * Arguments
       01  WS-TEST-COUNT            PIC 9(7)      COMP VALUE
100000.
       01  WS-INIT-YEAR             PIC 9999      COMP VALUE
1626.
       01  WS-INIT-PRINCIPLE        PIC 9(8)v9(2)      VALUE
12.00.
       01  WS-INTEREST-RATE         PIC 9v9(2)    COMP VALUE
0.04.
      * Computed initial conditions
       01  WS-MULTIPLIER            PIC 9v9(2)    COMP VALUE
ZEROS.
      * State variables
       01  WS-TEST                  PIC 9(7)      COMP VALUE
ZEROS.
       01  WS-PRINCIPLE             PIC 9(8)v9(2) COMP VALUE
ZEROS.
       01  WS-YEAR                  PIC 9(4)      COMP VALUE
ZEROS.
      * Statistics
       01  WS-ZERO-DATETIME.
           05  WS-ZERO-YEAR         PIC 9(4)      VALUE ZEROS.
           05  WS-ZERO-MONTH        PIC 99        VALUE ZEROS.
           05  WS-ZERO-DAY          PIC 99        VALUE ZEROS.
           05  WS-ZERO-HOUR         PIC 99        VALUE ZEROS.
           05  WS-ZERO-MINUTE       PIC 99        VALUE ZEROS.
           05  WS-ZERO-SECOND       PIC 99        VALUE ZEROS.
           05  WS-ZERO-HS           PIC 99        VALUE ZEROS.
           05  WS-ZERO-ZONE         PIC XXXXX.
       01  WS-FINAL-DATETIME.
           05  WS-FINAL-YEAR        PIC 9(4)      VALUE ZEROS.
           05  WS-FINAL-MONTH       PIC 99        VALUE ZEROS.
           05  WS-FINAL-DAY         PIC 99        VALUE ZEROS.
           05  WS-FINAL-HOUR        PIC 99        VALUE ZEROS.
           05  WS-FINAL-MINUTE      PIC 99        VALUE ZEROS.
           05  WS-FINAL-SECOND      PIC 99        VALUE ZEROS.
           05  WS-FINAL-HS          PIC 99        VALUE ZEROS.
           05  WS-FINAL-ZONE        PIC XXXXX.
       01  WS-ELAPSED               PIC S9(9)     VALUE ZEROS.
      * Scratch variables
       01  WS-TIME-DIFF             PIC S9(9)     VALUE ZEROS.
       01  WS-SOME-DATE             PIC 9(8)      .

       PROCEDURE DIVISION.

       MAIN.

      * Compute some initial conditions
           ADD 1.0 TO WS-INTEREST-RATE GIVING WS-MULTIPLIER.

      * Output initial conditions
           DISPLAY " ".
           DISPLAY "mbp Visual COBOL 3.6.0.8".
           DISPLAY "  Test Count:          " WS-TEST-COUNT.
           DISPLAY "Init -------------------------".
           DISPLAY "  Year:                   " WS-INIT-YEAR.
           DISPLAY "  Principle:       "
WS-INIT-PRINCIPLE.
           DISPLAY "  Rate:                   "
WS-INTEREST-RATE.

      * Start the clock
           MOVE FUNCTION CURRENT-DATE TO WS-ZERO-DATETIME.

           PERFORM ITERATE-TEST
               VARYING WS-TEST FROM 1 BY 1
               UNTIL WS-TEST > WS-TEST-COUNT.

      * Stop the clock
           MOVE FUNCTION CURRENT-DATE TO WS-FINAL-DATETIME.
           PERFORM COMPUTE-ELAPSED.

      * Kick results
           DISPLAY "Results ----------------------".
           DISPLAY "  Principle:       "      WS-PRINCIPLE.
           DISPLAY "  Elapsed (ms):      "      WS-ELAPSED.
      *    DISPLAY "  Time Zero:  " WS-ZERO-DATETIME.
      *    DISPLAY "  Time Final: " WS-FINAL-DATETIME.

           STOP RUN.

       ITERATE-TEST.
      * Run a test
           MOVE WS-INIT-PRINCIPLE TO WS-PRINCIPLE.
           PERFORM COMPOUND-INTEREST
               VARYING WS-YEAR FROM WS-INIT-YEAR BY 1
               UNTIL WS-YEAR >= WS-ZERO-YEAR.

       COMPOUND-INTEREST.
           MULTIPLY WS-MULTIPLIER BY WS-PRINCIPLE ROUNDED.

       COMPUTE-ELAPSED.
      * Determine elapsed time (in milliseconds)
           MOVE ZEROS TO WS-ELAPSED.

           MOVE WS-FINAL-DATETIME(1:8) TO WS-SOME-DATE.
           MOVE FUNCTION INTEGER-OF-DATE(WS-SOME-DATE)
               TO WS-ELAPSED.

           MOVE WS-ZERO-DATETIME(1:8) TO WS-SOME-DATE.
           MOVE FUNCTION INTEGER-OF-DATE(WS-SOME-DATE)
               TO WS-TIME-DIFF.
           SUBTRACT WS-TIME-DIFF FROM WS-ELAPSED.
           MULTIPLY 86400000 BY WS-ELAPSED.

           SUBTRACT WS-ZERO-HOUR FROM WS-FINAL-HOUR
               GIVING WS-TIME-DIFF.
           MULTIPLY 3600000 BY WS-TIME-DIFF.
           ADD WS-TIME-DIFF TO WS-ELAPSED.

           SUBTRACT WS-ZERO-MINUTE FROM WS-FINAL-MINUTE
               GIVING WS-TIME-DIFF.
           MULTIPLY 60000 BY WS-TIME-DIFF.
           ADD WS-TIME-DIFF TO WS-ELAPSED.

           SUBTRACT WS-ZERO-SECOND FROM WS-FINAL-SECOND
               GIVING WS-TIME-DIFF.
           MULTIPLY 1000 BY WS-TIME-DIFF.
           ADD WS-TIME-DIFF TO WS-ELAPSED.

           SUBTRACT WS-ZERO-HS FROM WS-FINAL-HS
               GIVING WS-TIME-DIFF.
           MULTIPLY 10 BY WS-TIME-DIFF.
           ADD WS-TIME-DIFF TO WS-ELAPSED.

       END-OF-SOURCE.
```

#### ↳ Truncation (instead of Rounding) give mbp COBOL a boost

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-29T14:13:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bla09m01bvc@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com>`

```
Annual compounding of interest is a bit unrealistic, but which
method is more "correct" -- truncation or rounding?

Truncation saves the COBOL and REXX implementations quite a bit
of time:

Summary:

Compiler/Interpreter          Principle    Elapsed
--------------------------   -----------   -------
Borland Delphi 5.0           31362020.66      3726
mbp Visual COBOL 3.6.0.8     31362020.66     34470
Microsoft C#.net 1.0         31362020.66      4656
Microsoft Visual Basic 6.0   31362020.66      2352
Regina REXX 3.2              31362020.66    144000

Run report:

Compiled =====================

mbp Visual COBOL 3.6.0.8
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31362020.66
  Elapsed (ms):          34470

Microsoft C#.net 1.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31362020.66
  Elapsed (ms):           4656

Borland Delphi 5.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31362020.66
  Elapsed (ms):           3726

Microsoft Visual Basic 6.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31362020.66
  Elapsed (ms):           2352

Interpreted ==================

Regina REXX 3.2
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31362020.66
  Elapsed (ms):         144000 +/- 1000
```

##### ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-09-29T21:17:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qj1eb.23013$ev2.4462311@newssrv26.news.prodigy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bla09m01bvc@enews1.newsguy.com>`

```
"Grinder" <grinder@no.spam.maam.com> wrote in message
news:bla09m01bvc@enews1.newsguy.com...
> Annual compounding of interest is a bit unrealistic, but which
> method is more "correct" -- truncation or rounding?

If you are using COMP-2 (IEEE double) you're only good to 18 significant
decimal digits, and of course, some decimal values (e.g., 0.10 ) are
irrational numbers in binary anyway so as soon as you get an irrational
number, all the subsequent calculations will be off. (They will - no pun
intended - "compound").

So I think the answer is, "fielder's choice" but you can minimize the amount
of 'slop' by selecting your PICTURE and USAGE clauses carefully.


MCM
```

###### ↳ ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-29T16:40:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bla8s9021v3@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bla09m01bvc@enews1.newsguy.com> <qj1eb.23013$ev2.4462311@newssrv26.news.prodigy.com>`

```

"Michael Mattias" <michael.mattias@gte.net> wrote in message
news:qj1eb.23013$ev2.4462311@newssrv26.news.prodigy.com...
> "Grinder" <grinder@no.spam.maam.com> wrote in message
> news:bla09m01bvc@enews1.newsguy.com...
> > Annual compounding of interest is a bit unrealistic, but
which
> > method is more "correct" -- truncation or rounding?
>
> If you are using COMP-2 (IEEE double) you're only good to 18
significant
> decimal digits, and of course, some decimal values (e.g.,
0.10 ) are
> irrational numbers in binary anyway so as soon as you get an
irrational
> number, all the subsequent calculations will be off. (They
will - no pun
> intended - "compound").

Just incidentally, I'm using COMP.

> So I think the answer is, "fielder's choice" but you can
minimize the amount
> of 'slop' by selecting your PICTURE and USAGE clauses
carefully.

I meant more in terms of business rules.  The technical
implementation will have to achieve it, but if each operation
is rounded or truncated, and to how many digits, should be in
the specification.

For instance, truncation yields 31362020.66, while rounding
returns 31658845.52  -- I'd rather have the additional 300k$,
or conversely, not have to pay it out.
```

###### ↳ ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-09-30T09:48:41-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F797BA9.386F5D63@istar.ca>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bla09m01bvc@enews1.newsguy.com> <qj1eb.23013$ev2.4462311@newssrv26.news.prodigy.com>`

```
Michael Mattias wrote:
> 
> "Grinder" <grinder@no.spam.maam.com> wrote in message
…[8 more quoted lines elided]…
> intended - "compound").

While I agree with the general thrust of the previous statement, COMP-2
on the IBM 360/370/390/z series COBOLs is IBM hex floating point, not
IEEE.  I have proposed that IBM implement the new binary floating point
COBOL data types as IEEE and leave the current COMP-1 and COMP-2 as is. 
This would have the side benefit of allowing COBOL to convert between
forms on at least one series of boxes.
> 
> So I think the answer is, "fielder's choice" but you can minimize the amount
> of 'slop' by selecting your PICTURE and USAGE clauses carefully.
> 
> MCM
```

###### ↳ ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-09-30T13:24:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mufeb.23221$ev2.4636043@newssrv26.news.prodigy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bla09m01bvc@enews1.newsguy.com> <qj1eb.23013$ev2.4462311@newssrv26.news.prodigy.com> <3F797BA9.386F5D63@istar.ca>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3F797BA9.386F5D63@istar.ca...
> > If you are using COMP-2 (IEEE double) ....

>
> While I agree with the general thrust of the previous statement, COMP-2
…[4 more quoted lines elided]…
> forms on at least one series of boxes.

I thought you have a user install-time/run-time/compile-time option to
control the data format via the 'FLOAT(HEX)' (='FLOAT(NATIVE)') or
'FLOAT(IEEE)' options.

Not the kind of thing I'd recommend applications programmers tinker with a
whole lot if COMP-1 or COMP-2 are stored on disk or passed to other modules,
though... might get some other folks a bit bent out of shape (and rightly
so!)

MCM
```

##### ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-29T17:46:53-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blacou028ic@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com> <bla09m01bvc@enews1.newsguy.com>`

```
Here's another one:

Compiler/Interpreter          Principle    Elapsed
--------------------------   -----------   -------
Borland Delphi 5.0           31362020.66      3726
mbp Visual COBOL 3.6.0.8     31362020.66     34470
Microsoft C#.net 1.0         31362020.66      4656
Microsoft Visual Basic 6.0   31362020.66      2352
Microsoft Visual C++ 6.0     31362020.66      5338
Regina REXX 3.2              31362020.66    144000

Run report:

Microsoft Visual C++ 6.0
  Test Count:           100000
Init -------------------------
  Year:                   1626
  Principle:             12.00
  Rate:                   0.04
Results ----------------------
  Principle:       31362020.66
  Elapsed (ms):           5338
```

###### ↳ ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-30T00:58:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030929205800.16605.00000041@mb-m07.aol.com>`
- **References:** `<blacou028ic@enews1.newsguy.com>`

```


In your COBOL app you should be careful about 
WS-INTEREST-RATE 
with value 0.04. It cannot be represented in binary.

Nonetheless, In your COBOL app you should make 
WS-MULTIPLIER 
a floating point number. COBOL is not alergic 
to these.  Infact make it a big fat double precision 64-bit 
honker, this will tend to relieve you of round / truncate concerns.
Atleast with one possible interpretation of the business rules. See below.

You will have one of several concerns about truncation / rounding 
when you do 

   ADD 1.0 TO WS-INTEREST-RATE GIVING WS-MULTIPLIER.

That needs careful awareness.
You will need to know when it gets converted to float.

That should produce a value approximately 1.03999999.....


I would exploit inline performs for efficiency. So consider these
transformations

Original 

      * Run a test
           MOVE WS-INIT-PRINCIPLE TO WS-PRINCIPLE.
           PERFORM COMPOUND-INTEREST
               VARYING WS-YEAR FROM WS-INIT-YEAR BY 1
               UNTIL WS-YEAR >= WS-ZERO-YEAR.

       COMPOUND-INTEREST.
           MULTIPLY WS-MULTIPLIER BY WS-PRINCIPLE ROUNDED.

Inlined for efficiency

      * Run a test
           MOVE WS-INIT-PRINCIPLE TO WS-PRINCIPLE.
           PERFORM 
               VARYING WS-YEAR FROM WS-INIT-YEAR BY 1
               UNTIL WS-YEAR >= WS-ZERO-YEAR.
              MULTIPLY WS-MULTIPLIER BY WS-PRINCIPLE ROUNDED
   	      end-multiply  
           end-perform. 

This may take some branch overhead out of the loop.

But frankly the principle is a minor detail that can be held out
until the end.  This will create floating-point to floating-point
calcs in the inner loop 
and get you out of decimal conversion for the loop.
(In fact the extra precision needed to hold the growing 
principle is in the way of the need to hold onto precision
in the compounding interest factor).


create a floating-point WS-MULT-ACCUMULATOR
  
      * concentrate computing power on the essential factor

      * ? may want init of (relates to your WS-ZERO-YEAR design)
      **?  MOVE WS-MULTIPLIER to WS-MULT-ACCUMULATOR.
      * ? but perhaps best to do this 
           MOVE 1.0           to WS-MULT-ACCUMULATOR.

      * slight modification to you loop
           PERFORM 
               VARYING WS-YEAR FROM WS-INIT-YEAR BY 1
               UNTIL WS-YEAR >= WS-ZERO-YEAR.
      * note here, fields different and trunc occuring
      * but double precision bits are getting truncated off!
              MULTIPLY WS-MULTIPLIER BY WS-MULT-ACCUMULATOR
                GIVING WS-MULT-ACCUMULATOR
   	      end-multiply  
           end-perform. 
	
      * apply the accumulated effect of compounding to principle
      * only once.  Decimal convert only once. 
      * deal with round / trunc here as separate issue.	
           MOVE WS-INIT-PRINCIPLE TO WS-PRINCIPLE.
	   MULTIPLY WS-PRINCIPLE BY WS-MULT-ACCUMULATOR
	     GIVING WS-PRINCIPLE 
             ROUNDED
	   END-MULTIPLY.

(If you consider this you would have to do similar  work in the C# version if
you are using decimal there).

The technical business term is compouned interest. An algorithm
of the proposed style explicates the true phenomenon.

William M. Klein has intelligently suggested that you consider COBOL intrinsic
functions. Don't be surprised if those are _not_ actually executed 
in decimal, Seems like they ought to be done in float. 
For all I know with the modern compilers these may be overloaded
functions. The 
intrinsics will rob you of the power to control round / trunc
at intermediate stages.  It is really best to use them for the 
factors not the products.


Scond part. The Rounded / Truncated issue is really a business rule question. 
It may be the difference between 'interest rate' and 'APR - annual percentage
rate'. 

In some of your earlier posts you were striving to 
get the programs written in different languages
to be consistent. That may be the correct spec.
Your actual business purpose is to compare the 
technology.  Do the calc either way, as long as they produce identical results,
your basic approach is valid.


Bankers will truncate whenever they can. Social minded government operatives
might have a tendency to meet certain political objectives in 
there decisions.
So using English, I would recommend that 
 If this is a bank loan truncate. If this is a government action, like a
reparation, then round, but round up and round up always..

You indicate as follows
"Grinder" grinder@no.spam.maam.com 
Date: 9/29/03 4:40 PM EST
Message-id: <bla8s9021v3@enews1.newsguy.com>

<<
For instance, truncation yields 31362020.66, while rounding
returns 31658845.52  -- I'd rather have the additional 300k$,
or conversely, not have to pay it out.

>>

Your most recent published code is
     MULTIPLY WS-MULTIPLIER BY WS-PRINCIPLE ROUNDED.

and the most recent figure published is
31362020.66. All of which seems like a contradiction. But I think we can see
the thing
clearly. If you want to give the bond holder a dream deal, then round up
(ceiling), at each compound.  If you want to give them a middle ground sweat
deal, then round normal 50/50 at each compound. If you want to do them dirt
then trunc (floor) at each compound.

You must know what the bank rule or the government rule says, not what opinion
says.
And part of that is to know the number of decimal places at the time of posting
the compounding amount.

You are inventing the concept, so actually you have to decide.

For the sake of comparison of language facitilities, either way may be good
enough. Your real point here is the number of years! 
But if you are analogizing it to bank software
then you need to get it into decimal at each compounding, and chop it one way
or the other.

So my comments above relate to a possibly faster calculation. And allude to the
fact that if you find applicable COBOL intrinsic fucntions, 
you may find that they spin in float or even double, not decimal, and they take
the truncations / rounding decision out of your hands. So if you use intrinsics
you might have 
to force the other language manual code to match algorithmically.

Hope this is useful to you.
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-10-04T21:27:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031004172749.15309.00000219@mb-m23.aol.com>`
- **References:** `<blacou028ic@enews1.newsguy.com>`

```


There have been comments here to the effect that REXX / COBOL are getting
pounded on rounding. I am thinking these are two really different problems and
it seems useful to suggest that we identify them if we can.

There is mentiion of use of Regina REXX 3.2.
REXX is one of the forefronts of the new floating-point decimal. Is this
present in Regina REXX 3.2?  Are you engaging it?  

There has been mention of "REXX ridiculous number of digits." Actually if you
are using the new decimal, and espcially if your implementation is bleeding
edge, the decimal may even be getting extented (looked like more than 28
decimal digits in your annotation, for example).

We are dealling with new prinicples of coding and data storage management, and
I think it would be good to list out some details if you are willing.

If COBOL hits the new decimal floating point as it moves to the practically
priced platforms, then it will hit the growing number of digits as iterative
computations progress.  Without explicit controls it too is likely to keep
extending the precision. (In that new format).

Truncation for REXX probably obviated the need for extension (do see how I mean
this). Where as, truncation for COBOL probably both limitted processing on the
girth of a given intermediate and obviated the need for rounding (rounding is
shallow recurse across some subset of digits). 

Two different things are happening, and both relate to the ultimate future
COBOL: first truncation and second containment of automatic internal decimal
precision extension to retain accuracy. (I am new at this so pardon the crudity
of the vocabulary).

When you are mystified by the contents of C# decimal types, and chagrinned at
the length of REXX decimal results (intermediate or final) you are having an
encounter of the third kind with the inhabitants of the new business data
processing world. We will need to work with this world in COBOL.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: Truncation (instead of Rounding) give mbp COBOL a boost

_(reply depth: 4)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-10-04T17:51:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<blniu00203v@enews1.newsguy.com>`
- **References:** `<blacou028ic@enews1.newsguy.com> <20031004172749.15309.00000219@mb-m23.aol.com>`

```

"RKRayhawk" <rkrayhawk@aol.com> wrote in message
news:20031004172749.15309.00000219@mb-m23.aol.com...
>
>
> There have been comments here to the effect that REXX / COBOL
are getting
> pounded on rounding. I am thinking these are two really
different problems and
> it seems useful to suggest that we identify them if we can.
>
> There is mentiion of use of Regina REXX 3.2.
> REXX is one of the forefronts of the new floating-point
decimal. Is this
> present in Regina REXX 3.2?  Are you engaging it?

No.  I'm am fixing the number of digits to a relatively small
number, though.

> There has been mention of "REXX ridiculous number of digits."
Actually if you
> are using the new decimal, and espcially if your
implementation is bleeding
> edge, the decimal may even be getting extented (looked like
more than 28
> decimal digits in your annotation, for example).
>
> We are dealling with new prinicples of coding and data
storage management, and
> I think it would be good to list out some details if you are
willing.
>
> If COBOL hits the new decimal floating point as it moves to
the practically
> priced platforms, then it will hit the growing number of
digits as iterative
> computations progress.  Without explicit controls it too is
likely to keep
> extending the precision. (In that new format).
>
> Truncation for REXX probably obviated the need for extension
(do see how I mean
> this). Where as, truncation for COBOL probably both limitted
processing on the
> girth of a given intermediate and obviated the need for
rounding (rounding is
> shallow recurse across some subset of digits).
>
> Two different things are happening, and both relate to the
ultimate future
> COBOL: first truncation and second containment of automatic
internal decimal
> precision extension to retain accuracy. (I am new at this so
pardon the crudity
> of the vocabulary).
>
> When you are mystified by the contents of C# decimal types,
and chagrinned at
> the length of REXX decimal results (intermediate or final)
you are having an
> encounter of the third kind with the inhabitants of the new
business data
> processing world. We will need to work with this world in
COBOL.

I was neither mystified nor chagrinned, but thanks for the
info.
```

#### ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2003-09-29T15:30:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bla4oo01n6p@enews1.newsguy.com>`
- **References:** `<bl24r10a9o@enews1.newsguy.com>`

```
I don't know if this link has already been posted, but here is
a language comparison on the net:
http://dada.perl.it/shootout/
```

##### ↳ ↳ Re: The Manhattan Benchmark (spin-off from Benchmark Java vs. COBOL)

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-09-30T09:41:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030930054116.00143.00000049@mb-m27.aol.com>`
- **References:** `<bla4oo01n6p@enews1.newsguy.com>`

```
Here is some fairly well commented C code, followed by a print of the result
with a few additional comments.

                
//
// grinder,  
//           
// Re: The Manhattan Benchmark
//
// I have thought more about your Manhattan Project
// and realized that your core loop is just a power function.
//
// I personally request that you publish the number of years
// in your loop (not just the start 'year'. An off by 1 error
// can be going on here.
                
// Here using Microsoft Visual C++ 1.52                
// Code generates "Bonanza (Non Truncating Algorithm using Inrinsic)"          
     
// this is the 'government calcs', as opposed to the 'banker calcs'.


// Author: Robert K. Rayhawk
// Illustration of 'efficient' Bonanza function
// Implicitly shows inflexibility of an intrinsic function
//   approach with naive interest rate, but shows it fast..
                
#include <stdlib.h>                
#include <stdio.h>                
#include <math.h>

/* declare functions */
void Manhattan_doubles();
void Manhattan_long_doubles();


                
int 	main( int argc, char *argv[ ], char *envp[ ] ) {          

char  InputLine[161];

  printf("64-bit IEEE 754  \n");
  Manhattan_doubles();      

  printf("\n");
  printf("Monsterous floats Calcs  \n");
	Manhattan_long_doubles();

  printf("\n");
  printf("Either precision involves miniscule binary truncation \n");

  printf("\n");
  printf("There are four possible algorithms (in order of increasing
result):\n");
  printf(" - trunc floor() each period \n");
  printf(" - round each period (50/50) \n");
  printf(" - continuous function (as RKR Bonanza here to illustrate efficiency)
\n");
  printf(" - round up ceil() each period (The Mega Bonanza) \n");

// notion of floor() ceil() meant advisedly 
// (multiply by 100, take such a function, then divide back)
// only
//  - continuous function. RKR Bonanza, shown here.


  scanf("%s", InputLine); // needed to keep screen for a moment
                          // must input non-blank line 	
	return 0;
}

 
void Manhattan_doubles() { /* function name with a certain ring to it */
double compounding_int = 1.04; 
double compounded_int  =  0.0;
double pinciple_orig   = 12.0;
double pinciple_result =  0.0;
int years_of_Dutch = 2003-1626;

double prev_published_result_t = 31362020.66; 
double prev_published_result_r = 31658845.52; 
double prev_published_result_c = 31677446.1774; 
                     
  compounded_int=pow(compounding_int,(double) years_of_Dutch);

  pinciple_result = pinciple_orig * compounded_int;

  printf("%23d Years \n",
               years_of_Dutch);
  printf("%23.2lf Compounding Interest Factor \n",
                  compounding_int);
  printf("%23.2lf Original Principle \n",
                  pinciple_orig);
  printf("%23.2lf RKR Bonanza (Non Truncating Algorithm using Inrinsic) \n",
                  pinciple_result);

  printf("                        Grinder's Previously Published Results:\n");
  printf("%23.2lf   stepwise truncation\n",
                    prev_published_result_t);    
  printf("%23.2lf   stepwise rounding\n",
                    prev_published_result_r);    
  printf("%25.4lf C# results discussed early on\n",
                    prev_published_result_c);    
                  
                  
                  
                  
}


void Manhattan_long_doubles() { /* for winter nights */
long double compounding_int = 1.04; 
long double compounded_int  =  0.0;
long double pinciple_orig   = 12.0;
long double pinciple_result =  0.0;
int years_of_Dutch = 2003-1626;

long double prev_published_result_t = 31362020.66; 
long double prev_published_result_r = 31658845.52; 
long double prev_published_result_c = 31677446.1774; 
                     
// note use of ..powl()
  compounded_int=powl(compounding_int,(long double) years_of_Dutch);

  pinciple_result = pinciple_orig * compounded_int;

  printf("%23d Years \n",
               years_of_Dutch);
  printf("%23.2Lf Compounding Interest Factor \n",
                  compounding_int);
  printf("%23.2Lf Original Principle \n",
                  pinciple_orig);
  printf("%23.2Lf RKR Bonanza (Non Truncating Algorithm using Inrinsic) \n",
                  pinciple_result);


  printf("                        Grinder's Previously Published Results:\n");
  printf("%23.2Lf   stepwise truncation\n",
                    prev_published_result_t);    
  printf("%23.2Lf   stepwise rounding\n",
                    prev_published_result_r);    
  printf("%25.4Lf C# results discussed early on\n",
                    prev_published_result_c);    
    
}
                   
                   
                   
                   


Results of run:

========================
64-bit IEEE 754  
                    377 Years 
                   1.04 Compounding Interest Factor 
                  12.00 Original Principle 
            31677446.18 RKR Bonanza (Non Truncating Algorithm using Inrinsic) 
                        Grinder's Previously Published Results:
            31362020.66   stepwise truncation
            31658845.52   stepwise rounding
            31677446.1774 C# results discussed early on

Monsterous floats Calcs  
                    377 Years 
                   1.04 Compounding Interest Factor 
                  12.00 Original Principle 
            31677446.18 RKR Bonanza (Non Truncating Algorithm using Inrinsic) 
                        Grinder's Previously Published Results:
            31362020.66   stepwise truncation
            31658845.52   stepwise rounding
            31677446.1774 C# results discussed early on

Either precision involves miniscule binary truncation 

There are four possible algorithms (in order of increasing result):
 - trunc floor() each period 
 - round each period (50/50) 
 - continuous function (as RKR Bonanza here to illustrate efficiency) 
 - round up ceil() each period (The Mega Bonanza) 

========================

A few more comments

The C example illustrates, and is commented as intrinsic function, because it
uses the common C pow() function.

For venerable COBOL you will need only

COMPUTE compounded_int = compounding_interest_rate ** years
END-COMPUTE

No COBOL intrinsic FUNCTION is necessary. 

You can eliminate the loop altogether with this approach.


Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
