[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fortress COBOL - Why?

_164 messages · 27 participants · 2003-07_

---

### Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-10T12:14:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0cb232_6@news.athenanews.com>`

```
I'm starting this thread because of a post from Joe Zitzelberger which said
the following:

">
> It's a symptom of the mainframe being around for 40ish years without
> requiring any users to expose themselves to any change if they didn't
> want to.  Many don't want to."

Several people responded with some interesting insights into why the
Fortress is maintained, but the thread was getting OT and overrun.

I believe this topic is important enough to warrant its own thread.

As  a start, let me define what I mean by the term "Fortress COBOL".

I first coined this term a couple of years ago when I was writing about the
extreme entrenched resistance on many mainframe sites to the new features in
COBOL. (I wish I could say the same occurs on non-mainframe sites, to make
it sound more balanced, but the fact is that theren't a lot of non-mainframe
COBOL sites I know of, and those I have seen are much more into experiment
and change (and are familiar with and glad to use "standard" software and
tools as well as COBOL) and simply don't have the "fortress" mentality.) It
bothered me especially that there was (and still is) strong resistance to
the use of Object Oriented Programming, even though COBOL now supports it.

Why did this bother me?

Because I could see that the future of programming is in OO. (It ISN'T just
another "fad" that would be fashionable for a while then disappear. It
represents a real advance in the art of programming and has been eagerly
embraced by everything Client/Server, to the point where the languages,
Operating Systems, and current Application packages and software all make
use of Objects. These Objects can be wrapped to make sharable, re-usable,
components, and this is quietly and quickly revolutionising the way computer
systems are developed and businesses are supported by IT.(I believe this
will bring about the demise of Procedural programming as we understand it,
but that is another story...)

It is like a horde of Barbarians riding fast little ponies and capturing the
outposts that stand in their way.They didn't fight "fair" in the "accepted"
way of doing battle, they simply overran the defence while the defenders
were implementing their "Standard Operating Procedure for attacks on our
Authority"  In many cases the defenders simply adopted the Barbarian culture
and started breeding their own fast little ponies... Many found that,
although this was a different culture, it was exhilarating and fun.
Also, instead of keeping the peasants in Serfdom, dependent on the goodwill
of the Lord of the Manor, the Barbarians actually embraced the peasants and
liberated them towards independence and self sufficiency in things IT...

The only resistance came from the Great Castles of Mainframe COBOL.

Here are the attributes that qualify a site as "Fortress" in my book (Not
all of these are necessary to ensure proliferation of the "Fortress COBOL"
mentality):

1. Use of 40 year old Development Methodology (usually, the "waterfall"),
where each phase is signed off before the next one can start. (Not suitable
for fast ponies, rather Clydesdale war horses...). Fortress sites see no
requirement to change this or even experiment with alternative
approaches...)

2. Root your Applications in the COBOL file system, which is completely
closed, and ensures that a new COBOL program must be written every time you
need a report...("We've always used ISAM, VSAM, for random access and our
systems work fine; why would we need a Database and have to acquire new
skills to use it?" This is an actual quote from a senior manager around 6
years ago. He wasn't wrong, but he wasn't using much vision either. Today,
they have RDB technology and freely exchange data between departments
WITHOUT the need to get IT to develop COBOL report programs for them...) As
at least one poster mentioned, most sites (even Fortress ones) have now been
dragged kicking and screaming into Relational technology.(I can smile now at
the extreme resistance I encountered right here in CLC when I first started
suggesting that maybe the COBOL file system was not a good option for the
future...).

3. View anything that isn't from IBM with extreme suspicion. View anything
NEW from IBM with equal suspicion.

4. PCs are toys and cannot be taken seriouly. Real user interfaces are by
character entry on a green screen. CICS is the ultimate TP monitor. (When
the peasants threaten revolt unless they get GUI, ensure that whatever they
get will be awful, will take a long time to develop, and will NEVER be as
good as if they had let us use CICS with native 3270. Colour is just
confusing, and graphics are for children and geeks...).

5. Don't use anything in COBOL that is subsequent to 1985, or requires more
than one line to write.

While the above is intended to be tongue-in-cheek, some of it is probably
too close to the bone for some people...<G>

For some years now I have wondered long and often as to WHY this attitude
pervades.

Generally, computer people are not stupid.

Is it just a "control and power" thing?

Is it fear of new things?

Is it simply apathy on the part of programmers? (Yet almost invariably, we
find at least ONE bright eyed bushy tailed programmer who "wants to know" on
most sites. Do they get the "yearning for learning" knocked out of them by
dim-witted managers and surly colleagues?)

I believe Joe's comment at the start of this post gives some insight into
the answer to WHY.

I would appreciate any opinions or discussion from anyone else who has
thoughts on this.

If we can understand the reasons for it, it may be possible to do something
about it.

Pete.
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-09T20:21:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beif33$87e$1@slb3.atl.mindspring.net>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
I'll respond in more detail, but it seems to me that there is SOME confusion
in Pete's note between his use of

   "mainframe"
        versus
    "IBM mainframe"

I have MINIMAL experience outside the IBM MVS-OS/390-z/OS environments (a
little VM, but no VSE - much less NON-IBM mainframes).   Whether all of
Pete's note is INTENDED to apply to all "proprietary mainframes" or JUST
IBM's - isn't clear to me.
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-10T21:36:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d3420_9@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beif33$87e$1@slb3.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:beif33$87e$1@slb3.atl.mindspring.net...
> I'll respond in more detail, but it seems to me that there is SOME
confusion
> in Pete's note between his use of
>
…[8 more quoted lines elided]…
>

Would it make any difference, Bill <G>?

It is an attitude of mind that I refer to as Fortress COBOL. It is almost
like a "siege mentality"...

I have found it to be prevalent on IBM installations but they are not
exclusive in their use of it.

Neither am I looking for "exclusions" on the basis of "Well, that can't
apply to us because we're <whatever>"

The goal here is to try and isolate the factors that lead to the development
of the Fortress Mentality.

Understand WHY it is so.

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T08:31:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejmbn$1g8$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beif33$87e$1@slb3.atl.mindspring.net> <3f0d3420_9@news.athenanews.com>`

```
In article <3f0d3420_9@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:

[snip]

>The goal here is to try and isolate the factors that lead to the development
>of the Fortress Mentality.

Any subset of an organisation usually reflects the goals, desires and 
values of that organisation.  A department does not exist in a vacuum.

Organisations exist to make money.  Money is to be guarded.  DP/IT/MIS 
systems manipulate representations of inventory and money.  Lose track of 
inventory or money, lose your company.

Oh... and don't forget 'a fish rots from the head'.

(Excessive use of simple nominative sentences can be gruelling.)

DD
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-10T01:48:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34685$3d2167e0$dfccf943@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
Well first of all lets face it, compared to many other languages COBOL has
historically not been dynamic in terms of changes and enhancements being
made to the language. This leads to people becoming complacent and adopting
the attitude of making do with what is available. LE may be great but how
many people already had code to do LE functions because they could not wait
and did not know that it was coming? Also prior to the internet, keeping up
with changes was pretty hit or miss depending on whatever magazines a
person read. Most of the time we did not know of the changes that were in
the pipeline. Most of the time the changes came by surprise with a new
release of the compiler. These days we have much more advance information.

As to OO in COBOL, name one really first rate book that covers this
subject, much less one that relates it to components and demonstrates their
power. (I have not finished Chris Richardson's book yet. It may be the one
but it is too early for me to tell). The main coverage of this seems to be
in vendor documentation that comes with COBOL environments costing in the
multiple thousands of dollars.

The first book on OO COBOL that I read was "Object Orientation An
Introduction for COBOL Programmers" by Raymound Obin, Micro Focus
Publishing. This showed how you could code exsisting COBOL do some OO type
things. It povided some definitions with some gaps (IIRC Factory was not
explained very well.) It disscused some possible syntax additions to COBOL.
This was published in 1993 and the first page mentions that the new
standard will be complete in 1997. Hard to get excited when access to a
real compiler seemed so far in the future.

The next OO COBOL book I bought was "Object-Oriented Development in COBOL"
by Andrew Topper. This was published in 1995. If you have a strong stomach
and can forget how much you overpaid for this book which is so flawed on so
many levels, then you could get something out of it. After reading it I
remember expecting to hear "real soon" about the new OO COBOL but it never
seemed to come.

There were some othe COBOL books that dicussed OO syntax but none ever
contained any powerful examples. And with no standard what consevartive
business is willing to bet on what may turn out to be a proprietary object
technology? If you think they were wrong then I ask you this: How would you
feel today if your business depended on 10,000 IBM OO COBOL programs using
the now discarded System Object Model (SOM)?

The best OO COBOL book that I have found to date is Will Price's "Elements
of Object Oriented COBOL". This is the first book with lots of examples.
Unfortunately it also contains a fair number errors, most of which an
experienced person might have little trouble with, but they could throw off
a beginner. This is why I would not consider it a first rate book. Also it
is Micro Focus proprietary but that is hardly the books fault. Being
published in 2001 (2nd edition) it still predates the debut of the 2002
Standard. How many vendors will implement that standard and if they don't,
how effective a standard will it be?

So despite trying, it is not so easy to learn OO COBOL on an economy
budget.  

One last point. At first OO programming sounds like a lot of hype. There
are a lot of new terms that seem to just be new words for old concepts. OO
programs don't CALL subprograms and pass them parameters, they INVOKE the
and send them message. Wow! What an advance!  I recall seeing lots of two
columns lists with the old terms in one column and the new terms in
another. Like most I was not visionary enough to see where all of this was
going. It was not until COM and other similar technologies came out that
the light began to pierce the darkness.

Even after all of this, I am faced with the fact that for me to progress
into OO COBOL, it will require an investment which may not be cost
effective so late in my career. Even if Chris Richardsond's book is first
rate and an out-of-the-park home run, VB.NET may make more career sense
besides costing less than OO COBOL.

<end of my top post>

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in article
<3f0cb232_6@news.athenanews.com>...
> I'm starting this thread because of a post from Joe Zitzelberger which
said
> the following:
> 
…[12 more quoted lines elided]…
> I first coined this term a couple of years ago when I was writing about
the
> extreme entrenched resistance on many mainframe sites to the new features
in
> COBOL. (I wish I could say the same occurs on non-mainframe sites, to
make
> it sound more balanced, but the fact is that theren't a lot of
non-mainframe
> COBOL sites I know of, and those I have seen are much more into
experiment
> and change (and are familiar with and glad to use "standard" software and
> tools as well as COBOL) and simply don't have the "fortress" mentality.)
It
> bothered me especially that there was (and still is) strong resistance to
> the use of Object Oriented Programming, even though COBOL now supports
it.
> 
> Why did this bother me?
> 
> Because I could see that the future of programming is in OO. (It ISN'T
just
> another "fad" that would be fashionable for a while then disappear. It
> represents a real advance in the art of programming and has been eagerly
…[3 more quoted lines elided]…
> components, and this is quietly and quickly revolutionising the way
computer
> systems are developed and businesses are supported by IT.(I believe this
> will bring about the demise of Procedural programming as we understand
it,
> but that is another story...)
> 
> It is like a horde of Barbarians riding fast little ponies and capturing
the
> outposts that stand in their way.They didn't fight "fair" in the
"accepted"
> way of doing battle, they simply overran the defence while the defenders
> were implementing their "Standard Operating Procedure for attacks on our
> Authority"  In many cases the defenders simply adopted the Barbarian
culture
> and started breeding their own fast little ponies... Many found that,
> although this was a different culture, it was exhilarating and fun.
> Also, instead of keeping the peasants in Serfdom, dependent on the
goodwill
> of the Lord of the Manor, the Barbarians actually embraced the peasants
and
> liberated them towards independence and self sufficiency in things IT...
> 
…[3 more quoted lines elided]…
> all of these are necessary to ensure proliferation of the "Fortress
COBOL"
> mentality):
> 
> 1. Use of 40 year old Development Methodology (usually, the "waterfall"),
> where each phase is signed off before the next one can start. (Not
suitable
> for fast ponies, rather Clydesdale war horses...). Fortress sites see no
> requirement to change this or even experiment with alternative
…[3 more quoted lines elided]…
> closed, and ensures that a new COBOL program must be written every time
you
> need a report...("We've always used ISAM, VSAM, for random access and our
> systems work fine; why would we need a Database and have to acquire new
> skills to use it?" This is an actual quote from a senior manager around 6
> years ago. He wasn't wrong, but he wasn't using much vision either.
Today,
> they have RDB technology and freely exchange data between departments
> WITHOUT the need to get IT to develop COBOL report programs for them...)
As
> at least one poster mentioned, most sites (even Fortress ones) have now
been
> dragged kicking and screaming into Relational technology.(I can smile now
at
> the extreme resistance I encountered right here in CLC when I first
started
> suggesting that maybe the COBOL file system was not a good option for the
> future...).
> 
> 3. View anything that isn't from IBM with extreme suspicion. View
anything
> NEW from IBM with equal suspicion.
> 
> 4. PCs are toys and cannot be taken seriouly. Real user interfaces are by
> character entry on a green screen. CICS is the ultimate TP monitor. (When
> the peasants threaten revolt unless they get GUI, ensure that whatever
they
> get will be awful, will take a long time to develop, and will NEVER be as
> good as if they had let us use CICS with native 3270. Colour is just
> confusing, and graphics are for children and geeks...).
> 
> 5. Don't use anything in COBOL that is subsequent to 1985, or requires
more
> than one line to write.
> 
…[12 more quoted lines elided]…
> Is it simply apathy on the part of programmers? (Yet almost invariably,
we
> find at least ONE bright eyed bushy tailed programmer who "wants to know"
on
> most sites. Do they get the "yearning for learning" knocked out of them
by
> dim-witted managers and surly colleagues?)
> 
…[6 more quoted lines elided]…
> If we can understand the reasons for it, it may be possible to do
something
> about it.
> 
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-10T22:22:11+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d3ee5_7@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34685$3d2167e0$dfccf943@chottel>`

```

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c34685$3d2167e0$dfccf943@chottel...
> Well first of all lets face it, compared to many other languages COBOL has
> historically not been dynamic in terms of changes and enhancements being
> made to the language. This leads to people becoming complacent and
adopting
> the attitude of making do with what is available. LE may be great but how
> many people already had code to do LE functions because they could not
wait
> and did not know that it was coming? Also prior to the internet, keeping
up
> with changes was pretty hit or miss depending on whatever magazines a
> person read. Most of the time we did not know of the changes that were in
…[4 more quoted lines elided]…
> subject, much less one that relates it to components and demonstrates
their
> power. (I have not finished Chris Richardson's book yet. It may be the one
> but it is too early for me to tell). The main coverage of this seems to be
…[7 more quoted lines elided]…
> explained very well.) It disscused some possible syntax additions to
COBOL.
> This was published in 1993 and the first page mentions that the new
> standard will be complete in 1997. Hard to get excited when access to a
…[4 more quoted lines elided]…
> and can forget how much you overpaid for this book which is so flawed on
so
> many levels, then you could get something out of it. After reading it I
> remember expecting to hear "real soon" about the new OO COBOL but it never
…[5 more quoted lines elided]…
> technology? If you think they were wrong then I ask you this: How would
you
> feel today if your business depended on 10,000 IBM OO COBOL programs using
> the now discarded System Object Model (SOM)?
…[4 more quoted lines elided]…
> experienced person might have little trouble with, but they could throw
off
> a beginner. This is why I would not consider it a first rate book. Also it
> is Micro Focus proprietary but that is hardly the books fault. Being
…[44 more quoted lines elided]…
> > extreme entrenched resistance on many mainframe sites to the new
features
> in
> > COBOL. (I wish I could say the same occurs on non-mainframe sites, to
…[5 more quoted lines elided]…
> > and change (and are familiar with and glad to use "standard" software
and
> > tools as well as COBOL) and simply don't have the "fortress" mentality.)
> It
> > bothered me especially that there was (and still is) strong resistance
to
> > the use of Object Oriented Programming, even though COBOL now supports
> it.
…[8 more quoted lines elided]…
> > Operating Systems, and current Application packages and software all
make
> > use of Objects. These Objects can be wrapped to make sharable,
re-usable,
> > components, and this is quietly and quickly revolutionising the way
> computer
…[23 more quoted lines elided]…
> > Here are the attributes that qualify a site as "Fortress" in my book
(Not
> > all of these are necessary to ensure proliferation of the "Fortress
> COBOL"
> > mentality):
> >
> > 1. Use of 40 year old Development Methodology (usually, the
"waterfall"),
> > where each phase is signed off before the next one can start. (Not
> suitable
…[7 more quoted lines elided]…
> > need a report...("We've always used ISAM, VSAM, for random access and
our
> > systems work fine; why would we need a Database and have to acquire new
> > skills to use it?" This is an actual quote from a senior manager around
6
> > years ago. He wasn't wrong, but he wasn't using much vision either.
> Today,
…[5 more quoted lines elided]…
> > dragged kicking and screaming into Relational technology.(I can smile
now
> at
> > the extreme resistance I encountered right here in CLC when I first
> started
> > suggesting that maybe the COBOL file system was not a good option for
the
> > future...).
> >
…[4 more quoted lines elided]…
> > 4. PCs are toys and cannot be taken seriouly. Real user interfaces are
by
> > character entry on a green screen. CICS is the ultimate TP monitor.
(When
> > the peasants threaten revolt unless they get GUI, ensure that whatever
> they
> > get will be awful, will take a long time to develop, and will NEVER be
as
> > good as if they had let us use CICS with native 3270. Colour is just
> > confusing, and graphics are for children and geeks...).
…[5 more quoted lines elided]…
> > While the above is intended to be tongue-in-cheek, some of it is
probably
> > too close to the bone for some people...<G>
> >
> > For some years now I have wondered long and often as to WHY this
attitude
> > pervades.
> >
…[8 more quoted lines elided]…
> > find at least ONE bright eyed bushy tailed programmer who "wants to
know"
> on
> > most sites. Do they get the "yearning for learning" knocked out of them
…[3 more quoted lines elided]…
> > I believe Joe's comment at the start of this post gives some insight
into
> > the answer to WHY.
> >
…[10 more quoted lines elided]…
> >
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T00:11:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d5889$1_4@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34685$3d2167e0$dfccf943@chottel>`

```
Sorry I posted a blank one before this, Charles... just ignore it...
("Me fingers ain't wot they used t' be..."
 "No?"
"No, they used t' be me toes...")

Ignore this deeply Freudian revelation also, and move on to the actual
response...<G>

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c34685$3d2167e0$dfccf943@chottel...
> Well first of all lets face it, compared to many other languages COBOL has
> historically not been dynamic in terms of changes and enhancements being
> made to the language. This leads to people becoming complacent and
adopting
> the attitude of making do with what is available. LE may be great but how
> many people already had code to do LE functions because they could not
wait
> and did not know that it was coming? Also prior to the internet, keeping
up
> with changes was pretty hit or miss depending on whatever magazines a
> person read. Most of the time we did not know of the changes that were in
> the pipeline. Most of the time the changes came by surprise with a new
> release of the compiler. These days we have much more advance information.
>
Hmmm...so if there was more "noise" about new facilities, we might see a
better uptake on them?


> As to OO in COBOL, name one really first rate book that covers this
> subject, much less one that relates it to components and demonstrates
their
> power. (I have not finished Chris Richardson's book yet. It may be the one
> but it is too early for me to tell). The main coverage of this seems to be
…[7 more quoted lines elided]…
> explained very well.) It disscused some possible syntax additions to
COBOL.
> This was published in 1993 and the first page mentions that the new
> standard will be complete in 1997. Hard to get excited when access to a
…[4 more quoted lines elided]…
> and can forget how much you overpaid for this book which is so flawed on
so
> many levels, then you could get something out of it. After reading it I
> remember expecting to hear "real soon" about the new OO COBOL but it never
…[5 more quoted lines elided]…
> technology? If you think they were wrong then I ask you this: How would
you
> feel today if your business depended on 10,000 IBM OO COBOL programs using
> the now discarded System Object Model (SOM)?
>

I'm pretty horrified at what you have experienced with regard to books on
OO. Maybe the problem is using books on OO _COBOL_ (although that would
certainly be the obvious place for a COBOL programmer to start...)

As for the demise of SOM, maybe it wouldn't have happened if the Market had
been more amenable...
(Actually, I believe IBM may live to regret this...It wouldn't surprise me
if a more OO approach is tried again, especially as they seem to be pinning
a lot of their hopes on Java...)

> The best OO COBOL book that I have found to date is Will Price's "Elements
> of Object Oriented COBOL". This is the first book with lots of examples.

Yes, I read Wil's book and found it excellent. (In fact I was considering
writing such a book at about the time he released it, but after reading it,
I figured I would be hard pressed to improve on it...<G>)


> Unfortunately it also contains a fair number errors, most of which an
> experienced person might have little trouble with, but they could throw
off
> a beginner. This is why I would not consider it a first rate book.

That's interesting. I didn't see any. As it required the MF compiler I
couldn't test the examples (the CD inside the back cover got broken in my
travels; that's the price of taking something everywhere...) I believe if
you have found errors in it, Charles, it would be worth telling Wil. I know
he would want to improve future editions. He sometimes posts here but I
could forward a message for you by private mail and he can contact you
directly, if you like?

> Also it
> is Micro Focus proprietary but that is hardly the books fault.

Not sure what you mean by this. It was published by ObjectZ which is a
company that is connected with Ed Arranga. Ed publishes the COBOL Report Web
Site, and I understand there is some MicroFocus sponsorship, but I don't
think that would make the book proprietary to MF. (The COBOLWorld Expo 2001
was organised by Ed and Wil Price, under this umbrella. Sadly, this year's
one didn't happen.)

> Being
> published in 2001 (2nd edition) it still predates the debut of the 2002
…[5 more quoted lines elided]…
>

OK. Supposing I put together a "Teach Yourself OO (including COBOL)" course
and it was FREE! How many people here do you think would go for it? I reckon
there'd be less than 6. That's why I won't do it, although I've been tempted
on a few occasions...

The point is, I don't believe it is the budget that is the problem.


> One last point. At first OO programming sounds like a lot of hype. There
> are a lot of new terms that seem to just be new words for old concepts. OO
> programs don't CALL subprograms and pass them parameters, they INVOKE the
> and send them message. Wow! What an advance!

Hold on. That's unfair and uncalled for. It is a superficial negative
reaction and quite unworthy of you, Charles. There are very sound reasons
why Methods are invoked rather than called.  The new words are (for the most
part) NOT just new words for old concepts, but until someone really grasps
the subtle distinctions, they CAN seem that way.

It's like saying "That new water rat is just another kind of  rat. They're
all rodents... no bloody difference..." Then finding that the object
referred to is, in fact, an otter. Except that sometimes it's a
platypus...<G> (in the surreal world of Object Orientation platypuses can
inherit certain traits from otters...). Now, if you have difficulty with
"Spot the Ball", "Find the 10 differences" or can't tell Tarka from a plat
billed duckibus, then OO is probably not for you...


>  I recall seeing lots of two
> columns lists with the old terms in one column and the new terms in
…[3 more quoted lines elided]…
>

Don't be too hard on yourself. For the most part this information is poorly
presented and it is rare to find a succinct statement of the concepts.

> Even after all of this, I am faced with the fact that for me to progress
> into OO COBOL, it will require an investment which may not be cost
> effective so late in my career.

Oddly enough I agree.  I believe OO COBOL has missed the boat. (I know only
a handful of people who are using it, and I only use it for building
components and as "glue" for other people's components...)The knowledge of
OO (in general) is useful for young programmers who are making a career in
"programming", but it is already being overtaken by events, and will be
reincarnated as components. I believe that OO will become necessary
"groundwork theory" to understand the other things that are (and will be)
predicated upon and derived from it. For COBOL programmers who see the end
of their career in sight it is certainly arguable whether or not the
required effort is worthwhile (certainly in financial terms). But then, the
alternative of sitting still and doing nothing is not particularly
attractive either...


>Even if Chris Richardsond's book is first
> rate and an out-of-the-park home run, VB.NET may make more career sense
> besides costing less than OO COBOL.
>

Knowing and understanding OO concepts would not be a hindrance to learning
.NET...


> <end of my top post>
>
I found nothing below it...<G>

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-11T01:30:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c3474b$db980c00$80caf943@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34685$3d2167e0$dfccf943@chottel> <3f0d5889$1_4@news.athenanews.com>`

```
At least they aren't growing out of your back <G>.

Changing from my usual annoying top posting, I am inserting comments below.

<snip>

> I'm pretty horrified at what you have experienced with regard to books on
> OO. Maybe the problem is using books on OO _COBOL_ (although that would
> certainly be the obvious place for a COBOL programmer to start...)
> 

I learned more about OO programming from taking a C++ course than from all
these COBOL books. Also from a Visual Basic book even though that language
was not considered OO by some.

> As for the demise of SOM, maybe it wouldn't have happened if the Market
had
> been more amenable...
> (Actually, I believe IBM may live to regret this...It wouldn't surprise
me
> if a more OO approach is tried again, especially as they seem to be
pinning
> a lot of their hopes on Java...)
> 

I don't think they will regret it because I don't think many places used
SOM. They have not abandoned OO they have just changed direction towards
interoperability with JAVA.

> > The best OO COBOL book that I have found to date is Will Price's
"Elements
> > of Object Oriented COBOL". This is the first book with lots of
examples.
> 
> Yes, I read Wil's book and found it excellent. (In fact I was considering
> writing such a book at about the time he released it, but after reading
it,
> I figured I would be hard pressed to improve on it...<G>)
>

Wel it sounds like you could certainly extend it further into the land of
components.
 
> 
> > Unfortunately it also contains a fair number errors, most of which an
…[7 more quoted lines elided]…
> you have found errors in it, Charles, it would be worth telling Wil. I
know
> he would want to improve future editions. He sometimes posts here but I
> could forward a message for you by private mail and he can contact you
> directly, if you like?
> 
Well I didn't test the examples either but I did study them closely. I
actually bought the book from Mike Murach's company and I emailed them a
list of the errors that I found. I did not receive any response from them
so I don't know what they did with it. I can't put my hands on the email at
this moment but IIRC some of the errors seemed to come from changing an
example and not updating all the places required to keep thge text and code
in sync. The ObjectZ site had an errata list.

> > Also it
> > is Micro Focus proprietary but that is hardly the books fault.
> 
> Not sure what you mean by this. It was published by ObjectZ which is a
> company that is connected with Ed Arranga. Ed publishes the COBOL Report
Web
> Site, and I understand there is some MicroFocus sponsorship, but I don't
> think that would make the book proprietary to MF. (The COBOLWorld Expo
2001
> was organised by Ed and Wil Price, under this umbrella. Sadly, this
year's
> one didn't happen.)
> 
What I meant was the examples were in MF COBOL. When you think about it, so
far all OO COBOL is proprietary. Now that we have the 2002 standard what
will the vendors do? Will they maintain backward compatibility while
providing the 2002 OO syntax. So much time has passed I think some will try
to ignore the standard as being unimportant.

> > Being
> > published in 2001 (2nd edition) it still predates the debut of the 2002
> > Standard. How many vendors will implement that standard and if they
don't,
> > how effective a standard will it be?
> >
…[4 more quoted lines elided]…
> OK. Supposing I put together a "Teach Yourself OO (including COBOL)"
course
> and it was FREE! How many people here do you think would go for it? I
reckon
> there'd be less than 6. That's why I won't do it, although I've been
tempted
> on a few occasions...
> 
> The point is, I don't believe it is the budget that is the problem.

Budget is not a problem for companies but it is for indiviuals. I seem to
recall you mentioning that you could not justify purchasing NetCOBOL for
.NET. It takes a pretty stong motivation or a deep pocket to put out $2000+
for a development environment that could easily become obsolete within five
years or so. I guess it helps if you can write it off as a business
expense.

Well you don't have to do it for free. You could write a book or a series
of magazine articles, whichever you could earn the most from. A lot more
than six were interested in your article on components. Right now the only
other place I know of where this info can be obtained is from the MF or
Fijitsu vendor documentation that comes with their $2000+ products. If you
do it for free I will personally take the course 7 times just to make you
feel better!<G>

> 
> > One last point. At first OO programming sounds like a lot of hype.
There
> > are a lot of new terms that seem to just be new words for old concepts.
OO
> > programs don't CALL subprograms and pass them parameters, they INVOKE
the
> > and send them message. Wow! What an advance!
> 
> Hold on. That's unfair and uncalled for. It is a superficial negative
> reaction and quite unworthy of you, Charles. There are very sound reasons
> why Methods are invoked rather than called.  The new words are (for the
most
> part) NOT just new words for old concepts, but until someone really
grasps
> the subtle distinctions, they CAN seem that way.
> 
> It's like saying "That new water rat is just another kind of  rat.
They're
> all rodents... no bloody difference..." Then finding that the object
> referred to is, in fact, an otter. Except that sometimes it's a
> platypus...<G> (in the surreal world of Object Orientation platypuses can
> inherit certain traits from otters...). Now, if you have difficulty with
> "Spot the Ball", "Find the 10 differences" or can't tell Tarka from a
plat
> billed duckibus, then OO is probably not for you...
> 
Well I did say "at first" and I guess my initial reaction to OO was
superficial and negative in reaction to the seemingly endless glorious
claims that were being made for it. There is a long learning curve before
you get your first glimpse of the glorious component land. Many like Moses
are destined never to enter therein. I think COBOL really missed the boat
because I much prefer the wordier OOCOBOL syntax to the cryptic C++ syntax.
I also don't like all the default behind the scene constuctor stuff of C++.
It would have been better to bring it out into the open and require the
programmer to provide it. The defaults are not usually what you want anyway
so they don't save any work most of the time. What a language. Based upon C
which had an obfuscated C contest. One guy has written 2 books containing
about 150 things you should avoid doing. Now it has the extra added power
of templates thrown in. Powerful yes, but even some of the strongest
proponents of templates are dismayed by how much more unreadable it makes
the language. No wonder Visual Basic and JAVA caught on.

> 
> >  I recall seeing lots of two
> > columns lists with the old terms in one column and the new terms in
> > another. Like most I was not visionary enough to see where all of this
was
> > going. It was not until COM and other similar technologies came out
that
> > the light began to pierce the darkness.
> >
> 
> Don't be too hard on yourself. For the most part this information is
poorly
> presented and it is rare to find a succinct statement of the concepts.
> 
> > Even after all of this, I am faced with the fact that for me to
progress
> > into OO COBOL, it will require an investment which may not be cost
> > effective so late in my career.
> 
> Oddly enough I agree.  I believe OO COBOL has missed the boat. (I know
only
> a handful of people who are using it, and I only use it for building
> components and as "glue" for other people's components...)The knowledge
of
> OO (in general) is useful for young programmers who are making a career
in
> "programming", but it is already being overtaken by events, and will be
> reincarnated as components. I believe that OO will become necessary
> "groundwork theory" to understand the other things that are (and will be)
> predicated upon and derived from it. For COBOL programmers who see the
end
> of their career in sight it is certainly arguable whether or not the
> required effort is worthwhile (certainly in financial terms). But then,
the
> alternative of sitting still and doing nothing is not particularly
> attractive either...
> 

Yeah I don't want them to say there lies Charlie Hottel a mouldering in the
grave, especially not while I am still breathing.

> 
> >Even if Chris Richardsond's book is first
…[4 more quoted lines elided]…
> Knowing and understanding OO concepts would not be a hindrance to
learning
> .NET...
> 
…[3 more quoted lines elided]…
> I found nothing below it...<G>

Are you saying your post was a big nothing?<G>

> 
> Pete.
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-10T21:17:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bel6nm$frp$1@slb9.atl.mindspring.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34685$3d2167e0$dfccf943@chottel> <3f0d5889$1_4@news.athenanews.com> <01c3474b$db980c00$80caf943@chottel>`

```
"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c3474b$db980c00$80caf943@chottel...
<snip>
> >
> What I meant was the examples were in MF COBOL. When you think about it,
so
> far all OO COBOL is proprietary. Now that we have the 2002 standard what
> will the vendors do? Will they maintain backward compatibility while
> providing the 2002 OO syntax. So much time has passed I think some will
try
> to ignore the standard as being unimportant.
>

I thought that I had posted this once (relatively recently) but Micro Focus,
in their NetExpress V4 product fully supports (or claims to support) the
"official" (approved) OO syntax.  They *also* continue to support their
previous syntax - and even allow for a mixing of the two.

May I suggest that you look at:


http://supportline.microfocus.com/supportline/documentation/books/nx40/oppubb.htm

and go to the chapter

    "Chapter 12: Micro Focus OO COBOL Alternative Syntax"

If you actually HAVE that product, you may also be interested in

      " Part 6: Micro Focus OO COBOL Tutorials"
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-11T02:27:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34753$cecb6640$80caf943@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34685$3d2167e0$dfccf943@chottel> <3f0d5889$1_4@news.athenanews.com> <01c3474b$db980c00$80caf943@chottel> <bel6nm$frp$1@slb9.atl.mindspring.net>`

```
Thanks. I did know they proclaimed they were going to support the 2002 OO
syntax, but didn't realize they had already done it. However it takes more
than a single vendor to make a standard a standard.

I plan on getting a copy of a good PC compiler as soon as my powerball
ticket hit the jackpot.

William M. Klein <wmklein@ix.netcom.com> wrote in article
<bel6nm$frp$1@slb9.atl.mindspring.net>...
> "Charles Hottel" <chottel@cpcug.org> wrote in message
> news:01c3474b$db980c00$80caf943@chottel...
> <snip>
> > >
> > What I meant was the examples were in MF COBOL. When you think about
it,
> so
> > far all OO COBOL is proprietary. Now that we have the 2002 standard
what
> > will the vendors do? Will they maintain backward compatibility while
> > providing the 2002 OO syntax. So much time has passed I think some will
…[4 more quoted lines elided]…
> I thought that I had posted this once (relatively recently) but Micro
Focus,
> in their NetExpress V4 product fully supports (or claims to support) the
> "official" (approved) OO syntax.  They *also* continue to support their
…[5 more quoted lines elided]…
>
http://supportline.microfocus.com/supportline/documentation/books/nx40/oppub
b.htm
> 
> and go to the chapter
…[12 more quoted lines elided]…
>
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** Steve Thompson <steve_nospam_t@ix.netcom.com>
- **Date:** 2003-07-09T22:02:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.19768963bd8f4626989684@News.CIS.DFN.DE>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
In article <3f0cb232_6@news.athenanews.com>, 
dashwood@enternet.co.nz says...
> I'm starting this thread because of a post from Joe Zitzelberger which said
> the following:
…[4 more quoted lines elided]…
> > want to.  Many don't want to."
<snip>

My biggest complaint about the "open systems" is that they 
haven't matured. They are treated like tinker toys by their 
biggest proponents. If some software on them fails, re-boot the 
system. Easy to violate and cause problems -- just look at Micro
$**t's software.

On the systems that I work with, yes, we take some time to get 
things written and delivered to the customers, but let's stop 
and look at this.

Most of the systems that I work on (mainframe or PC based) are 
rather complex. So I write code that gets the basic function 
done. Then I start adding to it the bells and whistles. Each set 
of functions added gets a new set of regression tests.

My software takes a while to develop as a result, costs a bit 
more, but doesn't crash over piddly little things. In fact, it 
typically takes some effort to crash it.

Now, is this the waterfall method? I do development in COBOL, 
REXX, RPG, ALC, FORTRAN, OO-COBOL, and CLIST. I try to write as 
much as I can as subroutines that will be portable between 
platforms so that I can compile link and go back to building on 
what we've done before. This type of development is poor-man's 
OO. But do you call this waterfall?

Fortress thinking by me is still there. I see where the fortress 
wanted things to work, and recover when things were bad without 
crashing. So the tinker toy drones got in and threw code on the 
wall and provided nice colorful displays and graphics. 

But in the end, did those things scale? Precious few do/have. 
But the end-roads were made and now the Hidden Cost of Computing 
is being discovered. As a result, the "Open Systems" projects 
are starting to be looked at from the viewpoint of "Show me" 
that you can _____.

Fast small ponies are good. Large draft horses are good. 
Aircraft carriers are good. Helicopters are good. But I sure 
wouldn't want to plow a field using an aircraft carrier. And I 
sure wouldn't want to pull a 20 ton load with 4 Shetland ponies.

As soon as corporations wake up to systems needing to be a mix 
of tools... Screwdrivers just don't scale well into a large pry-
bar.
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-10T02:16:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34689$34d453a0$dfccf943@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE>`

```
Where I work the problem is not waterfall, or RAD, or Agile, or Extreme ...
development. It is an a lack of
adequate, detailed specifications.  Even when deep into the testing phase
most of the bugs are due to
items that were omitted from the specification, that were not uncovered by
extensive questioning. Perhaps it is just my lack of mind reading ability.
I no longer remember how many memos I have written whose subject line reads
as follows:  "x questions regarding project fubar" where x is typically a
two to three digit number.  And then I am told  have a bad attitude or I am
trying to make someone look bad.

Dilbert is so funny, not in an abstract way but because it is so real.

Steve Thompson <steve_nospam_t@ix.netcom.com> wrote in article
<MPG.19768963bd8f4626989684@News.CIS.DFN.DE>...
> In article <3f0cb232_6@news.athenanews.com>, 
> dashwood@enternet.co.nz says...
> > I'm starting this thread because of a post from Joe Zitzelberger which
said
> > the following:
> > 
…[62 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T08:37:59-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejmn7$3k1$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <01c34689$34d453a0$dfccf943@chottel>`

```
In article <01c34689$34d453a0$dfccf943@chottel>,
Charles Hottel <chottel@cpcug.org> wrote:

[snip]

>Perhaps it is just my lack of mind reading ability.

One of my Standard Responses is 'Despite what you tell me I know I am a 
good programmer.  I am a *singing* programmer.  I can be a singing and 
*dancing* programmer... but if you want me to be a singing, dancing and 
mind-reading programmer then my rates will go up.'

>I no longer remember how many memos I have written whose subject line reads
>as follows:  "x questions regarding project fubar" where x is typically a
>two to three digit number.  And then I am told  have a bad attitude or I am
>trying to make someone look bad.

Another of my Standard Responses is 'If all you have to complain about is 
my Attitude then my Work must be *very* good... because Bad Work gets 
complained-about first.  It is my job to transmit user requests into code; 
why don't you, my boss, go tell the users' boss that their inability to 
voice their requests clearly and unambiguously is preventing me from Doing 
My Job?'

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-10T17:22:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0DE717.9030701@Netscape.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <01c34689$34d453a0$dfccf943@chottel>`

```
Charles Hottel wrote:
> Dilbert is so funny, not in an abstract way but because it is so real.

hear hear...
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-07-10T06:26:29-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<I9acnQ7SiNf40JCiXTWJkA@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE>`

```
Steve Thompson wrote:

> My biggest complaint about the "open systems" is that they
> haven't matured. They are treated like tinker toys by their
> biggest proponents. If some software on them fails, re-boot the
> system. Easy to violate and cause problems -- just look at Micro
> $**t's software.

Good point, bad example.

I'm running XP on my desktop and have been for 14 months. I have never
encountered the necessity for an unscheduled re-boot.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** Steve Thompson <steve_nospam_t@ix.netcom.com>
- **Date:** 2003-07-15T00:18:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.197d4aa79853089a989686@News.CIS.DFN.DE>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com>`

```
In article <I9acnQ7SiNf40JCiXTWJkA@giganews.com>, 
nospam@bisusa.com says...
> Steve Thompson wrote:
> 
…[9 more quoted lines elided]…
> encountered the necessity for an unscheduled re-boot.
<snip>

Congratulations! However, at a certain client's location, their 
mainframe's production LPAR has been up for over 60 days. Had to 
put on emergency maint for SYNCSORT, so an IPL was required.

Meanwhile, the webserver has needed to be re-booted at least 
once per week. The DNS servers had have some type of software 
problems and they have had to be re-booted at least twice. There 
are three printer servers that I know of, all three have to be 
rebooted weekly. The AIX systems (that are in production status) 
have not been able to run for 60+ days without at least being 
rebooted twice during that period. Then there are several other 
non-mainframe systems, that can't seem to function w/o having to 
be reloaded (rebooted, IPLed, etc.). Across all these platforms 
we are talking about W2k, AIX/5L, PICK, and AS/400. And last but 
not least, the Exchange server requires being shutdown and 
rebooted every month (can't do backups and flush bad mailboxes 
unless this is done!).

While on the subject of Micro$**t's software, why is it that 
most every time I get security upgrades from them it requires a 
re-boot to install them? And why do almost all of my security 
upgrades have to do with some hole in IE?

Meanwhile, z/OS only needs to be "re-booted" if we have a system 
failure, or must do a POR because of an I/O configuration 
change. We can take down the communications system (VTAM) and 
most every other system level product, update them and restart 
them, typically w/o having to do an IPL. 

I don't see or hear about these kinds of problems with UNISYS or 
Honeywell (the big systems) -- these problems being a need to 
re-load the O/S to keep them running correctly.

In order to demonstrate my example(s), I've only made my point 
even more.

Should and if more of the Professional Staff would point out 
these kinds of problems to their upper management, then I would 
think that more companies would balk at buying and loading the 
latest version while paying for maint. I think more would hold 
their vendors accountable should there be problems, which would 
force the vendors to stop treating their systems as experiments.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-07-15T08:44:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pMycnSAuHOq7mImiU-KYuQ@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE>`

```
Steve Thompson wrote:
>
> While on the subject of Micro$**t's software, why is it that
> most every time I get security upgrades from them it requires a
> re-boot to install them? And why do almost all of my security
> upgrades have to do with some hole in IE?

I don't know. I'll hazard a few guesses. First, as to the re-boot:

1. Whatever's being changed exists in an area of memory unaccessable to
anything but the boot sequence.
2. Code to chase all the links established since the last boot may be
horrifically complicated, prone to errors, or humanly impossible.

IE

1. IE is the part of the OS that interacts with the outside world. If a
virus, for example, wants to diddle with your hard drive, it must first GET
to your hard drive. To GET to your hard drive, it must first (generally)
pass through IE. Think of password file protection as the key to your
strongroom and IE as the moat around the castle. If your biggest threat is
from marauding barbarians, deeping the moat or cutting back branches
deserves more attention than a bigger lock on your vault.

2. IE is more and more integrated into the operating system. A patch to IE
may very well have nothing to do with internet connectivity but instead
involve itself with more fundamental and prosaic processes formerly
conducted by the file system or the timer or something else.

>
> Should and if more of the Professional Staff would point out
…[4 more quoted lines elided]…
> force the vendors to stop treating their systems as experiments.

One of the common laments is "That as soon as we figure out circumventions
to all the known bugs, we get a new release with new bugs to figure out."

All (most?) bugs are not known with a new release. But, by the same token,
they are not knowable. That's why the FDA doesn't rely solely on laboratory
data but instead requires clinical trials. Because of its size, Micros~1
probably does a better job than most software companies by having 300,000
users beta test a new product or release.

People bitch like sex-crazed monkeys over software bugs - but the authors of
the software cannot realistically be blamed. If, for example, Micros~1 alpha
tests an enhancement to already-functioning code for months, then a
half-million beta testers exercise the same code for half a year, what more
could reasonably be expected? At some point the vendor HAS to say: "Stick a
fork in it - it's done."

Then, the day after the general release, some script-kiddie running a
pirated copy of SQL Enterprise Server on an Altos finds a hole that brings
down the New York Stock Exchange and everybody's quick to point fingers.
Software bugs are like taxes: bitch if you like, but they'll always be
there. Our job is to minimze their impact or plan our endeavors to avoid
them.

Or find another line of work - like government service.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** Steve Thompson <steve_nospam_t@ix.netcom.com>
- **Date:** 2003-07-15T14:32:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.197e12dd577b1d75989688@News.CIS.DFN.DE>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com>`

```
In article <pMycnSAuHOq7mImiU-KYuQ@giganews.com>, 
nospam@bisusa.com says...
<snip>
> All (most?) bugs are not known with a new release. But, by the same token,
> they are not knowable. That's why the FDA doesn't rely solely on laboratory
…[7 more quoted lines elided]…
> half-million beta testers exercise the same code for half a year, what more

So how is it that AMD is able to put out a chip that does not 
have the bugs in it that Intel's has? Why was it that Amdahl 
could put out a machine, based on IBM's Principles of 
Operations, that adhered to those specs to such an extent that 
from one release of their hardware to another, Reliability & 
Availability (RA) was improved such that a new hardware release 
had to have the RA of the prior system at the point the new 
system went GA (that is, the RA of the newly shipping system had 
to match the current RA of the prior release at its midlife 
point).

The answer is, REGRESSION TESTING and ARCHITECTURAL VALIDATION 
TESTING. This is a rigorous set of tests written to detect and 
validate fixes for known bugs. If the platform (hardware and or 
software) passes these tests, then one is not promoting known 
bugs into the "next" release. 

This is the type of testing that I put system exits through. 
Test them for functionality and then test them for error 
recovery. Then test them for security violation problems. 
Result: I rarely if ever take down a production environment 
(crash the system).

So why is M/$ not known for serious software that holds its own?
Because they are too interested in getting the jump on their 
competitors in getting to the market. Blow away the users with 
functions and features -- so now Billy Boy is telling his people 
to start paying attention to quality!?!
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-15T19:56:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vh98m849ef0tf6@corp.supernews.com>`
- **In-Reply-To:** `<MPG.197e12dd577b1d75989688@News.CIS.DFN.DE>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE>`

```
Steve Thompson wrote:

> So why is M/$ not known for serious software that holds its own?
> Because they are too interested in getting the jump on their 
> competitors in getting to the market. Blow away the users with 
> functions and features -- so now Billy Boy is telling his people 
> to start paying attention to quality!?!

You've got to admit, though, that writing system software for a 
mainframe significantly narrows the scope of the amount of hardware 
devices you'll need to support.  IBM has their vendors, Unisys has 
theirs, etc. - it's very narrow.

Now, look at what Windows XP is expected to support - anything from an 
original Pentium with beefed-up memory (with lots of ISA cards) to chips 
that haven't even hit the market yet, on motherboards with various 
memory speeds, ISA, AGP, PCI, USB, IEEE 1394, and proprietary integrated 
peripherals.  Then, every Tom, Dick, and Harry can write scripts and 
little programs to run on them...

I'm a big believer in the mainframe for serious business computing.  It 
does what it does very well, quickly, and with stability that makes the 
PC world green with envy.  That being said, though, when I consider all 
that a PC-based operating system has to support, I've been really 
surprised at how stable WinXP Pro is.

I'm not defending Micros~1 - they've gotten in a hurry and made some 
blunders.  All I'm saying is, cut 'em a little slack.  :)
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-16T14:01:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f14b29f_2@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com>`

```
I agree with Daniel.
(Cut 'em a little slack...)

For the first 20 years of mainframes nothing much happened. Random access
got supported with disk drives and hardware improved out of sight, but
processing was still limited to character based business applications. (Even
the Scientific applications were based around this paradigm. I worked for
Control Data Corporation in the early seventies and they were much more
oriented towards scientific applications, but there was no sign of graphics
(apart from on the console of the Cyber 70 which used two round CRTs to keep
the Operator informed about what was going on.))

I remember watching a "revolutionary application" for mainframes in the
early seventies. OCR. It was going to revolutionise industry and put typists
out of work. Only trouble was it took the full resources of what was then
the most powerful computer in the World to read (careful) handprint at
approaching 80% accuracy.

IBM had 7770 Voice Response Units that could talk with a vocabulary of 4096
pre-recorded words. (The Bank of New Zealand was one of the first sites in
the World to implement them and Kiwis could phone their Bank and hear the
voice of Relda Familton (a well known TV presenter) telling them how badly
overdrawn they were...) The point is that these applications were "Science
Fiction". "Everybody knew" that REAL computing was about producing green
lineflo...

By 1983 when the first PCs started to appear, there was nothing different
about the average mainframe than there had been in 1962, when System 360
started to replace the old 1401s. They were just able to do it quicker.

Now compare the PC. 1983 it has a green screen and runs DOS. (Very much like
a mainframe because that was the "received wisdom" as  to what computing was
about.)

Today I am typing this on a pentium 4 Notebook that allows me to watch a
movie, listen to my favourite music, flash photographs instantly around the
world, as well as giving me a development platform that always has instant
response, does all of the above simultaneously, and goes over my shoulder to
travel around the world with me. What's the mainframe doing? Same as it was
in 1962...1982...2002, only quicker... And it can't do ANY of the above!!!
(Don't tell me developers get instant response on mainframes...I've used TSO
<G>.)

OK, so PC Operating Systems haven't been as stable as mainframe ones.

But they are getting MUCH better. XP Pro is superb.

I take Steve's point about reliability on the Networks. But it isn't
non-viable (if it was there would presumably be no Networks...) and, while
inconvenient, we are not prepared to do without it. Again, this can only
improve too.

Steve says the instability is a result of the fierce competition in the
Marketplace. There may be an element of that, but it is that kind of
pressure that fires innovation and expands envelopes. (Look at how
technology skyrockets when there is a war..).

I predict the time will come (and it is not so far away) when the
reliability of Client/Server will be every bit as good as mainframe. The
disk capacity will be equal, the CPU MIPS will be higher. The only reason
you would still support an expensive mainframe in that scenario would be
reliability and security. When those two factors are cancelled (and they
will be...) there is really no point in running a mainframe any more.

Pete.
<snipped Daniel's post which quoted Steve>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-07-16T14:11:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9mahvk8lds6sajkp0t1r1dm27mv0qi1ur@4ax.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>I agree with Daniel.
>(Cut 'em a little slack...)
…[37 more quoted lines elided]…
>in 1962...1982...2002, only quicker... And it can't do ANY of the above!!!

Peter:

I agree with everything you've said, but I suspect the reason that
Mainframes don't play movies, music or have the ability to send photos
around the world isn't because they incapable of being built to
perform these tasks.  I suspect that they don't do these things
because companies who use their mainframes to process massive payroll
systems, massive receivable and payable systems, inventory and sales
systems, etc. don't really want them to perform these tasks.

>(Don't tell me developers get instant response on mainframes...I've used TSO
><G>.)

I concur wholeheartedly on this one, although response always varied
during the day, based upon usage.

>OK, so PC Operating Systems haven't been as stable as mainframe ones.
>
>But they are getting MUCH better. XP Pro is superb.

That they are!  XP is certainly an improvement over all other Windows
versions from the past, but our experience with Linux and PC based
UNIX systems is that they come closer than any other OS which we have
used to mainframe reliability.  We've had a Linux machine running for
4 years and it have never been re-booted nor does it need to be.

>I take Steve's point about reliability on the Networks. But it isn't
>non-viable (if it was there would presumably be no Networks...) and, while
…[17 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-17T20:30:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vhejcv49b9ara6@corp.supernews.com>`
- **In-Reply-To:** `<a9mahvk8lds6sajkp0t1r1dm27mv0qi1ur@4ax.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <a9mahvk8lds6sajkp0t1r1dm27mv0qi1ur@4ax.com>`

```
Bob Wolfe wrote:

> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> 
…[16 more quoted lines elided]…
> systems, etc. don't really want them to perform these tasks.

Heck, my employer doesn't want me to perform these tasks on PCs, 
either...  :)
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** "Don Leahy" <don.leahy@nospamwhatever.leacom.ca>
- **Date:** 2003-07-16T10:51:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yIdRa.1728$r34.10133@news20.bellglobal.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f14b29f_2@news.athenanews.com...
<SNIP>
> (Don't tell me developers get instant response on mainframes...I've used
TSO
> <G>.)
>
Umm...have you used it *lately*?   The shop I am working at (large bank)
consistently delivers subsecond response time to TSO users.

It wasn't always the case of course.  Five years ago I would download
programs to my desktop because I could edit them much faster using SPF/PC.
I am no longer tempted to do that, even though download speeds have also
improved.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** Joseph Katnic <josephk@iinet.net.au>
- **Date:** 2003-07-17T19:47:06+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<170720031947067421%josephk@iinet.net.au>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <yIdRa.1728$r34.10133@news20.bellglobal.com>`

```
In article <yIdRa.1728$r34.10133@news20.bellglobal.com>, Don Leahy
<don.leahy@nospamwhatever.leacom.ca> wrote:

> Umm...have you used it *lately*?   The shop I am working at (large bank)
> consistently delivers subsecond response time to TSO users.
…[4 more quoted lines elided]…
> improved.

Indeed, I use it regularly and get instantaneous response (as far as
I'm concerned you couldn't measure it yourself, but the emulator
reports .1 Sec avg) from half way round the other side of the world.

Mainframe response was Never the Issue. The issue was always, how far
up the pecking order was your dept. in regards to performance. Most
sites gave all the performance to their working systems and what was
left over - if any- was for development.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-17T12:31:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com>`

```

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f14b29f_2@news.athenanews.com...
<<snip>>| |
| Today I am typing this on a pentium 4 Notebook that allows me to watch a
| movie, listen to my favourite music, flash photographs instantly around
the
| world, as well as giving me a development platform that always has instant
| response, does all of the above simultaneously, and goes over my shoulder
to
| travel around the world with me. What's the mainframe doing? Same as it
was
| in 1962...1982...2002, only quicker... And it can't do ANY of the above!!!
| (Don't tell me developers get instant response on mainframes...I've used
TSO
| <G>.)

MINOR POINT:
It isn't TSO that's slow, it's ISPF.
If you run things from the TSO "ready" prompt, response is extremely good.

AND one of the killer applications of the PC, E-mail, is doable from the
mainframe.
At one site, we integrated E-mail from the mainframe into our system for
critical report delivery, and abnormal result reporting.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-17T08:52:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-CF0291.08520917072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net>`

```
In article 
<OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net>,
 "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:

> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3f14b29f_2@news.athenanews.com...
…[21 more quoted lines elided]…
> critical report delivery, and abnormal result reporting.


It is worth mentioning one of my great pet peeves since this thread has 
gone that direction.

Why are we still using a 30 year old interface to the mainframe?  Why in 
the hell can't IBM set one or two programmers at just enhancing TSO and 
ISPF just a bit in ways that really matter?

Off the top of my list:

   Splits are nice, but how about keeping tasks actually running in 
those split screens instead of suspended?  Multi-tasking is supposed to 
be a mainframe plus, why doesn't it do it.  My workstation is better at 
this.

   Any screen size and/or geometry.  Even 80X160 looks toyish on a 21" 
monitor.  And why don't the various ISPF/TSO applications allow dynamic 
swapping (e.g. 133X60 for SDSF; 88x80 for EDIT; etc).  I know it wasn't 
designed with this in mind in 1972 -- why is that still limiting us?

This product, IMNSHO, illustrates the problem with "If we aren't getting 
paid for it, we aren't doing it" mentality that seems to run with the 
"Fortress" approach of only doing just enough to keep things running.

After a while it looks like you are selling shag carpet and bell bottoms 
because you haven't been explicitly paid to keep your product current 
with the times.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** Steve Thompson <steve_nospam_t@ix.netcom.com>
- **Date:** 2003-07-17T09:41:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.198071865fa69ec2989689@News.CIS.DFN.DE>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <joe_zitzelberger-CF0291.08520917072003@corp.supernews.com>`

```
In article <joe_zitzelberger-CF0291.08520917072003
@corp.supernews.com>, joe_zitzelberger@nospam.com says...
<snip>
> Off the top of my list:
> 
…[10 more quoted lines elided]…
> This product, IMNSHO, illustrates the problem with "If we aren't getting
<snip>

ISPF are you listening? ISPF was designed to support 3270. IBM's 
answer to your other points in this area are HTML! Yes, that's 
right, the mainframe DOES HTML and JAVA. Set up thing correctly 
in VTAM and you can drive your applications via a web 
browser/server.

Mainframes can't do movies (AVI, MPG, etc.)? Don't tell the UNIX 
Systems Services people that and in particular, don't tell LINUX 
users that.

ISPF can't do multi-tasking because of an architectural issue. 
Is there a way to overcome this? You betcha, because we did it 
with WYLBUR. WYLBUR was 1 address space that would support as 
many as 300 simultaneous users. When ACS decided to kill the 
department (right out from under me), we were in the process of 
fixing WYLBUR to use the ISPF interface to make WYLBUR universal 
-- who needs TSO (address space per user) when WYLBUR would do 
the same thing with MUCH LESS CPU and C-STORE.... </rant > along 
with fixing the Y2K exposures in WYLBUR.

Back to the architectural issue -- (1) It has to do with APF and 
an authorized task being compromised by a non-authorized task. 
So to avoid this, the non-displayed tasks are suspended. (2) The 
system is interrupt driven. So once you have sent off something 
to be done, until it completes, you can't also tell it to do 
something else until the first command has completed (related to 
how TSO handles I/O interrupt(s/ing)).

Now for those of us who do ALC, we know we can start daughter 
tasks and have them do things while the task talking to ISPF is 
suspended (now we get into the headaches at this point).

So, in order to avoid these problems, the x-Windows systems have 
each running task talking to a sub "panel/window" on the display 
(which means there is a display manager running that relates 
each running subtask to a specific sub"window" ...). This is a 
very different design and not one so easily supported by the 
3270 architecture (as it was originally designed).

This is why the "PC" is a much better display station than 3270, 
and 5250 (as I understand it's design -- which I have not used 
to any degree as I have 3270 where I write, from time to time, 
3270 data streams).

Back to the architectural testing -- IBM and others decided that 
they had to address problems and make their systems better. As a 
result, testing was done to ensure that all functions did as 
they were designed. Then testing was done to validate error 
modes (that error recovery was done correctly). As time went on, 
more and more of these things were done, incorporating the weird 
things that USER DEVELOPERS and ISVs were doing. This is why the 
mainframe is so stable (whether from IBM, UNISYS [Burroughs or 
UNIVAC], Honeywell, TANDEM, and all those others that have 
slowly disappeared).

M/$ apparently NEVER did this type of rigorous testing, which is 
why OS/2 to this day is still a functional O/S. OS/2 was done 
from the viewpoint of the lessons IBM learned from their 
mainframe operating systems (VM, MVS, VSE, etc.). So, there is 
an OS designed for the PC that worked well. Then there was APPLE 
which worked well (still does). Then Linux comes along with what 
appears to be a fairly rigorous testing (considering that it is 
OPEN Source...).

So, you want me to pat M/$ on the back for finally getting it 
right? You must be joking.

BTW - MVS and VM support all kinds of I/O devices. However, the 
specs for channel connection were very specific. So the drivers 
for those items could be installed and tested, knowing that they 
would work from release to release of the O/S where they were 
running.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-18T00:25:43-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-8D9A6E.00254318072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <joe_zitzelberger-CF0291.08520917072003@corp.supernews.com> <MPG.198071865fa69ec2989689@News.CIS.DFN.DE>`

```
In article <MPG.198071865fa69ec2989689@News.CIS.DFN.DE>,
 Steve Thompson <steve_nospam_t@ix.netcom.com> wrote:

> In article <joe_zitzelberger-CF0291.08520917072003
> @corp.supernews.com>, joe_zitzelberger@nospam.com says...
…[20 more quoted lines elided]…
> browser/server.

My applications are the compilers and assemblers that IBM produces.  Are 
you seriously suggesting that I edit source in a web browser?!?

As a development environment, ISPF if very slick is some ways, but 
greatly lacking in others (regex's and cross-line commands come to mind).


> ISPF can't do multi-tasking because of an architectural issue. 
> Is there a way to overcome this? You betcha, because we did it 
…[6 more quoted lines elided]…
> with fixing the Y2K exposures in WYLBUR.

This may be the case.  But you yourself say it can be done otherwise.  
Why are we still stuck with someones really bad design decision from 
1975???  Because it still works maybe?

IBM ought to improve this if nothing else.  Single-tasking is a serious 
hinderance.


> Back to the architectural issue -- (1) It has to do with APF and 
> an authorized task being compromised by a non-authorized task. 
…[8 more quoted lines elided]…
> suspended (now we get into the headaches at this point).

But not with a flick of a PF key.

This is excuse is just more mainframe 
centralized-control-freak-security-nazi mentality blocking a completely 
reasonable programmer request.  Programmers multi-task.  Their terminals 
should as well.


> So, in order to avoid these problems, the x-Windows systems have 
> each running task talking to a sub "panel/window" on the display 
…[8 more quoted lines elided]…
> 3270 data streams).

I would have many of these problems running on my old Apple ][, a 
contemporary of TSO and ISPF.  That does not mean I want to live with 
them today.  These limitations should have been fixed long ago, why is 
IBM so unwilling to step up to the plate?

FTR, the only place I know that you can buy an actual 3270 terminal is 
from a used computer junkyard down under.  That was 5 years ago, things 
may have changed.  IBM may still sell the things (I really don't know) 
but I think the vast, super majority of connections are made via 
emulators.  There is no need for IBM to keep itself chained to the 3270 
except for laziness and lack of vision.

Oh, yea, except 3270's still "work". 

> Back to the architectural testing -- IBM and others decided that 
> they had to address problems and make their systems better. As a 
…[7 more quoted lines elided]…
> slowly disappeared).

In this case, your use of "stable" would equally apply to my old Apple 
][.  ProDOS v2.8 is certainly very stable right now.  The functions are 
well tested and work as designed.

Of course, they have limitations...


> M/$ apparently NEVER did this type of rigorous testing, which is 
> why OS/2 to this day is still a functional O/S. OS/2 was done 
…[5 more quoted lines elided]…
> OPEN Source...).

M$ is always a bad choice for a comperand because their software has 
always sucked so badly.  No other manufacturer in history has produced 
such crap and continued to exist.  I just don't know how they do it.

IBM wins the award for 'No other computer manufacturer in history has 
rested on its proverbial laurels for so long'.  Much of the design of 
TSO, 3270's and ISPF is based on very limited resource situations.  (I 
think my current desktop might crank out more instructions in a day than 
all IBM mainframes in existence in the decade of the 1970s did in the 
entire decade... might be off by a year or two though)  Once those 
resource limitations ceased to exist IBM should have revisited some of 
these things.  Yet a 3278-2 still remains the default interface to 
everything they produce.


> So, you want me to pat M/$ on the back for finally getting it 
> right? You must be joking.

I have never patted M$ on the back.  But I think Apple did a bang up job 
in a few years on OSX.  And Linux looks great without even being in its 
teens.


> BTW - MVS and VM support all kinds of I/O devices. However, the 
> specs for channel connection were very specific. So the drivers 
> for those items could be installed and tested, knowing that they 
> would work from release to release of the O/S where they were 
> running.

So why doesn't IBM start promoting the idea of a more effective 
interface than the 3278-2?  The one time that I know they tried (OS/2 
Warp) they simultaneously released and murdered the creation.  Very odd 
of them.

This is one of those cases where old is just old and IBM has allowed 
some of their most visible products become decrepit and lame.

They may still work.  They may even work great.  But they need to be 
updated to fit the times and the hardware.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** Steve Thompson <steve_nospam_t@ix.netcom.com>
- **Date:** 2003-07-22T00:08:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.198682b65b75187598968b@News.CIS.DFN.DE>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <joe_zitzelberger-CF0291.08520917072003@corp.supernews.com> <MPG.198071865fa69ec2989689@News.CIS.DFN.DE> <joe_zitzelberger-8D9A6E.00254318072003@corp.supernews.com>`

```
In article <joe_zitzelberger-8D9A6E.00254318072003
@corp.supernews.com>, joe_zitzelberger@nospam.com says...
<snip>
> This may be the case.  But you yourself say it can be done otherwise.  
> Why are we still stuck with someones really bad design decision from 
…[3 more quoted lines elided]…
> hinderance.
<snip by software>

You can use a browser. IBM is supporting JAVA in such a way that 
your browser will emulate/simulate 3270 devices!

Single tasking with ISPF is, as I posted earlier, an 
architectural limitation. That you don't like the design (and I 
don't either) they are using doesn't negate the fact that this 
is placed upon them by the architecture they use.

To change ISPF to be multi-tasking oriented, they would need a 
way to have an area on the screen that is able to take a command 
and go do it. Then upon the next solicited interrupt, update 
that area with status. You would still be able to continue to 
edit code, files, etc. This would allow a certain amount of 
multi-tasking by ISPF. However, because of the AUTHORIZED 
functions that are done, how would *you* protect the integrity 
of the system? THAT is, in my opinion, the biggest hurdle they 
have to multi-tasking.

VM/CMS has a few ways around the tasking issues, but then, you 
can only screw up yourself (your CMS guest), you don't have the 
ability to screw up every other user.

Stable O/S: I was not talking about a functionally stabilized 
system. I was talking about how/why an O/S or even micro-code is 
tested so that it would be as stable or more so than the prior 
release. Architectural testing and validation programs (written 
based on the Principles of Operations, or some such) are used to 
verify that the hardware platform is working as designed. Then 
functional testing and validation programs are used to validate 
and verify that the O/S is working per specifications. Then all 
the weird stuff testing is thrown at the system to find those 
incredibly small windows of opportunity -- that are security 
exposures or hard-crash candidates....

Why discuss M/$? Because they have hyped their stuff to 
everyone. They have convinced H&R Block to incorporate M/$ code 
in their tax processing software so that users HAVE to run a 
fairly current copy of IE for the tax software to function! 
(Just one example.) So everyone and everything seems to support 
M/$ APIs and fall over if you attempt to use non-M/$ (hello, 
FTC, can you snatch some more defeat from the jaws of victory?).

If everyone and their St. Bernard weren't stuck on M/$ systems, 
I could ship used systems to various people and they would be 
able to function and get help from w/in their neighborhood. But 
because my system would be Linux based, and everyone in their 
neighborhood is M/$ oriented... And the same holds true for 
Apple...

As for the resting on their laurels: IBM made a commitment to 
its customer base. It learned a lesson in the 50's and early 
60's about the costs of computing. As a result, the S/360 came 
to be. Whatever you wrote for a S/360-30 would work on a S/360-
60 (w/in reason). Same compilers, generating the same executable 
code, allowed IBM to protect the investment of companies in 
their programming. This led to the S/370 and 90% or better of 
the code from the S/360 machines ran w/o even recompiling! Now 
if you were to migrate from an 1130 or 1401 to any other system 
you typically had a major migration... So, setting the standards 
for the 3270 and sticking to them did not harm IBM. But changing 
those standards willy-nilly will cause things that are currently 
working to cease and get unpredictable results.

Look around at those who are solidly on a mainframe. They want 
that box to be boringly stable. They don't want surprises. They 
want a system that will give them the same results from the same 
data with the same program, time after time after time.

Why doesn't IBM promote a better interface than the 3270-2? They 
are, you just aren't listening. JAVA driven from the mainframe 
to your web browser. As long as the platform you are using for 
display supports JAVA, IBM doesn't care what that platform is. 
And they can support anything that the 3270 can handle (such as 
the weird or odd screen sizes that are NOT part of the MOD 
1/2/3/4 or 5). Given a little bit of time, they will support (if 
they aren't already) the page build in CICS such that the whole 
page is view scrollable in your browser (something that 3270 
kinda does). 

BTW - I have at least 2 TSO logons. This is how I multi-task 
with TSO & ISPF. I either do that with a PC running 3270 
emulation or I make sure that the 3174 controller I'm attached 
to supports logical terminal sessions so I can switch between as 
many as 4 simultaneous sessions (and session managers can't take 
the place of this because they are also hampered by the 
interrupt architecture...).
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-24T09:15:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-BDE41A.09154424072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <joe_zitzelberger-CF0291.08520917072003@corp.supernews.com> <MPG.198071865fa69ec2989689@News.CIS.DFN.DE> <joe_zitzelberger-8D9A6E.00254318072003@corp.supernews.com> <MPG.198682b65b75187598968b@News.CIS.DFN.DE>`

```
In article <MPG.198682b65b75187598968b@News.CIS.DFN.DE>,
 Steve Thompson <steve_nospam_t@ix.netcom.com> wrote:

> In article <joe_zitzelberger-8D9A6E.00254318072003
> @corp.supernews.com>, joe_zitzelberger@nospam.com says...
…[10 more quoted lines elided]…
> your browser will emulate/simulate 3270 devices!

This is much of my complaint.  The 3270 was rather a rather smart device 
when originally designed, and this offloaded much CPU to it.  Today, 
compared to the workstations the 3270 emulators run on, it is abysmally 
stupid.  A new protocol that takes the workstation, the increased 
bandwidth, etc into account should be designed.

(BTW, IBM did this with OS/2, which they killed in the only known case 
of corporate postpartum depression in history)

> Single tasking with ISPF is, as I posted earlier, an 
> architectural limitation. That you don't like the design (and I 
…[15 more quoted lines elided]…
> ability to screw up every other user.

ISPF may have a limitation like this, but if falls into the same space 
as the 3270 and TSO -- what was once a great design that maximized 
resources is not cartoonishly out of date in it's approach.  ISPF has 
that limitation because IBM has never revisited many of its design 
decisions over the past 4 decades.  Things change, software should keep 
pace.

The simple approach to that is to allow multiple threads, but block them 
whenever one runs authorized programs.  I'm not sure that is much of a 
concern -- and many/most of a systems users will never need to (though 
some programs, like sort and iebupdte like to be authorized).  Is 
authorized even needed for everyday use?  If the answer is ISPF 
internals need to run authorized that sounds like someting IBM could fix 
easily, just run the entire thing in ordinary user space.


> As for the resting on their laurels: IBM made a commitment to 
> its customer base. It learned a lesson in the 50's and early 
…[10 more quoted lines elided]…
> working to cease and get unpredictable results.

It is/was a nice committment.  But the implementation has been 
problematic.  Consider, for example the 24-bit / 31-bit addressing 
problem.

IBM still fully supports 24-bit code in all things, just like it 
promised its customers several decades ago.  But it did so in a way that 
allowed new development to continue to use 24-bit addressing mode with 
no (I mean no, zero, zilch, none at all) pressure to every take ones 
code into 31-bit land.

So today you can see the unintended consequence of this.  People still 
write 24-bit code.  Lots of it.  We still live with below the like QSAM 
I/O and spend plenty of time juggleing our addressing modes.

Why didn't IBM take the sensible approach to this and say all new 
features are in 31-bit land, 24-bit land still works great, but you need 
to gradually update as you adopt new features.  (Rather like Apples 
slow, gradual, painless 68k->PPC migration).

They didn't though, so now, we also have the bar (though this is not a 
Cobol problem, and may never be) that we must also deal with at the same 
time as the line.

This just one example where age and lack of vision are showing in the 
z/OS world.  And efforts to make the customers life easier actually 
result in increased code complexity.


> Look around at those who are solidly on a mainframe. They want 
> that box to be boringly stable. They don't want surprises. They 
> want a system that will give them the same results from the same 
> data with the same program, time after time after time.

They also want all the latest functions.  The mainframe has lost huge 
chunks of market share in the last decade.  Example -- banks, the 
largest mainframe stronghold, have almost universally adopted PC & Unix 
solutions to their  web-based online banking customer interfaces.


> Why doesn't IBM promote a better interface than the 3270-2? They 
> are, you just aren't listening. JAVA driven from the mainframe 
…[7 more quoted lines elided]…
> kinda does). 

One could certainly write an editor with that, though I wouldn't host it 
in a web browser.  But how exactly does that get you a functional 
development environment to replace ISPF.  It sounds more like a thin 
layer of screen replacement over existing applications.  

Has IBM written editors and file utilities using this?  Or is it more of 
a library for end-user applications?  What exactly are we talking about?  
The VisualAge products?


> BTW - I have at least 2 TSO logons. This is how I multi-task 
> with TSO & ISPF. I either do that with a PC running 3270 
…[4 more quoted lines elided]…
> interrupt architecture...).

Yes, but you need to convince a sysprog not to propagate GRS enqueues to 
allow that to happen -- a widely and frequently used, but "unsupported" 
and "undocumented" hack.

(another place IBM hasn't been keeping up with the times, the officially 
"unofficial" documentation for this was written by (I think) an IBM 
employee.  And I have heard of a few IBM employees using this trick to 
enable multiple signons.  Why isn't this useful and otherwise harmless 
feature rolled into the OS?)
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-17T22:40:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34cb4$6e31fd60$ae91f243@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net>`

```
Let see I compiled a 30,000 line COBOL program today and it took .01 second
of cpu time. How slow can you go?

Harley <dennis.harleyNoSpam@worldnet.att.net> wrote in article
<OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net>...
> 
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
> news:3f14b29f_2@news.athenanews.com...
> <<snip>>| |
> | Today I am typing this on a pentium 4 Notebook that allows me to watch
a
> | movie, listen to my favourite music, flash photographs instantly around
> the
> | world, as well as giving me a development platform that always has
instant
> | response, does all of the above simultaneously, and goes over my
shoulder
> to
> | travel around the world with me. What's the mainframe doing? Same as it
> was
> | in 1962...1982...2002, only quicker... And it can't do ANY of the
above!!!
> | (Don't tell me developers get instant response on mainframes...I've
used
> TSO
> | <G>.)
…[3 more quoted lines elided]…
> If you run things from the TSO "ready" prompt, response is extremely
good.
> 
> AND one of the killer applications of the PC, E-mail, is doable from the
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-17T23:52:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel>`

```

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c34cb4$6e31fd60$ae91f243@chottel...
| Let see I compiled a 30,000 line COBOL program today and it took .01
second
| of cpu time. How slow can you go?

What was the Wall Time?

|
| Harley <dennis.harleyNoSpam@worldnet.att.net> wrote in article
…[7 more quoted lines elided]…
| > | movie, listen to my favourite music, flash photographs instantly
around
| > the
| > | world, as well as giving me a development platform that always has
…[4 more quoted lines elided]…
| > | travel around the world with me. What's the mainframe doing? Same as
it
| > was
| > | in 1962...1982...2002, only quicker... And it can't do ANY of the
…[17 more quoted lines elided]…
| >
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-18T03:22:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34cdb$d9f58180$3ec2f943@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel> <hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net>`

```
Well I use ROSCOE so after I SUBMIT the compile job I usually wait a few
seconds before I press SHIFT+PF1 to DISPLAY the job status. If there is a
serious enough compile error the compiler does not generate the object code
so it will finish quicker. The job is usually done by the time that I check
for it. It is fast enough that I never bother to check the wall time and it
 just happened that the cpu time was displayed in  when I checked  for the
return codes from the steps.

Harley <dennis.harleyNoSpam@worldnet.att.net> wrote in article
<hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net>...
> 
> "Charles Hottel" <chottel@cpcug.org> wrote in message
…[14 more quoted lines elided]…
> | > | Today I am typing this on a pentium 4 Notebook that allows me to
watch
> | a
> | > | movie, listen to my favourite music, flash photographs instantly
…[7 more quoted lines elided]…
> | > | travel around the world with me. What's the mainframe doing? Same
as
> it
> | > was
…[12 more quoted lines elided]…
> | > AND one of the killer applications of the PC, E-mail, is doable from
the
> | > mainframe.
> | > At one site, we integrated E-mail from the mainframe into our system
for
> | > critical report delivery, and abnormal result reporting.
> | >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-18T12:23:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GERRa.60846$0v4.4078917@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel> <hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net> <01c34cdb$d9f58180$3ec2f943@chottel>`

```

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c34cdb$d9f58180$3ec2f943@chottel...
| Well I use ROSCOE so after I SUBMIT the compile job I usually wait a few
| seconds before I press SHIFT+PF1 to DISPLAY the job status. If there is a
| serious enough compile error the compiler does not generate the object
code
| so it will finish quicker. The job is usually done by the time that I
check
| for it. It is fast enough that I never bother to check the wall time and
it
|  just happened that the cpu time was displayed in  when I checked  for the
| return codes from the steps.

It would have been more appropriate to run a compile under ISPF (on-line
compile).

I don't think anyone questions the turnaround time for a batch compile.

|
| Harley <dennis.harleyNoSpam@worldnet.att.net> wrote in article
…[34 more quoted lines elided]…
| > | > | (Don't tell me developers get instant response on
mainframes...I've
| > | used
| > | > TSO
…[18 more quoted lines elided]…
| >
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-18T19:29:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34d62$f4f5f780$8c93f243@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel> <hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net> <01c34cdb$d9f58180$3ec2f943@chottel> <GERRa.60846$0v4.4078917@bgtnsc04-news.ops.worldnet.att.net>`

```
Several years ago i worked in a group that used Endeavor and I had t use
TSO/ISPF. Those compile dis take much longer, often 30 minutes or more by
the wall clock. I could not believe is was so much slower than submitting a
compile from Roscoe.

Harley <dennis.harleyNoSpam@worldnet.att.net> wrote in article
<GERRa.60846$0v4.4078917@bgtnsc04-news.ops.worldnet.att.net>...
> 
> "Charles Hottel" <chottel@cpcug.org> wrote in message
> news:01c34cdb$d9f58180$3ec2f943@chottel...
> | Well I use ROSCOE so after I SUBMIT the compile job I usually wait a
few
> | seconds before I press SHIFT+PF1 to DISPLAY the job status. If there is
a
> | serious enough compile error the compiler does not generate the object
> code
> | so it will finish quicker. The job is usually done by the time that I
> check
> | for it. It is fast enough that I never bother to check the wall time
and
> it
> |  just happened that the cpu time was displayed in  when I checked  for
the
> | return codes from the steps.
> 
…[11 more quoted lines elided]…
> | > | Let see I compiled a 30,000 line COBOL program today and it took
01
> | > second
> | > | of cpu time. How slow can you go?
…[10 more quoted lines elided]…
> | > | > | Today I am typing this on a pentium 4 Notebook that allows me
to
> | watch
> | > | a
> | > | > | movie, listen to my favourite music, flash photographs
instantly
> | > around
> | > | > the
> | > | > | world, as well as giving me a development platform that always
has
> | > | instant
> | > | > | response, does all of the above simultaneously, and goes over
my
> | > | shoulder
> | > | > to
> | > | > | travel around the world with me. What's the mainframe doing?
Same
> | as
> | > it
> | > | > was
> | > | > | in 1962...1982...2002, only quicker... And it can't do ANY of
the
> | > | above!!!
> | > | > | (Don't tell me developers get instant response on
…[7 more quoted lines elided]…
> | > | > If you run things from the TSO "ready" prompt, response is
extremely
> | > | good.
> | > | >
> | > | > AND one of the killer applications of the PC, E-mail, is doable
from
> | the
> | > | > mainframe.
> | > | > At one site, we integrated E-mail from the mainframe into our
system
> | for
> | > | > critical report delivery, and abnormal result reporting.
…[8 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 14)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-18T20:06:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lrYRa.61488$0v4.4106795@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel> <hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net> <01c34cdb$d9f58180$3ec2f943@chottel> <GERRa.60846$0v4.4078917@bgtnsc04-news.ops.worldnet.att.net> <01c34d62$f4f5f780$8c93f243@chottel>`

```

"Charles Hottel" <chottel@cpcug.org> wrote in message
news:01c34d62$f4f5f780$8c93f243@chottel...
| Several years ago i worked in a group that used Endeavor and I had t use
| TSO/ISPF. Those compile dis take much longer, often 30 minutes or more by
| the wall clock. I could not believe is was so much slower than submitting
a
| compile from Roscoe.

I've used Changeman, and it submitted batch compiles.
I also submit my own batch compiles.
Compile times are generally good, but are sometimes affected by the day of
the month, or time of day.
It doesn't matter much though, I still have to check my e-mail and reply, as
well as take care of other duties. I have to multi-task whether I get
instantaneous results or have to wait.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 15)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-19T03:04:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34da2$7e38d3c0$5093f243@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel> <hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net> <01c34cdb$d9f58180$3ec2f943@chottel> <GERRa.60846$0v4.4078917@bgtnsc04-news.ops.worldnet.att.net> <01c34d62$f4f5f780$8c93f243@chottel> <lrYRa.61488$0v4.4106795@bgtnsc04-news.ops.worldnet.att.net>`

```
I looked at the JCL that Endeavor submitted and it contained one extra step
but I never did figure out why it took so much longer. I only had brief on
the job training on Endeavor and what manuals I found did not help as our
installation had made many customized modifications.

Harley <dennis.harleyNoSpam@worldnet.att.net> wrote in article
<lrYRa.61488$0v4.4106795@bgtnsc04-news.ops.worldnet.att.net>...
> 
> "Charles Hottel" <chottel@cpcug.org> wrote in message
> news:01c34d62$f4f5f780$8c93f243@chottel...
> | Several years ago i worked in a group that used Endeavor and I had t
use
> | TSO/ISPF. Those compile dis take much longer, often 30 minutes or more
by
> | the wall clock. I could not believe is was so much slower than
submitting
> a
> | compile from Roscoe.
…[3 more quoted lines elided]…
> Compile times are generally good, but are sometimes affected by the day
of
> the month, or time of day.
> It doesn't matter much though, I still have to check my e-mail and reply,
as
> well as take care of other duties. I have to multi-task whether I get
> instantaneous results or have to wait.
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 14)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-07-19T05:04:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F18D1A5.9C19EE13@worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel> <hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net> <01c34cdb$d9f58180$3ec2f943@chottel> <GERRa.60846$0v4.4078917@bgtnsc04-news.ops.worldnet.att.net> <01c34d62$f4f5f780$8c93f243@chottel>`

```
Charles Hottel wrote:
> 
> Several years ago i worked in a group that used Endeavor and I had t use
> TSO/ISPF. Those compile dis take much longer, often 30 minutes or more by
> the wall clock. I could not believe is was so much slower than submitting a
> compile from Roscoe.

I work in a shop with Endevor (that's how they misspell their product
name).  I submit Endevor compiles as batch jobs, but they aren't
really JCL, they're Endevor SCL (Software Control Language?).  I find
that a batch COBOL compile outside of Endevor takes about 10-15
seconds (unless the system is busy), and the Endevor compile takes
30-45 seconds.  Our Endevor is configured to control and install load
modules as well as source modules.  The machine is a z900 model
2064-2C4.

We used to submit our batch jobs from SYSD, which is a CICS-hosted
ISPF lookalike.  Several years ago they dumped SYSD and made the
applications programmers use TSO/ISPF/SDSF instead.  But the sysprogs
here have never set up online COBOL compiles unders ISPF.

How hard is it to set up COBOL compile under ISPF?  Would I want to do
that instead of submitting a batch job to compile?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-19T09:51:46-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfbidi$1r0$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34cdb$d9f58180$3ec2f943@chottel> <3F18D1A5.9C19EE13@worldnet.att.net>`

```
In article <3F18D1A5.9C19EE13@worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>How hard is it to set up COBOL compile under ISPF?

The 'Online Compile' option from the ISPF Main Menu?  I don't think I have 
ever worked in a shop where this was configured properly.

>Would I want to do
>that instead of submitting a batch job to compile?

Hmmmmm... most systems I've worked on give priority of resource-allocation 
to foreground tasks over background; it stands to reason that using the 
foreground compile options might move things along a bit more speedily 
than trying to find an answer to the Mainframe Zen question of 'How long 
does it take to get a Class (x) initiator?'

(One of the other Mainframe Zen questions is 'How large is an output 
dataset?')

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 16)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-07-19T11:09:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0307191009.e191353@posting.google.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34cdb$d9f58180$3ec2f943@chottel> <3F18D1A5.9C19EE13@worldnet.att.net> <bfbidi$1r0$1@panix1.panix.com>`

```
docdwarf@panix.com wrote in message news:<bfbidi$1r0$1@panix1.panix.com>...
> In article <3F18D1A5.9C19EE13@worldnet.att.net>,
> Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
…[4 more quoted lines elided]…
> 

> Hmmmmm... most systems I've worked on give priority of resource-allocation 
> to foreground tasks over background; it stands to reason that using the 
…[7 more quoted lines elided]…
> DD

One reason I can imagine why systems programmers would wish to
discourage people from doing online compiles, is that they are
relatively resource hungry and would tend to reduce overall response
times, especially if done by a lot of people at once.  Although batch
compiles would probably use similar resources, they would usually be
given a lower dispatching priority and not interfere so much with
relatively simple tasks such as editing source code, reviewing screen
and file contents, etc.

Robert
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 17)_

- **From:** Joseph Katnic <no@spam.mail>
- **Date:** 2003-07-20T21:50:12+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<200720032150124521%no@spam.mail>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34cdb$d9f58180$3ec2f943@chottel> <3F18D1A5.9C19EE13@worldnet.att.net> <bfbidi$1r0$1@panix1.panix.com> <fcd09c56.0307191009.e191353@posting.google.com>`

```
And in a properly setup MVS, even without WLM, this would present no
problem whatsoever. As the forground user consumed more resources, so
the priority of the user would be lowered until it no longer impacted
anyone but the user concerned.

This was the first thing you learned as a sysprog involved in tuning a
mainframe.

In article <fcd09c56.0307191009.e191353@posting.google.com>, Robert
Jones <robert@jones0086.freeserve.co.uk> wrote:

> docdwarf@panix.com wrote in message news:<bfbidi$1r0$1@panix1.panix.com>...
> 
…[9 more quoted lines elided]…
> Robert
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 18)_

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-07-20T13:14:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0307201214.cd897c2@posting.google.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34cdb$d9f58180$3ec2f943@chottel> <3F18D1A5.9C19EE13@worldnet.att.net> <bfbidi$1r0$1@panix1.panix.com> <fcd09c56.0307191009.e191353@posting.google.com> <200720032150124521%no@spam.mail>`

```
Thanks for the information.  However, a better reason for using a
batch compile is that one can use an installation supplied procedure
with standard compiler settings, which can of course be overridden for
test options, etc, but nevertheless apply general consistency in such
items as whether quotes or apostrophes are used to delimit literals,
etc.  Admittedly, it is probable that the online compile facility
could be set up similarly.  Another reason, is that if the compile
will take more than a few seconds, or perhaps a minute or two, the
programmer might be better occupied doing something else while
waiting.

Robert

Joseph Katnic <no@spam.mail> wrote in message news:<200720032150124521%no@spam.mail>...
> And in a properly setup MVS, even without WLM, this would present no
> problem whatsoever. As the forground user consumed more resources, so
…[20 more quoted lines elided]…
> > Robert
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 16)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-07-20T06:17:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F1A343D.AC01C6B4@worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <01c34cdb$d9f58180$3ec2f943@chottel> <3F18D1A5.9C19EE13@worldnet.att.net> <bfbidi$1r0$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> 
> In article <3F18D1A5.9C19EE13@worldnet.att.net>,
…[7 more quoted lines elided]…
> ever worked in a shop where this was configured properly.

Thanks, Doc.  I don't feel so bad now.  Although I have run into
contract programmers who only know ISPF menus, and can't run batch
jobs to copy members between PDS's.  Some of them seem to believe that
File-Aid is bundled with MVS/OS390/zOS, which forced us to actually
buy it.

> 
> >Would I want to do
…[6 more quoted lines elided]…
> does it take to get a Class (x) initiator?'

My shop must be well-managed.  I hardly ever wait for an initiator.


> 
> (One of the other Mainframe Zen questions is 'How large is an output
> dataset?')
> 
> DD

I just run an IDCAMS print.  If OPS calls and tells me I've filled up
JES Spool, then it's too large! 
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-20T09:39:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfe61p$nup$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F18D1A5.9C19EE13@worldnet.att.net> <bfbidi$1r0$1@panix1.panix.com> <3F1A343D.AC01C6B4@worldnet.att.net>`

```
In article <3F1A343D.AC01C6B4@worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>docdwarf@panix.com wrote:
>> 
…[14 more quoted lines elided]…
>buy it.

My experience differs; I am accustomed to a shop's personnel saying 
'(tool-name)?  No, we don't use that here because (some hackneyed reason 
skewed to imply superiority)' and then resisting the purchase/installation 
of same even more mightily.

>
>> 
…[9 more quoted lines elided]…
>My shop must be well-managed.  I hardly ever wait for an initiator.

This is not the case in all places... again, in my experience.

>
>
…[6 more quoted lines elided]…
>JES Spool, then it's too large! 

Hmmmmm... you might want to consider setting your SYSPRINT to DD  DUMMY or 
doing a REPRO to DUMMY; then there'd be no need to have OPS come back 
inside from smoking hashish... but your solution does not allow for one to 
code the SPACE parms during initial testing in order to avoid any one of 
the -37 ABENDs.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 15)_

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-19T15:02:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c34e06$cba27da0$3a91f243@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com> <MPG.197e12dd577b1d75989688@News.CIS.DFN.DE> <vh98m849ef0tf6@corp.supernews.com> <3f14b29f_2@news.athenanews.com> <OGwRa.59186$3o3.3938292@bgtnsc05-news.ops.worldnet.att.net> <01c34cb4$6e31fd60$ae91f243@chottel> <hFGRa.60046$3o3.3982510@bgtnsc05-news.ops.worldnet.att.net> <01c34cdb$d9f58180$3ec2f943@chottel> <GERRa.60846$0v4.4078917@bgtnsc04-news.ops.worldnet.att.net> <01c34d62$f4f5f780$8c93f243@chottel> <3F18D1A5.9C19EE13@worldnet.att.net>`

```
I have always used ROSCOE so I am not an expert at forground compile from
ISPF. I think you just use the ALLOC command for the datasets you use and
EXEC the compiler. Doing this manually would be a pain. In the past I
believe they did this by writing a CLIST and now days they probably use
REXX. Conceptually it is the same as what I do in ROSCOE, which is run an
RPF with the program name as a parameter.

Arnold Trembley <arnold.trembley@worldnet.att.net> wrote in article
<3F18D1A5.9C19EE13@worldnet.att.net>...
> How hard is it to set up COBOL compile under ISPF?  Would I want to do
> that instead of submitting a batch job to compile?
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-15T19:40:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vh97o4avoicj39@corp.supernews.com>`
- **In-Reply-To:** `<pMycnSAuHOq7mImiU-KYuQ@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <I9acnQ7SiNf40JCiXTWJkA@giganews.com> <MPG.197d4aa79853089a989686@News.CIS.DFN.DE> <pMycnSAuHOq7mImiU-KYuQ@giganews.com>`

```
JerryMouse wrote:
> People bitch like sex-crazed monkeys over software bugs - but the authors of
> the software cannot realistically be blamed. If, for example, Micros~1 alpha
…[10 more quoted lines elided]…
> them.

You know, I don't know if you were being serious or kidding, but this 
has a great deal of common sense.  First we have technically accurate 
posts, now common sense - holy cow!

> Or find another line of work - like government service.

Heh - we prefer to call it "civil" service...  We serve the civilian 
population, not the government itself.  :)
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T00:21:41+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d5ae6_7@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE>`

```

"Steve Thompson" <steve_nospam_t@ix.netcom.com> wrote in message
news:MPG.19768963bd8f4626989684@News.CIS.DFN.DE...
> In article <3f0cb232_6@news.athenanews.com>,
> dashwood@enternet.co.nz says...
> > I'm starting this thread because of a post from Joe Zitzelberger which
said
> > the following:
> >
…[11 more quoted lines elided]…
>
I'm not sure that is fair, Steve. I have to admit that since last Xmas when
I moved to XP I have NOT had a system crash or hang, or had to reboot.  This
is the first time since 1983 that I have felt satisfied with MicroSoft
software...

> On the systems that I work with, yes, we take some time to get
> things written and delivered to the customers, but let's stop
…[11 more quoted lines elided]…
> Now, is this the waterfall method?

No. This is a very sensible iterative, evolutionary, method of development.
I wish more shops whould go along this approach.


> I do development in COBOL,
> REXX, RPG, ALC, FORTRAN, OO-COBOL, and CLIST. I try to write as
…[20 more quoted lines elided]…
>

No, but you might with several hundred...

> As soon as corporations wake up to systems needing to be a mix
> of tools... Screwdrivers just don't scale well into a large pry-
> bar.

I understand what you're saying. But if you break it down into constituents
(decompose), even your most complex and huge system is comprised of smaller,
simpler functions. The secret is in how you assemble them, and that is
predicated on good design. (which may well include iteration and
interaction.) Hence, I am concerned with better, cost effective
methodologies for designing and developing systems.

The problem with the Waterfall approach is that it admits no other approach.
The Fortress mentality likes it for this reason. To depart from it would be
to admit that things could've been done better for the last several
decades...<G>

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T08:42:25-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejmvh$5do$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com>`

```
In article <3f0d5ae6_7@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
>"Steve Thompson" <steve_nospam_t@ix.netcom.com> wrote in message
>news:MPG.19768963bd8f4626989684@News.CIS.DFN.DE...

[snip]

>> My biggest complaint about the "open systems" is that they
>> haven't matured. They are treated like tinker toys by their
…[7 more quoted lines elided]…
>software...

With all due respect, Mr Dashwood, a calendar nearby shows me that the 
year is 2003.  What would it be like to have been a developer of a 
business-critical system who did not have a stable operating system for 
two decades?  What business would have tolerated a programmer who, when 
told 'Your application crashes unpredictably' responded 'Don't worry... in 
twenty years it will be stable and you'll forgive me for everything!'?

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T01:33:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d6bab_9@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <bejmvh$5do$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bejmvh$5do$1@panix1.panix.com...
> In article <3f0d5ae6_7@news.athenanews.com>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
…[12 more quoted lines elided]…
> >I'm not sure that is fair, Steve. I have to admit that since last Xmas
when
> >I moved to XP I have NOT had a system crash or hang, or had to reboot.
This
> >is the first time since 1983 that I have felt satisfied with MicroSoft
> >software...
…[4 more quoted lines elided]…
> two decades?

I've no idea, Doc. I wasn't stupid enough to try and develop serious
Business systems with it at that time. (I remember writing a graphics
program to help my girlfriend plan her new house, and a blackjack program
that implemented casino rules. All of this was in BASIC.)

The first business systems I wrote (in COBOL) for a PC, were Much Later (in
the 90s) and they were for a very narrow niche with a very small business.
The platform was unstable (Win 3.1) but the customer knew that and expected
it. It got re-booted about every 3rd day due to system crash. It still
managed a customer file with 30,000 people on it and scheduled them for
treatments at a very busy London clinic. It NEVER produced green
lineflo....<g> (A4 from day 1 with  many online displays in Windows). Since
then, MS have consistenlty improved their product. Today it is good. I'm
currently finishing  a Web Portal that will collect information from
anywhere on Earth 24/7 and route it to the right directory on the right
server (any one of potentially several hundred) for immediate processing,
interaction, and response to the user (eventually in his own language). It
uses OO COBOL and Components on a Web Server and needs a stable platform. We
are confident enough to go ahead with it.

>What business would have tolerated a programmer who, when
> told 'Your application crashes unpredictably' responded 'Don't worry... in
> twenty years it will be stable and you'll forgive me for everything!'?
>
You need to get out more, Doc. There are applications all over the World
that crash unpredictably, and are tolerated by the Business. Some of them
are NOT on MS platforms (Shock! Horror! No!).

We just had the whole EFTPOS (Electronic Funds Transfer at Point Of Sale -
they grab the cash from your bank account immediately when you say "I'll
take it!") system here go out for a couple of hours a few days ago.
Nationwide. Retailers  the length of the country wailing and gnashing of
teeth. I am informed it is mainframe based...

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T10:05:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejrqr$aps$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5ae6_7@news.athenanews.com> <bejmvh$5do$1@panix1.panix.com> <3f0d6bab_9@news.athenanews.com>`

```
In article <3f0d6bab_9@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:bejmvh$5do$1@panix1.panix.com...
…[25 more quoted lines elided]…
>Business systems with it at that time.

So, then... were you being appropriately cautious or living in a Fortress?

[snip]

>>What business would have tolerated a programmer who, when
>> told 'Your application crashes unpredictably' responded 'Don't worry... in
…[10 more quoted lines elided]…
>teeth. I am informed it is mainframe based...

It was never said, Mr Dashwood, that all applications are or must be
bulletproof;  what was stated - and has been readily acknowledged - is
that it took two decades for a major vendor to produce an OS that can be
more-or-less trusted not to crash.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T14:58:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejutt$cgm$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5ae6_7@news.athenanews.com> <bejmvh$5do$1@panix1.panix.com> <3f0d6bab_9@news.athenanews.com> <bejrqr$aps$1@panix1.panix.com>`

```

On 10-Jul-2003, docdwarf@panix.com wrote:

> It was never said, Mr Dashwood, that all applications are or must be
> bulletproof;  what was stated - and has been readily acknowledged - is
> that it took two decades for a major vendor to produce an OS that can be
> more-or-less trusted not to crash.

All OS's crash.   Our trust needs vary.   People's confidence in XP not crashing
is much higher than of previous versions of Windows, but significantly behind
their confidence of MacOs.   (I had a hard crash in an XP machine this morning).
   But more importantly, all business systems have bugs and failures.   The big
thing is to have designs where these failures do the least amount of damage.

This is especially obvious in integrated systems with multiply used objects.  
We can't make them bug proof, so we must design them so the bugs don't hurt too
much.    But it is true with fortress COBOL mainframe environments as well.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-15T22:41:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-E56B52.22411215072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5ae6_7@news.athenanews.com> <bejmvh$5do$1@panix1.panix.com> <3f0d6bab_9@news.athenanews.com> <bejrqr$aps$1@panix1.panix.com>`

```
In article <bejrqr$aps$1@panix1.panix.com>, docdwarf@panix.com wrote:
> 
> It was never said, Mr Dashwood, that all applications are or must be
…[4 more quoted lines elided]…
> DD

Only one major vendor.  Micro$oft.  And they make such great funds 
selling support and upgrades.

Apple just released a new OS that went from slightly shaky on the first 
release to rock solid on the next .1 release six months later.  I've not 
had a crash since 10.0.

OS/2 was very solid with only a few years.

Linux was born barely a decade ago and has been more reliable than 
anything that M$ has ever put out for most of that decade.

It doesn't take 20 years unless a vendor wants it to take 20 years.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-15T22:51:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf2ek3$og1$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d6bab_9@news.athenanews.com> <bejrqr$aps$1@panix1.panix.com> <joe_zitzelberger-E56B52.22411215072003@corp.supernews.com>`

```
In article <joe_zitzelberger-E56B52.22411215072003@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <bejrqr$aps$1@panix1.panix.com>, docdwarf@panix.com wrote:
>> 
…[6 more quoted lines elided]…
>Only one major vendor.

Last time I looked, Mr Zitzelberger, 'a' was a singular indefinite 
article.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** Patrick Herring <ph@anweald.co.uk>
- **Date:** 2003-07-10T14:48:04+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0D6E94.4AFFC42A@anweald.co.uk>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com>`

```
"Peter E.C. Dashwood" wrote:
...
> I'm not sure that is fair, Steve. I have to admit that since last Xmas
> when I moved to XP I have NOT had a system crash or hang, or had to
> reboot.  This is the first time since 1983 that I have felt satisfied
> with MicroSoft software...

My wife's WinXP/sp2 [1] hangs at least once an evening, with no
discernable common cause. My Win98se is much more stable unless my kids
run games.

[1] no, not /that/ sp2.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-07-14T13:33:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk>`

```
Patrick Herring <ph@anweald.co.uk> wrote:

>"Peter E.C. Dashwood" wrote:
>...
…[9 more quoted lines elided]…
>[1] no, not /that/ sp2.

Patrick is speaking of "WinXP/sp2" a.k.a. "WinXP/service pack 2"

;-)

When WinNT 4.0 service pack 2 was released years ago, one of my
customers contacted us in a panic because he read an article about
some serious problems with "sp2"  I explained that the article was
referring to "service pack 2" which greatly relieved the customer.




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** Patrick Herring <ph@anweald.co.uk>
- **Date:** 2003-07-15T12:37:43+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F13E787.7E137B5C@anweald.co.uk>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com>`

```
Bob Wolfe wrote:
> 
> Patrick Herring <ph@anweald.co.uk> wrote:
…[14 more quoted lines elided]…
> Patrick is speaking of "WinXP/sp2" a.k.a. "WinXP/service pack 2"

I now have more data: it was sp1, apparently, sp2 for XP doesn't exist
yet. And the hangs have been identified as an IRQ conflict caused by an
Nvidia video card that won't share IRQs properly, but changing things
would require a reinstall of everything, so the hangs are preferable for
the time being. 

I still don't call that stable - shouldn't the OS take charge of
everything?

I'm switching to linux as soon as I find out how to do a dual boot in
case I have some Win apps that can't run under Wine etc.

> When WinNT 4.0 service pack 2 was released years ago, one of my
> customers contacted us in a panic because he read an article about
> some serious problems with "sp2"  I explained that the article was
> referring to "service pack 2" which greatly relieved the customer.

<g>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-07-15T08:51:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IdOdna84U_6WmomiU-KYgw@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk>`

```
Patrick Herring wrote:
>
> I now have more data: it was sp1, apparently, sp2 for XP doesn't exist
…[6 more quoted lines elided]…
> everything?

Of course not. When a 3rd party vendor (Nvidia) flagrantly violates
connectivity, timing, and memory access specifications, what can the OS do?
XP warned you that the card was incompatible; XP can't physically REMOVE the
offending hardware - that's your responsibility. Better yet, get the proper
drivers from Nvidia. If they don't have workable drivers for XP, get your
money back from Nvidia.

Nvidia incompatibility is a problem of long duration and widely known.

>
> I'm switching to linux as soon as I find out how to do a dual boot in
> case I have some Win apps that can't run under Wine etc.
>

Go for it. Linux supports far fewer devices than XP. But you're fighting the
wrong problem. The problem is the crappy video card, not the operating
system.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-15T19:43:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vh97tink1cjp8f@corp.supernews.com>`
- **In-Reply-To:** `<IdOdna84U_6WmomiU-KYgw@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk> <IdOdna84U_6WmomiU-KYgw@giganews.com>`

```
JerryMouse wrote:

> Nvidia incompatibility is a problem of long duration and widely known.

That's really interesting to hear.  To this day, the only problem I ever 
have with my Windows XP laptop is when I start a DivX movie and switch 
Windows Media Player from skin mode to full mode.  Almost every time, my 
screen goes nutzo.  I know the keystrokes to shut the machine down, so 
I'll do it, and when I restart, inevitably it's the NVidia display driver.

Since it's a laptop, I can't really do much about it - but I can make 
sure that my next one has a better brand.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-07-15T14:06:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at18hv4pbidblfs9ggv7k6a2783gvi02i5@4ax.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk>`

```
Patrick Herring <ph@anweald.co.uk> wrote:

>Bob Wolfe wrote:
>> 
…[27 more quoted lines elided]…
>case I have some Win apps that can't run under Wine etc.

Patrick:

Although I haven't done it on my own XP box, my son and several other
acquaintences have told me that it is quite easy to set up WinXP for a
dual boot.

Here's what I gleaned from M$ help on XP....of course, they don't
mention Linux as a dual boot option......and I chuckled when I read
that they do not recommend it as a long term solution:

How to create a multiple-boot system with Windows NT 4.0 and Windows
XP

Using a multiple-boot system with both Windows NT 4.0 and Windows XP
is not recommended as a long-term solution. The NTFS update in Service
Pack 4 for Windows NT 4.0 is provided only to help you evaluate and
upgrade to Windows XP. 

After ensuring that your hard drive is formatted with the correct file
system, install Windows NT 4.0, and then install Windows XP.

Important

Before creating a multiple-boot configuration with Windows XP and
another operating system, such as MS-DOS, Windows 95, or Windows 98,
review the following precautions:

Each operating system must be installed on a separate volume.
Microsoft does not support installing multiple operating systems on
the same volume. 

If you have only one volume on your computer, you must reformat and
repartition your hard drive to contain multiple volumes before you
begin creating a multiple-boot configuration, unless you are simply
installing another copy of Windows XP. 

If you intend to install more than one operating system consisting of
some combination of Windows NT 4.0 with either Windows 2000 or Windows
XP as the only installed operating systems, you must ensure that you
have installed Service Pack 4 for Windows NT 4.0. Windows XP will
automatically upgrade any NTFS partitions it finds on your system to
the version of NTFS used in Windows 2000 and Windows XP. However,
Windows NT 4.0 requires Service Pack 4 to be able to read and write
files on a volume formatted with the version of NTFS used in Windows
2000 and Windows XP. 

Do not install Windows XP on a compressed drive that was not
compressed using the NTFS compression utility. 

You must use a different computer name for each operating system if
the computer is on a Windows 2000 or Windows XP secure domain. 


>
>> When WinNT 4.0 service pack 2 was released years ago, one of my
…[4 more quoted lines elided]…
><g>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-15T14:47:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf145v$ph8$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk> <at18hv4pbidblfs9ggv7k6a2783gvi02i5@4ax.com>`

```

On 15-Jul-2003, Bob Wolfe <rtwolfe@flexus.com> wrote:

> Although I haven't done it on my own XP box, my son and several other
> acquaintences have told me that it is quite easy to set up WinXP for a
> dual boot.

It's real easy.   But some software vendors won't support you if you admit to
using dual boot.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-07-16T10:19:02+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf1uth$kln$1@aklobs.kc.net.nz>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk>`

```
Patrick Herring wrote:

> I'm switching to linux as soon as I find out how to do a dual boot in
> case I have some Win apps that can't run under Wine etc.

There are several ways of running Windows apps.  Win4Lin runs an actual 
copy of Windows98 in a Windows on the Linux desktop and its file system is 
in a sub directory of the users home directory. It can also share the 
network card of the host machine for networking.

Because it is a real Windows it runs most stuff, and does so without having 
to reboot.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-15T20:00:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vh98svg4lfi54f@corp.supernews.com>`
- **In-Reply-To:** `<bf1uth$kln$1@aklobs.kc.net.nz>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk> <bf1uth$kln$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote:

> There are several ways of running Windows apps.  Win4Lin runs an actual 
> copy of Windows98 in a Windows on the Linux desktop and its file system is 
…[4 more quoted lines elided]…
> to reboot.

Is this open-source?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-07-16T13:39:40+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf2alo$phh$1@aklobs.kc.net.nz>`
- **References:** `<3f0cb232_6@news.athenanews.com> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk> <bf1uth$kln$1@aklobs.kc.net.nz> <vh98svg4lfi54f@corp.supernews.com>`

```
LX-i wrote:

>> There are several ways of running Windows apps.  Win4Lin runs an actual
>> copy of Windows98 

> Is this open-source?

No, it is commercial, but not expensive.  It originated in the SCO Merge 
product which ran MS-DOS and Windows 3.x in the Unixware CDE desktop.

See: http://www.netraverse.com or use Google to find reviews.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-16T14:14:23+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f14b59e_3@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com> <3F0D6E94.4AFFC42A@anweald.co.uk> <s0c5hvo24nokhglo8f2n3rdgds6mge10r1@4ax.com> <3F13E787.7E137B5C@anweald.co.uk>`

```

"Patrick Herring" <ph@anweald.co.uk> wrote in message
news:3F13E787.7E137B5C@anweald.co.uk...
> Bob Wolfe wrote:
> >
…[4 more quoted lines elided]…
> > >> I'm not sure that is fair, Steve. I have to admit that since last
Xmas
> > >> when I moved to XP I have NOT had a system crash or hang, or had to
> > >> reboot.  This is the first time since 1983 that I have felt satisfied
…[18 more quoted lines elided]…
>

Have a chat to your IBM sysprog and see what his reaction is to that
suggestion...<G>

ANY OS has to be configured, including mainframe ones. If you don't do it
right you will have problems on ANY platform.

In this case you have chosen to install a malfunctioning card.

The difference is that someone with reasonable competence could diagnose
your video card problem. If you were motivated enough you could read up on
IRQs and fix it yourself.(The information is in the Public Domain and
accessible from the Web). Or, you might choose to replace it with a
different (better behaved) video card. The OS does havea feature called Plug
n Play that will attempt to configure it for you. You have some options.

If that was a mainframe (say, in your garage...) you would be hiring IBM
consultancy at around $300 an hour, the information required to effect the
repair is Company Confidential and Proprietary, and they would come and fix
it when they got round to it.
Then they would run tests on it for the next two days so you couldn't use
it...

<snip>

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T14:26:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejt1u$bh2$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <MPG.19768963bd8f4626989684@News.CIS.DFN.DE> <3f0d5ae6_7@news.athenanews.com>`

```

On 10-Jul-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> The problem with the Waterfall approach is that it admits no other approach.

So whenever I worked in a shop that said they were using the Waterfall approach,
they were mistaken.   Because none of them used Waterfall exclusively.
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-07-10T02:35:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030709223543.28894.00000100@mb-m28.aol.com>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
>From: "Peter E.C. Dashwood" dashwood@enternet.co.nz 
>Date: 7/9/03 8:14 PM Eastern Daylight Time

I'm attempting to climb over the ramparts of the Fortress so I'll put my .02 in
here...

>1. Use of 40 year old Development Methodology (usually, the "waterfall"),
>where each phase is signed off before the next one can start. 

I was at a shop that did this for about 12 years - ain't there now.  If the
shop I'm at now has any Development Methodology other than - 'get it done'  I'm
unaware of it - and I've been there over 7 years.

>2. Root your Applications in the COBOL file system, which is completely
>closed, and ensures that a new COBOL program must be written every time you
>need a report...

We have very little VSAM left.  Most of the files have been converted to DB2. 
There are a few more to go but they aren't used much for reporting.  While some
of the users are pretty good at QMF most aren't and training them would be a
major task so - yes - we write a LOT of report programs. We could make canned
queries and put them in a library but at the moment none of us has the time to
do so (maybe because we're writing too many report programs?)

>3. View anything that isn't from IBM with extreme suspicion. View anything
>NEW from IBM with equal suspicion.

Nah - anything from CA is viewed with suspicion.  I think that the company as a
whole runs just about every platform you can think of.  My area just works with
the IBM mainframe and Cobol, with 2 of the people using MF with the bar code
system.

>4. PCs are toys and cannot be taken seriouly.

Not for most of the people in the company :) 

>Real user interfaces are by
>character entry on a green screen.

We tried putting a few inquiries on the Web and the users wondered what was so
wonderful about it.  I personally had nothing to do with this and have no idea
how to do it so I don't know if putting some of my data entry screens there
would make my users happier than they are with the 'green screen'.   I'll find
out later this year when we discuss the 'upgrade' of one of the VSAM files to
DB2.

>5. Don't use anything in COBOL that is subsequent to 1985, or requires more
>than one line to write.

While we're not up to the most current version of the IBM Cobol compiler we're
getting there. 

>
>Is it just a "control and power" thing?

Somewhat.  I did get my hand slapped for removing some EXITs in a few programs
when I had to convert them to use one of our new DB2 databases from the old
VSAM.

>Is it fear of new things?

For some of the people in our shop yes. Of the 8 1/2 of us (the 1/2 does IBM
mainframe Cobol and Unix stuff - our EDI person) 2 are definately stuck back in
1985, 1 I don't think has the capcity to learn something new other than by
sheer force, 2 will try but if it fails go around saying 'I told you so', 1
just goes with the flow (ie - if it's in a program they'll ask what it does and
maybe use it themselves but won't make an attempt to find out for themselves)
and the last 2 will try out all the new stuff they can.

>Is it simply apathy on the part of programmers?

Unlike the staff of CDW (see the commercial of the gal greedily reading all the
tech manuals?) learning about the new functions isn't automatic.  A new
compiler is installed and we get a list of things that won't work any more so
when we change a program that uses such (EXAMINE and INSPECT come to mind) we
can make appropriate changes - but we aren't told of the new goodies except
through places such as this forum.  Were the new goodies listed I think more of
us in my shop would use them (to clarify when I say listed I mean that the
document that is handed to us with the no-no's on it also contain the new stuff
- partly copied from the manual and partly digested by the tech staff). 

I'd like to add one other thing that I'm sure a lot of us here do/have done -
CLONING.  Need a new report - clone a program that does almost the same thing. 
Need a new screen - clone the map and program and so on.  Really NEW
developement is rare in my shop, and gutting another program to use new goodies
is kinda frowned upon because of the time it takes.
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T00:32:28+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d5d6e_5@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com>`

```

"YukonMama" <yukonmama@aol.com> wrote in message
news:20030709223543.28894.00000100@mb-m28.aol.com...
> >From: "Peter E.C. Dashwood" dashwood@enternet.co.nz
> >Date: 7/9/03 8:14 PM Eastern Daylight Time
>
> I'm attempting to climb over the ramparts of the Fortress so I'll put my
.02 in
> here...
>
…[3 more quoted lines elided]…
> I was at a shop that did this for about 12 years - ain't there now.  If
the
> shop I'm at now has any Development Methodology other than - 'get it done'
I'm
> unaware of it - and I've been there over 7 years.

At least that is a refreshing change (and a brave one <G>).
>
> >2. Root your Applications in the COBOL file system, which is completely
> >closed, and ensures that a new COBOL program must be written every time
you
> >need a report...
>
> We have very little VSAM left.  Most of the files have been converted to
DB2.
> There are a few more to go but they aren't used much for reporting.  While
some
> of the users are pretty good at QMF most aren't and training them would be
a
> major task so - yes - we write a LOT of report programs. We could make
canned
> queries and put them in a library but at the moment none of us has the
time to
> do so (maybe because we're writing too many report programs?)

QMF is not the ONLY option and there are English Language front ends to some
SQL tools. Then there are QBE and Crystal type graphic interfaces. Even if
none of this yanks your chain, SQL is not hard to learn and many users have
ACCESS at home and  can practice on the quiet with their own simple little
databases. As long as you keep writing report programs, you  are taking
their incentive to learn away, and making a rod for your own backs...
>
> >3. View anything that isn't from IBM with extreme suspicion. View
anything
> >NEW from IBM with equal suspicion.
>
> Nah - anything from CA is viewed with suspicion.  I think that the company
as a
> whole runs just about every platform you can think of.  My area just works
with
> the IBM mainframe and Cobol, with 2 of the people using MF with the bar
code
> system.
>

Your lack of "fortification" <G> is probably because of the multifarious
influences introduced from numerous different platforms and approaches. This
often happens. Fortress shops tend to be single platform for the most part
(sometimes with the network and Client Server as "second class citizens"
behind the "real" computers...Until they are seen to outperform the the
mainframes in terms of speed of development and delivery of solutions to
users...)



> >4. PCs are toys and cannot be taken seriouly.
>
…[5 more quoted lines elided]…
> We tried putting a few inquiries on the Web and the users wondered what
was so
> wonderful about it.  I personally had nothing to do with this and have no
idea
> how to do it so I don't know if putting some of my data entry screens
there
> would make my users happier than they are with the 'green screen'.   I'll
find
> out later this year when we discuss the 'upgrade' of one of the VSAM files
to
> DB2.
>
> >5. Don't use anything in COBOL that is subsequent to 1985, or requires
more
> >than one line to write.
>
> While we're not up to the most current version of the IBM Cobol compiler
we're
> getting there.
>
…[3 more quoted lines elided]…
> Somewhat.  I did get my hand slapped for removing some EXITs in a few
programs
> when I had to convert them to use one of our new DB2 databases from the
old
> VSAM.
>
> >Is it fear of new things?
>
> For some of the people in our shop yes. Of the 8 1/2 of us (the 1/2 does
IBM
> mainframe Cobol and Unix stuff - our EDI person) 2 are definately stuck
back in
> 1985, 1 I don't think has the capcity to learn something new other than by
> sheer force, 2 will try but if it fails go around saying 'I told you so',
1
> just goes with the flow (ie - if it's in a program they'll ask what it
does and
> maybe use it themselves but won't make an attempt to find out for
themselves)
> and the last 2 will try out all the new stuff they can.
>
> >Is it simply apathy on the part of programmers?
>
> Unlike the staff of CDW (see the commercial of the gal greedily reading
all the
> tech manuals?) learning about the new functions isn't automatic.  A new
> compiler is installed and we get a list of things that won't work any more
so
> when we change a program that uses such (EXAMINE and INSPECT come to mind)
we
> can make appropriate changes - but we aren't told of the new goodies
except
> through places such as this forum.  Were the new goodies listed I think
more of
> us in my shop would use them (to clarify when I say listed I mean that the
> document that is handed to us with the no-no's on it also contain the new
stuff
> - partly copied from the manual and partly digested by the tech staff).
>
> I'd like to add one other thing that I'm sure a lot of us here do/have
done -
> CLONING.  Need a new report - clone a program that does almost the same
thing.
> Need a new screen - clone the map and program and so on.  Really NEW
> developement is rare in my shop, and gutting another program to use new
goodies
> is kinda frowned upon because of the time it takes.
>

Interesting observations. Thanks Eileen. I'd say you are more of a "Hilltop
Redoubt" than a "Fortress" site...<G> things seem to be moving n the right
direction.

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T09:27:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejpkt$ope$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com>`

```
In article <3f0d5d6e_5@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
>"YukonMama" <yukonmama@aol.com> wrote in message
>news:20030709223543.28894.00000100@mb-m28.aol.com...

[snip]

>> We have very little VSAM left.  Most of the files have been converted to DB2.
>> There are a few more to go but they aren't used much for reporting.  While some
…[10 more quoted lines elided]…
>their incentive to learn away, and making a rod for your own backs...

NO, Mr Dashwood.  As long as they are writing report programs based on 
direct requests from their appropriate corporate superiors they are Doing 
Their Jobs.

As the textbook taught me, e'er-so-long ago, 'The allocation,
co-ordination and motivation of personnel and resources towards the
accomplishment of a stated Executive goal is the responsibility of
Management'; to the best of my knowledge this has changed but little.  If
it is decided by Management that the need for reports is best filled by
having programmers write them instead of teaching users to code them
ad-hoc - and being willing to pay them for being able to learn to do this
so that your competitors do not hire them away once they have learned to
do so - then disputing this is done at a subordinate's own risk.

(Side note - expecting users to 'practise on the quiet' with 'ACCESS at
home' in order to gain skills which will be profitable to the corporation
without a concommittant increase in profitability to the worker is, in my
opinion, an expectation of corporate theft.  To expect that workers use
their own time to make money for the corporation without making more money
for themselves is, I would say, equal to workers expecting to use company
time to make money for themselves without making money for the
corporation.)

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-07-10T11:50:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0zmdneoB45WlBJCiU-KYgg@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com>`

```
docdwarf@panix.com
>
> (Side note - expecting users to 'practise on the quiet' with 'ACCESS
…[11 more quoted lines elided]…
> corporation.)

PHB: "Wally, you've been too busy to get in the required 40 hours of annual
training, so I've hired a temp worker to give you a hand."

Wally: "Great, when does he start!"

PHB: "Yesterday. He's taking your class."
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T17:15:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bek6vu$h5q$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com>`

```

On 10-Jul-2003, "JerryMouse" <nospam@bisusa.com> wrote:

> PHB: "Wally, you've been too busy to get in the required 40 hours of annual
> training, so I've hired a temp worker to give you a hand."
…[3 more quoted lines elided]…
> PHB: "Yesterday. He's taking your class."


I just shared this with a bunch of mainframe programmers.   Their laughter was
tinged with tears because this is not much of an exaggeration at all.


(What they REALLY do, is cancel the class they promised and hire people who
already know the other technology).
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-10T20:29:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bek6vu$h5q$1@peabody.colorado.edu...
|
| On 10-Jul-2003, "JerryMouse" <nospam@bisusa.com> wrote:
|
| > PHB: "Wally, you've been too busy to get in the required 40 hours of
annual
| > training, so I've hired a temp worker to give you a hand."
| >
…[5 more quoted lines elided]…
| I just shared this with a bunch of mainframe programmers.   Their laughter
was
| tinged with tears because this is not much of an exaggeration at all.
|
|
| (What they REALLY do, is cancel the class they promised and hire people
who
| already know the other technology).

This might be part of the Fortress Mentality Pete keeps talking about.

I was working at a MAJOR Bank in New York, and we were converting a VSAM
system to DB2. SOME of the employees were excited about getting DB2
education, and of course they prepared themselves by doing nothing. The
never went to a library or a bookstore to get a head start on the class.
They never bothered to look at a manual. They never looked at any of the
programs under development. They never asked for informal education from the
people who were already working on the
project.

I, as a consultant, wasn't scheduled to go to the class.
I went to the library, and bookstores.
I got the manuals, and read them.
I looked at the programs under development, and I asked questions.

I worked on the project, they didn't.
I was already deeply involved by the time they got the class.

My advise is this, don't wait for the class.
By the time you get to the class, you should at least know enough to ask
intelligent questions.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T20:38:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bekirs$nom$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net>`

```

On 10-Jul-2003, "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:

> My advise is this, don't wait for the class.
> By the time you get to the class, you should at least know enough to ask
> intelligent questions.

I got myself a masters in OO.  I'm forgetting a lot of it, because it is awfully
hard to spend the time and money practicing it at home.   I know how high the
odds are that my expensive masters was wasted.   I know that playing with it at
home will have zero effect on whether I will use it at work.   Unless I make
myself less valuable at my present position, this is where I will stay.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-11T02:23:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gcpPa.49690$3o3.3281562@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <bekirs$nom$1@peabody.colorado.edu>`

```
I have to apologize for the tone of my previous post.
People waiting for classes is pet peeve of mine.
If you want it, go for it!

In any event, it wasn't directed at you but at the programmers who were
waiting for their class to be cancelled.

"Howard Brazee" <howard@brazee.net> wrote in message
news:bekirs$nom$1@peabody.colorado.edu...
|
| On 10-Jul-2003, "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:
…[5 more quoted lines elided]…
| I got myself a masters in OO.  I'm forgetting a lot of it, because it is
awfully
| hard to spend the time and money practicing it at home.   I know how high
the
| odds are that my expensive masters was wasted.

It's never a waste to learn anything.
At least you have a knowledge of OO, and I'm sure you can apply at least
some of it in the fortress.

This fortress thing may catch on.
"What do you do for a living?"
"I'm a Guardian of the Fortress" (sounds macho)

Maybe we can have a Secret Society for mainframers.

| I know that playing with it at
| home will have zero effect on whether I will use it at work.

Same here.
There just aren't any mainframe OO COBOL jobs yet.
I figure that it may work it's way in in the form of a package.
When it does I won't be ready at first, but I'll get up to speed if I have
to.

| Unless I make
| myself less valuable at my present position, this is where I will stay.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-15T22:34:21-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-65D288.22342115072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <bekirs$nom$1@peabody.colorado.edu>`

```
In article <bekirs$nom$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:

> On 10-Jul-2003, "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote:
> 
…[10 more quoted lines elided]…
> myself less valuable at my present position, this is where I will stay.

Education is never wasted.  

I use my masters in OO to bring lots of OO concepts to the procedural 
world I'm in.  In some case it adds some interesting things -- in others 
it causes eyes to glaze over and jaws to go slack with disinterest.  But 
it has certainly enhanced my designs.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-15T22:53:00-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf2emc$okr$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <bekirs$nom$1@peabody.colorado.edu> <joe_zitzelberger-65D288.22342115072003@corp.supernews.com>`

```
In article <joe_zitzelberger-65D288.22342115072003@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:

[snip]

>Education is never wasted.  

Oh, I *cannot* resist... y'know, I was taught that once, also, and I 
*still* can't figure out why.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-16T08:40:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-17B965.08401116072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <bekirs$nom$1@peabody.colorado.edu> <joe_zitzelberger-65D288.22342115072003@corp.supernews.com> <bf2emc$okr$1@panix1.panix.com>`

```
In article <bf2emc$okr$1@panix1.panix.com>, docdwarf@panix.com wrote:

> In article <joe_zitzelberger-65D288.22342115072003@corp.supernews.com>,
> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[8 more quoted lines elided]…
> DD

Because colleges are full of cute, bouncy, young ladies intent on 
spending 4+ years "finding themselves".  A process that usually involves 
mass quantities of mind altering beverages and expeimentation with all 
the various forms of debauchery.

I consider every day I spent in college well worth it.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-16T14:22:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3n2b$29q$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <bekirs$nom$1@peabody.colorado.edu> <joe_zitzelberger-65D288.22342115072003@corp.supernews.com> <bf2emc$okr$1@panix1.panix.com>`

```

On 15-Jul-2003, docdwarf@panix.com wrote:

> >Education is never wasted.
>
> Oh, I *cannot* resist... y'know, I was taught that once, also, and I
> *still* can't figure out why.

Trust your educator on this.

And trust your politicians when they say patriotism is the most important thing,
your clergy when they say religion is the most important thing.   Trust your
King when he says assassination is the worst crime.   Trust your public servants
when they say public service is the most important thing.

They wouldn't be biased would they?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-16T10:33:42-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3no6$dm8$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <joe_zitzelberger-65D288.22342115072003@corp.supernews.com> <bf2emc$okr$1@panix1.panix.com> <bf3n2b$29q$1@peabody.colorado.edu>`

```
In article <bf3n2b$29q$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 15-Jul-2003, docdwarf@panix.com wrote:
…[13 more quoted lines elided]…
>They wouldn't be biased would they?

An inclination of temperment or outlook away from bias is biased as well.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-16T14:19:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3msm$239$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <bekirs$nom$1@peabody.colorado.edu> <joe_zitzelberger-65D288.22342115072003@corp.supernews.com>`

```

On 15-Jul-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:

> Education is never wasted.
>
…[3 more quoted lines elided]…
> it has certainly enhanced my designs.

Agreed.   But I don't think it was cost-effective in my case.   My masters was
expensive, to make me a marginally better programmer.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-16T23:10:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-1355BB.23103816072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <bekirs$nom$1@peabody.colorado.edu> <joe_zitzelberger-65D288.22342115072003@corp.supernews.com> <bf3msm$239$1@peabody.colorado.edu>`

```
In article <bf3msm$239$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:

> On 15-Jul-2003, Joe Zitzelberger <joe_zitzelberger@nospam.com> wrote:
> 
…[8 more quoted lines elided]…
> expensive, to make me a marginally better programmer.

I would agree with that in some areas.  But I have also opened a great 
many doors by having the M.S.C.S. on the C.V.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-07-10T22:30:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3OlPa.40601$C83.3193803@newsread1.prod.itd.earthlink.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net>`

```

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net...

<<snip>>
>
> This might be part of the Fortress Mentality Pete keeps talking about.
…[6 more quoted lines elided]…
> programs under development. They never asked for informal education from
the
> people who were already working on the
> project.
…[12 more quoted lines elided]…
>

A good programmer, whether a consultant or not, will never stop trying to
learn new technologies.  Hopefully those technologies will be of direct
benefit in their current job.  But even if they are not, they still expand
the mindset of the programmer, providing updated neural connections and
making other tasks (to some degree) easier.  And then when the opportunity
presents itself, the programmer is ready.  As has been said, luck is where
opportunity meets preparation.

Paul
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T19:06:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0e6275_6@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <3OlPa.40601$C83.3193803@newsread1.prod.itd.earthlink.net>`

```
I'm glad to see I'm not alone <G>.

Agree 100%.

Pete.
"paul" <paulpigott@earthlink.net> wrote in message
news:3OlPa.40601$C83.3193803@newsread1.prod.itd.earthlink.net...
>
> "Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
…[39 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T19:04:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0e61f8_1@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <0zmdneoB45WlBJCiU-KYgg@giganews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net>`

```
Thank you Harley. You put it elegantly.

According to the Doc's argument the Corporation was stealing from you when
you did this.

Pete.

"Harley" <dennis.harleyNoSpam@worldnet.att.net> wrote in message
news:j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net...
>
> "Howard Brazee" <howard@brazee.net> wrote in message
…[13 more quoted lines elided]…
> | I just shared this with a bunch of mainframe programmers.   Their
laughter
> was
> | tinged with tears because this is not much of an exaggeration at all.
…[13 more quoted lines elided]…
> programs under development. They never asked for informal education from
the
> people who were already working on the
> project.
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T09:03:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemcjo$6kh$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bek6vu$h5q$1@peabody.colorado.edu> <j0kPa.47798$3o3.3251511@bgtnsc05-news.ops.worldnet.att.net> <3f0e61f8_1@news.athenanews.com>`

```
In article <3f0e61f8_1@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>Thank you Harley. You put it elegantly.
>
>According to the Doc's argument the Corporation was stealing from you when
>you did this.

NO, Mr Dashwood, you are wrong.  Notice that his participation was
strictly voluntary, that there was no corporate request or demand that he
use his own time to accomplish a task which would profit the company and
not profit him, as evidenced by 'I, as a consultant, wasn't scheduled to
go to the class'.

If you have a question about what I have written, Mr Dashwood, it might be 
more efficient to ask me about it directly; doing so might avoid 
demonstrations of error such as you made here.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-10T20:05:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eGjPa.47768$3o3.3250502@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bejpkt$ope$1@panix1.panix.com...
| In article <3f0d5d6e_5@news.athenanews.com>,
<<snip>>
|
| (Side note - expecting users to 'practise on the quiet' with 'ACCESS at
…[7 more quoted lines elided]…
|
I agree in part, but the workers who learn ACCESS are providing themselves
with a competitive edge. You'll find that most of the users who actually use
ACCESS are salaried, and are exempt from being paid for their time, and
effort, although they might take a course, and get reimbursed by the
company.

If you really want to bitch, read the Intellectual Property Agreements that
some corporations require their employees to sign.
You have an idea, you go to management, they say "no", you do it on your own
time, on your own machine, and develop a marketable product which then
belongs to the corporation that told you "no" in the first place.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T19:01:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0e6177_2@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bejpkt$ope$1@panix1.panix.com...
> In article <3f0d5d6e_5@news.athenanews.com>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
…[5 more quoted lines elided]…
>

I never argued that. I am suggesting that their Superiors expand their
horizons a bit.

One way to accomplish this is for the people opn the shop floor to make
suggestions. That is NOT a firing offence.

> As the textbook taught me, e'er-so-long ago, 'The allocation,
> co-ordination and motivation of personnel and resources towards the
> accomplishment of a stated Executive goal is the responsibility of
> Management'; to the best of my knowledge this has changed but little.

You obviously read different text book from me.

I believe that satisfaction in the workplace is a responsibility of all
employees, not JUST the Management.  Similarly, the profitability of the
concern is reflected by the degree of achievement reached by the people
working there. Happier employees achieve more.(Even when they don't, they
have more fun...). Corporations that are "good places to work" make more
profit.  We have argued this many times and we differ on it. I have little
to add on this occasion.


> If
> it is decided by Management that the need for reports is best filled by
…[6 more quoted lines elided]…
> home' in order to gain skills which will be profitable to the corporation

That is a gross misrepresentation of my position and you know it. People
work at home, not to improve Corporate profitability (although this also
happens, indirectly) but to increase their own profitability and, often,
simply for the satisfaction of achievement.

> without a concommittant increase in profitability to the worker is, in my
> opinion, an expectation of corporate theft.  To expect that workers use
…[3 more quoted lines elided]…
> corporation.)

Areed.  I never suggested any such thing.

Whether you accept it or not , there ARE people who want to improve their
chances and are interested in learning new stuff. (I know, I am one, and
have always been one.) Such people do not feel the Corporation is stealing
from them if they improve their skills.

That's just silly.

Pete.


>
> DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T09:43:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemet9$odu$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <3f0e6177_2@news.athenanews.com>`

```
In article <3f0e6177_2@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:bejpkt$ope$1@panix1.panix.com...
…[10 more quoted lines elided]…
>horizons a bit.

That argument seemed rather well-hidden, Mr Dashwood, in your statement to
which I responded - the one you editted out above - of 'As long as you
keep writing report programs, you are taking their incentive to learn
away, and making a rod for your own backs...'; might you show how a 'you'
in that statement is being used to refer to Superiors (caps original) and
not those who 'keep writing report programs'?

>
>One way to accomplish this is for the people opn the shop floor to make
>suggestions. That is NOT a firing offence.

I do not recall suggesting such a thing either, Mr Dashwood, and would 
appreciated your demonstrating how you might have come to such a 
conclusion based on what I posted.

>
>> As the textbook taught me, e'er-so-long ago, 'The allocation,
…[4 more quoted lines elided]…
>You obviously read different text book from me.

You may have read a different textbook than I, Mr Dashwood, but I've 
posted this definition previously and you've not seemed to disagree with 
it.

>
>I believe that satisfaction in the workplace is a responsibility of all
>employees, not JUST the Management.

Beliefs are a curious thing, Mr Dashwood... but please be so kind as to 
show where 'satisfaction' is in the list of 'allocation, co-ordination and 
motivation'.

>Similarly, the profitability of the
>concern is reflected by the degree of achievement reached by the people
>working there.

Mr Dashwood, your belief here seems to contradict the assertion found in 
The Economist of 'Cash is fact, profit is opinion'... well, maybe not, as 
Happy Accountants might have opinions which differ from those of Surly 
Accountants.  In either case you seem to be relating matters of opinion 
(profitability and 'degree of achievement', whatever that might be) in a 
fashion which cannot be measured.

>Happier employees achieve more.(Even when they don't, they
>have more fun...). Corporations that are "good places to work" make more
>profit.  We have argued this many times and we differ on it. I have little
>to add on this occasion.

On the other hand one needs to re-visit old arguments, lest one become 
stodgy... or stodgier than one already is.  Here's a simple rebuttal: if 
'happier employees achieve more' and 'corporations that are 'good places 
to work' make more profit' then there would have been no need for anyone 
to boycott Nike because of their sweatshops, there would have been no need 
for labor reform laws, there would be no need for any sort of workplace 
regulations to guarantee worker safety... need I continue?  Either 
employers are acting in direct conflict with their economic self-interest 
(a distinct possibility; homo economicus is not always homo rationalis) or 
there is a massive amount of evidence to the contrary.

>
>
…[13 more quoted lines elided]…
>simply for the satisfaction of achievement.

People do a variety of things at a variety of times for a variety of
reasons, Mr Dashwood; what I addressed here, clearly and unambiguously,
was an expectation that a worker use off-the-clock hours to gain and
practise a skill which would 'iomprove Corporate profitability'.

>
>> without a concommittant increase in profitability to the worker is, in my
…[6 more quoted lines elided]…
>Areed.  I never suggested any such thing.

I did not state that you had, Mr Dashwood... but do you think that it is 
so great a leap from 'many users have ACCESS at home and can practice on 
the quiet with their own simple little databases' an expectation that they 
might do so?

>
>Whether you accept it or not , there ARE people who want to improve their
…[4 more quoted lines elided]…
>That's just silly.

That is not what I posted, Mr Dashwood, and that does not seem to be a 
reasonable conclusion from what I posted.  Please be so kind as to address 
what I have written, not what you wish me to have written; what I posted - 
and what you interrupted in mide-sentence - was:

'To expect that workers use their own time to make money for the
corporation without making more money for themselves is, I would say,
equal to workers expecting to use company time to make money for
themselves without making money for the corporation.'

... and with that, as noted above, you agreed.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-11T13:53:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemfgt$oc5$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <3f0e6177_2@news.athenanews.com> <bemet9$odu$1@panix1.panix.com>`

```

On 11-Jul-2003, docdwarf@panix.com wrote:

> Here's a simple rebuttal: if
> 'happier employees achieve more' and 'corporations that are 'good places
> to work' make more profit' then there would have been no need for anyone
> to boycott Nike because of their sweatshops...

Except the people who boycott Nike do so because of their own self-interests
(such as a desire for high wages here).   The people who work in those sweat
shops are doing so because they are happy to have the opportunity to have a job.
  They move away from the ecologically damaging slash and burn economies, away
from jobless starvation, and into industry.   History shows that when a country
moves to that type of industry (as opposed to mining industry), the people get
skilled wealth increases within a generation or two.

The workers in the Nike sweatshops ARE happy to have their jobs.   They would be
unhappy if the protestors succeeded in making their labor as expensive as US
labor, so that Nike didn't see a reason to have the factories where the poor
need them the most.   They are not fans of "jobs for the rich", they are big
fans of "jobs for the poor".
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T10:25:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemhdi$f8d$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0e6177_2@news.athenanews.com> <bemet9$odu$1@panix1.panix.com> <bemfgt$oc5$1@peabody.colorado.edu>`

```
In article <bemfgt$oc5$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 11-Jul-2003, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>(such as a desire for high wages here).

That might well be the case... but if 'happier employees achieve more' and 
'corporations that are 'good places to work' make more profit' then Nike 
would never have built a sweatshop in the first place.

>The people who work in those sweat
>shops are doing so because they are happy to have the opportunity to have a job.

Ahhhh, look at it from the Corporate angle... setting aside, for the
moment, the subjectivity of measurement, what corporation builds a
facility with the intention of minimising profit?  Who says 'Hey, if we 
build/maintain our plant in this particular manner we'll Make Less 
Money... let's go for it!'?

If the answer is 'not too many folks who stay in business for very long' 
then the answer to many questions about 'What is the reason for...' seems 
to be 'In order to make More Money'.  For example:

Q. What is the reason for the abysmally poor lighting conditions in this
factory?

A. Poor lighting conditions result in more individual pieces being 
rejected for inspection reasons but, on the whole, save enough in 
electricity costs to earn this back and more.  We have poor lighting 
conditions in order to make More Money.

Q. What is the reason for all this dangerous equipment running without any 
safety equipment to guard the workers?

A. Dangerous equipment will, at times, kill or maim workers but the nature
of the task is such that another worker can be trained quickly with
minimum machine-downtime.  Saftey equipment slows down the rate at which
the worker can generate product.  Without safety equipment the worker can
generate more than sufficient product to cover the minimum downtime needed
to train a replacement *and* the pittance that local laws requires we pay 
for having killed/maimed a worker.  We have dangerous equipment running 
without any safety equipment in order to make More Money.

... etc., ad nauseum.  In short - if it made More Money to build safe, 
clean, pleasant places to work then Nike would never have built the 
sweatshops to begin with and folks would have had nothing to protest.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-11T14:56:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemj64$por$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0e6177_2@news.athenanews.com> <bemet9$odu$1@panix1.panix.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com>`

```

On 11-Jul-2003, docdwarf@panix.com wrote:

> >Except the people who boycott Nike do so because of their own self-interests
> >(such as a desire for high wages here).
…[3 more quoted lines elided]…
> would never have built a sweatshop in the first place.

Why?   If happy, low paid employees produce almost as much as happy, high paid
employees, they would go with the happy low-paid employees.   Or if they were
run by pointy-haired managers, they could make any decision.


> ... etc., ad nauseum.  In short - if it made More Money to build safe,
> clean, pleasant places to work then Nike would never have built the
> sweatshops to begin with and folks would have had nothing to protest.

Everything's a trade off.  It is quite possible for "happy employers to achieve
more", and still not achieve enough to be worth their cost.   Would an extra
$500/hour make you happier?   (not significantly more than an extra $400/hour -
but your company would go out of business with such a policy, which wouldn't
make you happier).

A starving person will be very happy to work long hours with bad lighting to
feed his family.   But a NBA player might find an offer of $10,000,000.00 per
year to be "insulting", and not work like a happy camper.    To keep me a happy
worker (who won't switch jobs), a company has to offer me more than it does
someone facing starvation.

> ... etc., ad nauseum.  In short - if it made More Money to build safe,
> clean, pleasant places to work then Nike would never have built the
> sweatshops to begin with and folks would have had nothing to protest.

Sure they would - they don't like Nike going overseas for any reason whatsoever.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T14:37:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben057$j6k$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <bemj64$por$1@peabody.colorado.edu>`

```
In article <bemj64$por$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 11-Jul-2003, docdwarf@panix.com wrote:
…[10 more quoted lines elided]…
>run by pointy-haired managers, they could make any decision.

Mr Brazee, the original assertions were 'happier employees achieve more'
and 'corporations that are 'good places to work' make more profit'.  


I am assuming, of course, that businesses are in business in order to
maximise profits; if a business makes decisions of 'we should deal with
our employees and their workplaces in a manner which decreases our
profits' then my conclusions, quite obviously, are wrong.

>
>
…[5 more quoted lines elided]…
>more", and still not achieve enough to be worth their cost.

This, then, contradicts the second assertion... unless you are saying, of 
course, that a 'good place to work' can be staffed by unhappy employees.

[snip]

>A starving person will be very happy to work long hours with bad lighting to
>feed his family.   But a NBA player might find an offer of $10,000,000.00 per
>year to be "insulting", and not work like a happy camper.    To keep me a happy
>worker (who won't switch jobs), a company has to offer me more than it does
>someone facing starvation.

Notice the original assertions, Mr Brazee... none of the qualifications 
you propose whatsoever.  Blanket assertions, both of them.

>
>> ... etc., ad nauseum.  In short - if it made More Money to build safe,
…[4 more quoted lines elided]…
>whatsoever.

Mr Brazee, I barely know what *I* like, let alone other people; I do know
that it might be reasonable to conclude thatif people are protesting
sweatshops and there are no sweatshops then people will not have
sweatshops against which to protest.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-11T19:11:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben256$2jd$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com>`

```

On 11-Jul-2003, docdwarf@panix.com wrote:

> Mr Brazee, the original assertions were 'happier employees achieve more'
> and 'corporations that are 'good places to work' make more profit'.

There is such a thing as an obvious generalization.   This is about as obvious
as can be.   Sort of like saying "happy people live longer", or "smokers die
sooner".   You can come up with counter examples, but that doesn't change
whether the generalization is true or at least useful.


> I am assuming, of course, that businesses are in business in order to
> maximise profits; if a business makes decisions of 'we should deal with
> our employees and their workplaces in a manner which decreases our
> profits' then my conclusions, quite obviously, are wrong.

First:   Businesses don't always do everything effectively to maximize profits.
 For instance, the obscene paychecks given to CEOs is not necessary to maximize
profitability.

Second:  Just because an element of their business is profitable, does not mean
that it is the most profitable use of a company's resources.

Third:  Most, if not all good things work on a curve.   The first glass of wine
I drink can help me live longer.   The 30th of the day can kill me.   Bigger
football players block better - but we don't find 600# linemen in the NFL.

Generalizations ARE useful.   Useful enough that we do create standards for such
things as structured programming, even though we can find examples of structured
programs that are worse than their non-structured counterparts.


> Notice the original assertions, Mr Brazee... none of the qualifications
> you propose whatsoever.  Blanket assertions, both of them.

Not at all.  I have seen this difficulty in the past with your conversations.  
You seem to reject a wide variety of generalizations because they are
generalizations.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T15:30:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben38t$ep0$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com> <ben256$2jd$1@peabody.colorado.edu>`

```
In article <ben256$2jd$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 11-Jul-2003, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>whether the generalization is true or at least useful.

What I attempted to demonstrate, Mr Brazee, was that the generalisation 
was so subtle that finding demonstrations of it were more difficult than 
finding demonstrations which appear to disprove it.

>
>
…[5 more quoted lines elided]…
>First:   Businesses don't always do everything effectively to maximize profits.

Nothing was stated about 'always', Mr Brazee... please be so kind as to 
address what I said, not what you wish me to have said.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-11T20:00:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben51i$3om$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com> <ben256$2jd$1@peabody.colorado.edu> <ben38t$ep0$1@panix1.panix.com>`

```

On 11-Jul-2003, docdwarf@panix.com wrote:

> What I attempted to demonstrate, Mr Brazee, was that the generalisation
> was so subtle that finding demonstrations of it were more difficult than
> finding demonstrations which appear to disprove it.

In that case your demonstration was too subtle for me.   Going back over this
thread again, I find it much too subtle for me, as I did not find any
demonstrations at all.

> >> I am assuming, of course, that businesses are in business in order to
> >> maximise profits; if a business makes decisions of 'we should deal with
…[7 more quoted lines elided]…
> address what I said, not what you wish me to have said.

That was one of multiple points designed to compare your theory with real life.


But if you don't like the word "always" there, take it out.   Are you aware of
any companies that "do everything effectively to maximize profits"?   I'm not.
I just included that word in case there is such a counter example.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T16:23:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben6c7$9qp$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <ben256$2jd$1@peabody.colorado.edu> <ben38t$ep0$1@panix1.panix.com> <ben51i$3om$1@peabody.colorado.edu>`

```
In article <ben51i$3om$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 11-Jul-2003, docdwarf@panix.com wrote:
…[7 more quoted lines elided]…
>demonstrations at all.

How curious... then what were you questioning?

>
>> >> I am assuming, of course, that businesses are in business in order to
…[10 more quoted lines elided]…
>That was one of multiple points designed to compare your theory with real life.

I try not to use phrases like 'real life', Mr Brazee... they can be *so* 
difficult to demonstrate.

>
>
>But if you don't like the word "always" there, take it out.   Are you aware of
>any companies that "do everything effectively to maximize profits"?

I don't believe I ever mentioned such a thing, Mr Brazee... when I do I 
shall endeavor to demonstrate it.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-07-12T09:38:06+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<benavi$m1r$1@aklobs.kc.net.nz>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

> Mr Brazee, the original assertions were 'happier employees achieve more'
> and 'corporations that are 'good places to work' make more profit'.

But are we sure which is the cause and which is the effect ?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T18:11:47-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bencn3$282$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com> <benavi$m1r$1@aklobs.kc.net.nz>`

```
In article <benavi$m1r$1@aklobs.kc.net.nz>,
Richard Plinston  <riplin@Azonic.co.nz> wrote:
>docdwarf@panix.com wrote:
>
…[3 more quoted lines elided]…
>But are we sure which is the cause and which is the effect ?

Plural majestatus est, Mr Plinston... I barely know of what *I* am sure, 
let alone anyone else.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-12T01:27:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0f62f2.30873096@news.optonline.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com> <benavi$m1r$1@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote:

>docdwarf@panix.com wrote:
>
…[3 more quoted lines elided]…
>But are we sure which is the cause and which is the effect ?

Good point. There is probably a confounding factor that causes both, to wit good
management.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-07-14T13:50:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fnc5hv8mk79k6t9gc5jibcq6qjhjau00sg@4ax.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <bemj64$por$1@peabody.colorado.edu>,
>Howard Brazee <howard@brazee.net> wrote:
…[21 more quoted lines elided]…
>profits' then my conclusions, quite obviously, are wrong.

Doc:

I attended a lecture years ago in which a corporate executive told us
he preferred the word "optimize" to the word "maximize" when referring
to profits and he preferred to analyze profitability on both a short
term as well as a long term basis.

He explained that when corporations merely consider short term
profitability instead of both long term and short term profitability,
they tend to be more likely to exploit resources.  These resources
involve not only human resources, but also capital equipment resources
and environmental resources.

When corporations give serious consideration to both long and short
term profitability, he explained they tend to avoid exploiting the
resources in favor of managing the resources more effectively.

He explained that this is the reaon he preferred to use the term
"optimizing" profit.  For example, for higher long term profitability,
it may be optimal to re-invest in machinery and equipment and take a
lower short term profit.



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-14T10:38:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beuf8d$32f$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com> <fnc5hv8mk79k6t9gc5jibcq6qjhjau00sg@4ax.com>`

```
In article <fnc5hv8mk79k6t9gc5jibcq6qjhjau00sg@4ax.com>,
Bob Wolfe  <rtwolfe.removethis@flexus.com> wrote:
>docdwarf@panix.com wrote:
>
…[30 more quoted lines elided]…
>term as well as a long term basis.

Mr Wolfe, I have heard a variety of people express a variety of opinions; 
as to which of them is 'truth' I cannot say.


I have heard, for instance, that quarterly reviews of performance (the
'Managers' Bane', as some knew them)  appear to be giving way to
up-to-the-minute evaluations by ad-hoc query.

I have heard, for instance, that the mantra is 'maximise shareholder
value' and that 'investors' are to be viewed as 'speculators' who are 
willing to move money into a competitor which seems more profitable at the 
drop of a hat.

I have heard, for instance, that in these belt-tightening times one of the 
first budgets to get cut is the one for Training and Development, despite 
the fact that 'our people are our biggest resource'.

What I have heard, granted, might not have anything to do with the way 
Business Is Done By 'The Many'... but it might also have as much to do 
with current business practises as does a lecture heard years ago.

What the executive taught you no doubt appears sound, that I cannot 
dispute... but what he taught you appears to be at variance with some of 
the practises of which I have heard.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-07-14T21:00:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h466hvcns3ph14knecciq7devk6bd101q3@4ax.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemj64$por$1@peabody.colorado.edu> <ben057$j6k$1@panix1.panix.com> <fnc5hv8mk79k6t9gc5jibcq6qjhjau00sg@4ax.com> <beuf8d$32f$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <fnc5hv8mk79k6t9gc5jibcq6qjhjau00sg@4ax.com>,
>Bob Wolfe  <rtwolfe.removethis@flexus.com> wrote:
…[53 more quoted lines elided]…
>with current business practises as does a lecture heard years ago.

I believe that good management practices are timeless.  The tools
businesses use to manage may change, but in my humble opinion, the
basic practices remain quite constant.

>What the executive taught you no doubt appears sound, that I cannot 
>dispute... but what he taught you appears to be at variance with some of 
>the practises of which I have heard.

No doubt.  I am often both surprised and alarmed by Ivy League
educated business executives who make decisions which are suicidal to
their own corporations and/or shareholders.

>
>DD


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-07-11T12:33:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgtpre4i030peb@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0e6177_2@news.athenanews.com> <bemet9$odu$1@panix1.panix.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bemhdi$f8d$1@panix1.panix.com...
> In article <bemfgt$oc5$1@peabody.colorado.edu>,
> Howard Brazee <howard@brazee.net> wrote:
[snipped]
> >The people who work in those sweat
> >shops are doing so because they are happy to have the opportunity to have
a job.
>
> Ahhhh, look at it from the Corporate angle... setting aside, for the
…[3 more quoted lines elided]…
> Money... let's go for it!'?

It may be difficult to identify a corporation planning to do so
but that it has been done was documented in Peter F. Drucker,
"Management: tasks, responsibilities, practices," Harper & Row,
1974, Chapter 24, "Management and the Quality of Life," page
320-321.

"... the company's top management asked a group of young
engineers and economist in its employ to prepare a plan for
the creation of employment opportunities in West Virginia,
and especially for the location of the company's new plant
facilities in areas of major unemployment in the state. For the
worst afflicted area, however, the westernmost corner of the
state on the border of Ohio, the planners could not come up
with an attractive project. Yet this area needed jobs the most.
In and around the little town of Vienna, West Virginia, there
was total unemployment, and no prospects for new industries.
The only plant that could possibly be put in the Vienna area
was a ferroalloy plant using a process that had already become
obsolete and had heavy cost disadvantages compared to more
modern processes such as Union Carbide's competitors were
already using.

"Even for the old process, Vienna was basically an
uneconomical location. The process required large amounts
of coal of fair quality. But the only coal available within the area
was coal of such high sulfur content that it could not be used
without expensive treatment and scrubbing. Even then--that is,
after heavy capital investment--the process was inherently noisy
and dirty, releasing large amounts of fly ash and of noxious gases.

"In addition, the only transportation facilities, both rail and road,
were not in West Virginia but across the river, on the Ohio side.
Putting the plant there, however, meant that the prevailing
westerly winds would blow the soot from the smokestacks and
the sulfur released by the power plants directly into the town of
Vienna, on the other bank of the river.

"Yet the Vienna plant would provide 1,500 jobs in Vienna itself
and another 500 to 1,000 jobs in a new coal field not too far
distant. In addition, the new coal field would be capable of
being stip-mined, so the new mining jobs would be free from
the accident and health hazards that had become increasingly
serious in the old and worked-out coal mines of the area. Union
Carbide top management came to the conclusion that social
responsibility demanded building the new plant, dispite its
maginal economics."
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T14:39:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben09k$k5e$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <vgtpre4i030peb@corp.supernews.com>`

```
In article <vgtpre4i030peb@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:bemhdi$f8d$1@panix1.panix.com...
…[11 more quoted lines elided]…
>> Money... let's go for it!'?

Quite right, Mr Smith... so, how many swallows is it going to take to make 
your particular summer this year?

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-07-11T15:20:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgu3jjeo5aps31@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:ben09k$k5e$1@panix1.panix.com...
> In article <vgtpre4i030peb@corp.supernews.com>,
[snip]
> Quite right, Mr Smith... so, how many swallows is it going to take to make
> your particular summer this year?

19,324

compute estimated-swallows
    = days-this-summer
      * average-cans-per-day
      * average-swallows-per-can
end-compute
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T15:31:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben3ai$f3r$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <vgu3jjeo5aps31@corp.supernews.com>`

```
In article <vgu3jjeo5aps31@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:ben09k$k5e$1@panix1.panix.com...
…[11 more quoted lines elided]…
>end-compute

More than enough swallows for a couple of guzzlings, then.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-11T19:48:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ben4ap$3ac$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <vgu3jjeo5aps31@corp.supernews.com>`

```

On 11-Jul-2003, "Rick Smith" <ricksmith@mfi.net> wrote:

> > Quite right, Mr Smith... so, how many swallows is it going to take to make
> > your particular summer this year?
…[7 more quoted lines elided]…
> end-compute

Didn't they return to Capistrano in March?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-07-11T17:06:16-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgu9q0gun1kj2c@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <vgu3jjeo5aps31@corp.supernews.com> <ben4ap$3ac$1@peabody.colorado.edu>`

```

Howard Brazee <howard@brazee.net> wrote in message
news:ben4ap$3ac$1@peabody.colorado.edu...
>
> On 11-Jul-2003, "Rick Smith" <ricksmith@mfi.net> wrote:
>
> > > Quite right, Mr Smith... so, how many swallows is it going to take to
make
> > > your particular summer this year?
> >
…[8 more quoted lines elided]…
> Didn't they return to Capistrano in March?

I have not spoken with the Swallows in ages. We had
a falling-out over what they did to the statue honoring
my great-uncle, Ivan Cann. They ... well ... did to the
statue about the same thing we are now doing to
Mr Dashwood's thread and perhaps the same explanation
applies, that these things happen.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-12T12:58:20+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0f5dc3_3@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <vgu3jjeo5aps31@corp.supernews.com> <ben4ap$3ac$1@peabody.colorado.edu> <vgu9q0gun1kj2c@corp.supernews.com>`

```

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:vgu9q0gun1kj2c@corp.supernews.com...
>
>
…[6 more quoted lines elided]…
>

I claim no ownership of this thread or any other in CLC. (I've been posting
here long enough to know what happens...)

Nevertheless, some very interesting insights are coming out of the posts.

I'll post my conclusions (for discussion or argument) some time next week.

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-12T12:55:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0f5d3f_5@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <vgu3jjeo5aps31@corp.supernews.com>`

```
LOL!

Good stuff, Rick!

Pete.

"Rick Smith" <ricksmith@mfi.net> wrote in message
news:vgu3jjeo5aps31@corp.supernews.com...
>
> <docdwarf@panix.com> wrote in message
news:ben09k$k5e$1@panix1.panix.com...
> > In article <vgtpre4i030peb@corp.supernews.com>,
> [snip]
> > Quite right, Mr Smith... so, how many swallows is it going to take to
make
> > your particular summer this year?
>
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 10)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-15T22:35:36-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemfgt$oc5$1@peabody.colorado.edu> <bemhdi$f8d$1@panix1.panix.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com>`

```
In article <ben09k$k5e$1@panix1.panix.com>, docdwarf@panix.com wrote:

> In article <vgtpre4i030peb@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
…[18 more quoted lines elided]…
> DD

African or European swallows?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-15T22:54:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf2epl$p6u$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com>`

```
In article <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <ben09k$k5e$1@panix1.panix.com>, docdwarf@panix.com wrote:

[snip]

>> Quite right, Mr Smith... so, how many swallows is it going to take to make 
>> your particular summer this year?
>> 
>
>African or European swallows?

Answering a question with a question is no answer at all, Mr Zitzelberger.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-16T23:17:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f153500_6@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bf2epl$p6u$1@panix1.panix.com...
> In article <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com>,
> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[4 more quoted lines elided]…
> >> Quite right, Mr Smith... so, how many swallows is it going to take to
make
> >> your particular summer this year?
> >>
…[4 more quoted lines elided]…
>
Isn't it?

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-16T08:03:31-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3euj$kk7$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <3f153500_6@news.athenanews.com>`

```
In article <3f153500_6@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:bf2epl$p6u$1@panix1.panix.com...
…[14 more quoted lines elided]…
>Isn't it?

Nope, t'ain't.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-17T01:14:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f15504d_1@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <3f153500_6@news.athenanews.com> <bf3euj$kk7$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bf3euj$kk7$1@panix1.panix.com...
> In article <3f153500_6@news.athenanews.com>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:bf2epl$p6u$1@panix1.panix.com...
> >> In article <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com>,
> >> Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[4 more quoted lines elided]…
> >> >> Quite right, Mr Smith... so, how many swallows is it going to take
to make
> >> >> your particular summer this year?
> >> >>
…[3 more quoted lines elided]…
> >> Answering a question with a question is no answer at all, Mr
Zitzelberger.
> >>
> >Isn't it?
>
> Nope, t'ain't.

What, never?

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-16T12:55:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lXbRa.57482$3o3.3841030@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bf2epl$p6u$1@panix1.panix.com...
| In article <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com>,
| Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
…[4 more quoted lines elided]…
| >> Quite right, Mr Smith... so, how many swallows is it going to take to
make
| >> your particular summer this year?
| >>
…[3 more quoted lines elided]…
| Answering a question with a question is no answer at all, Mr Zitzelberger.

It depends.
At times, it's better to answer a question with a question, especially when
the 2nd question causes the person who asked the 1st question to answer
their own question.
They're going to ask why, anyway.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-16T14:24:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3n7n$2a2$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com>`

```

On 15-Jul-2003, docdwarf@panix.com wrote:

> >African or European swallows?
>
> Answering a question with a question is no answer at all, Mr Zitzelberger.

In this case it was.   Are you familiar with the original question he quoted?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-16T10:37:51-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3nvv$f9p$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <bf3n7n$2a2$1@peabody.colorado.edu>`

```
In article <bf3n7n$2a2$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 15-Jul-2003, docdwarf@panix.com wrote:
…[5 more quoted lines elided]…
>In this case it was.   Are you familiar with the original question he quoted?

This case, I believe, is not different from all other cases, even were 
someone to attempt a reference to a film made nigh three decades ago that 
featured a British comedy-troupe.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-16T15:59:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf3spf$4hj$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <bf3n7n$2a2$1@peabody.colorado.edu> <bf3nvv$f9p$1@panix1.panix.com>`

```

On 16-Jul-2003, docdwarf@panix.com wrote:

> >> Answering a question with a question is no answer at all, Mr Zitzelberger.
> >
…[4 more quoted lines elided]…
> featured a British comedy-troupe.

In the original, answering the question with a question solved the problem.  
Which is an answer.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-16T15:44:35-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf49v3$9dc$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bf3n7n$2a2$1@peabody.colorado.edu> <bf3nvv$f9p$1@panix1.panix.com> <bf3spf$4hj$1@peabody.colorado.edu>`

```
In article <bf3spf$4hj$1@peabody.colorado.edu>,
Howard Brazee <howard@brazee.net> wrote:
>
>On 16-Jul-2003, docdwarf@panix.com wrote:
…[10 more quoted lines elided]…
>Which is an answer.

In movies a man wearing a cape can jump out of a window and fly... which 
is no solution.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 12)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-17T18:03:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vheapfk1irlt3a@corp.supernews.com>`
- **In-Reply-To:** `<bf2epl$p6u$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
>>>Quite right, Mr Smith... so, how many swallows is it going to take to make 
>>>your particular summer this year?
…[5 more quoted lines elided]…
> Answering a question with a question is no answer at all, Mr Zitzelberger.

Please tell me that Python references aren't lost on his highness...
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-07-18T00:28:12-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-70313C.00281218072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <vheapfk1irlt3a@corp.supernews.com>`

```
In article <vheapfk1irlt3a@corp.supernews.com>,
 LX-i <LXi0007@Netscape.net> wrote:

> docdwarf@panix.com wrote:
> >>>Quite right, Mr Smith... so, how many swallows is it going to take to make 
…[8 more quoted lines elided]…
> Please tell me that Python references aren't lost on his highness...

I'm not much of a Python guru...does it support references?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 14)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-18T18:36:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vhh14e7uh4t7c1@corp.supernews.com>`
- **In-Reply-To:** `<joe_zitzelberger-70313C.00281218072003@corp.supernews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vgtpre4i030peb@corp.supernews.com> <ben09k$k5e$1@panix1.panix.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <vheapfk1irlt3a@corp.supernews.com> <joe_zitzelberger-70313C.00281218072003@corp.supernews.com>`

```
Joe Zitzelberger wrote:

> In article <vheapfk1irlt3a@corp.supernews.com>,
>  LX-i <LXi0007@Netscape.net> wrote:
…[16 more quoted lines elided]…
> I'm not much of a Python guru...does it support references?

I'm not either - but if you're really into Python, you can see 
references in many places...

(Time to pull out the holy grail movie and watch it again...)
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-18T06:25:52-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bf8hvg$ma2$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <vheapfk1irlt3a@corp.supernews.com>`

```
In article <vheapfk1irlt3a@corp.supernews.com>,
LX-i  <LXi0007@Netscape.net> wrote:
>docdwarf@panix.com wrote:
>>>>Quite right, Mr Smith... so, how many swallows is it going to take to make 
…[8 more quoted lines elided]…
>Please tell me that Python references aren't lost on his highness...

I believe it was Nietzsche who spoke about someone who takes serious 
things humorously and humorous things seriously... I really should 
research the quotation and get it right, some day.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 14)_

- **From:** LX-i <LXi0007@Netscape.net>
- **Date:** 2003-07-18T19:28:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vhh46brmmooseb@corp.supernews.com>`
- **In-Reply-To:** `<bf8hvg$ma2$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <joe_zitzelberger-DA15C0.22353615072003@corp.supernews.com> <bf2epl$p6u$1@panix1.panix.com> <vheapfk1irlt3a@corp.supernews.com> <bf8hvg$ma2$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

> I believe it was Nietzsche who spoke about someone who takes serious 
> things humorously and humorous things seriously... I really should 
> research the quotation and get it right, some day.

So you could "cite it please"?  :)
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-18T21:06:48-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfa5j8$frt$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <vheapfk1irlt3a@corp.supernews.com> <bf8hvg$ma2$1@panix1.panix.com> <vhh46brmmooseb@corp.supernews.com>`

```
In article <vhh46brmmooseb@corp.supernews.com>,
LX-i  <LXi0007@Netscape.net> wrote:
>docdwarf@panix.com wrote:
>
…[4 more quoted lines elided]…
>So you could "cite it please"?  :)

That's one advantage... another is that I'd be able to attribute the 
quotation accurately and yet another is that I could learn the quotation 
as it was written.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-12T12:51:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0f5c29_1@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <3f0e6177_2@news.athenanews.com> <bemet9$odu$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bemet9$odu$1@panix1.panix.com...
> In article <3f0e6177_2@news.athenanews.com>,
> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:bejpkt$ope$1@panix1.panix.com...
> >> In article <3f0d5d6e_5@news.athenanews.com>,
> >> Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
…[3 more quoted lines elided]…
> >> direct requests from their appropriate corporate superiors they are
Doing
> >> Their Jobs.
> >>
…[9 more quoted lines elided]…
> not those who 'keep writing report programs'?

Certainly. It was "you" in the impersonal (I don't like using "one") and
plural sense. In other words the "you" in question covered the poster and
their colleagues, including their management.


>
> >
…[6 more quoted lines elided]…
>

It is not a conclusion; it is an observation. Don't become the effect of
your own pedantry, Doc.

> >
> >> As the textbook taught me, e'er-so-long ago, 'The allocation,
…[17 more quoted lines elided]…
>

Why? If I did that I'd be arguning on YOUR ground with YOUR definitions <G>.


> >Similarly, the profitability of the
> >concern is reflected by the degree of achievement reached by the people
…[8 more quoted lines elided]…
>

Absolutely. Many important factors in successful Businesses cannot be
measured and your "Argument from Authority" based on the Economist is
pathetic...who says The Economist has the monoply on business acumen?
(Besides, your quote is out of context; the The Economist expresses the
opinons of many people, many of whom don't always agree.)

> >Happier employees achieve more.(Even when they don't, they
> >have more fun...). Corporations that are "good places to work" make more
> >profit.  We have argued this many times and we differ on it. I have
little
> >to add on this occasion.
>
…[6 more quoted lines elided]…
> regulations to guarantee worker safety... need I continue?

Yes, I think you should, given that none of the above make a compelling
case.

(I'm not touching the Nike sweatshops, but I'd be surprised if no-one else
here does <G>...)

History is full of examples of injustice and bad treatment of workers but we
are not reviewing history.

My argument is that treating employees well is good for all concerned. (The
employees AND the company...)

Citing examples of cases where companies did NOT do this does not make it
any less true. All it shows is that they got it wrong.


> Either
> employers are acting in direct conflict with their economic self-interest
> (a distinct possibility; homo economicus is not always homo rationalis) or
> there is a massive amount of evidence to the contrary.
>

Those are not the only two possibilities, they are just the two that you
would like so you can "win" this argument.

Actually, you can't "win" it any more than I can, because we have two
completely differing views and neither of them is wrong.

I have a positive and flexible attitude. I don't want or need to work within
the "letter of the Law" (although I can do that if it is required), mostly I
am happy to go the "extra mile". (I don't find myself out of work very often
and when I am it is usually because I choose to be...). I am happy to invest
my own time and energy in making myself a more useful and marketable
commodity, whether that benefits the company I'm working for or not. I see
learning as part of my personal development; FAR more imoortant than any
corporate reward. At the end of the day I get satisfaction from what I have
achieved.

BUT, I don't think people who DON'T feel this way are wrong!

I won't presume to describe your profile, Doc. Limiting my comments to
statements you have posted here, I think it would be fair to say that the
above is NOT a description of your attitude.

I have no problem with you having whatever attitude you have. You seem to be
fair and I believe you are honest. But I believe you do get bogged down in
the details and enjoy scrutinising the small stuff.

You seem to have difficulty in understanding that I can approach the
workplace with an attitude different from your own, and still succeed in it.

The bottom line is that there is more than ONE truth when it comes to
succeeding in Business.

 >
> >
…[3 more quoted lines elided]…
> >> ad-hoc - and being willing to pay them for being able to learn to do
this
> >> so that your competitors do not hire them away once they have learned
to
> >> do so - then disputing this is done at a subordinate's own risk.

What risk would that be, Doc? Nobody I know has been flogged or thumbscrewed
(recently) for suggesting to the "Powers that Be", some possible flaws in
their policy.

The key is in "decided by Management". These decisions are made on the basis
of the information they have. If nobody on the "shop floor" feeds back
experience, then the quality of the decisions will be poorer. This is one
area where we differ. I see it as a RESPONSIBILITY to ensure that my input
goes into the decision making process (I've ALWAYS felt that way ever since
I was a very junior programmer - maybe it's a personality thing...I figure I
will have to live with what they decide so I should give it my best shot to
help them get it right); others see decision making as the responsibility of
Management who get paid for it and it is down to them if it is good, bad, or
indifferent. Neither viewpoint is "wrong" (but I know where I'd rather work
<G>).

In recent years when I have been on the other side of the fence (making the
decisions) I have always striven to ensure that people feel safe to suggest
things and if they disagree with a policy, they make their case (without
prejudice or worrying that their "card will be marked"). This policy extends
from the most senior experienced people (and Contractors) to the most
junior, as I believe if a member of a team adds nothing to it they shouldn't
be there...). Obviously, I make no distinction between Contractors and
Permanent staff and strongly discourage others from doing so.

> >>
> >> (Side note - expecting users to 'practise on the quiet' with 'ACCESS at
> >> home' in order to gain skills which will be profitable to the
corporation
> >

> >That is a gross misrepresentation of my position and you know it. People
> >work at home, not to improve Corporate profitability (although this also
…[7 more quoted lines elided]…
>
There was no such "expectation". If they do so, well and good. Many would
want to. Others won't. It's OK either way.

> >
> >> without a concommittant increase in profitability to the worker is, in
my
> >> opinion, an expectation of corporate theft.  To expect that workers use
> >> their own time to make money for the corporation without making more
money
> >> for themselves is, I would say, equal to workers expecting to use
company
> >> time to make money for themselves without making money for the
> >> corporation.)
…[7 more quoted lines elided]…
>

Yes I do. The key word is "expectation". There is no expectation or requirem
ent to do so, but it can help their PERSONAL development if they acquire
more knowledge. If that happens to be a skill that improves their
performance in the workplace, then that's a bonus. Everybody wins.

> >
> >Whether you accept it or not , there ARE people who want to improve their
> >chances and are interested in learning new stuff. (I know, I am one, and
> >have always been one.) Such people do not feel the Corporation is
stealing
> >from them if they improve their skills.
> >
…[4 more quoted lines elided]…
> what I have written, not what you wish me to have written

I don't wish you to have written anything. The conclusion was valid from
your post:

"Side note - expecting users to 'practise on the quiet' with 'ACCESS at
home' in order to gain skills which will be profitable to the corporation
without a concommittant increase in profitability to the worker is, in my
opinion, an expectation of corporate theft."

If people work at home to improve their workplace skills, without receiving
more money from their employer, the corporation is stealing from them. May
not be what you meant, but it is certainly what you wrote.

Now, getting back to the topic...

I wonder how much or little both of the attitudes described above influence
the establishment of the Fortress on any given site?

Pete.



> DD
>
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-07-11T21:02:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D_-cnV-Tovql8ZKiU-KYgg@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0d5d6e_5@news.athenanews.com> <bejpkt$ope$1@panix1.panix.com> <3f0e6177_2@news.athenanews.com> <bemet9$odu$1@panix1.panix.com> <3f0f5c29_1@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
>
> (I'm not touching the Nike sweatshops, but I'd be surprised if no-one
> else here does <G>...)

I'll touch it. Nike doesn't have sweatshops. Anyone who says differently is
exaggerating.

Nike's shops in Vietnam, China, and Indonesia have been accused of having
young female workers paid below the local minimum wage, forced to work
overtime, facing physical, verbal and sexual abuse on the job, and being
exposed to toxic chemicals with  inadequate health and safety equipment
(similar to conditions faced by my ex-wife).

But nobody ever said it was too hot.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T22:31:55-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<benrur$o28$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bemet9$odu$1@panix1.panix.com> <3f0f5c29_1@news.athenanews.com> <D_-cnV-Tovql8ZKiU-KYgg@giganews.com>`

```
In article <D_-cnV-Tovql8ZKiU-KYgg@giganews.com>,
JerryMouse <nospam@bisusa.com> wrote:
>Peter E.C. Dashwood wrote:
>>
…[12 more quoted lines elided]…
>But nobody ever said it was too hot.

Oh, I *cannot* resist... don't sound too hot to me, haw haw haw!

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T22:31:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<benrtb$npc$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0e6177_2@news.athenanews.com> <bemet9$odu$1@panix1.panix.com> <3f0f5c29_1@news.athenanews.com>`

```
In article <3f0f5c29_1@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:bemet9$odu$1@panix1.panix.com...
…[26 more quoted lines elided]…
>their colleagues, including their management.

Of *course* that was the case, Mr Dashwood... but I am uncertain how their 
management 'keep writing report programs'; as I understand it their 
management assigns them to write them.

>
>
…[11 more quoted lines elided]…
>your own pedantry, Doc.

No need for me to do that, Mr Dashwood, as long as others position 
themselves as victims of their own imprecision.

>
>> >
…[20 more quoted lines elided]…
>Why? If I did that I'd be arguning on YOUR ground with YOUR definitions <G>.

If you don't, Mr Dashwood, you are not only arguing something which was 
not presented by anyone but yourself... but you are agruing something that 
is, to the best of my knowledge, impossible to quantify or measure (that 
being 'satisfaction').  A neat trick... not very useful, perhaps, but 
neat.

>
>
…[12 more quoted lines elided]…
>Absolutely.

Good of you to admit this, Mr Dashwood... but since you are relating
matters of opinion in a fashion which cannot be measured it makes
discussion along other lines - say, quantifiable phenomena which might
lead to reproducible results - bit difficult.  Do you think that cheddar
or Stilton is better-filled with gustrons (units of flavor)?

>Many important factors in successful Businesses cannot be
>measured and your "Argument from Authority" based on the Economist is
>pathetic...who says The Economist has the monoply on business acumen?

Nobody in this thread has intimated as such, Mr Dashwood, and it makes 
things more difficult when you appear to confuse an attribution (which it 
was my intention to make) with an argumentum ad verecundiam. 

>(Besides, your quote is out of context; the The Economist expresses the
>opinons of many people, many of whom don't always agree.)

Ummmm... what does the plurality of authorship have to do with my 
attributing a quote to the publication?

>
>> >Happier employees achieve more.(Even when they don't, they
…[13 more quoted lines elided]…
>case.

Each of them is *quite* compelling, Mr Dashwood... there, see how easy an 
'it is/it isn't' argument is?

[snip]

>
>History is full of examples of injustice and bad treatment of workers but we
>are not reviewing history.

Those who learn what Santayana had to say about the mistake of the past, 
Mr Dashwood, are doomed to repeat it.  Are you proposing to argue from 
some manner of metaphysical condition of eternal immediacy?

>
>My argument is that treating employees well is good for all concerned. (The
…[3 more quoted lines elided]…
>any less true. All it shows is that they got it wrong.

No, Mr Dashwood, that the companies existed - sometimes for centuries - 
and did so in a fashion showing continuing profit seems to indicate they 
were doing something quite right.

Showing that The Market did not correct these things but the force of 
Government was needed to change matters seems to indicate rather strong 
economic incentives for continuing those practices.

>
>
…[7 more quoted lines elided]…
>would like so you can "win" this argument.

I did not say that there were no other possibilities, Mr Dashwood... but I 
notice that you haven't raised any.

>
>Actually, you can't "win" it any more than I can, because we have two
>completely differing views and neither of them is wrong.

Mr Dashwood, I have brought forward examples to support my assertions, you 
have dismissed them as being 'insufficiently compelling'.  Your dismissal, 
by these lights, is equally insufficiently compelling and is, itsself, 
dismissed.

Am I being clear, Mr Dashwood?  Just to respond to me with 'It ain't so, 
we disagree, that's all, we're both right' does not make much of a 
substantiated argument.

>
>I have a positive and flexible attitude. I don't want or need to work within
…[9 more quoted lines elided]…
>BUT, I don't think people who DON'T feel this way are wrong!

Mr Dashwood, the only person I have said stated something wrongly in this 
exchange was you.  You have made assertions, I have questioned them and 
given examples to support my argument.  You have responded with things 
like 'There are more possibilities' and then not given any, as though 
doing this has any impact.

>
>I won't presume to describe your profile, Doc. Limiting my comments to
>statements you have posted here, I think it would be fair to say that the
>above is NOT a description of your attitude.

Mr Dashwood, what does 'attitude' have to do with your inability to 
present a counterargument beyond 'none of the above make a compelling 
case'?

>
>I have no problem with you having whatever attitude you have. You seem to be
>fair and I believe you are honest. But I believe you do get bogged down in
>the details and enjoy scrutinising the small stuff.

The 'small stuff' here, Mr Dashwood, is the economic framework for how a 
workplace is to be structured.

>
>You seem to have difficulty in understanding that I can approach the
>workplace with an attitude different from your own, and still succeed in it.

NO, Mr Dashwood, this is wrong.  I have difficulty in understanding how
you can make assertions such as 'Corporations that are "good places to
work" make more profit' and, in the face of contrary evidence, refuse to 
substantiate them.

>
>The bottom line is that there is more than ONE truth when it comes to
>succeeding in Business.

The bottom line, Mr Dashwood, is that you have made assertions and, in the 
face of contrary evidence, refused to substantiate them.

>
> >
…[10 more quoted lines elided]…
>their policy.

Mr Dashwood, it was never suggested that anyone would be flogged or 
thumbscrewed for disputing management policy.  My experience is, granted, 
small and limited... but I know of people who have assigned to 
less-than-desireable tasks, demoted, transferred to less-than-desireable 
area and fired for doing so.

>
>The key is in "decided by Management". These decisions are made on the basis
>of the information they have. If nobody on the "shop floor" feeds back
>experience, then the quality of the decisions will be poorer.

Mr Dashwood, do you think that it would be possible to have a manager 
physically remove the door from his office to show how he is complying 
with the company's 'Open-Door Management Policy'... and then have his 
secretary send out a general memo that even though his door is open to all 
people at all time anyone who wants to see him has to make an appointment 
with the secretary first?

>This is one
>area where we differ. I see it as a RESPONSIBILITY to ensure that my input
…[6 more quoted lines elided]…
><G>).

One moment, let me dig in my briefcase... ahhhh, there it is.  From 
'Beyond Computing, May 1996' (a citing, Mr Dashwood, not an argumentum ad 
verecundiam), a sidebar called 'Cultural Contradictions'

--begin quoted text:

A gap between what management says in the name of corporate culture and 
what people actually experience on the job can produce a hidden 
counterculture and undermine the best management intentions.

In the following examples of doublespeak, the voice of management - the 
formal culture - is matched with a contradictory view from the ranks - the 
informal culture.  To prevent this from happening in your company, make 
sure you're listening to the middle and lower ranks.

WE MUST WORK AS A TEAM... But you get rewarded for standing out.

MERIT ALONE COUNTS IN GETTING AHEAD... But it makes a big difference if 
you're part of the old-boy network'

--end quoted text

>
>In recent years when I have been on the other side of the fence (making the
…[6 more quoted lines elided]…
>Permanent staff and strongly discourage others from doing so.

As my Sainted Paternal Grandfather - may he sleep with the angels! - used 
to say, Mr Dashwood, 'Never use yourself as a comparative, you'll only be 
disappointed.'

*You*, personally, might never decide that paying a fine of US$10,000 per 
day is cheaper than building an on-site pollution-control center to clean 
up your factory's waste... other people have.  From the aforementioned 
'Cultural Contradictions' -

--begin quoted text:

MANAGEMENT WELCOMES YOUR CRITICISM... As long as they like what they hear.

WE TRUST OUR EMPLOYEES... But not out of our sight.

SPEAK UP AT MEETINGS... And get shot down.

FRESH IDEAS, NEW WAYS OF DOING THINGS ARE WHAT MANAGEMENT WANTS... All we 
hear is 'If it ain't broke, don't fix it.'

--end quoted text

>
>> >>
…[15 more quoted lines elided]…
>want to. Others won't. It's OK either way.

Odd... well, as long as you feel there's no expectation for it to happen 
then why bother to mention it?

>
>> >
…[15 more quoted lines elided]…
>Yes I do.

Thanks for clearing that up, then... greatly appreciated.

>The key word is "expectation". There is no expectation or requirem
>ent to do so, but it can help their PERSONAL development if they acquire
>more knowledge. If that happens to be a skill that improves their
>performance in the workplace, then that's a bonus. Everybody wins.

So if folks do what is not expected of them... everybody wins!  Well, 
let's see... everyone expects folks to show up on time and put in a full 
day's work, so...


>
>> >
…[20 more quoted lines elided]…
>more money from their employer, the corporation is stealing from them.

NO, Mr Dashwood, that is wrong.  You addressed this above when you said 
there was no condition of 'expectation'.

>May
>not be what you meant, but it is certainly what you wrote.

What I wrote, Mr Dashwood, is that 'Expecting something... is an 
expectation of something'; that is in no wise the logical equivalent of 
'If people do... then it is theft'.

There is a difference, Mr Dashwood, between the expectation of an action 
and the voluntary performance of an action.  My apologies if this was a 
bit too subtle.

>
>Now, getting back to the topic...
>
>I wonder how much or little both of the attitudes described above influence
>the establishment of the Fortress on any given site?

I'm not sure, Mr Dashwood... it is so difficult to measure.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-07-14T04:44:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030714004413.03537.00000314@mb-m05.aol.com>`
- **References:** `<3f0d5d6e_5@news.athenanews.com>`

```
>From: "Peter E.C. Dashwood" dashwood@enternet.co.nz 
>Date: 7/10/03 8:32 AM Eastern Daylight Time

>QMF is not the ONLY option and there are English Language front ends to some
>SQL tools. Then there are QBE and Crystal type graphic interfaces. Even if
…[5 more quoted lines elided]…
>>

I'm writing from a mainframe standpoint.  There is a lot of data in the company
that doesn't reside on the mainframe and the users do use ACCESS and other
means of getting their information.  A lot of the reporting I used to do is now
handled by the Data Warehouse area as I feed my information to them.  I in turn
receive information from several other sources to update my files that are
required on the mainframe.  One of my biggest hassles is getting userids and
NON-EXPIRING passwords to the various servers around the company ::sigh::.


> Fortress shops tend to be single platform for the most part
>(sometimes with the network and Client Server as "second class citizens"

Here it's the mainframe that's the second class citizen.


>Interesting observations. Thanks Eileen. I'd say you are more of a "Hilltop
>Redoubt" than a "Fortress" site...<G> things seem to be moving n the right
>direction.

You're welcome :)
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T08:50:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejnec$8a8$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com>`

```
In article <20030709223543.28894.00000100@mb-m28.aol.com>,
YukonMama <yukonmama@aol.com> wrote:

[snip]

>I'd like to add one other thing that I'm sure a lot of us here do/have done -
>CLONING.  Need a new report - clone a program that does almost the same thing. 
>Need a new screen - clone the map and program and so on.  Really NEW
>developement is rare in my shop, and gutting another program to use new goodies
>is kinda frowned upon because of the time it takes.

'Really NEW development' may be rare due to a phenomenon I have 
observed... very few people are bright or creative enough to want 
something that actually hasn't been done before; most folks I have seen 
want only 'What Joe/Mary has, but in blue/broken down by department.'

(This, of course, is a variation of Ecc I.9.)

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T14:32:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejtdv$bqu$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <bejnec$8a8$1@panix1.panix.com>`

```
Fortress hammer - Why?

(I thought I would replace one old reliable tool with another in this
discussion).

New technologies such as fast drying glues and nail guns produce the desired
edifices much faster and cheaper.  But hammer users fight against the new
technology.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-07-14T13:58:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ugd5hv0trr2cn38me328dujust6pifk5hj@4ax.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com> <bejnec$8a8$1@panix1.panix.com> <bejtdv$bqu$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:

>Fortress hammer - Why?
>
…[5 more quoted lines elided]…
>technology.

Howard:

Your point is right on target!  I use both nail guns as well as Liquid
Nails brand construction adhesive on my various home construction
projects.

But I still use my three claw hammers as well.

It just depends on the specifics of the job I'm doing.

At the risk of repeating an old mantra in this group.  It appears that
you are suggesting that it's always important to "use the right tool
for the task at hand!"

And I agree 100%!




Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T14:29:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejt7h$bh4$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <20030709223543.28894.00000100@mb-m28.aol.com>`

```

On  9-Jul-2003, yukonmama@aol.com (YukonMama) wrote:

> We tried putting a few inquiries on the Web and the users wondered what was so
> wonderful about it.  I personally had nothing to do with this and have no idea
…[3 more quoted lines elided]…
> DB2.

It is useful when we have customers who need access to some data - but is
certainly a security headache.   There is lots of data which we do not want
available on the World Wide Web.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-07-14T05:07:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030714010724.03537.00000321@mb-m05.aol.com>`
- **References:** `<bejt7h$bh4$1@peabody.colorado.edu>`

```
>From: "Howard Brazee" howard@brazee.net 
>Date: 7/10/03 10:29 AM Eastern Daylight Time

>
>It is useful when we have customers who need access to some data - but is
>certainly a security headache.   There is lots of data which we do not want
>available on the World Wide Web.
>

Intranet dear boy - intranet.  Perhaps I should have said 'web-a-fy'?  To the
best of my knowledge there is no interaction between the company and it's
customers via the web in place at all - except perhaps a button to send an
e-mail.
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-07-09T21:37:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beijhk$qel$1@slb9.atl.mindspring.net>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
I have "snipped" all of Pete's original note - not because I am arguing with
it or that I disagree with much/all of it - but because my note is INTENDED
to represent my understanding/experience in this area.

To start with, let me explain my IBM mainframe background (for readers who
aren't familiar with it already)

First I was an application programmer (CICS, IMS, etc) in a large Bank, then
in a large Utility.  For the utility (phone company) I started in
applications, because a trainer, and eventually became a Systems Programmer.

I then went to work for a "major" COBOL development tool company  (ADS when
they were the vendor for Xpediter) where I was "more or less" a product
manager.

Then I went to work for Micro Focus (pre-MERANT, pre-Micro Focus again).
For them I concentrated on "IBM mainframe compatibility issues - as well as
representing them on CODASYL and ANSI/J4.

From my ADS days on, I was an active member of GUIDE (IBM User Group) in the
COBOL and languages areas.

Since 1996, I have been on "long term disability".  Although this has meant
that I have had limited "hands on" experience with the last 7 years of IBM
mainframes, I have kept my "hands" (or at least my mind) in.

    ***

When working for both ADS and Micro Focus, it always surprised me how much
money large IT companies would spend on software tools that "sat on the
shelf" - as programmers weren't given time to learn how to use them
effectively or to integrate them into their normal development cycle.

As others have stated, it really does seem that "time and budget" are (have
always been and probably will continue to be) the DEMANDS upon IBM mainframe
programmers (COBOL or otherwise).  As business ARE in the business of
"business",  I don't think there is anything "inherently wrong" with this.
However, I do think that it sometimes (often?) leads to "penny wise and
pound foolish" management decisions.

Continuing education SHOULD be a part of any programmer's career.
Furthermore, it has been my experience that this is actually a MOTIVATING
factor when correctly integrated with other incentives (including the "way
too often missed" cost-free feature of ADEQUATE PRAISE for work well done.)

In most of the LARGE IBM IT departments that I knew in the '80s and '90s,
training, conferences, and other ongoing educational opportunities were
RELATIVELY common.  However, in the 90's, I did see a significant decrease
in this (corresponding with the demise of GUIDE - among other things).
Similarly, "code walk thrus" as a method of learning from other (both more
and less experienced) programmers was one of the BEST ways of learning new
and different techniques.  I would be very interested in hearing how many
large shops still do this?

For those working in large IBM mainframe shops, it was often true that the
TRADITIONAL "advancement path" was to get OUT of programming and into
"management" or the "business-side" of the company.  Certainly, this was a
significant detriment to encouraging ongoing learning and experimentation.
For those who DID want to stay "in programming", it seems to me that even
BEFORE the days of "out-sourcing", it was very common to move into
"contracting" and away from being an "internal IT professional".  As DD
(among others) have indicated USUALLY the highest priority for a "contract
programmer" is to follow the "style" (techniques) already present (and
probably "standard") within a shop.  Again, this is NOT going to encourage
"changes/advances" in programming techniques within an IBM mainframe shop.

    ***

Now for an underlying fact that really DOES impact what code is used in IBM
mainframe shops.

The simple fact is that most (almost all?) business applications that are
coded or maintained in an IBM mainframe environment COULD be done in '74
Standard COBOL with OS/VS COBOL extensions.  If you can accomplish what is
required using "old and familiar techniques", why change????  (I don't agree
with this - but I do see it as an underlying view in MANY shops.)  If you
aren't encouraged to learn new techniques, aren't given time or resources
for continuing education, and your annual evaluations are NOT based on the
code you produce - but whether you deliver on-time and on-budget, then
"Fortress COBOL" is clearly going to be a (least) "common" denominator.

Just as I believe that there ARE development tools that are worth the time
to learn, I also believe that using "newer" techniques often (certainly NOT
always) can provide long-range advantages (ease of maintenance, reduction of
errors, etc).

I may be mistaken, but I am unaware of significant documented research to
show that "newer" project management techniques and/or coding techniques are
actually sufficiently "cost-effective" to justify "culture changes" in large
IBM mainframe shops.  For 40 years (that I know of) there have always been
"silver bullets" that sounded good to management - for eliminating
development backlogs.  However, most large companies have been "burnt" too
many times to believe in the latest "theories".  I am *NOT* saying that
changes in coding and design techniques would NOT improve most shops - I
simply think that most of such shops don't believe it.

There are a "number" of studies (and/or rumors) of failures in moving from
IBM traditional "methodologies" and "techniques" to
 - client/server
 - non-Waterfall design
 - etc
(obviously, there are also success stories - but at least in most shops
these aren't all that common)

It is MY impression that most of these "failures" result from inadequate
training/planning coupled with unrealistic "goals". Similarly, whether true
or false, it is my impression that the MAJORITY (certainly NOT all) IBM
mainframe COBOL programmers see programming as a JOB, not a "profession".
Their interest in pursuing COBOL (or programming) outside 8-5 hours is
minimal.  (Thus the relatively small number of IBM mainframe COBOL
programmers actively participating in comp.lang.cobol.)

    ***

To conclude, this (depressingly negative) response to Pete's question is
just my PERSONAL opinion of the answer to what he is asking.  The GOOD news
is that within every "fortress" that I know of, there ARE some people who
want to and DO grow in their technical skills.  Similarly, just as "S/370
assembler programmers" became too scarce for common application development
a decade or so ago, I do foresee the days of "fortress COBOL" IBM mainframe
application developers being limited.  Either these programmers will need to
change - or the shops will move away from COBOL - or a combination of the
two.
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T01:07:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d65a0_4@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:beijhk$qel$1@slb9.atl.mindspring.net...
> I have "snipped" all of Pete's original note - not because I am arguing
with
> it or that I disagree with much/all of it - but because my note is
INTENDED
> to represent my understanding/experience in this area.
>
…[3 more quoted lines elided]…
> First I was an application programmer (CICS, IMS, etc) in a large Bank,
then
> in a large Utility.  For the utility (phone company) I started in
> applications, because a trainer, and eventually became a Systems
Programmer.
>
> I then went to work for a "major" COBOL development tool company  (ADS
when
> they were the vendor for Xpediter) where I was "more or less" a product
> manager.
>
> Then I went to work for Micro Focus (pre-MERANT, pre-Micro Focus again).
> For them I concentrated on "IBM mainframe compatibility issues - as well
as
> representing them on CODASYL and ANSI/J4.
>
> From my ADS days on, I was an active member of GUIDE (IBM User Group) in
the
> COBOL and languages areas.
>
> Since 1996, I have been on "long term disability".  Although this has
meant
> that I have had limited "hands on" experience with the last 7 years of IBM
> mainframes, I have kept my "hands" (or at least my mind) in.
…[7 more quoted lines elided]…
>

This seems to be a consistently emerging pattern.

> As others have stated, it really does seem that "time and budget" are
(have
> always been and probably will continue to be) the DEMANDS upon IBM
mainframe
> programmers (COBOL or otherwise).  As business ARE in the business of
> "business",  I don't think there is anything "inherently wrong" with this.
…[6 more quoted lines elided]…
> too often missed" cost-free feature of ADEQUATE PRAISE for work well
done.)
>

I am persuaded that underacknowledgement, lack of recognition, and reward
are instrumental in the growth of the Fortress mentality.

> In most of the LARGE IBM IT departments that I knew in the '80s and '90s,
> training, conferences, and other ongoing educational opportunities were
…[18 more quoted lines elided]…
>

Yes. However, part of the reason for outsourcing is to get fresh ideas and
techniques and do a "skills transfer" to the permies...

>     ***
>
> Now for an underlying fact that really DOES impact what code is used in
IBM
> mainframe shops.
>
…[3 more quoted lines elided]…
> required using "old and familiar techniques", why change????  (I don't
agree
> with this - but I do see it as an underlying view in MANY shops.)

I believe this was the nub of Joe's original observation. I don't do this
myself and it just never occurred to me that there are many others who
definitely DO feel this way. I guess you can't blame them.

> If you
> aren't encouraged to learn new techniques, aren't given time or resources
…[3 more quoted lines elided]…
>

Yes.

> Just as I believe that there ARE development tools that are worth the time
> to learn, I also believe that using "newer" techniques often (certainly
NOT
> always) can provide long-range advantages (ease of maintenance, reduction
of
> errors, etc).
>
> I may be mistaken, but I am unaware of significant documented research to
> show that "newer" project management techniques and/or coding techniques
are
> actually sufficiently "cost-effective" to justify "culture changes" in
large
> IBM mainframe shops.  For 40 years (that I know of) there have always been
> "silver bullets" that sounded good to management - for eliminating
…[4 more quoted lines elided]…
>

I agree. Anyone who has spent decades in the industry has seen it. We have
certainly watched things come and go. But that is no reason to become smug
and complacent. This time there is something there that IS important. It is
already revolutionising the way systems are developed. And it is a major
factor in the "sidelining" of the once great COBOL language. It's no good
saying, "Well, we've seen it all before and anyway, we have done pretty well
for years now...no need to do anything about it...".

"Shorthand" languages, using OO techniques are simply more productive in
time and maintainability than traditional procedural COBOL.

That's why they have become "fashionable".

But it isn't the Computer Scientists who will have the last word, it is the
Business.

They don't care about the technology, they just care about the results. The
"New Technology" delivers. In time scales that could only be dreamed of on
the Waterfall. (The DSDM foundation claim RAD/DSDM projects are implemented
on average 3.5 times faster than Waterfall; my own experience confirms this
and improves on it. And that's doing it with COBOL!).

Yet the Fortress clings to the Waterfall and fervently resists any deviation
from it.


> There are a "number" of studies (and/or rumors) of failures in moving from
> IBM traditional "methodologies" and "techniques" to
…[4 more quoted lines elided]…
> these aren't all that common)
" A Man hears what he wants to hear and disregards the rest..." Simon and
Garfunkle.

Yes again. This is the "Elders of the Church" rubbing their beards and
saying: "See, we told you what would happen if you departed from Holy Writ
and our Ancient Wisdom..." In the meantime they and the acolytes who wish to
win favour with them, are doing everything within their power to bring about
the downfall of the pilot project as covertly as possible <G>.

Been there, seen it...(It made me smile<G>).

Personally, I have never had a failure with non-Waterfall development (Even
despite "enemy action" <G>).

All I will say on this one is this: "No system can ever be "successfully
developed and implemented" (goes in on time and budget, meets or exceeds
requirements, and is still runing without serious change a year later), NO
MATTER WHAT methodology or technology you use, UNLESS people want it!"

If you can suspend the Fortress Mentality long enough to open some (possibly
atrophied) minds, you have a chance of changing things.

> It is MY impression that most of these "failures" result from inadequate
> training/planning coupled with unrealistic "goals".

And sometimes limited experience overbalanced by unlimited enthusiasm in the
people managing the project. Unrealistic goals are fine as long as they are
prioritised...<G>


>Similarly, whether true
> or false, it is my impression that the MAJORITY (certainly NOT all) IBM
…[4 more quoted lines elided]…
>

I was hoping that wasn't true.

>     ***
>
> To conclude, this (depressingly negative) response to Pete's question is
> just my PERSONAL opinion of the answer to what he is asking.  The GOOD
news
> is that within every "fortress" that I know of, there ARE some people who
> want to and DO grow in their technical skills.  Similarly, just as "S/370
> assembler programmers" became too scarce for common application
development
> a decade or so ago, I do foresee the days of "fortress COBOL" IBM
mainframe
> application developers being limited.  Either these programmers will need
to
> change - or the shops will move away from COBOL - or a combination of the
> two.
>

Your last statement is the more probable, although by no means inevitable in
the short/medium term. (in the long term, the demise of COBOL and procedural
programming in general is inevitable.There are new breakthroughs in the labs
at the moment that will revolutionise the computer industry by 2020)

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T14:40:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejtt1$c1t$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net> <3f0d65a0_4@news.athenanews.com>`

```

On 10-Jul-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> "Shorthand" languages, using OO techniques are simply more productive in
> time and maintainability than traditional procedural COBOL.
>
> That's why they have become "fashionable".

I don't thinks so.   They have become fashionable because management wants a new
web page and asks how to get it.  The IS department didn't have anybody who
knew, so they hired some kid who created a web page.   This process continues
until IS is split into the web side and the traditional side.   Tools adjust so
that the traditional side could now solve the new problems, but nobody gets
trained in these new tools, and the company doesn't pay for the upgrade, as it
already has people who can solve their problems.

They don't evaluate which tools are more productive in this process.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2003-07-11T01:53:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c3474f$235d2040$80caf943@chottel>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net> <3f0d65a0_4@news.athenanews.com>`

```
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in article
<3f0d65a0_4@news.athenanews.com>...
> 
<snip>

> All I will say on this one is this: "No system can ever be "successfully
> developed and implemented" (goes in on time and budget, meets or exceeds
> requirements, and is still runing without serious change a year later),
NO
> MATTER WHAT methodology or technology you use, UNLESS people want it!"
> 

I have worked on several projects which involved generating data containing
embedded typesetting commands. Sometimes it involved converting word
processing commands to typesetting commands, sometime it involved
converting to a different word processor system or a different typesetting
system. In each case at the beginning of the project the user proclaimed
the project to be "impossible". Of course they wanted it to be impossible
because they made lots of overtime converting this stuff by hand.
Management wanted to save money as well a produce the output in a more
timely manner.

At the end of the project afet the "impossible" has been accomplished I was
almost always told that while the typsetting commands that my program had
inserted worked "that is not the way a professional typesetter would have
done the job".
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T09:48:04-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejqqk$3nu$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net>`

```
In article <beijhk$qel$1@slb9.atl.mindspring.net>,
William M. Klein <wmklein@ix.netcom.com> wrote:

[snip]

>As DD
>(among others) have indicated USUALLY the highest priority for a "contract
>programmer" is to follow the "style" (techniques) already present (and
>probably "standard") within a shop.

zzzzZZZZzzzz.... zzzzaaaAAAWWWKKKHHHhhhh... huh? whuh?

>Again, this is NOT going to encourage
>"changes/advances" in programming techniques within an IBM mainframe shop.

I've been told, during interviews, that I will be expected to provide 
'knowledge transfer'; my response is usually 'I can try to teach, sure, 
but others will have to try to learn.'

Once on the job the situation becomes 'We do things This Way here'... and 
This Way works, after a fashion, and it ain't broke.  As noted, though, I 
am a consultant/contractor/hired gun and as such tend to see the insides 
of 'sick shops' more often than healthy ones.

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-10T20:37:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<H8kPa.47810$3o3.3252270@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net> <bejqqk$3nu$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bejqqk$3nu$1@panix1.panix.com...
|
| Once on the job the situation becomes 'We do things This Way here'... and
| This Way works, after a fashion, and it ain't broke.  As noted, though, I
| am a consultant/contractor/hired gun and as such tend to see the insides
| of 'sick shops' more often than healthy ones.

I prefer the term "Migrant Programmer".
And, you do get an education.
Nobody does everything right, and nobody does everything wrong (although
some do come close).
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T17:30:17-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beklt9$8rd$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net> <bejqqk$3nu$1@panix1.panix.com> <H8kPa.47810$3o3.3252270@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <H8kPa.47810$3o3.3252270@bgtnsc05-news.ops.worldnet.att.net>,
Harley <dennis.harleyNoSpam@worldnet.att.net> wrote:
>
><docdwarf@panix.com> wrote in message news:bejqqk$3nu$1@panix1.panix.com...
…[6 more quoted lines elided]…
>I prefer the term "Migrant Programmer".

Anybody remember Woodie Guthrie?

I've been a-hittin' some hard programmin', I thought you knowed,
I've been a-churnin' out passable code, 'way down the road,
Been a-watchin' some youngster show to
Code fifty lines to save on a GO TO
I've been a-hittin' some hard programmin', Lord!

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-07-10T22:38:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CVlPa.40615$C83.3196145@newsread1.prod.itd.earthlink.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net> <bejqqk$3nu$1@panix1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:bejqqk$3nu$1@panix1.panix.com...
> In article <beijhk$qel$1@slb9.atl.mindspring.net>,
> William M. Klein <wmklein@ix.netcom.com> wrote:
…[4 more quoted lines elided]…
> >(among others) have indicated USUALLY the highest priority for a
"contract
> >programmer" is to follow the "style" (techniques) already present (and
> >probably "standard") within a shop.
…[4 more quoted lines elided]…
> >"changes/advances" in programming techniques within an IBM mainframe
shop.
>
> I've been told, during interviews, that I will be expected to provide
> 'knowledge transfer'; my response is usually 'I can try to teach, sure,
> but others will have to try to learn.'
>

<SNIP>

I can empathize on that one.  I may talk, but if you aren't listening, then
no benefit is accruing to either of us.

Paul
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T14:36:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejtku$br6$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net>`

```

On  9-Jul-2003, "William M. Klein" <wmklein@ix.netcom.com> wrote:

> I may be mistaken, but I am unaware of significant documented research to
> show that "newer" project management techniques and/or coding techniques are
…[6 more quoted lines elided]…
> simply think that most of such shops don't believe it.

And it is not an easy sell at all to persuade them differently.   The way they
do get persuaded is via the back door.   Some new technologies have new
applications that gradually replace the old ones.

This approach doesn't lead to upgrading the COBOL programs.   It just means they
stop asking for us to provide "X" reports.
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Harley" <dennis.harleyNoSpam@worldnet.att.net>
- **Date:** 2003-07-11T01:54:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pNoPa.49616$3o3.3279041@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <beijhk$qel$1@slb9.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:beijhk$qel$1@slb9.atl.mindspring.net...
<<snip>>
|
| As others have stated, it really does seem that "time and budget" are
(have
| always been and probably will continue to be) the DEMANDS upon IBM
mainframe
| programmers (COBOL or otherwise).  As business ARE in the business of
| "business",  I don't think there is anything "inherently wrong" with this.
| However, I do think that it sometimes (often?) leads to "penny wise and
| pound foolish" management decisions.

I agree, and I think this extends to all activity in the IT Dept.
A totally server based application will be judged by the same yardstick.
It's not the hardware platform, it the fact that it is a business, and
managers have budgets, and they don't want to affect their bottom line.
Business seem to focus on the last year, or quarter, and future costs and
savings don't really enter into the equation.

| Continuing education SHOULD be a part of any programmer's career.
| Furthermore, it has been my experience that this is actually a MOTIVATING
| factor when correctly integrated with other incentives (including the "way
| too often missed" cost-free feature of ADEQUATE PRAISE for work well
done.)
|
| In most of the LARGE IBM IT departments that I knew in the '80s and '90s,
| training, conferences, and other ongoing educational opportunities were
| RELATIVELY common.  However, in the 90's, I did see a significant decrease
| in this (corresponding with the demise of GUIDE - among other things).

Corporate sponsorship isn't a requirement, to me it's more a matter of
individual responsibility. The Corporate Sponsored events were often seen as
paid time away from the office anyway. People who like what they do, and who
want to be better at it don't need prodding, they do it on their own.
(Give a class on Forth, and nobody will attend, but include a free lunch,
and the room will be at capacity.)

I don't think education is a motivating factor by itself, it has to be
coupled with the opportunity to apply what was learned.

| Similarly, "code walk thrus" as a method of learning from other (both more
| and less experienced) programmers was one of the BEST ways of learning new
| and different techniques.  I would be very interested in hearing how many
| large shops still do this?

From what I've seen this is usually a group, or individual initiative.
There are no policies that require it, and it's left to the discretion of
the manager in charge.
I have found test plan walk-thrus to be effective. You usually have people
sharing their knowledge of the system, and in the end you not only have a
better test plan but a better understanding of the system as a whole.

| For those working in large IBM mainframe shops, it was often true that the
| TRADITIONAL "advancement path" was to get OUT of programming and into
…[4 more quoted lines elided]…
| "contracting" and away from being an "internal IT professional".

The COBOL community has also lost talent to other languages (PowerBuilder,
VB, Delphi, etc.).
It isn't only staying in "programming" that attracts people to
"contracting", it's better pay, and shorter hours. Contractors may be
expected to work overtime, but only after the additional cost has been
approved. Unfortunately, some manager worked salaried people to death in
order to come in under budget.

|As DD
| (among others) have indicated USUALLY the highest priority for a "contract
| programmer" is to follow the "style" (techniques) already present (and
| probably "standard") within a shop.  Again, this is NOT going to encourage
| "changes/advances" in programming techniques within an IBM mainframe shop.

Again, this will depend on the others in the group.
In general, you have to talk about what you want to do, and see how it is
received.
Sometimes people are stuck in the past because they don't have a current
manual.
(You show them where the manual is on the Web, and then do what you want
while they're occupied.)
|
| Now for an underlying fact that really DOES impact what code is used in
IBM
| mainframe shops.
|
…[3 more quoted lines elided]…
| required using "old and familiar techniques", why change????  (I don't
agree
| with this - but I do see it as an underlying view in MANY shops.)

I think people want to change.
Go into a CICS group, and say you want to develop a web based application,
and need volunteers. Add that this will require lots of overtime, and
off-hours training sessions. I doubt that many will turn down the
opportunity. Some may grumble a bit, but they'll do it.

|If you
| aren't encouraged to learn new techniques, aren't given time or resources
| for continuing education, and your annual evaluations are NOT based on the
| code you produce - but whether you deliver on-time and on-budget, then
| "Fortress COBOL" is clearly going to be a (least) "common" denominator.

I see nothing wrong with on-time, on-budget, as long as on-time includes:
produces the correct output, and doesn't abend.
To me, it's on-time when it's installed, and running CORRECTLY.

To be honest it usually takes longer to code, and test poorly written code.

| Just as I believe that there ARE development tools that are worth the time
| to learn, I also believe that using "newer" techniques often (certainly
NOT
| always) can provide long-range advantages (ease of maintenance, reduction
of
| errors, etc).
|
| I may be mistaken, but I am unaware of significant documented research to
| show that "newer" project management techniques and/or coding techniques
are
| actually sufficiently "cost-effective" to justify "culture changes" in
large
| IBM mainframe shops.  For 40 years (that I know of) there have always been
| "silver bullets" that sounded good to management - for eliminating
…[3 more quoted lines elided]…
| simply think that most of such shops don't believe it.

I don't know.
I worked with a CASE tool that effectively doubled personnel costs.

|
| There are a "number" of studies (and/or rumors) of failures in moving from
…[5 more quoted lines elided]…
| these aren't all that common)

There is a difference between learning a technique, and using it
effectively.
People sometimes say or think they understand the concepts, but they don't,
and they fail when they try to use something they don't understand.
It isn't the techniqe, it's the people.
|
| It is MY impression that most of these "failures" result from inadequate
| training/planning coupled with unrealistic "goals". Similarly, whether
true
| or false, it is my impression that the MAJORITY (certainly NOT all) IBM
| mainframe COBOL programmers see programming as a JOB, not a "profession".
| Their interest in pursuing COBOL (or programming) outside 8-5 hours is
| minimal.  (Thus the relatively small number of IBM mainframe COBOL
| programmers actively participating in comp.lang.cobol.)

I agree, some do see it as just a job, and there is also a portion who are
incapable of doing anything complex. (Oops, same people).
I've never met a true technical leader who considered it to be just a job.
(There are 2 types of technical leaders; those who think they are a
technical leader, and those who others recognize as a technical leader).

| To conclude, this (depressingly negative) response to Pete's question is
| just my PERSONAL opinion of the answer to what he is asking.  The GOOD
news
| is that within every "fortress" that I know of, there ARE some people who
| want to and DO grow in their technical skills.  Similarly, just as "S/370
| assembler programmers" became too scarce for common application
development
| a decade or so ago, I do foresee the days of "fortress COBOL" IBM
mainframe
| application developers being limited.  Either these programmers will need
to
| change - or the shops will move away from COBOL - or a combination of the
| two.

The Assembler people I knew became COBOL programmers.
(Systems programmers don't get to program that much.)

I don't see a move away from COBOL anytime soon.
Businesses have a large investment in their systems, and the cost of change
will be a factor in any decision to replace existing systems.
If there is a move away from COBOL it would occur in the general accounting
systems first (G/L, A/P, A/R, Purchasing, Order Entry) since they are
usually packages, and the vendor has a large pool of potential customers. I
wonder how many jobs there are for JAVA programmers with G/L experience.
(Seriously, anybody know what the demand is?) If OO COBOL comes to the
mainframe, it will be through these same systems.
Systems aren't chosen because of pretty screens, web pages, combo boxes,
etc.
They are chosen because they address the needs of the user, and the user
determines what those needs are, and what user friendly means.
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-10T03:36:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0cd3b8.307599400@news.optonline.com>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
The reason for mainframers' resistance to change is a belief that evolution is
more reliable than revolution. Mainframers are instinctively averse to
revolutionary change because they've seen so many revolutions fail. An
evolutionist wants to change one thing at a time, then test it thoroughly to
make sure it works before going on to the next change. He doesn't want two
simultaneous changes because if it doesn't work, he doesn't know which change
caused the failure. When asked to change many things at once, he sees that as a
revolution. 

With users banging on his door demanding many changes, he needs a way to slow
them down. The waterfall is a way of foot-dragging while appearing
professional. 

What to do about it? Encapsulate likely targets of change. File IO provides a
good example. I suggested a callable access module per file. With that in place,
the file can be moved to a database by changing "one thing". Calling programs
need not be touched or even recompiled, if the call is dynamic. The systems can
be regression tested and found to work as before relatively quickly (with the
right tools). Compare that to having 100 FDs in 100 programs. To the
evolutionist, it appears you're asking him to change 100 things simultaneously.
He'll want to run a database that mirrors the indexed file, and treat each of
the 100 programs as a separate change.

OO can be introduced the same way. Suppose you want to change reports to come
out as Word documents. First encapsulate report writing as much as possible,
using structures similar to Word templates. Then change the single report writer
to invoke Word via OLE. You're only changing one thing at a time. 

The worst approach would be introducing a component library with hundreds of
classes. An evolutionist can only assimulate them one at a time. If he thinks,
rightly or wrongly, that he's expected to use them all immediately, he'll reject
the whole package. This is not speculation. He has BEEN rejecting the whole
package for twenty years. 

------- history below ---------------------------------------

"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>I'm starting this thread because of a post from Joe Zitzelberger which said
>the following:
…[114 more quoted lines elided]…
>
```

##### ↳ ↳ gradualism (was: Fortress COBOL - Why?)

- **From:** Patrick Herring <ph@anweald.co.uk>
- **Date:** 2003-07-10T12:44:51+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0D51B3.D3AA13AC@anweald.co.uk>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0cd3b8.307599400@news.optonline.com>`

```
Robert Wagner wrote:
> 
> The reason for mainframers' resistance to change is a belief that evolution
…[9 more quoted lines elided]…
> as a revolution.

I've tended to spell your "evolutionary" as "gradualist", but the
thought's the same.

I'm wondering if there's a name for the development structure I use for
my own projects. The system is conceived as answering particular
questions about certain types of data. I start with one answer to one
particular question, get some code that will do that, divide the code up
into modules in such a way that changing each module is independent,
then keep re-visiting each module to make it answer more and more
general questions. I stop when I don't need to make it more general.
That seems to be a classically gradualist approach, it's also really
fast to show some results and I've rarely found it requiring a big
re-write. 

Is this the same as the RAD technique?
```

###### ↳ ↳ ↳ Re: gradualism (was: Fortress COBOL - Why?)

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-07-10T17:36:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0d92d1.13978902@news.optonline.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3f0cd3b8.307599400@news.optonline.com> <3F0D51B3.D3AA13AC@anweald.co.uk>`

```
Patrick Herring <ph@anweald.co.uk> wrote:

>Robert Wagner wrote:
>> 
…[24 more quoted lines elided]…
>re-write. 

Your technique is called bottom-up design, aka induction, which derives the
general from specifics. The opposite is top-down design, aka deduction, which
derives specific conclusions from general principles. 

I design top-down and program bottom-up. I start with high-modules asking
general questions -- the ones which be answered when the product is finished.
The low level logic is initially stubbed out, so all answers return 'unknown' or
a hard-coded test value. I call that the design phase. Then I switch to
programming mode, in which I do the same as you described -- answering specific
questions and observing the result _at the top level_. Alternating between
design mode and programming mode, all the stubs are eventually replaced with
working code. 

If I discover a more general question that I failed to anticipate, I glue an
additional top layer above the formerly topmost, with a parallel branch below
it. A good principle is to avoid changing working code, because I might
inadvertently break something that used to work. Instead, glue an additional
bump on the log to handle the new condition, leaving the formerly working
intact. I think of it as a poor man's overloading. 

>Is this the same as the RAD technique?

No. RAD glues existing components together. It can be multi-level i.e. some
components can themselves be RAD-developed, but it is essentially top-down. 
Your approach is bottom-up through the use of modules. If your modules were
generalized enough to be reusable, you'd have RAD.
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** "Douglas Gallant" <no@spam.net>
- **Date:** 2003-07-10T10:56:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KDbPa.26967$EQ5.7440@twister.nyroc.rr.com>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
I think my site qualifies by some of Pete's requirements and I've actually
communicated some or all of this to him before some time ago. However, a
recap may be useful.
First, a little site background. We are a large government agency using
Unisys Clearpath IX systems (formerly the 2200 and 1100 series hardware). We
run sizeable transaction volumes - ~3 million/day on one system and ~1+
million/day on another (but with a heavy MAPPER load as well) and have a
third for development work.
Reasons for Fortress-like behavior:
1) Historical based on platform. When the system was first being developed
in the late 70's, there was a decision made to utilize a non-standard (i.e.
in-house) terminal protocol for driving screens. This one decision has
probably had the most far-reaching impact on subsequent development work
that I have seen. In short, it prevented us from using any standard screen
technology, from Unisys or anyone else, either within the application or
even standard PC terminal emulation packages. This has only been completely
addressed, at least from the emulation perspective, in the past 2 years.
2) Technical, somewhat related to #1. Moving from the 1974 compliant
compiler (ACOB) to the 1985 compliant compiler (UCOB) is more than just a
recompile. Unisys changed the whole program execution environment.
Compiling, linking, dumps, etc were all changed. Most of those were
manageable but the big problem was that the way our transactions were coded,
in part due to issue #1, was unsupported in the newer compiler. You were
forced to upgrade to the standard Unisys DPS product to do screen handling.
(Actually it is a bit more complex than that but I'm trying to keep things
simple.) Doing that upgrade is good for a number of reasons but does result
in significant application changes and testing (all costing time and money
that we don't have). This results in batch programs being the only easy
ports and even then there can be a few gotchas.
3) Developer ignorance/apathy. (What's the difference between ignorance and
apathy? I don't know and I don't care.) Aside from the technical issues this
is probably the biggest issue. When I tried to get things moving for the
site to support the 85 compiler (about 1995) very few of the developers even
knew there was a new COBOL standard. (None, except for those I've told, are
aware of the 2002 standard.) Most still fail to see the benefit of simple
things like END-IF so have little motivation to consider the upgrade.
4) Upper managment. To varying degrees have bought into the COBOL is bad,
mainframes are bad arguments. In general, the less technical they are the
more they believe these stories. We are actively looking to "modernize" our
primary application by completely rebuilding it (looks like java, WebSphere,
a specialized framework product, etc.). [There are some valid reasons for
doing this because the legacy app does not necessarily meet our needs
anymore and maintenance is increasing difficult.]

There are other bits and pieces of course but I think that covers the high
points.


"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f0cb232_6@news.athenanews.com...
> I'm starting this thread because of a post from Joe Zitzelberger which
said
> the following:
>
…[14 more quoted lines elided]…
> If we can understand the reasons for it, it may be possible to do
something
> about it.
>
> Pete.
>
>
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** "paul" <paulpigott@earthlink.net>
- **Date:** 2003-07-10T10:58:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1FbPa.39432$C83.3132454@newsread1.prod.itd.earthlink.net>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
As a 20+ year mainframe programmer, recently moved to client/server (though
maintaining my mainframe roots as a SME), I'd like to insert my 2 cents.

I've read the posted responses, and I see the inherent truth in the majority
of them.

Yes, there does seem to be an entrenched fear among many mainframers of
moving to a new technology.  This applies to both staff and management.

One poster referred to PCs as being "...treated like tinker toys by their
biggest proponents. If some software on them fails, re-boot the system. Easy
to violate and cause problems -- just look at Micro
$**t's software."  And I've seen that too.  Mainframes however are expected
to be up 24x7, with perhaps an hour here or there for maintenance (usually
at Saturday, midnight).  And when your review depends on how good your
uptime is, Client/Server may seem woefully inappropriate.

The "Fortress" mentality appears to be the result of a conservative bent in
large corporations that implicitly says "We are not going to screw up our
systems".  What can be done about it?  Inside the Fortress, it's already
happening to some degree, as new tools and techniques make inroads.  After
all, even the strongest medieval castle weathers and disolves away given
enough time.

Those inside the Fortress can hurry the process along by demanding the same
kind of uptime as the mainframe can deliver.  Don't treat the PCs and
Servers like "tinker toys".  Unless it's the PC on your desk, don't
arbitrarily update, change, modify, insert, or delete code on the box "just
to see what will happen".  That way madness lies.  Never forget that there
are customers out there who rely on those systems.  Maybe they reside down
the hall, or maybe on the other side of the world, but they want the system
available when they need it.  It is the CUSTOMER'S system.  The programmer
is merely the STEWARD of that system.  The system is not, can not, should
never be, a programmer's play toy.

Unless you code for Nintendo of course.

Paul


"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3f0cb232_6@news.athenanews.com...
> I'm starting this thread because of a post from Joe Zitzelberger which
said
> the following:
>
…[12 more quoted lines elided]…
> I first coined this term a couple of years ago when I was writing about
the
> extreme entrenched resistance on many mainframe sites to the new features
in
> COBOL. (I wish I could say the same occurs on non-mainframe sites, to make
> it sound more balanced, but the fact is that theren't a lot of
non-mainframe
> COBOL sites I know of, and those I have seen are much more into experiment
> and change (and are familiar with and glad to use "standard" software and
> tools as well as COBOL) and simply don't have the "fortress" mentality.)
It
> bothered me especially that there was (and still is) strong resistance to
> the use of Object Oriented Programming, even though COBOL now supports it.
…[3 more quoted lines elided]…
> Because I could see that the future of programming is in OO. (It ISN'T
just
> another "fad" that would be fashionable for a while then disappear. It
> represents a real advance in the art of programming and has been eagerly
…[3 more quoted lines elided]…
> components, and this is quietly and quickly revolutionising the way
computer
> systems are developed and businesses are supported by IT.(I believe this
> will bring about the demise of Procedural programming as we understand it,
> but that is another story...)
>
> It is like a horde of Barbarians riding fast little ponies and capturing
the
> outposts that stand in their way.They didn't fight "fair" in the
"accepted"
> way of doing battle, they simply overran the defence while the defenders
> were implementing their "Standard Operating Procedure for attacks on our
> Authority"  In many cases the defenders simply adopted the Barbarian
culture
> and started breeding their own fast little ponies... Many found that,
> although this was a different culture, it was exhilarating and fun.
> Also, instead of keeping the peasants in Serfdom, dependent on the
goodwill
> of the Lord of the Manor, the Barbarians actually embraced the peasants
and
> liberated them towards independence and self sufficiency in things IT...
>
…[7 more quoted lines elided]…
> where each phase is signed off before the next one can start. (Not
suitable
> for fast ponies, rather Clydesdale war horses...). Fortress sites see no
> requirement to change this or even experiment with alternative
…[3 more quoted lines elided]…
> closed, and ensures that a new COBOL program must be written every time
you
> need a report...("We've always used ISAM, VSAM, for random access and our
> systems work fine; why would we need a Database and have to acquire new
…[3 more quoted lines elided]…
> WITHOUT the need to get IT to develop COBOL report programs for them...)
As
> at least one poster mentioned, most sites (even Fortress ones) have now
been
> dragged kicking and screaming into Relational technology.(I can smile now
at
> the extreme resistance I encountered right here in CLC when I first
started
> suggesting that maybe the COBOL file system was not a good option for the
> future...).
…[6 more quoted lines elided]…
> the peasants threaten revolt unless they get GUI, ensure that whatever
they
> get will be awful, will take a long time to develop, and will NEVER be as
> good as if they had let us use CICS with native 3270. Colour is just
> confusing, and graphics are for children and geeks...).
>
> 5. Don't use anything in COBOL that is subsequent to 1985, or requires
more
> than one line to write.
>
…[13 more quoted lines elided]…
> find at least ONE bright eyed bushy tailed programmer who "wants to know"
on
> most sites. Do they get the "yearning for learning" knocked out of them by
> dim-witted managers and surly colleagues?)
…[7 more quoted lines elided]…
> If we can understand the reasons for it, it may be possible to do
something
> about it.
>
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-10T09:55:27-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejr8f$6tl$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <1FbPa.39432$C83.3132454@newsread1.prod.itd.earthlink.net>`

```
In article <1FbPa.39432$C83.3132454@newsread1.prod.itd.earthlink.net>,
paul <paulpigott@earthlink.net> wrote:

[snip]

>The "Fortress" mentality appears to be the result of a conservative bent in
>large corporations that implicitly says "We are not going to screw up our
>systems".

In a different posting I mentioned that departments do noe exist in a 
vacuum, that they reflect and incorporate behaviors in the organisations 
of which they are a part.  The above seems to echo this... an organisation 
exists in order to Make Money.  The organisation depends on DP/IS/MIS 
systems in order to make and keep track of money.  If the ability to make 
and/or keep track of money is compromised then folks might well find 
themselves out of their jobs.  That which might run one out of a job is, 
quite frequently, approached with extreme caution.

DD
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-10T14:13:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bejs9f$b61$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```

On  9-Jul-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> 2. Root your Applications in the COBOL file system, which is completely
> closed, and ensures that a new COBOL program must be written every time you
> need a report...("We've always used ISAM, VSAM, for random access and our
> systems work fine; why would we need a Database and have to acquire new
> skills to use it?"

I don't see that whatever the "COBOL file system" is, is completely closed.

I don't know of any COBOL shops that don't use databases.

I also don't know of any COBOL shops that don't take PCs seriously.
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-07-10T11:53:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FMGcnVA3TfhqBJCiXTWJkw@giganews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <bejs9f$b61$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  9-Jul-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
…[7 more quoted lines elided]…
> closed.

Me either. Everybody uses text files, for example.

>
> I don't know of any COBOL shops that don't use databases.

Me either. Kinda hard to run a data processing center without data.

>
> I also don't know of any COBOL shops that don't take PCs seriously.

Sure. And many of them know a "mainframe" is the most expensive peripheral
one can attach to a PC.
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** Pat Hall <phall@certcoinc.com>
- **Date:** 2003-07-10T12:56:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0DA8BF.4E5A726B@certcoinc.com>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
I guess I am a "fortress" shop.  I've been here for 29 years.  I am the only
applications programmer.  When the operator goes on vacation I'm the operator.
When the dept manager who has been here 33 years goes on vac I'm him.  So for
the last 29 years I've mentioned that I really ought to go to a class or
something to "update" my skills.  They did send me to a class in 1998 to get up
to speed on intrinsic functions to correct our Y2K problem.  So the problem is
we are always too busy to send me off for a week or two. The operator has been
here 40 years.  So since I can't be gone while the operator is on vac., she gets
4 weeks a year, and I can't be gone when the  mgr is on vac, he gets 4 weeks a
year, and I want to take my 4 weeks each year......lets see that whacks 12 weeks
out of the year and since a lot of the vac is taken a day or two at a time it
sucks up even more weeks.  Soooo I can't seem to get away to take any classes to
update my skills.  But now they are finally seeing the light.  They have
purchased  some new software for the AS400,  we are also running a mainframe,
and are looking at another package.  I'm finally getting to take a course.  They
bought a "learn on the PC" course so I won't have to leave the office.  Now I
get to try and "shoe horn" a course in at the rate of about 30 minutes a week
and that is usually interrupted 3 or 4 times.  But the good news is after 29
years or writing COBOL and complaining about not getting my skills updated they
bought me a course in RPG.  ROFL  By the time I learn it I should be
retired<G>.   So sometimes "fortress" shops just seem to develop of their own
accord because of "Circumstances".  I can see how I got to be a "Fortress"  but
I'm not too sure I can see how I could have changed much.  Bottom line is I
really like my job and I'm not too concerned about being a "Fortress"  the work
gets done and I'm still getting paid.  I have a pretty low pressure job and I'm
fairly familiar with all the code run on our mainframe<G>.  Lets me shoot pool 4
or 5 times a week too.

Pat

"Peter E.C. Dashwood" wrote:

> I'm starting this thread because of a post from Joe Zitzelberger which said
> the following:
…[112 more quoted lines elided]…
> Pete.
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Donald Tees" <Donald_Tees@sympatico.ca>
- **Date:** 2003-07-10T16:52:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xokPa.16819$Tx.815108@news20.bellglobal.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com>`

```
"Pat Hall" <phall@certcoinc.com> wrote in message
news:3F0DA8BF.4E5A726B@certcoinc.com...
> I guess I am a "fortress" shop.  I've been here for 29 years.  I am the
only
> applications programmer.  When the operator goes on vacation I'm the
operator.
> When the dept manager who has been here 33 years goes on vac I'm him.  So
for
> the last 29 years I've mentioned that I really ought to go to a class or
> something to "update" my skills.  They did send me to a class in 1998 to
get up
> to speed on intrinsic functions to correct our Y2K problem.  So the
problem is
> we are always too busy to send me off for a week or two. The operator has
been
> here 40 years.  So since I can't be gone while the operator is on vac.,
she gets
> 4 weeks a year, and I can't be gone when the  mgr is on vac, he gets 4
weeks a
> year, and I want to take my 4 weeks each year......lets see that whacks 12
weeks
> out of the year and since a lot of the vac is taken a day or two at a time
it
> sucks up even more weeks.  Soooo I can't seem to get away to take any
classes to
> update my skills.  But now they are finally seeing the light.  They have
> purchased  some new software for the AS400,  we are also running a
mainframe,
> and are looking at another package.  I'm finally getting to take a course.
They
> bought a "learn on the PC" course so I won't have to leave the office.
Now I
> get to try and "shoe horn" a course in at the rate of about 30 minutes a
week
> and that is usually interrupted 3 or 4 times.  But the good news is after
29
> years or writing COBOL and complaining about not getting my skills updated
they
> bought me a course in RPG.  ROFL  By the time I learn it I should be
> retired<G>.   So sometimes "fortress" shops just seem to develop of their
own
> accord because of "Circumstances".  I can see how I got to be a "Fortress"
but
> I'm not too sure I can see how I could have changed much.  Bottom line is
I
> really like my job and I'm not too concerned about being a "Fortress"  the
work
> gets done and I'm still getting paid.  I have a pretty low pressure job
and I'm
> fairly familiar with all the code run on our mainframe<G>.  Lets me shoot
pool 4
> or 5 times a week too.
>
> Pat


Now all you need is that table in your office. <G>.  I figure a snooker
table and a decent piano in the office are minimums for inovative code ...

On a more serious note, I think one of the greatest factors in the
"fortress" mentallity is lack of new work ... or at the least a
preponderance of maintenance over new code.

I have heard it stated in here many times, often by the same people that
bemoan the lack of new techniques, that if one is maintaining code then one
should attempt to retain the style of the original ... always provided that
the style is not so poor as to be impossible to read. I also tend to agree
with that.  Bouncing around in a system from one style to another is error
prone ... you cannot trust the standard because there are a dozen different
ones all competing in the same program.

I've been lucky ... developing commercial products and maintaining them
forces a shop to limit the lifestyle of a product, or completely re-write it
every decade or so. New standards and techniques CAN be implimented during
such major re-writes and major re-structuring, but without them I am not
sure they are justified. That is not a "fortress" mentality, but simple
fiscal sense.

Donald
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** Pat Hall <phall@certcoinc.com>
- **Date:** 2003-07-11T06:49:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0EA467.8448B0F2@certcoinc.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com> <xokPa.16819$Tx.815108@news20.bellglobal.com>`

```
Hell If I had a snooker table in my office like some people I'd get no work done
at all.  I'll settle for a few nights a week out banging balls.  Last night was
very good for me on the pool table. But alas today and all next week the
operator is on vaction so I get to spend a few days on my feet .  But the up
side is I can say to the users "How the hell should I know I'm just the
operator"  LOL

PatH... who is wondering if operators can still post to this board or if I need
to take a sabatical

Donald Tees wrote:

> "Pat Hall" <phall@certcoinc.com> wrote in message
> news:3F0DA8BF.4E5A726B@certcoinc.com...
…[75 more quoted lines elided]…
> Donald
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-07-11T06:40:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JZsPa.49837$3o3.3304649@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com>`

```

Pat Hall <phall@certcoinc.com> wrote in message
news:3F0DA8BF.4E5A726B@certcoinc.com...

> I've been here for 29 years.  I am the only applications programmer.
> When the dept manager who has been here 33 years goes on vac I'm him.
> The operator has been here 40 years.

Your company is a tragedy away from a calamity.

Or is there also a company rule that the 3 of you
cannot go out to lunch together?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T22:23:43+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0e90c7_9@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com> <JZsPa.49837$3o3.3304649@bgtnsc05-news.ops.worldnet.att.net>`

```

"Hugh Candlin" <no@spam.com> wrote in message
news:JZsPa.49837$3o3.3304649@bgtnsc05-news.ops.worldnet.att.net...
>
> Pat Hall <phall@certcoinc.com> wrote in message
…[10 more quoted lines elided]…
>
Or travel in the same car <G>?

Pete.
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

- **From:** Pat Hall <phall@certcoinc.com>
- **Date:** 2003-07-11T06:45:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3F0EA34B.F29E6AB4@certcoinc.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com> <JZsPa.49837$3o3.3304649@bgtnsc05-news.ops.worldnet.att.net>`

```
Close but then to quote the great DD.  "I'se just a COBOL codin fool" or
something like that.  I'm sure management is aware of the situation but I
don't have a lot of control over it.

PatH

Hugh Candlin wrote:

> Pat Hall <phall@certcoinc.com> wrote in message
> news:3F0DA8BF.4E5A726B@certcoinc.com...
…[8 more quoted lines elided]…
> cannot go out to lunch together?
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T09:48:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemf6j$qgt$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com> <JZsPa.49837$3o3.3304649@bgtnsc05-news.ops.worldnet.att.net> <3F0EA34B.F29E6AB4@certcoinc.com>`

```
In article <3F0EA34B.F29E6AB4@certcoinc.com>,
Pat Hall  <phall@certcoinc.com> wrote:
>Close but then to quote the great DD.  "I'se just a COBOL codin fool" or
>something like that.

zzzzZZZZZZzzzzz.... zzzznnnNNNUURRRGGGGHHhhhh... whuh? huh? Did some, I 
say did somebody mention my name?

>I'm sure management is aware of the situation but I
>don't have a lot of control over it.

Actually, you do... but everyone seems satisfied with the situation ('the 
snake hasn't bitten anybody yet') and looking at it plainly might cause a 
bit of discomfort.  People can readily hold contradictory views; consider

'Our people are happy here, you couldn't pay them enough to work someplace 
else.'

... with ...

'Every person has their price.'

DD
```

###### ↳ ↳ ↳ Re: Fortress COBOL - Why?

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-07-11T14:19:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemh1s$ord$1@peabody.colorado.edu>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com> <JZsPa.49837$3o3.3304649@bgtnsc05-news.ops.worldnet.att.net> <3F0EA34B.F29E6AB4@certcoinc.com> <bemf6j$qgt$1@panix1.panix.com>`

```

On 11-Jul-2003, docdwarf@panix.com wrote:

> 'Our people are happy here, you couldn't pay them enough to work someplace
> else.'
…[3 more quoted lines elided]…
> 'Every person has their price.'

Their price must be more than I could pay.   8^)
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-07-11T22:28:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3f0e91fa_2@news.athenanews.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <3F0DA8BF.4E5A726B@certcoinc.com>`

```
Thanks for a refreshing post, Pat.

It made me smile but I can see how the situation could arise.

(Actually, I fell about when they offered you RPG...LOL!)

The good thing is that you enjoy working there and take it all in your
stride...<G>.

I don't think it qualifies as "Fortress", more like "barricaded" against
change...(or even anything resembling good sense...<G>)

Pete.


"Pat Hall" <phall@certcoinc.com> wrote in message
news:3F0DA8BF.4E5A726B@certcoinc.com...
> I guess I am a "fortress" shop.  I've been here for 29 years.  I am the
only
> applications programmer.  When the operator goes on vacation I'm the
operator.
> When the dept manager who has been here 33 years goes on vac I'm him.  So
for
> the last 29 years I've mentioned that I really ought to go to a class or
> something to "update" my skills.  They did send me to a class in 1998 to
get up
> to speed on intrinsic functions to correct our Y2K problem.  So the
problem is
> we are always too busy to send me off for a week or two. The operator has
been
> here 40 years.  So since I can't be gone while the operator is on vac.,
she gets
> 4 weeks a year, and I can't be gone when the  mgr is on vac, he gets 4
weeks a
> year, and I want to take my 4 weeks each year......lets see that whacks 12
weeks
> out of the year and since a lot of the vac is taken a day or two at a time
it
> sucks up even more weeks.  Soooo I can't seem to get away to take any
classes to
> update my skills.  But now they are finally seeing the light.  They have
> purchased  some new software for the AS400,  we are also running a
mainframe,
> and are looking at another package.  I'm finally getting to take a course.
They
> bought a "learn on the PC" course so I won't have to leave the office.
Now I
> get to try and "shoe horn" a course in at the rate of about 30 minutes a
week
> and that is usually interrupted 3 or 4 times.  But the good news is after
29
> years or writing COBOL and complaining about not getting my skills updated
they
> bought me a course in RPG.  ROFL  By the time I learn it I should be
> retired<G>.   So sometimes "fortress" shops just seem to develop of their
own
> accord because of "Circumstances".  I can see how I got to be a "Fortress"
but
> I'm not too sure I can see how I could have changed much.  Bottom line is
I
> really like my job and I'm not too concerned about being a "Fortress"  the
work
> gets done and I'm still getting paid.  I have a pretty low pressure job
and I'm
> fairly familiar with all the code run on our mainframe<G>.  Lets me shoot
pool 4
> or 5 times a week too.
>
> Pat
>
<snipped my own original post>
```

#### ↳ Re: Fortress COBOL - Why?

- **From:** "anon" <no@no.com>
- **Date:** 2003-07-11T05:43:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<U7sPa.54129$ZS3.5873509@news2.telusplanet.net>`
- **References:** `<3f0cb232_6@news.athenanews.com>`

```
I've seen it at 2 client sites so far this year:  managers with 10-20+ years
of legacy experience (and no OO, and/or web-services knowledge) "don't get"
a lot of the newer technology.  My current client expects to send their
COBOL staff to Java night-school and have them come out writing J2EE
applications <boggle>.

"Technology is the easy part".  I've heard this way too much recently.  It's
even some catch-phrase on an ad.

The current COBOL staff at my client-site a) are not smart enough to pick up
OO theory or n-tier technology theory (hell, they don't even know what
client-server really means); b) don't care about new tech because they "have
a job with a lot of seniority and won't be fired", or c) are fooling
themselves into thinking that having 10-20+ years of experience in something
means it will never be invalid or useless (ie: ego-shattering).

