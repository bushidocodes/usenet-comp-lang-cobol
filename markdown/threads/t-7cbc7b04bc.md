[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Misc. Comments

_2 messages · 2 participants · 1997-02_

---

### Misc. Comments

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-02-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32F77C57.1EBC@tandem.com>`

```

I tried to post these yesterday, but my news server (not a Tandem
machine - a Sun) wouldn't accept any postings. The diagnostic made no
sense at all. Anyhow, it works today.

BYates4237 wrote:
›
› Can one get Cobol to treat the system date as a 4 digit year (1997) rather
› than as a two digit year(97)?

Yes. The standard (and almost every current implementation) has an
intrinsic function called CURRENT-DATE that returns 4-digit years
among other things. It also has a group of functions to manipulate
dates. If you are using COBOL II from IBM you are out of luck. It
does not have these functions.

--------------------------------------------------------------

Richard Plinston wrote:
› 
› Why put in the extra E-X-I-T when you don't need it.
…[7 more quoted lines elided]…
› on the standards in relation to this.

The standard allows an empty paragraph. That is, you can say

a-paragraph.

another-paragraph.
MOVE ...

Note that the empty paragraph has nothing at all in it - not a period
by itself.

Another no-op method that does not violate the standard is to put
CONTINUE at the end. It doesn't add much, but is better than the
non-standard EXIT at the end of a paragraph that has stuff in it.

---
Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: Misc. Comments

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-02-05T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-7cbc7b04bc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32F77C57.1EBC@tandem.com>`
- **References:** `<32F77C57.1EBC@tandem.com>`

```

4 digit year escape is available for OS/VS COBOL and VS COBOL II.

BLATANT COMMERCIAL - The Brigde to the Next Century intrinsic function
emulators provide equivalent functionality for the next 99 years of
FUNCTION CURRENT-DATE, and for the full range of integer dates. End
BLATANT COMMERCIAL.

For info - email undersigned....

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
