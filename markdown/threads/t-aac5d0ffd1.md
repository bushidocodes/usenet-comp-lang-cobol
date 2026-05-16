[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Arithmetic, what are the rules?

_10 messages · 8 participants · 2001-06_

---

### Arithmetic, what are the rules?

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-06-22T11:52:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B333155.252044D4@istar.ca>`

```
If I learned nothing else from the course in Numerical Analysis and
Programming for Digital Computers, I learned that when you actually do
the arithmetic, I learned that A*(B+C) is not necessarily (A*B) + (A*C)
depending on precision, rounding and truncation rules, etc.  I remember
being intrigued with the implications of the way you define the
problem.  This was reinforced by just recently learning that there are
at least 5 rules for rounding (unless I had forgotten what I learned in
college).  Thus I was happy and relieved to learn that there is work
being done on decimal arithmetic as opposed to binary arithmetic.  There
are proposals for rules for floating point decimal to be used for
business arithmetic.  These proposals come from the realization that
there is not good support for doing arithmetic on
computers that will give results most people expect.  Few computer
architectures provide more than minimal assistance for fixed point
decimal arithmetic let alone floating point.  You can find the proposals
for standard arithmetic and a link for the proposed Java standard at
http://www2.hursley.ibm.com/decimal.  There is also information as to
why this is important.  If you forget the link just go to Google and
search for "decimal arithmetic".

After reading all of the proposals, I have several concerns.

The first is that I don't see any indication of participation by the
accounting and financial communities in the formation of the Java
standard.  This is typical of the problem of the industry where we can't
get the users of our product interested in the implications of the
decisions we make and give us a clear definition of what they want. 
This is further compounded by what I suspect is widespread programmer
ignorance of the rules for handling rounding and intermediate results
for a given organization.  I know that in the thirty plus years I have
been working in business and systems programming (systems administration
in the Unix and NT worlds), I have never been informed of any standards
at the 5 shops I have worked at. At most there has been a vague
reference to keeping the same number of decimal places for all operands
in addition and subtraction along with avoiding the COBOL COMPUTE
statement.  This is because the rules for dealing intermediate results
were unclear.  Indeed, as I stated earlier, it wasn't until this year
that I learned that there are 5 rules for rounding.  Other than one
payroll program where I had to round to the nearest half cent, I have
always used the standard COBOL rounding (round away from zero).  Thus
those who set the rules for an organization probably are not
communicating them to the people who have to implement them.

The second is that I am concerned about the emphasis on floating versus
fixed point.  The Gross World Product expressed in Italian lire
shouldn't require more nineteen or twenty digits plus no more than eight
or nine places of decimal precision so that the current COBOL limit of
31 digit numbers should be enough for most if not all business
calculations.  A floating point number with a 31 digit coefficient seems
to be overkill and use of floating point rather than
fixed decimal precision will give different results from what is
expected in some environments.  In the proposals support is given to the
character representation of both scientific and engineering numbers. 
While there is a definite use for this format, it is not a form that the
average person is used to when looking at numbers.  I will grant that
the variety of fixed decimal formats with at least two different types
of decimal points (period and comma that I know of) and leading or
trailing signs with a variety of representations for them makes it
difficult to come up with an unambiguous way of handling
numbers.  However, one of the major uses of numbers in business is to
communicate with people who are not aware these notations exist, let
alone understand them.  The suggestions should work well with
spreadsheets. 

The third is that the proposals do not address fixed point arithmetic
which is the major part of arithmetic that I have seen in the COBOL
programs over the years.  Most of the operations are simple addition and
subtraction and much of the multiplication retains the same number of
decimal places because at most only one of the operands is not an
integer.  Indeed the question arises as to whether the hardware
optimization should be for arithmetic on formatted character numbers as
opposed to specially formed floating point numbers or even packed
decimal.  This would eliminate a lot of the reformatting that currently
takes place and would not add that much to the actual disk storage
consumed because of the compression already being done.  Data
transmission in many cases is in character format anyway for many
reasons.  In addition, I contend that any savings gained by going to
anything more exotic than packed decimal will be lost in the conversion
overhead.  It could make sense to carry the exponent, sign and
coefficient as separate pieces and load them into separate registers,
where fixed point numbers only have a sign and coefficient.

The fourth concern is that we have no linguistic support that I am know
about to handle either the rules for rounding or the rules for handling
intermediate results.  There are global option settings for intermediate
results in some of the COBOL compilers but none that allow you to
specify any of the following rules:

1.  Round half away from zero.      6.5 -> 7, -6.5 -> -7,
                                    5.5 -> 6, -5.5 -> -6.
    This is the IBM hardware rounding and the COBOL rounding.
2.  Round half toward zero.         6.5 -> 6, -6.5 -> -6,
                                    5.5 -> 5, -5.5 -> -5.
3.  Round half toward + infinity.   6.5 -> 7, -6.5 -> -6,
                                    5.5 -> 6, -5.5 -> -5.
4.  Round half toward - infinity.   6.5 -> 6, -6.5 -> -7,
                                    5.5 -> 5, -5.5 -> -6.
5.  Round half toward nearest even. 6.5 -> 6, -6.5 -> -6,
                                    5.5 -> 6, -5.5 -> -6. 
               
The use of floating point and specification for the rules on number of
digits including the guard digit may obiviate the need for rules on
intermediate results.  This however may require changes in business or
even legal requirements.  While I see nothing in this caveat to hinder
the proposals for Java decimal handling from proceeding my next caveat
may well have an implication for it.  This has more to do with
understanding what changes may be needed and what other standards and
support for business arithmetic may need to be put in place.

The final caveat is that it would be extremely valuable if the rules for
decimal arithmetic were specified the same way for all languages that
support decimal arithmetic.  This would include COBOL, Java, PL1, REXX
and various proprietary languages that I know of.  At this point it
might be that the only way to do this would be to have a user specified
option for the new common arithmetic method(s) and both global
(program-wide) and local (statement leve) ways to make this
specification.  For example, there would be qualifiers for the word
ROUNDED so that the type of rounding would be controlled. 

In closing, the issues of simple arithmetic prove to be complex.  It is
extremely encouraging to see that work is being done on the issues
surrounding decimal arithmetic.  The concerns I raise may have been
dealt with but more people have to be aware and involved.  I am even
more worried about important concerns that I don't know enough to even
have.  As said earlier, a good way to start becoming aware and involved
is to go to http://www2.hursley.ibm.com/decimal, familiarize yourself
with the material there and then communicate with the appropriate
bodies.  I urge everyone to do so.
```

#### ↳ Re: Arithmetic, what are the rules?

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-06-22T20:27:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4TNY6.283495$NK4.19880894@news2.aus1.giganews.com>`
- **References:** `<3B333155.252044D4@istar.ca>`

```

"Clark F. Morris, Jr." <cfmtech@istar.ca>
>
> After reading all of the proposals, I have several concerns.
…[3 more quoted lines elided]…
> standard.  This is typical of the problem of the industry where we
can't
> get the users of our product interested in the implications of the
> decisions we make and give us a clear definition of what they want.

The accounting and financial community have no REASON to be involved
in the JAVA standard. The original design of JAVA did not, evidently,
contemplate its use in a commercial or financial environment. To add
that capability to JAVA would bloat it even further - like putting an
oil-can on the end of a hammer.

I'm mystified by the statement '... we can't get the users of our
product interested in the implications...' If this 'product' is JAVA,
that's no big surprise.

> This is further compounded by what I suspect is widespread
programmer
> ignorance of the rules for handling rounding and intermediate
results
> for a given organization.  I know that in the thirty plus years I
have
> been working in business and systems programming (systems
administration
> in the Unix and NT worlds), I have never been informed of any
standards
> at the 5 shops I have worked at. At most there has been a vague
> reference to keeping the same number of decimal places for all
operands
> in addition and subtraction along with avoiding the COBOL COMPUTE
> statement.  This is because the rules for dealing intermediate
results
> were unclear.

Hmmm. In every COBOL vendor-supplied manual I've ever seen, there was
a section on "Intermediate Results."
```

##### ↳ ↳ Re: Arithmetic, what are the rules?

- **From:** "James" <mangogrower@telocity.com>
- **Date:** 2001-06-22T19:11:10-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com>`

```
The 'Rounding in COBOL' is NOT away from ZERO:

When the size of the fractional result exceeds the number of places provided
for its storage, truncation  occurs unless ROUNDED is specified. When
ROUNDED is specified, the least significant digit of the resultant
identifier is increased by 1 whenever the most significant digit of the
excess is greater than or equal to 5.

In a floating-point arithmetic operation, the ROUNDED phrase has no effect;
the result of a floating-point  operation is always rounded.


The first part above means that if the excess is 1 thru 4, then the least
significant digit of the
resultant identifier is left alone.

10.1 thru 10.4 = 10
10.5 thru 10.9 = 11


Jerry P <jerryp@bisusa.com> wrote in message
news:4TNY6.283495$NK4.19880894@news2.aus1.giganews.com...
>
> "Clark F. Morris, Jr." <cfmtech@istar.ca>
…[42 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Arithmetic, what are the rules?

- **From:** "Grinder" <no.spam@no.spam.spam.spam.net>
- **Date:** 2001-06-22T18:18:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JjQY6.186$PE2.43384@e420r-atl2.usenetserver.com>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com> <MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net>`

```
Does COBOL utilize "Banker's Rounding?"
```

###### ↳ ↳ ↳ Re: Arithmetic, what are the rules?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-22T21:40:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9h0vhu$1bl$1@slb7.atl.mindspring.net>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com> <MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net>`

```

"James" <mangogrower@telocity.com> wrote in message
news:MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net...
 <snip>
>
> In a floating-point arithmetic operation, the ROUNDED phrase has no
effect;
> the result of a floating-point  operation is always rounded.
>

Interesting statement, ...

This is a "well documented" behavior in IBM COBOL's (where floating point is
an "old" extension).  HOWEVER, I see no such statement in the draft of the
next COBOL Standard.  What it does say (on page 406 of the FCD) is,

"14.8.3 ROUNDED phrase
If, after decimal point alignment, the number of places in the fractional
part of the result of an arithmetic operation is greater than the number of
places provided for the fraction of the resultant identifier, truncation is
relative to the size provided for the resultant identifier. When rounding is
requested, the absolute value of the resultant identifier is increased by
one in the low-order position whenever the most significant digit of the
excess is greater than or
equal to five.

When the low-order integer positions in a resultant identifier are
represented by the symbol P in the picture character-string for that
resultant identifier, rounding or truncation occurs relative to the
rightmost integer position for which storage is allocated."

I plan on "following up" on whether this existing IBM statement is also true
(but "implied"?) in the draft Standard or not.  I think it may be "implicit"
in the reference to "the number of places in the fractional part of the
result on an arithmetic operation" but I am not at all positive of this.
```

###### ↳ ↳ ↳ Re: Arithmetic, what are the rules?

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-23T22:35:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b352403_1@Usenet.com>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com> <MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net> <9h0vhu$1bl$1@slb7.atl.mindspring.net>`

```
 Bill,

Thanks for pointing this out. (I was rather hoping you'd comment...<G>)

Isn't this a perfect example of the criticism levelled at the standard as
being in "legalese" and unreadable to mere mortals (at least, those of who
speak English...)

I would've thought that whoever wrote this (and I agree it is not an easy
concept to convey with words alone) might have been moved to give some
EXAMPLEs showing what happens...

Then there is no doubt whatsoever... If you are following this up could you
pass on this suggestion?

Thanks,

Pete.



"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9h0vhu$1bl$1@slb7.atl.mindspring.net...
>
> "James" <mangogrower@telocity.com> wrote in message
…[10 more quoted lines elided]…
> This is a "well documented" behavior in IBM COBOL's (where floating point
is
> an "old" extension).  HOWEVER, I see no such statement in the draft of the
> next COBOL Standard.  What it does say (on page 406 of the FCD) is,
…[3 more quoted lines elided]…
> part of the result of an arithmetic operation is greater than the number
of
> places provided for the fraction of the resultant identifier, truncation
is
> relative to the size provided for the resultant identifier. When rounding
is
> requested, the absolute value of the resultant identifier is increased by
> one in the low-order position whenever the most significant digit of the
…[8 more quoted lines elided]…
> I plan on "following up" on whether this existing IBM statement is also
true
> (but "implied"?) in the draft Standard or not.  I think it may be
"implicit"
> in the reference to "the number of places in the fractional part of the
> result on an arithmetic operation" but I am not at all positive of this.
…[6 more quoted lines elided]…
>


Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Arithmetic, what are the rules?

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-06-26T10:11:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hafn6$jvl$1@mail.pl.unisys.com>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com> <MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net> <9h0vhu$1bl$1@slb7.atl.mindspring.net> <3b352403_1@Usenet.com>`

```
Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
news:3b352403_1@Usenet.com...

<<I would've thought that whoever wrote this (and I agree it is not an easy
concept to convey with words alone) might have been moved to give some
EXAMPLEs showing what happens...>>

