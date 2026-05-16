[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Recursive Call

_21 messages · 12 participants · 2005-11_

---

### Recursive Call

- **From:** "Paolo" <paolo.sanzotta@gmail.com>
- **Date:** 2005-11-02T06:48:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com>`

```
Hi,
i've a big problem with the recursives call under Fujitsu Cobol.Net.
It'happen an exception for recursive call and i don't know how to
resolve it!
Do it exist a work-around for this problem?
thank's
```

#### ↳ Re: Recursive Call

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-11-02T10:06:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Kr5af.34475$ty1.3550@bignews1.bellsouth.net>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com>`

```
"Paolo" <paolo.sanzotta@gmail.com> wrote:
> Hi,
> i've a big problem with the recursives call under Fujitsu Cobol.Net.
…[3 more quoted lines elided]…
> thank's


More detail! Is this a compiler syntax issue, or a runtime issue? What is 
the code that is giving the trouble?
```

#### ↳ Re: Recursive Call

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-11-02T08:46:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dkaqgc$tkf$1@si05.rsvl.unisys.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com>`

```
Note that within COBOL that is compliant with the three most recent 
standards, both direct and indirect recursion is prohibited.  If an 
implementor allows it (or provides additional syntax to support it), it's an 
extension and it does whatever the implementor says it does.

The draft standard proposed for 2008 allows the RECURSIVE clause in the 
PROGRAM-ID paragraph, and programs so marked may be called when they are 
already active, and may call themselves directly or indirectly.  Those that 
aren't can't.

    -Chuck Stevens

ANSI X3.23-1974, ANSI X3.23-1985, and ISO/IEC
"Paolo" <paolo.sanzotta@gmail.com> wrote in message 
news:1130942928.070790.49860@g47g2000cwa.googlegroups.com...
> Hi,
> i've a big problem with the recursives call under Fujitsu Cobol.Net.
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Recursive Call

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2005-11-02T12:55:51-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11mhvkqo0ibbv59@corp.supernews.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com>`

```

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:dkaqgc$tkf$1@si05.rsvl.unisys.com...
> Note that within COBOL that is compliant with the three most recent
> standards, both direct and indirect recursion is prohibited.  If an
> implementor allows it (or provides additional syntax to support it), it's
an
> extension and it does whatever the implementor says it does.
>
> The draft standard proposed for 2008 allows the RECURSIVE clause in the
> PROGRAM-ID paragraph, and programs so marked may be called when they are
> already active, and may call themselves directly or indirectly.  Those
that
> aren't can't.

Mr Stevens, I believe the capability you state for the
draft standard are already in ISO/IEC 1989:2002.
See 8.6.5, Common, initial, and recursive attributes
which states, in part, "A recursive program may call
itself directly or indirectly. The program's internal data
is initialized as described in 14.5.2, State of a function,
method, object, or program. The recursive attribute is
attained by specifying the RECURSIVE clause in the
program's identification division." and 11.9 PROGRAM-ID
paragraph, General rule 4, "The RECURSIVE clause
specifies that the program and any programs contained
within it are recursive. The program may be called while
it is active and may call itself. If the RECURSIVE clause
is not specified in a program or implied for a program,
the program shall not be called while it is active."
```

###### ↳ ↳ ↳ Re: Recursive Call

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-11-02T18:29:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cA7af.35317$WF5.31053@fe03.news.easynews.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <11mhvkqo0ibbv59@corp.supernews.com>`

```
Chuck,
  I agree with Rick (and it was also RECURSIVE - as well as OO - that explains 
why Local-Storage was added in the '02 Standard).  Having said that, I know of 
no "fully conforming" '02 Standard compiler - but do know of several that have 
the "IS RECURSIVE" syntax and semantics implemented.
```

###### ↳ ↳ ↳ Re: Recursive Call

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-11-02T15:18:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dkbhh0$1bcd$1@si05.rsvl.unisys.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <11mhvkqo0ibbv59@corp.supernews.com>`

```
Right you are.  I looked at "program-prototype" whose syntax diagram doesn't 
include it and presumed I'd read "program-definition" whose syntax diagram 
does.

'85 and '74 don't allow it, though.

    -Chuck Stevens


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:11mhvkqo0ibbv59@corp.supernews.com...
>
> "Chuck Stevens" <charles.stevens@unisys.com> wrote in message
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-11-03T13:59:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eJoaf.1476$p37.279@newssvr17.news.prodigy.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <11mhvkqo0ibbv59@corp.supernews.com> <dkbhh0$1bcd$1@si05.rsvl.unisys.com>`

```
Re: I don't really know the answer to this (I suspect it may be
compiler-dependent?)

