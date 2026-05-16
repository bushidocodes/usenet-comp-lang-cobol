[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] System Conversion - An Overview

_24 messages · 11 participants · 2007-10 → 2007-11_

---

### [OT] System Conversion - An Overview

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-30T09:38:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fg6u2d$qvk$1@reader1.panix.com>`

```

As an extension of an earlier thread regarding a COBOL-to-Java 
conversion... some meanderings.

As noted, the core of such a thing is not a technology change, it is a 
business process change and needs to be addressed both by those familiar 
with the present process (what the COBOL system does) as well as those who 
are familiar with the new technology's capabilities (what the Java system 
can do).  Right off the bat there may be difficulties... those familiar 
with the present process may respond with 'oh, we can do *that*, why 
didn't you ask?' when the new-tech team begins its proposals.

I recall reading, someplace, a consultant who said he'd been approached by 
a small insurance company in the early 1970s about converting their 
current paper-and-pencil system to a state-of-the-art COBOL/CICS 
green-screen system.  His off-the-record response was 'They wanted to 
duplicate their current processes... they had no idea how using a computer 
would change the way they work and the way they could work, essentially 
they wanted an electronic version of their current system and nothing 
more.'

In like manner... who has not seen a DB2 installation obviously designed 
by VSAM-heads? All the overhead of an RDBM system, none of the benefits.

