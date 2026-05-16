[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mapping (CoBOL) Methodologies to Problem Domains

_99 messages · 12 participants · 2008-01_

---

### Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-22T18:55:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com>`

```
All -

Haven't been here for a while due to personal demands, but now that
I'm back, I wanted to put out an informal Call for Participation along
the following lines. In another forum I participate in we discuss
methodological approaches more than languages (eg. CMM vs. Agile).
Here is the essence of a post I put out there, and I'm putting it in
CLC to solicit the CoBOL angle, to wit, what methodologies are you
using in your CoBOL efforts: structured analysis / structured design,
object-oriented, custom, code-and-fix :-), whatever. CoBOL to
"language-du-jour" converts' opinions also welcome (that's at least
*you*, Mr. Pete Dashwood :-) ).

I guess it's OK to do some follow up here within this thread in CLC,
but seeing as how this is just a little bit off the usual beaten track
of CLC, I don't want it to get "out of hand" (as if anything here ever
does!)

Anyway, here is a "copy and past" of what I posted elsewhere!

All -

Anonymous's last post got me thinking, and I reviewed my c:\ drive for
some articles I had culled regarding this problem, which is namely,

"What methodologies/methods should we apply to what domains of
problems?"

I have three seminal works by Robert Glass that are directly relevant
here (you will need ACM and/or IEEE membership to get these, but I can
help you):

"Contemporary Application Domain Taxonomies"
http://portal.acm.org/citation.cfm?id=625489

"Some Heresy Regarding Software Engineering"
http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?tp=&arnumber=1309657&isnumber=29063

"Matching Methodology to Problem Domain"
http://portal.acm.org/citation.cfm?id=986228

In these works Glass makes it abundantly clear how **little** work has
been done in this area, by either industry or academia, and so this
might be an opportunity for some (relatively) groundbreaking work.

Those interested in exploring this aspect independently of <CLC and
other Forums>, please post here in this thread, or contact me offline
at my e-mail address. The goal for this exploration should be
initially modest (I have a fair amount of personal business to attend
to in the short term, which limits my time), but could be on the order
of accumulating enough "stuff" (viewpoints, rough "artifacts") to
present a "Roundtable", "Birds of a Feather", "Panel", or simply
"Gathering" at something like GLSEC (Great Lakes Software Excellence
Conference), but certainly not so much as to qualify as a "seminar" or
"workshop", let alone a "conference" :-).

I think for the time being this effort would be organized as a simple
cc: list for some occasional group e-mailings, and not yet anything
more structured.

But I'd like to get started on it by accumlating a list of interested
parties?

Any takers?

Ken
```

#### ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-23T16:57:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vns9hF1ns38fU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com...
> All -
>
…[9 more quoted lines elided]…
> *you*, Mr. Pete Dashwood :-) ).

I believe that any attempt at problem solution that is driven from a 
Language perspective will not be optimum, so looking for approaches taken 
with COBOL (as opposed to anything else) for me, is a non-starter.

I apply the same problem solution approaches no matter WHAT language is in 
use.

>
> I guess it's OK to do some follow up here within this thread in CLC,
…[12 more quoted lines elided]…
> problems?"

Pre-supposes that there ARE different domains of problem; in commercial 
computer programming this is arguable: "Get a solution implemented that 
costs as little as possible, takes as little time as possible, meets the 
Business requirements, and is comfortable for users to use." If you can 
manage to also minimise future maintenance and make the new system integrate 
nicely with current and foreseeable technical environments, that's a 
bonus...:-)


>
> I have three seminal works by Robert Glass that are directly relevant
…[14 more quoted lines elided]…
> might be an opportunity for some (relatively) groundbreaking work.

Glass should speak for himself.

Personally, I've been researching, analysing, postulating, experimenting, 
and considering this for the last 43 years. I have arrived at some 
interesting conclusions which will be published in a forthcoming book that 
will be completed later this year.

I can tell you this for nothing:

1. No single one of the current methodologies works to complete satisfaction 
(with the POSSIBLE exception of DSDM...) when applied by itself, alone.
2. There is a marked lack of imagination on the part of both Business 
Management and Technical Management when addressing this problem.
3. The main reason for software engineering failures is very bright 
technical people being poorly led by managers who secretly despise them, and 
have little or no understanding of what they do/need. (Point being: It isn't 
necessarily about Methodology...)
4. It IS possible to formulate a General Solution to commercial software 
engineering, that will solve more than 80% of the problems projects 
encounter. (However, doing so requires vision, imagination, and acceptance 
of change which most organisations are not capable of, or simply don't 
have.) This "general solution" is possible because, at least in the domain 
of commercial software solution engineering, there are the same (or very 
similar) "general problems" that manifest thermselves on every project, 
despite the fact that EVERY Management team believes THEY are unique and 
THEIR business is completely different from everyone else's. I think this 
myopia occurs because they are not capable of the pattern recognition that 
their tech staff do instinctively.

I am postulating a completely different approach, but I don't want to spoil 
it by pre-announcing it here. I WILL say that it includes the best points of 
several currently successful methodologies, along with some quite innovative 
ideas, based on my own experience and what I've found to work. I can also 
say that it is as far divorced from Waterfall as it is possible to get :-)

Amazingly, I have a track record of 20 years in PM without a failure (1 
project was not completed due to international corporate politics, over 
which I had no control), yet I have NEVER implemented (completely) the 
standard approach required on any particular site. Had I done so, the 
project would have failed.:-)

I believe the factors required for successful implementation are not easily 
identifiable or quantifiable and I address this in the book. Certainly some 
of them cannot be taught, but must be learned by observation and experience. 
It IS possible to raise awareness of them and suggest some approaches...


>
> Those interested in exploring this aspect independently of <CLC and
…[17 more quoted lines elided]…
> Any takers?

Not at this stage, Ken. I believe it will be too dry and Academic to 
interest me, and I can't/won't contribute to a pissing contest about 
methodologies, none of which I believe to be perfect... :-)

Nevertheless, I wish you luck with it :-)

Pete.
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-23T13:35:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fn7fqf$dme$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net>`

```
In article <5vns9hF1ns38fU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>This "general solution" is possible because, at least in the domain 
>of commercial software solution engineering, there are the same (or very 
…[4 more quoted lines elided]…
>their tech staff do instinctively.

Mr Dashwood, I'm not sure about pattern recognition and such... but I've 
read in a few texts that it is a very ancient and human phenomenom to 
consider one's Place and one's People to be special and superior to 
everything else; the (that-which-caused-creation) made the Human Beings 
and their Land of which We are part, etc.

Given that as an almost species-level behavior the diffident sniff and 
'NIH' (Not Invented Here) dismissal aimed at a new idea or process 
seems... downright Human, it does.

DD
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-23T09:18:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net>`

```
On Jan 22, 10:57 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
>
> Not at this stage, Ken. I believe it will be too dry and Academic to
…[5 more quoted lines elided]…
> Pete.

Uhh, can you get me a pre-publication copy of your book? :-)


Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-01-23T19:37:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13pfndl35odtl3f@corp.supernews.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com>`

```

<klshafer@att.net> wrote in message 
news:5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com...
On Jan 22, 10:57 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
>
> Not at this stage, Ken. I believe it will be too dry and Academic to
…[5 more quoted lines elided]…
> Pete.

Uhh, can you get me a pre-publication copy of your book? :-)


Ken

See: www.amazon.com/HowToBedWomenAll OverTheWorld
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-24T21:06:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vqv7cF1nc1snU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com...
On Jan 22, 10:57 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
>
> Not at this stage, Ken. I believe it will be too dry and Academic to
…[5 more quoted lines elided]…
> Pete.

>Uhh, can you get me a pre-publication copy of your book? :-)

Sure. Can you get me the cover price :-)?

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-24T10:07:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<17da85f2-7c47-4ecd-b5cf-07f25f6cbbd8@j78g2000hsd.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com> <5vqv7cF1nc1snU1@mid.individual.net>`

```
On Jan 24, 3:06 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
…[4 more quoted lines elided]…
> Pete.

Does your bank accept cheques in $USD? Or is it better to send
International Money Order. Kindly solicit me at klshafer -at- att.net
and let us see what we can do.

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-24T19:07:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnanm3$4u4$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com> <5vqv7cF1nc1snU1@mid.individual.net> <17da85f2-7c47-4ecd-b5cf-07f25f6cbbd8@j78g2000hsd.googlegroups.com>`

```
In article <17da85f2-7c47-4ecd-b5cf-07f25f6cbbd8@j78g2000hsd.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jan 24, 3:06�am, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
>Does your bank accept cheques in $USD?

Perhaps not... but maybe his banque accepts checks.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-25T12:28:55+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vsl9pF1o367gU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <5fc209c8-8bc2-483f-9e81-d8818fe51ab1@c23g2000hsa.googlegroups.com> <5vqv7cF1nc1snU1@mid.individual.net> <17da85f2-7c47-4ecd-b5cf-07f25f6cbbd8@j78g2000hsd.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:17da85f2-7c47-4ecd-b5cf-07f25f6cbbd8@j78g2000hsd.googlegroups.com...
On Jan 24, 3:06 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> <klsha...@att.net> wrote in message
>
…[4 more quoted lines elided]…
> Pete.

Does your bank accept cheques in $USD? Or is it better to send
International Money Order. Kindly solicit me at klshafer -at- att.net
and let us see what we can do.

[Pete:]

The book is currently 75% written and I intend to finish it before end of 
April this year. It will be POD published, as I have a number of writers 
here who also want to get their books on the Net, and I will set up a Web 
site that they can use too. This means you will be able to order it and pay 
for it on-line, and receive it to your postal address within 7 days.

I don't expect people to buy a pig-in-a-poke, and excerpts of it will be 
made available when it is ready for publication.

Thanks for your support, Ken. (I'll organise a signed copy for you... :-))

Pete.
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-01-23T17:39:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hfQlj.10319$M24.5411@newsfe17.lga>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net>`

```

Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
news:5vns9hF1ns38fU1@mid.individual.net...
> I believe that any attempt at problem solution that is driven from a
> Language perspective will not be optimum, so looking for approaches taken
…[5 more quoted lines elided]…
>

If by this you mean that selecting the language first is a non-starter -
then you're absolutely right.  But if you mean that the language to be used
is of no consequence, then I venture to disagree.  Obvious examples: report
writers (including the much maligned RPG); FORTRAN in its place; or
assemblers for interacting directly with the hardware - shouldn't be a
priori ruled out.

It'll be interesting to see your book.  Something written by an experienced
practitioner as opposed to a theorist (who quite often has an axe to grind)
should be a treat.

PL
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-23T20:26:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lktfp31najs2v8eghvupu102v9j3b447n4@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <hfQlj.10319$M24.5411@newsfe17.lga>`

```
On Wed, 23 Jan 2008 17:39:23 -0600, "tlmfru" <lacey@mts.net> wrote:

>
>Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
…[15 more quoted lines elided]…
>priori ruled out.

Hey, crank up the Wayback Machine. How about IBM 650 SOAP (not to be confused with Simple
Object Access Protocol, this SOAP is about optimized drum storage)?
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-01-23T23:17:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zcVlj.20759$E01.10135@newsfe22.lga>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <hfQlj.10319$M24.5411@newsfe17.lga> <lktfp31najs2v8eghvupu102v9j3b447n4@4ax.com>`

```

Robert <no@e.mail> wrote in message
news:lktfp31najs2v8eghvupu102v9j3b447n4@4ax.com...
>
> Hey, crank up the Wayback Machine. How about IBM 650 SOAP (not to be
confused with Simple
> Object Access Protocol, this SOAP is about optimized drum storage)?

What new-fangled nonsense is this?  Don't you know that mercury delay lines
haven't reached their full potential yet???
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-24T21:24:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vr09oF1mjfkqU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <hfQlj.10319$M24.5411@newsfe17.lga>`

```


"tlmfru" <lacey@mts.net> wrote in message 
news:hfQlj.10319$M24.5411@newsfe17.lga...
>
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
…[14 more quoted lines elided]…
> is of no consequence, then I venture to disagree.

I have consistently maintained the position, (both here in CLC, and in 
"real" life :-)), that the best tools for the job should be used. I 
suggested this position here more than 12 years ago when the generally 
accepted response was "Everything I want to do, I can do in COBOL". I 
suggested people might do well to expand their skill sets, learn Java for 
example, and get a few more tools in the box alongside COBOL. I took my own 
advice and learned Java (it helped my understanding of OO COBOL apart from 
anything else...), and later (just over a year ago) moved to C#. During my 
career I have programmed with Fortran, PL/I, Delphi (Pascal), Basic, VB and 
half a dozen Assembler Languages.

I would NEVER advocate tying development to a single language. Neither would 
I advocate just using ANY language for any particular development (...the 
Language IS of consequence...).

We got away with it for COBOL because it was a centralized platform, the 
procedural paradigm was adequate for most of what we wanted to do, and it 
was financially and technically intimidating to maintain costly skill bases 
for more than one language, where code was maintained line by line. 
Furthermore, COBOL is/was ideally suited to commercial batch processing, 
anyway.

Today the environment is richer, the Network is King and we NEED a richer 
toolset.

>Obvious examples: report
> writers (including the much maligned RPG); FORTRAN in its place; or
> assemblers for interacting directly with the hardware - shouldn't be a
> priori ruled out.
>

NOTHING should be a priori ruled out...:-)

> It'll be interesting to see your book.  Something written by an 
> experienced
> practitioner as opposed to a theorist (who quite often has an axe to 
> grind)
> should be a treat.

Thank you for the encouragement. I'll try not to disappoint... :-)

Pete.
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-23T19:20:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net>`

```
On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

><klshafer@att.net> wrote in message 
>news:519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com...
…[18 more quoted lines elided]…
>use.

The dozen methodologies I've used were agnostic to language. It didn't matter whether they
were heavyweight, such as CMM, or lightweight, such as Agile and XP. They treat the
programming act as a black box. They control the inputs -- requirements, planning and
design -- and the outputs -- testing, implementation, training. The black box they do not
care about, called 'build',  includes detailed design, coding, peer review, programming
standards, change control and unit testing. One gets the impression methodology designers
regard developers (geeks) as inherently uncontrollable. I knew one who said "it's like
trying to herd cats."

At one big company there was a checklist of the steps to get a change made, start to
finish. There were 150 steps on the liist, of which ONE was the programming act. It said
simply "Make the program change." There was SECOND checklist breaking that step out into
25 activities. That second list was maintained by technical management; it was not part of
the corporate methodology. It is what passes for methodology in shops that don't really
have a formal methodology, shops run by programmer types. 

Both lists aimed to avoid mistakes, increase productivity and make users happy. The
difference was the methodology developed by programmers (second list) revolved around
source code, whereas the first list regarded source code as almost irrelevant. The formal
methodology (first list) was used on projects that involved no software at all.

>1. No single one of the current methodologies works to complete satisfaction 
>(with the POSSIBLE exception of DSDM...) when applied by itself, alone.
…[5 more quoted lines elided]…
>necessarily about Methodology...)

"You must know there are two ways of contesting, the one by the law, the other by force;
the first method is proper to men, the second to beasts; but because the first is
frequently not sufficient, it is necessary to have recourse to the second. Therefore it is
necessary for a prince to understand how to avail himself of the beast and the man - just
one is not enough."

