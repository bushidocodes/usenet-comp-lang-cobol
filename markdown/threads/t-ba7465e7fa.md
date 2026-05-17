[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Intrinsic functions

_4 messages · 4 participants · 1997-09_

---

### Intrinsic functions

- **From:** "kfo..." <ua-author-15004755@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<341925d9.4245647@news.tig.com.au>`

```

Are intrinsic functions considered as 'cobol standard'.

Wat is the 'standard' return for 'function integer-of-date' when you
give it a crap date. The OS/390 compiler manual does not define it.
```

#### ↳ Re: Intrinsic functions

- **From:** "geh..." <ua-author-17073020@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba7465e7fa-p2@usenetarchives.gap>`
- **In-Reply-To:** `<341925d9.4245647@news.tig.com.au>`
- **References:** `<341925d9.4245647@news.tig.com.au>`

```


In <341··.@new··m.au>, kfo··.@tig··m.au (Ken Foskey) writes:
› Are intrinsic functions considered as 'cobol standard'.
›
…[3 more quoted lines elided]…
›


As I understand it, the instrinstic functions are an 'optional' module of the cobol
standard. The software developer does not have to impletemnt them if they don't want to,
but if they are implemented, then they must work acording to the cobol specs.

I dont think that there is a standard return defined for a 'bad date'



------------------------------------------------------------------------
Glenn Hoffman Voice - 770-795-0155 State of Georgia
Team OS/2 Fax - 770-795-0355 Dept of Revenue - Motor Vehicles
------------------------------------------------------------------------
```

#### ↳ Re: Intrinsic functions

- **From:** "ar..." <ua-author-89056@usenetarchives.gap>
- **Date:** 1997-09-12T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba7465e7fa-p3@usenetarchives.gap>`
- **In-Reply-To:** `<341925d9.4245647@news.tig.com.au>`
- **References:** `<341925d9.4245647@news.tig.com.au>`

```


Ken Foskey (kfo··.@tig··m.au) writes:
› Are intrinsic functions considered as 'cobol standard'.
›
I don't believe they are part of any "standards" but are extensions first
provided with COBOL/370.

› Wat is the 'standard' return for 'function integer-of-date' when you
› give it a crap date. The OS/390 compiler manual does not define it.
›
LE will take you down with an ABEND U4038. A message is written to SYSOUT
(or the MESSAGE DDNAME specified in the install.) * Here are two examples:

01 YYYYMMDD PIC 9(8).
01 INTEGER-DATE PIC S9(9) BINARY.

move "19971512" to YYYYMMDD
compute INTEGER-DATE = function integer-of-date(YYYYMMDD)
CEE2517S The month value in a CEEISEC call was not recognized.
move "19971232" to YYYYMMDD
compute INTEGER-DATE = function integer-of-date(YYYYMMDD)
CEE2508S The date value passed to CEEDAYS or CEESECS was invalid.

If you do not want an ABEND, you can write an LE condition handler for
these specific conditions.

* also assuming the option TERMTHDACT(QUIET) is not in effect
```

#### ↳ Re: Intrinsic functions

- **From:** "wal..." <ua-author-12880379@usenetarchives.gap>
- **Date:** 1997-09-16T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ba7465e7fa-p4@usenetarchives.gap>`
- **In-Reply-To:** `<341925d9.4245647@news.tig.com.au>`
- **References:** `<341925d9.4245647@news.tig.com.au>`

```

Ken Foskey (kfo··.@tig··m.au) wrote:
: Are intrinsic functions considered as 'cobol standard'.

Yes. The Intrinsic Function module is an optional module.

: Wat is the 'standard' return for 'function integer-of-date' when you
: give it a crap date.

The returned value is undefined. In fact, the result of making
the call is undefined. This applies to all the functions. This
is spelled out in Paragraph 1.2.2 of Section A of the Standard.

Walter Murray
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
