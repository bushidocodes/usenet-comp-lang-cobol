[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_34 messages · 9 participants · 2013-10 → 2013-11_

---

### (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2013-10-25T14:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com>`

```
On Tuesday, October 22, 2013 2:11:09 AM UTC-4, Ken wrote:
› Dear Mr. HeyBub,
› 
…[4 more quoted lines elided]…
› 
[snip]

Rick Smith Wrote: The title name is "Systemantics" as in 'system' + 'antics'.
<>
A Wikipedia entry for the author is:
< http://en.wikipedia.org/wiki/John_Gall_(author) >

The book title given there is "Systemantics: How Systems Really Work
and [Especially] How They Fail". (title corrected)

That site quotes Gall's Law,
"A complex system that works is invariably found to have evolved from a
simple system that worked. A complex system designed from scratch never
works and cannot be patched up to make it work. You have to start over
with a working simple system. – John Gall (1975, p.71)"

One of Jerry's lists is at,
< https://groups.google.com/d/msg/comp.lang.cobol/EpsUkIy0KfE/z09rDT7ZLbcJ >

In any case, it appears that the implementation problems for the
Affordable Care Act were predicted by Gall's Law!
<>

Forbes is hardly my favorite business magazine, since Fortune, the Wall Street Journal, and Barrons are all better in my opinion, but I found this article on the web from Forbes which is pretty good. It challenges a bit the notion that submissions of updates causes retransmissions of everything (but without sufficient detail to justify that), but more important it highlights difficulties on the so-called "application server" or "database server" side. Noting again that elegibility and identification functions interface with external IRS, Social Security, Veterans Affairs, etc government sites, it goes to suggest that IT WOULD HAVE BEEN FAR BETTER TO COLLECT CLIENT INFO AND MAKE BATCH RUNS AT NIGHT TO INTERACT WITH THOSE EXTERNAL AGENCIES. It might take you a day to learn your errors and correct them, but it would do wonders for the workload. Furthermore, there is evidence that the system allows duplicate social security numbers of covered individuals, meaning incredibly that there is NO requirement for uniqueness of social security ID, a terrible database oversight! Also, there is a hint that the over-hyped "agile" development process was used, with limited "use cases" for test scripts, which for a highly regulated government program, was, in my development experience, an unwise thing to do. This explains why they thought they could do it in only two or three years, because Agile is so much "faster" than traditional / classical development methods. http://www.forbes.com/sites/anthonykosner/2013/10/21/obamacares-website-is-crashing-because-backend-was-doomed-in-the-requirements-stage/
```

#### ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-25T23:48:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p2@usenetarchives.gap>`
- **In-Reply-To:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com>`

```
On Friday, October 25, 2013 2:29:37 PM UTC-4, Ken wrote:
[snip]

› Also, there is a hint that the over-hyped "agile" development process
› was used, with limited "use cases" for test scripts, which for a highly
…[4 more quoted lines elided]…
› http://www.forbes.com/sites/anthonykosner/2013/10/21/obamacares-website-is-crashing-because-backend-was-doomed-in-the-requirements-stage/

It seems to me that the use of "requirements-stage" and "agile" are at
odds. The former being associated with "waterfall" and the latter with
"not waterfall".

In the several articles I read, there was little discussion concerning
the technologies used. I saw mention of HTML and 'tons of' JavaScript for
languages and one mention of an Oracle DB. One AP report mentioned, if
I recall correctly, a 'mind numbing diagram' of the system. These are
hardly enough for me to draw conclusions about the systems; but, if I
didn't have something to say, my response would be wasted.

Was 'agile' used? I think it likely that some of the contractors
used what they would call 'agile'. I think it also likely they used
what they would call 'OO'. I am aware there are some who upon learning
what was done would say "That's not 'agile'!" and "That's procedural
code using an OOPL!". I am also aware that such discussions go nowhere.

My interest is whether XML and XML Schema or XML DTD were used and
whether some functions were separated for SaaS. I expect that I will
never know.
```

##### ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "alistair.j.l.maclean" <ua-author-14501550@usenetarchives.gap>
- **Date:** 2013-10-26T07:04:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p2@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap>`

```
Perhaps the question should be: were any Republican/Tea Party contractors involved in the design and development of the system?
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "swiegand" <ua-author-131803@usenetarchives.gap>
- **Date:** 2013-10-26T11:27:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p3@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p3@usenetarchives.gap>`

```
On Sat, 26 Oct 2013 04:04:12 -0700 (PDT), Alistair Maclean
wrote:

› Perhaps the question should be: were any Republican/Tea Party contractors involved in the design and development of the system?

Good question. Since the contractors appeared before Congress and
threw the administration under the bus for basically not giving them
enough time to test, I'd say it is a possibility. No comment on the
quality of their code, or strength of design or any of the obvious
reason the web site failed.

Like someone said, Toys are Us's web site doesn't crash near Xmas
time; Amazon.Com never crashes around the holidays. The ability to
write a system to handle high volume exists. Apparently these
contractors never worked in that type of environment before.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Definition of - Compromise: The art of dividing a cake in 
such a way that everybody believes he got the biggest piece.
-- Unknown
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-26T10:41:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p2@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap>`

```
On Friday, October 25, 2013 11:48:55 PM UTC-4, Rick Smith wrote:
[snip]

› My interest is whether XML and XML Schema or XML DTD were used and
› whether some functions were separated for SaaS. I expect that I will
› never know.

According to Figure 1: FFE Enrollment Context Diagram, page 6, in
< http://www.cms.gov/CCIIO/Resources/Regulations-and-Guidance/Downloads/companion-guide-for-ffe-enrollment-transaction-v15.pdf >
XML is used internally; but, from additional sources, the EDI ("834")
document transferred to insurance companies is not XML.
```

##### ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "swiegand" <ua-author-131803@usenetarchives.gap>
- **Date:** 2013-10-26T11:23:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p2@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap>`

```
On Fri, 25 Oct 2013 20:48:55 -0700 (PDT), Rick Smith
wrote:

› On Friday, October 25, 2013 2:29:37 PM UTC-4, Ken wrote:
› [snip]
…[28 more quoted lines elided]…
› never know.

The client I am currently assigned to went with the Agile method
earlier last year, so I've had quite a bit of time to work under it. I
hate it. That's all I've got to say.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Definition of - Compromise: The art of dividing a cake in 
such a way that everybody believes he got the biggest piece.
-- Unknown
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-10-26T20:33:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p6@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap>`

```
SkippyPB wrote:
› On Fri, 25 Oct 2013 20:48:55 -0700 (PDT), Rick Smith
›  wrote:
…[3 more quoted lines elided]…
›› 


It is interesting to me to see people here reinforcing their own well
established predujices and supporting their own narrow minded views by
gleeful reference to the failures reported on the Obama web site.

(Agile is an excellent methodology. (I've used something like it for years,
as well as the alternatives, and have an informed opinion about it.))

Anyone who has ever built a complex Web Site (and that excludes most of the
pundits making their pronouncements here) knows that it is a difficult and
time consuming process once you get beyond serving up static pages from a
template. ANY web site CAN fail. The fact that some of the most used ones
on the Net, don't, is a tribute to the PEOPLE who keep them running. It has
little to do with whether they used Agile or PRINCE or Waterfall, or wrote
with Javascript or JSon or anything else.

No matter how much some people here might like it to be so, the failures on
the Obama site are NOT caused by project management methodology or Object
Oriented languages being used. Those same artifacts are used successfully
elsewhere. The fault is with people and poor management. (That kind of
transcends languages and methodologies... Never seen a Waterfalled project
using COBOL fail? Then you haven't been around much...)

Failure of projects using every kind of methodolgy, programming language,
paradigm, and strategy, is splashed in large letters across the history of
IT.


››
›› My interest is whether XML and XML Schema or XML DTD were used and
›› whether some functions were separated for SaaS. I expect that I will
›› never know.

Does it matter?

XML is useful for many things, whether it was used on the Obama site or not.

I'm find increasing uses for it as a transport layer and LINQ to XML is a
great way to manipulate it.

I have been using SOAP for years (which is really a protocol based on XML)
and swearing at it because, for a SIMPLE Object Access Protocol, it is
anything BUT simple. Lately I've stopped swearing at it. It is robust and
useful. The tools are better now and the days of building SOAP envelopes and
bodies by hand are long gone.


›
› The client I am currently assigned to went with the Agile method
› earlier last year, so I've had quite a bit of time to work under it. I
› hate it. That's all I've got to say.

Sorry to hear that, Steve.

I think that sometimes Evangelism has a part to play in these things. There
are aspects of the formal Agile methodology which are NOT really helpful and
can be easily discarded. There are aspects of PRINCE which don't really help
and can also be discarded. And, although we used the Waterfall for decades,
there is no denying it is a technology based on "cover your arse and ensure
that when the shit hits the fan, none of it sticks to you. ["I have your
signature on a document saying you agreed to those useless screen and report
outputs which you now realize don't help at all, and you want changed..."]
(An approach which found ready acceptance by most IT departments who were
much more interested in being seen to be beyond reproach, than in caring
about the level of IT services actually delivered to the Business.)

The fact is that EVERY Project Management methodolgy that has ever been
developed to date, is flawed in SOME way, but people go on a course and come
back with fire in their bellies and the glowing light of enlightenment in
their eyes, and the unshakeable belief that as long as you obey the Holy
Writ and stick to the words of the Mehodology, you will be fine. Don't think
about it; just do it. (And if it fails, the Priests (who are on a nice
little earner spreading the Word while it remains in fashion) will show that
it was because you deviated from the scripture and what you did was just
Sacrilege so no wonder it failed...)

As someone who spent decades in the trenches (and with a track record of
successfully delivered projects, never having failed to bring one in on time
and on budget (although it was a very close thing on a couple of
occasions)), I can tell you there are fundamental principles that DO work.

If you formalize these principles into a rigid set of Commandments and hand
them down from Mount Sinai, as Holy Writ to be followed, then what happens
is that you get Acolytes who don't REALLY understand the principles involved
but follow the letter of the "Law" because it must work. (It doesn't...
There is nothing that is right EVERY time, so there will always be
exceptions... if you understand the principles at work you can understand
how to modify things for the case in point...)

(Understanding trumps rote and dogma every time.)

I have been very fortunate in that many of the projects I have been engaged
to manage were considered lost causes or had already been attempted and
failed. That meant I could negotiate certain privileges, like being able to
override the methodology (if I have to be responsible for what we do, I
have to be allowed to do it as I see fit...) and having access to senior
management to get things facilitated when needed supplies and resources were
blocked, or little empires and political toes were being stepped on. These
are powerful weapons to be used sparingly and effectively, but they mean you
are not constrained by a methodology, instead, you are empowered by it.

It doesn't matter WHAT methodology you use, if you don't have buy-in from
senior management, it can NEVER succeed.

(Politics trumps technology and expertise, every time)

There is a fundamental principle in the Agile approach which makes it
superior to any Waterfall style approach (including PRINCE...): it uses
ITERATION and INTERACTION.

In effect, this means that your solution will evolve in real time and is
therefore much more likely to be closer to what the Business really needs
right now, than what they thought they needed during requirements gathering,
all those months ago...

You don't even attempt to get it "right first time" because experience has
shown that, in the time it takes to design such a solution that has a chance
of being right first time, the requirements have changed, so you will have
to change it anyway...

Instead of "Requirements Gathering" you sit down with the Business (I like
to have "shop floor" end-users in on these sessions, so I prefer JAD (Joint
Application Development) workshops rather than true Agile "scrums") and
LISTEN to what bugs them most about the existing processes and what would
make the biggest difference to them. From these sessions you can develop
deliverables, priorities (MOSCOW), and Use Cases. It isn't Evangelical, it
is common sense. You limit the risk of over-running by using timeboxes and
you interact with the business and iterate development through the
timeboxes.

The business are engaged throughout the process and actually feel like they
are being listened to (because they are...) and the system being delivered
is "theirs". That means IT has to be technically smart (so that changes can
be applied easily and quickly - fortunately, Object Oriented approaches are
much more "change tolerant" than older approaches and that's why I use Obect
modelling... ), and there is job satisfaction for the IT guys in seeing that
they are actually delivering something that is needed and wanted. Everybody
wins.

(And the development language does NOT drive what will be developed; the
FUNCTIONAL requirements do. (No, I'm not talking about a written Functional
Specification; I'm talking about reality...) Although I use object
modellling and identify objects in the JAD sessions, you could develop those
objects with COBOL, Java, C# or anything else. The object description is
designed to support Use Cases and that is FUNCTIONAL, NOT technical...)

Obviously, there is far too much to cover it all here, and I do have a book
I started writing some years back which is sitting in a drawer somewhere and
should probably be updated and published: "The Project Manager's Handbook"
(The danger there is that somebody reads it, decides it makes sense, so they
have a Spiritual Epiphany and before you know it, we have another new
Religion, which is the last thing I wanted...:-))

Despite your comment, Steve, I am persuaded that the Agile approach (even if
not the "letter of the law" in Agile methodology) is a superior one for
managing projects. I'd be interested to hear what turned you off it.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 4)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-27T05:46:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p7@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap>`

```
On Saturday, October 26, 2013 8:33:46 PM UTC-4, Pete Dashwood wrote:
[snip]
›› On Fri, 25 Oct 2013 20:48:55 -0700 (PDT), Rick Smith
››  wrote:
›› [snip]
 
››› My interest is whether XML and XML Schema or XML DTD were used and
››› whether some functions were separated for SaaS. I expect that I will
››› never know.
› 
› Does it matter?
 
› It does to me, hence 'My interest'!
 
› XML is useful for many things, whether it was used on the Obama site or not.

Hence 'My interest', whether it was used at healthcare.gov or not.

And, because there is a 'Native COBOL Syntax for XML Support' document
for implementing XML in COBOL, without regard to whether others have
an interest in using XML with COBOL.
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-10-27T20:12:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p8@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap> <gap-aa36e593de-p8@usenetarchives.gap>`

```
Rick Smith wrote:
› On Saturday, October 26, 2013 8:33:46 PM UTC-4, Pete Dashwood wrote:
› [snip]
…[19 more quoted lines elided]…
› an interest in using XML with COBOL.

Sorry Rick,

I misunderstaood your comment.

Thanks for clarifying.

Pete.

"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 4)_

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2013-10-27T16:38:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p7@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap>`

```
On Saturday, October 26, 2013 8:33:46 PM UTC-4, Pete Dashwood wrote:
› SkippyPB wrote:
› 
…[14 more quoted lines elided]…
› 
 
› As a supporter of the Affordable Care Act, my reaction has not been of glee, but one of disappointment in execution. Seems to me some kind of post mortem is in order, and from the likes of recent Congressional testimony, we certainly won't get much enlightenment from either the politicians or company CEO's or government heads. 
 
› 
› 
…[7 more quoted lines elided]…
› 
At this point we are mostly asking questions.

I do think that the tools you use matter, whether they be programming language, development methodology, or the overall environment. I once got burned on a project in a small company because they chose a real-time operating system (DEC RSX-11M) over a time-sharing operating system (RSTS/E) for a word processing litigation support system! Turned out RSX-11M was based upon a serial communications card WITHOUT CHARACTER LOOKAHEAD, since everything was interrupt-driven-prioritized, and there was no way to capture every character in the customized-to-be-written full screen editor.

Both were fine OS's. But RSTS/E was superior for general-use apps, and RSX-11M was designed for shop floor process control and SCADA (supervisory contol and data acquisition.)


› 
› 
› Failure of projects using every kind of methodolgy, programming language, 
› paradigm, and strategy, is splashed in large letters across the history of 
› IT.
 
› And it is appropriate to ask in each case - were the appropriate tools chosen for THAT KIND OF PROJECT?
 
› 
››› My interest is whether XML and XML Schema or XML DTD were used and
…[4 more quoted lines elided]…
› 
 
› I don't know enough about XML and SaaS to have an opinion. But I understand he is asking, "Were the right tools chosen to do what needed to be done?"
 
› 
›  
…[16 more quoted lines elided]…
› outputs which you now realize don't help at all, and you want changed..."] 

I guess I've worked on a lot of projects and none of them were pure waterfall or pure agile. Most all of them were/are hybrids. But suggesting that the rationale for Waterfall is entirely CYA seems overly cynical for me.

Because mistakes in design are cheaper to correct in design than in code, I think it is worthwhile to spend significant time in what some call Big Up Front Design (BFUD) or something like that. How much is significant and adequate is a judgment call, and that takes the people component that you refer to, Pete. Empirically, I believe it means that you do enough that when you implement it, and changes occur in requirements understanding, then your solution "converges" rather than "churns." For those of you with a math background, you probably recall that an infinite series of addends can either converge to a finite number, or diverge to infinity. A converged software solution is "stable" under change, a divergent software solution will churn, much as described in Jerry's Systemantics.


› 
› 
…[3 more quoted lines elided]…
› occasions)), I can tell you there are fundamental principles that  DO work.

Well, one of the fundamental principles that I learned is to do integration testing and system testing in a TEST ENVIRONMENT. So I was certainly awestruck to hear one of the contractors state (CGI?) that not only was this NOT done, it was NOT even possible!! As if they had never heard of load testing!

And I think it is reasonable to ask, "Where did they ever get that idea? Did they get it from Management? From a perverse interpretation of Agile? Did somebody just forget to write the Integration Use Case on a three-by-five card? :-)

› 
› 
…[5 more quoted lines elided]…
› ITERATION and INTERACTION.

See my comments above regarding Hybrids. I have used Waterfall with so-called Top Down Implementation very successfully, and it is certainly iterative.
And yes, it is important to *some* early results to obtain valuable user feedback. You also get very, very valuable feedback about the interaction between your application and the development and execution environments, where your (hidden and unknown) assumptions are challenged by reality.

› 
› 
…[4 more quoted lines elided]…
› 
 
› On the other hand, I kinow of a multi-million dollar development project where the "new system" failed to perform a valuable function present in the "old system." The "solution" was to change the policy present in the functionality of the old system!  I guess that's one way to "change requirements"! 
 
› 
› You don't even attempt to get it "right first time" because experience has 
…[3 more quoted lines elided]…
› 
 
› Have to disagree here. I believe it is always right to try to best to get "right the first time", even if deep down you know you won't. To do otherwise is to compromise too early.
 
› 
› 
…[6 more quoted lines elided]…
› Religion, which is the last thing I wanted...:-))
 
› Seems to me you must have tried writing that book using the Waterfall method. :-)
 
› 
› Despite your comment, Steve, I am persuaded that the Agile approach (even if 
…[3 more quoted lines elided]…
› Pete.

It's OK, Steve. I am not yet persuaded. What I am persuaded is that the right way is the one that, all factors considered, will be the most effective within the organization that has to use it.

Final aside, and food for thought. Once again, I find it incredible that such a high profile and expensive could have been fielded and rolled out without adequate integration testing, or any real integration testing at all, until it "went live" in production. Is the root cause of this debacle that not enough, not even one, of the many IT professionals did not stand up and say THIS IS MADNESS? If I understand Pete correctly, he seems to suggest it was a management problem, and not a methodology problem. I go further and suggest that, as professionals, it is always our responsibility to "manage our managers" :-), and if this was not done, why wasn't it, and did over-confidence in an Agile methodology contribute to a culture that made it all right to abdicate responsibility? Perhaps the REAL failure was a failure of enough developers of integrity to resign.

Ken
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 5)_

- **From:** "cfmpublic" <ua-author-127808@usenetarchives.gap>
- **Date:** 2013-10-27T17:20:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p10@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap> <gap-aa36e593de-p10@usenetarchives.gap>`

```
On Sun, 27 Oct 2013 13:38:33 -0700 (PDT), Ken
wrote:

› On Saturday, October 26, 2013 8:33:46 PM UTC-4, Pete Dashwood wrote:
›› SkippyPB wrote:
…[17 more quoted lines elided]…
› As a supporter of the Affordable Care Act, my reaction has not been of glee, but one of disappointment in execution. Seems to me some kind of post mortem is in order, and from the likes of recent Congressional testimony, we certainly won't get much enlightenment from either the politicians or company CEO's or government heads. 

One of the major question to ask is when were the rules set in place
and was enough time allowed to implement those rules? I have read
that many were not even out for public review before the 2012
election. Given the systems that needed to be used (various IRS
systems among others), was the design realistic? Before blaming the
grunts and companies involved, I would want to know what the political
masters did. The Affordable Care Act was passed in 2010. The
political landscape was known by the end of 2010. Were the flaws in
the design of the act which even more than much of the legislation in
the modern world are not known until some poor souls attempt to write
the regulations that implement the act so bad that it was impossible
to implement? Were there last minute decisions or last 6 month
decisions that torpedoed the effort?

Clark Morris
› 
›› 
…[125 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-10-27T20:06:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p10@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap> <gap-aa36e593de-p10@usenetarchives.gap>`

```
Ken wrote:


› On Saturday, October 26, 2013 8:33:46 PM UTC-4, Pete Dashwood wrote:
›› SkippyPB wrote:
…[3 more quoted lines elided]…
›› 


It's a good response, Ken, so I have taken a little more time to discuss it
further below...

›› 
›››› 
…[15 more quoted lines elided]…
› from either the politicians or company CEO's or government heads.

So, you want a post mortem, but accept that the people responsible are
unlikely to provide one?

I wouldn't disagree that analysis of failures can often be enlightening and
prevent the same mistakes being made in future, but that analysis has to be
within the constraints of a "blame-free" culture if it is to have any chance
of success.

If analysis is done for the purpose of assigning blame, all that happens is
that the guilty raise smoke and obfuscate what actually happened. Punishing
the guilty, while it may appease the innate desire for revenge in humans,
does not actually improve the situation one jot or tittle. I learned may
years ago to encourage responsibility and let people get it wrong sometimes.
If you have built the right culture, they will beat themselves up enough for
you not to have to do it; instead you help them fix what went wrong. Because
of the sensitive politics around this particular case can you seriously
expect anyone to front up and take responsibility for it?

Another of my fundamental rules on project management: It's not about WHO's
right, it is about WHAT's right.

› 
›› 
…[10 more quoted lines elided]…
› At this point we are mostly asking questions.

MY question is: "WHY?"

If there was a genuine spirit of enquiry I'd be more amenable, but I haven't
seen it in the posts to date.

I don't believe anything posted here will actually help the situation and I
have already watched the discussion descend into a chance to bang away at
modern IT practices, and trot out old prejudices.

If every time a mjor undeertaking fails it is seen simply as a chance to
wave the Luddite banner and bang the "Progress is bad" drum, I really can't
spend time responding to it.


›
› I do think that the tools you use matter, whether they be programming
› language, development methodology, or the overall environment.

That's a fair point, but it is actually trivial in the context. This project
didn't fail because they selected the wrong tools. It wasn't managed
properly and there were insufficient checks and balances to stop it going
off the rails when it first started to. It is a political arena and that
means multiple agendas working for and against it. You could choose any
tools or methodologies you like, but unless someone is made responsible and
answerable, such a project will never succeed.


› I once
› got burned on a project in a small company because they chose a
…[5 more quoted lines elided]…
› character in the customized-to-be-written full screen editor.

So, we can infer that whoever made the decision was not competent to make
it, was ill-advised, or there was some vested interest affecting the
decision making process. Is the problem the Operating System (it's just
software) or the decision making process? Ask yourself...
›
› Both were fine OS's. But RSTS/E was superior for general-use apps,
› and RSX-11M was designed for shop floor process control and SCADA
› (supervisory contol and data acquisition.)

The relative merits of the OSes have no bearing on the case in point UNLESS
there are requirements in the case in point which can only be met by ONE
choice. At that point the choice becomes a no-brainer...
› 
› 
…[7 more quoted lines elided]…
› tools chosen for THAT KIND OF PROJECT?

No, it isn't. And I'll tell you why it isn't...

Unless there is a clearly specifiable requirement (as in the example above)
the tools to be chosen are the very LEAST of your worries if you are
responsible for getting the project successfully concluded.

Without such "unique requirement" the "appropriate tools" come down entirely
to a matter of opinion.

You might as well re-phrase your statement above as:

(When buying a car...)

"And it is appropriate to ask in each case - was the appropriate
colour chosen for THAT KIND OF CAR?"

(If your motivation for buying the vehicle is to impress young members of
the opposite sex, there may be some small significance attached to the
colour and type of vehicle; if your motivation is to have reliable transport
between points A and B, then, whatever your personal opinion about colours
and marques is, it has no bearing on getting a successful outcome.)


IT people, (especially programmers) will ALWAYS go with what they have been
trained in and are comfortable using (quite logical really), WHETHER OR NOT
that particular language is actually the best fit for the job in hand.

To a man with a hammer, everything looks like a nail.

"I can do this in Fortran, so Fortran must be the best tool..."...

In the Obama case there are any number of tools which could be used
successfully to implement the web site.

Which to use is purely a matter of opinion. And that opinion has no bearing
on the success or failure of the project. There are much more important
decisions, much further up the ladder which DO affect the outcome.

A couple of days ago I was asked by a client who wants to take over the
running of his corporate web site (unhappy with the outsourced agency that
currently does it) what tools I would advise he use. His head was spinning
from searching on web development software so he would have preferred that
someone just tell him what to use.

I like to use ASP.NET because it means I can leverage my C# skills into
code-behinds and have a programmer level of control over how things work.
But that hasn't stopped me learning Javascript... Nevertheless, what is fine
for me is not necessarily fine for everyone. Tools like Joomla, and Magenta,
can be excellent for non-programmers to build very effective web sites
quickly and easily. There are a plethora of tools which you CAN use and none
of them are "bad"; whether you get a good site or not does not depend on the
tools (although having good tools that you are comfortable using, can cut
your development time quite significantly.)

Investing a lot of time in whipping cats over the tools or methodolgy used
for Obama Care, is a futile waste of time.

Until such time as the management/responsibility structure (or lack of
it...) is revealed (and my personal bet is that it never will be...),
everything else just adds to the smoke-screen and deflects from the real
causes of the debacle.

› 
›› 
…[10 more quoted lines elided]…
› 

XML is a perfectly good transport for SaaS web services and functions. (I DO
know about this having written a number of them...)

I believe Rick's interest is because XML support has recently been added to
COBOL, rather than XML being at the core of the failure of Obama Care. But
he is here and we don't need ot talk about him like he isn't... :-)

›› 
› 
…[24 more quoted lines elided]…
› 

I never said "entirely", and after 45+ years in this game I have a right to
be cynical... :-)

Despite my "cynicism" (I like to think of it as "reality check") I remain
optimistic generally, and I have been very pleased to see something I
envisioned in the 1960s come to fruition: the access to computer technology
for everyone and not just the technocrat elite. Notwithstanding the
reactionary attitude and resistance to change exhibited by many in the IT
industry, there has been incredible progress.

"Programming" is no longer an obscure mystical ritual known only to the
Priests of COBOL.

Some very bright people have dedicated their lives and careers to stripping
away the veils, making it easier, and getting it within the reach of the
average person who is inclined towards getting to understand their computer.
I've known some of them and I was very lucky to have some of the mentors I
did.

Perhaps that's why I have responded to this thread; it seems to me that any
failure in a modern project is a chance for the Old Guard to say: "See, we
told you this modern stuff doesn't work... if you had listened to us it
would have been fine..."

As if nothing ever failed in the past... :-)

Anyway, in my opinion, the failue of the Obama Care project has nothing to
do with languages or methodologies (they are just an excuse and part of the
smoke-screen to hide the real culprits who are the incompent management that
were supposed to administer and implement it.)


› Because mistakes in design are cheaper to correct in design than in
› code, I think it is worthwhile to spend significant time in what some
› call Big Up Front Design (BFUD) or something like that.

So, just eliminate formal design altogether.

I know... shocking!

But it actually isn't.

There WAS a time when you HAD to design everything. (Believe me, as a young
programmer I remember not being allowed to write any code until I had
produced a flowchart which was checked by a more experienced team member and
it really pissed me off... I wanted to be a "programmer" not a "Space Age
Clerk"... :-)) To compile COBOL took 3 days on that site; card decks had to
be couriered to another place and decks and listings returned, so even a
minor syntax error could set you back 3 days...)

But this is the 21st century... We can sit down with a user at a screen and
drag and drop controls onto a surface until everybody is happy with what
they are seeing. Click a mouse and the code to drive it is generated
instantly. Test it on the spot against a remote test database; don't like
how it works, change it then and there and regenerate it. (The process is
called "prototyping" and it obviates the need for formal design of control
functions on a user interface.)

"Design" in the "Agile" context becomes brainstorming functionality and Use
Cases in joint discussion (JAD workshops, for me) with the end users. IF you
have a capability to quickly and easily change what you have, (and
traditionally we didn't have that capability, but now we do...), then you
can certainly move to "building" stuff instead of "designing" it.

The innate encapsulation that comes from component based object design
allows the same kind of facility with back end (non-user-interface) code.
Brainstorm the required functionality, extract the Classes (objects) needed
to support it and build them quickly. (You don't have to have every
Property, Event, and Method in place, in order to prototype a back-end
Class) Components are small and clearly defined to do what they do; it is
EASY (and quick...) to modify them or enhance them.)

Given you have flexibility in your coding processes, you don't really need
"design" in the old sense...

You simply get core Use Cases working then share the components you built
for them with new spin offs or enhancements... It is asynchronous
development with different teams workng simultaneously on different
processes but sharing components where appropriate. (Source code management
is essential).

The reason we "design" computer systems in this day and age has much more to
do with ingrained habit than with any real requirement to do so.



› How much is
› significant and adequate is a judgment call, and that takes the
…[22 more quoted lines elided]…
› they had never heard of load testing!

I agree, it has been a sad story. But these are all symptoms, not causes.
How was such a situation ALLOWED to happen? WHY did nobody notice it or take
responsibility for it? Those are Management shortcomings, pure and simple.
› 
› And I think it is reasonable to ask, "Where did they ever get that
› idea? Did they get it from Management? From a perverse interpretation
› of Agile? Did somebody just forget to write the Integration Use Case
› on a three-by-five card? :-)
 
› Fair questions. I have stated my position on it.
›› 
…[11 more quoted lines elided]…
› are challenged by reality.

Absolutely. However, you need to timebox the iterations so it doesn't just
go off into the Wild Blue Yonder...

That means clear goals and priorities to be attempted for each timebox. And
an acceptance by all concerned ythat you may not get EVERYTHING in Release
1. (However, what you do get will be prioritised by the users and it will be
useful for them. Once something is working, everybody gets a clearer idea of
where the next priorities are and it is easier to get funding and approval
for phase 2.)
›

I have been constantly agreeably surprised by how understanding users can be
when they are involved in the process. They are very capable of assigning
priorities (after some discussion and argument amongst themselves) and will
work with you to ensure the Must Have priorities for a given timebox are
obtained.

(I often think of a Boss I once had who, when I asked him to prioritise our
workload, said:

"A is top priority."
"B is absolutely critical."
"C has to be done this week."
"... and D mustn't suffer!"

He didn't understand why I burst out laughing; it seemed quite reasonable to
him...)

›› 
›› 
…[10 more quoted lines elided]…
› way to "change requirements"!
 
› You do what you gotta do... :-)
› 
…[9 more quoted lines elided]…
› do otherwise is to compromise too early.

Perhaps I should have rephrased that: "...You don't even attempt to get it
"complete first time"..."

I'm not advocating shoddy workmanship and whatever you actually do, should
be done to the best of your ability. Of course what you produce must be
"right". But the criterion on rightness is decided by the people who will
use it; if they are happy with the functionality, then it is "right"... It
isn't "right" because it is coded in compliance with some precept of
computer science...
› 
›› 
…[11 more quoted lines elided]…
› method. :-)

No, not really... :-) but it was a bit of a self-indulgence and that was why
I shelved it. Perhaps next year I'll produce it... several people in other
forums have expressed interest.
› 
›› 
…[9 more quoted lines elided]…
› most effective within the organization that has to use it.

But that, Ken, is a generalized platitude that says nothing.

Who decides what is "most effective"? It better not be the IT people... :-)
› 
› Final aside, and food for thought. Once again, I find it incredible
…[6 more quoted lines elided]…
› problem, and not a methodology problem.
 
› Yep, that's my take on it.
 
› I go further and suggest
› that, as professionals, it is always our responsibility to "manage
› our managers" :-), and if this was not done, why wasn't it, and did
› over-confidence in an Agile methodology contribute to a culture that
› made it all right to abdicate responsibility?

Agile methodology and "Agile style" approaches (iterative and interactive)
do NOT abnegate responsibility. SOMEONE has to be at the helm, whether it is
a "steering committee" or a PM. Part of the process is to check that what
has been proritised is being achieved. (Usually the JAD teams themselves
will report their own progress because they are proud of it :-)) I use
regular weekly progress meetings to review progress from each team and to
raise problems I can facilitate for them. It is quite amazing (and
gratifying) how momentum and enthusiasm builds as people see things being
produced.




› Perhaps the REAL
› failure was a failure of enough developers of integrity to resign.
›

While I sympahise with the nobility of your professionalism, Ken, it is much
harder when you have landed a very lucrative government contract that looks
like keeping you in beer for the next couple of years and you have a wife,
kids, and a mortgage to take care of.

I don't personally blame the IT people on the project.

I have been "that guy" on at least 3 projects I can think of...I'll quickly
describe just one of them...

1. A major American Bank in London employed Arthur Andersen to "design" a
Forex system that used a new IBM platform that was still on paper.

I was a contractor and a "lead programmer" writing an Assembly language that
no-one had ever seen before (learned by reading the newly printed manual)
and testing on a system 370 emulator. I realized very quickly that the
system would not be capable of handling the projected loads because it
didn't have enough registers to do the necessary switching quickly enough.
The AA guy hadn't even looked at the projected volumes (despite getting paid
for a day what most of us were getting per week). Me, being me, (albeit less
experienced than I am now) I made a fuss about it. AA responded that I was a
nobody programmer who knew nothing, and a troublemaker (arguably true...)
and their guy was an expert so there was nothing to worry about.

The Agency I was working through were pressed to fire me and they terminated
my contract without compunction. (I learned much from this, about Banks,
Agencies, IBM, and Arthur Andersen....) Fortunately, before leaving, I had
expressed my reservations to the IBM site rep who was a young woman who
decided I was worth listening to. She ran some volume simulations back at
IBM and it confirmed what I had said. Too late for me... I was already
looking for another contract (through a different Agency), but you'd think
they would have taken AA to task.

They didn't.

IBM upgraded the hardware adding more registers and memory (on a machine
that was just going into production) but it never worked properly and I
heard the whole lot was replaced by DEC equipment sabout 9 months later.

BOTTOM LINE: If I had kept my mouth shut I would have been spared
humiliation and scorn, plus I could have saved a large sum of money by
staying on a lucrative contract for an extra 9 months...

On other occasions (mostly working as a contract programmer, occasionaly as
a Team Lead) I have spoken up and it has never had a good result (for me...)
but it's like I never learn and can't help myself :-). Fortunately, as my
career progressed and I started moving in more rarefied circles (with direct
access to the Board and often the CEO) I was able to get the ear of people
who matter and can actually influence things. The last couple of whistles I
blew were a good result for everybody (me and the company).

We all like to think we have integrity and will stand against stupidity, but
if you have responsibility to others, and/or have ever been on the bones of
your arse and know what it's like to go hungry, it makes this kind of
decision much more difficult.

I prefer to place the blame (not that I believe in blame as being of any use
at all) where it lies; with the people RESPONSIBLE.

That's the management, not the programmers.

Pete.
"I used to write COBOL...now I can do anything."
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 6)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-28T13:31:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p12@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap> <gap-aa36e593de-p10@usenetarchives.gap> <gap-aa36e593de-p12@usenetarchives.gap>`

```
On Sunday, October 27, 2013 8:06:04 PM UTC-4, Pete Dashwood wrote:
› Ken wrote:
›› On Saturday, October 26, 2013 8:33:46 PM UTC-4, Pete Dashwood wrote:
›› [snip]
›››› On Fri, 25 Oct 2013 20:48:55 -0700 (PDT), Rick Smith wrote:
›››› [snip]
 
››››› My interest is whether XML and XML Schema or XML DTD were used and
››››› whether some functions were separated for SaaS. I expect that I
…[13 more quoted lines elided]…
› he is here and we don't need ot talk about him like he isn't... :-)

I became interested in XML because it was added to COBOL.

Having recently gone through the pages at < http://www.w3schools.com/ >
for XML, XML DTD, XML Schema, and JavaScript, I decided that I don't
like them because ... well ... they are not COBOL.

When the problems with healthcare.gov began receiving a lot of media
attention, I, based on my limited understanding of what the
application must do and current technologies, imagined that
data transfers among the disparate systems might be accomplished
well with XML and Schema for data validation. I also considered
that the calculation of subsidies might be done as a service (SaaS),
since the same calculation would be needed for each of the state-run
exchanges.

So it wasn't so much about "Were the right tools chosen to do what
needed to be done?"; but more were the same tools I chose also chosen
by those building the system. Or, did I guess correctly?

Just for the record, I am exempt from the ACA so whatever happens
with healthcare.gov has no direct effect on me.
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-10-30T19:46:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p12@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap> <gap-aa36e593de-p10@usenetarchives.gap> <gap-aa36e593de-p12@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:

[snip]

› Perhaps that's why I have responded to this thread; it seems to me that any 
› failure in a modern project is a chance for the Old Guard to say: "See, we 
…[3 more quoted lines elided]…
› As if nothing ever failed in the past... :-)

In a similar wise: 'This has never been done before, are you able to tell
us how it will work?' 'No, but some of us might be able to show steps
which, when taken in the past, have almost always resulted in failure.'


DD
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-10-27T16:56:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p7@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p6@usenetarchives.gap> <gap-aa36e593de-p7@usenetarchives.gap>`

```
In article ,
Pete Dashwood wrote:
› SkippyPB wrote:
›› On Fri, 25 Oct 2013 20:48:55 -0700 (PDT), Rick Smith
…[9 more quoted lines elided]…
› gleeful reference to the failures reported on the Obama web site.

Compare and contrast this with 'Victory has many fathers, defeat is an
orphan.' After a half-dozen or so year-end cycles have been completed a
Real Professionl might don boots and wade into matters.

Pretty screens driven by bad data don't help. Pretty screen driven by
good data which have invalid relations built in don't help. Some bugs
take decades to find.

DD
```

##### ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-10-27T16:47:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p2@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap>`

```
In article ,
Rick Smith wrote:
› On Friday, October 25, 2013 2:29:37 PM UTC-4, Ken wrote:
› [snip]
…[12 more quoted lines elided]…
› "not waterfall". 

It seems to me that anyone who turns to Forbes Magazine when it comes to
Learning Serious Stuff about running big systems - Serious Stuff, not 'Bob
has a nice dentist, a good tailor and a stream of really swell jobs lined
up for when this one fails' stuff - deserves what they get.

DD
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2013-10-28T14:55:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p16@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap>`

```
On Sunday, October 27, 2013 4:47:57 PM UTC-4, doc··.@pa··x.com wrote:
› In article 
› 
…[26 more quoted lines elided]…
› DD

Perhaps I should have entered Barrons or Fortune into my google keyword search instead of leaving it "information source neutral". On the other hand, I certainly did not want to exclude any insightful analysis that might have been had from The Drudge Report. :-)

Ken
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 4)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-28T15:36:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p17@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap>`

```
On Monday, October 28, 2013 2:55:49 PM UTC-4, Ken wrote:
[snip]

› Perhaps I should have entered Barrons or Fortune into my google
› keyword search instead of leaving it "information source neutral".
› On the other hand, I certainly did not want to exclude any
› insightful analysis that might have been had from The Drudge Report. :-)

>From Oct 16, 2013,
< http://gcn.com/Articles/2013/10/16/Reality-Check-HealthCaregov-problems.aspx >
"Did agile processes contribute to HealthCare.gov's problems?"

The above references the following:

>From OCTOBER 4, 2013,
< http://talkingpointsmemo.com/cafe/a-programmer-s-perspective-on-healthcare-gov-and-aca-marketplaces >.
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 5)_

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2013-11-02T01:31:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p18@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap> <gap-aa36e593de-p18@usenetarchives.gap>`

```
On Monday, October 28, 2013 3:36:24 PM UTC-4, Rick Smith wrote:
› On Monday, October 28, 2013 2:55:49 PM UTC-4, Ken wrote:
› 
…[10 more quoted lines elided]…
› < http://talkingpointsmemo.com/cafe/a-programmer-s-perspective-on-healthcare-gov-and-aca-marketplaces >.

I read these and thought they were pretty good. Thanks for posting the links.

Ken
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 6)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-11-02T20:05:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p19@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap> <gap-aa36e593de-p18@usenetarchives.gap> <gap-aa36e593de-p19@usenetarchives.gap>`

```
On Saturday, November 2, 2013 1:31:39 AM UTC-4, Ken wrote:
› On Monday, October 28, 2013 3:36:24 PM UTC-4, Rick Smith wrote:
› [snip]
 
›› From Oct 16, 2013,
›› < http://gcn.com/Articles/2013/10/16/Reality-Check-HealthCaregov-problems.aspx >
›› "Did agile processes contribute to HealthCare.gov's problems?"
› [snip]
 
› I read these and thought they were pretty good. Thanks for posting the links.

You're welcome! Though I removed one of the links, there is a new
article by the same author as remaining link, above.
< http://gcn.com/blogs/reality-check/2013/11/healthcare-agile.aspx >
"Media got it wrong: HealthCare.gov failed despite agile practices"

"The bottom line is that those people who claimed that all would
be well if HealthCare.gov had used an agile process are wrong.
The reality is that the developers did use agile, and the project
failed miserably. Before the agile practitioners, fans and
consultants get in an uproar with the chant, “but they did it
wrong,” let me examine some of the facts of what they did and
compare them to some of my recent experiences in requirements
analysis and the design of data integration hubs."

Mr Daconta seems to have answered the question posed in the subject:
Was Agile used in Obama website development? To which the answer is
yes!
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 7)_

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2013-11-02T22:42:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p21@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p20@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap> <gap-aa36e593de-p18@usenetarchives.gap> <gap-aa36e593de-p19@usenetarchives.gap> <gap-aa36e593de-p20@usenetarchives.gap>`

```
On Saturday, November 2, 2013 8:05:03 PM UTC-4, Rick Smith wrote:
› On Saturday, November 2, 2013 1:31:39 AM UTC-4, Ken wrote:
› 
…[27 more quoted lines elided]…
›  analysis and the design of data integration hubs."
 
› Mr Daconta seems to have answered the question posed in the subject:
› Was Agile used in Obama website development? To which the answer is
› 
› yes!

Thank you. A very good article. Which, as usual, leaves me something to comment upon. :-)

If I'd had my druthers, they would have used structured transactional analysis (Larry Constantine) on the data hub back end, rather than the author's recommendation of UML Unified Modeling Language. And just to show how I at least *try* to be fair, use of O-O on the web and gui I think is OK, but structured methods incorporating ERD (entity-relationship-diagramming) for database is, againly only IMO, better for a functional back end requiring performance scalability.

Lost in all this so far is the question - did the federal government follow the usual practice of issuing a very detailed Statement of Work (SOW)? Having worked on a number of (quasi) federal and state projects, this is the second cut of requirements, the first being what is written in the legislative CFR (Code of Federal Regulations, I think it is.)

Ken
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-10-30T19:56:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p17@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap>`

```
In article <937dbbae-64b1-4d16-a7f3-aa9··d@goo··s.com>,
Ken wrote:
› On Sunday, October 27, 2013 4:47:57 PM UTC-4, doc··.@pa··x.com wrote:
›› In article 
…[30 more quoted lines elided]…
› search instead of leaving it "information source neutral".

'Information source neutrality'? Well, what kind of double-talk can you
expect from folks who prefer SECTIONS. When it comes to building a live
system, the likes of which has never been seen... fire up your 16mm
film-projector and watch some of the finest minds the nation could throw
at such stuff generate imploding rockets.

Watch a poor, lost dog wander across Galloping Gertie.

Remember the marvel John Glenn's thrice around the globe.

... and never, NEVER forget that 'got it right the first time' has been
shown by the second go to be mere 'beginner's luck'.

DD
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 5)_

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-31T13:51:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p23@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p22@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap> <gap-aa36e593de-p22@usenetarchives.gap>`

```
On Wednesday, October 30, 2013 7:56:51 PM UTC-4, doc··.@pa··x.com wrote:
[snip]

› Watch a poor, lost dog wander across Galloping Gertie.

Ah! A suitable reference for Halloween.

Tubby, the dog, was the only casualty of the bridge collapse.
His ghost destined to forever 'wander across Galloping Gertie'?
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 5)_

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2013-11-02T01:14:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p24@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p22@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap> <gap-aa36e593de-p22@usenetarchives.gap>`

```
On Wednesday, October 30, 2013 7:56:51 PM UTC-4, doc··.@pa··x.com wrote:
› In article 
› 
…[7 more quoted lines elided]…
› expect from folks who prefer SECTIONS.

I have just learned that including Barrons as a keyword in my google search regarding Obama-site failures would not have improved my search results.
Sadly, the witty and very smart columnist Alan Abelson, who was to the bizness world what Dilbert is to the technical world, has passed on at the ripe age of 87.

A succinct but still impressive biography:

http://online.wsj.com/news/articles/SB10001424127887324244304578473340966230464

He died too soon, for I never learned what he felt about SECTIONS. :-)

Ken
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 6)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-11-02T11:21:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p25@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p24@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p2@usenetarchives.gap> <gap-aa36e593de-p16@usenetarchives.gap> <gap-aa36e593de-p17@usenetarchives.gap> <gap-aa36e593de-p22@usenetarchives.gap> <gap-aa36e593de-p24@usenetarchives.gap>`

```
In article ,
Ken wrote:

› A succinct but still impressive biography:
›
› http://online.wsj.com/news/articles/SB10001424127887324244304578473340966230464
›
› He died too soon, for I never learned what he felt about SECTIONS. :-)

E'en a man who is pyure in haardt...

DD
```

#### ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "dashwood" <ua-author-2154790@usenetarchives.gap>
- **Date:** 2013-10-28T02:32:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p26@usenetarchives.gap>`
- **In-Reply-To:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com>`

```
Ken wrote:
› On Tuesday, October 22, 2013 2:11:09 AM UTC-4, Ken wrote:
››

Readers of this thread might find the following of interest:

http://www.informationweek.com/government/enterprise-architecture/tech-contractors-reject-blame-for-health/240163102

Pete.
"I used to write COBOL...now I can do anything."
```

##### ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "bill" <ua-author-12423647@usenetarchives.gap>
- **Date:** 2013-10-28T07:21:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p27@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p26@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p26@usenetarchives.gap>`

```
In article ,
"Pete Dashwood" writes:
› Ken wrote:
›› On Tuesday, October 22, 2013 2:11:09 AM UTC-4, Ken wrote:
…[5 more quoted lines elided]…
› 

Not necessarily. They rejected the blame for the last project that they
uterly failed on, too.

bill

Bill Gunshannon          |  de-moc-ra-cy (di mok' ra see) n.  Three wolves
bil··9@cs.··n.edu |  and a sheep voting on what's for dinner.
University of Scranton   |
Scranton, Pennsylvania   |         #include
```

#### ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "infodynamics_ph" <ua-author-14501527@usenetarchives.gap>
- **Date:** 2013-10-30T22:15:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p28@usenetarchives.gap>`
- **In-Reply-To:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com>`

```
QSSI Andrew Slavitt

"While the EIDM plays an important role in the registration system, tools developed by other vendors handle critical functions such as the user interface, the e-mail that is sent to the user to confirm registration, the link that the user clicks on to activate the account, and the Web page the user lands on. All these tools must work together seamlessly to ensure smooth registration."

Therefore;

"User interface" would be the culprit on the technical/programming side here. Poor web designers then...

As a 30yrs-experienced programmer here, I am wondering why these things happened? It should not be. Mismanagement of developers pool would be the culprit.
```

##### ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "rs847925" <ua-author-14501579@usenetarchives.gap>
- **Date:** 2013-10-31T13:41:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p29@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p28@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p28@usenetarchives.gap>`

```
On Wednesday, October 30, 2013 10:15:57 PM UTC-4, iNFO_rene wrote:
› QSSI Andrew Slavitt
› 
…[14 more quoted lines elided]…
› would be the culprit.

I am reminded that those who point their finger at others have
three fingers pointing at themselves!
```

##### ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-10-31T18:02:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p30@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p28@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p28@usenetarchives.gap>`

```
In article ,
iNFO_rene wrote:

[snip]

› "User interface" would be the culprit on the technical/programming side
› here. Poor web designers then...
 
› A few more transactions might generate a diferent conclusion.
 
› 
› As a 30yrs-experienced programmer here, I am wondering why these things
› happened? It should not be. Mismanagement of developers pool would be
› the culprit.

It might be something as simple as the Eternal Cause... an idiot
brother-in-law.

DD
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

- **From:** "klshafer" <ua-author-14501353@usenetarchives.gap>
- **Date:** 2013-11-02T01:29:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p31@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p30@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p28@usenetarchives.gap> <gap-aa36e593de-p30@usenetarchives.gap>`

```
On Thursday, October 31, 2013 6:02:42 PM UTC-4, doc··.@pa··x.com wrote:
› In article 
› 
…[5 more quoted lines elided]…
› A few more transactions might generate a diferent conclusion.

As has been accurately reported, even in the mainstream press, an inability to login is a fine way to hide problems that are further "downstream."

Reminds me of when a Systems Analyst on a project which I worked reported programs Unit Test Complete after they ran to normal EOJ on an empty input file.
Developer protestations were not heard. "If a programmer screams in a room of only Bizness Analysts and Managers, does he still make a sound?"

The most charitable thing said by her replacement (yes, after only five or six months, she was replaced) - "She's not incompetent, she's just inexperienced."

› 
›› As a 30yrs-experienced programmer here, I am wondering why these things
›› happened? It should not be. Mismanagement of developers pool would be
›› the culprit.
› 
 
› Uh, it was not incompetence, it was just inexperience. :-)
 
› 
› 
› It might be something as simple as the Eternal Cause... an idiot 
› brother-in-law.

I am appalled at your lack of gender sensitivity, Doc. I would have expected you to use proper moderne Inglish such as "brother-in-law or sister-in-law", or the more preferred "sibling-in-law."

But regardless, I've got your back. Having now divulged in public the Secret of the Eternal Cause of All Screwed Up Things, you can now expect to be charged with favoring the Destruction of The Family.

Your Family of Professional Peers stands shoulder-to-shoulder with you.

Ken
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2013-11-02T11:26:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p32@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p31@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p28@usenetarchives.gap> <gap-aa36e593de-p30@usenetarchives.gap> <gap-aa36e593de-p31@usenetarchives.gap>`

```
In article <9a3e7faf-ddb1-40d1-90f1-ca5··9@goo··s.com>,
Ken wrote:
› On Thursday, October 31, 2013 6:02:42 PM UTC-4, doc··.@pa··x.com wrote:
›› In article 
›› 
›› iNFO_rene  
 
›› [snip]
 
››› As a 30yrs-experienced programmer here, I am wondering why these things
››› happened? It should not be. Mismanagement of developers pool would be
››› the culprit.

Never underestimate a bug's ability to hide. The Ultimate Bug would be
one which would never betray it'sself by execution.

›› 
› 
…[7 more quoted lines elided]…
› I am appalled at your lack of gender sensitivity, Doc.

Really ought to get out more, laddie.

DD
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 5)_

- **From:** "alistair.j.l.maclean" <ua-author-14501550@usenetarchives.gap>
- **Date:** 2013-11-02T12:03:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p33@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p32@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p28@usenetarchives.gap> <gap-aa36e593de-p30@usenetarchives.gap> <gap-aa36e593de-p31@usenetarchives.gap> <gap-aa36e593de-p32@usenetarchives.gap>`

```
On Saturday, 2 November 2013 15:26:31 UTC, doc··.@pa··x.com wrote:
›
› Never underestimate a bug's ability to hide. The Ultimate Bug would be
›
› one which would never betray it'sself by execution.
›

Yep, seen those.
```

###### ↳ ↳ ↳ Re: (OT) Was Agile used in Obama website development?: [Was: An Open Request to HeyBub]

_(reply depth: 4)_

- **From:** "alistair.j.l.maclean" <ua-author-14501550@usenetarchives.gap>
- **Date:** 2013-11-02T12:04:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa36e593de-p34@usenetarchives.gap>`
- **In-Reply-To:** `<gap-aa36e593de-p31@usenetarchives.gap>`
- **References:** `<7b16b92a-f7fc-42df-8f13-2be4f9bd3fbb@googlegroups.com> <gap-aa36e593de-p28@usenetarchives.gap> <gap-aa36e593de-p30@usenetarchives.gap> <gap-aa36e593de-p31@usenetarchives.gap>`

```
On Saturday, 2 November 2013 05:29:09 UTC, Ken wrote:
›
› The most charitable thing said by her replacement (yes, after only five or six months, she was replaced) - "She's not incompetent, she's just inexperienced."
›


I did once know a programmer who considered that a compilation job, in failing to abend, was a sufficiency of testing.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
