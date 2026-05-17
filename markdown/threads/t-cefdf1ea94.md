[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Runtime & Y2K

_2 messages · 2 participants · 1998-01_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Runtime & Y2K

- **From:** "wm. gardner" <ua-author-3054840@usenetarchives.gap>
- **Date:** 1998-01-05T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<68u70j$iv9$1@gte1.gte.net>`

```

I apologize in advance for my ignorance but one of our customers asked a
question I don't know the answer to.......... Is there an actual problem
with the COBOL runtime not being 2YK compliant or just the programs that are
executed (product). I am obviously not a programmer (I am a C.S. manager)
but I have come up with a good answer as to why there is not a problem or
what we are doing to address it.

We use Micro Focus ver 3.2 (I think) for all of our products that are not
GUI. Half are fixed for 2YK already and the rest will be soon. I had
obviously heard about program problems and workstation BIOS problems but
this customer had a consultant advise them to research the actual
programming language.

Thanks in advance,
Wm Gardner
```

#### ↳ Re: Runtime & Y2K

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1998-01-06T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cefdf1ea94-p2@usenetarchives.gap>`
- **In-Reply-To:** `<68u70j$iv9$1@gte1.gte.net>`
- **References:** `<68u70j$iv9$1@gte1.gte.net>`

```

Wm. Gardner wrote:
› I apologize in advance for my ignorance but one of our customers asked a
› question I don't know the answer to..........   Is there an actual problem
…[10 more quoted lines elided]…
› programming language.

Y2k problem areas can be separated into three categories:
1. Application code which is century specific.
2. Century specific get current date from OS.
3. Century specific built-in compiler date manipulation functions.

Of those three categories, only the last two are compiler dependent. For
most applications, category 2 problems can easily be fixed for the near
future by expanding the year based on the year (e.g. if YY < 50 use 20YY else
use 19YY), or permanently by using a different function (e.g. FUNCTION
CURRENT-DATE) which returns the full year, if available. Category 3 problems
will require either another built-in function which is Y2k compliant, or
writing the functions in source code. I prefer to code this type of function
myself anyway.

The only category 3 functions I am aware of in Micro Focus COBOL 3.2 are the
intrinsic date functions, which are already Y2k compliant.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
