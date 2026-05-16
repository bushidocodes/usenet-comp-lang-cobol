[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# J4 - presentation/discussion on "Future of the COBOL Standard"

_37 messages · 12 participants · 2008-03_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-03-09T20:16:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HAXAj.5290$FE.820@fe05.news.easynews.com>`

```
I thought that some (many?) of those who watch CLC would be interested in a 
paper that was just put out on the J4 website.  The following are the "foils" 
for a Micro Focus presentation scheduled for next Wednesday, March 12.  If 
anyone reading this newsgroup has comments that they would like included in the 
discussion, you probably could still send them to the J4 chair (before Tuesday) 
and ask that they be included in the discussion.  You can send such comments to:

    bobkarlin <at> karlinskorner.com

and you may want to CC one of the presenters and ask for your views to be 
included in the discussion.  If so, CC:

    John.Billman <at> microfocus.com

The presentation foils are:

    08-0034 - Future of the COBOL Standard (Billman)

available at:

     http://www.cobolstandard.info/j4/files/08-0034.pdf
```

#### ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-10T17:07:03+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63jqf7F27lussU1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:HAXAj.5290$FE.820@fe05.news.easynews.com...
>I thought that some (many?) of those who watch CLC would be interested in a 
>paper that was just put out on the J4 website.  The following are the 
…[23 more quoted lines elided]…
> wmklein <at> ix.netcom.com

I won't be copying Bob Karlin, but here's what I think, anyway :-)

As COBOL is fundamental to MicroFocus' core business it is understandable 
they would want to try and rejuvenate or re-invent it.

I think their idea to rejuvenate the standard is not a bad one, but to 
expect COBOL to move into a world of objects and components, when there is 
no user interest in the OO features of it, is simply myopic.

Line by line development and maintenance of code is non-viable as a forward 
strategy, and the only place where there is likely to be a COBOL market  for 
some time yet is in Legacy and re-factoring or re-wrapping Legacy so it can 
run in modern environments like .NET/Mono.

Any new standard should be stressing support for building OO components in 
COBOL. As there is no user demand for that, there is little point in doing 
it.

Doing what there IS user demand for (pretty much "same old, same old"), 
while commendable on the part of MicroFocus, is expensive and ultimately 
pointless. COBOL users (for the most part...) are currently out of touch 
with IT reality. The people who are demanding features like XML support 
haven't realised that the world has already moved on and XML is almost 
obsolete. Sure let's cater for bigger numbers... (does it REALLY matter?) 
The demands of the (rapidly dwindling) COBOL community are really not worth 
catering to in the hopes of future long term revenue generation.

It's like Mediaeval scribes demanding better quality parchment and goose 
feathers, while Gutenburg is building his printing press.

Despite the claim of billions of lines of existing code (dubious at best; it 
has been eroded yearly for the last 5 years (at least...) at a rate of 
millions of lines every year, by replacement with packaged solutions, 
refactoring, and migration to Java and other solutions...), even the most 
optimistic observer cannot see an expanding future for COBOL as a procedural 
paradigm based language in a world that is increasingly more visual and more 
non-procedural.

If I were MicroFocus, I'd be doing some focusing on transport/migration 
mechanisms for COBOL, leveraging and re-factoring tools, and support for 
visually building COBOL components that can play nicely with other languages 
on level playing fields, like .NET.

Pete.
```

##### ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-10T07:16:52
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13t9o34h59fed18@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net>`

```
On Mon, 10 Mar 2008 17:07:03 +1300, Pete Dashwood wrote:

> I won't be copying Bob Karlin, but here's what I think, anyway :-)
> 
…[3 more quoted lines elided]…
>

I tend to agree - a new standard should be looking to take the rough edges
off and not much more. 2002 was a huge over-reach. There is no constituency
for major new additions to COBOL, as evidenced by the fact 2002 has not
been fully implemented by anybody.

Agree with you about XML also. XML was possibly exciting in about 1999. In
practice it is very cumbersome to use, and I don't see the XML proposals
for COBOL solving this.

COBOL is not a good candidate for running on JVMs and .NET due to
technical problems ie use of redefine and pointers (which are in effect
arbitrary redefines), also packed decimal which is not well supported off
the mainframe. You can make it work, but it will run slowly.

> Line by line development and maintenance of code is non-viable as a forward 
> strategy, and the only place where there is likely to be a COBOL market  for 
…[10 more quoted lines elided]…
> 

I would suggest, without having proof, that there are probably more lines
of code being written per year across all languages than ever before.
Packages and components are very useful but a lot of code is still needed.

My observation of big companies is that the COBOL base is going away very
slowly. I have seen things replaced by packages, but a lot of the packages
were written some time ago, in a language called COBOL.

It is hard to replace a custom application that is deeply embedded into
your business processes with a package. Look at the many debacles with SAP
implementations for some examples.

If the 200bn lines of code number is anywhere near right, the dollars
involved in replacing them is frightening. The cost is probably in the
$10-50 trillion dollar range.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-11T00:47:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63klf2F27u25dU1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com>`

```


"tim" <TimJ@internet.com> wrote in message 
news:13t9o34h59fed18@corp.supernews.com...
> On Mon, 10 Mar 2008 17:07:03 +1300, Pete Dashwood wrote:
>
…[45 more quoted lines elided]…
> Packages and components are very useful but a lot of code is still needed.

Yes, that is certainly true right now. But things are changing, and the rate 
of change is accellerating.
>
> My observation of big companies is that the COBOL base is going away very
> slowly. I have seen things replaced by packages, but a lot of the packages
> were written some time ago, in a language called COBOL.

Hmmm... I won't argue that one, because I really don't know, and I haven't 
been at the coal face for a couple of years. (I expect to be back there 
soon... :-)) Certainly, Peoplesoft I believe is COBOL based, IBM's HUON 
solution is too, and there are probably a few other corporate ones that were 
originally built for mainframes. There is a large installed base (at least 
in lines of code) for these packages and they are backed by large 
corporations like IBM, but that doesn't mean they can't also be eroded like 
so many on-site tailored corporate COBOL solutions.
>
> It is hard to replace a custom application that is deeply embedded into
> your business processes with a package.

