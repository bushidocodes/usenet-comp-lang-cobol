[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# blocksize efficiency in os/390

_8 messages · 6 participants · 1999-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### blocksize efficiency in os/390

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7niul5$1sb2@enews4.newsguy.com>`

```
Job running out of space... 500 lrecl * 400,000 records.  When I code 
blocksize=0, I have to code space=(0,(45000,4500),rlse) and it almost blows
up.  What's going on?  According to our Roscoe calculator, that dataset
shouldn't take more than about 11,000 blocks with a blksize of 18888.

Why is this?  Should I not code blksize=0?

Jeff
```

#### ↳ Re: blocksize efficiency in os/390

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nj3j2$nng@dfw-ixnews15.ix.netcom.com>`
- **References:** `<7niul5$1sb2@enews4.newsguy.com>`

```
Jeff Baynard <union27@macconnect.com> wrote in message
news:7niul5$1sb2@enews4.newsguy.com...
> Job running out of space... 500 lrecl * 400,000 records.  When I code
> blocksize=0, I have to code space=(0,(45000,4500),rlse) and it almost
blows
> up.  What's going on?  According to our Roscoe calculator, that dataset
> shouldn't take more than about 11,000 blocks with a blksize of 18888.
…[3 more quoted lines elided]…
> Jeff

Do you really mean that you have coded
   BLKSIZE=0
in your JCL - or do you mean you have coded
   BLOCK CONTAINS 0
in your COBOL program.  There is a big difference between the two.

Personally, I have never used (or SEEN) BLKSIZE=0 in JCL.   Is this supposed
to mean something special?

If what you have coded is really "BLOCK CONTAINS" in your COBOL program,
then you should NOT be using that "0" as the first parameter in your space=
statement (JCL).  Actually, I can't remember any GOOD reason for ever
allocating space in blocks - rather than tracks or cylinders - but your
application may have one.
```

##### ↳ ↳ Re: blocksize efficiency in os/390

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379d3cf1.261443577@news1.ibm.net>`
- **References:** `<7niul5$1sb2@enews4.newsguy.com> <7nj3j2$nng@dfw-ixnews15.ix.netcom.com>`

```
On Mon, 26 Jul 1999 20:57:57 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:


>Do you really mean that you have coded
>   BLKSIZE=0
…[3 more quoted lines elided]…
>

He should do both.

>Personally, I have never used (or SEEN) BLKSIZE=0 in JCL.   Is this supposed
>to mean something special?

Yep.  With our little OS/390 box I have found that if you let QSAM do
what it wants it does an efficient job - let it choose the most
efficient blocksize for the device.  I have also found the same to be
true of VSAM - leave off the CI SIZE - and that just reminded me, I
was supposed to rebuild a LARGE file at 8:00 - I'm late!


>
>If what you have coded is really "BLOCK CONTAINS" in your COBOL program,
…[9 more quoted lines elided]…
>
```

##### ↳ ↳ Re: blocksize efficiency in os/390

- **From:** John Trifon <jtrifon@ix.netcom.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379D8D30.E44072E@ix.netcom.com>`
- **References:** `<7niul5$1sb2@enews4.newsguy.com> <7nj3j2$nng@dfw-ixnews15.ix.netcom.com>`

```
BLKSIZE=0 (or omitting the BLKSIZE parameter) allows the system to determine the
optimal block size (optimal space usage) depending on the storage medium.. A
3380 will have a blocksize of roughly 23K, a 3390 28K, and cartridge 32K. This
is dependent on the program also having coded BLOCK 0.  When a data set is
opened, the DCB is filled first from the program, next the JCL, and finally the
data set itself. If the COBOL program had not coded BLOCK 0, it will default to
BLOCK 1. Not very efficient. One big advantage is that the JCL/program
blocksizes becomes device independent. Moving from  one device type to another
does not mean recalculating blocksizes. There are certain requirements for a new
dataset  to allow the system to determine the BLKSIZE:
(quoting IBM)
Block size is not available or specified from any source. BLKSIZE=0 can be
specified.
You specify LRECL or it is in the data class.
You specify RECFM or it is in the data class. It must be fixed or variable.
 You specify DSORG as PS or PO or you omit DSORG and it is PS or PO in the data
class.

"William M. Klein" wrote:

> Jeff Baynard <union27@macconnect.com> wrote in message
> news:7niul5$1sb2@enews4.newsguy.com...
…[27 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com
```

###### ↳ ↳ ↳ Re: blocksize efficiency in os/390

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nlur1$ksi@enews3.newsguy.com>`
- **References:** `<7niul5$1sb2@enews4.newsguy.com> <7nj3j2$nng@dfw-ixnews15.ix.netcom.com> <379D8D30.E44072E@ix.netcom.com>`

```
Well, that answers it.  I was only coding recording mode is f.  That 
explains why blksize=0 in the jcl wasn't working.  I'll try it tomorrow.

Still a rookie,
Jeff

----------
In article <379D8D30.E44072E@ix.netcom.com>, John Trifon
<jtrifon@ix.netcom.com> wrote:


> BLKSIZE=0 (or omitting the BLKSIZE parameter) allows the system to determine
the
> optimal block size (optimal space usage) depending on the storage medium.. A
> 3380 will have a blocksize of roughly 23K, a 3390 28K, and cartridge 32K. This
> is dependent on the program also having coded BLOCK 0.  When a data set is
> opened, the DCB is filled first from the program, next the JCL, and finally
the
> data set itself. If the COBOL program had not coded BLOCK 0, it will default
to
> BLOCK 1. Not very efficient. One big advantage is that the JCL/program
> blocksizes becomes device independent. Moving from  one device type to another
> does not mean recalculating blocksizes. There are certain requirements for a
new
> dataset  to allow the system to determine the BLKSIZE:
> (quoting IBM)
…[4 more quoted lines elided]…
>  You specify DSORG as PS or PO or you omit DSORG and it is PS or PO in the
data
> class.
>
…[32 more quoted lines elided]…
>
```

#### ↳ Re: blocksize efficiency in os/390

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379d3cbb.261388882@news1.ibm.net>`
- **References:** `<7niul5$1sb2@enews4.newsguy.com>`

```
On Mon, 26 Jul 1999 20:32:55 -0400, "Jeff Baynard"
<union27@macconnect.com> wrote:

>Job running out of space... 500 lrecl * 400,000 records.  When I code 
>blocksize=0, I have to code space=(0,(45000,4500),rlse) and it almost blows
…[5 more quoted lines elided]…
>Jeff

I always use blksize=0, but I allocate only in cylinders and tracks.
Tried records a few times, was not impressed.
```

#### ↳ Re: blocksize efficiency in os/390

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379d806f.1459138@news2.ibm.net>`
- **References:** `<7niul5$1sb2@enews4.newsguy.com>`

```
On Mon, 26 Jul 1999 20:32:55 -0400, "Jeff Baynard" <union27@macconnect.com> wrote:

>Job running out of space... 500 lrecl * 400,000 records.  When I code 
>blocksize=0, I have to code space=(0,(45000,4500),rlse) and it almost blows
…[5 more quoted lines elided]…
>Jeff

A Blksize of 18888?  With a record length of 500?  Weird.....


If your program does not include BLOCK CONTAINS 0, then the blocksize from the DCB in your
program will be used when creating the file.  Code a zero block size in the JCL AND in the
program.

If your shop uses SMS, you can specify the record length and number of records, instead of
the block size, and use the AVGREC as a counter multiplier, like this

//MYFILE DD DISP=(,CATLG,DELETE),DSN=WHATEVER,
//                              SPACE=(500,(400,10),RLSE),AVGREC=K,LRECL=500,RECFM=FB


with kind regards

Volker Bandke
(BSP GmbH)
```

#### ↳ Re: blocksize efficiency in os/390

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379D8A6D.AA73CE58@nbnet.nb.ca>`
- **References:** `<7niul5$1sb2@enews4.newsguy.com>`

```
You code BLOCK {CONTAINS} 0 (RECORDS) in the program and either omit the
BLKSIZE paramater in JCL or code BLKSIZE=0.  The space parameter depends
on whether SMS is active. If it is, code space in terms of AVGREC with
an LRECL of 500 or megabytes (20 meg).  Otherwise code space either in
cylinders or as (20000,(10000,1000),rlse) (or rlse,,round).  Check your
JCL manual or JCL reference.  

Jeff Baynard wrote:
> 
> Job running out of space... 500 lrecl * 400,000 records.  When I code
…[6 more quoted lines elided]…
> Jeff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
