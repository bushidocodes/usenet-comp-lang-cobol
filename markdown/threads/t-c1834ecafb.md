[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol coders: Going, going, gone?

_35 messages · 10 participants · 2008-11 → 2008-12_

---

### Cobol coders: Going, going, gone?

- **From:** Dokorek <info@noster-it.com>
- **Date:** 2008-11-25T00:53:37-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com>`

```
Cobol, that mainstay of business programming throughout the 1960s,
'70s and '80s, is not going away anytime soon. In a Computerworld
survey early this year of IT managers at 352 companies, 62 percent of
the respondents reported that they actively use Cobol. Of those, three
quarters said they use it "a lot" and 58 percent said they're using it
to develop new applications.

Nevertheless, with a few exceptions, companies aren't enthusiastically
expanding their use of Cobol. In the survey, of those who use Cobol,
36 percent said they are "gradually migrating away" from it, 16
percent said they will replace it "every chance we get," and 25
percent said they'd like to replace Cobol with something else but have
found that too difficult or too expensive.


Dokorek
_______
Join the Fastest Growing Emigrants Community - you know Facebook, Xing
or
MySpace, LinkedIn. It exists for emigrants as well:
build contacts, find jobs, friends
http://www.emicountry.com
```

#### ↳ Re: Cobol coders: Going, going, gone?

- **From:** Robert <no@e.mail>
- **Date:** 2008-11-25T08:17:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com>`

```
On Tue, 25 Nov 2008 00:53:37 -0800 (PST), Dokorek <info@noster-it.com> wrote:

>Cobol, that mainstay of business programming throughout the 1960s,
>'70s and '80s, is not going away anytime soon. In a Computerworld
…[3 more quoted lines elided]…
>to develop new applications.

Respondants must define "develop new applications" as maintenance enhancements that add a
few lines of code. Not one of the 15 places where I worked in 11 years was developing a
new application in Cobol. 

>Nevertheless, with a few exceptions, companies aren't enthusiastically
>expanding their use of Cobol. In the survey, of those who use Cobol,
…[3 more quoted lines elided]…
>found that too difficult or too expensive.

That's true. At several companies, my team was asked what it would take to "get rid of
Cobol." We responded with high estimates and heard no more about it. Those companies would
be the 25 percent "too expensive."

The application I'm working on now was rewritten from Cobol to C four years ago. It  still
has environment variables pointing to Cobol libraries that no longer exist. It is in the
36 percent "gradually migrating away."
```

##### ↳ ↳ Re: Cobol coders: Going, going, gone?

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2008-11-25T10:45:25-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e44f0361-1077-4c58-bada-a2706957e6a8@q26g2000prq.googlegroups.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com>`

```
On Nov 26, 2:17 am, Robert <n...@e.mail> wrote:
> On Tue, 25 Nov 2008 00:53:37 -0800 (PST), Dokorek <i...@noster-it.com> wrote:
> >Cobol, that mainstay of business programming throughout the 1960s,
…[21 more quoted lines elided]…
> The application I'm working on now was rewritten from Cobol to C four years ago.

Moving from a language that is 49 years old to one that is 36 years
old.

There was a Datamation article in the 80s that surveyed use of
languages. It found that for Cobol applications a high proportion of
the work was 'maintenance' while for C applications only a small
amount of maintenance was done with most work being 'new development'.

The conclusion was that if Cobol applications were converted to C then
the 'maintenance' cost would reduce.

This, of course, was complete crap. The main reason for the
'maintenance' in applications written in Cobol was changing business
rules, not 'bug fixing'.  Rewrite in C and the business will still
need changes to what the application does.


> It  still
> has environment variables pointing to Cobol libraries that no longer exist. It is in the
> 36 percent "gradually migrating away."
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-11-25T12:37:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6mkoi41cpmi1tg2hv1s8hdvv0ommiuccui@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com> <e44f0361-1077-4c58-bada-a2706957e6a8@q26g2000prq.googlegroups.com>`

```
On Tue, 25 Nov 2008 10:45:25 -0800 (PST), Richard
<riplin@Azonic.co.nz> wrote:

>The conclusion was that if Cobol applications were converted to C then
>the 'maintenance' cost would reduce.
…[4 more quoted lines elided]…
>need changes to what the application does.

I suspect a main reason for companies rewriting CoBOL is the
perception that they will be unable to hire CoBOL programmers in the
future.

But it appears that they may need go back to a much older hiring
strategy - don't expect coding expertise in, say, PeopleCode.   Hire
for general programming competency and good business knowledge.
Programmers will be expected to change tools as the businesses change.

So rewriting CoBOL programs in C won't address their long-term needs
the way they think it will.   It's a solution to the wrong problem,
using obsolete management.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-11-26T12:59:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p3hqaF69598U1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com> <e44f0361-1077-4c58-bada-a2706957e6a8@q26g2000prq.googlegroups.com> <6mkoi41cpmi1tg2hv1s8hdvv0ommiuccui@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 25 Nov 2008 10:45:25 -0800 (PST), Richard
> <riplin@Azonic.co.nz> wrote:
…[12 more quoted lines elided]…
>
Amongst the IT managers I speak with, that is definitely a contributing 
factor, but it is not the main reason.

They are more concerned with COBOL "fitting in" to their future architecture 
(which invariably uses Object approaches).

COBOL is perceived as a "legacy" language. They can't afford to write it 
off, but they don't want to proceed with it either.

There is much more excitement over high level tools like SharePoint 
(personally, I think it sucks, but I know at least one IT manager who sees 
it as the best thing since sliced bread), which allow easy sharing and 
manipulation of data. There is a general "drift" towards web based 
applications, using back end SOA, and there is no place for non-OO COBOL on 
the web. (Yes, you CAN write CGI and even ISAPI code in COBOL (I know 
because I've done it...) but these approaches are being rapidly outdated by 
compiled server-side code running on code-behind pages and controlled by 
Master Pages and CSS. (I've done that too and can confirm it is definitely 
better - in terms of security AND performance...) ASP.NET is a long way from 
the old "brute force" CGI of a few years back.)

The new tools (like SharePoint) and the new environments (.NET using ASP.NET 
is a popular one) are all Object/component based.

Even managers who support disparate systems on disparate platforms are 
realising that there has to be integration at some points. Non-OO languages 
are not easy to integrate. (Why would you want to support downstream data 
feeds through files, when you can pass an object reference in memory and 
directly invoke the behaviours you need?) One solution to this  tomake the 
COBOL stuff a service and then it is much easier to integrate it as part of 
an overall SOA. But sooner or later you are going to have to replace those 
services.

SCENARIO:

You are managing a medium sized site where there are a number of legacy 
COBOL applications which have been wrapped as services and integrate well 
with the remainder of your applications. Your COBOL guys are gone, but the 
apps just run as they always have.

One day a major problem is found that looks like it might require changing 
the underlying COBOL.

What are your options?

1. Buy someone to fix it (if you can get someone).

2. Rewrite that particular service with your current development team.

3. "Bend" the subsequent processing so as to minimise or obviate the 
problem.

As you can see, none of these are particularly attractive options. You start 
to wish you had insisted on the COBOL stuff being converted instead of 
"leveraged", but, at the time, that was an expensive option. Leveraging 
COBOL into services bought you time and caused minimal disruption to the 
business.



Politically, COBOL can be problematic also. On sites where there are COBOL 
teams and other development teams, the COBOL people see themselves as 
"waiting for God" and "second class citizens". (Whether this is real or 
imagined, it is demotivating and definitely counter productive.)  It isn't 
helped by both teams having little common ground, using different 
development methodologies, and speaking a different language. I know a 
couple of managers who will be very glad to see the end of COBOL on their 
sites. Not because there is anything wrong with COBOL as a language, but 
because it is just a constant hassle to try and manage it.)

Their COBOL guys don't want to learn OO COBOL; their Java people see COBOL 
as a primitive backward step.

> But it appears that they may need go back to a much older hiring
> strategy - don't expect coding expertise in, say, PeopleCode.   Hire
> for general programming competency and good business knowledge.
> Programmers will be expected to change tools as the businesses change.

The new generation of programmers are much closer to this description. They 
are not necessarily grounded in a single language or tool but understand 
programming principles and can apply them in nearly any language that is 
based on an OO paradigm. COBOL seems weird to them with esoteric data 
formats, no use of objects, encapsulation, inheritance, or any of the 
fundamentals that OO people take as read, and long-winded procedures.

>
> So rewriting CoBOL programs in C won't address their long-term needs
> the way they think it will.   It's a solution to the wrong problem,
> using obsolete management.

I'd agree with that.  If it were C++, that would be better (because it 
implies they would have completely reviewed the business requirements in 
order toarrive at an object model...), but I still don't see much advantage 
in swapping one old language for another.