Examples are a Good Thing, I agree.  At its last meeting, J4 discussed this
general issue (not the specific issue of examples of the application of
arithmetic rules, but the issue of examples in general) at  considerable
length, and my sense of that discussion is that working examples should be
encouraged and solicited from the COBOL user community at large.   Moreover,
I believe some J4 members are investigating setting up a mechanism whereby
the collection and perhaps dissemination of examples can be accomplished.

But the FCD is currently pushing 900 pages, and incorporating examples into
that document for every construct or situation that some reader might find
confusing or vague would almost certainly bloat it way beyond manageability.
So I believe J4's inclination to be that the body of examples should be
published / disseminated separately from the standard itself, not
incorporated into the FCD.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Arithmetic, what are the rules?

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-06-26T20:23:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B38EEE5.1CD75816@home.com>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com> <MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net> <9h0vhu$1bl$1@slb7.atl.mindspring.net> <3b352403_1@Usenet.com> <9hafn6$jvl$1@mail.pl.unisys.com>`

```
Chuck,

Good. Keep plugging it and make the examples happen. Apart from clarifying for
us 'oldies' what a boon for the 'newbies'

Jimmy

Chuck Stevens wrote:

> Peter E. C. Dashwood <dashwood@nospam.enternet.co.nz> wrote in message
> news:3b352403_1@Usenet.com...
…[20 more quoted lines elided]…
>     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Arithmetic, what are the rules?