You said in your post something to the effect that  "computer programmers
aren't stupid".  Well I'm going to say this:  you don't have to be smart to
learn COBOL, JCL or VSAM.   On the other hand, you have to have your fair
share of brain cells to pick up even the most basic best practices and
patterns of OO technology ala the gang of 4... and that's just to be a
certified programmer.

To get away from your Fortress effect, "the stuck ones" are going to have to
leave the industry and/or embrace the fact that programmatic solutions today
are more complicated to design -- even if they aren't inherently more
complicated to code.

--ANON
```

##### ↳ ↳ Re: Fortress COBOL - Why?

- **From:** docdwarf@panix.com
- **Date:** 2003-07-11T09:52:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bemff7$sgi$1@panix1.panix.com>`
- **References:** `<3f0cb232_6@news.athenanews.com> <U7sPa.54129$ZS3.5873509@news2.telusplanet.net>`

```
In article <U7sPa.54129$ZS3.5873509@news2.telusplanet.net>,
anon <no@no.com> wrote:

[snip]

>"Technology is the easy part".  I've heard this way too much recently.  It's
>even some catch-phrase on an ad.

'Oh good!  I'll be generous, then, and let you do *all* the 'easy' work; 
by the time you come back with a technological solution that is 
economically feasible I will have addressed all the management issues.'


(That's a *lot* nicer than my initial response of 'So... what you're 
telling me, then, is that you are so *stupid* that you cannot do 'easy' 
work, right?')
 
DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
