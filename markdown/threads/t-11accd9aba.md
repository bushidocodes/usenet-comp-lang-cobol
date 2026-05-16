[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: Trouble in Paradise

_104 messages · 13 participants · 2011-10_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: Trouble in Paradise

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-06T12:54:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f4924F1huU1@mid.individual.net>`

```
Does anyone here have any experience with programming nautical systems?

How can a modern container ship run into a well marked and charted reef?

http://www.sunlive.co.nz/news/17087-oil-leak-headed-mayor-island.html

You can see from the photos how beautiful this region is. Now we have a 2 
kilometre oil slick from a ship which they assured us yesterday had no 
rupture to its fuel tanks and was NOT leaking oil.

Anyone have any comments about modern nautical systems? Is this an 
application area that should be addressed?

It saddens me a lot to see these pictures and think it could have been 
avoided with decent technology.

Pete.
```

#### ↳ Re: OT: Trouble in Paradise

- **From:** Doug Miller <doug_at_milmacdotcom@example.com>
- **Date:** 2011-10-05T20:35:26-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6it4t$md5$1@dont-email.me>`
- **In-Reply-To:** `<9f4924F1huU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net>`

```
On 10/5/2011 7:54 PM, Pete Dashwood wrote:
> Does anyone here have any experience with programming nautical systems?
>
> How can a modern container ship run into a well marked and charted reef?

Human error is the simplest, and most obvious, explanation, and I have 
little doubt that it will prove to be the correct one as well.
>
> http://www.sunlive.co.nz/news/17087-oil-leak-headed-mayor-island.html
…[6 more quoted lines elided]…
> application area that should be addressed?

Probably not. Surely there will be an inquest. Its findings are almost a 
foregone conclusion: the board of inquiry will determine that someone 
screwed up, that some human being whose job it was to read nav charts 
and avoid hazards such as known reefs, failed to do so. Whether this was 
due to inattention, drug or alcohol use, a medical or psychiatric 
condition, sleep deprivation, deliberate intent, or ordinary 
incompetence will presumably be determined by the board -- but with 
respect to your question, which of these turns out to be the cause is 
really irrelevant: they're all human problems which don't have technical 
solutions.

Perhaps the board will determine the root cause to be some sort of 
equipment malfunction -- but then we're back to the human factor, 
specifically incompetence, as the proximate cause: for whatever reason 
(lack of training, carelessness, stupidity, etc.) the human operators of 
the vessel were unprepared to deal with the malfunction. Whether it's 
their fault for not carrying out procedures properly, or someone else's 
fault for not training them in the proper procedures, or a combination 
thereof, it's still, at bottom, a human problem.
>
> It saddens me a lot to see these pictures and think it could have been
> avoided with decent technology.

Probably not. Remember the Exxon Valdez? What technology could have 
prevented a drunken master from misreading or ignoring his navigation aids?
```

##### ↳ ↳ Re: OT: Trouble in Paradise

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-06T21:19:58+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f56liFnkjU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6it4t$md5$1@dont-email.me>`

```
Doug Miller wrote:
> On 10/5/2011 7:54 PM, Pete Dashwood wrote:
>> Does anyone here have any experience with programming nautical
…[42 more quoted lines elided]…
> aids?

Ever heard of TCAS, Doug?

It prevents arcraft colliding with each other.  Irrespective of the 
incompetence or otherwise of the pilot. (If a pilot overrides it, there will 
be a crash and this has led to most of the World's major airlines training 
their pilots to obey TCAS before they obey ATC.)

Human error is certainly a factor, but where we have technology that can 
take a human out of the loop that is one less factor to be considered.

I don't know much about what passes for shipping navigation aids these days 
(hence my question) but I don't think it is impossible to build something 
that can prevent this kind of stupidity. I sold my boat (equipped with every 
cutting edge navigational aid) in 1987. Even then we had Sat Nav and 
automatic depth alarms. Technology has progressed much since those days. If 
a depth sounder can "look down" why can't it "look ahead"?

It wouldn't be "too hard" to fit known reefs in high risk areas with 
transponders, or perhaps an underwater equivalent.

If there is no such system it is about time there was... The current 
technology could certainly support it.

Even if there aren't human costs, there are still significant costs to the 
environment.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2011-10-06T04:17:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2qq87l39c7vpldnna9ub7ckki09qfbra4@4ax.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6it4t$md5$1@dont-email.me> <9f56liFnkjU1@mid.individual.net>`

```
On Thu, 6 Oct 2011 21:19:58 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Doug Miller wrote:
>> On 10/5/2011 7:54 PM, Pete Dashwood wrote:
…[50 more quoted lines elided]…
>their pilots to obey TCAS before they obey ATC.)


Don't overestimate what TCAS does - There are *no* TCAS
implementations where an aircraft will automatically respond to a TCAS
"resolution advisory".  That's information presented to the pilot(s),
typically a suggestion to climb or descent to avoid the conflict, and
the pilots need to take the appropriate action.

Indeed, TCAS RAs normally take precedence over ATC instructions (TCAS
inherently has more current information than ATC does) and a failure
to respect that priority has led to at least one collision (a 757 /
Tu-154 over Europe in 2002).

TCAS depends on both aircraft having appropriate transponders which
are operating.  At least once accident occurred because of an
non-operating transponder (a 737 / Embraer Legacy collision over
Brazil in 2006).

TCAS generates a certain number of false alarms, and is uncoordinated
with things like ground proximity warnings, and aircraft performance
limitations.

In the marine world, AIS is a rough equivalent to TCAS, although
again, is dependent on all the vessels participating.

In any event, you'd probably be looking at something like the Ground
Proximity Warning System (GPWS - radar based) or EGPWS (Enhanced GWPWS
- position and map based) as a model for this function.  But those are
also warning systems that a crew could ignore.

But I'd be surprised if some marine navigation systems don't already
provide a map based warning system.  Which, of course, is subject to
being ignored.

Actually automatically taking an action based on a warning from one of
these systems is a huge step, fraught with all sorts of difficulties,
and introduces huge safety issues all on its own.  The military *does*
do that to some extent with terrain-follow-radar on some military
aircraft that fly at very low levels, but those have a less than
stellar safety record).

Something to consider for marine sub-surface hazards is that many of
them are *very* poorly charted, often including large errors and
flat-out omissions.  Also, some hazards are not actually stationary
(sandbars in rivers and near shores, for example).  Although from your
description that would not be an issue for this accident.  Even for
aircraft systems, new hazards appear on a regular basis (someone
builds a new radio antenna, for example), and there is often a time
lag between the hazard appearing and those hazards getting into the
map databases on all the aircraft.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T10:51:03+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f6m69FflmU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6it4t$md5$1@dont-email.me> <9f56liFnkjU1@mid.individual.net> <a2qq87l39c7vpldnna9ub7ckki09qfbra4@4ax.com>`

```
Robert Wessel wrote:
> On Thu, 6 Oct 2011 21:19:58 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[104 more quoted lines elided]…
> map databases on all the aircraft.

Thanks Robert,

a reasonable and informative response.

I take your points, but I'm so upset by this I just think it must be 
possible to do SOMETHING... :-)

Maybe people are already working on it.

And we can all agree that human error will always be a factor, unless humans 
are removed from the loop and most people have a problem with that :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2011-10-06T04:28:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i4tq87tubihpscih58g5mhhnplqhugsrg2@4ax.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6it4t$md5$1@dont-email.me> <9f56liFnkjU1@mid.individual.net>`

```
On Thu, 6 Oct 2011 21:19:58 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Doug Miller wrote:
>> On 10/5/2011 7:54 PM, Pete Dashwood wrote:
…[50 more quoted lines elided]…
>their pilots to obey TCAS before they obey ATC.)



Don't overestimate what TCAS does - There are *no* TCAS
implementations where an aircraft will automatically respond to a TCAS
"resolution advisory".  That's information presented to the pilot(s),
typically a suggestion to climb or descent to avoid the conflict, and
the pilots need to take the appropriate action.

Indeed, TCAS RAs normally take precedence over ATC instructions (TCAS
inherently has more current information than ATC does) and a failure
to respect that priority has led to at least one collision (a 757 /
Tu-154 over Europe in 2002).

TCAS depends on both aircraft having appropriate transponders which
are operating.  At least once accident occurred because of an
non-operating transponder (a 737 / Embraer Legacy collision over
Brazil in 2006).

TCAS generates a certain number of false alarms, and is uncoordinated
with things like ground proximity warnings, and aircraft performance
limitations.

In the marine world, AIS is a rough equivalent to TCAS, although
again, is dependent on all the vessels participating.

In any event, you'd probably be looking at something like the Ground
Proximity Warning System (GPWS - radar based) or EGPWS (Enhanced GWPWS
- position and map based) as a model for this function.  But those are
also warning systems that a crew could ignore.

But I'd be surprised if some marine navigation systems don't already
provide a map based warning system.  Which, of course, is subject to
being ignored.

Actually automatically taking an action based on a warning from one of
these systems is a huge step, fraught with all sorts of difficulties,
and introduces huge safety issues all on its own.  The military *does*
do that to some extent with terrain-follow-radar on some military
aircraft that fly at very low levels, but those have a less than
stellar safety record).

Something to consider for marine sub-surface hazards is that many of
them are *very* poorly charted, often including large errors and
flat-out omissions.  Also, some hazards are not actually stationary
(sandbars in rivers and near shores, for example).  Although from your
description that would not be an issue for this accident.  Even for
aircraft systems, new hazards appear on a regular basis (someone
builds a new radio antenna, for example), and there is often a time
lag between the hazard appearing and those hazards getting into the
map databases on all the aircraft.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

- **From:** Doug Miller <doug_at_milmacdotcom@example.com>
- **Date:** 2011-10-06T07:38:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6k3vd$pbl$1@dont-email.me>`
- **In-Reply-To:** `<9f56liFnkjU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6it4t$md5$1@dont-email.me> <9f56liFnkjU1@mid.individual.net>`

```
On 10/6/2011 4:19 AM, Pete Dashwood wrote:
> Doug Miller wrote:
>> On 10/5/2011 7:54 PM, Pete Dashwood wrote:
…[45 more quoted lines elided]…
> Ever heard of TCAS, Doug?

Yep.
>
> It prevents arcraft colliding with each other.

*If* it is functioning properly.
*If* it has not been disabled.
Etc.

> Irrespective of the
> incompetence or otherwise of the pilot. (If a pilot overrides it, there will
…[4 more quoted lines elided]…
> take a human out of the loop that is one less factor to be considered.

If you take the human out of the loop entirely, you have *no* means of 
compensating for equipment failure.
>
> I don't know much about what passes for shipping navigation aids these days
> (hence my question) but I don't think it is impossible to build something
> that can prevent this kind of stupidity.

I do think it's impossible. It's certainly possible to build something 
that will _reduce its likelihood_, perhaps reduce it to insignificant 
levels, but prevent it completely, with an assurance of 100.0%? No way.

> I sold my boat (equipped with every
> cutting edge navigational aid) in 1987. Even then we had Sat Nav and
…[7 more quoted lines elided]…
> technology could certainly support it.

I agree that it could; I disagree with the premise that it can be made 
infallible.
>
> Even if there aren't human costs, there are still significant costs to the
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T10:55:41+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f6mevFhfaU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6it4t$md5$1@dont-email.me> <9f56liFnkjU1@mid.individual.net> <j6k3vd$pbl$1@dont-email.me>`

```
Doug Miller wrote:
> On 10/6/2011 4:19 AM, Pete Dashwood wrote:
>> Doug Miller wrote:
…[94 more quoted lines elided]…
>> Pete.
A good response Doug.

I don't think it can ever be infallible either (without removing a human 
from the loop and having multiple redundant computers monitoring what's 
going on... even then, I agree it will never be 100%.)

But we must be able to do something better than currently.

I take your point that the risk can be reduced in likelihood. Even that 
would seem like a step in the right direction.

I'm just heartsick over this latest and it is probably affecting my 
judgement :-)

