[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# WRITING TO A FILE on Mainframe

_18 messages · 10 participants · 1999-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### WRITING TO A FILE on Mainframe

- **From:** "Darius Cooper" <Darius_cooper@Bigfoot.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<g2R03.38$_c.164@news.megsinet.net>`

```
When writing to a file (Mainframe batch) I understand that there is no
guarantee of the data actually being written unless the file is closed. Am I
correct?

In C, there is a flush() function that acts a little like a COMMIT. On
COBOL, I don't think there is anything similar. Is this true?

My file is simply a sequential output file. So, my program can keep closing
the file and opening it again in EXTEND. The file may be going to DASD or to
TAPE/CART. Should I be using the "NO REWIND" option?

Is there anything I can specify in the JCL that will force a write-through
of each record? If so, will this me a bigger performance hit than closing
and reopening the file?

I'm sure this is a familiar situation to many folks here. I'd appreciate any
advice as to the best way to handle this.

Thanks,

- Darius Cooper
```

#### ↳ Re: WRITING TO A FILE on Mainframe

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<7i0tb5$p4t$1@nnrp1.deja.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net>`

```
In article <g2R03.38$_c.164@news.megsinet.net>,
  "Darius Cooper" <Darius_cooper@Bigfoot.com> wrote:
> When writing to a file (Mainframe batch) I understand that there is no
> guarantee of the data actually being written unless the file is
closed. Am I
> correct?
>
…[3 more quoted lines elided]…
> My file is simply a sequential output file. So, my program can keep
closing
> the file and opening it again in EXTEND. The file may be going to DASD
or to
> TAPE/CART. Should I be using the "NO REWIND" option?
>
> Is there anything I can specify in the JCL that will force a
write-through
> of each record? If so, will this me a bigger performance hit than
closing
> and reopening the file?
>
> I'm sure this is a familiar situation to many folks here. I'd
appreciate any
> advice as to the best way to handle this.
>
…[4 more quoted lines elided]…
>

Hi Darius,

First of all, fflush() doesn't work on the mainframe as it would work in
a UNIX system. AFIK it worked with C/370, but not with the current
OS/390 compilers.

But now, the good news: You have not to care about physical writing on
the mainframe. The operationg system does it for you. Even in case of an
ABEND, the Language Environment closes all files for you. Only if you
set TRAP(OFF) or NOSTAE,NOSPIE, the last record might be lost.
If this parameter is set, the only solution I know is to set the BLKSIZE
of the file equal to the LRECL, but this is a HEAVY performance problem,
before all if you write to a tape.

And forget about rewind and open extend. Just open - write - close and
leave the rest to the OS. That's what everybody does.

Daniel
------------------------------------------------------------------------
visit us at http://www.winterthur.com


--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

#### ↳ Re: WRITING TO A FILE on Mainframe

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<37440863.AD82BD0F@zip.com.au>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net>`

```
Darius Cooper wrote:
> 
> In C, there is a flush() function that acts a little like a COMMIT. On
> COBOL, I don't think there is anything similar. Is this true?
> 

There is no need for flush in MVS because you are not using pipes
nor terminals.  In cobol the only reason that you might have
problems is that if you do not close the file an additional junk
record is written.

Ken
```

#### ↳ Re: WRITING TO A FILE on Mainframe

- **From:** MKS <m_k_s@hotmail.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<37440351.3AC7FE0F@hotmail.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net>`

```
Darius Cooper wrote:
> 
> When writing to a file (Mainframe batch) I understand that there is no
> guarantee of the data actually being written unless the file is closed. Am I
> correct?

I don't know what you are talking about.  I think you might be
confused.  A COBOL program writes to the output file when it executes
the write.  There is no "commit".  You might be thinking of the JCL that
might be used to run the job.  You can specify the disposition of the
dataset.  If you choose new,keep,keep - it will allocate a dataset and
keep it if the job ends normally or if it abends.  If you choose
old,delete,delete - it will grab the dataset (no one else can use it)
and delete the file when the job ends (normally or abends).  There are
other dispositions as well, mod and pass.  This is the closest thing I
can think of that you might be referring to.  

> In C, there is a flush() function that acts a little like a COMMIT. On
> COBOL, I don't think there is anything similar. Is this true?

There is a commit when you write to a database - DB2 for example.  I do
not think that there is a commit for a file in COBOL.

> My file is simply a sequential output file. So, my program can keep closing
> the file and opening it again in EXTEND. The file may be going to DASD or to
> TAPE/CART. Should I be using the "NO REWIND" option?

Why would you open and close the file multiple times in the same
program?
 
> Is there anything I can specify in the JCL that will force a write-through
> of each record? If so, will this me a bigger performance hit than closing
> and reopening the file?

It might be easier if you explain what you are trying to do first (big
picture).  I think you might want to specify mod,keep,keep.  This will
use an old dataset if the DSN exists.  It will create a new one if it
doesn't exist.  It will append data to the end of the file.  It will
keep the result whether or not the job abends or not.
 
> I'm sure this is a familiar situation to many folks here. I'd appreciate any
> advice as to the best way to handle this.

Matt
```

##### ↳ ↳ Re: WRITING TO A FILE on Mainframe

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<37441905.40E8EAF8@NOSPAMhome.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com>`

```
MKS wrote:
> 
> Darius Cooper wrote:
…[14 more quoted lines elided]…
> can think of that you might be referring to.

But on mainframes, records are saved up until a block is ready to be
written.  Sometimes, when I want to see the progress of a running
program, I will write a page full of displays - to make sure there were
enough data to do an actual write to the output queue.  I don't know
what happens when the system goes down while writing a flat file - I
always start over in this case.  With databases, the appropriate tools
to commit our updates are available.  When we write to a file using
random access, I imagine the write is immediate.
```

###### ↳ ↳ ↳ Re: WRITING TO A FILE on Mainframe

- **From:** MKS <m_k_s@hotmail.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<37442197.70C9A499@hotmail.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com> <37441905.40E8EAF8@NOSPAMhome.com>`

```
Howard,

If you change the disp of your output file to (,keep,keep) you will be
able to see the last record written regardless of whether or not it
abends.  However, if you are in the process of debugging your program,
it might be just as easy to write to the sysout with displays.  

I'm not certain about when the physical write actually takes place (re:
waiting until a block is sufficiently full), but I think it would write
out what is there in the case the program prematurely ends.  If you have
your disposition set appropriately you will be able to see your output. 
If you have a disposition of delete on an abend - the file will not be
out there.

