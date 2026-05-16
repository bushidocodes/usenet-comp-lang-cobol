[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol needs a sharp knife...

_5 messages · 3 participants · 2004-11_

---

### Re: Cobol needs a sharp knife...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-11-29T14:09:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<N4Gqd.25661$Rf1.2534@newssvr19.news.prodigy.com>`
- **References:** `<41758a6b.0411282237.7a42c3e1@posting.google.com>`

```

"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
news:41758a6b.0411282237.7a42c3e1@posting.google.com...
>
> I am trying to learn how to CUT and paste text or bitmap files
> into windows clipboard. I finally managed to put a skeleton code
> to perform most of this function -- however, i need help on how
> to copy Into and From the clipboard?

> *>------------------------------------------------------*
> *> need to know how to paste text into clipboard here   !
> *> need to know how to paste bitmap into clipboard here !

For text:
Copy (MOVE) your text to the address returned by GlobalLock before
unlocking, then call SetClipboardData with parameter #1 = CF_TEXT (value 1)
and parameter 2 = the global memory handle.

For Bitmaps:
A little different... instead of GlobalAlloc to get a handle, you need a
handle to the bitmap, which you can get with either LoadBitmap or LoadImage.
(or CreateBitmap, CreateBitmapindirect or CreateCompatibleBitmap)

Then call SetClipboardData with parameter 1 = CF_BITMAP (value 2) and
parameter 2 = Bitmap Handle.

In either case, once you (succesfully) call SetClipboardData, the handle is
no longer owned by your process, so don't try to use it.

Also note: when transferring text, your MEMORY-FLAGS parameter to
GlobalAlloc must include GMEM_MOVEABLE (must not include GMEM_FIXED)

As far as retrieving data from the clipboard, you simply reverse the
process: callling GetClipboardData returns either a global handle (when
CF_TEXT) or a bitmap handle (CF_BITMAP).

FWIW, you can look this all up for free on-line at the MDSN site. Start at
http://msdn.microsoft.com/library/default.asp  and search for the various
API calls. Everything there is written in "C" but it looks like you've been
able to port to COBOL OK so far.

MCM
```

#### ↳ Re: Cobol needs a sharp knife...

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2004-11-29T11:22:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0411291122.598bc59d@posting.google.com>`
- **References:** `<41758a6b.0411282237.7a42c3e1@posting.google.com> <N4Gqd.25661$Rf1.2534@newssvr19.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote in message news:<N4Gqd.25661$Rf1.2534@newssvr19.news.prodigy.com>...
> "KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
> news:41758a6b.0411282237.7a42c3e1@posting.google.com...
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Cobol needs a sharp knife...

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-11-29T19:30:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7NKqd.367392$Pl.339357@pd7tw1no>`
- **In-Reply-To:** `<N4Gqd.25661$Rf1.2534@newssvr19.news.prodigy.com>`
- **References:** `<41758a6b.0411282237.7a42c3e1@posting.google.com> <N4Gqd.25661$Rf1.2534@newssvr19.news.prodigy.com>`

```
Michael Mattias wrote:

>"KELLIE FITTON" <KELLIEFITTON@YAHOO.COM> wrote in message
>news:41758a6b.0411282237.7a42c3e1@posting.google.com...
…[10 more quoted lines elided]…
>
Hi Kellie,

Seems to me you already have a good handle on COBOL, and it would appear 
Michael has provided you sufficient info. However if you do get stuck, 
could always post your revised code at Micro Focus Answer Exchange. If 
you are using University Edition then post the query under that title, 
otherwise post to the general Net Express sub-forum.

Your title "Cobol needs a sharp knife". Not really - "It's Windows needs 
a sharp knife, right across the throat". :-) Most folks get a handle on 
COBOL real quick. Again and again, the queries in Answer Exchange are 
primarily, "How do I use this Windoze gizmo ?".  To a lesser extent, the 
syntax for switching between different Databases. As Michael points out 
MDSN is so very helpful always giving examples in "C" !.

(Just for info - checked the on-line references to clipboard, and they 
point you to OLE classes, using GUI templates - which is a route you 
have chosen not to use).

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Cobol needs a sharp knife...

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-11-29T22:24:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CkNqd.651$nE7.298@newssvr17.news.prodigy.com>`
- **References:** `<41758a6b.0411282237.7a42c3e1@posting.google.com> <N4Gqd.25661$Rf1.2534@newssvr19.news.prodigy.com> <7NKqd.367392$Pl.339357@pd7tw1no>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:7NKqd.367392$Pl.339357@pd7tw1no...
> Michael Mattias wrote:
>
…[11 more quoted lines elided]…
> have chosen not to use).

Yeah, I forgot about the COM interface(s). But I learned all this stuff
before the COM interface was a part of the 'official' Windows API  so I
stick with my old-fart methods.  (The COM methods have been available
longer, but for a while they were only offered as part of Microsoft-brand
development products, e.g., Visual BASIC, Visual C).

MCM
```

##### ↳ ↳ Re: Cobol needs a sharp knife...

- **From:** KELLIEFITTON@YAHOO.COM (KELLIE FITTON)
- **Date:** 2004-11-29T19:39:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<41758a6b.0411291939.735ea104@posting.google.com>`
- **References:** `<41758a6b.0411282237.7a42c3e1@posting.google.com> <N4Gqd.25661$Rf1.2534@newssvr19.news.prodigy.com> <7NKqd.367392$Pl.339357@pd7tw1no>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<7NKqd.367392$Pl.339357@pd7tw1no>...
>
> Hi Kellie,
…[15 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