Pete.
```

#### ↳ Re: OT: Trouble in Paradise

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-06T05:32:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1ba3bcd-f013-432a-bac1-32391d3a88d0@i33g2000yqm.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net>`

```
On Oct 6, 12:54 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Does anyone here have any experience with programming nautical systems?
>
…[13 more quoted lines elided]…
>

I've seen an excerpt from a UK documentary about a ship running
aground off of the Shetland islands. The ship's master complained that
the charts were inaccurate and showed water depth to be 25 feet where
he had hit a rock at 12 feet depth. It turned out that the charts had
been made using plumb soundings which had bracketed the rock. It took
a naval vessel with state-of-the-art sonar to prove the charts wrong.
```

##### ↳ ↳ Re: OT: Trouble in Paradise

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T11:02:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f6mquFksfU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <b1ba3bcd-f013-432a-bac1-32391d3a88d0@i33g2000yqm.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 6, 12:54 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[24 more quoted lines elided]…
> a naval vessel with state-of-the-art sonar to prove the charts wrong.

That is just plain sad.

I can assure you, Alistair, the Astrolable reef is a well-known sea mark in 
this area as many boaties fish there. It has been completely surveyed by the 
RNZN using modern technology, as has most of our coastline. It is a far cry 
from the days when Abel Tasman drew a line on a map which represented the 
West coast of the North Island, and James Cook did a figure 8 tour of both 
major islands. (Cook's map is staggering in its accuracy and looks a lot 
like satellite images of New Zealnad's coastline.) The point is that we DO 
have adequate charts and have had for decades.

I just reckon it must be possible ot do better with navigational aids than 
currently seems ot be the case.

Pete.
```

#### ↳ Re: Trouble in Paradise

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-06T11:13:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fe6dnaI0N_lUThDTnZ2dnUVZ_u2dnZ2d@earthlink.com>`
- **References:** `<9f4924F1huU1@mid.individual.net>`

```
Pete Dashwood wrote:
> Does anyone here have any experience with programming nautical
> systems?
…[6 more quoted lines elided]…
> had no rupture to its fuel tanks and was NOT leaking oil.

The attack on an unarmed cargo ship by a reef resulted in a leak of bilge 
area (probably). There's all kinds of nastiness in the bilge.

>
> Anyone have any comments about modern nautical systems? Is this an
…[4 more quoted lines elided]…
>

Decent technology is not a substitute - although some think it is - for 
common sense and mental alertness. We see reports all the time of drivers 
slavishly following GPS instructions and driving off a cliff or 100 yards 
into a bog.

Don't despair. I'm in Houston and aware of oil slicks. As oil slicks go, 
yours is virtually nothing. Various ocean dwellers, mainly bacteria, will 
take care of the oil in a matter of weeks if not days.

Last year, the BP well in the Gulf of Mexico blew out and spewed 780,000 
cubic meters of oil (4.9 million barrels). Your oil slick looks like, max, 
50 barrels.

Anyway, the BP blowout took place 18 months ago and today one can find no 
trace of it ever happening (except for our current administration's 
misguided ban on further drilling).
```

##### ↳ ↳ Re: Trouble in Paradise

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-06T21:05:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6l56s$b1b$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <fe6dnaI0N_lUThDTnZ2dnUVZ_u2dnZ2d@earthlink.com>`

```
In article <fe6dnaI0N_lUThDTnZ2dnUVZ_u2dnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:
>Pete Dashwood wrote:
>> Does anyone here have any experience with programming nautical
…[10 more quoted lines elided]…
>area (probably).

'The attack on an unarmed cargo ship by a reef'?  Honest, Ossifer, that 
tree just jumped right out and bit my car!

[snip]

>Decent technology is not a substitute - although some think it is - for 
>common sense and mental alertness.

The quote - perhaps apochryphal - is along the lines of 'I've heard enough 
about this 'artificial intelligence' stuff here.  Why can't we just go out 
and buy some the genuine kind?'

DD
```

##### ↳ ↳ Re: Trouble in Paradise

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-07T11:05:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9f6n26FmcvU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <fe6dnaI0N_lUThDTnZ2dnUVZ_u2dnZ2d@earthlink.com>`

```
HeyBub wrote:
> Pete Dashwood wrote:
>> Does anyone here have any experience with programming nautical
…[35 more quoted lines elided]…
> administration's misguided ban on further drilling).

Thanks for the encouragement, Jerry. You're probably right.

Nevertheless, we are all pretty environment conscious here and Mayor Island 
is an international venue for deep sea fishing. (Not to mention a very 
beautiful place to visit.)

I followed the BP problem with interest. If there is currently no trace that 
is an amazing result.

Pete.
```

###### ↳ ↳ ↳ Re: Trouble in Paradise

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-07T03:17:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0d1949b3-644e-45fa-a9d9-3c9513a51450@s9g2000yql.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <fe6dnaI0N_lUThDTnZ2dnUVZ_u2dnZ2d@earthlink.com> <9f6n26FmcvU1@mid.individual.net>`

```
On Oct 6, 11:05 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> HeyBub wrote:
> > Pete Dashwood wrote:
…[44 more quoted lines elided]…
>

See article http://www.sciencedaily.com/releases/2010/08/100807205655.htm
for information (as of Aug 2010) as to what happened to the oil. 49%
was chemically or naturally dispersed or evaporated or dissolved.
Which means that it is still out there but you won't see it from the
surface. Where oil companies and politicians are concerned, "out of
sight = out of mind". Where ecologists are concerned the story is very
different.
```

###### ↳ ↳ ↳ Re: Trouble in Paradise

_(reply depth: 4)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-07T16:51:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xKydnYhZuJTX6RLTnZ2dnUVZ_tmdnZ2d@earthlink.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <fe6dnaI0N_lUThDTnZ2dnUVZ_u2dnZ2d@earthlink.com> <9f6n26FmcvU1@mid.individual.net> <0d1949b3-644e-45fa-a9d9-3c9513a51450@s9g2000yql.googlegroups.com>`

```
Alistair Maclean wrote:
>>
>> I followed the BP problem with interest. If there is currently no
…[10 more quoted lines elided]…
> different.

Right. Ecologists often get exercised over things that cannot be seen, are 
not there, and even if they were there present the singular problem of 
irritating the ecologists.
```

###### ↳ ↳ ↳ Re: Trouble in Paradise

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-08T05:14:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81e4a571-6015-476b-90f6-666fc42210b3@d18g2000yql.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <fe6dnaI0N_lUThDTnZ2dnUVZ_u2dnZ2d@earthlink.com> <9f6n26FmcvU1@mid.individual.net> <0d1949b3-644e-45fa-a9d9-3c9513a51450@s9g2000yql.googlegroups.com> <xKydnYhZuJTX6RLTnZ2dnUVZ_tmdnZ2d@earthlink.com>`

```
On Oct 7, 10:51 pm, "HeyBub" <hey...@NOSPAMgmail.com> wrote:
> Alistair Maclean wrote:
>
…[14 more quoted lines elided]…
> irritating the ecologists.

Out of sight does not mean that the irritant is not there. When I was
at Uni, my tutor was an international expert in oil pollution in the
marine environment and he pointed out that spraying detergents on oil
slicks does not resolve the problem at all. It merely moves the
pollutant from the surface (where it affects cutesy animals such as
humand, dolphins, turtles and gulls) in to the water column and also
to the sea floor where it kills not at all cutesy animals such as fish
and worms (ugly critters). Still, it doesn't wash up on the beaches
and allows humans (cutesy in bikinis) to continue sunbathing in
ignorance of what is happening out at sea.

Ecologists are those who do not worry for nothing (paraphrasing Jack
the Ripper).
```

#### ↳ Re: OT: Trouble in Paradise

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-08T05:08:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net>`

```
On Oct 6, 12:54 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Does anyone here have any experience with programming nautical systems?
>
> How can a modern container ship run into a well marked and charted reef?
>

Errm... I've just finished browsing Scientific American articles re
the superluminal neutrinos at Gran Sasso, Italy, and GPS errors due to
moving satellites and signals being warped by troposphere, etc., can
lead to errors in positioning of 10-100 metres.
```

##### ↳ ↳ Re: OT: Trouble in Paradise

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-09T16:22:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fcib9Fvr3U1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 6, 12:54 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
> lead to errors in positioning of 10-100 metres.

Thanks Alistair. I think the jury is still out on the neutrinos.

The container ship however is another story.

This is a pageant of negligence, incompetence, and irresponsibility.

And that's just the efforts by NZ authorities to deal with it...

Too soon for a verdict on whether the skipper actually was asleep or drunk. 
I should think he has left the country by now and will not appear in NZ 
Courts.

Feelings here are running very high and there is deep dissatisfaction about 
the way the case is being dealt with by the media and the local authorities. 
A smokescreen of lies and prevarication is emerging and I believe the 
consequences will be serious for some people here. A 1 KM "no-go" area has 
been imposed around the ship so most of the "information" coming out is 
rumour and speculation from various vested interests. (At least one crew 
member has made serious money by talking to the media in an "unofficial" 
capacity.)The ship is apparently carrying dangerous cargo and it is yet to 
be confirmed whether this has been properly contained.

From a beach where I often walk, the ship is plainly visible and I sat down 
on a driftwood log and looked at it for a while. It is just heart-sickening.

From this same beach I have observed pods of Orca and dolphins, and there 
are a number of surf casters and fishermen who use kon-tikis from the beach 
and get really good fish. There are a variety of sea birds and I have even 
seen albatross skimming the waters just offshore. I once saw a blue penguin 
here but it re-entered the water when I approached it. In the summer, it is 
a major surf swimming beach and very popular with people who want to get 
away from the more crowded beaches at Mount Manganui and Omanu.

Earthquakes and natural disaster we can forgive because they are 
unavoidable, but this is just plain stupidity.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-09T03:59:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com> <9fcib9Fvr3U1@mid.individual.net>`

```
On Oct 9, 4:22 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
>
> The container ship however is another story.
…[7 more quoted lines elided]…
> Courts.

The first thing any maritime authority should do is arrest the ships'
officers and inprison them pending completion of investigations in to
the causes and culpabilities. Of course, that would infringe upon
their Human Rights.    :-O

>
> Feelings here are running very high and there is deep dissatisfaction about
…[11 more quoted lines elided]…
>

I watched an aerial film of the wreck with experts discussing the
likelihood of heavy weather breaking the wreck's back. You have 2000
tonnes of diesel oil to lift off of the ship and an oil slick to
contain. In the vackground could be seen what looks like a small oil
boom to restrain the oil, but it wasn't anywhere near the wreck! Talk
was of the oil hitting the shore (no mention of containing the slick
and lifting it using skimmers) and how devastating that was to the
gulls and whales and dolphins (all fish eating murderers).

I guess they will spray detergent and cause the oil to sink to the sea
floor where it will devastate the base of the ecology. Your friends
can look forward to years of being banned from landing their fish and
crustaceans because of the poisons in the oil. Still, the beaches will
be clean-ish although oil will still wash ashore for years after..

> From this same beach I have observed pods of Orca and dolphins, and there
> are a number of surf casters and fishermen who use kon-tikis from the beach
> and get really good fish. There are a variety of sea birds and I have even
> seen albatross skimming the waters just offshore. I once saw a blue penguin

It must have been really cold then.

> here but it re-entered the water when I approached it. In the summer, it is
> a major surf swimming beach and very popular with people who want to get
…[4 more quoted lines elided]…
>

Or maybe mechanical failure due to poor maintenance of the ship?

Are you involved in the cleanup? When the Cristos Bitos oil tanker
went down off of Wales I was involved in a research project based on
the dead awks and guillemots (more fish eating murderers).
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-09T21:25:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6t3gf$kkc$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com> <9fcib9Fvr3U1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com>`

```
In article <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 9, 4:22?am, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
>their Human Rights.    :-O

Leaving aside how long such a set of investigations might take, Mr 
Maclean, I believe that Garrow's assertion of 'innocent until proven 
guilty' (more recently specified to 'presumed to be innocent until proven 
guilty in a court of law') dates from the late 18th (or early 19th) 
century.

You are, of course, most welcome to consider how your life might be 
changed were you to be subject to the same legal considerations you 
propose for others... and, after all, since the whole matter occured o'er 
the briny deep it may be subject to Maritime Laws, a whole 'nother 
subject, entire.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 5)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2011-10-09T17:46:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<su7497d6vh7289lgp8n6642lqcash6sh1o@4ax.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com> <9fcib9Fvr3U1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <j6t3gf$kkc$1@reader1.panix.com>`

```
On Sun, 9 Oct 2011 21:25:36 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com>,
>Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
…[28 more quoted lines elided]…
>subject, entire.


