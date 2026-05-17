[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: Some good advice

_13 messages · 7 participants · 2014-06 → 2014-08_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT: Some good advice

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-06-11T20:58:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bvsc8vF8uicU1@mid.individual.net>`

```
I was looking at various web development frameworks to see if I need/want to
change from using C#/ASP.NET. (Not that I have time at the moment to do ANY
further web development...)

Anyway, I came across an extremely well written article that had some real
pearls of wisdom applicable to development in any language.

The author made a case for not getting too bogged down in the details of a
given approach (or language), but to step back occasionally and look at the
functionality you are trying to achieve.

The bit that made me smile was a quote from Donald Knuth. Here's the
context:

"If you're developing a brand new website, and you're worried about scaling
it to millions of users, you're focusing on a problem that doesn't exist.
This is called premature optimization. Donald Knuth explains that in the
computer science world, "Premature optimization is the root of all evil."

Don't be evil. Just pick a framework already. And go write some code."

It reminded me of the guy who attended a fancy dress ball in his boxer
shorts.

"So what are you meant to be?"

"Premature ejaculation."

"Premature ejaculation?"

"I've just come in my underpants...".

Focusing on problems that don't exist is something that does seem to pervade
program development.

One example:

I have seen numerous occasions where fixation and anxiety about performance
has set development back by weeks. It is exactly what Knuth describes,
"premature optimization".

The Boss wants a solution that is better than his competitors (fair
enough...) so he presses development for performance optimization before the
code is even written. (Very few professional programmers deliberately write
code that is designed to perform poorly...)

Get a solution, then optimize it.

It might be that there is no need to. In the rare cases where it does need
to be partially rewritten, the experience gained in the first draft makes it
better than if you had tried to optimize it from the start.

(I like to use a prototype as a Proof of Concept if I am doing something
that is "unknown territory". I recently spent some time developing such a
prototype as a general solution, then found the performance was very
disappointing. (It was using C# Reflection so the code could be
generalized). Removing the Reflection and making it emit "case-specific"code
was not as difficult as doing that from scratch would have been, and I had
the benefit of hindsight from experience gained in developing the
prototype.)

Another one:

The code has to be ready by Friday because the fate of nations hangs on it.

No, it doesn't.

The universe in general will continue, whether your code is ready or not.
Sure, it would be advantageous to have it by Friday, but life will go on
whether it is ready then or a little later. And if the "Friday solution" has
been hastily thrown together under pressure, it will come back and bite you
on the bum. (Being in this situation in the first place reflects on
Management failing to manage properly and really has nothing to do with
Development.)

Invest your time in designing and building a solution; don't hold yourself
back with premature optimization.

Pete.
I used to write COBOL...now I can do anything."
```

#### ↳ Re: OT: Some good advice

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-06-11T21:34:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p2@usenetarchives.gap>`
- **In-Reply-To:** `<bvsc8vF8uicU1@mid.individual.net>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net>`

```
In article ,
Pete Dashwood wrote:

[snip]

› The Boss wants a solution that is better than his competitors (fair 
› enough...) so he presses development for performance optimization before the 
…[7 more quoted lines elided]…
› better than if you had tried to optimize it from the start.

On the one hand, yes... when designing a thing which will bear loads one
must first determine how much of a load one wishes to bear.

Two passengers, maybe young children? A Voklswagen Beetle.

Five passengers? A Vespa in Saigon. (sorry, I could not resist)

A few hundred pounds of cargo? A station wagon (Brit. 'estate wagon').

A few ton(ne)s? A shipping container.

... et and cetera, across disciplines. A cottage is not a mansion is not
a grand hotel, a path is not a street is not a road is not a toll-way,
single-strand wire is not multi-strand-wire is not the cable that supplies
a city from a power-station.

Your anticipated load determines your architecture... EXCEPT...

... once a system is put into place it is subject to certain physical
laws, among them, inertia.

Patches fly, lookup-files beget lookup-files, code gets so large that I've
seen comments of 'REMOVED FROM LIBRARIAN 1987 BECAUSE CODE WAS TOO LARGE
FOR LIBRARIAN'... followed by twenty-something *more* years of change-log.

Folks resisted these 'new systems' - not as good as the old paper ones
where Everyone Knew where everything was! - and then they grew comfortable
with the new systems... and then folks began to demand more of the new
systems and transaction volume increased.

And in case anyone thinks I speak only of Glass Houses and High Priests...
does anyone remember when the entire UseNet feed could pass through a
1200-baud modem?

DD
```