>4. It IS possible to formulate a General Solution to commercial software 
>engineering, that will solve more than 80% of the problems projects 
…[6 more quoted lines elided]…
>THEIR business is completely different from everyone else's.

This made me smile. A running joke between computer company technical consultants is the
introductory statement from Mr. Big,  "This company is unique." We knew it wasn't;  it was
like all the others. It was difficult to suppress laughter until we were out of his
office.

> I think this 
>myopia occurs because they are not capable of the pattern recognition that 
>their tech staff do instinctively.

I think it's ego. 'Only a genius like me can understand the complex problems we face.'

>I am postulating a completely different approach, but I don't want to spoil 
>it by pre-announcing it here. I WILL say that it includes the best points of 
>several currently successful methodologies, along with some quite innovative 
>ideas, based on my own experience and what I've found to work. I can also 
>say that it is as far divorced from Waterfall as it is possible to get :-)

So are ALL Agile methods .. they say. Close inspection reveals the only difference is
shorter iterations. They seduce programmers into thinking they can be cowboys again, while
management thinks it's getting more output for less money.

Machiavelli wrote the seminal work on software management. He said a prince who does not
raise the contempt of the nobles and keeps the people satisfied should have no fear of
conspirators. 

"If a prince seizes a state, all the required injuries should be inflicted at one stroke.
This way it is not necessary to every day be a little evil. Injuries should be inflicted
once, swiftly - so that it may be forgotten. A prince should however deliver frequent,
small benefits to his people so that its positive effects last longer."

>Amazingly, I have a track record of 20 years in PM without a failure (1 
>project was not completed due to international corporate politics, over 
>which I had no control), yet I have NEVER implemented (completely) the 
>standard approach required on any particular site. Had I done so, the 
>project would have failed.:-)

I don't understand this talk about cost overruns and missed deadlines. I've never worked
on a project that wasn't delivered on time .. using existing methodologies. 

>I believe the factors required for successful implementation are not easily 
>identifiable or quantifiable and I address this in the book. Certainly some 
>of them cannot be taught, but must be learned by observation and experience. 
>It IS possible to raise awareness of them and suggest some approaches...

"In order to imitate war victories of other illustrious men and avoid defeats, a prince
should study war histories to learn the causes of war victories and defeats."
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-01-23T20:28:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13pfqdfqomlvp04@corp.supernews.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com...
> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[161 more quoted lines elided]…
>

In my early days as a progrmmer a frequent project was: make a listing of 
this tray of cards for the user

The first step was to prepare a pert chart.  I usually listed the cards 
first, gave them to the user and drew the chart later.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-23T18:34:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ecae817-8dd9-4a00-b792-f5ff511f002a@e6g2000prf.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>`

```
On Jan 23, 8:20 pm, Robert <n...@e.mail> wrote:
> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
>
> I don't understand this talk about cost overruns and missed deadlines. I've never worked
> on a project that wasn't delivered on time .. using existing methodologies.

I am not being deliberately *cheeky* here, but could you cite me some
of those "existing" methodologies and the general application domain
(insurance, process control, government, etc.) that the project was
on? This is the real *empirical* heart-of-the-matter I am trying to
touch. And to point out the-not-obvious-to-others-lie-of "the
traditional methods never work." Or maybe the existing ones you are
referring to are Agile-OO?

>"If a prince seizes a state, all the required injuries should be inflicted at one stroke.
>This way it is not necessary to every day be a little evil. Injuries should be inflicted
>once, swiftly - so that it may be forgotten. A prince should however deliver frequent,
>small benefits to his people so that its positive effects last longer."

I have quietly fed up the rumor-chain, more than once to a management
clique, that it is far, far better to "cut once, cut deep, cut to the
bone", and then *immediately* reassure everyone left that they are
*safe* (well, as safe as any one can be nowadays.) There is nothing
more destructive of morale and deleterious to a project than the drip,
drip, drip of attrition and going to work every day wondering, "Am I
next?" That this is so self-evident and yet so often ignored always
amazes me.

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-23T21:41:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dl0gp39opmlhg9gtl1vbc924phhmv2tkt2@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <5ecae817-8dd9-4a00-b792-f5ff511f002a@e6g2000prf.googlegroups.com>`

```
On Wed, 23 Jan 2008 18:34:15 -0800 (PST), "klshafer@att.net" <klshafer@att.net> wrote:

>On Jan 23, 8:20ï¿½pm, Robert <n...@e.mail> wrote:
>> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
…[11 more quoted lines elided]…
>referring to are Agile-OO?

All were CMM-3 or similar, none OO. The one I'm on now is CMM trying to be lightweight
with two month iterations; most were six month.  All were very large companies or
government agencies. 

Retail, Y2K fix on 100 very large assembly language programs, used interns to document per
Keane methodology

Insurance, enhancements, first project on CMM-3

Government Student Loan, enhancements, EDS 

Government Child Welfare, enhancements, Accenture

Pharmaceutical discounts and rebates, rehost from AS/400 to Unix, CMM-3

Pharmaceutical charge clearinghouse, enhacements,  CMM - one month iterations

Distribution, convert screens from text to GUI, CMM

Retail, add make for new platforms and test 500 programs, home-grown Wal-Mart

Soft drink, convert billing system to SAP, CMM (IBM)

Telephone, enhance billing for major acquisition, CMM - two month iterations
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-24T21:51:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vr1s8F1np3okU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <5ecae817-8dd9-4a00-b792-f5ff511f002a@e6g2000prf.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:5ecae817-8dd9-4a00-b792-f5ff511f002a@e6g2000prf.googlegroups.com...
On Jan 23, 8:20 pm, Robert <n...@e.mail> wrote:
> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" 
> <dashw...@removethis.enternet.co.nz>
…[5 more quoted lines elided]…
> methodologies.

I am not being deliberately *cheeky* here, but could you cite me some
of those "existing" methodologies and the general application domain
(insurance, process control, government, etc.) that the project was
on? This is the real *empirical* heart-of-the-matter I am trying to
touch. And to point out the-not-obvious-to-others-lie-of "the
traditional methods never work." Or maybe the existing ones you are
referring to are Agile-OO?

>"If a prince seizes a state, all the required injuries should be inflicted 
>at one stroke.
…[4 more quoted lines elided]…
>small benefits to his people so that its positive effects last longer."

I have quietly fed up the rumor-chain, more than once to a management
clique, that it is far, far better to "cut once, cut deep, cut to the
bone", and then *immediately* reassure everyone left that they are
*safe* (well, as safe as any one can be nowadays.) There is nothing
more destructive of morale and deleterious to a project than the drip,
drip, drip of attrition and going to work every day wondering, "Am I
next?" That this is so self-evident and yet so often ignored always
amazes me.

(Your post, like Alistair's, seems to be missing a chevron level when 
replied to, so I'll prefix my comments with...[Pete:])

[Pete:]

Nobody should have to work bearing this particular fardel.

Contractors don't (and, if they do, they shouldn't be contracting...)

The only security anybody has is how useful they are to have around. Knowing 
you can go down the road and get another job goes a long way to building 
confidence and letting you focus on the job in hand without wondering or 
fearing whether you are next for the chop.

How do you get to be "useful to have around"?  Expand your skill set, 
educate yourself, and delight in what you do.

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-24T11:11:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fn9rp0$1qn$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <5ecae817-8dd9-4a00-b792-f5ff511f002a@e6g2000prf.googlegroups.com>`

```
In article <5ecae817-8dd9-4a00-b792-f5ff511f002a@e6g2000prf.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:

[snip]

>There is nothing
>more destructive of morale and deleterious to a project than the drip,
>drip, drip of attrition and going to work every day wondering, "Am I
>next?"

I recall seeing an advertising-poster in Grand Central Station shortly 
after the Crash of 1987 - a time which caused, I believe, a fundamental 
change in the American Business Model - which showed a picture of a Young 
Business Type sitting in the back seat of a town-car/limousine staring 
blankly out a rain-spattered window.  The copy read something like:

'Which is worse... being told Friday not to come back Monday or being told 
Monday you have to take up the slack?'

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-24T21:38:31+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vr145F1ns614U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com...
> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[59 more quoted lines elided]…
> all.

I can relate to this and have been in companies where it was certainly the 
case. Your analysis of it is perceptive.

>
>>1. No single one of the current methodologies works to complete 
…[19 more quoted lines elided]…
> one is not enough."

Law and force are not the ONLY two ways... there are others.
>
>>4. It IS possible to formulate a General Solution to commercial software
…[62 more quoted lines elided]…
> methodologies.

