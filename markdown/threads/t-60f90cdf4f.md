[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Foreign Language Support in Cobol II

_2 messages · 2 participants · 1995-02 → 1995-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Foreign Language Support in Cobol II

- **From:** "pfo..." <ua-author-1852842@usenetarchives.gap>
- **Date:** 1995-02-28T23:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3j0s3r$5j7@newsbf02.news.aol.com>`

```
Is anyone aware of foreign language support capabilities with Cobol II???

I have the need to support French, German, Italian, Spanish, etc.

Any ideas would be appreciated.

Thanks,

Pat Forth
Patrick T. Forth
```

#### ↳ Re: Foreign Language Support in Cobol II

- **From:** "mayer goldberg" <ua-author-4361383@usenetarchives.gap>
- **Date:** 1995-03-02T21:18:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-60f90cdf4f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3j0s3r$5j7@newsbf02.news.aol.com>`
- **References:** `<3j0s3r$5j7@newsbf02.news.aol.com>`

```
pfo··.@a··.com (PForth) writes:

› Is anyone aware of foreign language support capabilities with Cobol II???
 
› I have the need to support French, German, Italian, Spanish, etc.
 
› Any ideas would be appreciated.

Most foreign language support sits in ASCII 128 and up. Micro Focus
COBOL is more than adequate for this: It allows comments, strings, and
check this one: variable names and labels to be in ascii 128 and up. I
have my student's version MF Personal COBOL working with Hebrew with
NO problems. The letter aleph is in fact, the C-cedile you'll need for
French, etc.

One final hint, though it may not benefit the person to whom I
responded: For languages like Hebrew, Arabic, Farsi, Syriac, Urdu,
etc. all of which go from right to left: You can qualify a pic with
"justify right", or the cute "just right", which makes right to
left output easy.

Mayer

Mayer Goldberg
ma··.@cs.··a.edu
URL: http://www.cs.indiana.edu/hyplan/mayer.html
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
