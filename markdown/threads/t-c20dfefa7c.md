[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Division and Remainders

_4 messages · 3 participants · 1998-03_

---

### Division and Remainders

- **From:** "robert mezzone" <ua-author-742348@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6eqf8q$jqg@taro.futuris.net>`

```

I'm taking my first COBOL class this semester and find it pretty
interesting, and a lot easier than I expected (just finished writing my
first two control-break program). Anyhow I've been reviewing for a test I
have next week and the only thing I'm having a problem understanding is
determining the remainder when you perform division. I know this sounds
really dumb but I just can't seem to understand it with the few examples
given in the book, and unfortunately my teacher is much help either. Can
anyone suggest a good source of information, be it web site or text book
that I could refer to for a better understanding of this concept. TIA and
have a great weekend.
Robert
```

#### ↳ Re: Division and Remainders

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c20dfefa7c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6eqf8q$jqg@taro.futuris.net>`
- **References:** `<6eqf8q$jqg@taro.futuris.net>`

```

Robert Mezzone wrote:
› 
› I'm taking my first COBOL class this semester and find it pretty
…[9 more quoted lines elided]…
› Robert

01 MY-QUOTIENT PIC 9(4).

01 MY-REMAINDER PIC 9(4).

01 MY-DATE.
05 MY-DATE-YY PIC 9(2).
05 MY-DATE-MM PIC 9(2).
05 MY-DATE-DD PIC 9(2).

DIVIDE MY-DATE-YY BY 4 GIVING my-quotient REMAINDER my-remainder.
IF MY-REMAINDER = 0 THEN
SET IT-IS-A-LEAP-YEAR TO TRUE.

Note that the example is not fully Y2K compliant, but it may give you
some hints on how to get a remainder.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

##### ↳ ↳ Re: Division and Remainders

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1998-03-18T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c20dfefa7c-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c20dfefa7c-p2@usenetarchives.gap>`
- **References:** `<6eqf8q$jqg@taro.futuris.net> <gap-c20dfefa7c-p2@usenetarchives.gap>`

```

Arnold Trembley wrote:

› Note that the example is not fully Y2K compliant, but it may give you
› some hints on how to get a remainder.
›

Darn it Arnold, I can't beleive that you are EXACERBATING the Y2K
problem by continuing to code in a non compliant fashion. You even
admit to it! How dare you! (For those of you who do not know Arnold,
or me, this is NOT a flame, insult, etc... just a mild ribbing ).
```

###### ↳ ↳ ↳ Re: Division and Remainders

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-03-19T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c20dfefa7c-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c20dfefa7c-p3@usenetarchives.gap>`
- **References:** `<6eqf8q$jqg@taro.futuris.net> <gap-c20dfefa7c-p2@usenetarchives.gap> <gap-c20dfefa7c-p3@usenetarchives.gap>`

```

Thane Hubbell wrote:
› 
› Arnold Trembley wrote:
…[8 more quoted lines elided]…
› or me, this is NOT a flame, insult, etc... just a mild ribbing ).

Thane is an old friend in internet terms, so I knew he was joshin' me.

I picked the non-Y2K compliant example, because it was the shortest one
I could think of that had a real use for getting a remainder in COBOL.
It can also be used for calculating the day of the week, but that would
have been a longer example.

Then again, there's FUNCTION MOD if you have intrinsics in your COBOL,
perhaps there's even a FUNCTION REMAINDER.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!" http://home.att.net/~arnold.trembley
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
