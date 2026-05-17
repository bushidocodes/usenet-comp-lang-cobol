[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (OT) Software License Contracts and Trade Secrets

_16 messages · 6 participants · 2014-11 → 2014-12_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs)

---

### (OT) Software License Contracts and Trade Secrets

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2014-11-20T15:17:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com>`

```
All -

I have a couple of examples of clauses in contracts between U.S. Counties and a vendor providing 911 / Emergency Computer Aided Dispatch (CAD, but not to be confused with Computer Aided Design) software. Such software is used to dispatch and direct emergency responders such as police, fire, and ambulance to those in need.

Consider these two examples:

County One -

"Customer may not distribute any of the Documentation for use outside of Customer's primary place of business except to the extent required by law, including the Georgia Open Records Act. Vendor hereby asserts that its user documentation and training manuals are trade secret information of vendor and should not be disclosed under the Georgia Open Records Act. Vendor will provide Customer with an affidavit regarding such trade secret information."

County Two -

"Customer may not distribute any of the Documentation for use outside Customer's Dispatch Center."

Note that the first example is explicit in justifying the restriction as protection of trade secrets. Note also that the second example is even more restrictive location-wise than the first - circulation of materials is confined to one building, and probably one room.

Seeing as how these restrictions apply to overt behaviors of the system, presumably the user interface, and the visible manifestation of how the system appears to its users, and is NOT referring to software source, technical architecture, database specifications, interface definitions, or the like, it seems to me that is is egregiously overly-restrictive.

Consider also that in Example Two, the County did not even issue a formal RFP (Request for Proposal) with accompanying list of "required features" on how the system is intended to perform. How could anyone outside the dispatch center even inform himself as to how the system should perform, let alone validate that it indeed is performing as it should?

By the way, the purchase price for software such as this for counties with population on the order of 100,000 - 200,000 is between $600K and $1.5M, with annual maintenance fees of another $100K - $200K a year.

All comments appreciated!

Thanks,
Ken
```

#### ↳ Re: (OT) Software License Contracts and Trade Secrets

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-11-21T10:06:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com>`

```
In article <9a45b0cc-7653-43fd-85e8-377··a@goo··s.com>,
Ken wrote:
› All -
› 
…[16 more quoted lines elided]…
› secret information."

I am not a lawyer. When an emergency occurs which requires co-ordinating
between, say, State and County personnel, the following would be illegal:

State Agency Liason: 'Our people will be on-site soon. What frequency
does the dispatch office use for mobile communications?'

County Liason: 'Hang on... (pages flipping) ... the documentation says
we're on (umble mumble) (wiggoHertz).'

Making this illegal would appear to render the product unfit for its
intended purpose, ergo absurdum est.

›
› County Two -
›
› "Customer may not distribute any of the Documentation for use outside
› Customer's Dispatch Center."

I am not a lawyer. When there is an emergency (fire, flood, blizzard,
rain of frogs) which renders the Dispatch Center unfit for use the
Documentation cannot be moved to a lawfully-declared Auxilliary Dispatch
Center, rendering the product unfit for its intended purpose, ergo
absurdum est.

Someone In Authority would do well to whisper to the vendor 'We need to
get rid of this restriction before we buy... is your code as well-written
as your boilerplate?'

DD
```

##### ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2014-11-21T10:20:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p2@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p2@usenetarchives.gap>`

```
Well, when the User Documentation is a trade secret, and the procuring authority did not bother to write a Statement of Work or a Required Features list in its solicitation, it does become rather easy for the vendor to respond to all complaints with a simple "It works as specified!" :-)

As startling coincidence, the City's IT Director, said City having entered into an Interlocal Agreement with said County for said replacement E911 system, and as such bears at least a trifling shared responsibility for seeing that the "combined" system works, currently serves also as a County Councilman and is considering running for Mayor.

Me thinks he should have spent a little less time politickin' and a little more time helping his IT worker bees write a User Acceptance Test.

Stay tuned...

Ken, the Journeyman
```

