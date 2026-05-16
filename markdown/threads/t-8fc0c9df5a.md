[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# thane and mr. wolfe, you'll love this

_12 messages · 8 participants · 1998-09_

---

### thane and mr. wolfe, you'll love this

- **From:** Mike Ganas <skidmike@mindspring.com>
- **Date:** 1998-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ECD25C.CF4E81D2@mindspring.com>`

```
fujitsu cobol seems to have learned math from "outcome-based education"
now am in the programs to print estimates/invoices.  (thane has seen the
pgm in action)  on the "create estimate" screen, when a part is added to
the estimate, the totals update correctly (it's 6% sales tax). but when
printing, and i used the identical coding for the subroutines, a $100
part (taxable) comes up as $101.40 in the sub-total line of the report. 
i like mark-up as much as anyone (am on straight commission and all) but
this won't work.  can you advise, as i have a .45 currently pointed at
this machine and i'm not afraid to shoot!
```

#### ↳ Re: thane and mr. wolfe, you'll love this

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com>`

```
Mike Ganas wrote:
>fujitsu cobol seems to have learned math from "outcome-based education"
>now am in the programs to print estimates/invoices.  (thane has seen the
…[6 more quoted lines elided]…
>this machine and i'm not afraid to shoot!

Mike, if you will simply structure your expressions so that the multiplies
are done before the divides, you will eliminate the vast majority of such
problems.  For example, when you are computing a percent, don't write it:

   COMPUTE Percent = Pct-Value / Tot-Value * 100.

but write it:

   COMPUTE Percent = Pct-Value * 100 / Tot-Value.

In other words, don't just write the expression dumb, *think* about what
the compiler is going to do with your expression, and how it is going to
evaluate it.  I learned this as a newbie programmer 30 years ago, and
have rarely a problem getting a COMPUTE to work as I intend.

This issue is a prime example of why programmers should know at least
one assembly language.  The compiler's task of evaluating an expression
using fixed point arithmetic, without overflow or undue truncation, is
not an easy one.  Having an understanding of how the expression will be
processed at assembly language level really helps you to articulate what
you want so the compiler will get it right.  I have always been glad to
have learned assembly language first.  It always pays to have a solid
understanding of what is really going on inside the box.
```

##### ↳ ↳ Re: thane and mr. wolfe, you'll love this

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ED7031.C649FEAD@att.net>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net>`

```
Judson McClendon wrote:
>
(snip)
> Mike, if you will simply structure your expressions so that the multiplies
> are done before the divides, you will eliminate the vast majority of such
…[20 more quoted lines elided]…
> understanding of what is really going on inside the box.

My approach to this issue has been to use parentheses to make the
calculation clear, even when they are not required. Certainly agree with
Judson that it's important to learn and remember the compiler's rules
for evaluating expressions, arithmetic & otherwise.

Bill Lynch
```

###### ↳ ↳ ↳ Re: thane and mr. wolfe, you'll love this

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6skkvn$iop$1@news.igs.net>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net> <35ED7031.C649FEAD@att.net>`

```

>Judson McClendon wrote:
>>
>(snip)
>> Mike, if you will simply structure your expressions so that the
multiplies
>> are done before the divides, you will eliminate the vast majority of such
>> problems.  For example, when you are computing a percent, don't write it:
…[5 more quoted lines elided]…
>>    COMPUTE Percent = Pct-Value * 100 / Tot-Value.
understanding of what is really going on inside the box.
>
>Bill Lynch
…[3 more quoted lines elided]…
>for evaluating expressions, arithmetic & otherwise.


I tend to agree with Bill.  I use redundant parentheses a lot, both in
compute
statements and in logical IF statements where there is more than one
condition.  While the order of evaluation is supposed to be set by a
standard,
I still find that it is an area that often causes problems not only within
particular compilers but also in conversions.  Specifying a specific order
of evaluation by using parentheses is a cheap (compile time only) and
simple surety that has the advantage of also documenting the order.
```

###### ↳ ↳ ↳ Re: thane and mr. wolfe, you'll love this

_(reply depth: 4)_

- **From:** Mike Ganas <skidmike@mindspring.com>
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EE21F7.1DB78B58@mindspring.com>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net> <35ED7031.C649FEAD@att.net> <6skkvn$iop$1@news.igs.net>`

```
thanks, next round on me.  actually, i found out the prob tonite.  all
of the math is done in dll's and i didn't remember to write right below
procedure division "move zeroes to..."  i was getting totals from
previous estimates and invoices in the program.  (i think the blonde
roots are starting to show, where is my grecian formula?!)
i try to keep my math simple for the next programmer to tackle this
turkey, one computation per line.  guess when i get to the cost-per-job
and gross-profit stuff it may get hairy.  meanwhile, in fujitsu 3.0 how
do i get a nice source code printout that doesn't run over the
perforations in the paper and includes copy files for the w-s and f-d
entries?

Donald Tees wrote:
> 
> >Judson McClendon wrote:
…[28 more quoted lines elided]…
> simple surety that has the advantage of also documenting the order.
```

###### ↳ ↳ ↳ Re: thane and mr. wolfe, you'll love this

_(reply depth: 5)_

- **From:** sff5ky@aol.com (Sff5ky)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1998090302310700.WAA06224@ladder03.news.aol.com>`
- **References:** `<35EE21F7.1DB78B58@mindspring.com>`

```
In article <35EE21F7.1DB78B58@mindspring.com>, Mike Ganas
<skidmike@mindspring.com> writes:

>turkey, one computation per line.  guess when i get to the cost-per-job
>and gross-profit stuff it may get hairy.  meanwhile, in fujitsu 3.0 how
…[3 more quoted lines elided]…
>
Have you tried adding these to your compile options?

[Compile Options]
COPY=Yes
LINECOUNT=60
PRINT=Yes 
SOURCE=Yes
```

###### ↳ ↳ ↳ Re: thane and mr. wolfe, you'll love this

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35ed7a3c.0@news1.ibm.net>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net> <35ED7031.C649FEAD@att.net>`

```

Bill Lynch wrote in message <35ED7031.C649FEAD@att.net>...
>Judson McClendon wrote:
>> Mike, if you will simply structure your expressions so that the
multiplies
>> are done before the divides, you will eliminate the vast majority of such
>> problems.  For example, when you are computing a percent, don't write it:
…[10 more quoted lines elided]…
>for evaluating expressions, arithmetic & otherwise.


Bill, the issue here is not really parenthesis but the fact some compilers
will truncate the result of the division to an integer, parenthesis or not.
Multiplying first solves that problem. Knowing assembler or how the
machine REALLY works is not important; knowing what the
compiler does is.
```

###### ↳ ↳ ↳ Re: thane and mr. wolfe, you'll love this

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1998-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M4fH1.1354$eZ3.1473394@news3.mia.bellsouth.net>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net> <35ED7031.C649FEAD@att.net> <35ed7a3c.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
>Bill Lynch wrote:
>>Judson McClendon wrote:
…[19 more quoted lines elided]…
>compiler does is.


You are correct about the parentheses.  But what the compiler does is
generate machine instructions.  How can you understand that, if you
have no concept about how they work? :-)  The answer is that you must
depend on round-about descriptions which may or may not be correct or
actually address the issue at hand.  Without knowing English, I might
know, because somebody told me, that English had certain strengths or
weaknesses for expressing a given concept.  But that is a very pale
substitute for actually knowing English, and being able to evaluate
first-hand what the difficulties are.  I'll bet that very few COBOL
programmers with much assembly language experience would need to ask
why you would multiply before divide when handling fixed point numbers.
```

###### ↳ ↳ ↳ Re: thane and mr. wolfe, you'll love this

_(reply depth: 4)_

- **From:** Bill Lynch <wblynch@att.net>
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35EE15B7.11B9FC8@att.net>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net> <35ED7031.C649FEAD@att.net> <35ed7a3c.0@news1.ibm.net>`

```
Leif Svalgaard wrote:
> 
(snip)
> 
> Bill, the issue here is not really parenthesis but the fact some compilers
…[3 more quoted lines elided]…
> compiler does is.

I didn't want to take this fork in the code, but I don't use the COMPUTE
verb - too many problems with truncated results, different
implementations, etc. My point in bringing up parentheses is that coding
them even when they aren't required is good documentation.

Bill Lynch

Who does not COMPUTE :-)
```

##### ↳ ↳ Re: thane and mr. wolfe, you'll love this

- **From:** Francis A. Ney, Jr <croaker@access.digex.net>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VA.00000ed9.000ccfda@access.digex.net>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net>`

```
> From: "Judson McClendon" <judmc123@bellsouth.net>
> Date: Wed, 02 Sep 1998 14:50:56 GMT
…[14 more quoted lines elided]…
> have rarely a problem getting a COMPUTE to work as I intend.

Anyone who took and passed basic arithmetic should know this, as the compiler 
uses the standard math rules for evaluating an arithmetic expression:

PEMDAS.


Frank Ney  N4ZHG  WV/EMT-B  VA/EMT-A  LPWV  NRA(L)  GOA  CCRKBA  JPFO
Are you ready for Y2K?  Read "Time Bomb 2000" by Ed Yourdon
Abuses by the BATF  http://www.access.digex.net/~croaker/batfabus.html
```

###### ↳ ↳ ↳ Re: thane and mr. wolfe, you'll love this

- **From:** skidmike <skidmike@mindspring.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35F68A25.74901DFA@mindspring.com>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com> <kXcH1.1188$eZ3.1392688@news3.mia.bellsouth.net> <VA.00000ed9.000ccfda@access.digex.net>`

```
actually the problem turned out to be a carless mistake on my part in
not initializing all the fields to zero at the start.  so when i hit the
command compute retail-comp-1 = quantity-sto * retail-sto, for some
reason quantity-sto instead of 1.0 (as i intended) had 1.4 as a value.
i'll be more careful next time.

Francis, A., Ney, Jr wrote:
> 
> > From: "Judson McClendon" <judmc123@bellsouth.net>
…[24 more quoted lines elided]…
> Abuses by the BATF  http://www.access.digex.net/~croaker/batfabus.html
```

#### ↳ Re: thane and mr. wolfe, you'll love this

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-4pe5dMt0EKlm@Dwight_Miller.iix.com>`
- **References:** `<35ECD25C.CF4E81D2@mindspring.com>`

```
On Wed, 2 Sep 1998 05:06:37, Mike Ganas <skidmike@mindspring.com> 
wrote:

> fujitsu cobol seems to have learned math from "outcome-based education"
> now am in the programs to print estimates/invoices.  (thane has seen the
…[6 more quoted lines elided]…
> this machine and i'm not afraid to shoot!

I don't have the code here, but can you post the code and the working 
storage entries.  I think there's an intermediate result problem here.
 Let's have a look.

Put the gun down.  Slowly.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