It is if you don't change the Business... :-)  Many places are finding it is 
actually cheaper to standardise their processes and procedures on a package 
that provides consistent results across all branches, than to keep on 
grinding out bespoke software.

But, I believe the biggest thing that prevents COBOL being a strong player 
for the future, is that more and more systems need to be web based, and 
that's an area where components are definitely required. Consequently, COBOL 
is perceived as not playing well there. (I find this ironic, because I used 
OO COBOL to develop some pretty smart web sites at a time when nobody did 
that or even thought it was possible (...apart from Richard Plinston who was 
using COBOL to drive CGI when most people here thought the Web was just a 
passing fad...:-))).

Having grown used to C# and ASP.NET I can't honestly say I'd easily go back 
to COBOL for web development, but I am certainly not blind to the fact that 
OO COBOL can be very useful in this area.

> Look at the many debacles with SAP
> implementations for some examples.
>

Yes, I have actually been required to look at some of them :-)

However, there are also many successful SAP and Siebel installations, and I 
haven't heard about too many recent SAP debacles. I was in Germany when SAP 
was first developed (early 1970s) and worked (around 1977) on one of the 
first major sites to evaluate it. It was written in IBM Assembler and was 
pretty appalling, we thought. We rejected it, but Systems, Applications, and 
Products in Data Processing (in Mannheim, Germany) went ahead undeterred and 
the rest is history. It is fair to say that the SAP of 2008, is a far cry 
from the SAP of 1978, or even of 1998...


> If the 200bn lines of code number is anywhere near right, the dollars
> involved in replacing them is frightening. The cost is probably in the
> $10-50 trillion dollar range.

Well, first, I don't believe it is even close. (I haven't seen any credible 
sources; Gartner have a vested interest in supporting a large COBOL base, 
although, as it has eroded, they have been less vociferous, and MicroFocus 
also have a vested interest in portraying COBOL as a major player (whether 
it is or not)).

Second, even if it were, it isn't about "replacement cost" as mostly it 
isn't done with a Big Bang replacement. The cost of converting data and 
code, or migrating systems, is part of the ongoing "maintenance" cost which, 
as we all know, is the major cost for computer systems anyway.

The cost of NOT  moving away from COBOL could be even more astronomical...

Pete.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-03-10T09:27:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nikat3tj211nuovo8kmmbdplfvmoddosb9@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <63klf2F27u25dU1@mid.individual.net>`

```
On Tue, 11 Mar 2008 00:47:46 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Yes, that is certainly true right now. But things are changing, and the rate 
>of change is accellerating.

Something in that wording sounds wrong to me.   But I can't say that
it is wrong.   If a rate of change is accelerating is that like saying
a velocity is accelerating?    Is it the same as saying "change is
accelerating"?   I'm not sure.

>But, I believe the biggest thing that prevents COBOL being a strong player 
>for the future, is that more and more systems need to be web based, and 
>that's an area where components are definitely required. Consequently, COBOL 
>is perceived as not playing well there. 

I still think of systems as data based.   The web part is the I/O for
the type of work I do.    But databases don't need CoBOL either.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-03-10T12:35:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4vat39oogub8ucqdao5qpk5arlbcbfmkv@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <63klf2F27u25dU1@mid.individual.net> <nikat3tj211nuovo8kmmbdplfvmoddosb9@4ax.com>`

```
On Mon, 10 Mar 2008 09:27:08 -0600, Howard Brazee <howard@brazee.net> wrote:

>On Tue, 11 Mar 2008 00:47:46 +1300, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
>accelerating"?   I'm not sure.

Both. It's the second derivative, written f'(x). In the example of a moving car, speed
f(p) is the rate of change of its position, acceleration f'(p) is the rate of change of
speed. 

A non-zero second derivative implies the original function (if it is a function) is of at
least 2nd degree. 

>>But, I believe the biggest thing that prevents COBOL being a strong player 
>>for the future, is that more and more systems need to be web based, and 
…[4 more quoted lines elided]…
>the type of work I do.    But databases don't need CoBOL either.

Data are nouns. Cobol is based on verbs (perform, move), as is SQL (select, update).
Object oriented languages are based on nouns.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-03-10T20:47:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tblldk2f3m41c@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <63klf2F27u25dU1@mid.individual.net> <nikat3tj211nuovo8kmmbdplfvmoddosb9@4ax.com>`

```

"Howard Brazee" <howard@brazee.net> wrote in message 
news:nikat3tj211nuovo8kmmbdplfvmoddosb9@4ax.com...
> On Tue, 11 Mar 2008 00:47:46 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[17 more quoted lines elided]…
> the type of work I do.    But databases don't need CoBOL either.

I can't speak for waht Pete Dashwood meant, but imagine an exponential 
equation that specifies a rate of change. Next imagine that the exponent in 
the equation is itself varying at an exponential rate.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-11T13:54:39+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63m3i9F289aarU1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <63klf2F27u25dU1@mid.individual.net> <nikat3tj211nuovo8kmmbdplfvmoddosb9@4ax.com> <13tblldk2f3m41c@corp.supernews.com>`

```


"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:13tblldk2f3m41c@corp.supernews.com...
>
> "Howard Brazee" <howard@brazee.net> wrote in message 
…[25 more quoted lines elided]…
> in the equation is itself varying at an exponential rate.

Thanks Charlie, you and Robert both correctly interpreted what I was saying.

Perhaps I should have said: " But things are changing, and the rate of 
change is speeding up." I just don't like using two words where one will 
do... :-) Perhaps "increasing" would have done. Anyway, I'm sure my meaning 
is now clear.

Pete.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-03-11T08:09:21-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sh4dt31acem3hbsgs3qictkiac9891afen@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <63klf2F27u25dU1@mid.individual.net> <nikat3tj211nuovo8kmmbdplfvmoddosb9@4ax.com> <13tblldk2f3m41c@corp.supernews.com>`

