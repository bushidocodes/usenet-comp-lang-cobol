[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# * Please read and comment

_94 messages · 20 participants · 1999-02_

---

### * Please read and comment

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1999-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
(Posted to the COBOL Usenet Newsgroups - but with CC's to various
individuals.)

Preface:
  For those who are regular readers of the COBOL newsgroups, you are aware
that I think that there are lots AND LOTS of great new  features in the
draft of the next COBOL Standard.  However, you are also aware that I have a
distinct reputation among the Standards committees for "throwing monkey
wrenches" into the works and never letting something that I disagree with
"drop" - even when all the "experts tell me I am wrong".  Given this
preface, I would like input from the readers (and if appropriate appreciate
these readers sending their comments PRO or CON to the appropriate places).

ISSUE:
  The following is a direct quote from the CD 1.4 draft of the next COBOL
Standard. (page 4)

"3.1.5 Processor-dependent language elements
     ...
The decision of whether to claim support for a processor-dependent component
is within an implementor's discretion.  Factors that may be considered
include, but are not limited to, hardware capability, software capability,
and market positioning of the processor. ..."

Some of the items in this list (which - historically - is a follow-on to the
ANSI'85 Hardware Dependent list) include (but are not limited to):

    - USAGEs BINARY, floating-point, and PACKED-DECIMAL
    - The DELETE and REWRITE statements
    - I-O and EXTEND mode on an OPEN statement
    - BEFORE/AFTER ADVANCING on WRITE
    - READ/START PREVIOUS
    - SCREEN SECTION ACCEPT/DISPLAY statements
    - Record Locking and File Sharing

****

Now, in my opinion,  the one thing that COBOL has going for it over other
popular languages (like C and C++) is its portability.  I am really REALLY
concerned that allowing vendors to decide to include (or EXCLUDE) support
for these old AND NEW features based on "market positioning" or ANY THING
ELSE THEY WANT (hence, the "not limited to" phrase in the definition) is the
worst possible thing to happen to COBOL.  In fact, it is so bad, that I
question (I haven't made up my mind completely on this yet) that having a
Standard with this definition is WORSE than having no Standard at all
(which - after all - is basically what we have at the current time - when
there is no way to get amendments or even interpretations done on the '85
Standard - and there are no  conformance tests to validate implementations).

What do you think?

Please respond in comp.lang.cobol or via private email to me.  However, no
matter which way you feel (agree with me or disagree with me), if you have
strong feelings about this, PLEASE, let the Standards committees know.

If you are in the US (US resident, work for a US company, etc), then you can
send any comments for consideration by the US delegation to the ISO WG4
committee to

     das@microfocus.com

(These can include indications that you think this feature would be bad/good
in an ISO Standard or that the ANSI Standard should be different from the
ISO Standard - if the ISO Standard includes this definition.)

If you are in a country other than the US (and I really hope some other
countries WILL provide their input on this topic),  you can find out HOW to
reach your country's delegation by contacting the WG4 convenor at

    nwallace@us.ibm.com

or you can try to find it via the WG4 home page at

    http://anubis.dkuug.dk/jtc1/sc22/wg4/
```

#### ↳ Re: * Please read and comment

- **From:** "don ferrario" <don@ferrario.com>
- **Date:** 1999-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7a7vir$fvg$1@news1.epix.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
I vote for commonality and portability ABOVE ALL ELSE.

don ferrario
http://www.ferrario.com/don

William M. Klein wrote in message <7a7s8e$34s@dfw-ixnews10.ix.netcom.com>...
>(Posted to the COBOL Usenet Newsgroups - but with CC's to various
>individuals.)
>
>Preface:
```

#### ↳ Re: * Please read and comment

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36c88a84.28546110@news.enter.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote:

>(Posted to the COBOL Usenet Newsgroups - but with CC's to various
>individuals.)
…[33 more quoted lines elided]…
>****

Bill:

Sounds to me like the compiler companies will be able to claim ANSI
standard compliance, yet a source program which only uses the ANSI
standard features in a specific compiler won't necessarily compile
using a different compiler.

I agree that if it is worth having a standard, then it is worth having
a standard which is consistent across all compilers.  Why would there
even be a need for a standards committee if the compiler companies can
pick and choose what will work in their compiler and still claim to
support the standard?

Am I missing something here?


Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: * Please read and comment

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36c84ce6.0@news3.uswest.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
William Klein,

At the risk of sounding like a defeatist, I think the antics of the
Standards committee are going to hurt COBOL. I do not predict the doom of
COBOL by any means, or even a downturn in its use. But instead of getting in
gear and positioning COBOL as an attractive and modern programming language,
the Standards Committee seems to vote in a direction implying language
integrity is not the issue, but rather convenience of vendor implementation
is.

COBOL's huge installed base is and will shield it from this sort of thing.
However, it doesn't take a genius to look at language manual and see '85 on
the last standard. Even with the '89 addendum, that is still older than
Fortran's last standard.

A ton of stuff in, say C++, is vendor-determined, but that doesn't seem to
prevent their standards committee from moving forward and releasing a
standard.

Dragging the next Standard farther and farther looks, well, bad. IMO.

To take C++ as a an example again, it has a number of standard header files
included with the language.  Many are necessary for simply language
functionality, however, a few carry information on the vendor-defined values
for the specific implementation.  Too bad COBOL can't come up with some
standard ways to include vendor-specific information directly in the
language.  It wouldn't even require a compiler re-write, just have a
language mandated copybook library that contains a limited number of
predefined data items.  The names and values would clearly show the
attributes of such things as Bytes-in-Halfword-Binary,
Bytes-in-Fullword-Binary, Max-Unsigned-Fullword-Binary,
Max-Signed-Fullword-Binary, etc.  Simply glancing through the copybook would
tell a prospective programmer everything they needed to know.

COBOL is my language of choice, and I would like to see it supported more
vigorously by the most prominent authority over it, the Standards Committee.
What form do I feel such support should take? Stop arguing over
implementation issues. Start agreeing on language integrity. Publish a
Standard. Now.
```

#### ↳ Re: * Please read and comment

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7a7uth$1ih@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
William M. Klein (wmklein@ix.netcom.com) wrote:

:     - USAGEs BINARY, floating-point, and PACKED-DECIMAL
   THis one I don't care about all that much. The compiler should
figure it out, in my opinion, rather than the programmer. It is a move
towards strong typing in the language. 

:     - The DELETE and REWRITE statements
:     - I-O and EXTEND mode on an OPEN statement
   These two seem to be utterly necessary to me, unless you are using 
a database I suppose. What do they propose to replace them?

:     - BEFORE/AFTER ADVANCING on WRITE
:     - READ/START PREVIOUS
   Read previous is handy, and the before /after advancing makes non-cics
programming nice. Again, what do they propose to replace them with? 

:     - SCREEN SECTION ACCEPT/DISPLAY statements
   Oh my, this I could do without. Nothing but trouble in my opinion. 
Every vendor does it differently, on purpose I believe, in an attempt
to lock in customers. Bob Wolfe & crew got it right, and so did IBM
with Visual Age and Visual Age COBOL. 


:     - Record Locking and File Sharing
  Again, what in the world do they plan to replace this with? 


Is there some strong political motion in the background to cripple the 
language, or what?
```

##### ↳ ↳ Re: * Please read and comment

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1999-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7a84ru$gq@dfw-ixnews7.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <7a7uth$1ih@lotho.delphi.com>`

```
No one (as far as I can figure out) is saying that some vendors will or will
not "replace" these Standard features with something else. What they are
trying to do (again in my interpretation) is:

A) Make it optional for the vendors to implement them at all

B) Let them implement totally NON-standard "features" if they want - instead
of what the Standard defines.  (For example, IBM could keep COMP-1 and
COMP-2 as floating point and NEVER add the new portable floating-point data
types.)

Note: There is a BIG difference between what the '85 Standard says and what
the draft says about USAGE BINARY (just an example).  The '85 Standard says
that every COBOL implementation needs to include this syntax - but how they
"store" the data is hardware/software dependent.  What the draft Standard
says is that if the vendor doesn't want to even support this USAGE, they
don't even need to include support for the syntax - they can say AT THEIR
OWN DISCRETION that this is not part of the "market position - or something
else" for their processor and simply not support the syntax or semantics.

AGAIN, please do send notes to the committee people if you think this is
"bad" - don't just tell me.


paulr wrote in message <7a7uth$1ih@lotho.delphi.com>...
>William M. Klein (wmklein@ix.netcom.com) wrote:
>
…[29 more quoted lines elided]…
>
```

#### ↳ Re: * Please read and comment

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<cdUx2.6436$wj1.9559529@news2.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
William M. Klein wrote:
>
>if you have
>strong feelings about this, PLEASE, let the Standards committees know.

I don't think they're listening.
```

##### ↳ ↳ Re: * Please read and comment

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7a93nj$95a@dfw-ixnews9.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <cdUx2.6436$wj1.9559529@news2.mia>`

```

Judson McClendon wrote in message ...
>William M. Klein wrote:
>>
…[4 more quoted lines elided]…
>--


Judson,
  I really don't think that they have received much official input to hear.
I may be wrong (they have disappointed me on other issues) but I sure would
appreciate people at least taking the time to send them email to see if we
can make some progress.
```

#### ↳ Re: * Please read and comment

- **From:** John Piggott <John_Piggott@compuserve.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C8BBEE.5660@compuserve.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
I definitely agree that there are far too many processor-dependent 
elements in the forthcoming new Standard.  I accept the need in certain 
areas i.e.

--  Where a feature might have no meaning on some types of processor, 
e.g. graphics where the terminal has only alphanumerics.

--  Where it's a peripheral feature, such as debugging, or listing the 
source, that doesn't affect the proccessing of the program.

--  Where differences in architecture necessarily imply there will be 
differences in physical interpretation, such as number of bits in a COMP 
field.

In all other cases, I simply cannot accept the case for processor-defined 
elements. Is it because the COBOL Committee can't be bothered or doesn't 
have the knowledge to get the precise details down on paper? Or is it 
because some Vendors have interpreted a woolly concept differently in the 
past and we can't reconcile them?

What strikes me most of all is that, instead of regarding these elements 
as historical mishaps, we're actually adding More and More in the new 
Standard. Bill's list shows exactly the sort of areas that are crucial to 
operation of the program and should Not have P-D concepts in them.


William M. Klein wrote:
> 
> (Posted to the COBOL Usenet Newsgroups - but with CC's to various
> individuals.)
> 
> Preface:etc.
    - USAGEs BINARY, floating-point, and PACKED-DECIMAL
    - The DELETE and REWRITE statements
    - I-O and EXTEND mode on an OPEN statement
    - BEFORE/AFTER ADVANCING on WRITE
    - READ/START PREVIOUS
    - SCREEN SECTION ACCEPT/DISPLAY statements
    - Record Locking and File Sharing
etc.
```

##### ↳ ↳ Re: * Please read and comment

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C86BB4.66CB@compaq.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com>`

```
John Piggott wrote:
> 
> I definitely agree that there are far too many processor-dependent
…[11 more quoted lines elided]…
> field.

Of course you left out where the operating system does not support the 
feature.  "They" (meaning me and the other committee members, who are 
not a bunch of ogres but just people trying to do the best we can to a 
very hostile bunch who don't really understand the standards process) 
don't want to force every vendor to rewrite their file system just to 
make a new COBOL feature.  That was done with indexed files for the 
'74 standard and there was a huge uproar, much of it from users who 
felt it was different than what they were using before and didn't want 
the vendors to hit them with the cost of implementing the feature.  
The crux of it all is that it would cost everybody money, including 
all the users, to force implementors to change their system (in some 
cases very dramatically) to make all this work.  In real life, most 
major vendors will have all this stuff anyhow.

I might also mention that I think the one sentence in the conformance 
section that says the vendor does not have to do the syntax should be 
changed to say that all the syntax should be supported, even if it 
isn't going to work.  Also, that paragraph is in conflict with the 
processor-dependent list where it merely says that certain features 
require certain devices.  There should be two lists, one that requires 
the stuff if you have that kind of device, and one where a system 
rewrite might be required.

> In all other cases, I simply cannot accept the case for processor-defined
> elements. Is it because the COBOL Committee can't be bothered or doesn't
> have the knowledge to get the precise details down on paper?

That is a cmpletely absurd statement and John knows it.  He is part of 
the process as well as I am.  We have the knowledge and know how to 
put down the precise details.  They are there and that is why they are 
PD.

>Or is it
> because some Vendors have interpreted a woolly concept differently in the
> past and we can't reconcile them?

In the case of screen processing, that is probably why.  Also, file 
sharing is somewhat in that category in that everybody does it in a 
different way.

> What strikes me most of all is that, instead of regarding these elements
> as historical mishaps, we're actually adding More and More in the new
…[9 more quoted lines elided]…
>     - USAGEs BINARY, floating-point, and PACKED-DECIMAL

The vendor has to do these in a way applicable to his hardware (and 
his historical way).  Not all the same way for everyone.  I do think 
all vendors should support the syntax in the same way.

>     - The DELETE and REWRITE statements

All this one says is that they require a mass storage device.  This is 
obvious.  I suppose if the vendor does not support mass storage 
devices then there is no need for these statements.

>     - I-O and EXTEND mode on an OPEN statement

Same as the previous one.

>     - BEFORE/AFTER ADVANCING on WRITE

All is says is that it requires a device that can position (like a 
printer).

>     - READ/START PREVIOUS

This one is different.  Another case of whether or not we should force 
implementors to rewrite their file system.

>     - SCREEN SECTION ACCEPT/DISPLAY statements

This definitely belongs where it is.  It is done all kinds of ways on 
all kinds of sytems.  In my opinion, it is obsolete already and should 
not even be in the standard.

>     - Record Locking and File Sharing

Another one requiring an operating system rewrite.  And, the systems 
that do have it all do it in a different way.
```

###### ↳ ↳ ↳ Re: * Please read and comment

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<DH%x2.6582$wj1.9761766@news2.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com>`

```
Don Nelson wrote:
>
> "They" (meaning me and the other committee members, who are
>not a bunch of ogres but just people trying to do the best we can to

Hey, we're just the shmucks who will spend the rest of our careers
living with this stuff. :-)

>a very hostile bunch who don't really understand the standards process)

Don, you're a nice guy.  But has it occurred to you that there may
be very good reasons for the hostility and lack of understanding?
I've spent my whole adult life programming, mostly in COBOL.  In my
only experience with the standards committees, I made what I know
from long experience were very good points.  They were dismissed out
of hand.  They weren't even interested in my input, whatever merit
might have been there was irrelevant.  The language was typical of
an arrogant elitist attitude.  I know that attitude well, because I
have seen it a lot.  I used to have such an attitude myself, many
years ago in my young and stupid days.  But I've lived all my life
so far without input to the standards committees; it won't hurt me
to live the rest of it without any. :-)  But it does help me to
understand where the hostility is coming from.  It also helps me to
understand why there is boneheaded stuff in the proposed standard.

Does it make more sense to disenfranchise all programmers who don't
know all the ins and outs of the standards process, or to structure
the standards process to glean the accumulated knowledge and wisdom
of those programmers?  Do you really think the people on the standards committees have a corner on understanding how things should
be done?
Why set the bar so high?  Who is better served by doing so?  Where is
the wisdom in rejecting input, just because it wasn't sent in the
proper form?  No wonder the new standard gets such criticism around
here.  Under any other circumstances, people would be judged as idiots
for so restricting their input.  Yet we are told "you just don't
understand the standards process."  Okay, so we have a process that
.01% of the affected programmers understand.  Who is at fault?  If we
have a task to make something happen correctly, what is the most
important, to create a series of arbitrary rules and enforce them no
matter if the result is good, or to adjust the rules to work?  If your
life depended on getting the very most accumulated knowledge and
wisdom from programmers as a whole, would you use the process used by
the standards committees?  What encouragement do programmers get who
do try to give input to the standards process?  I'm not talking about
your personal responses Don.  Be honest here, what is the typical
response when some programmer makes a suggestion, but does not know
the proper procedures?

Let's take a poll here.  You people in this "very hostile bunch", why
are you hostile? :-)
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** rtwolfe@flexus.com (Bob Wolfe)
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36c88d3b.29241049@news.enter.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <DH%x2.6582$wj1.9761766@news2.mia>`

```
"Judson McClendon" <judmc123@bellsouth.net> wrote:

>Let's take a poll here.  You people in this "very hostile bunch", why
>are you hostile? :-)

I'm hostile because I don't have a cool red sports car like you do!

;-)



Bob Wolfe, flexus
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C9B852.64B5@compaq.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <DH%x2.6582$wj1.9761766@news2.mia>`

```
Judson McClendon wrote:
> 
> Don Nelson wrote:
…[5 more quoted lines elided]…
> living with this stuff. :-)

So do we!!

> 
> >a very hostile bunch who don't really understand the standards process)
> 
> Don, you're a nice guy.

Thanks.

> But has it occurred to you that there may
> be very good reasons for the hostility and lack of understanding?
> I've spent my whole adult life programming, mostly in COBOL.

I've spent 38 years programming, using over 20 different languages 
(including COBOL).  And 7 years in punch card systems before that.  I 
do understand the life of a programmer (since I are one, as they say).

>  In my
> only experience with the standards committees, I made what I know
> from long experience were very good points.  They were dismissed out
> of hand.

Nothing is dismissed out of hand.  Everything that comes in is 
discussed and we try to be reasonable.

> They weren't even interested in my input, whatever merit
> might have been there was irrelevant.

I don't recall your input.  Often we get suggestions for new features 
way after the cutoff for them.  These are put in a list to be 
discussed after work on the current standard is completed.

> The language was typical of
> an arrogant elitist attitude.

Nobody in the group is arrogant and elitist.  I'm sorry that you and 
others seem to get that idea.

> I know that attitude well, because I
> have seen it a lot.  I used to have such an attitude myself, many
…[4 more quoted lines elided]…
> understand why there is boneheaded stuff in the proposed standard.

One person's bonehead is anothers cool head.  A lot of the criticism 
is because people don't know all of the stuff, they just hear 
fragments - a la Bill's initial message.  Taken out of context, lots 
of things seem boneheaded.

> Does it make more sense to disenfranchise all programmers who don't
> know all the ins and outs of the standards process, or to structure
> the standards process to glean the accumulated knowledge and wisdom
> of those programmers?

Absolutely no one is disenfranchised.  We discuss every item that is 
sent to us by non-members.  This is one of the reasons the standard is 
so late, by the way.

> Do you really think the people on the standards committees have a corner on understanding how things should
> be done?

Of course not.

> Why set the bar so high?  Who is better served by doing so?  Where is
> the wisdom in rejecting input, just because it wasn't sent in the
> proper form?

As I said, it is not rejected.

> No wonder the new standard gets such criticism around
> here.  Under any other circumstances, people would be judged as idiots
> for so restricting their input.  Yet we are told "you just don't
> understand the standards process."

What I meant by that (probably a bad choice of words - I was a bit 
steamed at the time) is that I feel from the tone of posts in this 
group that many think all we do is just put in a new feature and that 
is that.  We have to look at the impact on everything on the rest of 
the language, have all the text reviewed numerous times, resolve all 
the comments, and so on and so on.  That is the process I meant.  This 
includes comments from outside the group as well.

> Okay, so we have a process that
> .01% of the affected programmers understand.  Who is at fault?  If we
…[5 more quoted lines elided]…
> the standards committees?

What would you use?  We accept comments from any and all.

> What encouragement do programmers get who
> do try to give input to the standards process?  I'm not talking about
> your personal responses Don.  Be honest here, what is the typical
> response when some programmer makes a suggestion, but does not know
> the proper procedures?

It depends on the suggestion.  Some are of the form "you idiots didn't 
do this or that".  Some we can't really do for compatibility reasons, 
and so on.  Most of the new features in the standard resulted from 
programmers making suggestions (often to their vendors who then 
brought it on to us).

> Let's take a poll here.  You people in this "very hostile bunch", why
> are you hostile? :-)
> --
I might have been a bit too hostile.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<RVmy2.10706$Fs.10909974@news4.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <DH%x2.6582$wj1.9761766@news2.mia> <36C9B852.64B5@compaq.com>`

```
Don Nelson wrote:
>Judson McClendon wrote:
>>
…[6 more quoted lines elided]…
>discussed and we try to be reasonable.

So I'm lying, huh?  See what I mean Don, now even you are doing it.
Don't you think I know when I have tried to give input and it is
rejected out of hand?  Not only did I get the cold shoulder, I was
fairly chastised as well.

>> They weren't even interested in my input, whatever merit
>> might have been there was irrelevant.
…[3 more quoted lines elided]…
>discussed after work on the current standard is completed.

You don't recall my input because you never saw it.  It was rejected
out of hand, just as I said, and just as you said above that it never
is.  I think part of the problem is that people on the committees, and
yes, apparently even you, don't realize the face that is presented to
the programming community as a whole.

>> The language was typical of an arrogant elitist attitude.
>
>Nobody in the group is arrogant and elitist.  I'm sorry that you and
>others seem to get that idea.

Now you not only think I'm lying, you must think I'm stupid too.  I
don't know any of the people enough to know if they are arrogant and
elitist, but I didn't say that.  What I said was "The language was
typical of an arrogant elitist attitude."  And it was, absolutely.
Where do you think I 'and others' get that idea?  Don't you think we
have enough experience in dealing with people to recognize it?

>> I know that attitude well, because I
>> have seen it a lot.  I used to have such an attitude myself, many
…[9 more quoted lines elided]…
>of things seem boneheaded.

I realize that, but some things are boneheaded period.  I've been
around long enough to recognize that when I see it.  Unfortunately,
I've done boneheaded things myself, and so has the committee.

>> Does it make more sense to disenfranchise all programmers who don't
>> know all the ins and outs of the standards process, or to structure
…[4 more quoted lines elided]…
>sent to us by non-members.

You didn't discuss mine.  You said above you hadn't seen it, and I
believe you.  I was certainly 'disenfranchised'.  You think people
express hostility because their input is accepted too readily? ;-)

>> Why set the bar so high?  Who is better served by doing so?  Where is
>> the wisdom in rejecting input, just because it wasn't sent in the
>> proper form?
>
>As I said, it is not rejected.

Oh, but it is.  Perhaps you really don't realize that, but it happens.
That's what I am trying to get you to accept.

>> No wonder the new standard gets such criticism around
>> here.  Under any other circumstances, people would be judged as idiots
…[9 more quoted lines elided]…
>includes comments from outside the group as well.

I believe what you say.  But what you aren't seeing is that the process
simply is not as open as you seem to believe.  Being on the inside, you
don't see it as we on the outside do.  Why in the world do you think
people are 'hostile'?  Just for jollies?  There are reasons Don, and
I have been trying to articulate them, but you aren't very receptive.
I believe that you and probably most of the people on the committees
are well intentioned.  But the process does not appear to those on the
outside as you think it does.  Because you are well intentioned does
not make you right, or what you are doing effective.  That must be
judged by others, just as in any professional arena.

>> Okay, so we have a process that
>> .01% of the affected programmers understand.  Who is at fault?  If we
…[7 more quoted lines elided]…
>What would you use?

I would keep trying everything I or anyone else could think of until
something worked.  When the vast majority of programmers have no input
into the system, it is flawed.  No wonder they are hostile.

>We accept comments from any and all.

You didn't accept mine, and I sent it to two different committee members.
It is hard for me to believe that, of all the people who have tried to
submit input, I am the only one who got the cold shoulder.  One of the
ways the Japanese companies trounced us decades ago was by listening
to their employees.  Even the lowliest peon could put suggestions in a
suggestion box and it was fairly reviewed.  No one, and no group, has a
corner on good ideas.  I was jumped on because I had not submitted my
suggestion in the proper form.  Who gives a rip?  If somebody comes up
and tells me a good idea, I'm not going to chew him out because he didn't
do it in the proper format!  It's the idea that counts, not the format.
Sure, tell him the proper way for next time, but don't shut out the idea
because of it.  But that's exactly what happened to me, from two people.
Do you expect me to believe that was a completely unique event?  Do you
believe that?

>> What encouragement do programmers get who
>> do try to give input to the standards process?  I'm not talking about
…[5 more quoted lines elided]…
>do this or that".

I hope you believe I used a more respectful approach than that. ;-)
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7acvsm$l91@sjx-ixn5.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <DH%x2.6582$wj1.9761766@news2.mia> <36C9B852.64B5@compaq.com> <RVmy2.10706$Fs.10909974@news4.mia>`

```
I don't want to get into the history of what has and has not happened with
unsolicited input to the Standards committee in the past.  AND as readers of
this NG know, I don't always like what happens to much of the input that I
provide.

ON THE OTHER HAND,
  I do want to stress that (as far as I know) any and ALL input that is sent
to the J4 chair (via email or hardcopy) today - IS processed by the
committee.

Due to problems with the email system as Micro Focus shifts to Merant, Don
Schricker may be a "little" hard to get to for a few days, but please,
PLEASE, do send him anything that you want the committee to process and I
strongly believe it will be.  As a paid observer, I do see the agenda (which
is actually on-line and I can point other people to) - so if you think your
current input MAY not be processed, let me know and I will be happy to track
it for you.

For the current time, please send all email for consideration to

   doncobol@mediaone.net

(and CC me at wmklein@ix.netcom.com - if you want me to track it for you).

I want to stress that Don Schricker takes all input - regardless of "format"
and turns it into the correct input format.

NOTE:  Input to WG4 or the ISO committee is *not* accepted from
individuals - only from country delegations.  If anyone has tried to send
something to them in the past, this would be "rejected".  However, if you
submit it to YOUR country delegation, they can submit it for you.  (Again,
Don Schricker is the "portal" for US submissions.  If you need to know how
to reach some other country's delegation,  I can help you reach the WG4
convenor and she can provide you information on how to reach your
delegation.)
```

###### ↳ ↳ ↳ Re: * Please read and comment

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7aaf0h$bj6@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com>`

```

Hold up Don - 
  Nobody herei s calling you one of 'them.' If anything, you are definately
the 'Man in the White Hat.' <grin> 

  You know my background is not pure COBOL, and I find the diffeence i the 
COBOL standards practice and the Ada standards practice, well, 
mystifying. In Ada, if it does pass *all* the qualifiing standards, 
it is NOT Ada. It may be an Ada like compiler, but it isn't Ada. 

  This is an incredibly valuable thing. People can pick and choose 
Ada compilers based upon their extensions or platform specialities,
and *KNOW* that all the Ada things will work - as advertised. Every
time. 

  Ada, like COBOL, has some - ah - 'grey' areas. Tasking for example,
leaves a lot of things as 'Implemetor Defined'. But the base level of
tasking all have to be there and produce identical results. (Well, 
at least results identical enough to pass the validation suite.) 

  ALong those lines, why not make it possible for vendors to either 
leave out sections entirely (day file system processing) or include
a proprietary module? But if they *do* implement it in the core language,
it has to be such and such a way? 

 Not as good as totally standardized language, but then, there are 
still shops writing in COBOL 74 I think. Maybe even older stuff. 

  Hell, I have to fight at work to get the modern compiler on the mainframe.

-Paul




Don Nelson (don.nelson@compaq.com) wrote:
: John Piggott wrote:
: > 
: > I definitely agree that there are far too many processor-dependent
: > elements in the forthcoming new Standard.  I accept the need in certain
: > areas i.e.
: > 
: > --  Where a feature might have no meaning on some types of processor,
: > e.g. graphics where the terminal has only alphanumerics.
: > 
: > --  Where it's a peripheral feature, such as debugging, or listing the
: > source, that doesn't affect the proccessing of the program.
: > 
: > --  Where differences in architecture necessarily imply there will be
: > differences in physical interpretation, such as number of bits in a COMP
: > field.

: Of course you left out where the operating system does not support the 
: feature.  "They" (meaning me and the other committee members, who are 
: not a bunch of ogres but just people trying to do the best we can to a 
: very hostile bunch who don't really understand the standards process) 
: don't want to force every vendor to rewrite their file system just to 
: make a new COBOL feature.  That was done with indexed files for the 
: '74 standard and there was a huge uproar, much of it from users who 
: felt it was different than what they were using before and didn't want 
: the vendors to hit them with the cost of implementing the feature.  
: The crux of it all is that it would cost everybody money, including 
: all the users, to force implementors to change their system (in some 
: cases very dramatically) to make all this work.  In real life, most 
: major vendors will have all this stuff anyhow.

: I might also mention that I think the one sentence in the conformance 
: section that says the vendor does not have to do the syntax should be 
: changed to say that all the syntax should be supported, even if it 
: isn't going to work.  Also, that paragraph is in conflict with the 
: processor-dependent list where it merely says that certain features 
: require certain devices.  There should be two lists, one that requires 
: the stuff if you have that kind of device, and one where a system 
: rewrite might be required.

: > In all other cases, I simply cannot accept the case for processor-defined
: > elements. Is it because the COBOL Committee can't be bothered or doesn't
: > have the knowledge to get the precise details down on paper?

: That is a cmpletely absurd statement and John knows it.  He is part of 
: the process as well as I am.  We have the knowledge and know how to 
: put down the precise details.  They are there and that is why they are 
: PD.

: >Or is it
: > because some Vendors have interpreted a woolly concept differently in the
: > past and we can't reconcile them?

: In the case of screen processing, that is probably why.  Also, file 
: sharing is somewhat in that category in that everybody does it in a 
: different way.

: > What strikes me most of all is that, instead of regarding these elements
: > as historical mishaps, we're actually adding More and More in the new
: > Standard. Bill's list shows exactly the sort of areas that are crucial to
: > operation of the program and should Not have P-D concepts in them.
: > 
: > William M. Klein wrote:
: > >
: > > (Posted to the COBOL Usenet Newsgroups - but with CC's to various
: > > individuals.)
: > >
: > > Preface:etc.
: >     - USAGEs BINARY, floating-point, and PACKED-DECIMAL

: The vendor has to do these in a way applicable to his hardware (and 
: his historical way).  Not all the same way for everyone.  I do think 
: all vendors should support the syntax in the same way.

: >     - The DELETE and REWRITE statements

: All this one says is that they require a mass storage device.  This is 
: obvious.  I suppose if the vendor does not support mass storage 
: devices then there is no need for these statements.

: >     - I-O and EXTEND mode on an OPEN statement

: Same as the previous one.

: >     - BEFORE/AFTER ADVANCING on WRITE

: All is says is that it requires a device that can position (like a 
: printer).

: >     - READ/START PREVIOUS

: This one is different.  Another case of whether or not we should force 
: implementors to rewrite their file system.

: >     - SCREEN SECTION ACCEPT/DISPLAY statements

: This definitely belongs where it is.  It is done all kinds of ways on 
: all kinds of sytems.  In my opinion, it is obsolete already and should 
: not even be in the standard.

: >     - Record Locking and File Sharing

: Another one requiring an operating system rewrite.  And, the systems 
: that do have it all do it in a different way.

: -- 
: Don Nelson
: COBOL Development, Compaq Computer Corp.
: Member, NCITS J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
: don.nelson@compaq.com
: No clever quotes here
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-15T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7aaqh3$9ka$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <7aaf0h$bj6@lotho.delphi.com>`

```
Validation suite ... mmm.  Is there one for Cobol?

paulr wrote in message <7aaf0h$bj6@lotho.delphi.com>...
>
>Hold up Don -
…[26 more quoted lines elided]…
>  Hell, I have to fight at work to get the modern compiler on the
mainframe.
>
>-Paul
…[18 more quoted lines elided]…
>: > differences in physical interpretation, such as number of bits in a
COMP
>: > field.
>
…[23 more quoted lines elided]…
>: > In all other cases, I simply cannot accept the case for
processor-defined
>: > elements. Is it because the COBOL Committee can't be bothered or
doesn't
>: > have the knowledge to get the precise details down on paper?
>
…[6 more quoted lines elided]…
>: > because some Vendors have interpreted a woolly concept differently in
the
>: > past and we can't reconcile them?
>
…[4 more quoted lines elided]…
>: > What strikes me most of all is that, instead of regarding these
elements
>: > as historical mishaps, we're actually adding More and More in the new
>: > Standard. Bill's list shows exactly the sort of areas that are crucial
to
>: > operation of the program and should Not have P-D concepts in them.
>: >
…[48 more quoted lines elided]…
>: No clever quotes here
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C9BA1E.F82@compaq.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <7aaf0h$bj6@lotho.delphi.com> <7aaqh3$9ka$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Validation suite ... mmm.  Is there one for Cobol?
> 
There is.  However, due to government budget cuts the feds no longer 
do this service.  The did it starting with the 1974 standard on up to 
a year or so ago.  No fed contracts unless you passed.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** scm@bolo.freeserve.co.uk (Shaun C. Murray)
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36cdbf82.22341725@news.enterprise.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <7aaf0h$bj6@lotho.delphi.com> <7aaqh3$9ka$1@news.igs.net>`

```
On Mon, 15 Feb 1999 23:09:36 -0500, "Donald Tees"
<donald@willmack.com> wrote:

>Validation suite ... mmm.  Is there one for Cobol?

Oh yes. As a lowly 17 year old at Micro Focus I was made to run it
over and over again with mind-numbingly similar results. Oh did I not
look forward to the CM and DB tests and the odd NC test that was
manual. The results sheets still give me nightmares.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C9B999.139E@compaq.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36C8BBEE.5660@compuserve.com> <36C86BB4.66CB@compaq.com> <7aaf0h$bj6@lotho.delphi.com>`

```
paulr wrote:
> 
> Hold up Don -
…[16 more quoted lines elided]…
> at least results identical enough to pass the validation suite.)

Ada had it lots easier.  It was developed from scratch with a tough 
standard right off and could learn from the mistakes other languages 
made.  COBOL was somewhat loose (in fact really loose) in the 
beginning and we have always had to maintain compatibility with the 
past.  Lots of this is in areas that were not well defined so they 
have to remain so.  It would be cool if we could make an iron standard 
like Ada.  The closest we come is to require vendors to flag 
everything that is non-standard.  That way, users can create a program 
that is quite portable.

Another thing is that Ada has no real i-o.  Most of the fuzzy areas 
are in i-o.

>   ALong those lines, why not make it possible for vendors to either
> leave out sections entirely (day file system processing) or include
> a proprietary module? But if they *do* implement it in the core language,
> it has to be such and such a way?

Actually, that is pretty much how it is.

>  Not as good as totally standardized language, but then, there are
> still shops writing in COBOL 74 I think. Maybe even older stuff.

Even older stuff does still exist.

>   Hell, I have to fight at work to get the modern compiler on the mainframe.
> 
Keep fighting.
```

#### ↳ Re: * Please read and comment

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36c9685b@news3.us.ibm.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
William M. Klein wrote in message <7a7s8e$34s@dfw-ixnews10.ix.netcom.com>...
>Now, in my opinion,  the one thing that COBOL has going for it over other
>popular languages (like C and C++) is its portability.  I am really REALLY
>concerned that allowing vendors to decide to include (or EXCLUDE) support
>for these old AND NEW features based on "market positioning" or ANY THING
>ELSE THEY WANT (hence, the "not limited to" phrase in the definition) is
the
>worst possible thing to happen to COBOL.  In fact, it is so bad, that I
>question (I haven't made up my mind completely on this yet) that having a
…[3 more quoted lines elided]…
>Standard - and there are no  conformance tests to validate
implementations).


I agree 100% with Bill on all of his points. Some (e.g. Don Nelson) have
argued
that one cannot force the vendor to implement stuff not supported by his
hardware
or file system, and that, therefore, in/exclusion of "processor-dependent"
features
are necessary. This argument IMHO is weak. Consider the case of the PC.
Early PCs didn't have numeric co-processors, yet all COBOL vendors support
PACKED DECIMAL. No PC has indexed files as part of their file system, yet
all vendors support them, etc..

Now, there are some limitations that may be hard to circumvent, such as
length
and case-sensitivity of program names and file names, but these are under
programmer control and do not make it impossible to write portable programs.

If something must be optional, let it be the OO features. These have not yet
proven themselves "in the field". It might turn out that they will go the
way of
other attempts at pre-mature standardization, e.g. the COMMUNICATION
features..
```

##### ↳ ↳ Re: * Please read and comment

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<Pcey2.6846$Xl5.11005540@news1.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net>`

```
Leif Svalgaard wrote:
>
>I agree 100% with Bill on all of his points. Some (e.g. Don Nelson) have
…[19 more quoted lines elided]…
>features..


Excellent post!  I wholeheartedly concur, most particularly about the
OO features.  The financial figures I have seen from OO projects in other
languages to this date have simply not borne out the claims of the rabid
OO proponents.  I think it is amazing that so much time and energy has
been spent on a technique which has simply not proven itself conclusively,
yet we get quibbling over definitely needed features like record locking.
```

###### ↳ ↳ ↳ Re: * Please read and comment

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7abuco$ene@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia>`

```
Judson McClendon (judmc123@bellsouth.net) wrote:
: Leif Svalgaard wrote:
: >
: >I agree 100% with Bill on all of his points. Some (e.g. Don Nelson) have
: >argued
: >that one cannot force the vendor to implement stuff not supported by his
: >hardware
: >or file system, and that, therefore, in/exclusion of "processor-dependent"
: >features
: >are necessary. This argument IMHO is weak. Consider the case of the PC.
: >Early PCs didn't have numeric co-processors, yet all COBOL vendors support
: >PACKED DECIMAL. No PC has indexed files as part of their file system, yet
: >all vendors support them, etc..
: >
: >Now, there are some limitations that may be hard to circumvent, such as
: >length
: >and case-sensitivity of program names and file names, but these are under
: >programmer control and do not make it impossible to write portable programs.
: >
: >If something must be optional, let it be the OO features. These have not yet
: >proven themselves "in the field". It might turn out that they will go the
: >way of
: >other attempts at pre-mature standardization, e.g. the COMMUNICATION
: >features..


: Excellent post!  I wholeheartedly concur, most particularly about the
: OO features.  The financial figures I have seen from OO projects in other
: languages to this date have simply not borne out the claims of the rabid
: OO proponents.  I think it is amazing that so much time and energy has
: been spent on a technique which has simply not proven itself conclusively,
: yet we get quibbling over definitely needed features like record locking.
: --
: Judson McClendon      judmc123@bellsouth.net  (remove numbers)


Ah, but it *has* Judson. Time and time again it has proven itself 
valid in large scale projects, often bringing in extremely complex
projects ahead of schedule and under budget. 

The issue is that most COBOL projects, in fact *all* the COBOL 
projects I have ever seen, are not really 'large scale.' Think of 
a team of 200+ programmers going at something for 2+ years to
get an idea of what I mean by 'large scale.' 

OO Technology, if properly applied, always works. The problem is 
how to apply it to small to medium scale projects economically.

Given that, I do agree it is a little early to standardize on OO
technology, though I think IBM got it right, for a start. They
need to issue version 2 of thier technology. :) 

-Paul
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<rHfy2.6849$Xl5.11040286@news1.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com>`

```
paulr wrote:
>
>Ah, but it *has* Judson. Time and time again it has proven itself
>valid in large scale projects, often bringing in extremely complex
>projects ahead of schedule and under budget.


No doubt that's why 45% of all such MIS projects today fail from cost or
time overruns, or failure to meet design goals.  Twenty years ago this
figure would have been a joke.  Stop reading 'filtered' OO hype and look
at the bottom line figures; it's quite a different picture. :-)
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C99444.BF427C0F@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <rHfy2.6849$Xl5.11040286@news1.mia>`

```
> >Ah, but it *has* Judson. Time and time again it has proven itself
> >valid in large scale projects, often bringing in extremely complex
…[5 more quoted lines elided]…
> at the bottom line figures; it's quite a different picture. :-)

On the other hand, 20 years ago we didn't have the same type of
integrated mega projects.  Typically a bug in one COBOL program won't
crash the whole system.  Once we tightly integrate huge systems we need
different methodologies.  NT with all of its bugs and all of its
manhours couldn't be designed any other way.

My objection is the way academics (and others) have of assuming that
once they determined the value of this tool in some instances - that it
should be retrofitted to fit in all cases.  How many applications are
suited for both OO and for COBOL?  

If OO is good, and COBOL isn't a good fit for OO, does that mean COBOL
is bad?  It does if OO is good for everything.  But it isn't.  Different
needs require different tools.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7ac6lo$l8f@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <rHfy2.6849$Xl5.11040286@news1.mia>`

```
Judson McClendon (judmc123@bellsouth.net) wrote:
: paulr wrote:
: >
: >Ah, but it *has* Judson. Time and time again it has proven itself
: >valid in large scale projects, often bringing in extremely complex
: >projects ahead of schedule and under budget.


: No doubt that's why 45% of all such MIS projects today fail from cost or
: time overruns, or failure to meet design goals.  Twenty years ago this
: figure would have been a joke.  Stop reading 'filtered' OO hype and look
: at the bottom line figures; it's quite a different picture. :-)
: --
: whoever believes in Him should not perish but have everlasting life."

<grin> I'm not reading filtered OO stuff. :( I'm talking from flat 
out experience, though admittedly with real-time systems and not with 
COBOL. I bet after your first sucessful OO project, you turn into an
evangalistia... :) :) :) :) :) :)

-Paul

i
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 6)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C99FD5.868DB04C@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <rHfy2.6849$Xl5.11040286@news1.mia> <7ac6lo$l8f@lotho.delphi.com>`

```
> <grin> I'm not reading filtered OO stuff. :( I'm talking from flat
> out experience, though admittedly with real-time systems and not with
> COBOL. I bet after your first sucessful OO project, you turn into an
> evangalistia... :) :) :) :) :) :)

I get converted to lots of tools after I find how well they work.  But
not for all tasks.  I enjoyed the OO I did in school, but while my
masters was in OO, my capstone project was about how much life the old
technologies have and deserve.  No tool fits all problems the best.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CA8192.2EF0531F@att.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com>`

```
paulr wrote:
> 
(snip)
> 
> OO Technology, if properly applied, always works.

"Always" (along with "Never") is not a good word to use in USENET or in
a marriage (or in court, now that I think of it), tends to spark fights.

Bill Lynch :-)
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7aehju$p32$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net>`

```

William Lynch wrote in message <36CA8192.2EF0531F@att.net>...
>paulr wrote:
>>
…[5 more quoted lines elided]…
>a marriage (or in court, now that I think of it), tends to spark fights.


All technology, if properly applied, always works.  I have yet
to see a procedural program that is totally bug free just
decide not work one day, for absolutely no reason.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<%%zy2.7136$Xl5.11569436@news1.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net> <7aehju$p32$1@news.igs.net>`

```
Donald Tees wrote:
>
>I have yet
>to see a procedural program that is totally bug free just
>decide not work one day, for absolutely no reason.

Compiler bug? ;-)
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7af0on$7mj$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net> <7aehju$p32$1@news.igs.net> <%%zy2.7136$Xl5.11569436@news1.mia>`

```
And "OO" programs are immune to compiler bugs?

Judson McClendon wrote in message
>Donald Tees wrote:
>>
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<GgEy2.7191$Xl5.11697308@news1.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net> <7aehju$p32$1@news.igs.net> <%%zy2.7136$Xl5.11569436@news1.mia> <7af0on$7mj$1@news.igs.net>`

```
Donald Tees wrote:
>And "OO" programs are immune to compiler bugs?

Of course!  Don't you listen to the OO proponents? ;-)
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36cb86d1.30446305@news1.ibm.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net> <7aehju$p32$1@news.igs.net> <%%zy2.7136$Xl5.11569436@news1.mia> <7af0on$7mj$1@news.igs.net> <GgEy2.7191$Xl5.11697308@news1.mia>`

```
On Wed, 17 Feb 1999 18:55:34 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:

>Donald Tees wrote:
>>And "OO" programs are immune to compiler bugs?
>
>Of course!  Don't you listen to the OO proponents? ;-)

Ah... but the bad performance and erroneous results of the application
program are .... inherited.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7agshl$llc$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net> <7aehju$p32$1@news.igs.net> <%%zy2.7136$Xl5.11569436@news1.mia> <7af0on$7mj$1@news.igs.net> <GgEy2.7191$Xl5.11697308@news1.mia> <36cb86d1.30446305@news1.ibm.net>`

```
Does that make them legacy programs?
;<)

Thane Hubbell wrote in message <36cb86d1.30446305@news1.ibm.net>...
>On Wed, 17 Feb 1999 18:55:34 GMT, "Judson McClendon"
><judmc123@bellsouth.net> wrote:
…[7 more quoted lines elided]…
>program are .... inherited.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CAD11C.3E60C2B5@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net>`

```
> > OO Technology, if properly applied, always works.
> 
…[3 more quoted lines elided]…
> Bill Lynch :-)


Of course there is that clause making the statement meaningless.

A hammer, if properly applied, always works.  Of course when people use
a hammer to unscrew a screw, it isn't being properly applied.

It is quite possible to have OO technology with bugs in it. 

The word "works" is open to interpretation.  Does that mean that the
methodology works, or the programs work?

Spaghetti code, when properly applied, always works.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 6)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7aeo3q$thk@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <Pcey2.6846$Xl5.11005540@news1.mia> <7abuco$ene@lotho.delphi.com> <36CA8192.2EF0531F@att.net> <36CAD11C.3E60C2B5@NOSPAMhome.com>`

```
Well, if the methodology works, the programs will work. 
The end result of all this programming effort, from 
design to QA is to produce a peice of software that
meets a need, and operates properly, is as error free
as possible, runs within it its design limits, is reasonable
to modify, and costs as little as possible to develope, i
maintain and support. 

OO technology supports all of those aims of course. 
So does 'Structured Programming.' So does a half
dozen other methodologies...

OO Methodologies are as varied as any other field; what
works for an embedded system driving and aircraft probably
isn't going to be idea for an online cash managment system. 
And vice versa of course.

-Paul


Howard Brazee (brazee@NOSPAMhome.com) wrote:
: > > OO Technology, if properly applied, always works.
: > 
: > "Always" (along with "Never") is not a good word to use in USENET or in
: > a marriage (or in court, now that I think of it), tends to spark fights.
: > 
: > Bill Lynch :-)


: Of course there is that clause making the statement meaningless.

: A hammer, if properly applied, always works.  Of course when people use
: a hammer to unscrew a screw, it isn't being properly applied.

: It is quite possible to have OO technology with bugs in it. 

: The word "works" is open to interpretation.  Does that mean that the
: methodology works, or the programs work?

: Spaghetti code, when properly applied, always works.
```

##### ↳ ↳ Re: * Please read and comment

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<vthy2.5$682.144@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net>`

```

Leif Svalgaard wrote in message <36c9685b@news3.us.ibm.net>...
[...]
>
>I agree 100% with Bill on all of his points. Some (e.g. Don Nelson) have
…[8 more quoted lines elided]…
>all vendors support them, etc..


Numeric coprocessors on PCs have nothing to do with decimal
arithmetic. The coprocessor is for floating-point. The x86 micro-
processor instruction set has instructions for decimal arithmetic. It is
these instructions that allow for implementation of packed-decimal.

PCs have a concept of "mass storage" and a "mass storage
device" (in the form of a disk drive). This is sufficient to allow for
the implementation of indexed files.

Furthermore, the vendors, who implemented COBOL on PCs,
likely wanted to supply full-featured systems, "Just like the
mainframes!"

----- Hypothetical situation -------------

My company manufactures a line of data acquisition, data
collection, and message switching devices, intended for sale to
large manufacturers. These devices pre-process and re-direct
business data that aid in the control of the manufacturing and
business processes of the user. Because these users have
different requirements for the processing of this data, I chose
to make the devices programmable. Since the intended users
have employees that are familiar with the COBOL language, I
chose to implement a COBOL Virtual Machine to allow these
users to program the devices in a language with which they are
familiar. For all implemented COBOL features, the implementation
conforms to the requirements of the ANSI/ISO COBOL standard.

The devices are based on embedded PowerPCs which have
no floating-point coprocessor and no decimal arithmetic
instructions. There are no mass storage devices, no terminal
devices, and no printer devices.

Furthermore, as part of my marketing plan, I need to be able
to tell prospective users that my language implementation is
ANSI/ISO conforming.

----- End of hypothesis ------------------

Given the above hypothetical situation:

Why should I be required to implement PACKED-DECIMAL,
screen section, report writer, OPEN I-O, DELETE,
BEFORE/AFTER ADVANCING, etc.?

Why should I not be able to claim that my COBOL implementation
is ANSI/ISO conforming without these features?

Should I be required to process business data with a "conforming",
free standing C language or "conforming", embedded Java
implementation because it can not be "conforming" COBOL without
terminals, mass storage, printers, etc.?

The one thing missing from this discussion is that a standard
should never compel an implementor to do the impossible or
impractical; but, it must require that whatever is implemented
conform to the standard. I think the manufacturing representatives
to the COBOL Standard committees recognize this. Most users
tend not to recognize this because they do not work at the margin
of the implementation of the langauge; that is, at the point where
implementing some features becomes impossible or impractical.

[...]
>If something must be optional, let it be the OO features.

No disagreement here! :-)
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<k3ny2.4$j05.24@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com>`

```

Rick Smith wrote in message ...
>
[...]
>Numeric coprocessors on PCs have nothing to do with decimal
>arithmetic. The coprocessor is for floating-point. The x86 micro-
>processor instruction set has instructions for decimal arithmetic. It is
>these instructions that allow for implementation of packed-decimal.
>
With apologies, the coprocessor did have some capabilities
for loading and storing packed decimal numbers.

Even without the coprocessor the standard decimal instructions
were still sufficient to implement decimal arithmetic.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36ca11e9@news3.us.ibm.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com>`

```
Rick Smith wrote in message ...
>Leif Svalgaard wrote in message <36c9685b@news3.us.ibm.net>...
>>I agree 100% with Bill on all of his points. Some (e.g. Don Nelson) have
argued
>>that one cannot force the vendor to implement stuff not supported by his
hardware
>>or file system, and that, therefore, in/exclusion of "processor-dependent"
features
>>are necessary. This argument IMHO is weak. Consider the case of the PC.
>>Early PCs didn't have numeric co-processors, yet all COBOL vendors support
…[6 more quoted lines elided]…
>these instructions that allow for implementation of packed-decimal.

actually not. They allow for implementation of DECIMAL arithmetic
(usage DISPLAY).
>
>PCs have a concept of "mass storage" and a "mass storage
…[5 more quoted lines elided]…
>mainframes!"

yes, but Don's point was if the native file system did not support
ISAM directly, the Cobol vendor should not have to do it either.

>
>----- Hypothetical situation -------------
…[29 more quoted lines elided]…
>BEFORE/AFTER ADVANCING, etc.?


I actually agree with you. Personally, I do all my Cobol programming
in a very small subset of Cobol (only 6 verbs).

>
>Why should I not be able to claim that my COBOL implementation
>is ANSI/ISO conforming without these features?
>

well, here we disagree. If you don't fully support the standard, you
should not claim conformance.

But there is nothing wrong with being restricted to a small subset.
What I hate is the classical 'extended subset'  that locks you in
(IBM and M$ are experts at this).

I guess my bottom line was that in today's world it is not hard to be
fully conforming. Compiler, file system, database, etc technology
is well known and tested. There is nothing that is 'impossible'
anymore. Most of the restrictions of old were real hard, being
dictated by feeble hardware.

I don't want to hear a vendor tell me that "he can't do it".
Now, I would accept that "he won't do it". I just go somewhere
else. (In some environments - e.g. AS/400 - this may not be
possible, but then I would dump that environment and go Unix).
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<1Rty2.6$j05.65@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net>`

```

Leif Svalgaard wrote in message <36ca11e9@news3.us.ibm.net>...
>Rick Smith wrote in message ...
[...]
>>PCs have a concept of "mass storage" and a "mass storage
>>device" (in the form of a disk drive). This is sufficient to allow for
…[7 more quoted lines elided]…
>ISAM directly, the Cobol vendor should not have to do it either.


Don Nelson said: "Of course you left out where the operating
system does not support the feature."

I think you may have taken his comment "too" literally. Consider
the Screen Section and Report Writer. No operating system
(that I know of) provides direct support for either of these features.
(Some operating systems provide direct support for indexed files.)

In my interpretation of Don's comment, an operating system
provides support for Screen Section and Report Writer if it has a
means for accessing "character addressable" terminals and
printers with some means for positioning the output. Obviously,
the implementor would be required to provide the necessary
requests to the operating system to implement these COBOL
features.

What I was saying about PCs is that the operating system
provides support (in my intrepretation of Don's comment) for
indexed files because it is possible for the implementor to
access "mass storage files." It is still the responsibility of the
implementor to provide the necessary requests to the operating
system to implement the ISAM feature.

A case where a PC operating system provided no support
for a proposed COBOL feature is MS-DOS 2.0 which had
no operating system requests for file sharing or record
locking. In that case, it would not be possible to implement
that feature.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7aei9s$pd3$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com>`

```
Now we are getting silly.  A single stream system will not
have file locking, nor will a system with no screens
support the screen section.  So what?  If I run Cobol on a
system with no printer, the reports will not work.  If I run it
on a system with no tape drive, then the tape files will not
write on tape.  Is the standards committee trying to say
that Cobol will only be standard if every computer has
every device?

Standard means a standard way of using common devices.
It does not mean that every system is the same.  *IF* there
are character mode screens, the same Cobol should display
the same data.

As far as I am concerned, a compiler should be certified if
it runs a specific validation suite, period.  Any specification
which cannot be tested is just so much hot air.

Rick Smith wrote in message <1Rty2.6$j05.65@news19.ispnews.com>...
>
>Leif Svalgaard wrote in message <36ca11e9@news3.us.ibm.net>...
…[46 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7aeop9$4h0@dfw-ixnews3.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net>`

```


Donald Tees wrote in message <7aei9s$pd3$1@news.igs.net>...

   <much snippage>
>
>As far as I am concerned, a compiler should be certified if
>it runs a specific validation suite, period.  Any specification
>which cannot be tested is just so much hot air.
>


Then we (COBOL) are out of luck completely.  The US government has NO
certification suite that they are actively using for COBOL (they never
updated the one they have for the last Amendment to the Standard) and they
have given every indication that they have no intention of ever creating any
future certification/validation suite - much less requiring it.

No other group or country has stepped up to create or administer a
replacement.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7af125$806$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com>`

```
Then perhaps we are out of luck.  Tell me, would you design
or code a Cobol program that had absolutely no way that it
could be tested beyond reading the code?

I would be a lot more impressed with even a primitive test
for standardization than with a document that leaves all the
differences up in the air.

William M. Klein wrote in message <7aeop9$4h0@dfw-ixnews3.ix.netcom.com>...
>
>
…[13 more quoted lines elided]…
>have given every indication that they have no intention of ever creating
any
>future certification/validation suite - much less requiring it.
>
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CB1460.213B775D@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net>`

```
OO is designed to allow tested components to be integrated into a
system.   That's all find and good, but generally I find TESTING to be a
bigger chore than writing.  And just because a component has been tested
and debugged doesn't mean I will trust my application without testing
it.

And what happens when I have to change that object?  I have to re-test
every thing which uses that object.

So to get my job done, I make a copy of that object, make its
modifications, and don't let the other programs use the old object. 
That's not reuseability anymore than what I do now with COBOL.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afcq2$86i@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <36CB1460.213B775D@NOSPAMhome.com>`

```

Look into what a code repository is, and how it actually operates.
There are ways to handle this. 

You are actually being just a bit - um - paranoid here. Do you 
retest your compiler every time you use it on a different 
program? It is not beyond conception that other software components,
besides compilers, can be just as reliable...

-Paul


Howard Brazee (brazee@NOSPAMhome.com) wrote:
: OO is designed to allow tested components to be integrated into a
: system.   That's all find and good, but generally I find TESTING to be a
: bigger chore than writing.  And just because a component has been tested
: and debugged doesn't mean I will trust my application without testing
: it.

: And what happens when I have to change that object?  I have to re-test
: every thing which uses that object.

: So to get my job done, I make a copy of that object, make its
: modifications, and don't let the other programs use the old object. 
: That's not reuseability anymore than what I do now with COBOL.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CB3C54.264F3B87@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <36CB1460.213B775D@NOSPAMhome.com> <7afcq2$86i@lotho.delphi.com>`

```
I retest every application after I change a component of it.

paulr wrote:
> 
> Look into what a code repository is, and how it actually operates.
…[21 more quoted lines elided]…
> : That's not reuseability anymore than what I do now with COBOL.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 8)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afcm8$86i@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net>`

```

<GRIN> I think you are talking past each other a bit here. 
Believe me what I tell you that a validation suite can be
a hellish thing for a compiler to pass. And it should
be...

But it has NOTHING to do with validating that a program written
with the compiler is correct. 

-Paul
.


Donald Tees (donald@willmack.com) wrote:
: Then perhaps we are out of luck.  Tell me, would you design
: or code a Cobol program that had absolutely no way that it
: could be tested beyond reading the code?

: I would be a lot more impressed with even a primitive test
: for standardization than with a document that leaves all the
: differences up in the air.

: William M. Klein wrote in message <7aeop9$4h0@dfw-ixnews3.ix.netcom.com>...
: >
: >
: >Donald Tees wrote in message <7aei9s$pd3$1@news.igs.net>...
: >
: >   <much snippage>
: >>
: >>As far as I am concerned, a compiler should be certified if
: >>it runs a specific validation suite, period.  Any specification
: >>which cannot be tested is just so much hot air.
: >>
: >
: >
: >Then we (COBOL) are out of luck completely.  The US government has NO
: >certification suite that they are actively using for COBOL (they never
: >updated the one they have for the last Amendment to the Standard) and they
: >have given every indication that they have no intention of ever creating
: any
: >future certification/validation suite - much less requiring it.
: >
: >No other group or country has stepped up to create or administer a
: >replacement.
: >
: >--
: >Bill Klein (wmklein at ix dot netcom dot com)
: >
: >
: >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afrkf$4h7$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <7afcm8$86i@lotho.delphi.com>`

```
Of course not.  It has to do with the definition of "standard".
It makes it nice and easy ... just as a comprehensive set
of test datum makes testing a program easy.

paulr wrote in message <7afcm8$86i@lotho.delphi.com>...
>
><GRIN> I think you are talking past each other a bit here.
…[20 more quoted lines elided]…
>: William M. Klein wrote in message
<7aeop9$4h0@dfw-ixnews3.ix.netcom.com>...
>: >
>: >
…[12 more quoted lines elided]…
>: >updated the one they have for the last Amendment to the Standard) and
they
>: >have given every indication that they have no intention of ever creating
>: any
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<o3qA2.15017$OS5.14970923@news3.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <7afcm8$86i@lotho.delphi.com> <7afrkf$4h7$1@news.igs.net>`

```
Its is not the Government's place to validate the Compiler.
That is done by ANSII/CODASYL.  In order to be called 'COBOL'
the vendor must submit proof that the compiler meets the specifications
oulined by the committee.

Donald Tees wrote in message <7afrkf$4h7$1@news.igs.net>...
>Of course not.  It has to do with the definition of "standard".
>It makes it nice and easy ... just as a comprehensive set
…[43 more quoted lines elided]…
>>: >have given every indication that they have no intention of ever
creating
>>: any
>>: >future certification/validation suite - much less requiring it.
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7ati18$n77@dfw-ixnews8.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <7afcm8$86i@lotho.delphi.com> <7afrkf$4h7$1@news.igs.net> <o3qA2.15017$OS5.14970923@news3.mia>`

```
Neither CODASYL nor ANSI *ever* did COBOL validations.  The validations were
done (in the US) by NIST.  NIST has now stopped even offering this service.
Today, there is no way to get an outside "recognized" entity to run a set of
validation programs to confirm if a compiler is or is not conforming to the
'85 Standard (with or without amendments).
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36D2EE1A.7B76@compaq.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <7afcm8$86i@lotho.delphi.com> <7afrkf$4h7$1@news.igs.net> <o3qA2.15017$OS5.14970923@news3.mia>`

```
James King wrote:
> 
> Its is not the Government's place to validate the Compiler.
…[3 more quoted lines elided]…
> 
Sorry, you are quite wrong.  The government specified in RFPs 
(requests for proposals) that to be acceptable for purchase by the 
government the compiler (COBOL, FORTRAN, Ada, and C (I think)) must be 
validated by NIST (it started with the Air Force for the '74 standard 
and eventually would up with NIST).  Since the government is about the 
biggest purchaser of computer stuff, everyone ran the tests. What also 
happened, was that private sector companies realized the value of this 
and specified the same requirement in their proposals.  However, the 
feds were not doing the validation for them, only for the feds 
themselves.  Since they had the requirement it was indeed their job to 
provide the tests so people could meet the requirements.

This has nothing to do with ANSI or CODASYL.  Actually, neither group 
has anything to do with COBOL standards any more.  CODASYL is gone 
(the CODASYL COBOL Committee was merged into the ANSI COBOL Committee, 
which ended my tenure as chairman) and the ANSI efforts for compilers 
and such has become NCITS (National Committee for Information 
Technology Standardization).
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7b4mv9$msf$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <7afcm8$86i@lotho.delphi.com> <7afrkf$4h7$1@news.igs.net> <o3qA2.15017$OS5.14970923@news3.mia>`

```
Actually, I have never mentioned the government.  What I said
was that if we are going to have a standard, a validation test
makes a lot more sense than a specification written in human
language.

A standard with no way to test for it makes little sense to me. It
is a bit like writing a program knowing in advance that you cannot
test it, or ensure it works in any way.


James King wrote in message ...
>Its is not the Government's place to validate the Compiler.
>That is done by ANSII/CODASYL.  In order to be called 'COBOL'
…[67 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 12)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-25T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7b4pdl$lsi@dfw-ixnews7.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <7afcm8$86i@lotho.delphi.com> <7afrkf$4h7$1@news.igs.net> <o3qA2.15017$OS5.14970923@news3.mia> <7b4mv9$msf$1@news.igs.net>`

```
And the reality is that there will be NO validation suite for the next
Standard - or at least none is planned by anyone anywhere that I know of
(and certainly not by any organization that has provided them in the past).
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** Don Nelson <don.nelson@compaq.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CC5B29.13A7@compaq.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <7aeop9$4h0@dfw-ixnews3.ix.netcom.com> <7af125$806$1@news.igs.net> <7afcm8$86i@lotho.delphi.com>`

```
paulr wrote:
> 
> <GRIN> I think you are talking past each other a bit here.
…[6 more quoted lines elided]…
> 

Actually, it is not all that hard.  I've been through the process lots 
and lots of times.  I think there are around 700 tests in the suite.  
The most amazing one was back in 1975 or thereabouts when we (CDC) had 
to pass the 1974 validation tests right away and our '74 compiler was 
not done yet.  I took what we had and made it pass the tests.  It 
wouldn't compile and run hardly any other programs, but it did the 
validataion tests.  What this means is that a program compiled with it 
would probably not execute correctly.  A few months later we finished 
the real compiler and all was OK.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3KCy2.3$zb1.39@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net>`

```

Donald Tees wrote in message <7aei9s$pd3$1@news.igs.net>...
>Now we are getting silly.

Perhaps! ;-)

>  A single stream system will not
>have file locking, nor will a system with no screens
…[3 more quoted lines elided]…
>write on tape.

Actually, you would not be able to run the program since
it would not make it past the syntax checking; hence,
no executable program would be created.

>  Is the standards committee trying to say
>that Cobol will only be standard if every computer has
>every device?

No, the committee recognizes that all processors may not
be capable of doing everthing described in the standard.
These items are defined in the "processor dependent" list.
For these processor dependent items, an implementor may
choose to claim support. If the implementor chooses to
claim support, then the feature must be implemented as
described in the standard. Furthermore, even if the processor
has the capability to implement the processor dependent
feature, the implementor may choose to not claim support
for other reasons.

It is this last point that is the primary source of disagreement.

One clear example is packed decimal.

The processor dependent list [CD 1.2] says:

"6) The USAGE PACKED-DECIMAL clause is dependent
      upon the availability of a suitable computer architecture for
      the packed decimal data format."

If I am implementing COBOL on a processor that has integer
instructions but no native decimal instructions or data types,
I may choose to not claim support because the architecture is
not suitable. On the other hand, if the processor has multiply,
divide, and shift instructions, implementation of packed
decimal is possible, though far less efficient than BINARY.

The committee says that whether to implement packed
decimal is my choice. Those who are opposed to the
committee's position insist that, since it is possible to
implement the packed decimal data format, I should be
required to do so. The reason being that having packed
decimal available increases the portability of programs.

I support the committee's position.

It is problematic as to whether not claiming support for a
feature means that an implementor need not recognize the
syntax of that feature.

If Screen Section cannot be implemented, should the
implementor recognize the syntax and report the exceptions
as warnings or errors?

The committee's position seems to be that the syntax need
not be recognized. Those opposed to the committee's
position seem to be of the opinion that the syntax must be
recognized.

Again, I support the committee's position, though I would
prefer an error message stating that Screen Section is not
supported and skip to the next section without providing
additional error messages for the individual Screen Section
items.

>Standard means a standard way of using common devices.
>It does not mean that every system is the same.  *IF* there
>are character mode screens, the same Cobol should display
>the same data.

Except that not all screens are the same size or provide for
color; hence, the data may not display correctly or in the same
way.

>As far as I am concerned, a compiler should be certified if
>it runs a specific validation suite, period.  Any specification
>which cannot be tested is just so much hot air.

There must be multiple validations; one to validate the
non-processor dependent features and one for each of the
features that are processor dependent.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 7)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CB04A8.ADF65822@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com>`

```
Rick Smith wrote:

> >  A single stream system will not
> >have file locking, nor will a system with no screens
…[7 more quoted lines elided]…
> no executable program would be created.

I can create an executable of a program requiring a tape drive on a
system without a tape drive.  Of course it won't run.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afc9v$e8p@dfw-ixnews8.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com>`

```
First, as Don Nelson indicated, there is a conflict between the definition
of the compiler dependent list and the actual items in the list.  As of the
current time, I believe (but until the committee resolves this conflict it
is not certain) that you are missing the "implementor discretionary" part of
the actual conformance rules.

The reason that the definition was put in (in my opinion - and others will
certainly disagree) is that there are some implementors who DO HAVE THE FULL
CAPABILITY of having character screen support but want to avoid implementing
the new ACCEPT/DISPLAY facility  - just because they don't want to support
it. (There are also some who have the capability of supporting file sharing
and record locking as it is being revised in the draft Standard - but don't
want to support that either - but the original issue was screen section
support)

You have quoted one part of the Packed-Decimal definition.  However, as the
Standard currently is written in the CONFORMANCE rules, if an implementation
wanted to support COMP-3 as packed-decimal and NOT support USAGE
PACKED-DECIMAL, they would be fully conforming.  Furthermore,  if they did
not want to support either one but wanted you to use an API call or a call
to a C subroutine, they would be fully conforming.

It is THIS that I am disagreeing with.

As I say, many of us could disagree on which part of the draft Standard
"rules" - but until the committee resolves this difference, I don't think
there is any way for either of us to "win".  Please see J4 document 99-0096
via the J4 home page of

 http://people.ne.mediaone.net/doncobol/index.html

if you think this is a non-issue.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7dEz2.5$O_4.142@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com>`

```

William M. Klein wrote in message <7afc9v$e8p@dfw-ixnews8.ix.netcom.com>...
>First, as Don Nelson indicated, there is a conflict between the definition
>of the compiler dependent list and the actual items in the list.  As of the
>current time, I believe (but until the committee resolves this conflict it
>is not certain) that you are missing the "implementor discretionary" part
of
>the actual conformance rules.
>
>The reason that the definition was put in (in my opinion - and others will
>certainly disagree) is that there are some implementors who DO HAVE THE
FULL
>CAPABILITY of having character screen support but want to avoid
implementing
>the new ACCEPT/DISPLAY facility  - just because they don't want to support
>it. (There are also some who have the capability of supporting file sharing
…[3 more quoted lines elided]…
>
I wonder if it is possible to create a category, "Implementor Defined
Subset," to cover those situations where the implementation of a
feature is possible but the implementor desires not to implement that
feature. Such an implementation would necessarily carry a "Subset
COBOL" label and must identify the features of the language they
chose not to implement. This change would require a distinction
between that which is technologicaly feasable for the processor and
that which is not.

One problem is how to define "Subset" in such a way as to distinguish
it from non-conformance. For example, not supporting screen handling
could be a subset. Providing substantialy identical capabilities within
the implementation, in lieu of the standard screen handling feature,
could be non-conformance. Another could be that support for BEFORE
/ AFTER POSITIONING; but not supporting REPORT WRITER would
be non-conformance.

Another problem is, that with a definition of "Subset," could / should
other options be introduced; such as, not including object-orientation.
If the implementor chooses not to support OO, that is a subset.

Finally, I think going back to the older Module definition would be
undesireable.

In conclusion, having a "Subset COBOL" definition would allow
implementors to provide application-specific COBOL environments
without fragmenting the COBOL Standard. This is because every
subset implementation must carry the "Subset COBOL" label and must
identify those portions of the standard which were chosen for exclusion.
The implementor would be, relatively free, to choose those portions of
the standard which make the most sense for their intended market.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7an7ss$i92@dfw-ixnews9.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com> <7dEz2.5$O_4.142@news19.ispnews.com>`

```
Rick Smith wrote in message <7dEz2.5$O_4.142@news19.ispnews.com>...
>
  <much snippage>
>>
>I wonder if it is possible to create a category, "Implementor Defined
>Subset," to cover those situations where the implementation of a
>feature is possible but the implementor desires not to implement that
>feature.
 <more snippage>

What I would like to see (and have included in a paper to J4) is:

1) The "processor-dependent" list is returned to hardware/software dependent
items (such as IF you don't have a printer, you can't do AFTER/BEFORE
ADVANCING; if you don't have a mass-storage device, you can't do OPEN I-O)

2) Items that are up to the "discretion" of the vendor are (returned) to the
"OPTIONAL" list (which is where they always were before).  This might
include enhanced ACCEPT/DISPLAY and even file sharing/record locking.

  ***

Personally, I think that the optional items should as limited as possible
(as I think this is a PRIME reason that people don't know/use report-writer
today, i.e. that it is "optional" in the current Standard).  I really
question that any NEW feature should be added to the "optional" list - but
at least if it were in the optional list, then it would be clear that this
is what it is.

FYI,
  I believe that the current draft includes one and only one optional item -
and that is the Communications Section/Facility - which is also designated
as OBSOLETE.

FYI(2),
  The 'Implementor defined" list is still in the draft (and has grown
SUBSTANTIALLY since the '85 Standard).  The major change in this area is
that each item is distinguished between those items that MUST be documented
and those that need not be documented as to how they are implemented.  (I
haven't checked recently, but I think there may even be some items in this
already - that need not be implemented at all.)
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36cf2be8.269353236@news1.ibm.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com> <7dEz2.5$O_4.142@news19.ispnews.com> <7an7ss$i92@dfw-ixnews9.ix.netcom.com>`

```
On Sat, 20 Feb 1999 12:59:38 -0800, "William M. Klein"
<wmklein@inospam.netcom.com> wrote:


>Personally, I think that the optional items should as limited as possible
>(as I think this is a PRIME reason that people don't know/use report-writer
…[4 more quoted lines elided]…
>

Bill, 

Just to confirm.... I don't use report writer for jus this reason.  I
find myself constantly rehosting COBOL source programs.  I have moved
programs from the mainframe to the PC, or from the VMS system to the
mainframe, or from a Wang to VMS.  When moving back to the mainframe -
we don't have report writer (or didn't - I honestly have not check to
see of Cobol for this and that has it or noe).  I don't have it in my
CA-Realia compiler that I use for PC development -- but I do have it
in with my Fujitsu compiler - where I am moving.  HOWEVER - on the PC,
writing to the "text printer" is rapidly becoming obsolete.  Line
printing on the PC is not as simple (thanks to Mr Bill - I have no
tattoo - Gates) as it used to be.  So I'm not sure I'll every use it.
I USED to use it in a MicroFocus shop - till I got bit trying to move
a program to the mainframe and had to yank it all out.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-20T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7anh1g$59l@sjx-ixn10.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com> <7dEz2.5$O_4.142@news19.ispnews.com> <7an7ss$i92@dfw-ixnews9.ix.netcom.com> <36cf2be8.269353236@news1.ibm.net>`

```
Just for the information of anyone who is interested.

There is an add-on product that supports Report-Writer (both ANSI syntax -
and "traditional" OS/VS COBOL variations) on:

    - IBM Mainframes (COBOL for this-and-that, COBOL/VSE, and VS COBOL II)
    -  CA-Realia
    - Micro Focus
    -  Several other platforms and compilers.

If you are interested, contact John Piggott who is an occasional "visitor"
in comp.lang.cobol (and whose ID should be available from DejaNews).

If you are interested in this support on IBM mainframes - then you can get
this add-on directly from IBM - or from SPC Systems.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** John Piggott <John_Piggott@compuserve.com>
- **Date:** 1999-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36D21A9E.435C@compuserve.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com> <7dEz2.5$O_4.142@news19.ispnews.com> <7an7ss$i92@dfw-ixnews9.ix.netcom.com> <36cf2be8.269353236@news1.ibm.net>`

```
With IBM COBOL, Report Writer is a separate program product (5798-DYR) 
but once you've installed it, the compiler "magically" starts compiling 
Report Writer sources. (Actually a "precompiler" gets called by the 
compiler but it's so well hidden you hardly notice it.) IBM have had it 
ever since OS/VS COBOL and DOS/VS COBOL were superseded.

For CA-Realia COBOL, you get the same thing from Norcom for a song.


Thane Hubbell wrote:
> 
> On Sat, 20 Feb 1999 12:59:38 -0800, "William M. Klein"
…[24 more quoted lines elided]…
> a program to the mainframe and had to yank it all out.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 12)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-Q3SS3YickvDn@Dwight_Miller.iix.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com> <7dEz2.5$O_4.142@news19.ispnews.com> <7an7ss$i92@dfw-ixnews9.ix.netcom.com> <36cf2be8.269353236@news1.ibm.net> <36D21A9E.435C@compuserve.com>`

```
On Tue, 23 Feb 1999 03:03:58, John Piggott 
<John_Piggott@compuserve.com> wrote:

> With IBM COBOL, Report Writer is a separate program product (5798-DYR) 
> but once you've installed it, the compiler "magically" starts compiling 
…[5 more quoted lines elided]…
>

Very interesting.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36D16AEF.1B616B74@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com> <7dEz2.5$O_4.142@news19.ispnews.com>`

```
> One problem is how to define "Subset" in such a way as to distinguish
> it from non-conformance. For example, not supporting screen handling
…[4 more quoted lines elided]…
> be non-conformance.

Two companies could develop separate ways of handling a new need.  ANSI
then comes up with its way of handling this need.  The two companies
would need to support both their old ways (for a while), and the ANSI
way - possibly with some extensions if ANSI doesn't do everything they
handled.

To me "subset" means any additional functions not covered by ANSI. 
Non-conformance is failure to include everything covered by ANSI.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<p4iA2.4$Ws.16@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afc9v$e8p@dfw-ixnews8.ix.netcom.com> <7dEz2.5$O_4.142@news19.ispnews.com> <36D16AEF.1B616B74@NOSPAMhome.com>`

```

Howard Brazee wrote in message <36D16AEF.1B616B74@NOSPAMhome.com>...
>> One problem is how to define "Subset" in such a way as to distinguish
>> it from non-conformance. For example, not supporting screen handling
…[12 more quoted lines elided]…
>To me "subset" means any additional functions not covered by ANSI.

Additional functions are extensions. From CD 1.2:

"3.1.8 Nonstandard extensions

        An implementation may include language elements or functionality
        not defined in standard COBOL. That implementation meets the
        requirements of standard COBOL even though additional reserved
        words may be introduced by the implementor, thereby preventing
        translation of some compilation groups that meet the requirements
        of standard COBOL. ..."

The term "subset" has a mathematical meaning that is almost; but not
exactly, the opposite of additional functions (elements).
[Paraphased from Douglas Adams.]

To express this in elementary set theory, with which I have limited
exposure. Given the following:

    A is the set of language elements of the standard
    B is the set of language elements of the implementation
    C is the intersection of B with A (the elements of B that also exist in
A)
    D is the set of elements of B that do not exist in A (The complement of
        the intersection of B with A?)

If C does not equal A, then B contains a subset of A, or the implementation
of the language is a subset of the standard. Also, if D is not an empty set,
then D contains the implementors extensions to the language.

>Non-conformance is failure to include everything covered by ANSI.

The language standard "covers" some elements where exclusion is
permitted. An implementation which excludes those "covered"
elements may still conform.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 7)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afd1t$ovg$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com>`

```
Rick Smith wrote in message <3KCy2.3$zb1.39@news19.ispnews.com>...
>
>Actually, you would not be able to run the program since
>it would not make it past the syntax checking; hence,
>no executable program would be created.


Quite to the contrary.  If I write a Cobol programs that requires
printout, it will compile quite nicely on a system without a printer.
It will then give a runtime error when I try to print.  I have dozens
of programs that will only run on PC's that are configured with
the appropriate devices.

I know of *no* OS's that cannot support anything in the Cobol
standard, implimentor approval or not.  Show me a single computer,
for example, that does not have a screen that will display characters.
Sure, there are mainframes that have screens connected to
channel controlers, hence systems like CICS.  However, the fact
remains that a screen handling section *could* be written.  IBM
just does not want to.
>
>>  Is the standards committee trying to say
…[12 more quoted lines elided]…
>for other reasons.

Read Turing regarding what computers can and cannot do. I will
grant that usage's other than display are there for purposes of
CPU design.  However, if I do want to write STANDARD code,
there is absolutely no reason that I have to use them.  They are
there, primarily, to increase efficiency on specific machines. In
my opinion, *all* formats excepting display should be removed
from the standard.  A feature designed to speed execution on a
specific CPU has no place in a "standard".

>
>It is this last point that is the primary source of disagreement.
…[7 more quoted lines elided]…
>      the packed decimal data format."


as above

>If I am implementing COBOL on a processor that has integer
>instructions but no native decimal instructions or data types,
…[3 more quoted lines elided]…
>decimal is possible, though far less efficient than BINARY.

>The committee says that whether to implement packed
>decimal is my choice. Those who are opposed to the
…[28 more quoted lines elided]…
>way.

It does not take a rocket scientist to discover that a 130 by 50
line display will not fit on a 40 by 12 line screen.  I could have written
a screen driver, though, that did not crash, when I was a student
thirty years ago.

>
>>As far as I am concerned, a compiler should be certified if
…[5 more quoted lines elided]…
>features that are processor dependent.


Anything that is processor dependent is not "standard".  It
should just be left out.  That is half the problem.  We are still
trying to make a modern compiler adhere to a "standard" that
was not "standard" in the first place.  It had a thousand exceptions
to accommodate specific computers.  19 years later, we are
redesigning it and insisting that we make the same mistakes all
over again.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<MqIy2.3$at3.30@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net>`

```

Donald Tees wrote in message <7afd1t$ovg$1@news.igs.net>...
>Rick Smith wrote in message <3KCy2.3$zb1.39@news19.ispnews.com>...
>>
…[17 more quoted lines elided]…
>just does not want to.

Whoa! A few posts ago (I thought) we were discussing a COBOL
implementation for a device that has no concept of screens or
printers. My comments pertain to that system and the implementaion
for that system. Your comments pertain to general purpose computer
systems.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afm3m$pvc@dfw-ixnews6.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com>`

```
Rick Smith wrote in message ...
>
>Donald Tees wrote in message <7afd1t$ovg$1@news.igs.net>...
…[30 more quoted lines elided]…
>

Rick,
  No one (or certainly no one that I know) is arguing that a vendor must
support (run-time) a feature that is NOT supported by the hardware/software
in their environment.  The two issues that I have problems with are:

1) The fact that the current definition of the full processor-dependent list
lets an implementor NOT include run-time support for features that ARE
available in their environment.  (For example, they do have character mode
screens - but they don't WANT to support the new Accept/Display syntax)

2) The question of whether implementors should provide syntax support for
features that are not supported by their hardware/software environment.  For
example, if the environment doesn't have the "outside" support for file
sharing and record locking should they

    A) accept the syntax, but at run time give a "bad" file status code
    B) reject the syntax at compile-time - even though it is "accepted" by
other Standard conforming compilers without any "extension" flagging.

***

There is the related issue of WHAT lengths a vendor needs to go to provide
support for a feature.  For example, if the operating system doesn't include
any "native" packed-decimal support, must the vendor provide software
support for it?  How about file sharing/record locking?  What about OPEN
EXTEND? Indexed file systems? ASCII files?  In previous Standards, by and
large, the Standard has required the vendor to provide "software" support
for features that make sense in their environment - even if the "native"
support isn't there.  In this new definition of "processor-dependent" this
is EXPLICITLY not required.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<eDYy2.3$p.58@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afm3m$pvc@dfw-ixnews6.ix.netcom.com>`

```

William M. Klein wrote in message <7afm3m$pvc@dfw-ixnews6.ix.netcom.com>...
>
>Rick,
…[4 more quoted lines elided]…
>1) The fact that the current definition of the full processor-dependent
list
>lets an implementor NOT include run-time support for features that ARE
>available in their environment.  (For example, they do have character mode
>screens - but they don't WANT to support the new Accept/Display syntax)

I see no reason why they should. When a language specifies how
peripheral devices or operating system compenents must interact
with the language, this is equivalent to imposing design constraints
on the hardware vendor or operating system vendor. Whether to
support those features of the language MUST be the decision of
the hardware or operating system vendor. A hardware vendor
must be willing to supply devices that satisfy the requirements of
the language. An operating system vendor must be willing to
provide the necessary means to allow the executable program
from the language to interact with that device. Furthermore, an
implementor must be willing to supply the means for translating
the language source into an executable for that operating system.
This last item is generally a non-issue since implementors are
willing participants in the language standardization.

On June 22, 1998, I started a thread in <news:comp.lang.c> titled
"Should the C Programming Language be Amended to Provide
for a Standard Console?" I reasoned that since the COBOL Language
could support such a definition; a similar definition could be added
to the C Language. During the following week there were more than
100 posts and a few private e-mails. The vast majority of the
respondents, who offered reasoned arguments, argued that support
for character based (or any) terminal(s) or peripherals was within the
pervue of the operating system vendor and should not be defined in
any programming language. Their argument was quite compelling.

However, I did not fully accept their conclusions. I believe that it is
reasonable for a language to provide such a definition as long as
its implementation is at the discretion of the operating system
vendor.

>2) The question of whether implementors should provide syntax support for
>features that are not supported by their hardware/software environment.
For
>example, if the environment doesn't have the "outside" support for file
>sharing and record locking should they
…[3 more quoted lines elided]…
>other Standard conforming compilers without any "extension" flagging.

If the implementation can determine, at the time the program is tanslated,
that the program will not run, then reject the syntax during translation.
The error message should state that the feature required by the syntax
is not supported. The implementor should also provide a
"recommendation," where possible, for how to accomplish what was
intended.

Otherwise, at run time, the implementation should provide, where possible,
an appropriate exception, perhaps, EC-FEATURE-NOT-AVAILABLE.

>There is the related issue of WHAT lengths a vendor needs to go to provide
>support for a feature.  For example, if the operating system doesn't
include
>any "native" packed-decimal support, must the vendor provide software
>support for it?  How about file sharing/record locking?  What about OPEN
…[4 more quoted lines elided]…
>is EXPLICITLY not required.

IMO, I think the standard has been "over-specified." The inclusion of
BINARY and PACKED-DECIMAL was a mistake. Adding the
BINARY-xxx is also a mistake. If the intent of BINARY-LONG is to
allow a COBOL program to communicate with the operating system
or a program in another language, then call it LONG-INTEGER,
specify its intention, and its minimum range; then allow the
implementor to decide how best to provide the support.

The others require the cooperation of the operating system vendor.
Keep them in the standard, keep them processor dependent, and be
thankful for what is provided.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CC5848.4AA24F44@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afm3m$pvc@dfw-ixnews6.ix.netcom.com> <eDYy2.3$p.58@news19.ispnews.com>`

```
> On June 22, 1998, I started a thread in <news:comp.lang.c> titled
> "Should the C Programming Language be Amended to Provide
…[12 more quoted lines elided]…
> vendor.

What's interesting to watch is the development of Java, comparing it to
both COBOL and C.  It's history started off as an embedded systems
language, and it could talk to databases before it could print
effectively.  One way it has expanded was to require a common
environment wherever it runs.  Microsoft keeps trying to "improve" Java,
to make it run better on Windows at the expense of its portability.

So far, the public has been less willing to accept proprietary
"improvements" for Java than we were for COBOL when Big Blue dictated
terms to many.

We should watch Java carefully as we make decisions about Cobol.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 12)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-02-19T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CD5A00.313D4BB5@zip.com.au>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afm3m$pvc@dfw-ixnews6.ix.netcom.com> <eDYy2.3$p.58@news19.ispnews.com> <36CC5848.4AA24F44@NOSPAMhome.com>`

```
Howard Brazee wrote:
> 
..snip....
> 
> both COBOL and C.  It's history started off as an embedded systems
…[9 more quoted lines elided]…
> We should watch Java carefully as we make decisions about Cobol.

There are two types of standards defacto standards (which is how COMP-3
started) and committee standards.   According to 'standards science' the
optimal time to develop a standard is in the trough between when
researchers tinker and business really takes hold of a solution
spreading to many ways to bring it in.  Cobol unfortunately has missed
the prime opportunity time and the arguments are destined.

Java byte code is a great platform and I see one cobol compiler vendor
is using this platform to their advantage (Anyone remember the UCSD
P-system talk about everything old is new again).  Remember that many
people want to write code that can display without modification on any
computer systems.  The objective of a totally portable common code
language in today's market is to write a program once (with drop down
lists, etc) and being able to compile it on windows, X-Windows, (maybe)
text based, and CGI server without any changes to code (or at least only
minor changes).

In my opinion without this ability cobol (or any language) will die
except for some die hards for restricted distribution systems.  Linux
WILL become a force to be reckoned with in the next few years (it's use
is tripling every year) and it is very cheap so hardware vendor will be
keen to support it once it reaches critical mass.  If your favourite
cobol compiler cannot support X-windows and Windows automatically you
are shooting at a restricted market.

I write my code to be portable, this ensures that my company is not
restricted to IBM compilers or hardware, this gives my company leverage
when talking to the representatives.  The IBM reps (and everyone else
especially multiplatform compiler vendors) want to lock you into their
version of reality.  If we do not fight this and demand portability then
ultimately everyone loses.  You will not be able to test compiler A, B
and C for performance and choose the best because the cost of the
rewrite is to high.  You will not be able to pick a cheap compiler to
develop on at home knowing that it will work at work in the same way.

The flip side of this is the extensions, if it is a great idea then
other vendors will clone it.  If it is a bad idea (or of limited appeal)
it will wither on the vine.  Once most vendors support an option it
should be part of the standard and required but HOW it is implemented
should not be defined just that it is reasonable on the platform.

As an example on the PC I expect my compiler to support the packed
decimal notation but I would be happy with binary physical
representation.  The concept of packed on an external file should be
highly recommended (no matter what the internal representation of the
number) but if my code compiles with a warning and uses binary this is
where it is implementation specific.  The syntax is NOT optional, the
implementation of that syntax is.

What is the discussion about tapes and such with regard to portability.
I would have thought that every file is a sequence of records and the
concept of tape drive is external to all programs by now.

Ken
Your two cents has expired please insert comment to continue dialogue.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 13)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-22T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36D169F4.DB17E919@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afm3m$pvc@dfw-ixnews6.ix.netcom.com> <eDYy2.3$p.58@news19.ispnews.com> <36CC5848.4AA24F44@NOSPAMhome.com> <36CD5A00.313D4BB5@zip.com.au>`

```
> What is the discussion about tapes and such with regard to portability.
> I would have thought that every file is a sequence of records and the
…[3 more quoted lines elided]…
> Your two cents has expired please insert comment to continue dialogue.

I'm hoping for others to insert more coins - I'm more interested in
listening than talking about portability issues.

I once worked with an operating system called Aspen.  Amdahl designed it
for IBM clones and I liked it very much.  It never was released beyond
beta - I suspect for marketing reasons.   It had a help facility in
which I looked up tape labeling.  It mentioned one type of labeling
which was used by a company with "water cooled computers", a sly slap at
IBM.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 14)_

- **From:** paulr@bix.com (paulr)
- **Date:** 1999-02-23T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7at1eq$8p6@lotho.delphi.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afm3m$pvc@dfw-ixnews6.ix.netcom.com> <eDYy2.3$p.58@news19.ispnews.com> <36CC5848.4AA24F44@NOSPAMhome.com> <36CD5A00.313D4BB5@zip.com.au> <36D169F4.DB17E919@NOSPAMhome.com>`

```

Actually, there reference to 'water cooled computers' was more likey
a dig at CDC. ;) 

-Paul



Howard Brazee (brazee@NOSPAMhome.com) wrote:
: > What is the discussion about tapes and such with regard to portability.
: > I would have thought that every file is a sequence of records and the
: > concept of tape drive is external to all programs by now.
: > 
: > Ken
: > Your two cents has expired please insert comment to continue dialogue.

: I'm hoping for others to insert more coins - I'm more interested in
: listening than talking about portability issues.

: I once worked with an operating system called Aspen.  Amdahl designed it
: for IBM clones and I liked it very much.  It never was released beyond
: beta - I suspect for marketing reasons.   It had a help facility in
: which I looked up tape labeling.  It mentioned one type of labeling
: which was used by a company with "water cooled computers", a sly slap at
: IBM.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7ai81f$ohf@bgtnsc01.worldnet.att.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afm3m$pvc@dfw-ixnews6.ix.netcom.com> <eDYy2.3$p.58@news19.ispnews.com>`

```

Rick Smith wrote in message ...
>
>William M. Klein wrote in message <7afm3m$pvc@dfw-ixnews6.ix.netcom.com>...
>>
>>Rick,

This discussion is very interesting. It boils down to the fact that there
are vendors who are willing to opt out of the market supported by COBOL
because...

they lack the interest and see no profit

they lack the customer interest

they don't know their market

Why do users what these features may be misunderstood, but I can't figure
out how that could
be true.

Certainly, it should be clear that basic file management methods that read
and write files defined the same way is essential to avoid a major re-code
effort each time a new piece of hardware
is inserted in a system.

Certainly, it is clear that the layout of reports requires a certain level
of manipulation of the
data (left, center, right).

Major main frame systems have designed hardware
to handle the needs of move in COBOL.

Lots of time went into the design of hardware  since
COBOL became a standard, and found that the market for the hardware would
have to be supplemented by software before the market could really sell.

Surely, vendors would want their COBOL support to include unique abilities
of their hardware in a manner that can be duplicated elsewhere (well, now,
that may be a little optimistic).  I believe that the effort to make a
system and it's software support unique to garner more market is a waste of
effort as quality and service and price all play a part in the market
decisions.  I'm fairly sure without doing a study that vendors supporting
COBOL have been successful turning customers to their hardware because the
COBOL WAS the same. Or so nealy so that it was done via a computer program.

In my view, vendors and users in the community interested in this subject
have more to gain by finding a way to define "common" language for business
programming.  Otherwise, why waste their corporate assets trying to tear it
down from the inside. It doesn't make sense to me, and the problem perhaps
is that both sides need to remember that in no way is the hardware and
software required to be the same, only the results.

The vendor is free to use what ever means desired to meet the standard.  If
that means is to report that the feature is NOT supported, and it is sold on
that basis, fine.  Let the buyer beware.

While I have been out of touch since 1981, I have not  been dead. At an ACM
meeting here a few years ago, the RISC computer was detailed as the program.
After all was said and done, someone asked if the design was now complete or
would they be adding more instructions.  The answer, well, we find we have
to add some things to handle COBOL.

People need to learn that it's not COBOL they are supporting, it Business
Data Processing. This covers a lot of applications, and the University level
thinking of the uses a computer are put to may be somewhat out of focus.
The days of Scientific Computers and Data Processing Computers are gone
(with the possible exception of very large systems for predicting weather or
other more difficult applications). Today, the PIII arrives with abilities
to do things considered just for games.

Wait until you see what games businesses play.

Warren Simmons
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-21T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3nWz2.1$w02.60@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afm3m$pvc@dfw-ixnews6.ix.netcom.com> <eDYy2.3$p.58@news19.ispnews.com> <7ai81f$ohf@bgtnsc01.worldnet.att.net>`

```

Warren Simmons wrote in message <7ai81f$ohf@bgtnsc01.worldnet.att.net>...
[...]
>
>This discussion is very interesting. It boils down to the fact that there
…[7 more quoted lines elided]…
>they don't know their market

I think this is especially true of the new screen handling feature.

For Windows, an implementor may reasonably believe that
applications produced with their COBOL will, in the future, be GUI.
This is because some, perhaps most, users have been convinced
that "GUI is the future." For this reason the implementor may
choose not to implement screen handling for "market position."
After all, why support the feature if "nobody wants it."

Yet, as a developer, I still want character screens during
development, some testing, and maintenance. It simply takes
longer to create GUI interfaces than character screens. The
additional time for creating those GUI interfaces to support
development, testing, and maintenance is a waste since my
customer will never see them and character screens are sufficient.

Those implementors that choose not to implement screen handling
apparently don't understand that the developer is their market
and to satisfy those, who develop for Windows, both GUI and
screen handling must be available.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afsm9$583$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com>`

```
Can you name one computer system that Cobol runs
on that does not support screens or printers?

Rick Smith wrote in message ...
>
>Donald Tees wrote in message <7afd1t$ovg$1@news.igs.net>...
…[30 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afuoe$q29@dfw-ixnews8.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afsm9$583$1@news.igs.net>`

```
Donald Tees wrote in message <7afsm9$583$1@news.igs.net>...
>Can you name one computer system that Cobol runs
>on that does not support screens or printers?
>


When you are running an IBM mainframe "batch" program, there is no "access"
to any screen.  (Yes, there might be a CONSOLE operating the entire system -
but it is rarely running in a mode that the specific application can
monopolize.) I could imagine IBM providing a "cost-added" feature for
running in interactive environments (the same way that today they have a
cost-added feature for report-writer).

As far as printers go, I am well aware of some POS (point-of-sale)
environments that run COBOL applications but don't have printers available.

All of this goes to show that there are some legitimate (in my opinion)
features that are hardware/software dependent.  In most cases, IMHO, the
vendor does use the same compiler when both the hardware/software is
available as when it is not.  Therefore, I would expect the compile-time
support to be there while a "user-friendly" return code, file-status,
exception, etc would be returned at run-time - if the required run-time
facility were not there.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7agt4p$lup$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <7afsm9$583$1@news.igs.net> <7afuoe$q29@dfw-ixnews8.ix.netcom.com>`

```
I write POS systems. They are written for the PC,
in most cases.  In the case of customized hardware lacking
a standard printer, we do not try to implement reports. The
fact that a specific computer lacks a printer means very
little about a "platform".

While it has been many years since I worked in a batch
environment, I suspect it is very similar.

I am not saying that every environment has to support every
device.  I *am* saying that a "standard" compiler should support
the most common devices.  I also see no problem declaring that
a Timex computer will never run standard Cobol.

William M. Klein wrote in message <7afuoe$q29@dfw-ixnews8.ix.netcom.com>...
>Donald Tees wrote in message <7afsm9$583$1@news.igs.net>...
>>Can you name one computer system that Cobol runs
…[5 more quoted lines elided]…
>to any screen.  (Yes, there might be a CONSOLE operating the entire
system -
>but it is rarely running in a mode that the specific application can
>monopolize.) I could imagine IBM providing a "cost-added" feature for
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CC21FC.91D7126@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com>`

```
> Whoa! A few posts ago (I thought) we were discussing a COBOL
> implementation for a device that has no concept of screens or
> printers. My comments pertain to that system and the implementaion
> for that system. Your comments pertain to general purpose computer
> systems.

Cobol's a general purpose language, designed for general purpose
computer systems.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8DYy2.2$p.58@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <MqIy2.3$at3.30@news19.ispnews.com> <36CC21FC.91D7126@NOSPAMhome.com>`

```

Howard Brazee wrote in message <36CC21FC.91D7126@NOSPAMhome.com>...
>> Whoa! A few posts ago (I thought) we were discussing a COBOL
>> implementation for a device that has no concept of screens or
…[5 more quoted lines elided]…
>computer systems.

COBOL is a Business Oriented Language designed to provide
solutions for business problems. The definition of the language
allows these solutions to be done on general purpose computer
systems. The change in the definition of processor dependent
seemingly allows COBOL to be implemented on specific
purpose computer systems. That is what I have been discussing.
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CB3C14.D82898C0@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net>`

```
Donald Tees wrote:

> Read Turing regarding what computers can and cannot do. I will
> grant that usage's other than display are there for purposes of
…[5 more quoted lines elided]…
> specific CPU has no place in a "standard".

I almost agree with you.  But thinking of packed decimal (which can be
used to speed execution and can be used to save disk space) lead me to
think about EBCDIC and ASCII and unicode and double byte and different
sort sequences.  Should all of these be transparent to the COBOL
program?
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afsha$57k$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <36CB3C14.D82898C0@NOSPAMhome.com>`

```
Howard Brazee wrote in message <36CB3C14.D82898C0@NOSPAMhome.com>...

>I almost agree with you.  But thinking of packed decimal (which can be
>used to speed execution and can be used to save disk space) lead me to
>think about EBCDIC and ASCII and unicode and double byte and different
>sort sequences.  Should all of these be transparent to the COBOL
>program?

I think that things have changed a lot simply because of
prices of hardware.  I have seven to eight times the amount
of RAM that most of my systems require in disk space. By the
time the standard is published, a *microcomputer* is going
to have a !gig! of memory as a low end system.  The amount of
disk that packed decimal might save would take floating point
to express in pennies.  It would take 100 years to pay the cost
of the questions asked about it in the Cobol echo, let alone
the extra maintenance costs, conversion costs, etc. etc.  I have
even started to wonder if files are worth while ... maybe everything
should just be in arrays and tables.

But as to ASCII, EPCIDIC, Unicode, etc., I think yes, we need
the ability to handle all human languages.  That is quite a different
thing than cutting corners to save half a dozen transistors on a
CPU.  Likely, we would never see Cobol run on a 64k machine
again.  All those tricks were required then ... are they now?
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 10)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CC2192.8458CE1D@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <36CB3C14.D82898C0@NOSPAMhome.com> <7afsha$57k$1@news.igs.net>`

```
> But as to ASCII, EPCIDIC, Unicode, etc., I think yes, we need
> the ability to handle all human languages.  That is quite a different
> thing than cutting corners to save half a dozen transistors on a
> CPU.  Likely, we would never see Cobol run on a 64k machine
> again.  All those tricks were required then ... are they now?

I don't know how different it is.  With Unicode, text takes twice as
much space as it does with ASCII, also some operating systems are not
set up to handle Unicode.  At one time there were significant economic
and/or technological gains to using packed decimal instead of display,
now it is to using ASCII instead of Unicode, so we have means of
handling these.

The program logic would allow us to use display and/or Unicode
throughout.  So an argument that we should replace packed with display,
removing the choice from the programmer applies equally well/poorly with
replacing ASCII/EBCDIC with Unicode.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 11)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-18T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36CC27C2.88A807C7@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <36CB3C14.D82898C0@NOSPAMhome.com> <7afsha$57k$1@news.igs.net> <36CC2192.8458CE1D@NOSPAMhome.com>`

```
My word processor can print documents on both sides of the paper.  When
it comes time to print, it checks to see if the printer knows how to
print on both sides.  If it does, it tells it to do so, if it doesn't,
it prints odd pages and tells me to turn over my stack of output, then
prints the back sides.   I don't know what it would do if my printer was
an old fashoned band printer.

Many hardware implementations in COBOL can be done in a similar manner.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7affir$r8l@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <36ca11e9@news3.us.ibm.net> <1Rty2.6$j05.65@news19.ispnews.com> <7aei9s$pd3$1@news.igs.net> <3KCy2.3$zb1.39@news19.ispnews.com> <7afd1t$ovg$1@news.igs.net> <36CB3C14.D82898C0@NOSPAMhome.com>`

```
Howard Brazee wrote in message <36CB3C14.D82898C0@NOSPAMhome.com>...
>Donald Tees wrote:
>  <some sinppage>
…[4 more quoted lines elided]…
>program?

Funny, you should mention DBCS.  Some of this is in the processor-dependent
list and some of it is not.  I made a comment on this to the committee and
they ASSURED me that you can create a conforming implementation without full
ISO-10646 (DBCS and beyond) support - however, I am not totally convinces of
this yet.  However, again, the "language" is there in the draft Standard so
that *if* your processor supports the feature *and* the implementor's
discretion wants to implement it,  then the portable language does produce
portable semantics.

NOTE:  The Standard has for years *required* that all conforming
implementation provide support for ASCII (via the STANDARD-1 and STANDARD-2
required parts of the Special-Names paragraph).  The Standard does not (and
I don't think ever will) support EBCDIC, Unicode (when different from 10646)
or any other "proprietary" system.  Thus, if you are running in an EBCDIC
environment, the vendor is *FORCED* into providing some ASCII support for
you (and it is exactly this type of "forcing" that I would like to see
applied to file sharing and record locking, for example).
```

###### ↳ ↳ ↳ Re: * Please read and comment

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<qczy2.7070$Xl5.11549983@news1.mia>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com>`

```
Rick Smith wrote:
>
>Numeric coprocessors on PCs have nothing to do with decimal
>arithmetic. The coprocessor is for floating-point. The x86 micro-
>processor instruction set has instructions for decimal arithmetic. It is
>these instructions that allow for implementation of packed-decimal.

Rick, surely you know that the Intel FPU can handle binary and packed
decimal integers, just as well as real numbers.  The reason FPU's are
not always used for integers and decimal numbers is that the CPU can
often handle them as, or more, easily.  But the FPU can be useful when
integers and real numbers are used together in a calculation, or when
there are long chains of integer calculations.  All numbers are stored,
and calculations are done, inside the FPU in extended floating point,
which can represent the integer values exactly.
```

###### ↳ ↳ ↳ {OT} Inside Intel Nightmare (was: Re: * Please read and comment)

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<1ZGy2.2$at3.92@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <qczy2.7070$Xl5.11549983@news1.mia>`

```

Judson McClendon wrote in message ...
>Rick Smith wrote:
>>
…[6 more quoted lines elided]…
>decimal integers, just as well as real numbers.

About 1988 I knew it. Obviously, I did not know it when I posted.
I knew it again 6 hours after posting when it reached out of the
past and grabbed my ... well, er, ... attention.

Anyway, in the nightmare, I am trapped inside an Intel
microprocessor. I try to get out. I make all the right turns;
but I keep getting deeper and deeper because everything
is backward. ;-)
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: {OT} Inside Intel Nightmare (was: Re: * Please read and comment)

_(reply depth: 5)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7afsnq$586$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <36c9685b@news3.us.ibm.net> <vthy2.5$682.144@news19.ispnews.com> <qczy2.7070$Xl5.11549983@news1.mia> <1ZGy2.2$at3.92@news19.ispnews.com>`

```
<G> try a right shift ...

Rick Smith wrote in message <1ZGy2.2$at3.92@news19.ispnews.com>...
>
>Judson McClendon wrote in message ...
…[22 more quoted lines elided]…
>
```

#### ↳ Re: * Please read and comment

- **From:** riplin@kcbbs.gen.nz
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7acf4t$6fr$1@nnrp1.dejanews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com>`

```
In article <7a7s8e$34s@dfw-ixnews10.ix.netcom.com>,
  "William M. Klein" <wmklein@ix.netcom.com> wrote:
> "3.1.5 Processor-dependent language elements
>     - USAGEs BINARY, floating-point, and PACKED-DECIMAL
…[5 more quoted lines elided]…
>     - Record Locking and File Sharing

Some of these items may be un-implementable in certain environments.  eg
read previous may not be possible if the isam file system is built in and
there is no mechanism to get the previous record reliably.

Record locking relies of OS features, if the OS does not support this
then it cannot work reliably.

If the items are forced as a standard then some implementors will not
be able to produce a standard compiler and will thus veto the whole
process.  Having it hardware dependant means that the standard can get
passed.  It is doesn't have what _you_ want don't buy those that haven't
(or cannot) implement these features.

Richard

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: * Please read and comment

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<36C9C538.65AEA86B@NOSPAMhome.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <7acf4t$6fr$1@nnrp1.dejanews.com>`

```
> Some of these items may be un-implementable in certain environments.  eg
> read previous may not be possible if the isam file system is built in and
…[9 more quoted lines elided]…
> (or cannot) implement these features.

Then these should be features which should return warnings at compile
time and errors at run time.  To make this work, the program should be
able to do a run time check.  If this is done we could create ANSI
standard programs which work in a multi-OS environment.
```

##### ↳ ↳ Re: * Please read and comment

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-16T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7acrfj$jne@dfw-ixnews11.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <7acf4t$6fr$1@nnrp1.dejanews.com>`

```
I don 't agree with the following at all. In the history of COBOL there have
been a NUMBER of things that the existing/native/OS system did not support
and the COBOL implementor had to find a way of providing.

A relatively recent example of this was on IBM mainframes which did not
support variable length relative files when the ANSI'85 Standard required
them.  IBM introduced a SIMVRDS option which provided the semantic (and
syntactic) support for this - even before VSAM provided it.

If you go farther back (as Don Nelson himself pointed to) many environments
did not provide ANY "isam" support when COBOL required it (or provided it in
slightly to vastly different ways).  Because the COBOL Standard defined how
it had to "look" to a COBOL program a truly portable facility now exists -
even though the underlying software is often quite different.

Now, I am not saying that ever environment needs to support "character mode"
terminals (needed for the "new" Accept/Display facility).  But I would say
that every environment that HAS such terminals should be required to support
the Standard definition.

The same is certainly true for File Sharing and Record Locking.  There
simply is no reason that any operating systems or environment which has its
own "proprietary" system shouldn't be required to provide a PORTABLE
solution to the problem.
```

###### ↳ ↳ ↳ Re: * Please read and comment

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<vEAy2.2$zb1.50@news19.ispnews.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <7acf4t$6fr$1@nnrp1.dejanews.com> <7acrfj$jne@dfw-ixnews11.ix.netcom.com>`

```

William M. Klein wrote in message <7acrfj$jne@dfw-ixnews11.ix.netcom.com>...
[...]
>
>The same is certainly true for File Sharing and Record Locking.  There
…[3 more quoted lines elided]…
>
In other words, the standard for the COBOL Language supercedes the
"standard" for the operating system?
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@inospam.netcom.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7aeotm$4jd@dfw-ixnews3.ix.netcom.com>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <7acf4t$6fr$1@nnrp1.dejanews.com> <7acrfj$jne@dfw-ixnews11.ix.netcom.com> <vEAy2.2$zb1.50@news19.ispnews.com>`

```
Rick Smith wrote in message ...
>
>William M. Klein wrote in message
<7acrfj$jne@dfw-ixnews11.ix.netcom.com>...
>[...]
>>
>>The same is certainly true for File Sharing and Record Locking.  There
>>simply is no reason that any operating systems or environment which has
its
>>own "proprietary" system shouldn't be required to provide a PORTABLE
>>solution to the problem.
…[7 more quoted lines elided]…
>

No, the language Standard places semantics on its own syntax. *IF* you use
the COBOL syntax on any operating system, you have the right to expect the
COBOL semantics.  On the other hand, if you use the operating system
facilities (via external JCL, APIs, etc), I would expect you to get the
operating system semantics.
```

###### ↳ ↳ ↳ Re: * Please read and comment

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-02-17T00:00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7af1t9$8bj$1@news.igs.net>`
- **References:** `<7a7s8e$34s@dfw-ixnews10.ix.netcom.com> <7acf4t$6fr$1@nnrp1.dejanews.com> <7acrfj$jne@dfw-ixnews11.ix.netcom.com> <vEAy2.2$zb1.50@news19.ispnews.com>`

```
Yes.  If one is writing in Cobol.  The same as the specifications
for applications should not be altered to fit the computer.  The
whole point of using a computer is that it is generic.

Rick Smith wrote in message ...
>
>William M. Klein wrote in message
<7acrfj$jne@dfw-ixnews11.ix.netcom.com>...
>[...]
>>
>>The same is certainly true for File Sharing and Record Locking.  There
>>simply is no reason that any operating systems or environment which has
its
>>own "proprietary" system shouldn't be required to provide a PORTABLE
>>solution to the problem.
…[7 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
