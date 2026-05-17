[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NOT IF as opposed to IF NOT

_2 messages · 2 participants · 1995-02_

---

### NOT IF as opposed to IF NOT

- **From:** "yo..." <ua-author-14167347@usenetarchives.gap>
- **Date:** 1995-02-22T19:38:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-J-8LBX3hYTA@usenetarchives.gap>`

```
Out COBOL teacher wrote a test question and when going over the tests he
and the TA give different answers.

The code was...

IF NOT A = B AND C

Is this equal to IF A NOT = B AND A NOT = C

or is it equal to IF A NOT = B AND A = C

Had the question been IF A NOT = B AND C then it woul be clear that the
not applies to both of them. But how about when the not is before the
A?

Thanks in advance and if you could email me replies in addition to posting
them I would very much appreciateit.


David

David and Mozhgan Heyman
yo··.@hav··s.org
727··.@com··e.com
http://haven.zets.org/~yosi
```

#### ↳ Re: NOT IF as opposed to IF NOT

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1995-02-27T20:30:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0dffdcc6d3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-J-8LBX3hYTA@usenetarchives.gap>`
- **References:** `<ua-fallback-J-8LBX3hYTA@usenetarchives.gap>`

```
In article <793··.@enz··o.uk> Enzo J Siri,
e.··.@enz··o.uk writes:
› 
›› IF NOT A = B AND C 
…[13 more quoted lines elided]…
› Anyway, it is not the sort of expression I would use in a program! :)

You have the correct answer except that it has nothing to do with
priority. In fact, this exact example appears in the standard. And,
I agree that one should never use NOT anywhere in an abbreviated
combined relation condiiton because almost nobody can figure out what
it means.

The actual rules are:

If the word immediately following NOT is GREATER, >, LESS, <, EQUAL,
=, then the NOT participates as part of the ralational operator;
otherwise, the NOT is interpreted as a logical operator and,
therefore, the implied insertion of subject or relation operator
results in a negated relation condition.

You win a prize if you can figure out what this means.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
Project Editor, 1997 ISO COBOL Standard
Moderator, COBOL Conference, Bix
nel··.@tan··m.com
do··.@b··.com
No clever quotes here
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