```
On Mon, 10 Mar 2008 20:47:40 -0400, "Charles Hottel"
<chottel@earthlink.net> wrote:

>I can't speak for waht Pete Dashwood meant, but imagine an exponential 
>equation that specifies a rate of change. Next imagine that the exponent in 
>the equation is itself varying at an exponential rate. 

That is singularity type changes.   Or maybe just hyperbole.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-03-10T09:20:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com>`

```
On Mon, 10 Mar 2008 07:16:52 -0000, tim <TimJ@internet.com> wrote:

>COBOL is not a good candidate for running on JVMs and .NET due to
>technical problems ie use of redefine and pointers (which are in effect
>arbitrary redefines), also packed decimal which is not well supported off
>the mainframe. You can make it work, but it will run slowly.

Why does being able to use packed decimal make CoBOL a poor candidate?
If it doesn't fit in your environment, there's no requirement that it
has to be used.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 4)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-03-10T11:48:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OEdBj.19673$097.18812@newsfe21.lga>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com>`

```
As recently as last year, I worked with someone who insisted that PD had to
be used as it was faster. (In fact she dropped me from the project when I
didn't agree).   On the Univac machines we both worked on (DECADES ago), it
was true - well in the IBM 360 architecture-dominated world it certainly
was - but that of course ceased to be s o many years ago.  But there are
still people who haven't kept up to date, even on something as simple as
this, and such-like may insist on keeping things static.

People get such odd obsessions.  Some manufacturer - Honeywell, I think -
came up with  a proprietory silicon on sapphire memory structure.  It
worked - it had to!  But for a time there was a group of consultants who put
in their RPQ's the requirement that the proposed machine must have silicon
on sapphire memory.  How that would have affected processing their payrolls
or other mission-critical systems was never made out!

PL


Howard Brazee <howard@brazee.net> wrote in message
news:takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com...
> On Mon, 10 Mar 2008 07:16:52 -0000, tim <TimJ@internet.com> wrote:
>
…[7 more quoted lines elided]…
> has to be used.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 4)_

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-11T02:08:27
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tbqcrnr0sh3e3@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com>`

```
On Mon, 10 Mar 2008 09:20:46 -0600, Howard Brazee wrote:

> On Mon, 10 Mar 2008 07:16:52 -0000, tim <TimJ@internet.com> wrote:
> 
…[7 more quoted lines elided]…
> has to be used.

If the program you are compiling says packed-decimal the standard says it
must be stored in packed decimal format. Of course you can provide
optimization flags that allow this rule to be overridden in the name
of speed. But with redefines and pointers/linkage it gets very difficult to
maintain correctness in the generated code if you change the format from
packed decimal to binary for example.

Packed decimal is mostly about the same speed as binary on IBM mainframes,
but it's a lot slower than binary on most Unix/PC CPUs. Packed decimal is
a lot faster than display format on mainframes for arithmetic, due to lack
of microcode support for most arithmetic operations performed on display
format data.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-03-11T08:16:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com>`

```
On Tue, 11 Mar 2008 02:08:27 -0000, tim <TimJ@internet.com> wrote:

>
>If the program you are compiling says packed-decimal the standard says it
…[4 more quoted lines elided]…
>packed decimal to binary for example.

If the data are packed, then it doesn't matter what language is being
used - it has to handle the data.

If the data aren't packed, then it doesn't matter what language is
being used - it has to handle the data.

But if you are starting from scratch, if you don't wish to use packed
decimal.   Then don't.   Even if you're programming in CoBOL.

>Packed decimal is mostly about the same speed as binary on IBM mainframes,
>but it's a lot slower than binary on most Unix/PC CPUs. Packed decimal is
>a lot faster than display format on mainframes for arithmetic, due to lack
>of microcode support for most arithmetic operations performed on display
>format data.

On IBM mainframes I use packed-decimal for efficiency purposes.   On
Windows machines, I don't.    

Just because CoBOL knows how to handle packed decimal, doesn't mean I
have to use it when I program in CoBOL.

It doesn't make sense to switch from CoBOL to avoid using
packed-decimal.

That said - I know of people who argued shops should switch from CoBOL
to PL/I for a very similar reason.   They liked PL/I because it had
bounds checking on tables.   But they could have had bounds checking
on their CoBOL programs by changing a switch on their compilers.   I
guess it was easier to persuade management to switch languages than it
was to change the standard created by a long-gone systems programmer.

Idiocy.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 6)_

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-15T01:24:05
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tm99l2eagk6d4@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com>`

```
On Tue, 11 Mar 2008 08:16:22 -0600, Howard Brazee wrote:

> On Tue, 11 Mar 2008 02:08:27 -0000, tim <TimJ@internet.com> wrote:
> 
…[16 more quoted lines elided]…
> 

I was speaking from the compiler-writer's perspective. A compiler-writer
cannot control what the programmer codes, and is bound by the standard if
he wants to claim standards compliance.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-03-14T20:42:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<08dmt3dht4bejrrh6i954h78vfmq2c36em@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com>`

```
On Sat, 15 Mar 2008 01:24:05 -0000, tim <TimJ@internet.com> wrote:

>On Tue, 11 Mar 2008 08:16:22 -0600, Howard Brazee wrote:
>
…[22 more quoted lines elided]…
>he wants to claim standards compliance.

Serious question: why does the compiler writer want to claim standards compliance? 
Do users ask for it? No. Is it worth the effort to implement a huge feature such as
indexed files that you know no one will ever use? I don't think so. The only reason it's
in the standard is because indexed files used to be free, provided by the mainframe
operating system. That's no longer the case under Unix and Windows. 

Wouldn't intrinsic SQL make more sense? Not only is that something users would actually
use, but also it would be a gateway to legacy indexed files via ODBC drivers.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-03-14T21:39:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tmdoko86p7a8f@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com> <08dmt3dht4bejrrh6i954h78vfmq2c36em@4ax.com>`

