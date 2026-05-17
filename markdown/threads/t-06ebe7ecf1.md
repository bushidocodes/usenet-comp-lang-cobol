[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus Cobol conversion

_2 messages · 2 participants · 1998-03_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Microfocus Cobol conversion

- **From:** "sa..." <ua-author-15603129@usenetarchives.gap>
- **Date:** 1998-03-25T11:47:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fbcba$os7$1@nnrp2.dejanews.com>`

```

I am converting a Microfocus Cobol application (runtime environment v2.3)
to Visual Basic and had a question on deleted records.

I need to find out how a deleted record is represented by the system, since
the data stays in the .ism file.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: Microfocus Cobol conversion

- **From:** "gene..." <ua-author-6589206@usenetarchives.gap>
- **Date:** 1998-03-31T22:25:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-06ebe7ecf1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6fbcba$os7$1@nnrp2.dejanews.com>`
- **References:** `<6fbcba$os7$1@nnrp2.dejanews.com>`

```

In article <6fbcba$os7$1.··.@nnr··s.com>,
sa··.@cmi··c.com wrote:
› 
› I am converting a Microfocus Cobol application (runtime environment v2.3)
…[7 more quoted lines elided]…
› 
If your purpose in asking this question is so that you can exclude those
records don't bother with doing it with code. (although if you write the
conversion program in MicroFocus COBOL it would be exclude deleted records
anyway) just run the REBUILD utility against your file. That will
permanently delete the records and reclaim the space. The syntax is REBUILD
...

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
