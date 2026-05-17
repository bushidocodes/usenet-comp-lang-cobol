[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL research - help!!!

_22 messages · 17 participants · 1998-05_

---

### COBOL research - help!!!

- **From:** "david_..." <ua-author-761663@usenetarchives.gap>
- **Date:** 1998-05-21T05:04:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`

```

I'm doing some research on COBOL related Year 2000 issues, and need your help
- please!

I'm particularly interested in finding out whether and to what extent some
COBOL applications may fail in 1999 because of the use of 99 to signify 'end
file' or 'date not known'. I would welcome any advice (in simple English -
I'm only just IT literate enough to have registered for this group) on the
following:

1 I understand that COBOL is a language, and therefore may have been used as
a platform for any number of applications, but I would really like to get a
handle on which sorts of systems that ordinary people use (or are affected
by) are generally (or have historically generally been) COBOL based (I'd like
examples that people can easily relate to - eg airline ticketing operations,
payroll systems, etc);

2 I'd also like a better idea of the scale of the problem - to what extent
are such systems still in use (almost all/50%/very few etc). Again, I'd like
a better picture of just how much chaos people can expect - has the media
been overhyping even a little bit, or have people still really no idea how
critical the problems are likely to be?

3 As mentioned above, I gather that aside from the two-digit year notation
another problem with COBOL in relation to Year 2000 compliance is the use of
00 or 99 to indicate 'end file' or 'date not known'. Do all versions of
COBOL work like this, or are there more modern versions that use different
methods to flag the same things? Also, are there any other languages aside
from COBOL that work in the same way (ie use 00 or 99 to mean something other
than the numbers they represent)? If so, could they also fail to calculate
dates correctly?

4 I am trying to understand whether there is any risk that some systems could
fail before 2000 (ie in 1999) because of the use of 99 to mean 'end file' or
'date not known', and would be particularly grateful for examples of any
specific cases that you may have come across.

If you can help me out with any of these (or even think I need help
understanding the problem better) I would be really grateful for your
comments.

Thank you.

David Naylor

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: COBOL research - help!!!

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`

```

Dav··.@my-··s.com wrote:
› 
› (snipped)
…[6 more quoted lines elided]…
› http://www.dejanews.com/   Now offering spam-free web-based newsreading

David,

I've posted on this topic on 'comp.software.year-2000' more than once -
you might try a DejaNews search there.

With respect to my current position, I work for a NYC bank in the
securities processing area (we do a lot of custodial work). The only
signal date I'm aware of in the securities movement & control (smac)
area is "99/09/09". This is used to indicate a financial instrument with
an open maturity date, e.g., a REPO. If we did nothing, these
instruments would mature and settle on Sept. 9, 1999; the world would
not end suddenly, nor would our form of life be converted from carbon to
sulfur. Our plan is to deal with this (only a dozen, or so, programs
involved) after our y2K conversion is done, It'll be tested and in
production by July 1, 1999.

HTH,
Bill Lynch

PS: Our Y2K project, bank wide, is going surprisingly well, running
ahead of schedule:-)
```

#### ↳ Re: COBOL research - help!!!

- **From:** "dennis j. minette" <ua-author-8528253@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`

```

invisible ink?

Donald Tees wrote in message <6k1hrq$ruv$1.··.@new··s.net>...
›
›
›
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p3@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p3@usenetarchives.gap>`

```

invisible ink?

Donald Tees wrote in message <6k1hrq$ruv$1.··.@new··s.net>...
›

My mouse hiccuped. Damned cats are buggering up my mice.
They get full of fur.
```

#### ↳ Re: COBOL research - help!!!

- **From:** "hank" <ua-author-88501@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`

```

› 4 I am trying to understand whether there is any risk that some systems
› could
…[3 more quoted lines elided]…
› specific cases that you may have come across.

I've never heard of anyone using year 99 to signify end-of-file. Some
shops used 12/31/99 to signify "no expiration" for tapes or data but the
Y2K problem is primarily a data problem, not a language problem.
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "randallbart" <ua-author-464041@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p5@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p5@usenetarchives.gap>`

```