I think the point is that it's not unreasonable for persons suspected
of committing a crime to be prevented from leaving a jurisdiction for
a reasonable period of time.  In the United States, that's the initial
arraignment (usually with 48 hours of the arrest), at which point the
suspect is informed of the pending charges, and a judge will set bail
and whatnot (including travel restrictions).  The actual formal charge
and entry of a plea comes at the (later) second arraignment (which may
include bail changes).

From the location, they may have been within territorial waters, so
local laws would mostly supersede maritime law.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-10T13:06:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fer86Fdd3U1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com> <9fcib9Fvr3U1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <j6t3gf$kkc$1@reader1.panix.com> <su7497d6vh7289lgp8n6642lqcash6sh1o@4ax.com>`

```
Robert Wessel wrote:
> On Sun, 9 Oct 2011 21:25:36 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[47 more quoted lines elided]…
> local laws would mostly supersede maritime law.

It's certainly well within the 12 mile limit. I'm not sure what the legal 
situation is here but I'm sure it will be revealed as time goes by.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-10T17:17:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6v9ar$sqq$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <j6t3gf$kkc$1@reader1.panix.com> <su7497d6vh7289lgp8n6642lqcash6sh1o@4ax.com>`

```
In article <su7497d6vh7289lgp8n6642lqcash6sh1o@4ax.com>,
Robert Wessel  <robertwessel2@yahoo.com> wrote:
>On Sun, 9 Oct 2011 21:25:36 +0000 (UTC), docdwarf@panix.com () wrote:
>
>>In article <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com>,
>>Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:

[snip]

>>>The first thing any maritime authority should do is arrest the ships'
>>>officers and inprison them pending completion of investigations in to
…[23 more quoted lines elided]…
>include bail changes).

Precisely my point, Mr Wessel; there's a wee bit of difference between 
'It's best you don't plan to leave town for the next few days' and 'Toss 
th' lot o' brigands in th' brig 'till th' mess can be sorted!'

>
>From the location, they may have been within territorial waters, so
>local laws would mostly supersede maritime law.

That I cannot say.  As best I know it depends on what's happened, who's 
there and which cohort has the better and more numerous armamaments.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-10T03:03:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84bc7e59-7615-4f26-9731-82eb9c6691cc@db5g2000vbb.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com> <9fcib9Fvr3U1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <j6t3gf$kkc$1@reader1.panix.com>`

```
On Oct 9, 10:25 pm, docdw...@panix.com () wrote:
> In article <0b3cddcf-74a3-4afe-a5df-7c481146b...@dk6g2000vbb.googlegroups.com>,
> Alistair Maclean  <alistair.j.l.macl...@gmail.com> wrote:
…[37 more quoted lines elided]…
> - Show quoted text -

You are of course quite right. In the UK we have the long-standing
phenomenon of trial by press where guilt is assumed, often on the
flimsiest of evidence. In this case there is a case to answer (running
a ship aground by design or by accident) and someone is guilty (the
officers, collectively, or an officer). So why not put them all in
jail and let them argue it out? The ship's owners should also be
heavily punished (put the directors in prison and they'll ensure that
ships are properly maintained, crewed and safe routes are sailed).
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-10T17:20:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6v9h2$sqq$2@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <j6t3gf$kkc$1@reader1.panix.com> <84bc7e59-7615-4f26-9731-82eb9c6691cc@db5g2000vbb.googlegroups.com>`

```
In article <84bc7e59-7615-4f26-9731-82eb9c6691cc@db5g2000vbb.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 9, 10:25?pm, docdw...@panix.com () wrote:

[snip]

>> Leaving aside how long such a set of investigations might take, Mr
>> Maclean, I believe that Garrow's assertion of 'innocent until proven
…[13 more quoted lines elided]…
>flimsiest of evidence.

There was a wonderful story, decades on back, based on the concept of 
'absolute immunity'  but my memory is, admittedly, porous and the gang of 
cells which contains it has probably been pressed into service for the 
South China Seas.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-10T13:05:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fer5hFcv2U1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com> <9fcib9Fvr3U1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 9, 4:22 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> their Human Rights.    :-O

I think Robert's point on this is a good one. I'm not sure whether we have 
similar arraignment laws here but we certainly should have.
>
>>
…[20 more quoted lines elided]…
> contain.

A storm is forecast and all the salty sea dogs are saying the ship will 
break up. It is already being tested by the action of tides over the reef.


>In the vackground could be seen what looks like a small oil
> boom to restrain the oil, but it wasn't anywhere near the wreck! Talk
> was of the oil hitting the shore (no mention of containing the slick
> and lifting it using skimmers) and how devastating that was to the
> gulls and whales and dolphins (all fish eating murderers).

The news this morning is that oil has already hit the main beach at Mount 
Maunganui (this is one of the most beautiful places in the World and deeply 
ingrained in my heart - I learned to swim in surf there and was a lifeguard 
for a couple of  my teenage years at Omanu which is just down the bay from 
the Mount). I can't tell you how deeply upsetting this is. Many locals feel 
as I do.
>
> I guess they will spray detergent and cause the oil to sink to the sea
> floor where it will devastate the base of the ecology. Your friends
> can look forward to years of being banned from landing their fish and
> crustaceans because of the poisons in the oil.

A ban on all seafood from the local area was issued this morning.


> Still, the beaches will
> be clean-ish although oil will still wash ashore for years after..
>

A major concern for local Authority is that it could affect the tourist 
season which starts in a few weeks and goes through until March. During that 
time the population goes from 100,000 to over 300,000. It's like Amity in 
bloody Jaws... Suppress bad publicity ecause we might lose money...

>> From this same beach I have observed pods of Orca and dolphins, and
>> there are a number of surf casters and fishermen who use kon-tikis
…[4 more quoted lines elided]…
> It must have been really cold then.

No, oddly enough penguins are not particularly worried by the temperature. 
There are numerous nesting colonies of a variety of penguin species around 
NZ. Although the Bay of Plenty has a sub-tropical climate other areas of the 
country are cooler. I have seen penguins in Wellington harbour on a number 
of occasions when I was a kid, but only once in Auckland (which is 
considerably warmer). We had an Emperor penguin in trouble in Wellington and 
it was eating sand because it thought it was ice, apparently. The public 
took it to their hearts and a considerable sum of money was spent to operate 
on it, fix it, nurse it back to health, then release it back to the wild 
from an Antartic supply ship. They tagged it and I was amused to see it swam 
around in  large circles for quite some time after being released. (There's 
probly something on the web about it... they called it "Happy Feet")
>
>> here but it re-entered the water when I approached it. In the
…[8 more quoted lines elided]…
> Or maybe mechanical failure due to poor maintenance of the ship?

Too soon to say.
>
> Are you involved in the cleanup?

They are looking for volunteers and I'll probably do so at some point. Right 
now I'm trying to wind down after my Australian visit and finish some "good 
ideas" I had while off in Oz.

>When the Cristos Bitos oil tanker
> went down off of Wales I was involved in a research project based on
> the dead awks and guillemots (more fish eating murderers).

It's hardly murder when a species has to kill things in order to survive, 
Alistair. The very same fish you are championing, eat each other 
anyway...:-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-10T03:13:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <cec72b17-873d-4030-a636-34e67e6eaa3b@j20g2000vby.googlegroups.com> <9fcib9Fvr3U1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <9fer5hFcv2U1@mid.individual.net>`

```
On Oct 10, 1:05 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> >> There are a variety of sea
> >> birds and I have even seen albatross skimming the waters just
…[4 more quoted lines elided]…
> No,

Blue with cold! You missed the joke. I know penguins can be found much
further north (upo the coast of Chile).

> We had an Emperor penguin in trouble in Wellington and
> it was eating sand because it thought it was ice, apparently. The public
…[4 more quoted lines elided]…
> probly something on the web about it... they called it "Happy Feet")

Yeah we got that cutesy news story in the UK too.

>
> >When the Cristos Bitos oil tanker
…[5 more quoted lines elided]…
> anyway...:-)

I'm merely trying to get people to shift their concerns from large
marine mammals (whales, dolphins, seals, etc.,) and birds and face up
to the fact that there are more important lifeforms in the sea that
need the help of humans when such crises occur. The reef will probably
be devastated but will recover over time. The beach will be poisoned
but the oil will seep in to the sand and seep out again over the
years. And so on.

My Uni tutor did point out one bit of good news - it is not the first,
second or third oil pollution incident that will cause the worst
environmental damage but the fourth incident.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-10T17:27:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j6v9tp$sqq$3@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <9fer5hFcv2U1@mid.individual.net> <ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com>`

```
In article <ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 10, 1:05?am, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:

[snip]


>> It's hardly murder when a species has to kill things in order to survive,
>> Alistair. The very same fish you are championing, eat each other
…[5 more quoted lines elided]…
>need the help of humans when such crises occur.

Leaving aside the quality of audience you are reaching through this forum, 
Mr Maclean, you might do well to develop a catchy term that might back a 
bit more punch into fewer words.  'Charismatic megafauna', anyone?

'A man can be just as dead from lack of zinc as he can be from lack of 
bread.' - R. A. Heinlein

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-10-10T15:58:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rjq697prmfi6ngc57et6audhaqsinedg2h@4ax.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <9fer5hFcv2U1@mid.individual.net> <ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com> <j6v9tp$sqq$3@reader1.panix.com>`

```
On Mon, 10 Oct 2011 17:27:21 +0000 (UTC), docdwarf@panix.com () wrote:

>'A man can be just as dead from lack of zinc as he can be from lack of 
>bread.' - R. A. Heinlein

One can live without bread.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 8)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2011-10-10T22:50:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fhb6aFn4kU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <9fer5hFcv2U1@mid.individual.net> <ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com> <j6v9tp$sqq$3@reader1.panix.com> <rjq697prmfi6ngc57et6audhaqsinedg2h@4ax.com>`

```
In article <rjq697prmfi6ngc57et6audhaqsinedg2h@4ax.com>,
	Howard Brazee <howard@brazee.net> writes:
> On Mon, 10 Oct 2011 17:27:21 +0000 (UTC), docdwarf@panix.com () wrote:
> 
…[3 more quoted lines elided]…
> One can live without bread.

Maybe, but can they live without circuses?

bill
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-11T01:36:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j706ii$mva$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com> <j6v9tp$sqq$3@reader1.panix.com> <rjq697prmfi6ngc57et6audhaqsinedg2h@4ax.com>`

```
In article <rjq697prmfi6ngc57et6audhaqsinedg2h@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Mon, 10 Oct 2011 17:27:21 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[3 more quoted lines elided]…
>One can live without bread.

That this is a possibility was nevere denied... but think of the new 
standard that would have to be generated.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-11T03:35:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1ef1edd3-81e3-4521-b281-d88e4a2197fb@q26g2000vby.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <9fer5hFcv2U1@mid.individual.net> <ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com> <j6v9tp$sqq$3@reader1.panix.com>`

```
On Oct 10, 6:27 pm, docdw...@panix.com () wrote:
>
> >I'm merely trying to get people to shift their concerns from large
…[7 more quoted lines elided]…
>

I like that but 'fish eating murderers' is more punchy.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 8)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2011-10-12T14:04:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <0b3cddcf-74a3-4afe-a5df-7c481146b7bd@dk6g2000vbb.googlegroups.com> <9fer5hFcv2U1@mid.individual.net> <ee395a07-c4c7-4128-a63f-848d1c1fef86@de2g2000vbb.googlegroups.com> <j6v9tp$sqq$3@reader1.panix.com> <1ef1edd3-81e3-4521-b281-d88e4a2197fb@q26g2000vby.googlegroups.com>`

