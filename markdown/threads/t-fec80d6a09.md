[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] JCL/Utility to List Datasets by High-Order Node?

_20 messages · 8 participants · 2009-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-02T13:28:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ha4v4v$rtp$1@reader1.panix.com>`

```

All righty... I know that certain IBM mainframe ISPF functions can be 
invoked in batch programs; Search For (option 3.14) and Compare (option 
3.12) have a screen option for Online or Batch, the latter generating JCL 
to invoke program ISRSUPC with appropriate parameters and control-cards.

Is anyone aware of where I might find a similar function for the Data Set 
List Utility (option 3.4)?  All I know now is how to do it manually:

Invoke the Utility from the command line.
Type HINODE.* on the Dsname Level line and whack Enter.
Type SAVE on the command line... and the results will be sent to something 
like MYUID.SYSn.SPFm.LIST which I can then use for other manipulations.

There are, most likely, CLIST or REXX solutions to this as well; given the 
level of sophistication in my present environment I believe it would be 
best to use plain JCL.  If that cannot be done then one of these other 
methods might be used but first choice is Use What They're Familiar With.

Thanks much!

DD
```

#### ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-10-03T03:28:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7imh17F32hephU1@mid.individual.net>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> All righty... I know that certain IBM mainframe ISPF functions can be
> invoked in batch programs; Search For (option 3.14) and Compare
…[23 more quoted lines elided]…
> DD

Please do your own homework.

Pete.
```

##### ↳ ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2009-10-02T09:07:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ko5cc5t2229acrd4f8hk5qhg6q0gee8t77@4ax.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <7imh17F32hephU1@mid.individual.net>`

```
On Sat, 3 Oct 2009 03:28:53 +1300, "Pete Dashwood"
<dashwood@removethis.enternet.co.nz> wrote:

>> Thanks much!
>>
…[4 more quoted lines elided]…
>Pete.

LOL!
```

##### ↳ ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-02T15:10:16+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ha554n$e4u$2@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <7imh17F32hephU1@mid.individual.net>`

```
In article <7imh17F32hephU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:
>> All righty... I know that certain IBM mainframe ISPF functions can be
…[24 more quoted lines elided]…
>Please do your own homework.

That might almost be valid, Mr Dashwood, had I not described the mechanism 
by which I was currently accomplishing the task (work/effort already 
invested), pointed out similar functions in the same environment 
(indicating research/familiarity with similar situations and the solutions 
that have been applied) and requested 'where might I find', not 'do it for 
me'... but that's what I'd think appropriate from someone who proudly 
admits to being 'Not Technical'.

Oh... you never proudly admitted to being 'Not Technical'?  So much for 
the validity of the comment, I guess.

DD
```

###### ↳ ↳ ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2009-10-03T12:02:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7inf3gF32ch2vU1@mid.individual.net>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <7imh17F32hephU1@mid.individual.net> <ha554n$e4u$2@reader1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <7imh17F32hephU1@mid.individual.net>,
> Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
…[39 more quoted lines elided]…
> DD

It was a joke Doc...

Are you losing your sense of humour?

Pete.
```

###### ↳ ↳ ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-03T00:44:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ha66os$7e5$1@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <7imh17F32hephU1@mid.individual.net> <ha554n$e4u$2@reader1.panix.com> <7inf3gF32ch2vU1@mid.individual.net>`

```
In article <7inf3gF32ch2vU1@mid.individual.net>,
Pete Dashwood <dashwood@removethis.enternet.co.nz> wrote:
>docdwarf@panix.com wrote:

[snip]

>> Oh... you never proudly admitted to being 'Not Technical'?  So much
>> for the validity of the comment, I guess.
…[3 more quoted lines elided]…
>Are you losing your sense of humour?

When trying to get from 'why don't you just do it for these few users by 
hand' and knowing, as I do, how 'these few users' will become 'any user at 
any time' so I look for machine-based solutions rather than manual ones... 
then perhaps the quantity of said sense might diminish, a tad.

My apologies if I offended; would you feel better were I to excoriate you 
about something?

DD
```

#### ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2009-10-02T15:02:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d1txm.86916$Wo3.30124@en-nntp-04.dc1.easynews.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com>`

