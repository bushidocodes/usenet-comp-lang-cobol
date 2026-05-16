[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# INDEXED FILES AND SORT

_11 messages · 6 participants · 1998-12 → 1999-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### INDEXED FILES AND SORT

- **From:** "Max" <barx@iol.it>
- **Date:** 1998-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76fq80$i21$1@hermes.iol.it>`

```
My cobol doesn't work...

If I want order a sequential file with the sort task.
When I Run the program, it says me "run-time error".

If I want create a indexed file, it says me File status error 95.
I before run ISAM.exe.

Why?

Thanks and happy new year.

Answers in E-mail.

Max
```

#### ↳ Re: INDEXED FILES AND SORT

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<flYj2.1996$hE2.12747831@storm.twcol.com>`
- **References:** `<76fq80$i21$1@hermes.iol.it>`

```
>If I want order a sequential file with the sort task.
>When I Run the program, it says me "run-time error".
>
>If I want create a indexed file, it says me File status error 95.
>I before run ISAM.exe.


Not sure what OS you are working under, but on MYV the only way I have ever
put data into an indexed file is by using the REPRO program. Sorting the
data is not required, because the REPRO utility inserts the records into the
INDEXED file according to how the key is defined.

Also on MYS the only command I have used to create an indexed file was by
using a DEFINE statement from within IDCAMS. When defining in this manner
there is always a DELETE before the define to make sure nothing exists
beforehand. Your error sounds like you may have the definition parameters
wrong. Verify them with what is in a mnaual, or try modifying a currently
working definition to fit what you want.
```

##### ↳ ↳ Re: INDEXED FILES AND SORT

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bzYj2.2000$hE2.12754831@storm.twcol.com>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com>`

```
>Not sure what OS you are working under, but on MYV the only way I have ever


Not sure what OS you are working under, but on MVS the only way I have ever
...............................................^^^.........................
sorry for the typo.
```

##### ↳ ↳ Re: INDEXED FILES AND SORT

- **From:** "COBOL Frog (Huib Klink)" <H.Klink@IMN.nl>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369086D0.265976F0@IMN.nl>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com>`

```
Jeff wrote:

> Not sure what OS you are working under, but on MYV

Whats that, MYV?

> the only way I have ever
> put data into an indexed file is by using the REPRO program. Sorting the
> data is not required, because the REPRO utility inserts the records into the
> INDEXED file according to how the key is defined.

Try this with thousands or more records. The speed gained by using sorted input
is enormous.

> Also on MYS

Whats that, MYS?

> the only command I have used to create an indexed file was by
> using a DEFINE statement from within IDCAMS. When defining in this manner
…[3 more quoted lines elided]…
> working definition to fit what you want.

That V is in the bottom row of letters on your keyboard: zxcVbnm. :) You menat
MVS?

The Frog
```

###### ↳ ↳ ↳ Re: INDEXED FILES AND SORT

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Y1xk2.2174$hE2.13959416@storm.twcol.com>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com> <369086D0.265976F0@IMN.nl>`

```
Yes I meant MVS.

>Try this with thousands or more records. The speed gained by using sorted
input
>is enormous.


I regularly use this method on thousands and sometimes millions of records.
But the data is always from some type of backup which would already be
sorted. Sometimes I use SyncSort or DFSort to sort and load a file, but
never VSAM, but supposedly it works. Using Syncsort or DFSort would
definitely be recommended since they do funny things to optimize thier IO
beyond what would normally be accomplished from a normal, say COBOL,
program.
```

###### ↳ ↳ ↳ Re: INDEXED FILES AND SORT

_(reply depth: 4)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36929e54.174649099@news1.ibm.net>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com> <369086D0.265976F0@IMN.nl> <Y1xk2.2174$hE2.13959416@storm.twcol.com>`

```
On Tue, 5 Jan 1999 18:14:51 -0500, "Jeff" <a@a.com> wrote:

>Yes I meant MVS.
>
…[11 more quoted lines elided]…
>program.

This is a common misconception.  For COBOL program sorts DF or
SYNCSORT is often used ANYWAY.  (fastsrt compiler option).  Removing
the sort from the program OFTEN (not always) does NOTHING to improve
performance.
```

###### ↳ ↳ ↳ Re: INDEXED FILES AND SORT

_(reply depth: 4)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1999-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36937610.C8DD2AF9@home.com>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com> <369086D0.265976F0@IMN.nl> <Y1xk2.2174$hE2.13959416@storm.twcol.com>`

```
Jeff wrote:
> 
> Yes I meant MVS.
…[11 more quoted lines elided]…
> program.

The main reason to use a second step to create a flat file then REPRO it
to a KSDS file is to allow REPRO to make it more efficient.  I love
SyncSort's speed and power.  When I have it available I often merge one
file with conditions to create an extract.

I knew of a shop which had no sort utilities.  They sorted by copying to
an ISAM file and back again!

Also - I once converted a Univac 9030 shop to IBM.  (This computer was
the successor to the RCA - but after Univac laid off the design
engineers IBM hired them to build the 360, so these are similar
machines).  To keep our functionality, I made virtually every file
VSAM.  We had relative, flat, and indexed files (mostly relative). 
Anymore, just about everybody uses VSAM == IBM's ISAM, apparently ESDS &
RRDS files aren't used hardly at all anymore.  I guess most permanent
data are stored in databases.
```

###### ↳ ↳ ↳ Re: INDEXED FILES AND SORT

_(reply depth: 5)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-YP4S4vLHvxsr@Dwight_Miller.iix.com>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com> <369086D0.265976F0@IMN.nl> <Y1xk2.2174$hE2.13959416@storm.twcol.com> <36937610.C8DD2AF9@home.com>`

```
On Wed, 6 Jan 1999 14:41:20, Howard Brazee <NOSPAMbrazee@home.com> 
wrote:

 
> Also - I once converted a Univac 9030 shop to IBM.  (This computer was
> the successor to the RCA - but after Univac laid off the design
…[5 more quoted lines elided]…
> data are stored in databases.

We use some ESDS but where I might have "used" to have chosen to use 
ESDS I just use a QSAM file now.  (But I changed OS's too).
```

###### ↳ ↳ ↳ Re: INDEXED FILES AND SORT

_(reply depth: 5)_

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990106195631.25439.00002800@ngol06.aol.com>`
- **References:** `<36937610.C8DD2AF9@home.com>`

```

All our VSAM reorgs are done with SORT (was CA-SORT; now it is IBM's DFSORT)
with the MERGE FIELDS=COPY to copy out to tape (or flat file), and SORT again
with MERGE FIELDS=COPY after the DEL/DEF to repopulate the cluster.

For VSAM KSDS clusters being rebuilt from scratch (e.g., we have a couple "poor
man's alternate index" files), we use SORT (OUTFIL KSDS,TOL,REUSE) and the
SORTOUT is the freshly-defined cluster.

Mark A. Young
```

##### ↳ ↳ Re: INDEXED FILES AND SORT

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36917aa6.99967737@news1.ibm.net>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com>`

```
On Mon, 4 Jan 1999 00:29:33 -0500, "Jeff" <a@a.com> wrote:

>>If I want order a sequential file with the sort task.
>>When I Run the program, it says me "run-time error".
…[8 more quoted lines elided]…
>INDEXED file according to how the key is defined.

Just FYI - repro works much better if the data *is* sorted - it's much
faster.

Second - you don't HAVE to use REPRO to populate a VSAM file.  Once
defined, you can populate it with any program.
```

###### ↳ ↳ ↳ Re: INDEXED FILES AND SORT

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<y4xk2.2176$hE2.13961486@storm.twcol.com>`
- **References:** `<76fq80$i21$1@hermes.iol.it> <flYj2.1996$hE2.12747831@storm.twcol.com> <36917aa6.99967737@news1.ibm.net>`

```
>Second - you don't HAVE to use REPRO to populate a VSAM file.  Once
I always do have sorted input, geuss I'm just lucky that way.

>defined, you can populate it with any program.


I try not to write programs which are already designed and ready to use for
the same purpose.
Such as REPRO, IEBGENER, DFSort, or better yet SyncSort.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
