[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DB2 Summing - Decimals?

_3 messages · 2 participants · 2001-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### DB2 Summing - Decimals?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-09-07T18:49:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yE8m7.6377$ym4.251499@iad-read.news.verio.net>`

```

Greets, all... a bit of this was covered a few weeks back but I've run
into another interesting wrinkle.

The column is TOTAL_PRICE DECIMAL(11, 2); this gets translated into
BFLGMP-TOTAL-PRICE PIC S9(09)V99 USAGE COMP-3.  What's needed is a SELECT
SUM(TOTAL_PRICE) INTO :WS-SUMTOT... and I seem to be losing the decimals
when I define WS-SUMTOT PIC S9(9) COMP VALUE +0.

Other definitions give 'INVALID HOST VARIABLE' errors and trying to
REDEFINE the field still loses the decimals... anyone know where I might
find a way out?

Thanks much.

DD
```

#### ↳ Re: DB2 Summing - Decimals?

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2001-09-08T03:18:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<w6gm7.30239$OA2.4055737558@newssvr15.news.prodigy.com>`
- **References:** `<yE8m7.6377$ym4.251499@iad-read.news.verio.net>`

```
    If I understand you correctly, WS-SUMTOT needs to be of the same data
type (packed decimal) and length as the column being summed.  You're losing
the decimal places because an integer data type (binary) has no decimals.
```

##### ↳ ↳ Re: DB2 Summing - Decimals?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-09-10T13:14:44+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<813n7.6509$ym4.260195@iad-read.news.verio.net>`
- **References:** `<yE8m7.6377$ym4.251499@iad-read.news.verio.net> <w6gm7.30239$OA2.4055737558@newssvr15.news.prodigy.com>`

```
In article <w6gm7.30239$OA2.4055737558@newssvr15.news.prodigy.com>,
Terry Heinze <terryheinze@prodigy.net> wrote:
>    If I understand you correctly, WS-SUMTOT needs to be of the same data
>type (packed decimal) and length as the column being summed.  You're losing
>the decimal places because an integer data type (binary) has no decimals.

I am an idiot, I am a fool, I am a chump and a dolt, I am a janitor, not a
programmer... when I was looking at the DECLARE I mistranslated DECIMAL
(11, 2) as PIC S9(11)V99 COMP-3 instead of as S9(9)V99 COMP-3; when I
tried to define WS-SUMTOT as the former I would get the INVALID HOST
VARIABLE errors.  Your suggestion caused me to re-visit this and use the
right definition.

Greatly appreciated, Mr Heinze.

DD

>" NA" <docdwarf@clark.net> wrote in message
>news:yE8m7.6377$ym4.251499@iad-read.news.verio.net...
…[18 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
