[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Math problem

_7 messages · 5 participants · 1997-04_

---

### Math problem

- **From:** "flying dutchman" <ua-author-583956@usenetarchives.gap>
- **Date:** 1997-04-25T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc5261$78017cc0$084718c3@tom-s-133>`

```

I'm looking for two fast ANSI 85 Cobol math routines:

1. one which returns the week number of a given date in yyyymmdd format
2. and another which checks whether a given number (S9(9) Comp) is a prime
and if not returns the next higher prime number.

Thanks in advance for your help,

Tom
```

#### ↳ Re: Math problem

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1997-04-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac44f433ea-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5261$78017cc0$084718c3@tom-s-133>`
- **References:** `<01bc5261$78017cc0$084718c3@tom-s-133>`

```

In message <<01bc5261$78017cc0$084718c3@tom-s-133>> "Flying Dutchman" writes:
› I'm looking for two fast ANSI 85 Cobol math routines:
› 
…[6 more quoted lines elided]…
› Tom

These do look very much like 'do my homework for me please'.
```

##### ↳ ↳ Re: Math problem

- **From:** "flying dutchman" <ua-author-583956@usenetarchives.gap>
- **Date:** 1997-04-26T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac44f433ea-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac44f433ea-p2@usenetarchives.gap>`
- **References:** `<01bc5261$78017cc0$084718c3@tom-s-133> <gap-ac44f433ea-p2@usenetarchives.gap>`

```


Richard Plinston wrote
› These do look very much like 'do my homework for me please'.

I really like your comment and must admit that I am a rather lazy
programmer.
On the other hand, I somewhere read the saying:

Bad programmer write bad code
Good programmers write good code
Excellent programmers steal good code.

Ciao,

Tom.
```

#### ↳ Re: Math problem

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-04-27T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac44f433ea-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5261$78017cc0$084718c3@tom-s-133>`
- **References:** `<01bc5261$78017cc0$084718c3@tom-s-133>`

```

#1 - week number - is easy - if you would define "week number". Use the
intrinsic function INTEGER OF DATE to get a "lillian style" date, subtract
off the YYYY0101 function value - leaves day of year - then DIVIDE to get
week number (with adjustments for your definition of week number). You
can use the remainder from the division - will be a function of the day
of week to further adjust "week number".

COBOL's "Lillian style" date from the intrinsics starts with day 1 as a
Monday, so you can always tell the day of the week.
Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

#### ↳ Re: Math problem

- **From:** "flying dutchman" <ua-author-583956@usenetarchives.gap>
- **Date:** 1997-04-27T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac44f433ea-p5@usenetarchives.gap>`
- **In-Reply-To:** `<01bc5261$78017cc0$084718c3@tom-s-133>`
- **References:** `<01bc5261$78017cc0$084718c3@tom-s-133>`

```

Thanks for your help.

The weeknumber problem was a bit complex for me, because the 'logic' used
in my company is that the first week of a year should have more than 3 days
in it. Luckily I found an old Pascal routine on an old discarded CD rom,
which did that trick

For the prime number problem, I don't have a solution yet but I assume that
I'll have to use the Sieve of Eusthasias (hope I've got that name right),
with some extra controls.

Thanks again,

Tom
```

##### ↳ ↳ Re: Math problem

- **From:** "bob howell" <ua-author-4683081@usenetarchives.gap>
- **Date:** 1997-04-28T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac44f433ea-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac44f433ea-p5@usenetarchives.gap>`
- **References:** `<01bc5261$78017cc0$084718c3@tom-s-133> <gap-ac44f433ea-p5@usenetarchives.gap>`

```

Flying Dutchman wrote:
› 
› Thanks for your help.
…[9 more quoted lines elided]…
› Close.  Its the "Sieve of Eratosthenes", a systematic procedure for 
isolating prime numbers, invented by Eratosthenes of Cyrene, a
younger contemporary of Archimedes and Aristarchus, more noted for
making one of the most successful early measurements of the
circumference of the earth.
--------------------------------
Bob Howell
Pensacola, Florida
Mailto:rah··.@wor··t.net
```

###### ↳ ↳ ↳ Re: Math problem

- **From:** "noel p.c. ng" <ua-author-17072875@usenetarchives.gap>
- **Date:** 1997-04-30T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ac44f433ea-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ac44f433ea-p6@usenetarchives.gap>`
- **References:** `<01bc5261$78017cc0$084718c3@tom-s-133> <gap-ac44f433ea-p5@usenetarchives.gap> <gap-ac44f433ea-p6@usenetarchives.gap>`

```

Check my Prime Number page :: http://www.mtnlake.com/â€¾noelng/prime.htm
I have a JavaScript version that you may be able to adapt.

Noel Ng
Consultant,
Toronto Canada

Bob Howell wrote:
› 
› Flying Dutchman wrote:
…[19 more quoted lines elided]…
› Mailto:rah··.@wor··t.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
