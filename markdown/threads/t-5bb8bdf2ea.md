[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IEBGENER Question

_7 messages · 7 participants · 1998-04 → 1998-05_

---

### IEBGENER Question

- **From:** "kalpataru barman" <ua-author-17071492@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<353D7F58.A6B2F82F@mail-me.com>`

```

I want to copy a variable length QSAM file into one fixed
length QSAM file using a batch JCL job. ( MVS/ESA or OS390 ).
I tried IEBGENER, but it is giving trouble.
[ I know in ISPF 3.3 copy, an alarm comes that data may be truncated.]
```

#### ↳ Re: IEBGENER Question

- **From:** "mickey ben-tovim" <ua-author-17074116@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5bb8bdf2ea-p2@usenetarchives.gap>`
- **In-Reply-To:** `<353D7F58.A6B2F82F@mail-me.com>`
- **References:** `<353D7F58.A6B2F82F@mail-me.com>`

```

Try IEBCOPY.

mickey

Kalpataru Barman wrote:
› 
› I want to copy a variable length QSAM file into one fixed
› length QSAM file using a batch JCL job. ( MVS/ESA or OS390 ).
› I tried IEBGENER, but it is giving trouble.
› [ I know in ISPF 3.3 copy, an alarm comes that data may be truncated.]
```

##### ↳ ↳ Re: IEBGENER Question

- **From:** "binyami..." <ua-author-932190@usenetarchives.gap>
- **Date:** 1998-04-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5bb8bdf2ea-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5bb8bdf2ea-p2@usenetarchives.gap>`
- **References:** `<353D7F58.A6B2F82F@mail-me.com> <gap-5bb8bdf2ea-p2@usenetarchives.gap>`

```

On Wed, 22 Apr 1998 16:15:37 -0400 Mickey Ben-Tovim wrote:

:>Try IEBCOPY.

For a sequential data set???

Perhaps something like this (yeah, I know I should try it first, yada yada)

// EXEC PGM=IEBGENER
//SYSPRINT DD SYSOUT=*
//SYSUT2 DD DSN=FB.FILE,DCB=(RECFM=FB,LRECL=80,BLKSIZE=6160),......
//SYSUT1 DD DSN=VB.FILE,DCB=(RECFM=VB,LRECL=???,BLKSIZE=????),.....
//SYSIN DD *
GENERATE MAXFLDS=3,MAXLITS=80
RECORD FIELD=(40,' ',,1),
FIELD=(40,' ',,41),
FIELD=(80,1,,1)
/*

Or course, if the VB file has records larger than the FB LRECL, there is no
way to avoid truncation.

:>mickey

:>Kalpataru Barman wrote:

:>> I want to copy a variable length QSAM file into one fixed
:>> length QSAM file using a batch JCL job. ( MVS/ESA or OS390 ).
:>> I tried IEBGENER, but it is giving trouble.
:>> [ I know in ISPF 3.3 copy, an alarm comes that data may be truncated.]
```

#### ↳ Re: IEBGENER Question

- **From:** "joel c. ewing" <ua-author-40228@usenetarchives.gap>
- **Date:** 1998-04-21T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5bb8bdf2ea-p4@usenetarchives.gap>`
- **In-Reply-To:** `<353D7F58.A6B2F82F@mail-me.com>`
- **References:** `<353D7F58.A6B2F82F@mail-me.com>`

```

Kalpataru Barman wrote:
› I want to copy a variable length QSAM file into one fixed
› length QSAM file using a batch JCL job. ( MVS/ESA or OS390 ).
› I tried IEBGENER, but it is giving trouble.
› [ I know in ISPF 3.3 copy, an alarm comes that data may be truncated.]

IEBGENER is very old, "dumb", and inefficient (unless executing a SORT
utility's IEBGENER replacement under the covers). Almost anything
involving changes to LRECL or changes in RECFM either requires presence
of nonintuitive control cards or is impossible. The IDCAMS utility
REPRO command can handle variable-fixed and fixed-variable conversions
and can even copy RECFM=U datasets. REPRO will give error indications
if you copy variable to fixed and the destination LRECL is less than
required by some of the input records (based on actual record size
found, not the max record size declared for the VB dataset). The
warning you get in ISPF 3.3 copy is simply telling you that based on the
LRECL of source and destination datasets that truncation is possible,
not that it will actually occur. If all the actual input records are
short enough to fit within the FB dataset's LRECL, then there is no
truncation. If some records exist that are too long, they will be
truncated. Using IDCAMS REPRO these same records would cause an error
message, not be copied, and would force a bad return code.

Other possibilities are to use one of the standard SORT utilities
(SYNCSORT, DFSORT). These utilities can copy datasets while modifying
record format, including conversion between RECFM FB and VB, but will
require some control cards to instruct the utility how to proceed.
Joel C. Ewing, Fort Smith, AR        jce··.@a··.org
```

#### ↳ Re: IEBGENER Question

- **From:** "fyae..." <ua-author-17074334@usenetarchives.gap>
- **Date:** 1998-04-23T11:06:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5bb8bdf2ea-p5@usenetarchives.gap>`
- **In-Reply-To:** `<353D7F58.A6B2F82F@mail-me.com>`
- **References:** `<353D7F58.A6B2F82F@mail-me.com>`

```

In article <353··.@mai··e.com>,
Kalpataru Barman wrote:
› 
› I want to copy a variable length QSAM file into one fixed
…[4 more quoted lines elided]…
› 

If you'd like to find out how to do this with DFSORT, visit the following
Web page:

http://www.storage.ibm.com/storage/software/sort/srtmacvt.htm

Frank L. Yaeger - DFSORT Team (Specialties: ICETOOL, OUTFIL, Y2K :-)
=> DFSORT/MVS is on the WWW at
http://www.ibm.com/storage/dfsort/

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/ Now offering spam-free web-based newsreading
```

#### ↳ Re: IEBGENER Question

- **From:** "chip ling" <ua-author-6589301@usenetarchives.gap>
- **Date:** 1998-04-29T12:18:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5bb8bdf2ea-p6@usenetarchives.gap>`
- **In-Reply-To:** `<353D7F58.A6B2F82F@mail-me.com>`
- **References:** `<353D7F58.A6B2F82F@mail-me.com>`

```

Kalpataru Barman wrote:
› 
› I want to copy a variable length QSAM file into one fixed
› length QSAM file using a batch JCL job. ( MVS/ESA or OS390 ).
› I tried IEBGENER, but it is giving trouble.
› [ I know in ISPF 3.3 copy, an alarm comes that data may be truncated.]

IEBGENER should do the work OK. Got to be something wrong with
your JCL.

Rgds,
Chip Ling
```

#### ↳ Re: IEBGENER Question

- **From:** "kalpa barman" <ua-author-17075535@usenetarchives.gap>
- **Date:** 1998-05-05T12:34:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5bb8bdf2ea-p7@usenetarchives.gap>`
- **In-Reply-To:** `<353D7F58.A6B2F82F@mail-me.com>`
- **References:** `<353D7F58.A6B2F82F@mail-me.com>`

```

Thanks to all the help. I did it using SORT - OUTFIL CONVERT option.

- Kalpa


Kalpataru Barman wrote:

› I want to copy a variable length QSAM file into one fixed
› length QSAM file using a batch JCL job. ( MVS/ESA or OS390 ).
› I tried IEBGENER, but it is giving trouble.
› [ I know in ISPF 3.3 copy, an alarm comes that data may be truncated.]
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
