[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ACUCobol

_2 messages · 2 participants · 1997-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### ACUCobol

- **From:** "mann..." <ua-author-17071359@usenetarchives.gap>
- **Date:** 1997-04-23T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<335f7baa.69612178@news.eni.net>`

```

Help...

I'm trying to convert a pin calculating routine from ACUCobol to C and
I need to know numbers are respresented internally. The original
ACUCobol programmer is not available. Here are a few sample variable
declarations:

PIN-HEX-03-DEF PIC 9(5) COMP-1 VALUE 15

FILLER PIC 99 COMP-1 VALUE 15

I've been told that the numbers are two bytes and their internal
representation would be like a two byte unsigned integer in C. Ex: 15
would be 0x000f. I did some research and found that COMP-1 is four
byte floating point.

Can anyone answer this question?

Email responses to either: man··.@atl··a.com or
YSS··.@pro··y.com

Thanks,
Ted Baskin
```

#### ↳ Re: ACUCobol

- **From:** "dennis taylor" <ua-author-34211@usenetarchives.gap>
- **Date:** 1997-04-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ce392ad2f4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<335f7baa.69612178@news.eni.net>`
- **References:** `<335f7baa.69612178@news.eni.net>`

```

› 
› PIN-HEX-03-DEF                 PIC 9(5) COMP-1  VALUE 15  
…[6 more quoted lines elided]…
› byte floating point.

>From the Acucobol reference manual:

COMP-1 16-bit signed binary
COMP-2 store 1 byte per decimal position (not quite the same as usage
DISPLAY)
COMP-3 BCD
COMP-4 signed binary, intel format (big endian?), but as many bytes as
required for the picture.
COMP-5 like comp-4, but the endian-ness is based on the host machine.
COMP-6 unsigned COMP-3.


Knock yourself out.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