Then you have done well, Robert. Most Project Managers cannot claim this. Of 
course, it is easy to deliver projects on time if the deadlines are extended 
:-) (I'm not suggesting you do that...:-))  Timeboxed projects CANNOT slip; 
I like timeboxing.
>
>>I believe the factors required for successful implementation are not 
…[11 more quoted lines elided]…
>

Given your partiality to Machiavelli, I'm sure you'll not be surprised that 
Politics and Manipulation can both be added to Law and Force as useful 
methods for contesting... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-24T11:05:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fn9ree$b3c$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>`

```
In article <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>,
Robert  <no@e.mail> wrote:
>On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
>wrote:

[snip]

>Both lists aimed to avoid mistakes, increase productivity and make users happy. The
>difference was the methodology developed by programmers (second list) revolved around
>source code, whereas the first list regarded source code as almost irrelevant. The formal
>methodology (first list) was used on projects that involved no software at all.

It sounds like a good Corporate 'one size fits all' mentality, in that 
software is considered to be just like any other tool or process.  The 
folks in charge of software developed their own steps to deal with what 
they find to be different about installing a chunk o' code to, say, move 
money in a different direction... as opposed to the needs of buying a 
truck to move money in a different direction.

[snip]

>>This "general solution" is possible because, at least in the domain 
>>of commercial software solution engineering, there are the same (or very 
…[6 more quoted lines elided]…
>like all the others.

Grabbing but one example of the several times I've expressed the 
sentiment, 
<http://groups.google.com/group/comp.lang.cobol/msg/a720b9f80ca9e217?dmode=source>

--begin quoted text:

(Business Zen:  If, in all places, 'Things Are Different' then, in all 
places, things are the same.)

--end quoted text

[snip]

>"In order to imitate war victories of other illustrious men and avoid defeats, a prince
>should study war histories to learn the causes of war victories and defeats."

'The Great Prince issues commands, founds states, vests families with 
fiefs.  Inferior people should not be employed' - I Ching

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-25T18:47:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kmtkp3526tjrgiujugrgjhvrass86k33gj@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <fn9ree$b3c$1@reader2.panix.com>`

```
On Thu, 24 Jan 2008 11:05:50 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>,
>Robert  <no@e.mail> wrote:
…[15 more quoted lines elided]…
>truck to move money in a different direction.

I've noticed that corporate level systems generalists all have shaved heads and speak in
masculine tones like G. Gordon Liddy, decorate their cubicles with pictures of high risk
avocations like martial arts, motorcycling, skydving and rock climbing. They're freestyle
cowboys. Perhaps they impose discipline on everyone else to eliminate competition?

Havng worked in high risk occupatipons of USMC recon and options trading, I know there's a
huge attitude difference between professionals and amateurs like these guys. Professionals
are actually averse to risk, doing everythig they can to avoid danger, and are
unemotional. Amateurs, by contrast, are adrenaline and power junkies. They're always
running on either fear or greed. They're destined to crash and burn, the only unknown is
how long it will take. Most wives and families figure that out and bail. I feel sorry for
the ones who didn't.

>--begin quoted text:
>
…[3 more quoted lines elided]…
>--end quoted text

You're unique, just like everyone else.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-26T01:03:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fne0tl$8cf$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <fn9ree$b3c$1@reader2.panix.com> <kmtkp3526tjrgiujugrgjhvrass86k33gj@4ax.com>`

```
In article <kmtkp3526tjrgiujugrgjhvrass86k33gj@4ax.com>,
Robert  <no@e.mail> wrote:
>On Thu, 24 Jan 2008 11:05:50 +0000 (UTC), docdwarf@panix.com () wrote:

[snip]

>>It sounds like a good Corporate 'one size fits all' mentality, in that 
>>software is considered to be just like any other tool or process.  The 
…[9 more quoted lines elided]…
>avocations like martial arts, motorcycling, skydving and rock climbing.

I do not believe I have ever met anyone labelled as a 'corporate level 
systems generalist'... and that is probably a Good Thing, as I could see 
myself bursting into laughter and/or assuming a tone of solicitous 
sympathy.

[snip]

>Professionals
>are actually averse to risk, doing everythig they can to avoid danger, and are
>unemotional.

As those who have flown airplanes have told me: 'There are old pilots and 
there are bold pilots but there are no old, bold pilots.'

[snip]

>>--begin quoted text:
>>
…[5 more quoted lines elided]…
>You're unique, just like everyone else.

I think I've heard that from others, too.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-25T19:13:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s52lp3pl6gt1j96qbtb66bd0pbouer6r2j@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <fn9ree$b3c$1@reader2.panix.com> <kmtkp3526tjrgiujugrgjhvrass86k33gj@4ax.com> <fne0tl$8cf$1@reader2.panix.com>`

```
On Sat, 26 Jan 2008 01:03:49 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <kmtkp3526tjrgiujugrgjhvrass86k33gj@4ax.com>,
>Robert  <no@e.mail> wrote:
…[20 more quoted lines elided]…
>sympathy.

DBAs and system administrators warm the bench of second string wannabes.

>>Professionals
>>are actually averse to risk, doing everythig they can to avoid danger, and are
…[3 more quoted lines elided]…
>there are bold pilots but there are no old, bold pilots.'

Yep, that captures the essence of it.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-26T01:20:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fne1s1$hi7$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <kmtkp3526tjrgiujugrgjhvrass86k33gj@4ax.com> <fne0tl$8cf$1@reader2.panix.com> <s52lp3pl6gt1j96qbtb66bd0pbouer6r2j@4ax.com>`

```
In article <s52lp3pl6gt1j96qbtb66bd0pbouer6r2j@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 26 Jan 2008 01:03:49 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[24 more quoted lines elided]…
>DBAs and system administrators warm the bench of second string wannabes.

Is 'wannabe' some kind of rare wood... or one of the new plastics they 
make benches out of?  I've heard of benches made of both.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-25T20:40:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n97lp3lkoeucmru577inip2dme6m13ed3q@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <kmtkp3526tjrgiujugrgjhvrass86k33gj@4ax.com> <fne0tl$8cf$1@reader2.panix.com> <s52lp3pl6gt1j96qbtb66bd0pbouer6r2j@4ax.com> <fne1s1$hi7$1@reader2.panix.com>`

```
On Sat, 26 Jan 2008 01:20:01 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <s52lp3pl6gt1j96qbtb66bd0pbouer6r2j@4ax.com>,
>Robert  <no@e.mail> wrote:
…[29 more quoted lines elided]…
>make benches out of?  I've heard of benches made of both.

It's hard to believe you get PAID to live in a world of 1970s technology and Elizatethian
prose.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-26T12:34:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnf9bt$9hr$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <s52lp3pl6gt1j96qbtb66bd0pbouer6r2j@4ax.com> <fne1s1$hi7$1@reader2.panix.com> <n97lp3lkoeucmru577inip2dme6m13ed3q@4ax.com>`

```
In article <n97lp3lkoeucmru577inip2dme6m13ed3q@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 26 Jan 2008 01:20:01 +0000 (UTC), docdwarf@panix.com () wrote:
>
>>In article <s52lp3pl6gt1j96qbtb66bd0pbouer6r2j@4ax.com>,
>>Robert  <no@e.mail> wrote:

[snip]

>>>DBAs and system administrators warm the bench of second string wannabes.
>>
…[4 more quoted lines elided]…
>and Elizatethian prose. 

What I get paid for, Mr Wagner, seems to be doing what makes the person 
who signs checks for the system on which I work smile; the world I live in 
is, I hope, a bit more complex and amusing than that.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-24T10:04:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>`

```
On Jan 23, 8:20 pm, Robert <n...@e.mail> wrote:
> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
>

Robert,

I found your list of methods/applications of interest and significant
value to me (empirically speaking, :-) ). I am gratified. Thank you.


> So are ALL Agile methods .. they say. Close inspection reveals the only difference is
> shorter iterations.

I suppose that *differences* make for interesting reading, and, as
they say, for generating much heat but little light, but for me, I
find "what is common" is more interesting. Maybe because I feel such a
need to just "get along." :-)

To wit -

- Is not Agile Continuous Integration very similar to what we used to
do as Top-Down development, with stubs?
- Isn't TDD (Test Driven Development) very similar to Unit Testing
with Top-Down Development?,
- Isn't Agile "customer on site" very similar to the Analyst part of
the Analyst/Programmer (when there were such people, before they were
overcome with rote coders) walking down the Hall to see his User?
- Didn't the original Royce Waterfall article show feedback loops, not
only between adjoining steps in the SDLC, but jumping over steps, and
are not _these_ the Agile Iterations? (as in the Barry Boehm spiral
method.) (I somehow found the Royce Waterfall .pdf on the Web; if I
can find it again, and be convinced it is quasi-public-domain now, I
will post the link.)

I don't have the link, but I know I read it somewhere on the Web (so
it *must* be true :-) ), that much of Agile, and maybe the entirety of
the Agile Manifesto was in essence a _marketing move_. Let us not
begrudge them their success, to the extent that they are successful.
But neither let us lower our heads, brow beaten, through self-
submission to the thought that "They have discovered something
Entirely New, which we Know Not."

Be not mistaken now, we, and by "we" I mean those such as *I*, neo-
Classicists, Traditionalists, Pragmatic Practitioners, in a Word, we
*Journeymen*, who do not deign to call ourselves Methodology Masters,
all owe the Agilists a great debt of gratitude.

It is they (the Agilists) who have brought "refactoring" into the
popular venacular, management-wise, so that "rework" is now not always
a "dirty word". And it is they who have, more successfully than
others, driven the stake into the ground regarding what I call
Indivisibility (of effort), which contends that is very, very
difficult to completely separate analysis, design, coding, and testing
across a multitude of individuals, no matter _how_ good the
_documentation artifacts_ are.
Once upon a time, that was the rationale for "Analyst/Programmer", was
it not?.

There once was a time, and maybe it was Our Time, and yes, maybe it is
*gone* now, that all of this was Common Knowledge.

But presently, what others might see as Nouveau Secrets are really
Ancient Wisdom, mostly forgotten.

As long as there are Journeymen and Apprentices, let it be passed
down.

How could we expect it to be otherwise?

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-24T11:22:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4jlhp354954k638l7n52i00upil1dpcgoc@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com>`

```
On Thu, 24 Jan 2008 10:04:37 -0800 (PST), "klshafer@att.net"
<klshafer@att.net> wrote:

>*Journeymen*, who do not deign to call ourselves Methodology Masters,
>all owe the Agilists a great debt of gratitude.

...

>There once was a time, and maybe it was Our Time, and yes, maybe it is
>*gone* now, that all of this was Common Knowledge.
>
>But presently, what others might see as Nouveau Secrets are really
>Ancient Wisdom, mostly forgotten.


Nice post.

I am reminded of a management seminar where the lecturer stated that
his teachings weren't the most important element of the seminar.   The
most important part was the reminder that it can be good to sit back
and think about your processes - and that management was willing to
spend time and money to remind us of that.    He hoped that his
insights would help people do their common sense - but the important
part wasn't learning arcane secrets - it was to be reminded to make
the analysis and work on improvement.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-25T12:17:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vskknF1mlb3iU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com...
On Jan 23, 8:20 pm, Robert <n...@e.mail> wrote:
> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" 
> <dashw...@removethis.enternet.co.nz>
> wrote:
>

Robert,

I found your list of methods/applications of interest and significant
value to me (empirically speaking, :-) ). I am gratified. Thank you.


> So are ALL Agile methods .. they say. Close inspection reveals the only 
> difference is
> shorter iterations.

I suppose that *differences* make for interesting reading, and, as
they say, for generating much heat but little light, but for me, I
find "what is common" is more interesting. Maybe because I feel such a
need to just "get along." :-)

To wit -

- Is not Agile Continuous Integration very similar to what we used to
do as Top-Down development, with stubs?
- Isn't TDD (Test Driven Development) very similar to Unit Testing
with Top-Down Development?,
- Isn't Agile "customer on site" very similar to the Analyst part of
the Analyst/Programmer (when there were such people, before they were
overcome with rote coders) walking down the Hall to see his User?
- Didn't the original Royce Waterfall article show feedback loops, not
only between adjoining steps in the SDLC, but jumping over steps, and
are not _these_ the Agile Iterations? (as in the Barry Boehm spiral
method.) (I somehow found the Royce Waterfall .pdf on the Web; if I
can find it again, and be convinced it is quasi-public-domain now, I
will post the link.)

I don't have the link, but I know I read it somewhere on the Web (so
it *must* be true :-) ), that much of Agile, and maybe the entirety of
the Agile Manifesto was in essence a _marketing move_. Let us not
begrudge them their success, to the extent that they are successful.
But neither let us lower our heads, brow beaten, through self-
submission to the thought that "They have discovered something
Entirely New, which we Know Not."

Be not mistaken now, we, and by "we" I mean those such as *I*, neo-
Classicists, Traditionalists, Pragmatic Practitioners, in a Word, we
*Journeymen*, who do not deign to call ourselves Methodology Masters,
all owe the Agilists a great debt of gratitude.

It is they (the Agilists) who have brought "refactoring" into the
popular venacular, management-wise, so that "rework" is now not always
a "dirty word". And it is they who have, more successfully than
others, driven the stake into the ground regarding what I call
Indivisibility (of effort), which contends that is very, very
difficult to completely separate analysis, design, coding, and testing
across a multitude of individuals, no matter _how_ good the
_documentation artifacts_ are.
Once upon a time, that was the rationale for "Analyst/Programmer", was
it not?.

There once was a time, and maybe it was Our Time, and yes, maybe it is
*gone* now, that all of this was Common Knowledge.

But presently, what others might see as Nouveau Secrets are really
Ancient Wisdom, mostly forgotten.

As long as there are Journeymen and Apprentices, let it be passed
down.

How could we expect it to be otherwise?

Ken

[Pete:]

An excellent post, Ken. There is much wisdom in what you say above.

Certainly, the Ancient Wisdom has been re-invented many times, and 
re-marketed, and it is certainly true that unless Management are provided 
with simple (usually one word) hooks like "refactoring", then the REAL work 
is made much more difficult for everybody.

They have neither time nor inclination to understand what is actually going 
on in Development and this creates severe anxiety (especially when they see 
the cost of it...) If they can be given something that they "know" is right 
there and up with current "Best Practices" (don'tcha just LOVE "Best 
Practices"?...especially when it is used to cover some of the most senseless 
and stupid decisions imaginable :-)), then it is like a cuddle blanket and 
has a calming effect.

I've had a lot of contact with Managers over the years, including Doc's 
"Corner Office Idiots" (COI). In general, Senior management (say, Board 
level) are pretty astute and recognise that they don't know about IT. Their 
approach is to buy expertise and get the best they can. It is usally the 
middle managers and COIs who have SOME knowledge, that lose sight of the 
real agenda and instead, look for the line of least resistance and short 
term solutions. These same guys are often much more concerned about 
building/protecting their own little empires than they are about providing 
service to the Business. That is why there are so many IT departments with 
incoherent strategies, risky tactical solutions, and Business departments 
(Clients of IT) that think IT stinks...

A fundamental for success is Management buy-in. That is NOT COI buy-in 
(although that is very useful, too...) it is SENIOR management buy-in. Of 
course, to get this you have to establish credibility, and I have gone to 
extreme lengths (and taken risks that made me shudder in retrospect :-)) on 
many occasions to get it.

IT, especially when change is being introduced, needs the support of Senior 
management.

As a consultant being brought in to manage something, I know I will 
encounter animosity from the middle management. I deal with it in the 
following ways:

1. Sit down with the COIs and assure them I am not after their jobs or 
trying to make them look bad. Any and all "success" will be attributed to 
them (and their teams, of course). (See post in response to Doc, 
elsewhere...)

2. Make sure I have direct access to Senior Management and have primed them 
with what I intend to do and the likely problems that will be encountered. 
When issues arise with COIs, we negotiate and look for compromise. If none 
is forthcoming, then it gets escalated to Board level. (I have only had to 
do this very rarely, and it is always with the COI who is a control freak. 
The kind who uses standards to inhibit and stifle, rather than to support 
and ensure consistency. Unimaginative, incapable of thinking outside the 
box, or even considering any solution that might violate one line of 
"Standard Procedure". The kind who really should be a guard in a prison camp 
(nobody leaves the site without his permission... and so on...) These guys 
are walking examples of the Peter Principle...)

Once we have this nonsense sorted, I can sit down with the team and we can 
get on with the REAL work.

Tech teams seem to enjoy working with me... :-) (I certainly enjoy working 
with bright young people...)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-25T06:43:34-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bde70ea5-7ba0-44f2-b903-0cc794a6aeb7@q21g2000hsa.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <5vskknF1mlb3iU1@mid.individual.net>`

```
On 24 Jan, 23:17, "Pete Dashwood"
> Tech teams seem to enjoy working with me... :-) (I certainly enjoy working
> with bright young people...)
>

Many years ago I said to a senior manager that the user was happy with
the system because he had never complained about it. I was wrong (I
was not aware of the complaints that he had made). Just because people
wear happy smiley faces does not necessarily mean that they enjoyed
working with you. It may just mean that they are stoned. And I have
been known to attend leaving dos just to ensure that we've finally got
rid of the individual concerned.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-25T16:03:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnd192$a4v$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <5vskknF1mlb3iU1@mid.individual.net> <bde70ea5-7ba0-44f2-b903-0cc794a6aeb7@q21g2000hsa.googlegroups.com>`

```
In article <bde70ea5-7ba0-44f2-b903-0cc794a6aeb7@q21g2000hsa.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 24 Jan, 23:17, "Pete Dashwood"
>> Tech teams seem to enjoy working with me... :-) (I certainly enjoy working
…[5 more quoted lines elided]…
>was not aware of the complaints that he had made).

Well, now that you mention it... years on back I had a contract at a place 
where the consultants were used as pawns in Corner-Office Wars.  Given a 
simple rectangular arrangement it went something like this:

Corner-Office Idiot A comes out of the top-left office, looks around and 
snarls 'Bah!  Not enough getting done here, bring in some consultants!'

They'd then bring in a raft of consultants/contractors/hired guns, between 
twelve and twenty... and folks would get ID badges and logons, find out 
where the source libraries were, start to get a handle on things and begin 
to do some work...

... and then Corner-Office Idiot B would come out of the top-right office, 
look around and snarl 'Bah!  Too many consultants here, costs too much 
money... get rid of them!'

... and folks would pack up and go, and work would pile up and deadlines 
start to slip... and then Corner-Office Idiot C would come out of the 
bottom-right office and snarl 'Bah!  Not enough getting done here, bring 
in some consultants!'...

... and another dozen or so folks would be brought in, get ID badges, 
logons, etc.

Anyhow... I'd been there for a while, a Corner-Office Idiot came out and 
said 'Too many consultants!' and a bunch of folks (I was not included) 
were given two weeks' notice.

Being consultants/contractors/hired guns they began to behave as Dead Men 
do; they hit the telephones and began calling up friends, agencies, pimps, 
telephone-numbers they saw on restroom walls... and began looking for new 
contracts.  Listening to folks the next desk/cubicle over trying to wangle 
new work did not have a good effect on morale.

So... the Corner-Office Idiot has a brilliant ides: Consultants Don't Need 
Telephones.  (this was in the Oldene Dayse, before cellular service)  We 
all came in one day, those leaving and those staying, and saw our desks 
telephonically denuded... and the problem was solved, right?

Well... maybe *that* problem was solved... but others generated.  Later 
that day the Idiot went over to the Lead Consultant's desk - the Lead, 
like me'n another fellow or two, were spared during the firing - and asked 
'Well, what about those ABEND problems they've been having in the Prod 
online system?'

The Lead looked over to the naked, dusty spot where the telephone had been 
and said 'Oh, I haven't heard anything about those all morning'...

... and the Idiot brusquely said 'Very good, very good... no news is good 
news' and strode off.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T11:47:00+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vv774F1oahl1U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <5vskknF1mlb3iU1@mid.individual.net> <bde70ea5-7ba0-44f2-b903-0cc794a6aeb7@q21g2000hsa.googlegroups.com> <fnd192$a4v$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fnd192$a4v$1@reader2.panix.com...
> In article 
> <bde70ea5-7ba0-44f2-b903-0cc794a6aeb7@q21g2000hsa.googlegroups.com>,
…[63 more quoted lines elided]…
>
ROFL!

All you can do is laugh... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T11:44:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vv72hF1nvrroU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <5vskknF1mlb3iU1@mid.individual.net> <bde70ea5-7ba0-44f2-b903-0cc794a6aeb7@q21g2000hsa.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:bde70ea5-7ba0-44f2-b903-0cc794a6aeb7@q21g2000hsa.googlegroups.com...
> On 24 Jan, 23:17, "Pete Dashwood"
>> Tech teams seem to enjoy working with me... :-) (I certainly enjoy 
…[8 more quoted lines elided]…
> working with you.

It can be taken as an indicator (provided you are working with decent honest 
people, of course).

For me, if they stay in touch for years, it is a pretty fair bet that they 
learned something form you, or at least had an enjoyable time.

I still get emails from people I worked with 25 years ago, and even have the 
odd unexpected visit, if they are passing through Tauranga.

<anecdote - skip this if you don't like stories>

A little while back I received a text from the liner QE2. A girl who I had 
worked with in London around 30 years ago, and received the odd email from 
over the years...Christmas, that sort of thing..., was on the ship in Fiji 
and had just found out they had been diverted to Mount Maunganui instead of 
a port in Northland. She said she'd be arriving in 3 days. Of course, the 
whole of Tauranga and the Mount turned out to watch the great ship negotiate 
the entrance to our harbour. It was quite spectacular.

I collected her from the dock and whisked her off to Rotorua for a Maori 
concert party and hangi, getting her back just within the 8 hours they were 
allocated.

It was kind of spooky to think we were writing COBOL all those years ago and 
now she is cruising on QE2 and living in Spain... (There IS money in IT... 
:-)).

</anecdote - skip this if you don't like stories>

I value these contacts very much, and am interested to hear when they get 
new jobs or head overseas for better opportunities.

(The Java team lead on my last Auckland project sent me an email recently, 
saying she is heading off to Melbourne to take up a better paid job with a 
larger company. I'm glad for her; she is one of the brightest programmers 
I've ever worked with, and a great Team Lead.)

>It may just mean that they are stoned. And I have
> been known to attend leaving dos just to ensure that we've finally got
> rid of the individual concerned.

And drink his/her booze... right? I can honestly say I onl;y ever did this 
once. I manager I had some major head-butts with had stated publicly that he 
would have me fired within 3 weeks. I was pleased to attend his leavig do, 
raise a glass to him, smile sweetly, and say:"I'm still here..." :-)

For the most part, on the rare occasions when I am glad to see someone go, I 
excuse myself from the leaving do.

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-24T21:47:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com>`

```
On Thu, 24 Jan 2008 10:04:37 -0800 (PST), "klshafer@att.net" <klshafer@att.net> wrote:

>On Jan 23, 8:20ï¿½pm, Robert <n...@e.mail> wrote:
>> On Wed, 23 Jan 2008 16:57:36 +1300, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
…[15 more quoted lines elided]…
>need to just "get along." :-)

Sounds like you have management potential. :)

>To wit -
>
…[3 more quoted lines elided]…
>with Top-Down Development?,

An 'old wine in new bottles' argument is unpersuasive because it makes the advocate sound
like a sore loser.

>- Isn't Agile "customer on site" very similar to the Analyst part of
>the Analyst/Programmer (when there were such people, before they were
>overcome with rote coders) walking down the Hall to see his User?

Usually not. Rarely can a  programmer detach himself to truly think like a user. 

I've learned from experience that knowing more then the user about his own technical
specialty, such as accounting, law and statistics, really pisses them off. :)

>- Didn't the original Royce Waterfall article show feedback loops, not
>only between adjoining steps in the SDLC, but jumping over steps, and
>are not _these_ the Agile Iterations? (as in the Barry Boehm spiral
>method.) 

Yes, it does. Royce warns against a monotonic ("waterfall") process here:

"... the implementation described above is risky and invites failure. The testing phase
which occurs at the end of the development cycle is the first event for which timing,
storage, input/output transfers, etc., are experienced as distinguished from analyzed.
These phenomena are not precisely analyzable. ...  Yet if these phenomena fail to satisfy
the various external constraints, then invariably a major redesign is required. A simple
octal patch or redo of some isolated code will not fix these kinds of difficulties. The
required design changes are likely to be so disruptive that the software requirements upon
which the design is based and which provides the rationale for everything are violated.
Either the requirements must be modified, or a substantial change in the design is
required. In effect the development process has returned to the origin and one can expect
up to a lO0-percent overrun in schedule and/or costs."

His argument is based on inadequate hardware being the greatest danger. The system is too
slow. That was widely believed in 1970, and I believe prematue optimization was the
greatest CAUSE of bad system design. I see it every day, 38 years later, on hardware that
runs a thousand times faster than computers did in 1970. The genesis of this attidude is
in the techie psyche, not the real world where users live.  

Thus, a development process that revolves around 'optimized code' is a non-starter. The
process SHOULD revolve around the user.

>(I somehow found the Royce Waterfall .pdf on the Web; if I
>can find it again, and be convinced it is quasi-public-domain now, I
>will post the link.)

Here's the link:
http://www.cs.umd.edu/class/spring2003/cmsc838p/Process/waterfall.pdf

>I don't have the link, but I know I read it somewhere on the Web (so
>it *must* be true :-) ), that much of Agile, and maybe the entirety of
…[9 more quoted lines elided]…
>all owe the Agilists a great debt of gratitude.

You are being sardonic.

>It is they (the Agilists) who have brought "refactoring" into the
>popular venacular, management-wise, so that "rework" is now not always
…[5 more quoted lines elided]…
>_documentation artifacts_ are.

Royce says divisibility is the acid test for adequate documentation. 

" Many parts of the test process are best handled by test specialists who did not
necessarily contribute to the original design. If it is argued that only the designer can
perform a thorough test because he understands the area he built, this is a sure sign of a
failure to document properly."

>Once upon a time, that was the rationale for "Analyst/Programmer", was
>it not?.

It's just job title inflation. In some shops, everyone has been promoted to Senior
Technical Analyst or Lead Technical Engineer; there aren't any inadjectivated Developers.
In at least one state, Wisconsin, real engineers sued to stop debasement of their
occupational title. 

>There once was a time, and maybe it was Our Time, and yes, maybe it is
>*gone* now, that all of this was Common Knowledge.
>
>But presently, what others might see as Nouveau Secrets are really
>Ancient Wisdom, mostly forgotten.

The evolution of methodologies is the confluence of two sets of cycles. The first is the
generational cycle brilliantly described by Strauss and Howe in their book Generations.
The second is the tug of war between users and management and techies. In both, attempts
to correct past deficiencies overshoot the mark and become candidates for correction
during the next iteration. The path is not as simple as a two-dimensional sine wave.
Because of multiple degrees of freedom (dimensions), there can be multiple stages before
the supercycle starts over. There are four stages in the Generations model: Hero,
Technocrat/Artist, Puritan/Yuppie and XGen/Punk (my terminology). A methodology that seems
right to one generational style will seem all wrong to its successor. For example, the
Artistic style that you seem to favor seems undisciplined to Yuppies, who don't trust
anyone to do things right, least of all themselves. That's how we got Waterfall, which
seems too rigidly structured to XGens, who just want to get the job done as quickly as
possible. That XGens also disdain beautiful code shows the cycles are not simple
oscillation. 

http://en.wikipedia.org/wiki/Generations_%28book%29
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-25T12:55:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fncm8p$fsr$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com>`

```
In article <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>Here's the link:
>http://www.cs.umd.edu/class/spring2003/cmsc838p/Process/waterfall.pdf

Waw haw haw haw... this guy's *serious*?  Give this a listen, from .pdf 
page 5 (showing book page 332):

--begin quoted text

Step 2: DOCUMENT THE DESIGN

     At this point it is appropriate to raise the issue of - 'how much 
documentation?'  My own view is 'quite a lot'; certainly more than most 
programmers, analysts or program designers are willing to do if left to 
their own devices.  The first rule of managing software development is 
ruthless enforcement of documentation requirements.

     Occaisionally I am called upon to review the progress of other 
software design efforts.  My first step is to investigate the state of 
documentation.  If the documentation is in serious default my first 
recommendation is simple.  Replace project management.  Stop all 
activities not related to documentation.  Bring the documentation up to 
acceptable standards.

--end quoted text

All righty, by a show of hands... has anyone ever seen anything like this 
happen?  

(My experience, of course, is with 'sick shops' so I haven't run across an 
instance of a single manager - let along an entire project's management - 
being replaced because documentation was not 'up to acceptable standards', 
even where 'acceptable' was construed as 'scribble something in cuneiform 
- Akkadian or Hittite, your choice - on a bit of bathroom-tissue'.)

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-01-25T11:28:40-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M%omj.6150$HL1.21@newsfe21.lga>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:fncm8p$fsr$1@reader2.panix.com...
> > Waw haw haw haw... this guy's *serious*?  Give this a listen, from .pdf
> page 5 (showing book page 332):
…[10 more quoted lines elided]…
>
<snip>

> --end quoted text
>
…[10 more quoted lines elided]…
>

I often hear the argument - from programmers mostly - "how can you write the
specs before you write the program?"  To me, that's most peculiar.  I answer
"how can you draw the blueprints before you build the house?".  Trouble is,
they don't get it.

Whether or not they commit anything to paper, every programmer - every good
one, anyway - has a pretty good idea of what the program has to do.  A great
number of the details will have to be filled in but the basic flow and the
functions that the program has to accomplish are clear or at least obvious.
(OO programmers take note: I'm not using "function" in the OO sense).  I
have found, and the people I've convinced have found, that if you take time
and scribble all these notions down, and go over them a few times with
different coloured pens (Yes!  You can't write or debug a program without a
red pen!) you will have resolved most of the issues and greatly eased the
actual coding.   Notes and corrections can be likewise scribbled in; once
the program is working the whole mass can be neatly reformatted into the
program specs.

(Please keep your scorn generators off.  I'm speaking about something that
works, can be proved to work, and is easy to do.  That I choose to do it
with pencil & paper is irrelevant.)

(The process that PD uses is similar in essence but far more controlled and
precise in practice).

Apart from what I was calling task guides in 1980 but which are now known as
use cases, this is the only form of documentation which is controversial.  I
can truthfully state that it's saved my bacon on any number of occasions.

To answer DD's question: no, I haven't seen this done, but there have been
times when I wished it had!  And I'd agree that conformance with
documentation standards is essential to keep the shop out of trouble.

PL
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-25T11:41:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3m9kp3p009h7s9ilmop0shrlu0cpuj5hha@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <M%omj.6150$HL1.21@newsfe21.lga>`

```
On Fri, 25 Jan 2008 11:28:40 -0600, "tlmfru" <lacey@mts.net> wrote:

>I often hear the argument - from programmers mostly - "how can you write the
>specs before you write the program?"  To me, that's most peculiar.  I answer
>"how can you draw the blueprints before you build the house?".  Trouble is,
>they don't get it.

I suspect they think your programming with specs is kind of like when
an American Football coach scripts out the first 15 plays.   "How can
he know what the situation will be?".
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 8)_

- **From:** rpl <plinnane3@yahoo.com.invalid>
- **Date:** 2008-01-25T14:06:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fndbvo$27j$1@registered.motzarella.org>`
- **In-Reply-To:** `<3m9kp3p009h7s9ilmop0shrlu0cpuj5hha@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <M%omj.6150$HL1.21@newsfe21.lga> <3m9kp3p009h7s9ilmop0shrlu0cpuj5hha@4ax.com>`

```
Howard Brazee wrote:
> On Fri, 25 Jan 2008 11:28:40 -0600, "tlmfru" <lacey@mts.net> wrote:
> 
…[8 more quoted lines elided]…
> 

Interesting analogy... so who is the "opposing team" ?...

I rather like the blueprints analogy; after a certain point of 
complexity/size you pretty well have to use them if completion and 
safety are your concern.


rpl
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 9)_

- **From:** tim Josling <tejgcc_nospam@westnet.com.au>
- **Date:** 2008-01-25T21:40:36
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13pklqk13dkipd9@corp.supernews.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <M%omj.6150$HL1.21@newsfe21.lga> <3m9kp3p009h7s9ilmop0shrlu0cpuj5hha@4ax.com> <fndbvo$27j$1@registered.motzarella.org>`

```
On Fri, 25 Jan 2008 14:06:58 -0500, rpl wrote:

> Howard Brazee wrote:
>> On Fri, 25 Jan 2008 11:28:40 -0600, "tlmfru" <lacey@mts.net> wrote:
…[18 more quoted lines elided]…
> rpl

The problem with this theory is that in fact, the programs *are* the
design. The computer - specifically the compiler and link-editor - then
turns the design into the product (the executable files).

This is why the waterfall method that is being pushed by some in this
thread is usually such an expensive failure. Waterfall is literally trying
to design the design before the design is done. If the "design" has all
the details needed to write the programs, then it may as well be the
programs.

Invariably after a waterfall project, large slabs of the documentation is
wrong, because the initial design didn't all work and had to be changed.

This also also why the "software factory" concept doesn't work. The
manufacturing of software is very easy. Just type in "make" or whatever.
Then copy the data to the CDs.

It's the design that's hard. This includes the programming.

And of course this assumes that the requirements are known in detail,
which is rarely if every true. How often does someone build exactly what
they were asked to build, only to find it is now what was actually wanted.

Read up about extreme programming or agile methods for more details.

Tim Josling
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 10)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-01-25T23:42:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pLzmj.10734$M24.1977@newsfe17.lga>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <M%omj.6150$HL1.21@newsfe21.lga> <3m9kp3p009h7s9ilmop0shrlu0cpuj5hha@4ax.com> <fndbvo$27j$1@registered.motzarella.org> <13pklqk13dkipd9@corp.supernews.com>`

```

tim Josling <tejgcc_nospam@westnet.com.au> wrote in message
news:13pklqk13dkipd9@corp.supernews.com...
> On Fri, 25 Jan 2008 14:06:58 -0500, rpl wrote:
>
…[3 more quoted lines elided]…
> >>> I often hear the argument - from programmers mostly - "how can you
write the
> >>> specs before you write the program?"  To me, that's most peculiar.  I
answer
> >>> "how can you draw the blueprints before you build the house?".
Trouble is,
> >>> they don't get it.
> >>
…[23 more quoted lines elided]…
>


No, no, Tim - at no point do I assert that the whole program must be
documented in complete detail before it's written.  I do say write
pseudo-code and mess around with it for a while before coding really starts.
The solider you have the program mentally modelled - backed up by your
collected thoughts in any form - the easier it will be to write the program
and the better its quality.

I'm in agreement that a great deal of programming is now - or should be
now - in a state of "current art" - that is, already published somewhere or
other.  To take a very simple example - it's doubtful if anybody, anywhere,
needs to write a balance-line file update program from scratch - it's been
done a few thousand times already.

PL
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-26T12:43:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnf9t9$lfd$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <fndbvo$27j$1@registered.motzarella.org> <13pklqk13dkipd9@corp.supernews.com> <pLzmj.10734$M24.1977@newsfe17.lga>`

```
In article <pLzmj.10734$M24.1977@newsfe17.lga>, tlmfru <lacey@mts.net> wrote:
>
>tim Josling <tejgcc_nospam@westnet.com.au> wrote in message
>news:13pklqk13dkipd9@corp.supernews.com...

[snip]

>> The problem with this theory is that in fact, the programs *are* the
>> design. The computer - specifically the compiler and link-editor - then
…[15 more quoted lines elided]…
>and the better its quality.

As I was taught, e'er-so-long ago, by my first programming instructor: 
'All you need are three things: input spec, manipulations and output 
specs.  The input specifications tell you if the data come from a dataset, 
a screen or another program, the manipulations tell you what to do with 
them - add them, subtract, group them in a certain way - and the output 
specifications tell you where the data are going to, dataset, screen, 
passed-back parameters and the like.  If you have these three - input 
specs, manipulations and output specs - then the program will write 
it'sself.  If you are missing any one of these then it is like trying to 
sit on a three-legged stool with one leg gone.'

>
>I'm in agreement that a great deal of programming is now - or should be
…[3 more quoted lines elided]…
>done a few thousand times already.

In ever-so-many interviews I have been asked 'how would you write a 
match-merge program/data entry screen/report program breaking on 
department' and the like... and my response is always 'well, *first* I'd 
go to the Prod library and get the skeleton that's already in place for 
doing this...'

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 11)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-26T14:18:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0fddd08e-a174-4861-abd8-fcd9c0b1df30@f47g2000hsd.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <M%omj.6150$HL1.21@newsfe21.lga> <3m9kp3p009h7s9ilmop0shrlu0cpuj5hha@4ax.com> <fndbvo$27j$1@registered.motzarella.org> <13pklqk13dkipd9@corp.supernews.com> <pLzmj.10734$M24.1977@newsfe17.lga>`

```
On Jan 26, 12:42 am, "tlmfru" <la...@mts.net> wrote:
> tim Josling <tejgcc_nos...@westnet.com.au> wrote in message
>
…[30 more quoted lines elided]…
>

Mr. tlmfru/PL is on the mark here - the "stairstep" version of the
Waterfall, portrayed on page 2 of the Royce article whose .pdf Robert
so generously posted for us as at
http://www.cs.umd.edu/class/spring2003/cmsc838p/Process/waterfall.pdf
,
is the "straw man" that Agilists set up to make their own case for
more flexible methods. As Robert well pointed out, the "stairstep"
monotonic approach is fraught with pitfalls. (Nevertheless, it still
has its place, and shows remarkable longevity, but the reasons for
that should be for another time.)

On page 3 of the Royce article there are two more figures of the true
Waterfall, that clearly indicate the feedback loops among both
adjacent and non-adjacent phases. And this paper was published in
1970. Waterfall here is an entirely apt and descriptive moniker - the
feedback loops clearly show the whirlpools and eddies that we might
see in a waterfall.

The "strawwman" version that Agilists like to attack, or poke fun of
(see, for example, http://www.waterfall2006.com/ ), is actually, in my
opinion, the "stairstep" vulgarization of Waterfall as represented on
page 2. That we have lived so long with the problems of "stairstep" is
probably a testament to managers' being so busy that they did not have
the time to read past page 2 and get to page 3.

What Mr. tlmfru/PL seems to be advocating here is simply that his
preference to make his "mistakes" at a higher level, in the form of a
more "abstract" design, some of what he calls "modeling", and that he
does this before he prematurely congeals too many of these mistakes in
code. It is a question of where one prefers to do the "rework". Mr.
tlmfru/PL and I both prefer to some of our rework in boxes, circles,
and arrows. Others, the more extreme of the Agilsts (such as XPers)
prefer to do (nearly?) all of their rework by "refactoring" code. That
is their prerogative.

Another benefit of the modeling approach advocated by Mr. tlmfru/PL is
that on large, or very large, projects is the establishment of a
sufficiently large "intersection" of common knowledge among the entire
project team so that it carries the day. Yes, Mr. Dashwood points out
that there are better and better automated tools all the time to help
us with this; nevertheless, a more conceptual, though _incomplete_
(yes, we must acknowledge to Mr. Josling that any conceptual model
will be _incomplete_) representation is very useful in establishing
that "intersection", which may be painfully needed for good project
coordination.

But all of this is, uh, relatively _moot_. For the greater Truths are
these, and they are not Truths of my Creation :-), only my Discovery,
so I put them out for you:

1. Agile is a _marketing_ term. And now I have found the citation.
Here it is, by Brian Marick:
"It was explicitly conceived of as a marketing term: to be evocative,
to be less dismissable than "lightweight" (the previous common
term)."
http://www.testing.com/cgi-bin/blog/2006/06/13

As I have stated elsewhere, let us applaud them for their success
here, but note that neither should that detract from the
accomplishments of Traditionalists, Neo-Classicists, and Software
Engineers.

2. Reports of abject software project failures are _increasingly_
difficult to find. As an industry we are probably doing pretty well;
and certainly well compared to another industries. And here are the
citations, Robert Glass's _Software Practitioner_ publication, in two
articles:
 - Software Projects: 40% A Total Success, Only 5% Total Failures; and
 - IS Failure: It Happens, But Increasingly Infrequently
in http://www.robertlglass.com/sp/SoftwarePractitionerSampleIssue(MAY06).pdf
(this is the sample issue available for free download.)

Thus, back to the original intent of the anchor post in this thread,
what methodologies are better, or more appropriate, for what problem
domains? Or does it even matter that much?

Gentlemen, let me conclude on a different note -

V
|
}
|
{
|
|

let me toss my (clumsy) attempt at a character "rose" to Mr. Josling
for his work on the CoBOL for gcc effort. And note for our benefit,
that to a compiler write, it would seem very natural that yes,
the *source code* _is_ the *design*. Thank you, Mr. Josling...

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 10)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-26T21:35:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<63tnp3pjm6i3gnarr389vbl902ep102fml@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <M%omj.6150$HL1.21@newsfe21.lga> <3m9kp3p009h7s9ilmop0shrlu0cpuj5hha@4ax.com> <fndbvo$27j$1@registered.motzarella.org> <13pklqk13dkipd9@corp.supernews.com>`

```
On Fri, 25 Jan 2008 21:40:36 -0000, tim Josling <tejgcc_nospam@westnet.com.au> wrote:

>On Fri, 25 Jan 2008 14:06:58 -0500, rpl wrote:
>
…[24 more quoted lines elided]…
>turns the design into the product (the executable files).

Source programs are the deliverable work product. The compiler is a deployment tool. 
A source program looks and functions the same on every platform. It can even be exectuted
drectly by an interpreter. 

>This is why the waterfall method that is being pushed by some in this
>thread is usually such an expensive failure. 

It may be expensive, but it's not a failure. It's the NORM in the vast majority of
successful Fortune 500 companies. 

>Waterfall is literally trying
>to design the design before the design is done. If the "design" has all
>the details needed to write the programs, then it may as well be the
>programs.

Design isn't a single activity, it's a top-down process that proceeds from general to
specific. Waterfall quantifies at least three layers: general business requirement, high
level design and low level design. Any other methodology will have to go through the same
levels, whatever they're called and no matter how well or poorly they're documented.

>Invariably after a waterfall project, large slabs of the documentation is
>wrong, because the initial design didn't all work and had to be changed.

In my experience, VERY SMALL passages of the documentation are wrong. They are corrected
during the development phase, before testing begins.

>This also also why the "software factory" concept doesn't work. The
>manufacturing of software is very easy. Just type in "make" or whatever.
>Then copy the data to the CDs.

That's not development; that's deployment.

>It's the design that's hard. This includes the programming.

Bad programmers try to design from the bottom up. Good programmers have the ability to
rapidly alternate between top down design and bottom up implementation. They know that
objectives come from the outside, not the inside. 

>And of course this assumes that the requirements are known in detail,
>which is rarely if every true. How often does someone build exactly what
>they were asked to build, only to find it is now what was actually wanted.

Prototypes are a useful tool for experimenting with requirements. The real world is an
EXPENSIVE way to experiment.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-25T10:55:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<56e840e4-0421-4b54-9c17-ecf14afb9e4d@t1g2000pra.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com>`

```
On Jan 25, 7:55 am, docdw...@panix.com () wrote:
> In article <dn9ip39ak344qlvd5clil31hvvi5gdc...@4ax.com>,
>
…[6 more quoted lines elided]…
> DD

Methinks that Winston Royce was conducting something akin to an
Einsteinian "thought experiment." It is only in those programming
environments "approaching the speed of light" or "operating at the sub-
atomic level" that 'not up to acceptable documentation standards'
results in wholesale management replacement. :-)

Still, it is entirely useful to perform those "thought experiments",
for they help you get through a Friday afternoon, and after all, Hope
Springs Eternal, that Somewhere, Somehow, such things happen...

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-25T19:44:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnde72$jm3$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <56e840e4-0421-4b54-9c17-ecf14afb9e4d@t1g2000pra.googlegroups.com>`

```
In article <56e840e4-0421-4b54-9c17-ecf14afb9e4d@t1g2000pra.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jan 25, 7:55�am, docdw...@panix.com () wrote:
>> In article <dn9ip39ak344qlvd5clil31hvvi5gdc...@4ax.com>,
…[10 more quoted lines elided]…
>Einsteinian "thought experiment."

This would appear to be contradicted by Mr Royce's use of nominative 
phrases such as 'I am called upon to review' and 'my first recommendation 
is simple'.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T11:13:44+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vv58oF1o0lhmU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <56e840e4-0421-4b54-9c17-ecf14afb9e4d@t1g2000pra.googlegroups.com>`

```


<klshafer@att.net> wrote in message 
news:56e840e4-0421-4b54-9c17-ecf14afb9e4d@t1g2000pra.googlegroups.com...
On Jan 25, 7:55 am, docdw...@panix.com () wrote:
> In article <dn9ip39ak344qlvd5clil31hvvi5gdc...@4ax.com>,
>
…[6 more quoted lines elided]…
> DD

Methinks that Winston Royce was conducting something akin to an
Einsteinian "thought experiment." It is only in those programming
environments "approaching the speed of light" or "operating at the sub-
atomic level" that 'not up to acceptable documentation standards'
results in wholesale management replacement. :-)

Still, it is entirely useful to perform those "thought experiments",
for they help you get through a Friday afternoon, and after all, Hope
Springs Eternal, that Somewhere, Somehow, such things happen...

[Pete:]

Hope is always good.

As long as the light at the end of the tunnel is not an oncoming Express 
train...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T11:09:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vv517F1oefi0U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fncm8p$fsr$1@reader2.panix.com...
> In article <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com>,
> Robert  <no@e.mail> wrote:
…[17 more quoted lines elided]…
> ruthless enforcement of documentation requirements.

The FIRST rule? This is someone who hasn't done a lot of field work.
>
>     Occaisionally I am called upon to review the progress of other
…[4 more quoted lines elided]…
> acceptable standards.

Or, better still, adopt processes that produce documentation 
automatically...

>
> --end quoted text
>
> All righty, by a show of hands... has anyone ever seen anything like this
> happen?

No, and I hope I never shall.
>
> (My experience, of course, is with 'sick shops' so I haven't run across an
…[3 more quoted lines elided]…
> - Akkadian or Hittite, your choice - on a bit of bathroom-tissue'.)

Documentation is important, but it must be USEFUL documentation, and to be 
useful, it must be current.

We could have a whole thread about what is useful and what is not.

Program listings, for example, were once the core of documentation, (and 
COBOL was highly valued for its "readability" on such listings), but, in 
this day and age they are irrelevant. When the current source can be 
accessed nstantly online, there is no point in saving a hard copy which may 
or may not be the latest listing.

I like to see "conceptual" documents prepared by hand... (These contain a 
high level system flow, identify interfaces to other systems and are 
designed to give newcomers a conceptual overview of what the system does and 
how it fits in the environment. In an OO environment, each Class may have 
such a document that describes any special approaches or techniques 
implemented and the conceptual background as to why the Class is necessary 
and how it was identified. Details of Methods, Properties, and Events are 
NOT documented here, because these can be obtained quickly and easily by 
using an Object Browser, and, like the source code above, they are up to 
date.)

On one project where Rational tools were mandated, I wrote my own VB code 
into Rational to automatically produce documentation from each JAD session. 
It gave me a complete database of the state of over 400 processes, who was 
present, decisions taken and current iteration (plus a few other things) 
which I could slice and dice to quickly identify where there were problems, 
and to update my Project Plan automatically. The point is that useful 
current documentation SHOULD be prepared automatically, and programmers 
shouldn't have to spend time doing it. Analysts should document things that 
the system can't, like summaries of interviews, decisions made, and 
conceptual background.

The project was "surprise audited" (by external auditors) and passed with 
flying colours and a "commendation" for the documentation and ease of 
assimilation.

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-27T10:58:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <5vv517F1oefi0U1@mid.individual.net>`

```
On 25 Jan, 22:09, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> COBOL was highly valued for its "readability" on such listings), but, in
> this day and age they are irrelevant. When the current source can be
> accessed nstantly online, there is no point in saving a hard copy which may
> or may not be the latest listing.
>

I worked in a place where a man (his nickname became Pete The Delete)
deleted the entire source library with no backup. Most of the source
was typed in by hand from listings.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-28T10:50:14+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<604ckoF1oof05U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <5vv517F1oefi0U1@mid.individual.net> <d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com...
> On 25 Jan, 22:09, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[10 more quoted lines elided]…
>

And my COBOL code to this day, reflects the possibility that the source I'm 
writing may need to be re-entered from a listing.

But it hasn't happened for over 30 years and I'm betting that the anecdote 
you provide above didn't happen last week...:-)

Anyway, any site that undertakes development WITHOUT taking backups, 
deserves whatever it gets...

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 9)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-29T14:29:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <5vv517F1oefi0U1@mid.individual.net> <d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com> <604ckoF1oof05U1@mid.individual.net>`

```
On 27 Jan, 21:50, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[22 more quoted lines elided]…
>

The deletion incident happened about 1990. The site did take backups
so why it didn't have that particular library backed up is anyones
guess.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2008-01-29T17:15:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<csOnj.68384$N67.3685@bignews5.bellsouth.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <5vv517F1oefi0U1@mid.individual.net> <d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com> <604ckoF1oof05U1@mid.individual.net> <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com>`

```
"Alistair" <alistair@ld50macca.demon.co.uk> wrote:
> "Pete Dashwood" <dashw...@removethis.enternet.co.nz> wrote:
>> "Alistair" <alist...@ld50macca.demon.co.uk> wrote:
…[22 more quoted lines elided]…
> guess.

About 10 or 15 years ago I got a desperate call from a one-man IS
department at a small company. He was almost in tears. They had
been running for years without making any backups. Someone had
persuaded the guy that he needed to start making backups. He had
mounted a scratch disk pack to do it, but when he copied, he
copied in the wrong direction. Since the scratch disk pack was
empty, it only copied over the directory, and the data was likely
mostly still there. Someone had given him my name, and he called
asking if I could recover the data. I told him I could definitely
get the data off the disk pack, but the problem would be finding
and interpreting it. They were running all purchased packages and
didn't have any source code. I recommended a professional data
recovery service. I've often wondered what happened to that guy,
and wondered if he ever tried to make another backup.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-30T08:25:05-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ih51q3ttp3qpu8a469t4c8g531d0bitv5m@4ax.com>`
- **References:** `<3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com> <5vv517F1oefi0U1@mid.individual.net> <d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com> <604ckoF1oof05U1@mid.individual.net> <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com> <csOnj.68384$N67.3685@bignews5.bellsouth.net>`

```
On Tue, 29 Jan 2008 17:15:32 -0600, "Judson McClendon"
<judmc@sunvaley0.com> wrote:

>About 10 or 15 years ago I got a desperate call from a one-man IS
>department at a small company. He was almost in tears. They had
…[3 more quoted lines elided]…
>copied in the wrong direction.

I got a Shark-Tank T-shirt once from Computer World for describing a
similar incident.    I created a dBase application for a user that
included extensive backup instructions.    When the database got
corrupted, she belatedly remembered the instructions and immediately
backed up her corrupted database over the good backup.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-30T10:17:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnpis7$che$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com> <604ckoF1oof05U1@mid.individual.net> <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com>`

```
In article <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 27 Jan, 21:50, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
>wrote:
>> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message

[snip]

>> > I worked in a place where a man (his nickname became Pete The Delete)
>> > deleted the entire source library with no backup. Most of the source
…[14 more quoted lines elided]…
>guess.

I've had contracts on sites where I'd come in and find that my source 
libraries had been deleted... 'Oh, *everyone* knows that if the first 
letter of a pack-name is 'S' then it gets wiped clean every Sunday night, 
didn't anyone tell you that?  Hope you didn't lose much, Consultant... haw 
haw haw!'

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-31T11:35:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60cceeF1p1tv1U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <d63823d5-b16f-45de-93f4-8f4c9b1fee28@i7g2000prf.googlegroups.com> <604ckoF1oof05U1@mid.individual.net> <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com> <fnpis7$che$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fnpis7$che$1@reader2.panix.com...
> In article 
> <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com>,
…[33 more quoted lines elided]…
> DD
A good example of covert hostility from the permanent staff.  I never had 
source libraries deleted, but I had trays of cards dropped and shuffled... 
:-)

When it comes oto COBOL source, there is a good case for making a local copy 
to a personal file every night before going home....

Especially if you are a new contractor on the site...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-31T01:45:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnr976$v1$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com> <fnpis7$che$1@reader2.panix.com> <60cceeF1p1tv1U1@mid.individual.net>`

```
In article <60cceeF1p1tv1U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
><docdwarf@panix.com> wrote in message news:fnpis7$che$1@reader2.panix.com...

[snip]

>> I've had contracts on sites where I'd come in and find that my source
>> libraries had been deleted... 'Oh, *everyone* knows that if the first
…[6 more quoted lines elided]…
>:-)

A possibility, Mr Dashwood... or it might have been the standard kind of 
hazing that any newbie got, I'm not sure.  In the US Air Force the 
tradition was tell the New Guy to go over to the next shop and bring back 
'a yard of flight-line'.

>
>When it comes oto COBOL source, there is a good case for making a local copy 
>to a personal file every night before going home....

Local copy?  All the disk packs are in another room, maybe another 
building or another city... how does one know which pack is closer?

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-31T17:44:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60d21aF1p9us0U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <407ca4b5-1603-4ac5-8dae-d0a068062df6@s12g2000prg.googlegroups.com> <fnpis7$che$1@reader2.panix.com> <60cceeF1p1tv1U1@mid.individual.net> <fnr976$v1$1@reader2.panix.com>`

```

```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-31T14:28:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnslun$pvp$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <60cceeF1p1tv1U1@mid.individual.net> <fnr976$v1$1@reader2.panix.com> <60d21aF1p9us0U1@mid.individual.net>`

```
In article <60d21aF1p9us0U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
><docdwarf@panix.com> wrote in message news:fnr976$v1$1@reader2.panix.com...
>> In article <60cceeF1p1tv1U1@mid.individual.net>,
…[34 more quoted lines elided]…
>yourself, it is pretty hard to do the job...

Allocating a file's easy, Mr Dashwood... but on what pack?  From the 
example above: if the source PDS is on VOL=SER=STG01 and - crafty devil 
that I am! - I create a personal dataset on VOL=SER=STG09... comes Sunday 
both copies are wiped.

If I'm really lucky (and my userid has the rights to use it) maybe my 
personal copy will wind up on VOL=SER=WKG01... and *everyone* knows that 
pack-names beginning with 'W' are wiped clean on the *last* Sunday of the 
month... and I begin my contract on the Monday before that... then both 
get wiped when I show up for my second week.

>
>I'm having difficulty believing you couldn't get what was intended or failed 
>to catch my drift.

I'm barely sure of my own intentions and drifts, Mr Dashwood, let alone 
those of other folks... but if you're suggesting that one should use 
IND$FILE to do something then... what was one to do in the days before 
IND$FILE was written?

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-25T17:54:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<alskp3d84r1rj31rqmculc9gmapuql8tr8@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <fncm8p$fsr$1@reader2.panix.com>`

```
On Fri, 25 Jan 2008 12:55:53 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com>,
>Robert  <no@e.mail> wrote:
…[29 more quoted lines elided]…
>happen?  

I've seen managers disappeared because their projects failed after the fact audits. 
Audits are conducted by government agents in the medical, pharmaceutical and aircraft
industdries. 

>(My experience, of course, is with 'sick shops' so I haven't run across an 
>instance of a single manager - let along an entire project's management - 
>being replaced because documentation was not 'up to acceptable standards', 
>even where 'acceptable' was construed as 'scribble something in cuneiform 
>- Akkadian or Hittite, your choice - on a bit of bathroom-tissue'.)

Back-of-envelope specs are prevented in places with formal methodology because documents
must be approved and SIGNED by a diverse committee composed of outside IT managers, user
reps, documentation specialists, grunts and next level up management.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-25T09:17:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d583139a-19d4-4a3a-a939-fb62a53b04b2@q77g2000hsh.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com>`

```
On Jan 24, 10:47 pm, Robert <n...@e.mail> wrote:
> On Thu, 24 Jan 2008 10:04:37 -0800 (PST), "klsha...@att.net" <klsha...@att.net> wrote:

> An 'old wine in new bottles' argument is unpersuasive because it makes the advocate sound
> like a sore loser.

If I take comfort in discovery of Eternal (or at least Persistent)
Threads, what care *I* about whether others are unpersuaded? For me, a
successful project is one where I leave things a bit better than when
I came, with integrity, that I be paid adequately for it, and that I
be Happy. Should that coincide, even approximately, with others' needs
such as 'Meets Requirements', 'Within Budget', and 'On Time' - then so
much the better.

> Here's the link:http://www.cs.umd.edu/class/spring2003/cmsc838p/Process/waterfall.pdf

Thanks for the lookup - yes, that is the one! :-)

> >Be not mistaken now, we, and by "we" I mean those such as *I*, neo-
> >Classicists, Traditionalists, Pragmatic Practitioners, in a Word, we
…[3 more quoted lines elided]…
> You are being sardonic.

Actually, no. Really. It *is* simply as stated something that I
believe.

>
> Royce says divisibility is the acid test for adequate documentation.
…[4 more quoted lines elided]…
> failure to document properly."

Robert Glass makes the case more succintly and more articulately than
I can. In his landmark (for me) _Facts and Fallacies of Software
Engineering_, he sets forth Fact #29:

'Programmers shift from design to coding when the problem is
decomposed to a level of primitives that the designer understands. If
the coder is not the same person as the designer, the designer's
primitives are unlikely to match the coder's primitives, and trouble
will result.'

Commentary by me on what I think is a brilliant insight by Glass: If
the designer and coder are different people, then three situations are
possible - (1) the designer primitives are at the same level of
abstraction as the coder wants; (2) the designer primitives are at a
level of abstraction more detailed than the coder wants; or (3) the
primitives are at a level of abstraction more *general* than the coder
can handle.

Scenario (1), in my opinion is the least likely to occur. And that is
why we have trouble.

When Scenario (2) occurs, we all know what the coder does - he simply
throws away the design spec! Haven't all of us done that? :-)

When Scenario (3) occurs, what we have is "churn". As first-iterated
coded, just a little bit of testing reveals the program falls far
short of its "intended purpose", and then we go into a loooonnng cycle
of code-and-fix.

This has profound implications for the phenomenon of "outsourcing".

>
> >Once upon a time, that was the rationale for "Analyst/Programmer", was
> >it not?.
>
> It's just job title inflation.

Hmmmm.. I rather think Analyst/Programmer is an honest attempt to deal
with the Indivisibility issue described above.

But I do grant you, with much appreciation, that Analyst/Programmer
would fall into that Technocrat/Artist generational category that you
so clearly communicated to me.

>
> >There once was a time, and maybe it was Our Time, and yes, maybe it is
…[18 more quoted lines elided]…
> oscillation.

Wow, this last section I find very, very helpful to my understanding -
with your permission, I would like to excerpt it, along with the link
below, to cross-post (without attribution), in that other forum.
Really... and I am not being sardonic :-).

>
> http://en.wikipedia.org/wiki/Generations_%28book%29- Hide quoted text -
>
> - Show quoted text -

Thanks for making this effort to help me.

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-25T10:41:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9b7kp3pmc386egpbq2f6ae8hedb2oj5i1r@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <d583139a-19d4-4a3a-a939-fb62a53b04b2@q77g2000hsh.googlegroups.com>`

```
On Fri, 25 Jan 2008 09:17:36 -0800 (PST), "klshafer@att.net"
<klshafer@att.net> wrote:

>Robert Glass makes the case more succintly and more articulately than
>I can. In his landmark (for me) _Facts and Fallacies of Software
…[6 more quoted lines elided]…
>will result.'

This is where modern design tries to keep up with modern needs.    We
don't want programmers writing code, we want designers designing
solutions.    The ideal is to have the "code" created by the tools.
That's why assemblers were created, then compilers, and other design
tools.    

Of course we have a moving target here, as our components grow, so
does our environment.

...

>> >Once upon a time, that was the rationale for "Analyst/Programmer", was
>> >it not?.
…[4 more quoted lines elided]…
>with the Indivisibility issue described above.

Each iteration have these titles bumped up.    Analysis now requires
more of the company's big picture, and programming now is closer to
the old analyst level.

I've seen programmers be the people who control the accountants (the
stereotype is the opposite).    But they need to know and follow the
accounting basics instead of finding what can be done.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-26T21:01:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <d583139a-19d4-4a3a-a939-fb62a53b04b2@q77g2000hsh.googlegroups.com>`

```
On Fri, 25 Jan 2008 09:17:36 -0800 (PST), "klshafer@att.net" <klshafer@att.net> wrote:

