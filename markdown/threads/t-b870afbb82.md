[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Newbie question

_19 messages · 18 participants · 1998-02 → 1998-03_

**Topics:** [`Tutorials, books, learning`](../topics.md#learning) · [`Help requests and how-to`](../topics.md#help)

---

### Newbie question

- **From:** "stephen kim" <ua-author-17084136@usenetarchives.gap>
- **Date:** 1998-02-23T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#OnGqFbQ9GA.242@upnetnews04>`

```

Just curious about a couple of things.

1) What is the most time consuming portion of a Year 2000 project?

2) Which is used more often in Y2K fix? the 8 digit format, 6 digit with
windowing, or 6 digit w/o windowing.

3) What is the average project time in a Y2K project in terms of lines of
code?

Thanks.
(Newbie flame shield on)
```

#### ↳ Re: Newbie question

- **From:** "kiy..." <ua-author-598721@usenetarchives.gap>
- **Date:** 1998-02-24T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p2@usenetarchives.gap>`
- **In-Reply-To:** `<#OnGqFbQ9GA.242@upnetnews04>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04>`

```

In <#OnGqFbQ9GA.242@upnetnews04>, "Stephen Kim" writes:
› Just curious about a couple of things.
›
› 1) What is the most time consuming portion of a Year 2000 project?

Given that most companies haven't started remediation, it's obvious that the
realization phase is enormous, perhaps decades long.

›
› 2) Which is used more often in Y2K fix? the 8 digit format, 6 digit with
› windowing, or 6 digit w/o windowing.

The few that have started that I know of are using 5 digit windows which
means that the Y2K problem never ends. It is a perfect perpetual job
generator for programmers and window-washers. That is, internal form 99365,
12/31/1999, external. Yes this is U.S. centric.

›
› 3) What is the average project time in a Y2K project in terms of lines of
› code?

Time in lines of code? Let me tell you, this is the ship that made the Kessel
run in 9 parsecs, it's fast enough for you, kid.

›
› Thanks.
› (Newbie flame shield on)
›

cory hamasaki
```

##### ↳ ↳ Re: Newbie question

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-02-24T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p2@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p2@usenetarchives.gap>`

```

In article <34f··.@new··m.net>,
cory hamasaki wrote:

[snippage]
›
› Time in lines of code? Let me tell you, this is the ship that made the Kessel
› run in 9 parsecs, it's fast enough for you, kid.

Good to see that someone else went 'BLEARGH!' at that line... did you know
I used to make the 100-yard-dash in 300 feet?

DD
```

###### ↳ ↳ ↳ Re: Newbie question

- **From:** "lodge vice-chief" <ua-author-17074836@usenetarchives.gap>
- **Date:** 1998-03-09T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p3@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p2@usenetarchives.gap> <gap-b870afbb82-p3@usenetarchives.gap>`

```

Heh

doc··.@cl··k.net wrote:

› In article <34f··.@new··m.net>,
› cory hamasaki  wrote:
…[9 more quoted lines elided]…
› DD
```

#### ↳ Re: Newbie question

- **From:** "mark slaughter" <ua-author-8441784@usenetarchives.gap>
- **Date:** 1998-02-24T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p5@usenetarchives.gap>`
- **In-Reply-To:** `<#OnGqFbQ9GA.242@upnetnews04>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04>`

```


Stephen Kim wrote in message <#OnGqFbQ9GA.242@upnetnews04>...
› Just curious about a couple of things.
›
› 1) What is the most time consuming portion of a Year 2000 project?
›

Reading this news group
```

#### ↳ Re: Newbie question

- **From:** "scott secor" <ua-author-2710966@usenetarchives.gap>
- **Date:** 1998-02-24T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p6@usenetarchives.gap>`
- **In-Reply-To:** `<#OnGqFbQ9GA.242@upnetnews04>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04>`

```

Stephen Kim wrote in message <#OnGqFbQ9GA.242@upnetnews04>...
› Just curious about a couple of things.
› 
› 1) What is the most time consuming portion of a Year 2000 project?
 
 
› Fixing and testing ... the boring, thankless parts.
 
› 2) Which is used more often in Y2K fix? the 8 digit format, 6 digit with
› windowing, or 6 digit w/o windowing.

8-digits ONLY! Windowing is downright DANGEROUS when you are expected to
interface with dissimilar systems. It guaranties a glich per decade in the
next century.

› 3) What is the average project time in a Y2K project in terms of lines of
› code?

Too vague. One man offices can often be remediated in a day or two, major
corporations or government agencies will take years. For example, the
Department of Defense has been working on their issues for a couple of years
and expect completion in 2012. Does the term "duh" mean anything here?

Ciao,

Scott "asbestos underwear not required" Secor
```

##### ↳ ↳ Re: Newbie question

- **From:** "crys..." <ua-author-1603444@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p6@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p6@usenetarchives.gap>`

```

In article <34f··.@new··t.net>,
"Scott Secor" wrote:



<....>

› 8-digits ONLY! Windowing is downright DANGEROUS when you are expected
› to interface with dissimilar systems.

I've noticed you say this more than once and I'd like to ask you to go
into some detail on why you feel that way. Not for the concept of
expansion vs. windowing - I know that expansion is the one true way -
but why the reference to interface systems?

If you use windowing, it's internal to the system it's being used in and
doesn't affect the interfaces just because you've used it. When the
window calculation is done in the retreival/calculation functions in the
affected program and then the correct number is written to the file that
will be passed to the outside systems, where is the danger point?

At least that's been my experience so far...if there's a hole in it
somewhere that I'm missing I'd sure like to know about it now.

OG
```

#### ↳ Re: Newbie question

- **From:** "stev..." <ua-author-17074205@usenetarchives.gap>
- **Date:** 1998-02-27T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p8@usenetarchives.gap>`
- **In-Reply-To:** `<#OnGqFbQ9GA.242@upnetnews04>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04>`

```

On Tue, 24 Feb 1998 19:51:34 -1000, "Stephen Kim"
wrote:

› Just curious about a couple of things.
› 
…[11 more quoted lines elided]…
› 
What you are asking is very difficult to answer definitively as there
are many variable involved. However, based on the Y2K project I am
currently involved in, I can tell you:

1) The most time consuming portion of the Y2K project is the
Enterprise Testing portion, which we have scheduled at almost 1 year
in length.

2) This would depend on your applications and systems. 6 digit
windowing is the quickest fix, but should be followed up with file
expansion/8 digit dates as soon as possible. I don't believe 6 digit
without windowing is a viable solution.

3) Judging time of the project on lines of code is difficult to
measure because it also depends on how many resources you have and
what methodologies your are using to apply fixes (on-site manual,
offshore, factory). For a medium size shop utilizing all three
methodologies, expect renovation and system testing to take one year.

Hope this helps.



////
(o o)
-oOO--(_)--OOo-

Here's Looking at ya!
Steve
```

##### ↳ ↳ Re: Newbie question

- **From:** "rene..." <ua-author-6375353@usenetarchives.gap>
- **Date:** 1998-02-27T19:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p8@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p8@usenetarchives.gap>`

```

On Tue, 24 Feb 1998 19:51:34 -1000, "Stephen Kim"
wrote:
›
› Just curious about a couple of things.
›
› 1) What is the most time consuming portion of a Year 2000 project?
›
In our shop, the most time consuming factor is testing, by far. I
would guess that it takes about 4 times longer to test than it does to
analyze and change the code.

› 2) Which is used more often in Y2K fix? the 8 digit format, 6 digit with
› windowing, or 6 digit w/o windowing.
›
Our shop has gone primarly with the 8 digit (and 7 digit julian)
format. We do some 6 digit windowing, but, at least in our situation,
6 digit non-windowing really isn't an option.