#### ↳ Re: (OT) Software License Contracts and Trade Secrets

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-12-05T18:08:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com>`

```
Ken wrote:
› All -
› 
…[47 more quoted lines elided]…
› All comments appreciated!

OK, I'll comment... :-)

My first thought on reading this was that I should be writing such software
but I managed to restrain myself by looking again at the things I am
currently doing :-)

Such vital software should be more freely available but instead (probably
because it IS vital software) they are charging like a wounded bull for it.

So, why the secrecy and concern in case someone finds out something about
it?

Wouldn't you feel better knowing that the Emergency servces had free and
instant access to the software manuals and had been properly trained in it
in the first place?

(There is little point in training people then denying them access to
reference sources...)

It has to be fear that their competitors will gain some insight into the
features of their software and they could lose some competitive advantage.

Indicative of an attitude.

Wouldn't you think they would be screaming the amazing features they have
from the rooftops? (Or, at the very least, have overviews and demos of
their software online, with the manuals downloadable for all interested
parties.)

Doc has already covered the absurdity of this in terms of people at the coal
face trying to use it, but the really sad thing is they get away with it.

A county with 100,000 people pays $6 for every man, woman and child to have
a product that nobody is allowed to talk about or evaluate, but which they
HAVE to have.

God Bless America.

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

- **From:** "bill" <ua-author-14191366@usenetarchives.gap>
- **Date:** 2014-12-06T12:48:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p4@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap>`

```
In article ,
"Pete Dashwood" writes:
› Ken wrote:
›› All -
…[57 more quoted lines elided]…
› because it IS vital software) they are charging like a wounded bull for it.

Like any product, the cost is a two sided argument. The owner asks for
a certain amount and the buyer either pays it or finds another product.
If they wree " charging like a wounded bull for it" why didn't the buyer
go elsewhere?

›
› So, why the secrecy and concern in case someone finds out something about
› it?

Yeah, like their competitors. These are very competitive businesses and
one need to protect any advantages they may accomplish.

›
› Wouldn't you feel better knowing that the Emergency servces had free and
› instant access to the software manuals and had been properly trained in it
› in the first place?

Like any other product, it's not your feelings that matter. Wouldn't
you feel better if you had access to the sources for Windows? :-)

But on a more realistic note, ever do any reading about voting machines?
Wouldn't you think that someone, other than the company that sells it,
should be able to see how it works? But, no, it doesn't work like that.

› 
› (There is little point in training people then denying them access to 
…[3 more quoted lines elided]…
› features of their software and  they could lose some competitive advantage.

Not fear, it's just business. And, if you are doing work for sale to the
government, it is very competitive and you need to protect any advantage
you may have. Or decide to get out of the business.

›
› Indicative of an attitude.

Not an attitude, a business maodel. The same one that all the players in
that domain follow.

› 
› Wouldn't you think they would be screaming the amazing features they have 
› from the rooftops?  (Or, at the very least, have overviews and demos of 
› their software online, with the manuals downloadable for all interested 
› parties.)

Why? They aren't selling to the public. They are selling to a psecific
market with a very specific way of doing business and it does not involve
shopping on the Internet.

›
› Doc has already covered the absurdity of this in terms of people at the coal
› face trying to use it, but the really sad thing is they get away with it.

They "get away" with nothing. The terms of the contract are knownw by
all relevant parties before the sale is completed. The buyer has seen
the conditions of the sale and agreed to them. If these restrictions
are considered unacceptable, then they should not have accepted the
contract.

›
› A county with 100,000 people pays $6 for every man, woman and child to have
› a product that nobody is allowed to talk about or evaluate, but which they
› HAVE to have.

They don't "HAVE to have" that particular product. If the terms are
unacceptable don't accept them and buy from someone else. Unless,
there really aren't any alternatives.

›
› God Bless America.

I agree. But then I am not being sarcastic.

bill

Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
bil··9@cs.··n.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-12-08T23:15:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p5@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap>`

```
Bill Gunshannon wrote:
› In article ,
› "Pete Dashwood"  writes:
…[66 more quoted lines elided]…
› didn't the buyer go elsewhere?

Because they probably had no option or because everybody in that particular
niche market is charging like a wouned bull.

You think that $6 for every man woman and child is reasonable? I think it is
outrageous.
› 
›› 
…[4 more quoted lines elided]…
› and one need to protect any advantages they may accomplish.

I have encountered this attitude in many walks of Commerce and it is just
nonsense. The Military MAY have a case for it, but Emergency Services most
certainly don't. (Having worked on Military projects I can tell you they
take it WAY too far, but that is, again, indicative of a mentality.

If you write software that REALLY has clever stuff in it and you don't want
it available to your competitors, you take measures at the level of the
software to ensure that it is difficult to crack, you don't withold
information from your Users.
› 
›› 
…[5 more quoted lines elided]…
› you feel better if you had access to the sources for Windows?  :-)