>On Jan 24, 10:47ï¿½pm, Robert <n...@e.mail> wrote:
>> On Thu, 24 Jan 2008 10:04:37 -0800 (PST), "klsha...@att.net" <klsha...@att.net> wrote:
…[10 more quoted lines elided]…
>much the better.

If software DOESN'T meet requirements and budget, sooner or later they'll assign the work
to someone else, which will make you UNhappy.  :)


>> Royce says divisibility is the acid test for adequate documentation.
>>
…[32 more quoted lines elided]…
>of code-and-fix.

Scenario (3) is how good programmers learn to be better, and mediocre ones learn they
don't have what it takes. When the first attempt falls short, don't try to fix it, rewrite
from scratch. 

>This has profound implications for the phenomenon of "outsourcing".

My team was outsourced this week. The outsource company will do the same work with the
same people making the same money, for 60% of the cost. The only differences will be
management and the length of a work week.

>> >Once upon a time, that was the rationale for "Analyst/Programmer", was
>> >it not?.
…[8 more quoted lines elided]…
>so clearly communicated to me.

Programming management inherits from the problem solving style outside computers. The
technocrat generation is now aged 65 and above. Former yuppies, who gave us waterfall, are
aged 45 to 64. Today's programmers are mostly XGens, who respect pragmatism over
bureaucratic structure. 

