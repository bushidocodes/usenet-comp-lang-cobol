[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Value clause

_8 messages · 7 participants · 1994-11 → 1994-12_

---

### Value clause

- **From:** "s..." <ua-author-7149047@usenetarchives.gap>
- **Date:** 1994-11-29T16:29:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bfv2m$t0@news.tamu.edu>`

```
How can you include an apostrophe in a value clause. This won't work:
01 field-a pic x(30) value " sam's club".

Does anyone know what will work ???
```

#### ↳ Re: Value clause

- **From:** "cgo..." <ua-author-7675889@usenetarchives.gap>
- **Date:** 1994-11-29T19:27:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bff0c8e4c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3bfv2m$t0@news.tamu.edu>`
- **References:** `<3bfv2m$t0@news.tamu.edu>`

```
In <3bfv2m$t.··.@new··u.edu>, s.··.@tam··u.edu (Steve Browning) writes:
› How can you include an apostrophe in a value clause. This won't work:
› 01 field-a pic x(30) value " sam's club".
›
› Does anyone know what will work ???
›
Yes
use ' sam''s club' *> the double quote indicates it's an imbended quote. That a double apostrophy (') not (")
Charles Godwin
```

##### ↳ ↳ Re: Value clause

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1994-11-29T21:14:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bff0c8e4c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2bff0c8e4c-p2@usenetarchives.gap>`
- **References:** `<3bfv2m$t0@news.tamu.edu> <gap-2bff0c8e4c-p2@usenetarchives.gap>`

```
On 30 Nov 1994 00:27:05 GMT, Charles Godwin (cgo··.@i··.net) wrote:
› In <3bfv2m$t.··.@new··u.edu>, s.··.@tam··u.edu (Steve Browning) writes:
›› How can you include an apostrophe in a value clause.  This won't work:	
…[6 more quoted lines elided]…
› Charles Godwin

Also your compiler may have an option for using qoutes instead of
apostrophes. On IBM mainframes it's 'APOST/QUOTE'.
```

##### ↳ ↳ Re: Value clause

- **From:** "s..." <ua-author-7149047@usenetarchives.gap>
- **Date:** 1994-12-01T14:33:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bff0c8e4c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2bff0c8e4c-p2@usenetarchives.gap>`
- **References:** `<3bfv2m$t0@news.tamu.edu> <gap-2bff0c8e4c-p2@usenetarchives.gap>`

```
The double apostrophies worked great. Thanks for your help.
```

#### ↳ Re: Value clause

- **From:** "lgree..." <ua-author-17073836@usenetarchives.gap>
- **Date:** 1994-11-29T23:08:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bff0c8e4c-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3bfv2m$t0@news.tamu.edu>`
- **References:** `<3bfv2m$t0@news.tamu.edu>`

```
In article <3bfv2m$t.··.@new··u.edu>
s.··.@tam··u.edu (Steve Browning) writes:

› How can you include an apostrophe in a value clause. This won't work:
› 01 field-a pic x(30) value " sam's club".

You need to put two (2) consecutive single quotes together...

01 field-a pic x(30) value 'sam''s club'
....field-a will now contain .... sam's club

Lawrence H. Greenwald (lgr··.@pow··i.com>
"I'm looking over a three leaf clover that I overlooked be-three!"
--Bugs Bunny
```

##### ↳ ↳ Re: Value clause

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1994-12-02T10:16:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bff0c8e4c-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-2bff0c8e4c-p5@usenetarchives.gap>`
- **References:** `<3bfv2m$t0@news.tamu.edu> <gap-2bff0c8e4c-p5@usenetarchives.gap>`

```
Suggestion on newsgroup procedures, when someone asks a trivial question
(in this case how do I put a quote in a string, a question which one would
think anyone who can read and has a manual should be able to figure out
on their own), if you *do* feel like replying, send email, don't post to
the group. That cuts down on noise messages. It is particularly useless
to post a reply to the group late, long after answers have already been
posted.

Always read a thread to the end before posting any replies, that helps to
avoid unnecessary duplication of replies.
```

#### ↳ Re: Value clause

- **From:** "wc..." <ua-author-17073886@usenetarchives.gap>
- **Date:** 1994-12-02T11:36:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-2bff0c8e4c-p7@usenetarchives.gap>`
- **In-Reply-To:** `<3bfv2m$t0@news.tamu.edu>`
- **References:** `<3bfv2m$t0@news.tamu.edu>`

```

In article <3bfv2m$t.··.@new··u.edu>, writes:
›
› How can you include an apostrophe in a value clause. This won't work:
› 01 field-a pic x(30) value " sam's club".
›
› Does anyone know what will work ???


I can only answer from my experience in the IBM world; there we use single
quotes (apostrophes) to delineate non-numeric literals. In this case, two
single quotes in a row are interpreted as part of the literal, ie:

value ' sam''s club'

would give you a correctly punctuated literal.

You could try this, although I would have expected that if regular quote marks
were used to delineate non-numeric literals, you shouldn't have problems
putting anything between them other than quote marks.
```

#### ↳ Re: Value clause

- **From:** wcivy@adpc.purdue.edu
- **Date:** 1994-12-02T09:36:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bnbo5$7g5@mozo.cc.purdue.edu>`
- **References:** `<3bfv2m$t0@news.tamu.edu>`

```

In article <3bfv2m$t0@news.tamu.edu>, <srb@tamvm1.tamu.edu> writes:
> 
> How can you include an apostrophe in a value clause.  This won't work:	
> 	01  field-a        pic x(30) value " sam's club".		 
>  									 
>  Does anyone know what will work ???


I can only answer from my experience in the IBM world; there we use single 
quotes (apostrophes) to delineate non-numeric literals.  In this case, two 
single quotes in a row are interpreted as part of the literal, ie:
    
    value ' sam''s club'

would give you a correctly punctuated literal.  

You could try this, although I would have expected that if regular quote marks 
were used to delineate non-numeric literals, you shouldn't have problems 
putting anything between them other than quote marks.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
