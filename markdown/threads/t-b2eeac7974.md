[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Who cares about the ANSI/ISO Standard?

_23 messages · 12 participants · 2003-04_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Who cares about the ANSI/ISO Standard?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-04-03T13:44:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E8CAB45.2477C152@attglobal.net>`

```
I couldn't help but put in my $0.02 after reading the entire thread
about Fujitsu COBOL, and the difficulty they have in telling users
whether a COBOL program conforms to the standard.

One reply from an employee of a vendor of hardware and COBOL that runs
on the hardware says that customers seem to be interested and expect
Unisys to participate in setting the standard and to conform to it.

One "user" pointed out that, having done many ports of COBOL
applications between different hardware platforms, the reason this
activity was usually so easy was -- the standard.

I submit that one reason several others said the standard is of no
concern to them was precisely because it _has_ existed for a long time
(at least, long in terms of the computer industry), and it _has_ been
followed by so many compiler creators.  If Unisys COBOL, IBM COBOL, MF
COBOL, Fujitsu COBOL, and many others didn't all treat a MOVE statement
exactly the same, as defined by the standard, it seems very likely to me
that there wouldn't BE so many COBOL compilers.  There wouldn't be more
COBOL programs in existence than any other language (or is it all others
combined?).  And there very likely WOULD be a Microsoft COBOL, and it
would be different from all the others!

We don't always have to think about, or even know, a standard for it to
be of value to us.

There is a standard named ISO 8601, titled "Data elements and
interchange formats - Information interchange - Representation of date
and times", which, if we'd all paid attention to it, might have saved
hundreds of billions of dollars in Y2K repair costs.  The "repairs" my
organization did for our customers still do not conform to that
standard.
```

#### ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-04T01:59:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8ce599.237423893@news.optonline.net>`
- **References:** `<3E8CAB45.2477C152@attglobal.net>`

```
Colin Campbell <cmcampb@attglobal.net> wrote:


>There is a standard named ISO 8601, titled "Data elements and
>interchange formats - Information interchange - Representation of date
…[3 more quoted lines elided]…
>standard.

Most Y2K fixes I've seen in production code are incredibly short-sighted.  They
are good for 10 years. As we approach 2010, we'll have another date crisis. 

Some go out 30 or 50 years. They should use a 'sliding window' which would work
indefinitely.
```

##### ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-04-04T15:23:30+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6itt7$r2s$3@aklobs.kc.net.nz>`
- **References:** `<3E8CAB45.2477C152@attglobal.net> <3e8ce599.237423893@news.optonline.net>`

```
Robert Wagner wrote:

> Most Y2K fixes I've seen in production code are incredibly short-sighted. 
> They are good for 10 years. As we approach 2010, we'll have another date
> crisis.

No. _YOU_ will have another date crisis.

_I_ will not have another date crisis.

Many others will not have another date crisis.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** SkippyPB <swiegand@neo.NOSPAM.rr.com>
- **Date:** 2003-04-04T14:11:09-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95E8F8BEDC9DB07F.0F2F259413A3EB13.75CC710BC6CE44E9@lp.airnews.net>`
- **References:** `<3E8CAB45.2477C152@attglobal.net> <3e8ce599.237423893@news.optonline.net> <b6itt7$r2s$3@aklobs.kc.net.nz>`

```
On Fri, 04 Apr 2003 15:23:30 +1200, Richard Plinston
<riplin@Azonic.co.nz> enlightened us:

>Robert Wagner wrote:
>
…[9 more quoted lines elided]…
>

I know I wont because I know how to add 1 to a packed date field and
get a valid date.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

Micro$oft Haiku Error Message #111

The Tao that is seen
Is not the true Tao - until
You bring fresh toner.
 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

##### ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-05T03:42:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030404224216.25704.00000086@mb-cl.aol.com>`
- **References:** `<3e8ce599.237423893@news.optonline.net>`

```
>From: robert@wagner.net  (Robert Wagner)
>Date: 4/3/03 8:59 PM Eastern Standard Time
>

>Some go out 30 or 50 years. They should use a 'sliding window' which would
>work
>indefinitely. 
>

If they are still running in 30 or 50 years the SHOULD go out.  Seem to
remember hearing/reading someplace the average system life is 10-15 years. 
These would have definately outlived their usefulness.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-04-05T04:03:45-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0304050403.b37c560@posting.google.com>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote in message news:<20030404224216.25704.00000086@mb-cl.aol.com>...
> >From: robert@wagner.net  (Robert Wagner)
> >Date: 4/3/03 8:59 PM Eastern Standard Time
…[9 more quoted lines elided]…
> These would have definately outlived their usefulness.

Hmm.... I know a system I work on is not average, and I know that
"modern" language systems are often rewritten rather than maintained,
thus reducing the average lifespan, but I work on some code currently
that with programs that have a creation date of 1974.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-05T13:38:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x%Aja.2055$kd1.2006541@newssrv26.news.prodigy.com>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com>`

```
"YukonMama" <yukonmama@aol.com> wrote in message
news:20030404224216.25704.00000086@mb-cl.aol.com...
> >From: robert@wagner.net  (Robert Wagner)
> >Date: 4/3/03 8:59 PM Eastern Standard Time
> >
> >Some go out 30 or 50 years. They should use a 'sliding window' which
would
> >work>>indefinitely.
> >
>
> If they are still running in 30 or 50 years the SHOULD go out.  Seem to
> remember hearing/reading someplace the average system life is 10-15 years.

Proper Design Life Span = (Anticipated retirement age) - (Current age of
designer)

MCM
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 4)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-06T07:24:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030406032440.14640.00000578@mb-fe.aol.com>`
- **References:** `<x%Aja.2055$kd1.2006541@newssrv26.news.prodigy.com>`

```
>From: "Michael Mattias" michael.mattias@gte.net 
>Date: 4/5/03 9:38 AM Eastern Daylight Time

>Proper Design Life Span = (Anticipated retirement age) - (Current age of
>designer)

So that's the calculation!  Thank you Mr Mattias :)

From: robert@wagner.net  (Robert Wagner)
Date: 4/5/03 3:02 PM Eastern Daylight Time

>I worked on a system, written in 1991, >which used a ONE digit year.

I did to at one time.  Payroll program. When the decade changed it went into a
loop taking deductions from paycheck for the next 100 years.  However it was
written in RPG (the original) not COBOL.

>Does that apply to languages too? If so, >COBOL should have been replaced in
the
>70's.

According to some it has been :).

From: "Michael Mattias" michael.mattias@gte.net 
Date: 4/5/03 7:45 PM Eastern Daylight Time

>Electronic health care claims were (and >still are) submitted in a format
>known as "National Standard Format."

>Until early 2001, two NSF versions (one >for professional claims, one for
>facility claims) were still in use - versions >using a six-character "patient
>date of birth." Hmm, does  '00' mean >1800, 1900 or 2000?

>(New NSF standards were released in, oh, >mid '98 or so using eight-character
>dates. Just that not a whole lot of people >found it very important to
update).

I haven't been in health care for about 9 years but at that time the subscriber
databases and claims databases used twos complement to store dates.  Got some
strange results if you forgot to use the formula to translate :)
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-06T16:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e904f45.125114584@news.optonline.net>`
- **References:** `<x%Aja.2055$kd1.2006541@newssrv26.news.prodigy.com> <20030406032440.14640.00000578@mb-fe.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote:

>I haven't been in health care for about 9 years but at that time the subscriber
>databases and claims databases used twos complement to store dates.  Got some
>strange results if you forgot to use the formula to translate :)

They did that so dates would sort in descending order. Indexed files don't have
a descending option, so fields in the key must be complemented to accomplish
that.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 6)_

- **From:** "Lorne Sunley" <lsunley@mb.sympatico.ca>
- **Date:** 2003-04-06T18:24:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JMPlV5b5VFnN-pn2-5RdQ9KZF9yTv@h24-82-204-17.wp.shawcable.net>`
- **References:** `<x%Aja.2055$kd1.2006541@newssrv26.news.prodigy.com> <20030406032440.14640.00000578@mb-fe.aol.com> <3e904f45.125114584@news.optonline.net>`

```
On Sun, 6 Apr 2003 16:30:11 UTC, robert@wagner.net (Robert Wagner) 
wrote:

> yukonmama@aol.com (YukonMama) wrote:
> 
…[7 more quoted lines elided]…
> 

Cute trick...

Some ISAM file handlers do allow descending sequence on keys.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 7)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-07T02:49:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e907a36.136108901@news.optonline.net>`
- **References:** `<x%Aja.2055$kd1.2006541@newssrv26.news.prodigy.com> <20030406032440.14640.00000578@mb-fe.aol.com> <3e904f45.125114584@news.optonline.net> <JMPlV5b5VFnN-pn2-5RdQ9KZF9yTv@h24-82-204-17.wp.shawcable.net>`

```
"Lorne Sunley" <lsunley@mb.sympatico.ca> wrote:

>On Sun, 6 Apr 2003 16:30:11 UTC, robert@wagner.net (Robert Wagner) 
>wrote:
…[3 more quoted lines elided]…
>> >I haven't been in health care for about 9 years but at that time the
subscriber
>> >databases and claims databases used twos complement to store dates.  Got
some
>> >strange results if you forgot to use the formula to translate :)
>> 
>> They did that so dates would sort in descending order. Indexed files don't
have
>> a descending option, so fields in the key must be complemented to accomplish
>> that.
…[4 more quoted lines elided]…
>Some ISAM file handlers do allow descending sequence on keys.

Rather than using binary complement, I always do it 'the COBOL way'. Compute
key-date = 99999999 - regular-date followed by compute regular-date = 99999999 -
key-date. The formula is the same in both directions.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 8)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-04-08T03:13:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030407231354.08851.00000499@mb-fw.aol.com>`
- **References:** `<3e907a36.136108901@news.optonline.net>`

```
>>> >databases and claims databases used twos complement to store dates


>>On Sun, 6 Apr 2003 16:30:11 UTC, robert@wagner.net (Robert Wagner) 
>>wrote:

>>> 
>>> They did that so dates would sort in descending order. Indexed files don't
>have a descending option, so fields in the key must be complemented to
accomplish
 that.
>

Actually I was told it was that way to save on disk storage, along with all the
packed fields and other strangeness.  Dates were never used in keys, and we
really had no reason to sort on them.

Another ASSumption on your part.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-09T03:45:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e938b0f.191828925@news.optonline.net>`
- **References:** `<3e907a36.136108901@news.optonline.net> <20030407231354.08851.00000499@mb-fw.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote:

>>>> >databases and claims databases used twos complement to store dates
>
…[12 more quoted lines elided]…
>packed fields and other strangeness. 

Fields are exactly the same size. Complementing doesn't save space. 

>Dates were never used in keys, and we
>really had no reason to sort on them.

Wouldn't you want medical procedures sorted chronologically? Say, on a bill.

I'm familiar with dates in the context of price files, where the key is
part-number, date. When cutting an invoice, you look for the last price on or
before the invoice date. 

>Another ASSumption on your part.

Oh my, the lady doesn't like me. 

I haven't responded to most CLC postings tonight because I was watching Cher's
"Final Tour" on tape. (I don't have cable or etheric TV). I'm enthralled by this
woman. She's fabulously talented, intelligent, hard working (>100 performances
in 2002), and has the don't-give-a-damn attitude I find so attractive in biker
babes. She'll be 57 on May 10 yet is still a live one. The FINAL final
performance will be June 11 at Madison Square Garden. I'll be there and
afterwards stay at the Helmsley Parc Place on 59th Street (across from the
hamsom cabs). Is anyone interested in a face-to-face meeting?
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-04-09T10:48:31+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e93ec79_1@127.0.0.1>`
- **References:** `<3e907a36.136108901@news.optonline.net> <20030407231354.08851.00000499@mb-fw.aol.com> <3e938b0f.191828925@news.optonline.net>`

```

"Robert Wagner" <robert@wagner.net> wrote in message
news:3e938b0f.191828925@news.optonline.net...
> yukonmama@aol.com (YukonMama) wrote:
>
>
> I haven't responded to most CLC postings tonight because I was watching
Cher's
> "Final Tour" on tape. (I don't have cable or etheric TV). I'm enthralled
by this
> woman. She's fabulously talented, intelligent, hard working (>100
performances
> in 2002), and has the don't-give-a-damn attitude I find so attractive in
biker
> babes. She'll be 57 on May 10 yet is still a live one. The FINAL final
> performance will be June 11 at Madison Square Garden. I'll be there and
> afterwards stay at the Helmsley Parc Place on 59th Street (across from the
> hamsom cabs). Is anyone interested in a face-to-face meeting?
>
Would that be with pistols or swords <G>?

You are very brave posting your movements like this... JerryMouse has
already explained how they deal with dissent in Texas <G>.

Enjoy Cher's performance, but remember, "If I could turn back time" is only
a song...<G>

Pete.

>




----== Posted via Newsfeed.Com - Unlimited-Uncensored-Secure Usenet News==----
http://www.newsfeed.com The #1 Newsgroup Service in the World! >100,000 Newsgroups
---= 19 East/West-Coast Specialized Servers - Total Privacy via Encryption =---
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 11)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-10T02:30:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e94a539.264074291@news.optonline.net>`
- **References:** `<3e907a36.136108901@news.optonline.net> <20030407231354.08851.00000499@mb-fw.aol.com> <3e938b0f.191828925@news.optonline.net> <3e93ec79_1@127.0.0.1>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

>"Robert Wagner" <robert@wagner.net> wrote in message
>news:3e938b0f.191828925@news.optonline.net...

>You are very brave posting your movements like this... JerryMouse has
>already explained how they deal with dissent in Texas <G>.

I lived in Texas for many years and still maintain a residence there. So I'm
familar with conflict resolution Texas-style. In East Texas they use fists; in
West Texas they use wit.
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-04-05T15:07:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<EiCja.68$vQ2.50@newssvr16.news.prodigy.com>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com>`

```
The Y2K problem was anticipated by some in the 70s and 80s, but at that
time, we were assured that since the average system life span was 10-15
years, "Don't worry about it; use a two-digit year."  Look what happened.
:)
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-04-05T10:41:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b6mtei$p53$1@panix5.panix.com>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com> <EiCja.68$vQ2.50@newssvr16.news.prodigy.com>`

```
In article <EiCja.68$vQ2.50@newssvr16.news.prodigy.com>,
Terry Heinze <terryheinze@prodigy.net> wrote:
>The Y2K problem was anticipated by some in the 70s and 80s, but at that
>time, we were assured that since the average system life span was 10-15
>years, "Don't worry about it; use a two-digit year."

'Anticipated'?  Mr Heinze, I would argue that 'anticipation' occurred 
earlier; it might not be too far-fetched to conclude that someone in a 
bank, somewhere, said 'Hey... how are we going to calculate thirty-year 
mortgages?' in late 1969.

>Look what happened.
>:)

There is nothing unusual in programmers making a living due to managerial 
shortsightedness last I looked.

DD
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T19:02:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f274a.49331919@news.optonline.net>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com> <EiCja.68$vQ2.50@newssvr16.news.prodigy.com>`

```
I worked on a system, written in 1991, which used a ONE digit year. Why? Because
programmers were told it was temporary and would be replaced within 2-3 years.
When we fixed it in 1998, it was still writing accounts payable checks.


"Terry Heinze" <terryheinze@prodigy.net> wrote:

>The Y2K problem was anticipated by some in the 70s and 80s, but at that
>time, we were assured that since the average system life span was 10-15
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 4)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T19:12:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f293c.49829208@news.optonline.net>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com> <EiCja.68$vQ2.50@newssvr16.news.prodigy.com>`

```
Systems with a long time horizon, such as pension plans and bonds, always used a
four digit year. I was shocked to learn that most hospital systems used two
digits. We know they had patients older than 80. How did they compute the
patient's age? Well it came out negative. Sometimes software added 100, other
times it printed a negative number and 'everyone knew' how to make the
adjustment. Amazing.


"Terry Heinze" <terryheinze@prodigy.net> wrote:

>The Y2K problem was anticipated by some in the 70s and 80s, but at that
>time, we were assured that since the average system life span was 10-15
…[23 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-05T23:45:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yUJja.2189$kd1.2112121@newssrv26.news.prodigy.com>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com> <EiCja.68$vQ2.50@newssvr16.news.prodigy.com> <3e8f293c.49829208@news.optonline.net>`

```
"Robert Wagner" <robert@wagner.net> wrote in message
news:3e8f293c.49829208@news.optonline.net...
> Systems with a long time horizon, such as pension plans and bonds, always
used a
> four digit year. I was shocked to learn that most hospital systems used
two
> digits. We know they had patients older than 80. How did they compute the
> patient's age? Well it came out negative. Sometimes software added 100,
other
> times it printed a negative number and 'everyone knew' how to make the
> adjustment. Amazing.

Electronic health care claims were (and still are) submitted in a format
known as "National Standard Format."

Until early 2001, two NSF versions (one for professional claims, one for
facility claims) were still in use - versions using a six-character "patient
date of birth." Hmm, does  '00' mean 1800, 1900 or 2000?

(New NSF standards were released in, oh, mid '98 or so using eight-character
dates. Just that not a whole lot of people found it very important to
update).

MCM
```

###### ↳ ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-04-05T18:46:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e8f15b9.44833707@news.optonline.net>`
- **References:** `<3e8ce599.237423893@news.optonline.net> <20030404224216.25704.00000086@mb-cl.aol.com>`

```
yukonmama@aol.com (YukonMama) wrote:

>>From: robert@wagner.net  (Robert Wagner)
>>Date: 4/3/03 8:59 PM Eastern Standard Time
…[9 more quoted lines elided]…
>These would have definately outlived their usefulness.

Does that apply to languages too? If so, COBOL should have been replaced in the
70's.
```

#### ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-04-05T11:19:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-8CECA5.11193205042003@corp.supernews.com>`
- **References:** `<3E8CAB45.2477C152@attglobal.net>`

```
In article <3E8CAB45.2477C152@attglobal.net>,
 Colin Campbell <cmcampb@attglobal.net> wrote:

>  There wouldn't be more
> COBOL programs in existence than any other language (or is it all others
> combined?).  And there very likely WOULD be a Microsoft COBOL, and it
> would be different from all the others!

Surely you misstated.  Of course Microsoft COBOL would fully comply with 
the standard, but none of the other vendors would.
```

##### ↳ ↳ Re: Who cares about the ANSI/ISO Standard?

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2003-04-06T15:34:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E90AB90.2EB464E5@attglobal.net>`
- **References:** `<3E8CAB45.2477C152@attglobal.net> <joe_zitzelberger-8CECA5.11193205042003@corp.supernews.com>`

```
Yes, you're probably right.  Microsoft would just say, "The ANSI / ISO
organizations only provide standards for the world.  Microsoft works at a more
comprehensive level."

Joe Zitzelberger wrote:

> In article <3E8CAB45.2477C152@attglobal.net>,
>  Colin Campbell <cmcampb@attglobal.net> wrote:
…[7 more quoted lines elided]…
> the standard, but none of the other vendors would.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
