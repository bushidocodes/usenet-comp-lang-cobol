[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AREASIZE

_2 messages · 2 participants · 1998-08_

---

### AREASIZE

- **From:** "kfe..." <ua-author-8579235@usenetarchives.gap>
- **Date:** 1998-08-17T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6rciuk$1ag$1@eve.enteract.com>`

```
I'm looking for information about a COBOL File Descriptor feature
called AREASIZE. It appears in some legacy COBOL programs and our
current Microfocus compiler doesn't mention it in it's documentation,
although it does compile programs containing it successfully. I'd like
to know what it does and what sort of value one might attach to it.

Thanks,


Regards,

Kent Feiler
Communications Programming, Inc
http://www.cpiusa.com/
kfe··.@cpi··a.com
```

#### ↳ Re: AREASIZE

- **From:** "charles stevens" <ua-author-6373722@usenetarchives.gap>
- **Date:** 1998-08-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f42fe2d7ee-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6rciuk$1ag$1@eve.enteract.com>`
- **References:** `<6rciuk$1ag$1@eve.enteract.com>`

```
Unisys A Series and Clear Path HMP NX/LX series have a mechanism called
File Attributesof which AREASIZE is one. If I remember correctly so do
other ex-Burroughs Unisys (B1000, V-series) systems.
]
Presuming one of thes is the legacy you're dealing with, the attribute has
to do with what I guess would be "multiple XTENTs"on some other mainframes.
The attribute specifies how large, in RECORDS, a given AREA (or "section")
of the file is to be. Up to 1000 AREAS (another attribute) can be
specified for a file. The specific syntax would be "VALUE [OF] AREASIZE
[IS] "; the
general syntax is "VALUE [OF] [IS] ".

For systems that don't "page" their files on disk, the construct can be
deleted.

-Chuck Stevens [cha··.@uni··s.com]


Kent Feiler  wrote in article
<6rciuk$1ag$1.··.@eve··t.com>...
> I'm looking for information about a COBOL File Descriptor feature
> called AREASIZE. It appears in some legacy COBOL programs and our
…[14 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