```

"Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message 
news:1ef1edd3-81e3-4521-b281-d88e4a2197fb@q26g2000vby.googlegroups.com...
On Oct 10, 6:27 pm, docdw...@panix.com () wrote:
>
> >I'm merely trying to get people to shift their concerns from large
…[7 more quoted lines elided]…
>

I like that but 'fish eating murderers' is more punchy.

http://news.yahoo.com/stricken-ship-cracks-captain-faces-nz-court-114754126.html
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-12T22:24:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j75431$g3r$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6v9tp$sqq$3@reader1.panix.com> <1ef1edd3-81e3-4521-b281-d88e4a2197fb@q26g2000vby.googlegroups.com> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com>`

```
In article <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com>,
Charles Hottel <chottel@earthlink.net> wrote:
>
>"Alistair Maclean" <alistair.j.l.maclean@gmail.com> wrote in message 
…[13 more quoted lines elided]…
>I like that but 'fish eating murderers' is more punchy.

Perhaps like the famous 'man eating chicken'... right over there, next to 
the Great Egress.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 10)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-13T05:57:19-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <j6v9tp$sqq$3@reader1.panix.com> <1ef1edd3-81e3-4521-b281-d88e4a2197fb@q26g2000vby.googlegroups.com> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com>`

```
On Oct 12, 11:24 pm, docdw...@panix.com () wrote:
> In article <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdn...@earthlink.com>,
>
…[26 more quoted lines elided]…
> - Show quoted text -

I suppose, in the USA, it would be better to write "fish eating
murdered" (ref. the Sopranos).
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-13T16:07:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j772b7$j9e$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com>`

```
In article <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 12, 11:24?pm, docdw...@panix.com () wrote:

[snip]

>> Perhaps like the famous 'man eating chicken'... right over there, next to
>> the Great Egress.
…[3 more quoted lines elided]…
>murdered" (ref. the Sopranos).

Your supposition appears to reflect the amount of time you've spent in the
USA rather well, Mr Maclean.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 12)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-13T12:47:02-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com>`

```
On Oct 13, 5:07 pm, docdw...@panix.com () wrote:
> In article <be7f4f63-84d7-4a91-ba80-8f5e349d8...@s14g2000vbj.googlegroups.com>,
> Alistair Maclean  <alistair.j.l.macl...@gmail.com> wrote:
…[14 more quoted lines elided]…
> DD

You wouldn't catch me in the US.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-13T23:38:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j77sp6$bqc$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com>`

```
In article <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 13, 5:07?pm, docdw...@panix.com () wrote:
>> In article
…[16 more quoted lines elided]…
>You wouldn't catch me in the US.

I doubt that I would chase you there, either.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-14T13:15:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fpd9mFgehU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 13, 5:07 pm, docdw...@panix.com () wrote:
>> In article
…[19 more quoted lines elided]…
> You wouldn't catch me in the US.

It's a pity, Alistair.

Like so many people, I found that actually visiting the USA changed many of 
my pre-conceptions about it.

Although I believe most of my travelling is now over, I always enjoy visits 
to America.

And Americans at home are generally friendly and gracious hosts.

It is not at all how it is painted in some quarters.

So, a highly lucrative contract in say, California or Florida would not 
tempt you in the least? Expenses paid, sunshine, fantastic food and booze... 
no?

Like I said... a pity :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 14)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-10-13T18:45:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net>`

```
On Fri, 14 Oct 2011 13:15:50 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Like so many people, I found that actually visiting the USA changed many of 
>my pre-conceptions about it.

Visiting any place can do that.   Except you start expecting that
every place has people who you really like, and others who seem to
have problems.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 15)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-14T03:59:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com>`

```
On Oct 14, 1:45 am, Howard Brazee <how...@brazee.net> wrote:
> On Fri, 14 Oct 2011 13:15:50 +1300, "Pete Dashwood"
>
…[7 more quoted lines elided]…
>

I've found that the problem with visiting places is meeting people
from back home. By that I mean the Moaning-Minnies who complain that
the locals can't brew tea like back home.... I suspect that might be a
peculiarly British trait.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 16)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-10-14T11:08:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com>`

```
On Fri, 14 Oct 2011 03:59:59 -0700 (PDT), Alistair Maclean
<alistair.j.l.maclean@gmail.com> wrote:

>On Oct 14, 1:45ï¿½am, Howard Brazee <how...@brazee.net> wrote:
>> On Fri, 14 Oct 2011 13:15:50 +1300, "Pete Dashwood"
…[13 more quoted lines elided]…
>peculiarly British trait.

No it is not.  I'm an American who was posted to Bangkok for over 4
years.  At the time Bangkok was not the cleanest city in the world and
the traffic was horrific but there were worse places and all in all I
really enjoyed living there.

We had a group of 3 come from our corporate headquarters in Arkansas
to Bangkok to teach some application classes.  Two of the three
teachers were out every night sampling the local food, entertainment,
buying souvenirs and learning about and enjoying the city.  The other
refused to leave her hotel room, would only eat Western food and
wouldn't even go out and buy souvenirs for her kids because she was
afraid of the locals.  At lunch time when we residents would take them
out to lunch, she'd head back to the hotel.  I was surprised she even
trusted the taxi driver to get her there.  It was pretty pathetic.

Regards,
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 17)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2011-10-14T17:00:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fr85jFnk9U2@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com>`

```
In article <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com>,
	SkippyPB <swiegand@Nospam.neo.rr.com> writes:
> On Fri, 14 Oct 2011 03:59:59 -0700 (PDT), Alistair Maclean
> <alistair.j.l.maclean@gmail.com> wrote:
…[31 more quoted lines elided]…
> trusted the taxi driver to get her there.  It was pretty pathetic.

While I am sure it is not limited to Americans, we seem to have an over
abundance.  During my first Army tour I once (only once!!) went downtown
with a guy who walked down the street making nasty comments about the
people he passed.  I asked him what he thought he was doing and he said
what difference does it make, none of them speak english anyway!!  After
that I stopped going anywhere with my fellow soldiers and I made many
great friends in Germany.  Many who are still my friends today even though
I haven't been there for over 30 years!!

Another interesting anecdote:  My wife planned a trip to Cancun last spring.
It was to be her, I, my daughter and her husband.  She admited afterwards
to being a bit leery because she knew what my opinion of the third world
is.  :-)  Imagine here surprise when I turned out to be having as much if
not more fun than everyone else. (Imagine my daughters surprise to find out
were staying up and partying long after she and her husband were in bed!)
Not having a reference for a culture does not mean you can't find something
of value in it.  And, yes, I speak a little Spanish which only added to the
enjoyment.  American's proclivity for speaking only English has to be their
largest single shortcoming!!

bill
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-15T11:09:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9frq9kFcd1U1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com>,
> SkippyPB <swiegand@Nospam.neo.rr.com> writes:
…[58 more quoted lines elided]…
> bill

Bill!

Whatever makes you think Americans can speak English...? :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 19)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2011-10-14T22:42:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9frs60Fpk7U1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <9frq9kFcd1U1@mid.individual.net>`

```
In article <9frq9kFcd1U1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Bill Gunshannon wrote:
>> In article <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com>,
…[63 more quoted lines elided]…
> Whatever makes you think Americans can speak English...? :-)

Point well taken!!  :-)

bill
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-10-15T12:20:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net>`

```
On 14 Oct 2011 17:00:35 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>In article <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com>,
>	SkippyPB <swiegand@Nospam.neo.rr.com> writes:
…[43 more quoted lines elided]…
>

Your friend might be amazed to learn how many folks, especially in
Europe, speak English as well as their own language.  While in
Thailand, I took classed and learned enough Thai to get around the
city in a taxi or order in a restaurant and other mundane everyday
things.  One day I got into a taxi and told the driver in Thai where I
wanted to go.  He asked me in Thai if I spoke English.  I responded I
did and he asked me in English if I would converse with him in English
because he wanted to strengthen his English speaking skills.


>Another interesting anecdote:  My wife planned a trip to Cancun last spring.
>It was to be her, I, my daughter and her husband.  She admited afterwards
…[9 more quoted lines elided]…
>bill

I find that disheartening as well.  We (the US) are probably the only
country in the world that doesn't have a preponderance of
multi-language people.  I guess it is far easier to criticize than to
learn the language and culture of other folks.  God forbid you might
get some enrichment from that.

Regards,
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 19)_

- **From:** Fred Mobach <fred@mobach.nl>
- **Date:** 2011-10-16T14:17:41+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e9acb66$0$291$14726298@news.sunsite.dk>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com>`

```
SkippyPB wrote:

> Your friend might be amazed to learn how many folks, especially in
> Europe, speak English as well as their own language.

Well, as far as I know they try to speak an english-like language,
locally known as steenkolenengels (Dunglish). But it is indeed very
difficult to understand non-native languages, especially when trying to
understand the differences between dialects (also known in COBOL).

And still trying to understand english, german, french and the likes
correctly.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 20)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2011-10-16T13:23:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g0467Fo24U3@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com> <4e9acb66$0$291$14726298@news.sunsite.dk>`

```
In article <4e9acb66$0$291$14726298@news.sunsite.dk>,
	Fred Mobach <fred@mobach.nl> writes:
> SkippyPB wrote:
> 
…[5 more quoted lines elided]…
> difficult to understand non-native languages, 

Really?  Some of us seem to do alright.  And I will openly admint that
my abilities with non-english languages come nowhere near the english
speaking abilities of many of my European friends.

>                                               especially when trying to
> understand the differences between dialects (also known in COBOL).

When I first learned to speak German it was not in a classroom and I
learned the local dialect where I lived.  When I traveled around the
country people were easily able to tell me where I was livng based on
my use of Bauer-Deutsch a strong Pfï¿½ltzer dialect.  It only became
humorous when I came back tot he states and found that while I could
understand the German spoken by my techers from High School (I didn't
take High School German but the teachers were freinds of mine) they
could not understand me at all!!

> 
> And still trying to understand english, german, french and the likes
> correctly.

No problem there.  I listen to German Radio on the Internet every day
just like most office workers listen to local stations.  The human mind
is an amazing machine.  I don't think most people even half-understand
what it is capable of.

bill
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 21)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-17T12:18:12+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g171mFe1jU1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com> <4e9acb66$0$291$14726298@news.sunsite.dk> <9g0467Fo24U3@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <4e9acb66$0$291$14726298@news.sunsite.dk>,
> Fred Mobach <fred@mobach.nl> writes:
…[34 more quoted lines elided]…
> bill

Good for you, Bill.

I learned conversational German while living in Duesseldorf and consequently 
acquired some of the local "platt". Like you, I had no formal education in 
it but received willing help from friends and bought some "Teach Youself" 
books. I sometimes stream WDR2 to my computer, really just as a nostalgia 
thing rather than keeping my hand in :-). I like German as a language; it is 
like English was 400 years ago. (check the similarity, for example, between 
"Wohin gehts du?" and "Whither goest thou?")

I lived in Madrid for a few years so I acquired Spanish as well (although I 
seem to be losing it now and am no longer able to think in Spanish, although 
I still can in German).

Languages are a great portal into understanding a culture and becoming 
integrated with it.

Anything that promotes understanding in this world gets my vote :-)

Pete
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 22)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-18T02:47:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com> <4e9acb66$0$291$14726298@news.sunsite.dk> <9g0467Fo24U3@mid.individual.net> <9g171mFe1jU1@mid.individual.net>`