Instead of making the *program*  support recursion, can't you just use an
ENTRY with a LOCAL STORAGE SECTION?


MCM
(C'mon, I haven't written a line of COBOL in over four years).
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-11-03T09:00:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dkdfml$2h8j$1@si05.rsvl.unisys.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <11mhvkqo0ibbv59@corp.supernews.com> <dkbhh0$1bcd$1@si05.rsvl.unisys.com> <eJoaf.1476$p37.279@newssvr17.news.prodigy.com>`

```
Well, you *could*, I suppose ... if ENTRY were valid in standard COBOL (of 
any vintage) ...    ;-)

    -Chuck Stevens

"Michael Mattias" <michael.mattias@gte.net> wrote in message 
news:eJoaf.1476$p37.279@newssvr17.news.prodigy.com...
> Re: I don't really know the answer to this (I suspect it may be
> compiler-dependent?)
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2005-11-03T21:17:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W7vaf.1523$p37.108@newssvr17.news.prodigy.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <11mhvkqo0ibbv59@corp.supernews.com> <dkbhh0$1bcd$1@si05.rsvl.unisys.com> <eJoaf.1476$p37.279@newssvr17.news.prodigy.com> <dkdfml$2h8j$1@si05.rsvl.unisys.com>`

```
Hmm, you made me dig out the damn manual...

Yup, you got me: ENTRY is listed as an OSVS, VSC2 and MF extension to
standard COBOL. (I have the 1994 version of the manual).

So, can we take this intriguing factoid and make it the the basis for a
little contest?

For ten points, the two week vacation in Kenosha Wisconsin and whatever
might be inside Dumpster # 3.....please name the three COBOLs in which I
have done most of my work......

MCM

"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:dkdfml$2h8j$1@si05.rsvl.unisys.com...
> Well, you *could*, I suppose ... if ENTRY were valid in standard COBOL (of
> any vintage) ...    ;-)
…[8 more quoted lines elided]…
> > Instead of making the *program*  support recursion, can't you just use
an
> > ENTRY with a LOCAL STORAGE SECTION?
```

##### ↳ ↳ Re: Recursive Call

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-11-04T13:41:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lNOaf.14$%k.4@bignews6.bellsouth.net>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:
> Note that within COBOL that is compliant with the three most recent 
> standards, both direct and indirect recursion is prohibited.  If an 
> implementor allows it (or provides additional syntax to support it), it's 
> an extension and it does whatever the implementor says it does.

Why in the world would recursion be forbidden? I haven't used it often in 
COBOL, but I did find it extremely useful in writing a parts explosion 
module once. The code, which was pretty elegant, would have been somewhat 
tacky without recursion.
```

###### ↳ ↳ ↳ Re: Recursive Call

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-11-04T12:19:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dkgfnn$1a4n$1@si05.rsvl.unisys.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <lNOaf.14$%k.4@bignews6.bellsouth.net>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message 
news:lNOaf.14$%k.4@bignews6.bellsouth.net...
> "Chuck Stevens" <charles.stevens@unisys.com> wrote:
>> Note that within COBOL that is compliant with the three most recent 
…[7 more quoted lines elided]…
> tacky without recursion.

While recursion isn't a big issue for stack-oriented machines like the 
Unisys MCP systems -- on which the compiler has to go to the trouble to 
generate code to *prevent* recursion -- I believe there was some reluctance 
on the part of J4 to require it until it could be ascertained what the 
pitfalls were and what the appropriate syntax was.

The initial specification of Inter-Program Communication was in '74 COBOL, 
and my guess is the approach was "wait and see how it shakes out".