Absolutely, positively, and emphatically NOT! I am very happy to use Windows
on a daily basis, use the components that are part of it and .Net, and NOT
have the source code. But then, I moved off the COBOL Source code mentality
many years ago now. Source code is (almost) irrelevant; it is OBJECTs that
matter. Myself and millions of other people use .Net libraries and
components every day. Nobody minds not having the source.
› 
› But on a more realistic note, ever do any reading about voting
…[3 more quoted lines elided]…
› 
 
› Sorry, no interest in voting machines so unqualified to comment.
 
›› 
›› (There is little point in training people then denying them access to
…[8 more quoted lines elided]…
› advantage you may have.  Or decide to get out of the business.

I have done several successful deals with different Governments (and
Quasi-Governmental organizations like City Councils) and never worried about
the competition. Neither have I ever been secretive about what my products
can do or how they do them. But then, I've never been afraid that my product
is inferior to somebody else's; I know it isn't because I make sure it
isn't.

Maybe it depends on the Government you are dealing with.

Within the last few years I have had at least one US State Governments
looking at the PRIMA Toolset. But they can't buy it. Not because they don't
rate it (in all cases they have LOVED the product) but because they are tied
to a global federal IT policy and because PRIMA is not an American company.
I would be very glad to see it being used by these people because they
obviously need it, but I'm not prepared (at this stage) to incorporate in
Delaware and then lobby the powers that be to change their policy. (I'll
wait for a year or so until their current proposed idea fails, then try
again...) I'm pleased to report that American businesses have no such
constraints and buy what they consider to be useful from whoever has it.
That's a different "business model"...
›
››
…[3 more quoted lines elided]…
› players in that domain follow.

That would be the old "Snouts in the trough; we have a captive market..."
business model...


› 
›› 
…[7 more quoted lines elided]…
› does not involve shopping on the Internet.

The way in which you promote a product or service certainly varies with the
intended market, but that has nothing to do with secrecy surrounding it.
This is commercial computer software not WMD.
› 
›› 
…[4 more quoted lines elided]…
› They "get away" with nothing.

They "get away with" holding various Counties to ransom and over-charging
for software to run an essential service. Those costs get passed on to the
people who live in those Counties but never got to vote during the
purchasing process. It is sad you seem to think this is OK.


The terms of the contract are knownw by
› all relevant parties before the sale is completed.  The buyer has seen
› the conditions of the sale and agreed to them.  If these restrictions
› are considered unacceptable, then they should not have accepted the
› contract.
 
› They have no choice; the service is ESSENTIAL.
 
› 
›› 
…[6 more quoted lines elided]…
› there really aren't any alternatives.

If, as you stated above, all the players in this market are operating on the
same "business model", they really have no alternative.

I can tell you that here (I live in a "County" of around 100,000 people),
the software to run these services goes to (local and international) tender.
If they still can't get a price that is within the budget, then local
software houses would receive an RFP (non-secretive) stating what the
software must achieve, and it would be locally developed. Like I said
before, my first reaction was "We should be writing this software; we could
charge half of what is being charged and still come out way ahead." (To be
fair, software development costs are probably cheaper here than in the USA.)
›
››
›› God Bless America.
›
› I agree. But then I am not being sarcastic.

