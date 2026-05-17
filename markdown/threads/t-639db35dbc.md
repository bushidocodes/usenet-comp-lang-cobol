[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol - MFINS.ENV

_2 messages · 2 participants · 1995-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol - MFINS.ENV

- **From:** "rag..." <ua-author-654840@usenetarchives.gap>
- **Date:** 1995-12-18T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b7mm0$l1c@interport.net>`

```

I want to move from one logical drive to another working COBOL setup. I
know to edit config.sys - but what is the MFINS.ENV file?

This is a read only file in ¥COBOL¥LBR...

I really DON'T want to reinstall!

Thanks!

                                            Kevin Danzig
      rag··.@int··t.net               ----------------
        DEV0352 - IBMLink
```

#### ↳ Re: MF Cobol - MFINS.ENV

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1995-12-19T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-639db35dbc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4b7mm0$l1c@interport.net>`
- **References:** `<4b7mm0$l1c@interport.net>`

```
The MFINS.ENV file is created when you first installed the
product and records what choices you made. It is used whenever
you do maintenance (upgrades). This is *not* official Micro Focus
"policy" but I think that if you changed the attribute and copied
it over, then reset it, that you should be OK. (You might want
to look "in" it. I think it records what drive you installed
on.)

Hope this helps.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
