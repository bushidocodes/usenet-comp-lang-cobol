[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF 4.0 DLLs

_2 messages · 2 participants · 1996-01_

---

### MF 4.0 DLLs

- **From:** "rbe..." <ua-author-570851@usenetarchives.gap>
- **Date:** 1996-01-25T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4eamel$7qo@cloner2.ix.netcom.com>`

```
Has anybody had much experience with creating 32 bit DLL's using
Microfocus COBOL 4.0. We are moving into NT & we put much of our
business logic into DLL's. It seems that creating DLLS in 32 bit MF
COBOL is different than in 16 bits. Any help or experiences would be
appreciated.


Rich Benack
```

#### ↳ Re: MF 4.0 DLLs

- **From:** "don..." <ua-author-16533359@usenetarchives.gap>
- **Date:** 1996-01-28T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-bdfec772b5-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4eamel$7qo@cloner2.ix.netcom.com>`
- **References:** `<4eamel$7qo@cloner2.ix.netcom.com>`

```
In <4eamel$7.··.@clo··m.com>, rbe··.@ix.··m.com(Richard Benack) writes:
› Has anybody had much experience with creating 32 bit DLL's using
› Microfocus COBOL 4.0. We are moving into NT & we put much of our
› business logic into DLL's.

We are using MF COBOL 4.0 on NT server 3.51. We have created many DLLs. Most of our problems have been related to calling NT services like SQLServer or SNA server.

Those problems have been resolved by making some directives changes and by using calling conventions other than the default.

I would be happy to correspond about the details.

Terry Doner
Toronto-Dominion Bank
Toronto, Ontario, Canada
don··.@tdb··k.ca
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