Pete.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-11-26T14:07:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ggjl71$8mg$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <e44f0361-1077-4c58-bada-a2706957e6a8@q26g2000prq.googlegroups.com> <6mkoi41cpmi1tg2hv1s8hdvv0ommiuccui@4ax.com> <6p3hqaF69598U1@mid.individual.net>`

```
In article <6p3hqaF69598U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>Howard Brazee wrote:

[snip]

>SCENARIO:
>
…[15 more quoted lines elided]…
>problem.

(and before anyone says 'oh, there's another one of his anti-Management 
digs again'... those who have seen the following please raise a hand, at 
least mentally)

4. Hide/ignore/deny the problem, completely, until I can either retire, 
find another job or (best of all) get promoted so I can publicly belittle, 
sneer at and second-guess the poor idiot who has to clean up my mess... 
all to the accolades of my Senior Management colleagues.

[snip]

>Politically, COBOL can be problematic also. On sites where there are COBOL 
>teams and other development teams, the COBOL people see themselves as 
…[9 more quoted lines elided]…
>as a primitive backward step.

I'd be very interested to see what kind of atmosphere 'their' COBOL guys 
have been placed in and what kind of training/rewards offered on both 
sides of the shop.  At my current client's cite the non-COBOL programmers 
tend to get more training, more visibility, more responsibility and a 
general attitude of 'you're actually getting something done here!' - even 
when what is gotten done is a duplication of errors from the days of 
ENIAC, of course - while the COBOL group is allowed to age, uneducated, 
unadvancing and uninvolved.

Every so often a member of The Other Side will furtively approach my 
cubicle, making sure not to be seen... haltingly mumble out a few 
moderately coherent words and then smile, quizzically.  I'll offer to brew 
a fresh pot of tea and let them watch over my shoulder as I do... stuff, 
there's nothing to hide here... look, green letters on a black background, 
ever seen that before?... might not even need COBOL for this, maybe it can 
be done with DFSort, a fellow named Yaeger took some time, personally and 
generously, to trade emails with someone he knows only anonymously, by the 
UseNet... what's UseNet? oh, just a place where dinosaurs gather, traffic 
there's mostly spam nowadays... nope, multiple indexed files, I happen to 
have a skeleton here... and that goes over *there*... now perform the 
ancient martial-arts manuever called 'Wing That Sucker Off', submitting it 
to the internal reader... what's that?... well, back in the days of punch 
cards a deck had to be physically read into the machine so that... oh, 
your eyes are glazing, lovely weather, isn't it?... and... there ya go, 
let me release those datasets to print... and here's what you wanted, is 
there anything else?

... and then they go away.  One might think, Mr Dashwood, that Management 
might be aware of such capabilities, both human and machine, under Their 
purview, and leverage such things to the best of everyone's advantage...

... and one might think that I am the King of England, too.  God Save the 
Me!

>>
>> So rewriting CoBOL programs in C won't address their long-term needs
…[6 more quoted lines elided]…
>in swapping one old language for another.

I don't know about 'the' advantage, Mr Dashwood, but 'an' advantage to 
Doing It In A Way We Are Accustomed To dates back to... I think somewhere 
around the time of the formation of the medulla oblongata.

Back in the Oldene Dayse one would, quite often, build a computer system 
to mirror the pencil-and-paper system the company used... 'See?  There's 
nothing to be afraid of, it's just like the A529s you fill out every day 
except that it is on a television-screen.'  Never mind that having the 
data in files allows for kinds of manipulation that one cannot do (or can 
do only with great difficulty and much expense) with paper forms... 
imitating the paper is what folks are used to so that's how it is to be 
done.

Then... if a company was Truly Daring they'd replace their indexed files 
with a database set up in a fashion to duplicate the indexed files because 
that's what folks were used to.  Never mind that one gets more capability 
of manipulation if a database is used as a database... imitating the files 
is what folks are used to so that's how it is to be done.

Then... accountants began hauling in their own personal computers (because 
there was no need to purchase such expensive, limited things) and 
structuring spreadsheets... and Lotus had to duplicate a 
date-miscalculation from VisiCalc (or something like that) because one 
considered 1900 to have been a leap-year and the other didn't... never 
mind that 1900 was not, according to standard calculations, not a leap 
year... the numbers didn't come out the way folks were used to so 
imitating the error is how it is to be done.

What folks want, it seems, is new, exciting, unusual and un-thought of 
ways to approach situations... that are *exactly* like the way they've 
always done things... or something like that.  Complicated creatures, 
these human-being-type-folks.

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-11-27T10:25:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p5t65F6g8clU1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <e44f0361-1077-4c58-bada-a2706957e6a8@q26g2000prq.googlegroups.com> <6mkoi41cpmi1tg2hv1s8hdvv0ommiuccui@4ax.com> <6p3hqaF69598U1@mid.individual.net> <ggjl71$8mg$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <6p3hqaF69598U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[32 more quoted lines elided]…
> colleagues.

The point here was for you to consider what YOU might do, Doc.

I'm sorry you are so bitter; obviously someone has given you a real bad time 
somewhere. Focusing on bad management is only valuable if it can be improved 
by doing so. The above doesn't do that (in fact, it won't change 
anything...).

The behaviour you describe does happen because there are poor managers who 
also happen to be poor Human Beings. I am genuinely sorry you have been 
scarred by such. Maybe in time, you'll not be working in "sick shops" and 
some good experience with some decent management may help the healing 
process for you. Good managers do exist, as well as bad ones. But the ones 
who affect us most are the ones we remember.