```
I am not clear from your question if you are looking for a "JCL only - possibly 
with IBM utility" or if you are trying to find a "batch" solution.  If the 
latter, check out the ISPF service documented at;
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ISPZSG80/2.27

You can call that service from COBOL or many other "languages" (including - I 
think REXX).

If you are looking for a "utility only" solution, then I think (but haven't 
checked it) that IDCAMS will support this.
```

##### ↳ ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-10-02T22:13:47-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h59dc510aq227hqdod5i5v7oa79h4ujg68@4ax.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <d1txm.86916$Wo3.30124@en-nntp-04.dc1.easynews.com>`

```
On Fri, 2 Oct 2009 15:02:37 -0500, "William M. Klein"
<wmklein@nospam.ix.netcom.com> wrote:

>I am not clear from your question if you are looking for a "JCL only - possibly 
>with IBM utility" or if you are trying to find a "batch" solution.  If the 
…[7 more quoted lines elided]…
>checked it) that IDCAMS will support this.

They have made some improvements to IDCAMS in z/OS 1.10 or 1.11 that
support this in a non-intuitive manner and have problems if the user
catalog isn't known.  Fixes are being worked on.  See the archives of
bit.listserv.ibm-main or go to the ibm-main archives at bama.ua.edu.
You probably will need to register.
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

- **From:** slade <jnjsle1@optonline.net>
- **Date:** 2009-10-02T18:41:14-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0725168a-6aa6-42d5-83b4-97498a80d375@r36g2000vbn.googlegroups.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <d1txm.86916$Wo3.30124@en-nntp-04.dc1.easynews.com> <h59dc510aq227hqdod5i5v7oa79h4ujg68@4ax.com>`

```
On Oct 2, 9:13 pm, Clark F Morris <cfmpub...@ns.sympatico.ca> wrote:
> On Fri, 2 Oct 2009 15:02:37 -0500, "William M. Klein"
>
…[16 more quoted lines elided]…
> You probably will need to register.

This link should give you what you need, Doc.

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/handheld/Connected/BOOKS/DGT2I280/27.3.4?SHELF=&DT=20090603090124&CASE=
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-03T12:18:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ha7fee$8ue$2@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <d1txm.86916$Wo3.30124@en-nntp-04.dc1.easynews.com> <h59dc510aq227hqdod5i5v7oa79h4ujg68@4ax.com> <0725168a-6aa6-42d5-83b4-97498a80d375@r36g2000vbn.googlegroups.com>`

```
In article <0725168a-6aa6-42d5-83b4-97498a80d375@r36g2000vbn.googlegroups.com>,
slade  <jnjsle1@optonline.net> wrote:

[snip]

>This link should give you what you need, Doc.
>
>http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/handheld/Connected/BOOKS/DGT2I280/27.3.4?SHELF=&DT=20090603090124&CASE=

Greatly appreciated... when I'm back On The Clock I'll give a look-see and 
find out if my ancient, addled brain can still make sense of an IBM manual 
(which is defined as, according to my first programming instructor, 'a set 
of twenty-five chapters, each of which assumes intimate knowledge of the 
other twenty-three'.)

Thanks much!

DD
```

##### ↳ ↳ Re: [OT] JCL/Utility to List Datasets by High-Order Node?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-03T12:07:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ha7eql$8ue$1@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <d1txm.86916$Wo3.30124@en-nntp-04.dc1.easynews.com>`

```
In article <d1txm.86916$Wo3.30124@en-nntp-04.dc1.easynews.com>,
William M. Klein <wmklein@nospam.ix.netcom.com> wrote:
>I am not clear from your question if you are looking for a "JCL only - possibly 
>with IBM utility" or if you are trying to find a "batch" solution.

My apologies for my lack of clarity, Mr Klein.  I am looking for a 
solution which would consist of a batch job written in JCL and using only 
programs (eg, 'IBM utilities') which one might reasonably expect to be at 
even the most primitive of MVS installations.

>If the 
>latter, check out the ISPF service documented at;
…[6 more quoted lines elided]…
>checked it) that IDCAMS will support this.

Comes Monday in this part of the world and I'll get to snooping.

Thanks much!

DD
```