The ones to watch are the generation behind them, the Millennials, now under 27. They'll
laugh in your face if you tell them to work 60 hours a week. They want it all, want it to
work the first time and want it NOW. I think they'll change programming more than any
previous generation.

>> >There once was a time, and maybe it was Our Time, and yes, maybe it is
>> >*gone* now, that all of this was Common Knowledge.
…[22 more quoted lines elided]…
>Really... and I am not being sardonic :-).

Please do, but I think the four generational styles should be explained with examples such
as US Presidents. Good talking points would be why Jimmy Carter, the ineffective
technocrat, was relaced by a step backward to the heroic Reagan. Historically, a
generation took political power 40 years after its first birth. For yuppies, that would
have been the 1988 presidential election between G.H.W. Bush and Michael Dukakis. Why was
there no yuppie candidate? The only serious yuppie contender from either party was Al
Gore, who was 40. Dan Quayle, Bush's VP, was the token yuppie in the election. I think I
know why they held back (until Clinton), but would be interested to hear others'
hypotheses.

The Strauss & Howe generaltional model applies only to Anglo countries. Suppose WE have a
spoiled rotten generation with poor work ethic (Millennials), but India or China has one
with a strong work ethic. Wouldn't it make sense to move software development to the more
salubrious country? Suppose further that country has a long tradition of superior
education. 

