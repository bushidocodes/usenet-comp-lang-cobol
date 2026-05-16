[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to find the greatest of two numbers without using the comparison operators?

_190 messages · 20 participants · 2007-08 → 2007-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to find the greatest of two numbers without using the comparison operators?

- **From:** Aparajita <aparajita.mohanty@gmail.com>
- **Date:** 2007-08-31T06:41:03
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com>`

```
Hi,

I want to find the greatest of two given numbers say 'A' and 'B.
The condition is that I should use the IF clause but not comparison
operators like '<', '>','=' etc.
Is there any other operator in COBOL by which we can compare two
numbers.

Thanks!
Aparajita
```

#### ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-31T09:12:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb8m1q$m3l$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com>`

```
In article <1188542463.524263.317700@i38g2000prf.googlegroups.com>,
Aparajita  <aparajita.mohanty@gmail.com> wrote:
>Hi,
>
>I want to find the greatest of two given numbers say 'A' and 'B.

Please do your own homework.

DD
```

#### ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-08-31T22:28:51+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jq8r6Fqh1sU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com>`

```


"Aparajita" <aparajita.mohanty@gmail.com> wrote in message 
news:1188542463.524263.317700@i38g2000prf.googlegroups.com...
> Hi,
>
> I want to find the greatest of two given numbers say 'A' and 'B.

That would be the "greater" of two numbers; the "greatest" implies at least 
three...

> The condition is that I should use the IF clause but not comparison
> operators like '<', '>','=' etc.
> Is there any other operator in COBOL by which we can compare two
> numbers.
>
No there isn't.

But what you want CAN be done.

a clue: Check out the COBOL SIGN test.

Then think about how a computer is able to make comparisons. How would a 
"compare" instruction (on any platform) "work"? If you had to build a 
computer, how would you build a "compare" instruction? Given that all you 
can do is arithmetic and sign checking, how would you implement a "compare"?

Post your thoughts here, and we'll see how you go.

Pete.
```

##### ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** Aparajita <aparajita.mohanty@gmail.com>
- **Date:** 2007-08-31T12:03:19
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188561799.566239.84930@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5jq8r6Fqh1sU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net>`

```
On Aug 31, 3:28 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Aparajita" <aparajita.moha...@gmail.com> wrote in message
>
…[29 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

Hi Pete,
Thanks for your response.
I got an alternate solution,
like this
IF A-B IS POSITIVE
DISPLAY "A IS GREATER"
ELSE
DISPLAY "B IS GREATER"
END-IF.

What is your opinion on the above solution? Or if you find any
limitations or constraints with this code, please let me know.

Thanks!
Aparajita
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-08-31T13:09:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iqUBi.22098$eY.5730@newssvr13.news.prodigy.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <1188561799.566239.84930@22g2000hsm.googlegroups.com>`

```


"Aparajita" <aparajita.mohanty@gmail.com> wrote in message 
news:1188561799.566239.84930@22g2000hsm.googlegroups.com...
>> > Hi,
>>
>> > I want to find the greatest of two given numbers say 'A' and 'B.
>>
or your response.
> I got an alternate solution,
> like this
…[7 more quoted lines elided]…
> limitations or constraints with this code, please let me know.

I use three (3) tests for code:

1. Works correctly?
2. Relatively efficient?
3. Maintainable?

If  'yes' to all, it's a keeper.


MCM
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2007-08-31T13:18:01-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9jgd3dnlun4h7i4a923ur5dhahaauip91@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <1188561799.566239.84930@22g2000hsm.googlegroups.com> <iqUBi.22098$eY.5730@newssvr13.news.prodigy.net>`

```
On Fri, 31 Aug 2007 13:09:34 GMT, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>
>
…[28 more quoted lines elided]…
>

You need a 4th in this case Michael. 

4.  Is this what the teacher wanted?

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I'm not afraid of dying.  I just don't want to
be there when it happens."
--Woody Allen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-01T01:16:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jqil1Frav9U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <1188561799.566239.84930@22g2000hsm.googlegroups.com>`

```

"Aparajita" <aparajita.mohanty@gmail.com> wrote in message 
news:1188561799.566239.84930@22g2000hsm.googlegroups.com...
> On Aug 31, 3:28 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[46 more quoted lines elided]…
> limitations or constraints with this code, please let me know.

Yes, you are on the right track.  But the code is flawed.

What happens if A = B?  Your code will incorrectly display that "B IS 
GREATER".

You should seek to understand the code yourself, then you won't need my 
opinion (or anyone else's...) as to constraints or limitations on it. Had 
you taken my advice and checked out the COBOL SIGN test you could have 
written a better solution. HINT: It's not too late... :-)

Read about the COBOL SIGN Test, then see if you can fix it yourself.

Picking up a solution from someone else is only one way to solve a problem, 
although it is sometimes a valid approach. Always analyse whatever you pick 
up, until you understand it thoroughly yourself. If you don't understand it, 
don't use it... :-)

Cheers,

Pete.
```

##### ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-31T16:34:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0qXBi.233753$Bo7.185140@fe07.news.easynews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net>`

```
Pete,
   Usually I am "amused" by DD's "do your own homework" and don't follow up on 
it.  However, when I first saw this question last night, it had ME stumped. 
Certainly, it HAD TO BE homework (because I can't think of any "good" reason to 
make this restriction in a business environment).  Also, when I was thinking 
about it,  I was NOT looking at the original question, so I didn't remember that 
the two fields were numeric.  Therefore, I could think of ways to do it with 
words (not symbols) and without an IF (using intrinsic function MAX), or with 
only = (not > or <); but I couldn't come up with a solution that actually met 
the requirement.  I am glad you gave the hint and others more on the solution.

P.S.  To OP who gave

  IF A-B ....

This may just be a typo (or my misreading a post),but Standard COBOL requires 
spaces around the subtraction sign.
  "A-B" is a single data item name, like   ADDRESS-OF-HOUSE
        while
  "A - B" is an arithmetic expression
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** docdwarf@panix.com ()
- **Date:** 2007-08-31T18:15:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb9lsm$jmr$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com>`

```
In article <0qXBi.233753$Bo7.185140@fe07.news.easynews.com>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>Pete,
>   Usually I am "amused" by DD's "do your own homework" and don't follow up on 
>it.  However, when I first saw this question last night, it had ME stumped. 

Ahhhhh... might this be similar to 'the wisdom of Lao Tsu, confounded by 
the question of a dolt'?

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-01T13:41:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188679318.084872.317460@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<fb9lsm$jmr$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <fb9lsm$jmr$1@reader1.panix.com>`

```

docdw...@panix.com () wrote:
> In article <0qXBi.233753$Bo7.185140@fe07.news.easynews.com>,
> William M. Klein <wmklein@nospam.netcom.com> wrote:
…[5 more quoted lines elided]…
> the question of a dolt'?

I didn't know that Lao Tsu was familiar with modern German vernacular.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-02T01:08:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbd2dj$pf3$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <fb9lsm$jmr$1@reader1.panix.com> <1188679318.084872.317460@d55g2000hsg.googlegroups.com>`

```
In article <1188679318.084872.317460@d55g2000hsg.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>
>docdw...@panix.com () wrote:
…[10 more quoted lines elided]…
>I didn't know that Lao Tsu was familiar with modern German vernacular.

I barely know what *I* am familiar with, let alone anyone else.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-31T12:33:28-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mngd3ld5kvv09qinjn7nrjefvnhgsaogm@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com>`

```
On Fri, 31 Aug 2007 16:34:04 GMT, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Therefore, I could think of ways to do it with 
>words (not symbols) and without an IF (using intrinsic function MAX), or with 
>only = (not > or <);

I once had a requirement to use words, because our print train was
missing one of the above symbols.   Fortunately that need is long
past.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-01T11:50:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jrnpsF10st0U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:0qXBi.233753$Bo7.185140@fe07.news.easynews.com...
> Pete,
>   Usually I am "amused" by DD's "do your own homework" and don't follow up 
…[8 more quoted lines elided]…
> the hint and others more on the solution.

Normally, I endorse the policy of not doing homework for people.

But sometimes, even if it IS homework, a helping hand, or a pointer in the 
right direction does not go amiss.

In this case, I remembered a 19 year old trying to get to grips with the 
assembler on a certain computer and to understand the whole architecture and 
how it worked, at a time when computers were not part of the scenery and 
embedded in the lives of all of us.
It had instructions like "CFM"  (Compare for magnitude...), "CFE"  (Compare 
for equality).

The clues came when I looked at the Multiply and Divide instructions 
(Macros) and realised they were repetitive addition and subtraction.

Then in a flash of cognition I realised that that was ALL this "wonderful" 
machine could do... arithmetic. Nothing more. Everything else was derived 
from that. (Later I found out more, and got to grips with the reality of 
binary and Boolean operations, which at the lowest level are all that is 
required. I once wrote a program (for a bet) which read cards and printed, 
using ONLY Logical instructions AND, OR, NOT, and XOR...it was a good 
learning experience.)

Nowadays, we've come a long way and both hardware, software, and bioware are 
"smarter" than in those far off misty days... but the excitement I got from 
figuring how it did it, has never been forgotten and I thought someone else 
might benefit from that too.

Sadly, as is often the case today, the OP simply picked up a solution from 
someone who was happy to provide it, without really bothering to think about 
it.

It seems to me that thinking is no longer "fashionable" and solutions via 
the line of least resistance are more the order of the day. I'm not 
suggesting we should make our lives more difficult, but thought can often 
lead to understanding, and understanding can often lead to wisdom. (Of 
course, if you have no place for wisdom in your life then there is no real 
requirement for thinking, either... For myself, I find the acquisition of 
wisdom by personal growth to be a very useful survival tool... I've never 
been conned in a pyramid scam, for example :-))

Around four thousand years ago, before the distractions and pressures of 
modern life, TV, movies, travel, entertainment... people used to think. 
(Human brains are quite well adapted for this...) They worked out the 
distance from the Earth to the Sun just by sticking sticks in the sand on a 
beach and observing the shadows. This calculation was correct to within 5%. 
No reason for it; they weren't planning on going there, just an 
"interesting" intellectual exercise.

Unfortunately, this knowledge and, much more importantly, the attitude that 
nurtured it, was lost in the Dark ages and the advent of Religion, which 
taught that the Universe behaved the way the Church said it did, and there 
was therefore no need for people to think about it. The wise teachings of a 
few enlightened people were submerged into commercializing the "Faith" and 
the resulting parodies of the original teaching set us back thousands of 
years in our development, and are still affecting our lives today. Even in 
this "enlightened" age, when we can perform technical miracles, there are 
still people prepared to kill themselves and others for the sake of their 
imaginary friend, who is more powerful that anyone else's imaginary friend.

As you may have guessed, it is a quiet Saturday here.No one has driven a car 
loaded with explosives into the local market, there are monarch butterflies 
re-enacting the Battle of Britain around the newly arrived pink blossoms on 
my nectarine tree, I can go to the shops with the certainty that my chances 
of being shot are less than those of my being hit by a meteor, and the fact 
that there is a Salvation Army church on the corner of my street does not 
offend my Atheist sensibilities one jot or tittle. (I admire the work they 
do.)

It IS possible for us to "get along".

But we need to think about it.

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-01T01:10:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbae5i$rnu$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net>`

```
In article <5jrnpsF10st0U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>Sadly, as is often the case today, the OP simply picked up a solution from 
>someone who was happy to provide it, without really bothering to think about 
…[3 more quoted lines elided]…
>the line of least resistance are more the order of the day.

Ahhhhhh, for the Oldene Dayse, when a thinker could think things such as 
*ten* thinkers cannot, today!

In my experience, Mr Dashwood - and it has already been acknowledged that 
our experiences are, at times, rather different - then, as now, there were 
folks who would take the 'easy way' and others who agreed with Socrates 
that 'xalapa ta kala' (difficult/harsh/not easy (are) the 
good/beautiful/noble (things)'.

[snip]

>Around four thousand years ago, before the distractions and pressures of 
>modern life, TV, movies, travel, entertainment... people used to think. 

They also used to die a bit earlier.

>(Human brains are quite well adapted for this...) They worked out the 
>distance from the Earth to the Sun just by sticking sticks in the sand on a 
>beach and observing the shadows. This calculation was correct to within 5%. 

Eh?  I believe you are referring to Eratosthenes calculation of the 
earth's circumference... and that was closer to 2,500 years ago, not four 
millennia.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-01T16:20:09+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5js7jrF12ab2U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fbae5i$rnu$1@reader1.panix.com...
> In article <5jrnpsF10st0U1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[35 more quoted lines elided]…
> millennia.

Nope. I was not referring to Eratosthenes at all. Had I been, I would have 
said so.

Not that it matters, but I was referring to the same people who, 5000 years 
ago gave us the current 365 day calendar (based on their astronomical 
observations), built instruments to measure time and angles around 4500 
years ago, documented over 40 constellations which could be used for 
navigation 3300 years ago, had many of their accomplishments claimed by 
Greeks, (who they influenced immensely...Aristole acknowledged their 
superior Astronomical achievements and Pythagoras was tutored by them), and 
passed down across thousands of years, through their closed Priesthood, 
knowledge that was lost, destroyed (Clement of Alexandria documented at 
least four of their books on Astronomy that were in the famous library), and 
then re-discovered centuries later.

No more clues... do your own homework. :-)

Pete.
```

###### ↳ ↳ ↳ [OT] Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 6)_

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2007-09-01T11:39:17+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbbc0b$o1a$02$1@news.t-online.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net>`

```
May I repeat what I previously stated -
If you have something to say that is not
anything to do with the original topic, then
please OT it.
Bill has already said this.
This is no longer funny.
Especially for people that are trying this
list for an answer to their problems/questions.

Roger
```

###### ↳ ↳ ↳ Re: [OT] Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-09-01T12:54:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%hdCi.4606$JD.1291@newssvr21.news.prodigy.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message 
news:fbbc0b$o1a$02$1@news.t-online.com...
> May I repeat what I previously stated -
> If you have something to say that is not
…[5 more quoted lines elided]…
> list for an answer to their problems/questions.

If this specific thread/ this specific question is a source for answers, the 
"off-topic" comments are far more important than the answer.

MCM
```

###### ↳ ↳ ↳ Re: [OT] Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-02T01:21:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jt7amF1564tU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <%hdCi.4606$JD.1291@newssvr21.news.prodigy.net>`

```
"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:%hdCi.4606$JD.1291@newssvr21.news.prodigy.net...
> "Roger While" <simrw@sim-basis.de> wrote in message 
> news:fbbc0b$o1a$02$1@news.t-online.com...
…[11 more quoted lines elided]…
>
I agree :-) (but then, I would say that... :-))

Thanks for pointing it out, Michael.

 Pete.
```

###### ↳ ↳ ↳ Re: [OT] Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-02T01:01:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jt65rF13v7mU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com>`

```


"Roger While" <simrw@sim-basis.de> wrote in message 
news:fbbc0b$o1a$02$1@news.t-online.com...
> May I repeat what I previously stated -
> If you have something to say that is not
> anything to do with the original topic, then
> please OT it.

Most of the time I do. Not always...

> Bill has already said this.

It has been said here on a number of occasions by a number of people. Most 
of us do try and adhere to it, but we don't always succeed. You getting 
strident about it is unlikely to make a difference, and may very well 
alienate the people you are hoping to persuade.

> This is no longer funny.

Well, Gee, I'm sorry you're losing your sense of humour

As it is an umoderated forum there is nothing you can do about it.

I suggest you accept it for what it is; an unmoderated Usenet forum and not 
your personal Helpline.

If you post here, there is a risk that your questions will be taken off 
topic, ignored completely, or answered brilliantly. It is worth what you pay 
for it.

> Especially for people that are trying this
> list for an answer to their problems/questions.
>

Many people access this list for a myriad of reasons. Why is your reason 
more important than anybody else's?

As for getting help on questions, I have answered a number of them here 
recently. They ranged from sending faxes with COBOL ,to suggesting how 
comparisons might be made without using comparison operators (which IS the 
topic of this thread).

Actually Roger, I DO prefix topics that are OT with an OT prefix, if I 
originate the topic. In this case I didn't orginate the topic and it is 
debatable how far off it I wandered. As there are no thought police here to 
enforce on-topic postings, and as most of us do adhere to a code of conduct 
that is NOT enforced, I suggest you are way out of order with this post.

I'm not sure what I would do if I were you. But I wouldn't be getting 
unwrapped about it.

Calm down and accept CLC for what it is. No one is setting out to 
deliberately irritate you.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-01T14:13:45-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com>`
- **In-Reply-To:** `<5jt65rF13v7mU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net>`

```

Pete Dashwood wrote:
> "Roger While" <simrw@sim-basis.de> wrote in message
> news:fbbc0b$o1a$02$1@news.t-online.com...
…[22 more quoted lines elided]…
>

Sorry Pete but you are being a trifle rude in your response. The
poster (Roger) is right to point out that our deviations from the
straight and narrow are not pertinent to the larger view on life that
is Cobol. Perhaps we should live up to the world-wide view of being
boring IT people somewhat marginally less interesting than accountants
and only post relevant ON-TOPIC items here?

Perhaps, if I had any intent in following that suggestion, I would
have added an [OT] to the subject line...
```

###### ↳ ↳ ↳ [OT] Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-02T13:58:01+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jujlaF1b66jU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1188681225.360094.78060@o80g2000hse.googlegroups.com...
>
> Pete Dashwood wrote:
…[28 more quoted lines elided]…
> Sorry Pete but you are being a trifle rude in your response.

Only a trifle?... bugger! I must try harder... :-)

>The
> poster (Roger) is right to point out that our deviations from the
> straight and narrow are not pertinent to the larger view on life that
> is Cobol.

Bollocks! First off, COBOL Is not a "larger view on life" It is a computer 
programming language entering its Goetterdammerung.

Second off, while I am all in favour of on-topic posting, I'm not going to 
be taken to task publicly for not adhering to it in a forum that cannot 
enforce it anyway. Get over it.

>Perhaps we should live up to the world-wide view of being
> boring IT people somewhat marginally less interesting than accountants
> and only post relevant ON-TOPIC items here?

Speak for yourself (it's a free unmoderated forum... great, ain't it? :-)) 
I have NEVER been part of, or fitted the description you posit, and I NEVER 
will be! While I am very happy to make every effort to prefix off-topic 
posts with OT, (And actually do this anyway, if it is me instigating the 
topic) I can't promise or guarantee to always succeed.

Don't like it?

Tough. There's a lot of things posted here I don't like either, but you 
don't see me whining about it. It is not my personal forum required to 
conform to my personal expectations and requirements, any more than it is 
yours or anybody else's.

THAT is what makes it valuable, not the fact that there is a shared interest 
in COBOL amongst the people here, although that is also pretty important.

OK, here's the deal...

1. I'll take more care about prefixing topics that are OT with "OT", even 
though you can't make me :-), but just out of consideration for the 
community here, and because of the nice guy I really am... :-)

2. I'll say I'm sorry to you and Roger for rudeness (and I don't  say I'm 
sorry, when I'm not...)

IF....and only IF....

1. Both of you acknowledge the value of free speech  and agree that this 
forum should remain unmoderated.

2. You accept it for what it is; an unmoderated Usenet forum, not your 
personal Helpline, and accept that sometimes you won't get what you want.

Otherwise, I have nothing further to add on this topic.

>
> Perhaps, if I had any intent in following that suggestion, I would
> have added an [OT] to the subject line...
>
Rearrange these words to make a well known aphorism: :-)

kettle pot the the black calling

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 10)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-02T04:08:13-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188731293.799332.22640@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<5jujlaF1b66jU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net>`

```
On 2 Sep, 02:58, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
> > Pete Dashwood wrote:
…[17 more quoted lines elided]…
> programming language entering its Goetterdammerung.

If you don't believe in God or Gods how can you use a phrase which
translates as the Twilight of the Gods?

>
>
…[7 more quoted lines elided]…
> sorry, when I'm not...)

I require no apology. You haven't (yet) managed to offend me.

>
> IF....and only IF....
>
> 1. Both of you acknowledge the value of free speech  and agree that this
> forum should remain unmoderated.

I think that the nutter who posts anti-MI5 messages is a good
justification for moderation of this group.

>
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-03T01:33:58+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jvsdjF1fhpjU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1188731293.799332.22640@k79g2000hse.googlegroups.com...
> On 2 Sep, 02:58, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[24 more quoted lines elided]…
> translates as the Twilight of the Gods?

I don't believe in the Tooth Fairy but I can talk about teeth and fairies, 
or even fairies' teeth...

If you have ever seen a Wagner festival where they do (usually over several 
days) Goetterdammerung, you would realise why I used the term. It is a 
tragic epic with heroes and villains,  a deepening Darkness, and the Good 
and the Mighty laid low....just like the death of COBOL...

(I once got dragged along (much against my will) to the famous Wagner 
Festival at Bayreuth in Germany... 5 days of Wagner... not my cup of tea  (I 
thought...) but she was a pretty little thing and very persuasive. :-) I 
actually enjoyed it immensely.
>
>>
…[22 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 12)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-02T12:39:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188761957.395685.232300@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5jvsdjF1fhpjU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvsdjF1fhpjU1@mid.individual.net>`

```

Pete Dashwood wrote:
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1188731293.799332.22640@k79g2000hse.googlegroups.com...
…[39 more quoted lines elided]…
> actually enjoyed it immensely.

I did watch through the entire Ring Cycle. 9 hours of ....zzzzz. Only
two good songs and a long-drawn-out story line....zzzz.

