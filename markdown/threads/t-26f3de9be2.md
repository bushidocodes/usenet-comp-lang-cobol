[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CR/LF for IRS disk

_5 messages · 5 participants · 1998-01_

---

### CR/LF for IRS disk

- **From:** "gary..." <ua-author-572733@usenetarchives.gap>
- **Date:** 1998-01-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19980119222200.RAA10216@ladder02.news.aol.com>`

```

We have been submitting our 1099 data to the IRS using mag tape for several
years. My boss now wants to start sending a floppy disk. The IRS Mag. Media
manual says that for diskettes, they need a CR in position 419 and LF in 420.
We are using an HP 3000 using COBOL 85. Does anyone know how this can be done?

Thanks!

Gary
```

#### ↳ Re: CR/LF for IRS disk

- **From:** "the goobers" <ua-author-1837635@usenetarchives.gap>
- **Date:** 1998-01-18T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26f3de9be2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19980119222200.RAA10216@ladder02.news.aol.com>`
- **References:** `<19980119222200.RAA10216@ladder02.news.aol.com>`

```

GaryJay1 wrote:
› 
› We have been submitting our 1099 data to the IRS using mag tape for several
…[6 more quoted lines elided]…
› Gary

Yes, I know how this can be done... next?

DD
```

#### ↳ Re: CR/LF for IRS disk

- **From:** "bi..." <ua-author-8405640@usenetarchives.gap>
- **Date:** 1998-01-18T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26f3de9be2-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19980119222200.RAA10216@ladder02.news.aol.com>`
- **References:** `<19980119222200.RAA10216@ladder02.news.aol.com>`

```

In article <199··.@lad··l.com>,
gar··.@a··.com (GaryJay1) wrote:
› We have been submitting our 1099 data to the IRS using mag tape for several
› years. My boss now wants to start sending a floppy disk. The IRS Mag. Media
…[6 more quoted lines elided]…
› Gary

Hi Gary,

I'll solve your problem for you - read the manual again. Positions 419 and
420 are "reserved for use as ... CR/LF IF APPLICABLE". Those positions may be
spaces if you do not have to use CR/LF.
```

#### ↳ Re: CR/LF for IRS disk

- **From:** "joseph kohler" <ua-author-6589497@usenetarchives.gap>
- **Date:** 1998-01-19T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26f3de9be2-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19980119222200.RAA10216@ladder02.news.aol.com>`
- **References:** `<19980119222200.RAA10216@ladder02.news.aol.com>`

```

GaryJay1 wrote:
› 
› We have been submitting our 1099 data to the IRS using mag tape for several
…[6 more quoted lines elided]…
› Gary

Gary,
Why don't you just transmit the old tape file format via modem to the
IRSBBS system. They take the tape format compressed or uncompressed.
Check out their web site or call them to get the phone #. My client
uses this and it works fine.

Joe.
Joe
+-------------------------------------------------------+
| Nothing is fool-proof to a sufficiently talented fool.|
+-------------------------------------------------------+      
| In order to reply via e-mail address as follows:      |
|      jkohler at compuserve dot com                    |
| replace the at and dot with the appropriate symbols.  |
+-------------------------------------------------------+
```

#### ↳ Re: CR/LF for IRS disk

- **From:** "don eakin" <ua-author-2567354@usenetarchives.gap>
- **Date:** 1998-01-20T19:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-26f3de9be2-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19980119222200.RAA10216@ladder02.news.aol.com>`
- **References:** `<19980119222200.RAA10216@ladder02.news.aol.com>`

```

What hardware and COBOL compiler are you using??? Please spend some
time and place as much detail as possible in your questions.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