› 3) What is the average project time in a Y2K project in terms of lines of
› code?
›
Wow, this can really vary. The low end is probably around 5-6 lines.
High end, for me at least, has been around 200 lines. It really
depends on the particular type of programs you are working with...

› Thanks.
› (Newbie flame shield on)
›


Dave


You may e-mail replies to: renegade at (@) dwx dot (.) com
```

#### ↳ Re: Newbie question

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-03-01T19:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p10@usenetarchives.gap>`
- **In-Reply-To:** `<#OnGqFbQ9GA.242@upnetnews04>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04>`

```

Stephen Kim wrote:
› 
› Just curious about a couple of things.
…[10 more quoted lines elided]…
› (Newbie flame shield on)

Question 1.
Investigation and design of the fix should be the largest portion.
2nd is the testing phase.
3rd is the implementation phase.
the least is the coding phase.
(the above estimation is based on mainframe system only)

Question 2. I believe is the 8 digit approach.

Question 3. Depends on the complexity of the system. Don't trust those
lines of code figure. It's just a number games. Have you even study
statistic? You can always create the kind of result your manager loves
to see by using difference model.

Rgds,
Chip Ling
chi··.@sym··o.ca
```

#### ↳ Re: Newbie question

- **From:** "cit..." <ua-author-571523@usenetarchives.gap>
- **Date:** 1998-03-04T19:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p11@usenetarchives.gap>`
- **In-Reply-To:** `<#OnGqFbQ9GA.242@upnetnews04>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04>`