> >
> >>
…[22 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-03T01:52:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jvtfrF1gru2U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com>`

```

```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 12)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-02T14:37:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dm46tre8050cc@news.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net>`

```
Pete Dashwood wrote:
>>
>
…[24 more quoted lines elided]…
>

Heh! Take that attitude to the news.admin.net-abuse.email group!

There are admins who have to deal with 200+ spams, per day, at each of 
50,000 email addresses (such as a major university).

Let JUST ONE get through - or, conversely, dump JUST ONE legit message - and 
they catch unmitigated hell.

These administrators have developed empirical rules which might conflict 
with your free-for-all attitude, the most important of which is:

                       "My server, my rules."

My personal favorite metaphor to those who insist they are righteous, but 
nevertheless use the services of a sewer-dwelling ISP, goes like this:
---
1. Your emails are like sperm, ready to dash out and do their thing.
2. Your ISP is a prick.
3. [blocklist] is a condom.
4. You are asking for one teeny hole in the rubber.
5. We are innocent maidens who do not like surprises.

You'll have to get us drunk first!
---
Some of the entities who have appeared (as collateral damage) on ISP-centric 
blocklists include: The American Bar Association, The New York Philharmonic, 
Sloane-Kettering Cancer Center, and several smaller municipal governments.

No, I'll have to disagree with the unfettered speech doctrine where spammers 
are concerned.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 13)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-02T18:26:20-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dme45mnmt6372@corp.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com>`

```

"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:13dm46tre8050cc@news.supernews.com...

<snip>

> 1. Your emails are like sperm, ready to dash out and do their thing.
> 2. Your ISP is a prick.
…[3 more quoted lines elided]…
>

This sounds like a backhanded way of implying that one of Pete's tools 
leaks!
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 14)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-03T12:22:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k12elF1loonU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <13dme45mnmt6372@corp.supernews.com>`

```


"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:13dme45mnmt6372@corp.supernews.com...
>
> "HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
…[12 more quoted lines elided]…
> leaks!
Cheeky monkey!

I can reassure a caring world that there are no signs of decreasing function 
in ANY of my tools.

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 15)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-04T12:14:44-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188933284.356595.302360@19g2000hsx.googlegroups.com>`
- **In-Reply-To:** `<5k12elF1loonU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <13dme45mnmt6372@corp.supernews.com> <5k12elF1loonU1@mid.individual.net>`

```
On 3 Sep, 01:22, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Charles Hottel" <chot...@earthlink.net> wrote in message
>
…[10 more quoted lines elided]…
>

He might take that as an insult. Homo sapiens is an ape and not a
monkey (unless you subscribe to the discredited creationist view).
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 16)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-04T20:09:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13drstnqo2oaqb8@corp.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <13dme45mnmt6372@corp.supernews.com> <5k12elF1loonU1@mid.individual.net> <1188933284.356595.302360@19g2000hsx.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1188933284.356595.302360@19g2000hsx.googlegroups.com...
> On 3 Sep, 01:22, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[16 more quoted lines elided]…
>

No I did not take insult.  If I had I would have asked him to explain all 
those illegitimate children on continents all over the world.  My 
inderstanding is that without some "leakage" they would not exist ;-)
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 17)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-04T20:12:41-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13drt3c22e73rad@corp.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <13dme45mnmt6372@corp.supernews.com> <5k12elF1loonU1@mid.individual.net> <1188933284.356595.302360@19g2000hsx.googlegroups.com> <13drstnqo2oaqb8@corp.supernews.com>`

```

"Charles Hottel" <chottel@earthlink.net> wrote in message 
news:13drstnqo2oaqb8@corp.supernews.com...
>
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
…[24 more quoted lines elided]…
>

Sorry I meant to put OT but  I can never remember if it means "On Topic" or 
"Off Topic".
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-03T12:19:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k129aF1m29sU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com>`

```


"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:13dm46tre8050cc@news.supernews.com...
> Pete Dashwood wrote:
>>>
…[57 more quoted lines elided]…
> spammers are concerned.

You make a good point, Jerry.

I am persuaded by the "My Server, my rules" approach.

Anyone runnng a server has the right to control what goes over it.

However, IF you decide to allow your server to be used for PUBLIC 
UNMODERATED Newsgroups, then it is wrong to censor posts to those groups. (I 
am hopeful that the kind of public spirited person who would do this, would 
be righteous and not want to censor posts anyway, but that is optimism more 
than reality and certainly can't be guaranteed.)

The sub-moronic cretins who flood the netwrk with Spam are actually 
undermining the right of all of us to a voice.

I guess the only way we can ever guarantee the right to free speech is to 
control the media, and, for the most part, we don't.

I remember many years ago (long before the Internet, or even PCs) a certain 
young Auckland poet was unfairly dismissed  (partly for organizing the 
workers) from his job in the country's only sugar refinery at Chelsea in 
Auckland. He wrote a poem dishing the dirt on the practices in the refinery, 
but of course, no established newspaper or magazne would touch it.  I was 
walking down Queen Street (Auckland's main thoroughfare) in my lunch break 
and had an A4 page thrust into my hand by an unkempt man who was shouting 
about the injustice of business management. (I had much sympathy for this, 
being in my early twenties and suffering at the hands of a bastard PHB...)

I wish I had kept that piece of paper; (today it would be worth a 
considerable amount of money), but apart from that, to have been handed it 
by James K. Baxter himself is an experience that I can certainly dine out 
on.

The distribution of this Broadstreet Ballad by a lone person taking on the 
establishment created a furore in Auckland (Baxter was still relatively 
unknown outside fo literary circles, but his action was very 
uncharacteristic of the  Auckland populace and that alone raised interest.). 
TV got hold of it, there was an investigation; it was the beginning of the 
end, and Chelsea sugar refinery is now a derelict building on Auckland's 
North Shore. (It might even have been demolished now; it's a while since I 
was in that area.)

The point is that the only way Baxter could make his point was to control 
the medium of distribution for his message.

It's pretty desperate when you have to actually hand your words to 
individuals...

(The poem ("Ballad of the Stonegut Sugar Works") is a classic and I have 
parts of it still in my memory. I just did a GOOGLE search and was delighted 
to find it is now included in collections of his poems, but, sadly, it isn't 
published on the Internet: 
http://www.bookcouncil.org.nz/writers/baxterjk.html

Here's a taste, from memory...

"Oh, in the Stonegut Sugar Works
  The floors are black with grime
  I think they must have built it
  In Queen Victoria's time."
...
"And all the sugar in the land
 Flows through that dismal dump
 And all the drains run through the works
 Into a filthy sump.
 And then they boil it up again
 For the money in each lump."

Powerful stuff... :-)

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 14)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-03T09:08:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13do591egchnj22@news.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net>`

```
Pete Dashwood wrote:
>>
>> No, I'll have to disagree with the unfettered speech doctrine where
…[13 more quoted lines elided]…
> guaranteed.)

Skipping over the notion that censoring implies moderated, again practice is 
at variance with purity. Virtually all blogs that allow comments have to 
police the posters. There are too many who want to rant about global warming 
on a blog devoted to orchids (when everyone knows global warming is caused 
by the AIDS Quilt).

So, I think you'd agree, that off-topic posts simply clutter the 
conversation (much like this missive).

Secondly, a group or blog in favor of, say, the wonders of turnip stew, can 
harm its own cause by allowing advocates with an anti-social bent ("turnips 
improve your goat-fucking staying power...") to pervert the cause. This does 
not apply to American left-wing, progressive, posts. There, of course, the 
most virulent voices get the most play.

"The best way to counter hate is more conversation, not less," is a good 
rule. But it is best exercised when those with a differing opinion set up 
their own site, not pollute my favorite sites with a contrary position.

Sometimes censorship isn't necessary; tx.guns is a remarkably polite 
conversation board. We have contributors from everywhere and it's not too 
difficult for a member to visit a crank (no matter where he lives) and shoot 
his dog. But we don't censor posts.






>
> The sub-moronic cretins who flood the netwrk with Spam are actually
…[58 more quoted lines elided]…
> Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-04T10:46:15+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k3h5nF1ub9aU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com>`

```


> Pete Dashwood wrote:
>>>
…[20 more quoted lines elided]…
> is caused by the AIDS Quilt).

It is the right of the Blog owner to monitor posts. If people want to rant 
about stuff, that is a decision that the blog owner must take. I don't run a 
blog (mainly because I simply don't have time), but if I did I would not 
remove rants. If they became repetitious, I'd mail the poster. The point is 
that it is up to each individual server/blog runner to decide what they 
want.

My contention is that IF you open your server to an unmoderated, public 
newsgroup, then you should be prepared to run it as such.
>
> So, I think you'd agree, that off-topic posts simply clutter the 
> conversation (much like this missive).

(I don't think your post is clutter; it raises some important points.)

I'd like to agree, but I can't :-) If the off topic posts are adding more to 
the general value of the forum than the on topic ones, then where's the 
problem?

Yes, off-topic posts can be viewed as "clutter", but sometimes the clutter 
is more valuable than the posts to the subject under discussion.

The word "value" here varies for each individual. Different people post to 
Newsgroups for different reasons; it isn't always to get information on a 
particular topic. It can be for a myriad reasons, all of which are 
"valuable" to the person posting.

I come here for entertainment and a break from work, to see if  I can help 
someone who has requested help, to blow off steam, to be amused by some of 
the wit that is posted here, to try and pass on experience and to encourage 
COBOL people to expand their horizons. (Mostly for fun, in other words). Are 
any of those reasons less valuable that a debate about SECTIONs vs 
PARAGRAPHs, or whether subscripts are faster than indexes on a Bendix 
washing machine with release 7.03a of the Flummox OS running in 2.6KB 
without the OO compiler extensions?

Now, if you happen to be programming Bendix washing machines you probably 
are much more interested in posts pertaining to that, and you may well be 
trying to get questions answered. Fair enough, but the point everyone has to 
bear in mind is that, in an UNMODERATED PUBLIC forum you do NOT have a God 
given right to expect an answer. It ISN'T a free Help Line and people 
answering questions and helping posters (and that includes me, even though I 
come here mainly for fun), do so from the goodness of their hearts and not 
because they are obliged to.

I WOULD agree that if someone is determined to have a forum that stays 
religiously on topic and that is all they want to talk about, then don't 
make it an unmoderated public forum.

Maybe alt.cobol.lang could be moderated by volunteers from here. It is a 
very underused newsgroup.

Step forward all those prepared to act as moderators? No takers?

OK, then don't whinge about OT posts in a public forum.
>
> Secondly, a group or blog in favor of, say, the wonders of turnip stew, 
…[3 more quoted lines elided]…
> There, of course, the most virulent voices get the most play.

They may also improve the number of visits to the blog overall and almost 
certainly the entertainment value. Again, it comes down to whether it is 
moderated or not.
>
> "The best way to counter hate is more conversation, not less," is a good 
> rule. But it is best exercised when those with a differing opinion set up 
> their own site, not pollute my favorite sites with a contrary position.

So you favour sites where everyone is in agreement? That's fair enough, but 
it is just one viewpoint. If it is the viewpoint of the person running the 
blog or server, then they can enforce it and nobody can reasonably take 
issue with them doing so.

For myself, I see dissent as pretty indispensable for examining an issue 
comprehensively. How can I ever change my mind if I am unaware of what other 
positions are available, or if I have dismissed those positions without 
proper investigation?

I think a blog that has arguments going on has to be more valuable than one 
where everyone just congratulates themselves for thinking "right".

>
> Sometimes censorship isn't necessary; tx.guns is a remarkably polite 
…[3 more quoted lines elided]…
>
Lol!
Good for you. Mind you, you would have a right to if it isn't an unmoderated 
public group.

The bottom line here is that there is a big difference between an 
unmoderated public Usenet forum and a blog, or moderated forum where rules 
of conduct can be enforced.

I believe that unmoderated forums (like CLC) are far more valuable than most 
people realise. It is precisely because we take our freedoms for granted 
that we stand in danger of losing them.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 16)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-04T07:31:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dqk06oocd5704@news.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net>`

```
Pete Dashwood wrote:
>
> So you favour sites where everyone is in agreement? That's fair
…[7 more quoted lines elided]…
> positions without proper investigation?

I was once privleged to meet a chap who introduced me to "quality control 
thinking." His mantra was "I am not interested in what you 'believe,' I am 
only interested in what you can prove!" So, to answer your question, sure, 
I'm interested in what others can prove. I am not interested in personal 
animus as evidence sufficient for some preposterous notion.

Positions that rely on the Illuminati, UFOs, Halliburton, or Flouride - 
often coupled with "what else could it be?" - and amplified by hate are, to 
me, unacceptable. Fuckers should have their intestines turned into 
extestines.

As to your final question, "how can I ever change my mind," I can save you 
some time. Any argument that starts with "I believe..." can be dismissed out 
of hand. Any position that states a conclusion without evidence that would 
compel a rational mind to the probable truth of the position, can be 
dismissed out of hand. Any statement by a Hollywood actor or mainstream news 
anchor can be dismissed out of hand. Any political statement that appeals to 
"feelings" can be dismissed out of hand.

>
> I think a blog that has arguments going on has to be more valuable
> than one where everyone just congratulates themselves for thinking
> "right".

Arguments, reason, evidence, sure. But the cacophony of the insane asylum? 
Bah!

>
> I believe that unmoderated forums (like CLC) are far more valuable
> than most people realise. It is precisely because we take our
> freedoms for granted that we stand in danger of losing them.

As an administrator, I visit news.admin.net-abuse.email. It got so bad on 
that group - what with spammers trying to disrupt the exchange of 
information, malcontents, and the deranged,* that a new newsgroup was 
started: news.net-abuse.blocklisting. The latter is moderated.

------
* One form the abuse took was the so-called "dippy flood," up to 30,000 
messages in one day containing nonsensical text. Another was a kook who 
complained to ordinary poster's ISPs - repeatedly.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 17)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-04T12:50:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbjka2$bhv$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net> <13dqk06oocd5704@news.supernews.com>`

```
In article <13dqk06oocd5704@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>Pete Dashwood wrote:
>>
…[13 more quoted lines elided]…
>I'm interested in what others can prove.

It might be interesting, then, to examine what one considers to be the 
criteria for doing so... what constitutes 'proving'?

[snip]

>Any argument that starts with "I believe..." can be dismissed out 
>of hand.

This might cause one dismiss, out of hand, arguments that continue with 
'... that (criterion) generates (condition) based on (logical argument)"; 
to be so sensitive to matters of form could cause one to continue in a 
state of ignorance.

Perhaps it might be wiser to pay more attention to complete sentences than 
fragments.

>Any position that states a conclusion without evidence that would 
>compel a rational mind to the probable truth of the position, can be 
>dismissed out of hand.

A conclusion from this might be that statements like 'You might enjoy 
(foodstuff)' are to be dismissed, out of hand, as there is nothing there 
which is evidence, compelling, rationality, probability or truth... just 
possibility and taste.

Moderation in all things, remember... including moderation.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 17)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-04T09:05:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rtsqd31h1gi38a1r4g0ivrvm4nakhlfumh@4ax.com>`
- **References:** `<5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net> <13dqk06oocd5704@news.supernews.com>`

```
On Tue, 4 Sep 2007 07:31:52 -0500, "HeyBub" <heybubNOSPAM@gmail.com>
wrote:

>As to your final question, "how can I ever change my mind," I can save you 
>some time. Any argument that starts with "I believe..." can be dismissed out 
>of hand. 

I believe that is simplistic.

>Any position that states a conclusion without evidence that would 
>compel a rational mind to the probable truth of the position, can be 
>dismissed out of hand. Any statement by a Hollywood actor or mainstream news 
>anchor can be dismissed out of hand. Any political statement that appeals to 
>"feelings" can be dismissed out of hand.

Beliefs and feelings are real.   Ignoring them is ignoring reality
which is a dangerous thing to do.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 18)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-04T11:16:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dr14otpjtse69@news.supernews.com>`
- **References:** `<5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net> <13dqk06oocd5704@news.supernews.com> <rtsqd31h1gi38a1r4g0ivrvm4nakhlfumh@4ax.com>`

```
Howard Brazee wrote:
> On Tue, 4 Sep 2007 07:31:52 -0500, "HeyBub" <heybubNOSPAM@gmail.com>
> wrote:
…[14 more quoted lines elided]…
> which is a dangerous thing to do.

The reality of the belief or the belief in reality?

So what do you do regarding the man raving on the street corner "The End is 
Near!" To him, swarms of toads are galavanting through his grey matter. Do 
you base the rest of your life - or even the next thirty seconds - on his 
"real" belief?

Feelings and beliefs may be "real" to the person holding them. To the rest 
of us they are (or should be) accorded fantastic status. For example, 
Clinton's "I feel your pain," could be anything from paranormal empathy to a 
political calculation. How can one tell? "I believe in UFOs" is compelling 
only if you can put a piece of a UFO in my hand.

I don't want to get bogged down in semantics or sentence structure. The 
phrase, "I believe, based on a mountain of peer-reviewed evidence..." is 
magnitudes different from "I believe, with a perfect faith..."
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 19)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-04T16:46:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbk25a$jvj$1@reader1.panix.com>`
- **References:** `<5js7jrF12ab2U1@mid.individual.net> <13dqk06oocd5704@news.supernews.com> <rtsqd31h1gi38a1r4g0ivrvm4nakhlfumh@4ax.com> <13dr14otpjtse69@news.supernews.com>`

```
In article <13dr14otpjtse69@news.supernews.com>,
HeyBub <heybubNOSPAM@gmail.com> wrote:
>Howard Brazee wrote:
>> On Tue, 4 Sep 2007 07:31:52 -0500, "HeyBub" <heybubNOSPAM@gmail.com>
…[22 more quoted lines elided]…
>"real" belief?

There might be a bit of a difference between offering consideration to a 
statement which begins with 'I believe' and basing the rest of one's life 
on 'the man raving on the street corner'.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 19)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-04T12:29:24-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188934164.080195.235620@r29g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<13dr14otpjtse69@news.supernews.com>`
- **References:** `<5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net> <13dqk06oocd5704@news.supernews.com> <rtsqd31h1gi38a1r4g0ivrvm4nakhlfumh@4ax.com> <13dr14otpjtse69@news.supernews.com>`

```
On 4 Sep, 17:16, "HeyBub" <heybubNOS...@gmail.com> wrote:
> Howard Brazee wrote:
>
…[5 more quoted lines elided]…
>

I believe in UFOs. The abbreviation stands for Unidentified Flying
Objects. There are flying objects that are unidentified as also there
are falling and floating objects that remain identified. I don't
believe any of these unidentified objects are piloted by martians.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 19)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-05T09:58:59-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lfktd35flctnpemc9qtc859mvrhud3j78b@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net> <13dqk06oocd5704@news.supernews.com> <rtsqd31h1gi38a1r4g0ivrvm4nakhlfumh@4ax.com> <13dr14otpjtse69@news.supernews.com>`

```
On Tue, 4 Sep 2007 11:16:10 -0500, "HeyBub" <heybubNOSPAM@gmail.com>
wrote:

>I don't want to get bogged down in semantics or sentence structure. The 
>phrase, "I believe, based on a mountain of peer-reviewed evidence..." is 
>magnitudes different from "I believe, with a perfect faith..." 

Sure.   But don't be a Mr. Spock, surprised when people act like
people.   Wars are fought by nations which both *know* they are right.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-05T10:54:55+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k661uF2ad4kU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net> <13dqk06oocd5704@news.supernews.com>`

```


"HeyBub" <heybubNOSPAM@gmail.com> wrote in message 
news:13dqk06oocd5704@news.supernews.com...
> Pete Dashwood wrote:
>>
…[28 more quoted lines elided]…
>
That seems like a very adequate package for dealing with modern life and 
debate on the Internet :-)

>>
>> I think a blog that has arguments going on has to be more valuable
…[4 more quoted lines elided]…
> Bah!

Yes, I take your point. However, I believe that even the insane should have 
a voice. Sometimes there are diamonds in the dross.

>
>>
…[8 more quoted lines elided]…
>

I hasten to add that I am NOT against moderated Newsgroups, and there are 
times when groups SHOULD be moderated. I just wouldn't like to see ALL 
groups moderated and, to me, this one is valuable as being one of those that 
isn't.

> ------
> * One form the abuse took was the so-called "dippy flood," up to 30,000 
> messages in one day containing nonsensical text. Another was a kook who 
> complained to ordinary poster's ISPs - repeatedly.

That makes me sad.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 18)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-04T20:27:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ds1erivu1ik15@news.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net> <13dqk06oocd5704@news.supernews.com> <5k661uF2ad4kU1@mid.individual.net>`

```
Pete Dashwood wrote:
>> * One form the abuse took was the so-called "dippy flood," up to
>> 30,000 messages in one day containing nonsensical text. Another was
…[3 more quoted lines elided]…
>

For more on this business, see "Hipcrime" in Wikipedia.

SuperNews (to which I subscribe) and a couple of others have procedures in 
place to filter such drivel. I despair of the poor souls who have to rely on 
an ISP's news server.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 16)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-09-05T22:36:02-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T5mdncY2vNFkHkLbnZ2dnUVZ_u6rnZ2d@comcast.com>`
- **In-Reply-To:** `<5k3h5nF1ub9aU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net> <13do591egchnj22@news.supernews.com> <5k3h5nF1ub9aU1@mid.individual.net>`

```
Pete Dashwood wrote:
> 
> It is the right of the Blog owner to monitor posts. If people want to rant 
…[7 more quoted lines elided]…
> newsgroup, then you should be prepared to run it as such.

I don't censor posts on any of my blogs.  Of course, I state that I 
reserve the right to - I want my personal blog to be clean.  But, that 
doesn't stop me from running the anti-spam plugin that comes with 
WordPress.  There's just something about links to underage asian anal 
sex that doesn't jive with my site's content.  (At last check, the spam 
filter had caught 1,745 spams since I started using it a few months ago 
- and, it's only missed 2.  Good coding...)
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 14)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-04T02:45:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dpvvvnojod3f4@corp.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <5jvtfrF1gru2U1@mid.individual.net> <13dm46tre8050cc@news.supernews.com> <5k129aF1m29sU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5k129aF1m29sU1@mid.individual.net...
[snip]
> Anyone runnng a server has the right to control what goes over it.
>
> However, IF you decide to allow your server to be used for PUBLIC
> UNMODERATED Newsgroups, then it is wrong to censor posts to those groups.

Except that comp.lang.cobol is a semipublic unmoderated
newsgroup; therefore, any "rules" for public unmoderated
newsgroups do not apply, completely. <g>

What makes comp.lang.cobol semipublic is the name. It
suggests a public community that includes those with any
interest in the computer language COBOL; but excludes
those with no interest in COBOL.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-02T09:14:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n4hld3t5j1p3jo2g3e4p7n8foj2tbqp0kj@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com>`

```
On Sun, 02 Sep 2007 04:08:13 -0700, Alistair <alistair@ld50macca.demon.co.uk> wrote:


>I think that the nutter who posts anti-MI5 messages is a good
>justification for moderation of this group.

Maybe MI5 is a typo. He means MIS, the '80s term for the computer department.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 11)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-04T08:59:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com>`

```
On Sun, 02 Sep 2007 04:08:13 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> Bollocks! First off, COBOL Is not a "larger view on life" It is a computer
>> programming language entering its Goetterdammerung.
>
>If you don't believe in God or Gods how can you use a phrase which
>translates as the Twilight of the Gods?

Are you implying that there others who believe in Goetterdammerung, or
are you just wondering how can the term ever be used in a phrase?
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 12)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-04T12:26:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188933977.447765.204860@r34g2000hsd.googlegroups.com>`
- **In-Reply-To:** `<1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com>`

```
On 4 Sep, 15:59, Howard Brazee <how...@brazee.net> wrote:
> On Sun, 02 Sep 2007 04:08:13 -0700, Alistair
>
…[8 more quoted lines elided]…
> are you just wondering how can the term ever be used in a phrase?

There are people who are alive today and believe in the Norse Gods. I
would have expected an atheist to refrain from using phrases or
concepts relating to deities (a crime of which I am probably guilty).
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-05T11:02:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k66fvF2a38cU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1188933977.447765.204860@r34g2000hsd.googlegroups.com...
> On 4 Sep, 15:59, Howard Brazee <how...@brazee.net> wrote:
>> On Sun, 02 Sep 2007 04:08:13 -0700, Alistair
…[15 more quoted lines elided]…
>
Alistair, that's just silly.

There is nothing offensive, even to the most devout Druid, about my use of 
this term in the context above.

No offense was intended, and that is pretty crucial when you come to decide 
what is offensive.

The term has exactly the overtones and subtleties that I see in the demise 
of COBOL. I didn't say it to be offensive.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 14)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-05T03:25:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188987959.571316.221700@g4g2000hsf.googlegroups.com>`
- **In-Reply-To:** `<5k66fvF2a38cU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net>`

```

Pete Dashwood wrote:
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1188933977.447765.204860@r34g2000hsd.googlegroups.com...
…[28 more quoted lines elided]…
>

I didn't find the term offensive or the context in which it was used.
It does seem to sum up the current state of Cobol accurately (but what
about OO Goetterdammerung?).
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 15)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-06T03:25:54+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k803uF2fd0dU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1188987959.571316.221700@g4g2000hsf.googlegroups.com...
>
> Pete Dashwood wrote:
…[38 more quoted lines elided]…
>

OO is booming. Every new language supports it and the non-procedural 
paradigm has gained the high ground. In and of itself, OO is not a perfect 
answer, (interoperability of OO libraries is still problematic, although 
platforms like DotNET and Mono are addressing this very effectively), but it 
does lead to things like encapsulated components, and that is a major leap 
forward. There is no comparison between the way OO leverages reuse and the 
way that COBOL does, although many here never clicked on the differences and 
believed, some even to this day, that it is just modular programming 
re-invented. (it isn't...)

As to the Goetterdammerung of OO, I'd say around 2025, 2030, when artifical 
intelligence will be taking over what little "programming" remains to be 
done. By then we should be seeing increased intelligence through "hybrids" 
of humans and robots (probably nanobots, but still robots), until eventually 
(around 2045) the predicted "Singularity" takes over and the machines will 
be part of us, and indistinguishable from us. I would expect the logarithmic 
increases in (machine assisted) intelligence to produce smarter ways of 
programming machines (the few remaining ones that need to be programmed) By 
2060, programming will be an archaic concept with smart software writing 
itself.

I hope I live to see it, but it is very unlikely. Still, we are likely to 
see some life-prolonging technology before then, so you never know :-)

Personally, I'm much more excited by new advances in data retrieval 
(Lambdas, query expressions) and completely different approaches to 
programming like the heuristic and genetic models I mentioned here in 
passing some months ago:
( 
http://groups.google.co.nz/group/comp.lang.cobol/browse_thread/thread/2d08dc39637d5d80/176c85b8a63278e5?lnk=gst&q=heuristic+DNA+sort&rnum=1&hl=en#176c85b8a63278e5 )

Still, OO gets the job done in the meantime :-)

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 16)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-05T11:19:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s2ptd3d3h4gdpg53s16q4fab0c4on18l7f@4ax.com>`
- **References:** `<fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net>`

```
On Thu, 6 Sep 2007 03:25:54 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>OO is booming. Every new language supports it and the non-procedural 
>paradigm has gained the high ground. In and of itself, OO is not a perfect 
…[6 more quoted lines elided]…
>re-invented. (it isn't...)

CoBOL leverages reuse of the code behind ADD MY-FIELD TO SUMM-FIELD.

OO's main difference is that it's reuse granularity is bigger.

>As to the Goetterdammerung of OO, I'd say around 2025, 2030, when artifical 
>intelligence will be taking over what little "programming" remains to be 
…[7 more quoted lines elided]…
>itself.

I suspect we won't notice when we pass through that singularity.

Oh, Vernor Vinge's _Rainbows End_ just won this year's Hugo for best
SF novel.    One of the characters in that book wondered if that title
(when used to describe a retirement community) was a typo. Interesting
ambiguity there.    The novel has a near-singularity setting with
issues that we see coming.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-06T11:10:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k8raoF2ks1sU1@mid.individual.net>`
- **References:** `<fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <s2ptd3d3h4gdpg53s16q4fab0c4on18l7f@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:s2ptd3d3h4gdpg53s16q4fab0c4on18l7f@4ax.com...
> On Thu, 6 Sep 2007 03:25:54 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[16 more quoted lines elided]…
>

That's an interesting way to look at it, Howard.

I don't disagree; certainly the cost of maintaining code at a line by line 
level is becoming too high.

It is analogous to high level languages taking over from Assembler because 
the cost of writing and maintaining Assembler could not compete with 
generating code through a compiler.

While I agree that the "reuse granularity" is higher with OO, there are also 
other, more tangible, immediate benefits from using it. Like, severe 
reduction or even elimination of maintenance and regression testing, and, 
for me, most importantly, a different approach to system development which 
breaks the bloody Waterfall. :-)

Today I am working on the tool set for migrating VSAM/ISAM to RDBMS (for a 
client; I did this migration around 15 years ago for my own stuff). The 
central management console for these tools, and some of the tools 
themselves, are being written in C#, using VS2005 as the IDE. It staggers me 
how quickly and easily I can use objects from the DotNET framework to 
achieve things that were very painful when I did them in COBOL.

Want to let a user use a file selection dialogue and make multiple 
selections?  4 lines of code (including setting the header and the filter). 
Just instantiate a fileDialogue object. Want to know what version of ACCESS 
or SQL Server the user is running? Instantiate a Registry object and invoke 
it's search method.  Need to parse and filter COBOL code? Use Regular 
Expression objects and save hundreds of lines of COBOL code. (yesterday I 
had to smile because I needed to remove left and right brackets from a 
string (they were not necessarily at the start and end of it; could be 
embedded), and I wanted to remove all text after the first hyphen 
encountered (if there was a hyphen in it), at the same time. I managed to 
formulate a RegEx that actually worked, without referring back to any texts 
or searching the web for help. Two lines of code (for the sake of clarity... 
it could have been one.). The equivalent with INSPECT doesn't bear thinking 
about... I'm starting to get the hang of this :-))

About 70% of the final delivery is components that were written in COBOL and 
are now being re-wrapped for use from C#. This is where the OO approach has 
really paid off. If these were simply COBOL modules and DLLs it would be 
MUCH more difficult to get Interop Services to recognise and manage them. 
Because they are COM components they have a standard (OLE) interface, are 
encapsulated, and I have had remarkably few problems in getting them to run 
as unmanaged code in the CLR. The integration is easy and seamless (once you 
understand a few of the basic rules), but it wouldn't be if these components 
were COBOL programs.

So, OO (and the cmponent based approach, using it) has allowed me to move on 
to a more modern platform WITHOUT abandoning my investment in COBOL, and it 
is continuing to allow me to develop better and smarter components that will 
serve me well into the future.

I'm very happy with it :-)

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 18)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-09-05T21:05:54-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dukq99bacb41@corp.supernews.com>`
- **References:** `<fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <s2ptd3d3h4gdpg53s16q4fab0c4on18l7f@4ax.com> <5k8raoF2ks1sU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5k8raoF2ks1sU1@mid.individual.net...
[snip]
> While I agree that the "reuse granularity" is higher with OO, there are
also
> other, more tangible, immediate benefits from using it. Like, severe
> reduction or even elimination of maintenance and regression testing, and,
> for me, most importantly, a different approach to system development which
> breaks the bloody Waterfall. :-)

About twenty yeas ago, the spiral model began replacing
the waterfall model, though elements of the waterfall model
remain in the fourth spiral.

Object-Oriented Analysis, Object-Oriented Design, and
Object-Oriented Programming, thus OO, may still be used
in the spiral model; particularly, in those elements of the
waterfall model that remain in the fourth spiral.

There is nothing inherent in OO that is "a different approach
to system development which breaks the bloody Waterfall."
I say this because I believe your statement to be factually
inaccurate and, because the waterfall model is obsolete
[Waterfall Model, 1956-1988, R.I.P.], your continuing to
beat that dead horse is neither helpful nor informative. <g>

About 1982, the evolutionary development model was born.
There appear to be some off-shoots of that model that are
talked about in glowing terms and, if I recall correctly, the
development method you use, Mr Dashwood, falls into that
category.

Interestingly, Microsoft has revived the "dead" waterfall model,
treated it as something completely different than the spiral model,
and combined the two into the unified model which is used for
the Microsoft Solutions Framework (MSF). See
< http://www.microsoft.com/mspress/books/sampchap/3869.aspx >
for a description.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-06T23:58:38+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ka8bhF2r4r3U1@mid.individual.net>`
- **References:** `<fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <s2ptd3d3h4gdpg53s16q4fab0c4on18l7f@4ax.com> <5k8raoF2ks1sU1@mid.individual.net> <13dukq99bacb41@corp.supernews.com>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13dukq99bacb41@corp.supernews.com...
>
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
…[38 more quoted lines elided]…
>

I'm perfectly familiar with the spiral model and I know what it's 
shortcomings are. That's why I have modified it for my own use. Yes, I use 
the evolutionary approach and I find that Objects help that approach. I'm 
not interetsed in theories about what constitutes OOA/OOD/OOP, structured 
programming or modular programming or anything else, other than what works 
and delivers the goods. (As it happens, in passing, I have made it my 
business to nderstand the theories, but I am certainly not tied to them and 
what I actually do is a combination of many things form different 
methodologies, that have been found to work.)

I have worked, in the course of 40 years on more than 50 sites, in 7 
countries. I have never seen a text book implementation of  the spiral model 
employed successfully on any of them.

If there was a poll here you would find that the majority of the sites 
people here are working on are still using the Waterfall, be it obsolete or 
not. Ask how many people here are allowed to design and write code by 
iterative interaction with users, without requiring signoffs, and without a 
given phase starting before the previous is completed and signed off. Like 
COBOL it is far from a "dead horse" on many sites. That is what I was 
addressing.

There is plenty inherit in the Object approach that breaks the Waterfall. 
Objects can be identified and developed before the entire design is 
complete, timeboxed object development can proceed in parallel, as opposed 
to the serial requirements of the Waterfall. I just don't think you are 
qualified to speak on this Rick. (This is not meant to be critical or 
derogatory; there are many things you are well qualified to speak on, but 
practical management of IT development does not appear to be one of them.) 
Your knowledge is limited to text books and theories, and I don't see a 
track record of actual implementations you have managed. The fact is that 
life in the real world is a lot different from the Halls of Acadaemia.

You need to get out more.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 18)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-06T08:54:04-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e540e3hnbr7a7h33nrit870vql7dpg63q4@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <s2ptd3d3h4gdpg53s16q4fab0c4on18l7f@4ax.com> <5k8raoF2ks1sU1@mid.individual.net>`

```
On Thu, 6 Sep 2007 11:10:13 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>While I agree that the "reuse granularity" is higher with OO, there are also 
>other, more tangible, immediate benefits from using it. Like, severe 
>reduction or even elimination of maintenance and regression testing, and, 
>for me, most importantly, a different approach to system development which 
>breaks the bloody Waterfall. :-)

This is something that I've never been as convinced about as many
people are.    My experience of testing tools, is that they are great
at showing that my coding does what I think it does.    And creating
test programs means I have to think through a test plan, which is
good.

But coding is easy - the main purpose of testing is to make sure that
the users get the correct product.    This may not be what they asked
for, nor what I assumed they needed - nor even what they thought they
needed.   

The main advantage of automated testing tools is one that doesn't
apply to stand-alone programs.   This advantage is when I incorporate
or modify existing code and just want to make sure I didn't break any
existing functionality.

We have a program which used to be called by lots of other CoBOL
programs.   I have no idea why the vendor designed it, but it was our
standard to access KSDS files via this called program.    Trouble is,
it had a minor bug - it checked for the status code of commands, and
if the first digit wasn't a zero, it returned a "7" to the calling
program saying that the command failed.    The calling program didn't
know that the error was a "97", which is a successful return code. But
that program was called by a bunch of programs, and our standards
require a test plan that included extensive testing (with user
participation) of every job effected.    It just wasn't cost effective
to fix that program so we lived with an occasional abort and restart.

OO environments can't live in this environment, so standards were
developed around creating automated testing with enough confidence
that we can accept that changes made don't break existing
functionality.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-07T10:50:57+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kbeiiF2uem5U1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <s2ptd3d3h4gdpg53s16q4fab0c4on18l7f@4ax.com> <5k8raoF2ks1sU1@mid.individual.net> <e540e3hnbr7a7h33nrit870vql7dpg63q4@4ax.com>`

```


"Howard Brazee" <howard@brazee.net> wrote in message 
news:e540e3hnbr7a7h33nrit870vql7dpg63q4@4ax.com...
> On Thu, 6 Sep 2007 11:10:13 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[39 more quoted lines elided]…
> functionality.

 That sounds like a reasonable solution, given the environment you're in.

I'm certainly not against use of testing tools where it makes sense to do 
so.

I completely agree that users should get what they want and need, but it 
should be what they want and need NOW, NOT what was specced and signed off 6 
months ago. I see working with them in JAD workshops as the best way of 
achieving that.

I am slightly puzzled as to why fixing a highly used program with a known 
bug was considered "not cost effective". If it meant getting Users involved 
in regression testing, surely that's a good thing?

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 20)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-07T12:34:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbrgg2$ef$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5k8raoF2ks1sU1@mid.individual.net> <e540e3hnbr7a7h33nrit870vql7dpg63q4@4ax.com> <5kbeiiF2uem5U1@mid.individual.net>`

```
In article <5kbeiiF2uem5U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>I completely agree that users should get what they want and need, but it 
>should be what they want and need NOW, NOT what was specced and signed off 6 
>months ago.

I was hoping not to respond to this... but a situation that has come up in 
the past - and came up just again today! - suggests to me that it might be 
best to offer a differing viewpoint.

Mr Dashwood, the *business* should get what it wants and needs... not the 
users.  A user may be utterly unconcerned about how the changes requested 
will generate a distortion of a firm's financial picture; the Tax 
Authority or the Banking Commission or the Members of the Exchange may 
have a different focus.

What you suggest here is noble... but there may be constraints which work 
against it.  Were one to order (item) and (option01) from a merchant and 
then call back a few days later, saying 'You know, I changed my mind... I 
what (option02), as well' one might receive the response of 'We have 
already shipped your order; you will have to wait until we receive your 
return of it (if such a return is in our policy - if (option01) includes 
personal monogramming there might be a difficulty), built your next 
request and ship it out.'

I have heard there are shops where one's measurements can be 
laser-determined, styles chosen from catalogues and suits can be 
custom-made in a short time by transmitting these details to 
computer-controlled tailoring devices... were one to ask for Style 17805 
and come back a few hours later trying to change this to Style 17508 one 
might encounter a bit of resistance.

Likewise... when 'what they (see) they want and need NOW' generates, on 
the Technical Side, a kind of scope creep that causes a deadline to be 
pushed out... well, some people claim they never forget a missed deadline.

What causes me to make such obvious comments?  I've been working directly 
with users - or as directly as one can with users over a thousand miles 
away - on a Most Mundane request... monthly files to show employment and, 
sometimes, wages.  There are minimal specs, constant interaction with the 
users and nigh-immediate responses to change requests... and every time we 
ask 'Can this be considered done and moved into Production?' the response 
is 'I know we've told you everything is fine and haven't said a word for 
the past three months... but now that you mention it, can you change 
(thingie)?  Send us off a sample and we'll let you know.'

The situation, in short, has evolved into 'Don't do what I told you, do 
what I'm telling you'... and changes mean that historical data are 
rendered invalid ('Oh, you don't count an office under (condition), didn't 
we tell you that?') and have to be re-generated.  Time, of course, is 
money... and since no limits have been defined (or specified) the amount 
of time spent on the project can never be called 'enough'.

Nothing gets accomplished... all that gets done is an eternal re-visiting 
of yesterday's work because 'it's not what I see that I want and need 
NOW'.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 21)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-07T09:28:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YedEi.37759$7e6.33697@bignews4.bellsouth.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5k8raoF2ks1sU1@mid.individual.net> <e540e3hnbr7a7h33nrit870vql7dpg63q4@4ax.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote:
> ...
> The situation, in short, has evolved into 'Don't do what I told you, do
…[8 more quoted lines elided]…
> NOW'.

My guess is, most of those who have been in the software business for
a while have seen this kind of thing. Sometimes you can circumvent the
problem if you know enough about the situation and actual requirements
to think ahead of the users. I've had several clients comment to me, after
I delivered their new system, something like "You took what I asked you
for and made it better." Since I started my own company in 1980, I have
only contacted potential new clients twice, both at the urging of others,
and both successfully. Except for that, all my business has been from
word of mouth recommendations, from clients or friends of clients, so
I am simply not accustomed to unhappy clients. But you can't always
manage it, particularly if the client is afraid to make decisions.

In the 1980s I wrote a system for the local county Health Department,
for their environmental division. For may years the head of that
division had been one of those people who only tolerated "yes men"
working for him. The people in the department were afraid to make
decisions. He had recently retired when I was contracted to write this
system. I went through the steps, interviewed all the users who would
be involved, wrote up specs, created mock screen and report layouts,
all of which were duly signed off by the respective users. I wrote the
system, and the documentation, and we scheduled a time for the system
to be presented to the users so they could begin using it. During the
meeting, the users kept bringing up changes or additional features, to
the point that it required a virtual rewrite of the system. The Health
Department had been a good long time client, so I bit the bullet and
rewrote the system. When this system was presented as before, the
exact same thing happened. By this time I was getting annoyed, but I
again practically rewrote the system and the documentation. By this
time, I had written this system three times, and had used up all the
money in the contract, but I didn't say anything, and kept on working.
As the time drew near for the presentation, I could smell another trash
and burn session coming up, so I went to the MIS director, who went
to the comptroller, who went to the director, who called a meeting with
all of us. The environmental department had the gall to complain that,
not only was I taking too long, not giving them what they wanted, but
had gone "over budget" in the process. At this point, I was thinking
about a contract hit on these people. But when I explained to the
director, who knew me fairly well, that I had gone to every user,
designed a system to meet every request they had, taken the detailed
designs to them for signoff, and done it three times, had kept working
at my own expense after the money ran out, not billing one penny over
the original estimate, and slid the previous two sets of detailed designs
across the table to her, showing all the marked changes, she went
ballistic on the environmental people. They were given *one* chance
to request any needed changes from the now third iteration of the
design, and she extended my contract to pay for all the hours I had not
been paid for, and any needed money for the changes they might request.
Even though I was vindicated, and paid for all my work, it is not good to
have strained relations with your clients. Had I not had the documented
proof, or if there hadn't been more responsible upper management, or if
the director had not known that I was a reliable contractor, it could have
gone very badly. I'm not sure there was anything I could have done to
avoid that problem, other than declining the contract.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 22)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-07T14:52:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbrojt$q5d$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net>`

```
In article <YedEi.37759$7e6.33697@bignews4.bellsouth.net>,
Judson McClendon <judmc@sunvaley0.com> wrote:
><docdwarf@panix.com> wrote:
>> ...
…[12 more quoted lines elided]…
>a while have seen this kind of thing.

[snip]

>In the 1980s I wrote a system for the local county Health Department,
>for their environmental division.

[snip]

>As the time drew near for the presentation, I could smell another trash
>and burn session coming up, so I went to the MIS director, who went
…[3 more quoted lines elided]…
>had gone "over budget" in the process.

[snip]

>Even though I was vindicated, and paid for all my work, it is not good to
>have strained relations with your clients. Had I not had the documented
…[3 more quoted lines elided]…
>avoid that problem, other than declining the contract.

My apoligies for the snipping... but I believe I've managed to leave the 
intestines intact.  Currently the folks who sign my timesheet are of the 
'if I don't do what they ask I'll Look Bad', even if 'what they ask' is, 
as in this case, a contradiction of earlier explicit expressions and 
accepted work.

As in your case I've documented... by sending off previous emails showing 
What Was Asked For, What Was Sent and Thank You For The Accurate Work.

(A lot of this was taken care of by telephone... but *always* followed-up 
with an email, along the lines of 'lovely chatting with you, as I 
understand it you want (quack quack quack), did I get that right?')

The most recent version of 'now we want it THIS way' was met such 
documentation and a succinct 'To implement this contradictory request will 
require a fundamental change in processing which, in the opinion of a 
professional programmer, will be neither easy to do nor fast in its 
doing.'

DD
```

###### ↳ ↳ ↳ Can IT deal with change? was:

_(reply depth: 23)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-08T16:12:35+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kelplF3b3opU1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com>`

```
I'll use this reponse to respond to both of the excellent posts from Doc and 
Judson.

(In my previous post, I used "Users" to represent the Business, Doc, 
although I take your point that there is a distinction. )

If we are in the business of delivering a service to the Business (and I 
feel very strongly about that as being commercial IT's main mission) then we 
obviously want the Business to get what they need.

It doesn't matter what kind of "shop" you work in, or what methodologies are 
employed, you will feel good when you see that your hard work has made a 
difference, and life on the cutting edge of the Business is now easier 
because of work you did.

But so often, we don't get that "feel good" factor. Instead  what we get is: 
"It's very nice, but can we just have this one small change".

So why is it?

I see a number of factors that lead to the problems described by both Doc 
and Judson.

1. The Business seldom knows what it really wants, apart from core, business 
critical, processes. (Even then, different departments and User groups may 
see those processes in a different way with different emphasis). 
Furthermore, the Business is usually operating in a competitive marketplace 
where things are very fluid. If a competitor comes out with something that 
gives them an advantage, our Business must move to nullify it as quickly as 
possible. This will probably have repercussions for IT.

2. The Business don't know what IT is capable of. They are not IT experts. 
(Fortunately for all concerned, this pattern is changing and the average 
level of  computer literacy is rising exponentially. However, that also 
spawns problems for IT, when a few enlightened users develop some 
spreadsheets or databases that are "outside" of the Corporate IT fold. It is 
very hard to suggest replacing a 'fait accompli' when it is working fine, 
meets their requirements and it will cost them money to comply.

So what we end up with is an "us" and "them" situation which totally loses 
sight of the fact that everybody is on the same team and should be working 
together to solve problems.

More below...

<docdwarf@panix.com> wrote in message news:fbrojt$q5d$1@reader1.panix.com...
> In article <YedEi.37759$7e6.33697@bignews4.bellsouth.net>,
> Judson McClendon <judmc@sunvaley0.com> wrote:
…[16 more quoted lines elided]…
>>a while have seen this kind of thing.

Absolutely. I lived with it for many years on various sites. It finally came 
down to IT demanding an audit trail of sign-offs which the Business simply 
trumped by saying: "Well, whether that's what we agreed or not, it isn't 
what is needed NOW."  So you end up with sullen resentment from both sides 
and the situation never improves.
>
> [snip]
…[11 more quoted lines elided]…
>>had gone "over budget" in the process.

Ouch! Smarts, doesn't it? :-)

I think you were far too soft with them, Judson, but I understand why you 
were, and have stood in your shoes.
>
> [snip]
>
>>Even though I was vindicated, and paid for all my work, it is not good to
>>have strained relations with your clients.

No, it isn't. In fact, I find that intolerable, and if things look like 
becoming strained, I move very quickly to defuse it. Don't wait until it 
becomes a crisis... Next to your staff, your clients are the most important 
resource you have. It is very important to have things on the table where 
they can be addressed rather than to let resentment smoulder.

The same apples in Corporations. IT SHOULD be everybody's friend, but how 
many companies do you know where they speak highly of their IT department? 
It is a long history of promises made and broken on both sides.

> Had I not had the documented
>>proof, or if there hadn't been more responsible upper management, or if
>>the director had not known that I was a reliable contractor, it could have
>>gone very badly. I'm not sure there was anything I could have done to
>>avoid that problem, other than declining the contract.

Well, I can tell you there is, but we'll come to that in a moment. (Very 
glad to see you got it resolved and it is good to know there are SOME 
responsible managers somehwere :-))

>
> My apoligies for the snipping... but I believe I've managed to leave the
…[3 more quoted lines elided]…
> accepted work.

It is bad that you are not getting management support over this, Doc. Given 
the situation, and the fact that you have a documented trail of what has 
gone down, your management should be raising it so it can be addressed and 
dealt with. If they don't, the situation will not go away by itself. The 
Company needs to "learn" that what they are doing is not working and get 
something better in place. Stronger, more effective line management, for a 
start...
>
> As in your case I've documented... by sending off previous emails showing
…[10 more quoted lines elided]…
> doing.'

While I completely understand this position, in the broader scheme of 
things, it isn't helping.

Irrespective of whether the request is contradictory or not, the Business DO 
need something, and they need it now.

Before I go on, perhaps it is important to ask yourself: "If I COULD deliver 
on these contradictory requests, would I? Do I actually feel committed to 
providing a service to our Business?"

The reason I say this is because it can happen, after many years of working 
in these environments, that the real motivation for going to work in the 
morning gets lost, and instead it becomes about being seen to be "right" and 
collecting your cheque.

There is nothing we can do to prevent the Business from changing 
requirements. They don't usually do it to piss us off, they do it because 
they didn't think things through carefully enough in the first place, or 
because something happened in the Marketplace that requires them to change 
their processes and procedures.

So what CAN be done as far as IT is concerned?

The only effective approach I have ever found (and I've tried many)  is a 
combination of  JAD, RAD, evolution (interaction and iteration), and common 
sense (not being committed to ANY particular textbook approach.) DSDM is the 
ONLY one that works as it says on the box, IF you can manage  to do all the 
subtle things it requires. (It is based on the "spiral" approach).

Waterfall (SDLC), SSADM, PRINCE, RAD, I have found to all be flawed, IF you 
implement them as you are supposed to. This is NOT to say there is no value 
in any of them, on the contrary, there is much of value in most of 
them...except the Waterfall, which had value in a different time and is 
totally irrelevant today. Ironically, it is still the most used methodology 
on mainframe sites.)

It is far too much to go into here, but I can outline some principles:

1. Do NOT attempt to develop IT solutions in isolation from the Business (or 
end users). The IT ivory tower approach is doomed before it starts. (The 
Waterfall approach...gather requirements, get them signed off, then move to 
the next phase, with the Business only being consulted to set up the 
implementation date, is a typical example of this.) The Business should be 
involved from the start. Management and end users should be invited to 
Workshops with IT people (JAD) where the existing practices can be walked 
through and ways of improving them can be discussed.

Get The Business ENGAGED and they will feel like it is THEIR system and not 
something being thrust upon them by IT.

2. Get a decent Project Manager who can liaise with all interested parties 
and ensure that concerns and issues are addressed jointly and resolved. 
There should also be a public Project plan with milestones showing when 
deliverables will be available. (I use timeboxes, but that is not the only 
way...)

3. The Business must PRIORITISE the requirements defined. They call the 
shots. If they want to change something they can do so, but they will lose 
something else. (For small developments a single workshop is often enough to 
clarify priorities. I use MOSCOW but that is also not the only way...)

For IT, this represents some major changes in the way code is developed. 
Without sidetracking the discussion, I can say that Objects are ideally 
suited to this approach (Users can relate to objects easily; they get 
intimidated by jargon around Databases and processing cycles. It is much 
easier to discuss objects, methods, and properties in a JAD workshop than it 
is to talk database design.) Nevertheless, the approach I am outlining is 
applicable to both Procedural and OO systems.

Business Analysts can walk through Use Case scenarios with the Business and 
these can be scheduled for prototyping with programming.

Code is developed to support the given Use Cases. There won't be a program 
spec; the Use Case IS the spec and the programmer will have a full 
understanding of the process from being involved in the JAD session. 
Database design is completed only far enough to support the case. (You are 
going to change it anyway as things progress, so why do any more of it than 
you need to?) The programmer writes, tests and debugs the prototype, based 
on the Use Case.

The Use Case prototype is shown to the Users in a JAD workshop and any 
changes required are noted. (small changes can be made there and then, on 
the spot.) Users can see things happening and become supportive, rather than 
hostile. The project starts to buzz. The interaction and iteration between 
IT and the Business continues, with Use Case development continung in 
parallel, in accordance with the plan.

Changes are welcomed, not seen as a source of aggravation.

When the system is delivered it meets the CURRENT business requirement 
because it has evolved from the vision in the first workshops, with the 
Business and IT jointly evolving it, through iteration and interaction.

Now, obviously, it is unrealistic to expect a massive shift in organisations 
where they are using an approach they have used "successfully" for many 
years.

This comes back to my earlier point about line management. Unless someone 
makes a noise about what is happening and shows that it ISN'T working, there 
will be no call to change or improve it. I see that as down to line 
managers, in support of programmers who have raised the issue and shown the 
documents supporting it.

In Judson's case, where he is an independent consultant (like me), it is 
very tempting to go away and develop what you (and they) thought they 
wanted. Judson has already described what happens.  It is absolutely 
imperative that they be kept informed of what is going on and should be 
given the opportunity to change or re-prioritise it, always on the 
understanding that doing so will mean losing something else (or rescoping 
the whole project, which will cost them...)

I'm currently working on some tools for a client who is not here in NZ so I 
can't just "pop over" and have a chat or show them something I've just 
developed. Nevertheless, I produce a report every Friday explaining what I 
did, where things are on the plan, what I plan to do next week, any 
unforeseen difficulties and things that they can do to ease the transition 
for themselves. I also include screen shots of tools under development. I 
will fly to their location when I deliver, but if anything turns out to be 
not what they hoped, I'll gladly fix it free of charge.

As Judson noted above, "it is not good to have strained relations with your 
clients".

Whether I'm working as a Project Manager within an organization, with a team 
of IT People committed to providing service to the Business, or as an 
independent contract programmer or consultant providing support to my own 
clients, the deal is the same: "I'm here to provide a service. Without the 
consumers of that service, I don't have a business. By making them happy, I 
can achieve job satisfaction and a very good living."

If I ever stop feeling that way, I'll quit this business.

Pete.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 24)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-09-08T07:23:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5kelplF3b3opU1@mid.individual.net...
> I'll use this reponse to respond to both of the excellent posts from Doc 
> and Judson.
....

