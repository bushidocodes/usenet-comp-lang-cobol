[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Random number

_8 messages · 8 participants · 1996-10 → 1996-11_

---

### Random number

- **From:** "and..." <ua-author-17087241@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5592fn$360@thor.atcon.com>`

```

I'm looking for how to have cobol pick a random #
between 1-13. My teachers tell me it can't be done
I've written something that does the job but it is not
very effiencient. I accept time and use the last 99
to compute x and then I evluate it with 13 posible result.

If anyone has any ideas I would apreceate them

thank you

Andre LeBlanc
an··.@at··n.com
```

#### ↳ Re: Random number

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08eaa42e7c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5592fn$360@thor.atcon.com>`
- **References:** `<5592fn$360@thor.atcon.com>`

```

and··.@at··n.com (Andre LeBlanc) wrote:

› I'm looking for how to have cobol pick a random #
› between 1-13. My teachers tell me it can't be done
› I've written something that does the job but it is not
› very effiencient. I accept time and use the last 99
› to compute x and then I evluate it with 13 posible result.
 
› If anyone has any ideas I would apreceate them
 
› thank you
 
› Andre LeBlanc
› an··.@at··n.com

Make a number with the clock add the date, rolling in the hours
minutes seconds into one field. That is SEED #1.
Now multiply by PI or sqrt(3) or e ingnore decimals (use 12 digits) or
anything you care to use.
multiply by SEED#1 that is SEED #2. (carry many digits)

Take any two digits out of the middle and
compute RANDNUM = (13.00 * middle2) / 100.00 + 1.00
this gives you a number as a percentage i.e. middle2 / 100.

To generate another SEED#2 take the middle 6 digits of SEED#2 and use
it instead of SEED#1 and repeat.

Neat TRUE story:
In Las Vegas an electronic gambling machine used this type of
technique.

But, it had no battery. So after this PC based machine was turned off
for cleaning (?) and then turned on, the date was 1980 and time
started at midnight. It always used the same SEED#1.

An engineer noticed, after playing the machine, that patterns
repeated. He CLEANED UP. Maybe he new that these machines were
predictable. Big investigation.

The machines were pulled out. Or at least a battery was put in.

JR
```

#### ↳ Re: Random number

- **From:** "steve burns" <ua-author-645539@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08eaa42e7c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5592fn$360@thor.atcon.com>`
- **References:** `<5592fn$360@thor.atcon.com>`

```

Andre LeBlanc wrote:
› 
›         I'm looking for how to have cobol pick a random #
…[10 more quoted lines elided]…
›         an··.@at··n.com

If you have ANSI85 COBOL look for the RANDOM function and find some new
teachers. If you don't tell your teachers to get into the new age...

*****************************************************************
* Steve Burns    The Boeing Co.    I'm not sure if I subscribe  *
* PO Box 3707    Mail Stop 2L-14   to these opinions, I'm sure  *
* (206) 544-8264 Seattle, WA 98124    that Boeing doesn't.      *
```

#### ↳ Re: Random number

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08eaa42e7c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5592fn$360@thor.atcon.com>`
- **References:** `<5592fn$360@thor.atcon.com>`

```

Andre LeBlanc wrote:
›
› I'm looking for how to have cobol pick a random #
› between 1-13. My teachers tell me it can't be done

I find it really hard to believe that your teachers would tell you that. Can it
be done in C ? Can it be done in BASIC ? Yes, so it seems reasonable that it can
also be done in COBOL, then :)

›         I've written something that does the job but it is not
›         very effiencient. I accept time and use the last 99
›         to compute x and then I evluate it with 13 posible result.
› 
›         If anyone has any ideas I would apreceate them

If your COBOL supports it, you could call a standard library function that will
do it for you (on Unix, type "man rand" for an example).

Alternatively, for an ANSI-Standard COBOL version, checking whether your COBOL
compiler supports Intrinsic Functions would be a good start. You'll find some
useful stuff there.

Having said that - is this for an assignment ? If so, you might want to think
more about what the purpose of the assignment is. If it's to test what you know
about random number generation, then calling a system routine or whatever that
just hands you one on a plate is not going to get you many marks - your current
solution, however unelegant, will probably be preferable.

Of course, in the "real world", it's the *end result* that is often considered
more important, not the method!

Cheers, Kev.
```

#### ↳ Re: Random number

- **From:** "arnold...." <ua-author-6589409@usenetarchives.gap>
- **Date:** 1996-11-01T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08eaa42e7c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5592fn$360@thor.atcon.com>`
- **References:** `<5592fn$360@thor.atcon.com>`

```

and··.@at··n.com (Andre LeBlanc) wrote:

› I'm looking for how to have cobol pick a random #
› between 1-13. My teachers tell me it can't be done
› I've written something that does the job but it is not
› very effiencient. I accept time and use the last 99
› to compute x and then I evluate it with 13 posible result.
 
› If anyone has any ideas I would apreceate them
 
› thank you
 
› Andre LeBlanc
› an··.@at··n.com

There is a good routine for generating random numbers called the
Linear Congruence algorithm, LC for short. It was published in "The
Art of Computer Programming, Volume II, Semi-Numerical Algorithms" by
Donald E. Knuth, 1981 (Addison-Wesley Publishing Company). It is easy
to implement and gives statistically good results, but is considered
to be too predictable for cryptographic purposes. It's good enough
for games or simulations.

The general formula goes something like this:

R2 = ((R1 * Multiplier) + Adder) mod wordsize

R1 = The random number seed, or the previous number in the sequence of
pseudorandom numbers.

R2 = The next number in the pseudorandom series

Multiplier = The number the R1 seed is multiplied by. For decimal
numbers, Multiplier mod 200 should equal 21. For binary numbers, the
multiplier mod 8 should equal 5. This is based on some old notes I
have which suggest you get a better distribution of values.

Adder = Another number to modifiy the result, making the next
pseudorandom number just a little less obvious to predict.

wordsize = This is your truncation factor. For COBOL, you can
implement this by taking the REMAINDER of a DIVIDE, or if you are
working on decimal numbers, you can just truncate on a certain number
of digits.

For example, if you want to generate pseudorandom numbers from 000 to
999, you could do it like this:

01 random-number-workarea.
05 random-number pic 9(3) value zero.
05 seed pic 9(6) value zero.
05 multiplier pic 9(3) value 221.
05 adder pic 9(3) value 901.

Compute seed = ((random-number * multiplier) + adder.
move seed to random-number.

So if we initialize random number to zero, we should get the following
sequence of numbers: 0, 901, 158, 955, 92, 369, 586, 543, 40, 877,
854, et cetera.

To convert this to a range of numbers from 1 to 13, just divide
random-number by 13, take the remainder and add 1 to it.

There are more complicated formulas for generating random numbers, and
many of them are associated with cryptography. Linear Congruence is
not good enough for that, but works very well for games or
simulations.

I hope this helps!

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

##### ↳ ↳ Re: Random number

- **From:** "steve williams" <ua-author-529495@usenetarchives.gap>
- **Date:** 1996-11-02T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08eaa42e7c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-08eaa42e7c-p5@usenetarchives.gap>`
- **References:** `<5592fn$360@thor.atcon.com> <gap-08eaa42e7c-p5@usenetarchives.gap>`

```

Arnold J. Trembley wrote:

›
› The general formula goes something like this:
›
› R2 = ((R1 * Multiplier) + Adder) mod wordsize
›

I seem to remember another Knuth algo for pseudo random numbers which
uses an array of numbers, referencing array(24) and array(55) to produce
the next number, which was supposed to be pretty good and with a very
long cycle. Can anyone elaborate on this one?

Steve.


?????????????????????????????????????????????
??? exp··.@cel··o.uk
??? http://www.yi.com/home/WilliamsSteve
?????????????????????????????????????????????
```

##### ↳ ↳ Re: Random number

- **From:** "chris borgnaes" <ua-author-12407404@usenetarchives.gap>
- **Date:** 1996-11-06T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08eaa42e7c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-08eaa42e7c-p5@usenetarchives.gap>`
- **References:** `<5592fn$360@thor.atcon.com> <gap-08eaa42e7c-p5@usenetarchives.gap>`

```

There are compilers that allow intrinsic functions, including a random
function. They are available for COBOL85, which I'm guessing you don't
have access to at school. Just the same, here's what it would look like at
my site:

01 Random-1-13 PIC 99.
...Compute Random-1-13 = 1 + (12 * FUNCTION RANDOM).

If you don't have access to COBOL85, you should. Tell your profs they
ought to look into it. Unless they're trying to teach you random number
theory there's not much reason to have to define an algorithm for yourself.

Arnold J. Trembley wrote in article
<55egli$g.··.@mti··t.net>...
› and··.@at··n.com (Andre LeBlanc) wrote:
› 
…[12 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Random number

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-11-13T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08eaa42e7c-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-08eaa42e7c-p7@usenetarchives.gap>`
- **References:** `<5592fn$360@thor.atcon.com> <gap-08eaa42e7c-p5@usenetarchives.gap> <gap-08eaa42e7c-p7@usenetarchives.gap>`

```

I'm reposting an old article on this subject:

"Well, since no one is providing aid and confort, I'll give a hint.
One, learn and understand how to use COMP-1 and COMP-2 for single and
double-precision integers. Two, use the system's time as the seed
number and get a new time before generating a random number. Three,
find a book on algorithms so you can understand the following formula:

" (((seed * 1103515245) + 12345) / 65536) / 32768 = quotent with
remainder

"The remainder is your pseudo-random number. I found this formula in
the book "The Annotated ANSI C Library" - well, acutally it's C code
for the random number function which I made into the above formula.
The translation from C to COBOL is straight-forward but avoid using
COMPUTE as I found the results can get weird.

"Of course, the above is subject to review and flames."


"Chris Borgnaes" wrote:

› There are compilers that allow intrinsic functions, including a random
› function.  They are available for COBOL85, which I'm guessing you don't
› have access to at school.  Just the same, here's what it would look like at
› my site:
 
› 01  Random-1-13  PIC 99.
›    ...Compute Random-1-13 = 1 + (12 * FUNCTION RANDOM).
 
› If you don't have access to COBOL85, you should.  Tell your profs they
› ought to look into it.  Unless they're trying to teach you random number
› theory there's not much reason to have to define an algorithm for yourself.
 
› Arnold J. Trembley  wrote in article
› <55egli$g.··.@mti··t.net>...
…[14 more quoted lines elided]…
›› 

Hope this helps
Boyce G. Williams, Jr.

.---------------------------------------------------------------------.
| "People should have two virtues: purpose- the courage to envisage |
| and pursue valued goals uninhibited by the defeat of infantile |
| fantasies, by guilt and the failing fear punishment; and wisdom- a |
| detached concern with life itself, in the face of death itself." |
| Norman F. Dixon |
'---------------------------------------------------------------------'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
