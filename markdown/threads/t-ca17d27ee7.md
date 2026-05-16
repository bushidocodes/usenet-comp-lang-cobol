[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# U4038 JCL Abend in custom Statement Formatter

_7 messages · 6 participants · 2002-02 → 2002-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### U4038 JCL Abend in custom Statement Formatter

- **From:** nivas_shyam@indiatimes.com (shyam nivas)
- **Date:** 2002-02-26T09:29:13-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c02fd744.0202260929.582e965f@posting.google.com>`

```
Hi people,

    sorry to put this message in the COBOL language group, but found
no more suitable group to put my query.


We are trying to create a DDL for a sample report in the Custom
Statement Formatter. We have defined a maintenence card member that
contains record name and file name and it's description.

When we try to print ( using option 'P' ) the maintenence card to the
DDL, the JCL abends with a U4038 code. I searched many things around ,
but ended up with nothing in hand.

Could someone please help me out with the error ?
Or could someone please post the exact procedure to work on the CSF
utility ?


Thanks a lot,

Shyam.

could it be something related to the "sortflds=       " statement in
the CSF maintenence card ?
```

#### ↳ Re: U4038 JCL Abend in custom Statement Formatter

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2002-02-27T04:25:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20020226232546.21294.00000520@mb-ml.aol.com>`
- **References:** `<c02fd744.0202260929.582e965f@posting.google.com>`

```
>From: nivas_shyam@indiatimes.com  (shyam nivas)
>Date: 2/26/02 12:29 PM Eastern Standard Time

>, the JCL abends with a U4038 code. 

Ugly things ain't it.  I assume you're running OS/390 or z/OS?  There should be
a comment (sysout?) telling you which file is hosing - but - the length of the
record in the FD is not the same as the DCB LRECL (if memory serves - Y2K and
LE installation nightmares :D).

There is a great site for mainframe help - www.mvshelp.com - where you can
search for answers to questions such as this.  There is also a listserv for
mainframe but I don't have the subscription e-mail addres here at home, the
archives have postings on this error.

Eileen
```

#### ↳ Re: U4038 JCL Abend in custom Statement Formatter

- **From:** Harry Carter <hpcarter@attbi.com>
- **Date:** 2002-03-01T15:02:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jk5v7u85javk6t660verlblj01l6u95ssr@4ax.com>`
- **References:** `<c02fd744.0202260929.582e965f@posting.google.com>`

```
On 26 Feb 2002 09:29:13 -0800, nivas_shyam@indiatimes.com (shyam
nivas) wrote:


>We are trying to create a DDL for a sample report in the Custom
>Statement Formatter. We have defined a maintenence card member that
…[5 more quoted lines elided]…
>
I'm not a CSF jockie, but in good old-fashioned Cobol work, a 4038
frequently means a file attribute mismatch (i.e. the LRECL in the
program doesn't match the dataset or the DCB info if you're creating
it). Whenever I get this error, there is ususally a sysout message
telling you that the program expected dataset XXX to have a record
length of x but the file specified had one of Y.  Of course, this all
assumes you're running this on a mainframe which I think you are.
```

#### ↳ Re: U4038 JCL Abend in custom Statement Formatter

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-03-01T11:28:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0203011128.1dc24f00@posting.google.com>`
- **References:** `<c02fd744.0202260929.582e965f@posting.google.com>`

```
Hi Shyam,

Sounds like you got some good advice.  Perhaps you could help me. 
 
I've been trying for some time to get some information on CSF. Do you
know of a site or an address where it can be had?  Even a vendor name
would help.

Thanx, Jack.


nivas_shyam@indiatimes.com (shyam nivas) wrote in message news:<c02fd744.0202260929.582e965f@posting.google.com>...
> Hi people,
> 
…[22 more quoted lines elided]…
> the CSF maintenence card ?
```

##### ↳ ↳ Re: U4038 JCL Abend in custom Statement Formatter

- **From:** lowellhuff@hotmail.com (Lowell Huff)
- **Date:** 2002-03-03T14:52:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3b001db5.0203031452.6a8ad6f9@posting.google.com>`
- **References:** `<c02fd744.0202260929.582e965f@posting.google.com> <8a2d426e.0203011128.1dc24f00@posting.google.com>`

```
jacksleight@hotmail.com (Jack Sleight) wrote in message news:<8a2d426e.0203011128.1dc24f00@posting.google.com>...
> Hi Shyam,
> 
…[34 more quoted lines elided]…
> > the CSF maintenence card ?

CSF is Custom Statement Formatter from Metavante (formerly M&I).  
Take a look at www.metavante.com.
```

###### ↳ ↳ ↳ Re: U4038 JCL Abend in custom Statement Formatter

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-03-05T20:52:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0203052052.453c120f@posting.google.com>`
- **References:** `<c02fd744.0202260929.582e965f@posting.google.com> <8a2d426e.0203011128.1dc24f00@posting.google.com> <3b001db5.0203031452.6a8ad6f9@posting.google.com>`

```
Hi Lowell,

Thanx for taking the time to reply.

Regards, Jack.


lowellhuff@hotmail.com (Lowell Huff) wrote in message news:<3b001db5.0203031452.6a8ad6f9@posting.google.com>...
> jacksleight@hotmail.com (Jack Sleight) wrote in message news:<8a2d426e.0203011128.1dc24f00@posting.google.com>...
> > Hi Shyam,
…[38 more quoted lines elided]…
> Take a look at www.metavante.com.
```

#### ↳ Re: U4038 JCL Abend in custom Statement Formatter

- **From:** k_vasu <member@dbforums.com>
- **Date:** 2002-09-12T17:51:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1807657.1031853089@dbforums.com>`
- **References:** `<c02fd744.0202260929.582e965f@posting.google.com>`

```

Whne you rpogram runs under 16 meg line and try to get above 16 meg
line.  change your compile to data(24) and amode24) and rmode any. This
resolves your problem.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
