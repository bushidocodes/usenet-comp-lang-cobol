[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Procobol & oracle database...

_2 messages · 2 participants · 1997-06_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Procobol & oracle database...

- **From:** "eric & tatuy" <ua-author-17071611@usenetarchives.gap>
- **Date:** 1997-06-13T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc789b$07a74d00$1f836fce@delavega.bigger.net>`

```

Im trying to update some Oracle records in ProCobol. Part of the key I
thought to be spaces is not. Nor is it nulls after trying to retrieve the
rows through Databrowser. Data was loaded through an SQL loader script.
What is its value and how should I initialize the host variable???

Thanks!!
```

#### ↳ Re: Procobol & oracle database...

- **From:** "timothy nicholson" <ua-author-12840417@usenetarchives.gap>
- **Date:** 1997-06-19T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d1ecdf03b0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc789b$07a74d00$1f836fce@delavega.bigger.net>`
- **References:** `<01bc789b$07a74d00$1f836fce@delavega.bigger.net>`

```

When INSERTing the row, use NVL. Example:

INSERT INTO USER_PASSWORDS
(CUSTOMER_NAME,
VALUES
(NVL(HVD_02_PW_NAME,' '));

This will force spaces into the name field.

Eric & Tatuy wrote in article
<01bc789b$07a74d00$1f8··.@del··r.net>...
› Im trying to update some Oracle records in ProCobol.  Part of the key I
› thought to be spaces is not.  Nor is it nulls after trying to retrieve
…[5 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