The greatest difficulty, I would say, in these situations is that either 
marching-orders have already been given (some stinkwad, two-bit, 
Corner-Office Idiot says 'That last Executive Retreat I went to in the 
Bahamas - oh, the harsh burdens I bear for The Company! - taught that 
COBOL's worthless and Java's the way to go.  Get it done!') or that those 
with a particular dog in the fight (Preserve the Olde Wayse or New System 
Now) are more interested in keeping discussion in areas that they know 
about than in honestly learning something new.

(on my current site I do a lot of ad-hoc reporting and file-creation for a 
PeopleSoft system that gets ftp'd off the Big Iron... when it started the 
general attitude was 'Oh, that can't be done with COBOL'... and this has 
changed to 'Oh, only *he* can do that with COBOL', an equally distasteful 
view, I'd say)

All in all, it is usually a good thing to remember what Machiavelli had to 
say about the introduction of new systems 
<http://www.gutenberg.org/files/1232/1232.txt>

--begin quoted text:

And it ought to be remembered that there is nothing more difficult to take 
in hand, more perilous to conduct, or more uncertain in its success, then 
to take the lead in the introduction of a new order of things. Because the 
innovator has for enemies all those who have done well under the old 
conditions, and lukewarm defenders in those who may do well under the new. 
This coolness arises partly from fear of the opponents, who have the laws 
on their side, and partly from the incredulity of men, who do not readily 
believe in new things until they have had a long experience of them.

--end quoted text

DD
```

#### ↳ Re: System Conversion - An Overview

- **From:** Rene_Surop <infodynamics_ph@yahoo.com>
- **Date:** 2007-10-30T06:20:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193750415.054573.294890@q3g2000prf.googlegroups.com>`
- **In-Reply-To:** `<fg6u2d$qvk$1@reader1.panix.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com>`

```
Considering HansJ situation..... and with such a magnitude of
requirements. Woh! System language conversion is not my best solution.
Go to the Cobol vendor who provided the solutions and re-engineer.

If business logic is needed to be changed... then start with a "new"
language platform "you think" is best and IT people have "several"
solutions for it.

Best practice: Go to a Cobol provider.... or Java-based vendor for re-
engineering. Definitely you have a budget for it. Get several vendor
solutions for re-engineering and concentrate even more with budgets.

http://www.computerworld.com.au/index.php/id;1914725230;fp;;fpid;;pf;1

A link above would somehow help... but then again, somehow?!? Most
successful developers knew Cobol, that is why we are here in this
Cobol Google group anyway.
```

##### ↳ ↳ Re: System Conversion - An Overview

- **From:** HansJ <hjigel@kup.de>
- **Date:** 2007-10-30T07:37:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193755022.300465.265380@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<1193750415.054573.294890@q3g2000prf.googlegroups.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <1193750415.054573.294890@q3g2000prf.googlegroups.com>`

```
On 30 Okt., 14:20, Rene_Surop <infodynamics...@yahoo.com> wrote:
> Considering HansJ situation..... and with such a magnitude of
> requirements. Woh! System language conversion is not my best solution.
…[14 more quoted lines elided]…
> Cobol Google group anyway.

Rene,
I'm not advocating to convert a COBOL application to Java, I like to
know if anyone has seen a successful project od this type.

This question was raised because of a requirement in an RFP that
included that the target language would be Java where the original
language was COBOL (Unisys UCOB).

Regards HansJ
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

- **From:** bill@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2007-10-30T15:10:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5oovr1Fnvtu4U2@mid.individual.net>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <1193750415.054573.294890@q3g2000prf.googlegroups.com> <1193755022.300465.265380@k79g2000hse.googlegroups.com>`

```
In article <1193755022.300465.265380@k79g2000hse.googlegroups.com>,
	HansJ <hjigel@kup.de> writes:
> On 30 Okt., 14:20, Rene_Surop <infodynamics...@yahoo.com> wrote:
>> Considering HansJ situation..... and with such a magnitude of
…[24 more quoted lines elided]…
> 

Well, now that I know this is in answer to an RFP, I can put on my
contractor hat (after dusting it off as I haven't been in that world
for over two decades) and suggest bringing up my question to the
person putting out the RFP and if the answer is either inadequate
or demonstrates a complete lack of knowledge on the subject by the
proposing organization, a "no bid" might be the correct answer.

bill
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

_(reply depth: 4)_

- **From:** HansJ <hjigel@kup.de>
- **Date:** 2007-10-30T09:44:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193762697.301448.282240@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<5oovr1Fnvtu4U2@mid.individual.net>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <1193750415.054573.294890@q3g2000prf.googlegroups.com> <1193755022.300465.265380@k79g2000hse.googlegroups.com> <5oovr1Fnvtu4U2@mid.individual.net>`

```
On 30 Okt., 16:10, b...@cs.uofs.edu (Bill Gunshannon) wrote:
> In article <1193755022.300465.265...@k79g2000hse.googlegroups.com>,
>         HansJ <hji...@kup.de> writes:
…[38 more quoted lines elided]…
>

we did not bit.

You might be correct with your assumption "demonstrates a complete
lack of knowledge on the subject".

Regards HansJ

> --
> Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
> b...@cs.scranton.edu     |  and a sheep voting on what's for dinner.
> University of Scranton   |
> Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-10-30T19:48:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ifgmab9ihon5e@corp.supernews.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <1193750415.054573.294890@q3g2000prf.googlegroups.com> <1193755022.300465.265380@k79g2000hse.googlegroups.com>`

```

"HansJ" <hjigel@kup.de> wrote in message 
news:1193755022.300465.265380@k79g2000hse.googlegroups.com...
> On 30 Okt., 14:20, Rene_Surop <infodynamics...@yahoo.com> wrote:
>> Considering HansJ situation..... and with such a magnitude of
…[26 more quoted lines elided]…
>

I don't know about COBOL to Java.  We are doing it at work now but it will 
take many years before it will succeed or fail. Actuall I can tell you now 
that because of the huge amount of money being spent it will be called a 
success even if it fails.

You can go from COBOL to Java byte code user PerCOBOL.  Although I have not 
used it those I know who have say it works well.
```

#### ↳ Re: [OT] System Conversion - An Overview

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-10-30T21:30:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5opm2vFnnl68U1@mid.individual.net>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fg6u2d$qvk$1@reader1.panix.com...
>
> As an extension of an earlier thread regarding a COBOL-to-Java
…[45 more quoted lines elided]…
> to take the lead in the introduction of a new order of things.

Only if you're a sissy. REAL Men embrace change and have no problem with 
being responsible for it. :-)

> Because the
> innovator has for enemies all those who have done well under the old
> conditions, and lukewarm defenders in those who may do well under the new.

And should be lobbying both camps with the promises of the new and 
explaining how this change will benefit all concerned.

> This coolness arises partly from fear of the opponents, who have the laws
> on their side, and partly from the incredulity of men, who do not readily
> believe in new things until they have had a long experience of them.

That's part of a leader's job; address their incredulity and convert it into 
support. Part of the challenge is to motivate people to  be at worst, 
non-committal ("Ok, let's wait and see..."), at best, enthusiastic,  to see 
new systems.

Although there may be SOME parallels between Renaissance Italy and the 
modern Business World, for the most part, they are different. Machiavelli 
would be out of his depth in the politics, subtleties, and complexity of 
modern Board Rooms.

Pete.
```

##### ↳ ↳ Re: [OT] System Conversion - An Overview

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-31T00:16:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fg8hhd$mc$1@reader1.panix.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <5opm2vFnnl68U1@mid.individual.net>`

```
In article <5opm2vFnnl68U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
><docdwarf@panix.com> wrote in message news:fg6u2d$qvk$1@reader1.panix.com...

[snip]

>> All in all, it is usually a good thing to remember what Machiavelli had to
>> say about the introduction of new systems
…[9 more quoted lines elided]…
>being responsible for it. :-)

Just like military officers have no problems leading their men over the 
tops of the trenches... and the Gallipoli-like results which may ensue.

>
>> Because the
…[4 more quoted lines elided]…
>explaining how this change will benefit all concerned.

That might be the case, as well... but for me, I will leave lobbying to 
the lobbyists and selling to the salesfolk; they have their jobs and I 
have mine.

>
>> This coolness arises partly from fear of the opponents, who have the laws
…[6 more quoted lines elided]…
>new systems.

'Over the top, boys... I'll lead the way!'

>
>Although there may be SOME parallels between Renaissance Italy and the 
>modern Business World, for the most part, they are different. Machiavelli 
>would be out of his depth in the politics, subtleties, and complexity of 
>modern Board Rooms.

I'll take that as the Voice of Experience, one that spent much time in 
Renaissance Italy.  I don't know many folks who spent time in modern Board 
Rooms who have become Pope, as did Rodrigo Borgia.

DD
```

###### ↳ ↳ ↳ Re: [OT] System Conversion - An Overview

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-10-31T13:43:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5orf4qFnp62tU1@mid.individual.net>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <5opm2vFnnl68U1@mid.individual.net> <fg8hhd$mc$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fg8hhd$mc$1@reader1.panix.com...
> In article <5opm2vFnnl68U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[24 more quoted lines elided]…
> tops of the trenches... and the Gallipoli-like results which may ensue.

Death or Glory! THAT's the stuff for REAL men...

(I recently finished reading the best book on Gallipoli I have ever come 
across. Obviously, this particular battle is woven into our culture and the 
"Spirit of Anzac" is something we grow up with. Despite the courage and 
tenacity shown by both sides, there is no doubt that it was a real tragedy 
for all concerned. The book I just finished is called "Letters from the 
coffin trenches" by Ken Catran. It is the best anti-war novel I have ever 
read. Understated, doesn't preach, but has been extremely well researched, 
and gives insight into the mores and attitudes of the times, both at home 
and at war.)

The important point here is that in industry, when implementing change, 
people don't normally die.

(Having said that, I have worked on two projects where team members DID die, 
mainly as a result of work related stress. It made me think, and I have 
never had this happen on any of my projects. Much as I may hate the thought 
of being late or failing to achieve, the thought of people breaking down or 
dying is far more repugnant...)

>
>>
…[11 more quoted lines elided]…
>

That's fine if you have the people... :-)

>>
>>> This coolness arises partly from fear of the opponents, who have the 
…[13 more quoted lines elided]…
>

Ah, the exhilaration... !
>>
>>Although there may be SOME parallels between Renaissance Italy and the
…[5 more quoted lines elided]…
> Renaissance Italy.

I have a blue phone box, you know...

> I don't know many folks who spent time in modern Board
> Rooms who have become Pope, as did Rodrigo Borgia.

I heard that most Cardinals in the Catholic Church do Business Studies and 
are required to put some time in managing aspects of the Church's financial 
empire,(career progression?). Some are even Ivy League graduates (could be 
Honorary Degrees...)

The modern Church, like modern Business, is a very long way from how things 
were done in the Middle Ages.

Pete.
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-10-31T07:30:39-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193841039.657986.166280@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5orf4qFnp62tU1@mid.individual.net>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <5opm2vFnnl68U1@mid.individual.net> <fg8hhd$mc$1@reader1.panix.com> <5orf4qFnp62tU1@mid.individual.net>`

```
On 31 Oct, 13:43, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> <docdw...@panix.com> wrote in messagenews:fg8hhd$mc$1@reader1.panix.com...
> > In article <5opm2vFnnl6...@mid.individual.net>,
…[37 more quoted lines elided]…
>

Many years ago, I read a book (which I can highly recommend) called
"The reason why" published by Penguin and authored by Cecil Woodham-
Smith. It covered the Sebastopol campaign and the battle of Balaclava.
If you have ever seen the film of the charge of the Light Brigade with
Vanessa Redgrave then it accurately reflects the contents of the book.
I had thought that the film was a joke until I read the book.
```

###### ↳ ↳ ↳ Re: [OT] System Conversion - An Overview

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-31T22:54:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgb13m$920$1@reader1.panix.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <5opm2vFnnl68U1@mid.individual.net> <fg8hhd$mc$1@reader1.panix.com> <5orf4qFnp62tU1@mid.individual.net>`

```
In article <5orf4qFnp62tU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[29 more quoted lines elided]…
>Death or Glory! THAT's the stuff for REAL men...

Such 'REAL men' seem to ignore some simple, basic teachings that have held 
for a few millennia, it seems... Qoh.IX:4 - 5: 'For to him that is joined 
to all the living there is hope: for a living dog is better than a dead 
lion.  For the living know that they shall die: but the dead know not any 
thing, neither have they any more a reward; for the memory of them is 
forgotten.'

Or as a more modern author put it, 'Is there glory in a little heap of 
whitened bones?'

[snip]

>The important point here is that in industry, when implementing change, 
>people don't normally die.

That does not necessitate the conclusion, Mr Dashwood, that no lessons 
from the military might be learnt.

[snip]

>> That might be the case, as well... but for me, I will leave lobbying to
>> the lobbyists and selling to the salesfolk; they have their jobs and I
…[3 more quoted lines elided]…
>That's fine if you have the people... :-)

I'd disagree... it seems readily accepted that not everyone can be a 
decent programmer; in like manner not everyone can be a decent lobbyist or 
salesperson.  If someone of the right skills/temperment is not there to do 
a given job then the job tends to get done badly or not at all.

One can hook an Arabian stallion up to a wagon to haul bricks... but if 
one has a lot of hauling to do one might consider getting a more 
appropriate Clydesdale.

[snip]

>> I don't know many folks who spent time in modern Board
>> Rooms who have become Pope, as did Rodrigo Borgia.
…[4 more quoted lines elided]…
>Honorary Degrees...)