Neither was I. I am an Americaphile, but that doesn't blind me to greed (and
the facilitation of it as "hard nosed business") wherever it takes place.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 4)_

- **From:** "bill" <ua-author-12423647@usenetarchives.gap>
- **Date:** 2014-12-12T09:08:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p6@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap>`

```
In article ,
"Pete Dashwood" writes:
› Bill Gunshannon wrote:
›› In article ,
…[70 more quoted lines elided]…
› niche market is charging like a wouned bull.

How much do you sell your software for? If it's over $50 sounds like
"charging like a wouned bull" to me. Amazing how people with no idea
of the effort or expense in developing things always think it should
be given away.

›
› You think that $6 for every man woman and child is reasonable? I think it is
› outrageous.

Everyone is entitled to their opinion. But as you have no idea what it
actually costs to develop that praticular piece of software it reall is
irelevant. Of course, as stated, if you really think this then why not
write your own version (as you seem to think the effort is much less than
what they do) and drive them out of business.

›› 
››› 
…[8 more quoted lines elided]…
› certainly don't. 

Business is business. Yout either compete or die. If you have nothing
to diferentiate you from your competitors why would anyone buy from you?
If you have something you figured out (at some unspecified R&D cost) that
makes your system better, and you let your competitros have it how long
will you be in business?


› (Having worked on Military projects I can tell you they
› take it WAY too far, but that is, again, indicative of a mentality.

Having worked on both sides of the coin, government contractor and the guy
writting the RFP's they chase after, I disagree.

› 
› If you write software that REALLY has clever stuff in it and you don't want 
› it available to your competitors, you take measures at the level of the 
› software to ensure that it is difficult to crack, you don't withold 
› information from your Users.

Sorry, I didn't see where they are witholding anything fromt he users that
they needed to do the job. I did see that they were requiring that the
user not make any information available to people outside the scope of the
contract. All businesses do that. Try calling one of your competitiors
and asking for all their financials.

›› 
››› 
…[12 more quoted lines elided]…
› components every day. Nobody minds not having the source.

It is not the actual form of the data that matters, it is the secrecy.
You seem to think that Microsoft hiding stuff is OK but this other
company should make everything public. Interesting.


›› 
›› But on a more realistic note, ever do any reading about voting
…[5 more quoted lines elided]…
› Sorry, no interest in voting machines so unqualified to comment.

Don't need to have interest in them. At least over here, it has been
very evident in the public press. Machines that decide matters like
who the next president will be are completely secret. Even the
government can't see the code that makes them work. Do you not see
the problem there? And this has a potential for much greater impact
on a lot more people than some 911 phone system.

› 
››› 
…[16 more quoted lines elided]…
› isn't.

Who said any product is inferior? One being better than the other does
not imply inferiority, it only implies better or more extensive R&D and
that costs money which must be recouped and protected.

› 
› Maybe it depends on the Government you are dealing with.
 
› Probably depends more on how competitive that part of the market is.
 
› 
› Within the last few years I have had at least one US State Governments 
› looking at the PRIMA Toolset. But they can't buy it. Not because they don't 
› rate it (in all cases they have LOVED the product) but because they are tied 
› to a global federal IT policy and because PRIMA is not an American company. 

"Buy American" is not some nationaly mandated policy. It is decided, in
most cases, at the RFP level. The US Army M9 Pistol is a Baretta. You
must have missed the public flap over the US Olympic Teams clothing
ensemble. All made in China. Including the American Flags. :-)

› I would be very glad to see it being used by these people because they 
› obviously need it, but I'm not prepared (at this stage) to incorporate in 
…[4 more quoted lines elided]…
› That's a different "business model"...
 
› Not a business model difference, politics is not business.
 
