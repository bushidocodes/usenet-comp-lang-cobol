[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] Obvious Is In The Mind Of The Beholder - JCL illustrIllustration

_4 messages · 3 participants · 2004-11 → 2004-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [OT] Obvious Is In The Mind Of The Beholder - JCL illustrIllustration

- **From:** docdwarf@panix.com
- **Date:** 2004-11-15T13:37:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cnat1e$15h$1@panix5.panix.com>`

```

All righty... so there's some processing being done that requires some 
translation.  What comes in is a file with an SSN and a job number... due 
to some whacky accounting requirements there is billing that is done under 
a 'pseudo-SSN' which is assigned to this combination.  There's another 
file which contains all three of these elements; given that the number of 
records is moderate (about 70,000) the way to deal with this has been 
decided to be a VSAM (indexed) lookup-file, with real-SSN and job number, 
concatenated, as the key and the pseudo-SSN (which can be the same as the 
real) delivered as the result.

Since this is 'this week's solution' I didn't put too much into it... 
USER02 supplies a flat file and I put together some JCL to make a VSAM out 
of it.  Testing revealed a small problem... there were some records with 
the same real-SSN and job number but different pseudo-SSNs associated with 
them; the Corner-Office Guy said 'If we try to chase down why this was 
done we'll be here until next month... to hell with it, just grab one 
real-SSN/job number combination and use that, for now, we'll look at the 
problem of dupes When We Have Time.'

So... I cobbled together a jobstream, nothing too pretty but it works... 
and it looks like this:

//STEP000  EXEC PGM=IEFBR14
//DD01     DD  DISP=(MOD,DELETE),
//             UNIT=DISK,
//          DSN=USERID01.PSEUDSSN.FLAT
//*---------------------------------------------------------------*
//STEP010 EXEC  PGM=ICEMAN
//SORTLIB  DD  DSN=SYS1.SORTLIB,DISP=SHR
//SYSOUT   DD  SYSOUT=*
//SORTIN   DD    DISP=SHR,
//         DSN=USERID02.FLAT.SSN
//SORTOUT  DD DSN=USERID01.PSEUDSSN.FLAT,
//            DISP=(,CATLG,CATLG),
//            UNIT=FILE,
//            SPACE=(CYL,(10,5),RLSE),
//            DCB=(RECFM=FB,LRECL=26,BLKSIZE=0)
//SYSIN    DD  *
 SORT FIELDS=(1,9,CH,A,86,8,CH,A,12,9,CH,A)
 OUTREC   FIELDS=(01:01,9,10:86,8,18:12,9)
 END
//*
//STEP020 EXEC  PGM=ICEMAN
//SORTLIB  DD  DSN=SYS1.SORTLIB,DISP=SHR
//SYSOUT   DD  SYSOUT=*
//SORTIN   DD    DISP=SHR,
//         DSN=USERID01.PSEUDSSN.FLAT
//SORTOUT  DD DSN=USERID01.PSEUDSSN.FLAT,
//            DISP=SHR
//SYSIN    DD  *
 SORT FIELDS=(1,17,CH,A)
 SUM FIELDS=(NONE)
//*
//STEP030   EXEC PGM=IDCAMS,COND=(0,NE)
//SYSIN    DD *
  DELETE (USERID01.VSAM.PSEUDSSN) SCRATCH
  IF MAXCC NE 0 -
      THEN SET MAXCC=0
  DEFINE CLUSTER (NAME       (USERID01.VSAM.PSEUDSSN)                -
                  KEYS       (17 0)                                  -
                  VOLUMES    (FILE25)                                -
                  CYLINDERS  (5  5)                                  -
                  RECORDSIZE (26  26)                                -
                  FREESPACE  (15 20)                                 -
                  REUSE                                              -
                  SHAREOPTIONS (2 3))
