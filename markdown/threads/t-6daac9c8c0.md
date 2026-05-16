[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Splitting output file

_27 messages · 15 participants · 2000-06 → 2000-07_

---

### Splitting output file

- **From:** petert@my-deja.com
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jhl55$q24$1@nnrp1.deja.com>`

```
Hi all
I have a mainframe cobol program writing an output file that is over 8Gb
in size.
I want to split the output and produce say 4 files.  Can anyone think of
a way to write say 10000 records to one file then the next 10000 to the
second file and so on until finished?
Or should I sort the output in a second step to create the four files?
Any help would be appreciated
Thanks
Peter


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Splitting output file

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000630103332.01242.00000521@nso-cd.aol.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com>`

```
In article <8jhl55$q24$1@nnrp1.deja.com>, petert@my-deja.com writes:

>I want to split the output and produce say 4 files.  Can anyone think of
>a way to write say 10000 records to one file then the next 10000 to the
>second file and so on until finished?
>Or should I sort the output in a second step to create the four files?
>

It all depends on the needs of the following processes.
What is going to use the output files from this program?
is there any requirement for order?
I would first consider keeping a bytes-written counter to force
splitting the files on a specific byte-count boundary, keeping the
original order of the file intact.  If the original order is inconsequential,
then I would pass the output thru a sort job that would SPLIT the file
into a predetermined set of files containing an equal number of records
regardless of overall file size.

There would seem to be a need for more details regarding the Environment
this is to operate in (I assume that the target is a PC [2G file size] and 
the origin is a Mainframe [8G file]).  The purpose/use of the resulting 
SPLIT output files.  ....
```

#### ↳ Re: Splitting output file

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395D14B6.29D7@NOSPAMguysoftware.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com>`

```
petert@my-deja.com wrote:
> 
> Hi all
…[6 more quoted lines elided]…
> Any help would be appreciated

If you do it in a second step, at least you'll know how much data you are dealing with 
because you can count it on the first step.
```

##### ↳ ↳ Re: Splitting output file

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395D1593.E9803C68@cusys.edu>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <395D14B6.29D7@NOSPAMguysoftware.com>`

```


Ed Guy wrote:
> 
> petert@my-deja.com wrote:
…[11 more quoted lines elided]…
> because you can count it on the first step.

So what do you do, write out a record with the record count and read it
in with a second cobol program?
```

###### ↳ ↳ ↳ Re: Splitting output file

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395D5F75.1C91@NOSPAMguysoftware.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <395D14B6.29D7@NOSPAMguysoftware.com> <395D1593.E9803C68@cusys.edu>`

```
Howard Brazee wrote:
> 
> Ed Guy wrote:
…[16 more quoted lines elided]…
> in with a second cobol program?

Actually, I used C++, but the principal is the same.  I wrote out every record to an 
intermediate file and counted them as I was doing it.  Then I closed the file, opened it 
and did reads of the intermediates and writes to a permanent file.  When you have 
written enough records for a reasonable distribution between files, you close the output 
file and start a new one with the next record from the intermediate file.
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 4)_

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eApzZ534$GA.358@cpmsnbbsa07>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <395D14B6.29D7@NOSPAMguysoftware.com> <395D1593.E9803C68@cusys.edu> <395D5F75.1C91@NOSPAMguysoftware.com>`

```
Why not get the file header block data and then calculate the number of
record based on record length block size, %blocks used etc and calculate
number records(close estimate) in file if running on same platform?   I
understand you can read the file header block data using REXX.  I would like
to have a copy of code to do that if possible.

"Ed Guy" <ed_guy@NOSPAMguysoftware.com> wrote in message
news:395D5F75.1C91@NOSPAMguysoftware.com...
> Howard Brazee wrote:
> >
…[5 more quoted lines elided]…
> > > > I have a mainframe cobol program writing an output file that is over
8Gb
> > > > in size.
> > > > I want to split the output and produce say 4 files.  Can anyone
think of
> > > > a way to write say 10000 records to one file then the next 10000 to
the
> > > > second file and so on until finished?
> > > > Or should I sort the output in a second step to create the four
files?
> > > > Any help would be appreciated
> > >
> > > If you do it in a second step, at least you'll know how much data you
are dealing with
> > > because you can count it on the first step.
> >
…[3 more quoted lines elided]…
> Actually, I used C++, but the principal is the same.  I wrote out every
record to an
> intermediate file and counted them as I was doing it.  Then I closed the
file, opened it
> and did reads of the intermediates and writes to a permanent file.  When
you have
> written enough records for a reasonable distribution between files, you
close the output
> file and start a new one with the next record from the intermediate file.
>
…[7 more quoted lines elided]…
>  and ParseRat, the File Parser, Converter and Reorganizer"
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 5)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000702004716.01242.00000658@nso-cd.aol.com>`
- **References:** `<eApzZ534$GA.358@cpmsnbbsa07>`

```
In article <eApzZ534$GA.358@cpmsnbbsa07>, "brucepbarrett"
<brucepbarrett@email.msn.com> writes:

>Why not get the file header block data and then calculate the number of
>record based on record length block size, %blocks used etc and calculate
…[3 more quoted lines elided]…
>

I remember when working on a UNISYS environment, there were extensions 
to COBOL that allowed checking/changing the file attributes.  I have not heard
of such features available under the IBM environment.  I'd like to know/see
some code that would allow such 'information' gathering calls.
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 6)_

- **From:** "brucepbarrett" <brucepbarrett@email.msn.com>
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OnCi$xC5$GA.282@cpmsnbbsa09>`
- **References:** `<eApzZ534$GA.358@cpmsnbbsa07> <20000702004716.01242.00000658@nso-cd.aol.com>`

```
I don't know how to get it.  I know the information is there or somewhere
and should be available using REXX, Assembler, C etc.  You can see it using
TSO menu options 1.3.4 (?) therefore it should be available dynamically via
a called program by passing the PDS and member returning all data including
date last modified/created etc.  Some inovative individual has probably
already done it.


"Sff5ky" <sff5ky@aol.comxxx123> wrote in message
news:20000702004716.01242.00000658@nso-cd.aol.com...
> In article <eApzZ534$GA.358@cpmsnbbsa07>, "brucepbarrett"
> <brucepbarrett@email.msn.com> writes:
…[4 more quoted lines elided]…
> >understand you can read the file header block data using REXX.  I would
like
> >to have a copy of code to do that if possible.
> >
>
> I remember when working on a UNISYS environment, there were extensions
> to COBOL that allowed checking/changing the file attributes.  I have not
heard
> of such features available under the IBM environment.  I'd like to
know/see
> some code that would allow such 'information' gathering calls.
>
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jobnh$614$1@nntp9.atl.mindspring.net>`
- **References:** `<eApzZ534$GA.358@cpmsnbbsa07> <20000702004716.01242.00000658@nso-cd.aol.com> <OnCi$xC5$GA.282@cpmsnbbsa09>`

```
Check the COBOL FAQ for a reference to a COBOL program to get at the DCB
(among other things).
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 4)_

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000630233146.01242.00000568@nso-cd.aol.com>`
- **References:** `<395D5F75.1C91@NOSPAMguysoftware.com>`

```
In article <395D5F75.1C91@NOSPAMguysoftware.com>, Ed Guy
<ed_guy@NOSPAMguysoftware.com> writes:

>Actually, I used C++, but the principal is the same.  I wrote out every
>record to an 
…[7 more quoted lines elided]…
>

I would think that you could have your program accept a parameter that would be
either a byte-count or record-count to use for cutting each file.  Add some
code to the file closing process to report the byte/record count of each file
closed.  By looking at the numbers reported for the last file, you can get a
feel for when to 
adjust your cutoff opint higher to keep the file count to a predetermined
level.
```

###### ↳ ↳ ↳ Re: Splitting output file

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BJk75.32$fg3.16368@dfiatx1-snr1.gtei.net>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <395D14B6.29D7@NOSPAMguysoftware.com> <395D1593.E9803C68@cusys.edu>`

```
Howard Brazee <howard.brazee@cusys.edu> wrote in message
news:395D1593.E9803C68@cusys.edu...
>
>
…[5 more quoted lines elided]…
> > > I have a mainframe cobol program writing an output file that is over
8Gb
> > > in size.
> > > I want to split the output and produce say 4 files.  Can anyone think
of
> > > a way to write say 10000 records to one file then the next 10000 to
the
> > > second file and so on until finished?
> > > Or should I sort the output in a second step to create the four files?
> > > Any help would be appreciated
> >
> > If you do it in a second step, at least you'll know how much data you
are dealing with
> > because you can count it on the first step.
>
> So what do you do, write out a record with the record count and read it
> in with a second cobol program?

No need to use a second program. Just write all the output to a file, CLOSE
the file, then OPEN it again, this time for INPUT. You have your record
count, so you know how to to "fairly" divide up the output across the
multiple output files.

You can do the same thing if the "huge" file is the original input: Just
OPEN INPUT the file, read until end, counting; then CLOSE, OPEN INPUT again
and you are back at record one.

MCM
```

##### ↳ ↳ Re: Splitting output file

- **From:** hobbsb@my-deja.com
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jl57e$85e$1@nnrp1.deja.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <395D14B6.29D7@NOSPAMguysoftware.com>`

```

> > I have a mainframe cobol program writing an output file that
> > is over 8Gb in size.
…[9 more quoted lines elided]…
>

Maybe one can use a little finesse on this problem ...

Can the program that generates the 8 GB file determine how many records
*will* be generated?  If so, let it calculate how many records to write
to each file.  One can avoid creating a huge intermediate file or a last
output file with only a few records.  One could make this program work
such that it doesn't matter if the output files total 8 GB or 8 TB,
it'll create the appropriate number of properly sized files.

But ... why does the file have to broken up in the first place?  If the
next processing step aborts on files over a certain size or number of
records, I would suggest "fixing" that step.  One may not always
remember that that step will only process up to X GB files or Y number
of records - with the corresponding loss of time and scrambling around
trying to split the file.



Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Splitting output file

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com>`

```
Without using dynamic allocation (which I know can be done by I don;t know
how to do it), the only way I can think of is to use multiple SELECT..
ASSIGN statements in the program and a corresponding number of DD names in
JCL, and counting, as in..

SELECT FILE1 ASSIGN FILE1
SELECT FILE2 ASSIGN FILE2
..
SELECT FILEn ASSIGN FILEn

....

999-WRITE-OUTPUT.

  EVALUATE RECORDS-WRITTEN
   WHEN < 10000
     WRITE FILE1-RECORD
   WHEN <20000
     WRITE FILE2-RECORD
    ...
   WHEN <  (n* 10000)
     WRITE FILEn-RECORD


(Crude, but so is my brother-in law)

MCM

<petert@my-deja.com> wrote in message news:8jhl55$q24$1@nnrp1.deja.com...
> Hi all
> I have a mainframe cobol program writing an output file that is over 8Gb
…[4 more quoted lines elided]…
> Or should I sort the output in a second step to create the four files?
```

##### ↳ ↳ Re: Splitting output file

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395d4255.83531057@207.126.101.100>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net>`

```
I think you are all making this way too complicated.

Assign one file for input.
Assign a second for output, in the JCL assign it to a TAPE drive.

Read and write to the desired record count, then close the tape file
and open it again for output.  Make it non cataloged, non labeled if
necessary.  I've never had to do this, but I don't see on the face of
it why it won't work.  Never tried it though....

On Fri, 30 Jun 2000 22:44:44 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>Without using dynamic allocation (which I know can be done by I don;t know
>how to do it), the only way I can think of is to use multiple SELECT..
…[36 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Splitting output file

- **From:** William Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395D4844.9000A9B8@worldnet.att.net>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net> <395d4255.83531057@207.126.101.100>`

```
Thane Hubbell wrote:
> 
(snip)

> I think you are all making this way too complicated.
> 
…[6 more quoted lines elided]…
> it why it won't work.  Never tried it though....

If you're using tape, why not just write the file out as one entity
(tape, of course, assumes a flat file)? At the end of that step you know
all there is to know about the file you just created and you can split
it off into as many sub files as you want. 

What is it you're trying to accomplish, anyway?

Bill Lynch
```

###### ↳ ↳ ↳ Re: Splitting output file

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jjvcn$2od$1@sshuraab-i-1.production.compuserve.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net> <395d4255.83531057@207.126.101.100>`

```
    I have not dealt with mainframes in a while, but I understand
that
writing directly to a tape drive is more expensive than writing
to disk,
and then moving the file to tape with a system utility.

    Something along the lines of "Time is money", concerning
all resources.  In this case, the amount of time that the program
spends in memory doing nothing.



Thane Hubbell <thaneH@softwaresimple.com> wrote in message
news:395d4255.83531057@207.126.101.100...
> I think you are all making this way too complicated.
>
> Assign one file for input.
> Assign a second for output, in the JCL assign it to a TAPE
drive.
>
> Read and write to the desired record count, then close the tape
file
> and open it again for output.  Make it non cataloged, non
labeled if
> necessary.  I've never had to do this, but I don't see on the
face of
> it why it won't work.  Never tried it though....
>
…[3 more quoted lines elided]…
> >Without using dynamic allocation (which I know can be done by
I don;t know
> >how to do it), the only way I can think of is to use multiple
SELECT..
> >ASSIGN statements in the program and a corresponding number of
DD names in
> >JCL, and counting, as in..
> >
…[23 more quoted lines elided]…
> ><petert@my-deja.com> wrote in message
news:8jhl55$q24$1@nnrp1.deja.com...
> >> Hi all
> >> I have a mainframe cobol program writing an output file that
is over 8Gb
> >> in size.
> >> I want to split the output and produce say 4 files.  Can
anyone think of
> >> a way to write say 10000 records to one file then the next
10000 to the
> >> second file and so on until finished?
> >> Or should I sort the output in a second step to create the
four files?
> >
> >
…[4 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 4)_

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<58FD0C7B28C892AB.253ABE6507655D6B.1843E007A070BBCA@lp.airnews.net>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net> <395d4255.83531057@207.126.101.100> <8jjvcn$2od$1@sshuraab-i-1.production.compuserve.com>`

```
On Sat, 1 Jul 2000 01:25:11 -0400, "Russell Styles"
<RWSTYLES@COMPUSERVE.COM> enlightened us:

>    I have not dealt with mainframes in a while, but I understand
>that
…[7 more quoted lines elided]…
>

That used to be true in the days of reel tape, but it is not so in the
days of cartridge tapes.  The cartridges can hold up to a gig of data
and the transfer speeds are near those of a disk.  And if you're shop
is lucky enough to have a tape silo, multi tape processing is very
fast.

Regards,

>
>
…[70 more quoted lines elided]…
>

          ////
         (o o)
-oOO--(_)--OOo-

Wife who puts husband in doghouse soon find him in cathouse. 





Boycott Mitsubishi Industries

Remove nospam to email me.

 Steve
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 5)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-07-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395f322a.210482362@207.126.101.100>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net> <395d4255.83531057@207.126.101.100> <8jjvcn$2od$1@sshuraab-i-1.production.compuserve.com> <58FD0C7B28C892AB.253ABE6507655D6B.1843E007A070BBCA@lp.airnews.net>`

```
On Sat, 01 Jul 2000 14:52:46 -0400, SkippyPB
<swiegand@neo.rr.com.nospam> wrote:

>That used to be true in the days of reel tape, but it is not so in the
>days of cartridge tapes.  The cartridges can hold up to a gig of data
>and the transfer speeds are near those of a disk.  And if you're shop
>is lucky enough to have a tape silo, multi tape processing is very
>fast.

I concur.  On our piddly little 8 MIP P390 machine I found that some
jobs were actually quite a lot faster when I was able to split some of
the I/O out to tape.  
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Splitting output file

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000630232555.01242.00000567@nso-cd.aol.com>`
- **References:** `<wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net>`

```
In article <wp975.2607$Tr1.173422@dfiatx1-snr1.gtei.net>, "Michael Mattias"
<michael.mattias@gte.net> writes:

>
>Without using dynamic allocation (which I know can be done by I don;t know
…[3 more quoted lines elided]…
>

I'd have to do a little digging but I know that I have some code from this 
newgroup that allows switching DDnames attached to an FD.  It at least 
gets around the multiple SELECT/ASSIGN situation for creating a sequential
set of files from a program.

If there is no rule for record sequence or file content in the smaller files,
I would prefer to pass the entire file thru a sort with the SPLIT parm and a
list of 4-10 ddnames to separate the file out into smaller pieces.

If the first file MUST contain the first n records while the second file MUST 
contain the second n records, then I suppose the DDname switching DLL
is the route that I would take.

If anyone is interested, I can check on where I have that DDname switching
source.
```

#### ↳ Re: Splitting output file

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xc_65.10126$HD6.275274@iad-read.news.verio.net>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com>`

```
In article <8jhl55$q24$1@nnrp1.deja.com>,  <petert@my-deja.com> wrote:
>Hi all
>I have a mainframe cobol program writing an output file that is over 8Gb
>in size.
>I want to split the output and produce say 4 files.

Many folks want to do a variety of things... might I ask what is the
reason which causes you to have this desire?  Years ago I wrote an I-O
module for a company too lazy to clean out its VSAM files and it would be
best, I'd say, to re-think your design in order to avoid such things.

DD
```

##### ↳ ↳ Re: Splitting output file

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395C9D91.915F10FB@cusys.edu>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <xc_65.10126$HD6.275274@iad-read.news.verio.net>`

```


NA wrote:
> 
> In article <8jhl55$q24$1@nnrp1.deja.com>,  <petert@my-deja.com> wrote:
…[8 more quoted lines elided]…
> best, I'd say, to re-think your design in order to avoid such things.

I remember in olden times when we didn't have big DASD space.  One
technique to create large sorted files was to create a bunch of small
sorted files and then merge them.  The trick then was to find out how
many tape drives we would likely have available to figure out how many
generations of merging we needed to plan for.
```

###### ↳ ↳ ↳ Re: Splitting output file

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2000-07-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Mwd75.10244$HD6.282798@iad-read.news.verio.net>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <xc_65.10126$HD6.275274@iad-read.news.verio.net> <395C9D91.915F10FB@cusys.edu>`

```
In article <395C9D91.915F10FB@cusys.edu>,
Howard Brazee  <Please, do, not, e-mail, replies, to, Howard, Brazee, post,
 	them!!> wrote:
>
>
…[13 more quoted lines elided]…
>I remember in olden times when we didn't have big DASD space.

Ahhhh, for the Oldene Dayse... when one couldn't have disk-space such as
one cannot have space on *ten* disks today!

DD
```

###### ↳ ↳ ↳ Re: Splitting output file

- **From:** Fred Young <fred@perfectcircle.com>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396BBEA1.64A2C476@perfectcircle.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <xc_65.10126$HD6.275274@iad-read.news.verio.net> <395C9D91.915F10FB@cusys.edu>`

```


Howard Brazee wrote:

> NA wrote:
> >
…[15 more quoted lines elided]…
> generations of merging we needed to plan for.

If I remember my 1401 days, you could put half the file on tape, and the other
half on cards.  That should overcome the 8g limit.  And boy, that 1401 card
reader was sure fast.

enjoy
```

###### ↳ ↳ ↳ Re: Splitting output file

_(reply depth: 4)_

- **From:** Ed Guy <ed_guy@NOSPAMguysoftware.com>
- **Date:** 2000-07-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396BD0C4.1E2B@NOSPAMguysoftware.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com> <xc_65.10126$HD6.275274@iad-read.news.verio.net> <395C9D91.915F10FB@cusys.edu> <396BBEA1.64A2C476@perfectcircle.com>`

```
Fred Young wrote:

> 
> If I remember my 1401 days, you could put half the file on tape, and the other
> half on cards.  That should overcome the 8g limit.  And boy, that 1401 card
> reader was sure fast.

It was a thing of joy to watch.  When doing a binary load (i.e. not slowed down 
by processing) it was amazing to see those cards flying through the air and landing 
exactly where they were supposed to.  I moved to a Honeywell installation, and WHAT a 
contrast.  Frequently the thing threw the cards all over the floor.  Anybody who did not 
have a sequence key in their deck was in BIG trouble.
```

#### ↳ Re: Splitting output file

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395C9CC8.6257F5DA@cusys.edu>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com>`

```


petert@my-deja.com wrote:
> 
> Hi all
…[4 more quoted lines elided]…
> second file and so on until finished?

That's an odd question which looks as if you have never programmed
before.  You use a counter and an IF statement.

> Or should I sort the output in a second step to create the four files?
> Any help would be appreciated

Now this implies you have some familiarity with mainframe processes. 
I'm pretty sure a sort utility can do this and I would like to see some
replies to this part of your question.  (I am afraid people will assume
your question is homework and not get around to reading this part of
it).

One note is that neither of these methods will size the output files
depending on the total size.  You might consider opening all 4 files
simultaneously and then taking turns writing to each in turn.  That way
they will all be within a record of the same size when you're done.
```

#### ↳ Re: Splitting output file

- **From:** Warren Porter <wb999port@bellsouth12.net>
- **Date:** 2000-06-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<395CA207.885A9D12@bellsouth12.net>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com>`

```
petert@my-deja.com wrote:

> I have a mainframe cobol program writing an output file that is over 8Gb
> in size.
> I want to split the output and produce say 4 files.  Can anyone think of
> a way to write say 10000 records to one file then the next 10000 to the
> second file and so on until finished?

Perform a write paragraph to handle all output to your file(s).  On the
basis of a counter it would write to the proper file or close and reopen
with a different name as needed.
```

#### ↳ Re: Splitting output file

- **From:** petert@my-deja.com
- **Date:** 2000-07-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8jp0lc$o22$1@nnrp1.deja.com>`
- **References:** `<8jhl55$q24$1@nnrp1.deja.com>`

```
Thanks everybody for your input.....
Phew.....where to start....
The order IS important.... its the output of a fastscan of an IMS DB.
The order of course is parent, child....child, parent, parent, child,
child etc.
File must be split before new parent.
The reason for splitting is that the target is Oracle/Unix but the only
way to move it is via a PC (different networks, security, firewalls, you
dont wanna know....).  If I FTP to the PC in one go, I get hard disk
errors >2Gb...
We can split it via a mainframe sort, rejoin it back via Unix, then
logically split again for loading...
So, back to the problem....
the responder who suggested multiple select/assigns has pointed me the
way I think, also performing a paragraph for all the writes and deciding
the file in that.
That was the sort of detail/idea I was looking for.
Thanks
Peter

In article <8jhl55$q24$1@nnrp1.deja.com>,
  petert@my-deja.com wrote:
> Hi all
> I have a mainframe cobol program writing an output file that is over
8Gb
> in size.
> I want to split the output and produce say 4 files.  Can anyone think
of
> a way to write say 10000 records to one file then the next 10000 to
the
> second file and so on until finished?
> Or should I sort the output in a second step to create the four files?
…[6 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