›› 
››› 
…[6 more quoted lines elided]…
› business model...

Hey, anyone is welcome to enter the market. The fact that some have
already invested large sums in building their place in that market
and prefer to recoup that investment not withstanding.

I'll bet you're one of those people who think $500 hammers and $200
toilet seats are absurd, too. But then, you probably never looked
at the real reason why they cost that. It has to be those greedy
contractors trying to bilk the government.

› 
› 
…[13 more quoted lines elided]…
› This is commercial computer software not WMD.

As stated above, the market and the product are irelevant. Unless you
are dealing in commodities (like PC's) where the margins are razor thin
and all profit comes from quantity you need something to dieferntiate
you from your competitors and once you have that, you need to protect
it or lose the business.

›› 
››› 
…[9 more quoted lines elided]…
› purchasing process. It is sad you seem to think this is OK.

If the terms of the contract were unacceptable, then they should not have
accepted them. Saying that they are "getting away" with something their
customer agreed to up front is just plain silly. Those damn Porsches
salesmen. "Getting away with" charging $80,000 for a car. Ford sells
one for $19,000. Why should Porsche be alowed to "get away" with this?

› 
› 
…[6 more quoted lines elided]…
› They have no choice; the service is ESSENTIAL.

Sounds to me like some company saw a niche that needed to be filled and
filled it. There are always other choices. The "County", who ever that
is, could have opted to develop their own. Why didn't they? I would
assume because they quickly saw that it would a) cost more, b) not likely
be as functional, c) be more bug ridden, at least for some unacceptable
peiod of time, etc. Being government, they obviously put out an RFP and
compared all the respondents (assuming there actually were more than one)
and weighing all the factors picked this one. Blaming the company because
you don't like the terms after you have accepted the contract seems rather
silly. Especially when you consider that one of the options is to say
that none of them are acceptable, try again.

› 
›› 
…[10 more quoted lines elided]…
› same "business model", they really have no alternative.

Write their own. Put terms in the RFP that say they can't do that. Of
course, you then run the risk of no one bidding, or only your "inferior"
vendors bidding. But that's the nature of any business. Trust me, in
my day I put in hundreds of hours coming up with RFP responses only to
have someone higher up say that after due consideration we were not going
to bid at all. I have also been on projects where we withdrew our bid
for exactly these kinds of things. Customer notifies bidders that some
specified behavior would not be acceptable.

› 
› I can tell you that here (I live in a "County" of around 100,000 people), 
› the software to run these services goes to (local and international) tender. 
› If they still can't get a price that is within the budget, then local 
› software houses would receive an RFP (non-secretive) 

Not sure what this means, but no government RFP in the US is ever secret,
At the federal level there is even a national newspaper where they must be
published, Commerce Business Daily.

›                                                      stating what the 
› software must achieve, and it would be locally developed. Like I said 
› before, my first reaction was "We should be writing this software; we could 
› charge half of what is being charged and still come out way ahead."  (To be 
› fair, software development costs are probably cheaper here than in the USA.)

No argument there. Companies are always looking for niches where they can
make a profit. that's what business is about. Ever hear of a Canadian
Company called GEAC? When I first came to the University we had a GEAC
Library Catalog System. Custom Hardware, Custom Software, proprietary
data formats, etc. Guess what, they left that market completely. Once
people like DEC and IBM started doing it with their general purpose systems
GEAC was no longer competitive. They moved on to a Niche that was just
opening up that they thought had great potential. 911 Systems. Oh, and they
dumped the proprietary hardware in favor of PC's having learned their lesson
about being competitive.


›› 
››› 
…[5 more quoted lines elided]…
› the facilitation of it as "hard nosed business") wherever it takes place.

Sorry, I see more greed from companies outside the US that take US developed
products, steal tht IP and then undercut the US company cause they didn't
have any R&D costs to recoup. And, as stated above, the infamous $500
hammer and $200 toilet seat are not contractor greed when you actually
know and consider all the facts.