##### ↳ ↳ Re: OT: Some good advice

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-06-12T03:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p2@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p2@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[40 more quoted lines elided]…
› of change-log.
 
› Yep, that has certainly been the way of it...
› 
…[3 more quoted lines elided]…
› more of the new systems and transaction volume increased.

I believe this is addressed by what the kids nowadays call "scaling"... ( to
me, it has nasty lizard overtones and conjures images of castle walls and
boiling oil... I don't like it as a term, but the concept is fine.)

The idea seems to be that, back in the days when you were looking at what
size car or truck you would need, based on the estimated load, as you
pointed out, you SHOULD have been thinking in terms of something NOT limited
by load at all (obviously within reason) and come up with a hovercraft that
had an extendable deck... (this obviates the problem of scaling a Volkswagen
into an 18 wheel articulated rig...no wheels, no problem.)

This would be "scalable"...

Of course, if you really did this, your management would scream at you for
building an ugly overkill solution to the problem of transporting a few
people to the nearest pub, and your defense, showing the savings on tyres
and wheels would not get the attention it properly deserved.

Clearly, there are a whole raft of other problems attached to building
hovercraft... but the number of wheels is not one of them.

So it seems like you're damned if you do and you're damned if you don't.
Build what is needed, they'll squeal because it isn't "scalable"; build
something "scalable" and they'll say it is more than they need.

I reckon the Transformer movies have the right idea...

And Lego, of course.

(I have been building "Lego software" for over 20 years now and have very
little trouble in scaling it... the building blocks can be easily
re-arranged and re-used and if they are "objects" (as they are in my case)
they can be easily "cloned" (instantiated) to fit wherever needed.)


›
› And in case anyone thinks I speak only of Glass Houses and High
› Priests... does anyone remember when the entire UseNet feed could
› pass through a 1200-baud modem?

Sure. I remember being terribly impressed when it became possible to buy a
2400 baud modem which could run on batteries and fit in your pocket. (the
"pocket rocket"... I probably still have one in storage somewhere.)

Thanks for your response Doc. I was thinking about you the other day and
hoping you are OK. :-)

Pete.

›
› DD

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: OT: Some good advice

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-06-12T09:53:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p3@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p2@usenetarchives.gap> <gap-e91952fcda-p3@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
 
› [snip]
 
›› Patches fly, lookup-files beget lookup-files, code gets so large that
›› I've seen comments of 'REMOVED FROM LIBRARIAN 1987 BECAUSE CODE WAS
…[12 more quoted lines elided]…
› boiling oil... I don't like it as a term, but the concept is fine.)

It may be time to pause and revel in that impossible-to-learn English
language, Mr Dashwood. Years ago - before there were computers to
distract them - youngsters used to build 'scale models' of aircraft and
ships, musicians and vocalists would spend hours practising their scales
and detectives mused 'There was something fishy about the butler... I
think he was a Pisces, working for scale.'

› 
› The idea seems to be that, back in the days when you were looking at what 
…[4 more quoted lines elided]…
› into an 18 wheel articulated rig...no wheels, no problem.)

Shoulda, coulda, woulda. A few years back folks started making cordless
telephones, one that communicated with the house line through a 'base
station'... remember those? As land-lines go out of fashion so do such
devices but I've noticed that newer models no longer use custom-designed
batteries in the handsets, they use standard cells one can purchase at
many stores.

'Build with stuff already at hand and easily replaced' sounds simple
enough to be Good Advice; this is a reason for making system libraries and
common subroutines for date-arithmetic, error-handling and the like.

Another reason for doing so is that using standardised parts is less
expensive *and* the pool of folks who can maintain the final structure is
larger. There are lots of folks out there who can change the oil-filter
of a family car with relative ease; that might not be the case with a
hovercraft.

› 
› This would be "scalable"...
…[4 more quoted lines elided]…
› and wheels would not get the attention it properly deserved.

There's also the difficulty of having the pub-crawling vehicle conform to
local regulations about what is permitted on the streets it is expected to
traverse; in the United States of America this is called 'street-legal'
and presenting a solution to a problem of transportation with a device
that is not street-legal demonstrates a fundamental, perhaps insuperable,
misunderstanding on the builder's part.

