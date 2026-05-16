[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OS/VS to COBOL/390 Conversion Problem

_28 messages · 13 participants · 2000-04_

---

### OS/VS to COBOL/390 Conversion Problem

- **From:** "Thomas" <tanmoy@singnet.com.sg>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dt7qm$oi6$1@mawar.singnet.com.sg>`

```
We are converting an os/vs cobol program to cobol/390.
The program has an expression like this :
A = B * (1 - ((C/12) * D) * (1/1.05) ** (C/12)

The PIC clauses are :
A      PIC      9(7)V9(6).
B      PIC      9(7)V9(6).
C      PIC      9(2).
D      PIC      9V9(5).

For the same values of B,C,D the result obtained under cobol/390 is more
than that in os/vs.
e.g, when  B=125.0525, C=25, D=1.00489

A = 0000123.530454 [ os/vs cobol ]
A = 0000123.530747 [ cobol/390 ]

How can we get the same value under cobol/390? We want to use the cobol/390
compiler
but the result must be same as what was obtained using os/vs cobol compiler.

Is there any workaround?

TIA.
```

#### ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 2000-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QsqM4.3080$4O2.23612@typhoon.austin.rr.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg>`

```

Thomas <tanmoy@singnet.com.sg> wrote in message
news:8dt7qm$oi6$1@mawar.singnet.com.sg...
> We are converting an os/vs cobol program to cobol/390.
> The program has an expression like this :
> A = B * (1 - ((C/12) * D) * (1/1.05) ** (C/12)

===> missing parenthesis somewhere

>
> The PIC clauses are :
…[3 more quoted lines elided]…
> D      PIC      9V9(5).

try to allocate more decimals (use a temp if need be):
C  PIC 9(2)v9(6)
(1.0000001.050000) ** (C / 12)
```

##### ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "Thomas" <tanmoy@singnet.com.sg>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dtqah$t6l$1@clematis.singnet.com.sg>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <QsqM4.3080$4O2.23612@typhoon.austin.rr.com>`

```
> > A = B * (1 - ((C/12) * D) * (1/1.05) ** (C/12)
>
> ===> missing parenthesis somewhere

Oops!  It should have been:

A = B * (1 - ( (C/12) * D ) ) * (1/1.05) ** (C/12)




Leif Svalgaard <leif@ibm.net> wrote in message
news:QsqM4.3080$4O2.23612@typhoon.austin.rr.com...
>
> Thomas <tanmoy@singnet.com.sg> wrote in message
…[20 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MDNM4.4241$4O2.36168@typhoon.austin.rr.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <QsqM4.3080$4O2.23612@typhoon.austin.rr.com> <8dtqah$t6l$1@clematis.singnet.com.sg>`

```

Thomas <tanmoy@singnet.com.sg> wrote in message
news:8dtqah$t6l$1@clematis.singnet.com.sg...
> > > A = B * (1 - ((C/12) * D) * (1/1.05) ** (C/12)
> >
…[4 more quoted lines elided]…
> A = B * (1 - ( (C/12) * D ) ) * (1/1.05) ** (C/12)

If I try with approx. values B = 125, D=1, C/12=2
A= 125 * (1 - 2)  * 1 ** 2 = -125
that is negative, now, the picture of A is unsigned,
so one should take the absolute value, thus A = 125,
approx. This seems to be a ***dangerous*** practice.

Furthermore, if you perform the calculation, the
result is 123.5307467599 so the OS/390 result
is actually correct. Why do you the incorrect OS/VS
value?
```

#### ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dt9sj$n6c$1@slb6.atl.mindspring.net>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg>`

```
I have sent a note to one of my "usually reliable source" to see if this is a
known difference and/or if there is away around the problem.

Two things that you MIGHT try (and I don't know if this will work/help at
all) are:

1) Add some more digits to your numeric literal, e.g. Change "1" to "1.00"

2) Change at least one of your numeric literals to floating-point, e.g.
Change
   1 to 1.0E00 (I think that is a floating-point 1)

I don't know if either of these will change your results or not.  The
"complete rules" for how "intermediate results" are figured appear in both
the OS/VS COBOL and COBOL for OS/390 & VM "Programming Guide".  You could try
studying them to see what has changed, but what you are reporting does NOT
ring a bell with me.
```

#### ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** James <mangogwr@bellsouth.net>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3903C3C3.C6489BAE@bellsouth.net>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg>`

```
Verify that the compile options are set to get the same results,
esp. TRUNC (BIN/PIC)

Thomas wrote:

> We are converting an os/vs cobol program to cobol/390.
> The program has an expression like this :
…[21 more quoted lines elided]…
> TIA.
```

##### ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e080m$9db$1@slb7.atl.mindspring.net>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net>`

```
If he hasn't "cut too much" from the data descriptions, the TRUNC options
can't have any impact.  In his example, everything is (implicitly) USAGE
DISPLAY.  TRUNC only impacts USAGE BINARY/COMP items.
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "Thomas" <tanmoy@singnet.com.sg>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e2ghu$t63$1@coco.singnet.com.sg>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net>`

```
All data items are implicit USAGE DISPLAY. I have cut short only the
variable names
and represented as A,B,C,D .
Since it is an existing program, I'm not sure why the picture clauses are
not consistent
or why there is no provision for sign. My job is to convert the language &
keep the program
behaviour 'same as before'. Cobol/390 is computing more accurately--- that's
my problem!
User wants the same result as under os/vs, whether it is less accurate or
wrong or whatever.

I have tried all TRUNC options i.e. STD,OPT and BIN.
I have also tried all suggestions in this thread. The results were never
identical.

The basic fact is that the program is running in production. It produces a
report
which has many detail lines per page and there is a Total line. After
converting to
cobol/390, the change in the total value is in the integer portion, which is
not
acceptable to the user.

How would it be if I write a subroutine in os/vs cobol just to evaluate the
expression?
Then I call from the cobol/390 program. Any gotchas?




William M. Klein <wmklein@nospam.ix.netcom.com> wrote in message
news:8e080m$9db$1@slb7.atl.mindspring.net...
> If he hasn't "cut too much" from the data descriptions, the TRUNC options
> can't have any impact.  In his example, everything is (implicitly) USAGE
…[4 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sM3N4.4535$4O2.44175@typhoon.austin.rr.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg>`

```
see comments embedded below:

Thomas <tanmoy@singnet.com.sg> wrote in message
news:8e2ghu$t63$1@coco.singnet.com.sg...
> All data items are implicit USAGE DISPLAY. I have cut short only the
> variable names
…[5 more quoted lines elided]…
> behaviour 'same as before'. Cobol/390 is computing more accurately---
that's
> my problem!
> User wants the same result as under os/vs, whether it is less accurate or
…[10 more quoted lines elided]…
> cobol/390, the change in the total value is in the integer portion, which
is
> not
> acceptable to the user.

how can the WRONG result be acceptable? Can you not convince
him that a CORRECT result is better? Yeah, I know that human
folly knows no bounds, but come on...

simply show him using a calculator that the old value is wrong.


>
> How would it be if I write a subroutine in os/vs cobol just to evaluate
the
> expression?
> Then I call from the cobol/390 program. Any gotchas?
…[6 more quoted lines elided]…
> > If he hasn't "cut too much" from the data descriptions, the TRUNC
options
> > can't have any impact.  In his example, everything is (implicitly) USAGE
> > DISPLAY.  TRUNC only impacts USAGE BINARY/COMP items.
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 5)_

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e30rk$29jg$1@newssvr03-int.news.prodigy.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com>`

```

Your comment reminds me of a case where a slight inaccuracy had to be
introduced to satisfy the user.  When one sums rounded numbers, the total is
sometimes not 100%.  The user wanted the %-ages to add up to 100, so even
though it was mathematically less accurate, we had to adjust one of the
sub-totals so that the total added up to 100%!

Leif Svalgaard <leif@ibm.net> wrote in message
news:sM3N4.4535$4O2.44175@typhoon.austin.rr.com...
> see comments embedded below:
>
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e2kdb$n4e$1@slb7.atl.mindspring.net>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com>`

```
"Leif Svalgaard" <leif@ibm.net> wrote in message
news:sM3N4.4535$4O2.44175@typhoon.austin.rr.com...
> see comments embedded below:
>
> Thomas <tanmoy@singnet.com.sg> wrote in message
> news:8e2ghu$t63$1@coco.singnet.com.sg...
  <snip>
>
> how can the WRONG result be acceptable? Can you not convince
…[5 more quoted lines elided]…
>
  <snip>

I hate to be the bearer of bad news (which I am certain Thomas is aware of -
but others in the NG may not be).  It is RELATIVELY common in large business
applications to require "identical" - not "more correct" results from "before
and after" maintenance (whether an upgrade of compiler - or simple
application maintenance).  Especially when arithmetic expression end up in
"numbers" that are turned into dollars, it is very, VERY, difficult to
explain that what used to be charged was "wrong" (and we won't give you any
rebate) and what we are charging now is more accurate (and you will need to
start paying the new rate immediately).

The classic example that I ran into time and TIME AGAIN when working at Micro
Focus was in code like the following:

  01 A  Pic 9 Value 7.
  01 B  Pic 9  Value 4
  01 C  Pic 9  Value zero.

   Compute C = (A / B ) * B

Now anyone who has studied arithmetic (not even math) will tell you that C
should end up with a value of 7.  UNFOTUNTATELY for reasons that are well
documented (but a tad strange), the IBM mainframe COBOLs (old and new) will
give an answer of 4, not 7.

It didn't matter how many times that we in Micro Focus explained this to
customers, they STILL wanted the PC COBOL to provide an answer of 7 and not 4
(even for programs that were to be "ported" to the PC for production, not
just those developed there).

Therefore, I have a LOT of sympathy with a shop that is trying to get the
same old "bad" answers in a migration.  I don't know that they are going to
succeed (and I sure hope that the programmers HAVE shown the users how the
new answers are "better").
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 6)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39059BC2.312A427F@cusys.edu>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> I hate to be the bearer of bad news (which I am certain Thomas is aware of -
…[7 more quoted lines elided]…
> start paying the new rate immediately).

I still wish people learned to use slide rules.  Once you understand
estimation, significant digits, and proportion, you know all the math
95% of the people would ever need.

I remember a discussion people had about whether the Bible was 100%
accurate.  Someone picked a foolish example - he found where the Bible
mentioned a circular object which was 3 times as far around as it was
across.  Since this implies that pi=3, the Bible was wrong!!!    Putting
aside details about real world measurements etc - what does he think pi
is?   To one significant digit (which was applicable in this case)
pi=3.  That is the way it is.  How many digits does he think is 100%
accurate?

Data processing has many cases where we have to sit down with the
accountant to determine exactly how we should be rounding our figures. 
They have rules which have been established which are very strict (if
not completely logical).  A lot of this was designed to stop fraud. 
Some of it has been developed to stop people from doing currency trading
in a circle ( pounds -> Euros -> dollars -> pounds) to benefit from
today's rounding errors.
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 7)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WvhN4.4775$4O2.56331@typhoon.austin.rr.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net> <39059BC2.312A427F@cusys.edu>`

```

Howard Brazee <howard.brazee@cusys.edu> wrote in message
> "William M. Klein" wrote:
> > I hate to be the bearer of bad news (which I am certain Thomas is aware
of -
> > but others in the NG may not be).  It is RELATIVELY common in large
business
> > applications to require "identical" - not "more correct" results from
"before
> > and after" maintenance
> I remember a discussion people had about whether the Bible was 100%
> accurate.  Someone picked a foolish example - he found where the Bible
> mentioned a circular object which was 3 times as far around as it was
> across.  Since this implies that pi=3, the Bible was wrong

For the die-hard believers of a 100% correct Bible, consider this:

In 1 Kings, 7.23, it is written:
"And he made a molten sea, ten cubits from the one brim to other;
[...] and a line of thirty cubits did compass it round about."

Rabbi Nehemiah (A.D. 150) tells us that clearly the diameter of 10 cubits
was measured from the *inside* ("brim") of the wall while the circumference
was measured on the *outside* of the vessel. This account for the
difference.
Exercise for the reader: how thick was the wall?
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 8)_

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3905B0DB.A589FCDB@cusys.edu>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net> <39059BC2.312A427F@cusys.edu> <WvhN4.4775$4O2.56331@typhoon.austin.rr.com>`

```
Leif Svalgaard wrote:
> 
> Howard Brazee <howard.brazee@cusys.edu> wrote in message
…[23 more quoted lines elided]…
> Exercise for the reader: how thick was the wall?

How many significant digits do we have in the measurement?  Without
using scientific notation, those 10 and 30 cubits can either be 1 or 2
significant digits (or if you like, assume a precision).  With one
significant digit, the precision of the answer is variable enough to
make such a calculation meaningless.

Neither one of us is talking about the literalness of the Bible - we are
talking about how people get confused with numbers, significance, and
precision.
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6nrN4.903$mN2.207274@dfiatx1-snr1.gtei.net>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net> <39059BC2.312A427F@cusys.edu> <WvhN4.4775$4O2.56331@typhoon.austin.rr.com>`

```
Leif Svalgaard <leif@ibm.net> wrote in message
news:WvhN4.4775$4O2.56331@typhoon.austin.rr.com...
>
> For the die-hard believers of a 100% correct Bible, consider this:
…[6 more quoted lines elided]…
> was measured from the *inside* ("brim") of the wall while the
circumference
> was measured on the *outside* of the vessel. This account for the
> difference.
> Exercise for the reader: how thick was the wall?
>

Well, by modern math, the circumference of the brim (inside) should be 31.4
cubits give or take a tad.

Now if the outside wall is but 30 cubits, clearly what was made violates the
laws of physics, as the circumference of the outer wall must certainly by
greater than the 31.4 cubits of the inner wall.

So the real question is, "What was Rabbi Nehemiah smoking when her did the
measurements?"

MCM
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 9)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6TsN4.27$JH.2595@typhoon.austin.rr.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net> <39059BC2.312A427F@cusys.edu> <WvhN4.4775$4O2.56331@typhoon.austin.rr.com> <6nrN4.903$mN2.207274@dfiatx1-snr1.gtei.net>`

```
Well, maybe he had it backwards, but if the thickness
of the wall were -0.55 cubits, everything comes out right.
This is just like in Thomas's problem where the right-hand
size is actually negative, but since A's picture doesn't
have a sign, the result is positive. Moral: if you want
to fudge, you can always do it.
BTW, Thomas, what did you decide to do about
this whole miserable affair?
For Bill Klein: imagine that Thomas has to do yet
another migration to a third platform a few years
from now, should he still try to emulate the old error?
I mean, where does it end?

Michael Mattias <michael.mattias@gte.net> wrote in message
news:6nrN4.903$mN2.207274@dfiatx1-snr1.gtei.net...
> Leif Svalgaard <leif@ibm.net> wrote in message
> news:WvhN4.4775$4O2.56331@typhoon.austin.rr.com...
…[7 more quoted lines elided]…
> > Rabbi Nehemiah (A.D. 150) tells us that clearly the diameter of 10
cubits
> > was measured from the *inside* ("brim") of the wall while the
> circumference
…[5 more quoted lines elided]…
> Well, by modern math, the circumference of the brim (inside) should be
31.4
> cubits give or take a tad.
>
> Now if the outside wall is but 30 cubits, clearly what was made violates
the
> laws of physics, as the circumference of the outer wall must certainly by
> greater than the 31.4 cubits of the inner wall.
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e63pn$d36$1@slb2.atl.mindspring.net>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net> <39059BC2.312A427F@cusys.edu> <WvhN4.4775$4O2.56331@typhoon.austin.rr.com> <6nrN4.903$mN2.207274@dfiatx1-snr1.gtei.net> <6TsN4.27$JH.2595@typhoon.austin.rr.com>`

```
"Leif Svalgaard" <leif@ibm.net> wrote in message
news:6TsN4.27$JH.2595@typhoon.austin.rr.com...
 <nsip>
> BTW, Thomas, what did you decide to do about
> this whole miserable affair?
…[4 more quoted lines elided]…
>

That one is EASY.  It stops when the "users" stop paying for new versions
that give the same (semi-bad) results ... and it continues until then (with
occassional reminders to the user that they HAVE requested "less accurate"
results, do they really want to continue doing so when you CAN provide better
answers).
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 10)_

- **From:** "Thomas" <tanmoy@singnet.com.sg>
- **Date:** 2000-04-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eaf7u$l9r$1@coco.singnet.com.sg>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net> <39059BC2.312A427F@cusys.edu> <WvhN4.4775$4O2.56331@typhoon.austin.rr.com> <6nrN4.903$mN2.207274@dfiatx1-snr1.gtei.net> <6TsN4.27$JH.2595@typhoon.austin.rr.com>`

```

Leif Svalgaard <leif@ibm.net> wrote in message news:6TsN4.27$JH.2595@typhoon.austin.rr.com...
> BTW, Thomas, what did you decide to do about
> this whole miserable affair?


1. I have made a series of experiments (with various PIC clauses, data-types,
    breaking expression into temp variables, compiler options)
    and prepared a document showing comparative results at different conditions.
    Finally the document was given to the user.

2. I have informed user that it is impossible to keep the results same.
    This discussion thread has been of great help to support my claim.
    When experts (like you all) express their ideas, convincing others is much
     easier task for me :-)

3. Alternate suggestion given (keeping the computational part as vs cobol routine etc..)
    [Thanks Bill Klein!]


Now the matter is with users and top management. Until further decision, old prog will
continue running in production.


Thanks to all of you.
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 11)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 2000-04-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4y3O4.10$_l5.1986@typhoon.austin.rr.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net> <39059BC2.312A427F@cusys.edu> <WvhN4.4775$4O2.56331@typhoon.austin.rr.com> <6nrN4.903$mN2.207274@dfiatx1-snr1.gtei.net> <6TsN4.27$JH.2595@typhoon.austin.rr.com> <8eaf7u$l9r$1@coco.singnet.com.sg>`

```
Let's hope reason prevails.
You can quote me on that !

Good luck

Leif


Thomas <tanmoy@singnet.com.sg> wrote in message
news:8eaf7u$l9r$1@coco.singnet.com.sg...
>
> Leif Svalgaard <leif@ibm.net> wrote in message
news:6TsN4.27$JH.2595@typhoon.austin.rr.com...
> > BTW, Thomas, what did you decide to do about
> > this whole miserable affair?
>
>
> 1. I have made a series of experiments (with various PIC clauses,
data-types,
>     breaking expression into temp variables, compiler options)
>     and prepared a document showing comparative results at different
conditions.
>     Finally the document was given to the user.
>
> 2. I have informed user that it is impossible to keep the results same.
>     This discussion thread has been of great help to support my claim.
>     When experts (like you all) express their ideas, convincing others is
much
>      easier task for me :-)
>
> 3. Alternate suggestion given (keeping the computational part as vs cobol
routine etc..)
>     [Thanks Bill Klein!]
>
>
> Now the matter is with users and top management. Until further decision,
old prog will
> continue running in production.
>
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 6)_

- **From:** lengbirk@image.dk
- **Date:** 2000-04-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3906b186.96784358@news.get2net.dk>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com> <8e2kdb$n4e$1@slb7.atl.mindspring.net>`

```
On Mon, 24 Apr 2000 18:12:56 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

It's funny to see how the latest version of Micro Focus COBOL can
still produce a result of 4 and a result of 7 depending on the dialect
you choose.

Cheers,
Morten

>The classic example that I ran into time and TIME AGAIN when working at Micro
>Focus was in code like the following:
…[28 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 5)_

- **From:** "Thomas" <tanmoy@singnet.com.sg>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e2jna$nfo$1@violet.singnet.com.sg>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg> <sM3N4.4535$4O2.44175@typhoon.austin.rr.com>`

```

> how can the WRONG result be acceptable? Can you not convince
> him that a CORRECT result is better? Yeah, I know that human
…[3 more quoted lines elided]…
>

The debate is about consistency. One result is more accurate and the
other less accurate. Actually neither is absolutely WRONG.
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 4)_

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t34N4.4613$4O2.44691@typhoon.austin.rr.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg>`

```
> How would it be if I write a subroutine in os/vs cobol just to evaluate
the
> expression?
> Then I call from the cobol/390 program. Any gotchas?

dunno. but if everything fails, try to find out WHICH
of the factors of the formula cause the difference:

A = B * (1 - ( (C/12) * D ) ) * (1/1.05) ** (C/12)

is it (1-((C/12) * D)) or (1/1.05) ** (C/12) that
are different (with a bit of luck only one is).

my guess would be the exponentiation.
Let's say it is. Then since C can have at
most 100 values (pic 99), compute a
table (tongue beginning to press on inside
of cheek...) with the 100 differences
and simply apply that to falsify the result
to the user's satisfaction.
```

###### ↳ ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

_(reply depth: 4)_

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ijjags0tkefd4sveo0ql961lausvrd80h9@4ax.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net> <8e080m$9db$1@slb7.atl.mindspring.net> <8e2ghu$t63$1@coco.singnet.com.sg>`

```
On Tue, 25 Apr 2000 06:13:26 +0800 "Thomas" <tanmoy@singnet.com.sg> wrote:

:>All data items are implicit USAGE DISPLAY. I have cut short only the
:>variable names
:>and represented as A,B,C,D .
:>Since it is an existing program, I'm not sure why the picture clauses are
:>not consistent
:>or why there is no provision for sign. My job is to convert the language &
:>keep the program
:>behaviour 'same as before'. Cobol/390 is computing more accurately--- that's
:>my problem!
:>User wants the same result as under os/vs, whether it is less accurate or
:>wrong or whatever.

:>I have tried all TRUNC options i.e. STD,OPT and BIN.
:>I have also tried all suggestions in this thread. The results were never
:>identical.

:>The basic fact is that the program is running in production. It produces a
:>report
:>which has many detail lines per page and there is a Total line. After
:>converting to
:>cobol/390, the change in the total value is in the integer portion, which is
:>not
:>acceptable to the user.

:>How would it be if I write a subroutine in os/vs cobol just to evaluate the
:>expression?
:>Then I call from the cobol/390 program. Any gotchas?

I would suggest checking out the PMAP from the OS/VS Cobol compilation to
determine the lengths used for the intermediate fields.

Once you know that you can break up the compute statement to several
statements and use the OS/VS Cobol temporary lengths as the lengths of your
temporaries.

From 
  A = B * (1 - ((C/12) * D) * (1/1.05) ** (C/12))

To
  t1 = c / 12
  t2 = t1 * d
  t3 = 1 / 1.05  [1]
  t4 = t3 ** t1
  t5 = t4 * t2
  t6 = 1 - t5
  a = b * t6 

[1] Might be interesting to see if both COBOLs used the same value for this
constant (which cannot be exactly represented in either decimal or binary).
```

##### ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-04-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e39d4$2m8$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <3903C3C3.C6489BAE@bellsouth.net>`

```
    I am not up to date on mainframe Cobol, but I remember
hearing that
some older mainframe compilers limited the size of temporary
intermedate
variables to match the size of the receiving (or sending for all
I know) field.

    Current compilers use a maximum size temporary variable.  I
think that the
OS390 result is correct.



James <mangogwr@bellsouth.net> wrote in message
news:3903C3C3.C6489BAE@bellsouth.net...
> Verify that the compile options are set to get the same
results,
> esp. TRUNC (BIN/PIC)
>
…[12 more quoted lines elided]…
> > For the same values of B,C,D the result obtained under
cobol/390 is more
> > than that in os/vs.
> > e.g, when  B=125.0525, C=25, D=1.00489
…[4 more quoted lines elided]…
> > How can we get the same value under cobol/390? We want to use
the cobol/390
> > compiler
> > but the result must be same as what was obtained using os/vs
cobol compiler.
> >
> > Is there any workaround?
> >
> > TIA.
>
```

#### ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39025C7B.D1C5B9ED@home.com>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg>`

```


Thomas wrote:
> 
> We are converting an os/vs cobol program to cobol/390.
…[21 more quoted lines elided]…
> 
I can't answer your specific problem as I work on a PC, but I assume
from what you show above it is a COMPUTE ? As the books warn us there
can be problems with varying field sizes in computes. What I have done
PC-wise is to breakdown a COMPUTE into levels :-

compute result1 = (1/1.05) ** (C/12)
compute result2 = (C/12) * D) * result1
compute result3 = etc.....

Maybe you don't need to go the same extremes, but pick a 'break-up'
which gives you what you 'know' your results should be. Conceivably you
could get the correct result if you made all your fields the same size,
perhaps moving some values to temporary fields with a common size ?

Jimmy, Calgary AB
```

#### ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 2000-04-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dufnf$4gp$1@news.inet.tele.dk>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg>`

```
Hey,
I know that differences are described in some migration documents, published
by IBM. Search for 'Migration', or wait for Bill - his sources will probably
find it.

Regards
Ib

Thomas skrev i meddelelsen <8dt7qm$oi6$1@mawar.singnet.com.sg>...
>We are converting an os/vs cobol program to cobol/390.
>The program has an expression like this :
…[17 more quoted lines elided]…
>but the result must be same as what was obtained using os/vs cobol
compiler.
>
>Is there any workaround?
…[3 more quoted lines elided]…
>
```

#### ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RgoAOZAJfGB5EwVQ@ld50macca.demon.co.uk>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg>`

```
Wasn't this question answered in another thread late last year? I seem
to remember that the answer was something to do with compile options
determining truncation and intermediate field sizes rules.

In article <8dt7qm$oi6$1@mawar.singnet.com.sg>, Thomas
<tanmoy@singnet.com.sg> writes
>We are converting an os/vs cobol program to cobol/390.
>The program has an expression like this :
…[23 more quoted lines elided]…
>
```

##### ↳ ↳ Re: OS/VS to COBOL/390 Conversion Problem

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8e30q4$3hg$1@nntp9.atl.mindspring.net>`
- **References:** `<8dt7qm$oi6$1@mawar.singnet.com.sg> <RgoAOZAJfGB5EwVQ@ld50macca.demon.co.uk>`

```
One more time,
  TRUNCATION (and TRUNC compiler options) do NOT impact USAGE DISPLAY numeric
fields.

  ***

I believe (and am still working on verifying this) that as long as your
arithmetic expression includes fractional exponentiation (raising a number to
a fraction), that there is NO way to get identical results in new COBOLs as
were produced in OS/VS COBOL.  The "NewBOL" compilers (VS COBOL II and later)
*all* use a set of mathematical routines that are "shared" among DB2,
Fortran, COBOL, PL/I, C, etc.  These are "highly accurate" routines and just
will NOT (cannot) provide the same results as the older code (which was OS/VS
COBOL specific).

  ***

There is one "possible" solution to this problem (which would be practical if
you only have a few statements that need to get "same results" - but which
would be impractical if there are wide-spread arithmetic expression that need
to get "same results").

If you create a "small" OS/VS COBOL program that JUST does the requested
arithmetic expression and receives all the operands in Linkage Section and
returns the results also thru Linkage section, then you could compile this
program with OS/VS COBOL.

You then take your "major" logic and recompile it with the new COBOL (IBM
COBOL for OS/390 & VM - or similar compiler) and replace the current
arithmetic expression with a call (dynamic or static) to the OS/VS COBOL
program to do the arithmetic.  This would mean that your "main" program would
need to be compiled with DATA(24) - so it could pass the parameters to the
OS/VS COBOL program (where the linkage section needs to be "below the line").

If you aren't aware of it, IBM currently (and for the foreseeable future)
supports OS/VS COBOL compiled programs - as long as they are run with the LE
library.  (Theoretically, you aren't supposed to be compiling these programs
now - but I think the scenario I described above would PROBABLY be
supported.)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