Hank wrote:
› 
›› 4 I am trying to understand whether there is any risk that some systems
…[8 more quoted lines elided]…
› Y2K problem is primarily a data problem, not a language problem.

At Valley Federal we had transaction files where the key was YYMMDD
followed by an account number. The writing program denoted end of file
by putting all 9s in the key. The reading program tested just YY=99.

I  |\   Randall Bart
L  |/   mailto:Bar··.@usa··m.net             Bar··.@att··m.net
o  |\   1-310-542-6013                       Please reply without spam
v  | \  
e    |\ Californians:  Vote June 2nd         Dennis PERON for Governor
Y    |/ John PINKERTON For Senator   Bill LOCKYER for Attorney General
o    |\ Panic in the Year Zero Zero:  http://members.aol.com/PanicYr00
u    |/ Is it easy yet?:http://members.aol.com/PanicYr00/Sequence.html
```

#### ↳ Re: COBOL research - help!!!

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-05-20T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p7@usenetarchives.gap>`
- **In-Reply-To:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`

```

In article <6k0qnq$e5l$1.··.@nnr··s.com>,
wrote:
› I'm doing some research on COBOL related Year 2000 issues, and need your help
› - please!
…[7 more quoted lines elided]…
› 1 I understand that COBOL is a language,


Stop right there, please... do enough research to find out what the
acronym COBOL expands to and then try again. While you're at it please be
so kind as to indicate the cause of your research... are you writing an
article? Doing a thesis? Tired of waking up in the middle of the night
with your mouth dry, your heart pounding and your brain throbbing from the
question 'Is my understanding right or wrong... is COBOL a language or
not?'

DD
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "css..." <ua-author-6589296@usenetarchives.gap>
- **Date:** 1998-05-25T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p7@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p7@usenetarchives.gap>`

```


DD is funny....rofl...

-Chris
doc··.@cl··k.net wrote:
: In article <6k0qnq$e5l$1.··.@nnr··s.com>,
: wrote:
: >I'm doing some research on COBOL related Year 2000 issues, and need your help
: >- please!
: >
: >I'm particularly interested in finding out whether and to what extent some
: >COBOL applications may fail in 1999 because of the use of 99 to signify 'end
: >file' or 'date not known'. I would welcome any advice (in simple English -
: >I'm only just IT literate enough to have registered for this group) on the
: >following:
: >
: >1 I understand that COBOL is a language,


: Stop right there, please... do enough research to find out what the
: acronym COBOL expands to and then try again. While you're at it please be
: so kind as to indicate the cause of your research... are you writing an
: article? Doing a thesis? Tired of waking up in the middle of the night
: with your mouth dry, your heart pounding and your brain throbbing from the
: question 'Is my understanding right or wrong... is COBOL a language or
: not?'

: DD
```

###### ↳ ↳ ↳ Re: COBOL research - help!!!

- **From:** "docd..." <ua-author-514273@usenetarchives.gap>
- **Date:** 1998-05-25T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p8@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p7@usenetarchives.gap> <gap-a6e85e12bd-p8@usenetarchives.gap>`

```

In article <6kekab$rig$1.··.@new··u.edu>,
Skinner wrote:
›
› DD is funny....rofl...

Pfoo... you are easily amused.

DD
```

#### ↳ Re: COBOL research - help!!!

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-05-21T20:00:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p10@usenetarchives.gap>`
- **In-Reply-To:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`

```


Dav··.@my-··s.com wrote in message
<6k0qnq$e5l$1.··.@nnr··s.com>...

› 3 As mentioned above, I gather that aside from the two-digit year notation
› another problem with COBOL in relation to Year 2000 compliance is the use
…[8 more quoted lines elided]…
› 


There was NEVER any version of COBOL that used "99" or "00" as a flag for
end-of-file, date-unknown, etc. This was always an application specific -
or OTHER software specific"trick". For example, on IBM mainframes, a date
of 12/31/99 for a tape file's expiration meant that it had no expiration
date. This wasn't defined by COBOL but by the tape handling system (which
was a totally separate product).

There are a variety of other dates, that people are worried about as well -
because SOME applications have coded them as "special dates", for example,
01/01/99
09/09/99

I should make it clear, however, that COBOL itself did have one pretty
significant "problem". The Standard version of the language did not (and in
fact still does not) have any way of getting the current-date with a 4-digit
year. The next COBOL Standard will have a solution to this problem - and
many existing applications already provide a solution (as an "extension" to
the language).

P.S. You may want to look at and/or post your question in the
comp.software.year-2000
newsgroup as well as the COBOL ng.
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-05-21T20:00:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p10@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap>`