```

"Robert" <no@e.mail> wrote in message
news:08dmt3dht4bejrrh6i954h78vfmq2c36em@4ax.com...

[snip]

> Serious question: why does the compiler writer want to claim standards
compliance?
> Do users ask for it? No. Is it worth the effort to implement a huge
feature such as
> indexed files that you know no one will ever use? I don't think so. The
only reason it's
> in the standard is because indexed files used to be free, provided by the
mainframe
> operating system. That's no longer the case under Unix and Windows.

Elements in "B.3 Processor-dependent language element list"
need not be implemeted to comply with the 2002 standard.

See 3.1.5 Processor-dependent language elements, which says,
in part, "The decision of whether to claim support for a
processor-dependent language element is within an implementor's
discretion. Factors that may be considered include, but are not
limited to, hardware capability, software capability, and market
positioning of the processor."

Both decimal arithmetic and indexed-sequential files, which need
a "mass storage type of device," fall under processor-dependent.

Users will not ask for compliance when they have no reason to
suspect non-compliance!

> Wouldn't intrinsic SQL make more sense? Not only is that something users
would actually
> use, but also it would be a gateway to legacy indexed files via ODBC
drivers.

I'm satisfied with ISAM, so it wouldn't make more sense to me. <g>
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-03-15T13:24:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ki8ot3hj4s6brmfml4428t6ocgo6s096o1@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com>`

```
On Sat, 15 Mar 2008 01:24:05 -0000, tim <TimJ@internet.com> wrote:

>I was speaking from the compiler-writer's perspective. A compiler-writer
>cannot control what the programmer codes, and is bound by the standard if
>he wants to claim standards compliance.

So compiler writers include support for a wide variety of tools.   How
is that bad?

Programmers still are responsible for knowing what works for them.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 7)_

- **From:** Waldek Hebisch <hebisch@math.uni.wroc.pl>
- **Date:** 2008-03-16T18:41:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<frjpkq$q51$1@z-news.pwr.wroc.pl>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com>`

```
tim <TimJ@internet.com> wrote:
> On Tue, 11 Mar 2008 08:16:22 -0600, Howard Brazee wrote:
> 
…[23 more quoted lines elided]…
> 

I must admit that I did not see the Cobol standard.  But most standards
for programming languages have a chapter about compliance.  This chapter
tells you what an implementation ("processor") should do to be
complianat.  I have seen _no_ standard that requires using specific
format for data in memory.  Closest to such requirement is C standard,
but C standard is pretty clear ("as if" rule) that implementation can
do whatever is conveniet as long as _observable_ effect of running
program agrees with the standard.  Of course, there is a question
what is observable.  Clearly, rounding has observable effects, but
it is easy to do "decimal" rounding using binary aritmetic.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 8)_

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-16T22:17:12
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tr738gem9rm71@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com> <frjpkq$q51$1@z-news.pwr.wroc.pl>`

```
On Sun, 16 Mar 2008 18:41:30 +0000, Waldek Hebisch wrote:

> I must admit that I did not see the Cobol standard. But most standards
> for programming languages have a chapter about compliance. This chapter
…[9 more quoted lines elided]…
>
The COBOL standard is prescriptive about a lot of things in a way that
many other standards are not. I just checked and it is very specific that
the packed decimal data must be stored in radix-10 and each digit must
occupy the minimum amount of storage. Similar prescriptiveness exist about
usage synch and in other areas. Unfortunately cut and paste from the
cobol-85 standard does not work very well or I would include an extract
for you.

There are also a lot of rules about situations where errors or warnings
must be detected. For example in data definitions, clauses must be in a
certain order and warnings given about exceptions.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 9)_

- **From:** Waldek Hebisch <hebisch@math.uni.wroc.pl>
- **Date:** 2008-03-19T15:01:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<frr9ru$5so$1@z-news.pwr.wroc.pl>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com> <frjpkq$q51$1@z-news.pwr.wroc.pl> <13tr738gem9rm71@corp.supernews.com>`

```
tim <TimJ@internet.com> wrote:
> On Sun, 16 Mar 2008 18:41:30 +0000, Waldek Hebisch wrote:
> 
…[19 more quoted lines elided]…
>

Let me play devils advocate: current practice to get "minimum amount of
storage" is to use compression.  One very efficient compression method
is arithmetic coding.  With reasonable assumptions (that digits are
independent and that all values of a digit have equal probability)
for strings of digits arithmetic coding reduces to using binary encoding.
So, if you stress "minimum amount of storage" you can claim that other
implementations are non-compliant and binary is the only compilant 
implementation (on binary machine).  Now, one can argue that "each digit"
implies that digits are stored in separate storage units.  But this is
clearly not the case in PC implementations: at machine level storage unit
is 8-bit byte (octet) while traditional implementation puts two digits
into a byte.  In other words, accesing a digit is composite operation
involving addres aritmetic, shifts and bit masks.  Using binary
means that "digit accesor" employs division and remaider operation
-- at concetpual level this does not differ from previous case.

Back to normality: I do not seriously claim that traditional
implementations of packed decimal are non-compliant.  What I say is
that one should not read standards too literaly.  For example, typical
wording for assignment instruction says that data is stored 
(transferred to the storage) -- literal reading would forbid register
allocation.  Also, literal reading of standars would exclude
running on modern hardware: hardware executes instructions in
different order than they appear in the program.  In both cases
the crucial thing is that differences are not observable:
standards specify abstract machines, real machines are different
but without extra tools (beyond scope of the standard) nobody
can tell the difference.

Another remark: IBM is pushing "decimal floating point".  My
understanding of their announcements is that thay want to switch
decimal arithmetic in Cobol and PL/I to use "decimal floating point".
However, "decimal floating point" stores three-digit groups
ech in 10 bits.  Your interpretation of the fragment above
seem to be that representing packed decimal as "decimal floating
point" is non-compilant (IMHO the only sticky point is
"minimum amount of storage" -- "decimal floating point" stores
exponent, which for fixed point types is redundant).

So, I still belive that the intent of the Cobol standard is to
give you an abstract model and that implementation is compliant
as long as observable aspects agree with the model.  So really,
the question is what is intended to be observable.  Some folks
here in the past claimed to use packed decimal to be able to
easily read numbers in hexadecimal core dump.  I would say that
core dumps are outside scope of the Cobol standard, so can
be ignored.  More problematic may be interface to C/assembler
-- I am not sure how much Cobol standard says here, but I would
say that each Cobol compiler have enough possibilites to choose
data representation which is incompatible with other compileres
to make C/assembler interface compiler specific.  Another area
are files: files are frequently used to exchange data between
systems, so it makes sense to use "portable" represention for
items in the files.  But IIUC represention on disk may be
different from representation in memory.

Now, literally following standard may be the easiest way to
get compliant implementation -- abstract interpretation means
that you need to understand the whole standard in order to
determine observable consequences.  And when standard is revised
it may introduce changes which invalidate an implementation
which used some freedoms given by previous standard.

It would be interesting to get comment from Bill Klein what
the committee really intended concerning packed decimal.
 
> There are also a lot of rules about situations where errors or warnings
> must be detected. For example in data definitions, clauses must be in a
> certain order and warnings given about exceptions.
> 

Well, that completly different story: errors or warnings are clearly
observable.  OTOH it makes sense to have flags which turn on
nonstandard behaviour, where you detect less or more errors.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 10)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-03-19T09:25:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1c2u3hmb6kg365vv4voram8ggcimsc6ut@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com> <frjpkq$q51$1@z-news.pwr.wroc.pl> <13tr738gem9rm71@corp.supernews.com> <frr9ru$5so$1@z-news.pwr.wroc.pl>`