#### ↳ Re: JCL/Utility to List Datasets by High-Order Node?

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2009-10-04T06:27:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99c06c6e-47da-4ba8-bae6-c6ce16451f5d@e18g2000vbe.googlegroups.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com>`

```
On Oct 2, 2:28 pm, docdw...@panix.com () wrote:
> All righty... I know that certain IBM mainframe ISPF functions can be
> invoked in batch programs; Search For (option 3.14) and Compare (option
…[18 more quoted lines elided]…
> DD

Try:

http://www.tsotimes.com/articles/archive/summerfall98/ispf.html
```

##### ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-04T18:19:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<haaovp$qpe$1@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <99c06c6e-47da-4ba8-bae6-c6ce16451f5d@e18g2000vbe.googlegroups.com>`

```
In article <99c06c6e-47da-4ba8-bae6-c6ce16451f5d@e18g2000vbe.googlegroups.com>,
Alistair  <alistair@ld50macca.demon.co.uk> wrote:
>On Oct 2, 2:28?pm, docdw...@panix.com () wrote:

[snip]

>> Is anyone aware of where I might find a similar function for the Data Set
>> List Utility (option 3.4)? ?All I know now is how to do it manually:

[snip]

>Try:
>
>http://www.tsotimes.com/articles/archive/summerfall98/ispf.html

Greatly appreciated, Mr Maclean; come Monday morn I'll give this (and the 
others) various whacks and report back with the results.

DD
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-10-04T22:13:18-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mOOdnSq1pfGry1TXnZ2dnUVZ_qGdnZ2d@earthlink.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <99c06c6e-47da-4ba8-bae6-c6ce16451f5d@e18g2000vbe.googlegroups.com> <haaovp$qpe$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:haaovp$qpe$1@reader1.panix.com...
> In article 
> <99c06c6e-47da-4ba8-bae6-c6ce16451f5d@e18g2000vbe.googlegroups.com>,
…[19 more quoted lines elided]…
>
So you are taking up where Lizzie Borden left off:

Lizzie Borden took an axe
And gave her mother forty whacks.
When she saw what she had done
She gave her father forty-one
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-05T12:39:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hacpdg$msu$1@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <99c06c6e-47da-4ba8-bae6-c6ce16451f5d@e18g2000vbe.googlegroups.com> <haaovp$qpe$1@reader1.panix.com> <mOOdnSq1pfGry1TXnZ2dnUVZ_qGdnZ2d@earthlink.com>`

```
In article <mOOdnSq1pfGry1TXnZ2dnUVZ_qGdnZ2d@earthlink.com>,
Charles Hottel <chottel@earthlink.net> wrote:
>
><docdwarf@panix.com> wrote in message news:haaovp$qpe$1@reader1.panix.com...
…[18 more quoted lines elided]…
>> others) various whacks and report back with the results.

[snip]

>So you are taking up where Lizzie Borden left off:
>
…[3 more quoted lines elided]…
>She gave her father forty-one 

Actually... woke up this morning with some manner of amphibian lodged in 
my larynx and In These Days of Influenza-Transmission I sent off an email 
to a tech-lead (with cc:'s to two corner-office holders) saying 'Y'know... 
if someone else told me that they felt - and sounded - as I do I'd respond 
'Stay home and do the Big Three: bedrest, force fluids and aspirin.'

I then thought 'Wait a minute... I can remote log-in (even though they 
don't like it except for emergencies), I have email and a cellular 
telephone... why am I so unworthy of doing what I'd tell anyone else to do 
under these circumstances?'

So... an extra pot of coffee, a 16oz glass of half orange/half grapefruit 
juice, a curious combination of drugs and - just to be sure - a dollop of 
Nin Jiom Pei Pa Koa to soothe the frazzled throat.

E'en in illness... Life is Good, aye.

DD
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 5)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-07T17:10:42+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<haii2i$bbf$1@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <haaovp$qpe$1@reader1.panix.com> <mOOdnSq1pfGry1TXnZ2dnUVZ_qGdnZ2d@earthlink.com> <hacpdg$msu$1@reader1.panix.com>`

```

All righty... here's the bird's-eye low-down on this caper... whatever 
that means (Firesign Theatre).

Mr Klein suggested 
http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ISPZSG80/2.27 
and this details use of the LMDDISP data set list service.  I coded an 
IKJEFT01 job with ISPEXEC LMDDISP LISTID('MYUID') VIEW(VOLUME) 
CONFIRM(YES) and got a Condition Code of 20 (according to 
<http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ISPZSG80/2.27.4?SHELF=&DT=20090611002745&CASE=> 
this means 'A severe error occurred while processing the data set list'.

Another suggestion was to use a LISTCAT under IDCAMS... this both worked 
and did not work.  LISTCAT ENTRIES(MYUID.*) ALL gave me all the datasets 
with MYUID as the high-order node and only one lower level node; in other 
words it would return

MYUID.NODE1
MYUID.NODE3

... and *not* return MYUID.NODE2.NODE2.  Changing to MYUID.*.* or MYUID* 
both got me a Condition Code of 12 and error IDC3203I.

Mr Maclean offered 
http://www.tsotimes.com/articles/archive/summerfall98/ispf.html which lead 
to an article on how to invoke the ISPF Edit macro on a dataset which 
contained what I already wanted ('For example you could run a listcat job 
in batch for all datasets with the high level qualifier of "TEST". Have 
the output of this job go to a dataset which is then cataloged.')... but, 
as noted above, I could get LISTCAT to display only the two-noded 
datasets.

So close... and yet so far.  I recall using ADRDSSU in the wild-card 
manner I need... but not to list dataset names, just to delete them.  Call 
me lazy but I don't want to kill the datasets and then have to restore 
them just to get a listing.

Thanks to all for the help, though.

DD
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 6)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-10-08T21:51:40-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7f-dnbqsXZmxClPXnZ2dnUVZ_jadnZ2d@earthlink.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <haaovp$qpe$1@reader1.panix.com> <mOOdnSq1pfGry1TXnZ2dnUVZ_qGdnZ2d@earthlink.com> <hacpdg$msu$1@reader1.panix.com> <haii2i$bbf$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:haii2i$bbf$1@reader1.panix.com...
>
> All righty... here's the bird's-eye low-down on this caper... whatever
…[38 more quoted lines elided]…
>

I think this does what you want:

//JOBNAME JOB (ACCT,'ROOM'),HOTTEL,CLASS=A,MSGCLASS=S
//PROCLIB JCLLIB ORDER=USERID.DVL.PROC
//        SET TITLE1='PFX.LISTCAT'
//OUTPUT INCLUDE MEMBER=DESTCH
//*-------------------------------------------------------------------*
//*        IDCAMS                                                     *
//*-------------------------------------------------------------------*
//STEP1    EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
  LISTCAT  LEVEL(USERID) -
           NAME

```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 7)_