I remember helping a Japanese 10th grader with his math homework. He was doing
differential equations. I said this is a college subject in the US; you must be in an
honors or accelerated program, right? The answer as nope, this is normal curriculum that
every student takes. I thought to myself, shit in forty years these people will bury us.
Looks like I was right.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-27T14:03:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fni2vq$88r$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <d583139a-19d4-4a3a-a939-fb62a53b04b2@q77g2000hsh.googlegroups.com> <9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com>`

```
In article <9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>The ones to watch are the generation behind them, the Millennials, now under 27. They'll
>laugh in your face if you tell them to work 60 hours a week. They want it all, want it to
>work the first time and want it NOW. I think they'll change programming more than any
>previous generation.

Mr Wagner, I'd say this view neglects to consider something... like... the 
users for whom those Millennials are writing programs?  If a user wants an 
'it', all, now, that needs time to put together... or if the 'it' 
communicated is of the 'well, that's what I told you but it's not what I 
want'... or if what is put together is met with 'well, yes, that's nice, 
but I was thinking... can we get (x) along with it?'...

... then someone, either coder or user, is *not* going to get 'it all, to 
work the first time and... NOW'.  Learning that the world can, at times, 
present things in such a manner might be a Good Thing to Do as early as 
possible.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-28T10:47:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<604cf0F1p03s0U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <d583139a-19d4-4a3a-a939-fb62a53b04b2@q77g2000hsh.googlegroups.com> <9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com> <fni2vq$88r$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fni2vq$88r$1@reader2.panix.com...
> In article <9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com>,
> Robert  <no@e.mail> wrote:
…[24 more quoted lines elided]…
>

I agree with both of you here... :-)

Robert is correct in that the attitude of the rising generation is 
aggressive and impatient. They are also much more confident (having had 
instruction in Computer Science, that simply wasn't available when we were 
their age). And their confidence is based on the fact that they are using 
tools and approaches that DO enable things to be built (and re-built) very 
quickly.

Doc is correct in that if something is not properly stated (and it usually 
isn't, unless there are proper processes and procedures in place to make 
sure that it is), it doesn't matter how you cut it, it will need to be 
re-done and won't be available immediately. The difference is that these 
youngsters are NOT growing up in a procedural COBOL environment, with the 
Waterfall as their preferred methodology. They therefore CAN re-build thngs 
much quicker than would be the case if they WERE in such an environment.

Nevertheless, I agree with Doc that exposure to the real world may provide 
some experiences for which they will be better in the long run... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-28T01:47:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnjc8d$5tr$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com> <fni2vq$88r$1@reader2.panix.com> <604cf0F1p03s0U1@mid.individual.net>`

```
In article <604cf0F1p03s0U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[32 more quoted lines elided]…
>aggressive and impatient.

With all due respect, Mr Dashwood, such things have been said by geezers 
for many a year... I believe your evaluation fits right in with '... 'n 
don't git me started on what them kids're callin' 'music' nowadays, 
neither!'

[snip]

>Nevertheless, I agree with Doc that exposure to the real world may provide 
>some experiences for which they will be better in the long run... :-)

''We agree?  One of us must be wrong!', he cried, Wildely.'

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-28T22:41:42+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<605malF1ovumeU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com> <fni2vq$88r$1@reader2.panix.com> <604cf0F1p03s0U1@mid.individual.net> <fnjc8d$5tr$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fnjc8d$5tr$1@reader2.panix.com...
> In article <604cf0F1p03s0U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[44 more quoted lines elided]…
> neither!'

Yes, it is a generalization and there may well be exceptions to it... :-)

I based it on some of the younger team members I have worked with in the 
last few years; good people, but agressive and impatient... :-)

I'm quite sure people thought the same about me when I was 20 and a junior 
programmer. (There are probably some who still do...:-))