>
> [snip]
…[23 more quoted lines elided]…
>

Sounds pretty much like what I described.

> Every so often a member of The Other Side will furtively approach my
> cubicle, making sure not to be seen... haltingly mumble out a few
…[20 more quoted lines elided]…
> everyone's advantage...

Virtue is its own reward, Doc. No-one ever regretted acting professionally 
and it may well be that your actions are noticed even if not acknowledged.

I would strongly agree that management which allows an Us and Them 
perception when everyone is working for the same company, is poor. And if 
they don't acknowledge and encourage people then they would appear to be 
missing some of the fundamentals.

Your actions in "helping the enemy" are a step in the right direction 
towards changing this.
>
> ... and one might think that I am the King of England, too.  God Save
> the Me!


>
>>>
…[42 more quoted lines elided]…
>

Yes...complicated indeed. : - )

Pete.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-11-27T15:31:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ggmeh5$6gl$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p3hqaF69598U1@mid.individual.net> <ggjl71$8mg$1@reader1.panix.com> <6p5t65F6g8clU1@mid.individual.net>`

```
In article <6p5t65F6g8clU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <6p3hqaF69598U1@mid.individual.net>,
…[35 more quoted lines elided]…
>The point here was for you to consider what YOU might do, Doc.

I'm not quite certain what languages are common in the Antipodes, Mr
Dashwood... but in English as she is spoke in many places 'you' can be
either a direct address of a second person OR a substitute for the more
generic 'one', especially in hypothetical situations.  I was seeing it
used as the latter; my apologies if I misinterpreted.

>
>I'm sorry you are so bitter; obviously someone has given you a real bad time 
>somewhere. Focusing on bad management is only valuable if it can be improved 
>by doing so. The above doesn't do that (in fact, it won't change 
>anything...).

Mr Dashwood, fire can warm and fire can burn.  To ignore either is, I 
would say, Not A Good Idea.

Management can help and management can hinder.  To be ignorant of the 
symptoms of both is, I would say, a lack of knowledge.

>
>The behaviour you describe does happen because there are poor managers who 
>also happen to be poor Human Beings.

I'll take that as a 'raising of your hand'... so at least one other person 
has seen what I've described.

>I am genuinely sorry you have been 
>scarred by such.

Mr Dashwood, no need to feel sorry for my experiences... and I, 
personally, don't trust the experience of anyone who has worked with sharp 
tools who does not carry a few scars.

>Maybe in time, you'll not be working in "sick shops" and 
>some good experience with some decent management may help the healing 
>process for you. Good managers do exist, as well as bad ones. But the ones 
>who affect us most are the ones we remember.

That I have seen sickness, Mr Dashwood, and that I have learned to 
recognise the symptoms of it might not be signs of sickness in myself... 
that you see it as such might say something about your own view.  The life 
I've chosen requires me to be able to land on my feet in *any* kind of 
shop, sick or healthy, at *any* time... and I've been getting away with it 
for a few decades now.  Let others make of the crumbs I post what they 
may.

[snip]

>>> Their COBOL guys don't want to learn OO COBOL; their Java people see
>>> COBOL as a primitive backward step.
…[11 more quoted lines elided]…
>Sounds pretty much like what I described.

No, Mr Dashwood... it is not, in that the COBOL folks *want* to learn new 
things and they *want* to participate in the changes.  Two guesses as to 
what stops them.

[snip]

>> One might think, Mr Dashwood, that
>> Management might be aware of such capabilities, both human and
…[4 more quoted lines elided]…
>and it may well be that your actions are noticed even if not acknowledged.

Mr Dashwood, no matter what the quality of the shop or the skills I am 
paid to apply... I Sign My Work.  What I am permitted to do is noticed and 
acknowledged; I've actually had folks, after Big Meetings, say 'You're 
(name)?  I've heard of you in other meetings... quite the reputation you 
have here' or the like.

My response is always 'Oh, they'se jes' easily impressed... there's other 
stuff I can do, as well, and I only hope to be given the chance to do it.'

>I would strongly agree that management which allows an Us and Them 
>perception when everyone is working for the same company, is poor. And if 
>they don't acknowledge and encourage people then they would appear to be 
>missing some of the fundamentals.

I carry a photocopy in my briefcase of an article from Fortune Magazine 
entitled 'How I Would Turn Around GM' by H Ross Perot... lovely scree, 
even if it could never be applied.

>
>Your actions in "helping the enemy" are a step in the right direction 
>towards changing this.

Hmmm... a 'a bitter, scarred man' who 'helps the enemy' to Get The Job 
done and has done so for decades... good thing there are authors so 
creative as to invent such characters, none could exist in Real Life.

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-11-28T14:54:48+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p91b9F6oplrU1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p3hqaF69598U1@mid.individual.net> <ggjl71$8mg$1@reader1.panix.com> <6p5t65F6g8clU1@mid.individual.net> <ggmeh5$6gl$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <6p5t65F6g8clU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[44 more quoted lines elided]…
>

Sorry, can't buy that.  It was clear and unambiguous from the use of :

SCENARIO:

YOU are  ... (My emphasis) Substituting "one" simply doesn't work.

I really don't mind you getting it wrong, but don't ascribe your mistake to 
Antipodean usage. I take my English seriously.
>>
>> I'm sorry you are so bitter; obviously someone has given you a real
…[8 more quoted lines elided]…
> symptoms of both is, I would say, a lack of knowledge.

I have no disagreement with the above. But when there is focus only on one 
side, then lack of balance is even more ignorant.

>
>>
…[4 more quoted lines elided]…
> person has seen what I've described.

Yes, it was intended as such.

>
>> I am genuinely sorry you have been
…[4 more quoted lines elided]…
> sharp tools who does not carry a few scars.

I mean it. It seems sad to me that someone as demonstrably witty, 
knowledgeable, and refreshing in so many ways as yourself, just sees a red 
mist when this subject is discussed.

It's one thing to blow off steam about something, we all do that. But in 
your case, I have NEVER seen a post that grants anything to any manager you 
have ever worked with. Lack of balance? Or is that the reality for you?

If the latter, then as a sometime manager I feel sad at whatever it was you 
experienced. It isn't personal sympathy (that would be condescending...) it 
is genuine sadness that some managers really fuck things up, to the point 
were people are deeply affected by it. I would hate to think any of the 
people who have worked with/for me, would leave a project with the same 
feelings you have. I would seriously quit, if I thought that were so.. Some 
of us do the very best we can to ensure that the people we manage are 
actually valued and can enjoy coming to work. I guess being tarred with the 
same brush is distasteful to me. Sometimes, even when you're ("one is") not 
guilty, you (one) can feel bad by association...

If the former, then I have no problem with it. You have a right to be 
unbalanced... : - )

>
>> Maybe in time, you'll not be working in "sick shops" and
…[7 more quoted lines elided]…
> view.

I'm not suggesting you're sick; maybe wounded. Healing can apply to both.

>The life I've chosen requires me to be able to land on my feet
> in *any* kind of shop, sick or healthy, at *any* time... and I've
> been getting away with it for a few decades now.  Let others make of
> the crumbs I post what they may.
>