I'll not bother to quote from your somewhat lengthy post, but for all the 
suggestions you offer to narrow the gap between "what  I 
needed/wanted/expected" and "what I got" I am somewhat surprised you missed 
an important requirement: "project managers" and "management" and "progress 
reports" and "involving the business personnel" are fine, but how about "the 
developer must know and understand the business requirement FROM THE USER'S 
PERSPECTIVE?"

I'd like to have a nickel for every time I've suggested in response to "how 
do I get started with my software career?" questions here that prospective 
developers actually spend some time DOING the very tasks they are expected 
to support.

Spend some time on the sales/service desk. Invest a week on the 
shipping/receiving dock. Post some cash or enter payables in the accounting 
office. Do some real work on the shop floor. Help out generating a payroll. 
Hit the storage bins to assist with taking inventory. Speak with some client 
customers and vendors regarding things both routine and unusual.

Then you will know what users need, and I'll bet they start getting it.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 25)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-08T09:18:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f8yEi.38110$mp6.17467@bignews9.bellsouth.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com>`

```
Thanks, Pete and Michael, there's a lot of good stuff in there. While I
agree with everything both of you wrote, I'm doubtful that any of it
would have materially helped in my particular example.

For one thing, the project was small enough that the actual requirements
didn't materially change during development, even after writing it three
times. Only a few of the many change requests came from changing
requirements.

The real problem was in getting the users to make a final agreement that
*any* solution was sufficient. There was an indecisiveness and fear of
commitment that I've never seen before or since. From what I was told,
and what I saw, the former department head must have been a tyrant.
He had been head of that department for many years. You know how
ruthless dictators like Stalin and Hussein eliminate anyone who could
conceivably challenge or threaten them, then after the dictator dies there
is chaos, because anybody who could have been a leader had been
eliminated? This was something like that. As annoyed as I was at those
people, I was also sorry for them. I've never seen anything like it in a
sizable group of people.

There is always a bright spot. I was somewhat gratified that I was able
to write the system almost three times for my initial estimate. :-)
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 25)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-09T02:43:53+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kfqpcF3dnhrU1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com>`