To avoid offence to young people who are NOT aggressive and impatient  I'll 
add the qualifiers "For the most part, in my experience,...".

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-28T10:17:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnka3d$aj$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <604cf0F1p03s0U1@mid.individual.net> <fnjc8d$5tr$1@reader2.panix.com> <605malF1ovumeU1@mid.individual.net>`

```
In article <605malF1ovumeU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
><docdwarf@panix.com> wrote in message news:fnjc8d$5tr$1@reader2.panix.com...
>> In article <604cf0F1p03s0U1@mid.individual.net>,
>> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>>>Robert is correct in that the attitude of the rising generation is
>>>aggressive and impatient.
…[6 more quoted lines elided]…
>Yes, it is a generalization and there may well be exceptions to it... :-)

Not a generalisation, Mr Dashwood... but just something that Old Folks 
have been doing for a goodly long while.  I recall reading, someplace, 
about how that now well-accepted dance, the polka, was rerided as lewd and 
unfit for Polite Society because of the gyrations it allowed the 
youngsters to perform.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 12)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-28T09:03:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o3vrp39vsf1pv15ufkk88glr175aurbpga@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <604cf0F1p03s0U1@mid.individual.net> <fnjc8d$5tr$1@reader2.panix.com> <605malF1ovumeU1@mid.individual.net> <fnka3d$aj$1@reader2.panix.com>`

```
On Mon, 28 Jan 2008 10:17:17 +0000 (UTC), docdwarf@panix.com () wrote:

>Not a generalisation, Mr Dashwood... but just something that Old Folks 
>have been doing for a goodly long while.  I recall reading, someplace, 
>about how that now well-accepted dance, the polka, was rerided as lewd and 
>unfit for Polite Society because of the gyrations it allowed the 
>youngsters to perform.

I recently read an old advertisement created to tell us that the
record companies were stealing from live performers since we could
listen to Victrolas whenever we want.   It's interesting to see how
the more things change, the more things stay the same.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 12)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-29T14:30:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e33894a5-3ee5-4e82-a455-b2651f649b4f@q39g2000hsf.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <604cf0F1p03s0U1@mid.individual.net> <fnjc8d$5tr$1@reader2.panix.com> <605malF1ovumeU1@mid.individual.net> <fnka3d$aj$1@reader2.panix.com>`

```
On 28 Jan, 10:17, docdw...@panix.com () wrote:
> In article <605malF1ovum...@mid.individual.net>,
>
…[24 more quoted lines elided]…
> DD

Those were the days when the  sight of an inch of crinolene was enough
to turn a young man's head, eh?
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-30T10:23:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnpj6v$335$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <605malF1ovumeU1@mid.individual.net> <fnka3d$aj$1@reader2.panix.com> <e33894a5-3ee5-4e82-a455-b2651f649b4f@q39g2000hsf.googlegroups.com>`

```
In article <e33894a5-3ee5-4e82-a455-b2651f649b4f@q39g2000hsf.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 28 Jan, 10:17, docdw...@panix.com () wrote:

[snip]

>> I recall reading, someplace,
>> about how that now well-accepted dance, the polka, was rerided as lewd and
…[4 more quoted lines elided]…
>to turn a young man's head, eh?

Given the common habits of hygiene it could do the same for stomachs, 
aye... why, there was this mademoiselle from Armentieres who ain't been 
bathed in forty years.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-30T08:32:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dn51q35nbh3fod1to1hvuqd98ldi93tl9d@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <604cf0F1p03s0U1@mid.individual.net> <fnjc8d$5tr$1@reader2.panix.com> <605malF1ovumeU1@mid.individual.net> <fnka3d$aj$1@reader2.panix.com> <e33894a5-3ee5-4e82-a455-b2651f649b4f@q39g2000hsf.googlegroups.com>`

```
On Tue, 29 Jan 2008 14:30:45 -0800 (PST), Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> Not a generalisation, Mr Dashwood... but just something that Old Folks
>> have been doing for a goodly long while. ï¿½I recall reading, someplace,
…[7 more quoted lines elided]…
>to turn a young man's head, eh?

I know people who used to sit at the bus station to glimpse some thigh
as the ladies climbed up into the bus.    But it works - whatever is
public to all tends to become ordinary - what is private except for
the select is what excites us.   When underwear is public, it's just
clothes.   When various body parts are public, then they are just body
parts.   When my wife was hospitalized after a serious accident,
exposure of her private parts didn't excite me - the context was
different (as it is when bathing granddaughters).    The erotic organ
is the brain.





Times have changed,
And we've often rewound the clock,
Since the Puritans got a shock,
When they landed on Plymouth Rock.
If today,
Any shock they should try to stem,
'Stead of landing on Plymouth Rock,
Plymouth Rock would land on them.

In olden days a glimpse of stocking
Was looked on as something shocking,
But now, God knows,
Anything Goes.

Good authors too who once knew better words,
Now only use four letter words
Writing prose, Anything Goes.

The world has gone mad today
And good's bad today,
And black's white today,
And day's night today,
When most guys today
That women prize today
Are just silly gigolos
And though I'm not a great romancer
I know that I'm bound to answer
When you propose,
Anything goes

When grandmama whose age is eighty
In night clubs is getting matey with gigolo's,
Anything Goes.

When mothers pack and leave poor father
Because they decide they'd rather be tennis pros,
Anything Goes.

If driving fast cars you like,
If low bars you like,
If old hymns you like,
If bare limbs you like,
If Mae West you like
Or me undressed you like,
Why, nobody will oppose!
When every night,
The set that's smart
Is intruding in nudist parties in studios,
Anything Goes.

The world has gone mad today
And good's bad today,
And black's white today,
And day's night today,
When most guys today
That women prize today
Are just silly gigolos
And though I'm not a great romancer
I know that I'm bound to answer
When you propose,
Anything goes

If saying your prayers you like,
If green pears you like
If old chairs you like,
If back stairs you like,
If love affairs you like
With young bears you like,
Why nobody will oppose!

And though I'm not a great romancer
And though I'm not a great romancer
I know that I'm bound to answer
When you propose,
Anything goes...
Anything goes!
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-28T09:00:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nuurp390v51f0bcab428qstrvss9crdjc3@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com> <d583139a-19d4-4a3a-a939-fb62a53b04b2@q77g2000hsh.googlegroups.com> <9nump3h5dvdneenci8f50jphgiegu01jao@4ax.com>`

```
On Sat, 26 Jan 2008 21:01:47 -0600, Robert <no@e.mail> wrote:

>I remember helping a Japanese 10th grader with his math homework. He was doing
>differential equations. I said this is a college subject in the US; you must be in an
>honors or accelerated program, right? The answer as nope, this is normal curriculum that
>every student takes. I thought to myself, shit in forty years these people will bury us.
>Looks like I was right.

I've read that once Japanese students make it to college, things get
easy.

How long ago was it when you thought this?   Or more to the point is
when will this "in forty years" be reached when it looks as though we
will be buried?
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T10:46:47+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vv3m9F1oakh7U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com> <8fc01a64-2f4a-4973-8b20-c1691e16661d@s8g2000prg.googlegroups.com> <dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:dn9ip39ak344qlvd5clil31hvvi5gdcbao@4ax.com...
> On Thu, 24 Jan 2008 10:04:37 -0800 (PST), "klshafer@att.net" 
> <klshafer@att.net> wrote:
…[40 more quoted lines elided]…
> user.

That's why joint workshops are a good idea...

>
> I've learned from experience that knowing more then the user about his own 
> technical
> specialty, such as accounting, law and statistics, really pisses them off. 
> :)

Only if you rub their noses in it or come across as arrogant. Pertinent 
questions posed from a base of knowledge, usually get them thinking, rather 
than resenting.


>
>>- Didn't the original Royce Waterfall article show feedback loops, not
…[36 more quoted lines elided]…
> in the techie psyche, not the real world where users live.

I've seen this too, just as you describe it.

The reasons for it may also be as you describe (we see people here, to this 
day, passionately defending efficiency as a "Holy Grail" when it doesn't 
matter. There are times and cases where it DOES matter, but usually NOT in 
commercial data processing. Even the gains made by saving a few cycles in 
multithreaded environments (where it MIGHT matter) are rapidly being trumped 
by additional processors. I'm not saying we should write inefficient code; 
just that on a list of priorities, hardware efficiency of program code is no 
longer in the place where it once was.)

>
> Thus, a development process that revolves around 'optimized code' is a 
> non-starter. The
> process SHOULD revolve around the user.

Absolutely and Amen! :-)
>
>>(I somehow found the Royce Waterfall .pdf on the Web; if I
…[83 more quoted lines elided]…
> oscillation.

Interesting observation, and well stated. Not sure whether I agree or not 
but will think more on it... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-24T14:08:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6abcf80-2e6b-48bf-89a0-7eede7bec13c@s13g2000prd.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <3khfp39ibgkkhus4ut98c2q6a20he77idq@4ax.com>`

```
On 24 Jan, 01:20, Robert <n...@e.mail> wrote:
>
> "You must know there are two ways of contesting, the one by the law, the other by force;
…[18 more quoted lines elided]…
>

Successful Software Delivery By Machiavelli? Throw in Sun Tzu and
Miyamoto Musashi and you would have a winning methodology.

Keep quoting.
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-24T13:57:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89cb04cd-7242-4a6c-839c-32914d1cded3@1g2000hsl.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net>`

```
On 23 Jan, 03:57, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> <klsha...@att.net> wrote in message
>
…[154 more quoted lines elided]…
> - Show quoted text -

How is your management book coming along? My offer to proof read it is
still open.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-25T12:33:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vslhoF1nssncU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <89cb04cd-7242-4a6c-839c-32914d1cded3@1g2000hsl.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:89cb04cd-7242-4a6c-839c-32914d1cded3@1g2000hsl.googlegroups.com...
> On 23 Jan, 03:57, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[175 more quoted lines elided]…
> still open.

Thanks Alistair.

I am currently reviewing what I have (about 75% of the total). I'll send you 
a proof copy for review when I have 100%.

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-25T06:44:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7046e06f-2944-4fd6-8e01-94c42d579b58@v67g2000hse.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <89cb04cd-7242-4a6c-839c-32914d1cded3@1g2000hsl.googlegroups.com> <5vslhoF1nssncU1@mid.individual.net>`

```
On 24 Jan, 23:33, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[180 more quoted lines elided]…
> - Show quoted text -

Cheers, I can't wait   :-)
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-01-25T12:04:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13pk5jin9s2hj22@corp.supernews.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <89cb04cd-7242-4a6c-839c-32914d1cded3@1g2000hsl.googlegroups.com> <5vslhoF1nssncU1@mid.individual.net> <7046e06f-2944-4fd6-8e01-94c42d579b58@v67g2000hse.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:7046e06f-2944-4fd6-8e01-94c42d579b58@v67g2000hse.googlegroups.com...
> On 24 Jan, 23:33, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[218 more quoted lines elided]…
> Cheers, I can't wait   :-)

Hey, I'd like a free, ah, oh, a err, ... I mean a proof copy too!
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T11:49:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vv7blF1nmvshU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vns9hF1ns38fU1@mid.individual.net> <89cb04cd-7242-4a6c-839c-32914d1cded3@1g2000hsl.googlegroups.com> <5vslhoF1nssncU1@mid.individual.net> <7046e06f-2944-4fd6-8e01-94c42d579b58@v67g2000hse.googlegroups.com> <13pk5jin9s2hj22@corp.supernews.com>`

```


"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:13pk5jin9s2hj22@corp.supernews.com...
>
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
…[232 more quoted lines elided]…
>
Advice which costs nothng is usually worth the price... :-)

Pete.
```

#### ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-23T10:36:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fn75bd$nj6$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com>`

```
In article <519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>All -
>
…[7 more quoted lines elided]…
>object-oriented, custom, code-and-fix :-), whatever.

I use, of course, whatever style fits into the code that already exists at 
the client's site... if a programmer expects something to occur in a 
certain place or way then I want to make sure I do my best not to add 
confusion.  For example, if a program usually starts with something like:

Procedure Division using LinkParms.

    Evaluate PassThrough
    When 1
        Perform First-Calls
        Perform Edit-Data
    When 2
        Perform Edit-data
    When Other
        Perform LinkParms-Corrupt
    End-Evaluate

    Perform Cleanup

    Goback.

... then it is rather unlikely for me to write

PROCEDURE DIVISION USING LINKPARMS.

    PERFORM 0000-HOUSEKEEPING  THRU  0000-EX.

    PERFORM 5000-MAINLINE      THRU  5000-EX.

    PERFORM 9000-EOJ           THRU  9000-EX.

    GOBACK.

0000-HOUSEKEEPING.

    MOVE LS-PASS-FLD  TO  WK-PASS-FLD.
    IF NOT FIRST-TIME-IN
        GO TO 0000-EX.

... et and cetera.  If something just Isn't Working (certain things keep 
going wrong in certain ways) then I'll make my suggestions as to how I 
believe difficulties might be alleviated... but as long as what I do 
doesn't violate my own standards of Professional Ethics then, ultimately, 
I'll do what the person who signs my timesheets tells me to do; something 
about paying pipers and calling tunes.

DD
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-23T09:48:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <fn75bd$nj6$1@reader2.panix.com>`

```
On Jan 23, 5:36 am, docdw...@panix.com () wrote:
> In article <519b9104-a107-4f9d-b341-781c2185d...@d4g2000prg.googlegroups.com>,
>
…[38 more quoted lines elided]…
>

Hmmm... Doc, this actually is *very helpful*. I just need a moniker to
'tach to it. How about, "minimal impact" approach as the
"methodology", with the "problem domain" being "maintenance". Maybe
this is really a "meta-methodology", since it might subsume "if system
flowcharts exist, update the system flowcharts as needed, in the same
format as before." Given all the hub-bub of "transformational"
approaches and the like, "minimal impact" might actually be a valid
way of thinking about it.

Can you think of a better, ah, more *marketable* tagline than "minimal
impact" though? Something with a homonym of a Hollywood celebrity's
name, or the like?


> ... et and cetera.  If something just Isn't Working (certain things keep
> going wrong in certain ways) then I'll make my suggestions as to how I
…[4 more quoted lines elided]…
>

I seem to recall that when the ol' body wears out a little too much,
and there is little that the old' Doc can do, we usually shift away
from health Remediation to Pain Management. So what do we call these
for Software systems?

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-23T18:26:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fn80tb$gf9$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <fn75bd$nj6$1@reader2.panix.com> <a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com>`

```
In article <a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>On Jan 23, 5:36�am, docdw...@panix.com () wrote:
>> In article <519b9104-a107-4f9d-b341-781c2185d...@d4g2000prg.googlegroups.com>,
…[4 more quoted lines elided]…
>> confusion.

[snip]

>Hmmm... Doc, this actually is *very helpful*.

From *me*?  That's utterly impossible, just ask around the newsgroup.

>I just need a moniker to
>'tach to it. How about, "minimal impact" approach as the
…[5 more quoted lines elided]…
>way of thinking about it.

That is one of the difficulties, Mr Shafer... the reconciling of 'we want 
something new' with 'we're comfortable with what we do'.  If 'what we do' 
actually *works* then I've found the primary cause of 'we want something 
new' is a new Corner-Office Idiot who wants folks to say 'Jones is really 
shaking things up there.'

(never mind the fact that more work is getting done, or less, or the 
employees are more satisfied, or less... it's just 'Jones is really 
shaking things up there')

>
>Can you think of a better, ah, more *marketable* tagline than "minimal
>impact" though? Something with a homonym of a Hollywood celebrity's
>name, or the like?

If I could do that I'd be writing advertising-copy... 'It's this, it's 
that, it's the other thing!  It's all three, in one... yes, it's new 
Three-in-One!'

And so... I stick to COBOL.

>> ... et and cetera. �If something just Isn't Working (certain things keep
>> going wrong in certain ways) then I'll make my suggestions as to how I
…[9 more quoted lines elided]…
>for Software systems?

It could be the shift from 'curative coding to, perhaps, 'palliative 
programming'.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-01-23T11:46:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cr2fp3hc8lpkd3sdficv3jl9tn0lpk1mju@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <fn75bd$nj6$1@reader2.panix.com> <a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com> <fn80tb$gf9$1@reader2.panix.com>`

