[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

_7 messages · 5 participants · 2014-08_

---

### Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2014-08-14T08:54:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com>`

```
CLCers,

Having caught a bit of a recent CSPAN presentation about the Social Security Administration's "troubles" in its rewrite of its computer system for disability payments (Note - NOT retirement benefits), my curiosity was piqued. Seems that five years ago the estimate was completion in 18 - 24 months, and now five years and $300M later, the estimate to completion is... 18 - 24 months.

Googling DCPS (Disability Case Processing System) and SSA uncovers more of the story.

For a brief overview, see...
http://www.cnsnews.com/news/article/social-securitys-300m-it-project-doesnt-work

For a more in-depth "analysis" by the heavyweight consultants McKinsey & Co., see, and click McKinsey analysis here at the bottom of the page ...
http://oversight.house.gov/release/mckinsey-report-288-million-social-security-disability-program-failing-deliver-lacks-leadership/

Some observations...

The McKinsey study of "What Went Wrong" comes up in sideways landscape, and I think you need the full Adobe product to rotate it 90 degrees. I used the poor programmer's option of rotating my notebook screen 90 degrees instead. :-)

Either my version of Adobe is slightly out of date, or there are quite a few pages and portions "redacted", and the entire document has a footer "Pre-Decisional, Confidential, and Proprietary", obviously meant to protect those responsible.

And some opinions...

The project faced VERY serious challenges from the beginning, as its intent was to replace 54 distinct state (and territorial) disability elegibility case management systems with ONE uniform system. That there currently exists 54 systems to determine elegibility is not all that remarkable, since many other social welfare systems such as Temporary Assistance to Needy Families (TANF), Medicaid, and Child Support likewise have individual state variations.

McKinsey pontificates with the usual blather found only in the treatises created by such erudite and high-powered consultants. There are a few interesting gold nuggets to be found however.

Gosh! They tried to use Agile on the project... uh, just not ALL of Agile. Only some of it. Like they didn't use Co-Location, which I think is a synonym for Customer-on-Site. Well, gee, just how DO you co-locate 54 state IT managers into one place?? Oh, and the User Stories and Cases were written by the programmers instead of the Users themselves. Oops. The Study is also critical of HOW MUCH of the work was done on Time & Materials instead of Firm Fixed Price on one page, while on another page bemoans the fact that Agile does not accommodate delineating a sufficient number of requirements up front.

McKinsey's recommendation(s) - a checklist of Agile best practices, showing maybe 15-20% of them used thus far, and a recommendation of changing methodology to raise the Agile-ness up to about 40% by using several more.

But the biggest Laff Riot is on page 39 - with the header:
"SEVERAL PUBLIC SECTOR AGENCIES HAVE SUCCESSFULLY DELIVERED THEIR LARGE IT PROJECTS BY IMPLEMENTING SELECT AGILE PRACTICES" -

with the ENTIRE PAGE REDACTED AND BLANK!!!

Obviously, knowing how to use Agile successfully, and which Federal IT Contractors are capable of so doing, is a _TRADE SECRET_, which certainly must fall under one of the many Exclusionary Exceptions to the Freedom of Information Act.

Oh, and for the gratuitous remark under which I am relieved of using the OT - Off Topic designator, googling DCPS and Java does not turn up any architectural design documents, but it DOES result in a number of resume and LinkedIN entry hits of people who worked their six to nine months on the project using Java, J2EE,and the like, before moving on. Googling DCPS and CoBOL turned up a document justifying current efforts as a way of reducing use of CoBOL.

Ken
```

#### ↳ Re: Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-08-14T21:42:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1e9c9a2c9-p2@usenetarchives.gap>`
- **In-Reply-To:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com>`
- **References:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com>`

```
Ken wrote:
› CLCers,
› 
…[23 more quoted lines elided]…
› notebook screen 90 degrees instead. :-)

Click the Adobe logo at the end of the Adobe bar and request the full
taskbar. Shrink the document to 50% (so you can see what's going on), then
right click and use the rotate option. Once you have it aligned correctly
you can resize to 100% or whatever...

› 
› Either my version of Adobe is slightly out of date, or there are
…[52 more quoted lines elided]…
› Ken

There are many things that are wrong with this project but most of them come
down to lack of leadership and will. It hasn't failed because of Agile
(although even this has been shockingly mis-applied; iteration is the
lifeblood of any Agile approach and the report shows this didn't happen), or
because of any other technology or language. The internal politics were
never addressed and the result is what happens every time this is allowed to
happen. The recommendations are correct that there must be a clear single
authority, responsible for driving it and that authority has to be empowered
to implement what is needed.

The fault here is Management (actually, lack of it...)

Pete.
"I used to write COBOL...now I can do anything."
```

#### ↳ Re: Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2014-08-16T12:20:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1e9c9a2c9-p3@usenetarchives.gap>`
- **In-Reply-To:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com>`
- **References:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com>`

```
Hi, Pete!

Well, yes, I was hoping you would take notice and follow-up, and you did not disappoint me. Thanks tremendously for the Adobe hint. I will try it out.

Trying to figure out what happened by reviewing a "secondary source", i.e., a post-mortem report by another consulting firm, would be especially problematic. I would have much rather had interview access to some senior technical staff, team leaders, and the like.

I would hazard a fair amount has been written about Team Dynamics and the like, but I don't recsll much emphasis being paid to something we might call Sociology of IT Projects, or the Cultural Anthropology of IT Projects. As we Liberal Arts majors learned so many eons ago, societies have all kinds of ways to organize themselves to mutually benefit and/or to accomplish a mission.

"Leadership" can be achieved at any number of levels. I remain a tiny bit skeptical that most or all of the blame for this poor performance can be laid at the feet of the Top Leader.

But then again, I readily admit to my own bias, which is that probably as many projects succeed DESPITE their management as succeed BECAUSE of their management. Or putting it another way, in the Spirit of Empowerment, what could the middle echelons have done to help make the project succeed despite the failure of will/leadership that you refer to?

Glad to dialogue with you again, Pete, I say as I abuse the King's English by turning dialogue from a noun into a verb...

Ken
```

##### ↳ ↳ Re: Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

- **From:** "lkrupp" <ua-author-10879362@usenetarchives.gap>
- **Date:** 2014-08-16T13:13:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1e9c9a2c9-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1e9c9a2c9-p3@usenetarchives.gap>`
- **References:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com> <gap-e1e9c9a2c9-p3@usenetarchives.gap>`

```
On Sat, 16 Aug 2014 09:20:55 -0700 (PDT), Ken
wrote:

› Hi, Pete!
› 
…[11 more quoted lines elided]…
› 

Sociology ... anthropology ... has anyone (re)read Gerald Weinberg's
_The Psychology of Computer Programming_ lately? I see that a Sliver
Anniversary edition was published in 1998. I read the original in
about 1975, and I can't remember if it said anything that might be
relevant to massive conversion projects.

Perhaps the 2nd (2003) edition of Edward Yourdon's _Death March_ would
be more appropriate. :)

Louis
```

###### ↳ ↳ ↳ Re: Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

- **From:** "doctrinsograce" <ua-author-6402540@usenetarchives.gap>
- **Date:** 2014-08-18T10:49:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1e9c9a2c9-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1e9c9a2c9-p4@usenetarchives.gap>`
- **References:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com> <gap-e1e9c9a2c9-p3@usenetarchives.gap> <gap-e1e9c9a2c9-p4@usenetarchives.gap>`

```
On Saturday, August 16, 2014 12:13:19 PM UTC-5, Louis Krupp wrote:
› On Sat, 16 Aug 2014 09:20:55 -0700 (PDT), Ken 
› 
…[52 more quoted lines elided]…
› Louis

Both are wonderful books, especially the former. Over the years I have led a number of teams where Weinberg was mandatory reading.
```

##### ↳ ↳ Re: Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2014-08-16T14:07:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1e9c9a2c9-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1e9c9a2c9-p3@usenetarchives.gap>`
- **References:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com> <gap-e1e9c9a2c9-p3@usenetarchives.gap>`

```
In article <8e46421b-e762-463c-8744-021··b@goo··s.com>,
Ken wrote:

[snip]

› Glad to dialogue with you again, Pete, I say as I abuse the King's
› English by turning dialogue from a noun into a verb...

Last I looked, Mr Shafer, according to my copy of the Compact Edition of
the Oxford English Dictionary (c. 1971, Oxford University Press, 20th
printing, 1981), Page 175, pg 312 (Dialogue - Diamagnetic), col 1, entry
1) 'dialogue' has been used as a verb since 1607... granted that the first
cite is from Shakespeare and Everyone Knows how *he* mangled Our
language... and I am the King of England, God save the Me!

