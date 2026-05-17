[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help needed with file-handling

_4 messages · 4 participants · 1997-04_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Help needed with file-handling

- **From:** "sari haavisto" <ua-author-17073604@usenetarchives.gap>
- **Date:** 1997-04-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc4361$727fd440$8140dac3@default>`

```

What is wrong with this beginnig of my cobol-program??

$set ans85
identification division.
program-id. selaahenktied.
author. p-haavisto.
date-written. 5-4-97.
*
enviroment division.
input-output section.
file-control.
select henkilo assign to "a:henktied.seq"
organization is line sequential.
*
data division.
file section.
fd henkilo.
01 tyontekija.


Help me I'm beginner!
```

#### ↳ Re: Help needed with file-handling

- **From:** "lott..." <ua-author-4950817@usenetarchives.gap>
- **Date:** 1997-04-09T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b25c65eb6a-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc4361$727fd440$8140dac3@default>`
- **References:** `<01bc4361$727fd440$8140dac3@default>`

```

In article <01bc4361$727fd440$8140dac3@default>, sha··.@d··.fi says...
Try a smaller program-id (name).
› 
› What is wrong with this beginnig of my cobol-program??
…[21 more quoted lines elided]…
›
```

##### ↳ ↳ Re: Help needed with file-handling

- **From:** "the programmer" <ua-author-6589121@usenetarchives.gap>
- **Date:** 1997-04-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b25c65eb6a-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-b25c65eb6a-p2@usenetarchives.gap>`
- **References:** `<01bc4361$727fd440$8140dac3@default> <gap-b25c65eb6a-p2@usenetarchives.gap>`

```

Isn't it supposed to be ENVIRONMENT DIVISION? e-n-v-i-r-o-N-m-e-n-t
```

#### ↳ Re: Help needed with file-handling

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1997-04-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b25c65eb6a-p4@usenetarchives.gap>`
- **In-Reply-To:** `<01bc4361$727fd440$8140dac3@default>`
- **References:** `<01bc4361$727fd440$8140dac3@default>`

```

On 7 Apr 1997 14:36:10 GMT, "Sari Haavisto" wrote:

› What is wrong with this beginnig of my cobol-program??
› 
…[20 more quoted lines elided]…
› 
Of course, the program is incomplete, assuming that the column
alignment is correct, then the only "real" error so far is that
"enviroment division." is misspelled -- should be "enviroNment
division".

George Trudeau
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