_(reply depth: 6)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-06-27T15:58:46+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b3959be_1@Usenet.com>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com> <MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net> <9h0vhu$1bl$1@slb7.atl.mindspring.net> <3b352403_1@Usenet.com> <9hafn6$jvl$1@mail.pl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:9hafn6$jvl$1@mail.pl.unisys.com...

> Examples are a Good Thing, I agree.  At its last meeting, J4 discussed
this
> general issue (not the specific issue of examples of the application of
> arithmetic rules, but the issue of examples in general) at  considerable
> length, and my sense of that discussion is that working examples should be
> encouraged and solicited from the COBOL user community at large.
Moreover,
> I believe some J4 members are investigating setting up a mechanism whereby
> the collection and perhaps dissemination of examples can be accomplished.
>
> But the FCD is currently pushing 900 pages, and incorporating examples
into
> that document for every construct or situation that some reader might find
> confusing or vague would almost certainly bloat it way beyond
manageability.

NO! I disagree SO vehemently here... What the Hell do you mean by "bloat"?

If you mean it will make the document "fat" then split it into different
volumes... (Worked for Gibbons "Decline and Fall of the Roman Empire" and
every decent Encyclopaedia that's ever been published, not to mention the
Greater Oxford Dictionary...)

If you mean that it is just added verbiage which "bloats" the document then
examples certainly DON'T fit in THAT category...