```
On Wed, 19 Mar 2008 15:01:18 +0000 (UTC), Waldek Hebisch
<hebisch@math.uni.wroc.pl> wrote:

>Back to normality: I do not seriously claim that traditional
>implementations of packed decimal are non-compliant.  What I say is
…[9 more quoted lines elided]…
>can tell the difference.

Speaking of normality, it is interesting to look at what happens
behind the scenes in some large, efficient, "relational" databases.

But as you say - we really don't care, as long as they appear to us to
work the way we expect.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-03-19T19:51:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N8eEj.97829$us.10451@fe04.news.easynews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com> <frjpkq$q51$1@z-news.pwr.wroc.pl> <13tr738gem9rm71@corp.supernews.com> <frr9ru$5so$1@z-news.pwr.wroc.pl>`

```
What the committee intended for both USAGE PACKED-DECIMAL (and USAGE BINARY) is 
pretty clear if you look at the implementer defined list (and realize that these 
ARE in that list).  For Binary it states,

"169) USAGE BINARY clause (computer storage allocation, alignment and 
representation of data). This item is required. This item shall be documented in 
the implementor's user documentation. (13.16.58, USAGE clause
general rule 4)"

and for Paced-Decimal it states,

"178) USAGE PACKED-DECIMAL clause (computer storage allocation, alignment and 
representation of data). This item is required. This item shall be documented in 
the implementor's user documentation. (13.16.58, USAGE clause, general rule 10)"

It seems pretty clear to me that for these usages (and many others) that the
  "computer storage allocation, alignment and representation of data"

are all implementer defined and intended to be so.  There has always been a 
difference between implementations whenit comes to packed-decimal and unsigned, 
even-number of digit, data items.

On IBM (and IBM-compatible) systems,
     Pic 9(02)  Packed-Decimal
requires 2 bytes of storage becuase a nibble is used for X"F" to indicate it is 
unsigned

Several other systems allow that picture clause to be stored in 1 byte.

It is my belief that the Standard INTENDED to consider both "conforming".
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 11)_

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-19T22:01:18
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13u339e2bo5dk14@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com> <frjpkq$q51$1@z-news.pwr.wroc.pl> <13tr738gem9rm71@corp.supernews.com> <frr9ru$5so$1@z-news.pwr.wroc.pl> <N8eEj.97829$us.10451@fe04.news.easynews.com>`

```
On Wed, 19 Mar 2008 19:51:09 +0000, William M. Klein wrote:

> What the committee intended for both USAGE PACKED-DECIMAL (and USAGE
> BINARY) is pretty clear if you look at the implementer defined list (and
…[15 more quoted lines elided]…
>

From the 85 standard:

"(9)   The USAGE IS PACKED-DECIMAL clause specifies that a radix of 10 is
used to represent a numeric item in the storage of the computer.
Furthermore, this clause specifies hat each digit position must occupy the
minimum possible configuration in computer storage. Each implementor
specifies the precise effect of the USAGE IS PACKED-DECIMAL clause upon
the alignment and representation of the data item in the storage of the
computer, including the representation of any algebraic sign..."

My interpretation of the above is that packed decimal must be stored in a
radix 10 format and the digits must be packed up. I'm not sure what
those words mean if they do not mean that. The use of the word "precise" to
me indicates that the implementor has some latitude but not complete
licence to ignore the clear words of the standard.

Obviously, the "as if" rule applies. If a compiler generates the same
results "as if" the data were stored as specified, you can't really
complain. However this does not buy as much as you might think. The
implementor is required to document the "precise" packed decimal format.
If I pass a PD item to a subroutine, and redefine it there, the subroutine
is allowed to assume that the item is truly in PD format.

You can always provide compiler options that allow the compiler to
bend the rules. But I stand by my claim that the standard is quite
constraining.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 10)_

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-19T21:39:24
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13u320c7k3ton64@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <nl4dt3t8k2uck8595ji5qdhnjkd3hlpumq@4ax.com> <13tm99l2eagk6d4@corp.supernews.com> <frjpkq$q51$1@z-news.pwr.wroc.pl> <13tr738gem9rm71@corp.supernews.com> <frr9ru$5so$1@z-news.pwr.wroc.pl>`

