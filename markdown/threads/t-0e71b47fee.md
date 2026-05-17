[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Square root calcualtion with COBOL

_5 messages · 5 participants · 1995-07 → 1995-08_

---

### Square root calcualtion with COBOL

- **From:** "kenr6..." <ua-author-17088258@usenetarchives.gap>
- **Date:** 1995-07-27T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3vbr68$3di@newsbf02.news.aol.com>`

```
I need to compute a square root in a MF COBOL program running under UNIX.
I don't believe there is a COBOL verb to do this. Does anyone have an
algorithm or a piece of code that will do this??

Send reply to Ken··.@a··.com
```

#### ↳ Re: Square root calcualtion with COBOL

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1995-07-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e71b47fee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3vbr68$3di@newsbf02.news.aol.com>`
- **References:** `<3vbr68$3di@newsbf02.news.aol.com>`

```
In article <3vbr68$3.··.@new··l.com>,
ken··.@a··.com (KenR626843) wrote:
›
› I need to compute a square root in a MF COBOL program running under UNIX. I
› don't believe there is a COBOL verb to do this. Does anyone have an algorithm
› or a piece of code that will do this??

The CoBOL verb that computes the square root of a number is "compute":

COMPUTE WS-SQUARE-ROOT = WS-NUMBER ** .5


The newest compilers have an intrinsic function for square root:

COMPUTE WS-SQUARE-ROOT = FUNCTION SQRT(WS-NUMBER)


› Send reply to Ken··.@a··.com

Sorry, you post a question here, you get an answer here.
```

#### ↳ Re: Square root calcualtion with COBOL

- **From:** "gt..." <ua-author-2476667@usenetarchives.gap>
- **Date:** 1995-07-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e71b47fee-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3vbr68$3di@newsbf02.news.aol.com>`
- **References:** `<3vbr68$3di@newsbf02.news.aol.com>`

```
Compute W-SQRT = W-SQRT ** .5

Raise the value youwant to get a SQRT of to the 1/2 power.

GT
```

#### ↳ Re: Square root calcualtion with COBOL

- **From:** "bowil..." <ua-author-6588932@usenetarchives.gap>
- **Date:** 1995-07-31T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e71b47fee-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3vbr68$3di@newsbf02.news.aol.com>`
- **References:** `<3vbr68$3di@newsbf02.news.aol.com>`

```
ken··.@a··.com (KenR626843) wrote:

› I need to compute a square root in a MF COBOL program running under UNIX. 
› I don't believe there is a COBOL verb to do this.  Does anyone have an
› algorithm or a piece of code that will do this??
 
› Send reply to Ken··.@a··.com

Try:

COMPUTE result = product ** .5

Set up your WORKING STORAGE fields accordingly. If you need
precession, use COMP or COMP-2 (COMP is binary and COMP-2 is
double-precession floating point).

Hope this helps,
Boyce Williams
```

#### ↳ Re: Square root calcualtion with COBOL

- **From:** "j.p..." <ua-author-15533016@usenetarchives.gap>
- **Date:** 1995-08-01T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0e71b47fee-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3vbr68$3di@newsbf02.news.aol.com>`
- **References:** `<3vbr68$3di@newsbf02.news.aol.com>`

```
In article , cod··.@cix··o.uk ("Pete Dillon") says:
›
snip
snip
snip

› Ken -
› 
…[6 more quoted lines elided]…
› (cod··.@cix··o.uk)


but on wang vs, if you give a non-positive-integer argument, you get
a compile time error; or if you try and cheat with a variable, you get
a run time error. i seem to recall something similar on the as/400 too.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