Again, explain what you are trying to do.  

MKS
```

###### ↳ ↳ ↳ Re: WRITING TO A FILE on Mainframe

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<3744521B.70ADC79B@NOSPAMhome.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com> <37441905.40E8EAF8@NOSPAMhome.com> <37442197.70C9A499@hotmail.com>`

```
MKS wrote:
> 
> Howard,
…[13 more quoted lines elided]…
> Again, explain what you are trying to do.

I was trying to add to a discussion.

I have noticed that when I have a program which does an initial display
to SYSOUT=*, I don't see that displayed line.  If I display a bunch of
lines, I do see them.  This indicates to me that, at least of SYSOUT=*,
that nothing is actually written until a block has been filled up, or
until some other event happens to tell the hardware to do the write. 
The COBOL program can force this write by doing a close.  It has been my
impression that if you examine a file saved by (old,keep,keep) after an
abort - you may, or may not find the last record which the COBOL program
thinks it wrote. 

I am guessing that the OS might write the buffer when it closes down the
file after the abort, but obviously a power failure would eliminate this
possibility.  At any rate, I prefer to not trust this to be true.
```

###### ↳ ↳ ↳ Re: WRITING TO A FILE on Mainframe

_(reply depth: 5)_

- **From:** MKS <m_k_s@hotmail.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<374474F6.2CAD98CB@hotmail.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com> <37441905.40E8EAF8@NOSPAMhome.com> <37442197.70C9A499@hotmail.com> <3744521B.70ADC79B@NOSPAMhome.com>`

```
Howard,

> > Again, explain what you are trying to do.
> 
> I was trying to add to a discussion.

My apologies, I thought you were the original poster.  I did not mean to
be abrupt or rude.  I was trying to get clarification from the original
poster.  
 
> I have noticed that when I have a program which does an initial display
> to SYSOUT=*, I don't see that displayed line.  If I display a bunch of
…[6 more quoted lines elided]…
> thinks it wrote.

SYSOUT=* does not mean anything in itself.  The asterisk tells the job
to use whatever has been specified by the job or system beforehand. 
Usually it seems to mean to write to the output queue.  When you say
that you are not "seeing" the output, where are you looking.  Your job
settings might be displaying the output to the screen or to a queue.  I
haven't been in the business very long, but I have yet to see a physical
processing error, i.e. if the computer is told to write somewhere - it
definitely does write to where it has been told.  There might be a
failure rate, but I think that it would be less than 0.00001%.  As to
the last record being missing from a file after an abend, this depends
on whether or not the last record was successful.  If the program abends
and the last processed record was #101 and the last record you see on
the output file is #100, it is probably because #101 failed (for
whatever reason).  If you check the logic carefully and pinpoint exactly
where the abend happened, you will probably find that the operating
system did what it was supposed to.
 