- **From:** docdwarf@panix.com ()
- **Date:** 2009-10-09T09:59:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<han1io$d0p$1@reader1.panix.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <hacpdg$msu$1@reader1.panix.com> <haii2i$bbf$1@reader1.panix.com> <7f-dnbqsXZmxClPXnZ2dnUVZ_jadnZ2d@earthlink.com>`

```
In article <7f-dnbqsXZmxClPXnZ2dnUVZ_jadnZ2d@earthlink.com>,
Charles Hottel <chottel@earthlink.net> wrote:
>
><docdwarf@panix.com> wrote in message news:haii2i$bbf$1@reader1.panix.com...
>>
>> All righty... here's the bird's-eye low-down on this caper... whatever
>> that means (Firesign Theatre).

[details of failures snipped]

>I think this does what you want:
>
…[11 more quoted lines elided]…
>           NAME

A far sight more than what I had, Mr Hottel, and greatly appreciated... 
not quite there, yet, as I'll need to take the output of this LISTCAT and 
then use it as input to another series of LISTCATS (via DFSORT or a 
program I'm not sure... I've used COBOL for text-processing (as have 
others who have dealt with de-duping mailing lists and I don't like it as 
a tool for that) to get space used and Volume Name (the original goal was 
to batch-create the output of a 3.4 for MYUID with a command-line SAVE) 
but it provides much good use.

Thanks much!

DD
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 8)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2009-10-09T12:46:22-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rfluc59rc7e7j4mqe59ariaace5bd2a22o@4ax.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <hacpdg$msu$1@reader1.panix.com> <haii2i$bbf$1@reader1.panix.com> <7f-dnbqsXZmxClPXnZ2dnUVZ_jadnZ2d@earthlink.com> <han1io$d0p$1@reader1.panix.com>`

```
On Fri, 9 Oct 2009 09:59:52 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <7f-dnbqsXZmxClPXnZ2dnUVZ_jadnZ2d@earthlink.com>,
>Charles Hottel <chottel@earthlink.net> wrote:
…[30 more quoted lines elided]…
>but it provides much good use.

