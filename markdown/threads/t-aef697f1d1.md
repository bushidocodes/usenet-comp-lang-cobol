[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EOF Technique

_1 message · 1 participant · 2003-07_

---

### Re: EOF Technique

- **From:** "ShadowFox" <me@email.com>
- **Date:** 2003-07-12T12:35:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<CgTPa.41524$sY2.17783@rwcrnsc51.ops.asp.att.net>`
- **References:** `<le1sgv85u45941ifp1qh67vpqado4fhm0m@4ax.com>`

```
Jack,
The read at end is the IO and test.
EG
1000-read file.
     Read mastin into work-area at end
         perform 300-end-routines
         perform 400-close-files
         stop run.
Just my own 2 cents.
Bob fixit4you@attbi.com


"Jack Straw" <jackstraw@witchita> wrote in message
news:le1sgv85u45941ifp1qh67vpqado4fhm0m@4ax.com...
> I'm an experienced programmer, trying to get up to speed on Cobol.
> I've read the source to a few programs from various places, and I have
…[26 more quoted lines elided]…
> 0x3D561045
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
