[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS in batch

_7 messages · 7 participants · 2001-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS in batch

- **From:** petert@my-deja.com
- **Date:** 2001-01-24T10:05:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94m9d6$nou$1@nnrp1.deja.com>`

```
I want to have an MVS batch Cobol DL/I program do an EXEC CICS LINK.
It appears to be possible but the site I am at has never done it before
hence there is no example or procedures to follow.
Any ideas??


Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: CICS in batch

- **From:** WOB Consulting <wobconsult@sprynet.com>
- **Date:** 2001-01-24T10:35:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94mb5j$oo8$1@nnrp1.deja.com>`
- **References:** `<94m9d6$nou$1@nnrp1.deja.com>`

```
In article <94m9d6$nou$1@nnrp1.deja.com>,
  petert@my-deja.com wrote:
> I want to have an MVS batch Cobol DL/I program do an EXEC CICS LINK.
> It appears to be possible but the site I am at has never done it
before
> hence there is no example or procedures to follow.
> Any ideas??
…[3 more quoted lines elided]…
>

Look into "EXCI" (External CICS Interface). Minimum CICS/ESA
Version/Release is 4.1.0. No problem with any Version/Release of
CICS/TS.

IBM Bookmanager :

http://www.s390.ibm.com/bookmgr-cgi/bookmgr.cmd/LIBRARY

HTH....

Bill





Sent via Deja.com
http://www.deja.com/
```

#### ↳ Re: CICS in batch

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 2001-01-24T14:43:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94mpn9$4fl$1@nnrp1.deja.com>`
- **References:** `<94m9d6$nou$1@nnrp1.deja.com>`

```
In article <94m9d6$nou$1@nnrp1.deja.com>,
  petert@my-deja.com wrote:
> I want to have an MVS batch Cobol DL/I program do an EXEC CICS LINK.
> It appears to be possible but the site I am at has never done it
…[5 more quoted lines elided]…
>

Are you looking for a sample procedure to be able to prepare, compile
and link a COBOL program containing an EXEC CICS LINK?
You could use the IBM sample procedures in the library
cics.cicslevel.SDFHPROC. You could start with the member DFHEITCL.
You should evaluate to use the translator option NOLINKAGE if your
program depends on parameters since otherwise the transalator generates
two more parameters in your USING of your PROCEDURE DIVISION.
You might want to consult the CICS Programming Guide at:
http://www.s390.ibm.com:80/bookmgr-cgi/bookmgr.cmd/BOOKS/DFHJAP34
The chapter '1.2.16 COBOL3 translator option' could be your starting
point.
```

##### ↳ ↳ Re: CICS in batch

- **From:** "mangogrower" <mangogrower@telocity.co>
- **Date:** 2001-01-24T21:41:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RiMb6.353$Ch.201886@newsrump.sjc.telocity.net>`
- **References:** `<94m9d6$nou$1@nnrp1.deja.com> <94mpn9$4fl$1@nnrp1.deja.com>`

```
Look in your site's CICS libs for *.SDFHSAMP  (sample)
Look for DFH0CXCC
or do 3.14
search value 'EXCI '
DSN= '*.*.SDFHSAMP(*)'

Also using either the Mainfram 'BookManager'
or PC Library Reader,
Search CICS for
(manual External CICS Interface for your part, and Server Support for
Clients OR ? Interregion
Communication / IRC, and OR Resource Definition Online for the CICS groups
part)

Daniel Jacot <daniel.jacot@winterthur.ch> wrote in message
news:94mpn9$4fl$1@nnrp1.deja.com...
> In article <94m9d6$nou$1@nnrp1.deja.com>,
>   petert@my-deja.com wrote:
…[29 more quoted lines elided]…
> http://www.deja.com/
```

#### ↳ Re: CICS in batch

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2001-01-25T03:42:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010124224213.07463.00001180@ng-ct1.aol.com>`
- **References:** `<94m9d6$nou$1@nnrp1.deja.com>`

```
>rom: petert@my-deja.com
>Date: 1/24/01 5:05 AM Eastern Standard Time

>I want to have an MVS batch Cobol DL/I program do an EXEC CICS LINK.
>It appears to be possible but the site I am at has never done it before
>hence there is no example or procedures to follow.
>Any ideas??
>

For what purpose?

Several have suggested the EXCI and if that is the way you wish to go after you
read the documentation I have a paper on the step by step process to go thru to
program for it you can have.  It covers all the things I learned as I did my
first EXCI.

Eileen
```

##### ↳ ↳ Re: CICS in batch

- **From:** alex <alex.ortiz@cpa.state.tx.us+3>
- **Date:** 2001-01-25T06:08:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<94p4vp$kr$1@goblin.tdh.state.tx.us>`
- **References:** `<94m9d6$nou$1@nnrp1.deja.com> <20010124224213.07463.00001180@ng-ct1.aol.com>`

```
YukonMama wrote:

> >rom: petert@my-deja.com
> >Date: 1/24/01 5:05 AM Eastern Standard Time
…[9 more quoted lines elided]…
>

maybe to run an asynchronous transaction????? maybe to run an existing
cics program???   maybe just to fart round?????
```

##### ↳ ↳ Re: CICS in batch

- **From:** "Peter Taylor" <taycon@nospam.bigpond.com>
- **Date:** 2001-01-25T20:15:14+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9CUb6.9548$65.55103@newsfeeds.bigpond.com>`
- **References:** `<94m9d6$nou$1@nnrp1.deja.com> <20010124224213.07463.00001180@ng-ct1.aol.com>`

```
Batch appeared to be the way to go for a program to read a sequential file,
gather some data from DLI, prepare a commarea consisting of a large XML
structure and link to a cics process on Unix via Encina etc
But with little sysprog support, and no precedent we look like making the
program CICS, the file in via a DCT extrapartition entry - then we only have
to figure out how to trigger it off.....


YukonMama <yukonmama@aol.com> wrote in message
news:20010124224213.07463.00001180@ng-ct1.aol.com...
> >rom: petert@my-deja.com
> >Date: 1/24/01 5:05 AM Eastern Standard Time
…[9 more quoted lines elided]…
> Several have suggested the EXCI and if that is the way you wish to go
after you
> read the documentation I have a paper on the step by step process to go
thru to
> program for it you can have.  It covers all the things I learned as I did
my
> first EXCI.
>
> Eileen
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
