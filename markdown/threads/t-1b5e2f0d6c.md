[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do you keep a VSAM file healthy?

_7 messages · 7 participants · 1999-11_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### How do you keep a VSAM file healthy?

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81kv7n01i13@enews2.newsguy.com>`

```
I support/enhance an old MVS/COBOL II system that runs almost completely 
using VSAM datasets (there's a little bit of IDMS).  The system creates,
maintains, and reports on the host side of a POS system for a large grocery
store chain.  Many of the files we use are cleared out after the schedules
run but are not deleted and redefined.  Programs just open the file as
output and this clears them.  Looking at these datasets, I can see many of
them have been around since 1992 and several of them are extended out a
little too far for my tastes.  I'm wondering what kind of effect this has on
the speed of a VSAM dataset.  Is there something I should do, maybe do an
IDCAMS model to create a new dataset and repro to it?  Is there some other
IDCAMS utility to 'reorg' the dataset?  As an aside, these VSAM files would
kick IDMSs butt in any speed contest, any day of the week.  But I'm like Tim
Allen and if I can make it better with little effort, I want to know how.

Jeff
```

#### ↳ Re: How do you keep a VSAM file healthy?

- **From:** Gilbert Saint-flour <gsf@ibm.net>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383e9d1a$1$tfs$mr2ice@news>`
- **References:** `<81kv7n01i13@enews2.newsguy.com>`

```
In <81kv7n01i13@enews2.newsguy.com>, on 25 Nov 1999 at 22:36, "Jeff
Baynard" 

>........  Many of the files we use are cleared out after the 
>schedules run but are not deleted and redefined.  Programs just open the
…[5 more quoted lines elided]…
>it?  Is there some other IDCAMS utility to 'reorg' the dataset?

From what I understand, these files are reusable (defined with REUSE) and
you OPEN them for OUTPUT with the RESET option to clear them; this would
make the files permanent but the data in them temporary.  If that's the
case, you shouldn't be concerned with CI/CA splits, as I believe this only
occurs with data sets with permanent data in them, so forget about REORGs
and IDCAMS.

If these files have too many extents, you can consolidate them using the
COPY command of DFDSS (ADRDSSU) or a similar utility, although, depending
on the type of DASD you're using, this may not buy you much.

Another thing I'd recommend to optimize VSAM clusters: if the files have
been defined with IBMED and/or REPLICATE (which only wastes space on
cached DASD), re-DEFINE them with NOIMBED and NOREPLICATE.  You may want
to revisit the CI sizes also; bumping the CISZ of the Index from 512 bytes
to 4096 (or more) sometimes does a lot of good (you'd have to test it).

There is a simple trick you can use to speed up VSAM access without having
to even touch the file: it's called BLSR (Batch Local Shared Resources)
and works like a cache to reduce the amount of I/O performed against a
KSDS or AIX.  I've seen jobs recently go from 4 hours down to 15 minutes
just by modifying the JCL to use BLSR.  The catch is that, although BLSR
is a standard component of any MVS/ESA or OS/390 system, your sysprog has
to set it up in SYS1.PARMLIB(IEFSSNxx) before you can use it.  To check if
you can use BLSR, just modify any job that processes a KSDS, as shown in
the example below:

Without BLSR:

 //VSAMJOB EXEC PGM=VSAMPROG
 //KSDSDD   DD DSN=IBMUSER.AUDECHS.CLUSTER,DISP=SHR 

With BLSR:

 //VSAMJOB EXEC PGM=VSAMPROG
 //KSDSDD   DD SUBSYS=(BLSR,'DDNAME=KSDSDD2')
 //KSDSDD2  DD DSN=IBMUSER.AUDECHS.CLUSTER,DISP=SHR 

If your job fails with the following message:

 IEFC746I SUBSYSTEM BLSR DOES NOT EXIST 

then you have to ask tech support to modify SYS1.PARMLIB(IEFSSNxx) to add:

 SUBSYS SUBNAME(BLSR) INITRTN(CSRBISUB)  

BLSR can make you the king of the hill - try it today.

 Gilbert StFlour
 http://members.home/net/gsf/ 

PS: BLSR works 90% of the time.  If your program abends because it
receives unexpected VSAM status codes, try another one.
```

#### ↳ Re: How do you keep a VSAM file healthy?

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383E251A.28612E8B@att.net>`
- **References:** `<81kv7n01i13@enews2.newsguy.com>`

```
Jeff Baynard wrote:
> 
> I support/enhance an old MVS/COBOL II system that runs almost completely
…[13 more quoted lines elided]…
> Jeff

In my experience, VSAM reorgs consist of:

1. REPRO the file to a flat file (or run a purge program will delete (&
archive) old data)

2. DELETE/DEFINE the cluster

3. REPRO the data from the first step into the new cluster

You're done! As far as performance is concerned, do a LISTCAT and look
for CI & CA splits - especially CA splits.

Bill Lynch
```

##### ↳ ↳ Re: How do you keep a VSAM file healthy?

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1999-11-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383CDC60.4A0ED50D@worldnet.att.net>`
- **References:** `<81kv7n01i13@enews2.newsguy.com> <383E251A.28612E8B@att.net>`

```
William Lynch wrote:
> 
> Jeff Baynard wrote:
…[29 more quoted lines elided]…
> Bill Lynch

Many years ago I worked in a VM and VSE shop, and this was the standard
practice.  Most VSAM files in those systems were delete/defined every
day.  This has the advantage of potentially removing secondary
allocations automatically, if you have files that are subject to large
variations in the number of records day to day.

Now I work with large CICS systems that run 24x7, and we have mirrored
files.  During most of the day activity accumulates on the "A" files and
batch refresh jobs read the ESDS transaction log and apply updates to
the inactive "B" files.  During nightly maintenance the files are
switched.  We purge many of our "A" files while "B" files are active. 
Ten years ago we could not delete/define a VSAM file if it was allocated
to a running CICS region.  Now we can, but we still don't.  Our VSAM
files are defined with the REUSE option.  When we're ready to reload
them, we just issue and IDCAMS "REPRO" command with the REUSE option.  I
understand this completely rebuilds indexes as if the file had never
been previously loaded, but it won't remove secondary allocations.

I'm not sure, but I believe that if you use the REUSE option, or
possibly SHAREOPTIONS(3 3), that the maximum number of secondary
allocations you can get goes down from 123 to 16.  If this is true, or
is still a VSAM limitation, it would become more important to choose
good sizes for your primary and secondary allocations.

About 15 years ago I had a class in VSAM tuning.  There's a lot of
tricks, but basically it's a compromise between access speed, storage
utilization, and disk space utilization.  VSAM will generally keep
working even if your files aren't tuned very well, but you'll either be
slowing down your access speed or wasting memory or disk.

We used to worry a lot about CA splits in VSAM files in CICS.  It could
really slow down your access.  Generally, you want both your primary and
secondary allocation to be at least one cylinder.  At least that's a
general rule that seems to work fairly well.

There were some really odd problems that could occur.  A large data CA
size with a very small index CI size and looooong keys could create
files with record slots that you could never fill.

Normally you tune VSAM files differently depending upon whether they are
primarily used by batch applications or CICS, although memory is not as
big a limitation as it once was.  Tuning your freespace percentages can
have a big impact, depending upon the typical pattern of insert activity
you need to support.  But if your freespace percentages are high, you
will be preallocating lots of disk space you may not need.

It's always a tradeoff.
```

##### ↳ ↳ Re: How do you keep a VSAM file healthy?

- **From:** "Mike Fleischer" <softwaresolver@home.com>
- **Date:** 1999-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1mZ%3.146$59.52801@news1.rdc2.tx.home.com>`
- **References:** `<81kv7n01i13@enews2.newsguy.com> <383E251A.28612E8B@att.net>`

```

William Lynch <WBLynch@att.net> wrote in message
news:383E251A.28612E8B@att.net...
> Jeff Baynard wrote:
> >
> > I support/enhance an old MVS/COBOL II system that runs almost completely
> > using VSAM datasets (there's a little bit of IDMS).  The system creates,
> > maintains, and reports on the host side of a POS system for a large
grocery
> > store chain.  Many of the files we use are cleared out after the
schedules
> > run but are not deleted and redefined.  Programs just open the file as
> > output and this clears them.  Looking at these datasets, I can see many
of
> > them have been around since 1992 and several of them are extended out a
> > little too far for my tastes.  I'm wondering what kind of effect this
has on
> > the speed of a VSAM dataset.  Is there something I should do, maybe do
an
> > IDCAMS model to create a new dataset and repro to it?  Is there some
other
> > IDCAMS utility to 'reorg' the dataset?  As an aside, these VSAM files
would
> > kick IDMSs butt in any speed contest, any day of the week.  But I'm like
Tim
> > Allen and if I can make it better with little effort, I want to know
how.
> >
> > Jeff
…[13 more quoted lines elided]…
> Bill Lynch

One more trick you may want to consider..
1) Do a VSAM ALTER to another dataset vs repro to a flat file (no I\O to
read through the file)
2) Then do the define of the orig. cluster
3) repro from altered dsn to original dsn
4) delete altered files.

