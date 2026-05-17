[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SORT VERB vs separate sort

_3 messages · 3 participants · 1996-04_

**Topics:** [`VSAM, files, sorting`](../topics.md#files)

---

### SORT VERB vs separate sort

- **From:** "don nelson" <ua-author-20234@usenetarchives.gap>
- **Date:** 1996-04-25T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<31814A1E.23E7@tandem.com>`

```

› An application prgm uses memory that might be used to build longer
› sort strings and speed up the sort.

This depends entirely on the system and on what is being sorted. On
some systems the sort uses completely different memory (and
processor(s)). There is absolutely no difference on these systems
between a standalone and embedded sort when you are sorting from one
file and writing to another (or to the same one). Tandem is one of
these systems.

› A large standalone sort (slightly faster) preceeded and followed by
› applications cause data files to be passed an extra time per
› application and use extra file space.

I agree on this except the slightly faster part. The big advandage of
the embedded sort is that the output can be passed directly to the
program without going through a file (OUTPUT PROCEDURE IS ...). The
same can be said for the input data (INPUT PROCEDURE IS ...).

It is always amazing that various COBOL verbs are considered to be bad
or some such because of the vagarities of one specific implementation
(usually IBM).

Don Nelson
```

#### ↳ Re: SORT VERB vs separate sort

- **From:** "mor..." <ua-author-4892761@usenetarchives.gap>
- **Date:** 1996-04-27T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5ac49c6a8d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<31814A1E.23E7@tandem.com>`
- **References:** `<31814A1E.23E7@tandem.com>`

```

I started on IBM mainframes when my company had a 32k model 30
with a COBOL that didn't have a SORT verb. The reason that SORT had a
bad reputation in the mainframe environment was that in the
earlier years you were dealing with real memory machines, not virtual
and the amount of memory available for sorting was very limited if
there was also application code in the region. Our DOS
partitions started at 16K and we though we had gone big time when they
increased to 26K and then 46K when we got a 128K machine. When we
switched to MVT, a normal processing region was 100K. Now on MVS the
buffering for one file takes more memory than that. The advent
of large memory spaces with adequate and reasonably priced real
storage to back those spaces allowed the COBOL sort to become as
efficient as doing a standalone SORT or more so. Given that sorting
is real memory intensive, it took the advent of large memory spaces to
enable program invoked sorts to be efficient. I might add that I
consider it a sad commentary on the arcanity of our tools that IBM
batch sorting is dependent on statements such as SORT
FIELDS=(3,2,CH,A,10,4,PD,D) that will blow up if the record
description changes (or worse, give wrong results). Of course, the
previous statement gives absolutely no clue as to what fields are
being sorted. Think of the implications for shops that want to go
from 2 digit years to 4 digit years and do a lot of sorting on
dates.

›› A large standalone sort (slightly faster) preceeded and
›› followed by
…[12 more quoted lines elided]…
› Don Nelson


Clark F. Morris, Jr. - CFM Technical Programming Services
RR#1, 1339 Clarence Road, Bridgetown, Nova Scotia B0S 1C0
cmo··.@fox··n.ca
On assignment in St. John, New Brunswick
mor··.@nbn··b.ca
```

##### ↳ ↳ Re: SORT VERB vs separate sort

- **From:** "awar..." <ua-author-17086507@usenetarchives.gap>
- **Date:** 1996-04-28T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-5ac49c6a8d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-5ac49c6a8d-p2@usenetarchives.gap>`
- **References:** `<31814A1E.23E7@tandem.com> <gap-5ac49c6a8d-p2@usenetarchives.gap>`

```

Here's my take on Internal vs External Sorts under IBM MVS..
The correct choice is situational - it depends on what you are doing.

At my shop ...
COBOL invokes the same Sort software that JCL does.
Sort I/O is faster/better than COBOL I/O because the Sort uses EXCP type
I/O in track/cylinder sized chunks. Standard COBOL can't do this.
Using/Giving options invoke Sort I/O routines and thus show no performance
change over the external sort.

So, for us, the question comes down to the types and amounts of pre/post-
processing required. If we are using large records to drive a simple report,
then we improve performance by filtering the fields. We use the Input
Procedure to read long, 4K+ bytes, records and reformat them into short ones.

Extremely large files with little filtering often benefit from the Internal
Sort because we save two passes of the file.

<-External Sort-> <-----------COBOL Program------------>
Read->Sort->Write Read->Process->PrintCustomerStatements

<----------------------Internal Sort in COBOL Program--------------------->
Read->ReleaseToSort->Sort->ReturnFromSort->Process->PrintCustomerStatements

The Sort Release/Return verbs do not write to disk. Release passes the
record to the Sort Phase; Return receives the record from the last pass of
the String Merge Phase.

****************************************************************************
* Andy W. Arnold * Clever If *
* Falls Church VA * Quote I *
* * Goes Hear *
* awa··.@cp··g.org * Here One *
****************************************************************************
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
