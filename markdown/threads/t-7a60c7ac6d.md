[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# What are Spanned Records ?

_8 messages · 6 participants · 2001-02 → 2001-03_

---

### What are Spanned Records ?

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-02-28T02:01:11
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk>`

```
What are they and what are they used for ? I've been writing Cobol apps
for 15 years using unix and dos as the target op-sys. Only once have I
shoved code at a mainframe(didn't have a clue what I was doing but it
did work).
```

#### ↳ Re: What are Spanned Records ?

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-02-28T08:02:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97j0c2$m8r$1@slb3.atl.mindspring.net>`
- **References:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk>`

```
Well, ...
  First you need to understand about "blocking" records which is NOT
something that normally (ever?) occurs in UNIX and PC environments.  (The
COBOLs accept the "block contains" clause - but does NOTHING with them)

Once you understand what a "block" is, then a "spanned" record is one were
the record "spans" multiple blocks, i.e. the "record contains" clause is
LARGER than the "block contains" clause (in COBOL terms).

Even in systems that "fully support" blocked records, this is fairly unusual
(as "blocking" is usually an I/O efficiency issue - and spanning blocks
usually defeats the operating systems "blocking" efficiencies.)

Does this help at all?
```

#### ↳ Re: What are Spanned Records ?

- **From:** Steve Thompson <sthompson2_@neo.rr.com>
- **Date:** 2001-02-28T14:46:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A9D0EEB.62DE3DE@neo.rr.com>`
- **References:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk>`

```
Alister Munro wrote:
> 
> What are they and what are they used for ? I've been writing Cobol apps
> for 15 years using unix and dos as the target op-sys. Only once have I
> shoved code at a mainframe(didn't have a clue what I was doing but it
> did work).

The idea of spanned records is foreign to those using computers
that do not deal in "block I/O".  Most PC systems that I've dealt
with are byte I/O oriented, as are most UNIX platforms that I've
been exposed to.

To make this very simple, I will explain this in terms of the IBM
mainframe systems.

There are two types of records and they are fixed and variable.

If you take the fixed record format and you decide to take
advantage of the architecture, then you may find that you can put
multiple logical records (the way you and your program sees
things) into one physical record (the way the hardware sees
things).

This also holds true for variable length records.  You can put
them into blocks as well.  Here is where we run into a problem. 
How do you know one record from the other if they are not all the
same size?  Well, with MVS & DOS/VS based I/O, you have an RDW
(Record Descriptor Word).  This word tells you how long the
record is that follows it.  Then, if the blocks are variable in
size, you have the BDW (Block Descriptor Word), which tells you
how long the block is.

Suppose that I'm working with telemetry where the records are
very long.  To deal with this, we need to have something called
spanned records, so that the logical record can be longer than
the block (or physical record).

The area where this is used on a daily basis is the resource
accounting system called SMF (System Management Facility).  The
operating system writes out a VBS (Variable Blocked Spanned) file
that contains all the records for charge-back accounting for this
operating system.  Basically, all the I/O that your tasks do get
recorded in a record.  All the CPU usage gets recorded in a
record. All the memory usage and so forth.

Hope this is helpful.
```

#### ↳ Re: What are Spanned Records ?

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-02-28T15:02:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cq8n6.1634$7Y1.212430@newsread2.prod.itd.earthlink.net>`
- **References:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk>`

```
The trivial answer is: a spanned record is one which requires more
than one physical record. Suppose a customer record requires four
punched cards to contain all the information about a customer. You
have one customer record spanned over four physical records.

Hardware reads physical records - programs process logical records.

A physical record may contain: 1)multiple logical records, 2) one
logical record, 3)part of a logical record, 4)(from 0 to) multiple
physical records and (up to two) parts of additional physical records.

In cases 3 & 4, you have spanned records.

The case above on punched cards may seem silly, but most hardware has
some limitation as to the maximum physical size of a record. For
example, tape drives were once limited to 32k bytes per physical
record (and may still). Sometimes this physical limitation is
insufficient to accommodate the logical record requirements.