Fair enough.
> [snip]
>
…[18 more quoted lines elided]…
> guesses as to what stops them.

You would say Management. I would say that if someone is motivated and 
REALLY wants to learn something, then poor management is not going to stop 
them. An individual's career is far too important to leave to ANY 
management, good or bad. Each if us is responsible for the education we get, 
and the career progress we make or don't make.

I remember a very young Operator on a System 360 who read Assembler manuals 
on the night shift and kept pestering everyone to be moved to Programming. 
Finally, just out of sheer persistence, and to try and shut him up, the 
Chief Programmer set him some passages to read and some exercises to do 
based on that reading. This became a regular occurrence and the young man's 
skill grew. When the next programming vacancy became available, they didn't 
even advertise it; the Operator was a shoe-in. There was muttering among 
some of the other Operators who had been there longer and expected to be 
"promoted". (It wasn't helped by the fact that the new appointee was 
immediately sent on a COBOL course...) The other Operators were happy to let 
the process take its course; the young guy wasn't. Was it bad management to 
promote the keen guy and bypass the older hands?  Arguable.

BOTTOM LINE: If you want something, don't sit back. And don't just tolerate 
consistently bad management. Escalate the issues. Do it openly, pointing out 
politely that as no progress is being made and these issues are important, 
there is no option but to escalate.You won't always win, but more often than 
not you'll get a compromise that is way better than what you had. 
Furthermore, senior managers tend to notice lower level managers whose staff 
are always having issues with them.


>
> [snip]
…[14 more quoted lines elided]…
> quite the reputation you have here' or the like.

"Reputation" can be a two-edged sword, Mr. Dwarf... : - )

>
> My response is always 'Oh, they'se jes' easily impressed... there's
…[18 more quoted lines elided]…
> creative as to invent such characters, none could exist in Real Life.

It was your own description that they were "the other side". I believe that 
"enemy" is an acceptable synonym for such? As to you being bitter and 
scarred in matters management, I contend that that is easily deducible from 
your posts here. While in no way diminishng your uniqueness, Doc, it wasn't 
necessary for me to invent you : - )

Pete.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-11-28T16:37:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ggp6ov$ggn$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p5t65F6g8clU1@mid.individual.net> <ggmeh5$6gl$1@reader1.panix.com> <6p91b9F6oplrU1@mid.individual.net>`

```
In article <6p91b9F6oplrU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <6p5t65F6g8clU1@mid.individual.net>,
…[47 more quoted lines elided]…
>Sorry, can't buy that.

I am not selling anything, Mr Dashwood, I am telling you how I interpreted 
your words in accordance with http://www.m-w.com/you 2 or 2a and I 
apologised for my misinterpretation.  Yew want... more?

>It was clear and unambiguous from the use of :
>
…[5 more quoted lines elided]…
>Antipodean usage. I take my English seriously.

You might want to get in contact with those dictionary-folks, then, and 
have them reconsider what they list as definitions.

>>>
>>> I'm sorry you are so bitter; obviously someone has given you a real
…[11 more quoted lines elided]…
>side, then lack of balance is even more ignorant.

Quite so, Mr Dashwood... and that is why I do my best to make sure the 
balance is present.  There's little need for me to supply the parts that 
are already there, I'd say.

>
>>
…[7 more quoted lines elided]…
>Yes, it was intended as such.

I don't understand your difficulty, Mr Dashwood... a scenario is posted, a 
variety of responses are offered for choice and a response you have seen 
happen is left out by you and supplied by another.  What complexities lie 
in so simple an interaction?

>
>>
…[9 more quoted lines elided]…
>mist when this subject is discussed.

Mr Dashwood, there's an interesting argument going on in the United States 
right now about how the automotive companies are going to be treated by 
the government; a segment of the population I've seen - and heard, between 
traffic reports on the radio - seems downright delighted that this is the 
chance to break the back of the Unions which have (despite their declining 
enrollment over the past fifty years) been solely responsible for killing 
the American car industry (their view, not mine).

When I point out that Labor implements plans that were created by 
Management... I get called a 'socialist'.

An organisation is a product of (at least) three branches, Mr Dashwood: 
Executive, Managerial and Labor.  If the cause of a difficulty lies in the 
establishment of the strategic direction of an organisation then it is the 
responsibility of the Executives to remedy it.  If the cause of a 
difficulty lies in the allocation, co-ordination and motivation of 
personnel and resources towards a stated Executive goal then it is the 
responsibility of the Executives or Management to remedy it.

If the cause lies in low-quality workers turning out a substandard 
product... then whose responsibility is it to change the quality of the 
workforce?  Labor does not hire or fire, Labor does a job or quits.

>
>It's one thing to blow off steam about something, we all do that. But in 
>your case, I have NEVER seen a post that grants anything to any manager you 
>have ever worked with. Lack of balance? Or is that the reality for you?

Mr Dashwood, for over a decades I've made it very, very clear that my 
experiences are shaped by working almost universally in what I call 'sick 
shops'... do I nned to document that via DejaNews... errrrr, Google?  I 
can speak from theory, certainly - just completed the PMI course and am 
resting up a bit before getting my cert - but I find it difficult to 
ignore my experience in favor of that.

>
>If the latter, then as a sometime manager I feel sad at whatever it was you 
>experienced. It isn't personal sympathy (that would be condescending...) it 
>is genuine sadness that some managers really fuck things up, to the point 
>were people are deeply affected by it.

Bingo... Mr Dashwood, this is because the scope of Management usually has 
a greater affect than the scope of labor.  *Every* shop has to have a 
bottom-rung programmer, sure... but to make bottom-rung rules the norm for 
the shop, rather than train?  Who benefits from that?  A deep, 
longstanding flaw is exposed by a system's being stretched to its limits 
and it is time for a rewrite... in my experience a Programmer's response 
is 'let's get to the whiteboards and start analysing!' and a Manager's is 
'We don't have the budget/skills/time for that so you'll have to patch 
it... and besides, I'm not Technical but *I* don't see what's so hard 
about it, all ya gotta do is...'

... and so it is with technological change.  It has been decades since 
there's been an Industrial-era need to count noses and recta at an office; 
telecommuting saves everyone time and headaches... yet still, when I 
interview for a contract and ask 'what are your telecommuting policies?' 
the usual response is 'none, you have to be in your seat, pounding your 
keyboard at 9:am on the dot'... and when I ask about flex-time and the 
'core day' the response is often a bitter laugh and 'we asked about that 
years ago and it was shot down... you have to be in your seat, pounding 
your keyboard at 9:am on the dot.'

Programmers do not set such policies, Mr Dashwood... Management does.  
Again, it may be that I work in sick shops but many of them seem to have 
absorbed the most de-humanising aspects of Frederick Winslow Taylor's 'The 
Principles of Scientific Management' as the basis of their 
decision-making.

>I would hate to think any of the 
>people who have worked with/for me, would leave a project with the same 
…[7 more quoted lines elided]…
>unbalanced... : - )

