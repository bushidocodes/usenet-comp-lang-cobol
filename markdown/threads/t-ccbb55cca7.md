[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Centuries in VS Cobol II

_3 messages · 3 participants · 1997-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Centuries in VS Cobol II

- **From:** "freddie schwenke" <ua-author-13484813@usenetarchives.gap>
- **Date:** 1997-01-07T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32D3D484.3347@sanlam.co.za>`

```

Hi

Does anyone know how to obtain the century in VS Cobol II? Is it at all
possible? I'm not sure what happens in the background when the ACCEPT
...FROM DATE command is issued, that's why I have this question.

Thanks.

Freddie
:)
```

#### ↳ Re: Centuries in VS Cobol II

- **From:** "john mckown" <ua-author-1779298@usenetarchives.gap>
- **Date:** 1997-01-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccbb55cca7-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32D3D484.3347@sanlam.co.za>`
- **References:** `<32D3D484.3347@sanlam.co.za>`

```

Freddie,
IBM will supply you with a program that they developed. It is called
"IGZEDT4". Your COBOL/MVS type systems person can get this FREE from IBM by
requesting it. Basically you use it like:

01 TODAYS-DATE.
05 FOUR-DIGIT-YEAR PIC 9999.
05 MONTH PIC 99.
05 DAY PIC 99.

CALL "IGZEDT4" USING TODAYS-DATE.

There is an "Official" MVS APAR number for this puppy, but I don't remember
what it is.

Freddie Schwenke wrote in article
<32D··.@san··o.za>...
› Hi
› 
…[8 more quoted lines elided]…
›
```

#### ↳ Re: Centuries in VS Cobol II

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-01-08T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ccbb55cca7-p3@usenetarchives.gap>`
- **In-Reply-To:** `<32D3D484.3347@sanlam.co.za>`
- **References:** `<32D3D484.3347@sanlam.co.za>`

```

No function directly exists to obtain the centruy in VS COBOL II.

You could write an assembler program to do it.

You could imply it based on the year.

You could obtain the "Bridge to the next Century" package that provides
emulation for the 5 date related intrinsic functions that are available in
later (COBOL/370, COBOL for MVS and VM) compilers. (Near blatant
advertizement - cg··.@i··.net for info).

If you have LE/370 you could "cheat" and reference the LE intrinsics to
get the year.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
