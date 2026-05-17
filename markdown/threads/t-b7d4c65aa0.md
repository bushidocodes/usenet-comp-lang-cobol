[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Bad Verbs

_2 messages · 2 participants · 1996-04 → 1996-05_

---

### Bad Verbs

- **From:** "jsa" <ua-author-2098004@usenetarchives.gap>
- **Date:** 1996-04-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31870A7E.600F@alaska.net>`

```

Don Nelson Said:
› It is always amazing that various COBOL verbs are considered to be bad
› or some such because of the vagarities of one specific implementation
› (usually IBM).
›

Yes Don, and dont forget "Bad Characters"

I was told on my forst COBOL job to never use the > symbol
and always spell out GREATER THAN because my boss had one
time worked in a shop where the Print-Train (remember those)
did not have the > character. (Yup, IBM).


But how does your statement square with some of the recommendations
in your book to avoid certain verbs/syntax (NEXT SENTENCE)
because some programmers don't know the difference between a
sentence and a line?

I think there is plenty of verbiform prejudice to go around.

(Hate those ALTERed GO TOs).
__________________________________________
John Andersen |
Juneau Alaska |
__________________________________________|
```

#### ↳ Re: Bad Verbs

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-05-06T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b7d4c65aa0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31870A7E.600F@alaska.net>`
- **References:** `<31870A7E.600F@alaska.net>`

```

In message <<318··.@ala··a.net>> JSA writes:
›› It is always amazing that various COBOL verbs are considered to be bad
›› or some such because of the vagarities of one specific implementation
…[7 more quoted lines elided]…
› I think there is plenty of verbiform prejudice to go around.

The problem with NEXT SENTENCE is not because of 'the vagarities
of one specific implementation'. The problem is that it is not
always obvious what constitutes the 'next sentence'. Under the
74 standard it was relatively easy. NEXT SENTENCE is only
valid inside an IF statement. This is always ended by a full
stop (.). Thus NEXT SENTENCE always meant: after the next stop.

The '85 standard can terminate an IF with END-IF, so does the
NEXT SENTENCE refer to the end of the current IF level, or to the
next line after the following stop.

This is a problem in *all* implementations because it is a
problem of the change from 74 to 85. Solution: use CONTINUE.

›
› (Hate those ALTERed GO TOs).

Hopefully you never need to come across these ever again.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