If you add the keyword VOL to the statement you will get the Volume
Serial number and device type.  The catalog only has space allocation
for VSAM data set so you would need another utility.  If you are into
Assembler, there are several utilities available at www.cbttape.org.
If your site has FDR/ABR from innovation, it has FDRREPORT which
allows you the ability to get all of the information you want nicely
formatted and only the information you want.  This is an outstanding
utility.  For full information on this google IBM IDCAMS LISTCAT and
go to the first entry, then pick the manual DSSMS Access Method
Services For Catalogs and use LISTCAT.  The URL
http://publib.boulder.ibm.com/infocenter/zos/v1r9/topic/com.ibm.zos.r9.idai200/dgt2i251.htm
probably will get you to the exact entry.  For a system that is
supposedly Closed, you can get a wealth of information online
including every generally available manual (all of the COBOL manuals
and enough information to probably write your own 3270 emulator).  If
your shop has an IBM software product, you can view the manuals for it
anywhere in the world.
>
>Thanks much!
>
>DD
```

###### ↳ ↳ ↳ Re: JCL/Utility to List Datasets by High-Order Node?

_(reply depth: 8)_

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2009-10-09T14:03:58-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dNadnWmJ1r-W5lLXnZ2dnUVZ_g6dnZ2d@earthlink.com>`
- **References:** `<ha4v4v$rtp$1@reader1.panix.com> <hacpdg$msu$1@reader1.panix.com> <haii2i$bbf$1@reader1.panix.com> <7f-dnbqsXZmxClPXnZ2dnUVZ_jadnZ2d@earthlink.com> <han1io$d0p$1@reader1.panix.com>`