/*
//*
//STEP040   EXEC PGM=IDCAMS,COND=(0,NE)
//INPUT1   DD DSN=USERID01.PSEUDSSN.FLAT,DISP=SHR
//OUTPUT1  DD DSN=USERID01.VSAM.PSEUDSSN,DISP=SHR
//SYSIN    DD *
  REPRO INFILE(INPUT1) OUTFILE(OUTPUT1)
/*
//*

... and for those unfamiliar with the phenomenon... STEP000 deletes a 
previously-made flat file, STEP010 reads the input and grabs the real-SSN 
from position 1, the job number from position 86 and the pseudo-SSN from 
position 12 and writes all of these to another flat file, STEP020 goes 
through this newly-created file and removes the duplicates based on 
real-SSN and job number, STEP030 deletes the former VSAM file and defines 
a new one and STEP040 loads the de-duped flat file into the VSAM.

Nothing special, nothing pretty... but it works... for 'this week's 
solution'.

Anyhow... another programmer stopped by my cube and asked about my 
processing, seems like he'll be doing the reverse of what I'm doing and 
trying to look up a real-SSN based on a pseudo-SSN; I said that this was 
what I'd tossed together and he was welcome to it.  Then... I felt kinda 
bad about dumping so ugly into his lap and sent him an email, apologising 
for the unattractiveness of what I'd given him and the lack of explanatory 
comments in it.

His response was: 'No reason for apologies, it looked like a playboy 
centerfold compared to some of my stuff and it was pretty self 
explanatory.'

'Obvious' is in the mind of the beholder.

DD
```

#### ↳ Re: [OT] Obvious Is In The Mind Of The Beholder - JCL illustrIllustration

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-11-16T00:46:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-D7D773.00464316112004@knology.usenetserver.com>`
- **References:** `<cnat1e$15h$1@panix5.panix.com>`

```
In article <cnat1e$15h$1@panix5.panix.com>, docdwarf@panix.com wrote:

> All righty... so there's some processing being done that requires some 
> translation.  What comes in is a file with an SSN and a job number... due 
…[100 more quoted lines elided]…
> 

Your stream seems quite obvious to me...

Why not just alternate index your pseudo->2->real file for 
real->2->pseudo access?  Just drop a DEFINE PATH in STEP0030 and blah, 
blah, blah.

Then the other programmer has all he needs to be productive and the 
corner-office guy is impressed...
```

##### ↳ ↳ Re: [OT] Obvious Is In The Mind Of The Beholder - JCL illustrIllustration

- **From:** docdwarf@panix.com
- **Date:** 2004-11-16T02:59:21-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cncc0p$nfp$1@panix5.panix.com>`
- **References:** `<cnat1e$15h$1@panix5.panix.com> <joe_zitzelberger-D7D773.00464316112004@knology.usenetserver.com>`

```
In article <joe_zitzelberger-D7D773.00464316112004@knology.usenetserver.com>,
Joe Zitzelberger  <joe_zitzelberger@nospam.com> wrote:
>In article <cnat1e$15h$1@panix5.panix.com>, docdwarf@panix.com wrote:

[snip]

>> Then... I felt kinda 
>> bad about dumping so ugly into his lap and sent him an email, apologising 
…[10 more quoted lines elided]…
>Your stream seems quite obvious to me...

Of a similarly-bent mind, perhaps.

>
>Why not just alternate index your pseudo->2->real file for 
>real->2->pseudo access?  Just drop a DEFINE PATH in STEP0030 and blah, 
>blah, blah.

I've suggested this; the response was that while this might be the way 
things wind up his needs were evolving along with the specs he received 
and he did not want to subject my development to the vagaries of his 
user's whims.

>
>Then the other programmer has all he needs to be productive and the 
>corner-office guy is impressed...

We may end up like this, sure, once his situation has gelled a bit.

DD
```

#### ↳ SORTLIB should be dead was Re: [OT] Obvious Is In The Mind Of The Beholder - JCL illustrIllustration

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-12-16T16:04:22-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<32e841F3jn4i5U1@uni-berlin.de>`
- **In-Reply-To:** `<cnat1e$15h$1@panix5.panix.com>`
- **References:** `<cnat1e$15h$1@panix5.panix.com>`

```
docdwarf@panix.com wrote:

> All righty... so there's some processing being done that requires some 
> translation.  What comes in is a file with an SSN and a job number... due 
…[26 more quoted lines elided]…
> //SORTLIB  DD  DSN=SYS1.SORTLIB,DISP=SHR

I thought the need for a SORTLIB had died in the 1970's.  I know 
SYNCSORT doesn't need one and I doubt that DF/SORT does.  I think that I 
was able to kill SYS1.SORTLIB in the late 1970's or early 1980's where I 
used to work.

> //SYSOUT   DD  SYSOUT=*
> //SORTIN   DD    DISP=SHR,
…[71 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
