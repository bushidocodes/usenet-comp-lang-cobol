[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Sections vs. Paragraphs

_4 messages · 4 participants · 1996-11 → 1996-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### Sections vs. Paragraphs

- **From:** "dbret..." <ua-author-6588809@usenetarchives.gap>
- **Date:** 1996-11-27T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19961128085900.DAA16922@ladder01.news.aol.com>`

```

Gee.........what do all you "no go to" people do about an IF....CONTINUE.
:-)
```

#### ↳ Re: Sections vs. Paragraphs

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-11-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9e6a80ba4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19961128085900.DAA16922@ladder01.news.aol.com>`
- **References:** `<19961128085900.DAA16922@ladder01.news.aol.com>`

```

I'm not really one of those "no goto" people, although any NEW programs I
write contain no go to statements. What case are you talking about
(specific example please) where the If... Continue.. is used in conjuction
with the GO TO, and I'll explain a different way to do it, sans the go to.


dbr··.@a··.com wrote in article
<199··.@lad··l.com>...
› Gee.........what do all you "no go to" people do about an IF....CONTINUE.
 
› :-)
›
›
›
```

##### ↳ ↳ Re: Sections vs. Paragraphs

- **From:** "steven g. townsend" <ua-author-6589043@usenetarchives.gap>
- **Date:** 1996-12-21T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9e6a80ba4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-c9e6a80ba4-p2@usenetarchives.gap>`
- **References:** `<19961128085900.DAA16922@ladder01.news.aol.com> <gap-c9e6a80ba4-p2@usenetarchives.gap>`

```

Thane Hubbell wrote:
[ snip ]

› dbr··.@a··.com wrote in article
› <199··.@lad··l.com>...
›› Gee.........what do all you "no go to" people do about an IF....CONTINUE.
›

If I understand the question, it is what to do with a construct
like

IF
THEN

ELSE

END-IF

if so...

IF NOT
THEN

END-IF
```

#### ↳ Re: Sections vs. Paragraphs

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1996-12-01T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c9e6a80ba4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19961128085900.DAA16922@ladder01.news.aol.com>`
- **References:** `<19961128085900.DAA16922@ladder01.news.aol.com>`

```

dbr··.@a··.com wrote:

› Gee.........what do all you "no go to" people do about an IF....CONTINUE.
› :-)

It's contained within the paragraph and presents no problem to use.
The problem becomes when one start GO TO-ing from one non-continuious
paragraph to another all over the program and logic flow understanding
reaches the same rate as one needs to understand Assembler (or C).
That's how a lot of glitches gets introduced.

Just my 1.5 cents worth, adjusted for inflation
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