As with any profession, Mr Dashwood, I would say that 10% of the 
practioners have 'the touch'... and the remaining 90% just sort of 'get 
along', living with the uneasiness of suddenly being found out.  If I have 
seen only Kolkatta... errrrrr... Calcutta then I am able to speak, from 
experience, of that... there's not much I can bring to the table about how 
I have seen things done in Stockholm because I just haven't been there.

Likewise with postings, here... my memory is, admittedly, porous but I've 
not often seen a posting of 'Look what I found in a program I was called 
to maintain!  Isn't it beautiful, elegant and a joy to read?'

>
>>
…[10 more quoted lines elided]…
>I'm not suggesting you're sick; maybe wounded. Healing can apply to both.

That I have seen injuries, Mr Dashwood, and that I have learned to 
recognise the limitations caused by them might not be signs of having been 
wounded, myself.  Perhaps I manifest something referred to by my Sainted 
Paternal Grandfather - may he sleep with the angels! - when he said 
'Trains run on time, garbage gets collected, people behave decently... 
this usually doesn't make it into the newspapers.'

[snip]

>>>> I'd be very interested to see what kind of atmosphere 'their' COBOL
>>>> guys have been placed in and what kind of training/rewards offered
…[19 more quoted lines elided]…
>and the career progress we make or don't make.

Mr Dashwood, as your anecdote indicated... Management cannot stop an 
individual from studying, no, but It most certainly *can* stop that person 
from using what they have learned on the job.  Joe Coder can learn all the 
DB2 that there is to know... but if Management does not install DB2 or 
allow Joe to work with the DB2 group then Joe's learning benefits only 
him.

[snip]

>BOTTOM LINE: If you want something, don't sit back. And don't just tolerate 
>consistently bad management. Escalate the issues. Do it openly, pointing out 
>politely that as no progress is being made and these issues are important, 
>there is no option but to escalate.You won't always win, but more often than 
>not you'll get a compromise that is way better than what you had. 

That's not been my experience, Mr Dashwood... but, as noted before, our 
lives are different.  I may have mentioned it before but there was an 
Inter-Group meeting at my present site a while back where one group was 
upgrading from Oracle 8 to Oracle 9i and was short-handed when it came to 
coding test-SQLs to insure compatibility; the Team Lead asked, in public, 
if there was anyone who might be able to help.

I mentioned that I'd been working with SQL for a few decades (DB2 1.4, I 
think... sometime around 1987), that I am a certified Oracle DBA and I 
have a bit of spare time I could apply to this.  The Team Lead thanked me 
and started the process to get me access to their system...

... and was slapped down by the Corner-Office Idiot who, at that time, 
signed my timesheets; I was Not To Be Used for any kind of work outside of 
the mainframe coding I was already doing.  It turned out that the reason 
for this was that there was *another* consulting group - I'm an 
independent, remember - who felt this would be an intrusion on their turf 
and had Contractual Clauses which appeared to support this.

A Good Manager, of course, would renegotiate the contract or wait until it 
expired and make sure the next contract contained no such clauses about 
who works where.  This wasn't done by the then-current Manager, her 
replacement or the replacement which followed that.

[snip]

>> Mr Dashwood, no matter what the quality of the shop or the skills I am
>> paid to apply... I Sign My Work.  What I am permitted to do is
…[4 more quoted lines elided]…
>"Reputation" can be a two-edged sword, Mr. Dwarf... : - )

What's Life without a bit of Risk?  The nail that sticks out gets hammered 
down, of course... and the nail that gets hammered down cannot be used as 
a coat-hook.

[snip]

>>> Your actions in "helping the enemy" are a step in the right direction
>>> towards changing this.
…[6 more quoted lines elided]…
>"enemy" is an acceptable synonym for such?

No more than 'an enemy' is an acceptable synonym for an hypotenuse, Mr 
Dashwood... to a triangle it is just 'the other side'.  Am I getting 
obscure again?

>As to you being bitter and 
>scarred in matters management, I contend that that is easily deducible from 
>your posts here.

Your contention seems to be at variance the original division made in this 
thread between 'the COBOL side' and 'the non-COBOL side'... they are not, 
in my eyes, necessarily in opposition, as enemies, by definition, are.

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 10)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-11-28T20:02:15-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p5t65F6g8clU1@mid.individual.net> <ggmeh5$6gl$1@reader1.panix.com> <6p91b9F6oplrU1@mid.individual.net> <ggp6ov$ggn$1@reader1.panix.com>`

```
On Fri, 28 Nov 2008 16:37:51 +0000 (UTC), docdwarf@panix.com () wrote:

>Likewise with postings, here... my memory is, admittedly, porous but I've 
>not often seen a posting of 'Look what I found in a program I was called 
>to maintain!  Isn't it beautiful, elegant and a joy to read?'

I saw that once, in a C program written by a borrowed 'Java guy'. My attempts to
congratulate him were brushed aside with 'I think he lives in India.' 

It had two layers of abstraction that were just beautiful. It could have been written in
Cobol. Why wasn't it? Therein lies the answer to Cobol's demise .. talented programmers
don't work in Cobol, they were driven out by mediocrities.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-11-29T20:52:27+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6pcalhF7gje7U1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p5t65F6g8clU1@mid.individual.net> <ggmeh5$6gl$1@reader1.panix.com> <6p91b9F6oplrU1@mid.individual.net> <ggp6ov$ggn$1@reader1.panix.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com>`

```
Robert wrote:
> On Fri, 28 Nov 2008 16:37:51 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[12 more quoted lines elided]…
> driven out by mediocrities.

Not at all.

There ARE talented programmers working in COBOL, just like in many other 
languages.

It isn't about mediocrity, it is about the right tools for the job.

There are simply better tools than COBOL for the changed nature of IT 
requirements, and technologies, in this century.

Pete.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 12)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-11-29T05:21:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ob42j4lhtt1eqgbte6rb99sudhnpggoefh@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p5t65F6g8clU1@mid.individual.net> <ggmeh5$6gl$1@reader1.panix.com> <6p91b9F6oplrU1@mid.individual.net> <ggp6ov$ggn$1@reader1.panix.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <6pcalhF7gje7U1@mid.individual.net>`

```
On Sat, 29 Nov 2008 20:52:27 +1300, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>Robert wrote:
>> On Fri, 28 Nov 2008 16:37:51 +0000 (UTC), docdwarf@panix.com () wrote:
…[23 more quoted lines elided]…
>requirements, and technologies, in this century.

I had a friend who went from Cobol programmer in the '70s to Chief Computer Scientist for
a well known search engine company. He advised me to delete the word Cobol from my resume,
said it's the kiss of death in Silicon Valley, I wouldn't be taken seriously.

I didn't take his advice for ten years, during which I worked for some of the worst
'dinosaur' companies. This time I did and now work for a wonderful company. 

He was right.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-11-30T10:51:09+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6pdrqgF7dlh5U1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p5t65F6g8clU1@mid.individual.net> <ggmeh5$6gl$1@reader1.panix.com> <6p91b9F6oplrU1@mid.individual.net> <ggp6ov$ggn$1@reader1.panix.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <6pcalhF7gje7U1@mid.individual.net> <ob42j4lhtt1eqgbte6rb99sudhnpggoefh@4ax.com>`

