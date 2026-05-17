[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Unstring statement

_6 messages · 4 participants · 1998-04_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Unstring statement

- **From:** "mark" <ua-author-10783@usenetarchives.gap>
- **Date:** 1998-04-28T14:34:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35462255.5A32@leaguedata.com>`

```

Hello all !

I have the following problem: I need to take a date field and unstring
it so that I can populate my print record with this same date in the
following format, APR 28, 1998 . The date field has a format of PIC
9(10). I know that unstring will not work on a numeric field so I can
just move this date field into a holding field which is alphanumeric.
The question is how do I take the first 4 characters and move them into
a YEAR field, take the next 2 characters and move them into a MONTH
field, and take the last two characters and move them into a DAY field
? None of my resources adequately describes the UNSTRING statement so
I'm unclear as to how to proceed. Any help that you could offer would
be greatly appreciated.

Thanks in advance
Mark
```

#### ↳ Re: Unstring statement

- **From:** "hank" <ua-author-88501@usenetarchives.gap>
- **Date:** 1998-04-27T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff4212bca1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35462255.5A32@leaguedata.com>`
- **References:** `<35462255.5A32@leaguedata.com>`

```

Mark wrote in article
<354··.@lea··a.com>...
› Hello all !
› 
…[13 more quoted lines elided]…
› Mark

How about WS-DATE(1:4) to year, WS-DATE(5:2) to month, WS-DATE(9:2). This
still doesn't make sense, What format is the date in...at?(note: double
prepositions cancel each other out).
Shoot, just drop the class.
Hank Ingram 
Programmer,Tea-drinker, former corporate stooge,  member of the dreaded
Religious Right  @ http://www.nr.infi.net/~hingram
Needlessly consuming valuable resources in Blacksburg, Va
```

##### ↳ ↳ Re: Unstring statement

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-04-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff4212bca1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ff4212bca1-p2@usenetarchives.gap>`
- **References:** `<35462255.5A32@leaguedata.com> <gap-ff4212bca1-p2@usenetarchives.gap>`

```

On 28 Apr 1998 19:31:38 GMT, "Hank" wrote:

› Shoot, just drop the class.
› --
› Hank Ingram

darn, why didn't I think of that? this wasn't "real work", was it?
just another #%$@& 'class problem'.... I'm getting sick of playing
'homework monitor'.... thanks, Hank, for cutting through this. I'm
wasting my time ..... :-)

david

David d.s··.@ix.··m.com
____________________________________
```

#### ↳ Re: Unstring statement

- **From:** "sff..." <ua-author-4762962@usenetarchives.gap>
- **Date:** 1998-04-27T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff4212bca1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<35462255.5A32@leaguedata.com>`
- **References:** `<35462255.5A32@leaguedata.com>`

```

In article <354··.@lea··a.com>, Mark writes:

› I have the following problem:  I need to take a date field and unstring
› it so that I can populate my print record with this same date in the
…[9 more quoted lines elided]…
› 

Unstring may not be what you want to use, especially since you have no
delimiter on which to break the fields. How exactly is the date formatted
in the PIC 9(10) area as you have only defined 8-digits of information to
extract. Personally, I would either move the field to an area that has the
proper redefines below it to support the formatting of the incoming field
or use relative indexing to move the pieces to numeric defined elements
for report formatting and subscript/index usage.

Hope that this points you in the right direction.
```

##### ↳ ↳ Re: Unstring statement

- **From:** "mark" <ua-author-10783@usenetarchives.gap>
- **Date:** 1998-04-29T07:24:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff4212bca1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ff4212bca1-p4@usenetarchives.gap>`
- **References:** `<35462255.5A32@leaguedata.com> <gap-ff4212bca1-p4@usenetarchives.gap>`

```

Sff5ky wrote:
› 
› In article <354··.@lea··a.com>, Mark  writes:
…[22 more quoted lines elided]…
› Hope that this points you in the right direction.


Thank you all for taking the time to reply. Not long after my post I
actually figured it out on my own ! :-) I used the move statement
syntax that many of you suggested and of course it worked. I guess that
I WAS making a simple problem more complex because I was hung up on the
UNSTRING statement. Chalk it up to lack of experience with the
subtleties of COBOL. Anyway, I do appreciate your time.. thanks again.

Mark
```

#### ↳ Re: Unstring statement

- **From:** "d.s..." <ua-author-6569161@usenetarchives.gap>
- **Date:** 1998-04-27T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff4212bca1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<35462255.5A32@leaguedata.com>`
- **References:** `<35462255.5A32@leaguedata.com>`

```

On Tue, 28 Apr 1998 18:34:38 GMT, Mark wrote:

› Hello all !
› 
…[13 more quoted lines elided]…
› Mark

Mark, what you might want to consider is STRING. I say this because
you have a well-defined input field -- you know the length of each
data component- using string delimited by size can do this, but if you
have cobol II or higher you can directly access the bytes (called
'reference modification')

however - having said the above, it's all overkill. since you know the
contents of each subgroup of bytes, why not just redefine the 10 byte
field and do 3 moves? My inference is that this is a simple issue and
you're looking for complex solutions.... I always try to write code so
a junior programmer can figure it out -- then I can go on to other
things.... good luck.
david

David d.s··.@ix.··m.com
____________________________________
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