```
On Wed, 19 Mar 2008 15:01:18 +0000, Waldek Hebisch wrote:

> tim <TimJ@internet.com> wrote:
>> On Sun, 16 Mar 2008 18:41:30 +0000, Waldek Hebisch wrote:
>> 
>> > I must admit that I did not see the Cobol standard...

You should read the standard before indulging in all this speculation.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-03-20T00:34:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<frsbdu$e4m$1@reader2.panix.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <13tr738gem9rm71@corp.supernews.com> <frr9ru$5so$1@z-news.pwr.wroc.pl> <13u320c7k3ton64@corp.supernews.com>`

```
In article <13u320c7k3ton64@corp.supernews.com>,
tim  <TimJ@internet.com> wrote:
>On Wed, 19 Mar 2008 15:01:18 +0000, Waldek Hebisch wrote:
>
…[5 more quoted lines elided]…
>You should read the standard before indulging in all this speculation.

But... reading something might serve to decrease the amount about which 
one might indulge in speculation, what fun would *that* be?

DD
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 5)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-03-11T19:08:11-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<680et3p1p132cgq1ct75uuucrg6shba5i1@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com>`

```
On Tue, 11 Mar 2008 02:08:27 -0000, tim <TimJ@internet.com> wrote:

>On Mon, 10 Mar 2008 09:20:46 -0600, Howard Brazee wrote:
>
…[22 more quoted lines elided]…
>format data.


The only true decimal arithmetic on the IBM 360/370/390/z systems is
packed decimal and (IEE754 something on the latest z).  It is more
efficient than converting to binary, doing the arithmetic and
converting back.  It also is more efficient than what I think is
available for decimal arithmetic on the Intel chips.  It is not nearly
as efficient as binary on the z series (or predecessors) if you are
not trying to get decimal rounding and behavior in division and other
places where it matters.  Incidentally COBOL is NOT one of the
languages for which support for the new floating point decimal
arithmetic is announce on the z series.

Clark Morris

Clark Morris 
>
>Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 6)_

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-15T01:22:11
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tm963mrp35g83@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <680et3p1p132cgq1ct75uuucrg6shba5i1@4ax.com>`

```
On Tue, 11 Mar 2008 19:08:11 -0300, Clark F Morris wrote:

> The only true decimal arithmetic on the IBM 360/370/390/z systems is
> packed decimal and (IEE754 something on the latest z).  It is more
…[7 more quoted lines elided]…
> Clark Morris

Do you have evidence for this? I did test this a few years ago and found,
to my great surprise, that packed and binary were the same speed. This may
have changed in the intervening years of course.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 7)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2008-03-15T21:06:12-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<etoot3l1umr1jfrnnlaoiiv8abeqpvqc1c@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <680et3p1p132cgq1ct75uuucrg6shba5i1@4ax.com> <13tm963mrp35g83@corp.supernews.com>`

```
On Sat, 15 Mar 2008 01:22:11 -0000, tim <TimJ@internet.com> wrote:

>On Tue, 11 Mar 2008 19:08:11 -0300, Clark F Morris wrote:
>
…[13 more quoted lines elided]…
>have changed in the intervening years of course.

Granted that my last exposure to timings was for the 360/30 and 360/40
but IBM put more work into speeding up the binary instructions than
the decimal instruction.  Storage to storage is claimed to be slower
than register to register or register to storage.  I suspect people on
comp.lang.asm370 could give you a more definitive answer.

Clark Morris
>
>Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-16T15:49:46+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<643g6bF282olrU1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <680et3p1p132cgq1ct75uuucrg6shba5i1@4ax.com> <13tm963mrp35g83@corp.supernews.com> <etoot3l1umr1jfrnnlaoiiv8abeqpvqc1c@4ax.com>`

```

```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 9)_

- **From:** tim <TimJ@internet.com>
- **Date:** 2008-03-16T04:17:38
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tp7r2g970pka9@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <680et3p1p132cgq1ct75uuucrg6shba5i1@4ax.com> <13tm963mrp35g83@corp.supernews.com> <etoot3l1umr1jfrnnlaoiiv8abeqpvqc1c@4ax.com> <643g6bF282olrU1@mid.individual.net>`

```
On Sun, 16 Mar 2008 15:49:46 +1300, Pete Dashwood wrote:

>> Storage to storage is claimed to be slower
>> than register to register or register to storage.
…[12 more quoted lines elided]…
> Pete.

I am sure that the ratio of decimal to binary speed has moved
around over the years. Different ratios of register to main memory speeds,
different numbers and speeds of cache, various things moving from
microcode to hardware, parallel execution etc.

However, at least at one time (late 1980s) they were indistinguishable in
speed on IBM mainframes. Based on how CPU architectures have evolved since
then I would not be surprised if this hasn't changed much in the meantime.
The general trend is that times are dominated by cache misses and branch
prediction misses, which would affect decimal and binary similarly.

Tim
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-16T17:39:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<643mkrF29m232U1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com> <takat3hnac8rubopu84tofpqvq4j0vi8h5@4ax.com> <13tbqcrnr0sh3e3@corp.supernews.com> <680et3p1p132cgq1ct75uuucrg6shba5i1@4ax.com> <13tm963mrp35g83@corp.supernews.com> <etoot3l1umr1jfrnnlaoiiv8abeqpvqc1c@4ax.com> <643g6bF282olrU1@mid.individual.net> <13tp7r2g970pka9@corp.supernews.com>`

```


"tim" <TimJ@internet.com> wrote in message 
news:13tp7r2g970pka9@corp.supernews.com...
> On Sun, 16 Mar 2008 15:49:46 +1300, Pete Dashwood wrote:
>
…[29 more quoted lines elided]…
>

I think that's fair comment. No disagreement here :-)

My points related to an earlier era...

Pete.
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-03-10T11:36:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ytdBj.19672$097.10985@newsfe21.lga>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13t9o34h59fed18@corp.supernews.com>`

```

tim <TimJ@internet.com> wrote in message
news:13t9o34h59fed18@corp.supernews.com...