```

› 1) What is the most time consuming portion of a Year 2000 project?

Filling out all the paperwork required by the corporate
bean counter monkeys and C.Y.A. lawyers.

› 2) Which is used more often in Y2K fix? the 8 digit format, 6 digit with
› windowing, or 6 digit w/o windowing.

The 8 digit way is the correct way. Windowing requires writing
program logic which could cause incompatibilities with other
systems or outside vendors. "MOST" of the time, I can simply
expand the date field without seriously affecting program
logic. Windowing requires writing new logic which then has
to be tested as a program enhancement - more difficult, more
mistakes, more time, more bugs.

› 3) What is the average project time in a Y2K project in terms of lines of
› code?
Unknown. Totally system dependent.
```

##### ↳ ↳ Re: Newbie question

- **From:** "david virgil" <ua-author-17071569@usenetarchives.gap>
- **Date:** 1998-03-04T19:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p11@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap>`

```



Cit··.@Cr··s.Com [Ron] wrote in article
<6dkrlh$s.··.@exa··c.net>...

›› 2) Which is used more often in Y2K fix? the 8 digit format, 6 digit with
›› windowing, or 6 digit w/o windowing.
…[7 more quoted lines elided]…
›     mistakes, more time, more bugs.

Oops, I can't agree with this. Accounting systems, GL, AP, etc; often
don't need more than a few years of detail. With that in mind, are you
going to subject people to using 8 digit dates forever? I don't think so.
Depending on how long you think the system will be used, 6 digits with
windowing is a good solution. You can turn it off in a few years, after
such a time when it isn't important. (Like maybe 2002)

A better answer is that you must consider many aspects to deciding which
solution to use. I'm being forced to solve the Y2K issue in several
different ways. Each is different.


David Virgil
dvi··.@fox··l.com
```

###### ↳ ↳ ↳ Re: Newbie question

- **From:** "n..." <ua-author-39527@usenetarchives.gap>
- **Date:** 1998-03-04T19:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p12@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap> <gap-b870afbb82-p12@usenetarchives.gap>`

```

In article <01bd485d$cbb16180$71539ecf@dvirgil>, "David Virgil" says:
› 
› 
…[25 more quoted lines elided]…
› 
There's really two issues: date storage and date input.

It's unforgiveable these days to store 2-digit years in databases
if you can help it. (You may be forced to fix some ancient horror this
way by circumstances, though)

Date input is a different matter. IMHO the "right thing" is to
process every input date via a subroutine that accepts both the
date entered (text) and a specification of the validity range.
If that range is small, then it's both easy and sensible to
allow two-digit years to be keyed, translated by the routine into
4-digit years, and returned for internal storage or processing.
This same routine can also handle MM/DD/YY vs DD/MM/YY by reference
to the location of the person doing the keying, and of course
it helps prevent any number of possible foul-ups as a result of
an operator typing (say) 87 instead of 98, by reference to a
validity range that specifies +/- one year, or always in the future.

It's also the "right thing" for the operator to immediately see
the expanded 4-digit date on his or here screen as soon as it's
entered.

Of course, if you are fixing up ancient horrors then doing the right
thing is probably not practical!
```

###### ↳ ↳ ↳ Re: Newbie question

_(reply depth: 4)_

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-03-04T19:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p13@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap> <gap-b870afbb82-p12@usenetarchives.gap> <gap-b870afbb82-p13@usenetarchives.gap>`

```

In article <6dmver$8d$1.··.@wil··c.uk>,
Nigel Arnot wrote:

[snippage des etoufee]

›
› Of course, if you are fixing up ancient horrors then doing the right
› thing is probably not practical!

