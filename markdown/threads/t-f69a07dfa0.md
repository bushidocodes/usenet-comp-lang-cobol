[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Home-Grown Utilities

_9 messages · 9 participants · 1997-04_

---

### Home-Grown Utilities

- **From:** "ar..." <ua-author-89056@usenetarchives.gap>
- **Date:** 1997-04-18T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jb0tc$64d@freenet-news.carleton.ca>`

```


Hi, everyone. Our shop is deep in the throes of revising zillions of lines of
COBOL code to make our systems Year 2000 compliant. There is a COBOL date
conversion routine which is called by just about every program out there.
In a nutshell, it converts Julian to Gregorian and vice-versa -- with
either a passed date or the system date. The code is not Year 2000 compliant.

I have told the Year 2000 task force that any program calling this
utility should not be certified Year 2000 compliant. I have urged the
developers to can the routine and use the intrinsic functions of COBOL for
MVS & VM. The Julian-Gregorian conversions can be done in just a couple
of lines of inline code.

Some developers are clamouring to have the date utility re-written to make
it Year 2000 compliant. I responded that I will vigorously oppose any
campaign to write a new utility. I am not a fan of home-grown roll-yer-own
utilities. Every large shop I am familiar with has been plagued by this.
In our shop the group that once laid claim to the myriad utilities is long
disbanded, and just who now owns them is the subject of high-level
discussions.

I have found that the need for most utilities in the first place is often
a matter for debate, whoever wrote them is usually long gone, and they
inevitably stop working as the technical infrastructure is upgraded. On
the other hand, management seems to traditionally be in favour of
utilities. I think it's due to the power and control that goes along with
enforcing their use. A lot of stuff I've seen is nothing more than an
effort by certain individuals to make themselves indispensible.

I intend to hang tough with my position. I welcome feedback from others on
this topic.
```

#### ↳ Re: Home-Grown Utilities

- **From:** "j. lenz" <ua-author-1081463@usenetarchives.gap>
- **Date:** 1997-04-18T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5jb0tc$64d@freenet-news.carleton.ca>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca>`

```

Forget about the old routine, and change every program that uses it to
use the new intrinsic functions for COBOL? This sounds short-sighted to
me.

Why not update the old routine to make it Y2K compliant, and recompile
all the programs that use it? Seems to me to be better way to handle
your situation.

Joseph Lenz
TTI, Inc.
Fort Worth, TX
```

#### ↳ Re: Home-Grown Utilities

- **From:** "bill schofield" <ua-author-8438784@usenetarchives.gap>
- **Date:** 1997-04-18T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5jb0tc$64d@freenet-news.carleton.ca>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca>`

```

Denis Belton wrote:

Hi, everyone. Our shop is deep in the throes of revising zillions of
lines of
COBOL code to make our systems Year 2000 compliant. There is a COBOL
date
conversion routine which is called by just about every program out
there.
In a nutshell, it converts Julian to Gregorian and vice-versa --
with
either a passed date or the system date. The code is not Year 2000
compliant.

I have told the Year 2000 task force that any program calling this
utility should not be certified Year 2000 compliant. I have urged
the
developers to can the routine and use the intrinsic functions of
COBOL for
MVS & VM. The Julian-Gregorian conversions can be done in just a
couple
of lines of inline code.

Some developers are clamouring to have the date utility re-written
to make
it Year 2000 compliant. I responded that I will vigorously oppose
any
campaign to write a new utility. I am not a fan of home-grown
roll-yer-own
utilities. Every large shop I am familiar with has been plagued by
this.
In our shop the group that once laid claim to the myriad utilities
is long
disbanded, and just who now owns them is the subject of high-level
discussions.

I have found that the need for most utilities in the first place is
often
a matter for debate, whoever wrote them is usually long gone, and
they
inevitably stop working as the technical infrastructure is upgraded.
On
the other hand, management seems to traditionally be in favour of
utilities. I think it's due to the power and control that goes along
with
enforcing their use. A lot of stuff I've seen is nothing more than
an
effort by certain individuals to make themselves indispensible.

I intend to hang tough with my position. I welcome feedback from
others on
this topic.
```

##### ↳ ↳ Re: Home-Grown Utilities

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1997-04-19T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f69a07dfa0-p3@usenetarchives.gap>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca> <gap-f69a07dfa0-p3@usenetarchives.gap>`

```

This *IS* a joke, right??

If not, then, Bill Schofield ??: you're a pompous ass.
You're also stupid, ignorant, and, obviously, have no idea what you're doing.
Maybe, if you stopped blowing your own horn for five seconds, and actually did
some >>thinking<<... assuming that you know how to >>think<< of course... it
may dawn on you to simply change the date conversion routine to be Y2k
compliant, and then recompile the associated programs. That would cut out about
10 or 20 billion lines of COBOL code immediately.

Whoa! Wait a minute... Revenue Canada?? Is that, like, the IRS of The Great
White North? Aha! Well, THAT would explain why you're employed there.

In that case... I take back everything I just typed.

Bill Schofield ?

You're doing an absolutely wonderful job, guy! Keep at it. Generate extra work,
mass confusion, alienation... hey!, that's why there's a Federal Government,
right??? :D :D :D
```

###### ↳ ↳ ↳ Re: Home-Grown Utilities

- **From:** "x" <ua-author-15970@usenetarchives.gap>
- **Date:** 1997-04-18T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-f69a07dfa0-p4@usenetarchives.gap>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca> <gap-f69a07dfa0-p3@usenetarchives.gap> <gap-f69a07dfa0-p4@usenetarchives.gap>`

```

Bill WAS joking, and it went right over your head!
```

#### ↳ Re: Home-Grown Utilities

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-04-19T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5jb0tc$64d@freenet-news.carleton.ca>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca>`

```

Denis Belton wrote in article
<5jb0tc$6.··.@fre··n.ca>...
› 
› Hi, everyone. Our shop is deep in the throes of revising zillions of
…[4 more quoted lines elided]…
› either a passed date or the system date.
 
› That was an excellent design decision.
 
› The code is not Year 2000 compliant.
 
› Fine - change the code to make it compliant.
› 
…[5 more quoted lines elided]…
› of lines of inline code. 

That's right - have date conversions scattered throughout the program
making maintenance a nightmare.

I had to modify a data sampling system 10 years ago. The turkey who wrote
it had TEN different functions to convert real time to a Julian type of
elapsed time and TEN to convert back. Every one was WRONG! I wrote one
function to convert time to Julian and one to convert back. This time it
was correct. They have the source code and it's well documented.

› Some developers are clamouring to have the date utility re-written to
› make
…[7 more quoted lines elided]…
› discussions.

This is a bad decision. You're refusal to have one pair of well documented
subroutines where your company owns the source code to scattering the code
about inline is not good.

› I have found that the need for most utilities in the first place is often
› a matter for debate, whoever wrote them is usually long gone, and they
…[4 more quoted lines elided]…
› effort by certain individuals to make themselves indispensible.

It appears that better documentation and standards are needed, not
abandonment of utilities.

› I intend to hang tough with my position. I welcome feedback from others
› on
› this topic.

I hope you change your mind. Why create an unneeded delay or a maintenance
nightmare when a pair of subroutines will solve your problem.

Remove the '-' from orion-data for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.
```

#### ↳ Re: Home-Grown Utilities

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-04-19T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p7@usenetarchives.gap>`
- **In-Reply-To:** `<5jb0tc$64d@freenet-news.carleton.ca>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca>`

```

Denis Belton wrote:
› 
› Hi, everyone. Our shop is deep in the throes of revising zillions of lines of
…[3 more quoted lines elided]…
› either a passed date or the system date. The code is not Year 2000 compliant.

We have an assembler routine which does this in my shop. I tested it for
Y2K compliance. Since it assumes year 00 is a leap year, it provides the
correct results for all dates with two digit years ranging from 01/01/1901
through 12/31/2099. I documented that fact in our standards manual. It is
sufficient to get us through our current crisis.

› 
› I have told the Year 2000 task force that any program calling this
…[3 more quoted lines elided]…
› of lines of inline code.

Any shop which has COBOL/MVS should use the intrinsic functions for dates.
There would be no need for the vast majority of utility date routines. But
my shop won't install COBOL/MVS until next September, which is too late for
Y2K conversions already underway.

I recently attended a project kickoff meeting for LE/370 and COBOL/MVS. My
shop has several different mainframe development groups. My group has been
using COBOL II for about five years. Another very large group is still using
OS/VS COBOL, and is considering converting to COBOL II. They were SHOCKED to
hear we are considering cancelling our COBOL II license. There's no sense
paying license fees for both COBOL II and COBOL/MVS. Unfortunately, we pay
no license fee for OS/VS COBOL, and it's been very difficult to get rid of
it. There is a lot of resistance to change, which shows up as complaints
that the newer compilers are too hard to learn, produce less efficient code,
and are not as reliable.

› 
› Some developers are clamouring to have the date utility re-written to make
…[5 more quoted lines elided]…
› discussions.

While it may not be the optimum solution, I would advocate changing the date
utility if it is dynamically called. It is much less work and testing risk
to correct a date utility that to change every program that calls it.

I recently corrected two assembler date routines, one for day-of-week and one
for date-difference, to window them for two-digit years from 1950 to 2049.
The only reason for doing this was to reduce the amount of programming effort
to achieve some level of Y2K compliance.

I know of another date routine (in far fewer programs) that no one owns and
is not being changed. All those users need to convert to something else,
that will be a huge effort. That particular utility caused a very expensive
failure in December, 1992, due to a leap year related bug. Part of that
problem was political -- we couldn't determine which department owned that
routine to fix it. And that routine will fail after 12/31/1999.

I have also written utility date routines which require a four-digit year,
and one which will window a two-digit year into a four-digit year. If COBOL
for MVS and VM had been installed a year ago, I would have used intrinsics
instead. But it won't even be available to me until next September, and it
won't work for all our CICS regions. We're still running some CICS 2.1.2.
There's a separate project getting started to convert all our 50+ production
CICS regions to release 4.1.

You are absolutely right about the problem of support for these kinds of
utilities. Our tech services area was down-sized a while ago, and the
remaining staff is far too busy to fix those routines. They practically
kissed my feet when I fixed two of them.

› 
› I have found that the need for most utilities in the first place is often
…[5 more quoted lines elided]…
› effort by certain individuals to make themselves indispensible.

Certainly the value of some of these utilities is debatable. We are still
trying to stamp out assembler programs for accessing VSAM files, BDAM files,
and for calling subprograms dynamically. But right now the programmers in my
shop have no way to obtain current YYYYMMDD unless some utility is written
for that purpose. They still need to calculate the day-of-week,
date-difference, and generate future dates. Even if COBOL/MVS was available
to them right now, they would have great difficulty changing all the programs
in time.

› 
› I intend to hang tough with my position. I welcome feedback from others on
…[4 more quoted lines elided]…
› Revenue Canada

I would suggest you consider fixing the date routine, =IF= it would actually
reduce the programming effort required to survive Y2K. If your development
process is well-controlled, you could require all new programs to use
intrinsic date functions. Eventually, you could require all changed programs
to convert to intrinsics, but you have to survive the current crisis.

Sometimes the Best is the enemy of the Good.

I'm willing to accept a reasonably good Y2K solution if I can't have the
Best solution in time. Rewriting the entire inventory is not an option for
most shops. The question is, what's the best solution that can be achieved
under all the constraints of available time and programming staff.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Home-Grown Utilities

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-04-20T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p8@usenetarchives.gap>`
- **In-Reply-To:** `<5jb0tc$64d@freenet-news.carleton.ca>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca>`

```



Denis Belton wrote in article
<5jb0tc$6.··.@fre··n.ca>...
› 
› Hi, everyone. Our shop is deep in the throes of revising zillions of
…[23 more quoted lines elided]…
› discussions.


In the interest of clarity and ease of conversion, since your task is huge,
I would recommend rewriting the called routing USING the intrinsic function
calls. Yes these could be in each program, but this will ease the
conversion project considerably.
```

#### ↳ Re: Home-Grown Utilities

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1997-04-22T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f69a07dfa0-p9@usenetarchives.gap>`
- **In-Reply-To:** `<5jb0tc$64d@freenet-news.carleton.ca>`
- **References:** `<5jb0tc$64d@freenet-news.carleton.ca>`

```

One of my duties at the place where I am contracting my services is to look
at the various date routines that they have. The desire is to reduce the
number to just one. Since they use applications software from multiple
vendors it is highly probable that there will be multiple date formats.
There also will be each vendor's method of handling things. It is my
contention that when writing a program to deal with a file/database from
vendor X, one should use vendor X's file handling and date handling routines.
These may be in COBOL copybooks or separately compiled subroutines. Some
vendor may even be using a copybook containing one or more nested programs to
be called. The advantage to such a policy is that you are consistent in
handling that vendor's data. Also changes in those two areas can be left
with the vendor to do at the cost only of a recompilation depending on
methodology.

I have recommended the use of the vendor routines, hopefully with the ability
to use one of the methodologies for all programs not related to a given
vendor. If that is not the case I have recommended using one separately
compiled COBOL sub-routine for all non-vendor related date programming.
There are other alternatives such as specific routines for each function
versus one omnibus routine, using assembler, using nested programs or a
common perform copybook. Each of these alternatives has either performance
or maintenance advantages.

The use of a common routine also has the advantage of standardizing the date
handling. The COBOL functions are inadequate or too slow for many of the
functions. A gregorian to julian (IBM not astronomical) date is far less
expensive in terms of time if coded directly than if FUNCTION DAY-OF-INTEGER
(FUNCTION INTEGER-OF-DAY (field-name)) is used (at least on COBOL for MVS and
VM). There may be other organization specific date calculations that should
be standardized. One group should have the responsibility for all of the
utility functions within a given organization. The tradeoffs are many and
careful thought should be given to the alternatives. I know that I will not
feel that fantastic advice was ignored if a different set of options is
chosen in place of my recommendations. There are just too many factors
involved to say that there is one right way.
›  
› Denis Belton wrote: 
…[64 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at mor··.@nbn··b.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