```


Thane Hubbell wrote in message ...
› On Fri, 22 May 1998 19:32:20, "William M. Klein"
› wrote:
…[15 more quoted lines elided]…
› 
I am blushing in shame!
Of course the CURRENT-DATE intrinsic function provides this capability
(and using INTEGER-OF-DATE and DAY-of-INTEGER gives it in "Julian" format).
I stand (or rather type) fully corrected.
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "david johnson" <ua-author-2695697@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p10@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap>`

```

Unfortunately, most business systems are not much past COBOL 74.

Thane Hubbell wrote in message ...
› On Fri, 22 May 1998 19:32:20, "William M. Klein"
› wrote:
…[15 more quoted lines elided]…
›
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "e=mc^3..." <ua-author-6589663@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p13@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p10@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap>`

```

On Fri, 22 May 1998 12:32:20 -0700, "William M. Klein"
wrote:

› P.S. You may want to look at and/or post your question in the
› comp.software.year-2000
› newsgroup as well as the COBOL ng.

Dunno if this is such great advise anymore. After automatic
filtering eliminated some of the obvious trash, I retrieved but
THREE messages out of 100 available. And this was on the high
side of signal-to-noise ratio. I think that if it were not for
Cory's and Arnold's posts I would just blow off that group. Sigh!

Rick Anderson
Seattle
anderson aatt pobox fullstop com
```

###### ↳ ↳ ↳ Re: COBOL research - help!!!

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p14@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p13@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap> <gap-a6e85e12bd-p13@usenetarchives.gap>`

```

Richard Anderson wrote:
› 
› On Fri, 22 May 1998 12:32:20 -0700, "William M. Klein"
…[11 more quoted lines elided]…
› 

Sad, but true. I started following c.s.y2k last summer. It got taken
over by religious/political/gun nuts over the winter, so I simply
dropped it a few weeks ago. When the crap you have to endure outweighs
the benefits of belonging, split.

Bill Lynch

PS: Not intended to say that people shouldn't discuss religion,
politics, or firearms; USENET is a great place for that! Just that
c.s.y2k wasn't supposed to be that place.

› --
› Rick Anderson
› Seattle
› anderson aatt pobox fullstop com
```

###### ↳ ↳ ↳ Re: COBOL research - help!!!

_(reply depth: 4)_

- **From:** "material fellow" <ua-author-501273@usenetarchives.gap>
- **Date:** 1998-05-23T20:00:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p15@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p14@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap> <gap-a6e85e12bd-p13@usenetarchives.gap> <gap-a6e85e12bd-p14@usenetarchives.gap>`

```

Bill Lynch wrote:
› 
 
› 
› Sad, but true. I started following c.s.y2k last summer. It got taken
…[4 more quoted lines elided]…
› c.s.y2k wasn't supposed to be that place.

What about the theory that the year 2000 will be the second coming of
the messiah, and he will prove his holiness by solving the y2k problem
with but a wave of his hand.

This is the solution that business management has been waiting for.

I use stealth Java in my sig file.
It's there, but no one can detect it.
```

###### ↳ ↳ ↳ Re: COBOL research - help!!!

_(reply depth: 5)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-05-23T20:00:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p16@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p15@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap> <gap-a6e85e12bd-p13@usenetarchives.gap> <gap-a6e85e12bd-p14@usenetarchives.gap> <gap-a6e85e12bd-p15@usenetarchives.gap>`

```

Material Fellow wrote:
› 
› Bill Lynch wrote:
…[12 more quoted lines elided]…
› with but a wave of his hand.

