[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# "nested programs" - terminology

_39 messages · 15 participants · 2001-08 → 2001-09_

---

### "nested programs" - terminology

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-08-17T17:08:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net>`

```
Given the discussions that have been going on, I thought I would suggest
some "common" terminology - that might help us to stop comparing apples with
orange Popsicles <G>.

COBOL terms:

A) Inline PERFORMs - a set of COBOL imperative statements grouped "together"
inline (in the middle of source code) delimited by the PERFORM <no
procedure-name> and END-PERFORM "statements".  These can have "UNTIL" or
"TIMES" phrases.  In ANSI/ISO '85 Standard, they may NOT have "VARYING
AFTER" phrases, but some compilers already support this as an extension -
and this will also be added in the NEXT Standard. Neither the current
Standard or the draft allow for an "unterminated" inline perform, although
at least one vendor has such as an extension.

B) Out-of-line PERFORMs - transfer of control to (and automatically back
from - unlike GO TO) a NAMED set of COBOL statements.  The name may be
either a PARAGRAPH or a SECTION name.  Such named procedures may ALSO be
referenced in GO TO, Input/Output Procedures, and implicitly by "fall thru".
Such PERFORM statements may have VARYING (with or without AFTER), UNTIL, or
TIMEs phrases.  The "traditional" COBOL PERFORM UNTIL corresponds to the
theoretical "DO WHILE" and not "DO UNTIL" often taught in "language theory".
"DO UNTIL" logic was added in the '85 Standard with the "TEST BEFORE"
phrase.

C) Externally CALLed Programs - An entire COBOL (or non-COBOL) program with
all "required" features (such as Identification Division, Data Division,
etc).  Such a program may or MAY NOT actually be maintained in separate
source code.  If it is contained in the same source code as the "main
program" - then it must immediately FOLLOW the END PROGRAM construct of the
main program and such a "compilation unit" if usually referred to as a
SEQUENCE of programs.  (This feature was new with the '85 Standard -
although some vendors had such an extension before '85).  Data is "shared"
between the main program and the "sub-program" via:
  - parameters passed/received in CALL USING/PROCEDURE DIVISION USING
statements
  - EXTERNAL Data
  - other EXTENSION methods (such as "ADDRESS OF")
Data may be passed by REFERENCE (default and oldest method) or by CONTENT -
or as an extension (currently - but in draft of next Standard) by VALUE.
The concept of "static" versus "dynamic" CALLs is *not* a part of ANSI/ISO
COBOL definition but IS common among many implementations.  It normally
(always?) relates to whether or not the subprogram is "linked" (found?
bound?) at "development" time or run-time.

D) "nested PROGRAMs" - a new feature in the '85 Standard.  The source code
for the "calling" program is identical to that used for external programs.
However, the syntax for the nested program REQUIRES that that the entire
source program for the nested program be "contained" within the "main"
program. (This MAY be done by a COPY statement - but that is certainly NOT
required.)   There are explicit (and semi-complex) rules on when a nested
program is "visible" to a containing program - and more importantly other
nested programs in the same "compilation unit"  (See particularly the COMMON
phrase).  In addition to the ways that data may be shared between
"separately compiled programs" - nested programs may ALSO view GLOBAL data
defined in the containing program. (The default is that data defined in a
containing program is NOT visible to the nested program.) However, EXTERNAL
data defined in the containing program that is not ALSO "global" is not
visible to the nested program. Syntactically a nested program and a sequence
of programs is ONLY distinguished by the location of the END PROGRAM
"marker" of the containing/1st program.

E) There is an "odd" entity in the '85 and previous Standards (but not in
the next Standard - and not implemented in many CURRENT compilers).  This is
the ENTER (not ENTRY) statement which "sort-of" allows for a (semi-)external
set of statements to be included within a COBOL source program.  I won't go
into this as I don't see this as a particularly important concept today.

  ***

"ambiguous" terms - Unlike the term "subprogram" (and program) the terms
routine and subroutine are "basically" not known in COBOL terminology.  When
talking about COBOL, it is important to distinguish between procedures
(paragraphs and sections) and program/subprogram (nested or external).
Talking about "routines" and subroutines in a COBOL discussion is LIABLE to
lead to confusion.  Talking about "procedures" from language theory (or as
used in OTHER language definitions) is liable to run into conflict with the
way this term is used in COBOL.  However, the use of this term as used in
COBOL is "well established" and would be QUITE difficult to get rid of or
modify (with little "real world" benefit to current or future COBOL
programmers)

When discussing the "advantages" (performance or maintenance" of two (or
more) features of COBOL, I would suggest that you be clear whether you are
asking or talking about:

  - Procedures (inline or out-of-line) - i.e. PARAGRAPHs/SECTIONs
 - Programs (nested, sequence, or external)

It is my  "contention" that there is no "hard" evidence (at least none that
I have seen so far) as to which of these is "GENERALLY" easier to maintain.
The one rule of thumb that PROBABLY applies is that programmers who "know"
(understand) a specific technique will find it easier to maintain than a
methodology that they don't understand or use "regularly".  It is most
definitely TRUE that "nested program" when compared to procedures allows for
"local" data and does NOT allow for "UNTIL" or "TIMES" phrases.  However,
when one is and is not an "advantage" to maintenance seems unclear (at least
to me).

Depending on the compiler (and run-time and operating system), in GENERAL,
performance can be "graded" as follows (from best to worst)

 - inline perform
 - out-of-line perform
 - nested program
 - separately compiled program (static - or compile-time "binding")
 - separately compiled program (dynamic - or "run-time" binding")

To be clear, there is almost CERTAINLY exceptions to this order (based on
optimization provided by the vendor) but I think that this is a "generally"
true order.  Equally clear, if the "logic" is only to be activated a few (or
single) time, then the performance difference is likely to be undetectable;
if the logic is activated thousands (hundreds of thousands?) of times per
application run, then this MIGHT be a significant factor in the application
design.
```

#### ↳ Re: "nested programs" - terminology

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-08-17T15:41:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lk6j3$bbe$1@mail.pl.unisys.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9lk4ni$4o0$1@slb6.atl.mindspring.net...

> Depending on the compiler (and run-time and operating system), in GENERAL,
> performance can be "graded" as follows (from best to worst)

>  - inline perform
>  - out-of-line perform
>  - nested program
>  - separately compiled program (static - or compile-time "binding")
>  - separately compiled program (dynamic - or "run-time" binding")

> To be clear, there is almost CERTAINLY exceptions to this order (based on
> optimization provided by the vendor)...

Hmmm.  I still think you might be overstating this as a general rule, Bill.
There is no particular architecture-independent reason why this order should
hold true, nor is any deviation from this order necessarily the result of
some optimization on the part of the compiler implementor.

For example, on Unisys MCP/AS COBOL85, a call on a nested program *may*
require more resources than a call on an external one of the same name if it
is necessary for the run-time system to determine whether the call is indeed
to a nested program or a separately-compiled one.

And once the linkage between the caller and the called program (nested or
otherwise) is established (ordinarily by the first CALL with no intervening
CANCEL) and presuming no further "diagnoses" of program-name scope need to
be performed, any difference in performance among these three mechanisms
should be unmeasurable because they all use the same sequence of machine
instructions.

Unisys MCP/AS distinguishes between "dynamic" determination of CALLing scope
for a "CALL <literal>" statement, which is how I am interpreting "dynamic
binding", and the entire subject of "CALL <dataname>".  Unisys supports
"CALL <dataname>" because the '85 standard requires it, but we actively
discourage our users from writing applications using the feature; the
overhead of constructing the library template, establishing the library
linkage, calling the program, and tearing it all back down again on each and
every call is quite high.    If that particular feature is what you mean by
"dynamic binding", then I agree, it's likely to be costly.  But the
"binding" necessary for CALL <literal> is sometimes dynamic as well.

    -Chuck Stevens
```

##### ↳ ↳ Re: "nested programs" - terminology

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-19T03:07:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b7e84d4_2@goliath.newsgroups.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com>`

```
Interesting...

I have some questions and observations (see below) and would appreciate your
comments, Chuck.

Pete.
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:9lk6j3$bbe$1@mail.pl.unisys.com...
>
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
> news:9lk4ni$4o0$1@slb6.atl.mindspring.net...
>
> > Depending on the compiler (and run-time and operating system), in
GENERAL,
> > performance can be "graded" as follows (from best to worst)
>
…[6 more quoted lines elided]…
> > To be clear, there is almost CERTAINLY exceptions to this order (based
on
> > optimization provided by the vendor)...
>
This looks like a very fair statement to me. I have worked on 7 different
mainframe platforms and can't think of one where this would not be true,
including Burroughs...B500 (now extinct and hardly qualifying as a
mainframe; besides, it never implemented in-line perform... ) and B3500
running under MCP.
(In case anyone is unsure of what I am saying, as has happened in the past,
I mentioned Burroughs because they were the half of Unisys which wasn't
Univac...and Chuck is quoting from a Unisys background)



> Hmmm.  I still think you might be overstating this as a general rule,
Bill.
> There is no particular architecture-independent reason why this order
should
> hold true,

Sorry Chuck, I think there is.

The list makes a logical progression from "nearest to the execution point"
to "furthest from the execution point". Bill has "covered his arse" by
saying:

 "there is almost CERTAINLY exceptions to this order (based on  optimization
provided by the vendor)..."

Despite the bad grammar (G) the statement is fair...

Taken as a whole, the above list (with its qualifier) is almost certainly
true.

In-line perform has to be "quicker" than "out-of-line" perform, especially
on systems which use virtual storage.
Even on systems with REAL addressing in real memory, it cannot be quicker to
load and execute instructions at a "far" address rather than a "near" one
(although the difference would probably be negligible)

Out-of-line perform has to be quicker than any kind of call to an external
program, even if the program is already loaded, again, because the perform
is "nearer" to the point of execution than the external program possibly
could be.

Nested programs should be allocated address space closer to the calling
program than an external "non-nested" program, so again, the same reasoning
would hold.

"Nearness to the execution point" is valid on stack based and non-stack
based architectures, in both Real and Virtual environments.

So, I  would argue that the "nearness" to the execution point IS a
"particular architecture-independent reason why this order should hold
true".



> nor is any deviation from this order necessarily the result of
> some optimization on the part of the compiler implementor.
>
> For example, on Unisys MCP/AS COBOL85, a call on a nested program *may*
> require more resources than a call on an external one of the same name if
it
> is necessary for the run-time system to determine whether the call is
indeed
> to a nested program or a separately-compiled one.
>
Why would the RTS make such a decision? It is known at compile time whether
the call is to a nested program or not. I  worked on a particular Burroughs
compiler many years ago and was impressed with their general approach. You
are shaking my confidence here... <G>
(Could it be that Univac has "dragged them down" and the "Power of two" is
really the Power of 1 diminished by another 1...<G>?)