› 
› Clearly, there are a whole raft of other problems attached to building 
…[4 more quoted lines elided]…
› something "scalable" and they'll say it is more than they need.

Welcome to the World of Business, Mr Dashwood! So nice to have you here,
there's Good Work to be done... watch out for those guys who have
corner-offices and monograms on their shirt-cuffs, though.

[snip]

› Thanks for your response Doc. I was thinking about you the other day and
› hoping you are OK. :-)

You really should have better to do with you time, Mr Dashwood, but I
appreciate your concern. I saw some job-listings the other day where a
couple of NZ companies (Intergen and Provoke) were looking for Project
Managers to expand into the North American market - Seattle, a mere
couple-three thousand miles from my domicile - and I was reminded of you,
as well.

DD
```

##### ↳ ↳ Re: OT: Some good advice

- **From:** "doug_at_milmac_dot_com" <ua-author-176133@usenetarchives.gap>
- **Date:** 2014-06-12T07:14:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p2@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p2@usenetarchives.gap>`

```
doc··f@pa··x.com () wrote in news:lnb03n$3r$1··@rea··x.com:

› [...]
› 
…[3 more quoted lines elided]…
› 
Sadly, UseNet participation has declined so much that those days will probably soon return.
```

###### ↳ ↳ ↳ Re: OT: Some good advice

- **From:** "bill" <ua-author-12423647@usenetarchives.gap>
- **Date:** 2014-06-12T08:45:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p5@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p2@usenetarchives.gap> <gap-e91952fcda-p5@usenetarchives.gap>`

```
In article ,
Doug Miller writes:
› doc··f@pa··x.com () wrote in news:lnb03n$3r$1··@rea··x.com:
› 
…[6 more quoted lines elided]…
› Sadly, UseNet participation has declined so much that those days will probably soon return.

It is neither the number of participants or the sheer volume that is the
value of USENET. I, for one, look forward to the days when it returns
to a small number of users exchanging less but more useful information.

bill

Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
bil··9@cs.··n.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include
```

##### ↳ ↳ Re: OT: Some good advice

- **From:** "swiegand" <ua-author-131803@usenetarchives.gap>
- **Date:** 2014-06-12T11:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p2@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p2@usenetarchives.gap>`

```
On Thu, 12 Jun 2014 01:34:47 +0000 (UTC), doc··f@pa··x.com () wrote:

› In article ,
› Pete Dashwood  wrote:
…[48 more quoted lines elided]…
› DD

My first foray into a precursor of Usenet was done with a 300 Baud
modem on a Commodore C-64 and a site named CompuServe. Only around 30
or so years ago!

Regards,
               (o o) 
       -oOO--(_)--OOo-

"I always wanted to be somebody, but now I realize 
 I should have been more specific."
--  Lily Tomlin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: OT: Some good advice

- **From:** "me" <ua-author-683166@usenetarchives.gap>
- **Date:** 2014-08-02T14:01:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p2@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p2@usenetarchives.gap>`

```
wrote in message news:lnb03n$3r$1··@rea··...
› In article ,
› Pete Dashwood  wrote:
…[6 more quoted lines elided]…
› 
Well, actually it's an Estate Car though I prefer to use my Freelander for
transporting heavy loads even though it's got a high boot floor
```

###### ↳ ↳ ↳ Re: OT: Some good advice

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-08-03T12:23:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p8@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p2@usenetarchives.gap> <gap-e91952fcda-p8@usenetarchives.gap>`

```
In article , me wrote:
›  wrote in message news:lnb03n$3r$1··@rea··...
›› In article ,
…[9 more quoted lines elided]…
› transporting heavy loads even though it's got a high boot floor 

Thanks greatly... stout efforts are needed to keep countries separated by
a common language!

DD
```

#### ↳ Re: OT: Some good advice

- **From:** "doug_at_milmac_dot_com" <ua-author-176133@usenetarchives.gap>
- **Date:** 2014-06-12T07:12:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p10@usenetarchives.gap>`
- **In-Reply-To:** `<bvsc8vF8uicU1@mid.individual.net>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net>`