One extra step but less reads through the file.

Mike
```

#### ↳ Re: How do you keep a VSAM file healthy?

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383e2515.2389175@news2.attglobal.net>`
- **References:** `<81kv7n01i13@enews2.newsguy.com>`

```
On Thu, 25 Nov 1999 22:36:31 -0500, "Jeff Baynard" <union27@macconnect.com> wrote:

>I support/enhance an old MVS/COBOL II system that runs almost completely 
>using VSAM datasets (there's a little bit of IDMS).  The system creates,
…[12 more quoted lines elided]…
>Jeff

The usual way to "reorg" a VSAM dataset is with a four-step IDCAMS approach

	REPRO INDATASET(my.vsam.cluster) OUTFILE(SEQDD)
	DELETE my.vsam.cluster PURGE CLUSTER	
	DEFINE CLUSTER NAME(my.vsam.cluster) ......
	REPRO INFILE(SEQDD) OUTDATASET(my.vsam.cluster)
and, in a separte Step (or Job, just to play it safe)
	DELETE sequential.copy PURGE NONVSAM


     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         As a computer, I find your faith in technology amusing.
```

#### ↳ Re: How do you keep a VSAM file healthy?

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<383E265F.2A925A4D@acm.org>`
- **References:** `<81kv7n01i13@enews2.newsguy.com>`

```


Jeff Baynard wrote:
> 
> I support/enhance an old MVS/COBOL II system that runs almost completely
…[11 more quoted lines elided]…
> Allen and if I can make it better with little effort, I want to know how.

Assuming you are talking about VSAM KSDS files, having a number of
extents is not as bad as having a large number of CI and CA splits;
although widely separated extents will degrade performance some,
especially if the file is not behind a cached controller or gets a poor
percentage of cache hits.  To reset a VSAM KSDS back to ground zero
without a delete and redefine, the file has to be defined with REUSE
attribute and it has to be opened with RESET (? not sure about the COBOL
equivalent) option, not just for output.  If this is being done on a
regular basis, then the file is in effect being reorganized at that
point.  The main issue may be a need to redefine the file with a large
enough primary allocation to eliminate extra extents.  

There is no special utility just for reorganizing a KSDS.  REPROing a
VSAM KSDS dataset to new KSDS dataset will give a reorganized version of
the original dataset (with a new name).  Another common technique is to
REPRO the KSDS dataset to a sequential file, verify generation of the
flat file was good, delete and redefine the KSDS, REPRO the sequential
file back to the KSDS, and redefine any AIX or PATHs and rebuild any
AIX's.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