> Despite the claim of billions of lines of existing code (dubious at best;
it
> has been eroded yearly for the last 5 years (at least...) at a rate of
> millions of lines every year, by replacement with packaged solutions,
> refactoring, and migration to Java and other solutions...), even the most
> optimistic observer cannot see an expanding future for COBOL as a
procedural
> paradigm based language in a world that is increasingly more visual and
more
> non-procedural.
>

(Tongue in cheek!)

I dunno.  Looked at in one way there has been nothing new in computing for a
long, long time.  Way back when, the Whirlwind and other pioneering machines
had a very small instruction set - often just 32 instructions.  This of
course expanded as time went by until somebody invented the RISC concept -
cutting down the number and complexity of the instructions.  The first
mass-storage devices used fixed-length records, short sectors, and absolute
addressing.  Twenty years later, IBM reinvented the same thing but callled
it FBA.  Once upon a time there was a central machine and dumb terminals.
This was reintroduced as client-server (I think so anyway, because I have
never seen a standard definition).  There used to be service bureaux: now
it's software as a service and computing on demand, or even the cloud.  So
who knows?  Procedural programming is not dead yet, nor is Cobol: we only
have to wait for someone to repackage it as the Next Great Thing.  What
would be great is to be that someone.  The riches, the guru status!

PL
```

##### ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2008-03-10T21:02:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13tbq3hb852cjc9@corp.supernews.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:63jqf7F27lussU1@mid.individual.net...

[snip]

> Despite the claim of billions of lines of existing code (dubious at best;
it
> has been eroded yearly for the last 5 years (at least...) at a rate of
> millions of lines every year, by replacement with packaged solutions,
> refactoring, and migration to Java and other solutions...), even the most
> optimistic observer cannot see an expanding future for COBOL as a
procedural
> paradigm based language in a world that is increasingly more visual and
more
> non-procedural.

Just a couple of notes from an "optimistic observer". <g>

"COBOL (COmmon Business Oriented Language) is the
programming language most widely used for commercial
and administrative data processing." -- Micro Focus LRM,
probably from the COBOL 85 standard.

The most common paradigm for "commercial and
administrative data processing"  is "clerks performing
procedures on or with data". COBOL came into existence as
a domain-specific language for impementing that paradigm.
Regardless of the implementation paradigm (procedural, OO,
functional, etc.) the result will neccesarily reflect the underlying
procedural basis for the required data processing. I suspect
that a great deal of programming with OOPLs is procedural
programming; but incorrectly claimed to be OO.

The expanding role for COBOL comes from the addition of
general-purpose programming language features in 2002;
features that complement the domain-specific features. Once
the general-purpose features become widely available and
discussed, more "multilingual" programmers can become
comfortable with "I can do that in COBOL".
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-12T00:38:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63n99oF27ou73U1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13tbq3hb852cjc9@corp.supernews.com>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13tbq3hb852cjc9@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[15 more quoted lines elided]…
> Just a couple of notes from an "optimistic observer". <g>

Other viewpoints always welcomed by me... :-)
>
> "COBOL (COmmon Business Oriented Language) is the
> programming language most widely used for commercial
> and administrative data processing." -- Micro Focus LRM,
> probably from the COBOL 85 standard.

Well, as it is the core of their business, they WOULD say that, wouldn't 
they? :-)

I don't believe it is even true today, but I can't prove it so won't argue 
it.

>
> The most common paradigm for "commercial and
> administrative data processing"  is "clerks performing
> procedures on or with data". COBOL came into existence as
> a domain-specific language for impementing that paradigm.

Not exactly as I recall... and I was there :-)

COBOL's major attraction was that it offered an "easily maintainable, 
platform independent" approach to "data processing".  It is true that  it 
was about "performing procedures on or with data" but it also offered 
freedom from being locked in to a specific vendor (at least, that was a 
major perceived benefit; in practice, it was not so easy to switch 
vendors...) People were more excited by COBOL at a technical level than at a 
functional level.

And, in those days, the concept of online interaction was not a 
consideration. All processing was deferred Batch processing. There weren't 
even random access devices; data was stored and processed sequentially on 
tapes. These were the roots of COBOL. We have come a long way since. True, 
when inteeractive devices became available, COBOL was enhanced to 
accommodate them, but the strength of the language was, and is, sequential 
batch processing.

It is not COBOL's "fault" that it is not so good at interactive processing. 
For years it was "the only game in town". Then came new approaches to 
programming and processing. The Object paradigm arrived and, again, COBOL 
was enhanced to accommodate it. A fantastic feat of software engineering, 
but wasted because of the limited vision of the COBOL community who 
perceived it as just a fashion statement, unnecessary, and really just 
"modular programming, re-invented". The reality was that entrenched COBOL 
systems were doing most of the backbone processing and this led to a smug 
attitude on the part of COBOL practitioners who couldn't see COBOL being 
replaced any time soon... They had not factored the global effect and power 
of the Internet into their calculations... Within a decade, thousands of 
COBOL programmers were jobless, and COBOL fell from being the No. 1 most 
popular language for developing commercial computer systems,  to being 
outside the top 12 programming languages, according to a number of 
independent surveys.
(http://www.scriptol.org/choose.php
http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html
http://www.devtopics.com/most-popular-programming-languages/)

The rest of the world, not having been indoctrinated into the procedural 
paradigm, rushed to embrace the non-procedural paradigm and it was found 
ideal for distributed, encapsulated processing. New languages, designed 
specifically for building Object Oriented systems emerged. They weren't 
"self  documenting" and "easily maintainable" in the sense that COBOL was, 
and neither did they need to be. They were far more powerful and required 
less coding, and components built with them could be easily re-used. If 
something didn't work it didn't need to be "maintained", it could simply be 
discarded and rebuilt, quickly and easily. By the 21st century, visual tools 
capable of generating these objects were available, and today they are 
increasing in power exponentially, while COBOL is still tied to line by line 
coding and green screen editing.

COBOL, as a language, was simply overtaken by events.

> Regardless of the implementation paradigm (procedural, OO,
> functional, etc.) the result will neccesarily reflect the underlying
> procedural basis for the required data processing. I suspect
> that a great deal of programming with OOPLs is procedural
> programming; but incorrectly claimed to be OO.

Maybe, but that is an academic argument. It doesn't matter what you call it, 
the fact is that the new languages can be written quicker, re-written 
quicker, require much less code, and have facilities that COBOL simply 
doesn't. Whether they are doing procedural processing under the guise of OO 
or not is immaterial; they can be generated to do it quicker than a good 
COBOL programmer can code the thousands of lines it takes.

I have been astounded at the encapsulated functionality in languages like 
C#, that simply isn't available in COBOL. It doesn't even matter what the 
paradigm is, it is quicker to point and click in Visual Studio, than it is 
to write hundreds of lines of COBOL in ISPF. End of story.

>
> The expanding role for COBOL comes from the addition of
…[4 more quoted lines elided]…
> comfortable with "I can do that in COBOL".

I understand what you're saying, Rick, but I contend that they won't. I know 
from my own experience (somewhat like being dragged kicking and screaming 
into Java and C#) that the desire to go back to COBOL diminishes with the 
increasing understanding and facility in OO languages. Yes, I COULD develop 
web applications in OO COBOL, yes, I COULD write OO COBOL components, but I 
won't and don't. (I did for many years and felt like a "voice in the 
wilderness" receiving scorn and vitriol from most of the COBOL community 
when I suggested that OO might be important for COBOL,  and a total lack of 
support from COBOL vendors when problems arose. Nowadays when I have a 
problem, I don't need or want to go to MicroSoft; there are around 60 
million people writing C#... I can get a GOOGLEd solution in minutes. Also, 
the demonstrated attitude of the C# community is a helpful and positive one 
in the C# forums I have used...) I just don't believe that once 
"multilingual" programmers go away from COBOL, they will need or want to go 
back to it.

The "new" features in COBOL, even if they could be implemented, are not 
going to make any difference.

I respect MicroFocus for taking a hand in the standards debacle and I 
honestly wish them well. Whether they are driven by commercial necessity or 
a genuine desire to improve COBOL, what they are doing is commendable.

Unfortunately, I believe it is too late.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-03-11T08:28:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tc5dt31e3nggu69u61r8ffom301rhre9fu@4ax.com>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13tbq3hb852cjc9@corp.supernews.com> <63n99oF27ou73U1@mid.individual.net>`