```
On Oct 17, 12:18 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> I learned conversational German while living in Duesseldorf and consequently
> acquired some of the local "platt". Like you, I had no formal education in
…[4 more quoted lines elided]…
> "Wohin gehts du?" and "Whither goest thou?")

Do people still say Whither Goest Thou?
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-19T02:13:21+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g5cbiF8sgU1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com> <4e9acb66$0$291$14726298@news.sunsite.dk> <9g0467Fo24U3@mid.individual.net> <9g171mFe1jU1@mid.individual.net> <174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 17, 12:18 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
> Do people still say Whither Goest Thou?

"Quo vadis?"  as Peter is supposed to have said to the vision of Christ he 
saw coming to Rome. Christ said he was going to Rome to again be crucified. 
Peter did not realise that it was his own crucifixion that was being 
referred to until later.

Sometimes it's best not to ask...

> Do people still say Whither Goest Thou?

They did 400 years ago.

We dropped the second person singular or "intimate" form around 150 years 
ago, except in poetry and religious texts.

French and German (plus some other Latin Languages) still retain it, 
especially for addressing children.

I like to use all of these forms occasionally. (My friends just smile 
indulgently)

I think "Whither goest thou?" has a more dramatic ring than "Wher're ya 
goin'?", but that's just me...

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 24)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-10-18T11:30:06-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gk6r971fkf8g75460mg183rphtfs9q806q@4ax.com>`
- **References:** `<te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com> <4e9acb66$0$291$14726298@news.sunsite.dk> <9g0467Fo24U3@mid.individual.net> <9g171mFe1jU1@mid.individual.net> <174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com> <9g5cbiF8sgU1@mid.individual.net>`

```
On Wed, 19 Oct 2011 02:13:21 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Alistair Maclean wrote:
>> On Oct 17, 12:18 am, "Pete Dashwood"
…[35 more quoted lines elided]…
>Pete.

I like that!  I think I shall beigin to use that phrase as well.


Regards,
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 24)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-18T22:48:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7kvnv$gjr$2@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g171mFe1jU1@mid.individual.net> <174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com> <9g5cbiF8sgU1@mid.individual.net>`

```
In article <9g5cbiF8sgU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Alistair Maclean wrote:

[snip]

>> Do people still say Whither Goest Thou?
>
>"Quo vadis?"  as Peter is supposed to have said to the vision of Christ he 
>saw coming to Rome.

Kind of odd to address the vision of a Nazarene carpenter rabbi in Latin, 
one might think.  Perhaps this 'religion' stuff isn't supposed to be 
rational.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 25)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-20T11:24:28+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g910uF4u7U1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g171mFe1jU1@mid.individual.net> <174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <9g5cbiF8sgU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[13 more quoted lines elided]…
> DD

For the last seven months I have been researching the life and times in 
Palestine during the first century, for a book I am currently writing. As 
you may know I have no particular religious views apart from atheism, but I 
have been absolutely fascinated by the events of this century and the 
effects they had right down to our own society today.

If the reported event above actually transpired (and I don't believe it did, 
but it is still a good story) Peter had been living in Rome previously and 
for some time so it would be natural to speak Latin.

Most people in Palestine at that time spoke their native language (there 
were many nationalities living there) and Greek, which was the Lingua 
Franca. The native Palestinians (about 700,000 of whom were Jewish) spoke 
Aramaic; the educated ones spoke Greek as well. (It is interesting that 
despite Palestine being a Roman Protectorate after the death of Herod 
Archelaus (6 CE), the Romans never imposed their own language or culture on 
the subjugated people.) The Jewish population did not generally speak Hebrew 
as you might expect, that was reserved for scholars, priests and scribes. 
(Mainly Sadducees)

The point is that it was a polyglot time and people generally went with the 
flow. (Quite a number of Palestinians spoke Latin after the Roman 
Procurators started arriving, but they were not forced to by Rome.)

Given that, and the fact that Peter had been in Rome for some time, it seems 
reasonable that he would address Jesus in the main language being used in 
that place at that time.

Maybe this 'religion' stuff is not so irrational, after all :-)?

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 26)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-19T22:35:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7njap$i3f$2@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com> <9g910uF4u7U1@mid.individual.net>`

```
In article <9g910uF4u7U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <9g5cbiF8sgU1@mid.individual.net>,
…[12 more quoted lines elided]…
>> to be rational.

[snip]

>If the reported event above actually transpired (and I don't believe it did, 
>but it is still a good story) Peter had been living in Rome previously and 
>for some time so it would be natural to speak Latin.

Natural for the envisioning, perhaps, but not the envisioned.

Didn't Nietzsche have something to say about God learning Greek... and 
badly?

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 27)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-20T13:27:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g987fFoqjU1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com> <9g910uF4u7U1@mid.individual.net> <j7njap$i3f$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <9g910uF4u7U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[27 more quoted lines elided]…
> DD

It seems reasonable to me, Doc, to expect that a manifestation of the 
Supreme Being would be fluent in any language He was addressed in... :-)

Given He would understand Swahili, Hottentot, Urdu, and Maori, I shouldn't 
think Latin would be a problem...

Personally, I believe God speaks German. (Or, I would if I believed in 
God...)

I base this on the fact that the Bible sounds quite thrilling when read 
aloud in German, but it in English it is just....well, boring. (Hence the 
fact that large percentages of Anglican congregations fall asleep in Church 
:-) The only Church service I ever attended in Germany (in Cologne 
cathedral) everybody was very much awake and on their toes...

I believe the antics of Southern Baptists in the USA is probably an attempt 
to enliven the proceedings.

I do have a couple of questions regarding Religious services though:

If God is all powerful and can do anything, why doesn't He just contact 
everyone on Earth telepathically and explain what is required of each 
individual, without any need for boring sermons or readings or arguments 
over scripture, or organized religion?

If God is the embodiment of spiritual perfection, how come he still needs 
adoration and worship? (Strikes me as being a bit insecure for the 
Almighty...)

Never mind... I'll just get back to working out my own salvation with 
diligence... :-)

Pete.
 -- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 28)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-20T00:54:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7nrgl$ejv$1@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g910uF4u7U1@mid.individual.net> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net>`

```
In article <9g987fFoqjU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <9g910uF4u7U1@mid.individual.net>,
…[29 more quoted lines elided]…
>Supreme Being would be fluent in any language He was addressed in... :-)

It might seem reasonable to many folks, Mr Dashwood, that an Omniscient 
Deity would know in advance how any of Its creations would respond to a 
given situation... and yet many Sacred Texts are full of tales of human 
beings being so tested.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 28)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-20T03:44:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com> <9g910uF4u7U1@mid.individual.net> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net>`

```
On Oct 20, 1:27 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> If God is all powerful and can do anything, why doesn't He just contact
> everyone on Earth telepathically and explain what is required of each
> individual, without any need for boring sermons or readings or arguments
> over scripture, or organized religion?

Ah, should we debate free will? God wants you to lead your own life,
wherever that may lead you. The notion of omniscience tends to imply
that he already knows what you are going to do....blah blah blah.

>
> If God is the embodiment of spiritual perfection, how come he still needs
> adoration and worship? (Strikes me as being a bit insecure for the
> Almighty...)
>

Before I kicked God out of my life I had come to the realisation that
God and Satan are merely two aspects of a multiple personality (also
involving a self-proclaimed Son and a Holy Spook) and is, in at least
one of those aspects, insecure with a fragile ego and a superiority
complex.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-20T12:56:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7p5qe$brv$1@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com>`

```
In article <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 20, 1:27?am, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:
…[5 more quoted lines elided]…
>Ah, should we debate free will?

Mr Maclean, answering a question with a question is no answer at all.

>God wants you to lead your own life,
>wherever that may lead you.

A finite creature's postulatings of an infinite entity's desires might, 
quite possibly, be of little value.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-21T03:29:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9gapimFlmqU1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com> <j7p5qe$brv$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article
> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com>,
…[17 more quoted lines elided]…
> quite possibly, be of little value.

Yes, quite right. It has to be an unknowable mystery or there's no chance of 
making money from it... :-)

While explaining the colour red to a blind man may be very difficult, it 
certainly isn't impossible and the action of doing so may be of more than a 
little value for both of the parties concerned.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 31)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-20T08:06:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcfa69d8-ff3a-46fd-af32-7641972e9502@fk25g2000vbb.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com> <j7p5qe$brv$1@reader1.panix.com> <9gapimFlmqU1@mid.individual.net>`

```
On Oct 20, 3:29 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> While explaining the colour red to a blind man may be very difficult, it
> certainly isn't impossible and the action of doing so may be of more than a
> little value for both of the parties concerned.
>

Easy: visible red light has a wavelength of about 650 nm.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 32)_

- **From:** Kerry Liles <"kerry.liles[minus_the_spam]"@gmail.com>
- **Date:** 2011-10-20T11:09:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7pdin$pnv$1@dont-email.me>`
- **In-Reply-To:** `<dcfa69d8-ff3a-46fd-af32-7641972e9502@fk25g2000vbb.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com> <j7p5qe$brv$1@reader1.panix.com> <9gapimFlmqU1@mid.individual.net> <dcfa69d8-ff3a-46fd-af32-7641972e9502@fk25g2000vbb.googlegroups.com>`

```
On 10/20/2011 11:06 AM, Alistair Maclean wrote:
> On Oct 20, 3:29 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz>  wrote:
…[5 more quoted lines elided]…
> Easy: visible red light has a wavelength of about 650 nm.

well, even though I am sighted, I learned something.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-21T01:12:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7qgu2$3b2$3@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com> <j7p5qe$brv$1@reader1.panix.com> <9gapimFlmqU1@mid.individual.net>`

```
In article <9gapimFlmqU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> A finite creature's postulatings of an infinite entity's desires
>> might,
…[3 more quoted lines elided]…
>making money from it... :-)

I know what I pass when I eat beans... but what has someone been eating 
when they pass the ammunition?

>
>While explaining the colour red to a blind man may be very difficult, it 
>certainly isn't impossible and the action of doing so may be of more than a 
>little value for both of the parties concerned.

'Ware that edge on which you dance, Mr Dashwood... a seemingly reasonable 
next step could lead to Bobby Browning's 'A man's reach should exceed his 
grasp... or what's a heaven for?' and you're back to searching for 
salvation by impossible acts.

On the other hand... the act becomes simple when 'explaining' consists of 
'Just as 'loud' is a characteristic encountered by some folks with hearing 
and 'soft' a characteristic encountered by some folks endowed with tactile 
senses so is 'red' a characteristic encountered by some folks who are 
commonly referred to as 'sighted'.'

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 32)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-10-21T11:41:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mk43a7thjktkjn87vbkn9nlafqd7rg445g@4ax.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com> <j7p5qe$brv$1@reader1.panix.com> <9gapimFlmqU1@mid.individual.net> <j7qgu2$3b2$3@reader1.panix.com>`

```
On Fri, 21 Oct 2011 01:12:34 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <9gapimFlmqU1@mid.individual.net>,
>Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[13 more quoted lines elided]…
>

Bigger beans.


>>
>>While explaining the colour red to a blind man may be very difficult, it 
…[14 more quoted lines elided]…
>DD

Regards,
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 30)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-20T08:04:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<506106c3-96ab-4a46-ad26-d889003bdb44@y32g2000yqh.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com> <j7p5qe$brv$1@reader1.panix.com>`

```
On Oct 20, 1:56 pm, docdw...@panix.com () wrote:
> In article <5dfa7a85-9b74-4c42-8229-d5465b493...@ff5g2000vbb.googlegroups.com>,
> >God wants you to lead your own life,
…[5 more quoted lines elided]…
> DD

Hey, it's the best that this finite entity can do given the absence of
hard evidence.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-21T01:02:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7qgar$3b2$1@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <5dfa7a85-9b74-4c42-8229-d5465b493c24@ff5g2000vbb.googlegroups.com> <j7p5qe$brv$1@reader1.panix.com> <506106c3-96ab-4a46-ad26-d889003bdb44@y32g2000yqh.googlegroups.com>`