```
On Wed, 23 Jan 2008 18:26:51 +0000 (UTC), docdwarf@panix.com () wrote:

>It could be the shift from 'curative coding to, perhaps, 'palliative 
>programming'.

Sometimes that's sufficient.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** "klshafer@att.net" <klshafer@att.net>
- **Date:** 2008-01-23T18:36:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eb399072-2ca3-42b8-867f-35fd27546fdd@y5g2000hsf.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <fn75bd$nj6$1@reader2.panix.com> <a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com> <fn80tb$gf9$1@reader2.panix.com>`

```
>
> It could be the shift from 'curative coding to, perhaps, 'palliative
> programming'.
>
> DD

Palliative programming? That actually is very, VERY good! So apt! So
descriptive! I'm so glad I prompted you! I will have to tell the
*World* that it was a Doc who coined the term!

Ken
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-24T11:15:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fn9s1a$eak$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com> <fn80tb$gf9$1@reader2.panix.com> <eb399072-2ca3-42b8-867f-35fd27546fdd@y5g2000hsf.googlegroups.com>`

```
In article <eb399072-2ca3-42b8-867f-35fd27546fdd@y5g2000hsf.googlegroups.com>,
klshafer@att.net <klshafer@att.net> wrote:
>>
>> It could be the shift from 'curative coding to, perhaps, 'palliative
…[4 more quoted lines elided]…
>*World* that it was a Doc who coined the term!

The best I can ask for is to be cited as a source by a good scholar... a 
right close second, though, is to be the recipient of royalty-checks.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-25T11:36:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vsi8cF1nflagU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com> <fn80tb$gf9$1@reader2.panix.com> <eb399072-2ca3-42b8-867f-35fd27546fdd@y5g2000hsf.googlegroups.com> <fn9s1a$eak$1@reader2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:fn9s1a$eak$1@reader2.panix.com...
> In article 
> <eb399072-2ca3-42b8-867f-35fd27546fdd@y5g2000hsf.googlegroups.com>,
…[13 more quoted lines elided]…
>
You'd rather fame than money, Doc?

Not me.

I'm very happy to ensure that the "success" is passed to the permanent 
employees (for whom I usually throw a party with a percentage of the 
cash...)

While this may sound mercenary, I find that acquiring cash, rather than 
being an end in itself, is a great enabler; it lets me do the things I 
really want to do.

We are having a glorious summer here (yesterday was 28 and today looks like 
being the same). I am able to relax and enjoy it with friends, go to the 
beach, take a walk around the Mount, sit and read a book, play my guitar, or 
acquire some more information on C# or whatever... I can only do this 
because I maximised the money when I last worked... :-)

Work is great (and I certainly enjoy mine...) but life is greater. We need 
time for life as well as work, and cash is the enabler... :-)

By April or so, I'll probably need to refill the coffers, but until then... 
(raises Jack Daniels with sparkling coke and fresh lime aromas, large ice 
cubes just visible through the condensation on the glass...)... very good 
health to you all. :-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-25T02:20:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnbh0s$seg$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <eb399072-2ca3-42b8-867f-35fd27546fdd@y5g2000hsf.googlegroups.com> <fn9s1a$eak$1@reader2.panix.com> <5vsi8cF1nflagU1@mid.individual.net>`

```
In article <5vsi8cF1nflagU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:fn9s1a$eak$1@reader2.panix.com...
…[14 more quoted lines elided]…
>You'd rather fame than money, Doc?

One does not rule out the other, Mr Dashwood; one can ask for the best, 
the second-best, the third-best... all the way down to a sub-zero sausage, 
sometimes called the 'absolute wurst'.  As... someone pointed out in a 
posting to This Very Newsgroup, nigh a decade back: 
<http://groups.google.com/group/comp.lang.cobol/msg/d1ab4181eb38f543?dmode=source>

--begin quoted text:

As I've said many times: 'Honor is a wonderful coin... but my landlord
doesn't accept it.'

--end quoted text

>
>Not me.

Well, if all you can think of is to ask for one OR the other to the 
exclusion of any else... have at it!

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T10:32:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vv2qiF1n8o0iU1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <eb399072-2ca3-42b8-867f-35fd27546fdd@y5g2000hsf.googlegroups.com> <fn9s1a$eak$1@reader2.panix.com> <5vsi8cF1nflagU1@mid.individual.net> <fnbh0s$seg$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fnbh0s$seg$1@reader2.panix.com...
> In article <5vsi8cF1nflagU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[37 more quoted lines elided]…
>
My statement wasn't clear. No exclusivity was intended, simply a priority. 
Both are nice to have but, for myself, I prefer the money... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-26T01:18:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fne1oh$4vi$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vsi8cF1nflagU1@mid.individual.net> <fnbh0s$seg$1@reader2.panix.com> <5vv2qiF1n8o0iU1@mid.individual.net>`

```
In article <5vv2qiF1n8o0iU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[7 more quoted lines elided]…
>> sometimes called the 'absolute wurst'.

[snip]

>>>
>>>Not me.
…[4 more quoted lines elided]…
>My statement wasn't clear. No exclusivity was intended, simply a priority. 

In the English I was taught, Mr Dashwood, the question of 'you would 
rather have (a) than (b)' is clear and represents an exclusivity, as is 
indicated by the formation 'you would rather have (a) than (b) or 
both'.... perhaps a different dialect is common in the Antipodes.  (What 
*is* a 'dinkum' and why are they always relatively devoid of melanin?)

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-01-26T14:48:32+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5vvhrhF1ofcc6U1@mid.individual.net>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vsi8cF1nflagU1@mid.individual.net> <fnbh0s$seg$1@reader2.panix.com> <5vv2qiF1n8o0iU1@mid.individual.net> <fne1oh$4vi$1@reader2.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fne1oh$4vi$1@reader2.panix.com...
> In article <5vv2qiF1n8o0iU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[26 more quoted lines elided]…
> both'.... perhaps a different dialect is common in the Antipodes.

Perhaps :-)

Any of my compatriots, given the context would have caught my drift... :-)


 (What
> *is* a 'dinkum' and why are they always relatively devoid of melanin?)
>

"Dinkum"   and "Fair Dinkum" means "the genuine article". The origin is 
obscure; it may relate to gum digging or it may be related to Lincolnshire 
English where a similar word denotes "honest". It is certainly late 19th 
century in both Australia and New Zealand, but I haven't heard it used 
recently.

Sometimes corrupted to "Dinky Di".

It does NOT mean "hard work".... (that's "yakker")

As for being devoid of melanin, there are many Dinkum New Zealanders who 
would contest that... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-26T14:59:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnfhsn$q4$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vv2qiF1n8o0iU1@mid.individual.net> <fne1oh$4vi$1@reader2.panix.com> <5vvhrhF1ofcc6U1@mid.individual.net>`

```
In article <5vvhrhF1ofcc6U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[33 more quoted lines elided]…
>Any of my compatriots, given the context would have caught my drift... :-)

Anyone from your country would have understood that 'rather have (a) than 
(b)' indicates no exclusivity?  It might be wise, then, to realise that 
this group commands an International Audience - folks have mentioned this 
a few times - and that such provincialism might cause confusion or be seen 
as a sort of nationalistic arrogance.  Have a care!

(oh, have *two*... they're not very fattening)

>
>
…[8 more quoted lines elided]…
>recently.

Ummmmm... by certain standards the late 19th century *is* 'recently'... 
but neither here nor there.

>
>Sometimes corrupted to "Dinky Di".
…[4 more quoted lines elided]…
>would contest that... :-)

That may be my limited experience, then.  The only use I'd heard was 'fair 
dinkum' and according to my copy of the OED (Vol I, p. 951 showing 6. 26, 
col iii, topmost entry) 'II. 6. Of complexion and hair: Light as opposed 
to dark'... so perhaps 'devoid' was a bit strong.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 10)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-27T11:06:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2740def-25ea-41d3-8909-b38f369449a9@i3g2000hsf.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vsi8cF1nflagU1@mid.individual.net> <fnbh0s$seg$1@reader2.panix.com> <5vv2qiF1n8o0iU1@mid.individual.net> <fne1oh$4vi$1@reader2.panix.com>`

```
On 26 Jan, 01:18, docdw...@panix.com () wrote:
> In article <5vv2qiF1n8o0...@mid.individual.net>,
>
…[28 more quoted lines elided]…
> DD

I don't know much about dinkums except that:
1.  They are definitely southern hemisphere;
2.  They are usually fair.
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 11)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-01-27T13:42:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d95nj.27313$R55.26203@newsfe13.lga>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vsi8cF1nflagU1@mid.individual.net> <fnbh0s$seg$1@reader2.panix.com> <5vv2qiF1n8o0iU1@mid.individual.net> <fne1oh$4vi$1@reader2.panix.com> <a2740def-25ea-41d3-8909-b38f369449a9@i3g2000hsf.googlegroups.com>`

```

Alistair <alistair@ld50macca.demon.co.uk> wrote in message
news:a2740def-25ea-41d3-8909-b38f369449a9@i3g2000hsf.googlegroups.com...
>
> In the English I was taught, Mr Dashwood, the question of 'you would
…[5 more quoted lines elided]…
> DD

>I don't know much about dinkums except that:
>1.  They are definitely southern hemisphere;
>2.  They are usually fair.

You can put a blinkin' deaner on it, cobber!

PL
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 12)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-29T14:27:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d290aebb-51f6-44e6-8037-453f90f4e218@j20g2000hsi.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <5vsi8cF1nflagU1@mid.individual.net> <fnbh0s$seg$1@reader2.panix.com> <5vv2qiF1n8o0iU1@mid.individual.net> <fne1oh$4vi$1@reader2.panix.com> <a2740def-25ea-41d3-8909-b38f369449a9@i3g2000hsf.googlegroups.com> <d95nj.27313$R55.26203@newsfe13.lga>`

```
On 27 Jan, 19:42, "tlmfru" <la...@mts.net> wrote:
> Alistair <alist...@ld50macca.demon.co.uk> wrote in message
>
…[17 more quoted lines elided]…
> PL

No shit, mate. What'sa deaner?
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-01-30T10:24:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnpj9p$se$1@reader2.panix.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <a2740def-25ea-41d3-8909-b38f369449a9@i3g2000hsf.googlegroups.com> <d95nj.27313$R55.26203@newsfe13.lga> <d290aebb-51f6-44e6-8037-453f90f4e218@j20g2000hsi.googlegroups.com>`

```
In article <d290aebb-51f6-44e6-8037-453f90f4e218@j20g2000hsi.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 27 Jan, 19:42, "tlmfru" <la...@mts.net> wrote:
>> Alistair <alist...@ld50macca.demon.co.uk> wrote in message

[snip]

>> >I don't know much about dinkums except that:
>> >1. �They are definitely southern hemisphere;
…[5 more quoted lines elided]…
>No shit, mate. What'sa deaner?

It could be the one in charge of a department of professorers.

DD
```

###### ↳ ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2008-01-24T14:00:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0376e9d-5481-4fc0-adf7-e8843856d343@z17g2000hsg.googlegroups.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <fn75bd$nj6$1@reader2.panix.com> <a875426b-021a-440c-adf1-a1df307299cd@e23g2000prf.googlegroups.com> <fn80tb$gf9$1@reader2.panix.com>`

```
On 23 Jan, 18:26, docdw...@panix.com () wrote:
> In article <a875426b-021a-440c-adf1-a1df30729...@e23g2000prf.googlegroups.com>,
>
…[61 more quoted lines elided]…
> DD

Or perhaps: Phase Six of any project - find a new job.
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2008-01-23T14:26:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nv4fp3p3olirv2reqp5no4hvlsqf584433@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <fn75bd$nj6$1@reader2.panix.com>`

```
On Wed, 23 Jan 2008 10:36:29 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com>,
>klshafer@att.net <klshafer@att.net> wrote:
…[57 more quoted lines elided]…
>DD

In terms of methodologies to solve a problem, I'm so old school I
still flow chart at times when the logic path isn't clear or the
problem too complex.  Then, depending on what language is available to
me at the client site, I write the code to fit the flow.  Structured
analysis / structured design, object-oriented, custom, code-and-fix
are useless unless you know the path you need to take to solve the
problem.  They, in and of themselves, will solve nothing and therefore
I don't feel are worth much discussion.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

"Well, that kind of puts a damper on another Yankees win."
--Announcer Phil Rizzuto, after a news bulletin reporting
 the death of Pope Paul VI, 1978
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2008-01-23T19:32:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13pfn4jrssat53a@corp.supernews.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com>`

```

<klshafer@att.net> wrote in message 
news:519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com...
> All -
>
…[63 more quoted lines elided]…
> Ken

This response may be more low level than you are looking for. I am not 
heavily into project management although I have been exposed to CMM.  I was 
not impressed with how it was implemented where I work.  People often 
generated a lot of the required documentaion after the fact so it was not 
true CMM.

For business application I have found data flow diagrams, process mini specs 
and data dictionaries helpful.  See "How to Design and Develop Business 
systems" by Steve Eckols.  This book is dated by now. I have used 
data-structured design. See "Programming on Purpose" seriesby P.J. Plager.

For CICS I have found screen flow diagrams helpful. See "CICS for the COBOL 
Programmer" by Doug Lowe.

For manitenance I have used structure charts to show what 
CALLs/PERFORMs/XCTLs/LINKs  what.  For some twisted logic flowcharts can 
help, and where they don't help a debugger that allows breakpoints and 
tracing usually works.

For OO design patterns are great. See "head First Design Patterns".
```

##### ↳ ↳ Re: Mapping (CoBOL) Methodologies to Problem Domains

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-23T20:41:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lcufp3t672oebduub29g7ifahjtui6574p@4ax.com>`
- **References:** `<519b9104-a107-4f9d-b341-781c2185da40@d4g2000prg.googlegroups.com> <13pfn4jrssat53a@corp.supernews.com>`

```
On Wed, 23 Jan 2008 19:32:33 -0500, "Charles Hottel" <chottel@earthlink.net> wrote:

>This response may be more low level than you are looking for. I am not 
>heavily into project management although I have been exposed to CMM.  I was 
>not impressed with how it was implemented where I work.  People often 
>generated a lot of the required documentaion after the fact so it was not 
>true CMM.

That's the RIGHT way. First write the program, then the detailed design. They always
agree! There's no rework and you can use interns or offshore contractors rather than
wasting programmer time. I'm not joking, that's how it's done in F-100 companies. 

>For manitenance I have used structure charts to show what 
>CALLs/PERFORMs/XCTLs/LINKs  what.  For some twisted logic flowcharts can 
>help

What's a flowchart? I think I saw one in the '70s.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
