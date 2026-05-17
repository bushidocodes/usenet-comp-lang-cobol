[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What is comp-6 ?

_8 messages · 8 participants · 1996-10 → 1996-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### What is comp-6 ?

- **From:** "robert benson" <ua-author-905059@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32787A28.10D4@ul.ie>`

```

can anyone tell me what COMPUTATIONAL-6 means. ie what is its useage in
COBOL.


Thanks.
```

#### ↳ Re: What is comp-6 ?

- **From:** "michel krabshuis" <ua-author-6589453@usenetarchives.gap>
- **Date:** 1996-10-30T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d97da7b89a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32787A28.10D4@ul.ie>`
- **References:** `<32787A28.10D4@ul.ie>`

```

It's something like an packed decimal in other languages without a decimal.
2 bytes packed together in 1 byte.
Grtx /\/\ichel

Robert Benson schreef in artikel
<327··.@u··.ie>...
| can anyone tell me what COMPUTATIONAL-6 means. ie what is its useage in
| COBOL.
…[3 more quoted lines elided]…
|
```

#### ↳ Re: What is comp-6 ?

- **From:** "ggr..." <ua-author-1091801@usenetarchives.gap>
- **Date:** 1996-10-31T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d97da7b89a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32787A28.10D4@ul.ie>`
- **References:** `<32787A28.10D4@ul.ie>`

```

Robert Benson wrote:

› can anyone tell me what COMPUTATIONAL-6 means. ie what is its useage in
› COBOL.

if I recall, this would depend on your particular compiler, because
AFAIK, COMPUTATIONAL values only go out to 3 in the standard itself...
```

##### ↳ ↳ Re: What is comp-6 ?

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-10-31T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d97da7b89a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d97da7b89a-p3@usenetarchives.gap>`
- **References:** `<32787A28.10D4@ul.ie> <gap-d97da7b89a-p3@usenetarchives.gap>`

```

Glenn Grotzinger wrote:
› 
› Robert Benson  wrote:
…[5 more quoted lines elided]…
› AFAIK, COMPUTATIONAL values only go out to 3 in the standard itself...

There are no COMP-n values in the standard. Any -n values are
implementor-defined. COMP (COMPUTATIONAL) with no -n says it is some
implementor-defined method of any radix. That is all. PACKED-DECIMAL
says it is some sort of implementor-defined gizmo that is radix 10 but
is scrunched. BINARY says it is some sort of implementor-defined
method of radix 2. Anything other than the default or DISPLAY is
implementor-defined. In fact, even DISPLAY is implementor-defined if
there is an S in the PICTURE (if there is no SIGN ... SEPARATE
clause).

Don Nelson
COBOL Development, Tandem Computers, Inc.
Member, ANSI X3J4 and ISO/IEC JTC1/SC22 WG4 COBOL Committees
nel··.@tan··m.com
No clever quotes here
```

###### ↳ ↳ ↳ Re: What is comp-6 ?

- **From:** "chris borgnaes" <ua-author-12407404@usenetarchives.gap>
- **Date:** 1996-11-03T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d97da7b89a-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-d97da7b89a-p4@usenetarchives.gap>`
- **References:** `<32787A28.10D4@ul.ie> <gap-d97da7b89a-p3@usenetarchives.gap> <gap-d97da7b89a-p4@usenetarchives.gap>`

```

At my site, COMP-6 is a 36-bit binary field.

Don Nelson wrote in article
<327··.@tan··m.com>...
› Glenn Grotzinger wrote:
›› 
…[8 more quoted lines elided]…
›
```

#### ↳ Re: What is comp-6 ?

- **From:** "pkei..." <ua-author-17086679@usenetarchives.gap>
- **Date:** 1996-11-03T19:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d97da7b89a-p6@usenetarchives.gap>`
- **In-Reply-To:** `<32787A28.10D4@ul.ie>`
- **References:** `<32787A28.10D4@ul.ie>`

```

In article <327··.@u··.ie>, Robert Benson writes:
› can anyone tell me what COMPUTATIONAL-6 means. ie what is its useage in
› COBOL.
›
›
› Thanks.
```

#### ↳ Re: What is comp-6 ?

- **From:** "tom morrison" <ua-author-1138665@usenetarchives.gap>
- **Date:** 1996-11-03T19:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d97da7b89a-p7@usenetarchives.gap>`
- **In-Reply-To:** `<32787A28.10D4@ul.ie>`
- **References:** `<32787A28.10D4@ul.ie>`

```

Robert Benson wrote in article
<327··.@u··.ie>...
› can anyone tell me what COMPUTATIONAL-6 means. ie what is its useage in
› COBOL.

COMP-6 as used in RM/COBOL and it predecessors (e.g. NCR, TI) is a packed
decimal, two BCD digits per 8-bit byte, representation with no sign. For
example:
A-NUMBER PIC 9(8) COMP-6 value 123
would be stored in three bytes as X"000123". This was mainly a storage
saving usage that was also somewhat useful when one wished to use unsigned
numbers in an indexed file key, since there was no sign representation to
interfere with the collating sequence.
COMP-6 is now an anachronism which should not be used in any new code.

Micro Focus can treat COMP-6 either equivalent to the RM representation, or
as "regular" packed decimal (see the description of the COMP-6 directive).

I hope this helps.

Tom Morrison, T.M··.@li··t.com
Liant Software Corporation
512-719-7019  FAX:512-719-7070  WWW: http://www.liant.com/
```

#### ↳ Re: What is comp-6 ?

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1996-11-09T19:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d97da7b89a-p8@usenetarchives.gap>`
- **In-Reply-To:** `<32787A28.10D4@ul.ie>`
- **References:** `<32787A28.10D4@ul.ie>`

```

Robert Benson wrote:
: can anyone tell me what COMPUTATIONAL-6 means. ie what is its useage in
: COBOL.


: Thanks.

Comp-6 is the same as Comp-3 without the sign. As such, it always stores
an even number of digits in the field.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
