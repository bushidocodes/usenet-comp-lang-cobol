[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rosetta Code

_12 messages · 6 participants · 2020-02_

---

### Rosetta Code

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2020-02-04T20:59:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h9ulrjF2mjtU1@mid.individual.net>`

```

Well, retirement boredom has finally got to me. I looked at
Rosetta Code and was amazed at how many tasks did not have a
COBOL solution. So I started doing some....

I have uploaded versions of 99 Bottles of Beer and Nth Root.
The first is cute and uses sequential files in a very typical
COBOL manner.

The second, Finding the Nth Root of a Number is a math problem
and not typical COBOL, but the task was done easily in COBOL
anyway.

Now to decide which one I want to do next...

bill
```

#### ↳ Re: Rosetta Code

- **From:** "houten.van" <ua-author-14501871@usenetarchives.gap>
- **Date:** 2020-02-05T06:41:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p2@usenetarchives.gap>`
- **In-Reply-To:** `<h9ulrjF2mjtU1@mid.individual.net>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net>`

```
Le 05/02/2020 à 02:59, Bill Gunshannon a écrit :
› 
› Well, retirement boredom has finally got to me.  I looked at
…[14 more quoted lines elided]…
› 

I went to visit the site that I didn't know. Very interesting!

But, for the Nth root in particular:

It's a bit strange as most programs use the "pow" function, or ** in COBOL.

If you are allowed to use it, why don't you just write:
x**(1/n)

??

Guillaume.
```

##### ↳ ↳ Re: Rosetta Code

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2020-02-05T12:28:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p2@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p2@usenetarchives.gap>`

```
On 2/5/20 6:41 AM, Arachide wrote:
› Le 05/02/2020 à 02:59, Bill Gunshannon a écrit :
›› 
…[26 more quoted lines elided]…
› ??

The way I read the requirement (and I guess everyone else as
no one did it that way) a particular algorithm was required.
Plus the optional need for specifying Precision. I just
read a bunch of the other language implementations (at least
the ones where I know the language!) and implemented it
accordingly.

bill
```

###### ↳ ↳ ↳ Re: Rosetta Code

- **From:** "houten.van" <ua-author-14501871@usenetarchives.gap>
- **Date:** 2020-02-06T07:55:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p3@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p2@usenetarchives.gap> <gap-16dd3bcd67-p3@usenetarchives.gap>`

```
Le 05/02/2020 à 18:28, Bill Gunshannon a écrit :

› The way I read the requirement (and I guess everyone else as
› no one did it that way) a particular algorithm was required.
…[3 more quoted lines elided]…
› accordingly.

Sure, that's what I understood.
But, that was just a little remark...

The same when my pupils have to calculate one side of an triangle, they
take their ruler, get the measurement of the two other sides and use
Pythagoras' theorem.
Why don't you use rirectly the ruler on the third side that you want?

:-)

Guillaume.
›
› bill
›
```

###### ↳ ↳ ↳ Re: Rosetta Code

_(reply depth: 4)_

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2020-02-06T09:04:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p4@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p2@usenetarchives.gap> <gap-16dd3bcd67-p3@usenetarchives.gap> <gap-16dd3bcd67-p4@usenetarchives.gap>`

```
In article ,
Arachide wrote:

[snip]

› The same when my pupils have to calculate one side of an triangle, they 
› take their ruler, get the measurement of the two other sides and use 
› Pythagoras' theorem.
› Why don't you use rirectly the ruler on the third side that you want?

'You have been instructed to calculate the third side, not to measure
it, and calculate it you will. Thank you for reminding me to request that
you show your work, as well.

DD
```

###### ↳ ↳ ↳ Re: Rosetta Code

_(reply depth: 4)_

- **From:** "robin.vowels" <ua-author-13497444@usenetarchives.gap>
- **Date:** 2020-02-08T06:08:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p4@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p2@usenetarchives.gap> <gap-16dd3bcd67-p3@usenetarchives.gap> <gap-16dd3bcd67-p4@usenetarchives.gap>`

```
On Thursday, February 6, 2020 at 11:55:45 PM UTC+11, Arachide wrote:
› Le 05/02/2020 à 18:28, Bill Gunshannon a écrit :
› 
…[12 more quoted lines elided]…
› Pythagoras' theorem.

Pythagoras's Theorem is for right-angled triangles only,
not for any old triangle.

› Why don't you use rirectly the ruler on the third side that you want?
```

###### ↳ ↳ ↳ Re: Rosetta Code

- **From:** "snetxa" <ua-author-7470312@usenetarchives.gap>
- **Date:** 2020-02-09T07:37:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p3@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p2@usenetarchives.gap> <gap-16dd3bcd67-p3@usenetarchives.gap>`

```
On 2/6/2020 1:28 AM, Bill Gunshannon wrote:
› I just
› read a bunch of the other language implementations (at least
› the ones where I know the language!) and implemented it
› accordingly.
Which is how I've done most of my contributions. Another thing you can
do, and I've done it once or twice, is to contribute a task, e.g.
"Teacup rim text".

-- Bruce (on RosettaCode as "Axtens")
```

###### ↳ ↳ ↳ Re: Rosetta Code

_(reply depth: 4)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2020-02-09T12:10:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p7@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p2@usenetarchives.gap> <gap-16dd3bcd67-p3@usenetarchives.gap> <gap-16dd3bcd67-p7@usenetarchives.gap>`

```
On 2/9/20 7:37 AM, Bruce Axtens wrote:
› On 2/6/2020 1:28 AM, Bill Gunshannon wrote:
›› I just
…[5 more quoted lines elided]…
› "Teacup rim text".

I don't see myself creating any tasks as there are plenty to go around.
I do have one minor nit to pick, however.

The challenge is to use language A to accomplish task B.
Many of them are cases of using language A to call a subroutine
in language C to do task B. Any I do will have the work actually
done in the language I choose to use. But, to each his own.

bill
```

###### ↳ ↳ ↳ Re: Rosetta Code

_(reply depth: 5)_

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2020-02-09T13:54:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p8@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p2@usenetarchives.gap> <gap-16dd3bcd67-p3@usenetarchives.gap> <gap-16dd3bcd67-p7@usenetarchives.gap> <gap-16dd3bcd67-p8@usenetarchives.gap>`

```


Added my next one.

Parsing/RPN calculator algorithm

This is turning out to be m ore fun than I expected. It also
shows some interesting shortcomings of COBOL which, as programmers,
we always seemed to work around. I really miss those days.

bill
```

#### ↳ Re: Rosetta Code

- **From:** "jmccue" <ua-author-8301969@usenetarchives.gap>
- **Date:** 2020-02-05T07:17:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p10@usenetarchives.gap>`
- **In-Reply-To:** `<h9ulrjF2mjtU1@mid.individual.net>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net>`

```
Bill Gunshannon wrote:
› 
› Well, retirement boredom has finally got to me.  I looked at
› Rosetta Code and was amazed at how many tasks did not have a
› COBOL solution.  So I started doing some....
 
› Never knew that site existed.
 
› 
› I have uploaded versions of 99 Bottles of Beer and Nth Root.
› The first is cute and uses sequential files in a very typical
› COBOL manner.
› 

Checked it out, nice.



› Now to decide which one I want to do next...

An interesting article to read:

https://medium.com/@bellmar/is-cobol-holding-you-hostage-with-math-5498c0eb428b

showing in some cases COBOL can gave better numeric results

›
› bill
›
```

#### ↳ Re: Rosetta Code

- **From:** "bill.gunshannon" <ua-author-12020547@usenetarchives.gap>
- **Date:** 2020-02-05T18:40:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p11@usenetarchives.gap>`
- **In-Reply-To:** `<h9ulrjF2mjtU1@mid.individual.net>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net>`

```
On 2/4/20 8:59 PM, Bill Gunshannon wrote:
› 
› Well, retirement boredom has finally got to me.  I looked at
…[5 more quoted lines elided]…
› COBOL manner.

My mistake. My 99 Bottles in COBOL was for another site.
Someone else had already done it on Rosetta Code.

The first COBOL Program I put on Rosetta Code was Word Frequency.
That was a fun one. A simple parser and then typical COBOL file
handling to count all the words.

bill
```

##### ↳ ↳ Re: Rosetta Code

- **From:** "snetxa" <ua-author-7470312@usenetarchives.gap>
- **Date:** 2020-02-09T07:45:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-16dd3bcd67-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-16dd3bcd67-p11@usenetarchives.gap>`
- **References:** `<h9ulrjF2mjtU1@mid.individual.net> <gap-16dd3bcd67-p11@usenetarchives.gap>`

```
On 2/6/2020 7:40 AM, Bill Gunshannon wrote:
› My mistake.Â  My 99 Bottles in COBOL was for another site.
› Someone else had already done it on Rosetta Code.

Umm, yeah, that was me. I learned COBOL in a diploma level course and
subsequent never used it. Everything on RosettaCode is open for
modification, so if you with your years of real-world experience see
something that could be done better (or at least less naively) just go
ahead and change it.

That applies to everything, not just my code.

-- Bruce.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