```
Robert wrote:
> On Sat, 29 Nov 2008 20:52:27 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[38 more quoted lines elided]…
> He was right.

Yes, he was. I would have told you the same thing though probably around 5 
years ago.

(Glad the new job is working out well, BTW...)

I still have my COBOL experience on my CV, but it has been a number of years 
since I was looking for a job, and when I was, it was not for a programming 
job.

I don't think it's about mediocrity of programmers, Robert. I don't even 
think that shops still using COBOL are "wrong", although I am picking up 
more urgency in attempts to get off it. It is about future needs and being 
able to integrate solutions with web based delivery mechanisms. COBOL just 
doesn't fit well in that environment. The Network and the Web belong to 
components and objects. The desktop is also increasingly employing tools 
which are object based. Why would you develop something once for the desktop 
and again for the Intra/Inter NET when, if you use an OO language you can 
write it as a component, do it once and run it anywhere you like?

It is about changing needs and paradigms.

There are "dinosaurs" (both personnel and companies) who just don't see it 
and believe they can go on indefinitely doing the same old same old. Some of 
them are being persuaded that by moving their COBOL to a network platform 
all their worries will be over. But these are the ones who don't see or 
recognise a paradigm shift. Moving standard COBOL to .NET (for example...) 
is like running a z/OS mainframe in 1401 compatibility mode; it buys you 
some time but it doesn't solve your problem. If you continue writing 
procedural code and compiling it to CLR (with tools like .NET COBOL) you are 
NOT getting any real benefit.All you have done is trade one platform for 
another; the benefits you SHOULD have got will continue to elude you.You 
simply have a very powerful environment, which you are constraining so you 
don't get the benefits of it, to run your antiquated applications in. Until 
you present that environment with the objects it was designed for, you are 
no further ahead. Only when the paradigm shift is recognised, can the full 
benefits of the new environment be unleashed.

Pete.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-11-29T12:00:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ggrate$2p6$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p91b9F6oplrU1@mid.individual.net> <ggp6ov$ggn$1@reader1.panix.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com>`

```
In article <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 28 Nov 2008 16:37:51 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[4 more quoted lines elided]…
>I saw that once, in a C program written by a borrowed 'Java guy'.

You saw that once... in how many decades?

[snip]

>Therein lies the answer to Cobol's demise ..
>talented programmers
>don't work in Cobol, they were driven out by mediocrities. 

Gresham's Law, at it again, aye... but I'm not quite sure.  Assuming the 
accuracy of your assertion... COBOL was designed to be maintained, C 
wasn't.  That you can think of such an example out of all the languages 
you've worked in, over all the decades does... something with my point, 
I'm not sure what.

In other News... trains run on time, garbage gets collected, cops arrest 
the right criminal with no trouble at all.

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 12)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-11-30T01:42:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p9c4j492t5tr978af17853ihbp7ag91566@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p91b9F6oplrU1@mid.individual.net> <ggp6ov$ggn$1@reader1.panix.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com>`

```
On Sat, 29 Nov 2008 12:00:47 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com>,
>Robert  <no@e.mail> wrote:
…[8 more quoted lines elided]…
>You saw that once... in how many decades?

Recent memory, ten years.

>>Therein lies the answer to Cobol's demise ..
>>talented programmers
…[6 more quoted lines elided]…
>I'm not sure what.

I know good programming when I see it. Language ooesn't matter. Designed to be is
aftermarket image, not a design goal. Java wasn't designed to be a Web centric language.

>In other News... trains run on time, garbage gets collected, cops arrest 
>the right criminal with no trouble at all.

Mediocrities run trains, collect garbage and catch criminals. You seem to be saying
mediocrity is good enough, or even better. Management thinks so. You sound like a
candidate for management.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 13)_

- **From:** AgustinZabala <agustinza@gmail.com>
- **Date:** 2008-11-30T04:38:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<151288fb-eadb-4e95-b8a9-9dfdd0fb2747@41g2000yqf.googlegroups.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <6p91b9F6oplrU1@mid.individual.net> <ggp6ov$ggn$1@reader1.panix.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com>`

```
COBOL ...!

We are 3.000 Cobol programmers.
Look at http://www.cobol.com.ar

... and the new, last of Microfocus Cobol, free version, (University)
at www.microfocus.com

Regards
Arq. Agustin V. Zabala
Buenos Aires
Argentina


Robert wrote:
> On Sat, 29 Nov 2008 12:00:47 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[32 more quoted lines elided]…
> candidate for management.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-12-01T15:00:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gh0u6p$1hd$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com>`

```
In article <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 29 Nov 2008 12:00:47 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[12 more quoted lines elided]…
>Recent memory, ten years.

... and how many before that?

[snip]

>I know good programming when I see it.

Just like Art, I'm sure... quite the aesthete you seem to hold yourself to 
be, Mr Wagner.

[snip]

>>In other News... trains run on time, garbage gets collected, cops arrest 
>>the right criminal with no trouble at all.
…[3 more quoted lines elided]…
>mediocrity is good enough, or even better.

No, Mr Wagner, what I am saying is that when Things Happen As They Should 
it isn't News.  You seem to be asserting the attitude hinted at by Orwell 
when he said 'I shouthg that only a Socialist could have such contempt for 
ordinary people'.

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 14)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-12-02T00:05:28-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com>`

```
On Mon, 1 Dec 2008 15:00:42 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com>,
>Robert  <no@e.mail> wrote:
…[16 more quoted lines elided]…
>... and how many before that?

A few in books and magazines. Early McCracken was good.

>>I know good programming when I see it.
>
>Just like Art, I'm sure... quite the aesthete you seem to hold yourself to 
>be, Mr Wagner.

Oh shucks, you're just easily impressed.

>>>In other News... trains run on time, garbage gets collected, cops arrest 
>>>the right criminal with no trouble at all.
…[8 more quoted lines elided]…
>ordinary people'.

If you'll reread The Road To Wigan Pier, you'll find Orwell was a fan of socialism. He was
describing British middle class contempt for the working class, and the working class's
contempt for socialists, whom they saw as leftist nonconformists. 

Like Orwell, you're confusing taste with vanity and wrapping both in a bundle labeled
snobbery. The difference is this -- the vain snob has a perception of quality in his own
mind; the craftsman elicits a perception of quality in ANOTHER's mind.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-12-02T21:35:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6pkaatF8fha9U1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com>`

```
Robert wrote:
> On Mon, 1 Dec 2008 15:00:42 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[23 more quoted lines elided]…
> A few in books and magazines. Early McCracken was good.

I have to disagree here, Robert.

McCracken was the "standard" COBOL text for many COBOL courses in Polytechs 
during the 60s and 70s.

I thought it was apalling and I wouldn't use it for teaching purposes.

On the other hand, "COBOL Logic and Programming" by Dr. Fritz D. MacCameron 
of Louisiana State University was light years ahead of McCracken. He gives 
the best explanation of nested IFs and complex PERFORMS that I have ever 
seen before or since, and I still use his approach to explain these things 
to new COBOL programmers when I am required to.

Perhaps beauty is indeed in the eye of the beholder... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 16)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2008-12-02T21:11:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6plmj6F8nde3U3@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com> <6pkaatF8fha9U1@mid.individual.net>`

