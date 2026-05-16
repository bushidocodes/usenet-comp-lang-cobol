[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wang COBOL alive and well as Wang VS makes a comeback

_49 messages · 14 participants · 2009-04 → 2009-05_

**Topics:** [`COBOL's future, legacy, and obsolescence`](../topics.md#future)

---

### Wang COBOL alive and well as Wang VS makes a comeback

- **From:** tjunker@tjunker.com
- **Date:** 2009-04-14T01:47:35-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com>`

```
I am happy to report that Wang COBOL is alive and well at numerous
sites around the world.  Although the population of legacy Wang VS
sites is now very small, the new generation of Wang VS, running mostly
on Dell PowerEdge servers under Linux, is growing, with at least 70
sold to date in 11 countries.

The New VS, also called the VS22000 family, is a 100% seamless
virtualization of the Wang VS machine.  It runs the VS Operating
System, all Wang utilities, all language processors, the PACE database
system, and all user applications, all with zero conversion.  It is a
true VS, just freed from proprietary Wang hardware.

It's also the official new generation of the Wang VS, with
participation, support and certification from Compucom (successor to
Getronics North America, which was successor to Wang Global,
originally Wang Laboratories).

The New VS easily supports user populations up to about 500 Lightspeed
PCs or up to about 1,000 using other workstation emulators.  A new VS
OS supporing twice those numbers is in test and should be released
this year.

Performance in the New VS line ranges up to 240% of the legacy high-
end VS18950 released in 1999.  In Wang's "FAST" benchmark system,
that's a FAST rating of about 15,000 versus the VS18950's rating of
6,300.

At any of the performance tiers the New VS performs file I/O much
faster than any legacy VS, resulting in improvements in backups and
file-intensive operations such as reports and massive updates.

The New VS virtualizes not only the VS machine but all the essential
IO Coprocessors (IOCs) as well.  I/O subsystems that now operate
virtually include SCSI, Universal Serial IOC, 802.3, RSF, async and
mag tape.  Physical Wang SCSI disk drives are directly supported as
well as a wider range of physical mag tape technologies than was ever
supported in the legacy line.

WSN (Wang's networking system) now operates over IP networks, as does
RSF (Wang's VS clustering technology).

The New VS even accommodates legacy "928" devices -- legacy
workstations, printers, TCBs and WACS.  It does this by means of a
microcode-loadable PCI Universal Serial IOC and external legacy APAs
for connecting devices by coax, twisted pair or fiber.

Upgrade to the New VS is comparable to upgrade of the system unit in
earlier VS models.  No conversion is required, just restoring or
copying VS volumes into the New VS, configuring, and IPLing.  The
fastest New VS install was the first one sold, in 2005.  It was
installed, accepted and put into production in less than one day.
Most installs take a but longer but involve none of the time, cost or
risks of conversions to other platforms.  No conversion on the planet
to any other platform offers comparable speed and lack of risk.

The VS community has long recognized the Wang VS as the friendliest
and most efficient mainframe class platform to program, administer and
use.  It typically requires far fewer programming and operations staff
than IBM mainframes.

70 New VS systems have been sold in 11 countries and the number
continues to grow.  It has been difficult to contact surviving Wang VS
sites because not even Wang was able to keep track of all the VS
systems in use.  Since Getronics announced end of support for the
legacy VS in 2008 and designated TransVirtual Systems as the exclusive
reseller of Wang VS system software and support, it's now pretty much
of a no-brainer for anyone still using a legacy VS to contact TVS and
move up to the fully viable, reliable, efficient New VS.

The New VS is also a viable platform for those who have never used a
Wang VS but wish to adopt a mainframe-class platform that is more
affordable and much less costly to operate than an IBM mainframe.  It
is a candidate for porting COBOL, RPG II and PL/I applications from
other platforms as well as for development of new applications.

Wang's Professional Application Creation Environment (PACE)is a
powerful 4GL and database useful for rapid development of
applications.  PACE utilizes the native Wang VS transaction processing
features to provide rollback recovery and transaction delineation.
Wang COBOL also supports transaction processing.  PACE supports Host
Language Interface programming in COBOL and RPG II for application
behavior more complex than can be done without programming.
Straightforward PACE apps are created and mained with zero
programming, entirely through its menu-based Data Dictionary and
Application Builder.

There were about 30,000 Wang VS systems extant at its height in the
1980s, in every conceivable industry and in many government
organizations at all levels.  There were Wang VS systems on U.S. Navy
ships and in all U.S. State Department facilities worldwide.  A third
party software catalog last published by Wang in 1989 listed 900 pages
of offerings.

The Wang VS has been tne enterprise system in many companies and
organizations up to and larger than $500 million/year in annual sales
volume and up to several thousands of employees.  It has performed for
concurrent VS user populations up to about 500 Lightspeed users and up
to about 1,000 non-Lightspeed users.  The New VS will soon support
twice those numbers.

The legacy and New VS offers clustering technology that provides for
shared disk volumes, cross-logon, and allocation of Job and Print
classes to nodes in the cluster for automatic routing of submitted
Jobs and printing of Print Jobs.  Up to 16 VS systems can be
clustered.  The VS supports distributed database operations across the
cluster with two-phase commit.

There is also a way to use Wang COBOL natively in Unix (IBM's AIX and
HP's HP/UX).  It is called COBOL ReSource.  It provides a VS-like
environment and supports VS argument passing by reference.  It
contains the VS Procedure Language, COBOL 85 and the essential VS
utilities.  Soft recoverable files are supported, although the PACE
database system is not.

Anyone interested can Google for "Wang VS", "Transvirtual Systems",
"COBOL ReSource", can contact me, or visit the following websites:

www.tjunker.com
www.transvirtualsystems.com
www.lsnvs.com
www.cobolresource.com

Thomas Junker
V.P., TransVirtual Systems
and
proprietor of The Unofficial Wang VS Information Center website
and
agent for COBOL ReSource
```

#### ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-14T13:39:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gs23m8$bog$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com>`

```
In article <bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com>,
 <tjunker@tjunker.com> wrote:
>I am happy to report that Wang COBOL is alive and well at numerous
>sites around the world.  Although the population of legacy Wang VS
>sites is now very small, the new generation of Wang VS, running mostly
>on Dell PowerEdge servers under Linux, is growing, with at least 70
>sold to date in 11 countries.

With all appropriate respect due to the stunning growth quoted here, Mr 
Junker - seventy sold in eleven countries! - I must say that I, 
personally, find myself to be moderately underwhelmed.

This is not due to my experience with the WANG as a platform; I found it 
to be a real 'programmer's machine' upon which miracles could be worked in 
an amazingly short amount of time.  Granted that the I-O could get, at 
times, a bit... unstable (file corruption and record loss were, in my 
experience, common in anything more complex than dataset with more than 
two alternate indices); the user community was very supportive and 
miracles (for its time) could be worked.  I generated a COBOL program that 
would, for a given record, generate a pop-up window so that the user could 
jot free-form notes of unlimited length (the 2000-char LRECL took a bit of 
doing to overcome) in 1987.

That was considered to be Quite Something... in 1987.  Sadly, it seemed 
that scarcely a nickel's worth of R&D was invested since then; your 
posting mentioned a list of third-party developers of some 900 pages that 
was printed in 1989.

That was two decades ago.

I wish you the best of luck in your venture.

DD
```

##### ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-04-14T13:24:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<py4Fl.20748$Qh6.192@newsfe14.iad>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com>`

```
What's happening, of course,  is that there are applications developed in
"Wang" that are working well enough that there's no psrticular urge to
replace them, and a dwindling talent pool available to do it in any event.
Prime is another example: I don't think there are any actual Prime machines
still running in western Canada, but I know of a dozen places that are still
running the applications under emulation in Linux environments.  There must
be all sorts of tiny niches like this - I wonder if there are any Singer
apps still running??!?? - and eventually they will all run out of traction
and be abandoned, or will be rewritten for some other environment.  And that
may be a stressful time for the ones responsible.  But facts are facts and
everything has its lifespan.  What's a great pity is that there are concepts
and utilities in each environment that are done exceptionally well (I was
going to say unique but I doubt if anything is actually unique) which will
get lost when the environment is abandoned.  Since I've worked on the Prime
I have been able to implement some of the ideas I came across: not
particularly new but done in ways I hadn't thought of..

I/T seems to lack the practice of other engineering disciplines - that of
preserving history for the benefit of future students of the field.

PL

<docdwarf@panix.com> wrote in message news:gs23m8$bog$1@reader1.panix.com...
> In article
<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com>,
>  <tjunker@tjunker.com> wrote:
> >I am happy to report that Wang COBOL is alive and well at numerous
…[12 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-04-15T12:04:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74kml0F13dcc2U1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad>`

```
tlmfru wrote:
> What's happening, of course,  is that there are applications
> developed in "Wang" that are working well enough that there's no
…[15 more quoted lines elided]…
> not particularly new but done in ways I hadn't thought of..

That's a very good point.

I found out many years ago that moving around and getting experience on 
different platforms seems to have a synergistic effect... Your overall 
capability increases to become more than the sum of its parts...:-)

If you stay with one environment it is very easy to think there is only way 
to do things.

>
> I/T seems to lack the practice of other engineering disciplines -
> that of preserving history for the benefit of future students of the
> field.

COBOL code is being carefully preserved and enshrined as we speak. I 
understand billions of lines of it will be around for some time yet...:-)

Whether this is useful to students is debatable. Most of the ones I 
encounter through private mail are simply puzzled by it.

<unreferenced previous snipped>

Pete.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 4)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-04-15T13:13:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74m4rnF1454jgU1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net>`

```
In article <74kml0F13dcc2U1@mid.individual.net>,
	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:
> tlmfru wrote:
>> What's happening, of course,  is that there are applications
…[25 more quoted lines elided]…
> to do things.

I wholeheartedly agree.  Sadly, the industry does not usually see it this
way and looks for specialization rather than generalization.

> 
>>
…[8 more quoted lines elided]…
> encounter through private mail are simply puzzled by it.

I fought to the last to keep COBOL at least peripherally in the
program here. (Not as a specific subject, but used in courses
like File Processing.  In the end, I lost out to Java and whatever
will be the next language du jour.  Who kows, maybe after I retire
I will get my wish to once again work with COBOL when they are out
looking for people to maintain/modify all those Information Systems
written in COBOL and still running.  :-)

bill
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-15T13:49:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gs4om6$o4o$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net>`

```
In article <74m4rnF1454jgU1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <74kml0F13dcc2U1@mid.individual.net>,
>	"Pete Dashwood" <dashwood@removethis.enternet.co.nz> writes:

[snip]

>> I found out many years ago that moving around and getting experience on 
>> different platforms seems to have a synergistic effect... Your overall 
…[6 more quoted lines elided]…
>way and looks for specialization rather than generalization.

With all due respect, Mr Gunshannon... 'the industry'?  Now I am reminded 
of... A Story!

I graduated college with a BA in Liberal Arts from what some might call 
the 'liberal-artiest' school in the country; we studied grammar, rhetoric, 
logic, arithmetic, music, geometry and astronomy... and as often as we 
could, from the original texts.  Shortly after that I read an article in 
the Wall Street Journal where the reporter had Important Executive after 
Important Executive saying that what their companies needed were 
generalists, not narrowly-trained specialists; I broke out my trusty 
Olivetti and began sending out cover-sheets and resumes.

I shortly after that began to receive 'ding' notes... 'Thank you for your 
interest in our organisation but at present we do not have any positions 
for which your background is suited'.  I papered an entire wall in my 
bathroom with these so that at appropriate times I could say 'This one's 
for *you*, Kodak... and this one's for *you*, Citibank... don't feel left 
out, DuPont, I've got some left...'

In short... *every* company in *every* industry that I applied to, when 
offered a generalist, said 'thanks, but no'; it wasn't until I picked up 
COBOL - then a language the need for which was frequently seen in 
newspaper-advertisements - that I began to get jobs.

Things now, of course, have changed... and I am the King of England.  I've 
been told that the trend now is to remove human interaction as much as 
possible; a resume is scanned for keywords and if those aren't there then 
consideration is not given.

Who cares if you can wrap your mind around Minkowski's reformulation of 
Einstein's 1905 paper into geometric terms... if you don't know (our 
business need) already then thanks, but no.

As the Germans say, Mr Gunshannon... plus ca change, plus c'est la meme 
chose.

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 6)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-04-15T15:32:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74md0pF10du24U1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com>`

```
In article <gs4om6$o4o$1@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <74m4rnF1454jgU1@mid.individual.net>,
> Bill Gunshannon <billg999@cs.uofs.edu> wrote:
…[15 more quoted lines elided]…
> With all due respect, Mr Gunshannon... 'the industry'?  

Every part of it that I talked to.  :-)  At least as regards COBOL.

>                                                          Now I am reminded 
> of... A Story!
…[32 more quoted lines elided]…
> chose.

First, Mr. Gunshannon was by father, now deceased.  My name is "bill".

Now, time for my story.  :-)

I decided almost a decade ago that I was tiring of the academic world
so I gave some thought to what I wanted to do to round out my career.
I decided that of all the things I have done I probably enjoyed writting
COBOL the most.  So, I decided to look for a COBOL position.  Now, over
the past 20-some years I have done COBOL on IBM, Unisys (Sperry in those
days), Prime, RT-11, RSTS/E, VMS, Unix and numerous PC (and other less
popular micros) dialects.  Pretty well rounded background you would think.
All spread out over the period with the VMS being the most current.
But a job search returned only "current CICS experience required" or
"current Unisys experience required".  Of course, VMS is all but dead
and that was my latest.  One would think that with this background it
would demonstrate my ability to work with COBOL in pretty much any
environment.  The best I got was an offer from a very big COBOL shop
in Georgia.  Unfortunately, they were not interested in my COBOL
experience at all and wanted me as a Unix Sys Admin.  Would not even
consider me for one of their many COBOL positions.

But I still hold out hope.  I will retire in under 10 years (hopefully,
not much more than 5) and when that happens, I will hang out my shingle
as a COBOL Programmer available for contract work and see what happens.
Or, just write COBOL for the pure hell of it at home.  :-)

bill
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-15T16:54:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gs53gg$eol$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74md0pF10du24U1@mid.individual.net>`

```
In article <74md0pF10du24U1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <gs4om6$o4o$1@reader1.panix.com>,
>	docdwarf@panix.com () writes:

[snip]

>> As the Germans say, Mr Gunshannon... plus ca change, plus c'est la meme 
>> chose.
>
>First, Mr. Gunshannon was by father, now deceased.  My name is "bill".

My apologies, Mr Gunshannon, but this was a habit (one of the 'Three Rules 
of Discourse') drummed into me decades ago; *everyone*, when possible, 
from janitor to Board Chairperson and back again, is to be addressed as Mr 
or Ms.  If you want Special Treatment from me you might find yourself 
disappointed.

(the other two Rules are 'One person speaks at a time' and 'Any opinion, 
unless supported by reasoned argument, may be dismissed as mere 
opinion'... and all three have held me, for the most part, in good stead)

[snip]

>But I still hold out hope.  I will retire in under 10 years (hopefully,
>not much more than 5) and when that happens, I will hang out my shingle
>as a COBOL Programmer available for contract work and see what happens.
>Or, just write COBOL for the pure hell of it at home.  :-)

Another aphorism is 'the difference between a dream and a plan is a 
timetable'... and you appear to have a timetable.

And yet... *another* aphorism, a bit more bitter, is 'Do you want to hear 
God laugh?  Tell Him your plans.'  Me, I have a contract renewal until 31 
August; as long as the checks clear the bank I'll keep showing up for 
work.

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 8)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-04-15T17:27:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74mjo6F1453nsU1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74md0pF10du24U1@mid.individual.net> <gs53gg$eol$1@reader1.panix.com>`

```
In article <gs53gg$eol$1@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <74md0pF10du24U1@mid.individual.net>,
> Bill Gunshannon <billg999@cs.uofs.edu> wrote:
…[14 more quoted lines elided]…
> disappointed.

Well, I am certainly not upset at being addressed as Mr.  Funny you
should mention the Germans as I lived over there for a number of years
and one thing you get used to is even after knowing someone for more
than a decade you don't use the familiar form of the english word "you"
("Sie" vs. "Du") until directed to do so by that person.  When I make
the comment above it is usually intended as a sign that one may address
me informally.  :-)

> 
> (the other two Rules are 'One person speaks at a time' and 'Any opinion, 
…[11 more quoted lines elided]…
> timetable'... and you appear to have a timetable.

More than one, actually.  My first retirement (from military service) is
fixed.  When I reach a certain age they drag me, kicking and screaming, to
the door.  It is the second, my civilian retirement that is still up for
grabs, How long wil depend more on how muc I like my job and how much
fun I am having.  But I am pretty much drawing the line at 10 years
from now.

> 
> And yet... *another* aphorism, a bit more bitter, is 'Do you want to hear 
> God laugh?  Tell Him your plans.'  

Ah yes, "gang aft agley".  But one can always hope.

>                                    Me, I have a contract renewal until 31 
> August; as long as the checks clear the bank I'll keep showing up for 
> work.

May you have many more pleasant contracts.  At least until you decide the
golf club or the fishing pole feels better in your hands than the mouse and
keyboard.

bill
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-04-15T13:55:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aoecu49ekkrpg7v4jkbdpbr0hlgvt68tn0@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74md0pF10du24U1@mid.individual.net> <gs53gg$eol$1@reader1.panix.com> <74mjo6F1453nsU1@mid.individual.net>`

```
On 15 Apr 2009 17:27:35 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>More than one, actually.  My first retirement (from military service) is
>fixed.  When I reach a certain age they drag me, kicking and screaming, to
…[3 more quoted lines elided]…
>from now.

I am comfortable to know that with my vacation time accrued, I have
enough time and age to retire.   If I did so, they would hire me back
part time (after 90 days) - to work on our legacy system until it is
gone in 2010.    But since I plan on continuing to work, I will be
working more and more with its replacement.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-16T13:38:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gs7ccd$lh7$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74md0pF10du24U1@mid.individual.net> <gs53gg$eol$1@reader1.panix.com> <74mjo6F1453nsU1@mid.individual.net>`

```
In article <74mjo6F1453nsU1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <gs53gg$eol$1@reader1.panix.com>,
>	docdwarf@panix.com () writes:
…[18 more quoted lines elided]…
>Well, I am certainly not upset at being addressed as Mr.

Well, if it's upset you're looking for... let me see if I can shimmy, like 
my sister, Kate.  Been known to drive folks from the room, screaming.

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 8)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-04-15T13:51:49-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74md0pF10du24U1@mid.individual.net> <gs53gg$eol$1@reader1.panix.com>`

```
On Wed, 15 Apr 2009 16:54:40 +0000 (UTC), docdwarf@panix.com () wrote:

>My apologies, Mr Gunshannon, but this was a habit (one of the 'Three Rules 
>of Discourse') drummed into me decades ago; *everyone*, when possible, 
>from janitor to Board Chairperson and back again, is to be addressed as Mr 
>or Ms.  If you want Special Treatment from me you might find yourself 
>disappointed.

I've been intrigued by the practice, common in the U.S.American south
which is alien to me - of children referring to adults as "Miss Anne",
or Mr. Bill.   I don't know if adults use that same kind of honorific.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-16T13:50:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gs7d42$kne$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74md0pF10du24U1@mid.individual.net> <gs53gg$eol$1@reader1.panix.com> <2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com>`

```
In article <2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:
>On Wed, 15 Apr 2009 16:54:40 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[8 more quoted lines elided]…
>or Mr. Bill.   I don't know if adults use that same kind of honorific.

(names changed to protect the guilty)

Decades on back I went on a Family Vacation and my Eldest Niece - then a 
lass of nine years old or so - became a fast friend of another girl, of 
similar age, whose family was also Being Vacant.  At one point this other 
girl looked at me and whined, exasperatedly, 'I don't know whether to call 
you 'Frederico' or 'Uncle Frederico'!'

My response was 'My parents and my brothers call me 'Frederico'.  My 
nieces call me 'Uncle Frederico'.  *You* may call me 'Mr O'Shaugnessey 
Guiterrez-Camacho Yee-Tang.'

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 10)_

- **From:** John <john.loughnan@gmail.com>
- **Date:** 2009-04-16T08:25:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12e8c3ed-245b-46bf-b8d8-55c225211ef1@a7g2000yqk.googlegroups.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74md0pF10du24U1@mid.individual.net> <gs53gg$eol$1@reader1.panix.com> <2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com> <gs7d42$kne$1@reader1.panix.com>`

```
On Apr 16, 2:50 pm, docdw...@panix.com () wrote:
> In article <2jecu411iosem0fdib2gs4v2ngehi5s...@4ax.com>,
> Howard Brazee  <how...@brazee.net> wrote:
…[25 more quoted lines elided]…
> DD


Hi Guys,
Believe it or not I am still working in COBOL on a virtualized VS but
I think it will be replaced within a year or 2 and then I expect I
will be on the scrap heap.

John
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 10)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2009-04-17T02:05:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<gs7d42$kne$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74md0pF10du24U1@mid.individual.net> <gs53gg$eol$1@reader1.panix.com> <2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com> <gs7d42$kne$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> (snip) I
> 
…[5 more quoted lines elided]…
> 

Finally!  After all these years!  I now know DocDwarf's REAL NAME!

With kindest regards,
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-17T14:06:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsa2d8$8cl$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com> <gs7d42$kne$1@reader1.panix.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>docdwarf@panix.com wrote:
>> (snip) I
…[5 more quoted lines elided]…
>Finally!  After all these years!  I now know DocDwarf's REAL NAME!

... and the reasons it has been kept so well-concealed as well, Mr 
Trembley.  Who would take seriously a COBOL-codin' fool with a monicker of 
'Frederico O'Shaughnessey Guiterrez-Camacho Yee-Tang'?

(then again... who takes me seriously, anyhow?  Not I, for the most part)

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 12)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-04-17T15:27:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74rlf6F13rnb8U1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com> <gs7d42$kne$1@reader1.panix.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com>`

```
In article <gsa2d8$8cl$1@reader1.panix.com>,
	docdwarf@panix.com () writes:
> In article <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net>,
> Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
…[14 more quoted lines elided]…
> 

Sounds like a character from a Heinlein book.  :-)

bill
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-17T16:51:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsac2b$nde$2@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <74rlf6F13rnb8U1@mid.individual.net>`

```
In article <74rlf6F13rnb8U1@mid.individual.net>,
Bill Gunshannon <billg999@cs.uofs.edu> wrote:
>In article <gsa2d8$8cl$1@reader1.panix.com>,
>	docdwarf@panix.com () writes:

[snip]

>> ... and the reasons it has been kept so well-concealed as well, Mr 
>> Trembley.  Who would take seriously a COBOL-codin' fool with a monicker of 
…[5 more quoted lines elided]…
>Sounds like a character from a Heinlein book.  :-)

Like a character?  Properly and frequently used it becomes a goodly half 
of the text!

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 12)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-04-17T11:54:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <2jecu411iosem0fdib2gs4v2ngehi5sbsu@4ax.com> <gs7d42$kne$1@reader1.panix.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com>`

```
On Fri, 17 Apr 2009 14:06:32 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net>,
>Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
…[15 more quoted lines elided]…
>DD

Doc Yee has a nice ring to it :)

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"He may look like an idiot and talk like an idiot but
don't let that fool you.  He really is an idiot."
-- Groucho Marx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 13)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-17T16:58:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsacf6$nde$3@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com>`

```
In article <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com>,
SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:
>On Fri, 17 Apr 2009 14:06:32 +0000 (UTC), docdwarf@panix.com () wrote:

[snip]

>>... and the reasons it has been kept so well-concealed as well, Mr 
>>Trembley.  Who would take seriously a COBOL-codin' fool with a monicker of 
…[4 more quoted lines elided]…
>Doc Yee has a nice ring to it :)

I offereth thou my thanks, Mr Wiegand; thine own monicker might be heard 
euphoniously, as well.

(note to non-native English speakers: 'ye' is an archaic form for 'you' 
and I played on the sound and the older form of English in a small attempt 
at humor... but I think I have managed, once again, to demonstrate that 'a 
joke explained is a joke lost')

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-04-18T17:20:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74t68pF12pne9U1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com>,
> SkippyPB  <swiegand@Nospam.neo.rr.com> wrote:
…[22 more quoted lines elided]…
> DD

Verily, Master Dwarf, wilst thou offer a paltry example of the language of 
thine ancestors? I had taken thee for one who placed import on such matters, 
but, in this instance at least, thy current hath turned awry. "I offereth 
thou my thanks" is ungrammatical and confoundeth the ear of anyone who truly 
hath affection for our ancient and venerable tongue.

Hie thee thither to the schoolroom and complete an hundred repetitions upon 
thy slate: "I offereth THEE my thanks."

Pete.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-04-18T08:53:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gXkGl.120221$5Z3.22259@en-nntp-05.dc1.easynews.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com> <74t68pF12pne9U1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:74t68pF12pne9U1@mid.individual.net...
> docdwarf@panix.com wrote:
>> In article <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com>,
…[36 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."


I am not certain, but isn't it,
  "I offer"
 "he, she or it Offereth"
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 16)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-04-19T14:08:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74vfclF160h49U1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com> <74t68pF12pne9U1@mid.individual.net> <gXkGl.120221$5Z3.22259@en-nntp-05.dc1.easynews.com>`

```
William M. Klein wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
> news:74t68pF12pne9U1@mid.individual.net...
…[43 more quoted lines elided]…
> "he, she or it Offereth"

Yes, Bill. Well spotted!

Pete.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 15)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-18T14:08:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gscmtk$r1u$2@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com> <74t68pF12pne9U1@mid.individual.net>`

```
In article <74t68pF12pne9U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> In article <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com>,
…[24 more quoted lines elided]…
>thine ancestors?

'Hey, close the door... we're not paying to heat the neighborhood!' 

>I had taken thee for one who placed import on such matters, 
>but, in this instance at least, thy current hath turned awry. "I offereth 
…[4 more quoted lines elided]…
>thy slate: "I offereth THEE my thanks."

Were I to do such, I might betray the lessons of the Three Great Masters 
from whom I learned much of my Elisabethan English, Moe-eth, Larry-eth and 
Shemp-eth.

(yes, I know that Shemp was a poor excuse for Curly... but there was one 
two-reeler in which Moe cried out 'Larry-eth!  Shemp-eth!  Help-eth me!'; 
this has served unto me as paradigm for lo, these many years)

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 15)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-04-20T08:44:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nh2pu4d8k6l064huot1m3mtv2rhi6celhj@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com> <74t68pF12pne9U1@mid.individual.net>`

```
On Sat, 18 Apr 2009 17:20:26 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>Hie thee thither to the schoolroom and complete an hundred repetitions upon 
>thy slate: "I offereth THEE my thanks."

One thing we have lost over time, is the distinction between second
person singular and second person plural pronouns.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 16)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-04-20T12:15:45-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s7pu415jg15boq4114vet5o9ro79hgcuo@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com> <74t68pF12pne9U1@mid.individual.net> <nh2pu4d8k6l064huot1m3mtv2rhi6celhj@4ax.com>`

```
On Mon, 20 Apr 2009 08:44:31 -0600, Howard Brazee <howard@brazee.net>
wrote:

>On Sat, 18 Apr 2009 17:20:26 +1200, "Pete Dashwood"
><dashwood@removethis.enternet.co.nz> wrote:
…[6 more quoted lines elided]…
>person singular and second person plural pronouns.

Except in the Southern U.S. where you is singular and youall is
plural.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I believe that sex is one of the most beautiful, 
natural, wholesome things that money can buy." 
--Steve Martin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 17)_

- **From:** "Kerry Liles" <kerry.removethisandoneperiod.liles@gmail.com>
- **Date:** 2009-04-20T14:18:05-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsie92$6pf$1@news.motzarella.org>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com> <74t68pF12pne9U1@mid.individual.net> <nh2pu4d8k6l064huot1m3mtv2rhi6celhj@4ax.com> <7s7pu415jg15boq4114vet5o9ro79hgcuo@4ax.com>`

```
"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
news:7s7pu415jg15boq4114vet5o9ro79hgcuo@4ax.com...
> On Mon, 20 Apr 2009 08:44:31 -0600, Howard Brazee <howard@brazee.net>
> wrote:
…[14 more quoted lines elided]…
>

I always understood that "all y'all" was the plural of "y'all" (the latter 
being the singular form of course).

cheers
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 18)_

- **From:** SkippyPB <swiegand@Nospam.neo.rr.com>
- **Date:** 2009-04-21T11:53:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ksqru4l1pkn4oou2eclef7sv21gobjbprm@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <MtRFl.126852$4m1.80762@bgtnsc05-news.ops.worldnet.att.net> <gsa2d8$8cl$1@reader1.panix.com> <jh9hu45ivl63sb80btr4k2ubhf2q76ra8b@4ax.com> <gsacf6$nde$3@reader1.panix.com> <74t68pF12pne9U1@mid.individual.net> <nh2pu4d8k6l064huot1m3mtv2rhi6celhj@4ax.com> <7s7pu415jg15boq4114vet5o9ro79hgcuo@4ax.com> <gsie92$6pf$1@news.motzarella.org>`

```
On Mon, 20 Apr 2009 14:18:05 -0400, "Kerry Liles"
<kerry.removethisandoneperiod.liles@gmail.com> wrote:

>"SkippyPB" <swiegand@Nospam.neo.rr.com> wrote in message 
>news:7s7pu415jg15boq4114vet5o9ro79hgcuo@4ax.com...
…[22 more quoted lines elided]…
>

Well I guess it depends on which part of Southern U.S. you live in.  I
lived in New Orleans for nearly 3 years and "all y'all" was just too
much to say all at once.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I believe that sex is one of the most beautiful, 
natural, wholesome things that money can buy." 
--Steve Martin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-04-15T13:03:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ambcu4tg1rjih27om9v2ar98ug1k6m3qd9@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74md0pF10du24U1@mid.individual.net>`

```
On 15 Apr 2009 15:32:42 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>Pretty well rounded background you would think.
>All spread out over the period with the VMS being the most current.
…[4 more quoted lines elided]…
>environment. 

I remember once not getting a job because I didn't have CoBOL II
experience.  I found out later that CoBOL II was the same ANSI CoBOL I
was working with elsewhere (with the differences being differences I
was familiar with my previous IBM Mainframe CoBOL experience).

Human Resources employees often use key words to narrow their work
load.   But this shop would have been better off hiring a good Fortran
programmer who knows their industry than a CoBOL II programmer who
didn't.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-04-16T13:09:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74neq7F14kksjU1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <74m4rnF1454jgU1@mid.individual.net>,
> Bill Gunshannon <billg999@cs.uofs.edu> wrote:
…[34 more quoted lines elided]…
> Citibank... don't feel left out, DuPont, I've got some left...'

ROFL!

Thanks for sharing that, Doc... :-)
>
> In short... *every* company in *every* industry that I applied to,
…[16 more quoted lines elided]…
> DD

I have to agree. It is sad that it has come to this, but these days 
candidate selection is almost exclusively by software.

I don't normally apply for jobs, but I recently did. It was a top NZ IT job 
and I really would love to have done it. Although I am pretty much coming to 
the end of my "career", I honestly felt I could bring something to this job 
and within a couple of years I could train my replacement and make a real 
difference to the way-less-than-optimum Government service it provides. I 
knocked up a 4 page summary (my full CV is 35 pages and I only produce it at 
interviews, when appropriate; I NEVER give it to pimps...), highlighting the 
best stuff I've been involved with (some of it was specific to the industry 
in question) and stressing what a general all-round capable IT guy I am :-), 
and my enthusiasm for this task. I received a job description (from an 
Agency) and went through it carefully. I had everything they requested, and 
in depth.

I  never even got an interview :-)

I think the CV summary was maybe too general (but my experience is pretty 
general, and I avoid lying in job applications), or perhaps they didn't like 
the photo :-). They said they had received 230 applications, which I found 
quite staggering; I would have expected probably no more than about 50 
people in the country would have been properly qualified to do this job.

I find that what works for me is to sit across a table from someone who 
needs IT support, listen to his/her problem, and suggest possible solution 
outlines, based on a lifetime of IT experience. I don't remember ever 
"failing" an interview. Unfortunately, most people don't get this 
opportunity and are completely at the mercy of inept and often downright 
dishonest pimps.

In my case it doesn't really matter; I applied because I wanted to do the 
job, not because I HAVE to, but it would be too bad if that were not the 
case.

If any of you are looking for jobs I would recommend using Agencies only as 
a SECOND-LEVEL layer. Find out who the IT Directors are at the larger 
companies in your town and send CVs direct. Ideally, try and set up a 
meeting (buy the guy a sandwich or a coffee, keep it relaxed and be 
yourself. Don't be intimidated by someone's corporate standing; respect is 
good, but fear or arse-licking are not... :-))

(I should have really followed this advice myself and gone down to 
Wellington to see their current CEO, but I've just been too busy. Having 
written that, I guess I couldn't have been really serious about getting the 
job... :-))

Pete.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 7)_

- **From:** SeaSideSam <sam@sea.side>
- **Date:** 2009-04-15T22:00:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7e61$49e69f55$621629c9$12546@ALLTEL.NET>`
- **In-Reply-To:** `<74neq7F14kksjU1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74neq7F14kksjU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> I  never even got an interview :-)
> 
> Pete.

my personal experience was once i went over 40 the interviews dried up 
(mid 90s).  i was informed at some point that in the good ole usa 
insurance companies frowned on hiring anyone over 38.  my 'exceptional' 
skills list gained me two years.  i had managed to shop my 'real-world' 
degree much longer than many believed possible, but i never found a way 
to overcome the 'age' liability.  the irony is/was that a medical 
doctor's prescription did me in.

i own vb5, advanced pick 2.0, and rm/cobol 6.50.00 (all for windows). 
make me an offer and i'll ship them all to you.

sss
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-04-16T13:16:50-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qv0fu417em9c6mtq9ecl0cj3eomsn2mvjp@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74neq7F14kksjU1@mid.individual.net>`

```
On Thu, 16 Apr 2009 13:09:26 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>I don't normally apply for jobs, but I recently did. It was a top NZ IT job 
>and I really would love to have done it. Although I am pretty much coming to 
…[11 more quoted lines elided]…
>I  never even got an interview :-)

Sometimes a government agency is required to post whenever a position
comes up - even when it already knows that it's going to hire the temp
who is already doing the job.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-04-17T11:36:31+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74pto1F157kkiU1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74neq7F14kksjU1@mid.individual.net> <qv0fu417em9c6mtq9ecl0cj3eomsn2mvjp@4ax.com>`

```
Howard Brazee wrote:
> On Thu, 16 Apr 2009 13:09:26 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[19 more quoted lines elided]…
> who is already doing the job.

LOL! I could just see a temp doing this job... :-)

Pete.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 9)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-04-17T09:38:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5e8hu4hi0mq7qrc7gkkg9si0dfe26qa6uc@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74neq7F14kksjU1@mid.individual.net> <qv0fu417em9c6mtq9ecl0cj3eomsn2mvjp@4ax.com> <74pto1F157kkiU1@mid.individual.net>`

```
On Fri, 17 Apr 2009 11:36:31 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Sometimes a government agency is required to post whenever a position
>> comes up - even when it already knows that it's going to hire the temp
>> who is already doing the job.
>
>LOL! I could just see a temp doing this job... :-)

Huh?   Haven't you done contract work before?    That hypothetical
temp could have been you - and when they saw how much more you could
do besides whatever you were hired for - they might create a full-time
position in order to keep you.

And since it is a government agency, they would have to post the
position that they created for you.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 10)_

- **From:** billg999@cs.uofs.edu (Bill Gunshannon)
- **Date:** 2009-04-17T15:42:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74rmakF13rnb8U3@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74neq7F14kksjU1@mid.individual.net> <qv0fu417em9c6mtq9ecl0cj3eomsn2mvjp@4ax.com> <74pto1F157kkiU1@mid.individual.net> <5e8hu4hi0mq7qrc7gkkg9si0dfe26qa6uc@4ax.com>`

```
In article <5e8hu4hi0mq7qrc7gkkg9si0dfe26qa6uc@4ax.com>,
	Howard Brazee <howard@brazee.net> writes:
> On Fri, 17 Apr 2009 11:36:31 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[13 more quoted lines elided]…
> position that they created for you.

And when someone with better credentials (even if he is lying about
them) applies, they have to hire him and you are back out on the
street.

bill
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-04-17T11:29:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gtehu4pkk3qlbdjo33hnbj9jl92um4t235@4ax.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <gs4om6$o4o$1@reader1.panix.com> <74neq7F14kksjU1@mid.individual.net> <qv0fu417em9c6mtq9ecl0cj3eomsn2mvjp@4ax.com> <74pto1F157kkiU1@mid.individual.net> <5e8hu4hi0mq7qrc7gkkg9si0dfe26qa6uc@4ax.com> <74rmakF13rnb8U3@mid.individual.net>`

```
On 17 Apr 2009 15:42:12 GMT, billg999@cs.uofs.edu (Bill Gunshannon)
wrote:

>> And since it is a government agency, they would have to post the
>> position that they created for you.
…[3 more quoted lines elided]…
>street.

When you set up criteria to get one person - that person fits best.
(not "over-qualified").   Bureaucrats know how to use the system.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-17T18:15:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsah0q$nqt$2@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <5e8hu4hi0mq7qrc7gkkg9si0dfe26qa6uc@4ax.com> <74rmakF13rnb8U3@mid.individual.net> <gtehu4pkk3qlbdjo33hnbj9jl92um4t235@4ax.com>`

```
In article <gtehu4pkk3qlbdjo33hnbj9jl92um4t235@4ax.com>,
Howard Brazee  <howard@brazee.net> wrote:

[snip]

>When you set up criteria to get one person - that person fits best.
>(not "over-qualified").

I've applied for consulting-slots and have been told that I'm 
'overqualified'... my response is a simple and honest 'All right, what 
would you like me to forget?'

I still don't get the gig, for some reason.

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 13)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2009-04-17T13:33:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WX3Gl.5078$im1.1610@nlpi061.nbdc.sbc.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <5e8hu4hi0mq7qrc7gkkg9si0dfe26qa6uc@4ax.com> <74rmakF13rnb8U3@mid.individual.net> <gtehu4pkk3qlbdjo33hnbj9jl92um4t235@4ax.com> <gsah0q$nqt$2@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:gsah0q$nqt$2@reader1.panix.com...
> I've applied for consulting-slots and have been told that I'm
> 'overqualified'...

Ooh, ooh....I cannot resist....

All things considered, I'd  say they were telling you a little white lie to 
avoid hurting your feelings......

MCM
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-04-17T18:40:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gsaifg$jah$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gtehu4pkk3qlbdjo33hnbj9jl92um4t235@4ax.com> <gsah0q$nqt$2@reader1.panix.com> <WX3Gl.5078$im1.1610@nlpi061.nbdc.sbc.com>`

```
In article <WX3Gl.5078$im1.1610@nlpi061.nbdc.sbc.com>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:gsah0q$nqt$2@reader1.panix.com...
>> I've applied for consulting-slots and have been told that I'm
…[5 more quoted lines elided]…
>avoid hurting your feelings......

Come now, Mr Mattias... *everyone* knows that 
consultants/contractors/hired guns have no feelings.

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 5)_

- **From:** tjunker@tjunker.com
- **Date:** 2009-05-20T14:07:11-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<955f9ba9-b95d-4b4c-9883-0ddf2f4dcdf8@r34g2000vba.googlegroups.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net>`

```
On Apr 15, 7:13 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:

> ...
> I fought to the last to keep COBOL at least peripherally in the
> program here. (Not as a specific subject, but used in courses
> like File Processing.  In the end, I lost out to Java and whatever
> will be the next language du jour...

That last is a major but largely unrecognized and undiscussed problem
in IT today.  The language du jour may not last even as long as a
project using it.  In a stable mainframe environment we are accustomed
more to the language du décennie (of the decade) or du siècle (of the
century).  This contributes to the stability of programming efforts
and the resulting applications.  The instability that is rampant in IT
today works to undermine the companies involved, in ways their
management evidently doesn't see or understand.

When I was a young smartass I used to look down my nose at ordinary
programming and thought that the world needed more superprogrammers,
and the truly significant things were only done by the brightest and
the best.  Later in life I came to realize that really good and useful
work is mostly done by small, stable groups of ordinary but
constructive programmers, groups with very low turnover.  This was
really brought home to me by my acquaintance with a civil service
group of about six, who had personally written most of their
repository of 50,000 programs, 37K of which were in current use by
actual audit.  They were being displaced by a trend toward
outsourcing, and at one meeting with an outside firm about some new
requirements were told by the outside rep that it might take about six
months to do the work.  After the meeeting the in-house guys put their
heads together in the hallway and figured out that with boilerplate
from their repository they could complete the work in a few days.
When the outside rep caught wind of that she said two interesting
things:  "That's impossible!" and "They're lying!"  Both were
reasonable conclusions from her point of view, in her reality, but
both were sadly wrong.  These guys had no need to lie, and would be
put on the spot to deliver (which they had been going, thank you very
much, for the last 15 or so years).  Nor was it impossible in the
reality of a small and cohesive group that had been writing that kind
of software for a couple of decades.

I think there is a parallel in the instability found in IT today.  No
language du jour offers benefits in more than the very short term that
even begin to compare with what can be done with stable tools and
platforms, even if the latter are not sexy.  And the work product of
the stable tools, on a stable platform, is lasting, witness the
millions or billions of lines of COBOL still doing useful work today.
The work product of the language and platform du jour is fairly likely
to be discarded next year or the year after, when the next fashion
trend strikes.

Personally I prefer to work with stable tools on stable platforms and
solve challenges once, not the same challenge again and again on
shifting ground.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 6)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-05-22T02:13:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<77l5rrF1hsgm8U1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <955f9ba9-b95d-4b4c-9883-0ddf2f4dcdf8@r34g2000vba.googlegroups.com>`

```
tjunker@tjunker.com wrote:
> On Apr 15, 7:13 am, billg...@cs.uofs.edu (Bill Gunshannon) wrote:
>
…[11 more quoted lines elided]…
> and the resulting applications.

I don't know of any projects that use Java and have been running longer than 
the Java language has been around, or even that use Ruby, or C# and have 
been running as long as those languages have been available. Can you cite 
some instances? (or even one...)

Your comment is an interesting one. It seems to imply that application 
stability depends on platform stability and this is demonstrably not the 
case. The mainframe environment has been "unstable" throughout the decades 
it has been around. There are always new releases of system software that 
impact applications. Even new releases of COBOL have unsettling effects on 
applications written in the "old" dialect. Sometimes converting from one 
level of COBOL to another can be as big a deal as migrating across platforms 
altogether.

Certainly, if you were a mainframe COBOL shop, there was a CONSISTENT 
approach to the programming, despite upheavals imposed by IBM changing the 
technical environment every couple of years, but that was more to do with 
the paradigm the language was based on, than with the platforms where it was 
run.

There is a very fine line between the "stability" you commend, and the 
failure to recognise when change was needed, and adapt and evolve.

As the network expanded, the idea of a centralised processor driving 
everything became obsolete. The procedural paradigm that COBOL was created 
for became less and less relevant. Object oriented programming changed the 
face of the IT world. COBOL picked it up, but too little too late.

The "Language du jour" is a myth. Unlike the days when there was only COBOL, 
(and it WAS a "language du jour") modern environments use a number of 
different programming and scripting languages, selecting the best tools for 
the job, rather than manipulating the job to fit the only tool available.


> The instability that is rampant in IT
> today works to undermine the companies involved, in ways their
> management evidently doesn't see or understand.

I'm wondering exactly what you mean by "instability".  I don't look around 
IT and see "rampant instability"; I do see people using different tools to 
solve different problems but the solutions are no more or less "unstable" 
than they have always been. How long can a production system stay in 
production if it is truly "unstable"?

>
> When I was a young smartass I used to look down my nose at ordinary
> programming and thought that the world needed more superprogrammers,
> and the truly significant things were only done by the brightest and
> the best.

Yes, that was a popular misconception in many places for many years. "We 
don't write that kind of software; it gets written by experts in Detroit or 
Poughkeepskie, or Dayton..."  (The "modern" equivalent might be Redmond or 
Seattle), and then one day you need something so badly you simply can't wait 
for the vendor to do it, so you sit down and disassemble the compiler and 
find out how it works and bend it to your will...or, you come in contact 
with someone who has never bought into the "superprogrammer" idea and just 
inspires you by example.... the kind of guy who picks up an assembler manual 
for a machine he has never seen, works nights, and produces a new Operating 
System that is far better than the one the vendor gave you... It comes down 
to attitude.



> Later in life I came to realize that really good and useful
> work is mostly done by small, stable groups of ordinary but
> constructive programmers, groups with very low turnover.

That is often the case, mainly because they understand the business, having 
worked there most of their lives. It isn't exclsively so though. I've seen 
teams assmbled for a particular purpose achieve amazing things. It comes 
down to motivation, management, the quality of the people and corporate 
culture.

>This was
> really brought home to me by my acquaintance with a civil service
…[15 more quoted lines elided]…
> of software for a couple of decades.

Good example. The lady concerned betrayed a lack of experience.
>
> I think there is a parallel in the instability found in IT today.

What "instability"? Are you saying that anything NOT written in COBOL is 
"unstable"? That would be a very difficult position to defend.

> No
> language du jour offers benefits in more than the very short term that
> even begin to compare with what can be done with stable tools and
> platforms, even if the latter are not sexy.

Sorry, I disagree. In fact the converse is true, at least for me.  Since 
moving away from the "stability" of COBOL, I have more than doubled my 
productivity. The new languages and scripts are more powerful, take less 
time to write, and component based development means high level of re-use of 
code and minimal maintenance.

>And the work product of
> the stable tools, on a stable platform, is lasting, witness the
> millions or billions of lines of COBOL still doing useful work today.

And being rapidly outnumbered by even more billions of lines of other 
languages, every day. The "stability" you keep mentioning is NOT about 
languages it is about functionality. If you can isolate functionality and 
encapsulate it (and we know a lot more about how to do that now, than we did 
in days of yore), it really doesn't matter WHAT language you write it in. I 
have recently posted some code that I wrote in COBOL for a mainframe 35 
years ago. It is running today as a  .Net COM component on a web site, 
controlled by server side pre-compiled C# code-behind. 
(http://primacomputing.co.nz/cobol21/S2NTestServer.aspx) You can interact 
with it through a web page today, just as you would have through a green 
screen 35 years ago.  A tribute to the "stability" of COBOL?  Maybe. A 
tribute to the longevity of encapsulated functionality? Definitely. It could 
have been written in Fortran, Pascal, Algol, Assembler or Jovial and it 
would have been just as useful.

> The work product of the language and platform du jour is fairly likely
> to be discarded next year or the year after, when the next fashion
> trend strikes.

Oddly enough, it is only the peope who HAVEN'T embraced the new technology 
who see it that way. People using these languages to create objects and 
components that encapsulate functionality in a platform independent manner, 
are really not concerned about what is "fashionable". If a new language 
arrives that makes the job easier, or maybe the new language has a better 
innate implementation of the new paradigms, like Java implementing object 
oriented programming, then they will move to it. That isn't "wrong" or 
"unstable", it is effective computer programming. People observing it from 
"outside" see a "fashion change".  Swapping an axe for a chainsaw, isn't a 
"fashion change", it is an evolution. But if all you know is axes, you may 
well see it as "fashion".
>
> Personally I prefer to work with stable tools on stable platforms and
> solve challenges once, not the same challenge again and again on
> shifting ground.

Where's the fun in that? :-)

Pete.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-25T16:20:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gvegg2$cgn$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <74kml0F13dcc2U1@mid.individual.net> <74m4rnF1454jgU1@mid.individual.net> <955f9ba9-b95d-4b4c-9883-0ddf2f4dcdf8@r34g2000vba.googlegroups.com>`

```
In article <955f9ba9-b95d-4b4c-9883-0ddf2f4dcdf8@r34g2000vba.googlegroups.com>,
 <tjunker@tjunker.com> wrote:

[snip]

>When the outside rep caught wind of that she said two interesting
>things:  "That's impossible!" and "They're lying!"  Both were
>reasonable conclusions from her point of view, in her reality, but
>both were sadly wrong.

I have run across similar situations... my response is simple.  The rep. 
the client manager and I go into a closed room and I say ' With all due 
respect... Mr Jones here has accused me of telling lies.  I do not take 
such accusations lightly and therefore offer a solution slightly short of 
the Field of Honor.

'I have studied statistics, probability theory, project management 
workflow and based on this small bit of study I don't gamble... The House 
always wins.  I cannot let this insult pass, however, and I make the 
following offer: I am willing to wager a small amount - one pay check, 
mine against hers, that what I say can and will be done.  You, the client 
manager, will serve as the neutral party to ensure compliance.

'That's it.  One paycheck, mine against hers, that what I say will happen.  
We all know what money does and we all know what fertiliser does.  Ms 
Jones, that's what I'm willing to do... what are *you* willing to offer in 
response?'

I have never been taken up on that offer... and the Ms Jones-es of the 
world have given me a wide berth.  I am too busy doing my job to put up 
with that kind of trash.

DD
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 4)_

- **From:** "tlmfru" <lacey@mts.net>
- **Date:** 2009-04-15T11:07:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LEnFl.42458$ua7.2158@newsfe17.iad>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <74kml0F13dcc2U1@mid.individual.net>`

```

Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote in message
news:74kml0F13dcc2U1@mid.individual.net...
> tlmfru wrote:
> >
…[9 more quoted lines elided]…
>

\

I wasn't thinking of languages, more of concepts.  For instance, the
sequential file update using the "process the lowest key and write record
when the key changes" algorithm should be a standard method (non-OO
vocabulary)  taught to all programmers.  There are any number of "standards"
(in the musical sense, like Flatt & Scruggs) like that which should be
included in curriculi.  As far as the Prime is concerned, the language
(InfoBasic) is tedious, labour-intensive and not worth worrying about (apart
from those sites still using it!)  but the way it implements "select lists "
is definitely worth preserving.

PL
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2009-04-16T16:06:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gs84g801abo@news1.newsguy.com>`
- **In-Reply-To:** `<py4Fl.20748$Qh6.192@newsfe14.iad>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad>`

```
tlmfru wrote:
>
> I/T seems to lack the practice of other engineering disciplines -
that of
> preserving history for the benefit of future students of the field.

You just have to know where to find it. There are substantial efforts
to preserve IT history: the various Computer Museums, bitsavers.org,
textfiles.com, alt.folklore.computers, and so on. Academic work in
computing history is growing, including within the new but popular
field of "software studies".

On this topic, the OP might want to mention the resurrection of Wang
VS on alt.folklore.computers, where such things are frequently
discussed. Preferably with a bit more brevity than the rather lengthy
item here, but that is of course to the author's discretion.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-04-17T11:38:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74ptsaF154np2U1@mid.individual.net>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <gs84g801abo@news1.newsguy.com>`

```
Michael Wojcik wrote:
> tlmfru wrote:
>>
…[13 more quoted lines elided]…
> item here, but that is of course to the author's discretion.

I am completely neutral on Wang, never having used it.

However, I agree the post was too long. It was also repetitive and it made 
me keep thinking of Persil soap powder, for some inexplicable reason...

Pete.
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

- **From:** tjunker@tjunker.com
- **Date:** 2009-05-20T13:26:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59940d24-b7bf-4452-893a-33cbfea4e293@z5g2000vba.googlegroups.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad>`

```
On Apr 14, 12:24 pm, "tlmfru" <la...@mts.net> wrote:

> What's happening, of course,  is that there are applications developed in
> "Wang" that are working well enough that there's no psrticular urge to
> replace them, and a dwindling talent pool available to do it in any event.

While there is some truth to that in the wide context of COBOL apps in
general, that isn't our experience in the Wang VS world.  We do have
some stagnant sites but our strong ones, the majority, are active
production sites where the Wang VS runs the company.  That means it
isn't just an app, it's everything, and it has to evolve and grow to
match the requirements of the business.

Nor do we see the "dwindling talent pool" problem in the Wang VS
world.  Our production customers have no difficulty finding and
retaining programmers.  We even know of one site where their
applications are 100% in Wang VS Assembler language, almost a clone of
IBM BAL.  They have recruited IBM mainframe programmers and have even
trained up a few non-programmers to be VS Assembler programmers.

TJ
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-25T16:05:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gvefkr$38h$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <py4Fl.20748$Qh6.192@newsfe14.iad> <59940d24-b7bf-4452-893a-33cbfea4e293@z5g2000vba.googlegroups.com>`

```
In article <59940d24-b7bf-4452-893a-33cbfea4e293@z5g2000vba.googlegroups.com>,
 <tjunker@tjunker.com> wrote:

[snip]

>Nor do we see the "dwindling talent pool" problem in the Wang VS
>world.

New York: <http://www.indeed.com/jobs?q=wang&l=nyc>

Washington DC: <http://www.indeed.com/jobs?q=wang&l=dc>

Chicago: <http://www.indeed.com/jobs?q=wang&l=chicago>

Atlanta: <http://www.indeed.com/jobs?q=wang&l=atlanta>

Colordo: <http://www.indeed.com/jobs?q=wang&l=colorado>

San Frncisco: <http://www.indeed.com/jobs?q=wang&l=san+francisco>

Am I missing something?  As I've said, I enjoy the machine but I can't 
find anything out there that pays a decent rate... in fact, I can't find 
anything at all.  What am I doing wrong?

DD
```

##### ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

- **From:** tjunker@tjunker.com
- **Date:** 2009-05-20T13:07:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d90dc8df-54b1-4196-945b-33ba1b8c57d2@j12g2000vbl.googlegroups.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com>`

```
On Apr 14, 7:39 am, docdw...@panix.com () wrote:
> In article <bd6e07da-cfb5-4a98-8815-2ed360057...@y9g2000yqg.googlegroups.com>,
>
…[9 more quoted lines elided]…
> personally, find myself to be moderately underwhelmed.

With all due respect to your jaded cynicism, I don't care that you
find yourself moderately underwhelmed.  For a platform that was given
up for dead, 70 new systems (now 78), most full production sites
running companies, is not bad, and it's growing.  It's also keeping a
bunch of families alive in our companies and in Compucom, where the
vestiges of the old Wang Labs survive.

> This is not due to my experience with theWANGas a platform; I found it
> to be a real 'programmer's machine' upon which miracles could be worked in
> an amazingly short amount of time.  

Quite so.

> Granted that the I-O could get, at
> times, a bit... unstable (file corruption and record loss were, in my
> experience, common in anything more complex than dataset with more than
> two alternate indices);

You must have had a flaky system, perhaps an OS version in need of
update.  What you describe has certainly not been my experience at a
number of fairly large VS sites in mortgage, insurance, distribution
and manufacturing industries, with 300-500 users and very intensive
daily cycles of daytime online activity and nighttime report
generation.  Those systems could not have run had they the kinds of
problems you describe.  In fact, the VS file system is one of the most
resilient I have seen, usually surviving complete stoppages with no
corruption.  Of course after a power failure or system halt it is
necessary to do a scan for crashed files and reorganize any found.
Many sites didn't do that, to their ultimate regret.  Also, as the VS
declined, many sites dropped software support, a silly thing to do for
any software on which a company depends.  That meant they had no
recourse to dump analysis and patches, and no updates of software.
Such sites experienced degradation and just lived with it, but that
was certainly not the rule when the VS was strong.

> the user community was very supportive and
> miracles (for its time) could be worked.  I generated a COBOL program that
> would, for a given record, generate a pop-up window so that the user could
> jot free-form notes of unlimited length (the 2000-char LRECL took a bit of
> doing to overcome) in 1987.

Cool.  I worked mostly on large applications involving hundreds or
thousands of programs and hundreds of indexed files.  Along the way I
wrote many utilities to do system stuff, and many helper and fixup
programs in the application context.  In 46+ years I've never worked
with any systems more stable or easier to work with than properly
maintained Wang VS systems.

> That was considered to be Quite Something... in 1987.  Sadly, it seemed
> that scarcely a nickel's worth of R&D was invested since then;

I used to think that things at Wang started downhill in the late 1980s
but was surprised to read that their internal difficulties actually
began in the early 1980s, notably marked by the disaster of Fred
Wang's tenure before he was removed.  I think you're right that R&D
fell off drastically by the late 1980s, although crucial things like
the development of several VS12000 models and CPU upgrades of VS16000
and VS18000 occurred through the 1990s.  The VS couldn't have
continued as it did had the majority of the software infrastructure
not been created by very capable people in the early 1980s.  Major
features such as WSN and RSF date to the early 1980s, with PACE
probably being the last major feature, PACE 2 dating to the last half
of the 1980s.

> your
> posting mentioned a list of third-party developers of some 900 pages that
> was printed in 1989.
> That was two decades ago.

And your point is?  My point was to show how pervasive the VS was, not
is, and the strength of applications it had, not has.  It's true that
almost all the verticals have disappeared, although we are trying to
find those that may still exist on someone's shelf.  In DP, some
applications never really go out of date.

> I wish you the best of luck in your venture.

Thank you.  Really.  We're having fun and we're helping quite a few
substantial organizations that didn't jump ship in the 1990s.  Typical
is our largest customer, who said something like, "We love the VS, but
we weren't able to count on the hardware anymore and no new hardware
was in sight.  Your product is exactly what we need in this
situation.  Our applications do exactly what we need and want them to
do, and now we can continue to use and develop them."

I posted what I posted for those who _would_ be interested to see it.
There are literally millions of people who have had their hands on
Wang keyboards, and surprisingly large numbers of people who did
programming or operations or management around Wang VS systems.  With
a high water mark of about 30,000 systems (my estimate but validated
by those who were there in Wang at the time) you can roughly figure
out how many people were users, operators, programmers, and multiply
those numbers by staff turnover... it's a large number.  I've created
a new community site at wangvs.ning.com and it attracts people with
past VS experience and a sense of nostalgia as well as people
currently working with VS systems and our New VS.  My focus, though,
is not the past but the production present.  We stabilize VS sites and
make them once again fully viable.  The trick, though, will be to
figure out how to sell the New VS to folks who have never used a VS.

Regards,

Thomas Junker
tjunker at tjunker.com

The Unofficial Wang VS Information Center
http://www.tjunker.com/

Vice President
TransVirtual Systems
tjunker at transvirtualsystems.com
www.transvirtualsystems.com

Lightspeed NVS
www.lsnvs.com

Wang VS community
wangvs.ning.com

COBOL ReSource
www.cobolresource.com
```

###### ↳ ↳ ↳ Re: Wang COBOL alive and well as Wang VS makes a comeback

- **From:** docdwarf@panix.com ()
- **Date:** 2009-05-25T14:54:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gvebfv$2ca$1@reader1.panix.com>`
- **References:** `<bd6e07da-cfb5-4a98-8815-2ed360057fe1@y9g2000yqg.googlegroups.com> <gs23m8$bog$1@reader1.panix.com> <d90dc8df-54b1-4196-945b-33ba1b8c57d2@j12g2000vbl.googlegroups.com>`

```
In article <d90dc8df-54b1-4196-945b-33ba1b8c57d2@j12g2000vbl.googlegroups.com>,
 <tjunker@tjunker.com> wrote:
>On Apr 14, 7:39?am, docdw...@panix.com () wrote:
>> In article <bd6e07da-cfb5-4a98-8815-2ed360057...@y9g2000yqg.googlegroups.com>,
…[13 more quoted lines elided]…
>find yourself moderately underwhelmed.

Mr Junker, if you see calling attention to the fact that seventy systems 
sold in eleven countries constitutes an apparently neglibible number of 
the total number of systems of similar or greater power sold in even 
double the number of countries then I would suggest a course or two in 
statistics and market-share.

If you don't care about a posting then dealing with it is a rather simple 
matter... try using the Anciente Tactic of Not Replying and we all may be 
the richer. 

[snip]

>> That was considered to be Quite Something... in 1987. ?Sadly, it seemed
>> that scarcely a nickel's worth of R&D was invested since then;
…[12 more quoted lines elided]…
>of the 1980s.

It is now a few months away from the early '10s, Mr Junker.  Two decades, 
no R&D.

>
>> your
…[4 more quoted lines elided]…
>And your point is?

Slibhtly beyond your grasp, it seems... but I'll repeat it just in case 
SMTP jumbled the bits.


>My point was to show how pervasive the VS was, not
>is, and the strength of applications it had, not has.  It's true that
>almost all the verticals have disappeared, although we are trying to
>find those that may still exist on someone's shelf.  In DP, some
>applications never really go out of date.

My point was that in the last two decades quite a few improvements have 
been made in computers due to the investment of Research and Development.  
WANG has made nearly no investment in R&D in those twenty years and, as 
such, does not show the improvements.  In *any* disciplines there are some 
applications that never really go out of date... this does not mean that 
newer, faster, more reliable and more efficient developments should be 
neglected.  'If it ain't broke, don't fix it... but don't stop attempts to 
improve, either.'

>
>> I wish you the best of luck in your venture.
>
>Thank you.  Really.  We're having fun and we're helping quite a few
>substantial organizations that didn't jump ship in the 1990s.

You are welcome, really.  As I have said before the WANG is a 'coder's 
machine' and I had a Grande Olde Tyme working with them... two decades 
back.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
