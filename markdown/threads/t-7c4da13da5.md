[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] Musings After Go-Live

_7 messages · 4 participants · 2005-06_

---

### [OT] Musings After Go-Live

- **From:** docdwarf@panix.com
- **Date:** 2005-06-23T08:58:53-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9ebmd$4n7$1@panix5.panix.com>`

```

This isn't strictly about COBOL, mind you, hence the [OT].

I subscribe to a listserv for the alumni... alumnae... alumnuoles... folks 
who graduated from my Alma Mater; we all subjected ourselves to an 
uncommon course of study and some of us still keep in contact.  Anyhow, a 
short while back - 27 May, to be precise - I posted the following to the 
list; since traffic here's a bit slow I thought it might provide a bit of 
amusement to those whose job it might be, at time, to deal with such 
things.

--begin quoted text:

From docdwarf@panix.com Fri May 27 09:09:26 2005
Subject: Musings After Go-Live


This might take a while... and it really doesn't go anywhere... so some 
folks might say it fits right in with the rest of my blitherings.

The project I've been working since November '03 went live at the 
beginning of the month.  It's a delicate one, a Federal payroll system 
that cuts checks every other week for about sixty thousand people and has 
a rather primitive design dating back to the late '70s which has been 
modified so that it no longer cuts checks but passes data over to a 
different Federal agency.

Rules for generating paychecks can be exquisitely simple; the following is 
valid COBOL code:

COMPUTE OVERTIME-RATE   =  HOURLY-RATE * 1.5.
COMPUTE REGULAR-GROSS   =  REGULAR-HRS * HOURLY-RATE.
COMPUTE OVERTIME-GROSS  =  OVERTIME-HOURS * OVERTIME-RATE.
COMPUTE GROSS-PAY       =  REGULAR-GROSS + OVERTIME-GROSS.

... and they can be horrifically complex... how do you calculate pay for a 
float-pool nurse from the Indian Health Service who reports regular hours, 
overtime hours, Sunday shift differential and paid holiday time in the 
same 24-hour shift?  (Answer: it depends on whether they are covered by 
the union contract or not.)  Add to this mixture the fact that these are 
peoples' paychecks being dealt with here, just about everyone looks at 
those closely and many are prone to make at least quiet murmurmings if the 
numbers are not to their liking.