"Alister Munro" <alister@specsoft.freeserve.co.uk> wrote in message
news:97hm1g$eag$1@newsg4.svr.pol.co.uk...
> What are they and what are they used for ? I've been writing Cobol
apps
> for 15 years using unix and dos as the target op-sys. Only once have
I
> shoved code at a mainframe(didn't have a clue what I was doing but
it
> did work).
>
>
>
>
```

#### ↳ Re: What are Spanned Records ?

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-03-01T00:05:58
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97k3lg$9ai$1@news8.svr.pol.co.uk>`
- **References:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk>`

```
Thanks for the reply people. As mentioned by an earlier post these spanned
records must be bad news as to the I-O overhead.

The largest record I have used is certainly no more that 4096 bytes except
for a general purpose screen enquiry which contains 8960bytes (32 * 280
byte records used as a form of 'Bucketing)'.

Just out of interest, what type of systems are you people writing where
such large records are required ?

"Alister Munro" <alister@specsoft.freeserve.co.uk> wrote in message
news:97hm1g$eag$1@newsg4.svr.pol.co.uk...
> What are they and what are they used for ? I've been writing Cobol apps
> for 15 years using unix and dos as the target op-sys. Only once have I
…[5 more quoted lines elided]…
>
```

##### ↳ ↳ Re: What are Spanned Records ?

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2001-03-07T22:06:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AA6B0CD.6A72E466@boeing.com>`
- **References:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk> <97k3lg$9ai$1@news8.svr.pol.co.uk>`

```
Alister Munro wrote:
> > 
> Just out of interest, what type of systems are you people writing where
> such large records are required ?
> 

I have a Heritage system feed (meaning the system was written some time
ago and I use the data from that system)

It is a mainframe system that has a 32K record length - when I download
that record to relational tables - it creates 8 different tables - one
of the GROUP areas is repeated as many as 450 times (which creates one
very, very large master record).

	Susan A
```

#### ↳ Re: What are Spanned Records ?

- **From:** "Don Nelson" <don.nelson@compaq.com>
- **Date:** 2001-03-01T17:21:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<%ACn6.2$ou6.102@gazette.loc1.tandem.com>`
- **References:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk>`

```
Although the replies seemed to indicate that these apply to mainframes only,
that is not true.  Many mini-computers support them as well as other
machines.  They are not limited to IBM either.  The ANSI tape standard
defines such records as well (in a much better way than IBM).  The other
comments do say what they are so I won't go into that.  I might also mention
that they do not slow down I-O, they generally speed it up.  The bigger the
blocks the faster the I-O (normally).  And, if a record can span blocks you
have blocks that are consistent in size.  For example, if your block is 5000
characters and your records are 132 some of them will span a block.  That
is, you can pack lots of records in a block and only the first part of the
block and last part of the block will have spanned ones.  Or, you can have
giant records where one may span more than one block.

Don Nelson
```

##### ↳ ↳ Re: What are Spanned Records ?

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-03-02T03:34:42
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<97n48m$obb$1@news5.svr.pol.co.uk>`
- **References:** `<97hm1g$eag$1@newsg4.svr.pol.co.uk> <%ACn6.2$ou6.102@gazette.loc1.tandem.com>`

```
How is record locking handled when using blocking ? Does the 'block' act
as a cache ? (Last one) Are there any differences code wise in working with
blocks other than the definition ?

"Don Nelson" <don.nelson@compaq.com> wrote in message
news:%ACn6.2$ou6.102@gazette.loc1.tandem.com...
> Although the replies seemed to indicate that these apply to mainframes
only,
> that is not true.  Many mini-computers support them as well as other
> machines.  They are not limited to IBM either.  The ANSI tape standard
> defines such records as well (in a much better way than IBM).  The other
> comments do say what they are so I won't go into that.  I might also
mention
> that they do not slow down I-O, they generally speed it up.  The bigger
the
> blocks the faster the I-O (normally).  And, if a record can span blocks
you
> have blocks that are consistent in size.  For example, if your block is
5000
> characters and your records are 132 some of them will span a block.  That
> is, you can pack lots of records in a block and only the first part of the
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