All the best.

bill

Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
bil··9@cs.··n.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 5)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-12-12T14:01:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p7@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap>`

```
In article ,
Bill Gunshannon wrote:

[snip for effect]

› Amazing how people with no idea
› of the effort or expense in developing things always think it should
› be given away.
 
› [snip]
 
› Of course, as stated, if you really think this then why not
› write your own version (as you seem to think the effort is much less than
› what they do) and drive them out of business.
 
› [snip]
 
› Business is business.  Yout either compete or die.
 
› [snip]
 
› One being better than the other does
› not imply inferiority, it only implies better or more extensive R&D and
› that costs money which must be recouped and protected.
 
› [snip]
 
› Hey, anyone is welcome to enter the market.
 
› [snip]
 
› Sounds to me like some company saw a niche that needed to be filled and
› filled it.  There are always other choices.  The "County", who ever that
› is, could have opted to develop their own.

America - Offering Econ 101 Solutions to Econ 201 Problems!

Tune in for next week's episode, 'You'll Never Find Money in the Street
Because Someone Else Will Have Found It First'.

DD
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 6)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-12-14T03:50:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p8@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap> <gap-bad2feadcc-p8@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Bill Gunshannon  wrote:
…[38 more quoted lines elided]…
› DD

Sorry Doc,

this is too obtuse for my tired brain at the end of the week.

Could you give us a clue as to what the point is?

(Simple direct English would be appreciated...)

Pete.

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 7)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-12-14T19:02:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p9@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap> <gap-bad2feadcc-p8@usenetarchives.gap> <gap-bad2feadcc-p9@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› doc··f@pa··x.com wrote:
›› In article ,
…[16 more quoted lines elided]…
››› Business is business.  Yout either compete or die.
 
›› [snip for greater effect]
 
›› America - Offering Econ 101 Solutions to Econ 201 Problems!
›› 
…[9 more quoted lines elided]…
› (Simple direct English would be appreciated...)

My apologies, Mr Dashwood! At times I strive for so much elegance that I
veer off into obscurity.

There is a cohort of my countrymen... countryfolk... fellow-citizens who,
with apparently gleeful ignoring of facts or the way things were before
(L., 'status quo ante'), bray incessant and simple-minded mantras about
Really Complex Stuff.

It is a kind of a societal 'all ya gotta do' and Mr Gunshannon's
assertions seem to be of that sort. There's a kind of 'build a better
mousetrap and the world will beat a path to your door' jingoism to it that
was - to my ear - at first a charming naievete... but it has grown so
impervious to argument that I reduced it to the first simple phrase I used
above.

A course in basic economics - Econ 101, as it used to be taught to college
freshman... freshfolk... first-year students - gives, well... a basic
understanding of economics. An advanced course - Econ 201, taught to
sophomores - gives a understanding that the world just might be a bit more
intricate than what was taught in Econ 101.

Leaving aside junior- and senior-year courses (and entirely neglecting
post-graduate studies)... whenever a problem involving markets, money, or
labor arises the Econ 101 arguments are trotted out and droned as if they
were the end of all knowledge.

Hence my observation of 'America - offering Econ 101 solutions to Econ 201
Problems'.

That was followed by a joke about economists which I'd read in The
Economist long ago: 'an economist is someone who'll tell you that you'll
never find money in the street because someone else will have found it
first'. It seemed appropriate but it may be that my sense of propriety is
skewed.

DD
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 8)_

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2014-12-15T04:22:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p10@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap> <gap-bad2feadcc-p8@usenetarchives.gap> <gap-bad2feadcc-p9@usenetarchives.gap> <gap-bad2feadcc-p10@usenetarchives.gap>`

```
On 12/14/2014 6:02 PM, doc··f@pa··x.com wrote:
› (SNIP)
› 
…[7 more quoted lines elided]…
› 

Then there's President Harry Truman's joke about wanting to find a
one-armed economist, so he couldn't say, "...on the other hand..."

