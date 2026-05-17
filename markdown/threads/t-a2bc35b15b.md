[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help, funky #'s from COBOL?

_4 messages · 4 participants · 1997-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help, funky #'s from COBOL?

- **From:** "kmck..." <ua-author-17073184@usenetarchives.gap>
- **Date:** 1997-01-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970104055000.AAA09338@ladder01.news.aol.com>`

```

I am a COBOL novice, attempting to write a program to read in data from a
flat file
which is produced from an ancient COBOL program. These numbers are
supposed to be
floating point, but appear as follows in the file: 0000000000000{ or
000000000000}.

What format is this? and how do I define a working storage element that
will understand
this numeric format?? Please e-mail any help you can offer.

Thanks in advance..
```

#### ↳ Re: Help, funky #'s from COBOL?

- **From:** "lebl..." <ua-author-14800849@usenetarchives.gap>
- **Date:** 1997-01-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2bc35b15b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970104055000.AAA09338@ladder01.news.aol.com>`
- **References:** `<19970104055000.AAA09338@ladder01.news.aol.com>`

```

On a mainframe, this is a signed DISPLAY format. The picture would be
S9(14) or S9(15) (the number of zeroes was not consistent). I can't
tell if there should be an implied decimal point or not. Hope this
helps.

kmc··.@a··.com (KMckeown) wrote:

› I am a COBOL novice, attempting to write a program to read in data from a
› flat file
…[11 more quoted lines elided]…
›
```

#### ↳ Re: Help, funky #'s from COBOL?

- **From:** "del archer" <ua-author-6589011@usenetarchives.gap>
- **Date:** 1997-01-03T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2bc35b15b-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19970104055000.AAA09338@ladder01.news.aol.com>`
- **References:** `<19970104055000.AAA09338@ladder01.news.aol.com>`

```

KMckeown wrote:

› I am a COBOL novice, attempting to write a program to read in data from a
› flat file
…[7 more quoted lines elided]…
› this numeric format?? ...

These are display format numbers (pic S9(n)). The curly brace is the sign
(trailing in this case); '{' is positive, and '}' is negative.


Del.
```

##### ↳ ↳ Re: Help, funky #'s from COBOL?

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-01-03T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2bc35b15b-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a2bc35b15b-p3@usenetarchives.gap>`
- **References:** `<19970104055000.AAA09338@ladder01.news.aol.com> <gap-a2bc35b15b-p3@usenetarchives.gap>`

```

Del Archer wrote:

› KMckeown wrote:
› 
…[15 more quoted lines elided]…
› Del.

actually that is { is a plus zero; 1{ is +10
last digit {ABCDEFGHI +0...+9 }JKLMNOPQR -0...-9

JR

and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