Given that what you say is correct (I hope it isn't...) then what "extra
resources" are required? Surely it comes down to a memory load list search,
followed by a library index search, either way...? I am puzzled by this.

> And once the linkage between the caller and the called program (nested or
> otherwise) is established (ordinarily by the first CALL with no
intervening
> CANCEL) and presuming no further "diagnoses" of program-name scope need to
> be performed, any difference in performance among these three mechanisms
> should be unmeasurable because they all use the same sequence of machine
> instructions.
>
Well, yes, they are certainly executing the same sequence. The difference is
in the LOCATION of the sequence. As described above, code which is "nearer"
to the point of execution will be found fractionally quicker than code which
is "further" from the point of execution. The actual execution time (once it
is "found") SHOULD be identical, but MAY not be if dynamic relocation is
occurring or a different addressing mode is required, based on how "far" the
code is from the current execution point. In any case, "near" code MUST load
and execute faster (albeit microscopically) than "far" code.

> Unisys MCP/AS distinguishes between "dynamic" determination of CALLing
scope
> for a "CALL <literal>" statement, which is how I am interpreting "dynamic
> binding",

There is nothing dynamic about "CALL <literal>" It is resolved at compile
time and normally "static" linked (as part of the Load module) or "early
bound" at load time, on systems equipped with a linking loader.


> and the entire subject of "CALL <dataname>".  Unisys supports
> "CALL <dataname>" because the '85 standard requires it, but we actively
> discourage our users from writing applications using the feature; the
> overhead of constructing the library template, establishing the library
> linkage, calling the program, and tearing it all back down again on each
and
> every call is quite high.    If that particular feature is what you mean
by
> "dynamic binding", then I agree, it's likely to be costly.  But the
> "binding" necessary for CALL <literal> is sometimes dynamic as well.
>
I sure hope your users don't pay too much attention to your advice if this
advice is "Don't use dynamic linkage" <G>

The ability to call different modules at run time, depending on what the
circumstances dictate is an essential feature of Modular Programming. Taking
this approach means no duplication of static modules called by several
different callers, and the re-use of common modules which only need to be
maintained in one place.

For shops who have not yet cottoned to OO COBOL, Modular Programming is the
next best thing, especially for on-line systems (considerations for Batch
are different).

I believe that DYNAMIC Modular Programming is a VERY Good Thing and would
certainly not dissuade users from doing it.

If the "overheads" you describe are really such a problem, isn't it time
something was done about the system software? (How hard can it be...everyone
else does it OK?)

As for implementing it just to be compliant with the 85 Standard...would it
be fair to conclude that the implementation of the Standard has caused
Unisys to provide a very inefficient mechanism which it is now necessary to
advise customers to steer clear of <tee hee>?

Bet it won't happen with the NEW standard...<G>

Pete.




-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-08-20T02:03:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B806F8E.4056926E@istar.ca>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com>`

```
Normally, I would agree with you but I got a real shock when testing a
date routine and thought I was differentiating between a dynamic CALL
and a CALL to a nested program by using CALL data-name where data-name
was PIC X(8) VALUE 'DATERTN'.  DATERTN was also the name of the nested
program which was called by CALL 'DATERTN'.  Lo and behold, the program
checked to see if the value of the variable name was that of a nested
program and caused me to write separate test drivers.

Clark F. Morris, Jr. 

"Peter E. C. Dashwood" wrote:
> 
> Interesting...
…[9 more quoted lines elided]…
> > > more snippage < < < <
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-20T14:49:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b8079a0_9@goliath.newsgroups.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <3B806F8E.4056926E@istar.ca>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3B806F8E.4056926E@istar.ca...

> Normally, I would agree with you

Now THAT's scary...<G>!

So, I take it this is an "abnormal" post, right <G>?


> but I got a real shock when testing a
> date routine and thought I was differentiating between a dynamic CALL
…[5 more quoted lines elided]…
>

Well, it's a very good point...

Here's my defence <G> (And I stringently implement all of the points below
when using Nested Programs):

1. Check that Nested program Names are DIFFERENT to any likely external
programs. (It isn't too hard in this age of "long" program names (at least
on PCs) to concatenate the base program id with an identifier in order to
arrive at a unique nested program id...) Alternatively, use a prefix like
"nst" in the program id of the nested program to avoid any possible
confusion with external subprograms.

2. Do NOT call nested programs dynamically! (I'm not even sure that you CAN,
as I have never attempted it...sure someone will be able to quote Holy
Scripture here...).

I consider them to be "extensions" of the base program (I mentioned
elsewhere that I use them only in an Object Oriented environment to specify
Methods...) so they are always specifically invoked with a 'literal' in my
code . The reason for this is, that within the invoking code I always know
exactly which Method I want, so dynamic invocation is not necessary. With
external programs this is not always the case, and dynamic calling is an
essential part of flexible modular systems.

3. Static calls to nested programs can be resolved at compile time. There is
NO need for the RTS to try and figure it out.

Pete.



> Clark F. Morris, Jr.
>
…[5 more quoted lines elided]…
> > Why would the RTS make such a decision? It is known at compile time
whether
> > the call is to a nested program or not. I  worked on a particular
Burroughs
> > compiler many years ago and was impressed with their general approach.
You
> > are shaking my confidence here... <G>
> > (Could it be that Univac has "dragged them down" and the "Power of two"
is
> > really the Power of 1 diminished by another 1...<G>?)
> >
> > > > more snippage < < < <



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-08-20T13:43:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lrluh$me7$1@slb4.atl.mindspring.net>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <3B806F8E.4056926E@istar.ca> <3b8079a0_9@goliath.newsgroups.com>`

```
Concerning "holy writ" <G>
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

_(reply depth: 6)_

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-08-21T00:48:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdig7.998$ZN5.164902@newsread1.prod.itd.earthlink.net>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <3B806F8E.4056926E@istar.ca> <3b8079a0_9@goliath.newsgroups.com> <9lrluh$me7$1@slb4.atl.mindspring.net>`

```
Interesting. I suppose that makes it impossible or difficult to
effectively implement an informal template facility? Then again, maybe
something like that should be formal because of the potential for really
bad errors....
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-08-20T13:37:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lr3pe$bsb$1@peabody.colorado.edu>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com>`

```

On 18-Aug-2001, "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
wrote:

> In-line perform has to be "quicker" than "out-of-line" perform, especially
> on systems which use virtual storage.
…[3 more quoted lines elided]…
> (although the difference would probably be negligible)


But you're comparing source code with object code.  With smart optimizing
compilers these can be two different things.
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-21T02:56:34+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b812539_8@goliath.newsgroups.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9lr3pe$bsb$1@peabody.colorado.edu>`

```
How do you relate "near" and "far" addressing to "Source" code, Howard?

Having worked with both Source AND Object code over as many years as some
people here have been alive, I think I know the difference between
them....<G>

I was patching Object code when men were first walking on the Moon...Source
code took too long to compile in those days...

Puhleese...<G>!

See below, also...

Pete.
"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:9lr3pe$bsb$1@peabody.colorado.edu...
>
> On 18-Aug-2001, "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
> wrote:
>
> > In-line perform has to be "quicker" than "out-of-line" perform,
especially
> > on systems which use virtual storage.
> > Even on systems with REAL addressing in real memory, it cannot be
quicker
> > to
> > load and execute instructions at a "far" address rather than a "near"
one
> > (although the difference would probably be negligible)
>
> But you're comparing source code with object code.

NO! I'm NOT!

I'm talking about Object code, generated from Source code. I thought it was
obvious as soon as the words "load", "execute", and "address" were
introduced, never mind "near" and "far"...

> With smart optimizing
> compilers these can be two different things.
(Well, Source and Object are ALWAYS 2 different things, whether an
Optimizing compiler is used or not...)

Bill already mentioned the point about optimizing compilers as a rider to
his original list. No issue with that.

Yes, the compiler can re-arrange Object code as part of its optimization,
but that DOESN'T invalidate the list which Bill posted. My discourse was in
support of Bill's list and attempted to explain WHY it is so...(it
represents a logical progression based on the "current execution point" ).

(That's "OBJECT" code to you, Howard, as COBOL "SOURCE" does NOT get
executed. But you know this, and I am totally bewildered by your post...)

Don't lose sight of the point that we are discussing here.

Pete.







-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-08-20T17:23:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lrh14$h8o$1@peabody.colorado.edu>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9lr3pe$bsb$1@peabody.colorado.edu> <3b812539_8@goliath.newsgroups.com>`

```

On 20-Aug-2001, "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
wrote:

> How do you relate "near" and "far" addressing to "Source" code, Howard?
>
…[55 more quoted lines elided]…
> Don't lose sight of the point that we are discussing here.

Apparently I wasn't clear.   Or possibly I didn't understand what you were
saying.  It appeared to me that we were discussing the difference between
In-line performs, performs and nested programs.   Then it appeared to me
that I was reading how people were defining which ran the most efficiently
by comparing them to assembler code.   Maybe I missunderstood - but a
reminder to the lowest common denominator (which may be me), doesn't hurt.
As you agree - they are two different things.
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

- **From:** "Robert M. Pritchett - RMP Consulting Partners LLC" <Sending-Email-To-This-Address-Constitutes-A-Promise-To-Send-One-Thousand-Dollars-To-RMPCP@rmpcp.com?Subject=I-Am-A-Spammer-So-I-Promise-To-Send-One-Thousand-Dollars-To-RMPCP-For-Each-Message>
- **Date:** 2001-08-21T00:48:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xdig7.999$ZN5.164902@newsread1.prod.itd.earthlink.net>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com>`

```
Or is it? Can you call a nested procedure dynamically via a variable name?
Interesting - could allow for a table-driven standardized editing
facility, for example....
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-08-27T09:11:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mds1h$lef$1@mail.pl.unisys.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com>`

```
Responses interspersed:

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3b7e84d4_2@goliath.newsgroups.com...
> Interesting...
>
> I have some questions and observations (see below) and would appreciate
your
> comments, Chuck.
>
…[9 more quoted lines elided]…
> running under MCP.

Neither in-line PERFORM nor nested programs was available on these Burroughs
machines.   Of Bill's list, the only standards-compliant statement on this
list that was available on the B500 was out-of-line PERFORM, and (late)
Burroughs Medium Systems added calls to separately-compiled programs.
Neither of these architectures are currently supported.

> (In case anyone is unsure of what I am saying, as has happened in the
past,
> I mentioned Burroughs because they were the half of Unisys which wasn't
> Univac...and Chuck is quoting from a Unisys background)

Actually, I'm quoting from a background that reflects the one ex-Burroughs
architecture that remains:  the Burroughs Large System (B5-7x00), which
became the A Series, which was followed by the HMP NX and LX series, etc.;
the term I use most often is MCP/AS for this architecture.  I cannot speak
at all to what might or might not be a vendor optimization in the COBOLs on
the ex-Univac 2200 architecture.

> Sorry Chuck, I think there is.
>
…[4 more quoted lines elided]…
>  "there is almost CERTAINLY exceptions to this order (based on
optimization
> provided by the vendor)..."

The order does not apply in any sort of blanket fashion to the MCP/AS
architecture.  It is true that in-line PERFORM is faster than "out-of-line"
PERFORM on this architecture, but it is by no means a "given" that a call on
a nested program can be assumed to be faster than a statically-bound or
dynamically-bound call, depending on how you are defining the term.  And
once the "binding" is established for any of these CALLs (with the
aforementioned exception of a CALL <dataname>) the performance is *the
same*, because the machine ops generated are *the same*.

Moreover, it is a detail of machine architecture entirely outside of the
purview of the MCP/AS COBOL85 compiler as to whether the object code for a
simple "out-of-line" PERFORM is faster or slower than, for example, a
noninitial parameterless CALL on a non-initial program (be it
separately-compiled or nested).   As it happens, more "machine ops" are
involved in the former than in the most basic form of the latter, and
presuming the linkage has been established by a prior CALL I'd not be in the
least surprised if a CALL <literal> on an externally-compiled program was
somewhat faster than a simple PERFORM on some MCP/AS systems.

Point being, none of these considerations relate to Unisys *optimizations*,
they're simply characteristic of the architecture.  They aren't the result
of deliberate efforts on COBOL's behalf, they simply are because that's the
way the hardware works.   The basic instruction sequences were in use
decades before the introduction of in-line PERFORM and calls on
separately-compiled (to say nothing of nested) programs.  Nobody optimized
COBOL85 to use them, and we didn't invent the instruction sequences for CALL
to support COBOL85 (or COBOL74 or COBOL68, for that matter).

> Taken as a whole, the above list (with its qualifier) is almost certainly
> true.

It's the qualifier -- "based on optimization provided by the vendor" -- that
I'm commenting on.   'Tain't necessarily an optimization.

> In-line perform has to be "quicker" than "out-of-line" perform, especially
> on systems which use virtual storage.

I'm not sure what virtual storage has to do with it.  Certainly the
difference between in-line PERFORM and out-of-line PERFORM on MCP/AS doesn't
have anything to do with "virtual storage"; it has to do with getting to and
from the "out-of-line" code as contrasted with code that's in-line and thus
doesn't have to be "gotten to or from".  The object code on such a PERFORM
on MCP/AS differs slightly if the target of the PERFORM is in a different
object code segment, and in that sense a PERFORM on a "close" target is
likely to be a little faster than one on a "distant" one -- but user control
over this detail is not exactly straightforward, and user efforts at
optimization are best directed elsewhere, I believe.

> Even on systems with REAL addressing in real memory, it cannot be quicker
to
> load and execute instructions at a "far" address rather than a "near" one
> (although the difference would probably be negligible)

An out-of-line PERFORM could be either.  Any out-of-line PERFORM will be
more expensive than an in-line PERFORM, but I've already granted that; an
in-line PERFORM isn't to either a "far" address or to a "near" one, it's
"right here" and needn't necessarily have an address at all.  .

