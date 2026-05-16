[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Attempting to read variable length records as raw data

_5 messages · 4 participants · 2002-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### Attempting to read variable length records as raw data

- **From:** broom@voicenet.com (broom)
- **Date:** 2002-04-13T11:33:03-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c948eb61.0204131033.17dcbe06@posting.google.com>`

```
I've got 3490 EBCDIC tapes that were produced on an IBM S/390 
box.

The language that created them is COBOL, and the layout shows 
multiple "occurs" fields at the end of the record.

I'm told that these are variable length records, and if the 
tailend occurs fields are not used, then they won't be stored 
on tape.

Looking at the tape shows be the 1st record starts with
3E 26 00 00 02 DF 00 00 and then the actual data (I think),
and then all other records have a 4 byte prefix which seems
to vary.

02 DF 00 00 seems common, as it 97 60 00 00 and others.
The record size is LRECL (max, I guess) of 7261, but it
should be a minimum of 277 (which is the end of the last
non-occurs field).

Doing a "big-endian" unsigned 16 bit dump of the 02 DF
gives me 735, which is 40 bytes into the next record so
that can't be right.

Is there any reference that can show me how to dump this
data?

Thanks.

Please email, as well as post, and I will summarize.

Thanks.

Barry
```

#### ↳ Re: Attempting to read variable length records as raw data

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-04-13T18:21:44-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9aeif$83m$1@slb2.atl.mindspring.net>`
- **References:** `<c948eb61.0204131033.17dcbe06@posting.google.com>`

```
It would help us if you could show us the JCL that created the tape file.
For the moment, I will assume that it is a VB (Variable blocked) format
file.  If so, there is a "block descriptor word" at the beginning of each
block and then a record descriptor word at the beginning of each record.
(This would explain the 1st record's prefix being "different" from later
ones - at least until you reach the next block).

Can you tell us what operating system and "tools" you are using to "dump"
this file?  If you have COBOL on the "receiving system" - the chances are
that this would be your easiest method of reading the file.

I think that before anyone can tell you exactly how to "interpret" your
file, we will need to know more about how it was created and where/how you
are trying to "dump" it.
```

#### ↳ Re: Attempting to read variable length records as raw data

- **From:** Liam Devlin <LiamD@dontspam.optonline.net>
- **Date:** 2002-04-14T07:13:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CB92C0F.F3D8B48B@dontspam.optonline.net>`
- **References:** `<c948eb61.0204131033.17dcbe06@posting.google.com>`

```
broom wrote:
> 
> I've got 3490 EBCDIC tapes that were produced on an IBM S/390
…[21 more quoted lines elided]…
> that can't be right.

The language isn't the determining factor on IBM mf's, it's a function
of the access method. This looks like straightforward VB QSAM. The
length of records is stored by QSAM as LLbb, i.e., a 2-byte binary
length followed by the "bb" field, typically binary zeroes, called a
Record Descriptor Word (RDW). The "LL" includes the length of the RDW. 

A block of VB data looks like:

RDW = block length, so this block is 15,910 bytes long (max LRECL is
probably something like 16,000 or 16,384. 
The first logical record begins at the 5th byte and is 735 bytes long.
Its RDW is located at start of block +4 bytes. 

The 2nd logical record is located at the beginning of the block+4+735,
and so on. This logical record contains 731 bytes of data.

(offsets are relative to one)

HTH
```

#### ↳ Re: Attempting to read variable length records as raw data

- **From:** Liam Devlin <LiamD@dontspam.optonline.net>
- **Date:** 2002-04-14T07:13:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3CB92C1C.83DC06C0@dontspam.optonline.net>`
- **References:** `<c948eb61.0204131033.17dcbe06@posting.google.com>`

```
broom wrote:
> 
> I've got 3490 EBCDIC tapes that were produced on an IBM S/390
…[21 more quoted lines elided]…
> that can't be right.

The language isn't the determining factor on IBM mf's, it's a function
of the access method. This looks like straightforward VB QSAM. The
length of records is stored by QSAM as LLbb, i.e., a 2-byte binary
length followed by the "bb" field, typically binary zeroes, called a
Record Descriptor Word (RDW). The "LL" includes the length of the RDW. 

A block of VB data looks like:

RDW = block length, so this block is 15,910 bytes long (max LRECL is
probably something like 16,000 or 16,384. 
The first logical record begins at the 5th byte and is 735 bytes long.
Its RDW is located at start of block +4 bytes. 

The 2nd logical record is located at the beginning of the block+4+735,
and so on. This logical record contains 731 bytes of data.

(offsets are relative to one)

HTH
```

#### ↳ Re: Attempting to read variable length records as raw data

- **From:** jnjsle@aol.com (Jnjsle)
- **Date:** 2002-04-15T04:37:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020415003719.11106.00003782@mb-ca.aol.com>`
- **References:** `<c948eb61.0204131033.17dcbe06@posting.google.com>`

```
Hi Barry,

You don't mention what environment you plan to use this data in or what you
intend to do to it. So I'll assume you don't have mainframe or COBOL resources
at your disposal. 

If you have the capabilty of reading the data  a block at a time, you can use
the info Liam provided to loop thru the block and extract the individual
records. 

The remaining problem you face is the tables at the end of the recs (the
multiple occurs). If you provide a copy of the record layout, that may provide
some clues.

Regards, Jack.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