```


"Michael Mattias" <mmattias@talsystems.com> wrote in message 
news:vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com...
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:5kelplF3b3opU1@mid.individual.net...
…[10 more quoted lines elided]…
> FROM THE USER'S PERSPECTIVE?"

Sorry, I thought I  covered that...and I agree it is essential... let me 
see... Ah, yes...

"Code is developed to support the given Use Cases. There won't be a program
spec; the Use Case IS the spec and the programmer will have a full
understanding of the process from being involved in the JAD session. "

If you have never sat in on a Joint Application Development workshop where a 
particular Use Case is being modelled, it is hard to imagine how much people 
benefit from being involved in the process. Programmers and Business 
Analysts will gain more understanding of the Business requirements and 
processes than they could in a week on the shop floor. However, time on the 
shop floor is always an option and I have seen one or two workshops where IT 
people ended up working in the business for a week. It certainly did no 
harm.

The good thing about such a workshop is that the Business people can do the 
walkthrough and explain what the existing process does and how it fails to 
meet their criteria (if it does). The IT people can see it and discuss 
options for fixing it or changing it in the new system. Both sides work 
together to get what I once laughingly referred to as a  "Really USEFUL Use 
Case" ... the name stuck and to this day in that particular organisation 
they consider a Use Case to be complete when it is "RU" (Really Useful) :-) 
But the important point which Michael raised is that programmers should 
understand the Business process.

(This is one good reason for dispensing with a program spec. and going with 
an iterative approach instead. A program spec can be programmed, with no 
real understanding, as if by an automaton, and it can be used to justify a 
position. (I once fired someone for following a spec. knowing full well it 
was wrong, because he was having a personal vendetta with the Analyst who 
wrote it. He made a mistake in saying to me: "You can't touch me; I did what 
it said in the spec."   He was terminated not for following the spec. but 
because I don't take shit like that from anyone, and becase I don't want 
people with that attitude on my team.:-)))

Many organizations would throw up their hands in horror at the suggestion of 
not preparing a spec.  "What will we have to beat up the users with when 
they claim what they got is wrong?"  Well, they don't claim what they got is 
wrong, because it isn't, and their attitude is not a hostile one because 
they have been engaged in the process throughout and know what decisions 
were taken and agreed in JAD workshops and Use Case walkthroughs. Besides if 
it WAS wrong, it is no big deal to fix it, as changes are welcomed.

So what does a maintenance programmer refer to when the process needs 
maintenance? Two things: The program souce code and the documented Use Case. 
There is other system documentation and minutes of JAD sessions and 
workshops than can also be referenced for background.

Pete.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 25)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T12:47:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com>`

```
On Sat, 8 Sep 2007 07:23:43 -0500, "Michael Mattias" <mmattias@talsystems.com> wrote:

>Spend some time on the sales/service desk. Invest a week on the 
>shipping/receiving dock. Post some cash or enter payables in the accounting 
…[4 more quoted lines elided]…
>Then you will know what users need, and I'll bet they start getting it.

Wal-Mart requires new programmers to work in a store 2-4 weeks before they start coding.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 26)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-09-08T17:43:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9WFEi.2590$3Y1.2232@newssvr17.news.prodigy.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com> <9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com...
> On Sat, 8 Sep 2007 07:23:43 -0500, "Michael Mattias" 
> <mmattias@talsystems.com> wrote:
…[13 more quoted lines elided]…
> start coding.

What a coincidence. I have been saying for years that Walmart is one of the 
most sophisticated IT users in the world.

Nothing personal, but I will try to get a second source to confirm this. (So 
"I told you so" doesn't bite me in the ass).

MCM
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 27)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T21:59:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com> <9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com> <9WFEi.2590$3Y1.2232@newssvr17.news.prodigy.net>`

```
On Sat, 8 Sep 2007 17:43:16 -0500, "Michael Mattias" <mmattias@talsystems.com> wrote:

>"Robert" <no@e.mail> wrote in message 
>news:9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com...
…[18 more quoted lines elided]…
>most sophisticated IT users in the world.

That's what I thought .. until I worked there in central change management. It's all hot
air. The David Glass Technology Center is full of 2,500 operations types who spend all day
stomping out fires in dozens of war rooms. There's no thought given to fixing problems
because the few developers they have aren't allowed to change anything. Programs haven't
been compiled in ten years because they don't know which source is running in production.
The "world's largest private network" can't send a file unless you manually split it into
pieces smaller than 100K, then manually reassemble the pieces. They're afraid you might
interfere with a credit card authorization and don't know how to assign priorities to
packets.

They have impressive capability. One weekend we opened 54 new stores. But it ain't
sophisticated by any definition. 

I was very disappointed. They have the money and clout to do things right, but they're
pissing away the opportunity.

>Nothing personal, but I will try to get a second source to confirm this. (So 
>"I told you so" doesn't bite me in the ass).

You can probably find it on their Web site. Their programmers tend to be young, Arkansas
locals,  undereducated, unsophisticated, ambitious and very intelligent. They don't do
much real programming, they do production support. What a waste of talent.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 28)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-09T09:14:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc0dhp$dgl$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com> <9WFEi.2590$3Y1.2232@newssvr17.news.prodigy.net> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com>`

```
In article <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 8 Sep 2007 17:43:16 -0500, "Michael Mattias"
><mmattias@talsystems.com> wrote:
>
>>"Robert" <no@e.mail> wrote in message 
>>news:9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com...

[snip]

>>> Wal-Mart requires new programmers to work in a store 2-4 weeks before they 
>>> start coding.
…[6 more quoted lines elided]…
>air.

[snip]

>Their programmers tend to be
>young, Arkansas
>locals,  undereducated, unsophisticated, ambitious and very intelligent.
>They don't do
>much real programming, they do production support. What a waste of talent.

I was once offered a contracting gig in Bentonville... what floored me was 
that how immediately my comment about how low the rate was generated a 
response of 'Oh, the cost of living's so low over here, it makes up for 
it.'

I replied 'Oh... so when I buy a new car or send my kid to Princeton or 
take a two-week cruise through Alaska then people will say 'Ahhhhh, you 
are from Bentonville, for *you* we have Special Low Rates!'... and that 
garngered a giggle.  there was then talk about how one could not live a 
Fancy Life, that one's dewllings and doings had to fit into the 
parsimonious example set by The Founder... what good is earning even high 
los rates when you can't spend any of it?

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 29)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-09T05:51:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com> <9WFEi.2590$3Y1.2232@newssvr17.news.prodigy.net> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com>`

```
On Sun, 9 Sep 2007 09:14:33 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com>,
>Robert  <no@e.mail> wrote:
…[37 more quoted lines elided]…
>los rates when you can't spend any of it?

Wal-Mart pays average or slightly above. Cobol contractor gigs pay $45-50/hr. The cost of
housing in Bentonville is higher than expected. I was paying $1,800/mo for an 'executive'
apartment and was furnished and month-to-month. Modest houses sell for $300K. The price of
housing is driven up by Wal-Mart middle managers.

Bentonville and Rogers, which run together, have a combined population of 70,000. It's not
a little hick town, although there isn't much to do for entertainment. Eureka Springs, 30
miles away, is a popular weekend destination. It's a tourist town run by aging hippies.
The nearest cities are Fayetteville/Springdale 20 miles, Joplin MO 50 miles and Tulsa 100
miles. There is a nice small commercial airport at Bentonville. 

Outsiders mistakenly expect NW Arkansas to be full of hillbilly hicks. It's not like that.
People are similar to  Dallas residents. Wal-Mart systems programmers are as sharp as
you'll find anywhere. 

Wal-Mart's IT is in a building that looks from the outside like an abandoned warehouse. It
was actually purpose built. It is Spartan, no frills functional. There is no art work nor
windows; you have to empty your own trash. The server room is an impressive sight, if you
can get inside. Most workers never do. It has seemingly miles of rack mounted servers.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-09T16:09:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc15s0$bjt$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com>`

```
In article <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>There
>is no art work nor
>windows; you have to empty your own trash.

*Everyone* in there is on their own Dumpster Detail?  (It'd be kind of 
weird to see the maintenance folks going down the aisles, consulting a 
list as to whose trash they are to empty or not.)  How interesting... 
those numbers might tell a story.

Hmmmmm... so, let's see... programmers work in there so the average rate 
will be a bit higher than, say, in a data-entry operation... so Il'' guess 
that time costs, on average, US$1/min to the corporation (some are 
contractors, making more, some are juniors, making less, some are 
managers, sitting in corner cubicles... a WAG average) and there are a 
hundred people working there, each taking two minutes a day - one minute 
to get to Trash Central, zero time to dump and one minute to get back - to 
deal with their garbage.

One hundred people times two minutes a day times one dollar per hour works 
out to... cancel out on this side, carry the nought... two hundred dollars 
a day; based on the simple-minded five-day fifty-week year that's an 
annual cost of US$50,000.

In that part of the world I'd also guess that a maintenance worker, 
dedicated *solely* to emptying and carting trash - and I have never seen a 
worker allocated thusly, they always have other tasks - might be had for a 
cost of US$35,000.

So... if they hired someone just to deal with the wastebaskets everyone 
else in the building could get an additional US$100/year and the company 
would *still* show a cash benefit.  The conclusions from this include that 
WalMart cannot perform simple Cost/Benefit Analyses and Something Else is 
Going On Here.

(that might be another interesting sociological survey... assuming this is 
a company-wide practise I wonder at what point people are considered as 
being worthy of having someone else empty their wastebaskets)

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 31)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-09T12:39:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com>`

```
On Sun, 9 Sep 2007 16:09:36 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com>,
>Robert  <no@e.mail> wrote:
…[5 more quoted lines elided]…
>>windows; you have to empty your own trash.

>So... if they hired someone just to deal with the wastebaskets everyone 
>else in the building could get an additional US$100/year and the company 
…[6 more quoted lines elided]…
>being worthy of having someone else empty their wastebaskets)

There is a lot of symbolic stuff going on at Wal-Mart. In rooms where buyers meet vendors,
furnishings are plastic lawn chairs and folding tables. The image is frugality, cutting
costs to the bone. They use normal office furniture in cubicles that visitors don't see. 

They make visitors and employees pay for coffee at their cost, which comes to .05 per cup.
They squeeze snack machine vendors' profit. Items that sell for $1 elsewhere are priced at
$.25. The normal work week for exampt employees is 45 hours. Most start work at 7am. 

They are paranoic about security. Failing to lock your keyboard when you go to the
bathroom (in a secure building) is punished by loss of network access. Managers receive a
weekly report listing every Web page you visited and every outside email sent and
received. Devices with WiFi capability are not allowed in the building; cell phones are
not allowed near the server room. I believe there's a Faraday cage around the building.
Store computers with RF do not have access to the network, causing a headache for support.

>I was once offered a contracting gig in Bentonville... what floored me was 
>that how immediately my comment about how low the rate was generated a 
>response of 'Oh, the cost of living's so low over here, it makes up for 
>it.'

When the pimp talks of low cost of living, it means his markup is above normal.

Cost of living is a function of home ownership. Contractors don't buy houses, they live in
apartments. Apartment rent is the same almost everywhere -- $800-1,000 per month, except
for NYC and SanFran.  Contractors are better off in high cost of living places because
more of their income is sheltered from taxes by per diem. It is $70K per year in big
cities versus $30K elsewhere.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 32)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-09T18:01:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc1ce4$bmp$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com>`

```
In article <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sun, 9 Sep 2007 16:09:36 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[19 more quoted lines elided]…
>There is a lot of symbolic stuff going on at Wal-Mart.

For some reason I have a feeling that all the symbolic stuff is instituted 
with an idea of generating more income for The Corporation at the 
expense/bother/head-ache of *anyone* else... not necessarily the practise 
of doing so, as the above-snipped example might have demonstrated, but the 
idea thereof.

It reminds me of a tactic used by spokesfolk for Major League Baseball 
teams in the United States of America; they will begin by talking about 
the sport as The National Passtime, about how sport's history and that of 
the country are inseparably interwoven, about how the Symbolism of 
Baseball is a part of each American's psyche...

... and then, at any given time, respond with 'Well, it may be the 
National Passtime but let's all be Grown Ups here and remember that it is, 
after all, a business... and as such a business has to make business 
decisions...'

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 33)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-09T15:53:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com>`

```
On Sun, 9 Sep 2007 18:01:41 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com>,
>Robert  <no@e.mail> wrote:
…[27 more quoted lines elided]…
>idea thereof.

Receiving free gifts is a major no-no in the Wal-Mart culture. Not only are salesman-paid
lunches out, you can't even accept a lunch paid for by another employee. The company
doesn't provide free coffee and trash removal because they don't want employees to get in
the habit of accepting anything free. 

Wal-Mart is very ethical. They drive a hard bargain on cost, but never renege on a promise
nor lie about anything.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 34)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-09T22:01:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc1qeu$cu7$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>`

```
In article <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sun, 9 Sep 2007 18:01:41 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[31 more quoted lines elided]…
>Receiving free gifts is a major no-no in the Wal-Mart culture.

Ummmmm... I thought a gift, by definition ('something voluntarily 
transferred by one person to another without compensation', 
http://m-w.com/dictionary/gift ), was free.

>Not only
>are salesman-paid
>lunches out, you can't even accept a lunch paid for by another employee.

If The Company (*any* company) believe it will dictate what legal acts I 
will perform during my own hours with another consenting adult during 
their own hours thenit might be rather disappointed... and if my behavior 
is not dictated by my whim then I'm on The Company's clock.

(this might be a reason why I have never worked for a company where I had 
to carry a beeper; my policy has been 'If I cannot get falling-down drunk 
then I'm on your dime.')

>The company
>doesn't provide free coffee and trash removal because they don't want
>employees to get in
>the habit of accepting anything free. 

Let me get this straight... the company making sound economic decisions 
and keeping its workplaces in a sanitary condition is allowing 'employees 
to get in the habit of accepting anything free'?  Leaving that bit of 
apparent nonsense aside someone might want to notify Bentonvill about 
Bentonville's behavior.  Granted it is an old source, from 2004... but 
Walmart's culture is notoriously conservative, I don't think *that* much 
has changed since then.  From 
<http://www.forbes.com/2005/11/11/charities-corporations-giving-cx_lm_1114charity.html>

--begin quoted text:

Philanthropy was on the rise last year, thanks to increases in earnings in 
2003. Since most companies budget their charitable donations on the basis 
of the previous year's profits, that would seem to bode well for giving 
this year, too.

[snip]

In terms of the sheer size of cash donations, Wal-Mart Stores, the 
nation's largest retailer, would be at the top of the list. The Arkansas 
company gave some $197 million last year in cash ($188 million of it in 
the U.S. alone). That puts Wal-Mart ahead of Bank of America, Johnson & 
Johnson and Altria Group.

--end quoted text

So... on the one hand The Company is allowed to give away stuff... no, 
wait, it isn't really *giving*, The Company is generating tax 
write-offs... so The Company participates in quid pro quo while it forbids 
its employees to gain similar advantages.  Didn't someone say, recently, 
that 'For some reason I have a feeling that all the symbolic stuff is 
instituted with an idea of generating more income for The Corporation at 
the expense/bother/head-ache of *anyone* else'?

>
>Wal-Mart is very ethical. They drive a hard bargain on cost, but never
>renege on a promise
>nor lie about anything. 

I believe that WalMart is as ethical and as truthful as any other 
corporation in its class, more-or-less... oh, wait, didn't someone 
recently say that a statement that begins with 'I believe' can be 
dismissed out of hand?

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 35)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-10T14:03:42+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kjn00F3ui90U1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <fc1qeu$cu7$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fc1qeu$cu7$1@reader1.panix.com...
> In article <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>,
> Robert  <no@e.mail> wrote:
…[9 more quoted lines elided]…
>>>>>[snip]
.
>
> I believe that WalMart is as ethical and as truthful as any other
…[3 more quoted lines elided]…
>

The fact that such a statement was made, does not make it true. :-)

If it WERE true, then all the beliefs of all the people contributing to this 
forum  could be "dismissed out of hand...", including the beliefs of the 
person making the statement.

Anyway, that's what I believe...:-)

Pete.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 35)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-09T22:42:36-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <fc1qeu$cu7$1@reader1.panix.com>`

```
On Sun, 9 Sep 2007 22:01:02 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>,
>Robert  <no@e.mail> wrote:
…[37 more quoted lines elided]…
>http://m-w.com/dictionary/gift ), was free.

Business 'gifts' are not free, they carry an expectation of something in return.

>>Not only
>>are salesman-paid
…[5 more quoted lines elided]…
>is not dictated by my whim then I'm on The Company's clock.

It is difficult to be impartial toward sex partners, drinking buddies, golfing partners,
your child's godparent, etc. 

>>The company
>>doesn't provide free coffee and trash removal because they don't want
…[8 more quoted lines elided]…
>Walmart's culture is notoriously conservative

If conservative means resistant to change, the company is a flaming liberal. It is
constantly experimenting with concepts intended to change its image. For example, a
boutique in South Beach (Miami FL) selling hip trendy clothing for discount prices. For
example, a green store in McKinney TX built from recycled material and using
wind-generated electricity. For example, a 'yuppie' Wal-Mart in Plano TX that has a
Starbucks, doesn't sell guns or paint, has hardwood floors, employees wear sports jackets.

>In terms of the sheer size of cash donations, Wal-Mart Stores, the 
>nation's largest retailer, would be at the top of the list. The Arkansas 
>company gave some $197 million last year in cash ($188 million of it in 
>the U.S. alone). That puts Wal-Mart ahead of Bank of America, Johnson & 
>Johnson and Altria Group.

Most of that money went to local charities selected by employees or local civic leaders.
It didn't go to conservative causes. None of it went to churches. 

The Walton Family Foundation supports conservative causes, primarily voucher-based
ediucation, to the tune of $100M/yr. That's not the company, that's the family. When Helen
Walton dies, the Family Foundation will mushroom from $1B to $20B to become the world's
largest charity. 

>So... on the one hand The Company is allowed to give away stuff... no, 
>wait, it isn't really *giving*, The Company is generating tax 
…[4 more quoted lines elided]…
>the expense/bother/head-ache of *anyone* else'?

Retail stores frequently get requests for charity. They need an organized way to handle
those requests.

"92% of Americans think that it is important for companies to make charitable
contributions or donate products and/or services to nonprofit organizations in the
community."
http://www.sdgrantmakers.com/news_facts/corporate-giving.asp
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 36)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-10T13:32:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc3h1e$nun$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <fc1qeu$cu7$1@reader1.panix.com> <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com>`

```
In article <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sun, 9 Sep 2007 22:01:02 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[42 more quoted lines elided]…
>something in return.

Mr Wagner, I have no idea what happens to a word when you first use it 
without quotation marks and then respond with the same word 
quotes-enclosed.  A gift, by definition cited above, is free; what you are 
now labelling as 'business 'gifts'' (internal ' original') appears to be 
an example of 'quid pro quo'.  Please try to remember that - at least 
according to Lincoln - 'calling a tail a leg doesn't make it one'.

>
>>>Not only
…[10 more quoted lines elided]…
>your child's godparent, etc. 

If it were easy then everyone would already be doing it, Mr Wagner... and 
it has been argued that human beings cannot be impartial.

>
>>>The company
…[12 more quoted lines elided]…
>liberal.

In this use conservative means 'still providing charitable constibutions 
as it did for the last documentable tax-year'; my apologies for not being 
more specific.

[snip]

>>In terms of the sheer size of cash donations, Wal-Mart Stores, the 
>>nation's largest retailer, would be at the top of the list. The Arkansas 
…[6 more quoted lines elided]…
>It didn't go to conservative causes. None of it went to churches. 

Our habits seem to differ, Mr Wagner.  Just above I posted an assertion 
about WalMart's 'giving away free gifts' and followed it, immediately, 
with documentation from what might be called 'a commonly-accepted source'.  
You have just made an assertion about where the contributions went - as 
though that changes things, somehow - and have shown no documentation.

Is there something you might find to document your assertion or shall it 
be dismissed as readily as the rest of your argument?

>
>The Walton Family Foundation supports conservative causes, primarily
>voucher-based
>ediucation, to the tune of $100M/yr. That's not the company, that's the
>family.

See above, Mr Wagner... as per Forbes Magazine - that URL you snipped in 
another bit of uncomment editing - 'The *Arkansas company* (emphasis 
added) gave (etc)', not the Family Foundation.

[snip]

>>So... on the one hand The Company is allowed to give away stuff... no, 
>>wait, it isn't really *giving*, The Company is generating tax 
…[8 more quoted lines elided]…
>those requests.

*I* frequently get requests for charity, Mr Wagner; that does not make me 
the largest contributor in the way that WalMart has been shown to be.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 37)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-10T23:18:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r62ce3tj9qkdm09c3otc2d6q35gqg1gpoe@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <fc1qeu$cu7$1@reader1.panix.com> <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com> <fc3h1e$nun$1@reader1.panix.com>`

