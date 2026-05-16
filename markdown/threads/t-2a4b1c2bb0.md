[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to get record len for RECFM=U recs

_6 messages · 4 participants · 2003-01_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to get record len for RECFM=U recs

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-01-10T18:02:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0301101802.3d8aac51@posting.google.com>`

```
Hi,

Can someone out there help? I don't have access to a mainframe, so I
cant't test this.

I know you can get the length of a RECFM=V/VB rec by using 

RECORD VARYING .... DEPENDING ON WS-LEN

in the FD and WS-LEN will contain the rec length after a READ.

In spite of the fact that V/VB recs contain RDW/BDWs and RECFM U recs
don't, will the same technique work for RECFM U recs?

Thanx for your help, Jack.
```

#### ↳ Re: How to get record len for RECFM=U recs

- **From:** robert@jones0086.freeserve.co.uk (Robert Jones)
- **Date:** 2003-01-11T12:54:36-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fcd09c56.0301111254.5b47131@posting.google.com>`
- **References:** `<8a2d426e.0301101802.3d8aac51@posting.google.com>`

```
Hello Jack,

The bad news is that there is/was no way to do this directly from
COBOL.  Usually, RECFM=U files are set up as VB equivalents with a
length count in the first two bytes of the four byte record
descriptor, but they don't have to be, in which case you have to rely
on determining the record descriptions and record types from the
program that creates them.  I think it would be possible to get
individual record lengths, if you used an assembler program for the
file access, but I don't know how to do that myself, it's probably in
the DSCB, but I haven't delved that far myself.  Other people have
posted certain assembler programs and interfaces on this newsgroup in
the past (perhaps Gilbert St-Flour), which may give you a clue where
to look, though I don't think any have actually done what you request.

Good luck

Robert

jacksleight@hotmail.com (Jack Sleight) wrote in message news:<8a2d426e.0301101802.3d8aac51@posting.google.com>...
> Hi,
> 
…[12 more quoted lines elided]…
> Thanx for your help, Jack.
```

#### ↳ Re: How to get record len for RECFM=U recs

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2003-01-11T15:51:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<avq3km$e2p$1@slb0.atl.mindspring.net>`
- **References:** `<8a2d426e.0301101802.3d8aac51@posting.google.com>`

```
Jack,
  Have you read the section on

"3.5.3 Change in file handling for COBOL programs with RECORDING MODE U
under OS/390, Version 2 Release 10"

at:

 http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3mg10/3.5.3

I am not POSITIVE that this is "relevant" to your question, but it does
relate to at least one other post in this thread - and I think *MAY* give
you an idea of why trying to do this in COBOL is not a good idea.
```

##### ↳ ↳ Re: How to get record len for RECFM=U recs

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-01-11T20:02:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0301112002.3eb305ab@posting.google.com>`
- **References:** `<8a2d426e.0301101802.3d8aac51@posting.google.com> <avq3km$e2p$1@slb0.atl.mindspring.net>`

```
Robert,

Thanx for your reply. You're right, this can be done in BAL. The field
to use, as I recall from days gone by, is the risidual byte count of
the IOB. But I'm looking for a COBOL solution.

One would assume that if they allow you to specify RECORDING MODE U,
they would give you the tool(s) to process that type file.

I guess I could specify a max block size for the record then
initialize it to all X'FF' or some such. After the read I could loop
thuough the record until I encounter X'FF's. Seems kind of clumsy and
it doesn't solve the problem of rewriting the block. How do you
specify the size of the block to be written?

Bill,

Thank you too for the reply. I read the munual section you were kind
enough to supply, but it doesn't solve my problem.

Yes, I do plan to use VB recs as RECFM=U annd I would do as suggested
in the manual, but the length probllem still remains. I guess I'll
have to wait until I can get my hands on a mainframe to see if RECORD
VARYING... DEPENDING... solves the problem.

Thanx again to both of you for your help, Jack. 




"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<avq3km$e2p$1@slb0.atl.mindspring.net>...
> Jack,
>   Have you read the section on
…[32 more quoted lines elided]…
> > Thanx for your help, Jack.
```

###### ↳ ↳ ↳ Re: How to get record len for RECFM=U recs

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-01-13T08:46:02-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E22B50A.563D3222@istar.ca>`
- **References:** `<8a2d426e.0301101802.3d8aac51@posting.google.com> <avq3km$e2p$1@slb0.atl.mindspring.net> <8a2d426e.0301112002.3eb305ab@posting.google.com>`

```
Given what you are doing, the COBOL READ of a RECFM=U file reads a block
at a time.  Thus the first 4 bytes contain the blocksize in the first
two bytes.  The second 4 bytes contain the record size of the first
record in the first two bytes.  If the file is variable block spanned
(VBS) read the manual for what the second two bytes contains (one of the
DF series of manuals I think). In effect, you are doing your own record
handling for each block.  If you are reading a true RECFM=U file you
will need to get access to the DCB (data control block) in order to get
the length of the block read.  I believe that it is in the DCBRECFM
field. 

Jack Sleight wrote:
> 
> Robert,
…[61 more quoted lines elided]…
> > > Thanx for your help, Jack.
```

###### ↳ ↳ ↳ Re: How to get record len for RECFM=U recs

_(reply depth: 4)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-01-13T19:30:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0301131930.58b6b99e@posting.google.com>`
- **References:** `<8a2d426e.0301101802.3d8aac51@posting.google.com> <avq3km$e2p$1@slb0.atl.mindspring.net> <8a2d426e.0301112002.3eb305ab@posting.google.com> <3E22B50A.563D3222@istar.ca>`

```
Clark,

You're correct that processing V/VB recs as U recs doesn't pose a
problem. But one would think that COBOL, giving you the ability to
read/write a RECFM=U file, would give you the ability to do so
correctly, and hopefully, document the process fully.

It's my contention that the documentation is lacking.

Has anyone tried to use the RECORD VARYING...DEPENDING ON... technique
to read/write a RECFM=U file? Did it return the blksize in the
DEPENDING on object field?

Thanx, Jack.

   



"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message news:<3E22B50A.563D3222@istar.ca>...
> Given what you are doing, the COBOL READ of a RECFM=U file reads a block
> at a time.  Thus the first 4 bytes contain the blocksize in the first
…[73 more quoted lines elided]…
> > > > Thanx for your help, Jack.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
