[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol: arithmetic result not placed in field even though it would fit

_5 messages · 5 participants · 1997-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol: arithmetic result not placed in field even though it would fit

- **From:** "lev..." <ua-author-1135463@usenetarchives.gap>
- **Date:** 1997-05-01T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<862594052snx@warren.demon.co.uk>`

```


We have a substantial body of code written in MF Cobol 4.5, cross-compiled
from DOS to run under OS/2. We've just run across a problem whereby some
simple arithmetical results do not get stored in the receiving field, even
though they would fit. Consider the following example program:

data division.
working-storage section.

01 foo pic s99.
01 bar pic s999 value 100.

procedure division.

move -4 to foo.
add 100 to foo.
display foo.

move -4 to foo.
add 100, foo giving foo.
display foo.

move -4 to foo.
add bar to foo.
display foo.

move -4 to foo.
add bar, foo giving foo.
display foo.

Following the rules for alignment of output, I would expect all four
answers to be 96. However, the actual results are -4, 96, 04, 96. If
however I replace all the 100's by 99's, the answers are 95, 95, 95, 95.
Also, adding an "ON SIZE ERROR" clause with an additor (is that a word?)
of 100 gives the correct result all across the board.

It appears to me that unless it is absolutely forced to use an internal
workfield, the compiler is looking at the magnitude of the original
components of the sum, and not in fact at the magnitude of the result.
I've been "doing COBOL" for ten years and never come across this before,
but if I've overlooked some obscure paragraph of the spec I'm happy to be
told! The fix is (now) obvious. Nevertheless I'd greatly appreciate the
opinions of others, especially any hints as to directives or other
"quick fixes", because I don't want to have to inspect 267,000 lines
of code to see where else this may be a problem. And it is a problem, it
is currently causing some debit cards which cross the Y2K boundary to be
rejected - so where else can't we trust the "obvious" interpretations ?

Nick Leverton

[Apologies if this posting is duplicated: I'm sure I posted it
yesterday, but I don't see it in my outgoing news log or in
DejaNews so I think it didn't actually get sent]
```

#### ↳ Re: MF Cobol: arithmetic result not placed in field even though it would fit

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1997-05-01T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8ecadd8fc6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<862594052snx@warren.demon.co.uk>`
- **References:** `<862594052snx@warren.demon.co.uk>`

```

Nick Leverton wrote:
› 
› ... (deleted example) 
…[10 more quoted lines elided]…
› rejected - so where else can't we trust the "obvious" interpretations ?

According to the standard, you should get 96 in all cases. The
relevant line for the ADD statement (page VI-74) is:

"The compiler insures that enough places are carried so as not to lose
any significant digits during execution.".

There are other statements elsewhere about the implementor defining
the intermediate and such for arithmetic expressions, but this is not
an arithmetic expression.

Not only did you lose significant digits you lost the right answer as
well.

You have found a bug and should report it to MF.

Just to be sure I didn't make the same error in my compiler, I tried
it and got 96 across the board. What they probably did is assume an
intermediate of two digits. This kind of thing is not too unusual for
compiler writers.

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

#### ↳ Re: MF Cobol: arithmetic result not placed in field even though it would fit

- **From:** "le..." <ua-author-782493@usenetarchives.gap>
- **Date:** 1997-05-01T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8ecadd8fc6-p3@usenetarchives.gap>`
- **In-Reply-To:** `<862594052snx@warren.demon.co.uk>`
- **References:** `<862594052snx@warren.demon.co.uk>`

```

Nick Leverton wrote:
› 
› We have a substantial body of code written in MF Cobol 4.5, cross-compiled
…[50 more quoted lines elided]…
› DejaNews so I think it didn't actually get sent]

MF is notorious for being a bit flaky on computations.
You may find a statement in the COBOL standard (Don Nelson?)
that says that in your case (values out of range) the
result is "implementor defined".
```

##### ↳ ↳ Re: MF Cobol: arithmetic result not placed in field even though it would fit

- **From:** "eugene a. pallat" <ua-author-501199@usenetarchives.gap>
- **Date:** 1997-05-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8ecadd8fc6-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8ecadd8fc6-p3@usenetarchives.gap>`
- **References:** `<862594052snx@warren.demon.co.uk> <gap-8ecadd8fc6-p3@usenetarchives.gap>`

```

The rsults of the computations make perfect sense. This is the kind of
trouble people get when the fields are smaller than the magnitude of the
data.

Always make sure of the size of the fields is compatable with the data
whith which you are working. After all, would you expect to get valid
results storing a value of 1268974 to a pic s99 field?

Remove the '-' from orion-data for sending email to me.

Gene eap··.@ori··a.com

Orion Data Systems

Solicitations to me must be pre-approved in writing
by me after soliciitor pays $1,000 US per incident.
Solicitations sent to me are proof you accept this
notice and will send a certified check forthwith.


le··.@i··.net wrote in article <336··.@i··.net>...
› Nick Leverton wrote:
›› 
…[67 more quoted lines elided]…
›
```

#### ↳ Re: MF Cobol: arithmetic result not placed in field even though it would fit

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-05-05T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8ecadd8fc6-p5@usenetarchives.gap>`
- **In-Reply-To:** `<862594052snx@warren.demon.co.uk>`
- **References:** `<862594052snx@warren.demon.co.uk>`

```

Nick Leverton wrote:
› 
› We have a substantial body of code written in MF Cobol 4.5, cross-compiled
› from DOS to run under OS/2.  We've just run across a problem whereby some
› simple arithmetical results do not get stored in the receiving field, even
› though they would fit. 
Nick,
I'm not sure what compiler you're using, but I know that the MVS COBOL
II compiler has certain options that affect the way Cobol itself handles
intermediate results, especially the TRUNC() option. Many of these
options were no doubt implemented to assist in migration from one
release to the next (on the same platform, at least).
I'd check your compilers options to see if there's anything there.
Also, if you have a few minutes, look at the TRUNC() and MIGR options on
your MF compiler; it may provide some insight.
Good luck :-)

Jim Van Sickle   
Manager, Operations and Tech Support
United Retail Group. Inc.
Rochelle Park, NJ
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