The point is that examples NEED to be IN CONTEXT. Hiving them off to an
appendix or a separate document, renders them almost useless. They should be
considered as at least as valuable as "the priceless prose" written by the
document authors and indeed, should be an essential complement to it.

> So I believe J4's inclination to be that the body of examples should be
> published / disseminated separately from the standard itself, not
> incorporated into the FCD.

How did I know that would be their attitude...?<sigh>

Pete.



Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Arithmetic, what are the rules?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-06-26T14:03:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9hamaa$q3f$1@slb5.atl.mindspring.net>`
- **References:** `<3B333155.252044D4@istar.ca> <4TNY6.283495$NK4.19880894@news2.aus1.giganews.com> <MeQY6.1188$Tk.233978@newsrump.sjc.telocity.net> <9h0vhu$1bl$1@slb7.atl.mindspring.net>`

```
I have now verified the status of "rounding" with "floating-point" in the
FCD (draft of the next COBOL Standard).

1) If an arithmetic expression uses data-items of any of the new
floating-point usages (e.g. FLOAT-SHORT, FLOAT-LONG), then the evaluation of
the entire arithmetic expression is "implementor defined".  This means that
they MIGHT (but need not) automatically ROUND even when the ROUNDED phrase
is not specified.

2) If an arithmetic expression includes a floating-point literal but all
other items are fixed-point (and not the new binary-xxxx usages), then the
following rules apply:

  A) If the "ARITHMETIC IS NATIVE" phrase is in effect (which it is - by
default for upward compatibility) then the "normal" rules apply - when
truncation is required it occurs; when rounding is specified, it occurs; and
when COMPUTE is used results are "implementor defined" as always.

 B) If the (new) "ARITHMETIC IS STANDARD" phrase is in effect, then
floating-point literals (unlike floating-point USAGEs) does NOT make the
statement "implementor defined".  Truncation and Rounding MUST apply (in a
Standard conforming implementation).


   ***

P.S.  *none* of this applies (of course) to such existing extensions as
COMP-1 or COMP-2 in IBM compilers.  In those cases, the implementor may
continue to define how they work - as they will remain "extensions".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
