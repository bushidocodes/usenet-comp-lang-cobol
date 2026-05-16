[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to Recover records Deleted using COBOL physical delete comman?

_6 messages · 4 participants · 2003-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to Recover records Deleted using COBOL physical delete comman?

- **From:** calvinchin@fm333.com (Calvin)
- **Date:** 2003-01-07T17:49:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62843e96.0301071749.742a9704@posting.google.com>`

```
Hi there,

I need help here.

I was doing my year end program to clear out some records in a file.

I was using DELETE abc-file command in the program. After deleted, I
am no longer able to access those records deleted.

But when I type the file out int DOS PROMPT, it seems that the record
still there with a special character in front of it (could be an
indicator in DOS).

I would like to ask to help on how to get back those deleted records?
using COBOL commands or DOS commands?

Thank you in advance.

Regards,

Calvin
```

#### ↳ Re: How to Recover records Deleted using COBOL physical delete comman?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-07T22:34:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5uadnesGEbIBN4ajXTWckw@giganews.com>`
- **References:** `<62843e96.0301071749.742a9704@posting.google.com>`

```

"Calvin" <calvinchin@fm333.com> wrote in message
news:62843e96.0301071749.742a9704@posting.google.com...
> Hi there,
>
…[14 more quoted lines elided]…
> Thank you in advance.

Write a program to copy the file in sequential format (instead of relative)
and change the first byte during the copy to whatever character does NOT
mean deleted.
```

##### ↳ ↳ Re: How to Recover records Deleted using COBOL physical delete comman?

- **From:** calvinchin@fm333.com (Calvin)
- **Date:** 2003-01-08T20:54:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62843e96.0301082054.7d4ab190@posting.google.com>`
- **References:** `<62843e96.0301071749.742a9704@posting.google.com> <5uadnesGEbIBN4ajXTWckw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message news:<5uadnesGEbIBN4ajXTWckw@giganews.com>...
> "Calvin" <calvinchin@fm333.com> wrote in message
> news:62843e96.0301071749.742a9704@posting.google.com...
…[20 more quoted lines elided]…
> mean deleted.


Thanks for your answer. However, when reading the file, COBOL will not
be able to read those deleted records, so how can I write it to the
sequential format?

Thank you.

Regards,
Calvin
```

###### ↳ ↳ ↳ Re: How to Recover records Deleted using COBOL physical delete comman?

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-01-10T01:20:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cdpT9.35236$p_6.2995688@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<62843e96.0301071749.742a9704@posting.google.com> <5uadnesGEbIBN4ajXTWckw@giganews.com> <62843e96.0301082054.7d4ab190@posting.google.com>`

```

Calvin <calvinchin@fm333.com> wrote in message news:62843e96.0301082054.7d4ab190@posting.google.com...
> "JerryMouse" <nospam@bisusa.com> wrote in message news:<5uadnesGEbIBN4ajXTWckw@giganews.com>...
> > "Calvin" <calvinchin@fm333.com> wrote in message
…[26 more quoted lines elided]…
> sequential format?

Read the file in straight sequential format also.  You are basically treating it
as a simple text file.  Read each record, manipulate the first byte if necessary,
and write each record.
```

###### ↳ ↳ ↳ Re: How to Recover records Deleted using COBOL physical delete comman?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-01-09T18:17:10-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0301091817.5f3d228@posting.google.com>`
- **References:** `<62843e96.0301071749.742a9704@posting.google.com> <5uadnesGEbIBN4ajXTWckw@giganews.com> <62843e96.0301082054.7d4ab190@posting.google.com>`

```
calvinchin@fm333.com (Calvin) wrote 

> Thanks for your answer. However, when reading the file, COBOL will not
> be able to read those deleted records, so how can I write it to the
> sequential format?

The suggestion was that you _read_ the file as if it were a sequential
file.  A sequential file is just 'one record after another' and has no
concept of whether a record is deleted or not.

Whether this can be done or not is entirely dependant on how the files
are structured and this is different for each vendor, and sometimes by
version.

For example with MF Level II format indexed files an indexed file is
in two parts: a data file and an index file.  The data file is just a
collection of fixed size records, each terminated by x'0D0A'.  A
deleted record is marked by changing this to x'0D00'.

It is possible to read the data part of an indexed file as
organization sequential and to specify the record as 2 bytes longer to
cover the record marker.  Reading this file will give all records
including deleted ones and 'junk' records where file space has been
allocated and no record has yet been written.  The records will be in
physical order.

However, different Cobol systems have different mechanisms and there
is no guarantee that a system will be able to read the data file in
any way that would be useful.  For example Fujitsu Cobol may have its
indexed file as a single file with data records and index blocks
mixed.  This may make it impossible to access deleted records.

As you have not mentioned the brand of Cobol, the version, the
operating system or any other relevant details, any suggestions are
merely guesses and may be less than helpful.
```

#### ↳ Re: How to Recover records Deleted using COBOL physical delete comman?

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-01-07T22:41:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0301072240.23f51c86@posting.google.com>`
- **References:** `<62843e96.0301071749.742a9704@posting.google.com>`

```
calvinchin@fm333.com (Calvin) wrote 

> I was using DELETE abc-file command in the program. After deleted, I
> am no longer able to access those records deleted.

That is correct, DELETE makes them no longer accessable.
 
> But when I type the file out int DOS PROMPT, it seems that the record
> still there with a special character in front of it (could be an
> indicator in DOS).

That is quite likely.  The file still occupies the same space on the
disk and the DELETEd records are marked as being reusable space.  If
you write new records to the file then the file probably won't expand
in size, the new records will overwrite the deleted ones.
 
> I would like to ask to help on how to get back those deleted records?
> using COBOL commands or DOS commands?

In general you can't.  However, if you mention the brand of Cobol and
version, and how the SELECT..ASSIGN then someone may be able to
suggest something.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