The *second* specification added nested programs, which was a significant 
advancement, and again, enough syntax was added to raise the question as to 
whether adding recursion would break something.

Since our systems fundamentally support recursion, and since it's a common 
technique in ALGOL and related languages, I am led to suggest that the 
technique must be used very carefully.  The impact of a runaway loop in a 
recursive environment can be significantly greater and can cause escalating 
resource consumption in ways that an "ordinary" runaway loop wouldn't. 
COBOL doesn't (yet) have a standardized mechanism for asynchronous 
processing, either (our COBOL85 does, and I happen to think the syntax 
involving USAGE EVENT and USAGE LOCK is clean and clear),  and I think 
similar issues occur there.  It becomes the programmer's responsibility to 
protect the data for each user in a multithreaded program, and the issues 
there can easily get very sticky very quickly on efficiency, security, and 
effectiveness grounds.

      -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2005-11-04T16:27:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<odRaf.41945$ty1.3696@bignews1.bellsouth.net>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <lNOaf.14$%k.4@bignews6.bellsouth.net> <dkgfnn$1a4n$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote:

Chuck, do you remember if the COBOL74 compiler, circa 1996, supported 
embedded programs? My memory is that it did not, or had problems or 
limitations somehow. I know we looked at using CALLed subprograms for each 
screen within an online program, but the idea was nixed at the time. Might 
have been a problem in linking together separately compiled programs. I 
haven't used that compiler in several years.
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 5)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2005-11-04T15:04:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dkgpel$1fqb$1@si05.rsvl.unisys.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <lNOaf.14$%k.4@bignews6.bellsouth.net> <dkgfnn$1a4n$1@si05.rsvl.unisys.com> <odRaf.41945$ty1.3696@bignews1.bellsouth.net>`

```
Presuming you're talking about the MCP environment, the COBOL74 compiler is 
still actively supported, and no, it does not support nested programs.  That 
feature was introduced with ANSI-85, and the complexities entailed by the 
requirements of that feature formed the primary justification for the 
decision that we would not *ever* consider using the COBOL74 compiler symbol 
(itself rooted in the COBOL(68) compiler symbol) as a base for producing a 
COBOL85-compliant compiler back in the mid-1980's.

What COBOL74 does support (as did COBOL(68)!) is *bound procedures* (BINDER 
is analogous to IBM's linkage editor), but that's a whole different approach 
to the problem.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2005-11-08T23:47:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <lNOaf.14$%k.4@bignews6.bellsouth.net> <dkgfnn$1a4n$1@si05.rsvl.unisys.com>`

```
In article <dkgfnn$1a4n$1@si05.rsvl.unisys.com>,
 "Chuck Stevens" <charles.stevens@unisys.com> wrote:

> "Judson McClendon" <judmc@sunvaley0.com> wrote in message 
> news:lNOaf.14$%k.4@bignews6.bellsouth.net...
…[15 more quoted lines elided]…
> pitfalls were and what the appropriate syntax was.

I'm unfamiliar with a non-stack oriented, non-obsolete, machine that has 
existed since the 85 standard was written.

Even the IBM mainframe, originally a non-stack machine, made hardware 
allowances for stack-style things (e.g. Program Call & Return) somewhere 
in the 70's.

Stack machines really have proven their worth over non-stack machines.  
What isn't at least simulating a stack these days?
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 5)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2005-11-09T05:40:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <lNOaf.14$%k.4@bignews6.bellsouth.net> <dkgfnn$1a4n$1@si05.rsvl.unisys.com> <joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com>`

```


Joe Zitzelberger wrote:

> (snip) 
> Even the IBM mainframe, originally a non-stack machine, made hardware 
> allowances for stack-style things (e.g. Program Call & Return) somewhere 
> in the 70's.

Program Call and Return was implemented on System 370 architecture 
without hardware or software stacks, to the best of my knowledge.  And 
  even today, IBM Z-series mainframes still do not have hardware 
