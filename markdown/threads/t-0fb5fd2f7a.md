[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Var equal to ('a' or 'b' or 'c') legal?

_3 messages · 3 participants · 1995-01_

---

### Var equal to ('a' or 'b' or 'c') legal?

- **From:** "va..." <ua-author-9435888@usenetarchives.gap>
- **Date:** 1995-01-21T19:44:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fs9q9$pqm@elan.cs.umd.edu>`

```

Yes, Is this construct legal?

variable equal to ('a' or 'b' or 'c').


I know, in COBOL it's possible to abbreviate comparisons,
so instead of writing

var = 'a' or var = 'b' or var = 'c'

one can write

var = 'a' or 'b' or 'c'


Or it can be parenthesized as:

(var = 'a' or 'b' or 'c')

for use in a more complicated condition.

However, the form

var = ('a' or 'b' or 'c') is illegal as I think
since 'a' or 'b' or 'c' is illegal expression and it cannot be
paranthesized. However, I met stuff like this in supposedly working
COBOL OSVS programs.

So, COBOL gurus out there: is it a legal construct?


Vadim Maslov
```

#### ↳ Re: Var equal to ('a' or 'b' or 'c') legal?

- **From:** "tip..." <ua-author-4488463@usenetarchives.gap>
- **Date:** 1995-01-22T12:03:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0fb5fd2f7a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3fs9q9$pqm@elan.cs.umd.edu>`
- **References:** `<3fs9q9$pqm@elan.cs.umd.edu>`

```
In <3fs9q9$p.··.@ela··d.edu> va··.@cs.··d.edu (Vadim Maslov) writes:


› one can write
› var = 'a' or 'b' or 'c'
› Or it can be parenthesized as:
› (var = 'a' or 'b' or 'c')
› for use in a more complicated condition.

I would like to point out a warning here! Be sure in a complicated
condition you DO put parentheses around the whole thing. I have made
the mistake of:

IF CONDITION AND
VAR = 'A' OR 'B'

This is interpreted left to right as
IF (CONDITION AND VAR = 'A') OR VAR = 'B'
which is probably not what you intended, not what I intended, & not
what it looks like at first glance at the code.

› However, the form
› var = ('a' or 'b' or 'c') is illegal as I think
› since 'a' or 'b' or 'c' is illegal expression and it cannot be

I think you're right about ('a' or 'b' or 'c') in parentheses.
Haven't tried it, though.
```

##### ↳ ↳ Re: Var equal to ('a' or 'b' or 'c') legal?

- **From:** "de..." <ua-author-10962348@usenetarchives.gap>
- **Date:** 1995-01-23T18:43:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0fb5fd2f7a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0fb5fd2f7a-p2@usenetarchives.gap>`
- **References:** `<3fs9q9$pqm@elan.cs.umd.edu> <gap-0fb5fd2f7a-p2@usenetarchives.gap>`

```
"I think you're right about ('a' or 'b' or 'c') in parentheses.
Haven't tried it, though."

be careful, the quesion was about what was legal in COBOL, the language.
You can't answer that kind of question by "trying it", that only tells
you what the implementation does. You can only answer a question like
that by looking at the standard.

Having a secure knowledge of what is in the standard vs what is in the
implementation is of key importance in writing portable code!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
