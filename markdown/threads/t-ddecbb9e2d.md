[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Nice way to set high-order bit of a fullword??

_6 messages · 4 participants · 1997-11_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Nice way to set high-order bit of a fullword??

- **From:** "lee whitaker" <ua-author-17071806@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64cprk$gpg$1@gte1.gte.net>`

```

I need to set the high order bit of a fullword in order to call the
assembler WAIT macro with an ECB list. Obviously, this is on an MVS host,
and I am using Cobol for MVS. My best solution is to call either an
assembler or C module which does the logical 'or', but it seems
just-too-clunky. I can not blast the entire first byte, so I have given up
on character manipulation. Any ideas out there?

thnks.
```

#### ↳ Re: Nice way to set high-order bit of a fullword??

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-11-11T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddecbb9e2d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<64cprk$gpg$1@gte1.gte.net>`
- **References:** `<64cprk$gpg$1@gte1.gte.net>`

```

Lee Whitaker wrote:
› 
› I need to set the high order bit of a fullword in order to call the
…[6 more quoted lines elided]…
› thnks.
Lee,
I assume the fullword is probably coming from somewhere outside of your COBOL
program?
How 'bout this:

01 DOUBLEWORD PIC S9(9) COMP.
01 FILLER REDEFINES DOUBLEWORD.
05 FILLER PIC XXXX VALUE LOW-VALUES.
05 FULLWORD PIC S9(8) COMP.

then...

IF DOUBLEWORD > 32767

Just need to be careful if moving to FULLWORD.

I hope I didn't completely miss the point, but then again, it wouldn't be the
first time :-)
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

##### ↳ ↳ Re: Nice way to set high-order bit of a fullword??

- **From:** "freddie schwenke" <ua-author-13484813@usenetarchives.gap>
- **Date:** 1997-11-13T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddecbb9e2d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ddecbb9e2d-p2@usenetarchives.gap>`
- **References:** `<64cprk$gpg$1@gte1.gte.net> <gap-ddecbb9e2d-p2@usenetarchives.gap>`

```

As far as I know, you are not allowed to use the VALUE-clause in a field
that redefines another!!!

The compiler doesn't like it.

Freddie
:)

Jim Van Sickle wrote in article
<346··.@i··.net>...
› Lee Whitaker wrote:
›› 
…[39 more quoted lines elided]…
›
```

###### ↳ ↳ ↳ Re: Nice way to set high-order bit of a fullword??

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1997-11-16T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddecbb9e2d-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ddecbb9e2d-p3@usenetarchives.gap>`
- **References:** `<64cprk$gpg$1@gte1.gte.net> <gap-ddecbb9e2d-p2@usenetarchives.gap> <gap-ddecbb9e2d-p3@usenetarchives.gap>`

```

Freddie,

You got me...quick fix is to remove value clause from FILLER and add VALUE ZERO
to DOUBLEWORD.

However, in re-reading the post, I just noticed the original request was to SET
the hi-order bit, not TEST it, in which case the statement should read something
like:

IF DOUBLEWORD < 32768
ADD 32768 TO DOUBLEWORD

Must have been having a bad day.....


Freddie Schwenke wrote:
› 
› As far as I know, you are not allowed to use the VALUE-clause in a field
…[41 more quoted lines elided]…
›› --
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

###### ↳ ↳ ↳ Re: Nice way to set high-order bit of a fullword??

- **From:** "don eakin" <ua-author-2567354@usenetarchives.gap>
- **Date:** 1997-11-18T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddecbb9e2d-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ddecbb9e2d-p3@usenetarchives.gap>`
- **References:** `<64cprk$gpg$1@gte1.gte.net> <gap-ddecbb9e2d-p2@usenetarchives.gap> <gap-ddecbb9e2d-p3@usenetarchives.gap>`

```

Just issue the call and the compiler does the rest. The last address in
any parameter string hs the hi-bit turned on, i.e.;

call "xyz" using a,b,c.,

r14 = return address,
r15 address of field with "xyz" as a value, or in some cases, depending
on quotes or no quotes around the called program and the the linkage
editor parms, the actual address of xyz in your load module
and, in r1 an address of a list of parms, namely a,b,c, with the
compiler turning on the hi-bit of address c to x'80'
```

##### ↳ ↳ Re: Nice way to set high-order bit of a fullword??

- **From:** "lee whitaker" <ua-author-17071806@usenetarchives.gap>
- **Date:** 1997-11-16T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ddecbb9e2d-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ddecbb9e2d-p2@usenetarchives.gap>`
- **References:** `<64cprk$gpg$1@gte1.gte.net> <gap-ddecbb9e2d-p2@usenetarchives.gap>`

```

True to form, there seem to be several ways around the issue. Thnx to all
for the redefines approaches.

My problem was the compiler TRUNC option. I set this to TRUNC(BIN), and I
was able to just add 2^31+1 to the binary value. I guess that I just
looked at this too long and wandered down the wrong (asm) path.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