> Out-of-line perform has to be quicker than any kind of call to an external
> program, even if the program is already loaded, again, because the perform
> is "nearer" to the point of execution than the external program possibly
> could be.

No.  That may be true on some hardware, but it is not true on all hardware.

> Nested programs should be allocated address space closer to the calling
> program than an external "non-nested" program, so again, the same
reasoning
> would hold.

Each code segment and each data segment on MCP/AS has its own data space and
is separately addressed and managed by the operating system.  Presuming that
the information is somewhere in memory, the "distance" between any two of
these components in memory is a concept that is simply irrelevant on MCP/AS.

> "Nearness to the execution point" is valid on stack based and non-stack
> based architectures, in both Real and Virtual environments.

Maybe on systems you're familiar with.  Not necessarily on all systems.

> So, I  would argue that the "nearness" to the execution point IS a
> "particular architecture-independent reason why this order should hold
> true".

Presuming both of the code segments -- the one from which the CALL takes
place and the one that the CALL enters -- are resident in memory, the
relative distance in memory between the code segments -- or for that matter
the details of the location of either one, so long as both are indeed
resident -- is simply irrelevant to performance on MCP/AS systems.   They're
either resident or they're not .  And if one or both has been rolled out,
it's a simple PBIT to bring them back in; that, however, is independent of
the behavior of either the calling or the called program, but is rather
influenced by overall system resource utilization factors!

I can't address whether "nearness" was an issue on B500 systems, or for that
matter on B2500/B3500 systems.  But on a system in which both code and data
are addressed through descriptor-based hardware, the relative memory
locations to which any two descriptors point is simply irrelevant to how
rapidly they are accessed.

> Why would the RTS make such a decision? It is known at compile time
whether
> the call is to a nested program or not. I  worked on a particular
Burroughs
> compiler many years ago and was impressed with their general approach. You
> are shaking my confidence here... <G>

The MCP/AS COBOL85 compiler is a single-pass compiler, unlike its two-pass
COBOL74 and COBOL(68) predecessors, and unlike the the multi-pass compilers
on earlier ex-Burroughs systems.  The generation of the object code for a
CALL thus often precedes the declaration of the target as a nested program,
so when the code is generated the compiler has no way to know whether the
target is nested or not.  A compiler control option is available to defeat
this execution-time overhead for a given CALL or for the entire program.

> Well, yes, they are certainly executing the same sequence. The difference
is
> in the LOCATION of the sequence. As described above, code which is
"nearer"
> to the point of execution will be found fractionally quicker than code
which
> is "further" from the point of execution. The actual execution time (once
it
> is "found") SHOULD be identical, but MAY not be if dynamic relocation is
> occurring or a different addressing mode is required, based on how "far"
the
> code is from the current execution point. In any case, "near" code MUST
load
> and execute faster (albeit microscopically) than "far" code.

Nope.  On the systems you're familiar with, maybe.

> There is nothing dynamic about "CALL <literal>" It is resolved at compile
> time and normally "static" linked (as part of the Load module) or "early
> bound" at load time, on systems equipped with a linking loader.

Not for ANSI-compliant "external" CALL <literal> on MCP/AS.  The resolution
is at execution time and the object code files are entirely separate
entities throughout.   The closest thing to "static" linking as you describe
it is the use of USE EXTERNAL and separately-compiled subprograms with
BINDER.   It is true that if $CALLNESTED is set indicating that all CALLs
are to be resolved to nested programs and that any "missing" ones end up as
syntax errors, the linkage is done at compile time.  But only then.

> I sure hope your users don't pay too much attention to your advice if this
> advice is "Don't use dynamic linkage" <G>

Why?  CALL <dataname> is at least an order of magnitude more costly than an
equivalent CALL <literal>, in the general case.  Has been since the
introduction of COBOL74.  Most of our users simply avoid it.

> The ability to call different modules at run time, depending on what the
> circumstances dictate is an essential feature of Modular Programming.

And there are other ways to skin that same cat in MCP/AS COBOLs.

>Taking this approach means no duplication of static modules called by
several
> different callers, and the re-use of common modules which only need to be
> maintained in one place.

Yeah, and I'm not yet convinced that MCP/AS doesn't provide such
capabilities.  All I'm trying to communicate is that the *best* way to skin
that particular cat on this system may *not* be through the wholesale use of
CALL <dataname>!

> I believe that DYNAMIC Modular Programming is a VERY Good Thing and would
> certainly not dissuade users from doing it.

Recommend away.  But ...

> If the "overheads" you describe are really such a problem, isn't it time
> something was done about the system software? (How hard can it
be...everyone
> else does it OK?)

Not if there are other ways to accomplish the same thing.  The only
difference between a $SHAREDBYALL library and a COBOL85 called program is
the setting of the compiler control option.

> As for implementing it just to be compliant with the 85 Standard...would
it
> be fair to conclude that the implementation of the Standard has caused
> Unisys to provide a very inefficient mechanism which it is now necessary
to
> advise customers to steer clear of <tee hee>?

No, we provided a mechanism that worked for both CALL <literal> and CALL
<dataname>, and we noticed that there were certain dynamic requirements
associated with the latter that were not needed with the former, which meant
that the latter was a LOT more costly.  We note in our documentation that
this is the case.

I for one am not convinced that there's a *business* case for developing a
replacement for the library template mechanism that underlies the external
CALL statements for COBOL85 (and COBOL74, for that matter), and I haven't
heard all that much demand from our customers for it.    And although you've
asserted that "DYNAMIC  Modular Programming is a VERY good thing", you
haven't yet demonstrated this to be the case.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

_(reply depth: 4)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-29T01:10:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b8b986d_4@goliath.newsgroups.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com>`

```
Thanks for the response, Chuck.

It is a good argument for the most part but I am not convinced on one point:

"...the performance is *the
> same*, because the machine ops generated are *the same*."

The reason for my reservation is outlined starting from the next paragraph,
and my comments on your response are interspersed below that.

The same machine op can take different times to execute, depending on where
and how it has to fetch the data operands from. Manufacturer's timings
always assume that the data is fetched, ready for the operation. The
exception is data manipulation instructions like MOVE, where they will often
give an AVERAGE timing to fetch each byte, and there is a formula to adjust
the timings given, depending on the number of bytes being manipulated.

Modern hardware is actually being limited by the time it takes to send a
pulse down a wire or through a circuit. If electricity has to travel say 1
metre, it will take MORE  time than  if it has to travel HALF a metre
(although it is not necessarily HALF as long because there are other factors
which come into it; Quantum cookery governs it when chips are involved...).

This "distance" limitation is one of the main reasons that we have seen
successive generations of hardware getting smaller... If you can integrate
it all onto a chip you can drive it pretty close to the limit...(the limit
theoretically being the speed of light, but Relativity tells us this can
never be achieved - a particle travelling at this speed has infinite mass,
unless, like a photon, it is massless to begin with. Electrons do have mass
and therefore can never be pushed to the speed of light, even with cryogenic
systems. Note that this is even assuming there is no such thing as
resistance...).  The times we are talking about are way beyond human
perception or even comprehension, but there ARE differences. If you ran
several trillion "fetches" to memory address 001, they will complete a
fraction quicker than several trillion "fetches" to memory address 002. Why?
Because the "distance" is shorter to address 001 than it is to address 002.
At least, it is in a conventionally wired sequential Von Neumann computer
(it may not be in theoretical models like Quantum Computers or Parallel
models where every address is given its own control circuitry)

The actual difference would be far beyond our comprehension but it would be
there. Only in systems where truly concurrent memory architecture allows
parallel simultaneous fetches with duplexed hardware to implement it, can we
get over this hurdle. Even with systems which implement DMA (Direct Memory
Addressing) bussing, there are still "bank conflicts" which cause requests
to "wait" while the control circuitry queues requests for a given piece of
address space. This was much more visible in the old days when we threaded
donuts on wire lattices, but the principle is still true today, and will
remain so as long as control circuitry is required to "manage" a piece of
address space.

