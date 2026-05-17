[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File open limit of HP MF cobol?

_2 messages · 2 participants · 1996-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### File open limit of HP MF cobol?

- **From:** "jung-ho ahn" <ua-author-17073801@usenetarchives.gap>
- **Date:** 1996-12-23T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<59oeel$il0$1@snunews.snu.ac.kr>`

```


What is the number of files that can be opened
simultaneously in HP MF cobol?
(I failed to open 120 indexed files simultaneously.
(error code: 9) )
Is that limit configurable? If not, how can I
handle a large number of files?

Thanks in advance,

==============================================================
 Jung-Ho Ahn                        || 
 OOPSLA Lab. Dept. of Computer Eng. ||
 Seoul National University          ||
 Shilim-Dong Gwanak-Gu,             || E-mail: 
 Seoul 151-742, KOREA               ||  jh··.@pap··c.kr
==============================================================
```

#### ↳ Re: File open limit of HP MF cobol?

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-12-25T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e5fe23d6ee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<59oeel$il0$1@snunews.snu.ac.kr>`
- **References:** `<59oeel$il0$1@snunews.snu.ac.kr>`

```

I get disconcerted sometimes on the COBOL news group when people do not
answer the question posed, and instead question the posters intent/method.
However, I am about to become guilty of that. Why do you need to open so
many indexed files all at once?

But to answer your question, there is a RTS switch you can set (I think
it's /F) to set the number of files that can be opened at once in Micro
Focus COBOL.

I beleive the limit is 255.

Jung-Ho Ahn wrote in article
<59oeel$il0$1.··.@snu··c.kr>...
› 
› What is the number of files that can be opened
…[16 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
