[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Internal sort in MF cobol

_4 messages · 4 participants · 1996-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Internal sort in MF cobol

- **From:** "bert duerinck" <ua-author-17072731@usenetarchives.gap>
- **Date:** 1996-12-04T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32A6BB4B.5FAA@denkart.be>`

```

Hello,

Does anybody know if there are some problems with the sort memory, when
you sort a file with the internal MF cobol SORT?
Because i wanted to sort a file with variable record size and a size of
12M, the result was that the file was not sorted correctly.

thanks
```

#### ↳ Re: Internal sort in MF cobol

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1996-12-04T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e9abcaf48-p2@usenetarchives.gap>`
- **In-Reply-To:** `<32A6BB4B.5FAA@denkart.be>`
- **References:** `<32A6BB4B.5FAA@denkart.be>`

```

We have sorted much larger files with no problems, but to my knowledge, we
have never tried to sort a variable length record file.


Bert Duerinck wrote in article
<32A··.@den··t.be>...
› Hello,
› 
…[6 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Internal sort in MF cobol

- **From:** "celg..." <ua-author-14983142@usenetarchives.gap>
- **Date:** 1996-12-04T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e9abcaf48-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8e9abcaf48-p2@usenetarchives.gap>`
- **References:** `<32A6BB4B.5FAA@denkart.be> <gap-8e9abcaf48-p2@usenetarchives.gap>`

```

Did you try defining the input file as line sequential? I have used that
technique before with good results.

Gary

› 
› Bert Duerinck  wrote in article
…[9 more quoted lines elided]…
››
```

#### ↳ Re: Internal sort in MF cobol

- **From:** "clark morris" <ua-author-8441861@usenetarchives.gap>
- **Date:** 1996-12-09T19:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8e9abcaf48-p4@usenetarchives.gap>`
- **In-Reply-To:** `<32A6BB4B.5FAA@denkart.be>`
- **References:** `<32A6BB4B.5FAA@denkart.be>`

```

One thing to watch out for is that the key is wholly contained within
the shortest record in the file. Wierd results will occur when
sorting on positions 50-55 of a 40 byte record.
›  
› We have sorted much larger files with no problems, but to my   
…[17 more quoted lines elided]…
› 

Clark F. Morris, Jr.
CFM Technical Programming Services
Bridgetown, Nova Scotia, Canada
cmo··.@fox··n.ca
on assignment at morrisc.nbnet.nb.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