> I am guessing that the OS might write the buffer when it closes down the
> file after the abort, but obviously a power failure would eliminate this
> possibility.  At any rate, I prefer to not trust this to be true.

Again, in my experience, the computer rarely does not do what it is told
to do.  I have encountered a few problems, but it is very very rare.

Matt
```

###### ↳ ↳ ↳ Re: WRITING TO A FILE on Mainframe

_(reply depth: 6)_

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<3745C3D0.D262560@att.net>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com> <37441905.40E8EAF8@NOSPAMhome.com> <37442197.70C9A499@hotmail.com> <3744521B.70ADC79B@NOSPAMhome.com> <374474F6.2CAD98CB@hotmail.com>`

```
MKS wrote:
> 
(snipped)

> SYSOUT=* does not mean anything in itself.  The asterisk tells the job
> to use whatever has been specified by the job or system beforehand.

It means to use the class from the MSGCLASS parameter in the JOB card.

> Usually it seems to mean to write to the output queue. When you say
> that you are not "seeing" the output, where are you looking.

He's looking in SDSF. This is a common occurance and I believe Howard's
explanation is correct, meaning SDSF doesn't display partial blocks
while the file is open (the partial block in this case is the block
whose buffer is being filled as I'm displaying the SYSOUT for the job).

I'm curious as to what you mean by "output queue"?

Bill Lynch
```

###### ↳ ↳ ↳ Re: WRITING TO A FILE on Mainframe

_(reply depth: 7)_

- **From:** MKS <m_k_s@hotmail.com>
- **Date:** 1999-05-24T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<374958A3.7EB8283F@hotmail.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com> <37441905.40E8EAF8@NOSPAMhome.com> <37442197.70C9A499@hotmail.com> <3744521B.70ADC79B@NOSPAMhome.com> <374474F6.2CAD98CB@hotmail.com> <3745C3D0.D262560@att.net>`

```
Bill,

I'm not sure if "output queue" is the correct diction here, but I use it
refer to the listings created from running a job.  I work in shop that
uses IOF and not SDSF, but even in the SDSF shop I think I might have
heard it referred to as the output queue.  (Please correct me if it is
wrong to refer to it this way - I am trying to learn too).

Thanks,

Matt
```

###### ↳ ↳ ↳ Re: WRITING TO A FILE on Mainframe

_(reply depth: 6)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-05-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374554B5.6E869149@zip.com.au>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com> <37441905.40E8EAF8@NOSPAMhome.com> <37442197.70C9A499@hotmail.com> <3744521B.70ADC79B@NOSPAMhome.com> <374474F6.2CAD98CB@hotmail.com>`

```
Basically SYSOUT is still DASD somewhere on the system.  Some of
the sysout readers (SDSF and others) are not especially good at
getting the data from active jobs out of these areas.  I think
that some MVS systems are not set flush the output as often as
they can, for performance reasons.

You might want to check out the buffering options in SYSOUT if you
really need instant access.  The sequential files are
automatically set to buffers=2 so sysout may have something very
similar.
```

##### ↳ ↳ Re: WRITING TO A FILE on Mainframe

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<37441C1D.82403AFF@NOSPAMhome.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <37440351.3AC7FE0F@hotmail.com>`

```
> Why would you open and close the file multiple times in the same
> program?

Good question.  Let's come up with some reasons:

Open input, process data, close, open extend, add record, close.

Open access is sequential.  Close, open access is random.

I have seen OPEN output write a header, close then open extend - but I'm
drawing a blank at the moment as to why this was done.

Any other ideas?
```

#### ↳ Re: WRITING TO A FILE on Mainframe

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** bit.listserv.ibm-main,comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-LgVl2RBDgw0G@Dwight_Miller.iix.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net>`

```
Darius, 

I never worry about it.  I have NEVER had a problem with data not 
being written. 
What is the clock duration of your job?  If it's not DAYS you probably
don't need to worry.  If it is DAYS, then you might need to get into 
some checkpoint processing.  There's no need to worrry about forcing 
the write before the close.

On Thu, 20 May 1999 10:02:55, "Darius Cooper" 
<Darius_cooper@Bigfoot.com> wrote:

> When writing to a file (Mainframe batch) I understand that there is no
> guarantee of the data actually being written unless the file is closed. Am I
…[21 more quoted lines elided]…
> 

-------------------------
Trust the computer industry to shorten "Year 2000" to Y2K.  It was 
this
kind of thinking that caused the problem in the first place.

Visit my updated website at
http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: WRITING TO A FILE on Mainframe

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<7i1bil$ptp@dfw-ixnews9.ix.netcom.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net>`