I have heard many things... some of them I've even seen myself.  I don't 
know of a Pope lately who comes from the ranks of what you describe as 
'most Cardinals'.

>
>The modern Church, like modern Business, is a very long way from how things 
>were done in the Middle Ages.

As the Germans say, Mr Dashwood, 'plus ca change, plus c'est la meme 
chose'; those who learn what Santayana said about the mistakes of the past 
are doomed to repeat it.

DD
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-10-31T07:21:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193840492.880726.4060@z9g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<fg8hhd$mc$1@reader1.panix.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <5opm2vFnnl68U1@mid.individual.net> <fg8hhd$mc$1@reader1.panix.com>`

```
On 31 Oct, 00:16, docdw...@panix.com () wrote:
> In article <5opm2vFnnl6...@mid.individual.net>,
>
…[21 more quoted lines elided]…
>

Gallipoli was a disaster because of the prevarication of the officers
who failed to realise the dangers of being sniped upon by Turks on
surrounding hills. So they leisurely organised cricket matches rather
than marching off of the beachhead.
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-10-31T23:01:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgb1g9$e8j$1@reader1.panix.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <5opm2vFnnl68U1@mid.individual.net> <fg8hhd$mc$1@reader1.panix.com> <1193840492.880726.4060@z9g2000hsf.googlegroups.com>`

```
In article <1193840492.880726.4060@z9g2000hsf.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 31 Oct, 00:16, docdw...@panix.com () wrote:
>> In article <5opm2vFnnl6...@mid.individual.net>,
…[27 more quoted lines elided]…
>than marching off of the beachhead.