```
In article <6pkaatF8fha9U1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> Robert wrote:
>> On Mon, 1 Dec 2008 15:00:42 +0000 (UTC), docdwarf@panix.com () wrote:
…[31 more quoted lines elided]…
> I thought it was apalling and I wouldn't use it for teaching purposes.

I thought McCracken was a Fortran guy?  I don't remember ever seeing a
COBOL text by him.  When I was studying COBOL the authority of the day
was Shelley & Cashman.  Of course, that was before I found out they were
professional textbook writers and not IT experts.  :-)

bill
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-12-02T09:38:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gh2vmg$s5h$2@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com>`

```
In article <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com>,
Robert  <no@e.mail> wrote:
>On Mon, 1 Dec 2008 15:00:42 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[20 more quoted lines elided]…
>A few in books and magazines. Early McCracken was good.

So outside of examplles for publication, not from Prod... let's say fewer 
than half-a-dozen times over three decades and change.

What, then, is the rule... and what is the exception?

>
>>>I know good programming when I see it.
…[4 more quoted lines elided]…
>Oh shucks, you're just easily impressed.

Not by that line, I ain't.

>
>>>>In other News... trains run on time, garbage gets collected, cops arrest 
…[12 more quoted lines elided]…
>socialism.

If you read (notice the lack of 're-') later Orwell you might find that 
his views changed.

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 16)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2008-12-02T13:14:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JNfZk.17$tr1.13@newsfe05.iad>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com> <gh2vmg$s5h$2@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:gh2vmg$s5h$2@reader1.panix.com...
> >>>>In other News... trains run on time, garbage gets collected, cops
arrest
> >>>>the right criminal with no trouble at all.
> >>>
…[4 more quoted lines elided]…
> >>No, Mr Wagner, what I am saying is that when Things Happen As They
Should
> >>it isn't News.  You seem to be asserting the attitude hinted at by
Orwell
> >>when he said 'I shouthg that only a Socialist could have such contempt
for
> >>ordinary people'.
> >
…[6 more quoted lines elided]…
> DD

By the time he wrote 1984, Orwell had come to appreciate the gap between
theory and practice of Socialism.  There was just as much selfishness,
factionalism, betrayal, and brutality in "socialist" societies as in any
other.  This was a man who fought on the Socialists' side in the Spanish
civil war, so he knew wherof he spoke - before and after .

PL
>
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-12-02T12:30:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<j23bj4th2boq2jdkvhia7jpvooacop3dso@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com> <gh2vmg$s5h$2@reader1.panix.com> <JNfZk.17$tr1.13@newsfe05.iad>`

```
On Tue, 2 Dec 2008 13:14:36 -0600, "tlmfru" <lacey@mts.net> wrote:

>By the time he wrote 1984, Orwell had come to appreciate the gap between
>theory and practice of Socialism.  There was just as much selfishness,
>factionalism, betrayal, and brutality in "socialist" societies as in any
>other.  This was a man who fought on the Socialists' side in the Spanish
>civil war, so he knew wherof he spoke - before and after .

Which explains both 1984 with its interchangeable states and Animal
Farm with its "some animals are created more equal than others".
Idealism sometimes feels betrayed when people realize that people will
be people.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 17)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-12-03T01:32:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gh4niq$br$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com> <gh2vmg$s5h$2@reader1.panix.com> <JNfZk.17$tr1.13@newsfe05.iad>`

```
In article <JNfZk.17$tr1.13@newsfe05.iad>, tlmfru <lacey@mts.net> wrote:
>
><docdwarf@panix.com> wrote in message news:gh2vmg$s5h$2@reader1.panix.com...
…[22 more quoted lines elided]…
>civil war, so he knew wherof he spoke - before and after .

That is what I attempted to communicate, Mr Lacey... back in the Oldene Dayse 
folks were not only permitted to change their views, it was almost 
expected... as evidenced by Churchhill's 'If you are 18 and not a Socialist, 
you have no heart.  If you are 22 and still a Socialist, you have no brain.'

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 18)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-12-03T08:22:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1r7dj49lnajmvt6b1q6iom477lmgj9f5t0@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com> <gh2vmg$s5h$2@reader1.panix.com> <JNfZk.17$tr1.13@newsfe05.iad> <gh4niq$br$1@reader1.panix.com>`

```
On Wed, 3 Dec 2008 01:32:11 +0000 (UTC), docdwarf@panix.com () wrote:

>That is what I attempted to communicate, Mr Lacey... back in the Oldene Dayse 
>folks were not only permitted to change their views, it was almost 
>expected... as evidenced by Churchhill's 'If you are 18 and not a Socialist, 
>you have no heart.  If you are 22 and still a Socialist, you have no brain.'

One of my favorite quotes.    But I don't have to look to far to find
examples of tolerance today and of intolerance in Oldene Dayse of such
changes.   The veneer of civilization has always been thin.
```

###### ↳ ↳ ↳ [OT] Permissibility of Change? (Re: Cobol coders: Going, going, gone?)

_(reply depth: 19)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-12-04T01:01:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gh7a5d$bns$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <JNfZk.17$tr1.13@newsfe05.iad> <gh4niq$br$1@reader1.panix.com> <1r7dj49lnajmvt6b1q6iom477lmgj9f5t0@4ax.com>`

```
In article <1r7dj49lnajmvt6b1q6iom477lmgj9f5t0@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 3 Dec 2008 01:32:11 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[7 more quoted lines elided]…
>changes.

Eh?  I'm not sure how you intend this, Mr Brazee.  What I gave was an 
example of how one was expected, as a younger person, to think/speak/act 
in political matters as a younger person and then, as an Adult, to put 
away 'childish' things (an even more Anciente Sentiment).  Are you saying 
that this has changed?

DD
```

###### ↳ ↳ ↳ Re: [OT] Permissibility of Change? (Re: Cobol coders: Going, going, gone?)

_(reply depth: 20)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-12-04T07:54:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9mrfj45rb346j57bsd99v3bb39i2hrkslj@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <JNfZk.17$tr1.13@newsfe05.iad> <gh4niq$br$1@reader1.panix.com> <1r7dj49lnajmvt6b1q6iom477lmgj9f5t0@4ax.com> <gh7a5d$bns$1@reader1.panix.com>`

```
On Thu, 4 Dec 2008 01:01:33 +0000 (UTC), docdwarf@panix.com () wrote:

>>>That is what I attempted to communicate, Mr Lacey... back in the Oldene Dayse 
>>>folks were not only permitted to change their views, it was almost 
…[11 more quoted lines elided]…
>that this has changed?

Things like that usually don't change as much as people think.
Different people have always had different ideas on changing views,
about what is acceptable and what is not.
```

###### ↳ ↳ ↳ Re: [OT] Permissibility of Change? (Re: Cobol coders: Going, going, gone?)

