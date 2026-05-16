[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reading CopyBook & Data Files

_1 message · 1 participant · 2007-12_

---

### Re: Reading CopyBook & Data Files

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2007-12-14T11:39:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f5e4c8f9-f671-4b12-b9d2-390432d7d708@e23g2000prf.googlegroups.com>`

```
On Dec 15, 5:49 am, "Will" <W...@somewhere.com> wrote:
> I'm still trying to extract the data from an old COBOL data base. (Thanks
> for the help so far!)
…[20 more quoted lines elided]…
> there is a file header that I want to discard.

I am not sure that you have posted the exact identification of the
Cobol product. It seems most likely to be MicroFocus Cobol/2 version
between 2.1 and 3,4.

These could write several different formats for indexed files. If
there is a 'file header' then this is most likely the C2 format. The
formats are fully explained in the manuals for the product.

With C2 there is a 128byte file header. Each record then has a 2 (or
4) byte record header. You should note that in using an indexed file
records may be rewritten or deleted. The record header indicates the
status of the following record and particular values indicate
'deleted' or a system record or other. Only when the first 4 bits of
the record header contain '0100' is it a user record. If you find a
value here > 0100 (4) then you will find that it is even more
complicated with pointers and reduced data.

Each record header will start on a 4 byte boundary, so up to 3 padding
characters will follow each data record. The other 12 bits of the
record header give the record length as this may be variable, and this
does not include the padding.

> I'm looking for the first
> byte of actual data here. Is it true that the first three lines in the above
…[8 more quoted lines elided]…
> discarded as I am only interested in getting a file with just the data...

Maybe, but discarding the headers may mean that you get more than
'just the data' you will also get deleted records and other stuff.

> Here is the first fo the data file Owners.FIL (I inserted the "-" for nulls
> and other non ASCII characters)
…[8 more quoted lines elided]…
> each record ???

No. there two bytes are system generated header. Only the PICs reserve
space in the records.

Under the FD there may be more than one 01 record level (though it
seems unlikely for this file).  Each 01 in a single FD describes the
same record area, they implicitly redefine each other. If there is
more than one 01 then you will need to identify the record to choose
which layout applies.

> Thanks for any assistance here as I think I'm getting close.

If this is MicroFocus then you should have a REBUILD.EXE program.
This can do most of the work for you by extracting the data records
and ignoring the deleted records and headers.

For example if you rebuild to a Level II format then the data file for
that will not have file or record headers

   REBUILD OWNERS.FIL,XOWNERS.LII /s:mf /t:lii

The data file (there will also be a separate .IDX) will be a simple
structure consisting of fixed length datarecordCRLF where CRLF is
x"0D0A" for valid records and x"0D00" for deleted or no record.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