```
On Mon, 10 Sep 2007 13:32:30 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com>,
>Robert  <no@e.mail> wrote:

>>Business 'gifts' are not free, they carry an expectation of 
>>something in return.
…[6 more quoted lines elided]…
>according to Lincoln - 'calling a tail a leg doesn't make it one'.

Quotation marks are used to indicate that the writer realizes that a word is not being
used in its (currently) accepted sense.

    In the fifteenth century, we ï¿½knewï¿½ that the Sunï¿½s revolution divided day from night.
   
euphemism: the act or an example of substituting a mild, indirect, or vague term for one
considered harsh, blunt, or offensive [or illegal, unethical]

here's the opposite

dysphemism - an offensive or disparaging expression that is substituted for an inoffensive
one; "his favorite dysphemism was to ask for axle grease when he wanted butter"

>>>Granted it is an old source, from 2004... but 
>>>Walmart's culture is notoriously conservative

>>If conservative means resistant to change, the company is a flaming
>>liberal.
…[24 more quoted lines elided]…
>be dismissed as readily as the rest of your argument?

This document examines Wal-Mart philanthropy. Start on page 12.

http://reclaimdemocracy.org/walmart/walton_philanthropy.pdf

>>The Walton Family Foundation supports conservative causes, primarily
>>voucher-based
…[5 more quoted lines elided]…
>added) gave (etc)', not the Family Foundation.

Your citation, restored below, says nothing about conservative causes.
http://www.forbes.com/2005/11/11/charities-corporations-giving-cx_lm_1114charity.html

>>>So... on the one hand The Company is allowed to give away stuff... no, 
>>>wait, it isn't really *giving*, The Company is generating tax 
…[4 more quoted lines elided]…
>>>the expense/bother/head-ache of *anyone* else'?

Here is a list of Wal-Mart Foundation major contributions for 2005. Do you see any quid
pro quo on it? Do you see any right-wing groups?

$1 Million and Over
ï¿½ American Cancer Society
ï¿½ American Legion
ï¿½ American Red Cross
ï¿½ Boy Scouts
ï¿½ Boys & Girls Clubs
ï¿½ Bush-Clinton Katrina Fund
ï¿½ Childrenï¿½s Miracle Network
ï¿½ Girl Scouts
ï¿½ Laura Bush Library Foundation
ï¿½ Martin Luther King, Jr. Memorial
ï¿½ National Council of La Raza
ï¿½ National Fish and Wildlife Foundation
ï¿½ National Minority Supplier Development Council, Business Consortium Fund
ï¿½ Salvation Army
ï¿½ United Negro College Fund
ï¿½ United Way
ï¿½ Veterans of Foreign Wars Foundation

$500,000 - $999,999
ï¿½ American Heart Association
ï¿½ Big Brothers & Big Sisters
ï¿½ Give Kids the World
ï¿½ Speaking of Womenï¿½s Health
ï¿½ Special Olympics
ï¿½ Young Menï¿½s Christian Association

$100,000 - $499,999
ï¿½ American Diabetes Association
ï¿½ America Supports You
ï¿½ Cancer Research and Prevention Foundation
ï¿½ Close Up Foundation
ï¿½ Congressional Black Caucus Institute
ï¿½ Habitat for Humanity
ï¿½ Junior Achievement
ï¿½ Juvenile Diabetes Research Foundation
ï¿½ National Association for the Advancement of Colored People
ï¿½ National Center for Missing and Exploited Children
ï¿½ National Society to Prevent Blindness (Prevent Blindness America)
ï¿½ National Urban League
ï¿½ Students In Free Enterprise
ï¿½ Susan G. Komen Breast Cancer Foundation
ï¿½ Thurgood Marshall Scholarship Fund
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 38)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-11T09:40:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc5nq6$srk$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com> <fc3h1e$nun$1@reader1.panix.com> <r62ce3tj9qkdm09c3otc2d6q35gqg1gpoe@4ax.com>`

```
In article <r62ce3tj9qkdm09c3otc2d6q35gqg1gpoe@4ax.com>,
Robert  <no@e.mail> wrote:
>On Mon, 10 Sep 2007 13:32:30 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[15 more quoted lines elided]…
>used in its (currently) accepted sense.

Ahhhh... so it is your way of redefining a term when it is shown that 
accepted use demonstrates your conclusions invalid.  That must be a handy 
device.

>>>>Granted it is an old source, from 2004... but 
>>>>Walmart's culture is notoriously conservative
…[31 more quoted lines elided]…
>http://reclaimdemocracy.org/walmart/walton_philanthropy.pdf

Mr Wagner, I received a message from my Adobe plug-in of 'this document is 
damaged and can't be repaired'... but this page contains links to articles 
such as 'Wisconsin Seeks Back Taxes from Wal-Mart, Alleges Illegal Tax 
Evasion', 'Wal-Mart and the Corporate Media Mislead Public on Generic 
Drugs' and 'Review of Bank Leases Show Wal-Mart Executive Lied to FDIC'... 
these do not seem to support your previous assertions.

>
>>>The Walton Family Foundation supports conservative causes, primarily
…[8 more quoted lines elided]…
>Your citation, restored below, says nothing about conservative causes.

That might be due to my never having made claims about WalMart's 
charitable contributions and conservative clauses... funny, eh?

>http://www.forbes.com/2005/11/11/charities-corporations-giving-cx_lm_1114charity.html
>
…[10 more quoted lines elided]…
>pro quo on it? Do you see any right-wing groups?

I don't know what causes you to harp on conservative causes or right-wing 
groups, whatever those might be... but if there is no quid quo pro in it 
then The Company is, in your words, 'giving away free stuff', an activity 
which you claimed The Company prohibited Its employees.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 39)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-12T01:03:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s0vee31r2ddhakp78obr8r8jtobutdq1qq@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com> <fc3h1e$nun$1@reader1.panix.com> <r62ce3tj9qkdm09c3otc2d6q35gqg1gpoe@4ax.com> <fc5nq6$srk$1@reader1.panix.com>`

```
On Tue, 11 Sep 2007 09:40:22 +0000 (UTC), docdwarf@panix.com () wrote:

>Mr Wagner, I received a message from my Adobe plug-in of 'this document is 
>damaged and can't be repaired'... 

The .pdf isn't broken, it's copy protected. Evidently your reader got confused.

>but this page contains links to articles 
>such as 'Wisconsin Seeks Back Taxes from Wal-Mart, Alleges Illegal Tax 
>Evasion', 'Wal-Mart and the Corporate Media Mislead Public on Generic 
>Drugs' and 'Review of Bank Leases Show Wal-Mart Executive Lied to FDIC'... 
>these do not seem to support your previous assertions.

It's a Wal-Mart bashing site. The report they linked to was less biased.

>I don't know what causes you to harp on conservative causes or right-wing 
>groups, whatever those might be... but if there is no quid quo pro in it 
>then The Company is, in your words, 'giving away free stuff', an activity 
>which you claimed The Company prohibited Its employees.

Employees are permitted to give stuff away; they are not allowed to receive gifts.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 40)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-12T09:46:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc8chk$n93$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <r62ce3tj9qkdm09c3otc2d6q35gqg1gpoe@4ax.com> <fc5nq6$srk$1@reader1.panix.com> <s0vee31r2ddhakp78obr8r8jtobutdq1qq@4ax.com>`

```
In article <s0vee31r2ddhakp78obr8r8jtobutdq1qq@4ax.com>,
Robert  <no@e.mail> wrote:
>On Tue, 11 Sep 2007 09:40:22 +0000 (UTC), docdwarf@panix.com () wrote:

[snip]

>>I don't know what causes you to harp on conservative causes or right-wing 
>>groups, whatever those might be... but if there is no quid quo pro in it 
…[4 more quoted lines elided]…
>receive gifts. 

This seems to contradict your assertion that 'you can't even accept a 
lunch paid for by another employee'; the 'other employee', in the act of 
giving, is employing a practise reserved by The Company.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 38)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-09-11T08:20:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TYudnSdxK_g_OXvbnZ2dnUVZ_gadnZ2d@comcast.com>`
- **In-Reply-To:** `<r62ce3tj9qkdm09c3otc2d6q35gqg1gpoe@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <fc1qeu$cu7$1@reader1.panix.com> <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com> <fc3h1e$nun$1@reader1.panix.com> <r62ce3tj9qkdm09c3otc2d6q35gqg1gpoe@4ax.com>`

```
Robert wrote:
> 
> Here is a list of Wal-Mart Foundation major contributions for 2005. Do you see any quid
…[3 more quoted lines elided]…
> ï¿½ National Council of La Raza

You've got to be kidding me...  :(  That sucks.

For those not in the US of A, La Raza is Spanish for "the Race", and is 
dedicated to reclaiming the land that was won by the US in the 
Mexican-American War.  Some of that land just happens to be where I 
currently reside.  They're opposed to *any* immigration enforcement, as 
streaming illegal aliens across our border is an easy way to amass an 
army within our own borders.  Left-wingers cry "human rights" (as if 
being in this country is some sort of inalienable human right) and 
unscrupulous businesses (mostly right-wingers) turn a blind eye because 
they like the cheap labor (for illegal workers, minimum wage laws don't 
apply).

Of course, with Wal-Mart's desire to "buy American whenever possible," 
it makes sense - but it doesn't mean I have to like it.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 36)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-10T11:01:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10uae35dr7r3t7a1pvlg761er0u6tfc517@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <fc1qeu$cu7$1@reader1.panix.com> <fka9e31lr85b7fnq9q5m48412ncbs3q3kp@4ax.com>`

```
On Sun, 09 Sep 2007 22:42:36 -0500, Robert <no@e.mail> wrote:

>
>Business 'gifts' are not free, they carry an expectation of something in return.

It's amazing how many conservative bankers have country club
membership paid for by their banks - and they figure it's a good
investment, as it's a great place to persuade clients to work with
them.

Sure, they can't take home a round of golf, but the quality of the
golf club has nothing to do with the interest rate received.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 35)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-11T04:06:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189508789.318352.284880@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<fc1qeu$cu7$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <fc1qeu$cu7$1@reader1.panix.com>`

```

docdw...@panix.com () wrote:
>  From
> <http://www.forbes.com/2005/11/11/charities-corporations-giving-cx_lm_1114charity.html>
…[17 more quoted lines elided]…
>

I once worked for a client company which was frequently asked for
donations by a large UK-based retail company which then trumpeted
loudly about how much it gave to charity (without mentioning the fact
that it was the supplier who trumped up the cash).
> So... on the one hand The Company is allowed to give away stuff... no,
> wait, it isn't really *giving*, The Company is generating tax
…[16 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 34)_

- **From:** donald tees <donaldtees@execulink.com>
- **Date:** 2007-09-10T00:31:19-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d7ydnWpyIewHVXnbnZ2dnUVZ_oOnnZ2d@golden.net>`
- **In-Reply-To:** `<d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>`

```
Robert wrote:
> On Sun, 9 Sep 2007 18:01:41 +0000 (UTC), docdwarf@panix.com () wrote:
> 
…[34 more quoted lines elided]…
> nor lie about anything. 

Bullshit.  Here in Canada, they have repeatedly broken the labour laws 
by closing stores that attempted to unionize, for example. I do not know 
about you, but *I* consider breaking the law as reneging on a deal. 
When you start a business in a country, and when you hire people, you 
are tacitly agreeing to abide by the law as of that country. Their 
approach to all laws, including labour laws and zoning laws, seems to be 
that if you submit a bribe high enough, it is quite all right to break them.

Donald
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 35)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-09-10T12:27:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6LaFi.6629$JD.627@newssvr21.news.prodigy.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <d7ydnWpyIewHVXnbnZ2dnUVZ_oOnnZ2d@golden.net>`

```
"donald tees" <donaldtees@execulink.com> wrote in message 
news:d7ydnWpyIewHVXnbnZ2dnUVZ_oOnnZ2d@golden.net...

>> Wal-Mart is very ethical. They drive a hard bargain on cost, but never 
>> renege on a promise
…[3 more quoted lines elided]…
> closing stores that attempted to unionize, for example.

Here is Wisconsin our esteemed legislature and other politicians are up in a 
snit about Walmart not paying its "fair share" of Wisconsin taxes.

And why?  Because the people at Wal-mart organized their local businesses to 
use the advantages the same legislature wrote into our tax laws.... that is, 
everything they have done is perfectly legal.

When you are the biggest, you are the biggest target. For everything.

MCM
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 35)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-10T21:23:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mkrbe3lm2o3b5vmaldlpa07conbtoqc7cf@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <d7ydnWpyIewHVXnbnZ2dnUVZ_oOnnZ2d@golden.net>`

```
On Mon, 10 Sep 2007 00:31:19 -0400, donald tees <donaldtees@execulink.com> wrote:

>Robert wrote:
>> On Sun, 9 Sep 2007 18:01:41 +0000 (UTC), docdwarf@panix.com () wrote:
…[38 more quoted lines elided]…
>by closing stores that attempted to unionize, for example.

You exaggerate. They closed ONE store, in Jonquiere, in 2005.

>I do not know 
>about you, but *I* consider breaking the law as reneging on a deal. 

There is no law against closing a store in Quebec, even if the purpose of the closure is
union busting.

>When you start a business in a country, and when you hire people, you 
>are tacitly agreeing to abide by the law as of that country. Their 
>approach to all laws, including labour laws and zoning laws, seems to be 
>that if you submit a bribe high enough, it is quite all right to break them.

Instead of making up baseless charges, vote with your wallet. Whole countries have gotten
rid of them -- South Korea, Singapore, soon Germany.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 34)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-10T11:57:58-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HIeFi.15942$Y7.5837@bignews3.bellsouth.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com>`

```
"Robert" <no@e.mail> wrote:
>
> Wal-Mart is very ethical. They drive a hard bargain on cost, but never
> renege on a promise nor lie about anything.

That may have been true at one time, but it isn't true now. Wal-Mart has
apparently gone as far as they can go in reducing costs, and now has
begun to use deceptive marketing. For example: Slightly reducing the
amount of product (to give the impression it is the same as always) and
keeping the price the same. Increasing the price, but removing the price
tags so customers hopefully won't notice. Reducing quality. Take their
Equate brand, for example. If you used to see a brand name product
and an equate copy beside it, you could expect the Equate product to
have just as much product inside as the brand name. Just check several
different products in your local Wal-Mart these days and you will find
the Equate products are often a few ounces less than the "equal" brand
name. If you've paid attention over time, you will notice missing price
tags much more often than in the past. I shop at Wal-mart (several) all
the time, and have done so for years. But I've been seeing these and
other deceptive practices for a number of months now. While these
practices may not be technically "lying," they are certainly meant to
deceive the customer, which is dishonest and unethical. Wal-Mart isn't
the only company doing this, of course. Most have done it for a long
time.

One of my pet peeves is that companies are usually run by accountants
rather than by people whose heart is for the products and services the
company provides. This concentration on profit alone, at any cost, will
inevitably result in a company losing whatever qualities made them
great. It's starting to happen at Wal-Mart right now. A good example
is Hewlett-Packard, started in the 1930's by electrical engineers Bill
Hewlett and Dave Packard. They had a passion for quality, and HP
used to make some of the finest equipment you could buy. But after
they retired, and HP was run by the bean counters, the company began
to degenerate, and now HP stuff is no better than average. We all suffer
loss when this happens. There is no place I can go now, to buy a
calculator rugged enough to bang against the wall and it still work.
Profit is necessary. But there are other priorities, often more important,
than continually increasing profits. You can only increase efficiency so
much, and beyond that, quality will inevitably suffer, if increased profit
is always the overriding priority.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 35)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-10T23:53:02-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net>`

```
On Mon, 10 Sep 2007 11:57:58 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>"Robert" <no@e.mail> wrote:
>>
>> Wal-Mart is very ethical. They drive a hard bargain on cost, but never
>> renege on a promise nor lie about anything.

> If you've paid attention over time, you will notice missing price
>tags much more often than in the past. I shop at Wal-mart (several) all
…[5 more quoted lines elided]…
>time.

Keeping shelf tags correct is a major problem for every retailer. A supermarket company
where I worked sent a new shelf tag to its stores every time there was a change. They were
printed in the store. We got lots of complaints about wrong prices i.e. the shelf tag
doesn't maatch the scanner price. I'd go to the store and find six months of shelf tags
piled up on the manager's desk. When asked why they didn't hang them, they said they
didn't have time. 

The home office started sending auditors to spot check tags. If they found more than 1%
wrong, we would 're-tag the store', meaning send a complete set, typically 20,000. Hanging
them took a lot of labor. 

Another reason they disagree, to the customer's favor, involves special sale prices. 
Suppose the company offers private label coffee for $2 off. Someone in the store or buying
office screws up, doesn't order enough extra coffee shipped to the store. Customers are
irate, accuse is of bait and switch. To make them happy, the store manager goes into the
POS and lowers the price of Folgers by $2. When the sale goes off, the home office raises
the private label coffee to regular, but doesn't know about the Folger's change. The store
manager forgets to change it back. For the next several months, until there's a price
change on Folgers, we're selling it for $2 off. 

I used to pull back price files and compare them to correct prices. It was common to find
50-100 items that were wrong. I went to reloading price files once a month to get rid of
the errors. 

What we wanted were electronic shelf tags. There have been many experiments; it's too
expensive. An interesting alternative is running now in a ShopRite in Parsippany, NJ (a
store I used to shop at). They have an computer equipped with scanner and RF link in the
shopping cart. Customers can scan their own stuff to see how much it is. The computer can
also read RFID, but there isn't enough of that on the shelf yet (it's used on cases and
pallets). 

>One of my pet peeves is that companies are usually run by accountants
>rather than by people whose heart is for the products and services the
…[13 more quoted lines elided]…
>is always the overriding priority.

Companies don't make the rules, they just play the game. Look at the customers in a
Wal-Mart and ask why they are there. The answer is price. Read financial publications.
They talk about sales and earnings, not quality. The game has one rule: it's all about
money. 

The HP Instruments Division was spun off to Agilent.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 36)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2007-09-11T08:22:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<IEwFi.82736$pu2.50505@bignews1.bellsouth.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net> <do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com>`

```
"Robert" <no@e.mail> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>>"Robert" <no@e.mail> wrote:
…[42 more quoted lines elided]…
> pallets).

Would these things not have been just as true, say one year, or three years ago?
As I clearly stated, it is the significant increase in missing price tags over the last
several months that bothers me.

>>One of my pet peeves is that companies are usually run by accountants
>>rather than by people whose heart is for the products and services the
…[18 more quoted lines elided]…
> money.

I agree that Wal-Mart's primary appeal is low prices. I don't quibble about
the methods they use to get lower prices, my complaint is when they start
intentionally deceiving their customers. But not every company's reason for
existence is low prices. Sometimes it's high quality products, or very good
service. My point is that putting increased profits ahead of everything else
will eventually inevitably destroy whatever made that company great. When
Wal-Mart begins to deceive their customers, they are essentially cheating
them, which negates what people go to Wal-Mart for in the first place. Once
customers realize that, in reality, they are no longer getting the "good deal"
they used to get at Wal-Mart, they will move elsewhere. When people buy
from a company to get high quality, and quality is sacrificed on the altar of
ever increasing profits, people will move elsewhere. And so on. It leads to
inevitable financial death, or at best mediocrity, for that company, long term.

If a company had the long term commitment to stick to whatever made them
great, when they hit the point of diminishing returns in seeking continually
increasing profits, they would stay their course, and continue to deliver what
their customers came to them for in the first place. That's the only way I can
see of anybody ever making a difference, as unlikely as it is. As long as
everybody says "There's no way to fix it" then it won't get fixed, whether it
could be fixed or not.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 37)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-12T01:19:20-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net> <do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com> <IEwFi.82736$pu2.50505@bignews1.bellsouth.net>`

```
On Tue, 11 Sep 2007 08:22:30 -0500, "Judson McClendon" <judmc@sunvaley0.com> wrote:


>I agree that Wal-Mart's primary appeal is low prices. I don't quibble about
>the methods they use to get lower prices, my complaint is when they start
>intentionally deceiving their customers

My quibble is that they have the means and opportunity to do world-class IT, but they're
blowing it because they lack vision and leadership. Resistance to change isn't coming from
programmers, as is usually the case, it's coming from IT management. There is a huge pool
of programming talent in Bentonville. It is used for production support rather than
development.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 38)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-12T23:26:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kq0nsF4h563U1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net> <do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com> <IEwFi.82736$pu2.50505@bignews1.bellsouth.net> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com...
> On Tue, 11 Sep 2007 08:22:30 -0500, "Judson McClendon" 
> <judmc@sunvaley0.com> wrote:
…[9 more quoted lines elided]…
> blowing it because they lack vision and leadership.

Why would they consider they need to do "world-class IT"? They're not in the 
IT business.

Is it really fair to say that, Robert, if you didn't make any attempt to 
change it?


> Resistance to change isn't coming from
> programmers, as is usually the case, it's coming from IT management. There 
…[3 more quoted lines elided]…
> development.

Maybe they employ programmers to support production? Development may be much 
less of a priority for them.

So what would you do about it? Did you talk to any senior managers or make a 
case?

I understand that you probably wouldn't if you were employed as a contract 
programmer, and don't hold that against you, nevertheless, it wouldn't stop 
me from preparing some notes and copying them to my Boss and up the line. If 
no-one suggests need for change they're going to continue as they are.

Maybe they need an IT Health Check with some independent views, looking at 
what they do and how it could be improved, and maybe even suggesting avenues 
where they could get some quick wins... Having worked in the organisation 
and with your application knowledge of that kind of Business, maybe you 
could give them a proposal...?

Pete.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 39)_

- **From:** Richard <riplin@Azonic.co.nz>
- **Date:** 2007-09-12T12:01:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189623687.314201.240160@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5kq0nsF4h563U1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net> <do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com> <IEwFi.82736$pu2.50505@bignews1.bellsouth.net> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com> <5kq0nsF4h563U1@mid.individual.net>`

```
On Sep 12, 11:26 pm, "Pete Dashwood"
<dashw...@removethis.enternet.co.nz> wrote:
> "Robert" <n...@e.mail> wrote in message
>
…[42 more quoted lines elided]…
> could give them a proposal...?

Maybe he did, but his "you're blowing it because you lack vision and
leadership" probably didn't go down too well with the leaders, which
may be why he isn't there any more.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 40)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-13T12:26:18+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kredbF4enj4U1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net> <do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com> <IEwFi.82736$pu2.50505@bignews1.bellsouth.net> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com> <5kq0nsF4h563U1@mid.individual.net> <1189623687.314201.240160@22g2000hsm.googlegroups.com>`

```


"Richard" <riplin@Azonic.co.nz> wrote in message 
news:1189623687.314201.240160@22g2000hsm.googlegroups.com...
> On Sep 12, 11:26 pm, "Pete Dashwood"
> <dashw...@removethis.enternet.co.nz> wrote:
…[60 more quoted lines elided]…
>

:-)

Possibly...:-)

Robert tends to be about as subtle as an air raid; that doesn't gain 
Management support.

Pete.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 39)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-12T23:29:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net> <do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com> <IEwFi.82736$pu2.50505@bignews1.bellsouth.net> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com> <5kq0nsF4h563U1@mid.individual.net>`

```
On Wed, 12 Sep 2007 23:26:49 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>"Robert" <no@e.mail> wrote in message 
>news:fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com...
…[14 more quoted lines elided]…
>IT business.

Why does their Web page http://walmartstores.com/GlobalWMStoresWeb/navigate.do?catg=283
say they are? "Wal-Mart leads the retail industry ", "Do you crave the excitement of
working on the latest technology? Do you want to push the envelope, influencing technology
innovation in retail and even throughout the world? How would you like to make a
multi-operational impact your first day whether you have been coding 20 years or 2
months?" "The mission of the Wal-Mart Information Systems Division is to help make our
Business Customers the most efficient and effective in the World." "did you know Wal-Mart
has the largest civilian database? Yes, Wal-Mart! D id you know Wal-Mart has consistently
been ranked as one of the top places to work in the Information Systems Industry? Yes,
Wal-Mart! You probably didn't know we drive many of the largest technology suppliers
businesses with our input concerning the technology they create! Yes, Wal-Mart!"

It's all bullshit. 

>Is it really fair to say that, Robert, if you didn't make any attempt to 
>change it?

<laugh> I worked in Change Control.  There wasn't much change to control because they
hadn't recompiled a back office program in ten years."

>> Resistance to change isn't coming from
>> programmers, as is usually the case, it's coming from IT management. There 
…[6 more quoted lines elided]…
>less of a priority for them.

Right. Development SHOULD be a priority because their stores really are leading the retail
industry. Did you know Wal-Mart is the largest supermarket in the US? It sells more food
than Kroger, Safeway and Albertsons, the next three, COMBINED> 

>So what would you do about it? Did you talk to any senior managers or make a 
>case?

I finished my project and left after it was done, in 3 months. I could have stayed another
6 months doing little. They had the budget money.

>I understand that you probably wouldn't if you were employed as a contract 
>programmer, and don't hold that against you, nevertheless, it wouldn't stop 
>me from preparing some notes and copying them to my Boss and up the line. If 
>no-one suggests need for change they're going to continue as they are.

>Maybe they need an IT Health Check with some independent views, looking at 
>what they do and how it could be improved, and maybe even suggesting avenues 
>where they could get some quick wins... Having worked in the organisation 
>and with your application knowledge of that kind of Business, maybe you 
>could give them a proposal...?

They get propositions like that every week, from big polished companies like IBM, HP and
Accenture. 

There are some flashes of light. The in-house deveoped change control system, called
Power, is better than any other I've seen, with the possible exception of Subversion. One
individual made a difference in that case.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 40)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2007-09-13T21:09:07-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13ejnoadsdh2vfc@corp.supernews.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <4m88e358gvb7vhupj43dsl4fap4o5jprui@4ax.com> <fc1ce4$bmp$1@reader1.panix.com> <d6m8e3likresf0so7e5504kr72d3n4t1rm@4ax.com> <HIeFi.15942$Y7.5837@bignews3.bellsouth.net> <do5ce3hkij4i7cd60552kuvp01i6quacho@4ax.com> <IEwFi.82736$pu2.50505@bignews1.bellsouth.net> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com> <5kq0nsF4h563U1@mid.individual.net> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com...

<sniP>

> Why does their Web page 
> http://walmartstores.com/GlobalWMStoresWeb/navigate.do?catg=283
…[22 more quoted lines elided]…
>

I wondered where you got your inexhaustable supply ;-)

<snip>
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 40)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-14T09:31:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcdkef$4os$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com> <5kq0nsF4h563U1@mid.individual.net> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com>`

