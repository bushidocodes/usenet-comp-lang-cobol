[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# End of the century

_12 messages · 9 participants · 1994-11 → 1994-12_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### End of the century

- **From:** "joe.k..." <ua-author-12816976@usenetarchives.gap>
- **Date:** 1994-12-01T22:41:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
jts··.@pri··t.com wrote in a message to All:

›› Then again, there is such a thing as Julian dates (which I can store quit 
›› happily in 4 bytes).
 
› 1) Am I correct in understanding that Julian dating is the system in which
›   dates are represented by the number of days between the date in question
›   and a standard reference date?

jp> No. Julian date is the system in which dates are
jp> represented by the number of days since the beginning of the
jp> current year. Thus February 5 would always be Julian date
jp> 036. What you are referring to is called Lilian date. IBM
jp> has picked some date several centuries back for their
jp> mainframe development tools (haven't used it). Others have
jp> picked some other date. I think SAS uses Jan 1, 1961.

Actually I believe the starting date is Jan 1, 1900 in MVS.

Later,
Joe
---------
Fidonet: Joe Klemmer 1:109/370
Internet: Joe··.@f37··t.org
```

#### ↳ Re: End of the century

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-11-28T14:44:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
Gary Sharp (100··.@Com··e.COM) wrote:
: Is there any truth in the rumour that there a lot of BIG
: companies and corporations wo are running cobol accounts programs
: from years ago, and that these programs may not be written to
: recognise any dates after 31st Dec 1999, and that many of these
: companies have , er, "mislaid" the source code and cannot fix
: this problem-to-be?

: Good laugh if it's true!

Certainly true. Lots of older applications saved 2 characters by
ignoring the century. Especially true of accounting packages that
kept thousands/millions of records where the date is part of the key.
Shame because Cobol nicely provides an 8-digit date. I'm not so sure
that people actually 'lose' source code. More likely no one dares to
touch it, or knows what program does what. Or even knows how to a
program if they dared to change it. #-\
```

#### ↳ Re: End of the century

- **From:** "smr..." <ua-author-510208@usenetarchives.gap>
- **Date:** 1994-11-28T20:40:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
Why do you think so many people are predicting the Apocaplyse
for 1 Jan 2000?

 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ __________________________________
| | | | | | | | | | | | | | | | | | | | | smr··.@net··m.com	PO Box 1563
| | | | | | | | | | | | | | | | | | | | |             Cupertino, California
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_(xxx)xxx-xxxx_______________95015
```

#### ↳ Re: End of the century

- **From:** "mi..." <ua-author-617202@usenetarchives.gap>
- **Date:** 1994-11-29T09:53:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p4@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
In article <3bd3jr$2a2$1.··.@mha··e.com> Gary Sharp <100··.@Com··e.COM> writes:

› Is there any truth in the rumour that there a lot of BIG 
› companies and corporations wo are running cobol accounts programs 
…[3 more quoted lines elided]…
› this problem-to-be?

Yes, it's true that many of these legacy programs were written as
if the year 2000 would never come. A lot of these were written in the 1970's
by programmers who never for a moment thought that the work that they were
doing would be used for more than ten years. Then when you consider the more
recent advent of the 8 digit date field you have the explanation.

My company, Software Eclectics, Inc., developed a COBOL understanding tool
which will show programmers the date fields in COBOL programs. Enough said,
this isn't an ad.

I've not been told about source code being mislaid. Most of the time in
the larger programs, there have been numerous undocumented changes made over
the years. People are afraid to touch them at this point.
```

#### ↳ Re: End of the century

- **From:** "khor..." <ua-author-17073973@usenetarchives.gap>
- **Date:** 1994-11-30T10:29:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p5@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
In article <3bd3jr$2a2$1.··.@mha··e.com>, Gary Sharp <100··.@Com··e.COM> writes:
|> Is there any truth in the rumour that there a lot of BIG
|> companies and corporations who are running cobol accounts programs
…[5 more quoted lines elided]…
|> Good laugh if it's true!
...
A few TRUE/FALSE comments:

Turn of the century = 12/31/1999: FALSE
The first centry was the year 1 to year 100, 2nd centry 101-200, so the
new century starts 1/1/2001. This is a common misconception. (Decades too).

Source code MIA: TRUE
Most code is well tracked in companies, but there is always some MIA.

Pieter A. Hintjens writes:
› [lost source code] ... More likely no one dares to touch it, or knows what
› program does what. Or even knows how to [fix?] a program if they dared
› change it.

Knows what or how to fix a program: TRUE (somewhat)
There is a lot of code out there that is hard to understand and fix as well
as many levels of unknown program relationships. Trying to track down ALL
the code for dates in a application can be a nightmare, but with some good
testing, can be done.

Programs having a problem with the year change from 1999 to 2000: TRUE
But not just cobol. I remeber a problem with a LARGE computer operating
system having a problem not knowing about julian day 84366 (the 366th day
of the LEAP YEAR 1984), luckily not too much critical processing goes on
the day before new years. Again this LARGE computer company had a problem
with one of their system programs, where in 1992, processes on February 29th
showed up as 3/01/92. March 1st showed up as 3/02/92. This went on for
about a month before a fix was put in.


Good laugh if it's true: FALSE
I doubt too many people will be laughing. Some will be able to turn a profit
by offering services to companies to identify and correct year 2000 problems
before they happen, others will profit by comming in just after to clean up.
Some people may loose their jobs as scapegoats are looked for.
It may be hard to laugh if your checking account is not available or has the
wrong balance due to complications from date errors. Imagine if a utility
company bills you for a gaint amount because it's accounts shows that you have
a bill overdue by 99 years. Maybe funny at first, but it will take time to
straightten out, customer service time, and monies might not be collected in
a timely manner, and this could put this ficticious company in debt for not
having enough cash. But in the end, guess who really pays for this, that's
right, us, the customers, the big companies just pass the cost on down.
And then there is the media. The scare factor of 2000-itus (or whatever
cutesy media label catches on, 'date-gate'? 'computus-interruptus'?) will
be so outrageous, as to eclipse the Michaelangelo-virus scare a few years ago.


I don't mean to be scorching, over-serious, or show a lack of humor. I can
see the humor behind the situation, I just thought it would be good to put a
small wake-up call out there, and maybe, just maybe, stem some of the
negative counter-effects when we hit the year aught-aught (zero-zero).

P.S. Some of my code that relies on 2-digit year might just fail in 2000,
but I know some of it will fail in 2070. I coded a test for <70 = 20xx else
19xx. I sould be retired before then. (And the code should be retired way
before then.)

(How about 'aught-aught-ism'? I guess that wouldn't be PC. (politically
correct.))
```

#### ↳ Re: End of the century

- **From:** "har..." <ua-author-2202518@usenetarchives.gap>
- **Date:** 1994-12-02T07:29:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p6@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
In Article <3bd3jr$2a2$1.··.@mha··e.com>, Gary Sharp
<100··.@Com··e.COM> wrote:

› Is there any truth in the rumour that there a lot of BIG 
› companies and corporations wo are running cobol accounts programs 
…[3 more quoted lines elided]…
› this problem-to-be?

COBOL programs are just the tip of the iceberg. ANY KIND OF COMPUTER
ROUTINE that doesn't take century into account will break down. Not just
mainframe COBOL programs. I'm talking spreadsheets, DOS batch files, Unix
shell scripts, BASIC programs, etc., etc.

The popular assumption these days is that mainframe COBOL programs will be
the only thing affected by the turn of the century. Expect a whole new slew
of articles to appear in the trade press when other programs, etc. start to
break down.
---
* Harry Myhre
```