This is it! The magic bullet we've all been waiting for! Now even I have
seen the light.

Bill Lynch :-)

PS: Still no reason, IMHO, to have to wade thru all those posts on
c.s.y2k.

› 
› This is the solution that business management has been waiting for.
…[3 more quoted lines elided]…
› It's there, but no one can detect it.
```

###### ↳ ↳ ↳ Re: COBOL research - help!!!

_(reply depth: 6)_

- **From:** "mickey" <ua-author-28912@usenetarchives.gap>
- **Date:** 1998-05-24T19:54:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p17@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p16@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap> <gap-a6e85e12bd-p13@usenetarchives.gap> <gap-a6e85e12bd-p14@usenetarchives.gap> <gap-a6e85e12bd-p15@usenetarchives.gap> <gap-a6e85e12bd-p16@usenetarchives.gap>`

```

Bill Lynch wrote:
› 
› Material Fellow wrote:
…[23 more quoted lines elided]…
› 
Oh, I don't know. Baiting Milne is just too much fun to resist. I will
admit, however, that lately he has stopped responding to my posts. Think
I singed his butt once too many times??

mickey
```

###### ↳ ↳ ↳ Re: COBOL research - help!!!

_(reply depth: 7)_

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1998-05-24T20:00:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p18@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p17@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap> <gap-a6e85e12bd-p13@usenetarchives.gap> <gap-a6e85e12bd-p14@usenetarchives.gap> <gap-a6e85e12bd-p15@usenetarchives.gap> <gap-a6e85e12bd-p16@usenetarchives.gap> <gap-a6e85e12bd-p17@usenetarchives.gap>`

```

Mickey wrote:
› 
› Bill Lynch wrote:
…[11 more quoted lines elided]…
› mickey

Can't say, I stopped reading his cant many moons ago (something about no
added value) and dropped the NG approx. 3 weeks ago now. Surely like
to think what you asked is true:-)

Bill Lynch
```

###### ↳ ↳ ↳ Re: COBOL research - help!!!

_(reply depth: 5)_

- **From:** "bob..." <ua-author-91503@usenetarchives.gap>
- **Date:** 1998-05-24T20:00:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p19@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p15@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap> <gap-a6e85e12bd-p13@usenetarchives.gap> <gap-a6e85e12bd-p14@usenetarchives.gap> <gap-a6e85e12bd-p15@usenetarchives.gap>`

```

On Sun, 24 May 1998 10:17:25 -0700, Material Fellow
wrote:

› Bill Lynch wrote:
›› 
…[11 more quoted lines elided]…
› with but a wave of his hand.
If the second comming does occur, problem will be fixed by
simply setting the date back year 0001 (A2 [after 2nd comming]) :)
bob hunt
›
› This is the solution that business management has been waiting for.
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "boo..." <ua-author-17074127@usenetarchives.gap>
- **Date:** 1998-05-22T20:00:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p20@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p10@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p10@usenetarchives.gap>`

```

"William M. Klein" wrote:

› 
› There was NEVER any version of COBOL that used "99" or "00" as a flag for
…[6 more quoted lines elided]…
›››››››››››› snip <<<<<<<<<<<<<<<<<<

You are correct ; I think the original writer was confused by three
situations which I know existed around 1975 :

1. During that period, it was a quite common technique to design
transaction files involving multiple record types to indicate end of
file by having a dummy record type '99' as the very last record of the
file. Because of that file design, a lot of cobol programs were
written to recognise the end of the transaction file by the dummy
record type 99. If it was a problem at all, it was a file design
problem , not a cobol problem.


2. Also in those days of heavy sequential, non-random update
processing involving an input master file and an input transaction
file, it was also an accepted programming techique to assign all 9s
(akin to high values) to the (transaction or master) record-id
once the end-of file is reached. This technique will ensure that both
files are fully processed, irrespective of which file ends first.
Again, this situation was due to program design rather than Cobol.

3). 00 representing date unknown ? I remember working in a University
where the academic sttaff did a lot a survey studies which were then
processsed using SPSS (Statistical package for the Social Sciences).
In these surveys, it was important to differentiate between no-respose
(blank) and an actual 0 code (representing something).. The SPSS
package had good facilities to differentiate between the two of them.
I suppose if one was to write a cobol program to validate(and clean)
the data, one had to differentiate between a blank and a zero . Again
this was a problem of questionaire design and not a cobol problem.

None of the above 3 situations are Y2k problems and they would not
cause any problems come Y2k, unless you have a scanning program that
goes through every source program and treats every occurrance ot '99'
as referring to the year ! Then there could be a problem.

And finally after going through the above, to come to think of it,
there is hardly any problem with cobol :-)


===================================================

Boon Lee
Melbourne PC User Group

E-mail : boo··.@mel··g.au

===================================================
```