```
In article <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>Why does their Web page
>http://walmartstores.com/GlobalWMStoresWeb/navigate.do?catg=283
>say they are?

It says that they are because someone wrote it that way and it got 
approved for use, Mr Wagner; this may have little to do with anything else 
within the organisation.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 41)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-15T00:03:21+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kvbkaF5ona9U1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com> <5kq0nsF4h563U1@mid.individual.net> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fcdkef$4os$1@reader1.panix.com...
> In article <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com>,
> Robert  <no@e.mail> wrote:
…[11 more quoted lines elided]…
> DD

Hey, hang on a minute, Doc.

You're not seriously suggesting that things written on Web Pages could be 
(shudder...) ... untrue?!

If this idea was to get about, it could seriously damage the upcoming launch 
of a new website I have invested hundreds of hours in...

Can we just maintain the illusion of Gospel on the Web for a few more 
month's, please?

Next you'll be saying their ain't no Sanity Clause...

Pete.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 42)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-14T13:31:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fce2en$g9e$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com> <5kvbkaF5ona9U1@mid.individual.net>`

```
In article <5kvbkaF5ona9U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[17 more quoted lines elided]…
>(shudder...) ... untrue?!

Not at all, Mr Dashwood.  I'm suggesting that something exists on this 
particular web-page for the reasons stated - and I might be wrong on that, 
of course - and doing my usual best to avoid sticky concepts such as 
'true' versus 'True' versus 'Truth'.  Anyone familiar with a Latin version 
of the New Testament and some Brit-slang would be aware that the Pound 
Sterling is Truth... if one turns a question (John.XVIII:38) into an 
assertion.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 41)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-14T19:28:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <fa0fe3tbqqbf2eb5egt29422be23b5e0so@4ax.com> <5kq0nsF4h563U1@mid.individual.net> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com>`

```
On Fri, 14 Sep 2007 09:31:59 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com>,
>Robert  <no@e.mail> wrote:
…[9 more quoted lines elided]…
>within the organisation.

The page isn't pushing programmer buttons, it's pushing top management buttons. The page
is a litany of what's politically correct within the company.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 42)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-15T12:25:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcgj04$hd3$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com>`

```
In article <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com>,
Robert  <no@e.mail> wrote:
>On Fri, 14 Sep 2007 09:31:59 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[15 more quoted lines elided]…
>is a litany of what's politically correct within the company.

I'm not sure about this 'politically correct' nonsense, Mr Wagner, but I 
*would* say that the page might reflect less about 'de rereum natura' and 
more about 'how we like to think of ourselves.

If that is a re-statement of your words then you already knew the answer 
to the question you asked... was there any particularly good reason for 
asking a question to which you already knew the answer?

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 43)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-15T09:17:07-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com>`

```
On Sat, 15 Sep 2007 12:25:41 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com>,
>Robert  <no@e.mail> wrote:
…[25 more quoted lines elided]…
>asking a question to which you already knew the answer?

There are at least two reasons to ask for the others' explnation. First, it's polite.
Second, if they don't have one, yours wins by default.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 44)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-15T17:46:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fch5q7$qfg$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com> <i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com>`

```
In article <i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sat, 15 Sep 2007 12:25:41 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[30 more quoted lines elided]…
>it's polite.

I did not realise this motivation figured so strongly into your 
interactions, Mr Wagner... learn something new every day.

>Second, if they don't have one, yours wins by default.

Ahhhhh, the old '*any* explanation - even a bad one - is superior to no 
explanation' argument.  I've seen it before... and ranks right up there 
with 'it is better to have the first answer than to have the first correct 
answer'.

DD
```

###### ↳ ↳ ↳ No reply, means NO TEPLY (was: Can IT deal with change? was:

_(reply depth: 44)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-16T05:45:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pq3Hi.517$1o1.498@fe12.news.easynews.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com> <i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com...
> On Sat, 15 Sep 2007 12:25:41 +0000 (UTC), docdwarf@panix.com () wrote:
>
<snip>

> There are at least two reasons to ask for the others' explnation. First, it's 
> polite.
> Second, if they don't have one, yours wins by default.
>

Robert,
  You may have your own personal opinion that,

    "if they don't have one, yours wins by default."

Furthermore, you may even live your life as if this were generally (or even 
universally true).

HOWEVER, I don't personally think that is a generally (much less generally in 
CLC) accepted reasoning.

Often (n my perception and understanding) when one asks for another person's 
"explanation" and no reply (or explanation) is given, this means:

1) The person asked never saw the request (for either electronic or personal 
reasons)
        or
2) The person asked did not think any further explanation was needed (often 
believing - correctly or not - that the original "statement" stood on its own)
        or
3) That the person asked doesn't think that the request was sincere and/or worth 
a reply.
```

###### ↳ ↳ ↳ Re: No reply, means NO REPLY (was: Can IT deal with change? was:

_(reply depth: 45)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-16T16:49:46-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ls8re3pjfnig83eq6jba8blcc2umupk8cs@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com> <i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com> <pq3Hi.517$1o1.498@fe12.news.easynews.com>`

```
On Sun, 16 Sep 2007 05:45:57 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>
>"Robert" <no@e.mail> wrote in message 
…[31 more quoted lines elided]…
>a reply.

The reason for no reply doesn't show up in the archive, nor do the social dynamics. The
only things that appear are the words posted.
```

###### ↳ ↳ ↳ Re: No reply, means NO REPLY (was: Can IT deal with change? was:

_(reply depth: 46)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-17T02:08:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dklHi.181060$M%1.61645@fe10.news.easynews.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com> <i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com> <pq3Hi.517$1o1.498@fe12.news.easynews.com> <ls8re3pjfnig83eq6jba8blcc2umupk8cs@4ax.com>`

```

"Robert" <no@e.mail> wrote in message 
news:ls8re3pjfnig83eq6jba8blcc2umupk8cs@4ax.com...
> On Sun, 16 Sep 2007 05:45:57 GMT, "William M. Klein" 
> <wmklein@nospam.netcom.com> wrote:
…[40 more quoted lines elided]…
> only things that appear are the words posted.

I agree with you 100% on this.  However, my point is what you can (or should in 
my opinion) take away from "zero words posted" is that you can SAFELY conclude 
absolutely NOTHING about what those zero words mean.  (Not that they mean they 
"accept" your post, that they reject your post, that your post was even read.)
```

###### ↳ ↳ ↳ Re: No reply, means NO REPLY (was: Can IT deal with change? was:

_(reply depth: 46)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-17T09:37:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fclhtd$db$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <i5qne3d082u6lgmpfe55s7it8st8nraq9g@4ax.com> <pq3Hi.517$1o1.498@fe12.news.easynews.com> <ls8re3pjfnig83eq6jba8blcc2umupk8cs@4ax.com>`

```
In article <ls8re3pjfnig83eq6jba8blcc2umupk8cs@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>The reason for no reply doesn't show up in the archive, nor do the
>social dynamics. The
>only things that appear are the words posted. 

Some say, Mr Wagner, that absence of evidence is not evidence of absence.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 43)_

- **From:** donald tees <donaldtees@execulink.com>
- **Date:** 2007-09-15T19:06:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3M2dnakFVeb1-HHbnZ2dnUVZ_hGdnZ2d@golden.net>`
- **In-Reply-To:** `<fcgj04$hd3$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <4kdhe3tm1odip9ree7tsbvaklhcpcskju5@4ax.com> <fcdkef$4os$1@reader1.panix.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com>,
> Robert  <no@e.mail> wrote:
…[26 more quoted lines elided]…
> 
I doubt any firm the size of Walmart gets technical staff to write web 
page text. I'd be extremely surprised if they do not have an advertising 
department to do such things.

I have yet to read ad copy that has much credence in the tech world. 
 From any large firm.

Donald
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 44)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-16T00:34:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fchtmu$4b1$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com> <3M2dnakFVeb1-HHbnZ2dnUVZ_hGdnZ2d@golden.net>`

```
In article <3M2dnakFVeb1-HHbnZ2dnUVZ_hGdnZ2d@golden.net>,
donald tees  <donaldtees@execulink.com> wrote:

[snip]

>I doubt any firm the size of Walmart gets technical staff to write web 
>page text. I'd be extremely surprised if they do not have an advertising 
>department to do such things.

What's this, Mr Tees... will you next be saying that 'Personnel 
departments don't know from a hole in the ground about technical 
requirements; one might see, say, an advertisement asking for six years' 
worth of experience in a technology only four years old'?  Utterly 
shocking!

>I have yet to read ad copy that has much credence in the tech world. 
> From any large firm.

I don't read much in the way of ad copy from *any* firm, Mr Tees, because 
it is... well, because it is advertising.  I'll do my best to garner a bit 
of information from the gibberings ('Bumfco announces a revolution in 
modern paradigms by revealing to the world, for the first time, its new, 
improved, chromium-plated, back-planed, double-reversed, titanium-shielded 
widget!' = 'Bumfco may, at some point, be getting a new widget to 
market... titanium might be involved') and go off to do my own research.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 45)_

- **From:** donald tees <donaldtees@execulink.com>
- **Date:** 2007-09-19T09:58:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rI-dnXgt3YJlt2zbnZ2dnUVZ_j6dnZ2d@golden.net>`
- **In-Reply-To:** `<fchtmu$4b1$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <vh9me3d3ggimko2rgp61o88r65p0on5i7h@4ax.com> <fcgj04$hd3$1@reader1.panix.com> <3M2dnakFVeb1-HHbnZ2dnUVZ_hGdnZ2d@golden.net> <fchtmu$4b1$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <3M2dnakFVeb1-HHbnZ2dnUVZ_hGdnZ2d@golden.net>,
> donald tees  <donaldtees@execulink.com> wrote:
…[12 more quoted lines elided]…
> 

I think you are getting the idea, Doc.

>> I have yet to read ad copy that has much credence in the tech world. 
>> From any large firm.
…[8 more quoted lines elided]…
> 

Sounds about the way I read ad stuff on the net too.

Donald
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 31)_

- **From:** L Pruitt <LMPruitt@gmail.com>
- **Date:** 2007-09-10T15:05:11
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189436711.709784.274850@w3g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<fc15s0$bjt$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com>`

```
On Sep 9, 10:09 am, docdw...@panix.com () wrote:
> In article <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34...@4ax.com>,
>
…[42 more quoted lines elided]…
> DD

I got into it a few months back on a consulting gig when I mentioned
to the 'paperwork happy' junior manager that since he was paying Sr.
programmers at a pay rate of $50/hr (thru a contracting firm, so let's
go with $80 billable), but having them spend 30 minutes a day
'recreating data' for a spreadsheet that tracked information that was
already in other spreadsheets that he was requiring them to fill out
daily... (it was Excel-happy-land) given that there were 16 coders on
the project, he was billing a solid 8-hour man-day at Sr. programmer
*consulting agency* rates - for something an entry-level secretary/
admin could do for $12/hr...
$400/day vs. $96/day...
He grumbled something about 'that would mean having to find someone
and hire them and train them how to do it' and decided to leave things
as they were.
The coders took to calling the spreadsheets in question TPS reports -
in honor of Office Space - and he still managed to remain oblivious.

Cost-effective seems to be a phrase that is lost on middle management.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 32)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-10T12:38:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<820be3hu3fst1bp25rgm6v7vmlffer3i5c@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <1189436711.709784.274850@w3g2000hsg.googlegroups.com>`

```
On Mon, 10 Sep 2007 15:05:11 -0000, L Pruitt <LMPruitt@gmail.com> wrote:

>On Sep 9, 10:09 am, docdw...@panix.com () wrote:
>> In article <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34...@4ax.com>,
…[60 more quoted lines elided]…
>in honor of Office Space - and he still managed to remain oblivious.

They call themselves PROGRAMmers. Why didn't they write a PROGRAM that copies numbers from
one spreadsheet to the other. It can be done 100% in SQL, in a macro written in VB, or in
an OLE program written in any language, including Cobol.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 32)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-10T18:51:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc43mn$mle$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <bhh7e3l68s7f2p2tnjlfi7dh4cd5o34ega@4ax.com> <fc15s0$bjt$1@reader1.panix.com> <1189436711.709784.274850@w3g2000hsg.googlegroups.com>`

```
In article <1189436711.709784.274850@w3g2000hsg.googlegroups.com>,
L Pruitt  <LMPruitt@gmail.com> wrote:
>On Sep 9, 10:09 am, docdw...@panix.com () wrote:

[snip]

>> In that part of the world I'd also guess that a maintenance worker,
>> dedicated *solely* to emptying and carting trash - and I have never seen a
…[7 more quoted lines elided]…
>> Going On Here.

[snip - pardon my midsentence interruption but I don't think I've changed 
context all that much]

>... given that there were 16 coders on
>the project, he was billing a solid 8-hour man-day at Sr. programmer
…[5 more quoted lines elided]…
>as they were.

I recall reading, somehere, that replacement costs for a given employee 
amount to three or four months of salary... so, for the sake of an 
argument, take the high figure and cut it in half.  (since it is a new 
position there are no 'replacement costs', per se, and no time lost from 
having someone who knows the position not in that position).

Assuming zero productivity for the first two months at US$96/hr the result 
would be an expense of (22.5 days/mo * US$96/day * 2 mo =) US$4,320.

Assuming 100% productivity following the first two months then the 
resulting savings of US$304/day would pay for this investment in less than 
fifteen business days... call it three calendar weeks.  Not a bad ROI, or 
so I would say... then again, I'm not a manager.

>The coders took to calling the spreadsheets in question TPS reports -
>in honor of Office Space - and he still managed to remain oblivious.

Life imitates Art imitates Life imitates Art.

>Cost-effective seems to be a phrase that is lost on middle management.

Yes... and no.  Having a responsibility for a larger budget usually 
equates to having greater status in the organisation, among other things.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 29)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-09-09T08:35:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GFSEi.3521$7P7.3289@newssvr19.news.prodigy.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com> <9WFEi.2590$3Y1.2232@newssvr17.news.prodigy.net> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com>`

```
<docdwarf@panix.com> wrote in message news:fc0dhp$dgl$1@reader1.panix.com...
>  what good is earning even high  los [sic] rates when you can't spend any 
> of it?

That, sir, is a topic unto itself.

Money becomes an indicator or scorecard of success - and by inference 
excellence - even if not spent.

You'll find this particular attitude particularly among commissioned 
salesmen, although it does pop up in every profession.

MCM
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-09T16:14:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc165j$cfo$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com> <GFSEi.3521$7P7.3289@newssvr19.news.prodigy.net>`

```
In article <GFSEi.3521$7P7.3289@newssvr19.news.prodigy.net>,
Michael Mattias <mmattias@talsystems.com> wrote:
><docdwarf@panix.com> wrote in message news:fc0dhp$dgl$1@reader1.panix.com...
>>  what good is earning even high  los [sic] rates when you can't spend any 
>> of it?
>
>That, sir, is a topic unto itself.

I think it was first voiced by a Hollywood star (back in the days when the 
studios *really* ran every aspect of their lives) who was forbidden to go 
out to those notorious Hollywood Parties... or nightclubs... or just about 
anywhere, due to her Good Woman image.

>
>Money becomes an indicator or scorecard of success - and by inference 
>excellence - even if not spent.

To some folks, sure... 'I just use it to keep track' is something I've 
heard/read many times.  When asked 'keep track of what?' the best answer I 
received was 'Why... to keep track of how much money I've made!'

As for myself, the cash is not the end... what I can do with the cash, 
like... afford the rent, keep the lights on, have something in the 
refrigerator besides a half-empty bottle of green maraschino cherries and 
some Laughing Cow cheese-bits... *that* is what pleases me.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 31)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-10T11:03:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5uae3tr8v7je1ndt73edhovnifta7pjkn@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com> <GFSEi.3521$7P7.3289@newssvr19.news.prodigy.net> <fc165j$cfo$1@reader1.panix.com>`

```
On Sun, 9 Sep 2007 16:14:43 +0000 (UTC), docdwarf@panix.com () wrote:

>I think it was first voiced by a Hollywood star (back in the days when the 
>studios *really* ran every aspect of their lives) who was forbidden to go 
>out to those notorious Hollywood Parties... or nightclubs... or just about 
>anywhere, due to her Good Woman image.

Currently pro sports seems to be on the leading edge here.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 29)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-09-10T17:53:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46E58494.6F0F.0085.0@efirstbank.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <9vn5e3d42u373okf99an1fuevnt471qjf2@4ax.com> <9WFEi.2590$3Y1.2232@newssvr17.news.prodigy.net> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com>`

```
>>> On 9/9/2007 at 3:14 AM, in message <fc0dhp$dgl$1@reader1.panix.com>,
<docdwarf@panix.com> wrote:
> In article <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com>,
> 
…[13 more quoted lines elided]…
> los rates when you can't spend any of it?

Are you referring to Sam Walton or L. Ron Hubbard?

:-)
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 30)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-11T00:11:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc4mg9$2a3$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com> <fc0dhp$dgl$1@reader1.panix.com> <46E58494.6F0F.0085.0@efirstbank.com>`

```
In article <46E58494.6F0F.0085.0@efirstbank.com>,
Frank Swarbrick <Frank.Swarbrick@efirstbank.com> wrote:
>>>> On 9/9/2007 at 3:14 AM, in message <fc0dhp$dgl$1@reader1.panix.com>,
><docdwarf@panix.com> wrote:
>> In article <8am6e31nb91ghn726orsn2erou0j1vcj6p@4ax.com>,

[snip]

>> there was then talk about how one could not live a 
>> Fancy Life, that one's dewllings and doings had to fit into the 
…[3 more quoted lines elided]…
>Are you referring to Sam Walton or L. Ron Hubbard?

You must be joking... one of those was a raving, paranoic, micro-managing 
control-freak who sought to amass wealth beyond the dreams of avarice...

... the other managed to do it.  Perhaps that doesn't answer your question 
but... I know They are watching.

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 25)_

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-09-10T16:52:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46E57644.6F0F.0085.0@efirstbank.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com>`

```
>>> On 9/8/2007 at 6:23 AM, in message
<vvwEi.1979$ZA5.813@nlpi068.nbdc.sbc.com>, Michael
Mattias<mmattias@talsystems.com> wrote:
> "Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
> news:5kelplF3b3opU1@mid.individual.net...
>> I'll use this reponse to respond to both of the excellent posts from Doc

> 
>> and Judson.
…[32 more quoted lines elided]…
> Then you will know what users need, and I'll bet they start getting it.

Indeed.  One of the great advantages I've had here is that I was an actual
'business user' for five years prior to becoming a programmer here.  In fact
quite a few programmers here were business users first.

Not that I'd suggest everyone spend five years in this manner!  :-)  But
certainly seeing how things are currently done is a great benefit when
developing an application for a business user.

Frank
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 24)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-08T22:22:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbv7c3$kfp$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net>`

```
In article <5kelplF3b3opU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:

[snip]

>More below...
>
><docdwarf@panix.com> wrote in message news:fbrojt$q5d$1@reader1.panix.com...
>> In article <YedEi.37759$7e6.33697@bignews4.bellsouth.net>,

[snip]

>> My apoligies for the snipping... but I believe I've managed to leave the
>> intestines intact.  Currently the folks who sign my timesheet are of the
…[10 more quoted lines elided]…
>start...

Mirable dictu... just when you think you have these human-being type of 
people figured out they show a different dance-step.

In this immediate case I mentioned... the Timesheet-Signers didn't get 
involved, it was the User Liason.  He's been involved in this project 
since it began a year-and-change back and he, too, was Mightily Annoyed 
that after months of 'Gee, that's great!' we received a 'Well... now we 
want it *this* way.'

His solution?  A lie.

He contacted the User and said we'd be more than happy to provide the 
changes in format and processing desired... BUT... the program had, due to 
earlier expressions of satisfaction, already been moved into Prod.

Now that it is in Prod an entirely different mechanism must be employed in 
order to change it, of course... a Formal Change Request had to be made, 
this Requests have to be weighed ('prioritised') against other Requests, 
time will have to be allocated... oh, and fiscal year-end is approaching, 
that's going to push things off... and then you're moving on into Calendar 
year-end, that means another buncha stuff is going to be moved to the 
front burner...

... but we'll be glad to help, honest... you've done this before, they 
have it all on the web; just go to www.support.page and initiate the 
request there.

The lie, of course, was that the program had been moved to Prod... it 
hadn't.  We had contacted the user looking for a final 'all clear' before 
surrendering our wills to The Scheduler.

Anyhow... I expressed admiration and gratitude over this, saying that... 
it made me feel strangely; it is My Job to do what the User wants...

... and he broke in on me right there, saying 'Sure, that's great... *if* 
they know what they (fornicating) want.  If they take any opportunity they 
can to say 'Maybe we want it in blue this week' then... (fornicate) 'em; 
what we have now is in compliance with six months' worth of emails *and* 
the Federal Laws that started this whole mess.  If they don't like that 
let 'em issue a Change Request.'

[snip]

>> The most recent version of 'now we want it THIS way' was met such
>> documentation and a succinct 'To implement this contradictory request will
…[5 more quoted lines elided]…
>things, it isn't helping.

Actually... it *did* help, in that the aforementioned User Liason said it 
made him smile but he couldn't tell the User this... so he had to lean 
back and think of what to say.

>Irrespective of whether the request is contradictory or not, the Business DO 
>need something, and they need it now.

That was just the point, Mr Dashwood... the Business' needs, in terms of 
compliance with Federal Law, were already being met... the *User* wanted 
something else.

>Before I go on, perhaps it is important to ask yourself: "If I COULD deliver 
>on these contradictory requests, would I? Do I actually feel committed to 
…[5 more quoted lines elided]…
>collecting your cheque.

Mr Dashwood, I work in order to earn money and I make no bones about it... 
but the greatest satisfaction I get from my work is when someone, 
*anyone*, looks at me and says 'You know... this makes my job *so* much 
easier!'  

When that satisfaction goes then it'll be time to find another way to pay 
the landlord, sure... but at the moment it still holds.

[snip]

>Changes are welcomed, not seen as a source of aggravation.

All things in moderation, even moderation... it is the User's privelege to 
request changes and the User's responsibility to at least make an attempt 
to insure that the privelege is not abused.  Changes take work, work takes 
time, time is money... and Business' money is not to be spent unless there 
is a Business benefit gained.

(I've seen far too Users say 'Well, the competition just introduced this 
feature, we *must* have it'... and I've seen no-one (besides me) asking 
'It might just be a passing fad, you know... is this feature making the 
competition any more money?')

DD
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 25)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-08T22:12:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vpo6e3lfph1ufc91la1prkcpa2t4kvcfjo@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <fbv7c3$kfp$1@reader1.panix.com>`

```
On Sat, 8 Sep 2007 22:22:59 +0000 (UTC), docdwarf@panix.com () wrote:

>Mr Dashwood, I work in order to earn money and I make no bones about it... 
>but the greatest satisfaction I get from my work is when someone, 
>*anyone*, looks at me and says 'You know... this makes my job *so* much 
>easier!'  

My greatest satisfaction is when someone says "This code is beautiful. Who wrote it?" and
the answer is not 'I did', as you're probably thinking, but rather 'George, the guy
sitting next to you, wrote it.' Then I know I've done my job as manager.
```

###### ↳ ↳ ↳ Re: Can IT deal with change? was:

_(reply depth: 25)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-10T11:08:47-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<79uae315lu1671ki2vdblblcbhhnpvmbvs@4ax.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <YedEi.37759$7e6.33697@bignews4.bellsouth.net> <fbrojt$q5d$1@reader1.panix.com> <5kelplF3b3opU1@mid.individual.net> <fbv7c3$kfp$1@reader1.panix.com>`

```
On Sat, 8 Sep 2007 22:22:59 +0000 (UTC), docdwarf@panix.com () wrote:

>His solution?  A lie.
>
…[10 more quoted lines elided]…
>front burner...

An alternative to this is to figure out which procedures we can be
sticky about that not only are more work for the late changing user -
but for that user's peers as well.    A "we need sign offs of our
detailed specs with changes by all of the guys who would rather be
doing their work than approving your change" can work great.

Of course, we need to have the ability to streamline this when a
request really helps.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 21)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-09T06:42:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189345348.699446.246220@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<fbrgg2$ef$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5k8raoF2ks1sU1@mid.individual.net> <e540e3hnbr7a7h33nrit870vql7dpg63q4@4ax.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com>`

```
On 7 Sep, 13:34, docdw...@panix.com () wrote:
> In article <5kbeiiF2uem...@mid.individual.net>,
>
…[59 more quoted lines elided]…
> DD

Is your shop a cost-centre? If the users' management saw the costs
involved with this evolving development they might be inclined to bite
the bullet and implement. At one site where I worked, the clients
asked for a lot of ad-hoc work but when we introduced charges against
departmental budgets, their attitude changed and the torrent of minor
requests was stemmed.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 22)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-09T16:18:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc16dc$de7$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com>`

```
In article <1189345348.699446.246220@22g2000hsm.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On 7 Sep, 13:34, docdw...@panix.com () wrote:

[snip]

>> Nothing gets accomplished... all that gets done is an eternal re-visiting
>> of yesterday's work because 'it's not what I see that I want and need
>> NOW'.
>
>Is your shop a cost-centre?

If you are calling 'cost-centre' what I was taught to call a 'strict 
chargeback shop' - where costs of development, maintenance and processing 
are kept track of and invoiced back to the requesting party - then no, it 
is not.

I have, in meetings, heard the heavily-sighed 'What are ya gonna do... 
this is the way they've always behaved'; my response is 'Until a 
motivation can be found which will make a different form of behavior be 
seen as superior then the current form will, most likely, continue for a 
goodly long time.'

(side note - I sent you an email a while back and just got notice from 
your ISP that it had not been picked up in thirty days; I hope all is 
going well with you)

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 23)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-11T03:58:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189508328.348639.131150@19g2000hsx.googlegroups.com>`
- **In-Reply-To:** `<fc16dc$de7$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com> <fc16dc$de7$1@reader1.panix.com>`

```

docdw...@panix.com () wrote:
> In article <1189345348.699446.246220@22g2000hsm.googlegroups.com>,
> Alistair  <alistair@ld50macca.demon.co.uk> wrote:
…[25 more quoted lines elided]…
> DD

You sent me an email? Sorry, but I don't know why it would not have
been picked up as my email feed is pretty much automated. No just
checked using webmail - no sign of any message. Sorry, would you be
kind enough to re-send please? Ta (yer majesty).
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 24)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-11T12:33:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc61vd$9h8$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com> <fc16dc$de7$1@reader1.panix.com> <1189508328.348639.131150@19g2000hsx.googlegroups.com>`

```
In article <1189508328.348639.131150@19g2000hsx.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>
>docdw...@panix.com () wrote:

[snip]

>> (side note - I sent you an email a while back and just got notice from
>> your ISP that it had not been picked up in thirty days; I hope all is
>> going well with you)
>
>You sent me an email?

I believe I posted something which might, possibly, have been interpreted 
in such a manner, aye.

>Sorry, but I don't know why it would not have
>been picked up as my email feed is pretty much automated. No just
>checked using webmail - no sign of any message. Sorry, would you be
>kind enough to re-send please? Ta (yer majesty).

Done and done; both the bounce-note and another copy of the email have 
been sent to address givenname@surname.demon.co.uk... and you're getting 
it all greasy, you have Our permission to let go of that forelock.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 25)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-11T12:00:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189537209.813088.318850@e9g2000prf.googlegroups.com>`
- **In-Reply-To:** `<fc61vd$9h8$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com> <fc16dc$de7$1@reader1.panix.com> <1189508328.348639.131150@19g2000hsx.googlegroups.com> <fc61vd$9h8$1@reader1.panix.com>`

```

docdw...@panix.com () wrote:
> In article <1189508328.348639.131150@19g2000hsx.googlegroups.com>,
> Alistair  <alistair@ld50macca.demon.co.uk> wrote:
…[23 more quoted lines elided]…
> DD


Consider forelock un-tugged. Thanks for the emails. I suspect that you
are getting at my tendency to agree with two conflicting views at one
and the same time (something that I am prone to do in pubs). I can
only apologise and promise to vehemently denounce all views that
differ from my own bigotted ones, in future. Sorry. It must have been
a major point to merit an email and an observation in the newsgroup. I
am well but am a little haphazard in following the newsgroup these
days; so I do miss stuff.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 23)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-11T04:00:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189508404.929749.259150@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<fc16dc$de7$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com> <fc16dc$de7$1@reader1.panix.com>`

```

docdw...@panix.com () wrote:

I should have added my email address is
alistair@ld50macca.demon.co.uk    - best to cut and paste it.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 24)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-11T12:37:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc626f$qdc$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com> <fc16dc$de7$1@reader1.panix.com> <1189508404.929749.259150@y42g2000hsy.googlegroups.com>`

```
In article <1189508404.929749.259150@y42g2000hsy.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>
>I should have added my email address is
>alistair@ld50macca.demon.co.uk  

Ye Goddes and Little Fishies... a Purloined Letter gambit, eh?  I was 
Absolutely Certain that the indication of a dose that would cause death in 
half of a tested population was a bit of spam-munging on your part... it 
seems I was being 'too clever by fifty per cent', as well.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 25)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-11T12:02:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189537329.165356.77350@b32g2000prf.googlegroups.com>`
- **In-Reply-To:** `<fc626f$qdc$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com> <fc16dc$de7$1@reader1.panix.com> <1189508404.929749.259150@y42g2000hsy.googlegroups.com> <fc626f$qdc$1@reader1.panix.com>`

```

docdw...@panix.com () wrote:
> In article <1189508404.929749.259150@y42g2000hsy.googlegroups.com>,
> Alistair  <alistair@ld50macca.demon.co.uk> wrote:
…[9 more quoted lines elided]…
> DD

Perhaps not clever enough for the upper fifty-percentile. Well spotted
on the lethal dose: you are correct in that observation.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 26)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-11T19:06:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fc6p08$5qj$1@reader1.panix.com>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <1189508404.929749.259150@y42g2000hsy.googlegroups.com> <fc626f$qdc$1@reader1.panix.com> <1189537329.165356.77350@b32g2000prf.googlegroups.com>`

```
In article <1189537329.165356.77350@b32g2000prf.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>
>docdw...@panix.com () wrote:

[snip]

>> I was
>> Absolutely Certain that the indication of a dose that would cause death in
…[4 more quoted lines elided]…
>on the lethal dose: you are correct in that observation.

I noticed something that was plainly out in the open... somebody notify 
Reuters, hoo haemorrhaging ray.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 22)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-10T14:32:04+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kjol6F3vjg6U1@mid.individual.net>`
- **References:** `<1188681225.360094.78060@o80g2000hse.googlegroups.com> <5k8raoF2ks1sU1@mid.individual.net> <e540e3hnbr7a7h33nrit870vql7dpg63q4@4ax.com> <5kbeiiF2uem5U1@mid.individual.net> <fbrgg2$ef$1@reader1.panix.com> <1189345348.699446.246220@22g2000hsm.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1189345348.699446.246220@22g2000hsm.googlegroups.com...
> On 7 Sep, 13:34, docdw...@panix.com () wrote:
>> In article <5kbeiiF2uem...@mid.individual.net>,
…[74 more quoted lines elided]…
>
Sure. Everyone wants a chocolate fish when they're free...:-)

An essential point of this model is that the Client (Business or Users) 
calls the shots. If they want a particular change they can have it, BUT they 
do not have carte blanche and something else will be lost. (In the worst 
case things will need to be completely rescoped in order to accommodate 
their request. This will inevitably cost them more.) The difference is that 
the final onus for making changes is on them (which is where it should be), 
and NOT on IT, although it is a shared responsibility and both sides will 
work together to make the change.

It works extremely well compared to the other alternatives; the Clients like 
to feel they are in control and getting support from IT to achieve their 
goals. It is subtle, but it makes a major difference. I have seen them argue 
among themselves about a proposed change and eventually decide not to make 
it. It also leads to much better understanding by the IT people of the 
problems of the Business, and to a greater appreciation by Business people 
of the problems handled by IT. The "joint ownership" is fundamental and key 
to it. Support  (buy in) must be obtained from Senior Management in both IT 
and the Business if it is to have any chance of success.  There is too much 
to go into here, but as soon as I have time and inclination, I'll finish the 
half-written book I have on these aproaches. (It is easy to write a book on, 
because there is so much in it...:-))

It IS possible for IT to be dynamic and responsive to change, but it needs 
commitment from Senior Management right down the chain, and the will to 
provide a superlative support to the Business.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 16)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-09T06:26:26-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189344386.201042.62250@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<5k803uF2fd0dU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net>`

```
On 5 Sep, 16:25, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
wrote:
> "Alistair" <alist...@ld50macca.demon.co.uk> wrote in message
>
…[83 more quoted lines elided]…
> - Show quoted text -

I had used the term 'OO Goetterdammerung' as a feed in the hope that
you would have come back with one of your humourous articles similar
to the Glasshopper one. Perhaps Thor and Odin bemoaning the passing of
OO Goetterdammerung with young upstarts such as Loki coming in with
new languages representing a paradigm shift in coding and design?
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 17)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-10T14:42:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kjp8aF3ubfcU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <1189344386.201042.62250@k79g2000hse.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1189344386.201042.62250@k79g2000hse.googlegroups.com...
> On 5 Sep, 16:25, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[108 more quoted lines elided]…
>
OK :-)

Sometimes it is hard to know what people are serious about and what they are 
not, here.

There are some quite precise parallels between what has happened with COBOL 
and the Teutonic fables of Goetterdammerung... I'll give it some 
thought...:-)

Currently, I am recovering from a rotten cold that has made it impossible 
for me to even do any work for a few days (simply unable to concentrate) but 
I'm getting better and, once I 've caught up to my schedule, I'll be in a 
lighter frame of mind.

Pete.
```

###### ↳ ↳ ↳ OT - Goetterdammerung (wase: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-09-10T06:08:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ob5Fi.20949$gR1.3806@fe03.news.easynews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <1189344386.201042.62250@k79g2000hse.googlegroups.com> <5kjp8aF3ubfcU1@mid.individual.net>`

```
Pete,
   Anyone who has EVER been at an X3J4 or J4 COBOL Standard meeting would 
certainly have to include Anna Russell's

  "I don't make these things up, you know"

frequently.  (I know that I certainly think it both at and after the meetings)

P.S.  For those not familiar with her - but who like Wagner, Gilbert & Sullivan, 
etc - see:
   http://www.amazon.com/Anna-Russell-Album/dp/customer-reviews/B0000027JD
```

###### ↳ ↳ ↳ Re: OT - Goetterdammerung (wase: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-10T23:21:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5kknm2F49ammU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <1189344386.201042.62250@k79g2000hse.googlegroups.com> <5kjp8aF3ubfcU1@mid.individual.net> <ob5Fi.20949$gR1.3806@fe03.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:ob5Fi.20949$gR1.3806@fe03.news.easynews.com...
> Pete,
>   Anyone who has EVER been at an X3J4 or J4 COBOL Standard meeting would 
…[10 more quoted lines elided]…
>

Thanks Bill.

I'm not familiar with her, but I've ordered it through Amazon. It's showing 
delivery around 11th of next month. I'll let you know what I think :-)

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 18)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-11T04:10:46-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189509046.147588.271760@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5kjp8aF3ubfcU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <1189344386.201042.62250@k79g2000hse.googlegroups.com> <5kjp8aF3ubfcU1@mid.individual.net>`

```

Pete Dashwood wrote:

> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1189344386.201042.62250@k79g2000hse.googlegroups.com...
…[12 more quoted lines elided]…
>

We have something in the northern hemisphere called Day Nurse and
another called Night Nurse. Both are very effective on colds. Night
Nurse can only be beaten by the real thing and by whisky (preferably
Laphroiag).
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 19)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-12T05:07:49+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ko0b3F4nhciU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <1189344386.201042.62250@k79g2000hse.googlegroups.com> <5kjp8aF3ubfcU1@mid.individual.net> <1189509046.147588.271760@50g2000hsm.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1189509046.147588.271760@50g2000hsm.googlegroups.com...
>
> Pete Dashwood wrote:
…[22 more quoted lines elided]…
>
Yes, I was introduced to Night Nurse by a nurse in the U.K. whom I often 
spent nights with. A lovely girl from Te Awamutu in NZ (she was doing her 
big O.E  (overseas experience) ... I was very happy to be part of it :-)

We also have the same Vicks products here in NZ, but I'm pleased to say that 
I seem to be recovering (loads of Vitamin C, garlic, and chicken soup) and I 
haven't had to resort to those products.

For me the only whisky is Jack Daniels, but I realise that is sacrilege to a 
Scot :-)

Thanks for the thought, Alistair :-)

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 20)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-11T12:06:33-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189537593.957246.262000@q5g2000prf.googlegroups.com>`
- **In-Reply-To:** `<5ko0b3F4nhciU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com> <5k66fvF2a38cU1@mid.individual.net> <1188987959.571316.221700@g4g2000hsf.googlegroups.com> <5k803uF2fd0dU1@mid.individual.net> <1189344386.201042.62250@k79g2000hse.googlegroups.com> <5kjp8aF3ubfcU1@mid.individual.net> <1189509046.147588.271760@50g2000hsm.googlegroups.com> <5ko0b3F4nhciU1@mid.individual.net>`

```

Pete Dashwood wrote:
> "Alistair" <alistair@ld50macca.demon.co.uk> wrote in message
> news:1189509046.147588.271760@50g2000hsm.googlegroups.com...
…[4 more quoted lines elided]…
>

Not sacrilege. If you want to drink neat and unrefined petrol feel
free to continue with JD. Personally, I always prefered Rebel Yell and
Wild Turkey.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 13)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-05T11:14:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hootd39hkelsdjsuka8jjbkcdonmq6eh5l@4ax.com>`
- **References:** `<0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <5jt65rF13v7mU1@mid.individual.net> <1188681225.360094.78060@o80g2000hse.googlegroups.com> <5jujlaF1b66jU1@mid.individual.net> <1188731293.799332.22640@k79g2000hse.googlegroups.com> <1jsqd3h37ttph69f76n6qshkcu0p78n5f6@4ax.com> <1188933977.447765.204860@r34g2000hsd.googlegroups.com>`

```
On Tue, 04 Sep 2007 12:26:17 -0700, Alistair
<alistair@ld50macca.demon.co.uk> wrote:

>> Are you implying that there others who believe in Goetterdammerung, or
>> are you just wondering how can the term ever be used in a phrase?
…[3 more quoted lines elided]…
>concepts relating to deities (a crime of which I am probably guilty).

Why should an atheist be less likely to use the term Goetterdammerung
than, say a Christian?    

While it is obvious from watching Hollywood movies about Santa Clause,
that some people believe the important thing is to believe in
*something*, that is not dogma of any of the religions of the book. 

Atheists don't believe you will be punished in the afterlife for
believing in the wrong deity.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-01T14:05:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188680738.372165.29590@22g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<fbbc0b$o1a$02$1@news.t-online.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com>`

```

Roger While wrote:
> May I repeat what I previously stated -
> If you have something to say that is not
…[7 more quoted lines elided]…
> Roger

So should this response have been:

OT [OT] RE:  blahblahblah

or

RE: [OT} RE: blahblahblahdiblah?
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** Aparajita <aparajita.mohanty@gmail.com>
- **Date:** 2007-09-04T05:43:58
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188884638.358598.311330@o80g2000hse.googlegroups.com>`
- **In-Reply-To:** `<fbbc0b$o1a$02$1@news.t-online.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com>`

```
It is pathetic to see what my query has led to.
I am sorry to see what all discussions have followed which are of
absolutely no relevance to the original query.

Aparajita.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-04T19:06:29+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k4efkF21iiiU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com>`

```


"Aparajita" <aparajita.mohanty@gmail.com> wrote in message 
news:1188884638.358598.311330@o80g2000hse.googlegroups.com...
> It is pathetic to see what my query has led to.
> I am sorry to see what all discussions have followed which are of
> absolutely no relevance to the original query.
>

Why does this make you sorry?

You received help that was relevant to your query.

You are not a frequent contributor here so why would you care what we choose 
to discuss?

If you WERE a frequent visitor, you'd know that this is pretty normal for 
this group.

It strikes me as being somewhat churlish to accept help, then describe the 
group who gave it as "pathetic".

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-09-04T11:29:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akbDi.31559$RX.163@newssvr11.news.prodigy.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com>`

```
"Aparajita" <aparajita.mohanty@gmail.com> wrote in message 
news:1188884638.358598.311330@o80g2000hse.googlegroups.com...
> It is pathetic to see what my query has led to.
> I am sorry to see what all discussions have followed which are of
> absolutely no relevance to the original query.

Of course they are relevant.

No programming challenge exists in a vacuum, no man is an island.

MCM
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2007-09-04T07:32:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dqk1hs8eqpb29@news.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com>`

```
Aparajita wrote:
> It is pathetic to see what my query has led to.
> I am sorry to see what all discussions have followed which are of
> absolutely no relevance to the original query.
>
> Aparajita.

I will pray to Baby Jesus for your speedy recovery.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-04T12:34:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbjjc0$6h4$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com>`

```
In article <1188884638.358598.311330@o80g2000hse.googlegroups.com>,
Aparajita  <aparajita.mohanty@gmail.com> wrote:
>It is pathetic to see what my query has led to.

If that is considered to be the case then it might be possible, in future, 
to avoid 'where something leads' by avoiding 'what started something out'.

Please do your own homework.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-05T11:05:37+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k66m0F2ap8iU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com> <fbjjc0$6h4$1@reader1.panix.com>`

```


<docdwarf@panix.com> wrote in message news:fbjjc0$6h4$1@reader1.panix.com...
> In article <1188884638.358598.311330@o80g2000hse.googlegroups.com>,
> Aparajita  <aparajita.mohanty@gmail.com> wrote:
…[6 more quoted lines elided]…
>
It's funny, that exact same thought occurred to me yesterday.

I've already explained why I responded on this occasion rather than leaving 
it at that, but there is a definite case to be made for your standard 
response, Doc.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-05T00:37:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbktng$qpm$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com> <fbjjc0$6h4$1@reader1.panix.com> <5k66m0F2ap8iU1@mid.individual.net>`

```
In article <5k66m0F2ap8iU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[10 more quoted lines elided]…
>It's funny, that exact same thought occurred to me yesterday.

Space Aliens stealing my brainwaves and planting them into your skull, Mr 
Dashwood, is anything *but* funny.

>
>I've already explained why I responded on this occasion rather than leaving 
>it at that, but there is a definite case to be made for your standard 
>response, Doc.

The boilerplate I employ may, at times, seem hackneyed or boring from much 
use... but there might as well be a bit of accuracy or straight-on-ness to 
its being applied; hence it might be seen as...

... trite, and true.

DD
```

###### ↳ ↳ ↳ OT Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** Lucretia <LMPruitt@gmail.com>
- **Date:** 2007-09-06T23:30:05
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189121405.435232.215490@y42g2000hsy.googlegroups.com>`
- **In-Reply-To:** `<1188884638.358598.311330@o80g2000hse.googlegroups.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com>`

```
On Sep 3, 11:43 pm, Aparajita <aparajita.moha...@gmail.com> wrote:
> It is pathetic to see what my query has led to.
> I am sorry to see what all discussions have followed which are of
> absolutely no relevance to the original query.
>
> Aparajita.

Are you? Sorry that is?  How sad.
Hopefully when you are no longer stuck trying to find answers for your
homework you will gain both a sense of humor and some perspective.

I haven't been to this forum in a good 8 years, and yet it was
refreshing to see that a post which is obviously a thinly-veiled
attempt to solve a homework problem is *still* being met by Doc's long-
echoing refrain, and still likely to send the regulars off on fun and
interesting tangents.  It's what makes CLC such a dynamic place.

The irony for me was that I drifted back after having Googled a
variation of my name only to be confronted with old archived CLC posts
of mine from 10 years ago.  I think I was just as upset then about
"serious" threads about "strictly COBOL" devolving this way as you
seem to be now.

Time provides perspective - and it's good to see that the CLC brain
trust is still here and functioning and as feisty as ever!
Kudos to them - and from someone who has spent time teaching COBOL at
University in the interim? Shame on you for not doing your own
assignment!

Lucretia
```

###### ↳ ↳ ↳ Re: OT Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 9)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-06T23:49:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbq3li$pu7$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com> <1189121405.435232.215490@y42g2000hsy.googlegroups.com>`

```
In article <1189121405.435232.215490@y42g2000hsy.googlegroups.com>,
Lucretia  <LMPruitt@gmail.com> wrote:
>On Sep 3, 11:43 pm, Aparajita <aparajita.moha...@gmail.com> wrote:
>> It is pathetic to see what my query has led to.
…[3 more quoted lines elided]…
>> Aparajita.

[snip]

>I haven't been to this forum in a good 8 years, and yet it was
>refreshing to see that a post which is obviously a thinly-veiled
>attempt to solve a homework problem is *still* being met by Doc's long-
>echoing refrain, and still likely to send the regulars off on fun and
>interesting tangents.

Shucks, I'd blush, were I able to remember how... but really, you'se jes' 
easily refreshed, that's all.

DD
```

###### ↳ ↳ ↳ Re: OT Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 10)_

- **From:** L Pruitt <LMPruitt@gmail.com>
- **Date:** 2007-09-06T23:52:37
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1189122757.382862.237090@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<fbq3li$pu7$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <fbbc0b$o1a$02$1@news.t-online.com> <1188884638.358598.311330@o80g2000hse.googlegroups.com> <1189121405.435232.215490@y42g2000hsy.googlegroups.com> <fbq3li$pu7$1@reader1.panix.com>`

```
On Sep 6, 5:49 pm, docdw...@panix.com () wrote:
> In article <1189121405.435232.215...@y42g2000hsy.googlegroups.com>,
>
…[19 more quoted lines elided]…
> DD

Now I sound like a javascript! ;)
```

###### ↳ ↳ ↳ Re: OT Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 11)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-06T23:59:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbq49d$13r$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <1189121405.435232.215490@y42g2000hsy.googlegroups.com> <fbq3li$pu7$1@reader1.panix.com> <1189122757.382862.237090@d55g2000hsg.googlegroups.com>`

```
In article <1189122757.382862.237090@d55g2000hsg.googlegroups.com>,
L Pruitt  <LMPruitt@gmail.com> wrote:
>On Sep 6, 5:49 pm, docdw...@panix.com () wrote:
>> In article <1189121405.435232.215...@y42g2000hsy.googlegroups.com>,
…[20 more quoted lines elided]…
>Now I sound like a javascript! ;)

Well, when you feel like something gritty and raunchy...

... perhaps a bit of lotion might help.

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-01T14:01:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188680478.424311.59990@50g2000hsm.googlegroups.com>`
- **In-Reply-To:** `<5js7jrF12ab2U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net>`

```

Pete Dashwood wrote:
> <docdwarf@panix.com> wrote in message news:fbae5i$rnu$1@reader1.panix.com...
> > In article <5jrnpsF10st0U1@mid.individual.net>,
…[57 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

Phoenicians or Mycenaeans?
```

###### ↳ ↳ ↳ [OT]Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-02T14:11:00+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jukdlF1bb30U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1188680478.424311.59990@50g2000hsm.googlegroups.com...
>
> Pete Dashwood wrote:
…[75 more quoted lines elided]…
>
Good try, but neither, actually. It is a sad reflection on our view of 
History that the achievements of these people is only starting to come to 
light. It is partly their own fault because they believed the stars were 
Gods and so only the Priesthood were privy to knowledge of Astronomy. It was 
sacred, and to publicise it would have rendered it profane. It also enabled 
them to predict various events, which gave them power over the populace. No 
Religion is going to give away its power base (and put Priests out of 
work...and yes, I HAVE read "The Shoes of the Fisherman" :-)), for the 
public good...:-) This one was no exception.

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-01T22:41:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0vbkd3phr9bihnmvi17s8vmi8sfi8ljg7t@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net>`

```
On Sun, 2 Sep 2007 14:11:00 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

> It also enabled 
>them to predict various events, which gave them power over the populace. No 
>Religion is going to give away its power base (and put Priests out of 
>work...and yes, I HAVE read "The Shoes of the Fisherman" :-)), for the 
>public good...:-)

I removed the Off Topic subject prefix because you described the power dynamic in a  COBOL
shop.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-02T17:50:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jv19mF1c763U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net> <0vbkd3phr9bihnmvi17s8vmi8sfi8ljg7t@4ax.com>`

```


"I used to write COBOL...now I can do anything."
"Robert" <no@e.mail> wrote in message 
news:0vbkd3phr9bihnmvi17s8vmi8sfi8ljg7t@4ax.com...
> On Sun, 2 Sep 2007 14:11:00 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[11 more quoted lines elided]…
> shop.

Ah, Robert, I see your absence has done nothing to diminish your 
mischievousness... :-)

Play nicely with the dinosaurs and don't tease them; those are the rules of 
the Park... :-).

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 10)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-02T08:10:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ppbld35bequo3s5e5nbtej3207q8orch95@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net> <0vbkd3phr9bihnmvi17s8vmi8sfi8ljg7t@4ax.com> <5jv19mF1c763U1@mid.individual.net>`

```
On Sun, 2 Sep 2007 17:50:44 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>Ah, Robert, I see your absence has done nothing to diminish your 
>mischievousness... :-)
>
>Play nicely with the dinosaurs and don't tease them; those are the rules of 
>the Park... :-).

I got my rejection letter from the Clique Membership Committee. It seems CLC is for the
worship of COBOL not discussion of good programming. They also dinged me for posting lower
case code and for mentioning The Name Of The Beast: xinU. They said their ecuminism could
tolerate AS/400, Unisys, even an occasional PCer, but admitting an xinU was asking too
much. They seemed to equate xinU with OO and Wicca.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 11)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-03T02:01:24+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jvu17F1g1anU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net> <0vbkd3phr9bihnmvi17s8vmi8sfi8ljg7t@4ax.com> <5jv19mF1c763U1@mid.individual.net> <ppbld35bequo3s5e5nbtej3207q8orch95@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:ppbld35bequo3s5e5nbtej3207q8orch95@4ax.com...
> On Sun, 2 Sep 2007 17:50:44 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[17 more quoted lines elided]…
> much. They seemed to equate xinU with OO and Wicca.