#### ↳ Re: End of the century

- **From:** "smr..." <ua-author-510208@usenetarchives.gap>
- **Date:** 1994-12-03T06:34:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p7@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
: What's this got to do with COBOL ? I've seen 'C' programs which do not
: take dates properly into account. I might just mean that a corporate
: is not as forward-looking as their prospectus would attempt to make you
: believe.

The C situation is more complicated. Dates in C are usually expressed
as number of seconds after an implied start of epoch date (1Jan1901 for
Unix). Which means the big change will be 4 billion seconds after the
start of the epoch, rather than 1Jan2000. (Or in something I wrote,
16,383 days after July 1994.)

The pair de_art_u_on a _ors_ _ _        +----------------------------------
and fare to fa| | |eir| |t| | | |ourse. | smr··.@net··m.com	PO Box 1563
Away! the wall| | |wei| |e| | | |e!     |             Cupertino, California
Away! the weal|_|_|d w|_|i|_|_|_|ne!    |_(xxx)xxx-xxxx_______________95015
```

#### ↳ Re: End of the century

- **From:** "ant..." <ua-author-6589789@usenetarchives.gap>
- **Date:** 1994-12-05T09:35:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p8@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
In article kho··.@csf··c.com (Keith Horowitz) writes:

› Turn of the century = 12/31/1999: FALSE
› The first centry was the year 1 to year 100, 2nd centry 101-200, so the
› new century starts 1/1/2001. This is a common misconception. (Decades too).

I beg to differ on the "Decades too" comment. For me, the '90s will always be
those years that have a '9' as the second to the last digit. The difference
is that decades are not numbered, they are just a reference to a group of
years.

Nuff said. If anyone dissagrees, lets take it to E-mail rather than generate
and off-topic thread in comp.lang.cobol.

BTW: The main reason I posted this was to test Trumpet under Windows 95.
Wasn't this more pleasant than a "Just testing" message ;-)

===============================================================================
Just say no to .signature files. | ant··.@rmc··t.com
===============================================================================
```

