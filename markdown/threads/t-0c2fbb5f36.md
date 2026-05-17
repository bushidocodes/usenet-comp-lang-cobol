[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus Cobol/Environment Variables Question

_2 messages · 2 participants · 1997-06_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MicroFocus Cobol/Environment Variables Question

- **From:** "eric albacete" <ua-author-16628475@usenetarchives.gap>
- **Date:** 1997-06-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc703a$6a2169c0$d525a497@ealbacetent>`

```

Does anyone have an example of how to read UNIX environment variables from
a MF COBOL program? I think it involves using ACCEPT and the
ENVIRONMENT-NAME/ENVIRONMENT-VALUE functions but I am not clear on how to
use them.

Please email me directly if possible.

Thanks!
```

#### ↳ Re: MicroFocus Cobol/Environment Variables Question

- **From:** "wmcc..." <ua-author-2320533@usenetarchives.gap>
- **Date:** 1997-06-02T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0c2fbb5f36-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc703a$6a2169c0$d525a497@ealbacetent>`
- **References:** `<01bc703a$6a2169c0$d525a497@ealbacetent>`

```

Eric Albacete wrote:

› Does anyone have an example of how to read UNIX environment variables from
› a MF COBOL program?  I think it involves using ACCEPT and the
› ENVIRONMENT-NAME/ENVIRONMENT-VALUE functions but I am not clear on how to
› use them.

[posted and emailed]

First load the variable name, then read its value:

DISPLAY "job_id" UPON ENVIRONMENT-NAME
ACCEPT ing-job-id FROM ENVIRONMENT-VALUE

I got this off of the Microfocus web page long ago.

-Bill
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