I was not there, of course, and rely on what I can recall reading in 
various places... but what I recall is echoed by 
http://en.wikipedia.org/wiki/Battle_of_Gallipoli#August_offensive :

--begin quoted text:

The landing at Suvla Bay was only lightly opposed but the British 
commander, Lieutenant-General Sir Frederick Stopford, had so diluted his 
early objectives that little more than the beach was seized. Once again 
the Turks were able to win the race for the high ground of the Anafarta 
Hills thereby rendering the Suvla front another case of static trench 
warfare.

[snip]

The New Zealanders held out on Chunuk Bair for two days before relief was 
provided by two New Army battalions from the Wiltshire and Loyal North 
Lancashire Regiments. A massive Turkish counter-attack, led in person by 
Mustafa Kemal, swept these two battalions from the heights.

Of the 760 men of the New Zealanders' Wellington Battalion who reached the 
summit, 711 were casualties.

[snip]

Following the landing at Suvla Bay, casualties among the opposing armies 
were particularly high, and the hot and humid weather made the stench of 
bodies especially nauseating. A day's truce was arranged to facilitate the 
removal of the dead and wounded; this momentary contact led to a strange 
camaraderie between the armies much like the Christmas truce of 1914.

--end quoted text

An utter horror.

DD
```

#### ↳ Re: [OT] System Conversion - An Overview

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-10-30T19:44:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ifgepdp96ov45@corp.supernews.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:fg6u2d$qvk$1@reader1.panix.com...
>
> As an extension of an earlier thread regarding a COBOL-to-Java
…[55 more quoted lines elided]…
>

I have learned that we now have  around 860 contractors working on our "new" 
system.  I put new in quotes because the current system was used for the 
specifications for the new system. That 860 number is after they got rid of 
a lot of SAP people.  They tried to replace one subsystem with 80% vanilla 
SAP and 20% ABAP, but the vanilla SAP could not do even 60%.  All of this 
just to say they no longer have COBOL and now have the new and improved and 
20% to 30% slower state of the art Java. In one lunch room they have a huge 
chart of system development processes and paperwork deliverables. If you 
live in the USA then sorry, it it your tax dollars at work :-(
```