#### ↳ Re: End of the century

- **From:** "codecr..." <ua-author-7766424@usenetarchives.gap>
- **Date:** 1994-12-06T17:06:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p9@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
Although I too have coded quickie fixes for this sort of thing (i.e. year
less than 70, ergo century = 20) wouldn't a USAGE DATE be a wonderful
thing?

Problem is ... think about long-term bonds. Some of these go back to the
19th century or earlier. Also, a COBOL program used to keep track of
museum exhibits (catalogued, say, by approximate date of origin!) might
be a problem. But surely there must be a happy compromise -- say, a
64-bit unsigned integer-based sort of thing, with an accompanying
ABSURD-DATE exception?

Don? Has anyone proposed such a thing, now or in the past, and what
became of it?

Pete

(cod··.@cix··o.uk)
```

#### ↳ Re: End of the century

- **From:** "har..." <ua-author-2202518@usenetarchives.gap>
- **Date:** 1994-12-09T09:14:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p10@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
In Article <3c5ro5$9.··.@crl··l.com>, mg··.@c··.com (Michael G. Phillips) wrote:

› If not, use some contrived rule to decide when
› it's 19xx and when it's 20xx.

A friend and I at work had to write a routine like this a few years ago. We
have a file that carries year in a key, but not decade. You look at the
current date and then predict what the decade would be for the key in
question. It's all based on the fact that records in this particular file
are purged on a regular basis, so we never (crossing fingers) come across
ten year old records.
---
* Harry Myhre
```

#### ↳ Re: End of the century

- **From:** "har..." <ua-author-2202518@usenetarchives.gap>
- **Date:** 1994-12-13T10:09:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p11@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```

›› processing cycles, having to decode "number-of-days" to determine
›› if this account processes on the 15th or not is *much* more computing
›› than I want my computer to do on every record.

On most modern computers I think you'd have a hard time measuring the amount
of time it took to do this time of compare.
---
* Harry Myhre
```

#### ↳ Re: End of the century

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1994-12-20T16:55:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cdf3fe00e3-p12@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`
- **References:** `<ua-fallback-g55UM5lL0eY@usenetarchives.gap>`

```
In article <941220$214306$424··.@oze··m.au> Stephen Frost,
fro··.@oze··m.au writes:

› Actually, what I intended to convey was DDDDDD and pick a totally
› arbitrary
…[6 more quoted lines elided]…
› When I get time someday (like in the next 5 years...) I'll tackle it.

Why? COBOL 85 (the official one) includes functions that do exactly
that based on January 1, 1601 (not a completely arbitrary date).

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