```
In article <506106c3-96ab-4a46-ad26-d889003bdb44@y32g2000yqh.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 20, 1:56?pm, docdw...@panix.com () wrote:
>> In article
…[9 more quoted lines elided]…
>hard evidence.

I might question the criteria used for 'the best' here, Mr Maclean.  I do 
not need to question what the 'hard evidence' is of 'an infinite entity's 
desires', though... I've found those in night-stands in cheap motel rooms.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 28)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-10-20T15:45:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3e2b80-2204-468c-bf24-6466d12e964b@g27g2000pro.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com> <9g910uF4u7U1@mid.individual.net> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net>`

```
On Oct 20, 1:27 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
>
> If God is the embodiment of spiritual perfection, how come he still needs
> adoration and worship? (Strikes me as being a bit insecure for the
> Almighty...)

When Mark Twain was in NZ in 1895 he reported that he had a discussion
with some Maoris. They complained that the missionaries were trying to
stop them praying the their 'bad' gods and instead pray to the
missionaries 'good' gods. "What is the point in that?, the good gods
aren't out to harm us."
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 28)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-10-20T15:55:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com> <9g910uF4u7U1@mid.individual.net> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net>`

```
On Oct 20, 1:27 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:

> >>>> "Quo vadis?"  as Peter is supposed to have said to the vision of
> >>>> Christ he saw coming to Rome.
[...]

> It seems reasonable to me, Doc, to expect that a manifestation of the
> Supreme Being would be fluent in any language He was addressed in... :-)

So you think that Jesus was the 'Supreme Being' ?

> Personally, I believe God speaks German. (Or, I would if I believed in
> God...)

Miriam Ferguson, along with a few others, have been credited with the
quote: “If English was good enough for Jesus Christ, it ought to be
good enough for the children of Texas.”
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 29)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-21T01:04:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7qgfb$3b2$2@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com>`

```
In article <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com>,
Richard  <riplin@Azonic.co.nz> wrote:
>On Oct 20, 1:27?pm, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
>So you think that Jesus was the 'Supreme Being' ?

I barely know what *I* think, Mr Plinston, but I can't see where in 'a 
manifestation of a Supreme Being' one can find 'I think (x) was/is a/the 
'Supreme Being'.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 30)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-10-20T19:35:20-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd596a8b-5f84-4b3c-aa04-528cdb1cce92@v33g2000prm.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com> <j7qgfb$3b2$2@reader1.panix.com>`

```
On Oct 21, 2:04 pm, docdw...@panix.com () wrote:
> In article <c7df92f1-3963-4b1b-996b-c64a449b7...@p20g2000prm.googlegroups.com>,
>
…[15 more quoted lines elided]…
> 'Supreme Being'.

No, you probably can't see that.

But then there are probably a lot of things that you can't see, such
as the direct relationship between the references to "vision of
Christ" and "manifestation of the Supreme Being".
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-21T12:38:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7rp3n$gc6$1@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com> <j7qgfb$3b2$2@reader1.panix.com> <cd596a8b-5f84-4b3c-aa04-528cdb1cce92@v33g2000prm.googlegroups.com>`

```
In article <cd596a8b-5f84-4b3c-aa04-528cdb1cce92@v33g2000prm.googlegroups.com>,
Richard  <riplin@Azonic.co.nz> wrote:
>On Oct 21, 2:04?pm, docdw...@panix.com () wrote:
>> In article
…[23 more quoted lines elided]…
>Christ" and "manifestation of the Supreme Being".

I believe I can see such, Mr Plinston, but are you capable of concluding 
that Mr Dashwood might have been referring to Paul's interpretation of the 
vision and not his (Mr Dashwood's) own?

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 32)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2011-10-21T11:56:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0f046aef-9c23-4629-8fd6-f96e8a516b45@p27g2000prp.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com> <j7qgfb$3b2$2@reader1.panix.com> <cd596a8b-5f84-4b3c-aa04-528cdb1cce92@v33g2000prm.googlegroups.com> <j7rp3n$gc6$1@reader1.panix.com>`

```
On Oct 22, 1:38 am, docdw...@panix.com () wrote:
> In article <cd596a8b-5f84-4b3c-aa04-528cdb1cc...@v33g2000prm.googlegroups.com>,
>
…[38 more quoted lines elided]…
> vision and not his (Mr Dashwood's) own?

I base my conclusion on what was written. There was no post in this
thread from Paul explaining his interpretation.

Of course PD may not believe in either, but he did conjoin them.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 33)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-22T13:45:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7uhd8$fog$1@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <cd596a8b-5f84-4b3c-aa04-528cdb1cce92@v33g2000prm.googlegroups.com> <j7rp3n$gc6$1@reader1.panix.com> <0f046aef-9c23-4629-8fd6-f96e8a516b45@p27g2000prp.googlegroups.com>`

```
In article <0f046aef-9c23-4629-8fd6-f96e8a516b45@p27g2000prp.googlegroups.com>,
Richard  <riplin@Azonic.co.nz> wrote:
>On Oct 22, 1:38?am, docdw...@panix.com () wrote:

[snip]

>> I believe I can see such, Mr Plinston, but are you capable of concluding
>> that Mr Dashwood might have been referring to Paul's interpretation of the
…[3 more quoted lines elided]…
>thread from Paul explaining his interpretation.

And yet... in another posting Mr Dashwood indicated that my interpretation 
of what he posted was in accord with what he had written.  This is called, 
in some circles, 'concurrence with the author's intent' and is considered, 
by some, to be fundamental to approaching an author's work.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 30)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-21T16:21:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9gc6qfFgnsU1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j7njap$i3f$2@reader1.panix.com> <9g987fFoqjU1@mid.individual.net> <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com> <j7qgfb$3b2$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article
> <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com>,
…[18 more quoted lines elided]…
> DD

I haven't seen Richard's direct post(s) and I can't be bothered going to 
Google Groups to do so, but I would have thought that my being an atheist 
was an established matter of record.

That being so, no, I don't believe Jesus (or any other of the candidates 
favoured by many of the World's major Religions) was/is an incarnation of a 
"Supreme Being".

I don't believe in a Supreme Being at all. (a= without, theism= belief in 
God/Supreme Being)

While I might be wrong about this, (I'll find out when I die, or I won't 
find out because there is nothing to find and nothing to be finding it...) I 
have studied the question for a number of decades and am satisfied that the 
position I currently support is the most likely one.

Having said all of that, I have nothing but respect and regard for the 
beliefs of people who see it differently. I do not feel compelled to 
evangelize my personal reality.

Thank you for pointing out the non-specifity of what I said, Doc.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 31)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-21T12:40:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7rp87$gc6$2@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <c7df92f1-3963-4b1b-996b-c64a449b719b@p20g2000prm.googlegroups.com> <j7qgfb$3b2$2@reader1.panix.com> <9gc6qfFgnsU1@mid.individual.net>`

```
In article <9gc6qfFgnsU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article
…[21 more quoted lines elided]…
>was an established matter of record.

[snip]

>Thank you for pointing out the non-specifity of what I said, Doc.

It was just a lucky guess and paying a bit of attention to the logic, Mr 
Dashwood.  You're quite welcome.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 25)_

- **From:** HansJ <hans.igel@googlemail.com>
- **Date:** 2011-10-20T02:24:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<67611579-a13b-4bc9-8f40-cc6725f98a04@x7g2000yqn.googlegroups.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g171mFe1jU1@mid.individual.net> <174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com>`

```
On 19 Okt., 00:48, docdw...@panix.com () wrote:
> In article <9g5cbiF8s...@mid.individual.net>,
>
…[13 more quoted lines elided]…
> DD

... well while many people believe that "religion" stuff as you call
it, is rational, I'm more than sceptical.

One person that is sharing my point of view is: http://www.youtube.com/watch?v=MeSSwKffj9o

Regards Hans
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 26)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-20T13:04:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7p690$brv$2@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g5cbiF8sgU1@mid.individual.net> <j7kvnv$gjr$2@reader1.panix.com> <67611579-a13b-4bc9-8f40-cc6725f98a04@x7g2000yqn.googlegroups.com>`

```
In article <67611579-a13b-4bc9-8f40-cc6725f98a04@x7g2000yqn.googlegroups.com>,
HansJ  <hans.igel@googlemail.com> wrote:
>On 19 Okt., 00:48, docdw...@panix.com () wrote:

[snip]

>>... ?Perhaps this 'religion' stuff isn't supposed to be
>> rational.
>
>... well while many people believe that "religion" stuff as you call
>it, is rational, I'm more than sceptical.

I have difficulties based on more radical things, Mr Igel... the roots 
(radices) of the words used to discuss such matters.  Millimetre, 
centimetre, kilometre... well and good, all based on a common unit of 
measure.  Believe (conjugate with German glauben), rational (ratio), 
credible (credo), religion (ligare)... there are many different ways these 
might get tied together (ligare), some of them perhaps valid ('of 
strength').

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 23)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-18T22:44:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7kvh0$gjr$1@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <9g0467Fo24U3@mid.individual.net> <9g171mFe1jU1@mid.individual.net> <174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com>`

```
In article <174f1988-030f-46da-8707-cd8ee99aad7e@fk25g2000vbb.googlegroups.com>,
Alistair Maclean  <alistair.j.l.maclean@gmail.com> wrote:
>On Oct 17, 12:18?am, "Pete Dashwood"
><dashw...@removethis.enternet.co.nz> wrote:
…[8 more quoted lines elided]…
>Do people still say Whither Goest Thou?

Perhaps some time in the United States of America might change your 
knowledge of current English usage, Mr Maclean.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 21)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-17T01:57:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7g22g$or9$2@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com> <4e9acb66$0$291$14726298@news.sunsite.dk> <9g0467Fo24U3@mid.individual.net>`

```
In article <9g0467Fo24U3@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:

[snip]

>The human mind
>is an amazing machine.  I don't think most people even half-understand
>what it is capable of.

Taking a step back from that, Mr Gunshannon, might allow someone a 
different appreciation of anthropogenerated beauties... and horrors, 
likewise.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 19)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-17T01:54:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7g1tf$or9$1@reader1.panix.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com>`

```
In article <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com>,
SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:

[snip]

>I find that disheartening as well.  We (the US) are probably the only
>country in the world that doesn't have a preponderance of
>multi-language people.  I guess it is far easier to criticize than to
>learn the language and culture of other folks.  God forbid you might
>get some enrichment from that.

There was a fellow I knew, decades on back, who mustered out of the United 
States Army Air Corps and took his GI Benefits to medical school with him 
in Switzerland.  He had a decent command of German and Latin and a few 
years' worth of time in-country gave him the Swiss dialect used around 
Berne... and The Locals felt so comfortable with him that they took him 
into their confidence and asked him to explain a Great Mystery:

'What is this with the Americans and their languages?  They don't have 
any, except their version of English.  How did this happen?'

(Flash forward to the late 1980s, when my client was a German bank... I 
was on contract for nine months before they knew I spoke a word of 
Deutsch, let alone studied a few of Einstein's 1905 papers in it... and 
their riddle was 'If a person who speaks three languages is trilingual and 
a person who speaks two languages is bilingual then what is a person who 
speaks one language?

... An American.')

Back to post-war Switzerland... the med student gave an elegant 
explanation which rested on facts and a single '... well, that happens a 
lot'.  He said that in Europe, especially in Switzerland, you had to learn 
other languages as a matter of just getting by; if you crossed a street 
and inquired into the cost of something in the wrong language you'd get an 
answer, sure, but the price for (eg) Italian-speakers would be 
(lower/higher) than the price charged for those who inquited in French.

In the United States of America, on the other hand, one could travel not 
just across the street but for ten thousand kilometers... and still use, 
more-or-less, the same language.  Since people can be lazy and not 
concentrate on things that seem to be of immediate importance (the 'well, 
that happens a lot' mentioned above) then they just don't bother to learn 
other tongues.

Me, I was different.  I was taught 'learn a new language, learn a new way 
to speak'... and I've been confusing folks with a variety of blatherings 
for a few decades.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 19)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-17T17:28:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6JmdnYocAvW2MQHTnZ2dnUVZ_jidnZ2d@earthlink.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <vnjg971acg4tbmo6aho76m0619lm667ulq@4ax.com> <9fr85jFnk9U2@mid.individual.net> <vbcj97p0ctpifb80238bdmj557ghab2l56@4ax.com>`

