[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Difference between Cobol 74 and 85

_4 messages · 4 participants · 1997-04_

**Topics:** [`COBOL standards (ANS, ISO, 74/85/2002/2014)`](../topics.md#standards)

---

### Difference between Cobol 74 and 85

- **From:** "markus eldryn" <ua-author-17073815@usenetarchives.gap>
- **Date:** 1997-04-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33470562.5EA9@ricochet.net>`

```

Hi,

I am a beginner to Cobol and was taught
Cobol '74/CICS in school. I like to know
more about Cobol '85. Is there much difference
between Cobol '74 and Cobol '85. Any pointer
on this on the *web/book I can buy* would
be appreciated.


Thanks in advance
../Markus
```

#### ↳ Re: Difference between Cobol 74 and 85

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-04-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecdc41f737-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33470562.5EA9@ricochet.net>`
- **References:** `<33470562.5EA9@ricochet.net>`

```

The real difference is not 74 vs 85 when speaking to CICS. While there are certainly differences due to the 85 standard, the bigger hit for CICS is the elimination of BL / BLL cell manipulation.

With VS COBOL II, even R1.0, a new, architected interface between COBOL and CICS was introduced. This new interface uses pointer data types and the ADDRESS syntax.

In general, far simpler, and more obvious than the olde interface. No more SERVICE RELOADs, no restrictions on using INSPECT or other non-I/O verbs.

This new interface exists without concern of 74 standard or 85 standard (CMPR2 / NOCMPR2) in VS COBOL II, COBOL/370 and COBOL for MVS and VM.

The new function introduced by the 85 standard, and the intrinsic function addendum are not necessary (but may be usefull) in the COBOL / CICS environment.

The different behaviors introduced by the 85 standard are generally minor for programs which do not do I/O operations. The different behaviors introduced by the new code patterns inherent in the
COBOL II and later compilers typically only affect programs where data does not match pictures (much fun results).

I recommend the VS COBOL II, COBOL/370 and COBOL for MVS and VM Migration Guides (available on the net) as a starting point.

OldBOL to NewBOL by Bill Klein - MicroFocus Press is also highly recommended.
Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

#### ↳ Re: Difference between Cobol 74 and 85

- **From:** "sft..." <ua-author-476529@usenetarchives.gap>
- **Date:** 1997-04-06T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecdc41f737-p3@usenetarchives.gap>`
- **In-Reply-To:** `<33470562.5EA9@ricochet.net>`
- **References:** `<33470562.5EA9@ricochet.net>`

```

Markus,

There is alot of minor differences between 74 and 85 cobol, but none
I would consider to drastic. If you have a good cobol II book and you
know cobol 74 well, I don't see why you would have too much trouble
"bellying up to a terminal" and writing cobol 85. ( I certainly prefer
'85 by far, and I think you would too once you start writing it. :)
```

#### ↳ Re: Difference between Cobol 74 and 85

- **From:** "cobo..." <ua-author-6589055@usenetarchives.gap>
- **Date:** 1997-04-08T22:07:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ecdc41f737-p4@usenetarchives.gap>`
- **In-Reply-To:** `<33470562.5EA9@ricochet.net>`
- **References:** `<33470562.5EA9@ricochet.net>`

```

In article <334··.@ric··t.net>,
mel··.@ric··t.net wrote:
› 
› Hi,
…[9 more quoted lines elided]…
› ../Markus


Yes there is an excellent book called "The COBOL 85 Example Book" by
Jerome Garfunkel that explains
all of the differences between COBOL 74 and COBOL 85 and shows
actual coding examples of all of the new features.
Unfortunately, the book is out of print.
There is a plan to reprint this book along with all of the new
features that are coming in COBOL 2000.

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
