[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Writing to stderr v. stdout

_3 messages · 3 participants · 1996-06_

---

### Writing to stderr v. stdout

- **From:** "sma..." <ua-author-17086983@usenetarchives.gap>
- **Date:** 1996-06-25T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4qrl3c$f8h@ns.interserf.net>`

```

I am use to DISPLAY going to 'stdout', but now that we are on unix I
would like some msgs to go to 'stderr'. Since we are remote users we
have no books and the FAQ I found for this group does not cover this
question.

So, how does one write to 'stderr' in COBOL. If it matters we are
using MicroFoucus COBOL.

Thank you.
----------------------
Scott Mattes
I-Net, Inc
```

#### ↳ Re: Writing to stderr v. stdout

- **From:** "kevin digweed" <ua-author-6588872@usenetarchives.gap>
- **Date:** 1996-06-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff4ca8834d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4qrl3c$f8h@ns.interserf.net>`
- **References:** `<4qrl3c$f8h@ns.interserf.net>`

```

sma··.@Int··F.net (Scott Mattes) wrote:

› So, how does one write to 'stderr' in COBOL. If it matters we are
› using MicroFoucus COBOL.

DISPLAY "Hello stderr world" UPON SYSERR.
```

#### ↳ Re: Writing to stderr v. stdout

- **From:** "1017..." <ua-author-961424@usenetarchives.gap>
- **Date:** 1996-06-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff4ca8834d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4qrl3c$f8h@ns.interserf.net>`
- **References:** `<4qrl3c$f8h@ns.interserf.net>`

```
dco··.@con··x.com (Dennis Collin) wrote:

› sma··.@Int··F.net (Scott Mattes) wrote:
› 
…[12 more quoted lines elided]…
› 
Indeed, but what if he wants some messages to go to stdout, and some
to stderr.

Don't quote me on this (fuzzy memory), but I think there's an
environment variable (or compiler directive?) for MF Cobol that sends
DISPLAY UPON CONSOLE to stderr, while plain DISPLAY goes to stdout.
It's in the (excellent) manuals somewhere!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