Or Nassim Nicholas Taleb (author of "The Black Swan") who seems to think
that Nobel Prize in Economics is awarded for very foolish academic work.

http://www.bloomberg.com/news/2010-10-08/taleb-says-crisis-makes-nobel-panel-liable-for-legitimizing-economists.html

Kind regards,



http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 9)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-12-19T19:52:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p11@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap> <gap-bad2feadcc-p8@usenetarchives.gap> <gap-bad2feadcc-p9@usenetarchives.gap> <gap-bad2feadcc-p10@usenetarchives.gap> <gap-bad2feadcc-p11@usenetarchives.gap>`

```
Arnold Trembley wrote:
› On 12/14/2014 6:02 PM, doc··f@pa··x.com wrote:
›› (SNIP)
…[11 more quoted lines elided]…
› one-armed economist, so he couldn't say, "...on the other hand..."

LOL! I like that one...

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 8)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-12-19T19:50:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p10@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap> <gap-bad2feadcc-p8@usenetarchives.gap> <gap-bad2feadcc-p9@usenetarchives.gap> <gap-bad2feadcc-p10@usenetarchives.gap>`

```
doc··f@pa··x.com wrote:
› In article ,
› Pete Dashwood  wrote:
…[70 more quoted lines elided]…
› DD
OK, I'm with it now. Sorry, I know having to explain a joke is never a good
thing...

Nice to see you still in form. :-)

Happy Holidays!

Pete.

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 9)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-12-24T13:18:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p13@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap> <gap-bad2feadcc-p8@usenetarchives.gap> <gap-bad2feadcc-p9@usenetarchives.gap> <gap-bad2feadcc-p10@usenetarchives.gap> <gap-bad2feadcc-p13@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:

[snip]

› Happy Holidays!

Season's Greets to you and yours, old man. and may you all be blessed with
fresh air, good light, clear waters and food that satisfies tongue and
body both.

DD
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-12-14T03:48:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p7@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap>`

```
Bill Gunshannon wrote:
› In article ,
› "Pete Dashwood"  writes:
›› Bill Gunshannon wrote:
››› In article ,
››› "Pete Dashwood"  writes:


Bill,

I read your response and considered it.

Unfortunately, I don't have time at the moment to engage in what would be an
interesting discussion on the relative aspects of doing business.

It seems to me it comes down to attitude. (And I don't think yours is
"wrong"... :-))

I try to be fair in business as I am in Life and I'm not even slighly
paranoid about people stealing trade secrets from me. I don't have any. Want
to know something? Ask me.
If it's a fair question, I'll answer it. (Even if you are competing with
me...) I'm not intimidated by competition and I never denigrate them. I'd
rather talk about my products than someone else's.

If I my code does things that other people's doesn't, I'm happy for them to
try and develop the same functionality. I'd rather BE the Jones's than have
to keep up with them.

As far as profit goes, I'm very happy to make something conscionable, rather
than what the traffic can be forced to bear, because I have to sleep nights
and I wouldn't if I knew we were ripping people off.

PRIMA very often does things for nothing because it is the "right" thing to
do. (http://primacomputing.co.nz/PRIMAMetro/Testimonials.aspx)

No, I would never sell a $500 hammer, any more than I would charge a
community $6.00 for every man woman child in it, to have an essential
system that didn't cost a fraction of that amount to write.

Guess I'm not much of a Businessman, really... :-)

I do understand your points and I have encountered people who are driven
only by profit. Profit is good, as long as it is fair. Greed is something
else again. That's my case.

Pete.

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Software License Contracts and Trade Secrets

_(reply depth: 6)_

- **From:** "bill" <ua-author-12423647@usenetarchives.gap>
- **Date:** 2014-12-15T09:20:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bad2feadcc-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-bad2feadcc-p15@usenetarchives.gap>`
- **References:** `<9a45b0cc-7653-43fd-85e8-377ecd2f4a8a@googlegroups.com> <gap-bad2feadcc-p4@usenetarchives.gap> <gap-bad2feadcc-p5@usenetarchives.gap> <gap-bad2feadcc-p6@usenetarchives.gap> <gap-bad2feadcc-p7@usenetarchives.gap> <gap-bad2feadcc-p15@usenetarchives.gap>`

```
In article ,
"Pete Dashwood" writes:
› Bill Gunshannon wrote:
›› In article ,
…[14 more quoted lines elided]…
› "wrong"... :-))

