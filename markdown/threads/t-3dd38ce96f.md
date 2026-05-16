[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mersenne Twister RNG

_8 messages · 5 participants · 2006-10_

---

### Mersenne Twister RNG

- **From:** "djeanne" <djeanne75@gmail.com>
- **Date:** 2006-10-06T05:18:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com>`

```
Hi all,

I am back with random number generators.
Does anybody know of a Mersenne Twister implementation under Cobol,
including SHA-1 disturbance so as to avoid predictability ?

The random generator under Cobol I am looking for shoud generate
uniformly distributed numbers and it should also be unpredictable
(which means, you cannot guess the seed by observing a few outputs).

Basic generators such as "modulo random generators" are quite week
from this point of view but I read Mersenne Twister with SHA-1 was
good.

Do you know about it ?

Thanks in advance,

Djeanne.
```

#### ↳ Re: Mersenne Twister RNG

- **From:** "HeyBub" <heybubNOSPAM@gmail.com>
- **Date:** 2006-10-06T10:02:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<12ics0atj0hr77a@news.supernews.com>`
- **References:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com>`

```
djeanne wrote:
> Hi all,
>
…[16 more quoted lines elided]…
> Djeanne.

The accounting department where Dilbert works has a random-generator troll. 
He simply says "Nine, nine, nine..."

When Dilbert observed that the numbers didn't seem random, the head 
accounting troll said: "With random numbers you can never be sure..."

(Yeah, I know there are tests for randomness, but it made a good comic.)
```

##### ↳ ↳ Re: Mersenne Twister RNG

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-10-06T10:38:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160156292.245322.164890@b28g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<12ics0atj0hr77a@news.supernews.com>`
- **References:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com> <12ics0atj0hr77a@news.supernews.com>`

```

HeyBub wrote:
> djeanne wrote:
> > Hi all,
…[4 more quoted lines elided]…
> >

I would have thought that assembler would make for a better random
number generator than cobol.

> > Thanks in advance,
> >
…[3 more quoted lines elided]…
> He simply says "Nine, nine, nine..."

Obviously spent too much time listening to the beatles

>
> When Dilbert observed that the numbers didn't seem random, the head
> accounting troll said: "With random numbers you can never be sure..."
>
> (Yeah, I know there are tests for randomness, but it made a good comic.)

The law of large numbers dictates that any sequence would eventually
repeat (perhaps ad nauseum) so maybe the troll was right?
```

##### ↳ ↳ Re: Mersenne Twister RNG

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-10-06T10:47:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160156849.257065.305810@e3g2000cwe.googlegroups.com>`
- **In-Reply-To:** `<12ics0atj0hr77a@news.supernews.com>`
- **References:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com> <12ics0atj0hr77a@news.supernews.com>`

```

HeyBub wrote:
> djeanne wrote:
> > Hi all,
…[3 more quoted lines elided]…
> > including SHA-1 disturbance so as to avoid predictability ?

I wouldn't have thought that Cobol would be particularly good at random
number gerneration.

> >
> >
…[3 more quoted lines elided]…
> He simply says "Nine, nine, nine..."

Obviously listened to the Beatles too much.

>
> When Dilbert observed that the numbers didn't seem random, the head
> accounting troll said: "With random numbers you can never be sure..."
>
> (Yeah, I know there are tests for randomness, but it made a good comic.)

There is no reason why a random number generator could not generate a
sequence of nines. The longer the series generated the more likely it
is that nine would repeat (possibly ad nauseum).
```

#### ↳ Re: Mersenne Twister RNG

- **From:** SkippyPB <swiegand@neo.rr.NOSPAM.com>
- **Date:** 2006-10-07T13:45:14-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hrpfi2da885jknp0kh5r8r4hu3h5hl93om@4ax.com>`
- **References:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com>`

```
On 6 Oct 2006 05:18:49 -0700, "djeanne" <djeanne75@gmail.com>
enlightened us:

>Hi all,
>
…[3 more quoted lines elided]…
>

I don't know of one but if you Google Mersenne Twister you'll find a C
solution which you could either use as a subroutine or translate into
Cobol.

>The random generator under Cobol I am looking for shoud generate
>uniformly distributed numbers and it should also be unpredictable
…[10 more quoted lines elided]…
>Djeanne.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-


"I want to share something with you the three sentences that 
will get you through life. 
Number one, 'Cover for me.' 
Number two,'Oh, good idea, boss.' 
Number three, 'It was like that when I got here.'"
-- Homer Simpson
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: Mersenne Twister RNG

- **From:** "ski" <t4na5nb02@sneakemail.com>
- **Date:** 2006-10-08T14:01:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160341315.579573.293620@c28g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com>`
- **References:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com>`

```

djeanne wrote:
> Hi all,
>
…[3 more quoted lines elided]…
> Do you know about it ?

Use existing C routines, and CALL it from COBOL.
```

##### ↳ ↳ Re: Mersenne Twister RNG

- **From:** "djeanne" <djeanne75@gmail.com>
- **Date:** 2006-10-09T04:53:50-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160394830.083351.64310@k70g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1160341315.579573.293620@c28g2000cwb.googlegroups.com>`
- **References:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com> <1160341315.579573.293620@c28g2000cwb.googlegroups.com>`

```


The problem is, the existing C routines I found don't include SHA-1.
Does anybody know of a complete implementation ?

djeanne

ski wrote:
> djeanne wrote:
> > Hi all,
…[6 more quoted lines elided]…
> Use existing C routines, and CALL it from COBOL.
```

###### ↳ ↳ ↳ Re: Mersenne Twister RNG

- **From:** "ski" <t4na5nb02@sneakemail.com>
- **Date:** 2006-10-09T05:36:09-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1160397369.828090.207590@m7g2000cwm.googlegroups.com>`
- **In-Reply-To:** `<1160394830.083351.64310@k70g2000cwa.googlegroups.com>`
- **References:** `<1160137128.813729.178440@k70g2000cwa.googlegroups.com> <1160341315.579573.293620@c28g2000cwb.googlegroups.com> <1160394830.083351.64310@k70g2000cwa.googlegroups.com>`

```

djeanne wrote:
> The problem is, the existing C routines I found don't include SHA-1.
> Does anybody know of a complete implementation ?
google? :)
http://www-personal.engin.umich.edu/~wagnerr/MersenneTwister.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
