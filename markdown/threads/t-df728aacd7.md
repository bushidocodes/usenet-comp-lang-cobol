[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How can I keep MF .CBL and .GNT files separate using Adv. Org.?

_3 messages · 3 participants · 1997-01_

---

### How can I keep MF .CBL and .GNT files separate using Adv. Org.?

- **From:** "sha..." <ua-author-12482346@usenetarchives.gap>
- **Date:** 1997-01-01T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5ah7nc$epe@wrdiss1.robins.af.mil>`

```

Can I set up MF Advanced Organizer so that source files can be kept in
one directory and the generated .INT or .GNT files kept in another?


Lee Shafer

Computer Sciences Corporation
[ opinions expressed are my own ]
[ and do not reflect those of CSC]
```

#### ↳ Re: How can I keep MF .CBL and .GNT files separate using Adv. Org.?

- **From:** "r..." <ua-author-2587243@usenetarchives.gap>
- **Date:** 1997-01-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df728aacd7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5ah7nc$epe@wrdiss1.robins.af.mil>`
- **References:** `<5ah7nc$epe@wrdiss1.robins.af.mil>`

```

In article <5ah7nc$e.··.@wrd··f.mil>
sha··.@a··.org "Lee Shafer" writes:
› Can I set up MF Advanced Organizer so that source files can be kept in
› one directory and the generated .INT or .GNT files kept in another?

While you're waiting for an answer, and assuming that you are
operating under MSDOS/Windows on a PC, you might want to start off
with a couple of subdirectories and a batch program something like
this:

MOVE SOURCE\*.?NT OBJECT\

Cheers
Richard Ross-Langley        +44 1727 852 801
Mine of Information Ltd, PO BOX 1000, St Albans AL3 5NY, GB
* Independent Computer Consultancy    Established in 1977 *
```

#### ↳ Re: How can I keep MF .CBL and .GNT files separate using Adv. Org.?

- **From:** "a..." <ua-author-512315@usenetarchives.gap>
- **Date:** 1997-01-17T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-df728aacd7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5ah7nc$epe@wrdiss1.robins.af.mil>`
- **References:** `<5ah7nc$epe@wrdiss1.robins.af.mil>`

```

sha··.@a··.org (Lee Shafer) wrote:

› Can I set up MF Advanced Organizer so that source files can be kept in
› one directory and the generated .INT or .GNT files kept in another?


have a look at the checker directive
INT(pathname\)
and the compiler directive
GNT(pathname\)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