(Interchange from a meeting: 'You mean we've been paying these folks 
*wrong* for the past fifteen years?  How did that happen, why didn't 
anyone *say* anything?' 'We coded that according to the specs that came 
down in the '88 revision... and not too many people are going to say 
anything if their paychecks are larger than expected.')

Anyhow... it was a large project and it is has gone live... and 
consultants/contractors/hired guns are starting to be let go.  I, in part, 
am responsible for this... and it makes me feel... odd.

Back in the Oldene Dayse computerising an operation used to make people 
*very* upset... The Computer's Stealing My Job!  I put this into an 
historical perspective... back in the Even More Oldene Dayse the ability 
to add up a long column of figures, accurately and in a legible hand, was 
a valuable skill.  Companies had entire roomsful of clerks, standing at 
their stations, totting up bills of lading with their quills... and these 
clerks had, by the standards of those days, pretty decent jobs; their 
working-conditions were better than those of the laborers, they earned a 
better wage than the laborers and they were granted better social status 
than the laborers.

Then came mechanical tabulating engines... ummmmm, adding-machines... and 
things changed.  One no longer needed the mathematical skills nor the 
ability to maintain penmanship over extended hours, just needed to hit the 
buttons accurately... and output increased, one person hitting buttons 
could wade through a bunch more stuff than several folks writing numbers.

What happened?  If your only skill was the ability to add up long columns 
of figures accurately and present the results in a legible hand... the 
machine took your job.  Computers seem to follow in this tradition.

Now... the system I worked on converting takes input from four feeder 
systems, each of the feeders supplies data in a common format... but each 
of the feeders sends bad data down the line.  As mentioned above the rules 
for paying people vary and what are invalid data for one person might be 
valid for another... rather than doing the Work to make sure that these 
rules are applied on the front-end to provide clean data folks follow Rule 
Number Zero ('Nobody wants to do any work') and send trash down the line. 
The folks who receive the trash complain, of course... but the recipients 
do not have the authority to cause change on the front-ends and are 
subject to the 'touched it last' rule; a pile o' crap gets dumped in their 
laps and it is up to them to make sure that folks get paid so folks don't 
get upset.

Still with me?  What has resulted from this is a sub-group of 
consultants/contractors/hired guns who have as their only job the 
responsibility of taking the incoming data, loading them to small 
databases (Oracle) and dealing with bad data and the resulting 
complaints... something will go wrong, someone will file a trouble-ticket 
and these folks will look at the data and say 'Oh, Timekeeper Joe sent us 
down some trash'... and they'll fix up their data, generate an 
extract-file and send this extract back into the main processing-stream to 
generate corrections.  They're nice people, this sub-group... a small 
company composed of Mr Brahmagupta, his wife, her sister-in-law, a couple 
of other folks from their neighborhood... all competent in what they do 
and pleasant-enough to work with.

Now things have changed.  This agency is no longer cutting the checks, all 
data are being sent to a different Federal agency... so instead of the 
feeder-system files going into these small databases I modified an ungodly 
ugly program to be even more ugly - not too large, a bit more than 15,000 
lines of code, but what it lacks in size it makes up for in 
unattractiveness - to process them and send the data off in order that the 
different agency can deal with them.

My code has rendered the work this sub-group does unnecessary.  Today is 
their last day on-site.

On the one hand... hey, that's the consultant's life, the work comes, the 
work goes, time to find another job.  On the other hand... my work has 
caused other folks to have to look for new jobs.  This makes me feel... 
odd.

On the third hand... the system went live at the beginning of May and 
there are still bugs to be worked out and modifications to be made, some 
consultants are being kept on to deal with this.  Who gets to stay, 
though, depends on what kind of budget can be maintained... and budget 
negotiations are slow, delicate things... and in the meantime contracts 
for consultants are expiring.  This leads to conversations like the one I 
had with a different consultant last week:

Him: Heard anything about renewals?

Me: Not a word... as far as I know my contract expires on the 31th.  I'd 
like to show up for work on the 1st... but nobody can tell me if I'll get 
paid if I do.

Him: Same here... well, is there anyone else who can run the jobs you've 
put together?

Me: Sure, anyone who can read code... my project-leader and I have been 
working together through all of this, he ain't bad at what he does... he 
ain't *me*, of course.  I try to make sure, though, that anything I write 
can be handled by a 2-year programmer... that's just the way I do things.

Him: (superior smirk) That's not always the best for *you*, you know... in 
my case it is different, I don't think there's anyone here who can handle 
what I've put together.

Me: Eh... 'job security throught idiosyncratic knowledge' isn't how I deal 
with things, I pride myself on writing stuff that people will look at and 
say 'This is so *simple*... why did we pay him so much to do it?'

Him: (smirk and head-shake) That's one way to do things... it can make for 
trouble, though, when renewal-time comes.

Word came down about renewals yesterday.  I'm good for another three 
months, at the Final Go-Live Farewell Luncheon yesterday the Project 
Director told me that this was really a stopgap and that once things 
settle there'll be more stuff for me, they want me around for the problems 
that are sure to arise when they close the books for the year in 
December...

... the other guy?  He doesn't come back on Wednesday.

--end quoted text

DD
```

#### ↳ Re: [OT] Musings After Go-Live

- **From:** "Pete Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2005-06-24T20:50:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3i1vqjFjaeooU1@individual.net>`
- **References:** `<d9ebmd$4n7$1@panix5.panix.com>`

```

<docdwarf@panix.com> wrote in message news:d9ebmd$4n7$1@panix5.panix.com...
>
> This isn't strictly about COBOL, mind you, hence the [OT].
…[17 more quoted lines elided]…
>
As if....:-)

> The project I've been working since November '03 went live at the
> beginning of the month.  It's a delicate one, a Federal payroll system
…[21 more quoted lines elided]…
>
:-)
Or even not turn up for work... <gasp>

> (Interchange from a meeting: 'You mean we've been paying these folks
> *wrong* for the past fifteen years?  How did that happen, why didn't
…[3 more quoted lines elided]…
>

ROFL! I absolutely LOVED this... Says a lot about system audits, checks and
balances (pardon the pun) and the testing and handover procedures...
especially liked the defense "We did it according to spec.".... So, I have
to ask: If the person writing the spec had included in it that certain
checks, for certain amounts, would be produced under certain random
conditions, and these checks just happened to be payable to said spec writer
(or cronies), would this then have been programmed into the system also?  If
the answer is "yes", then I'd like to know if there is any chance of getting
a job there; if the answer is "no", then the defence above is invalidated.

And what about handover? No-one in the user department even noticed? No base
case checking? On a Federal Financial system? Still, it is delightful to
think that everyone was overpaid for 15 years... Of course they paid more
tax than they should have too, and those taxes go to finance Feder.... uhhh
....lost it. :-)

> Anyhow... it was a large project and it is has gone live... and
> consultants/contractors/hired guns are starting to be let go.  I, in part,
…[36 more quoted lines elided]…
> Still with me?

Hanging on every word... :-) (Seriously, it is very interesting and well
written...)


> What has resulted from this is a sub-group of
> consultants/contractors/hired guns who have as their only job the
…[21 more quoted lines elided]…
>

Completely understand how you feel. Been there. Console yourself with the
fact that you did a job and did it fairly and to the best of your ability.
The fact is that if you hadn't, someone else would have. Also there is no
doubt that when the sub-group started this service, it wasn't going to be
for life...

I think most of us have (certainly the ones with any imagination, never mind
sensitivity) agonised over stuff like this. It is even harder when you
develop or implement systems that put programmers out of work. (I've done
that and realised that I was one of those who would be rendered redundant by
software I had designed and built.). There is no bucking progress. Our job
is to see that computer technology makes the company more competitive and
makes life easier for the people working in the company.

Sometimes it works the other way; capacity increases with better efficiency
and the company expands and takes on more staff. (Seen that, too). It's all
a bit of a dice throw... the days of guaranteed jobs for life are long gone,
even in Japan which was one of the the last bastions of the 'Company family'
philosophy.


> On the one hand... hey, that's the consultant's life, the work comes, the
> work goes, time to find another job.  On the other hand... my work has
> caused other folks to have to look for new jobs.  This makes me feel...
> odd.
>
At least you are considering it. Time to quit when you become so completely
dispassionate that it never even occurs to you.


> On the third hand... the system went live at the beginning of May and
> there are still bugs to be worked out and modifications to be made, some
…[24 more quoted lines elided]…
>

I have encountered this attitude in various places, too, Doc. It is world
wide, not just confined to any one place. There are always the insecure
individuals who believe they are indispensible and have worked towards
making themselves so... Invariably, they get replaced, or removed, or
bypassed. No corporation (or even SME, for that matter) wants a gun at its
head. People who want to make careers in commerce realise that unless they
document what they have done and/or train a replacement, there is no chance
of them being promoted. It makes sense to share expertise. But there are
those, like the guy you're outlining, who believe it is unwise.

> Me: Eh... 'job security throught idiosyncratic knowledge' isn't how I deal
> with things, I pride myself on writing stuff that people will look at and
…[14 more quoted lines elided]…
> --end quoted text

I hope he finds another job and is wiser next time.

Really interesting post, thanks for sharing it.

Pete.
```

##### ↳ ↳ Re: [OT] Musings After Go-Live

- **From:** docdwarf@panix.com
- **Date:** 2005-06-24T08:12:49-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9gtc1$kgf$1@panix5.panix.com>`
- **References:** `<d9ebmd$4n7$1@panix5.panix.com> <3i1vqjFjaeooU1@individual.net>`

```
In article <3i1vqjFjaeooU1@individual.net>,
Pete Dashwood <dashwood@enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:d9ebmd$4n7$1@panix5.panix.com...

[snip]

>> Add to this mixture the fact that these are
>> peoples' paychecks being dealt with here, just about everyone looks at
…[4 more quoted lines elided]…
>Or even not turn up for work... <gasp>

What?  Come now, people don't work for mere money, they work for The 
Challenges!...

... and I am the King of England.

>
>> (Interchange from a meeting: 'You mean we've been paying these folks
…[14 more quoted lines elided]…
>a job there; if the answer is "no", then the defence above is invalidated.

Well... yes and no.  I've mentioned in other postings how some folks' pay 
gets handled... differently than other folks'; if interested you can 
search for 'negative deduction' in the archives.  There was another job I 
worked on where I was asked to put together a program to report on who was 
scheduled to come up on their twenty-, twenty-five- or thirty-year 
anniversary of employment in six month's time so they could be given a 
special pin and a Longevity Memo or somesuch... but it would be just as 
easy for a manager to read this report and say 'Hmmmmm, here's another 
pension liability to get rid of.'  Ugly situation, to say the least, and 
possibly worthy of discussion in another thread.

(Consider: my Respected Father's Elder Sister - may she sleep with the 
angels! - well... she used to be his Elder Sister until *he* got so old 
that a woman could not be older than that... was fired by R H Macy's after 
working there for nineteen years and three months, as were many of her 
co-workers.  Nowadays in the US such firings are illegal, back then they 
weren't.)

[snip]

>> Still with me?
>
>Hanging on every word... :-)

That's good noose... errrrr, news!

>(Seriously, it is very interesting and well
>written...)

Interesting is in the mind of the beholder, of course... as for 'well 
written' it is just ex tempore, you'se jes' easily amused.

[snip]

>> My code has rendered the work this sub-group does unnecessary.  Today is
>> their last day on-site.
…[4 more quoted lines elided]…
>The fact is that if you hadn't, someone else would have.

Ow... you *do* realise, don't you, that this 'If I didn't then someone 
else woulda' has been a rationale employed by strikebreakers and scabs 
ever since... well, ever since there have been strikebreakers and scabs.

>Also there is no
>doubt that when the sub-group started this service, it wasn't going to be
>for life...

Life is temporary, aye.

>
>I think most of us have (certainly the ones with any imagination, never mind
>sensitivity) agonised over stuff like this.

Such a 'sensitivity' appears to preclude a position in the Upper 
Management or Executive realms... those people close entire factories and 
offshore departments at the drop of a hat.

[snip]

>> On the one hand... hey, that's the consultant's life, the work comes, the
>> work goes, time to find another job.  On the other hand... my work has
…[4 more quoted lines elided]…
>dispassionate that it never even occurs to you.

Or... see above about Upper Management and Executives.

[snip]

>> ... the other guy?  He doesn't come back on Wednesday.
>>
>> --end quoted text
>
>I hope he finds another job and is wiser next time.

There's always another job, aye.

>
>Really interesting post, thanks for sharing it.

Glad you enjoyed.

DD
```

###### ↳ ↳ ↳ Re: [OT] Musings After Go-Live

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2005-06-24T20:04:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<492df$42bcad96$45491c57$8153@KNOLOGY.NET>`
- **In-Reply-To:** `<d9gtc1$kgf$1@panix5.panix.com>`
- **References:** `<d9ebmd$4n7$1@panix5.panix.com> <3i1vqjFjaeooU1@individual.net> <d9gtc1$kgf$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
>>I think most of us have (certainly the ones with any imagination, never mind
>>sensitivity) agonised over stuff like this.
…[3 more quoted lines elided]…
> offshore departments at the drop of a hat.

I'm sure that some of those folks do just that - but I think you'd be 
surprised to know how many of them actually do feel bad about some of 
their decisions.
```

###### ↳ ↳ ↳ Re: [OT] Musings After Go-Live

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2005-06-25T09:02:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9jkkl$ash$1@panix5.panix.com>`
- **References:** `<d9ebmd$4n7$1@panix5.panix.com> <3i1vqjFjaeooU1@individual.net> <d9gtc1$kgf$1@panix5.panix.com> <492df$42bcad96$45491c57$8153@KNOLOGY.NET>`

```
In article <492df$42bcad96$45491c57$8153@KNOLOGY.NET>,
LX-i  <lxi0007@netscape.net> wrote:
>docdwarf@panix.com wrote:
>>>I think most of us have (certainly the ones with any imagination, never mind
…[8 more quoted lines elided]…
>their decisions.

Granted that those who manage not to close factories don't often make the 
news... and those who feel badly about it may limit their sorrows to 'Such 
a sad thing... ah well... another round, Felice, our glasses near 
empty!'...

... but that an exception or three exists demonstrates, at least to me... 
that an exception or three exists.

DD
```

#### ↳ Re: [OT] Musings After Go-Live

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2005-06-24T09:41:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11bo6ss1h9rv29f@news.supernews.com>`
- **References:** `<d9ebmd$4n7$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:
> ... and they can be horrifically complex... how do you calculate pay
> for a float-pool nurse from the Indian Health Service who reports
…[6 more quoted lines elided]…
> liking.

How about a lawyer billing by the hour who takes a cross-country air trip - 
crossing three time zones - and submits billing for 27 hours in one day?

> Now... the system I worked on converting takes input from four feeder
> systems, each of the feeders supplies data in a common format... but
…[9 more quoted lines elided]…
> them to make sure that folks get paid so folks don't get upset.

I agree that data should be validated at entry, that a report writer should 
not have to make decisions about the integrity of a field. I worked on one 
project, dirt-simple: Read a master file and create a report. One of the 
fields (allegedly) contained the depth of the oil well in feet. Sometimes 
the field had a number, say "4705," meaning the well was producing at 4,705 
feet. Other times the field had a number like "-8650" meaning there was a 
mile-and-a-half of pipe sticking up in the air.

Before I even got to that situation I asked: "In what order are these data?" 
The answer was: "It depends on what was last done to the file." "You mean 
you SORT the MASTER FILE?" I gasped. "Sure...."
```

##### ↳ ↳ Re: [OT] Musings After Go-Live

- **From:** docdwarf@panix.com
- **Date:** 2005-06-24T11:14:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9h80m$s8m$1@panix5.panix.com>`
- **References:** `<d9ebmd$4n7$1@panix5.panix.com> <11bo6ss1h9rv29f@news.supernews.com>`

```
In article <11bo6ss1h9rv29f@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>docdwarf@panix.com wrote:
>> ... and they can be horrifically complex... how do you calculate pay
…[3 more quoted lines elided]…
>> whether they are covered by the union contract or not.)

[snip]

>How about a lawyer billing by the hour who takes a cross-country air trip - 
>crossing three time zones - and submits billing for 27 hours in one day?

It reminds me of the joke about the lawyer who was hit by a bus and was 
met at the Pearly Gates (hey, I said it was a joke!) by Saint Peter:

SP: 'I just wanted to greet the oldest human being, ever!'

L: 'Me?  I'm not... *wasn't* that old.'

SP: 'Don't be modest... who else - after Biblical times - has lived to be 
one hundred and seventy-seven years old?'

L: 'Ummmm... I don't understand, I was forty-eight.'

SP: (shuffles papers) 'Oh... I see... we were going by submitted billable 
hours.'

>
>> Now... the system I worked on converting takes input from four feeder
>> systems, each of the feeders supplies data in a common format... but
>> each of the feeders sends bad data down the line.

[snip]

>I agree that data should be validated at entry, that a report writer should 
>not have to make decisions about the integrity of a field.

... and I agree that I should be tall, young, handsome and the scion of a 
wealthy family... oh, and a good singer, too.

>I worked on one 
>project, dirt-simple: Read a master file and create a report. One of the 
…[3 more quoted lines elided]…
>mile-and-a-half of pipe sticking up in the air.

Trying to reach those low-molecular-weight aliphatics, perhaps.

>
>Before I even got to that situation I asked: "In what order are these data?" 
>The answer was: "It depends on what was last done to the file." "You mean 
>you SORT the MASTER FILE?" I gasped. "Sure...."

Well... disk space's expensive, you know.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