```
I have read several replies to this original question - some of which are
absolutely correct and others less so; some of which seem to understand
COBOL on MVS (OS/390) more than others.

  NOTE: This thread is talking ONLY about "sequential" files, i.e. QSAM.  I
think the issues for VSAM are similar - but not identical.

In truth and fact, IF (and only if) an OS/390 COBOL program is writing
output to a "blocked" file (I don't think that buffering matters - but I
could be wrong on this), then there is a POTENTIAL problem between any
"logical" WRITE with a "successful" I/O status and the "physical" write of
that block (whether it is at a CLOSE or simply a filled block).  Therefore,
if performance is *NOT* a consideration, then you can use UNBLOCKED files
(DCB=F/V rather than DCB=FB/VB) to "guarantee" that your COBOL program will
obtain the "correct" I/O status code after every WRITE.  (You could also use
blocked records - with the LRECL = BLKSIZE as suggested in other notes, but
I don't see what that would get you - other than more wasted space for the
block descriptor word.)  ON THE OTHER HAND, even this would only let you
know that you have a "problem" when the I/O error occurred - it would not
guarantee that all previous records were "safe" (which is what I think that
the desire for "commit" capability was asking for).  For example, if you did
3 WRITEs that "worked" (to an unblocked file) and then a 4th WRITE got an
error, the chances are that the entire file would be "messed up".  One part
of the thread talked about closing the file after each write and then
opening it up either via the COBOL "OPEN EXTEND" or the JCL "DISP=MOD" - but
here again, if the file has a problem on the next OPEN or WRITE, my guess
(assumption? certainty?) would be that the file would all be messed up
anyway - so all previous WRITEs wouldn't be "saved" by this technique
either.

As someone who "trusts" the OS/390 (MVS) file systems, it is hard for me to
imagine designing a system where I was "guaranteed" that all previous WRITE
statements were "saved" - no matter what happened with my next WRITE.  I
guess you would have to close the file after every write, then copy a
back-up file to a 2nd back-up file, then copy the new file to the 1st backup
file and THEN re-open your active file (or some "obscure" variation of
this).  It would seem to me that looking at the OS/390 and/or COBOL "rerun"
facility would be much more appropriate than this (but I suppose there MIGHT
be some application design requirement that might necessitate such a
"secure" WRITE facility).

The bottom-line (IMHO) is:
   A) The chance of a WRITE in COBOL (for a blocked file) being
uccessful  - but the physical write of the block failing are slim - but not
0%. (If the physical write is what fails, then the COBOL I/O status code
would only show a bad value on that last I/O statement.)
   B) Using unblocked files would let you know with each and every WRITE
statement whether it has succeeded (in a physical WRITE) - but the
performance implications are pretty horrendous.
   C) Nothing other than a rather "tortured" application design is going to
give you GUARANTEED "safe" records after a COBOL WRITE - until you are
finished using that file (and even then - the next OPEN of it as INPUT could
"destroy" it somehow).
```

##### ↳ ↳ Re: WRITING TO A FILE on Mainframe

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<3744878C.D6899A97@acm.org>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <7i1bil$ptp@dfw-ixnews9.ix.netcom.com>`

```


"William M. Klein" wrote:
> 
> I have read several replies to this original question - some of which are
…[13 more quoted lines elided]…
> obtain the "correct" I/O status code after every WRITE.  (You could also use
...
> The bottom-line (IMHO) is:
>    A) The chance of a WRITE in COBOL (for a blocked file) being
…[12 more quoted lines elided]…
> Bill Klein
...
> > When writing to a file (Mainframe batch) I understand that there is no
> > guarantee of the data actually being written unless the file is closed. Am
> > I correct?
...

For QSAM output, a write request is made to the operating system
whenever (1) a full-block is contained in a buffer, or (2) the file is
closed, and there is a partial block remaining to be written.  Except at
CLOSE, the write requests proceed asynchronously and the program is only
forced to wait for a successful completion if all buffers are
exhausted.  So, in a situation where the program is able to generate
records much faster than the I/O subsystem can write, the total number
of buffers allocated (QSAM default is 5) could in a worst-case scenario
represent the number of blocks that might be in-flight and subject to
loss in the event of catastrophic failure.  Having said that, such
catastophic failures in the MVS world are very rare - unless you have
power instabilities and are running without a UPS. 

There are a few scenarios short of system failure in which the automatic
CLOSE (either because of program ABEND or because the program simply
fails to CLOSE a dataset) can fail, but all the ones of which I am aware
are the result of application "bugs".  The automatic CLOSE requires that
file control blocks and buffers be intact, so obviously if the program
runs amok in some way that trashes or releases storage containing the
required information, you couldn't expect an auto-CLOSE to preserve
in-flight records.  This is also the only way I can conceive that you
might end up with garbage records in the file, as opposed to just losing
records.