:-)
At least you have retained your sense of humour.

xinU eh?  "XinU Is Not Unix"    Have you seriously had experience with it? I 
thought it was just for teaching.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 12)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-02T11:57:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mlqld3p8ua0k3j88antv8qtj5ok4tf21l7@4ax.com>`
- **References:** `<5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net> <0vbkd3phr9bihnmvi17s8vmi8sfi8ljg7t@4ax.com> <5jv19mF1c763U1@mid.individual.net> <ppbld35bequo3s5e5nbtej3207q8orch95@4ax.com> <5jvu17F1g1anU1@mid.individual.net>`

```
On Mon, 3 Sep 2007 02:01:24 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:

>At least you have retained your sense of humour.
>
>xinU eh?  "XinU Is Not Unix"    Have you seriously had experience with it? I 
>thought it was just for teaching.

I have no experience with it, but its author, Douglas Comer, has a good sense of humor.
Example: http://www.cs.purdue.edu/homes/dec/essay.jargon.html
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 13)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-03T12:30:59+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k12u6F1m228U1@mid.individual.net>`
- **References:** `<5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net> <0vbkd3phr9bihnmvi17s8vmi8sfi8ljg7t@4ax.com> <5jv19mF1c763U1@mid.individual.net> <ppbld35bequo3s5e5nbtej3207q8orch95@4ax.com> <5jvu17F1g1anU1@mid.individual.net> <mlqld3p8ua0k3j88antv8qtj5ok4tf21l7@4ax.com>`

```


"Robert" <no@e.mail> wrote in message 
news:mlqld3p8ua0k3j88antv8qtj5ok4tf21l7@4ax.com...
> On Mon, 3 Sep 2007 02:01:24 +1200, "Pete Dashwood" 
> <dashwood@removethis.enternet.co.nz>
…[10 more quoted lines elided]…
> Example: http://www.cs.purdue.edu/homes/dec/essay.jargon.html

I checked the link, found it amusing,  and can definitely relate to at least 
two items on the list (my lips are sealed :-))

Pete.
```

###### ↳ ↳ ↳ OT: Was it Egypt? was Re: [OT]Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-09-03T14:24:24-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dlgod3pbh7ised34i54rtjacqgm1f25ngt@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net>`

```
On Sun, 2 Sep 2007 14:11:00 +1200, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>
>
…[88 more quoted lines elided]…
>public good...:-) This one was no exception.

I assumed Egypt from your writing.  It would be interesting to know if
there were parallel developments in China or India.
>
>Pete
```

###### ↳ ↳ ↳ Re: Was it Egypt? was Re: [OT]Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-04T11:16:19+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k3iu6F20ofqU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <1188680478.424311.59990@50g2000hsm.googlegroups.com> <5jukdlF1bb30U1@mid.individual.net> <dlgod3pbh7ised34i54rtjacqgm1f25ngt@4ax.com>`

```


"Clark F Morris" <cfmpublic@ns.sympatico.ca> wrote in message 
news:dlgod3pbh7ised34i54rtjacqgm1f25ngt@4ax.com...
> On Sun, 2 Sep 2007 14:11:00 +1200, "Pete Dashwood"
> <dashwood@removethis.enternet.co.nz> wrote:
…[104 more quoted lines elided]…
>>
Well Done, Clark!

It was indeed Egypt. There is some very interesting stuff starting to emerge 
from information inscribed on tablets  and the fact that the modern 
Egyptians are doing intense investigation of their past. Perhaps, in the 
past, British historians (with Classical educations) were more inclined to 
the traditional Western views and saw Egypt as being primitive and not in 
the same Civilization League as the Greeks and Romans (who, in fact, were 
strongly, if subtly, influenced by Egyptian teachers). As Egyptian scholars 
have gained recognition in their own right, a less racist view of History is 
starting to emerge. (Of course, you could argue it is biased, and it 
probably is, but there is no denying what is carved in stone or clay.)  It 
is as certain as anything can be after 4000 years, that the Ancient Egyptian 
Astronomers knew the distance to the sun and deduced it using devices that 
measured angles and time, which they built around 4500 years ago. It is very 
likely that both Eratosthenes and Aristarchos were simply repeating 
(possibly even confirming) experiments that were part of the culture passed 
on by the Egyptians, and which had been done millenia before they lived.

I agree it would be very interesting to know what the state of "Science" was 
in India and China 4000 years ago, or even longer.

It is becoming apparent that the traditional view of History which we all 
learned at school, has some serious errors and omissions in it...

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-01T19:25:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pa0kd39rn3nb4qb2fojfphj83pqvin6bbv@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net>`

```
On Sat, 1 Sep 2007 16:20:09 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:
>I was referring to the same people who, 5000 years 
>ago gave us the current 365 day calendar (based on their astronomical 
…[10 more quoted lines elided]…
>No more clues... do your own homework. :-)

US Marines destroyed 2,500 year-old Babylonian roads by driving tanks over them, dug
trenches through archeological digs and caused the collapse of one building. They said
they had to destroy the ruins in order to save them (from looters).
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-09-04T16:48:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hdSdnUaX2v2ffEDbnZ2dnUVZ_rzinZ2d@comcast.com>`
- **In-Reply-To:** `<pa0kd39rn3nb4qb2fojfphj83pqvin6bbv@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <pa0kd39rn3nb4qb2fojfphj83pqvin6bbv@4ax.com>`

```
Robert wrote:
> On Sat, 1 Sep 2007 16:20:09 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
> wrote:
…[16 more quoted lines elided]…
> they had to destroy the ruins in order to save them (from looters). 

What does that have to do with anything?
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-04T22:52:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ku9sd3hjmva8etk5i8lvre8p3tr7c8a292@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <pa0kd39rn3nb4qb2fojfphj83pqvin6bbv@4ax.com> <hdSdnUaX2v2ffEDbnZ2dnUVZ_rzinZ2d@comcast.com>`

```
On Tue, 04 Sep 2007 16:48:30 -0600, LX-i <lxi0007@netscape.net> wrote:

>Robert wrote:
>> On Sat, 1 Sep 2007 16:20:09 +1200, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
…[19 more quoted lines elided]…
>What does that have to do with anything?

I thought Pete was referring to Babylon.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 9)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-09-05T22:42:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<T5mdncE2vNEcGELbnZ2dnUVZ_u7inZ2d@comcast.com>`
- **In-Reply-To:** `<ku9sd3hjmva8etk5i8lvre8p3tr7c8a292@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <pa0kd39rn3nb4qb2fojfphj83pqvin6bbv@4ax.com> <hdSdnUaX2v2ffEDbnZ2dnUVZ_rzinZ2d@comcast.com> <ku9sd3hjmva8etk5i8lvre8p3tr7c8a292@4ax.com>`

```
Robert wrote:
> On Tue, 04 Sep 2007 16:48:30 -0600, LX-i <lxi0007@netscape.net> wrote:
> 
…[21 more quoted lines elided]…
> I thought Pete was referring to Babylon.

Ah - gotcha...
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-09-05T11:23:15-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9fptd3t19k6ksd4qo20neu8ocrlttjfqi5@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net> <pa0kd39rn3nb4qb2fojfphj83pqvin6bbv@4ax.com>`

```
On Sat, 01 Sep 2007 19:25:52 -0500, Robert <no@e.mail> wrote:

>>No more clues... do your own homework. :-)
>
>US Marines destroyed 2,500 year-old Babylonian roads by driving tanks over them, dug
>trenches through archeological digs and caused the collapse of one building. They said
>they had to destroy the ruins in order to save them (from looters). 

Well, in that case, don't do you own homework. ;-)
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-02T01:17:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbd306$n1m$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jrnpsF10st0U1@mid.individual.net> <fbae5i$rnu$1@reader1.panix.com> <5js7jrF12ab2U1@mid.individual.net>`

```
In article <5js7jrF12ab2U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[55 more quoted lines elided]…
>No more clues... do your own homework. :-)

My homework has, at times, encompassed the works of the Babylonians, Mr 
Dashwood... but many do not pay them much mind, their learning being the 
result of their Priesthood and all that.

(oh... and according to data published by the High Altitude Observatory 
the distance to the sun was first calculated somewhere around 250BC by 
Aristarchus of Samos (see 
http://www.hao.ucar.edu/Public/education/Timeline.A.html#250bc )... but 
what do *they* know about such matters, anyhow?)

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2007-09-01T12:54:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%hdCi.4605$JD.3820@newssvr21.news.prodigy.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net>`

```
"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
news:5jrnpsF10st0U1@mid.individual.net...
> Sadly, as is often the case today, the OP simply picked up a solution from 
> someone who was happy to provide it, without really bothering to think 
…[3 more quoted lines elided]…
> the line of least resistance are more the order of the day....

This is a really good point.

If you look at the classified ads, you'll see what employers want in 
addition to 'technical competence' are three 'intangibles':

First, they all want "communications skills"  - however you want to define 
that.

Second, they all want a "team player" - whatever that means.

And, they want "problem solving skills" - another somewhat amorphous term.

While in this case the OP demonstrated communications skills and "team play" 
(he *was* able to express his challenge (?) and had no problems accepting 
the suggestions of others), his 'problem solving skills' were left 
unenhanced.

I have a saying I use when asked the difference between school and Real 
Life: "In Real Life, the answers are *not* found in Appendix B."

But a young man I encountered some years ago had his own take on this: "In 
Real Life, *all* problems are 'story' problems."

I think this thread demonstrates how that young man's view would be 
something for the OP to keep in mind.

MCM
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 5)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-02T01:29:56+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jt7qmF15gjgU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net>`

```

```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 6)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-02T12:44:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188762276.838841.116880@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<5jt7qmF15gjgU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net> <5jt7qmF15gjgU1@mid.individual.net>`

```

Pete Dashwood wrote:
> --
> "I used to write COBOL...now I can do anything."
…[64 more quoted lines elided]…
> "I used to write COBOL...now I can do anything."

I've just had another drunken session with my boozy chum. He is in the
process of interviewing for a particular vacancy at his site. They
keep getting the usual CICS DB2 contractors but they all, so far, are
weirdos who either could not do the job or would not do it (they got
turned down by one bloke). He has repeatedly put me forward for the
position (he knows that I would fit in and can do the job) but because
I don't have CICS and DB2 threaded throughout my cv they are not
interested. When the latest interview turned out to be unacceptable
(his responses to questions were slowly expressed) I had to smile.
Perhaps there is a God after all. His project is now behind schedule.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-02T23:19:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbfge7$4j6$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net> <5jt7qmF15gjgU1@mid.individual.net> <1188762276.838841.116880@d55g2000hsg.googlegroups.com>`

```
In article <1188762276.838841.116880@d55g2000hsg.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:

[snip]

>They
>keep getting the usual CICS DB2 contractors but they all, so far, are
>weirdos who either could not do the job or would not do it (they got
>turned down by one bloke).

'Everyone we can get for the rate we're offering is unqualified to do the 
job... there must be something wrong with the applicant pool!'

[snip]

>When the latest interview turned out to be unacceptable
>(his responses to questions were slowly expressed) I had to smile.

Well, it used to be that machine time was expensive and human time was 
cheap... and that's when coding for micro-efficiency paid off.  Nowadays, 
when human time is expensive, those slow answers cost Real Money.

(during interviews when it became obvious that I didn't want to take the 
job I'd wait until the interviewer would toss off the mandatory 'Is there 
anything you'd like to ask me?'... and then I'd respond with 'Yes, there 
is... in this organisation which is thought of as being better, having the 
first answer to a question or having the first correct answer?'

it was a rare day, indeed, when the interviewer would snap back, 
instinctively, 'The first correct answer, of course'... so I'd get to 
watch some stammer and dodge and weave... and then I'd call up 
the pimps *before* the client could and tell them that I didn't feel the 
job was a Good Fit)

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 8)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-04T12:11:15-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188933075.689002.69360@d55g2000hsg.googlegroups.com>`
- **In-Reply-To:** `<fbfge7$4j6$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net> <5jt7qmF15gjgU1@mid.individual.net> <1188762276.838841.116880@d55g2000hsg.googlegroups.com> <fbfge7$4j6$1@reader1.panix.com>`

```
On 3 Sep, 00:19, docdw...@panix.com () wrote:
> In article <1188762276.838841.116...@d55g2000hsg.googlegroups.com>,
>
…[11 more quoted lines elided]…
>

You are beginning to sound like a manager.

>
> >When the latest interview turned out to be unacceptable
…[18 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-05T11:08:13+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5k66qsF29583U1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net> <5jt7qmF15gjgU1@mid.individual.net> <1188762276.838841.116880@d55g2000hsg.googlegroups.com> <fbfge7$4j6$1@reader1.panix.com> <1188933075.689002.69360@d55g2000hsg.googlegroups.com>`

```


"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1188933075.689002.69360@d55g2000hsg.googlegroups.com...
> On 3 Sep, 00:19, docdw...@panix.com () wrote:
>> In article <1188762276.838841.116...@d55g2000hsg.googlegroups.com>,
…[14 more quoted lines elided]…
> You are beginning to sound like a manager.

I believe that was Doc's point, Alistair.

I'm making no comment because I know this happens, and there are bad 
managers out there.

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-05T00:39:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbktr4$r7v$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <fbfge7$4j6$1@reader1.panix.com> <1188933075.689002.69360@d55g2000hsg.googlegroups.com> <5k66qsF29583U1@mid.individual.net>`

```
In article <5k66qsF29583U1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>
>
…[23 more quoted lines elided]…
>managers out there.

Ummmmm... isn't the above a comment... and is this not a pipe?

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-09-02T01:23:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fbd3aq$1dv$1@reader1.panix.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net>`

```
In article <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net>,
Michael Mattias <mmattias@talsystems.com> wrote:
>"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message 
>news:5jrnpsF10st0U1@mid.individual.net...
…[17 more quoted lines elided]…
>And, they want "problem solving skills" - another somewhat amorphous term.

Not much new there, Mr Mattias... from 
<http://groups.google.com/group/comp.lang.cobol/msg/6e71bedba6ee62e2?dmode=source>

--begin quoted text:

[snippage]

> Experience with full Lifecycle development Quick study -- MUST be able to
> hit the ground running Effective communicator both written and oral Must be
> a true "team player" assuming lead roles as well as taking directions as the
> need arises

... MUST have all the burning, searing, tortured insight of a True 
Introvert... and be Good With People, too.

--end quoted text

DD
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2007-09-01T22:21:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tcakd3tlrto67ees00pb20jr7hniet1jen@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <5jq8r6Fqh1sU1@mid.individual.net> <0qXBi.233753$Bo7.185140@fe07.news.easynews.com> <5jrnpsF10st0U1@mid.individual.net> <%hdCi.4605$JD.3820@newssvr21.news.prodigy.net>`

```
On Sat, 01 Sep 2007 12:54:19 GMT, "Michael Mattias" <mmattias@talsystems.com> wrote:

>If you look at the classified ads, you'll see what employers want in 
>addition to 'technical competence' are three 'intangibles':
>
>First, they all want "communications skills"  - however you want to define 
>that.

Uses complete sentences when writing about production support issues. 

Does not use words like failure, abort, abend, crash when describing issues.

>Second, they all want a "team player" - whatever that means.

Brings bagels once a week.

Laughs a lot.

>And, they want "problem solving skills" - another somewhat amorphous term.

Solves production crashes without access to the production machine or database, without
any tools except those that came with the operating system, and does it quickly, without
complaining.

Refrains from recommending changes to application code to prevent the same problem
recurring. This is seen as finger-pointing, a bad thing.
```

#### ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2007-08-31T07:52:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o67gd3h6adbgdr8e4qa1cku2eok6bv28nq@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com>`

```
On Fri, 31 Aug 2007 06:41:03 -0000, Aparajita
<aparajita.mohanty@gmail.com> wrote:

>I want to find the greatest of two given numbers say 'A' and 'B.
>The condition is that I should use the IF clause but not comparison
>operators like '<', '>','=' etc.

Why?     If it is because you don't like the symbols, use the words.

>Is there any other operator in COBOL by which we can compare two
>numbers.

There are ways to solve your problem in CoBOL.   I don't know what
kind of operator you want for this excluding the operators designed
for it.
```

#### ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-31T09:38:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46D7E17F.6F0F.0085.0@efirstbank.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com>`

```
>>> On 8/31/2007 at 12:41 AM, in message
<1188542463.524263.317700@i38g2000prf.googlegroups.com>,
Aparajita<aparajita.mohanty@gmail.com> wrote:
> Hi,
> 
…[4 more quoted lines elided]…
> numbers.

Not sure why you need this, but perhaps FUNCTION MAX could give you what you
want?

COMPUTE MAX = FUNCTION MAX(A B)

Well, I guess there's no IF in that.

I guess the POSITIVE usage others have given is the answer.

Frank
```

##### ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-31T12:32:37-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dggs41m0sc4c@corp.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com>`

```

"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
news:46D7E17F.6F0F.0085.0@efirstbank.com...
[snip]
> Not sure why you need this, but perhaps FUNCTION MAX could give you what
you
> want?
>
> COMPUTE MAX = FUNCTION MAX(A B)

Another intereting approach might be:
-----
           evaluate
               function ord-max(A B) - function ord-min(A B)
           when 1
               display "A is less than B"
           when 0
               display "A is equal to B"
           when -1
               display "A is greater than B"
           end-evaluate
-----

A and B may be either numeric or alphanumeric, as long as
they are the same.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2007-08-31T18:31:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_7ZBi.297833$rk4.155800@fe09.news.easynews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com> <13dggs41m0sc4c@corp.supernews.com>`

```
If you didn't need to use the IF statement, I can think of a number of 
(ridiculously expensive) ways to do it. (I was thinking of these when I wasn't 
looking at the original assignment where we knew the items were numeric)

 - Create a temp file and SORT it
 - Create an indexed file (and see what entry you get first)
 - Put them into a table and use SEARCH (I am not even certain this could work)

And then there is my favorite (that actually meets the original assignment)

 - use Object Orientation and create a method for comparing two items, e.g.

 If whatever::"compare" (Field-A  Field-B)  Numeric
    Then Display "Field-A > Field-B)


... where the compare method returns zero if the first operand is > than the 
second
   it returns spaces if the 2nd operand is > than the first
 - it returns high-values if they are equal (so you would need to do a 2nd test)

      ***

Don't you think THAT would impress the teacher <G>
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-01T12:05:05+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jrolmF11g4qU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com> <13dggs41m0sc4c@corp.supernews.com> <_7ZBi.297833$rk4.155800@fe09.news.easynews.com>`

```


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message 
news:_7ZBi.297833$rk4.155800@fe09.news.easynews.com...
> If you didn't need to use the IF statement, I can think of a number of 
> (ridiculously expensive) ways to do it. (I was thinking of these when I 
> wasn't looking at the original assignment where we knew the items were 
> numeric)
>
Bill, it doesn't matter if the operands are numeric or not. It is the 
principle of doing "arithemetic" (in the sense that the ALU does 
"arithmetic") on them, and testing the resulting sign that matters. 
(Although I really liked Rick's Evaluate approach as well...) It is not for 
nothing that the the heart of the CPU is an "Arithmetic Logic Unit"... :-)

> - Create a temp file and SORT it
> - Create an indexed file (and see what entry you get first)
…[9 more quoted lines elided]…
>    Then Display "Field-A > Field-B)

C# has almost exactly such a method... as a kind of "blanket" for cases 
where strings need comparison and the usual innate methods are unsuitable 
:-) (Fortunately, you only need to use it rarely...:-))
>
>
…[9 more quoted lines elided]…
>

I think that, in the unlikely event the teacher reads this thread, he/she 
will run screaming from the room... :-)

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

- **From:** "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com>
- **Date:** 2007-08-31T17:08:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<46D84B1D.6F0F.0085.0@efirstbank.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com> <13dggs41m0sc4c@corp.supernews.com>`

```
>>> On 8/31/2007 at 10:32 AM, in message
<13dggs41m0sc4c@corp.supernews.com>,
Rick Smith<ricksmith@mfi.net> wrote:

> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
> news:46D7E17F.6F0F.0085.0@efirstbank.com...
…[21 more quoted lines elided]…
> they are the same.

This whole discussion makes me wonder if the OP is trying to win an
"Obfuscated Cobol" contest!

:-)
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without usingthecomparison operators?

_(reply depth: 4)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-01T12:55:14+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jrrjmF10djgU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com> <13dggs41m0sc4c@corp.supernews.com> <46D84B1D.6F0F.0085.0@efirstbank.com>`

```


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:46D84B1D.6F0F.0085.0@efirstbank.com...
>>>> On 8/31/2007 at 10:32 AM, in message
> <13dggs41m0sc4c@corp.supernews.com>,
…[31 more quoted lines elided]…
>
Frank, it is hardly fair to blame the OP for triggering the subsequent 
outpourings from the denizens of CLC :-) He asked a simple question; what 
happened after that is what makes this Newsgroup great...:-)

Pete.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

_(reply depth: 4)_

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2007-09-01T13:44:07-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1188679447.910830.11390@k79g2000hse.googlegroups.com>`
- **In-Reply-To:** `<46D84B1D.6F0F.0085.0@efirstbank.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com> <13dggs41m0sc4c@corp.supernews.com> <46D84B1D.6F0F.0085.0@efirstbank.com>`

```

Frank Swarbrick wrote:
> >>> On 8/31/2007 at 10:32 AM, in message
> <13dggs41m0sc4c@corp.supernews.com>,
…[30 more quoted lines elided]…
> :-)

He would be bettewr off using BEFUNGE to win that competition.
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-01T11:54:45+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jro26F117mpU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com> <13dggs41m0sc4c@corp.supernews.com>`

```


"Rick Smith" <ricksmith@mfi.net> wrote in message 
news:13dggs41m0sc4c@corp.supernews.com...
>
> "Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message
…[23 more quoted lines elided]…
>
A nice solution Rick. Good job.

(At least you thought about it ... :-))

Pete
```

###### ↳ ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

_(reply depth: 4)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2007-08-31T20:29:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13dhcpecj533g45@corp.supernews.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com> <13dggs41m0sc4c@corp.supernews.com> <5jro26F117mpU1@mid.individual.net>`

```

"Pete Dashwood" <dashwood@removethis.enternet.co.nz> wrote in message
news:5jro26F117mpU1@mid.individual.net...
>
>
> "Rick Smith" <ricksmith@mfi.net> wrote in message
> news:13dggs41m0sc4c@corp.supernews.com...
[snip]
> > Another intereting approach might be:
> > -----
…[16 more quoted lines elided]…
> (At least you thought about it ... :-))

I was just using some erudition triggered by the mention
of intrinsic functions. <g>
```

##### ↳ ↳ Re: How to find the greatest of two numbers without using thecomparison operators?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-09-01T11:52:16+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5jrntkF10jikU1@mid.individual.net>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com>`

```


"Frank Swarbrick" <Frank.Swarbrick@efirstbank.com> wrote in message 
news:46D7E17F.6F0F.0085.0@efirstbank.com...
>>>> On 8/31/2007 at 12:41 AM, in message
> <1188542463.524263.317700@i38g2000prf.googlegroups.com>,
…[18 more quoted lines elided]…
>

No, the SIGN test is the answer. (POSITIVE is only one aspect of it...)

Pete.
```

##### ↳ ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2007-08-31T18:13:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<W6Odnc-c-axUM0XbnZ2dnUVZ_q_inZ2d@comcast.com>`
- **In-Reply-To:** `<46D7E17F.6F0F.0085.0@efirstbank.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com> <46D7E17F.6F0F.0085.0@efirstbank.com>`

```
Frank Swarbrick wrote:
>>>> On 8/31/2007 at 12:41 AM, in message
> <1188542463.524263.317700@i38g2000prf.googlegroups.com>,
…[14 more quoted lines elided]…
> Well, I guess there's no IF in that.

You're still going to have to use an IF to tell if MAX became A or B - 
and, this still suffers from the inability to solve the question "what 
if they're equal".

As to why, it smells quite like an educational exercise to teach the 
student that there's more than one way to do things.  :)
```

#### ↳ Re: How to find the greatest of two numbers without using the comparison operators?

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2007-08-31T13:17:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s6jgd359jena7ro2699co0lel2jcbf7ts2@4ax.com>`
- **References:** `<1188542463.524263.317700@i38g2000prf.googlegroups.com>`

```
On Fri, 31 Aug 2007 06:41:03 -0000, Aparajita
<aparajita.mohanty@gmail.com> wrote:

>Hi,
>
…[7 more quoted lines elided]…
>Aparajita

Can't use operators?  How about words?  You know like:

IF A IS GREATER THAN B
  Then do something.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I'm not afraid of dying.  I just don't want to
be there when it happens."
--Woody Allen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
