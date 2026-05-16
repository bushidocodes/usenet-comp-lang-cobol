[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Format of Microfocus Sequential files or conversion utility?

_2 messages · 2 participants · 2000-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`VSAM, files, sorting`](../topics.md#files)

---

### Format of Microfocus Sequential files or conversion utility?

- **From:** Tim Josling <tej@melbpc.org.au>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<392D93BD.7343EA5F@melbpc.org.au>`

```
Does anyone know the format of the microfocus/merant sequential
files (variable length, non-fixed format).

The records themselves seem to be x'40' then a one byte length
(at least for short records), then the data then it is padded out
to a multiple of 4 bytes, sometimes with zeros sometimes with
spaces. But there is 128 bytes at the start of the file that I
cannot entirely understand. There are two date/time stamps but
beyond that it is a mystery

Thanks,
Tim Josling
```

#### ↳ Re: Format of Microfocus Sequential files or conversion utility?

- **From:** "Bill Yarnall" <Bill.Yarnall@merant.com>
- **Date:** 2000-05-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8gnhpt$8mp$1@hyperion.mfltd.co.uk>`
- **References:** `<392D93BD.7343EA5F@melbpc.org.au>`

```
All variable length files under Micro Focus COBOL have a 128 byte header
which contains basic information about the file. Each data record in a
variable file has a record header the record header is identified by bit 6
ON ie x'40' followed by another byte containing the record length  is common
when writing  shorter record lengths(< 256), if you write bigger records
you'll see other values ie 41 or 42  and if you write really large records
then the record header will be 4 bytes long instead of only 2.

There are other record header used with in variable files , all of these
record headers are documented in the section of the documents titled 'file
structures'. The 128 byte file header  is documented in this section also.
Tim Josling <tej@melbpc.org.au> wrote in message
news:392D93BD.7343EA5F@melbpc.org.au...
> Does anyone know the format of the microfocus/merant sequential
> files (variable length, non-fixed format).
…[10 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
