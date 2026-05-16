[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# test IF A AND B AND C in COBOL (82)

_21 messages · 13 participants · 2001-10_

**Topics:** [`Meta: FAQs, group policy, charter`](../topics.md#meta)

---

### test IF A AND B AND C in COBOL (82)

- **From:** kyle.katarn@nospam.free.fr (Kyle Katarn)
- **Date:** 2001-10-04T15:26:16+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```
    	Hello,

I've a question about the evaluation of the expression:

IF A AND B AND C  ....

if A is false, are B and C evaluate ?
(by example if the validity of B depends of value of A....)

it depends of options ?

(I think that A B C are evaluate first)


    	Thanks !
```

#### ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-04T14:48:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9phspd$ja$1@peabody.colorado.edu>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```

On  4-Oct-2001, kyle.katarn@nospam.free.fr (Kyle Katarn) wrote:

> I've a question about the evaluation of the expression:
>
…[5 more quoted lines elided]…
> it depends of options ?

I don't understand "(by example if the validity of B depends of value of
A....)".    A and B and C are separate conditions.  Testing for A won't
change whether B is true.

Why does it matter whether B and C are evaluated?   Logically the order
doesn't matter - your only concern is which code runs faster (and this
concern will be very rare in this instance).

If your conditions are complex enough and you have knowledge that makes you
smarter than your optimizer - then change the AND to another IF.  
Otherwise, trust your optimizer, which might out-guess you otherwise.
```

##### ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-04T11:53:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pi46r$l87$1@slb1.atl.mindspring.net>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu>`

```
There are actually two times (that I can think of) that actually impact
program logic - depending on whether all three "things" are evaluated - or
just the first one (that turns out to be false).

1)  If A is false, but B or C have "incompatible data" in them, I know that
HISTORICALLY some compilers have produced code that "abended" - or ended
abnormally.  I believe that this is "standard conforming" as B and C are
"referenced" - even if their values are never needed.  My guess is that MOST
compilers do not do this - but some do (or did).

2) If B or C reference the RANDOM intrinsic function, there is some question
about whether or not one more in the "series" of returned values is
incremented.  This is actually a place where the '85 (actually '89) Standard
and the draft of the next standard differ (for EVALUATE - not IF).  I won't
go into the details (as this really is pretty obscure) - but it COULD impact
program logic.
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-04T17:33:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a41v7.375164$Lw3.23611968@news2.aus1.giganews.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu> <9pi46r$l87$1@slb1.atl.mindspring.net>`

```

On  4-Oct-2001, "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:

> There are actually two times (that I can think of) that actually impact
> program logic - depending on whether all three "things" are evaluated - or
…[7 more quoted lines elided]…
> MOST  compilers do not do this - but some do (or did).

Where this is a concern, I nest an IF instead of using AND

> 2) If B or C reference the RANDOM intrinsic function, there is some
> question
…[6 more quoted lines elided]…
> impact  program logic.

Interesting.

I am trying to think of a case where we care which RANDOM is used first (or
not used at all) in such an IF statement - but I am failing even to come up
with a scenario where I would use RANDOM that way.
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-05T07:19:17+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BBD50E5.56614F45@Azonic.co.nz>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu> <9pi46r$l87$1@slb1.atl.mindspring.net>`

```
William M. Klein wrote:
> 
> There are actually two times (that I can think of) that actually impact
…[7 more quoted lines elided]…
> compilers do not do this - but some do (or did).

According to Jim Inglis in his 'Cobol 85 for Programmers' in Cobol 85
the "evaluation ceases as soon as the truth value of the expression can
be determined".  The 85 Standard certainly states that data items are
referenced only when required to be evaluated.  My experience is that
all compilers I have used work this way.

It is perfectly safe in '85 (using compilers that correctly implement
this) to have:

         
         PERFORM
             VARYING Table-Index FROM 1 BY 1
               UNTIL Table-Index > Table-Occurs
                  OR Table-Item(Table-Index) = Search-Item

Without having a bound error.  It could fail if the two conditions were
transposed because '85 specifies Left to Right evaluation.  That is: if
a bound error occurs then the compiler is broken.

I have seen examples of code, some posted right here by those who should
know better, where the conditions were ordered incorrectly (ie the
reverse of the above example).  The only reason why they didn't get an
abend seems to be because bound-checking was off when it checked the
array item beyond the bound (or maybe it never failed to match in the
array - but might do at 2am some day).  
 
> 2) If B or C reference the RANDOM intrinsic function, there is some question
> about whether or not one more in the "series" of returned values is
…[3 more quoted lines elided]…
> program logic.

There is a significant problem with side-effects (or lack of them) when
short-circuit of evaluation occurs and the condition contains a
function.  As you say, it is only RANDOM that has any impact with Cobol,
and this is why user defined functions are such an issue.

If user-defined functions could be used in conditional expressions and
the function has side-effects, then they need to care about whether it
is evaluated or not.

Many inexperienced C programmers are mystified when the code in their
conditionals fails to execute due to short-circuit evaluation.  As
assignment is just another operator in C, it is quite common to have
assignments in conditions.  Cobol programmers are not ready for that, I
doubt that many even consider the implications of combined conditionals
and short circuiting and probably would be tempted to use a GO TO rather
than an AND or an OR.
```

##### ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-10-05T07:36:34+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BBD54F2.9631C1D6@Azonic.co.nz>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
> Why does it matter whether B and C are evaluated?   Logically the order
> doesn't matter - 

Oh yes it does:

     01  Table.
         03  Table-Item             PIC X OCCURS 10.
     ...

         IF X > 0 AND X NOT > 10 AND Table-Item(X) = SPACES
             ...

Logically the order and whether 'C' is evaluated is _very_ important. 
'85 gets this right by doing left to right evaluation, short circuiting
as soon as it can determine the value and by only referencing values
when required.
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-10-05T18:14:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ILmv7.17603$ev2.27668@www.newsranger.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu> <3BBD54F2.9631C1D6@Azonic.co.nz>`

```
Just as a matter of "trivia" the ICL runtime of Microsoft.net stops evaluation
when truth can be determined.  This has broken many visual basic programs -
especially those using functions as items in the comparison - as the functions
are never performed if truth can be determined before the fact.



In article <3BBD54F2.9631C1D6@Azonic.co.nz>, Richard Plinston says...
>
>Howard Brazee wrote:
…[16 more quoted lines elided]…
>when required.
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

_(reply depth: 4)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-10-05T20:46:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9plp2f02pff@enews3.newsguy.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu> <3BBD54F2.9631C1D6@Azonic.co.nz> <ILmv7.17603$ev2.27668@www.newsranger.com>`

```
"Thane Hubbell" <nospam@newsranger.com> wrote in message
news:ILmv7.17603$ev2.27668@www.newsranger.com...
> Just as a matter of "trivia" the ICL runtime of Microsoft.net
stops evaluation
> when truth can be determined.  This has broken many visual
basic programs -
> especially those using functions as items in the comparison -
as the functions
> are never performed if truth can be determined before the
fact.

This was true with Beta1, but Microsoft backed up a bit with
some nasty AndAlso OrElse operators--leaving And, Or, Xor and
Not as the non-short-circuting, bitwise freaks they are (in
VB6.)

http://www.dotnetwire.com/press/010409vbdotnet.asp
http://www.devx.com/dotnet/articles/fb_0628.asp
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

_(reply depth: 4)_

- **From:** "Grinder" <grinder@no.spam.maam.com>
- **Date:** 2001-10-05T21:11:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9plpdu02qjq@enews3.newsguy.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu> <3BBD54F2.9631C1D6@Azonic.co.nz> <ILmv7.17603$ev2.27668@www.newsranger.com>`

```
I like the density of the code you can write utilizing
short-circuits, but largely avoid them in favor of being
explicit.  Also, I tend to believe that an approach that
ambitiously uses short-circuits will present subtle bugs that
could have been avoid by nesting the checks.

Delphi allows short-circuits based upon a compiler switch--so
you can flip-flop back and forth.  What a reverse-engineering
nightmare!
```

##### ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** Volker Bandke <vbandke@bsp-gmbh.com>
- **Date:** 2001-10-05T14:00:16+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n08rrtgv38135figb3p4r3mgf5h1uun9ip@4ax.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9phspd$ja$1@peabody.colorado.edu>`

```
On Thu, 4 Oct 2001 14:48:57 GMT, "Howard Brazee"
<howard.brazee@cusys.edu> wrote:

>
>On  4-Oct-2001, kyle.katarn@nospam.free.fr (Kyle Katarn) wrote:
…[13 more quoted lines elided]…
>

It does make sense, though:  

If A NOT EQUAL ZERO AND 1/A GREATER THAN 1000

will give a runtime error if the second condition (1/A > 10000) is
evaluated even after the first (A=0) was evaluated as false

In cases like this, BTW, I use nested IFs

IF A NOT EQUAL ZERO
   IF 1/A GREATER THAN 1000
      PERFORM Some-action
   END-IF
END-IF





>Why does it matter whether B and C are evaluated?   Logically the order
>doesn't matter - your only concern is which code runs faster (and this
…[4 more quoted lines elided]…
>Otherwise, trust your optimizer, which might out-guess you otherwise.

                                                            
     With kind Regards            |\      _,,,---,,_        
                            ZZZzz /,`.-'`'    -.  ;-;;,     
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'   
      (BSP GmbH)                '---''(_/--'  `-'\_)        
                                                            
      A dull mind, once arriving at an inference that flatters a desire, is rarely able to retain the impression that the notion from which the inference started was purely problematic. -- George Eliot
      
        (Another Wisdom from my fortune cookie jar)         
______________________________________________________________________________
Posted Via Binaries.net = SPEED+RETENTION+COMPLETION = http://www.binaries.net
```

#### ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2001-10-04T11:46:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F998C198C7AA2C38.FE70965C50B6ED79.BBC749A66CDDD021@lp.airnews.net>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```
On Thu, 4 Oct 2001 15:26:16 +0200 , kyle.katarn@nospam.free.fr (Kyle
Katarn) enlightened us:

>    	Hello,
>
…[12 more quoted lines elided]…
>    	Thanks !

I believe the answer depends on the platform.  If on an IBM Mainframe
(S390/MVS), the Assembler code generated by the instruction shows that
once the comparison is False, a branch out of the evaluation routine
takes place.  

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I don't do drugs anymore 'cause I find I get the 
same effect just by standing up really fast.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-10-04T11:13:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pi1v7$41n$1@suaar1ac.prod.compuserve.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```
Looking at the generated assembler code on OS/390 the evaluation
of the expression is terminated when a false condition is found.
In other words, if a 'A' is false then 'B' and 'C' are not evaluated.
In an 'IF' statement with only 'AND' conditions, every test must
be true for the entire 'IF' to be considered true. When one condition
is determined false then the 'IF' is considered false and evaluation
stops. It sometimes can be important how you code this as well.
For example:

01  INPUTREC.
 05  A  PIC 99.
 05  B  PIC XXX.

   IF A IS NUMERIC   AND
      A >= 10        AND
      A <= 20        AND
      B = '123'
         PERFORM DO-SOMETHING.

If the value 'A' is spaces the entire 'IF' is false and evaluation
is abandoned at the numeric test.

If however you code:

  IF A >= 10         AND
     A <= 20         AND
     A IS NUMERIC    AND
     B = '123'
        PERFORM DO-SOMETHING.

You will most likely abend S0C7 if the value of 'A' is spaces because
'A' is not valid.

I know this is kind of a cheesy example... it's just to illustrate the
point how it works.

================================================================


"Kyle Katarn" <kyle.katarn@nospam.free.fr> wrote in message
news:Xns91309FFF334ACkatarnkyle@2.1.1.45...
>     Hello,
>
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-04T16:47:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oo0v7.101678$hh.9070966@bin1.nnrp.aus1.giganews.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9pi1v7$41n$1@suaar1ac.prod.compuserve.com>`

```

On  4-Oct-2001, "Ron" <Ron@NoSpamForMe.Com> wrote:

>    IF A IS NUMERIC   AND
>       A >= 10        AND
>       A <= 20        AND
>       B = '123'
>          PERFORM DO-SOMETHING.


Why not be safe and change that first AND to an IF?

That way, you don't have to guess that the optimizer will do the same thing
next time.  No maintenance programmers will wonder which will happen first
either.
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-10-04T12:17:40-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pi5lo$61t$1@suaar1ac.prod.compuserve.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9pi1v7$41n$1@suaar1ac.prod.compuserve.com> <oo0v7.101678$hh.9070966@bin1.nnrp.aus1.giganews.com>`

```
> Why not be safe and change that first AND to an IF?
>
> That way, you don't have to guess that the optimizer will do the same
thing
> next time.  No maintenance programmers will wonder which will happen first
> either.

Oh I agree with you. That is what I do in real life. It was just
a demonstration example.
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-10-04T12:18:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pi5lq$61t$2@suaar1ac.prod.compuserve.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <9pi1v7$41n$1@suaar1ac.prod.compuserve.com> <oo0v7.101678$hh.9070966@bin1.nnrp.aus1.giganews.com>`

```
> Why not be safe and change that first AND to an IF?
>
> That way, you don't have to guess that the optimizer will do the same
thing
> next time.  No maintenance programmers will wonder which will happen first
> either.

Oh I agree with you. That is what I do in real life. It was just
a demonstration example.
```

#### ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Ron" <Ron@NoSpamForMe.Com>
- **Date:** 2001-10-04T11:15:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pi1v9$41n$2@suaar1ac.prod.compuserve.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```
Looking at the generated assembler code on OS/390 the evaluation
of the expression is terminated when a false condition is found.
In other words, if a 'A' is false then 'B' and 'C' are not evaluated.
In an 'IF' statement with only 'AND' conditions, every test must
be true for the entire 'IF' to be considered true. When one condition
is determined false then the 'IF' is considered false and evaluation
stops. It sometimes can be important how you code this as well.
For example:

01  INPUTREC.
 05  A  PIC 99.
 05  B  PIC XXX.

   IF A IS NUMERIC   AND
      A >= 10        AND
      A <= 20        AND
      B = '123'
         PERFORM DO-SOMETHING.

If the value 'A' is spaces the entire 'IF' is false and evaluation
is abandoned at the numeric test.

If however you code:

  IF A >= 10         AND
     A <= 20         AND
     A IS NUMERIC    AND
     B = '123'
        PERFORM DO-SOMETHING.

You will most likely abend S0C7 if the value of 'A' is spaces because
'A' is not valid.

I know this is kind of a cheesy example... it's just to illustrate the
point how it works.

================================================================


"Kyle Katarn" <kyle.katarn@nospam.free.fr> wrote in message
news:Xns91309FFF334ACkatarnkyle@2.1.1.45...
>     Hello,
>
…[16 more quoted lines elided]…
>
```

#### ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** lesterzick@worldnet.att.net
- **Date:** 2001-10-04T16:30:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bbc6325.510699@netnews.att.net>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```
I don't know if it's still true, but years ago the COBOL language
specs and programmer's guide contained detailed charts showing exactly
the order of  evaluation for conditionals. As I recall for the example
shown, without parentheses, the expression would simply be evaluated
left to right and terminated when a false condition is found. If an OR
were included, the AND's would be evaluated first and then the OR.

Regards - Lester 

On Thu, 4 Oct 2001 15:26:16 +0200 , kyle.katarn@nospam.free.fr (Kyle
Katarn) wrote:

>    	Hello,
>
…[16 more quoted lines elided]…
>

Regards - Lester

ref http://home.earthlink.net/~lesterzick
```

##### ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-10-04T16:50:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3r0v7.374920$Lw3.23592284@news2.aus1.giganews.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <3bbc6325.510699@netnews.att.net>`

```

On  4-Oct-2001, lesterzick@worldnet.att.net wrote:

> I don't know if it's still true, but years ago the COBOL language
> specs and programmer's guide contained detailed charts showing exactly
…[3 more quoted lines elided]…
> were included, the AND's would be evaluated first and then the OR.

These are nice to have and to know - but a wise programmer puts in redundant
parenthesis.

Code that does what you want is necessary.  Code that does what you want -
and is clear - is better.  (your intentions should be clear)
```

###### ↳ ↳ ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** Calvin Crumrine <Calvin_Crumrine@dced.state.ak.us>
- **Date:** 2001-10-04T10:02:05-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BBCA41C.352BE458@dced.state.ak.us>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45> <3bbc6325.510699@netnews.att.net> <3r0v7.374920$Lw3.23592284@news2.aus1.giganews.com>`

```
Howard Brazee wrote:

> On  4-Oct-2001, lesterzick@worldnet.att.net wrote:
>
…[11 more quoted lines elided]…
> and is clear - is better.  (your intentions should be clear)

Similarly wise programmers don't rely on defaults. Explicitly initialize your
variables, etc. Not only is it clearer but defaults change with different
installations while explicit statements don't.
```

#### ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "James" <mangogrower@telocity.com>
- **Date:** 2001-10-04T14:16:08-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qG1v7.8411$W11.1909400@newsrump.sjc.telocity.net>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```
The question (restated) is:
IF CONDITION-A TRUE and CONDITION-B TRUE and CONDITION-C TRUE

Well, If CONDITION-A AINT TRUE, it don't matter what the others be.
Without Parenthesis, the compilers will evaluate similar relations /
operands in LEFT to RIGHT order.

The compilers should be ignoring B&C if A is FALSE.  (Without Optimization)
"Kyle Katarn" <kyle.katarn@nospam.free.fr> wrote in message
news:Xns91309FFF334ACkatarnkyle@2.1.1.45...
>     Hello,
>
…[16 more quoted lines elided]…
>
```

#### ↳ Re: test IF A AND B AND C in COBOL (82)

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-10-05T03:22:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lI9v7.6030$bp6.1122533658@newssvr17.news.prodigy.com>`
- **References:** `<Xns91309FFF334ACkatarnkyle@2.1.1.45>`

```
    On a related note, older compilers used to croak on the following if A
was not numeric:
IF A > ZERO AND A NUMERIC
As a result, it was important to reverse the checks as follows:
IF A NUMERIC AND A > ZERO
I've noticed recently that the first example will no longer abend.  It
apparently checks for numeric before checking the value of A.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
