[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Rounding

_3 messages · 3 participants · 1995-08_

---

### Rounding

- **From:** "g..." <ua-author-7405396@usenetarchives.gap>
- **Date:** 1995-08-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<422kav$lvg@aztec.co.za>`

```
if I multiply with cobol 400 on the as/400 how do I round the result.
compute x = y * z
thanks
```

#### ↳ Re: Rounding

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1995-08-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d2fee8b000-p2@usenetarchives.gap>`
- **In-Reply-To:** `<422kav$lvg@aztec.co.za>`
- **References:** `<422kav$lvg@aztec.co.za>`

```
I don't have my COBOL/400 LRM handy, but I assume (believe) that
they support the ROUNDED phrase, i.e.

COMPUTE XYZ ROUNDED = A * B

"ROUNDED" is part of the ANSI standard, but as I recall COBOL/400
is "intermediate" not "high" ANSI so, this phrase may or may not
be there.
```

#### ↳ Re: Rounding

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1995-08-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d2fee8b000-p3@usenetarchives.gap>`
- **In-Reply-To:** `<422kav$lvg@aztec.co.za>`
- **References:** `<422kav$lvg@aztec.co.za>`

```
COMPUTE X ROUNDED = Y * Z END-COMPUTE

Note that the intermediate results of complex compute statements are not
standardized, they are left as "implementor defined". This was in
response to lots of public comments when the 1985 standard was under
discussion.

IBM warns that differences may exist in COMPUTE results across their 1985
conforming COBOL implementations, and suggest the use of explicit
arithmetic verbs. (SAA COBOL CPI Book - COMPUTE verb section).

An alternative to compute in this case is

MULTIPLY Y BY Z GIVING X ROUNDED END-MULTIPLY

The answer should be the same, and no potential for intermediate results
exists. The result of this statement should be very standard.

Late in the process of the 1985 standard, a concept of more predictable
arithmetic was brought up. Unfortunately for a variety of reasons it did
not make the cut for the current standard. Look for "ARITHMETIC IS
STANDARD" as a construct in the 1997 (?) standard proposal. This would
allow folks with ancient code (like me) to continue to get historically
correct behavior, but new code to be more portable across implementations.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