```
"Pete Dashwood" wrote in news:bvsc8vF8uicU1
@mid.individual.net:

› [...]
› The Boss wants a solution that is better than his competitors (fair 
› enough...) so he presses development for performance optimization before the 
› code is even written. (Very few professional programmers deliberately write 
› code that is designed to perform poorly...)

No, but many write code that *does* perform poorly, due to ignorance of the principles of
writing code that performs well.

› Get a solution, then optimize it.

I couldn't disagree more. Code that is written with little or no thought to how it will perform
often cannot be optimized but must be completely rewritten instead.

› It might be that there is no need to. In the rare cases where it does need
› to be partially rewritten, the experience gained in the first draft makes it
› better than if you had tried to optimize it from the start.

That should be "in the rare cases where it *can be* rewritten only partially...". Better to do it
right, or at least mostly right, the first time. And this *cannot* be done without at least some
attention being paid to performance during the development phase.

[...]
› Another one:
› 
…[10 more quoted lines elided]…
› Development.)

Here, we agree completely. I've asked several development managers "If we don't have
the time to do it *right*, when will we ever find the time to do it *over*?"
```

##### ↳ ↳ Re: OT: Some good advice

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-06-12T20:06:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p10@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p10@usenetarchives.gap>`

```
Doug Miller wrote:
› "Pete Dashwood"  wrote in
› news:bvsc8vF8uicU1 @mid.individual.net:
…[14 more quoted lines elided]…
› completely rewritten instead.

I guess we can agree to differ about this. In the old days (when most of us
used Assembler and low level languages) it was pretty important to
understand how things worked at the platform level and code appropriately.
Processors were "slow" by today's standards (the first machine I ever
programmed, in 1965, executed 300,000 instructions per second (.3 MIPS);
there are digital watches today that are faster than that, yet we thought it
was amazing). We thought it was pretty wonderful that you could access
ferrite core memory in 1.5 microseconds; today that access is thousands of
times faster and the bandwidth for it is many times wider... So, the
"problem" of performance has been addressed by much more powerful hardware
and optimizing compilers for high level languages like COBOL. You would
actually have to have very little understanding at all in order to write
SERIOUSLY degraded code, and yet, I agree it does happen.

I'm not advocating that people should use poorly trained and supervised
programmers, and I'm not advocating that poor code is OK. Neither am I
saying that systems should be "written" rather than "designed". Rather, I'm
saying that performance considerations today (in applications other than
real-time management of physical processes) is not as important as it once
was because modern technology (both hardware and software) absorbs much of
the slack.

The problem is that if you spend a lot of time rethinking code to save a few
milliseconds (maybe...) you are not getting a solution written. If you write
the solution with regard to the solution, rather than the platform, then it
is possible to monitor the solution and detect areas that need performance
improvement. You are also going to have a much better chance of porting that
solution to a different platform if that need should arise.

In the example I gave (using reflection in C# to obtain a general solution -
in effect, the code analyzed the data at run time to decide how to process
it) the performance was many times slower than if the solution had NOT been
generalized, but had been coded specifically for specific sets of data. I
understood before embarking on it that it would not be high performance, but
it was only after it was written that it was possible to measure it and
decide whether it was acceptable or not. (It wasn't... so I re-wrote the
general solution to be generated for specific cases.) My point was that
writing the general solution gave me much more insight into the details of
the processing requirements, so it wasn't as difficult to write the code
generator as it would have been if I had gone that route in the first place.
Because the solution was component based (like ALL my solutions) it was
possible to re-use about 60% of it so no complete rewrite was required.)
BUT, the original generic solution took about 3 weeks to write and the
partial rewrite took about a week, so you could argue that it might have
been quicker to do a specific solution from the start.

I don't personally believe that code performance in high level languages is
as important today as it once was, but I don't think people who do think
that are "wrong", and I would agree it is arguable.
› 
›› It might be that there is no need to.  In the rare cases where it
…[6 more quoted lines elided]…
› first time.

The keyword here is "right". If you define "right" as "code that achieves
the purpose intended" then it isn't "wrong" if it isn't perfect in terms of
performance. It really comes down to the priorities for development. There
are some classes of problem (especially when writing complex software) where
ANY working solution is achieved gratefully... There may be other things
predicated on that solution and you can't proceed at all unless you have it.
Whether it is optimal or not, a working solution allows you to proceed.