All kinds of clever schemes to minimise these effects or circumvent them
have been implemented by manufacturers over the years. This is why we have
seen PCs gradually evolving from 8 bit through 16 to 32 bit architecture. It
is better to fetch 32 bits (even if you don't immediately need them all)
than to fetch 8... chances are that your next "fetch" will require something
"close" and it is already available in a hardware register... We can expect
this to continue extending until the law of "diminishing returns" renders it
pointless (probably somewhere around 512 bit architecture...but that is just
a guess).

Lookahead caches and hardware to drive them, are all attempts to minimise
this effect. But they can NEVER eliminate it completely, without radical
change to the fundamental hardware, which would render the system so
expensive it would not be a viable economic proposition.

I therefore remain convinced that the principle of things "nearer to the
execution point" executing faster than "things further from the execution
point" is valid for all sequential Von Neumann hardware, although I respect
your right to disagree.

Further comments below...

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:9mds1h$lef$1@mail.pl.unisys.com...
> Responses interspersed:
>
> > Sorry Chuck, I think there is.
> >
> > The list makes a logical progression from "nearest to the execution
point"
> > to "furthest from the execution point". Bill has "covered his arse" by
> > saying:
…[4 more quoted lines elided]…
>
<snipped points in agreement>

> The order does not apply in any sort of blanket fashion to the MCP/AS
> architecture.  It is true that in-line PERFORM is faster than
"out-of-line"
> PERFORM on this architecture, but it is by no means a "given" that a call
on
> a nested program can be assumed to be faster than a statically-bound or
> dynamically-bound call, depending on how you are defining the term.  And
> once the "binding" is established for any of these CALLs (with the
> aforementioned exception of a CALL <dataname>) the performance is *the
> same*, because the machine ops generated are *the same*.

I have a problem with the last statement... see my discourse above..<G>

>
> Moreover, it is a detail of machine architecture entirely outside of the
…[5 more quoted lines elided]…
> presuming the linkage has been established by a prior CALL I'd not be in
the
> least surprised if a CALL <literal> on an externally-compiled program was
> somewhat faster than a simple PERFORM on some MCP/AS systems.
>
OK, that's fair comment. I find it remarkable, but will accept your
assurance that that is how it works on Unisys.

> Point being, none of these considerations relate to Unisys
*optimizations*,
> they're simply characteristic of the architecture.  They aren't the result
> of deliberate efforts on COBOL's behalf, they simply are because that's
the
> way the hardware works.   The basic instruction sequences were in use
> decades before the introduction of in-line PERFORM and calls on
> separately-compiled (to say nothing of nested) programs.  Nobody optimized
> COBOL85 to use them, and we didn't invent the instruction sequences for
CALL
> to support COBOL85 (or COBOL74 or COBOL68, for that matter).
>
This is also a very valid point. Most hardware vendors DON'T build
architecture to support COBOL...

> > Taken as a whole, the above list (with its qualifier) is almost
certainly
> > true.
>
> It's the qualifier -- "based on optimization provided by the vendor" --
that
> I'm commenting on.   'Tain't necessarily an optimization.
>

Ah, that is a fine shade of meaning which I had missed. Are you arguing that
"optimization" as provided for COBOL "ain't necessarily so" at least on
Unisys platforms?

> > In-line perform has to be "quicker" than "out-of-line" perform,
especially
> > on systems which use virtual storage.
>
> I'm not sure what virtual storage has to do with it.

Virtual storage can affect it substantially. "Near" code is likely to be on
the current virtual page; "far" code isn't. Sometimes, of course, even the
"near" code requires a virtual page fetch (current execution is close to the
page boundary)  but it should always be to a virtual page whose address is
nearer than any other virtual page address (in effect, the NEXT sequential
virtual page. Modern Operating systems go to some pains to ensure that this
page is already loaded in memory...)


> Certainly the
> difference between in-line PERFORM and out-of-line PERFORM on MCP/AS
doesn't
> have anything to do with "virtual storage"; it has to do with getting to
and
> from the "out-of-line" code as contrasted with code that's in-line and
thus
> doesn't have to be "gotten to or from".

Isn't that exactly the principle I just described above?


> The object code on such a PERFORM
> on MCP/AS differs slightly if the target of the PERFORM is in a different
> object code segment, and in that sense a PERFORM on a "close" target is
> likely to be a little faster than one on a "distant" one -- but user
control
> over this detail is not exactly straightforward, and user efforts at
> optimization are best directed elsewhere, I believe.
>

Good. So we agree on this.

Your last sentence is a very good one. It is a whole different argument
whether we should leave this type of "optimization" to the User or the
system, or a combination of both.

> > Even on systems with REAL addressing in real memory, it cannot be
quicker
> to
> > load and execute instructions at a "far" address rather than a "near"
one
> > (although the difference would probably be negligible)
>
…[4 more quoted lines elided]…
>
Hmmmm...I'd be interested to see hardware which can implement instructions
with no "address at all" <G>, but I catch your drift...you are saying the
CURRENT execution point could be the in-line perform. This is a special case
of my argument regarding near and far...you can't get any nearer than "here"
<G>. ("Heaven is being perfect. Perfect speed is just being there." -
Jonathan Livingstone Seagull)



> > Out-of-line perform has to be quicker than any kind of call to an
external
> > program, even if the program is already loaded, again, because the
perform
> > is "nearer" to the point of execution than the external program possibly
> > could be.
>
> No.  That may be true on some hardware, but it is not true on all
hardware.
>

Oh, yes it is...<G> (chorus in background..."Oh, NO, it isn't..."...."look
out behind you!")

I'll try and persuade you by explaining my argument... Would you accept that
an out-of-line perform will be loaded into the same address space as the
program containing it? (kind of axiomatic really, so not so hard to agree
to...).

Then, would you further agree that an external program will NOT be loaded
into this same space? (again, a no brainer...).

Now, given that all the "overheads" you mentioned regarding the loading of
the external program have been completed, and it is resident, we MUST
conclude that it HAS to be "further" away than the space containing the
current execution point and the out-of-line perform.

Therefore, the out-of-line perform has to be quicker to get to than the
external program. QED.

For this NOT to be true, it would require a system that loaded external
programs into space occupied by already executing programs. From an
Operating System point of view this would be complex to manage and
disastrous when it  (almost inevitably) failed. I can imagine a complex
system which "interleaved" pages of virtual memory WITHOUT keeping
individual address spaces inviolate, but I have never seen one and I can't
believe this is implemented on Unisys. (I WILL believe it if you say
so...<G>).


> > Nested programs should be allocated address space closer to the calling
> > program than an external "non-nested" program, so again, the same
…[3 more quoted lines elided]…
> Each code segment and each data segment on MCP/AS has its own data space
and
> is separately addressed and managed by the operating system.  Presuming
that
> the information is somewhere in memory, the "distance" between any two of
> these components in memory is a concept that is simply irrelevant on
MCP/AS.
>
Yes, the concept is  totally irrelevant from a programming point of view
(Thank Goodness...<G>!).
But it is NOT irrelevant when it comes to timing. If, as you mention, these
spaces (data and instruction segments) are managed by the OS, then context
switching must occur in order to execute them. If your argument here is that
a nested sub-program is "indistinguishable" from an external called program
(and I think that is what you are saying ??), then you are absolutely
correct from the point of view of a programmer, and I also agree that the
times involved are totally irrelevant to a Human (let's include "Programmer"
in the set of things "Human"...<G>).

However the system sees things differently...

Some spaces will be closer to the current execution point than others. I
think we have agreed that "near" things will be executed faster than "far"
things, even though the differences may be (and usually are) far beyond
human comprehension... (If you haven't agreed to this, then our discussion
cannot be continued because I can't agree to the converse <G>). Given that,
then the same arguments over system timing apply and nested sub-programs
WILL execute quicker than external called programs because they are closer
in the address space to the current execution point. (This is assuming that
LOAD overheads, parameter passing, library template access on your system,
and all the other "variables" are the same, so we are comparing apples with
apples...)


> > "Nearness to the execution point" is valid on stack based and non-stack
> > based architectures, in both Real and Virtual environments.
>
> Maybe on systems you're familiar with.  Not necessarily on all systems.
>
Sorry, you have failed to persuade me of this, for the reasons outlined
above. I DO agree that programmer perception is not necessarily the same,
but hardware is hardware. There are only certain things you can do with it.

> > So, I  would argue that the "nearness" to the execution point IS a
> > "particular architecture-independent reason why this order should hold
…[4 more quoted lines elided]…
> relative distance in memory between the code segments -- or for that
matter
> the details of the location of either one, so long as both are indeed
> resident -- is simply irrelevant to performance on MCP/AS systems.
They're
> either resident or they're not .

No it isn't from the system point of view. It certainly is from the
programmer's point of view.

This is based on the perception that all addresses in a given address space
are accessed in exactly the same time. That is a fine working postulate for
an application Programmer.  I'm not arguing that.

It is NOT a fine perception for an OS designer or true System Programmer or
anyone whose job it is to improve/optimize system performance. The fact is
that most of these differences cannot be demonstrated because they are so
small, and there are many other things which can make much more measurable
differences to overall system throughput.

What I am saying is that when all these other differences are removed
(cancelled out, if you like) there IS a difference between accessing "near"
addresses and accessing "far" ones. It is NOT true to invoke the Programmer
perception and say "It's all the same."

Therefore, Bill's list (which is what this discussion is all about) MUST be
true because it is based on this concept.


>And if one or both has been rolled out,
> it's a simple PBIT to bring them back in; that, however, is independent of
> the behavior of either the calling or the called program, but is rather
> influenced by overall system resource utilization factors!
>
Exactly! So you agree that your PBIT can have different execution times,
depending on resource utilization factors. The address of a program space is
just such a factor, whether you recognize it as such or not. (I think we may
be closer to agreement than either of us realised...<G>)


> I can't address whether "nearness" was an issue on B500 systems, or for
that
> matter on B2500/B3500 systems.  But on a system in which both code and
data
> are addressed through descriptor-based hardware, the relative memory
> locations to which any two descriptors point is simply irrelevant to how
> rapidly they are accessed.
>
No it isn't, for the reasons discussed at length above. I agree it SEEMS
that way, but in reality it isn't and it cannot be.

However, the differences are microscopic...nevertheless they are
differences. The reason for this is that current takes longer to flow over a
longer distance than it does over a shorter one, even if the difference in
length is tiny. Memory control circuitry recognises this and that is why
memory access is divided into individually controllable sections. (In the
old days they were called "banks" because they were physically located on
separate "planes" of ferrite cores. Nowadays, with integrated memory chips,
the "distances" involved are much tinier (and the cycle times to read a byte
correspondingly quicker...) but the control logic is still present on the
chip and "bank conflicts" can still occur. It is just transparent to the
COBOL programmer so a popular (and perfectly valid  for normal working
purposes) perception that ALL memory access takes the same time, arises. It
isn't true, but to all intents and purposes (at least in our "reality") it
might as well be...)


> > Why would the RTS make such a decision? It is known at compile time
> whether
> > the call is to a nested program or not. I  worked on a particular
> Burroughs
> > compiler many years ago and was impressed with their general approach.
You
> > are shaking my confidence here... <G>
>
> The MCP/AS COBOL85 compiler is a single-pass compiler, unlike its two-pass
> COBOL74 and COBOL(68) predecessors, and unlike the the multi-pass
compilers
> on earlier ex-Burroughs systems.

OK, you covered it with "multi-pass"...

My statement assumed that calls to nested sub-programs would be static ('cos
that's how I use them...<G>), but I realise now that this is not necessarily
the case and my comment therefore is not fair. I withdraw it.

>
> > There is nothing dynamic about "CALL <literal>" It is resolved at
compile
> > time and normally "static" linked (as part of the Load module) or "early
> > bound" at load time, on systems equipped with a linking loader.
>
> Not for ANSI-compliant "external" CALL <literal> on MCP/AS.  The
resolution
> is at execution time and the object code files are entirely separate
> entities throughout.   The closest thing to "static" linking as you
describe
> it is the use of USE EXTERNAL and separately-compiled subprograms with
> BINDER.   It is true that if $CALLNESTED is set indicating that all CALLs
> are to be resolved to nested programs and that any "missing" ones end up
as
> syntax errors, the linkage is done at compile time.  But only then.
>

Ah, so it can be handled with compiler options. Fair enough...

> > I sure hope your users don't pay too much attention to your advice if
this
> > advice is "Don't use dynamic linkage" <G>
>
> Why?  CALL <dataname> is at least an order of magnitude more costly than
an
> equivalent CALL <literal>, in the general case.  Has been since the
> introduction of COBOL74.  Most of our users simply avoid it.
…[5 more quoted lines elided]…
>

On some other occasion, I'd be REALLY interested to see how this is achieved
if you DON'T use late binding...


> >Taking this approach means no duplication of static modules called by
> several
> > different callers, and the re-use of common modules which only need to
be
> > maintained in one place.
>
> Yeah, and I'm not yet convinced that MCP/AS doesn't provide such
> capabilities.  All I'm trying to communicate is that the *best* way to
skin
> that particular cat on this system may *not* be through the wholesale use
of
> CALL <dataname>!
>
And I am suggesting that the ONLY way (I can think of) to achieve the above
is by Late Binding or Dynamic Linkage, unless you go to Object Orientation,
which is probably beyond the scope of this discussion.

I HATE suggesting that ANYTHING is "the only way", (and would be the first
to agree that my vision is limited by past experience which does not include
Unisys) so I would be very interested to see alternatives for achieving the
same goals, that were just as viable as dynamic calls.

> > I believe that DYNAMIC Modular Programming is a VERY Good Thing and
would
> > certainly not dissuade users from doing it.
>
> Recommend away.  But ...
>


> > If the "overheads" you describe are really such a problem, isn't it time
> > something was done about the system software? (How hard can it
…[6 more quoted lines elided]…
>
This does not address the issue of dynamic calling, based on specific
circumstances at run time. Simply ensuring that only one copy is available
to all callers doesn't help with WHICH program is called....



> > As for implementing it just to be compliant with the 85 Standard...would
> it
…[7 more quoted lines elided]…
> associated with the latter that were not needed with the former, which
meant
> that the latter was a LOT more costly.  We note in our documentation that
> this is the case.
>
(Good response...and you didn't rise to my bait...<G>)
It may be a "lot more costly" in terms of system overhead (and we don't need
to argue that that is probably the case) but if it returns benefits in terms
of application flexibility  and maintenance then that needs to be balanced a
gainst the downside. I applaud the fact that the manual makes it clear that
this will be less efficient. Is there a User Manual which explores why you
might want to use it anyway?


> I for one am not convinced that there's a *business* case for developing a
> replacement for the library template mechanism that underlies the external
> CALL statements for COBOL85 (and COBOL74, for that matter), and I haven't
> heard all that much demand from our customers for it.

Ah, the old "Business Case" justification... Usually interpreted as "I have
lost this argument on technical grounds but I'll shift the ground to the
Application area and try pursuing it there..."<G>.

Nobody, (least of all in an environment where their tech support advises
them NOT to do something) is going to try and make a Business Case for doing
it... That doesn't mean that there isn't one.

But you have had some customers express some dissatisfaction with the
current arrangement?
(It's OK, in a public forum, I wouldn't really expect you to answer this; I
just have to ask...<G>)

 Without knowing a lot more about your "library template mechanism" I cannot
comment. I note you said in previous post that it had to be set up and
destroyed for every call and that strikes me as being unfortunate.


> And although you've
> asserted that "DYNAMIC  Modular Programming is a VERY good thing", you
> haven't yet demonstrated this to be the case.
>
Well, actually, I have. In numerous other places and on numerous other
occasions. But you're right, I haven't done so here. Obviously I arrived at
the stated conclusion after trying this and alternative approaches in many
different environments....(But, to be fair, none of these was Unisys...)

Summing up:

1. The truth or otherwise of the statement: "Access to near addresses has to
be faster than access to far addresses" remains open to question.

I am persuaded that it is true, irrespective of hardware, if we look at what
must happen at a physical hardware level.

You believe it is not, because of certain features implemented in the Unisys
range, but I believe your perception is based on a Programming viewpoint
rather than an engineering one.

2.  We agree that there other factors which will affect performance much
more greatly than the location of code. (This discussion comes down to what
happens when all those other factors are cancelled out or equal).

3. Bill's original "performance list" (whether it was stated or not at the
time) is a logical progression based on the postulate in "1" above. I
therefore agree with it. You say it is not necessarily so for Unisys
hardware. But, again, I believe you are considering the programming
interface rather than the actual hardware.

4. We disagree about the relative merits of Dynamic Modular Programming. It
is inefficient and not recommended on Unisys equipment. But you say there
are other ways of implementing the same effect. I can't think of any, but
I'm not prepared to push this argument because it is superseded by Object
Oriented programming anyway...

Looks like we will agree to differ, having explored some of these arguments.
I do feel that your response was very fair (thanks for that) and take no
issue with it, except where stated above.

I am now quite fascinated to look at Unisys hardware/software... but it will
have to wait...<G>

Pete.



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Memory Architectures (was Re: "nested programs" - terminology)

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-08-28T12:38:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mgrus$82a$1@mail.pl.unisys.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com>`

```
Rather than reproduce the twelve pages of text Peter Dashwood provided in
his response of 8/28 on the previous topic, I'm starting a new topic.

Probably most symptomatic of the misunderstanding is your paragraph

<<Virtual storage can affect it substantially. "Near" code is likely to be
on the current virtual page; "far" code isn't. Sometimes, of course, even
the "near" code requires a virtual page fetch (current execution is close to
the page boundary)  but it should always be to a virtual page whose address
is nearer than any other virtual page address (in effect, the NEXT
sequential virtual page. Modern Operating systems go to some pains to ensure
that this page is already loaded in memory...) >>

Unisys MCP/AS does NOT rely on the concept of a "virtual page fetch" for
transfers of control from one object code segment to another in the sense
that, for example, IBM S/370 virtual memory did.

Every memory space is independently allocated -- data, code, control
structures, whatever.  The concept of a single contiguous memory space is
largely foreign to the MCP/AS memory architecture ("save memory" is a
special case not applicable to COBOL).  Where a code segment, or a data
space, is located in memory is pretty much a matter of chance, not just at
initialization time but between any two accesses to the code or data space.
The memory spaces associated with the execution of any given program are
*dynamically* scattered all over the system, pretty much randomly, and in a
much more fragmentary manner than you seem to be expecting!

In MCP/AS COBOL74, in fact, every 01-level item in WORKING-STORAGE is
allocated independently when it is first "touched", and if it isn't
"touched", no memory space is allocated for it.  There is no danger of
overwriting from the data space belonging to one 01-level record into that
belonging to another (or into any other structure); such is prevented very
effectively by the hardware.  And the 01-level record associated with one
program could end up being adjacent in memory to just about anything else on
the system; it's rather unlikely, in fact, that it would end up being
adjacent to anything particularly related to the program that owns it.
COBOL85 tends to allocate larger chunks of working-storage memory ("pooling"
01-level and 77-level records rather more like a Pascal heap), but it is
still impossible to go outside the bounds of the overall memory space, and
the memory space required for this structure is determined by the compiler
at compile time.  From the MCP standpoint, it's a single memory space devoid
of subdivision; the operating system thinks it's a single record.

Object code segments (and other static structures) are NEVER modified in
memory.  They always appear in memory exactly as they appear on disk within
the object code file, and are retrieved from there as needed.  Fifty copies
of the same object program executing simultaneously share THE SAME copy of
the object code file on disk, and THE SAME copy of the static structures
from the object code file in memory.  Since the object code segments are
static, the detection of transition from one code segment to the next is the
job of the compiler.  The first user of an object code file segment will
encounter an interrupt when it attempts to access it; the MCP handles this
by making the code segment available and restarting the control transfer
operation once the appropriate stack cell has been updated to point to the
now-resident segment.  If the MCP should decide that it needs the memory
space occupied by a code segment, it simply marks the descriptor for that
memory space "absent", and it is immediately available for the next
requestor for memory.  This is all handled by a combination of hardware and
software, and it is a mechanism that in one form or another has worked very
welll for Unisys for around four decades.

This leads to:

<<I'll try and persuade you by explaining my argument... Would you accept
that an out-of-line perform will be loaded into the same address space as
the program containing it? (kind of axiomatic really, so not so hard to
agree  to...).>>

Axiomatic perhaps on systems that have dedicated "address spaces", for data
and/or code, but that's not Unisys MCP/AS.  There is no general concept of
an "address space" associated with the execution of a program aside from the
stack itself.

The object code for the out-of-line PERFORM is in the object code segment
from the object code file that's currently being executed and it's most
likely in memory, and I'll agree that that's pretty much axiomatic, but
that's about as much as you can say about it.

If the object code segment containing the *target* of the PERFORM has never
been "touched", the hardware will recognize that, the software will load the
code segment from disk into memory (and just about anywhere in memory),
update the descriptor to indicate its resident status, and restart the
dynamic branch that received the presencebit interrupt.

With respect to in-line and out-of-line PERFORMs:

<<Hmmmm...I'd be interested to see hardware which can implement instructions
with no "address at all" <G>, but I catch your drift...you are saying the
CURRENT execution point could be the in-line perform. This is a special case
of my argument regarding near and far...you can't get any nearer than "here"
<G>. ("Heaven is being perfect. Perfect speed is just being there." -
Jonathan Livingstone Seagull) >>

MCP/AS COBOL85 generates no code at all -- with or without addresses -- for
    PERFORM CONTINUE END-PERFORM
and I don't think that's an optimization -- there's nothing to generate.
For
    PERFORM 100 TIMES CONTINUE END-PERFORM
all addresses are within the current object code segment.  There is no "go
out" logic or "come back" logic as there is for an out-of-line PERFORM.  The
difference between the "in-line" and "out-of-line" PERFORM is precisely the
"go out" and "come back" logic.

If the out-of-line PERFORM is to a location *in the same code segment*, the
instruction that takes you to the target is a "static" one, faster than the
"dynamic" one required if the target's in a different code segment.  Getting
back still requires a dynamic branch.  The difference is small, but
measurable.

<<Then, would you further agree that an external program will NOT be loaded
into this same space? (again, a no brainer...).>>

The "space" an object code segment is loaded into for an external program is
not the same space as the CALL -- but then neither is the paragraph being
PERFORMed, if it's in a different code segment!  Any presumptions about
"distance" or "proximity" between the paragraph or section being PERFORMed
and an already-linked external program being CALLed apply equally to either
one.

<<Now, given that all the "overheads" you mentioned regarding the loading of
the external program have been completed, and it is resident, we MUST
conclude that it HAS to be "further" away than the space containing the
current execution point and the out-of-line perform.>>

Perhaps *you* must, Peter, but you haven't convinced me that the Unisys
MCP/AS system actually can't do what it and its ancestors have been doing
since the days of the Burroughs B5000 ...

<<Therefore, the out-of-line perform has to be quicker to get to than the
external program. QED.>>

I could go into the MCP/AS machine operators generated for each of these
cases, but I think most of the readership would find it boring.  Suffice it
to say that QED wasn't.

<<For this NOT to be true, it would require a system that loaded external
programs into space occupied by already executing programs.  From an
Operating System point of view this would be complex to manage>>

Without hardware support, yes, it might.  But since the invention of the
Burroughs B6500 some decades back the subject system has had exactly such
hardware support.  It may be complex to manage, but that's the operating
system's job, and it's been pretty successful at it for a very long time!

<<and disastrous when it  (almost inevitably) failed. I can imagine a
complex system which "interleaved" pages of virtual memory WITHOUT keeping
individual address spaces inviolate, but I have never seen one and I can't
believe this is implemented on Unisys. (I WILL believe it if you say
so...<G>).>>

Over and above the 48-bit "data bits" associated with memory words on the
Burroughs B6700 system and all its descendants, the hardware includes "tag
bits" indicating what sort of information was located in that word, and
hardware support involving those tag bits and involving the limits in the
"descriptors" that delimit every memory space in the system, prevent the
misuse of memory.  As all memory addressing is indirect, it is relatively
straightforward for the hardware to make sure that a given "write" to memory
doesn't exceed the limits specified in the descriptor, and to prevent the
overwriting of memory spaces that are occupied by other than data.   An
attempt to overwrite a code word triggers a *hardware interrupt*.  An
attempt to store a single-precision item on the stack into a
double-precision word triggers a *hardware interrupt*.  An attempt to store
information past the end of a memory space triggers a *hardware interrupt*.
This brief dcescription is a gross oversimplifcation of the way it all
works, but suffice it to say that whether you can bring yourself to accept
that anybody could accomplish such a feat, I'd have to respond that
Burroughs did so over thirty years ago, and Unisys continues to do so to
this day.

<<However the system sees things differently ...

Some spaces will be closer to the current execution point than others ... >>

Problem is, Peter, that "nearness" and "farness", as you have described it,
is independent of whether the association between the two code segments is
the result of a CALL or a PERFORM, and again using your definition may
actually vary significantly between any two executions of the CALL or the
PERFORM in a given execution of the calling or performing program.  The
concept of "near" vs. "far" in the "address space" is a concept foreign to
the MCP/AS system.  There is no "address space" to be "near" or "far" in.
There are MORE instructions in the theoretical minimum code necessary to
produce an out-of-line PERFORM and come back than in the theoretical minimum
object code necessary to produce a CALL and to return from the CALLed
program (though I grant that both theoretical minima are unlikely).   Given
hardware support for address translation through the descriptors, and
presuming all structures are present, why will the SHORTER sequence of
machine instructions incontrovertibly take more resources than the LONGER?

<<Given that, then the same arguments over system timing apply and nested
sub-programs WILL execute quicker than external called programs because they
are closer in the address space to the current execution point.>>

Nope.

Nested subprograms are no "closer" in the address space because there is no
address space associated with code for the program.  (There is a memory
stack space, for data and descriptors, but neither the code nor the
individual memory spaces referenced by the descriptors is there).

The resident object code for a nested subprogram is in an object code
segment that is no "nearer" nor "farther" from the current execution point
than the object code for an external program -- or for that matter to a
paragraph in a different code segment in the same program that's the target
of either a PERFORM or GO TO.   Or even to the code segment you "fall into"
because you "fell out of" the one you were executing in.   The concepts of
"near" and "far" simply do not apply.

<<It is NOT a fine perception for an OS designer or true System Programmer
or anyone whose job it is to improve/optimize system performance.>>

Unisys has historically prided itself in that its customers rarely require
"true System Programmers" like those of some other vendors might.  The
characteristics of memory management that might be applicable to one MCP/AS
system would likely be a disaster on another.  Poking around in the memory
management schemata of the Unisys MCP/AS operating system and associated
software is an activity we *strrongly* recommend be left to the plant.

<<The fact is that most of these differences cannot be demonstrated because
they are so small ...>>

THAT I most definitely agree with!

<<What I am saying is ... there is a difference between accessing "near"
addresses and "accessing "far" ones.  It is NOT true to invoke the
Programmer perception and say "it's all the same." >>

What is a "near" address this microsecond may well be a "far" address next
microsecond, and vice versa.  A descriptor pointing to a memory space can at
least theoretically point to a different memory space, located anywhere on
the system, each time it's touched.  That's as true of code as it is of
data.

<<Therefore, Bill's list (which is what this discussion is all about) MUST
be true because it is based on this concept.>>

Yes, it's based on the concept of an "address space" in which all parts of
an executing program reside.   And I could even agree that *for systems that
have such a monolithic memory space* Bill's list could arguably be presumed
true.  But it just can't be applied outside of that particular view of how
computers operate.

But the Unisys MCP/AS exists in a worldview in which code and data NEVER
coexist in the same memory space.

It is an environment in which the system loads an object code segment into a
memory location without any regard for which of any number of executions of
the object program of which it's a part asked for it, or where the other
code or data structures associated with that execution might be located.

It is an environment in which *any number* of executions of the same object
code file share *a single* copy of that object code file (including its
individual code segments) in memory as well as on disk.  The stack
associated with a given execution has pointers to a table maintained by the
operating system (for all executions) that contains the descriptors to the
individual code segments.

Bill's list is arguably applicable to some systems.  But not to all, and the
assertion is that the list is universally true on philosophical grounds.
Not all languages share assumptions that may be valid for Indo-European; not
all architectures share assumptions that may be valid for IBM.

     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Memory Architectures (was Re: "nested programs" - terminology)

_(reply depth: 6)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2001-08-28T19:09:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0108281809.6644c444@posting.google.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mgrus$82a$1@mail.pl.unisys.com>`

```
Chuck,

I really enjoyed this response and found it fascinating.

Obviously the combination of hardware/software in the Unisys systems
is quite unique.

I am persuaded by your arguments that it really IS a different case.

Thanks for that.

Pete.

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message news:<9mgrus$82a$1@mail.pl.unisys.com>...
> Rather than reproduce the twelve pages of text Peter Dashwood provided in
> his response of 8/28 on the previous topic, I'm starting a new topic.
…[259 more quoted lines elided]…
>      -Chuck Stevens
```

###### ↳ ↳ ↳ Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-08-28T13:26:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mguqa$9f6$1@mail.pl.unisys.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com>`

```

"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3b8b986d_4@goliath.newsgroups.com...

<major snippage>

> > > The ability to call different modules at run time, depending on what
the
> > > circumstances dictate is an essential feature of Modular Programming.
> >
…[3 more quoted lines elided]…
> On some other occasion, I'd be REALLY interested to see how this is
achieved
> if you DON'T use late binding...

Personally, I think the cases in which you truly *need* the capability of an
absolutely arbitrary title in a CALL dataname statement are very, very
limited.  I think, rather than
    CALL PROGRAM-TITLE USING ...
since you know you're going to crash-and-burn if the library you try to call
is invalid anyway, most instances of "dynamic modular programming" could be
served, instead by something like:
    EVALUATE PROGRAM-TITLE
    WHEN "PROGRAM-A" CALL "PROGRAM-A" USING ...
    WHEN "PROGRAM-B" CALL "PROGRAM-B" USING ...
                    ...
    WHEN OTHER CALL "INVALID-LIBRARY" USING ...
    END-EVALUATE  ...

In either case the choice is dynamic; the point is that rarely is the list
of choices truly infinite.  This approach also has the advantage of
providing a current centralized list of valid routines for the context, and
a straightforward way to protect programmatically against the possibility of
an invalid program-title (instead of reacting to it)!

I agree that determining which program to CALL at execution time is a
central feature of "dynamic modular programming", but I fail to see why the
list of possible program-titles that one could call must be absolutely
indeterminate until execution time, or that the determination must reside
strictly within the confines of the CALL statement itself, to allow the
implementation to qualify as dynamic in this context.   Is there something
I'm missing in your definitions or criteria?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 6)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2001-08-28T18:56:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0108281756.248ce6bb@posting.google.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com>`

```
Trying this through Google for the first time, bear with me...<G>

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message news:<9mguqa$9f6$1@mail.pl.unisys.com>...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
> news:3b8b986d_4@goliath.newsgroups.com...
…[19 more quoted lines elided]…
> is invalid anyway, most instances of "dynamic modular programming" could be

Well, one of the reasons we do testing is to ensure that we WON'T
"crash and burn"... I have designed and built Dynamic Modular Systems
on a number of platforms and NEVER had a dynamic call crash in
Production.

But the MAIN reason for using this approach is the SAME reason that I
write "generalised" solutions, rather than "one-off" ones... It saves
me time and effort in the long run. Investing some time now to turn a
specific solution into a generalised concept repays itself many times
over. (You can start to understand why I am a devotee of Components
and OO technology...).

In the absence of OO, dynamic modular programming allows a generalised
flexible solution to be developed. Static linking doesn't.

> served, instead by something like:
>     EVALUATE PROGRAM-TITLE
…[5 more quoted lines elided]…
>

> In either case the choice is dynamic; the point is that rarely is the list
> of choices truly infinite.  This approach also has the advantage of
…[3 more quoted lines elided]…
> 
This is a stilted and inflexible attempt to provide the same service
as a dynamic call. It fails dismally. Here are my main objections to
it:

1. I have to recompile every calling program when I write a new called
module (and there could be hundreds of them...)

2. It does not allow me to "compute" the name of a module, based on
the installation standard naming conventions.

3. What if your EVALUATE requires say, 100 programs? Am I supposed to
include this into every possible calling program?

True dynamic calling allows me to decide what I am going to call based
on ANY criteria I like (Not just an EVALUATE). It could be the outcome
of several modules working together which will decide what function is
now required and construct the appropriate module name based on naming
standards. In a development environment, the module may not even exist
yet. (If we don't want to provide a stub for it we could use ON
EXCEPTION with the call.) When it DOES exist, I do not have to
re-compile every program that calls it, it just succeeds.

Both Development and Production can benefit from dynamic modular
programming.

However, Object Orientation is the ultimate extension of this and
provides all the benefits plus more. I therefore see this as
"outmoded" technology. I see Chuck's "equivalent" as "stilted,
obsolete" technology.

But that's just my opinion...<G>

Pete.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 7)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-08-29T22:22:45+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<josephk-BA10D8.22224529082001@echo-01.iinet.net.au>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com>`

```
In article <b3638c46.0108281756.248ce6bb@posting.google.com>,
 dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:

> 
> But the MAIN reason for using this approach is the SAME reason that I
…[5 more quoted lines elided]…
> 
However, the technique of eXtreme programming would teach that it is a 
waste of time to generalise. You should only code exactly what is need 
to accomplish the users request and no more. This saves time the 
following ways:
1. reduced testing. This is because you only need to test the exact 
cases that the user requires.
2. saved errors. The more lines of code, the more errors. If you don't 
include code to generalise - when the generalisation may never be needed 
- then you will reduce your exposure to errors.
3. redundant effort. When the time comes to use the generalization - 
generally - it is insufficient to the needs and has to be changed. This 
is more coding and more testing and more errors.

So do you ever generalise in eXtreme programming. YES. but only when it 
is requested. That is you ask yourself if you need to refactor 
(generalise) the module at the time you find yourself wanting to call it 
with different parameters or for a different reason.

This way your solution evolves with the business and the business is not 
paying for features that they do not immediately need - thus lowering 
the cost of the solution.

How do "components" fit into this scheme. They don't.
However, there is nothing to prevent the component creators from 
adopting this practice. This would be a goodness as it would help to 
prevent the advance of featuritis in the component. Something that many 
relational databases and PC operating systems could do with.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 8)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-08-29T18:53:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010829145342.29724.00006107@nso-fd.aol.com>`
- **References:** `<josephk-BA10D8.22224529082001@echo-01.iinet.net.au>`

```
In article <josephk-BA10D8.22224529082001@echo-01.iinet.net.au>, Joseph J
Katnic <josephk@iinet.net.au> writes:

>
>This way your solution evolves with the business and the business is not 
…[8 more quoted lines elided]…
>

This solution may work if you are working with a single client.  
When you have a product that is to be used as a ssolution for multiple
clients, you would want to generalize and based on some parameters
or configuration file fine tune the component responses/verbiage/presentation.
I have seen where a single piece of software is capable of some 
200 clients simultaneously and each client having their own unique 
presentation criteria, calculation options, payment methods, and 
account validation methods.
How would you approach this in your scenario?
Have 200 separate versions of the 'base' product?
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-30T11:39:07+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b8d7fab_9@goliath.newsgroups.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <josephk-BA10D8.22224529082001@echo-01.iinet.net.au>`

```
Interesting response Joe.

I am not familiar with the theory of Xtreme Programming and from what you've
written, it doesn't impress.

However, I'll reserve judgement until I know more about it.

Can you direct me to some background, please?

Pete.


"Joseph J Katnic" <josephk@iinet.net.au> wrote in message
news:josephk-BA10D8.22224529082001@echo-01.iinet.net.au...
> In article <b3638c46.0108281756.248ce6bb@posting.google.com>,
>  dashwood@enternet.co.nz (Peter E. C. Dashwood) wrote:
…[38 more quoted lines elided]…
> Joe Katnic



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 9)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-08-30T20:32:33+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<josephk-D2F68B.20323330082001@echo-01.iinet.net.au>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <josephk-BA10D8.22224529082001@echo-01.iinet.net.au> <3b8d7fab_9@goliath.newsgroups.com>`

```
In article <3b8d7fab_9@goliath.newsgroups.com>,
 "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

> Interesting response Joe.
> 
…[6 more quoted lines elided]…
> 
Hi Pete,

Check out

http://www.extremeprogramming.org
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 7)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-08-29T11:31:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mjcei$e8g$1@mail.pl.unisys.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com>`

```
The environment that precipitated the question is one in which dynamic
program calls are significantly less efficient than static ones.  I have no
personal *objection* to any user using dynamic calls -- this is a
fully-supported feature of two dialects of the COBOL language.  If, however,
a user is expecting the dynamic calls -- to nested programs or to external
ones, in COBOL85 -- to perform with the same alacrity as static ones, the
user is cautioned that they will be disappointed.

My suggestions here are intended to provide equivalent functionality to the
dynamic CALL in that environment, for an application that already exists or
is well under development, with minimal difference in logic, while offering
rather better performance.

It isn't clear to me whether the approach proposed involves only nested
programs, only externally-compiled ones, or a combination of both.  I
initially presupposed external CALLs, but have reconsidered based on nested
ones (and my main concern about the nested ones relates to data shared
between the caller and the called module).

In this particular environment, compiling a new (or revised) nested program
implies recompiling the entire program that contains it.  The argument that
the caller has to be recompiled every time a new nested module is added
applies in exactly the same way to my proposal as to the dynamic case; every
program that calls that "nested" module must already be recompiled either
way, when the nested module is introduced or whenever it is changed.  You
can't compile just a nested program; you have to compile the entire program.
Adding the name of the nested program to the EVALUATE in the calling part of
the same source file is trivial hosuekeeping.

If the module being called is "non-nested", it is itself independently
compiled.  But if it is "non-nested", the only shared data between the
calling program and the called one is either in the parameter list or must
itself be external to both programs to begin with.   To cover the "non-neste
d" case, consider:
    Program a:  CALL CALLDIRECTOR USING PROGRAM-NAME, PARAMETER-LIST ...
    Program b ("PROGRAM-ID.  CALLDIRECTOR.")
                        EVALUATE PROGRAM-NAME
                        WHEN "PROGRAM-A" CALL PROGRAM-A USING ...
                                ...
The independent called programs are EXACTLY the same, and the calling
program differs only in that instead of calling the target program itself it
calls CALLDIRECTOR with the name of the program, and the latter actually
performs the CALL.  That's a pretty tiny difference for a LARGE improvement
in performance.   A comment in program a in the vicinity of the CALL
CALLDIRECTOR statement, to the effect that "This CALL and the program it
calls provide the functionality of CALL PROGRAMNAME, at considerably less
cost, for all externally-compiled programs." would probably prove useful to
those who wondered decades hence why it was coded the way it was.  I don't
see any other change needed in the calling program, or in the programs being
called, for the non-nested case.

Yes, it is perhaps not quite so elegant to have to execute two static CALL
statements -- or an EVALUATE and a static CALL statement, for the nested
case -- to provide the application results that could be expected from one
dynamic CALL, but if the two-static-CALL approach consumes a whole lot less
system resources than the single-dynamic-CALL approach, with relatively
insignificant differences in the source file between the two approaches, I
think most DP managers would rather allocate their budget to causes other
than elegance.

We'd be happy to sell them a much more powerful machine if they're that
enamored of the dynamic CALL approach.

    -Chuck Stevens

"Peter E. C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:b3638c46.0108281756.248ce6bb@posting.google.com...
> Trying this through Google for the first time, bear with me...<G>
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:<9mguqa$9f6$1@mail.pl.unisys.com>...
> > "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
> > news:3b8b986d_4@goliath.newsgroups.com...
…[3 more quoted lines elided]…
> > > > > The ability to call different modules at run time, depending on
what
> >  the
> > > > > circumstances dictate is an essential feature of Modular
Programming.
> > > >
> > > > And there are other ways to skin that same cat in MCP/AS COBOLs.
…[6 more quoted lines elided]…
> > Personally, I think the cases in which you truly *need* the capability
of an
> > absolutely arbitrary title in a CALL dataname statement are very, very
> > limited.  I think, rather than
> >     CALL PROGRAM-TITLE USING ...
> > since you know you're going to crash-and-burn if the library you try to
call
> > is invalid anyway, most instances of "dynamic modular programming" could
be
>
> Well, one of the reasons we do testing is to ensure that we WON'T
…[23 more quoted lines elided]…
> > In either case the choice is dynamic; the point is that rarely is the
list
> > of choices truly infinite.  This approach also has the advantage of
> > providing a current centralized list of valid routines for the context,
and
> > a straightforward way to protect programmatically against the
possibility of
> > an invalid program-title (instead of reacting to it)!
> >
…[32 more quoted lines elided]…
> Pete.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 7)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-08-30T07:35:58+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B8DDECE.A2548BD4@Azonic.co.nz>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com>`

```
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
> 
>  Personally, I think the cases in which you truly *need* the capability of an
>  absolutely arbitrary title in a CALL dataname statement are very, very
>  limited.  

My systems call 'absolutely arbitrary titles' almost exclusively.  The
startup program only knows the name of the user login program and the
default menu program, when the user logs in this sets up the required
company code, system type, base menu, and other system information,
including overriding the menu program if necessary, and then the whole
system is (usually) data driven with (eg) menu selections getting the
required program name from the system control file (plus security level
required, pprogram password requirements etc).  In fact, given an
adequate security level, I can type in a program name and have it run in
an entirely arbitrary way.

This mechanism allows the use of the same set of system programs for a
wide variety of completely different systems.

>  I think, rather than
>      CALL PROGRAM-TITLE USING ...
>  since you know you're going to crash-and-burn if the library you try to call
>  is invalid anyway, 

Why would it 'crash and burn' ?  Programs are called from the core
program and this checks that the program name exists, ensures it is
correct case for case-sensitive systems and uses ON EXCEPTION.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-08-29T13:37:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mjjpj$msi$1@mail.pl.unisys.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <3B8DDECE.A2548BD4@Azonic.co.nz>`

```
I wasn't arguing on the general suitability or utility of CALL <dataname>;
my point was that this construct is significantly less efficient on some
systems than CALL <literal> is, enough so that many users of those systems
would be discouraged from using it by the overhead associated with the
construct.

I have no doubt that such an application as you describe would run, nor do I
doubt that you have chosen to design your application in this fashion.  I do
not agree, however, that this design is obviously or necessarily the most
*efficient* possible approach to all aspects of the problem in every
environment in which one might wish to solve it!

<<Why would it 'crash and burn' ?>>

If you have ON EXCEPTION on the call, that phrase handles the
"crash-and-burn" of the CALL.  If you don't, the caller does a
"crash-and-burn".   The CALL will "crash-and-burn" either way.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 9)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-08-29T22:53:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B8D71E8.2E5366BD@istar.ca>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <3B8DDECE.A2548BD4@Azonic.co.nz> <9mjjpj$msi$1@mail.pl.unisys.com>`

```
In the past three shops I have been in, (2 IBM and 1 HP-UX), the batch
programs have defaulted to dynamic call.  This has measurable initial
call and per execution call overhead.  However that overhead is small
enough that nobody (including me who bothered to measure it) cared.

Clark Morris, CFM Technical Programming Services Inc.

Chuck Stevens wrote:
> 
> I wasn't arguing on the general suitability or utility of CALL <dataname>;
…[17 more quoted lines elided]…
>     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 9)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-08-30T18:26:22+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B8E773E.4C284717@Azonic.co.nz>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <3B8DDECE.A2548BD4@Azonic.co.nz> <9mjjpj$msi$1@mail.pl.unisys.com>`

```
Chuck Stevens wrote:
> 
> I have no doubt that such an application as you describe would run, nor do I
…[3 more quoted lines elided]…
> environment in which one might wish to solve it!

It is _absolutely_ the most efficient when 'efficiency' is measured as
time spent in development and testing.  There may be some machine
overhead for the call, but who cares about that ?

Given a system of 100 or so programs, or more, then dynamic linking
allows each to be maintained, updated, replaced, independantly.  And
this means that only those being replaced need be tested.  With static
linking it is necessary to retest every function before releasing a new
version because the whole system is replaced. 

And, of course, add-ons are a no-brainer.  Just add a line to the menu
and drop in the program.

> <<Why would it 'crash and burn' ?>>
> 
> If you have ON EXCEPTION on the call, that phrase handles the
> "crash-and-burn" of the CALL.  If you don't, the caller does a
> "crash-and-burn".   The CALL will "crash-and-burn" either way.

I don't see that the system producing a message to the user that the
program is: unavailable/ has insufficient security / is not part of this
system; as 'crash-and-burn'.  My systems certainly do not 'crash' in any
way, let alone 'burn', just because of a program name.  YMMV
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 10)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2001-08-30T09:53:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mlr20$q41$1@mail.pl.unisys.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <3B8DDECE.A2548BD4@Azonic.co.nz> <9mjjpj$msi$1@mail.pl.unisys.com> <3B8E773E.4C284717@Azonic.co.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B8E773E.4C284717@Azonic.co.nz...

<<It is _absolutely_ the most efficient when 'efficiency' is measured as
time spent in development and testing.  There may be some machine overhead
for the call, but who cares about that ?>>

Depends on how much it is.  If it's a few percentage points, OK.  If it's
twice as much, maybe that's tolerable.  How about more?  How about a LOT
more?

<<Given a system of 100 or so programs, or more, then dynamic linking allows
each to be maintained, updated, replaced, independantly.>>

Maybe I'm misunderstanding something.  On Unisys MCP/AS systems, which is
what I'm referring to here, in COBOL74 all you have to do to the program
that has a "CALL <literal>" statement is compile it, and it's executable.
All you have to do to the external program named in that CALL is to compile
it, and it's CALLable.

Before the program being CALLed is compiled, an attempt to execute the CALL
will crash-and-burn.  That crash-and-burn takes the form of execution
failure if there is NOT an ON EXCEPTION clause on the CALL, and it takes the
form of doing whatever the ON EXCEPTION clause says to do if there is one
(in either case, the CALL itself crashes; whether the program does is up to
the programmer).

Presuming the file naming conventions have been followed, once both programs
are compiled, it is the operating system's job to make the linkage on the
initial call (and for that matter to "fire up" the called program as part of
that process).   Once the linkage is made, subsequent static calls are very
efficient; subsequent dynamic ones aren't because the linkage is broken and
reconstructed on each CALL.

For either "static" or "dynamic" CALLS, there is no relationship between the
calling program and the called external program on disk or in memory, they
remain separate object code files, there is no "linkedit" step to produce a
single code file.  Each program is physically independent; the only
relationship between a calling program and the called program is an
execution-time aspect of the stack structure of the caller.

There are some detail differences between MCP/AS COBOL74 and COBOL85 in the
area of CALL <literal> behavior, but the overall concepts are the same.

Presuming the programs in question are external (not nested), and the calls
are static, the only programs that would need to be compiled are the new
program and the program that has new logic to call it.  While dynamic
linking does allow the user to forego recompiling the caller, some mechanism
whereby the new program can be called (or is needed) has to be present in
the caller, and I as yet am unconvinced that adding that logic is trivial
while adding the call itself onerous.

(BTW, I don't think of a system of 100 or so programs as particularly large,
particularly a system in which there's one "driver" program and a series of
"server" programs.   We regularly deal with figures in the thousands, as
well as monolithic COBOL programs on the order of half a million source
lines).

One of the drawbacks I see to the dynamic linkage approach is the imposition
of the requirements that the parameter lists for each of the called routines
must match, regardless of how well that "universal" parameter list fits the
needs of the particular module being called.  Personally, I find that
requirement of the "CALL <dataname> USING ..." approach rather restrictive
for that very reason!

Now, I have presumed throughout this discussion that the targets of the CALL
<dataname> statement are all non-nested.  If they are nested, they are *part
of* the program, and can't be independently compiled anyway.  Adding a new
nested program to the repertoire implies recompilation of the whole program,
whether the CALLs are static or dynamic.  While some implementors may
provide the ability to compile a nested program independently, it does not
seem to me that that is a feature of *standard* COBOL (though I'm sure
somebody will point out the chapter-and-verse if I'm mistaken!), so I must
presume that the concept of changing a program includes changing any of the
subprograms nested within it, just as would be true for a Pascal or Algol
nested procedure.  Barring extensions, the presumption is that the whole is
recompiled in each case.

<<And this means that only those being replaced need be tested. >>

Why would any component not modified, not recompiled and not replaced need
to be tested in any event?

<<With static linking it is necessary to retest every function before
releasing a new version because the whole system is replaced. >>

Why is the whole system replaced because one of the hundreds of individual
object programs got replaced, or a new program added?   Maybe we don't mean
the same thing by "static linking".

<<And, of course, add-ons are a no-brainer.  Just add a line to the menu and
drop in the program.>>

A bit more work for the static call, I grant, but with a little thought as
to what automated processes can get fired off by the act of "adding a line
to the menu", no manual intervention other than the two steps described is
necessarily required.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2001-08-30T20:59:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mm9c5$do9$1@peabody.colorado.edu>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <3B8DDECE.A2548BD4@Azonic.co.nz> <9mjjpj$msi$1@mail.pl.unisys.com> <3B8E773E.4C284717@Azonic.co.nz> <9mlr20$q41$1@mail.pl.unisys.com>`

```

On 30-Aug-2001, "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> <<It is _absolutely_ the most efficient when 'efficiency' is measured as
> time spent in development and testing.  There may be some machine overhead
…[4 more quoted lines elided]…
> more?

If a job needs to finish before 7:00 A.M. or it will be killed, and can't
start until after midnight, and takes 7 hours and 1 minute to run, then a
few percentage points of efficiency are a mandatory minimum.

Efficiency needs aren't constant.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 12)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-08-31T19:13:07+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B8FD3B3.89410158@Azonic.co.nz>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <3B8DDECE.A2548BD4@Azonic.co.nz> <9mjjpj$msi$1@mail.pl.unisys.com> <3B8E773E.4C284717@Azonic.co.nz> <9mlr20$q41$1@mail.pl.unisys.com> <9mm9c5$do9$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> 
> If a job needs to finish before 7:00 A.M. or it will be killed, and can't
> start until after midnight, and takes 7 hours and 1 minute to run, then a
> few percentage points of efficiency are a mandatory minimum.

While a single of initial dynamic call _can_ take much longer to
complete than a static linked one, repetitive calls to a loaded routine
are insignificantly more than to a static one, and only use a few CPU
cycles.

Any run that takes several hours is most likely to be:
    * Disk or database limited
    * Variable depending on data volumes
    * Better served by improving other tuning options    

Certainly you could 'prove a point' by adding a CANCEL after each CALL
to show how slow it _could_ be made if you were really struggling to
support your view.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 8)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-30T11:46:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b8d7fb1_9@goliath.newsgroups.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <b3638c46.0108281756.248ce6bb@posting.google.com> <3B8DDECE.A2548BD4@Azonic.co.nz>`

```
Thanks Richard.

I endorse this 100% and it is a better example than I was able to provide
myself.

The concept I was trying to get across to Chuck was the FLEXIBILITY of true
dynamic calling.

You provided an excellent concrete example of it.

Pete.
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3B8DDECE.A2548BD4@Azonic.co.nz...
> > "Chuck Stevens" <charles.stevens@unisys.com> wrote:
> >
> >  Personally, I think the cases in which you truly *need* the capability
of an
> >  absolutely arbitrary title in a CALL dataname statement are very, very
> >  limited.
…[17 more quoted lines elided]…
> >  since you know you're going to crash-and-burn if the library you try to
call
> >  is invalid anyway,
>
> Why would it 'crash and burn' ?  Programs are called from the core
> program and this checks that the program name exists, ensures it is
> correct case for case-sensitive systems and uses ON EXCEPTION.



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 6)_

- **From:** gospodin.spasebaw@tanstaafl.com (freewheelin)
- **Date:** 2001-08-29T15:50:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b8cff7b.4481299@news.uswest.net>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com>`

```
On Tue, 28 Aug 2001 13:26:49 -0700, "Chuck Stevens"
<charles.stevens@unisys.com> wrote:

>
>"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
…[44 more quoted lines elided]…
>
Chuck, this is an application system design issue.  Transaction
processors often used this technique.   An application may generate a
large set of transactions and many programs might generate the same
transaction.  Depending on the transaction and its origin, the
destination could be variable, both local and remote.   Rather than
writing each program to deal with each situation we created a general
transaction format in a wrapper for a transaction processor.   The
processor program read from a single queue file and based on tables,
figured out which formatting programs to call.  The idea was to get a
grip on transaction proliferation in applications.  Implementing a new
transaction, removing a transaction or simply changing the scope of
distribution required less work and made things easier when the
business changed its rules.

One such processor I wrote had an initial startup phase where it first
"polled" all the programs loaded in its table and flagged them when it
had trouble and signaled support.  Corporate transaction "04"
generated by the order application might be sent to several other
application sytems while an "04"  from the receiving dock might only
report to the inventory system.  The transaction processor's resource
tables (loaded at startup)  mapped the relationships and they included
PROGRAM-ID names.   So the processor had a single CALL statement.

JF
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2001-08-30T11:49:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b8d7fb8_9@goliath.newsgroups.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <3b8cff7b.4481299@news.uswest.net>`

```
Thanks for another good example.

The keyword here is FLEXIBILITY.

Pete.

"freewheelin" <gospodin.spasebaw@tanstaafl.com> wrote in message
news:3b8cff7b.4481299@news.uswest.net...
> On Tue, 28 Aug 2001 13:26:49 -0700, "Chuck Stevens"
> <charles.stevens@unisys.com> wrote:
…[7 more quoted lines elided]…
> >> > > The ability to call different modules at run time, depending on
what
> >the
> >> > > circumstances dictate is an essential feature of Modular
Programming.
> >> >
> >> > And there are other ways to skin that same cat in MCP/AS COBOLs.
…[6 more quoted lines elided]…
> >Personally, I think the cases in which you truly *need* the capability of
an
> >absolutely arbitrary title in a CALL dataname statement are very, very
> >limited.  I think, rather than
> >    CALL PROGRAM-TITLE USING ...
> >since you know you're going to crash-and-burn if the library you try to
call
> >is invalid anyway, most instances of "dynamic modular programming" could
be
> >served, instead by something like:
> >    EVALUATE PROGRAM-TITLE
…[6 more quoted lines elided]…
> >In either case the choice is dynamic; the point is that rarely is the
list
> >of choices truly infinite.  This approach also has the advantage of
> >providing a current centralized list of valid routines for the context,
and
> >a straightforward way to protect programmatically against the possibility
of
> >an invalid program-title (instead of reacting to it)!
> >
> >I agree that determining which program to CALL at execution time is a
> >central feature of "dynamic modular programming", but I fail to see why
the
> >list of possible program-titles that one could call must be absolutely
> >indeterminate until execution time, or that the determination must reside
> >strictly within the confines of the CALL statement itself, to allow the
> >implementation to qualify as dynamic in this context.   Is there
something
> >I'm missing in your definitions or criteria?
> >
…[25 more quoted lines elided]…
> JF



-----=  Posted via Newsfeeds.Com, Uncensored Usenet News  =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
 Check out our new Unlimited Server. No Download or Time Limits!
-----==  Over 80,000 Newsgroups - 19 Different Servers!  ==-----
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 8)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2001-08-31T11:28:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0108311028.550485dc@posting.google.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <3b8cff7b.4481299@news.uswest.net> <3b8d7fb8_9@goliath.newsgroups.com>`

```
>various people wrote on nested programs, dynamic versus static calls,
etc

Surely the point is to use the appropriate technique for the
circumstances, rather than always one or the other, for example

inline performs - a few lines of code

out-of-line performs - rather more lines of code

nested programs - even more lines of code and for common routines
within a system that can be included via copybooks

static calls to independently compiled subprograms - for routines
common within a system and the names of which are known at compilation
time

dynamic calls - for independently compiled subprograms common within a
system and whose names are not known at compilation time

This is only a very brief summary.  The way in which linkage editing
can be done varies between implementations and can provide a certain
amount of overlap between the last two techniques, as independent load
modules can be linked either statically or dynamically even when
called statically and subprograms can be made reentrant or reusable,
especially when written in other languages.  The use of nested
programs seems beneficial for encapsulating data and procedures from
the remainder of a program while not paying the efficiency overheads
that come from compiling and linking independently compiled programs,
such a use could be recommended where it is known that it is unlikely
to be necessary to frequently recompile the constituent subprograms
while leaving the calling programs unchanged.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 9)_

- **From:** "James" <mangogrower@telocity.com>
- **Date:** 2001-09-01T04:10:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<G9Sj7.18$ix.22150@newsrump.sjc.telocity.net>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <3b8cff7b.4481299@news.uswest.net> <3b8d7fb8_9@goliath.newsgroups.com> <fcd09c56.0108311028.550485dc@posting.google.com>`

```
I must diagree on most of your 'reasoning'.

Except when a compiler 'optimizes' the code, out of line performs may be
converted to 'inline' performs and various other things are done until the
code size is increased by (generally) 50% at which point that type of
optimize
is stopped.

Static calls should never be used UNLESS the routine is called VERY OFTEN
(20 % or more of the time it is in that routine) otherwise it wastes memory
that
coould be used for file buffers, utilities, etc.

Dynamic calls are NOT just for 'when the name isn't known'.  Its also for
INFREQUENTLY called routines, routines that change often, routines that if
static-linked, would cause the object module to exceed a certain size.

"Robert Jones" <robert@jones0086.freeserve.co.uk> wrote in message
news:fcd09c56.0108311028.550485dc@posting.google.com...
> >various people wrote on nested programs, dynamic versus static calls,
> etc
…[29 more quoted lines elided]…
> while leaving the calling programs unchanged.
```

###### ↳ ↳ ↳ Re: Alternates to Dynamic Linkage (Re: "nested programs" - terminology)

_(reply depth: 10)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2001-09-02T07:09:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0109020609.6243f845@posting.google.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com> <9mguqa$9f6$1@mail.pl.unisys.com> <3b8cff7b.4481299@news.uswest.net> <3b8d7fb8_9@goliath.newsgroups.com> <fcd09c56.0108311028.550485dc@posting.google.com> <G9Sj7.18$ix.22150@newsrump.sjc.telocity.net>`

```
I must admit to an error of terminology as I agree that dynamic calls
are often preferable for independently compiled subprograms.  I should
have used the terms CALL literal and CALL identifier instead of static
and dynamic calls, since while CALL identifier must be dynamic, CALL
literal may be either dynamic or static depending upon the way the
program is linked.  As well as reducing overheads, the use of CALL
literal makes it much easier to analyse the calls between programs
with an automated code analysing tool.

"James" <mangogrower@telocity.com> wrote in message news:<G9Sj7.18$ix.22150@newsrump.sjc.telocity.net>...
> I must diagree on most of your 'reasoning'.
> 
…[48 more quoted lines elided]…
> > while leaving the calling programs unchanged.
```

###### ↳ ↳ ↳ Re: "nested programs" - terminology

_(reply depth: 5)_

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-08-29T22:03:53+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<josephk-3996C0.22035229082001@echo-01.iinet.net.au>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3b7e84d4_2@goliath.newsgroups.com> <9mds1h$lef$1@mail.pl.unisys.com> <3b8b986d_4@goliath.newsgroups.com>`

```
In article <3b8b986d_4@goliath.newsgroups.com>,
 "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote:

> Oh, yes it is...<G> (chorus in background..."Oh, NO, it isn't..."...."look
> out behind you!")
…[16 more quoted lines elided]…
> 
Not to be too rude, but this is a load of "ball pucky".

Look, you have a 128 byte cache - for example. This is broken into 2 x 
64 byte cache lines. Cache line 0 contains the mainline, cache line 1 
will contain the subroutine. Branching from mainline to subroutine and 
back again is simply a matter of switching cache lines. NO memory access 
required - except for data - hopefully in a separate data cache.

Scale this up to Mainframe and current Micro-processor cache sizes and 
you can see that this argument starts to become redundant.

At the end of the day, you can forget about hardware performance issues 
when writing high level languages. If the compiler writer is any good 
they will have at least optimized the code for the target hardware.

With COBOL, you do get a choice of optimizations via different langauge 
elements to perform the same action. I.E. use of indexes versus 
subscripts etc. But please note, SOME compilers will even remove that 
distinction and will optimise away any high level decisions on which 
language element you need to use to get better performance.
```

##### ↳ ↳ Performance of performs and calls was Re: "nested programs" - terminology

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2001-08-20T01:55:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B806DAC.904673D6@istar.ca>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com>`

```
Based on testing with the COBOL for MVS and VM compiler. Bill's
heirarchy is generally true.  Because of optimizations paragraphs being
PERFORMed may be moved in-line and thus have no more overhead than
in-line PERFORMs.  If the program is properly structured the PERFORM of
a separate paragraph not moved in-line will have less overhead than a
PERFORM in a program not properly structured (overlapping PERFORMs,
PERFORMs with GO TO statements that may go out of range, etc.).  A CALL
of a nested program also theoretically can be moved in-line although I
have not seen it.  The call definitely has less overhead than a dynamic
call both on an intial use and per instance basis.  An earlier posting
to this thread explained why for even the statically linked programs. 
It has to do with how much context switching must be done.

I would be very interested in the performance of nested programs in a
current Micro-Focus environment because their manual says there is a
performance penalty if the compile option allows nested programming even
if it isn't used.

Clark F. Morris, Jr. 

Chuck Stevens wrote:
> 
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
…[42 more quoted lines elided]…
>     -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Performance of performs and calls was Re: "nested programs" - terminology

- **From:** "Robert Sales" <Robert.Sales@merant.com>
- **Date:** 2001-08-20T10:22:10+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lql7n$jpn$1@hyperion.eu.merant.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net> <9lk6j3$bbe$1@mail.pl.unisys.com> <3B806DAC.904673D6@istar.ca>`

```
In current Micro Focus products (Net Express and Server Express), the
compiler option to enable nested programs is no longer required (i.e. the
NESTCALL directive is simply ignored).  Nested programs may be used freely
and there is no performance penalty associated with their use.  Generally a
call to a nested program will be considerably faster than a call to an
external program.

"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message
news:3B806DAC.904673D6@istar.ca...
> Based on testing with the COBOL for MVS and VM compiler. Bill's
> heirarchy is generally true.  Because of optimizations paragraphs being
…[23 more quoted lines elided]…
> > > Depending on the compiler (and run-time and operating system), in
GENERAL,
> > > performance can be "graded" as follows (from best to worst)
> >
…[6 more quoted lines elided]…
> > > To be clear, there is almost CERTAINLY exceptions to this order (based
on
> > > optimization provided by the vendor)...
> >
> > Hmmm.  I still think you might be overstating this as a general rule,
Bill.
> > There is no particular architecture-independent reason why this order
should
> > hold true, nor is any deviation from this order necessarily the result
of
> > some optimization on the part of the compiler implementor.
> >
> > For example, on Unisys MCP/AS COBOL85, a call on a nested program *may*
> > require more resources than a call on an external one of the same name
if it
> > is necessary for the run-time system to determine whether the call is
indeed
> > to a nested program or a separately-compiled one.
> >
> > And once the linkage between the caller and the called program (nested
or
> > otherwise) is established (ordinarily by the first CALL with no
intervening
> > CANCEL) and presuming no further "diagnoses" of program-name scope need
to
> > be performed, any difference in performance among these three mechanisms
> > should be unmeasurable because they all use the same sequence of machine
> > instructions.
> >
> > Unisys MCP/AS distinguishes between "dynamic" determination of CALLing
scope
> > for a "CALL <literal>" statement, which is how I am interpreting
"dynamic
> > binding", and the entire subject of "CALL <dataname>".  Unisys supports
> > "CALL <dataname>" because the '85 standard requires it, but we actively
> > discourage our users from writing applications using the feature; the
> > overhead of constructing the library template, establishing the library
> > linkage, calling the program, and tearing it all back down again on each
and
> > every call is quite high.    If that particular feature is what you mean
by
> > "dynamic binding", then I agree, it's likely to be costly.  But the
> > "binding" necessary for CALL <literal> is sometimes dynamic as well.
> >
> >     -Chuck Stevens
```

#### ↳ Re: "nested programs" - terminology

- **From:** "Walter Murray" <walter_murray@hp.com>
- **Date:** 2001-08-20T10:02:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9lrg06$3kt$1@web1.cup.hp.com>`
- **References:** `<9lk4ni$4o0$1@slb6.atl.mindspring.net>`

```

"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:9lk4ni$4o0$1@slb6.atl.mindspring.net...

[an excellent explanation of the various kinds of "subroutines" in COBOL]

Just one minor thing ...

> The "traditional" COBOL PERFORM UNTIL corresponds to the
> theoretical "DO WHILE" and not "DO UNTIL" often taught in "language
theory".
> "DO UNTIL" logic was added in the '85 Standard with the "TEST BEFORE"
> phrase.

I think Bill meant to write "the TEST AFTER phrase".  TEST BEFORE is the
default.

Walter
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
