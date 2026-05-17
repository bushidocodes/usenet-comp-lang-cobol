[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# In Search of a Random number generator

_3 messages · 3 participants · 1995-05_

---

### In Search of a Random number generator

- **From:** "clan..." <ua-author-17088272@usenetarchives.gap>
- **Date:** 1995-05-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o5mfc$t2@services.arn.net>`

```
I need a random number generator for use in Cobol.


Thanks in advance

Patrick Cagle
```

#### ↳ Re: In Search of a Random number generator

- **From:** "gordon...." <ua-author-10958913@usenetarchives.gap>
- **Date:** 1995-05-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6fa96c57aa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3o5mfc$t2@services.arn.net>`
- **References:** `<3o5mfc$t2@services.arn.net>`

```
cla··.@a··.net (Patrick Cagle) wrote:

› I need a random number generator for use in Cobol.
 
 
› Thanks in advance
 
› Patrick Cagle

If I am not mistaken, the COBOL 85 (or 89 addition) adds something
called ANSI Intrinsics. The intrinsics include a random number
generator. I have read many books about ANSI Cobol 85 and they all
mention the intrinsics.

The way you call the intrinsic is:
COMPUTE random-num = FUNCTION RANDOM (seed).

The seed is optional.

I have seen this function in the MicroFocus Cobol manual as well as
the IBM VS COBOLII, and the Unisys A Series COBOL85 compilers.

Hope this helps.
------------------------------------------------------
Internet: Gor··.@pi··g.be
Compuserve: 100273,1562
Snappy quote for this week: Meskimen's Law:
There's never time to do it right, but there's always time to do it over.
```

#### ↳ Re: In Search of a Random number generator

- **From:** "jts..." <ua-author-12520169@usenetarchives.gap>
- **Date:** 1995-05-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6fa96c57aa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3o5mfc$t2@services.arn.net>`
- **References:** `<3o5mfc$t2@services.arn.net>`

```
On 2 May 1995 16:26:20 GMT, Patrick Cagle (cla··.@a··.net) wrote:
› I need a random number generator for use in Cobol.


How about RANDOM function?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
