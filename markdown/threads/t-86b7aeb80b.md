[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol DATACOMPRESS

_2 messages · 2 participants · 1996-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol DATACOMPRESS

- **From:** "victor odhner" <ua-author-10907080@usenetarchives.gap>
- **Date:** 1996-04-02T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4jut5d$csf@nnrp1.news.primenet.com>`

```
I am trying to produce a compressed sequential file on a Sun Unix system
with MF COBOL. The directive $SET DATACOMPRESS"1" works very nicely
for our indexed files, but when I put that directive in a program that
writes a 'line sequential' file, no compression occurs. I also added
$SET CALLFH"EXTFH" although this is supposed to be the default on Unix.
Apparently there's no attempt at compression, though the file contains
strings of 8 or more spaces all over the place.

Am I missing something I should do? Should this really be working?
```

#### ↳ Re: MF Cobol DATACOMPRESS

- **From:** "s..." <ua-author-599642@usenetarchives.gap>
- **Date:** 1996-04-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-86b7aeb80b-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4jut5d$csf@nnrp1.news.primenet.com>`
- **References:** `<4jut5d$csf@nnrp1.news.primenet.com>`

```
In article <4jut5d$c.··.@nnr··t.com>, vod··.@pri··t.com says...
› 
› I am trying to produce a compressed sequential file on a Sun Unix system
…[7 more quoted lines elided]…
› Am I missing something I should do?  Should this really be working?

It's working as it should AFAIK. It doesn't compress line sequential. Why
would you want to do that? The idea behind line sequential is for print
reports or readable text files.

Shaun C. Murray                        | e-mail: s.··.@mfl··o.uk 
Micro Focus Ltd, Newbury, UK.          | www:    http://www.mfltd.co.uk/~scm/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