There are environments in MVS where the problem of in-flight records is
explicitly addressed:  VSAM updates under CICS using journaling support
and SYNC points, and DB2 with COMMIT processing.  Both of these use
non-QSAM I/O techniques to insure that there is a point when log records
are "known" to have been successfully written or committed to the
hardware I/O subsystem.  This is a serious issue in online environments,
where re-creation of the user interactions supplying data to the
application can be very difficult.  It really shouldn't be an issue in a
batch application.  There are many reasons why a step in a batch job may
fail: unanticipated input (perhaps a user error), inadequate file sizes
(the user may have doubled the amount of data from the time of
application design), tape drive failure, operator finger-check, etc. 
One of the cardinal rules of batch job design is that there should be
restart capabilty designed into the job stream to handle a failure in
any job step. Files essential to job restart that are changed or
destroyed by the job stream should either have a backup or be
recoverable by some other means.  Then there is no need to treat restart
from a rare system failure any differently than restart from the much
less rare application job-step failure, where the contents of all
datasets with update activity is suspect.
```

##### ↳ ↳ Re: WRITING TO A FILE on Mainframe

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<7i2c8p$oeg$1@news.igs.net>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <7i1bil$ptp@dfw-ixnews9.ix.netcom.com>`

```

William M. Klein wrote in message <7i1bil$ptp@dfw-ixnews9.ix.netcom.com>...

<with regard to file commit snippage>

Bill, I know nothing about IBM mainframe, but if I am following your
explanation, how can you accomplish something like transaction
processing or record level lockout?  Of course why one would want
to on a line sequential file is quite another question.

Some sort of "commit" statement is going to be almost required
to share files well, unless everthing is queued to a server.
```

###### ↳ ↳ ↳ Re: WRITING TO A FILE on Mainframe

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7i2nfj$dup@dfw-ixnews5.ix.netcom.com>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <7i1bil$ptp@dfw-ixnews9.ix.netcom.com> <7i2c8p$oeg$1@news.igs.net>`

```
Donald (not CC'ing the IBM-MAIN list where this is "understood")

First, the original question explicitly asked about "batch" processing.  By
and large, "QSAM" (which is "record sequential" in PC-ish terms - there is
no "line sequential" as such) is NEVER used in "transaction processing"
environments.  (That is a gross over-simplification - but does somewhat
answer your question.)

"Long ago and far away" - when ANSI/ISO were FIRST starting to think about
what to put in the next Standard (then hoped for about 1996 or 1997!), it
was explicitly decided NOT to add "commit" and "rollback" syntax/semantics
to standard COBOL.  Interestingly enough, they are now even backing away
from requiring record-locking/file-sharing in "new" compliant compilers.
(The IBM DISP=SHR/OLD facility EXPLICITLY provides file-level sharing and
*not* record-level lockouts as mentioned in Donald's question.)

In a "traditional" MVS (OS/390) environment, there are other software
products (IMS, CICS, DB2, - etc) which do the "transaction" processing and
COBOL "sequential" files are either explicitly prohibited (e.g. CICS) or
cause strong application design restrictions (e.g. IMS/BMPs).  (IBMers - I
don't think that we need to get into VSAM ESDS files - which are neither
"fish nor fowl nor good red-meat" when it comes to COBOL sequential file
processing.)

ON THE OTHER HAND (as indicated elsewhere in this thread), the actual risk
of "losing data" because of block (or buffer) WRITE failures are minimal.
IBM also provides (from "ye goode olde tape days") significant "re-run"
features which is how the old non-transaction applications usually handled
such risks.
```

##### ↳ ↳ Re: WRITING TO A FILE on Mainframe

- **From:** "Darius Cooper" <Darius_cooper@Bigfoot.com>
- **Date:** 1999-05-20T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.ibm-main
- **Message-ID:** `<rXZ03.8$UA.221@news.megsinet.net>`
- **References:** `<g2R03.38$_c.164@news.megsinet.net> <7i1bil$ptp@dfw-ixnews9.ix.netcom.com>`

```
Thank you to all for the replies; very useful.

In a nutshell, it seems I can truct the mainframe. My application runs on
AIX and on the mainframe, and has some stuff that isn't relevant for one
platform or the other. This CLOSE/OPEN loop seems to be one such thing.

Thanks again,

- Darius

PS: Now all I need is for an AIX guru to tell me that I don't need this on
AIX either :)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
