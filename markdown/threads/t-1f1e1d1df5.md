[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Error handling

_5 messages · 5 participants · 1996-01_

---

### Error handling

- **From:** "alexander eller" <ua-author-2643838@usenetarchives.gap>
- **Date:** 1996-01-28T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<310DA977.2663@muc.de>`

```
Hi, there!

I am new to COBOL, so my question may sound silly.
Is there any chance to handle errors in COBOL. I know about the
FileStatus-Variable for File-I/O-activities and OVERFLOW and SIZE-errors.
But I can't find anything like general Error-routines (for example ON
ERROR like PL/1). Is it "normal" to COBOL that I have to embed every
arithmetic operation in a ON OVERFLOW PERFORM <....>?

Thanks for Your help
Alex
```

#### ↳ Re: Error handling

- **From:** "david_..." <ua-author-3348436@usenetarchives.gap>
- **Date:** 1996-01-29T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f1e1d1df5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<310DA977.2663@muc.de>`
- **References:** `<310DA977.2663@muc.de>`

```
In article <310··.@m··.de>, ell··.@m··.de says...
› 
› Hi, there!
…[9 more quoted lines elided]…
› Alex

For file access, you can set up declarative sections at the beginning
of the procedure division. They are described in the 'use statement' in
cobol manual. I was told that they were not the best thing in the world to
use as normal system actions during abends could be masked so no one knew a
problem occured. Never have used them so no real opion, but it sounds
similar to what you're describing.
There is also no requirement to code the on overflow. If you're sure
it won't happen, no need to put it in.
```

#### ↳ Re: Error handling

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-01-29T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f1e1d1df5-p3@usenetarchives.gap>`
- **In-Reply-To:** `<310DA977.2663@muc.de>`
- **References:** `<310DA977.2663@muc.de>`

```
Some error handling is available with the DECLARATIVES construct.

Which platform are you interested in.... some error handling may exist as
vendor extensions. Seems like exception handling is still in the pending
category for standard COBOL. Our learned experts - Mr. Nelson, Mr. Kelin
etc may be able to shed some light on where exception handling is in the
199? standard process.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

##### ↳ ↳ Re: Error handling

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-01-31T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f1e1d1df5-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-1f1e1d1df5-p3@usenetarchives.gap>`
- **References:** `<310DA977.2663@muc.de> <gap-1f1e1d1df5-p3@usenetarchives.gap>`

```
In article <4elch7$b.··.@new··l.com> RWidmer, rwi··.@a··.com
writes:
› Some error handling is available with the DECLARATIVES construct.
› 
…[4 more quoted lines elided]…
› 199? standard process.

The exception processing facility has been added to the draft standard.
What that means is that it will be included in the final standard.

You specify a declarative - perhaps USE AFTER EXCEPTION EC-SIZE-OVERFLOW
(or perhaps just EC-SIZE to get all possible size errors). Then you
specify the compiler directive TURN to cause checking to be done for that
condition (like >>TURN EC-SIZE-OVERFLOW CHECKING ON). There are around a
hundred exceptions you can check for. You can specify ALL to get
everything.

Don Nelson
```

#### ↳ Re: Error handling

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1996-01-29T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f1e1d1df5-p5@usenetarchives.gap>`
- **In-Reply-To:** `<310DA977.2663@muc.de>`
- **References:** `<310DA977.2663@muc.de>`

```
Currently DECLARATIVES can handle a few errors (similarly to PL/I
ON-units). However, the next revision of the COBOL Standard will
introduce a "Common Exception Handling" facility that provides
the same type (and breadth) of exception handling as PL/I has.

You might want to check with your compiler-vendor to see if they
plan on waiting for the next Standard or if they can provide the
ANSI/ISO exception handling "soon".
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
