[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# DFSDDLT0 problem

_2 messages · 2 participants · 1996-08_

---

### DFSDDLT0 problem

- **From:** "ha..." <ua-author-17072611@usenetarchives.gap>
- **Date:** 1996-08-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6E94uohVZZB@wharp.rhein-main.de>`

```

I need some information how to write a batch DFSDDLT0 JCL statement:

Suppose I have an IMS-Database only with root segments and a length of 300
Bytes each. Now I want for every segment to

1.) replace the contens of the three columns 34 to 36 with 'XXX' when the
contens of columns 4 to 7 is 'YYYY'

2.) replace the contens of the three columns 38 to 40 with X'00001C' when
the contens of columns 9 to 10 is X'003C'

3.) add 1 to the value in column 16 to 18

Is this feasible ?

Where can I get further appropriate information about that (on the web) ?

Thanx in advance

Michael
```

#### ↳ Re: DFSDDLT0 problem

- **From:** "sara and michael bass" <ua-author-17086175@usenetarchives.gap>
- **Date:** 1996-08-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ff185b6eb-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6E94uohVZZB@wharp.rhein-main.de>`
- **References:** `<6E94uohVZZB@wharp.rhein-main.de>`

```
Michael Haertfelder wrote:
› 
› I need some information how to write a batch DFSDDLT0 JCL statement:
…[22 more quoted lines elided]…
› 

You can do all of that and more.... Attached is a zip file containing a word doc with
DLT0 explanations and examples. Also included is a font which will make it easier to
read.

Good luck,
Mike
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