_(reply depth: 21)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-12-05T09:22:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gharsa$472$1@reader1.panix.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <1r7dj49lnajmvt6b1q6iom477lmgj9f5t0@4ax.com> <gh7a5d$bns$1@reader1.panix.com> <9mrfj45rb346j57bsd99v3bb39i2hrkslj@4ax.com>`

```
In article <9mrfj45rb346j57bsd99v3bb39i2hrkslj@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Thu, 4 Dec 2008 01:01:33 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[15 more quoted lines elided]…
>Things like that usually don't change as much as people think.

Of course not... or maybe otherwise.  Could you be so kind as to clarify 
what methods you used to arrived at the quantites of 'how much they 
thought then' and 'how much they thought now'?

>Different people have always had different ideas on changing views,
>about what is acceptable and what is not.

The depths of the profundity behind this are... something.

DD
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 15)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-12-02T08:21:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2ikaj4lrv88k02ou1qkbdk2r4biiai86ip@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com>`

```
On Tue, 02 Dec 2008 00:05:28 -0500, Robert <no@e.mail> wrote:

>Like Orwell, you're confusing taste with vanity and wrapping both in a bundle labeled
>snobbery. The difference is this -- the vain snob has a perception of quality in his own
>mind; the craftsman elicits a perception of quality in ANOTHER's mind.

However, there are people without taste who find "quality" in vain
snobs and celebrities.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 16)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2008-12-02T12:12:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f2raj4tetl2orotp1a4sq7ciibh3v0l2nu@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <bd41j45l60nj7t5u4jgov0u3540drpr5c2@4ax.com> <ggrate$2p6$1@reader1.panix.com> <p9c4j492t5tr978af17853ihbp7ag91566@4ax.com> <gh0u6p$1hd$1@reader1.panix.com> <4vd9j4l3ktc187qn0nnosg1gq5o66p9amu@4ax.com> <2ikaj4lrv88k02ou1qkbdk2r4biiai86ip@4ax.com>`

```
On Tue, 02 Dec 2008 08:21:24 -0700, Howard Brazee <howard@brazee.net>
wrote:

>On Tue, 02 Dec 2008 00:05:28 -0500, Robert <no@e.mail> wrote:
>
…[5 more quoted lines elided]…
>snobs and celebrities.

Why else would Paris Hilton be famous?

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I wouldn't recommend sex, drugs, and insanity for everyone, 
but they've always worked for me."
-- Unknown
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-11-26T07:27:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p1nqi4p611uga06j03dbi9diajtm3jt6gd@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com> <e44f0361-1077-4c58-bada-a2706957e6a8@q26g2000prq.googlegroups.com> <6mkoi41cpmi1tg2hv1s8hdvv0ommiuccui@4ax.com> <6p3hqaF69598U1@mid.individual.net>`

```
On Wed, 26 Nov 2008 12:59:09 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>There is much more excitement over high level tools like SharePoint 
>(personally, I think it sucks, but I know at least one IT manager who sees 
>it as the best thing since sliced bread), which allow easy sharing and 
>manipulation of data.

SharePoint is a management tool.   I find it difficult to use, and my
managers keep forgetting to close out documents as well.   In order to
check out a document, we must use I.E., although it is easier to log
on (only once is necessary, and the ID is simpler) using other
browsers.

Lots of paperwork is on SharePoint - and our indexing is turned off,
making it very hard to make sure I've found all of the paperwork I'm
supposed to know.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-11-27T10:33:23+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p5tl5F6jdr9U1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com> <e44f0361-1077-4c58-bada-a2706957e6a8@q26g2000prq.googlegroups.com> <6mkoi41cpmi1tg2hv1s8hdvv0ommiuccui@4ax.com> <6p3hqaF69598U1@mid.individual.net> <p1nqi4p611uga06j03dbi9diajtm3jt6gd@4ax.com>`

```
Howard Brazee wrote:
> On Wed, 26 Nov 2008 12:59:09 +1300, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> supposed to know.

I have limited experience with it although I spent half a day helping a 
SharePoint "expert" get breadcrumbs on the pages. In the end I wrote a Java 
script that did it and the guy was really impressed. If I had known at the 
start of the exercise what I knew by the end of it, I would've immediately 
written the JavaScript and got on with something else. Apparently the system 
was supposed to be able to provide the breadcrumb trail but neither of us 
could get it to do so.

It can be useful and I heard that the later implementations are much better, 
but my own experience is "best avoided"... I was supposed to use it for one 
of the projects I was managing, but I managed not to... We published our own 
pages on the Intranet instead. I think, in retrospect this was not good but 
at the time it made sense.

Pete.
```

##### ↳ ↳ Re: Cobol coders: Going, going, gone?

- **From:** Robert <no@e.mail>
- **Date:** 2008-11-26T23:23:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vdjri4l40mej0emaf643r2ottdhbig4p1s@4ax.com>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com>`

```
On Tue, 25 Nov 2008 08:17:22 -0500, Robert <no@e.mail> wrote:

>The application I'm working on now was rewritten from Cobol to C four years ago. It  still
>has environment variables pointing to Cobol libraries that no longer exist. It is in the
>36 percent "gradually migrating away."

Responses remind me of "Why did the chicken cross the road?" humor in which philosophers
spin the answers within their personal outlooks.

Richard: Complete waste of time and money.
Howard: If they were smart, they'd hire people like me.
Doc: Management screwed up again.
Pete: How ya gonna keep em down on the farm after they've seen OO?

A professional response:
      The company was faced with
      significant challenges to create and develop the competencies
      required for the newly competitive market.  Accenture,
       in a partnering relationship with the client,
      helped the company by rethinking its supply chain 
      strategy and implementation processes. Using the Language 
      Upgrade Benefit Exemplar  (LUBE), Accenture helped the company use its
      skills, methodologies, knowledge capital and experiences to
      align the company's people, processes and technology in support
      of its overall strategy within a Program Management framework.
      Accenture  convened a diverse cross-spectrum of systems 
      engineers and computer scientists along with Andersen consultants with
      deep skills in the information technology industry to engage in a
      two-day itinerary of meetings in order to leverage their
      personal knowledge capital, both tacit and explicit, and to
      enable them to synergize with each other in order to achieve
      the implicit goals of delivering and successfully architecting
      and implementing an enterprise-wide value framework across the
      continuum of application development processes.  The meeting was
      held in a park like setting enabling and creating an impactful
      environment which was strategically based, industry-focused,
      and built upon a consistent, clear, and unified market message
      and aligned with the company's mission, vision, and core
      values. This was conducive towards the creation of a total
      business integration solution using out of the box ideas.
```

###### ↳ ↳ ↳ Re: Cobol coders: Going, going, gone?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-11-28T02:11:52+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p7kkqF6qdefU1@mid.individual.net>`
- **References:** `<cd4fb054-9473-4ecb-a57c-2e57fa91788d@l42g2000yqe.googlegroups.com> <9dsni49smvam81vq57eg4p2s8vb2tlhmog@4ax.com> <vdjri4l40mej0emaf643r2ottdhbig4p1s@4ax.com>`

```
Robert wrote:
> On Tue, 25 Nov 2008 08:17:22 -0500, Robert <no@e.mail> wrote:
>
…[39 more quoted lines elided]…
> ideas.

ROFL!!!

Man, I hope you quoted that from an official document and didn't just make 
it up : - }

Either way, it made ME laugh...

Pete.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
