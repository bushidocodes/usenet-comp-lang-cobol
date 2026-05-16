[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# See Delete Records

_3 messages · 3 participants · 2001-07_

---

### See Delete Records

- **From:** "PorTy" <euromercante1@clix.pt>
- **Date:** 2001-07-20T18:38:26+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m1_57.13007$fd2.38274061@newsserver.ip.pt>`

```
Hello,
How could see delete records in a Micro Focus File (indexed).
I need recover some records.

Very Thanks,
Joe
```

#### ↳ Re: See Delete Records

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-07-20T20:43:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9j9tmp$qjl$1@newsg3.svr.pol.co.uk>`
- **References:** `<m1_57.13007$fd2.38274061@newsserver.ip.pt>`

```
Reading the data file as if it were sequential should give all records
including those deleted.

"PorTy" <euromercante1@clix.pt> wrote in message
news:m1_57.13007$fd2.38274061@newsserver.ip.pt...
> Hello,
> How could see delete records in a Micro Focus File (indexed).
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: See Delete Records

- **From:** "Russell Styles" <rwstyles@worldnet.att.net>
- **Date:** 2001-07-21T01:30:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NW467.45486$C81.3831329@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<m1_57.13007$fd2.38274061@newsserver.ip.pt> <9j9tmp$qjl$1@newsg3.svr.pol.co.uk>`

```
    This might be a problem.  If the file has fixed length
reccords, and NO
compression, this might work, but you will probably need to
read the file as a byte stream, not as a micro focus variable
record size (with 128 byte header) sequential file.

    See the manual, it has a fair explanation of file structure,
but no help on what the various "system records" are.

    Try creating a (very) short test file, and examining it.
With known data and history, you will have a better
chance of figuring things out.


"Alister Munro" <alister@specsoft.freeserve.co.uk> wrote in
message news:9j9tmp$qjl$1@newsg3.svr.pol.co.uk...
> Reading the data file as if it were sequential should give all
records
> including those deleted.
>
…[11 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
