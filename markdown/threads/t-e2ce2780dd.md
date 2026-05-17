[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Convert Compressed EBCDIC ->ascii

_2 messages · 2 participants · 1995-01_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Convert Compressed EBCDIC ->ascii

- **From:** "craw..." <ua-author-6065189@usenetarchives.gap>
- **Date:** 1995-01-09T07:12:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3er97a$n6a@cronkite.ocis.temple.edu>`

```
Im trying to EBCDIC Packed Decimals and compressed fields (looks like
cobol compression) to an ascii format. I started playing around
with recode (GNU) and I think I figured out how to change it to
ascii (dd also) but the packed things are screwing me up...
how do the words/vectors look in compressed and packed format.
Keep in mind that an IBM mainframe's cobol did the compressing.

FYI, its all numbers that are compressed

I take the data off a tape using dd conv=ascii
but the packed decimals stay packed...(in cobol & ebcdic)

What am I trying to do... just look at the data in human readable form.
I can convert using C or perl easily if I knew what it looked like

|0|1|2|3|4|5|6|7|
^
|
first bit does? etc etc
Any help appreciated,
```

#### ↳ Re: Convert Compressed EBCDIC ->ascii

- **From:** "burton m. strauss iii" <ua-author-1717645@usenetarchives.gap>
- **Date:** 1995-01-09T07:58:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e2ce2780dd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3er97a$n6a@cronkite.ocis.temple.edu>`
- **References:** `<3er97a$n6a@cronkite.ocis.temple.edu>`

```
cra··.@ast··e.edu (David Crawford) wrote:
›
› Im trying to EBCDIC Packed Decimals

Packed decimals are packed decimals. With zoned decimal, it's just
the high order bits that change ASCII vs. EBCDIC.

Packed decimal uses each half (nibble) of the byte to store one
digit, except for the last nibble which is the sign.

(NB: All of this is in the Principals of Operations manual in FAR
more detail)...

So a 3 byte packed field containing 4322 is

0x04 32 2f

note the sign is 'f' meaning unsigned. c and d are the + and -
respectively... 0x 04 32 2d = -4322

Zoned decimal uses the characters (so it's ASCII vs. EBCDIC
sensitive) 0..9 with the last high order nibble used for a
sign:

0x F0 F4 F3 F2 F2 = 04322

0x F0 F4 F3 F2 D2 = 04322-

-----Burton
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