I have no real "attitude" in this, only a very good perception of how
it works. While I am purely a "techie" my ability to understand business
made me a valuable player in my days before joining academia.

› 
› I try to be fair in business as I am in Life and I'm not even slighly 
…[8 more quoted lines elided]…
› to keep up with them.

And that's fine, as long as your business is small enough and your market
wide enough that you don't need to worry about being pushed out entirely.
The government contracting business is not like that.

›
› As far as profit goes, I'm very happy to make something conscionable, rather
› than what the traffic can be forced to bear, because I have to sleep nights
› and I wouldn't if I knew we were ripping people off.

Charging a lot is not necessarily "ripping people off". One thing that
is missing in this whole discussion is any concept of the cost of the
actual development of the product.

›
› PRIMA very often does things for nothing because it is the "right" thing to
› do. (http://primacomputing.co.nz/PRIMAMetro/Testimonials.aspx)

Believe it or not, when I was doing government contracting we often did
stuff for nothing. To include purchasing extremely rare and expensive
items to test wether or not this might be a solution to a customer problem.
An Array Processor comes immediately to mind. Cost over $100K and after
testing turned out to not be the proper solution. So, we ate the cost.
I often did small software projects for nothing. And then there were
always the things I did without even asking my higher-ups because it was
just the thing to do.

›
› No, I would never sell a $500 hammer,

And that is because you don't know why it was a $500 hammer. The press
that reported its existence didn't bother with the explanation of why.

› any more than I would charge a
› community $6.00 for every man woman child in it, to have an essential
› system that didn't cost a fraction of that amount to write.

How do you know what it cost? And then we have this "essential" idea.
We got along just fine before we had the ridiculously expensive systems.
In many cases, the response is poorer and the service worse since getting
them. Way too many unknowns here. But then, that's government. (We
have a small local municipality that is getting rid of its police force
because it says it can no longer afford it. My question: Why not get
rid of the other un-needed services, like a mayor and a town council in
order to fund the police force? And then you have the fact that many
of our local communities run their own garbage service. Usually at a
greater cost than private companies (who they ban from operation in their
little fiefdom) and at a loss and with poorer service. But the first
thing to go is almost always the police force!!)

It is, in most cases, not the contractor but the government customer
that is the problem. Like the $500 hammer. OK, I have kept you in
suspense long enough. The $500 hammer was the result of a specification
that called for a hammer of a specific size and weight that was not
like any available commercial product. An operation would have to be
set up to custom manufacture this hammer. Oh, and by the way, the
government would only guarantee the purchase of a very small handful of
these custom hammers so all costs had to be absorbed with the assumption
that only that small handful would ever be purchased and the price had
to reflect that.

›
› Guess I'm not much of a Businessman, really... :-)

I am sure you are, but not in that kind of or at that level of business.
There is a very big difference between Bob's Custom Christmas Lawn
Decorations (you know, those plywood reindeer) and Lockheed-Martin.

›
› I do understand your points and I have encountered people who are driven
› only by profit.

When you are a publicly traded company with stock-holders you have a
legal and moral responsibility to return a reasonable profit to your
investors.

› Profit is good, as long as it is fair.

And there is insufficient information to amake the assumption that this
company is not making fair profit.

› Greed is something
› else again. That's my case.

Like many other things, greed can also be in the eye of the beholder.
Why does a Kia cost $17,000 and a Porsche cost $80,000? After all,
they are both just cars.

All the best.

bill

Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
bil··9@cs.··n.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