##### ↳ ↳ Re: [OT] System Conversion - An Overview

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-30T19:57:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ifknbime540d2@news.supernews.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com>`

```
Charles Hottel wrote:
>
> I have learned that we now have  around 860 contractors working on
…[8 more quoted lines elided]…
> USA then sorry, it it your tax dollars at work :-(

This echos what I've learned from long experience.

A large system designed from scratch will not work and cannot be made to 
work. You have to start over with a working, smaller system. However, a 
large system, produced by expanding the dimensions of a smaller system, does 
not behave like the smaller system.

In a large system, malfunction, or even total non-function, may not be 
detectable for long periods, if ever. The total behavior of large systems 
cannot be predicted.

Some complex systems actually work. If a system is working, leave it alone.

In setting up a new system, tread softly. You may be disturbing another 
system that is actually working.
```

###### ↳ ↳ ↳ Re: [OT] System Conversion - An Overview

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-10-31T13:50:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5orfh5Fo07d8U1@mid.individual.net>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com> <13ifknbime540d2@news.supernews.com>`

```


"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:13ifknbime540d2@news.supernews.com...
> Charles Hottel wrote:
>>
…[26 more quoted lines elided]…
> system that is actually working.

Somewhat surprisingly, I actually agree with this. While I enjoy change and 
large challenges, I think your analysis is pretty much on the button, Jerry.

One of the reasons I get excited about Web Services and OO components is 
because you can implement them without the risk of destroying something else 
which, as you say, could be working fine.

My experience bears out what you say about starting with a smaller system 
and expanding it incrementally. Obviously, encapsulated building blocks 
facilitate this.

Pete.
```

###### ↳ ↳ ↳ Re: [OT] System Conversion - An Overview

_(reply depth: 4)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-10-31T10:02:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zN0Wi.46633$q7.21015@bignews3.bellsouth.net>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com> <13ifknbime540d2@news.supernews.com> <5orfh5Fo07d8U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote:
>
> My experience bears out what you say about starting with a smaller system and expanding it incrementally. Obviously, encapsulated 
> building blocks facilitate this.

I don't agree that you should always start small and scale up. Build a system
modularly, absolutely. But not all designs scale up well. For some applications,
you need to "thing big" from the beginning, or it may not scale up properly. Or,
sometimes you miss opportunities if you "think small" but eventually will
"need big". Designing toward the actual target seems more appropriate to me.
Parhaps I'm just lucky, but I've never designed a system that didn't work as
well or better than the user's expectations.
```

##### ↳ ↳ Re: [OT] System Conversion - An Overview

- **From:** Robert <no@e.mail>
- **Date:** 2007-10-30T22:52:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i1gi39darb3r0175mpg7ttie21572ktn1@4ax.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com>`

```
On Tue, 30 Oct 2007 19:44:40 -0400, "Charles Hottel" <chottel@earthlink.net> wrote:

>I have learned that we now have  around 860 contractors working on our "new" 
>system.  I put new in quotes because the current system was used for the 
>specifications for the new system. That 860 number is after they got rid of 
>a lot of SAP people.  

SAP people are usually very good, and very expensve. IBMers are just very expensive.

>They tried to replace one subsystem with 80% vanilla 
>SAP and 20% ABAP, but the vanilla SAP could not do even 60%. 

SOA is about turning the old code into a Service, rather than rewriting it.

>All of this 
>just to say they no longer have COBOL and now have the new and improved and 
>20% to 30% slower state of the art Java. 

SAP is written in C and ABAP, not Java. If it's only 20-30% slower, it's better than most
new systems, which are typically 2-3 TIMES slower. Tuning often produces dramatic
improvements in speed.

>In one lunch room they have a huge 
>chart of system development processes and paperwork deliverables. 

In the old days, deliverables were things like Code Complete and Integration Testing
Passed. Now, deliverables are paperwork attesting to those milestones. Someone should ask
why, if development was complete two months ago, they're still making code changes. 

>If you live in the USA then sorry, it it your tax dollars at work :-( 

"Pessimist drowns in half empty bathtub."  :)

YOU could be one of those 860 contractors. If you can't beat 'em, join 'em.
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-10-31T07:24:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193840655.471927.266490@19g2000hsx.googlegroups.com>`
- **In-Reply-To:** `<7i1gi39darb3r0175mpg7ttie21572ktn1@4ax.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com> <7i1gi39darb3r0175mpg7ttie21572ktn1@4ax.com>`

```
On 31 Oct, 04:52, Robert <n...@e.mail> wrote:

> >If you live in the USA then sorry, it it your tax dollars at work :-(
>
> "Pessimist drowns in half empty bathtub."  :)
>

And an engineer would point out that the bathtub is twice the size
that it needs to be.
```

###### ↳ ↳ ↳ Re: System Conversion - An Overview

_(reply depth: 4)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-10-31T14:06:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ihkhc8ss43nd0@news.supernews.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com> <7i1gi39darb3r0175mpg7ttie21572ktn1@4ax.com> <1193840655.471927.266490@19g2000hsx.googlegroups.com>`

```
Alistair wrote:
> On 31 Oct, 04:52, Robert <n...@e.mail> wrote:
>
…[7 more quoted lines elided]…
> that it needs to be.

No, the dude drowned, didn't he?
```

###### ↳ ↳ ↳ Re: [OT] System Conversion - An Overview

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-10-31T18:55:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ii1uh2qo6gm45@corp.supernews.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com> <7i1gi39darb3r0175mpg7ttie21572ktn1@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:7i1gi39darb3r0175mpg7ttie21572ktn1@4ax.com...
> On Tue, 30 Oct 2007 19:44:40 -0400, "Charles Hottel" 
> <chottel@earthlink.net> wrote:
>

<snip>

> SAP is written in C and ABAP, not Java. If it's only 20-30% slower, it's 
> better than most
…[3 more quoted lines elided]…
>
Yes I know. I did not make it clear (perhaps because I posted about this 
before).  They will keep whatever they have in SAP and now they will use 
Java to develop the rest.  Othe rsubsytems will be totally conveted to Java.


<snip>
```

##### ↳ ↳ Re: System Conversion - An Overview

- **From:** HansJ <hjigel@kup.de>
- **Date:** 2007-10-31T04:47:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1193831222.228619.123680@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<13ifgepdp96ov45@corp.supernews.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <13ifgepdp96ov45@corp.supernews.com>`

```
... They tried to replace one subsystem with 80% vanilla
> SAP and 20% ABAP, but the vanilla SAP could not do even 60%.  All of this
> just to say they no longer have COBOL and now have the new and improved and
> 20% to 30% slower state of the art Java. In one lunch room they have a huge
> chart of system development processes and paperwork deliverables. If you
> live in the USA then sorry, it it your tax dollars at work :-(

Charles,
the trend is definitely going to replace existing individual
application with packaged software. If it makes sense or not is
another question, but I'd admit that in many cases it makes sense.
I have seen successful and unseccessfull attempts to replace large
COBOL applications with both packages (mostly SAP) and individual
developments. So there is no reason to use an unseccessfull example as
a general statement.
Regarding the tax dollars spent, no I'm not living in the US...

Regards HansJ
```

#### ↳ Re: System Conversion - An Overview

- **From:** Ranger <tarr@tiburontech.com>
- **Date:** 2007-11-04T14:26:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1194215218.855930.75200@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<fg6u2d$qvk$1@reader1.panix.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com>`

```
On Oct 30, 4:38 am, docdw...@panix.com () wrote:
> As an extension of an earlier thread regarding a COBOL-to-Java
> conversion... some meanderings.
>


I did want to provide a summary of a response that I provided to DD
privately, but maybe the group could benefit as well.

I own a technology company that provides an automated migraton for
COBOL based applications. Most of our clients have IDMS, Datacom, IMS,
VSAM and Adabas and are looking to migrate to DB2, Oracle or SQL
Server.

I am hearing from our clients that they need to migrate for
predominately two reasons - we getting off of the mainframe or we feel
at risk running some of the older databases/files. For those looking
to stay on the mainframe we have been migrating them to DB2 and rarely
do we hear a request for  JAVA. Regarding clients that are migrating
off of the mainframe we are hearing an increased amount of requests to
convert part or all of the COBOL application to JAVA. We have one
client that said "I want to get off the mainframe, convert to JAVA and
outsource to India". Other client comments are "I had to sell JAVA to
ge the project funded".

What we are finding when clients actually migrate, they begin to see
the value in the COBOL based applications. They have years of
experience, and a temendous amount of business logic that no longer
has a subject matter expert.

Several of our projects started out with the intention to migrate the
COBOL applicatons to JAVA, and then they realize the cost and risk,
and usually determine the "customer facing, high value" functions will
be written in JAVA. At the end of the day, the application remains 95%
COBOL.

I am responding to a client RFP this month, the original conversation
was "We have to get off the maniframe, its a CIO directive. We thought
that this would be a good time to go to the board one time and ask for
the funding to get off the mainframe and convert to JAVA". My original
comment to them was to migrate the COBOL mainframe application to
COBOL distributed platform and take inventory. SOA and web services
can be initiated through COBOL and you can leverage your business
logic embedded in your existing programs. The training requirements
for coming off of the mainframe will be limited to environmental
issues, you can protect the productivity and experience of your staff
as well. At first they did not like that thought, and now, 60 days
later, they are asking for three approaches. The first is COBOL to
COBOL, the second is a hybrid, with all the heavy lifting being done
by COBOL, and the online/high-value programs being JAVA, and the third
option is all JAVA.

I hope this group benefits by some of the feedback that I have been
hearing. We have migrated over 50M lines of COBOL code the past few
years, with less than 2% going to JAVA. It is however, being requested
as an option on almost all of our "getting off the mainframe" RFP's.

Ranger
```

##### ↳ ↳ Re: System Conversion - An Overview

- **From:** docdwarf@panix.com ()
- **Date:** 2007-11-05T10:24:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgmr1a$ieu$1@reader1.panix.com>`
- **References:** `<fg6u2d$qvk$1@reader1.panix.com> <1194215218.855930.75200@d55g2000hsg.googlegroups.com>`

```
In article <1194215218.855930.75200@d55g2000hsg.googlegroups.com>,
Ranger  <tarr@tiburontech.com> wrote:

>I am hearing from our clients that they need to migrate for
>predominately two reasons - we getting off of the mainframe or we feel
>at risk running some of the older databases/files. For those looking
>to stay on the mainframe we have been migrating them to DB2 and rarely
>do we hear a request for  JAVA.

Outside of what is said in The Press about such matters... I wonder what
gives them this 'feeling'.  Are their systems maxing out, are they having
trouble hiring folks for the pittance salaries they offer, are their own
people incapable of being trained in these technologies... all 
possibilities
and others, I'm sure, but asking those questions might deny your own
organisation some business.

'Oh, you don't need to migrate anything... all you need is to train some
folks and then slap on some golden handcuffs to keep them on the job!'

>Regarding clients that are migrating
>off of the mainframe we are hearing an increased amount of requests to
>convert part or all of the COBOL application to JAVA. We have one
>client that said "I want to get off the mainframe, convert to JAVA and
>outsource to India".

To which one might respond 'And you believe that denying yourself control 
of the resource of IT ownership would be of benefit... how?'

>Other client comments are "I had to sell JAVA to
>ge the project funded".

Welcome to the World of Business, aye... 'everyone's talking about 
'longer, lower, wider and with port-holes, we can't get left behind!'

>
>What we are finding when clients actually migrate, they begin to see
>the value in the COBOL based applications. They have years of
>experience, and a temendous amount of business logic that no longer
>has a subject matter expert.

Oooooooooo... don't get me started on the Death of Business Analyst. 
'COBOL is self-documenting so we only need programmers, not analysts... 
but keep those programmers out of the meetings, they tend to be 
distracting with all this 'logic' stuff.'

>
>Several of our projects started out with the intention to migrate the
…[3 more quoted lines elided]…
>COBOL.

On the front end, nice screens, drop-down menus, easy-to-understand error 
text ('1961 not a leap year' instead of 'XMB17355 - DATE ERROR')... on the 
inside code that's been running for the past two decades.  I have trouble 
understanding why many folks consider this a problem... 'Well, all our 
salesfolk drive cars to visit clients, we should have all our deliveries 
made by car, too... no trucks!'

>
>I am responding to a client RFP this month, the original conversation
>was "We have to get off the maniframe, its a CIO directive. We thought
>that this would be a good time to go to the board one time and ask for
>the funding to get off the mainframe and convert to JAVA".

Who was the general who tried to demonstrate the loyalty of his troops by 
making them march off a cliff?

[snip]

>I hope this group benefits by some of the feedback that I have been
>hearing. We have migrated over 50M lines of COBOL code the past few
>years, with less than 2% going to JAVA.

Thanks much for this view from Another Side of the Irregular Polygon of 
Life.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