#### ↳ Re: COBOL research - help!!!

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-05-21T20:00:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p21@usenetarchives.gap>`
- **In-Reply-To:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com>`

```

In article <6k0qnq$e5l$1.··.@nnr··s.com>, Dav··.@my-··s.com
writes:

› 1 I understand that COBOL is a language, and therefore may have been used as
› a platform for any number of applications, but I would really like to get a
…[3 more quoted lines elided]…
› payroll systems, etc);

Class registration.
Class lists.
Course offering. (Our printed schedule is fed from a download from the
mainframe.)
Recording payments for classes taken.
Financial aid disbursement system.
Grades & Transcripts.
Marching order for graduation ceremony.
Payroll system.
Personnel system.
Contracts (people hired to teach one or two classes).
Insurance benefits & premium payments.
Room scheduling system.
CWE (Carreer Work Experience) / job placement.
General ledger / accounts receivable / accounts payable.
Budgeting.

Those are just a few applicatons that come to mind off the top of my head.

› 2 I'd also like a better idea of the scale of the problem - to what extent
› are such systems still in use (almost all/50%/very few etc).  Again, I'd like
› a better picture of just how much chaos people can expect - has the media
› been overhyping even a little bit, or have people still really no idea how
› critical the problems are likely to be?

General Ledger and financial aid systems are okay (they are third-party
packages and we are currently installing Y2k-ready releases of them).

We are working on everything else.

› 3 As mentioned above, I gather that aside from the two-digit year notation
› another problem with COBOL in relation to Year 2000 compliance is the use of
…[5 more quoted lines elided]…
› dates correctly?

In the many messages I have read, I have yet to come across a single case where
someone was really using YEAR=99 to represent end-of-file. Even the '68 version
of COBOL has a READ ... AT END clause that is far more reliable than any
incidental data values. We have had programs that would use a 9's record
(MMDDYY=999999, obviously impossible to mistaken for a valid date) because at
one time VSAM wouldn't handle never-initialized files, and processing logic was
written to ignore all-9's records (e.g., DATE=999999 or CORSE-SECTION =
'999999999').

Actually, COBOL does not have a date type; instead, a character field, or a
numeric field, is used to hold some representation of a date. A construct like
MOVE CURRENT-DATE TO field will move 8 characters (mm/dd/yy) to the receiving
field (which must be defined as 8 characters, or a group name where the group
length is 8 bytes long).

It is up to the application programmer (or the project manager, or the
specifications writer) to define what value or convention would represent
missing values or other special considerations. We have used all spaces (for
character fields) to mean no date; we have used all zeroes; at one time we had
used 8/8/88 to represent no birth date provided, but a few years ago we
expanded the birth year to be 4 digits and went to spaces to mean no birth date
provided.

COBOL gets blamed because most business applications are written in COBOL.
(Hint: COBOL stands for COmmon Business Oriented Language.) We have the same
exposures in Gener/OL and Easytrieve-Plus. The problem is not the language as
such, but with how dates were implemented in the data structures.

At one time (back in the '60s) disk space was expensive so it was economically
unfeasable to punch "19" at the start of every year in every record. However,
in many cases one didn't even use disks for master files but cards, and cards
were the primary form of data entry, so there was a strong incentive to keep
each record only 80 bytes long because one more byte would mean using two
cards, which would double the costs of data storage (if the master file is on
cards) or would add tremendously to the data entry costs (since handling two
card types would take more effort than one card type because the keypunch
operator would have to switch between programs on the drum card for every card
punched).

When the price of disks went down and the capacity of disks went up, we already
had lots of programs that accessed those files, so it turned out to be cheaper
to use the same record structures (even if moved to sequential disk files, even
when moved to ISAM files, even when moved to VSAM files) than it was to
restructure the data and have to alter every program that access those files.
Sure, we expanded the records and added fields at the end, but other than a
recompile, the old programs would continue using the part of the record they
had always used and we had to modify only the programs that accessed the new
fields. It was management's reluctance to authorize us to restructure the data
(which would require us to redo all the programs that access those files) that
kept us from working on our Y2k project any sooner.

Remember: this is not just a COBOL program; if another programming language had
captured the business application market, we would be blaming that language.

More modern data respositories, such as SQL, do have an explicit DATE type, so
in that case we can use SQL's DATE type to hold a valid date, or an indicator
variable to indicate that we don't have a date.

› 4 I am trying to understand whether there is any risk that some systems could
› fail before 2000 (ie in 1999) because of the use of 99 to mean 'end file' or
› 'date not known', and would be particularly grateful for examples of any
› specific cases that you may have come across.

The event threshold of failure is somewhat application depenedent. We have
already had a failure last summer when one of the employees decided to request
retirement in the year 2000. The transaction was entered in our personnel
system with a future effective date. When trial payroll was next run, that
person's paycheck was rejected with the error, "That person has already
retired." (Yes, we know year 2000 is after year 1996, but the computer saw 00
as before 96.) Personnel backed out that transaction so that that employee
could be paid.

We anticipate problems with budgeting for fiscal year 00, problems with our
general ledger system for fiscal year 00. (Fiscal Year 2000 for us runs July 1,
1999 through June 30, 2000, so budgeting for year 2000 would start about July
1998 and serious budgeting data entry normally takes place September-October
1998.)

We roll over a subset of our course offering file to the next year so that a
lot of data entry could be skipped. We anticipate problems in July 1999 when
the course offering for academic year 99 (mid June 1998-mid June 1999) is
rolled over to academic year 00.

We also anticipate problems for deferred payment contracts (where a student
contracts to pay a third at registration time, a third half-way through the
term, and a third shortly before the end of the term).

We _know_ tha if we don't fix our systems, if a student registers during the
last few business days of 1999 but elects to send a check, that person _will_
be dropped from our registration files for non-payment because a payment due
date of January 3, 2000 (000103 in the data structure we have today) would be
less than, say, December 28, 1999 (991228), so the computer would compare
000103 to 991228 and decide that the payment due date had already passed.

These are problems that we anticipate happening before Saturday, January 1,
2000, and one had actually happened about three and a half years before January
1, 2000. Again, none of these problems are for 99 = end-of-file (I don't know
any COBOL programmer who ever claimed 99 was used for EOF), and none fo these
problems are from 00 being used to represent missing values, and none of these
are problems that would be specific to COBOL.

Mark A. Young
```

##### ↳ ↳ Re: COBOL research - help!!!

- **From:** "rtw..." <ua-author-6550399@usenetarchives.gap>
- **Date:** 1998-05-21T20:00:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a6e85e12bd-p22@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a6e85e12bd-p21@usenetarchives.gap>`
- **References:** `<6k0qnq$e5l$1@nnrp1.dejanews.com> <gap-a6e85e12bd-p21@usenetarchives.gap>`

```

mar··.@a··.com (Mark0Young) wrote:

› In article <6k0qnq$e5l$1.··.@nnr··s.com>, Dav··.@my-··s.com
› writes:
…[26 more quoted lines elided]…
› 

Mark:

Don't forget about the fact that those infra-red flushing devices in
airports as well as the faucets on the sinks are also controlled by
COBOL programs.

Beware! Don't shake hands with anyone in an airport on January 1,
2000!

;-)




Bob Wolfe, flexus, rtwolfe at spammers-are-meat-heads flexus dot com
To reply, look at my e-mail address, get rid of the spammer insult and fix the address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
