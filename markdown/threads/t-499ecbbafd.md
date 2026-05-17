[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WHEN phrase, MF COBOL

_3 messages · 3 participants · 1997-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### WHEN phrase, MF COBOL

- **From:** "w..." <ua-author-12858376@usenetarchives.gap>
- **Date:** 1997-08-26T04:42:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<872584929.18498@dejanews.com>`

```

Hi there,

for a data warehouse project I'm using a COBOL generator. The generated
code is compiled on HPUX with microfocus v4. The compiler gives an error
message:
A "WHEN" phrase did not have a matching verb and was discarded.
However, in the whole cobol source there is no WHEN phrase.
The line number points to one line after the last source code line.

Any idea?

Thanks in advance,
Martin Wallmer

-------------------==== Posted via Deja News ====-----------------------
http://www.dejanews.com/ Search, Read, Post to Usenet
```

#### ↳ Re: WHEN phrase, MF COBOL

- **From:** "john m. saxton, jr" <ua-author-17071440@usenetarchives.gap>
- **Date:** 1997-08-25T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-499ecbbafd-p2@usenetarchives.gap>`
- **In-Reply-To:** `<872584929.18498@dejanews.com>`
- **References:** `<872584929.18498@dejanews.com>`

```


w.··.@sof··g.de wrote:
› 
› Hi there,
…[14 more quoted lines elided]…
›       http://www.dejanews.com/     Search, Read, Post to Usenet
Any evaulates? Missing period is my best guess
Return address is John underscore Saxton at ML dot com
```

#### ↳ Re: WHEN phrase, MF COBOL

- **From:** "sdlbr..." <ua-author-17071763@usenetarchives.gap>
- **Date:** 1997-08-27T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-499ecbbafd-p3@usenetarchives.gap>`
- **In-Reply-To:** `<872584929.18498@dejanews.com>`
- **References:** `<872584929.18498@dejanews.com>`

```

If the error message said the WHEN was discarded, that is why you cannot
find it. However, the times I have seen that particular error have been if
I used EVALUATE and forgot the WHEN within the EVALUATE. Could that be the
problem??
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