```
SkippyPB wrote:
>
> Your friend might be amazed to learn how many folks, especially in
> Europe, speak English as well as their own language.

Likewise in the United States.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-15T11:07:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9frq4fFbbjU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 14, 1:45 am, Howard Brazee <how...@brazee.net> wrote:
>> On Fri, 14 Oct 2011 13:15:50 +1300, "Pete Dashwood"
…[13 more quoted lines elided]…
> peculiarly British trait.

Speaking as an Anglophile who has nothing but affection for Albion and her 
peoples, I can say that the English (generally) are NOT good travellers. 
(The Scots, on the other hand are excellent... they deliberately go to 
out-of-the-way and difficult places. I remember sharing a bottle of scotch 
with an ex-pat Scot in Dacca, Bangladesh - we were the only two white people 
in the hotel. He was very good company :-))

Here in NZ I have a number of friends who have immigrated from the UK. The 
pattern often goes as follows:

1. Family arrives and it is all strange and new. They soon realise that the 
culture is quite different form back home and it is a bit like living on a 
different planet. The kids (who are usually much more adaptable than their 
parents) soon settle into school, make new friends, and start to realise the 
opportunities to do things they couldn't easily do back home.

2. The Father makes friends from his workplace and goes fishing at the 
weekend or gets into a local sports team. He learns very quickly not to 
"whinge" (complain and moan) because even if what he says is true and 
certain aspects of life back home were better, the Kiwis don't want to hear 
it, and besides, he is also discovering other things that more than 
compensate.

3. The wife has the hardest time of all. Her husband and the kids seem to be 
settling in but she misses her family, her friends, and the shops, the 
community and the pub. Although the neighbours are friendly, it isn't the 
same as it was back home. She finds herself becoming very unhappy and just 
wants to go back.

4. After around a year to 18 months things have become quite serious. Even 
the husband is getting tired of his wife's constant whinging and comparing 
things to the life they left. The whole reason they emigrated in the first 
place (which is usually about better opportunities for the kids) gets lost. 
Finally, they decide to return home.

5. They go home and are usually there for three to six months. The pub has 
been turned into a new shopping mall, their friends have moved, in pursuit 
of better jobs, the parents and in-laws become very tedious after a few 
weeks, the kids keep going on about NZ. And they come face-to-face with the 
reality of overcrowded cities and all the reasons they left in the first 
place.

6. They arrive back in NZ and are no longer "whingeing Poms" but new New 
Zealanders who are ready to get involved in the community and become part of 
it.

I have one friend in particular who has just come back from a visit to 
England after living in NZ for about 6 years. She enjoyed her trip, but she 
is going to apply for NZ Citizenship as she realised that arriving back here 
was "coming home" for her. I have never heard her whinge about anything.

She does make excellent tea, but I am a coffee drinker... :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 17)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2011-10-14T22:50:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9frsmdFpk7U2@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <9frq4fFbbjU1@mid.individual.net>`

```
In article <9frq4fFbbjU1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Alistair Maclean wrote:
>> On Oct 14, 1:45 am, Howard Brazee <how...@brazee.net> wrote:
…[67 more quoted lines elided]…
> She does make excellent tea, but I am a coffee drinker... :-)

 
Ever heard "Eric Bogle & John Munro  Kissing English Arses Talking Blues"

bill
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-16T14:23:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fuq01F74mU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <9frq4fFbbjU1@mid.individual.net> <9frsmdFpk7U2@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <9frq4fFbbjU1@mid.individual.net>,
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
…[79 more quoted lines elided]…
> bill

No, sorry. When I get some time, I'll check it out.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 17)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-15T07:29:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TKadnTdNLKwN4QTTnZ2dnUVZ_hGdnZ2d@earthlink.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <te1f97t9hvfe6nn76020g3hd8967mfsprk@4ax.com> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <9frq4fFbbjU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> Speaking as an Anglophile who has nothing but affection for Albion
…[5 more quoted lines elided]…
> company :-))

Culture Shock happens here, too. Years ago I was visiting a bookstore in 
south Florida. The owners were mid-20's, born and bread Mannhattanites. They 
wanted to start a family and (rightly) concluded that Manhattan was no place 
for kids. They moved to Florida and opened a bookstore.

They were trying mightily to get with the program: joined a church, got 
involved with the civic association and chamber of commerce, and so on.

During a lull in the training, I stepped next door and picked up the local 
paper. There was an article in the paper about how elementary school kids, 
when walking to school, crossed a foot bridge spanning a drainage canal.

An alligator lived in the canal.

Anyway, the story went on about the kids tossing Twinkies (a sugar-filled 
confection) to the 'gator and enjoying his (or her) antics while eating the 
cake.

I showed the article to the couple. They went nuts.

"What are they going to DO about this alligator?" they asked.

"Uh, nothing," said I. "The alligator lives there."

"Lives there?! We're talking about LITTLE CHILDREN" the couple exclaimed.

"You're in Florida. Florida has alligators. It's just a fact of life. Now 
let me ask you, suppose you're walking down a residential street in 
Manhattan and you see a bum sleeping in a doorway. You don't go over and 
kick him do you?"

"Er, no..."

"Same here except you'll see alligators basking in the sun."

"IT'S NOT THE SAME THING!... How big is this alligator anyway?"

Looking at the paper, I said: "The article says about eight feet."

"Oh Lord! Eight feet! What are we going to do."

Trying to be rational I offered: "Look, again while walking a Manhattan 
street, don't you carry a few extra quarters for the bums asking for spare 
change?"

"Uh, yeah. Sometimes."

"Same thing here. Kids carry Twinkies."

"IT'S NOT THE SAME THING! (moan)"

I had a really good time.

(I have a couple more stories featuring indigenous wildlife if anyone is 
interested)
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-15T15:32:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7c91r$9jf$1@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <e81d5aa0-3d20-4f52-8c5e-b297b87e5efb@u13g2000vbx.googlegroups.com> <9frq4fFbbjU1@mid.individual.net> <TKadnTdNLKwN4QTTnZ2dnUVZ_hGdnZ2d@earthlink.com>`

```
In article <TKadnTdNLKwN4QTTnZ2dnUVZ_hGdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:

[snip]

>"IT'S NOT THE SAME THING!... How big is this alligator anyway?"

[snip]

>"IT'S NOT THE SAME THING! (moan)"
>
>I had a really good time.

When I encounter similar assertions of dissimilarities ('It's not the same 
thing' or - more commonly, in my experience - 'But it's *different*!') my 
response is an engaging 'Really?  What are the differences that you see 
between them?'

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 14)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2011-10-14T03:57:37-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net>`

```
On Oct 14, 1:15 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> > You wouldn't catch me in the US.
>
…[3 more quoted lines elided]…
> my pre-conceptions about it.

I have no pre-conceptions that need to be changed. I just have no
interest in visiting the US beyond New Orleans and the Grand Canyon.

> It is not at all how it is painted in some quarters.

I know the country gets a lot of negative press but that doesn't
bother me. I definitely don't have the view that the backwoods areas
are populated with Deliverance style yokels or that all females in NY
are like those in Sex In The City. I just don't have any interest in
anything in the US other than the two places I have already mentioned.
And I can live without seeing them but I would like to go to Olympus
and Delphi and Giza before I snuff it.

>
> So, a highly lucrative contract in say, California or Florida would not
> tempt you in the least? Expenses paid, sunshine, fantastic food and booze...
> no?

That would give me a reason to go there, which I currently lack.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-15T11:18:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9frqp5Fg5rU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 14, 1:15 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[25 more quoted lines elided]…
> That would give me a reason to go there, which I currently lack.

OK.

I understand.

Like you, I had certain places I REALLY wanted to go. The Acropolis was one. 
When I got there it was a bitter disappointment. The cradle of democracy 
littered with coke cans and MacDonalds wrappers and lit up at night like a 
scene on a chocolate box for a degrading
Son et Lumiere. The Taj Mahal was better, and by moonlight you can't see the 
bits that need maintenance. I think, of all the places on my bucket list, 
the ONLY one that actually was what I hoped for was sunrise over Everest.

What I learned from this was not to romanticize places you haven't visited, 
just go there and take them as you find them. The real experience is in the 
journey, not the destination.

I hope you get to see the places you mention, and I hope you enjoy that 
experience.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 15)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-15T07:36:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com>`

```
Alistair Maclean wrote:
> On Oct 14, 1:15 am, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[9 more quoted lines elided]…
>

The United States is a HUGE country, with much to see. Add to your list a 
few of my favorites:

* Niagra Falls
* Mount Rushmore
* Death Valley
* Las Vegas
* The Appalachian Trail

While the British Museum is a magnificant outing and not to be missed, any 
one of the seven museums making up the Smithsonian Institution dwarfs it by 
comparison.

Right now, for example, the Air & Space Museum is featuring an exhibit of 
military drones and how we can kill anybody in the world while sitting at a 
console in Virginia.

It makes one proud to be an American.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-15T15:36:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7c9a9$9jf$2@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com>`

```
In article <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com>,
HeyBub <heybub@NOSPAMgmail.com> wrote:

[snip]

>The United States is a HUGE country, with much to see. Add to your list a 
>few of my favorites:
>
>* Niagra Falls

Be prepared to be seized by an uncontrollable impulse to turn, slowly, 
step by step, inch by inch...

[snip]

>Right now, for example, the Air & Space Museum is featuring an exhibit of 
>military drones and how we can kill anybody in the world while sitting at a 
>console in Virginia.
>
>It makes one proud to be an American. 

Being an American is either an accident of birth or an intentional 
compliance with a set of laws.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-16T14:38:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fuqtfFd2pU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <j7c9a9$9jf$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com>,
> HeyBub <heybub@NOSPAMgmail.com> wrote:
…[22 more quoted lines elided]…
> DD

Still, everybody SHOULD be proud of where they live and do their best to 
make it a decent place to live and worthy of respect.

I draw the line at "Patriotism" because it seems to cause a lot of deaths (I 
like to think I am a Human Being before I am a Kiwi), but tonight NZ plays 
Australia for a place in the final of the Rugby World Cup, and you could cut 
the tension here with a knife... :-)

France has already made it to the final by having the luckiest win over 
Wales that you could imagine. I was very sorry for the Welsh who played like 
Champions  while the French stonewalled once they had a lead. Despite being 
14 against 15 for most of the game (the Welsh Captain was sent off in a 
questionable refereeing decision -technically accurate but morally 
reprehensible), the Welsh prevented the French from crossing their line and 
finally lost by one point after being robbed on several occasions by simple 
bad luck.

NZ and Oz are traditional rivals in this arena and two of the best teams in 
the World. Either of us should be able to beat France if they play like they 
did last night... In the meantime, tonight's game will be a cliffhaner and 
probably a fantastic spectacle for anyone who enjoys Rugby. I'm having a few 
friends over and it will be wine and pizza and "Go the All Blacks!"

I hope some of you can get this on cable or satellite. If you never watched 
Rugby in your life, this is an ideal introduction. When played by expert 
teams there is a beauty and elegance to it, not to mention some nailbiting 
physical contact. The TV audience is predicted to be around 1.6 billion in 
20 countries. Because NZ are playing they will perform the traditional Maori 
challenge to the Australians (haka) and this is usually enough to make 
anyone smile :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2011-10-16T06:27:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<472dnW2N8tg7IgfTnZ2dnUVZ_rqdnZ2d@earthlink.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <j7c9a9$9jf$2@reader1.panix.com> <9fuqtfFd2pU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> I hope some of you can get this on cable or satellite. If you never
…[6 more quoted lines elided]…
>

I've never played or watched a rugby match. I did, however, participate in a 
(mostly) naked girl scrum, so I know what you mean.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** docdwarf@panix.com ()
- **Date:** 2011-10-17T02:04:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j7g2f8$or9$3@reader1.panix.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <j7c9a9$9jf$2@reader1.panix.com> <9fuqtfFd2pU1@mid.individual.net>`