stacks, as far as I know.  Perhaps someone can correct me if my 
impression is wrong.
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 6)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-11-09T14:36:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dkt1h402c2f@news4.newsguy.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <lNOaf.14$%k.4@bignews6.bellsouth.net> <dkgfnn$1a4n$1@si05.rsvl.unisys.com> <joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com> <HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net>`

```

In article <HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net>, Arnold Trembley <arnold.trembley@worldnet.att.net> writes:
> 
> Joe Zitzelberger wrote:
…[8 more quoted lines elided]…
> stacks, as far as I know.

Even if zSeries doesn't have a "hardware" stack (which I imagine to
mean opcodes for pushing and popping values, and a register which is
either reserved or used by convention as a stack pointer), I believe
Joe's correct that pretty much all general-purpose systems these
days at least provide some stack mechanism as part of their standard
ABI.

That's no doubt due in part to the popularity of C.  C can be
implemented without a classic contiguous stack - for example using
chained activation records - but the language treats function calls,
function parameters and return values, and automatic variable
allocation and deallocation in a stack-oriented fashion, so some
relatively efficient stack mechanism is a must for a reasonable C
implementation.

There are no doubt still small embedded systems that do not provide
a stack, but these days even most embedded machines are programmed
in C or another high-level language with similar requirements.
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-11-09T17:40:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dktc9l$169$1@reader2.panix.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com> <HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net> <dkt1h402c2f@news4.newsguy.com>`

```
In article <dkt1h402c2f@news4.newsguy.com>,
Michael Wojcik <mwojcik@newsguy.com> wrote:

[snip]

>There are no doubt still small embedded systems that do not provide
>a stack, but these days even most embedded machines are programmed
>in C or another high-level language with similar requirements.

This brings up a point about which I may have made an error someplace 
else... so I might as well try to get information here that I might 
correct myself, delicately.

The fellow with whom I was conversing mentioned use of the stack-trace in 
debugging; I said that this was not, in my experience, a common method 
applied to IBM-architecture mainframes.  I based this on my experience as 
a mere apps-jockey; when something blows up I look for the PSW, find the 
address of the previous statement and proceed from there.

This ignores - in the radical sense of 'in (not) gnosis' - what folks at 
the systems level do.  Is there something akin to stack tracing done on 
Big Blue Big Iron running 'classic' (COBOL/CICS/DB2) systems?

DD
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 8)_

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2005-11-11T16:42:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dl2hl00kku@news4.newsguy.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com> <HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net> <dkt1h402c2f@news4.newsguy.com> <dktc9l$169$1@reader2.panix.com>`

```

In article <dktc9l$169$1@reader2.panix.com>, docdwarf@panix.com () writes:
> 
> The fellow with whom I was conversing mentioned use of the stack-trace in 
…[7 more quoted lines elided]…
> Big Blue Big Iron running 'classic' (COBOL/CICS/DB2) systems?

I was curious to see answers to this, but it doesn't appear that you've
had any takers.

I've not done much debugging of mainframe systems-level code, but the
folks I've seen do it generally start with a dump, and do sometimes
manually backtrack through subroutine calls.  These programs were
mostly written in assembly, and they used some variant of BAL (branch
and link) for subroutine calls, and maintained their own scratch
areas for return addresses, parameters, and so forth.  So there was
no contiguous "stack" as there is on x86 and the like, but they did
sometimes trace the flow of execution back using the dump.
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2005-11-11T17:14:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dl2jgv$6t3$1@reader2.panix.com>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkt1h402c2f@news4.newsguy.com> <dktc9l$169$1@reader2.panix.com> <dl2hl00kku@news4.newsguy.com>`

```
In article <dl2hl00kku@news4.newsguy.com>,
Michael Wojcik <mwojcik@newsguy.com> wrote:
>
>In article <dktc9l$169$1@reader2.panix.com>, docdwarf@panix.com () writes:

[snip]

>> This ignores - in the radical sense of 'in (not) gnosis' - what folks at 
>> the systems level do.  Is there something akin to stack tracing done on 
…[3 more quoted lines elided]…
>had any takers.

Oh, that's only because I add nothing but noise to the newsgroup... and 
the questions I ask are so *hard*, too!