DD
```

##### ↳ ↳ Re: Agile vs. Classical, Java vs. CoBOL, Management vs. Workers ... The Endless Saga Continues

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2014-08-16T21:55:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e1e9c9a2c9-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e1e9c9a2c9-p3@usenetarchives.gap>`
- **References:** `<d26c8d9a-8d88-44d0-acb4-52c6f9ee93e0@googlegroups.com> <gap-e1e9c9a2c9-p3@usenetarchives.gap>`

```
Ken wrote:
› Hi, Pete!
› 
…[18 more quoted lines elided]…
› can be laid at the feet of the Top Leader.

Having worn that hat myself on a number of occasions, I can tell you that
"the buck stops here". If you are not prepared to be responsible for it,
don't take on that job. The "assets" you have are your team and the fact
that you are perceived within the organization as having "power" (whether
you do or not, in reality...); the liabilities are all the things you are
not directly responsible for but must make happen...

Delegation and engagement are two critical things that can help. You have to
be "safe" and people must know they can give you bad news and you won't
shoot the messenger. Your staff have to know they can trust you and that you
will support them and facilitate the achievement of their goals.

The case in point involves probably several thousand people so it is much
more difficult to stay engaged, but the principles are the same. The
"culture" that you want is outlined to your direct reports and you make sure
they implement it.

In the end, it is the responsibility of the Top Leader to make sure it
succeeds. That's what he's paid for...

Doc has sometimes commented here that a "fish rots from the head". Although
I haven't spent a lot of time observing rotting fish, (so I can't be sure
he's right), I can certainly confirm that Senior Management make a HUGE
difference to the success of an Organization. In my career as a consultant I
have worked with CEOs and Managing Directors who were absolutely brilliant,
and I have also worked with ones who were not so good. The difference can be
seen in the Organization. It is the difference between people coming to work
because they have to pay a mortgage and people coming to work because they
get satisfaction and fulfillment from interacting with their colleagues and
achieving workplace goals.

› 
› But then again, I readily admit to my own bias, which is that
…[4 more quoted lines elided]…
› refer to?

A very fair question, and I'll address it thus:

1. It is a primary function of Management, at ANY level to facilitate the
work of their team.

That means clear goals, proper tools, support and training if required. (If
the job will be done by outside contractors, you treat them as if they were
your own team and you make sure that there is a skills transfer to your own
team.)

2. It is the job of management at ANY level to keep politics away from the
ongoing work.

If there are certain peole who don't want what you are doing to succeed, you
sit down with them and understand their objections. If , after fair debate
there is still an impasse and no-one has been persuaded then you escalate
the issues to the next level of Management and if they can't resolve it,
that process gets iterated until the issues are resolved or a different
direction is agreed. (If you are the Top Leader there is no further level to
escalate it to and you must make a call. You will certainly piss someone
off, but if you can't deal with that you are in the wrong job...I find it
helps if I explain the reasons why a certain call is being made, but
sometimes people just feel resentment because they "lost"... this is where
the "culture" I mentioned earlier can make a big difference. If the culture
breeds sulky, petulant, egomaniacs, who take everything personally, then you
need to work on changing the culture... I worked with one CEO who was
inspirational in this regard. He inherited a dispirited, demotivated,
lacklustre work force, whose confidence had been shattered and whose
performance was below average for that industry. Within three years he had
turned it around completely and it was by making sure that there was a
change of culture. No excuses or blaming people, OK to make a mistake as
long as you learn from it, open to all, happy to ask the opinions of people
and listen to them, and making policy decisions that were sensible, fair,
and, ultimately, profitable. But most of all, this particular man valued the
PEOPLE in the organization as the greatest asset he had. (He was unversally
loved by the staff and there were tears when he retired...)

So, given the above, to answer your question: "...what could the middle
echelons have done to help make the project succeed despite the failure of
will/leadership... "

1. Don't accept work that is blatantly pointless or stupid. If you MUST,
then make your reservations known in writing (e-mail is good). These mails
can serve as an audit trail of the bad decisions that were taken by the poor
management and can serve to prevent repetitions of it.

2. Make sure that, even if the overall will is lacking, you keep your team
motivated. Make sure your (and their) objections to policy or tasking are
heard and presented to the next level of management. Try and stop pointless
stuff from going on.

Negotiation and conflict resolution are key skills here and they don't mean
getting what you want at the expense of someone else. (What Von Neumann
refers to as a "zero sum" game). It is about keeping the overall goals in
sight and getting a FAIR resolution towards those goals.

3. Engage the stakeholders and stay engaged with them. Get them to support
your objections and find out what they actually NEED. Ensure this is
translated into IT terms and implemented as far as possible; how will the
professed targets and goals meet these needs?

4. If you intend to use an Agile style of management remember that adherence
to the details of that methodolgy are far less important than actually
delivering useful functionality to the stakeholders. There are 2
fundamental things that must be in place: ITERATION ("How did our last
action work out? Shall we refine it this time around?") and INTERACTION (see
"engagement" above). I have found that, in order to prevent this from
becoming an infinite loop, it is helpful to implement agreed priorites
(MOSCOW) and time boxing.

I think it is fair to say there was no real engagement on the project we are
talking about. That failure is reflected through ALL levels of Management,
although an astute Top Leader would have recognised it early on and
addressed it.

It is easy to be armchair critics.

You could look on it positively as $300,000,000 got disbursed to the
community, but there is little to show for it where it was intended.

Anyone can point fingers and say: "Well, if they had used THIS technology
instead of THAT one, it would have been different...". The fact is that
there is no control experiment to justify such a claim.

In the end, I believe the responsibility lies with the Project Management...
and that was what I said.

›
› Glad to dialogue with you again, Pete, I say as I abuse the King's
› English by turning dialogue from a noun into a verb...

Actually, old chum, it is the QUEEN'S English (at the moment...Gawd Bless
'er!)

And I'm used to Americans murdering it... :-)

Pete.
"I used to write COBOL...now I can do anything."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