```

<docdwarf@panix.com> wrote in message news:han1io$d0p$1@reader1.panix.com...
> In article <7f-dnbqsXZmxClPXnZ2dnUVZ_jadnZ2d@earthlink.com>,
> Charles Hottel <chottel@earthlink.net> wrote:
…[36 more quoted lines elided]…
>

Here is a program, COBTSO, from Gilbert St. Flour that can issue a TSO/E 
command.  You might be able to modify it into what you want.

//JOBNAME  JOB (ACCT,'ROOM'),'HOTTEL COBTSO',MSGCLASS=S,CLASS=K
//PROCLIB JCLLIB ORDER=USERID.DVL.PROC
//        SET TITLE1='PFX.COB00007'
//OUTPUT INCLUDE MEMBER=DESTCH
//*-------------------------------------------------------------------*
//*        COBOL II COMPILE                                           *
//*-------------------------------------------------------------------*
//STEP01   EXEC  COB3CLG,LIBRARY='DVL.SOURCE.LIBMAST',PROG=IEFBR14,
//    OPT=DYNAM,LOPT='AMODE=31,RMODE=ANY'
//COMP.SYSIN DD  *
       IDENTIFICATION DIVISION.
         PROGRAM-ID. COBTSO.
      ******************************************************************
      *                                                                *
      *   MODULE NAME = COBTSO                                         *
      *                                                                *
      *   DESCRIPTIVE NAME = ISSUE TSO COMMANDS FROM A COBOL PROGRAM.  *
      *                                                                *
      *   FUNCTION = THIS SAMPLE PROGRAM DEMONSTRATES HOW TO INVOKE    *
      *              TSO COMMANDS FROM A COBOL PROGRAM USING           *
      *              STANDARD TSO SERVICES AS DOCUMENTED IN THE        *
      *              TSO/E PROGRAMMING SERVICES MANUAL.                *
      *                                                                *
      *              MOST TSO COMMANDS, INCLUDING CLISTS AND REXX      *
      *              EXECS CAN BE EXECUTED USING THIS TECHNIQUE.       *
      *              TSO COMMANDS WHICH REQUIRE AUTHORIZATION          *
      *              (SUCH AS OUTPUT, SEND, TRANSMIT AND RECEIVE)      *
      *              WILL NOT WORK.                                    *
      *                                                                *
      *   AUTHOR   =  GILBERT SAINT-FLOUR <GSF@POBOX.COM>              *
      *                                                                *
      ******************************************************************
      /
       DATA DIVISION.
        WORKING-STORAGE SECTION.
         01 FILLER.
           05 WS-DUMMY        PIC S9(8) COMP.
           05 WS-RETURN-CODE  PIC S9(8) COMP.
           05 WS-REASON-CODE  PIC S9(8) COMP.
           05 WS-INFO-CODE    PIC S9(8) COMP.
           05 WS-CPPL-ADDRESS PIC S9(8) COMP.
           05 WS-FLAGS        PIC X(4) VALUE X'00010001'.
           05 WS-BUFFER       PIC X(256).
           05 WS-LENGTH       PIC S9(8) COMP VALUE 256.
      /
       PROCEDURE DIVISION.
      *----------------------------------------------------------------*
      *          CALL IKJTSOEV TO CREATE THE TSO/E ENVIRONMENT         *
      *----------------------------------------------------------------*
           CALL 'IKJTSOEV' USING WS-DUMMY
                                 WS-RETURN-CODE
                                 WS-REASON-CODE
                                 WS-INFO-CODE
                                 WS-CPPL-ADDRESS.
           IF WS-RETURN-CODE > ZERO
             DISPLAY 'IKJTSOEV FAILED, RETURN-CODE=' WS-RETURN-CODE
                                     ' REASON-CODE=' WS-REASON-CODE
                                     'INFO-CODE='    WS-INFO-CODE
             MOVE WS-RETURN-CODE TO RETURN-CODE
             STOP RUN.
      *----------------------------------------------------------------*
      *          BUILD THE TSO/E COMMAND IN WS-BUFFER                  *
      *----------------------------------------------------------------*

           MOVE 'ALLOCATE DD(SYSPUNCH) SYSOUT HOLD' TO WS-BUFFER.

      *----------------------------------------------------------------*
      *   CALL THE TSO/E SERVICE ROUTINE TO EXECUTE THE TSO/E COMMAND  *
      *----------------------------------------------------------------*
           CALL 'IKJEFTSR' USING WS-FLAGS
                                 WS-BUFFER
                                 WS-LENGTH
                                 WS-RETURN-CODE
                                 WS-REASON-CODE
                                 WS-DUMMY.
           IF WS-RETURN-CODE > ZERO
             DISPLAY 'IKJEFTSR FAILED, RETURN-CODE=' WS-RETURN-CODE
                                     ' REASON-CODE=' WS-REASON-CODE
             MOVE WS-RETURN-CODE TO RETURN-CODE
             STOP RUN.

      *----------------------------------------------------------------*
      *          CHECK THAT THE ALLOCATE COMMAND WORKED                *
      *----------------------------------------------------------------*
           DISPLAY 'ALLOCATE WORKED ! ' UPON SYSPUNCH.

           STOP RUN.
//LKED.SYSLIB  DD
//             DD
//             DD DSN=XXXX.YYY.DVL.BATLOAD,DISP=SHR
//LKED.SYSLMOD DD DSN=&&LOADLIB(COBTSO),DISP=(OLD,PASS)
//LKED.SYSIN DD *
  NAME COBTSO(R)
//GO.SYSUDUMP DD SYSOUT=*
//GO.SYSPRINT DD SYSOUT=*
//GO.SYSOUT   DD SYSOUT=*
//GO.SYSDBOUT DD SYSOUT=*

```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