>
>I've not done much debugging of mainframe systems-level code, but the
…[6 more quoted lines elided]…
>sometimes trace the flow of execution back using the dump.

That's what I recall from what I learned of Assembley code, aye... you 
always started out with a BALR, a USING and somewhere near the top there'd 
be something like ST R14,SAVEAREA to stash away the return address... but 
nothing physically built into the system that one would call a 'stack'.

Thanks much.

DD
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 9)_

- **From:** "charles hottel" <jghottel@yahoo.com>
- **Date:** 2005-11-11T19:08:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b8ae$43753264$4f9c601$312@DIALUPUSA.NET>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com> <HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net> <dkt1h402c2f@news4.newsguy.com> <dktc9l$169$1@reader2.panix.com> <dl2hl00kku@news4.newsguy.com>`

```
On IBM mainframes there was/is a standard linkage convention to be followed 
that uses a standard  18 fullword save area and certain standard register 
usage conventions. Register 15 contains the "branch to" address and Register 
14 contains the "Return address". So to "call" another program you would do 
something like:

    L         R15,=V(MYSUBRTN)
    BALR R14,R15

Another part of this linkage convention is that the calling program provide 
within its storage an 18 fullword save area that the subroutine can use to 
save the callers registers. The standard is that Register 13 will point to 
this save area at entry to the subroutine.  The save areas themselves 
contain standard offsets where the register contents are saved plus there 
are forward/backward pointers that chain the save areas together into a 
linked list stack. Usually the first thing a subroutine does is save the 
caller's registers and set register 13 to point to it's save area. When an 
abend occurs a save area trace is produced in the dump and shows the call 
chain.  In assembly language there are SAVE and RETURN macros and the RETURN 
macros has an option that can be used to set a bit in the save area to 
indicate to the dump program that a save area is no longer active. When a 
subroutine ends it restores the callers registers and branches to the return 
address.

Of course all of the above was the original convention.  As IBM hardware and 
addressing modes have evolved there are more/different linkage instructions 
and branching instructions.  Some of these use a linkage stack area and 
there are instructions that are used to access and manipulate it.  Some work 
with 31-bit addressing and others work with 64-bit addressing. With 64 bit 
addressing the save area layout had to be modified to accommodate the larger 
addresses and larger/wider registers.

This is a pretty standard process for all the machines that I have worked on 
and each has it standard entry/exit magic instruction sequences to 
accomplish this.  Also not mentioned, there is usually a standard way to 
pass parameters to the subroutine. I believe that on the IBM mainframe COBOL 
follows the convention when subprograms are CALLed.

"Michael Wojcik" <mwojcik@newsguy.com> wrote in message 
news:dl2hl00kku@news4.newsguy.com...
>
> In article <dktc9l$169$1@reader2.panix.com>, docdwarf@panix.com () writes:
…[31 more quoted lines elided]…
>   -- Dylan Thomas
```

###### ↳ ↳ ↳ Re: Recursive Call

_(reply depth: 6)_

- **From:** "Joel C. Ewing" <jcREMOVEewing@CAPSacm.org>
- **Date:** 2005-11-12T16:35:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dRodf.7539$2y.262@newsread2.news.atl.earthlink.net>`
- **In-Reply-To:** `<HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<1130942928.070790.49860@g47g2000cwa.googlegroups.com> <dkaqgc$tkf$1@si05.rsvl.unisys.com> <lNOaf.14$%k.4@bignews6.bellsouth.net> <dkgfnn$1a4n$1@si05.rsvl.unisys.com> <joe_zitzelberger-F22DBE.23470808112005@ispnews.usenetserver.com> <HZfcf.64578$zb5.43562@bgtnsc04-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> 
…[13 more quoted lines elided]…
> 

At least on ESA architecture and later the PROGRAM CALL and related 
instructions do indeed use hardware-supported stacks, the Linkage Stack, 
which is allocated in 64 KiB blocks and tracked via hardware control 
registers.  The Program Call instruction and its management complexity 
is generally hidden from application code, as it main (only?) usage from 
the application code standpoint is to issue function requests to the 
operating system that previously would have required using SVC 
Supervisor Calls.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
