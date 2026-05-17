[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# General COMP-3 question

_7 messages · 7 participants · 1997-10_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### General COMP-3 question

- **From:** "myron rumsey" <ua-author-11902457@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34351582.3167@servtech.com>`

```

I am a little rusty with my COBOL, but I'm working on converting some
files to a COBOL record layout for an outside vendor, but I don't have a
COBOL compiler and am using another language. I ran into a stumbling
block with the layout's COMP-3 packed decimals and am working on a
manual conversion procedure. Here's my question:

If I have a PIC S9(3) COMP-3 format to represent the signed number
"+375" then the number will be stored in 2 bytes, one with "37" in it
and one with "5C" in it. But on a binary level is the 1st byte stored
as "0010 0101" (37) or "0011 0111" (a 3 and a 7)? If it is stored like
in the 1st scenario, then how is the "5C" stored?

Any help is GREATLY appreciated! Thanks!
```

#### ↳ Re: General COMP-3 question

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41ef6b4ad1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34351582.3167@servtech.com>`
- **References:** `<34351582.3167@servtech.com>`

```

Myron Rumsey wrote:
› 
› 
…[7 more quoted lines elided]…
› Any help is GREATLY appreciated!  Thanks!

It's a '3' and a '7' in each half-byte, as in your second example. Thus
a '5' and a 'C'

John
```

#### ↳ Re: General COMP-3 question

- **From:** "bill lynch" <ua-author-92065@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41ef6b4ad1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34351582.3167@servtech.com>`
- **References:** `<34351582.3167@servtech.com>`

```

Myron Rumsey wrote:
› 
› I am a little rusty with my COBOL, but I'm working on converting some
…[11 more quoted lines elided]…
› Any help is GREATLY appreciated!  Thanks!

It'll be stored as X'375c' - each digit takes up 4 bits, as does the
sign (your 2nd scenario).

Hope this helps,
Bill Lynch
```

#### ↳ Re: General COMP-3 question

- **From:** "richard j jackson" <ua-author-13440361@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41ef6b4ad1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34351582.3167@servtech.com>`
- **References:** `<34351582.3167@servtech.com>`

```

Myron Rumsey wrote:

› I am a little rusty with my COBOL, but I'm working on converting some
› files to a COBOL record layout for an outside vendor, but I don't have
…[13 more quoted lines elided]…
› Any help is GREATLY appreciated!  Thanks!

In the binary format the sign is stored in the high order bit.
The number 375 is stored in binary.

Richard Jackson
Houston, Tx
```

#### ↳ Re: General COMP-3 question

- **From:** "adam.j..." <ua-author-17072612@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41ef6b4ad1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34351582.3167@servtech.com>`
- **References:** `<34351582.3167@servtech.com>`

```

On Fri, 03 Oct 1997 08:55:47 -0700, Myron Rumsey
wrote:

› If I have a PIC S9(3) COMP-3 format to represent the signed number
› "+375" then the number will be stored in 2 bytes, one with "37" in it
› and one with "5C" in it.  But on a binary level is the 1st byte stored
› as "0010 0101" (37) or "0011 0111" (a 3 and a 7)?  If it is stored like
› in the 1st scenario, then how is the "5C" stored?


It isn't, it is stored in the second manner, so +375 is:

0011 0111 0101 1100.

and -375 is:

0011 0111 0101 1101.

Therefore, if you look at a COMP-3 field in hexadecimal dump format,
you can see the actual decimal values stored.
====================================================================
Adam Jon Jefferson Work mailto:ada··.@ge··m.com
EASAMS Ltd. Home mailto:Ada··.@m··.com
Manufacturing Systems Division
Chelmsford ESSEX UK
** Opinions not those of EASAMS Ltd. **
====================================================================
```

#### ↳ Re: General COMP-3 question

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-10-02T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41ef6b4ad1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<34351582.3167@servtech.com>`
- **References:** `<34351582.3167@servtech.com>`

```

In article <343··.@ser··h.com>,
Myron Rumsey wrote:
› 
› If I have a PIC S9(3) COMP-3 format to represent the signed number
› "+375" then the number will be stored in 2 bytes, one with "37" in it
› and one with "5C" in it.  But on a binary level is the 1st byte stored
› as "0010 0101" (37) or "0011 0111" (a 3 and a 7)?
 
› The latter.
 
 
› [...] how is the "5C" stored?

"0101 1100".

Decimal +375 is X'177' or B'0000 0001 0111 0111'. Notice that there is
no obvious relationship between the decimal number and its hexadecimal
representation.

Packed decimal 375+ is X'375C' or B'0011 0111 0101 1100'. Notice how
easy it is to spot the original number.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: General COMP-3 question

- **From:** "be..." <ua-author-17073405@usenetarchives.gap>
- **Date:** 1997-10-03T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-41ef6b4ad1-p7@usenetarchives.gap>`
- **In-Reply-To:** `<34351582.3167@servtech.com>`
- **References:** `<34351582.3167@servtech.com>`

```

If the true integer is +375, then it's '0011 0111 0101 1100'=x'375c'.




Myron Rumsey wrote:
› 
› I am a little rusty with my COBOL, but I'm working on converting some
…[11 more quoted lines elided]…
› Any help is GREATLY appreciated!  Thanks!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