(I had exactly this situation a few days ago when I found that a component
written some years back (not by me) and in daily use, failed if it was
pushed... Because other things were predicated on it, I had no choice but to
"fix" it. It was written originally in COBOL and it worked reliably for a
number of years until it had to deal with multi-dimensional COBOL tables.
Surprisingly, the very experienced COBOL guy who wrote it, had a flawed
understanding of how groups and elements under OCCURS are actually stored in
memory... at a single level, no problem; multiple levels, death and
destruction... I looked at the COBOL source but it was convoluted and simply
wrong, in extreme cases. It parsed COBOL using indexing of strings defined
with OCCURS... DEPENDING and, in performance terms, that is a horror show
compared to the methods now available in other languages.I rewrote it in C#
and also extended some of the functionality. I benchmarked the new version
against the old and it is 4 times quicker, so if you "care" about
performance, maybe COBOL is not the tool you should be using...)

› And this *cannot* be done without at least some attention
› being paid to performance during the development phase.

Depends on what you mean by "right". (see above) It really comes down to
development priorities and these vary across sites and projects.
› 
› [...]
…[18 more quoted lines elided]…
› *over*?"

Sadly, there always seems to be time to do it over, but seldom time to
invest in design. I think it is because non-technical managers don't believe
anything is happening if they can't see a result. You have to train them to
get over this. One way is to give them a date ("It'll be ready Friday.")
then on Tuesday, Wednesday, and Thursday, in response to their "Are we there
yet?" whines, you just do the "broken record" ("It'll be ready Friday.").
Make sure you deliver it on Friday (even if it requires some unpaid
overtime; you gave them the date, take responsibility for it...) and you
gradually establish credibility and they become more secure. Training poor
managers is something that is an art but it can be fun and eventually you
get someone who will trust you and support you.
(Then he moves to another company because he is now worth more, so the
process starts over :-))

If you decide to play this game, NEVER make excuses, and NEVER pad your
estimate. If you CAN'T deliver by Friday, accept that you got it wrong, tell
him so, and learn from the experience.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: OT: Some good advice

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-06-13T16:51:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e91952fcda-p11@usenetarchives.gap>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net> <gap-e91952fcda-p10@usenetarchives.gap> <gap-e91952fcda-p11@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› Doug Miller wrote:
 
› [snip]
 
›› That should be "in the rare cases where it *can be* rewritten only
›› partially...". Better to do it right, or at least mostly right, the
…[4 more quoted lines elided]…
› performance.

Mr Dashwood, really... in this world of clouds, smoke, appearances and
deceptions then nothing is perfect in terms of anything.

If you want code that does what it is supposed to do the you may be
satisfied with the eventual product.

If you want perfection you might resign yourself to waiting longer.

› It really comes down to the priorities for development.

I do not believe the priorities for development have changed in the past
half-century:

On time, on spec, on budget... now, pick two.

› There
› are some classes of problem (especially when writing complex software) where
› ANY working solution is achieved gratefully...

Any problem is seen as 'complex software' by a sufficiently inexperienced
programmer... remember your first report with two control-breaks?

As someone posted nigh a decade-and-a-half ago, in
<https://groups.google.com/forum/#!original/comp.lang.cobol/6ShD4zoPu8E/St6GYoXX6REJ>

--begin quoted text

... programming practises which accomplish the desired task in a reliable
and repeatable manner (IF PROGRAM-RUNS PERFORM NEXT-ASSIGNMENT ELSE
PERFORM CODE-LIKE-HELLL UNTIL DAMNED-THING-WORKS)...

--end quoted text

... and the same fool may have posted similarly even earlier... my skills
at searching the UseNet have rusted o'er the years.

(In reading the abovequoted posting in its entirety I was gratified to see
that someone took the responsibility of Proper Teaching so deeply that the
razor-sharp castigation of a negligent practioner was given such
attention... or maybe it was my bones starting to ache in anticipation of
the weather turning bad and I was being Just Nasty... what's Life without
a bit of Uncertainty?)

DD
```

#### ↳ Re: OT: Some good advice

- **From:** "infodynamics_ph" <ua-author-14501527@usenetarchives.gap>
- **Date:** 2014-06-13T01:59:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e91952fcda-p13@usenetarchives.gap>`
- **In-Reply-To:** `<bvsc8vF8uicU1@mid.individual.net>`
- **References:** `<bvsc8vF8uicU1@mid.individual.net>`

```
On Thursday, June 12, 2014 8:58:07 AM UTC+8, Pete Dashwood wrote:
› 
› Invest your time in designing and building a solution; don't hold yourself 
…[4 more quoted lines elided]…
› I used to write COBOL...now I can do anything."


This, I fully agree.... though optimization is by default present when designing UI and coding back-end solutions.


infoRene
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