```
On Wed, 12 Mar 2008 00:38:37 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Unfortunately, I believe it is too late.

Except for those of us whose best skills are CoBOL, I don't see that
this is particularly unfortunate.    Adapting CoBOL, or for that
matter C is not necessarily the best way to build new tools for our
new needs.

Kind of like the old idea of building a robot who drives a car just
like a chauffeur, sitting in the driver's seat, turning his head
around to see behind him, and stepping on the throttle.  Or for that
matter, designing a one person car to run just like a horse.

Sometimes starting over will create a better product.

(I wish computers had been designed from scratch to store data with
GMT in all their time-date-stamps - and languages such as CoBOL had a
function to convert the computer time to local).
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 4)_

- **From:** Jeff Campbell <n8wxs@arrl.net>
- **Date:** 2008-03-11T12:33:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1205259923_658@isp.n>`
- **In-Reply-To:** `<63n99oF27ou73U1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13tbq3hb852cjc9@corp.supernews.com> <63n99oF27ou73U1@mid.individual.net>`

```
Pete Dashwood wrote:
> "Rick Smith" <ricksmith@mfi.net> wrote in message 
> news:13tbq3hb852cjc9@corp.supernews.com...
…[35 more quoted lines elided]…
> 

[snipped]

>> Regardless of the implementation paradigm (procedural, OO,
>> functional, etc.) the result will neccesarily reflect the underlying
…[14 more quoted lines elided]…
> to write hundreds of lines of COBOL in ISPF. End of story.

Let me second or third or whatever that!  8-)

I discovered yesterday that list boxes in .NET store objects rather than just
strings (strings are objects). That means I can store an array of records
encapsulated as object instances in the list box. When an item in the displayed
list is selected, the code processing the click event has direct access to the
objects contents. No searching or sorting!

A PowerCOBOL list box ,at least as of version 5, only stores text, meaning that
code needs to be written to find the corresponding record in a table. Indicies
need to be managed in a synchronized fashion in the list box and the backing
table. Insertion, deletion, modification routines, etc. More code to write,
debug and support.

The really cool thing about storing  objects in the list box is that the objects
do not have to all be of the same type. I'm not sure how often this will be useful
but I can see having a list box that presents the user with a hierarchy of choices
the choices relating to different types of things.

> 
>> The expanding role for COBOL comes from the addition of
…[32 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

Jeff

> 
> 
> 


----== Posted via Pronews.Com - Unlimited-Unrestricted-Secure Usenet News==----
http://www.pronews.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: J4 - presentation/discussion on "Future of the COBOL Standard"

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-03-12T11:48:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63ogh8F28qtu6U1@mid.individual.net>`
- **References:** `<HAXAj.5290$FE.820@fe05.news.easynews.com> <63jqf7F27lussU1@mid.individual.net> <13tbq3hb852cjc9@corp.supernews.com> <63n99oF27ou73U1@mid.individual.net> <1205259923_658@isp.n>`

```


"Jeff Campbell" <n8wxs@arrl.net> wrote in message 
news:1205259923_658@isp.n...
> Pete Dashwood wrote:
>> "Rick Smith" <ricksmith@mfi.net> wrote in message 
…[61 more quoted lines elided]…
>

Thanks for your support, Jeff :-)

> I discovered yesterday that list boxes in .NET store objects rather than 
> just
…[24 more quoted lines elided]…
>

This is a good example, but it is just one of many...

Facilities like code reflection, generalized procedures through delegation, 
access to event models, simple building and processing of collections, 
access to a host of components that run across platforms and save 
incalcuable amounts of time, are just some of the facilities that COBOL 
simply doesn't even begin to address...

For batch processing, it doesn't matter; beyond that, it certainly does 
matter...

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
