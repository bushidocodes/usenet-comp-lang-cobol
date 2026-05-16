[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

_12 messages · 8 participants · 1999-01_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** David M Payne <dmpayne@ibm.net>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368F615D.40A1CA40@ibm.net>`

```
I am in a bit of a dilemma.  I have written a CL/LE370 COBOL module that
allows a user to perform a search of a VSAM KSDS based on 7 different
variables four of which may or may not be ranges.  All of these
variables are optional.  Since the user may or may not enter some or all
of the variables I decided the best way to handle the search was through
a browse of the dataset.

The KSDS is currently approximately 230 tracks on a 3390.  We run CICS
4.1 MRO on an OS390 platform.  CICS apparently has a monitor installed
that assumes that any transaction processing for over a specified CPU
time is in a loop and needs to be canceled.

I have talked with our CICS tech support people who I convinced to
increase the CPU time limit from 7 to 10 CPU seconds.  They were
unwilling to increase the time-out over that.  The reason being that
they thought that the more CPU my transaction uses the less that any
other transaction has available.  I see their point from an overall
systems view.  Any batch job would do it as well, but we put no
limitations on batch jobs.  Am I right or not?  Is there some limitation
within CICS that would hold up processing other transactions just
because I am using repetitive readnext/readprev commands?

If there is, then how can I overcome this dilemma?  Will a call to an
assembler routine performing a STIMER work?  Can I simply break the
readnext/readprev with a send after a predetermined record count?

If there isn't then how can I convince our tech support that my
transactions activities have no effect on the processing of other
transactions over what a normal batch job does?

Thanks in advance for the help.
```

#### ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<76om9e$sbh@sjx-ixn3.ix.netcom.com>`
- **References:** `<368F615D.40A1CA40@ibm.net>`

```
Obvious question,
  Is your program conversational or pseudo-conversational?

The whole reason that people use pseudo-conversational is so that any single
transaction (program) *NOT* "hog" CICS resources (causing other transactions
to wait for them).  Therefore, if your application really needs to lock
everyone else out for more than 10 cpu seconds, then I think you do have a
design flaw. From what I read, it sounds like you are reading thru the
entire KSDS dataset for EVERY transaction.  This certainly can't be the best
design.

"Prettiest" solution (from what you describe) would be to switch from a KSDS
dataset to a DB2 database.  (However, as this seems unlikely for any single
application) I suggest looking at alternate keys, creating partial datasets
or several other application design changes.  (Possibly each "request" could
queue an async program to do the search and then gain control once the
results come back - this is "relatively" easy in CICS - as I recall.
Although I haven't really looked at this type of thing for years.)


David M Payne wrote in message <368F615D.40A1CA40@ibm.net>...
>I am in a bit of a dilemma.  I have written a CL/LE370 COBOL module that
>allows a user to perform a search of a VSAM KSDS based on 7 different
…[29 more quoted lines elided]…
>
```

##### ↳ ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** David M Payne <dmpayne@ibm.net>
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36911279.B27B41EE@ibm.net>`
- **References:** `<368F615D.40A1CA40@ibm.net> <76om9e$sbh@sjx-ixn3.ix.netcom.com>`

```
The program is pseudo-conversational.

We do not have DB2.

I thought about using Alternate indexes but discounted it due to the overhead
when records are updated.  Since the KSDS is not updated online and used only
for history of previous transactions,  your response gave me an idea.  Instead
of alternate indexes, create alternate KSDS's with keys on each of the selection
criteria.  Since there is an update and aging process that runs nightly on the
dataset I could sort the AMS backup on each key to refresh each copy with the
current data using a REPRO REUSE.  Kind of nasty though.  It would also be a
disk hog, All of that duplicate data on disk.

After thinking about it a little I think I like the idea of a call to an asynch
module.  How should I get the retrieved data back to my issuing program?  Should
I use a TD queue?  Due to the amount of information any request can create I
would think that I could eat up CICS storage.  I guess I could create a screens
worth at a time and call the asynch module again when the user issues a
PF7/PF8.  What do you think?

William M. Klein wrote:

> Obvious question,
>   Is your program conversational or pseudo-conversational?
…[49 more quoted lines elided]…
> ?
```

###### ↳ ↳ ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36917fbb.101269371@news1.ibm.net>`
- **References:** `<368F615D.40A1CA40@ibm.net> <76om9e$sbh@sjx-ixn3.ix.netcom.com> <36911279.B27B41EE@ibm.net>`

```
On Mon, 04 Jan 1999 19:11:54 +0000, David M Payne <dmpayne@ibm.net>
wrote:


>After thinking about it a little I think I like the idea of a call to an asynch
>module.  How should I get the retrieved data back to my issuing program?  Should
…[3 more quoted lines elided]…
>PF7/PF8.  What do you think?

There's a good plan.  A screen at a time might not require the extra
time.
```

#### ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1999-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990103212336.23737.00002190@ngol04.aol.com>`
- **References:** `<368F615D.40A1CA40@ibm.net>`

```

In article <368F615D.40A1CA40@ibm.net>, David M Payne <dmpayne@ibm.net> writes:

>If there is, then how can I overcome this dilemma?  Will a call to an
>assembler routine performing a STIMER work?  Can I simply break the
>readnext/readprev with a send after a predetermined record count?

It is a pain when people try to have CICS programs do what should have been
batch applications. Reading many records from large files penalize _all_ users
of that CICS. (99% of the time when I am asked why CICS is so slow, it turns
out it is one of those applications our programmers wrote that read thousands
of records without doing a DELAY to give other transactions an opportunity to
run.)

In our shop where we have some programs that read 57,000 records, 
every 50 to 100 records (the exact number may differ based on the application,
etc.) we do an EXEC CICS DELAY with a delay time of 1 second. This will give
other transactions a chance to run.

We have several applications that use alternate indixes. If one can construct
the base record so that an alternate index could be constructed, one could have
VSAM automatically maintain the alternate index without changes to other
programs that update that file. (VSAM rules: the alternate index, just like the
base index, must be a contiguous set of bytes, starting at a specific distance
into a record, and the key displacement + key length cannot exceed the shortest
record on the file.) In some cases, we used alternate indexes without altering
the base cluster record, but in one application, we have three alternate
indexes and some fields are repeated several times in the record just so we
could have an index that covers what we need.

In another application, we tried an alternate index, but found it taking too
long to build (yes, even in batch--90 minutes just to build the index), so we
ended up writing our own "poor man's index" and modified the programs that
update or reorganize the base file to also update the "poor man's index". This
has allowed the transaction that had 20-minute run-times to be rewritten to use
the "poor man's index" and runs in 1 to 2 seconds. It was so successful that we
did the same for another application.

A better solution would be to use an SQL engine (such as DB2) and build keys
that would work well for the queries one anticipates using. Alas, that
typically means that all applications going after that data would have to be
changed to use SQL statements, which might not be so handy if there are lots of
programs alreay written to access the data using VSAM calls.

Mark A. Young
```

#### ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** "Steve Richards" <steve_spamno@aducredit.com>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgrirnqhperqvgpbz.f53ti52.pminews@news.harvard.net>`
- **References:** `<368F615D.40A1CA40@ibm.net>`

```
On Sun, 03 Jan 1999 12:23:57 +0000, David M Payne wrote:

:>I am in a bit of a dilemma.  I have written a CL/LE370 COBOL module that
:>allows a user to perform a search of a VSAM KSDS based on 7 different
:>variables four of which may or may not be ranges.  All of these
:>variables are optional.  Since the user may or may not enter some or all
:>of the variables I decided the best way to handle the search was through
:>a browse of the dataset.
:>
:>The KSDS is currently approximately 230 tracks on a 3390.  We run CICS
:>4.1 MRO on an OS390 platform.  CICS apparently has a monitor installed
:>that assumes that any transaction processing for over a specified CPU
:>time is in a loop and needs to be canceled.
:>
:>I have talked with our CICS tech support people who I convinced to
:>increase the CPU time limit from 7 to 10 CPU seconds.  They were
:>unwilling to increase the time-out over that.  The reason being that
:>they thought that the more CPU my transaction uses the less that any
:>other transaction has available.  I see their point from an overall
:>systems view.  Any batch job would do it as well, but we put no
:>limitations on batch jobs.  Am I right or not?  Is there some limitation
:>within CICS that would hold up processing other transactions just
:>because I am using repetitive readnext/readprev commands?
:>
:>If there is, then how can I overcome this dilemma?  Will a call to an
:>assembler routine performing a STIMER work?  Can I simply break the
:>readnext/readprev with a send after a predetermined record count?
:>
:>If there isn't then how can I convince our tech support that my
:>transactions activities have no effect on the processing of other
:>transactions over what a normal batch job does?
:>
:>Thanks in advance for the help.
:>
I've read through the other replies that were posted before my posting of
this.
It seems that the opinions differ on what is actually happening. Here is my
understanding of what CICS does.

Each call to a CICS API causes the transaction to lose control. In other
words
each time you do a READ all the other transactions in the region get a chance
to 
get CPU time.  You do not need a "DELAY" nor a "SUSPEND". Neither
is going to solve your particular problem.

Your program will not give up control if you are looping in COBOL code
without doing some sort of EXEC CICS call.

If your program is in a loop you can prevent runaway task abends by inserting
an EXEC CICS SUSPEND in the code loop.

So, it appears to me your getting blown out by just using to much CPU time.
If you don't need to process data in all of the records then an additional
index,
either VSAM alternate or just a file that points to the records you need is a

good solution. If you need to look at every record then indeed you have a
problem.

As has been indicated in the other posts, 7 to 10 CPU seconds is quite a bit
of
processing time for the amount of data you have. You didn't say what model
the CPU was, nor the size or number of records,  so it's hard to gleen
exactly
what may be reasonable for CPU time.

You may be able to tweak the program with some performance analysis,
particularly if you have tables with loops, or many arithmetic calculations. 
 

                               or

You could tell the tech support people you are willing to trade some
transaction priority if they give you more CPU time...
```

##### ↳ ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** mark0young@aol.com (Mark0Young)
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990106195633.25439.00002801@ngol06.aol.com>`
- **References:** `<fgrirnqhperqvgpbz.f53ti52.pminews@news.harvard.net>`

```

In article <fgrirnqhperqvgpbz.f53ti52.pminews@news.harvard.net>, "Steve
Richards" <steve_spamno@aducredit.com> writes:

>Each call to a CICS API causes the transaction to lose control. In other
>words
>each time you do a READ all the other transactions in the region get a chance
>to 
>get CPU time.

This has been discussed on the CICS-L mailing list. A lot of commands,
including EXEC CICS READ DATASET..., do NOT necessarily reset the time the
transaction has been running and thus could still timeout even though it does
only a very small amount of processing _per record_. I know this is the case
(the time for purposes of detecting runaway loops is _not_ reset for forward
browses) with CICS/VSE 2.2 and CICS/VSE 2.3.

Mark A. Young
```

##### ↳ ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36967595.2465154@news3.ibm.net>`
- **References:** `<368F615D.40A1CA40@ibm.net> <fgrirnqhperqvgpbz.f53ti52.pminews@news.harvard.net>`

```
On Tue, 05 Jan 1999 15:42:05 -0500 (EST), "Steve Richards" <steve_spamno@aducredit.com>
wrote:

>
>Each call to a CICS API causes the transaction to lose control. In other
>words
Not entirely try.  The rules are :

If an EXEC CICS COMMAND includes a WAIT, then the issuing task get's suspended and other
tasks get a chance to access the CPU.

Working-Storage Section
01  Status-Flag  PIC X VALUE 'N".
      88 Hell-Freezes-Over  VALUE 'Y'.

Procedure Division
	PERFORM UNTIL Hell-Freezes-Over
		EXEC CICS SUSPEND END-EXEC
             END-PERFORM

This will run forever, as the EXEC CICS SUSPEND command ALWAYS includes a WAIT, (and
nothing else)

	PERFORM UNTIL Hell-Freezes-Over
		EXEC CICS ASKTIME END-EXEC
             END-PERFORM

This will give an abend AICA (or the task might be purged by some governor function), as
the ASKTIME never incurres a WAIT and the task timer therefore never gets reset
              EXEC CICS STARTBR ................
	PERFORM UNTIL Hell-Freezes-Over
		EXEC CICS READNEXT .........END-EXEC
             END-PERFORM

This may or may not abend AICA, depending on various possibilities.

a)  VSAM sub tasking is NOT active (CICS Version 2), or it is CICS Version 3 or up
	a1)  If the record is already in the buffer, then there is no WAIT
	a2)  If the record is NOT in the buffer, there will be a WAIT
b) If VSAM sub tasking IS active (CICS Version 2), there will be a WAIT


	PERFORM UNTIL Hell-Freezes-Over
		EXEC CICS SEND FROM ....... END-EXEC
             END-PERFORM

This is a weird one.   The first SEND issued does not contain a WAIT, but the second (and
all subsequent) SEND commands will have a WAIT included


with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** "Steve Richards" <steve_spamno@aducredit.com>
- **Date:** 1999-01-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fgrirnqhperqvgpbz.f575ii0.pminews@news.harvard.net>`
- **References:** `<368F615D.40A1CA40@ibm.net> <fgrirnqhperqvgpbz.f53ti52.pminews@news.harvard.net> <36967595.2465154@news3.ibm.net>`

```
On Thu, 07 Jan 1999 09:08:31 GMT, Volker Bandke wrote:

:>On Tue, 05 Jan 1999 15:42:05 -0500 (EST), "Steve Richards" <steve_spamno@aducredit.com>
:>wrote:
:>
:>>
:>>Each call to a CICS API causes the transaction to lose control. In other
:>>words
:>Not entirely try.  The rules are :
:>
:>If an EXEC CICS COMMAND includes a WAIT, then the issuing task get's suspended and other
:>tasks get a chance to access the CPU.
:>
:>Working-Storage Section
:>01  Status-Flag  PIC X VALUE 'N".
:>      88 Hell-Freezes-Over  VALUE 'Y'.
:>
:>Procedure Division
:>	PERFORM UNTIL Hell-Freezes-Over
:>		EXEC CICS SUSPEND END-EXEC
:>             END-PERFORM
:>
:>This will run forever, as the EXEC CICS SUSPEND command ALWAYS includes a WAIT, (and
:>nothing else)
:>
:>	PERFORM UNTIL Hell-Freezes-Over
:>		EXEC CICS ASKTIME END-EXEC
:>             END-PERFORM
:>
:>This will give an abend AICA (or the task might be purged by some governor function), as
:>the ASKTIME never incurres a WAIT and the task timer therefore never gets reset
:>              EXEC CICS STARTBR ................
:>	PERFORM UNTIL Hell-Freezes-Over
:>		EXEC CICS READNEXT .........END-EXEC
:>             END-PERFORM
:>
:>This may or may not abend AICA, depending on various possibilities.
:>
:>a)  VSAM sub tasking is NOT active (CICS Version 2), or it is CICS Version 3 or up
:>	a1)  If the record is already in the buffer, then there is no WAIT
:>	a2)  If the record is NOT in the buffer, there will be a WAIT
:>b) If VSAM sub tasking IS active (CICS Version 2), there will be a WAIT
:>
:>
:>	PERFORM UNTIL Hell-Freezes-Over
:>		EXEC CICS SEND FROM ....... END-EXEC
:>             END-PERFORM
:>
:>This is a weird one.   The first SEND issued does not contain a WAIT, but the second (and
:>all subsequent) SEND commands will have a WAIT included
:>
:>
:>with kind regards
:>
:>Volker Bandke
:>(BSP GmbH)


Based on both your response and Mark's can we clear up the issues?

I think  we all agree that some EXEC CICS commands will not reset the timer
for the AICA abend.

I'm now not clear on giving up the CPU. I thought that every EXEC CICS
command
causes the progam to give up the CPU regardless of whether is gets suspended
or not.
This then can cause task control to reschedule other transactions. Is this
true or not?
Or does is vary by the implementation of CICS?

Finally, Mark  mentions the CICS LIST    [ CICS List <CICS-L@UGA.CC.UGA.EDU>]

This is a good source of CICS discussion. Although sometimes there is a lot
of traffic that
could be taken offline.

Thanks!
```

###### ↳ ↳ ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

_(reply depth: 4)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1999-01-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990108133612.01015.00000472@ng-cb1.aol.com>`
- **References:** `<fgrirnqhperqvgpbz.f575ii0.pminews@news.harvard.net>`

```
You have received numerous useful comments already, but let me add this since I
haven't seen mention of this aspect in the interaction so far.

You appear to be misapplying the access method technology entirely.  You do not
seem to understand buffers, and their impact on CPU time.  You should go back
to the drawing board for a while.  All of that is meant as mild but direct
constructive criticism. With genuine positive and supportive intentions, I will
say to you, if you have a performance problem with I/O and have not mentioned
buffers, really, you are not understanding access methods.

Learn about buffers, don't just skim past it in the manual.

With a KSDS your computer, no matter how many layers of confusing components
you build on top, can only use two DATA buffers. At that point you is dead in
the water should you enter this yatch in a performance competition.

Reading KSDSes as flat files is a non sequitor. Reading KSDSes as flat files
online is double dumb.

From what you have said you probably should load this file as an ESDS for the
online 'scans' you are doing.  Buffering could then assist you.
A thrashing system is doing more than making the disk drive rock like an
unbalanced washer in spin mode.  A thrasher can actually peg the CPU needle,
especially when the driving READs are mediated by an crosss task integrity
purveyor like CICS.

As a minor aside, you may also want to check that CICS does not allocate the
file with update enabled (you describe a read-only application, but no one has
mentioned that it will make a difference in CICS CPU utilization if the UPD bit
is on, even if all you do is browse and read).
But that is not your main problem.  

You need buffers, DATA buffers, as opposed to INDEX buffers, for sequential
processing.

Also note that it is possible to build AIXes on top of ESDSes! This can allow
the CICS region to get to the file as ESDS, get DATA buffers, and provide a mix
of sequential and keyed access by means of the sophistication of VSAM.

With the variety of accesses you describe, you may benefit from multiple
solutions, some continued sequential access (but against an ESDS) and some
keyed via an AIX or against a keyed copy of the file.

Your file does not sound that large to me (but that is a company resource
issue, not a concensus issue).  Duplicating a file for improved access is
definitely a reasonable solution, especially for non dynamic data (such as your
read only 'historical' data).

Best Wishes, and enjoy your reading in the VSAM manuals, buffering makes one
very large difference.  The VSAM technical manuals are worth their weight in
gold in saved CPU resources.



Robert Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

_(reply depth: 5)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-01-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<369817f3.1341338@news3.ibm.net>`
- **References:** `<fgrirnqhperqvgpbz.f575ii0.pminews@news.harvard.net> <19990108133612.01015.00000472@ng-cb1.aol.com>`

```
On 8 Jan 1999 18:36:12 GMT, rkrayhawk@aol.com (RKRayhawk) wrote:

>
>Learn about buffers, don't just skim past it in the manual.
>
The application is running under CICS, there is nothing the application programmer can
directly do about buffering

>With a KSDS your computer, no matter how many layers of confusing components
>you build on top, can only use two DATA buffers. At that point you is dead in
>the water should you enter this yatch in a performance competition.
>
Pardon me?  Possibly I am misunderstanding something here. I have been using hundreds,
even several thousands of buffers in a CICS (LSR) environment, and it performs like a snap
- achieving 98%+ buffer hit rates on reads

>Reading KSDSes as flat files is a non sequitor. Reading KSDSes as flat files
>online is double dumb.
>
Sometimes it isn't.  Sometimes, like in a browsing type application, this is exactly what
you want, bypassing a lot of index I/O s that way

>
>You need buffers, DATA buffers, as opposed to INDEX buffers, for sequential
>processing.

Also, for sequential processing, make those DATA buffers BIIIIIG


>

with kind regards

Volker Bandke
(BSP GmbH)
```

#### ↳ Re: AKC3/ATNI Abends on Command Level Cobol using STARTBR/READNEXT on VSAM KSDS

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1999-01-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3691B7AB.F0B64571@att.net>`
- **References:** `<368F615D.40A1CA40@ibm.net>`

```
David M Payne wrote:
> 
> I am in a bit of a dilemma.  I have written a CL/LE370 COBOL module that
…[9 more quoted lines elided]…
> time is in a loop and needs to be canceled.

We have the same option turned on in Omegamon and get called by the
performance people from time to time, always about the same transaction.
What puzzles me is how you can take so long to read 230 *tracks*. That's
nothing - maybe you should pull the thing into memory. I have no direct
experience, yet, with CICS data tables; but this might be a good place
to use one. If you can't get sufficient feedback here, why don't you try
"bit.listserv.cics-l"? (that's CICS-L)

> I have talked with our CICS tech support people who I convinced to
> increase the CPU time limit from 7 to 10 CPU seconds.  They were
…[4 more quoted lines elided]…
> limitations on batch jobs.  Am I right or not?

This varies by installation; but, in general, no, batch jobs don't have
unlimited CPU time. Most MVS shops (those I've seen anyway) have a set
of job classes for test jobs, which are serviced by certain initiators.
In general, the job class with the highest priority will be limited to
the least CPU. E.g., we have classes D, M, C, & T. D has the highest
priority, but is limited to 1 second of CPU. This is great for quick
jobs, including assemblies; but don't try to compile a big COBOL program
or REPRO a big file. M is next, with a lower priority but with more CPU.
Then C, which we use for our COBOL compiles (I think class C can use up
to 15 CPU seconds). Class T is last, lowest priority; but can run
forever.

Bill Lynch

PS: Do you have any performance stats or other doc?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
