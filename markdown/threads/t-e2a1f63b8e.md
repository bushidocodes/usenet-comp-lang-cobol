[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# JCL Megabytes

_3 messages · 3 participants · 1998-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### JCL Megabytes

- **From:** "patrick finnegan" <ua-author-1889869@usenetarchives.gap>
- **Date:** 1998-04-05T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6gajee$hf7$1@reader1.reader.news.ozemail.net>`

```



Recently I started work on a project which involves transferring large PC
files to an IBM 3090 mainframe via FTP. We had to determine the size of the
files but the PC analyst kept talking in megabytes while I talked in
cylinders and tracks. Wile trawling through the JCL manuals I came across
the AVGREC parameter which can be used to specify file size in kilobytes or
megabytes. The instructions are confusing because the command is meant to
specify space per record. Since my records were 480 bytes I used
SPACE=(480,(1,1),RLSE) with AVGREC=M. However this allocated a file of 480
Mb. I then tried SPACE=(1,(1,1),RLSE) with AVGREC=M and this allocated a 1
MB file(see JCL below). Is this the way the command should be used or was
this a fluke?





//*********************************************************************
001300 //* ALLOCATE KPI WATER FILES
001400
//*********************************************************************
001500 //STEP01 EXEC PGM=IEFBR14
001600 //SYSUT1 DD DUMMY,RECFM=FBA,LRECL=133,BLKSIZE=23408
001700 //SYSUT2 DD DSN=WAGWFD.KPI.WAPF,
001800 // DISP=(NEW,CATLG,DELETE),
001900 // RECFM=FB,
002000 // LRECL=480,
002100 // DSORG=PS,
002200 // SPACE=(1,(1,1),RLSE),
002300 // AVGREC=M
002400 //SYSIN DD DUMMY
002500 //SYSPRINT DD SYSOUT=*
002600 //*
002610 //
002620
//*********************************************************************
```

#### ↳ Re: JCL Megabytes

- **From:** "scom..." <ua-author-2666089@usenetarchives.gap>
- **Date:** 1998-04-05T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e2a1f63b8e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6gajee$hf7$1@reader1.reader.news.ozemail.net>`
- **References:** `<6gajee$hf7$1@reader1.reader.news.ozemail.net>`

```

"Patrick Finnegan" writes ...

› Wile [sic] trawling through the JCL manuals I came across
› the AVGREC parameter which can be used to specify file size in kilobytes or
› megabytes.  The instructions are confusing because the command is meant to
› specify space per record. 

No, not space per record, but total amount of space needed, based on record
size. see below.

› Since my records were 480 bytes I used
› SPACE=(480,(1,1),RLSE) with AVGREC=M. However this allocated a file of 480
› Mb.  I then tried  SPACE=(1,(1,1),RLSE) with AVGREC=M and this allocated a 1
› MB file(see JCL below).  Is this the way the command should be used or was
› this a fluke?

OK, so here's the story.

AVGREC works in conjunction with the SPACE parameter. If you use AVGREC, you
specify SPACE as follows:

SPACE=(lrecl,(pri,sec))

Then AVGREC=U or AVGREC=K or AVGREC=M

"lrecl" is your record size. "pri" is your primary (initial) space request,
"sec" is your secondary (additional) space request in case you fill up the
primary and need more. The U, K, or M are used to indicate the "pri" value
indicates Units, Thousands, or Millions of records. DASDM then figures out the
number of tracks or cylinders you need.

For example, if you code SPACE=(480,(4,2)),AVGREC=K, you are asking for enough
room to hold 4000 records of 480 bytes for your primary allocation and enough
space to hold 2000 records for secondary allocation. If you change AVGREC to M,
then you are asking for enough room to hold 4000000 records of 480 bytes
primary and 2000000 records of 480 bytes secondary.

Cheers,


Steve Comstock
Telephone: 303-393-8716
email: SCo··.@a··.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: JCL Megabytes

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1998-04-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e2a1f63b8e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e2a1f63b8e-p2@usenetarchives.gap>`
- **References:** `<6gajee$hf7$1@reader1.reader.news.ozemail.net> <gap-e2a1f63b8e-p2@usenetarchives.gap>`

```

S Comstock wrote:
...
› For example, if you code SPACE=(480,(4,2)),AVGREC=K, you are asking for enough
› room to hold 4000 records of 480 bytes for your primary allocation and enough
…[3 more quoted lines elided]…
› 
In their infinite wisdom (or a deliberate attempt to confuse end users
that deal with business problems in base 10), IBM actually chose to
define AVGREC=K as multiples of 1024 records and AVRGEC=M as multiples
of 2**20 = 1048576 records, an unfortunate example of binary mindset
carried to unnecessary and ridiculous extremes. SPACE=(480,(4,2)) with
AVGREC=K is requesting space for 4096 records primary, 2048 records
secondary, and with AVGREC=M, space for 4194304 records primary, 2097152
records secondary. In cases where space requests are estimates anyhow,
that you might get 2-5% more than you expected is no big deal. If you
are trying for exact allocation, the nonintutive definition of K and M
is an annoyance. Another thing to keep in mind is that the allocation
algorithm presumes an efficient blocksize (like system-determined
blocksize). If you force a very inefficient block size through JCL or
the program when you write the data, it may not fit in the allocated
space. If the user only thinks well in KB and MB and not in records,
then you can "lie" about the record size in the SPACE parameter as you
have already discovered, as there is no enforced correlation with actual
LRECL or BLKSIZE and the 1st positional parameter of the SPACE
parameter.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