```
In article <9fuqtfFd2pU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com>,
>> HeyBub <heybub@NOSPAMgmail.com> wrote:

[snip]


>>> Right now, for example, the Air & Space Museum is featuring an
>>> exhibit of military drones and how we can kill anybody in the world
…[8 more quoted lines elided]…
>make it a decent place to live and worthy of respect.

Making the place where one lives decent and worthy of respect (and that 
'respect' thing I might take issue with... courtesy is to be granted 
immediately but respect must be earned) might not have much to do with 
pride, Mr Dashwood... these are words and attitudes which dance, 
intertwine and wiggle their warply-wooves in rather intricate fashions.

'Gosh, don't I feel fine because I live in a place where people took money 
from me - and I objected to it, too! - and now the patina of time has 
caused me to say 'I'm proud to be of the group that was associated in that 
undertaking!'

Thanks but no... I'll take pride in what I do.

DD
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 16)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-10-15T12:25:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com>`

```
On Sat, 15 Oct 2011 07:36:22 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>Alistair Maclean wrote:
>> On Oct 14, 1:15 am, "Pete Dashwood"
…[30 more quoted lines elided]…
>

That notwithstanding, a visit to Cape Kennedy is a must.  Saturn
rockets, space shuttles and an old Mercury capsule are must sees.

Regards,
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-16T14:45:49+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9furafFfojU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com>`

```
SkippyPB wrote:
> On Sat, 15 Oct 2011 07:36:22 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
> wrote:
…[38 more quoted lines elided]…
> Regards,

Hmmm.... I thought they changed it back to Canaveral?

What's the story on that?

It seems sad to me that Kennedy has been so denigrated after his death. I 
don't personally care about the booze and women (as long as it was separate 
from his political performance). I remember him with fondness because, when 
I was a teenager he gave our generation hope and it was refreshing to have 
someone less than 60 years old in charge.

Many Americans don't realise that we were subject to the threat of nuclear 
annihilation in the 60s (just like you were) and we never even got a vote... 
The American President (and his attitude and actions) was of deep concern to 
us...

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2011-10-15T21:35:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8bgk97lvsj25shjojbmq9n6i6pdrc595lu@4ax.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com> <9furafFfojU1@mid.individual.net>`

```
On Sun, 16 Oct 2011 14:45:49 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>SkippyPB wrote:
>> On Sat, 15 Oct 2011 07:36:22 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
…[54 more quoted lines elided]…
>us...


It's still the Kennedy Space Center.  Cape Canaveral (on which KSC
happens to sit, along with a lot of other stuff, including an
eponymous town), the piece of land (the entire cape), was renamed Cape
Kennedy at Jackie's request after the assassination.  The locals never
liked having their spot renamed, and Florida passed a law renaming it
back in 1973, and the Interior Department (and the Kennedy family) did
not object.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-17T01:36:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g01euFgv0U1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com> <9furafFfojU1@mid.individual.net> <8bgk97lvsj25shjojbmq9n6i6pdrc595lu@4ax.com>`

```
Robert Wessel wrote:
> On Sun, 16 Oct 2011 14:45:49 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[68 more quoted lines elided]…
> not object.

Thanks Robert.

Interesting and informative.

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-10-16T10:27:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f1m975egl6hhe1668j97so3ch76n46tve@4ax.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com> <9furafFfojU1@mid.individual.net>`

```
On Sun, 16 Oct 2011 14:45:49 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Many Americans don't realise that we were subject to the threat of nuclear 
>annihilation in the 60s (just like you were) and we never even got a vote... 
>The American President (and his attitude and actions) was of deep concern to 
>us...

Having a vote didn't change anything.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-17T12:19:37+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g174bFeetU1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com> <9furafFfojU1@mid.individual.net> <3f1m975egl6hhe1668j97so3ch76n46tve@4ax.com>`

```
Howard Brazee wrote:
> On Sun, 16 Oct 2011 14:45:49 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
> Having a vote didn't change anything.

Maybe not, Howard.

But can you imagine how bad NOT having one makes you feel?

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 20)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2011-10-16T18:45:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qgum97l4bavm4pjc3ss3dar8e7spm9tnao@4ax.com>`
- **References:** `<be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com> <9furafFfojU1@mid.individual.net> <3f1m975egl6hhe1668j97so3ch76n46tve@4ax.com> <9g174bFeetU1@mid.individual.net>`

```
On Mon, 17 Oct 2011 12:19:37 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>>> Many Americans don't realise that we were subject to the threat of
>>> nuclear annihilation in the 60s (just like you were) and we never
…[7 more quoted lines elided]…
>But can you imagine how bad NOT having one makes you feel?

Yes.   I bet you know how bad it is to vote for someone who betrays
your vote.

Of course, we all have been in danger of foreign bad guys as well as
domestic - without opportunities to vote.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 18)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2011-10-16T13:36:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pn4m975v7mrd2raebfeonkgv0l4uqggg9f@4ax.com>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com> <9furafFfojU1@mid.individual.net>`

```
On Sun, 16 Oct 2011 14:45:49 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>SkippyPB wrote:
>> On Sat, 15 Oct 2011 07:36:22 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
…[43 more quoted lines elided]…
>What's the story on that?

Yes, that's true but I still call it Cape Kennedy.  On November 28,
1963 President Lyndon B. Johnson announced in a televised address that
Cape Canaveral would be renamed Cape Kennedy in memory of President
John F. Kennedy, who was assassinated six days earlier. President
Johnson said the name change had been sanctioned by the U.S. Board of
Geographic Names.  That name change officially took effect on December
20, 1963.

The Air Force subsequently changed the name of the Cape Canaveral
Missile Test Annex to Cape Kennedy Air Force Station (CKAFS). That
name change took somewhat longer, but became official on January 22,
1964.

The City of Cape Canaveral, incorporated in 1962 and sandwiched
between Port Canaveral to the north and Cocoa Beach to the south,
decided by city council vote not to change its name, although debate
was bitter. The name of Port Canaveral also remained unchanged.

The U.S. Board of Geographic Names confirmed the name change of
geographic Cape Canaveral to Cape Kennedy in their Decision List
Number 6303, September through December, 1963 published in the spring
of 1964.

After a ten-year campaign by Florida residents failed to convince the
U.S Congress to change the name Cape Kennedy back to Cape Canaveral,
the name it had held for 400 years, the Florida Legislature took
action. On May 18, 1973 Florida Governor Rueben Askew signed a Florida
Statute requiring that Cape Kennedy be renamed Cape Canaveral on all
State of Florida official documents and maps.

The U.S. Board of Geographic Names responded on October 9, 1973 by
agreeing to officially recognize the name change from Cape Kennedy to
Cape Canaveral at the national level. The name John F. Kennedy Space
Center, NASA remained the same.


>
>It seems sad to me that Kennedy has been so denigrated after his death. I 
…[4 more quoted lines elided]…
>

Totally agree and yes he and his brothers were certainly "players" but
it never got in the way of their jobs and it didn't lessen their
devotion to America.  Those who tried to denigrate them were just
jealous of the family and their success.  But never has one family
given so much for this country.  For that, I'd excuse their few
dalliances.


>Many Americans don't realise that we were subject to the threat of nuclear 
>annihilation in the 60s (just like you were) and we never even got a vote... 
…[3 more quoted lines elided]…
>Pete.

So true.  Kennedy was president when  Premier Nikita Khrushchev tried
to station nucleur missles in Cuba.   


For the United States, the crisis began on October 15, 1962 when
reconnaissance photographs revealed Soviet missiles under construction
in Cuba. Early the next day, President John Kennedy was informed of
the missile installations. Kennedy immediately organized the EX-COMM,
a group of his twelve most important advisors to handle the crisis.
After seven days of guarded and intense debate within the upper
echelons of government, Kennedy concluded to impose a naval quarantine
around Cuba. He wished to prevent the arrival of more Soviet offensive
weapons on the island. On October 22, Kennedy announced the discovery
of the missile installations to the public and his decision to
quarantine the island. He also proclaimed that any nuclear missile
launched from Cuba would be regarded as an attack on the United States
by the Soviet Union and demanded that the Soviets remove all of their
offensive weapons from Cuba.

During the public phase of the Crisis, tensions began to build on both
sides. Kennedy eventually ordered low-level reconnaissance missions
once every two hours. On the 25th of October Kennedy pulled the
quarantine line back and raised military readiness to DEFCON 2. Then
on the 26th EX-COMM heard from Khrushchev in an impassioned letter. He
proposed removing Soviet missiles and personnel if the U.S. would
guarantee not to invade Cuba. October 27 was the worst day of the
crisis. A U-2 was shot down over Cuba and EX-COMM received a second
letter from Khrushchev demanding the removal of U.S. missiles in
Turkey in exchange for Soviet missiles in Cuba. Attorney General
Robert Kennedy suggested ignoring the second letter and contacted
Soviet Ambassador Anatoly Dobrynin to tell him of the U.S. agreement
with the first.

Tensions finally began to ease on October 28 when Khrushchev announced
that he would dismantle the installations and return the missiles to
the Soviet Union, expressing his trust that the United States would
not invade Cuba. Further negotiations were held to implement the
October 28 agreement, including a United States demand that Soviet
light bombers be removed from Cuba, and specifying the exact form and
conditions of United States assurances not to invade Cuba. 

My cousin was in the Navy at the time and was a gunner on a destroyer
that was involved in the quarantine.  He had to sit at his gun turret
24 hours a day, was only allowed to leave to go to the bathroom.
According to him, it was very tense but they were ready to blast
anything that tried to get through the line of naval vessels.


Regards,
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-17T12:31:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9g17rbFjkoU1@mid.individual.net>`
- **References:** `<i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <gtcj97lopkemftat2hpv7kk9sqrachc248@4ax.com> <9furafFfojU1@mid.individual.net> <pn4m975v7mrd2raebfeonkgv0l4uqggg9f@4ax.com>`

```
SkippyPB wrote:
> On Sun, 16 Oct 2011 14:45:49 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[157 more quoted lines elided]…
> Regards,

Thanks for that Steve.

I remember the missile crisis very well. It is amazing how often during the 
Cold War both sides approached the abyss and I think there is a certain 
element of luck involved, as well as sanity prevailing, that lets us be here 
today to discuss it.

Luck is always good to have but we need to work on minimizing it if we are 
to deal with the problems of the future :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2011-10-16T14:22:24+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fupujF6phU1@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com>`

```
HeyBub wrote:
> Alistair Maclean wrote:
>> On Oct 14, 1:15 am, "Pete Dashwood"
…[29 more quoted lines elided]…
> It makes one proud to be an American.

You cracked me up, Jerry... :-)

I hope the guy at the console has the same sense of humour. :-)

Pete.
```

###### ↳ ↳ ↳ Re: OT: Trouble in Paradise

_(reply depth: 17)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2011-10-16T12:07:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fvvn4Fo24U2@mid.individual.net>`
- **References:** `<9f4924F1huU1@mid.individual.net> <i8mdnRCxkPwESwjTnZ2dnUVZ_gWdnZ2d@earthlink.com> <j75431$g3r$1@reader1.panix.com> <be7f4f63-84d7-4a91-ba80-8f5e349d8619@s14g2000vbj.googlegroups.com> <j772b7$j9e$1@reader1.panix.com> <6c8948e7-9a90-4f8c-a8eb-3da17fc4220d@u2g2000yqi.googlegroups.com> <9fpd9mFgehU1@mid.individual.net> <0734bc88-db53-432a-b0d2-eadd2443966e@p25g2000yqh.googlegroups.com> <ksqdndYkz5_b4wTTnZ2dnUVZ_oOdnZ2d@earthlink.com> <9fupujF6phU1@mid.individual.net>`

```
In article <9fupujF6phU1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> HeyBub wrote:
>> Alistair Maclean wrote:
…[34 more quoted lines elided]…
> I hope the guy at the console has the same sense of humour. :-)

He got it wrong, anyway.  He is not in Virginia, he is in Colorado Springs.
:-)

bill
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