Curious you should mention that... I'm working on a chunk o' code right
now, one of the more recent programs written in 1982 and run thru a
structuring engine in 1987... last compiled in 1991, a veritable infant of
a program. Anyhow, in checking the code we found that this thing had been
running in error for the past 8 years, seems someone used a single-digit
target for a two-digit subscript... throwing out a garbage-report every
month, like clockwork. Since the two-digit subscript was a kind of a date
(MM) I went in and cleaned it up...

... and the user just *beamed*... for a good thirty seconds... and then
started with 'Well, we haven't looked at this one for a while, of course,
but now that you mention it... *this* classification was discontinued,
these *two* have been rolled into one new one... oh, and now we are
sorting everything in inverse barometric pressure sequence... while you're
in there can you clean it up? Allyagottadois...'

DD
```

###### ↳ ↳ ↳ Re: Newbie question

_(reply depth: 4)_

- **From:** "christopher clark" <ua-author-11702837@usenetarchives.gap>
- **Date:** 1998-03-05T19:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p13@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap> <gap-b870afbb82-p12@usenetarchives.gap> <gap-b870afbb82-p13@usenetarchives.gap>`

```



Nigel Arnot wrote:

›››› 2) Which is used more often in Y2K fix? the 8 digit format, 6 digit with
›››› windowing, or 6 digit w/o windowing.
›› 
›› Oops, I can't agree with this.  Accounting systems, GL, AP, etc; often
›› don't need more than a few years of detail.  With that in mind, are you

You lucky, lucky person... We've got one client that insists on keepingevery scrap of
accounting data, even after Revenue Canada's 7-year
limit...

› There's really two issues: date storage and date input.
 
›     You missed date output.
 
› an operator typing (say) 87 instead of 98, by reference to a
› validity range that specifies +/- one year, or always in the future.
 
›     Assuming your users never have to go back and redo something...
 
› It's also the "right thing" for the operator to immediately see
› the expanded 4-digit date on his or here screen as soon as it's
› entered.
 
›     IME, that just annoys or confuses most users.
 
› Of course, if you are fixing up ancient horrors then doing the right
› thing is probably not practical!

I don't know if fixing up ancient horrors _can_ ever be the right thing...

@>-`--,--
Chris Clark
com··.@cad··n.com
kit··.@hot··l.com
```

###### ↳ ↳ ↳ Re: Newbie question

_(reply depth: 4)_

- **From:** "gary lee nsp" <ua-author-17074378@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p13@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap> <gap-b870afbb82-p12@usenetarchives.gap> <gap-b870afbb82-p13@usenetarchives.gap>`

```

------------ snip -------------------------------
›› Cit··.@Cr··s.Com [Ron] wrote in article
›› <6dkrlh$s.··.@exa··c.net>...
…[4 more quoted lines elided]…
››› 
----------------- major snip --------------------------------
Actually, you might say that the most common is the solution used
internally by virtually every DBMS. Don't represent your dates as any
combination of years, months and days internally. Instead, represent them
as an absolute number of days from some arbitrary starting date. Come to
think of it, most operating systems (DOS, MVS, UNIX, OS/400, etc.) also do
this.

Once you have decided on a base date, you need two routines for each input
and display format with which you need to deal, as in
absolute-->mm/dd/yyyy, and mm/dd/yyyy to absolute. If you need any other
routines, (e.g., mm/dd/yyyy-->julian), you go to absolute as an
intermediate.

This has some real advantages. First, there are many calculations used in
real world business applications (interest accrual, inventory spoilage,
tracking Hale-Bopp, etc.) where the interval between two dates is the
important thing. With absolute dates, you can say SUBTRACT START-DATE FROM
END-DATE GIVING NUMBER-OF-DAYS. Try calculating that with mm/dd/yyyy
fields (I've seen the routines some people have written...they're not
pretty, and often not accurate).

Another advantage is that if you have to exchange dates with another system
using absolute date (say, for example, DB2) you only have to take the base
absolute date in the source, expressed in the target, and add. Say, for
example, you used 01/01/1960, and you want to convert to SAS dates (which
use 01/01/1900, I think). The correct calculation would be SAS-DATE =
YOUR-DATE + '01/01/1960'D. It doesn't even matter whether your system's
base date is earlier, later, the same as the target, or if you have no clue
what the base date in the target system is.

As to the 'range of relevancy', or how long this date will last, an
unsigned four byte binary will give you a couple of million years of
accurate dates. As an alternative, take this down to seconds for a
date-time, and you get about 300 years.

Popular starting dates are 01/01/0000, 01/01/0001, 01/01/1960, 01/01/80,
01/01/1522 (or thereabouts), or whatever else turns your crank. I suggest
a date which is 01/01/yyyy, where yyyy is a multiple of 400, for the leap
year thing. The calculation for LEAP-YEAR YES/NO becomes very simple then.


If you do need to actually go earlier than 1522, however, you need to make
some adjustments for a non-Gregorian calendar.

And no, I'm not talking about julian dates.

Gary Lee, Consultec, Inc. and points West.
```

