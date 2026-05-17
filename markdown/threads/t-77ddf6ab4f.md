[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Contrarian view of COBOL

_38 messages · 11 participants · 2013-02_

---

### Contrarian view of COBOL

- **From:** Arnold Trembley <arnold.trembley@att.net>
- **Date:** 2013-02-14T03:43:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com>`

```
This article spawned a long thread in bit.listserv.ibm-main:

http://www.itworld.com/career/341879/cobol-will-outlive-us-all


-- 
http://www.arnoldtrembley.com/
```

#### ↳ Re: Contrarian view of COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-15T02:47:16+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ao4874Fg3acU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com>`

```
Arnold Trembley wrote:
> This article spawned a long thread in bit.listserv.ibm-main:
>
> http://www.itworld.com/career/341879/cobol-will-outlive-us-all

This is written by someone who hasn't grapsped the difference in paradigm 
and thinks that because there is still a requirement for mainframe COBOL, 
COBOL will be around for ever.

When the need for large volume batch processing goes, so will mainframe 
COBOL.

When the mainframe is replaced, so will COBOL be.

Nobody in their right mind is going to write COBOL on the Network, (unless 
they HAVE to, and generally, they don't...)
(Some will write OO COBOL for a while but my personal belief is that this 
will diminish as the new generation arrives and as people realize there are 
better and cheaper OO languages than COBOL.

I don't mind him talking up COBOL but I seriously disapprove of him 
recommending young people hang their career on it. That ship sailed long 
ago. It is good to know COBOL. It is good to know other languages. It is 
best to understand the difference.

The rate of mainframe attrition is actually accelerating and even the last 
bastions of Fortress COBOL are being eroded as more and more financial 
institutions realize the mainframe cannot compete with a large, modern, 
properly designed, network.

IBM is doing best of the suppliers 
(http://esj.com/articles/2011/09/12/proprietary-mainframe-servers-decline.aspx) 
but even they are seeing signs of erosion...
http://www.reuters.com/article/2012/08/28/us-ibm-mainframe-idUSBRE87R03S20120828
(The above article draws heavily on Gartner estimates which I wouldn't 
personally trust, even though what they say makes sense...They have been 
cavalier with figures in the past.)

So, how long before mainframes disappear?

It comes down to a number of factors, some of which are:

1. The financial drive to reduce IT costs. (Although mainframe prices have 
dropped and top end server prices have risen, there is still a wide gap. 
Also, the cost of ownership of mainframe systems (with the infrastructure, 
system programmers, etc.) is still considerably higher than connecting a 
bunch of servers together over a LAN or VPN.)
2. The attrition of the traditional school of IT that grew up with batch 
processing. The traditionalists are retiring and being replaced by people 
with more dynamic approaches (Agile style development vs Waterfall). 
Although this CAN be done with mainframes, tradtionally, it hasn't been.
3. The influx of a new generation of programmers and system designers who 
are more interested in using the power available to model the real world and 
process transactions completely in real time. Batch processing is not a big 
feature in modern systems because it isn't needed if the system is designed 
to reflect the real world. High volume concurrent transactions are addressed 
by extending the network and load levelling, rather than batching overnight. 
As noted above, if batch processing declines, so does the need for a 
mainframe...
4. The influx of a new generation who can do their own local processing 
using standard software tools without specialised programming knowledge.

Nevertheless, mainframe markets are still in the billion dollar league so it 
is hard to see them collapsing overnight.

Realistically, it will be 15 years before the mainframe becomes a museum 
curiosity but within 3 to 5 years you will see the majority of businesses 
moving to the network and COBOL will be even more of a historical 
programming language than it is today.

I'm not sure what is "contrarian" here, but that is my view on it.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: Contrarian view of COBOL

- **From:** David L <david.lee.lambert@acm.org>
- **Date:** 2013-02-22T09:21:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com>`
- **In-Reply-To:** `<ao4874Fg3acU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net>`

```
On Thursday, February 14, 2013 8:47:16 AM UTC-5, Pete Dashwood wrote:
> When the need for large volume batch processing goes, so will mainframe 
> COBOL.
> 
> When the mainframe is replaced, so will COBOL be.

Certainly there's some correlation between using a mainframe, and batch processing, and COBOL;  but it's not perfect.  It's possible to run COBOL on non-mainframe systems; even a 10-year-old cheap laptop or the smallest possible VM in Amazon Web Services has much more CPU, memory and disk storage than something like the System/360 model 40.  COBOL on a mainframe supports non-batch transactional processing as well (e.g., with CICS).  A modern mainframe can also run non-COBOL software;  there's a version of Linux that will run in a VM on System z, and z/OS itself will run perl, Java, Apache HTTP server, etc.

> I don't mind him talking up COBOL but I seriously disapprove of him 
> recommending young people hang their career on it. That ship sailed long 
> ago. It is good to know COBOL. It is good to know other languages. It is 
> best to understand the difference.

About 1997, the community-college in the town where I grew up was still teaching COBOL as an "introductory programming" course.  By 2003, it was still in the listing of courses for the department, but hadn't actually been offered for a while.  As of now, it's not even listed.

There are also a few COBOL-like languages that are definitely divorced from the mainframe, and will probably stay around for a while.  One is SAP ABAP.  Also, while it's definitely not COBOL, Oracle PL/SQL (and similar stored procedure languages on other databases) is closer to COBOL than to C in its syntactic flavor.  (Oracle also sells a COBOL compiler for the systems its database will run on.)

> Realistically, it will be 15 years before the mainframe becomes a museum 
> curiosity but within 3 to 5 years you will see the majority of businesses 
> moving to the network and COBOL will be even more of a historical 
> programming language than it is today.

I don't think there ever was a time where the "majority of businesses", that is more than half of all commercial organizations, owned or leased a mainframe.  However, there probably was a time when the publicly traded companies representing between them more than half of all commercial revenue, or more than half of all market-value, owned a mainframe.  Do you think that is no longer true?

Also, there are probably still some industries where more than 90% of all transactions are recorded in at least one party's mainframe.  I imagine health-insurance claims processing, stock-market, commodities market, and passenger air travel all fall into that, although I can't prove it without some research.  Do you expect and industries or market segments to move out of that category within the next 3 to 5 years? Within the next 15 years?

--
DLL
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2013-02-22T17:58:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aopptiFa43vU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com>`

```
In article <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com>,
	David L <david.lee.lambert@acm.org> writes:
> On Thursday, February 14, 2013 8:47:16 AM UTC-5, Pete Dashwood wrote:
>> When the need for large volume batch processing goes, so will mainframe 
…[18 more quoted lines elided]…
> DLL

Being on the opposite side of the argument from Pete I have actually
given it (and continue to give it) consderable thought.  What I
actually see is the same thing I saw in academia with other languages.
Rather than providing the tools students need to succeed in the iT world
they are much more interested in driving the bus. (As a side not, it is
even funier in light of the recent construction of the new science
center which had "ergonomists" and "education experts" telling the
faculty they couldn't have the classrooms laid out or equiped the way
they wanted cause that wasn't how teaching was done!)  I have repeatedly
pointed out large numbers of massive COBOL systems that are not going
to be re-written in Java.  It has reached the point of vendors having
to plan on training their own programmers.  Over the long run do people
even realize the negative impact this could have on academia?  In working
on my Masters I have had to read quyite a bit about life in the 19th
century.  The "enlightened" during that period were totally against
University as a source for a utilitarian education.  They wanted it
to be about "the well rounded man" and not the place you went to get
a trade. They lost.  I have gone to a lot of open-houses at the University
(working them, not visiting them) and I can assure one of the biggest
concerns is future profit from their education.  On both the students
and parents list of concerns.

Research is fine and if something good comes of it, all the better, but
it is really time for education to get back in touch with the IT world
and start giving the students what they need to succeed (and in this
economy just survive) and like it or not, COBOL is still one of those
things and will likely be for at least another entire generation of
programmers.

bill


-- 
Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
billg999@cs.scranton.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2013-02-22T19:45:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kg8hso$ll4$1@reader1.panix.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net>`

```
In article <aopptiFa43vU1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:

[snip]

>In working
>on my Masters I have had to read quyite a bit about life in the 19th
…[3 more quoted lines elided]…
>a trade. They lost.

Mr Gunshannon, our readings have been different.  What you describe above 
seems like the British system, bent on training administrators for The 
Empire.  The German system allied academic and business systems, 
especially in the Saar region.

The Swedes used to say 'in media felicitas est'.

>I have gone to a lot of open-houses at the University
>(working them, not visiting them) and I can assure one of the biggest
>concerns is future profit from their education.  On both the students
>and parents list of concerns.

It might be a Good Thing to remind folks - gently, of course - that five 
years after graduation fewer than 50% of baccalureates work in their 
degree-field.  The allopathic theory of reconstructive surgery may have 
fallen by the wayside but a bit of pleasure can still be had from 
recognising the sonata allegro form.

(I have stepped outside of stores and stood under the overhang with folks 
while an unexpected downpour rages.  When my desire to be elsewhere 
overcomes my avoidance of dampness I will exclaim 'Blow, wind, and crack 
thy cheeks!' and stride off.)

DD
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-23T21:06:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aorbjaFlieoU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <kg8hso$ll4$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <aopptiFa43vU1@mid.individual.net>,
> Bill Gunshannon <billg999@cs.uofs.edu> wrote:
…[31 more quoted lines elided]…
> wind, and crack thy cheeks!' and stride off.)

Learing at girls in the rain... :-)

For some reason I can't explain, the above quote always conjures images of 
farting...

I'm ashamed of myself and glad the Bard doesn't know...

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2013-02-25T14:41:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kgft75$cck$1@reader1.panix.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <aopptiFa43vU1@mid.individual.net> <kg8hso$ll4$1@reader1.panix.com> <aorbjaFlieoU1@mid.individual.net>`

```
In article <aorbjaFlieoU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> (I have stepped outside of stores and stood under the overhang with
>> folks while an unexpected downpour rages.  When my desire to be
…[8 more quoted lines elided]…
>I'm ashamed of myself and glad the Bard doesn't know...

Great minds and similar, small circles, Mr Dashwood.

(explanatory note - for those whose English might not include those 
colloquialisms 'wind' is a euphemism for flatulenced, 'cheek' for buttock, 
'crack' for the cleft between buttocks and 'cracking one', again, 
flatulence)

In a class for which we'd read the play I made that exact suggestion and 
the professor - gently and archly - said that my interpretation was 
incorrect.  From what I've read of Shakespeare since I've concluded that 
my professor was wrong about this tiny point and that whose view is 
correct matters even less.

DD
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-23T23:35:11+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aorkb0Fnek4U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net>`

```
Bill Gunshannon wrote:
> In article <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com>,
> David L <david.lee.lambert@acm.org> writes:
…[55 more quoted lines elided]…
> world they are much more interested in driving the bus.

I take your point, Bill, but we must also recognise that unless someone 
drives the bus we are not going anywhere... :-)

> (As a side
> not, it is even funier in light of the recent construction of the new
…[3 more quoted lines elided]…
> they wanted cause that wasn't how teaching was done!)

I really love self-proclaimed experts; hours of amusement...

Wouldn't you love to meet the aerodynamicist who claimed bumblebees can't 
fly? (I think this has to be an urban myth; I can't imagine a scientist 
saying that.)




> I have
> repeatedly pointed out large numbers of massive COBOL systems that
> are not going
> to be re-written in Java.

And I have repeatedly agreed with you on that.

But it is NOT the ONLY option for dealing with the COBOL legacy. (In fact, 
it isn't even a good option and that's why it is highly unlikely that anyone 
with any understanding about legacy will undertake it. There will be some 
where Evangelical zeal  for Java overcomes plain common sense, there will be 
some where they just HAVE to do SOMETHING and Java looks like it is a 
popular option, but the ones who actually think about it will realise this 
is NOT the way to go.

As I said somewhere else: Mixing COBOL and Java is like mixing whisky and 
water; it ruins two good things....)

> It has reached the point of vendors having
> to plan on training their own programmers.

Serve's 'em right, I reckon.

They had 30 years to do something about it and they chose not to.

If they had invested more in training their staff years ago and had kept up 
with what was happening in programming, they probably wouldn't be in the 
situation they are in.

If they are so desperate to maintain an obsolete staus quo, it seems 
perfectly fair to me that they have to pay for it.

Why should your tax dollars pay for them to resist change?


>Over the long run do
> people even realize the negative impact this could have on academia?

It doesn't seem very negative so far... Our local Polytechnic has dropped 
COBOL and no-one seems to be hurting.

> In working on my Masters I have had to read quyite a bit about life
> in the 19th century.  The "enlightened" during that period were
…[7 more quoted lines elided]…
> and parents list of concerns.

Not unreasonabe though, is it Bill?

When you look at the cost of a College degree in real terms it is 
frightening. Even at a reasonable school, never mind the top of the league. 
Many parents (and kids) make huge sacrifices to ensure that their kids get 
educated. Wanting some kind of return on the investment seems fair to me.
>
> Research is fine and if something good comes of it, all the better,
…[4 more quoted lines elided]…
> generation of programmers.

Well, that is your position and you have stated it very well. Unfortunately, 
just saying it doesn't make it so.

COBOL is being dropped for exactly the reason that it DOESN'T add very much 
to the value of a programmer in 2013. (Look at the job sites...)

But even if you were right, it is really a matter for individual 
institutions to decide what they are going to teach. They don't have 
unlimited resources and time is a precious commodity.

Although we have different positions on this, I do try to understand yours.

I still feel the evidence doesn't support it, though... :-)

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-23T05:05:27-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hd8hi8ddmritt5olfme6unv190mbc94jau@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <aorkb0Fnek4U1@mid.individual.net>`

```
On Sat, 23 Feb 2013 23:35:11 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:
>
>Wouldn't you love to meet the aerodynamicist who claimed bumblebees can't 
>fly? (I think this has to be an urban myth; I can't imagine a scientist 
>saying that.)


If it happened at all, it was clearly more along the lines of an
admission that the aerodynamic model being used clearly had limits.

http://en.wikipedia.org/wiki/Bumblebee#Flight
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2013-02-23T15:37:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aos62cFrgn2U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <aorkb0Fnek4U1@mid.individual.net>`

```
In article <aorkb0Fnek4U1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Bill Gunshannon wrote:
>> In article <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com>,
…[59 more quoted lines elided]…
> drives the bus we are not going anywhere... :-)

I have no problem with academia doing research and coming up with new
ideas (even OO :-).  But the problem is when these new ideas become
the only acceptable solution to any problem.  And, as I said, when
the result is that students aren't being prepared for the reality of
the industry and the real needs of the industry are not being met.
That's a lose-lose proposition.

> 
>> (As a side
…[6 more quoted lines elided]…
> I really love self-proclaimed experts; hours of amusement...

But that is precisely what I saw in academia. "I saw this whiz-bang
language at a conference of theoreticists and I now proclaim this is
the solution to all the world's IT problems.  Nothing else shall be
taught!!"  We went thru a period where CS I and CS II were taught
using Ada.  Now, don't get me wrong, I do Ada and had done Ada long
before this (back in my governmetn contractor days) but do realize
how many unhappy emails I got from our former students who had learned
Ada as their primary language and then went out into the IT world to
find noone using it.  (Well, I guess our students who went to work for
Lockheed-Martin were OK with it.  :-)

> 
> Wouldn't you love to meet the aerodynamicist who claimed bumblebees can't 
> fly? (I think this has to be an urban myth; I can't imagine a scientist 
> saying that.)
> 

Actually, the exact same interpretation of the theory of aerodynamics 
"proves" that helicopters can't fly either.  :-)
 
> 
> 
…[7 more quoted lines elided]…
> But it is NOT the ONLY option for dealing with the COBOL legacy. 

Well, it seems to me that there are really only two options.  Either
you get rid of it or you maintain it.  If you can't get rid of it then
you are going to need people to maintain it.  And even some of those
places that are being forced into (or mistakenly being led into) getting
rid of their COBOL are being pushed into even more niche and very likely
short-lived languages as potential replacements.  Or, worse still,
proprietary languages (PL/SQL) that do nothing but lock you into a
particular vendor unless you want to go thru the whole re-write
process all over again. (My last COBOL gig - beginning of this year!)

>                                                                   (In fact, 
> it isn't even a good option and that's why it is highly unlikely that anyone 
…[7 more quoted lines elided]…
> water; it ruins two good things....)

Well, I only picked on Java because it is still in vogue.  There are
other silly languages thrown nto the mix.

> 
>> It has reached the point of vendors having
…[4 more quoted lines elided]…
> They had 30 years to do something about it and they chose not to.

Why?  They chose the right tool for the job.  It is still the right tool
for the job.  Just not in vogue in the academic ivory towers.

By the way, I can throw an even more obscure system at you that not
only gets no coverage in Universities but most of them are unaware
of it's existence. And yet it is the most common system that hospital
systems are based on and also holds a large percentage of the financial
and insurance markets.  MUMPS - now known as ANSI-M.

> 
> If they had invested more in training their staff years ago and had kept up 
> with what was happening in programming, they probably wouldn't be in the 
> situation they are in.

If they had never used COBOL it would just be another language that
academia abandoned for no good technical reason.  Ada, anyone!!

> 
> If they are so desperate to maintain an obsolete staus quo, it seems 
> perfectly fair to me that they have to pay for it.

What makes it "obsolete"?  The fact that you or academia no longer like
it?  It does the job.  It is used in tested and proven systems, many of
them in places where errors are not a good thing. (we are not talking
Angry Birds here!!)

> 
> Why should your tax dollars pay for them to resist change?

Ummm...   Actually, it is tax dollars paying to train people.  The
US Department of Defense Mediacl System is written in COBOL and
maintained by General Dynamics.  Do you even have an inkling how
many facilities from clinics to full hospitals that involves?

> 
> 
…[4 more quoted lines elided]…
> COBOL and no-one seems to be hurting.

There is this large pendulum.  On one side is education and on the other
is experience.  When I started in this business I had very little formal
education in programming.  But I was a "hacker" (back in the days when
that was a good thing) and garnered a lot of experience in my first jobs.
It allowed me to advance rapidly.  But I watched the pendulum swing
ever further towards the education side until eventually I was told
when applying for new jobs that with 30 years of experience I lacked
the necessary credentials for jobs that were being given to recent
college grads with no experience at all.  Even the government, who's
own regulations specifically say that education is not a substitute for
experience started placing excessive value on that little piece of
paper.  I now see this trend reversing. I think, from my observation
and reading of trade journals that it is academia's failure to meet
the needs of the IT industry that is driving this reversal.  When
the pendulum was at the peak on the education side I saw every two-
bit liberal arts college suddenly become a University and offer a
degree program in CS.  Now, even Community Colleges and Trade Schools
do it (we have one that offers degrees in IS right alongside their
degrees in carpentry and diesel mechanics).  The value of the IS/IT
degree is decreasing and that does not bode well for a lot of schools.
I used to work in a paper mill.  I worked alongside people with
advanced degrees in things like english and philosophy.  Half the
waitresses in the restaurant I frequently eat breakfast in have
education degrees. (My own daughter has a MS in Education and currently
works in a hospital call center!)  I expect that these will soon be
joined by people with IT degrees but no experience. And, of course,
waiting tables will not count as IT experience in the future either. :-)

> 
>> In working on my Masters I have had to read quyite a bit about life
…[15 more quoted lines elided]…
> educated. Wanting some kind of return on the investment seems fair to me.

So then, shouldn't one expect the school to be more concerned with
preparing the student for what the job market needs than what might
be in vogue in 5 years?

>>
>> Research is fine and if something good comes of it, all the better,
…[10 more quoted lines elided]…
> to the value of a programmer in 2013. (Look at the job sites...)

You keep saying that and I keep pointing out that there are COBOL jobs out
there and that most of them pay very well, offer stability and the potential
for along and profitiable career.  The best jobs are not found on Monster
Dice or Indeed.  Most serious employers won't use them.  When you see a
job with Lockheed-Martin or Raytheon or Gneral Dynamics (and numerous
others) on these sites they were not put there by the primary they were
scraped from the primaries career site using some form of search engine.
You can not apply to any of these (and most other large corporations)
thru any of these sites.  They are a very bad measure of the serious
IT world.  But I guess if you think no one can lie on the INTERNET you
will take them at face value.  :-)

> 
> But even if you were right, it is really a matter for individual 
> institutions to decide what they are going to teach. They don't have 
> unlimited resources and time is a precious commodity.

I don't know what it is like over there, but over here higher education is
becoming amore and more competitive endeavor.  I think we now have way too
many "Universities" and expect a cahnge to come as economice get tighter.
The survivors are likely tobe the ones who offer the programs that can
sell.  That means the ones that are most likely to lead to a job.
Obviously the big names like MIT and Stanford have no fears.  But in
an area like where I live with over a dozen schools offering some form
of CS/IS/IT degree within a twenty mile circle it is unlikely that all
will succeed.

> 
> Although we have different positions on this, I do try to understand yours.
> 
> I still feel the evidence doesn't support it, though... :-)

And yet, I see evidence that does.  But then, my observations are pretty
much academic at this point as well as while I may go back to work, it
is less likely every day and won't be for very long if I do (my previous
employer at the University has still not filled the position I left a year
and a half ago and is moderately interested in my coming back!)  And,
unless it was a telework job it won't be in COBOL as my next relocation
will be to a home down south where the weather is much warmer and the
greens much faster.

All the best.

bill

-- 
Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
billg999@cs.scranton.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** Rick Smith <rs847925@gmail.com>
- **Date:** 2013-02-23T11:33:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c2807dee-d26c-4c1f-a141-7e530d236fca@googlegroups.com>`
- **In-Reply-To:** `<aos62cFrgn2U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <aorkb0Fnek4U1@mid.individual.net> <aos62cFrgn2U1@mid.individual.net>`

```
On Saturday, February 23, 2013 10:37:49 AM UTC-5, Bill Gunshannon wrote:
[snip]
> [...] And,
> unless it was a telework job it won't be in COBOL as my next relocation
> will be to a home down south where the weather is much warmer and the
> greens much faster.

In North Central Florida, the weather is warm (some say unbearably
hot, but polar bears would say that), the greens are fast, and
the local university still teaches COBOL.

University of Florida
< https://catalog.ufl.edu/ugrad/current/courses/descriptions/computer-science.aspx >

COP 2121 Introduction to COBOL for CISE Majors
Credits: 3; Prereq: MAC 2233 or MAC 2311 or MAC 3472.
Techniques for business information systems programming in COBOL
utilizing comprehensive facilities of the COBOL language.
Business applications and examples of their solutions will be
employed throughout. Topics include advanced table handling
as well as sequential, random and indexed file organizations
and manipulation techniques in COBOL. (MR)
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 7)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2013-02-23T19:49:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aoskqsF5uuU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <aorkb0Fnek4U1@mid.individual.net> <aos62cFrgn2U1@mid.individual.net> <c2807dee-d26c-4c1f-a141-7e530d236fca@googlegroups.com>`

```
In article <c2807dee-d26c-4c1f-a141-7e530d236fca@googlegroups.com>,
	Rick Smith <rs847925@gmail.com> writes:
> On Saturday, February 23, 2013 10:37:49 AM UTC-5, Bill Gunshannon wrote:
> [snip]
…[6 more quoted lines elided]…
> hot, but polar bears would say that), the greens are fast, and

Sorry, that COBOL gig I spoke of was in Kingsland, GA right over the
border from Jacksonville.  And I have family in Gainesville and have
been there recently, too.  Contrary to popular belief Florida is not
really a retirement friendly state.  I am looking more at Southern
Alabama (I would say Southeastern Texas but I would need a divorce
first.)

> the local university still teaches COBOL.
> 
…[10 more quoted lines elided]…
> and manipulation techniques in COBOL. (MR)

Don't confuse a catalog entry with a real course.  COBOL as a separate
and distinct course remained in our course catalog, unoffered, for almost
two decades.  You need to look at the offerings for the semester to see
if they actually teach it.  I would guess, not.  Hmmmm...  Wonder if
anyone I know is still there that I could ask?

bill

-- 
Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
billg999@cs.scranton.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include <std.disclaimer.h>
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2013-02-23T13:33:47-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d31a597e-d3a5-4bcd-a933-546de4edb829@kk9g2000pbc.googlegroups.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <aorkb0Fnek4U1@mid.individual.net>`

```
On 23 Feb, 23:35, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:

> I really love self-proclaimed experts; hours of amusement...
>
> Wouldn't you love to meet the aerodynamicist who claimed bumblebees can't
> fly? (I think this has to be an urban myth; I can't imagine a scientist
> saying that.)

When Mitchell was designing the Spitfire they were working with flying
models. These did not produce the results that the calculations
predicted. By calculating different sized models they showed that the
problem was related to the scale effect of viscosity of air. By
introducing the Reynolds number into the calculations they were able
to get conformance between the calculations and the actual model
results.

Exactly the same was the claim about the bumblebees. It wasn't a
statement about the bees, it was about the then current state of the
aerodynamic theory.

That is to say he _didn't_ claim that bumblebees couldn't fly, he
claimed that calculations showed that bumblebees should not be able to
fly.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-24T11:00:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aossfbF23ifU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <aorkb0Fnek4U1@mid.individual.net> <d31a597e-d3a5-4bcd-a933-546de4edb829@kk9g2000pbc.googlegroups.com>`

```
Richard wrote:
> On 23 Feb, 23:35, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[21 more quoted lines elided]…
> fly.

A very important distinction.

I guess it forced them to look further so it is no bad thing.

I spent a few months at Hursley Park, working on contract to IBM in 
Southampton. It was an amazing place; the Spitfire was largely designed and 
prototyped there, (There is a really beautiful painting of one, along with 
some photos taken at the time). Of course, CICS was also designed and built 
there so it is rich in history at a number of different levels. The grounds 
are quite beautiful (just like the grounds at IBM Southampton which were 
landscaped from reclaimed land), but the offices are largely underground and 
I found that a bit disconcerting. It is neither pleasant nor healthy to work 
all day in artifical light then emerge to find the world in darkness... :-)

At the time I was there IBM were leasing it from the National Trust and they 
certainly took good care of it.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** Alistair Maclean <alistair.j.l.maclean@gmail.com>
- **Date:** 2013-02-23T13:35:12-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29b1482c-2afd-4900-b17c-4069b54a1c6b@googlegroups.com>`
- **In-Reply-To:** `<aorkb0Fnek4U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aopptiFa43vU1@mid.individual.net> <aorkb0Fnek4U1@mid.individual.net>`

```
On Saturday, February 23, 2013 10:35:11 AM UTC, Pete Dashwood wrote:
> I really love self-proclaimed experts; hours of amusement... Wouldn't you love to meet the aerodynamicist who claimed bumblebees can't fly? (I think this has to be an urban myth; I can't imagine a scientist saying that.) 

From Wikipedia:
The origin of this claim has been difficult to pin down with any certainty. John McMasters recounted an anecdote about an unnamed Swiss aerodynamicist at a dinner party who performed some rough calculations and concluded, presumably in jest, that according to the equations, bumblebees cannot fly.[36] In later years McMasters has backed away from this origin, suggesting that there could be multiple sources, and that the earliest he has found was a reference in the 1934 French book Le vol des insectes; they had applied the equations of air resistance to insects and found that their flight was impossible, but that "One shouldn't be surprised that the results of the calculations don't square with reality".[37]

Some credit physicist Ludwig Prandtl (1875–1953) of the University of Göttingen in Germany with popularizing the idea. Others say it was Swiss gas dynamicist Jacob Ackeret (1898–1981) who did the calculations.

In 1934, French entomologist Antoine Magnan (1881-1938) included the following passage in the introduction to his book Le Vol des Insectes:

Tout d'abord poussé par ce qui se fait en aviation, j'ai appliqué aux insectes les lois de la résistance de l'air, et je suis arrivé avec M. Sainte-Laguë à cette conclusion que leur vol est impossible.

This translates to:

First prompted by what is done in aviation, I applied the laws of air resistance to insects, and I arrived, with Mr. Sainte-Laguë, at this conclusion that their flight is impossible.

Magnan refers to his assistant André Sainte-Laguë, a mathematician.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-22T15:55:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com>`

```
On Fri, 22 Feb 2013 09:21:16 -0800 (PST), David L
<david.lee.lambert@acm.org> wrote:

>On Thursday, February 14, 2013 8:47:16 AM UTC-5, Pete Dashwood wrote:
>> When the need for large volume batch processing goes, so will mainframe 
…[4 more quoted lines elided]…
>Certainly there's some correlation between using a mainframe, and batch processing, and COBOL;  but it's not perfect.  It's possible to run COBOL on non-mainframe systems; even a 10-year-old cheap laptop or the smallest possible VM in Amazon Web Services has much more CPU, memory and disk storage than something like the System/360 model 40.  COBOL on a mainframe supports non-batch transactional processing as well (e.g., with CICS).  A modern mainframe can also run non-COBOL software;  there's a version of Linux that will run in a VM on System z, and z/OS itself will run perl, Java, Apache HTTP server, etc.


Perl on MVS is stuck somewhere at around 5.1 (nearly a decade old),
and is in imminent danger of having the Perl folks abandon any
semblance of even *trying* to maintain EBCDIC support.

http://www.nntp.perl.org/group/perl.mvs/2013/02/msg1619.html

While Cobol does run on other platforms, on most it's expensive and
not particularly native to the environment.  You have to really need
it.  But I think we'd all agree that the biggest hotspot of Cobol is
IBM mainframes.  The problem with that is that it's a fairly small
niche of software development.  There are few than 10,000 boxes in
about half that many organizations installed in the world.

And it's clearly not growing.  Even the usage of existing language
features that would drag Cobol out of the eighties is almost nil.

The long term outlook is not positive.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2013-02-23T00:57:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kg945q$cns$1@reader1.panix.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com>`

```
In article <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com>,
Robert Wessel  <robertwessel2@yahoo.com> wrote:

[snip]

>Even the usage of existing language
>features that would drag Cobol out of the eighties is almost nil.

Just to keep the dust off the link - take a gander at something that gets 
re-posted every few years since 19 May 1999 from
<http://groups.google.com/group/comp.lang.rexx/msg/29d1b77320d7bfc7?hl=en&dmode=source> 
(note the cross-postings):

--begin quoted text:

'What is *this* stuff?  EVALUATE TRUE WHEN cond-1 imperative statement... 
you call this COBOL?!?'

'Oh, please, Mr Standards-and-Practises Reviewmeister, it is exactly what 
is allowed by the ANSI '85 Standard.'

'ANSI '85?  Crap, I *knew* things were goin' ta hell in a handbasket when 
we allowed them fancy ANSI '74 constructs in a couple a' years back... 
look, 1985 is only 14 years ago, we oughta wait until the technology is 
Really Proven before we implement it.  Go back and rewrite this in *real* 
COBOL, then try again.'

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-22T20:32:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pfagi81amrnl7dedsnr4563v6sgrsli5s1@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com> <kg945q$cns$1@reader1.panix.com>`

```
On Sat, 23 Feb 2013 00:57:30 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com>,
>Robert Wessel  <robertwessel2@yahoo.com> wrote:
…[25 more quoted lines elided]…
>--end quoted text


Unfortunately that's a lot truer than it should be in a healthy
software development community.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 4)_

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2013-02-22T20:00:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o35gi85k1q1sjantioev2vpjohgmc9kt3b@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com>`

```
On Fri, 22 Feb 2013 15:55:24 -0600, Robert Wessel
<robertwessel2@yahoo.com> wrote:

>On Fri, 22 Feb 2013 09:21:16 -0800 (PST), David L
><david.lee.lambert@acm.org> wrote:
…[26 more quoted lines elided]…
>The long term outlook is not positive.
---
Robert,
Where did you find the < 10000 number?
Please, thanks,
Graham Hobbs
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-22T20:29:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v9agi8l33jqqnap3p2lv81ovmeqogrnukk@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com> <o35gi85k1q1sjantioev2vpjohgmc9kt3b@4ax.com>`

```
On Fri, 22 Feb 2013 20:00:31 -0500, Graham Hobbs <ghobbs@cdpwise.net>
wrote:

>On Fri, 22 Feb 2013 15:55:24 -0600, Robert Wessel

>>While Cobol does run on other platforms, on most it's expensive and
>>not particularly native to the environment.  You have to really need
…[11 more quoted lines elided]…
>Where did you find the < 10000 number?


It's rare that IBM ever leaks that kind of info, but from a 2007
interview:

"Bob Hoey, vice president of worldwide sales for the System z line at
IBM, spends a lot of time on the road visiting mainframe shops. And
while the mainframe base is not small enough to know every account
personally, there are by no means as many mainframe shops as there are
companies using Windows and Linux on X86 and X64 servers or those
using RISC/Unix machines. In fact, Hoey leveled with me--as few IBMers
have done in the past--and said flat out that there were about 10,000
mainframe footprints in the world. "I know where the machines are by
serial number and zip code," Hoey joked. About a third of these
machines are in the financial services sector, and when you add in
insurance and related businesses, these businesses account for about
half of the footprints"

http://www.itjungle.com/big/big071007-story01.html
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** Graham Hobbs <ghobbs@cdpwise.net>
- **Date:** 2013-02-22T22:14:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgcgi8hb69ejjj7jeftvhmatdd28996gol@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com> <o35gi85k1q1sjantioev2vpjohgmc9kt3b@4ax.com> <v9agi8l33jqqnap3p2lv81ovmeqogrnukk@4ax.com>`

```
On Fri, 22 Feb 2013 20:29:31 -0600, Robert Wessel
<robertwessel2@yahoo.com> wrote:

>On Fri, 22 Feb 2013 20:00:31 -0500, Graham Hobbs <ghobbs@cdpwise.net>
>wrote:
…[36 more quoted lines elided]…
>
---
Thanks very much, interesting article but 2007! Their share price
doubled in the last six years, likely prices too, whatelse might
indicate up to date figures...
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 7)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-23T00:44:38-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<clngi8daqid5k5kudnl2k5h86jl2unl35r@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com> <o35gi85k1q1sjantioev2vpjohgmc9kt3b@4ax.com> <v9agi8l33jqqnap3p2lv81ovmeqogrnukk@4ax.com> <vgcgi8hb69ejjj7jeftvhmatdd28996gol@4ax.com>`

```
On Fri, 22 Feb 2013 22:14:31 -0500, Graham Hobbs <ghobbs@cdpwise.net>
wrote:

>On Fri, 22 Feb 2013 20:29:31 -0600, Robert Wessel
><robertwessel2@yahoo.com> wrote:
…[43 more quoted lines elided]…
>indicate up to date figures...


We do know approximate system list prices:

http://www.tech-news.com/publib/

Similar models have hardly moved in price, a 2008 2097-701 (z9) and a
2012 2827-701 (z12) both for about $1.7M, but performance has improved
a 50%.  Similarly -764s of both models have list prices of about $25M,
although the z12 shows more of a performance improvement (somewhat
naturally, since the z12 scales to rather more cores, the
multi-processor overhead doesn't kick in as badly at a 2/3rds size
system as for a full sized system).

IBM sells a ton of software and services with Z.  IBM also has a great
deal of non-Z business.

IBM resolutely doesn't break out revenue by product line, but I'm
reasonable sure that IBM earns a pretty decent return on the Z
ecosystem.  OTOH, I *don't* think this is a growth business for them.

Nor do I think that think anyone is expecting the installed base of Z
systems to have grown meaningfully since 2007.  Attrition at the low
end appears to be continuing at a fair pace, so the number of systems
has almost certainly declined, although clearly the number of
installed MIPS has increased.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-23T21:01:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aorbb1Flgp8U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <bqofi8h6t6h2a2bhhp54h7t5jeeko01uug@4ax.com> <o35gi85k1q1sjantioev2vpjohgmc9kt3b@4ax.com> <v9agi8l33jqqnap3p2lv81ovmeqogrnukk@4ax.com>`

```
Robert Wessel wrote:
> On Fri, 22 Feb 2013 20:00:31 -0500, Graham Hobbs <ghobbs@cdpwise.net>
> wrote:
…[35 more quoted lines elided]…
> http://www.itjungle.com/big/big071007-story01.html

A really interesting little nugget, Robert.

Given the > $1 billion turnover it makes you wonder how much each site is 
spending on their IT... :-)

Thanks for posting the quote.

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-23T20:51:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aoraomFld0rU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com>`

```
David L wrote:
> On Thursday, February 14, 2013 8:47:16 AM UTC-5, Pete Dashwood wrote:
>> When the need for large volume batch processing goes, so will
…[8 more quoted lines elided]…
> memory and disk storage than something like the System/360 model 40.

Of course.  I ve been running COBOL on no-mainframe systems for over 30 
years... The difference is that people developing networked solutions 
understand the paradigm difference and use OO languages. Most COBOL people 
don't... yet.

I agree it is gradually changing and some mainframe people are realizing why 
it is important.

The fact is that objects and layers have never been a part of traditional 
mainframe development and are therefore seen as "foreign" to that platform.


> COBOL on a mainframe supports non-batch transactional processing as
> well (e.g., with CICS).

Yes. But it uses serial reusability and pseduo-conversational processing to 
do it, rather than true multi-instanced objects and layers. CICS is a good 
system (although there have been much better mainframe teleprocessing 
monitors, which never made it because they didn't have an IBM stamp on them 
(Shadow, Taskmaster, to name but two...)) and I worked with it from the tme 
it was invented until people realized that IMS/DC was better. It was later 
re-invented after the death of hierarchic databases on the mainframe meant 
the demise of IMS/DB and along with it, its transactional processing 
facility (IMS/DC), so the "competition" for CICS was removed. The new modern 
incarnation is much better than the original but it still can't compete with 
a load levelled network which distributes processes and resources in real 
time to where they are needed.

There are still a few mainframe sites that use IMS/DC although it has been 
renamed because nobody wants to admit they actually LIKED hierarchic 
databases :-).

Even the "new" CICIS is still a "centralized" concept and that's not what 
networks are about.



> A modern mainframe can also run non-COBOL
> software;  there's a version of Linux that will run in a VM on System
> z, and z/OS itself will run perl, Java, Apache HTTP server, etc.

Not in dispute. Although many people are finding it is cheaper to use 
networked servers to do all of these tasks.

Just because you CAN, doesn't mean you SHOULD... :-)


>
>> I don't mind him talking up COBOL but I seriously disapprove of him
…[8 more quoted lines elided]…
> listed.

Ever wondered why?

It isn't a fashion change; it is a paradigm shift. It stopped being relevant 
to the majority of computer processing around the World.

Colleges and Acadaemia in general have a responsibility to teach skills that 
are useful and likely to have a future.

COBOL can't be justified on those grounds.

(Certainly, it is "useful" but in a narrow sphere that most of commerce is 
trying to move away from (mainframe processing), particularly batch, which 
runs on procedural, centralized, monolithic code. That's a 20th century 
paradigm which derived from the Von Neumann model. OO is a paradigm which 
extends the Von Neumann model to multiple concurrent threads and instances, 
and isn't tied to a procedural execution....)

I realised this when I first tried to write a sort in COBOL, WITHOUT 
employing Fibonacci or Bubble or Tournament. A single engine that swapped 
stuff around. It became much easier when I was able to manufacture instances 
of little "workers" that could swap things around. (they were all identical 
in what they d"knew" but I could have as many of them running concurrently 
as I desired.) If there was a lot of sorting to do, throw more workers at 
it... This was one of the most fun programming exercises I have ever 
undertaken. I spent a week playing with it many years ago and I don't have a 
copy of it. I'm kind of loth to write it again because the novelty is 
gone... :-)

>
> There are also a few COBOL-like languages that are definitely
> divorced from the mainframe, and will probably stay around for a
> while.  One is SAP ABAP.

The success of  ABAP is tied in with the success of SAP. However, an 
increasing number of SAP customers don't want to tailor their own 
("non-standard") solution code. SAP is responding with better and more 
increased functionality within the base modules. It is interesting that when 
SAP was first developed in Germany (I was there at the time and tested it 
for the Company I was working with) you could ONLY use Assembler for 
"tailoring" it. ABAP came later as a "COBOL-like" language that customers 
could use to add their own functionality to the base package. Why do you 
suppose they chose to make it "COBOL-Like"? Because that's what most of 
their customers were using.

As demand for and use of COBOL declines, so will ABAP programming. (I 
wouldn't be surprised to see it revert to BAL :-))

This whole subject brings up something I have written about elsewhere. 
Namely the need for a focus on Functionality and not on Code. If the SAP 
modules you purchase do everything you need, you would have no requirement 
to tailor it. This is desirable for both Software AG and their clients.


>Also, while it's definitely not COBOL,
> Oracle PL/SQL (and similar stored procedure languages on other
> databases) is closer to COBOL than to C in its syntactic flavor.
> (Oracle also sells a COBOL compiler for the systems its database will
> run on.)

Yes, I know. I choose not to comment.
>
>> Realistically, it will be 15 years before the mainframe becomes a
…[6 more quoted lines elided]…
> owned or leased a mainframe.

You should have been here in the 1960s... it was the "only game in town" :-)

>However, there probably was a time when
> the publicly traded companies representing between them more than
> half of all commercial revenue, or more than half of all
> market-value, owned a mainframe.  Do you think that is no longer
> true?

It is a very fair point and a very good question. Yes, I think it is no 
longer true. I believe the percentage in the early 1970s would have been 
well over 80%, by the end of the 1980s, still around 80%, maybe down a 
little due to the influence of "early adopters", by the end of the 1990s 
(let's say, 2001...) hovering around 50%, and currently 40% and declining. 
In the last 10 years I have seen my Bank (a major international group) move 
off mainframes completely, my Insurance company do the same and an Insurance 
company I actually worked with in 2003 had moved all of their COBOL 
mainframe legacy to client server before I arrived and were working to 
replace it completely.

Sadly, there are few solid statistics to either confirm or deny my intuition 
above.

>
> Also, there are probably still some industries where more than 90% of
> all transactions are recorded in at least one party's mainframe.

Why not 100%? :-) (just as likely...) It would be 90% because they are 
working on decreasing their reliance on mainframes. :-)

I think this would be true for some COMPANIES rather than some INDUSTRIES...

What you describe is certainly true in the USA, but America is becominging 
increasingly an island as far as this goes. I have only a few contacts in 
the US and they say COBOL is alive and well at the moment, but there are 
management plans to phase out the mainframe long term. Some of them just 
don't see any options. (Which is sad, because there are some extremely good 
ones...) Also, of course, some managements don't like the shop floor to be 
privy to their long term strategy, so it is hard to know what is really 
being discussed in the Boardroom. (Also sad, but even worse, actually 
stupid... It comes from short sighted managers treating staff as cannon 
fodder and not recognizing them for the major asset they usually are. 
Companies that don't see US and THEM are invariably much more pleasant 
places to work and they have better morale and productivity.)

There are some US based companies who actually moved off the mainframe some 
time ago but they do seem to be the minority at the moment.

> I imagine health-insurance claims processing, stock-market, commodities
> market, and passenger air travel all fall into that, although I can't
> prove it without some research.

If you do that research you may be surprised.

Yes, many of these industries are still using mainframes but it is becoming 
increasingly less usual, particularly outside the United States, and, almost 
without exception even the most "staunch" are seeking for options that will 
get them off COBOL and off the mainframe. The stock market (just to pick one 
of your examples) is certainly no longer mainframe based in London and 
Europe and both the NYSE and Chicago are running Chi-X which is built around 
Enyx FPGA boards in top end servers. No mainframes in sight; and there 
haven't been for some years now. It is not without incident as we saw in 
2007 in London (although no fault was found with the servers, OS (Windows), 
or system software; it was application programming error), and again in 2012 
when another major stock Exchange was halted for a day, this time running 
Chi-X and Linux. This time the outage was caused by failure of a hardware 
component, which can happen on mainframes or servers.

I know from first hand experience (outside the USA) that some major Banks 
and Insurance companies are phasing out their mainframes, or have already 
done so. These are conservative industries where a nervous eye is kept on 
what the competition is doing. Once the landslide starts, the pebbles don't 
get to vote.


> Do you expect and industries or
> market segments to move out of that category within the next 3 to 5
> years? Within the next 15 years?

Yes, I do.

The trading of Stocks and similar already has. (Speed requirements are such 
that it requires secial hardware boards in top end servers to get the around 
100 microsecond transaction speeds required, across the staggering daily 
volumes of trades.)

Airline flight processing (logistics, seating, baggage, provisioning) is 
already mostly server based so it is logical to extend this to actual 
booking. Most of us book our own flights online and, while most of the 
searching is through legacy mainframe engines like Sabre, it will make sense 
for the airlines running this to optimise it or lose business to competing 
search engines. So I see the Airline industry beocming completely server 
based within say, 7 years.

If you think these time frames are short, you have to factor in the 
increasing acceleration of change. (See Kurzweil, "The Singularity is near" 
for a detailed description, backed by statistical projections, of this 
effect. Basically, he is saying that an idea 300 years ago might take a 
century to come into effect; today, an idea of the same magnitude could 
take, say, 30 years, and this "lag time" is getting shorter as technology 
drives the population ever faster. Pretty soon we won't be able to cope and 
we will resort to artificial enhancements to help us think faster and 
better. By 2047, it won't be possible to know what part of our thinking is 
artificial and what is wetware; we will have merged with the machinery as a 
"singularity".)

In 1995 (when COBOL was still pretty strong) I predicted that it would be 
dead by 2015. I based this on a noticeable decline in COBOL jobs being 
posted, and what I saw going on around me.  After the abuse I took in this 
forum for suggesting that OO COBOL might be important and that it was 
actually a new idea for COBOL, I was also keenly aware that it wouldn't be 
picked up by COBOLlers.

The OO paradigm was accepted by everyone except Fortress COBOL and I 
believed that spelled the end for COBOL. (I was wrong, that was only ONE 
factor in the decline of COBOL, but it is all too complex to go into 
here...) The World voted with its feet, the Network emerged victorious, and 
COBOL was simply bypassed.

What we are seeing now is a mopping up operation.

To most intents and purposes COBOL is already dead as a commercial language, 
apart from the isolated pockets we are discussing here.

To be fair, the whole way in which people and businesses use computers has 
changed dramatically, so comparing COBOL use in 1995 to COBOL use today is a 
bit like apples and oranges... actually more like apples and bananas :-).

Be that as it may, I believe it is wrong (today) to advise young people to 
make a career in COBOL, even though in 1995, that might not have been SO 
wrong, in 1975 it was a pretty good option, and in 1965, it was very sound 
advice.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 4)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-23T03:04:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mj0hi89fbbsg6l2hpbl99mh9diogvgl1ol@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net>`

```
On Sat, 23 Feb 2013 20:51:48 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>David L wrote:
>> Also, there are probably still some industries where more than 90% of
…[47 more quoted lines elided]…
>get to vote.


One reason for the growth of non-mainframe platforms in those
industries outside the U.S. and Europe (and a few other places) is
simply that these are often newer companies, and don't have systems
that were built on mainframes that are currently running their
businesses.  And very few of those have chosen to convert to the
mainframe as they've grown.

A somewhat analogous situation is the telephone network in the U.S.,
vs. just about anywhere else.  The U.S. had, by far, the best POTS
network on the planet.  And while cell phones were originally
introduced in the U.S., it was other places, starting in Europe, Japan
and some other countries where cell phones *really* took off, and the
opportunity to build a really good cell based telephone network for
cheap (relative to POTS service) presented itself, and was
enthusiastically adopted.

In the U.S. cell phones were originally nice-to-have, as opposed to
many other places where a cell phone was a huge improvement over the
local POTS service) , and network development lagged sharply.  Even
today, POTS service is stellar in the U.S. (but who cares anymore?),
and the cell network is just embarrassing when compared to most
developed countries (and a few not-so-developed countries).

And in many poorly developed countries, cell phones vastly outnumber
anything POTS-like, simply because of the cost of deployment of the
network.

We're not doing so hot on deploying Internet connectivity either.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-24T00:01:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aorlspFnpacU1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net> <mj0hi89fbbsg6l2hpbl99mh9diogvgl1ol@4ax.com>`

```
Robert Wessel wrote:
> On Sat, 23 Feb 2013 20:51:48 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[64 more quoted lines elided]…
> mainframe as they've grown.

That sounds reasonable. One of the Insurance companies I mentioned certainly 
fits that description. However, the Bank (a major Australasian one) and the 
other insurance company were both running on mainframes in the 1970s. When I 
thought about this I remembered another (Australian) insurance company which 
is still a major player in that sector. They sold off their IBM and Fujitsu 
mainframes in the 1980s and then leased the service back for a net saving of 
around $17,000,000 a year (which was a lot of money at the time.) What 
happened there was that their IT was becoming so expensive (around 
$25,000,000 a year) that their Directors started asking why they were in the 
IT business when the Company was suppposed to be an Insurance Company...
>
> A somewhat analogous situation is the telephone network in the U.S.,
…[19 more quoted lines elided]…
> We're not doing so hot on deploying Internet connectivity either.

High-Speed fibre is being rolled out here and the Government is mostly 
paying for it. I was able to get it for no installation charge and it has 
doubled my download speed, given me around 36 times the upload speed, and 
more than doubled my monthly bandwidth, for $2 a month more than I was 
paying for ADSL. If I choose to pay more, I can increase the download speed 
to around 100 MBS (currently 10 MBS, and was 5 MBS with ADSL2.) Of course, 
the USA is a much bigger country to cover... :-)

I was a bit skeptical about fibre as we have high speed wireless also 
available in Tauranga and that just seems more sensible to me. (However,  I 
live in a valley and they need a LOS transmitter.receiver...) I talked to a 
local Engineer and he pointed out that the wireless stuff is limited to 
around 50 MBS, can be subject to interference under extreme and unusual 
circumstances, and is a less stable technology. The form of wireless 
coverage we have here came from Israel and is very effective, but apparently 
there are different standards for wireless and different systems so it is a 
bit less clearly defined than fibre.

Currently, I'm extremely happy with the fibre connection, but I haven't 
thrown away my ADSL router, just in case... :-)

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-24T00:59:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<k5eji8h7348qnokfd859frc3en2q1lu9n6@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net> <mj0hi89fbbsg6l2hpbl99mh9diogvgl1ol@4ax.com> <aorlspFnpacU1@mid.individual.net>`

```
On Sun, 24 Feb 2013 00:01:43 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Robert Wessel wrote:
>> We're not doing so hot on deploying Internet connectivity either.
…[20 more quoted lines elided]…
>thrown away my ADSL router, just in case... :-)


Like I said, the deployment in the U.S. is just sad by comparison. And
a large portion of the population reflexively rejects any possibility
that the U.S. might not be #1 in some area, and comparisons to anyone
else are defacto wrong (at best) or (more likely) plain un-American.
Facts be damned.  *sigh*
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 4)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2013-02-23T13:21:31-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ceafaf2-cb32-47e1-8fde-591d56b77fb2@xb8g2000pbc.googlegroups.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net>`

```
On 23 Feb, 20:51, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:

> Of course.  I ve been running COBOL on no-mainframe systems for over 30
> years... The difference is that people developing networked solutions
> understand the paradigm difference and use OO languages. Most COBOL people
> don't... yet.

OO is not the answer to all questions. A large number of problems that
are still being solved by COBOL are applications where serial reuse is
more appropriate than object creation and garbage collection. For
example: banking where millions of transactions must be serialised
through the account updates.

> > COBOL on a mainframe supports non-batch transactional processing as
> > well (e.g., with CICS).
>
> Yes. But it uses serial reusability and pseduo-conversational processing to
> do it, rather than true multi-instanced objects and layers.

Modern Web based systems (eg: CGI and derivatives) also do serial
reusable and pseudo-conversational. Database servers also do this, as
do many other servers.

> Not in dispute. Although many people are finding it is cheaper to use
> networked servers to do all of these tasks.

Networked servers with load levelling are suitable for some tasks,
such as email servers or search processing. They are not suitable for
all applications.

> (Certainly, it is "useful" but in a narrow sphere that most of commerce is
> trying to move away from (mainframe processing), particularly batch, which
…[3 more quoted lines elided]…
> and isn't tied to a procedural execution....)

It is not necessary to have OO for multiple concurrent threads. It is
useful, though not essential, for multiple instances.

> I realised this when I first tried to write a sort in COBOL, WITHOUT
> employing Fibonacci or Bubble or Tournament. A single engine that swapped
…[4 more quoted lines elided]…
> it...

'Throwing' more workers is only useful up to the number of CPU cores
available to the program, and often it should be much less. Beyond
that the context swapping degrades the total performance.

> This whole subject brings up something I have written about elsewhere.
> Namely the need for a focus on Functionality and not on Code. If the SAP
> modules you purchase do everything you need, you would have no requirement
> to tailor it. This is desirable for both Software AG and their clients.

If all businesses were the same and had the identical business model
then none would have any advantage and the market would be flat. Then
some bright spark in one of the businesses would come up with the idea
that offering a discount might get them to sell more. If all
businesses used the same computer system then it would not cater for
the changes that businesses use to get an edge. While having a set of
standard rules may be 'desirable' for the software company, it is much
less so for the clients.

The whole point of having in-house IT is so that the business can
develop _without_ those procedures becoming available to every other
business.

> > I don't think there ever was a time where the "majority of
> > businesses", that is more than half of all commercial organizations,
> > owned or leased a mainframe.
>
> You should have been here in the 1960s... it was the "only game in town" :-)

The 'majority of businesses' are one or two man operations. They may
have a PC now, but they never had a mainframe.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-24T11:47:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aosv8hF2n22U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net> <9ceafaf2-cb32-47e1-8fde-591d56b77fb2@xb8g2000pbc.googlegroups.com>`

```
Richard wrote:
> On 23 Feb, 20:51, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[10 more quoted lines elided]…
> through the account updates.

Not a good example.The "overheads" of object creation and garbage collection 
are being optimized and minimized all the time. If you factor in the load 
levelling that is possible with a series of networked cores,  your 
centralized serial reuse is not so superior. The example of the Stock 
Exchange where very high performance and throughput for millions of 
transactions is required, is one that supports my case. Banking (and it is 
certainly not ALL Banks) uses serial reuse more from tradition and a history 
of mainframe processing, than from any real need to do so.

>
>>> COBOL on a mainframe supports non-batch transactional processing as
…[8 more quoted lines elided]…
> do many other servers.

CGI is not a "modern" Web Technology. Although it is effective, it doesn't 
compete with modern server side code alternatives that use code behind to 
dynamically manage web pages. It is about flexibility as well as processing 
and CGI can be a bottleneck where multiple page requests are queued up.

Database servers are really an "emerging technology" and the jury is still 
out. Both Oracle and SQL Server support multiple concurrent instances 
although the processing within a given instance may be serially reusable, as 
you noted.
>
>> Not in dispute. Although many people are finding it is cheaper to use
…[27 more quoted lines elided]…
> that the context swapping degrades the total performance.

Sometimes and in some environments, yes. But by no means always. CDC 
mainframes, for example had hardware instructions for context swapping. Most 
OSes support multiple threads which don't always require context swapping 
(depending on the number and use of registers on the platform)  running on a 
single core. Even where context swapping is an overhead, it is usually given 
a priority that ensures any overhead is minimized. Nevertheless, I agree 
there is a point of "diminishing returns" in the example I cited and there 
comes a point where using more workers doesn't improve things.
>
>> This whole subject brings up something I have written about
…[6 more quoted lines elided]…
> then none would have any advantage and the market would be flat.

The fact that most carpenters have no competitive advantage with the hammer 
technology they use does not prevent an infinite diversity in the houses 
they build.

IT is just a tool; it is imagination that builds businesses (and houses...)

>Then
> some bright spark in one of the businesses would come up with the idea
> that offering a discount might get them to sell more. If all
> businesses used the same computer system then it would not cater for
> the changes that businesses use to get an edge.

But it would if it was designed to. Some package vendors make exactly this 
claim.


>While having a set of
> standard rules may be 'desirable' for the software company, it is much
> less so for the clients.
>

And yet increasing numbers of businesses are moving to "standardize" their 
administration around a "standard package". It doesn't seem to stifle their 
business models or their specifc competitive advantages.


> The whole point of having in-house IT is so that the business can
> develop _without_ those procedures becoming available to every other
> business.

That's debatable. You could equally argue that the "whole point" in having 
in-house IT is because that was how it evolved. From a time when there were 
no real packages and the only way to get data processed was to write 
programs to do so. Certiainly, many businesses feel more comfortable with 
"control" of their IT processes but when it becomes outrageously expensive 
then they tend to rethink their options. (See example of Insurance Company I 
noted)

>
>>> I don't think there ever was a time where the "majority of
…[7 more quoted lines elided]…
> have a PC now, but they never had a mainframe.

I believe the OP was talking about specifc large scale industries.

Some fair points and some that are debatable. I don't think OO is the answer 
to "everything" but it is certainly the answer to Networked applications. As 
that is what I am interested in, that's what I tend to be talking about. I 
also believe that eventually the network will consume everything so it makes 
sense to think about it now... :-)

We could argue "serialization of transactions" but I don't disagree strongly 
enough to do so...  There is a often a smugness in mainframe circles that 
nothing can match the mainframe for transaction throughput; it is important 
that the networked alternatives should be noted, especially as this area of 
processing is improving all the time. In terms of cost per transaction a top 
end server network is way better than a mainframe and it brings synergies 
like better failover with it.

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-24T01:37:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vleji8tbqmeilt9p2bbnb2p5i387hu6b03@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net> <9ceafaf2-cb32-47e1-8fde-591d56b77fb2@xb8g2000pbc.googlegroups.com> <aosv8hF2n22U1@mid.individual.net>`

```
On Sun, 24 Feb 2013 11:47:43 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Richard wrote:
>Database servers are really an "emerging technology" and the jury is still 
>out. Both Oracle and SQL Server support multiple concurrent instances 
>although the processing within a given instance may be serially reusable, as 
>you noted.


How in the world are database servers emergent?  All of the serious
ones support multiple concurrent updates, the whole gamut of locking
operations, and whatnot, and have for decades.  Even when database
servers tended not to be on different machines, they still worked that
way (consider a DB2 or IMS region serving many simultaneous programs).


>> 'Throwing' more workers is only useful up to the number of CPU cores
>> available to the program, and often it should be much less. Beyond
…[9 more quoted lines elided]…
>comes a point where using more workers doesn't improve things.


Sure, there's a cost to context switching, but it's usually not that
large, especially given that it almost always happens when a thread
becomes blocked.  If contention between threads causes more blocking
(say the increase in operations against the database server cause
there to be a database disk cache shortage), that sort of over commit
can be a problem.  But usually if you tune things so that you've got
enough parallel work happening to keep your most critical resource
near 100% busy (and not overloaded), the context switching overhead is
immaterial.

Only if you're context switching because the CPU is overloaded, does
that become material, and then only to the extent that time-slice
based context switches actually occur.  On most non-HPC systems,
time-slice based context switches are a small fraction of a percent of
the total number of context switches - and if they're not, it's
probably an indication of other problems.

The hardware based context switch has been reinvented many times.
x86-32 has full support, and there's partial/limited support in
x86-64.  The problem with that is the same every time.  The hardware
facilities are poorly matched to OS needs, and they tend to almost
always be ignored by the OS designers (note that MVS is a bit of an
exception here, but then the hardware facilities were pretty much
designed specifically to support MVS).  In any event, it's not the
nominal task switch itself that's the problem, rather the thrashing of
caches and TLBs that hurts.  Executing a bunch of instructions to save
and reload all the registers is the least of the issues.


>> The whole point of having in-house IT is so that the business can
>> develop _without_ those procedures becoming available to every other
…[8 more quoted lines elided]…
>noted)


This is true.  A few decades ago everyone wrote everything they needed
in house.  These days everything from accounting to sales management
is available for relatively* little, and those packages contain more
functionality than almost any in-house developed system.

To be sure there are specializations that need to happen for some
businesses, particularly very large ones.  But if you were starting a
small bank or insurance company (for example), there's no possible way
you could afford to develop your own systems (either in terms of money
or time).  But then there are a couple of dozen vendors who can see
you a (near) turn-key package, and usually considerable**
customization is possible.  There are even vendors who will outsource
the entire operation for you.  Perhaps that's not viable for a Citi or
Zurich, but not many of us are Citi...

Of course a major exception is businesses whose main product is
information-y.  So big banks might qualify for serious in house
development, but a big car manufacturer mostly does not (except as
related to the products).


*particularly relative to the cost of developing these things in house

**consider SAP as a similar scale package that is highly customizable
- that may be more familiar to many people than the core banking
systems (not that I'm a big SAP fan)
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-25T02:56:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aoukgvFdol5U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net> <9ceafaf2-cb32-47e1-8fde-591d56b77fb2@xb8g2000pbc.googlegroups.com> <aosv8hF2n22U1@mid.individual.net> <vleji8tbqmeilt9p2bbnb2p5i387hu6b03@4ax.com>`

```
Robert Wessel wrote:
> On Sun, 24 Feb 2013 11:47:43 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
>
>> Richard wrote:

No, it was I who wrote the following statement ...
>> Database servers are really an "emerging technology" and the jury is
>> still out. Both Oracle and SQL Server support multiple concurrent
…[4 more quoted lines elided]…
> How in the world are database servers emergent?

I understand your consternation and I was being deliberately provocative. 
:-)

However, it wasn't just mischief; I honestly believe we are going to see 
some major changes in the architecture of RDBMS within the next 10 years.

For some time, I thought embedded SQL was all there was, then I discovered 
LINQ and Lambda statements that enable the manipulation of entire imaginary 
result sets...  In some cases a number of "SQL" statements can be issued and 
they are never actually executed. It's like a whole algebra of result sets 
which enables filtering and refining  simply by manipulating the queries, 
without actually doing them.  The Lambdas allow a complex query to 
represented by a single symbol so it can be easily manipulated. Only at the 
last moment (JIT) is actual access to the DB carried out, and by then it has 
been refined and optimised to be minimal. Only exactly what is needed is 
actually retrieved.

Now, all of this is heady stuff, but it still generates standard SQL. The 
reason it does so is because that's what we have...

But if a new Data Access technology was to come along (and I have reason to 
believe such engines are currently being worked on) then LINQ would still be 
valid and it would just generate different code instead of SQL. It is 
intended for multi-core, multi-threaded access and the fact that it runs 
very well on one or two cores just validates the concept.

If somebody was to build a Content Addressable File storage facility (and 
ICL did many years ago) it could be accessed by LINQ without any change 
being necessary to existing LINQ code. (Obviously, recompilation would be 
necessary, but beyond that, nothing.)

ICL's CAFS could be both content addressable and location addressable but it 
needed a specific query language to use it and it favoured the Networked DB 
model (IDBMS). As the Relational model took over the World, CAFS fell out of 
favour and it was not until the late 1990s that any serious effort was made 
to revive the concept.

(ICL gave it up and then they were taken over by Fujitsu. However, a number 
of companies and individuals have produced some interesting results with 
content addressable stores and it is likely to be revived as a hybrid system 
in the near future. The main thing stopping alternative DB technologies is 
the amazing success of the Relational Model and the SQL it spawned. 
Investment in this worldwide is collossal, so any contender would need to be 
able to leverage the existing SQL...)

CAFS is an example of an idea that was ahead of its time and there wasn't 
the software for it. (The CAF queries were resolved in hardware in the disk 
controller).

Now we have the software (LINQ and Lambdas) which is completely layered 
above the hardware and  SQL and independent of both of them. You could put 
ANY engine under LINQ (including ones we haven't thought of yet :-)) and it 
would continue to work.  It is because the whole algebra of data access has 
been devised and it is independent of any hardware. This stuff is light 
years away from ESQL.

And CAFS is only ONE alternative data repository.  There are others.

For all of these reasons I said that SQL based Relational engines are still 
emerging.

Until they manage to let go of SQL altogether they will not, at least in my 
opinion, have come of age.

However, they ARE what we have at the moment and mostly they serve us pretty 
well. :-)


> All of the serious
> ones support multiple concurrent updates, the whole gamut of locking
…[3 more quoted lines elided]…
>
Yes, what we have today is pretty good. But it has been evolving for 30 
years and there are alternatives (see above)
>
>>> 'Throwing' more workers is only useful up to the number of CPU cores
…[22 more quoted lines elided]…
> immaterial.

My experience on IBM and CDC mainframes confirms this.
>
> Only if you're context switching because the CPU is overloaded, does
…[4 more quoted lines elided]…
> probably an indication of other problems.

Agreed.

>
> The hardware based context switch has been reinvented many times.
…[8 more quoted lines elided]…
> and reload all the registers is the least of the issues.

Especially if the architecture has instructions specifically designed to 
deal with that...

>
>
…[16 more quoted lines elided]…
> functionality than almost any in-house developed system.

Yes, this is one of the things I realized when I first decided to go with 
componet based design. There are people in the World writing components (and 
packages) that encapsulate lifetimes of specialized experience. They provide 
facilities and functionality you may not have even imagined. Life is too 
short to be expert at everything; it is great to be able to get encapsulated 
experience from someone else. I'm grateful for it and appreciate the work 
that goes into some of this stuff...
>
> To be sure there are specializations that need to happen for some
…[19 more quoted lines elided]…
> systems (not that I'm a big SAP fan)

I'm not either :-). But my position is softening... :-) It has improved a 
long way from the package I looked at in Germany in the late 70s. I have a 
friend in Germany who is an ABAPS programmer and she seems to have a fair 
bit of work. I think that all the "Enterprise Packages" (SAP, Siebel, 
Oracle - although Oracle now owns Siebel) have improved immensely since the 
early days and the process is continuing.

Early packages were pretty much a nightmare. That certainly isn't true any 
longer.

Pete.

-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2013-02-25T15:53:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kgg1dm$dci$2@reader1.panix.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <aosv8hF2n22U1@mid.individual.net> <vleji8tbqmeilt9p2bbnb2p5i387hu6b03@4ax.com> <aoukgvFdol5U1@mid.individual.net>`

```
In article <aoukgvFdol5U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>(Obviously, recompilation would be 
>necessary, but beyond that, nothing.)

This strikes my ear as an 'All ya gotta do is...'

Has anyone else ever worked in a shop where recompile = re-test through to 
audit?

DD
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2013-02-26T11:57:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ap28j1F6ot9U1@mid.individual.net>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <aosv8hF2n22U1@mid.individual.net> <vleji8tbqmeilt9p2bbnb2p5i387hu6b03@4ax.com> <aoukgvFdol5U1@mid.individual.net> <kgg1dm$dci$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <aoukgvFdol5U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[11 more quoted lines elided]…
> DD

Yes, you're right.

I guess I should have said: "There is no theoretical reason why you need oto 
do anything other than recompile. In practise, you may find regression 
testing brings some comfort and peace of mind."

Pete.
-- 
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2013-02-26T14:19:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kgiga4$f59$1@reader1.panix.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <aoukgvFdol5U1@mid.individual.net> <kgg1dm$dci$2@reader1.panix.com> <ap28j1F6ot9U1@mid.individual.net>`

```
In article <ap28j1F6ot9U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <aoukgvFdol5U1@mid.individual.net>,
…[17 more quoted lines elided]…
>testing brings some comfort and peace of mind."

When 'brings some comfort and peace of mind' can equate to 'allows one to 
maintain audit compliance/employment/a contract' one might be saying what 
one should have said, aye.

DD
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 10)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2013-02-26T13:12:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joupi85gqub4t9kq8cupgcs47d11afi15a@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <aosv8hF2n22U1@mid.individual.net> <vleji8tbqmeilt9p2bbnb2p5i387hu6b03@4ax.com> <aoukgvFdol5U1@mid.individual.net> <kgg1dm$dci$2@reader1.panix.com> <ap28j1F6ot9U1@mid.individual.net>`

```
On Tue, 26 Feb 2013 11:57:35 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>docdwarf@panix.com wrote:
>> In article <aoukgvFdol5U1@mid.individual.net>,
…[20 more quoted lines elided]…
>Pete.

Regression testing keeps the auditors from knocking on my door!

Regards,
-- 

          ////
         (o o)
-oOO--(_)--OOo-

My Dictionary:  Conference Room: A place where everybody talks, 
nobody listens and everybody disagrees later on.
-- Unknown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 8)_

- **From:** Robert Wessel <robertwessel2@yahoo.com>
- **Date:** 2013-02-26T03:54:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vvoi81tt2dg0d812s7aqh64q2ol0kg6ns@4ax.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net> <9ceafaf2-cb32-47e1-8fde-591d56b77fb2@xb8g2000pbc.googlegroups.com> <aosv8hF2n22U1@mid.individual.net> <vleji8tbqmeilt9p2bbnb2p5i387hu6b03@4ax.com> <aoukgvFdol5U1@mid.individual.net>`

```
On Mon, 25 Feb 2013 02:56:45 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>Robert Wessel wrote:
>> How in the world are database servers emergent?
…[66 more quoted lines elided]…
>well. :-)


There have been numerous attempts to replace the relational model over
the years (OODBMSs has considerable buzz a decade ago, for example),
but the darn thing refuses to die.  There are two problems: First,
most of the non-relational approaches are significantly less general
purpose the RDBMSs, while providing admittedly providing non-trivial
advantages, usually in terms of performance or scalability.  Often
these tie your database scheme to your access methods, which is great,
until you need to change that.  Second, many of the features of the
new systems have been absorbed by RDBMSs over the years, and many of
the tuning options allow a significant part of the replaced
constraints (most commonly relaxation of the strict isolation
constraints) if the application wants that.

So RDBMSs are moving targets, with huge infrastructure and R&D behind
them.  I'm certainly don't have any emotional attachment ot the model,
but at the end of the day, their highly general purpose and flexible
nature provides huge advantages that I'm lothe to give up if I don't
have to.

But by all means keep an eye on the emerging alternatives, especially
for applicatoins those are particularly suited for, but don't bet the
farm on them quite yet.

Nor is SQL all that interesting, or particularly required for RDBMSs.
And in most cases SQL is not really the internal language of the
database, the SQL is invariably parsed into some internal query
structure, and *that's* what then used to build the access plan, etc.
SQL's commonality, though, has much of the same advantages as the
commonality of C, and just like C, SQL has more than a few warts.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 6)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2013-02-24T14:53:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c5742f7f-9c39-471d-a471-bb23aa901cab@y2g2000pbg.googlegroups.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net> <9ceafaf2-cb32-47e1-8fde-591d56b77fb2@xb8g2000pbc.googlegroups.com> <aosv8hF2n22U1@mid.individual.net>`

```
On Feb 24, 11:47 am, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> Richard wrote:
> > On 23 Feb, 20:51, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
…[16 more quoted lines elided]…
> centralized serial reuse is not so superior.

In what way is it not a 'good example' ? While there may be
optimization these are still more expensive than _not_ doing it.

Even in Java serial reuse is advocated for high performance systems.

http://oreilly.com/catalog/javapt/chapter/ch04.html

> The example of the Stock
> Exchange where very high performance and throughput for millions of
> transactions is required, is one that supports my case.

You do not know whether they use serial reuse (from a pool perhaps) or
not, therefore your claim of support is null.


> >>> COBOL on a mainframe supports non-batch transactional processing as
> >>> well (e.g., with CICS).
…[9 more quoted lines elided]…
> CGI is not a "modern" Web Technology.

Perhaps I should have phrased it as "CGI and modern derivatives".

> Although it is effective, it doesn't
> compete with modern server side code alternatives that use code behind to
> dynamically manage web pages. It is about flexibility as well as processing
> and CGI can be a bottleneck where multiple page requests are queued up.

Even CGI uses a pool of reusable servers and adds to the pool to avoid
'queueing up'. For example I use mod_python which is a resident,
reusable, plug-in to Apache that supports a pool of servers.

I assume your 'code behind' is just 'code in page', such as aspx. This
has no benefits over other mechanisms. I dislike 'code in page' as
much as I dislike 'page in code' (eg such things as "print '<html>'").
The UI should be separate from the code, which is why I use templates.

> Database servers are really an "emerging technology" and the jury is still
> out. Both Oracle and SQL Server support multiple concurrent instances
> although the processing within a given instance may be serially reusable, as
> you noted.

They have been 'emerging' for what, 40 years. I don't know of any
serious server that doesn't use a pool of reusable connections for
_performance_ reasons.


> >> Not in dispute. Although many people are finding it is cheaper to use
> >> networked servers to do all of these tasks.
…[28 more quoted lines elided]…
> Sometimes and in some environments, yes.

The example you provided was 'sorting' which will be CPU limited if
core resident or disk access limited if it is disk based or requires
swapping. As disk accesses are serialised (though elevator seeking has
been tried) it is likely that adding more threads beyond a small
number would be counter productive.

> But by no means always. CDC
> mainframes, for example had hardware instructions for context swapping. Most
…[5 more quoted lines elided]…
> comes a point where using more workers doesn't improve things.

So you do agree with me then.

> >> This whole subject brings up something I have written about
> >> elsewhere. Namely the need for a focus on Functionality and not on
…[9 more quoted lines elided]…
> they build.

The 'if' should have indicated to you that this was a hypothetical.

> IT is just a tool; it is imagination that builds businesses (and houses...)

If the tools that are available are limited then imagination may not
be fulfillable. The advantage of being able to build your own tools
are: they can be anything that you can imagine (rather then what is
available in the shops), and the opposition cannot just go to the shop
to buy the same as you have.

So is some carpenter can create a new hammer then he can build houses
faster and/or cheaper than the others who can only buy what is in the
shops.


> >Then
> > some bright spark in one of the businesses would come up with the idea
…[5 more quoted lines elided]…
> claim.

The important point was "if it was designed to". Businesses change,
they are not the same as the business next door, nor are they the same
as they were a year ago. If they are the same - because the software
they use restricts how they can change - then they will be limited how
they will grow.


> >While having a set of
> > standard rules may be 'desirable' for the software company, it is much
…[4 more quoted lines elided]…
> business models or their specifc competitive advantages.

That is because 'accountants' see IT as a cost rather than a business
plan.

In any case I doubt that moving to a 'standard package' actually saves
money. I have observed several moves to SAP that seemed to take
thousands of man-months.

> > The whole point of having in-house IT is so that the business can
> > develop _without_ those procedures becoming available to every other
…[8 more quoted lines elided]…
> noted)


> >>> I don't think there ever was a time where the "majority of
> >>> businesses", that is more than half of all commercial organizations,
…[3 more quoted lines elided]…
> >> town" :-)

I was there in the 60s and started working for a Service Bureau where
the business neither needed to own or lease a mainframe. These days
many businesses use a hosting company rather than owning their own web
servers.


> > The 'majority of businesses' are one or two man operations. They may
> > have a PC now, but they never had a mainframe.
>
> I believe the OP was talking about specifc large scale industries.

The wording was "all commercial organizations". Of course one could
claim that 'the majority of x organizations do ...' where x is the
number that do plus some smaller undefined number.


> Some fair points and some that are debatable. I don't think OO is the answer
> to "everything" but it is certainly the answer to Networked applications. As
…[10 more quoted lines elided]…
> like better failover with it.

Even if you distribute the processing if it is updating a database,
such as bank accounts, then this has to be centralised in some way so
that there is one master instance (which may then be replicated). In
the particular case of bank accounts they need to be serialised so
that the transactions are in the correct datetime sequence, and that
they interact with multiple accounts simultaneously.
```

###### ↳ ↳ ↳ Re: Contrarian view of COBOL

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2013-02-25T15:50:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<kgg18i$dci$1@reader1.panix.com>`
- **References:** `<DIKdnbSXkZ86LIHMnZ2dnUVZ5jSdnZ2d@giganews.com> <ao4874Fg3acU1@mid.individual.net> <74dee3cf-b14a-4561-a6a7-2089ef8fcde4@googlegroups.com> <aoraomFld0rU1@mid.individual.net>`

```
In article <aoraomFld0rU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>David L wrote:

[snip]

>> About 1997, the community-college in the town where I grew up was
>> still teaching COBOL as an "introductory programming" course.  By
…[10 more quoted lines elided]…
>are useful and likely to have a future.

Some might call this view 'narrowly utilitarian', Mr Dashwood... others 
might call it 'utter hogwash'.

Does teaching history have a future?

>
>COBOL can't be justified on those grounds.

It might be frightening to live in a world where choice of language, 
computer or human, would be.

[snip]

>I realised this when I first tried to write a sort in COBOL, WITHOUT 
>employing Fibonacci or Bubble or Tournament.

Not 'would be' or 'might be'... what was the business functionality of 
this exercise and how had the internal SORT, Fibonacci, Bubble and 
Tournament algorithms proven as failures?

Someone might desire to use a torque-wrench as a hammer.

[snip]

>This was one of the most fun programming exercises I have ever 
>undertaken. I spent a week playing with it many years ago and I don't have a 
>copy of it.

Fun's fun, Mr Dashwood... business can be different, at times.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
