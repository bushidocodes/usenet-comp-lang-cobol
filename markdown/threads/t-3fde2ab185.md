[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# how to optimise VSAM KSDS file : Space and I/O

_7 messages · 7 participants · 1999-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### how to optimise VSAM KSDS file : Space and I/O

- **From:** "gritche" <gritche@france-mail.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<7ffqms$aqa$1@front3.grolier.fr>`

```
Help me please !!!

Sorry for my english. I'm french
I hope you will understand my questions!

We have a VSAM KSDS file (variable length) which is used as a
"log file" for our apllications (CICS the day and BATCH the night)
The length is variable (from 134 to 4000 byte).
key is 60 byte length
Usually we have about 3000 records daily and no problem with R/W.
(we use also BLSR)

This week a job will run and will do about 1 Million "add" record in this
file.
300 000 records of 580 bytes
300 000 records of 1580 bytes
440 000 records of  380 bytes
300 000 records of 150 bytes.

My questions are :
1- what are the best parameters  "idcams" to minimize the space occupied by
this file ?
2- what are the best parameters "BLSR" to minimise the I/O and reduce the
time of this job ?

or where can i find "formulas" to determine these parameters?

Thanks
```

#### ↳ Re: how to optimise VSAM KSDS file : Space and I/O

- **From:** wthompson@my-dejanews.com
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<7fg29g$trl$1@nnrp1.dejanews.com>`
- **References:** `<7ffqms$aqa$1@front3.grolier.fr>`

```
Generally the answer is in your need for recoverability.  A high degree of
recoverability would mandate smaller CIs and update/insert mode processing.
Less recoverability could allow larger CIs and mass insert/load mode
processing.

If you could avoid the requirement of having the file keyed at load time, you
could just flat file it out and sort it into load after the day's (or week's)
processing.  This would enhance thruput.

Last time I looked, the rule-of-thumb was large allocations of data CIs, even
numbers up to (one or two) CAs in length and as many index CIs as you have (or
expect) in the index (including and expecially the highest and intermedate
levels).


>
> This week a job will run and will do about 1 Million "add" record in this
…[12 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

##### ↳ ↳ Re: how to optimise VSAM KSDS file : Space and I/O

- **From:** "Joel C. Ewing" <jcewing@acm.org>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<371BFBE9.2AF70D00@acm.org>`
- **References:** `<7ffqms$aqa$1@front3.grolier.fr> <7fg29g$trl$1@nnrp1.dejanews.com>`

```
CI size should be chosen based on how the KSDS will be used after it is
created, not on recoverability.  Should you have a major
hardware/software disaster during the creation process using large
number of buffers, the asynchronous nature of the physical writes means
you have an unpredictably large number of CI's in doubt, not just a
single CI; and the only way to have complete confidence in you file
would be to rebuild, regardless of CI size.  Predominantly random access
would probably favor a 4K CISIZE, while a majority of sequential or
skip-sequential access would perhaps favor a 8K or 16K CISIZE.

The total amount of data involved appears to be around 0.8 GB, so unless
you are talking about an Extended Format file (which allows going over 4
GB), you are either talking about replacing a very significant portion
of the file, or possibly building a completely new file from scratch. 
In either case, a general ROT is that sequential update techniques
(placing records to be retained along with records to be added into a
flat file, doing an external sort on the key field, and then loading an
empty KSDS with the sorted records) can outperform doing the adds via
random updates even if as little as 5% of the records are being
replaced/added, and in your case the percentage would appear much higher
than 5%.  Adding the equivalent of 25-100% of the file randomly, even
with many buffers, even with Batch LSR, you cannot avoid an incredible
number of CI/CA splits, which will greatly add to the overhead of the
process.  Loading these records into an empty file in sorted order would
also eliminate the need or rationale for specifying any CI/CA free space
and minimize the space required by the file.

BLSR is optimized for random access and does not transfer multiple CI's
per I/O.  Doing the updates randomly using BLSR buffering, requesting
DEFERRED WRITE, and supplying enough INDEX and DATA buffers will at best
give you one physical write for each INDEX and DATA CI.  For sequential
updates, BLSR performs more poorly than standard BUFNI BUFND buffer
techniques.  If building the file sequentially,  with sufficient buffers
for your input flat file and sufficient DATA buffers for the KSDS file,
the build can be done with as little as one write per INDEX CI and one
write for all DATA CI's in the same CA  -- considerably less MVS
overhead and probably less DASD time as well.

If you have no choice but to perform these updates randomly, then the
large number of updates pretty much makes any defined FreeSpace values
irrelevant -- you would need to plan on allocating at least twice as
much space as the number of records would suggest, and should consider
reorganizing the file after the update process if a significant number
of records will be accessed afterwards.

Tuning considerations for subsequent reading of the file after its
creation are a separate issue (i.e, if the creation and usage of the
file are two separate phases in a single program, different DDNAMEs
should be referenced to permit different tuning techniques for each type
of usage).

wthompson@my-dejanews.com wrote:
> Generally the answer is in your need for recoverability.  A high degree of
> recoverability would mandate smaller CIs and update/insert mode processing.
…[29 more quoted lines elided]…
> http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: how to optimise VSAM KSDS file : Space and I/O

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fgr2a$3ju@dfw-ixnews4.ix.netcom.com>`
- **References:** `<7ffqms$aqa$1@front3.grolier.fr>`

```
This is a question that would probably get a better answer in
     bit.listserv.ibm-main

Many of the comp.lang.cobol newsgroup participants are quite familiar with
VSAM, but I think you would get the best "performance tuning" information
from the IBM-MAIN group.
```

#### ↳ Re: how to optimise VSAM KSDS file : Space and I/O

- **From:** "Sarah W" <sworspamblk@erols.com>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<01be8b41$c4815d20$d704938c@mmga1127.loc.gov>`
- **References:** `<7ffqms$aqa$1@front3.grolier.fr>`

```
You don't say what your keys are.  Here's something to think about:

If your records will be presented to the process adding to the file in
ascending key sequence (for example, if your log records have date and time
as their primary key) then if you use normal one-at-a-time add processes,
you will end up needing at least 4 times the amount of space that the
records will occupy (probably more) because of the CI and CA split
processes.  When a CI or CA gets full, VSAM will split it and  leave about
half of the split CI or CA empty to accommodate future adds.  But if your
keys only go up, the unused space that was left will remain empty until the
cluster is reorganized.  

Good luck,

Sarah W.
```

#### ↳ Re: how to optimise VSAM KSDS file : Space and I/O

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<371C80BB.CC6681D4@zip.com.au>`
- **References:** `<7ffqms$aqa$1@front3.grolier.fr>`

```
gritche wrote:
> 
> Help me please !!!
> 
> This week a job will run and will do about 1 Million "add" record in this
> file.

The non-obvious answer.

Don't use VSAM directly:

Create sequential file,
unload VSAM cluster
reload VSAM cluster from sorted version of unload and sequential
file.  No VSAM insertions and very tidy VSAM cluster for the next
day.

Good if it can work this way,
Ken
```

#### ↳ Re: how to optimise VSAM KSDS file : Space and I/O

- **From:** wtsquid@my-dejanews.com
- **Date:** 1999-04-20T00:00:00
- **Newsgroups:** bit.listserv.cics-l,comp.lang.cobol
- **Message-ID:** `<7fi6vc$qnj$1@nnrp1.dejanews.com>`
- **References:** `<7ffqms$aqa$1@front3.grolier.fr>`

```
All the responses I have read are excellent options and alternatives,
especially handling the data sequentially rather than randomly. However, if
randomly is your only processing method, try "pre-formatting" your data space
to reduce your CI and CA splits. You must know a good deal about your keys
and insertions, so that you can estimate the number of records and range of
keys to be uniformly added to your file.

The least complex method is to process sequentially.

Good Luck.


In article <7ffqms$aqa$1@front3.grolier.fr>,
  "gritche" <gritche@france-mail.com> wrote:
> Help me please !!!
>
…[27 more quoted lines elided]…
>

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