###### ↳ ↳ ↳ Re: Newbie question

_(reply depth: 5)_

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p16@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap> <gap-b870afbb82-p12@usenetarchives.gap> <gap-b870afbb82-p13@usenetarchives.gap> <gap-b870afbb82-p16@usenetarchives.gap>`

```

And the nice/easy thing about using an integer-from-a-start-date approach
for storing data is that COBOL has native language (that is portable across
ANSI implementations) to get such a date and to convert from/to it. See the
intrinsic functions

INTEGER-TO-DATE
INTEGER-TO-DAY
DATE-TO-INTEGER
DAY-TO-INTEGER

This is a great solution for new development and major application
overhauls. On the other hand, I can't see many companies having the time
and resources for doing remediation by changing all their programs and data
to this approach at this late stage of the problem.
```

###### ↳ ↳ ↳ Re: Newbie question

_(reply depth: 6)_

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-03-10T19:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p17@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap> <gap-b870afbb82-p12@usenetarchives.gap> <gap-b870afbb82-p13@usenetarchives.gap> <gap-b870afbb82-p16@usenetarchives.gap> <gap-b870afbb82-p17@usenetarchives.gap>`

```

In article <6e5rk5$u.··.@sjx··m.com>, wmk··.@ix.··m.com says...

› This is a great solution for new development and major application
› overhauls.  On the other hand, I can't see many companies having the time
› and resources for doing remediation by changing all their programs and data
› to this approach at this late stage of the problem.

A bigger concern at the moment that I'm seeing from systems I'm working on are
the EC EMU (European Monetary Union) criteria. This could have more to do with
the types of systems I'm working with but it's a much larger problem to fix
than Y2K. Y2K is dead easy to fix if you know what you're doing and the system
is reasonably well written in the first place.

Shaun
```

###### ↳ ↳ ↳ Re: Newbie question

_(reply depth: 5)_

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-03-11T19:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b870afbb82-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b870afbb82-p16@usenetarchives.gap>`
- **References:** `<#OnGqFbQ9GA.242@upnetnews04> <gap-b870afbb82-p11@usenetarchives.gap> <gap-b870afbb82-p12@usenetarchives.gap> <gap-b870afbb82-p13@usenetarchives.gap> <gap-b870afbb82-p16@usenetarchives.gap>`

```

Dear all:

Gary Lee NSP wrote:
[8< First part of plee for absolute date]
› This has some real advantages.  First, there are many calculations used in
› real world business applications (interest accrual, inventory spoilage,
…[4 more quoted lines elided]…
› pretty, and often not accurate).
[8< Rest of plee]

An abs.date has not all. The ccyy/mm/dd format, extenden to
ccyy/mm/dd/hh:mm:ss.dcm etc has the advantage that a difference in
calendar months is easily calculated. Leasing and lending periods cars,
repay periods of loans etc. are pretty much expressed in months. Taxes
based on property-value with a change in value during the calendar year
are calculated relativly to months/weeks (at least in my country).
Having two abs.date requires conversion to the ccyy/mm/dd format to get
an integer number of months! Time is a strange thing, however.

Being a little off-topic perhaps, but still cobol-related:

In an object oriented solution all those problems are non-existing (when
well-implemented). Dates and times are just objects that are addable to
and subtractable from each other. Internal representation will undoubtly
be in the absolute format, but presentation, functionality like
"giveDiffInMonths", Gregorian issues, time zone differences,
geographical differences (f.e. implementation date of greg calendar
type) etc. are all encapsultable.

Waiting for the junp to The New Standard,

The Cobol Frog
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
