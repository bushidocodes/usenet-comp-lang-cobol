[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Variable vs. fixed length - tuning question

_5 messages · 5 participants · 1997-08_

---

### Variable vs. fixed length - tuning question

- **From:** "ta..." <ua-author-37821@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19970804193701.PAA24836@ladder01.news.aol.com>`

```

I am currently trying to tune a rather massive COBOL system. Massive in
terms of the amount of data passed from program to program. File sizes are
in the hundreds of gigabytes.

After lining up all the usual tuning suspects we are still left with some
staggering processing times. Consequently, I am still looking for any
extra speed I can wring out of the system. I have never seen it discussed
in tuning terms, but I was wondering:

Is it faster to process a variable length file or a fixed length file?
(For argument's sake, let's say the file in question averages 500 bytes
per record as a variable file and would be 1000 bytes per record if it
were fixed)

I am sure there is much additional overhead encountered with variable
length files in terms of reading the file header and each RDW (record
descriptor word), but is this offset by the smaller file size and
resultant cache read benefits?

If anyone can share any experiences I would be greatful.

Kevin
```

#### ↳ Re: Variable vs. fixed length - tuning question

- **From:** "wds" <ua-author-1064034@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0df6bd5a61-p2@usenetarchives.gap>`
- **In-Reply-To:** `<19970804193701.PAA24836@ladder01.news.aol.com>`
- **References:** `<19970804193701.PAA24836@ladder01.news.aol.com>`

```

Tao36 wrote:
› 
› I am currently trying to tune a rather massive COBOL system. Massive in
…[20 more quoted lines elided]…
› Kevin

This concerns issues that are rather dependent on the individual
implementation. First, each vendor decides how it will implement
variable length records, and each individual hardware configuration will
have its own influence (disk speed, cache sizes, channel load, etc.).

In a general sense, it is likely that variable length records will
require more CPU resources than will fixed length records, but will use
less disk space. It is also likely that variable length records will
not allow you to benefit much from increasing the blocking factor as a
means of reducing disk accesses, and some implementations will actually
either result in increased overhead (to manage record
blocking/deblocking) or prohibit variable length records from being
blocked.

The issues of blocking factor and record size will depend on the actual
hardware (and interfaces) used to store the data. The resulting access
speed will depend on such things as number of bytes per sector, number
of sectors per physical disk read/write, number of bytes per record,
number of records per block, cache size/speed, cylinder size and
organization, etc. There are no absolute rules that will apply to all
hardware.

Another consideration regarding blocking is whether the most used access
to the data is sequential or random. Also related to this will be
whether multiple users/processes access the data simultaneously. For
these two things, random access and multiple/concurrent access both tend
to mitigate any benefits of blocked records, and they also tend to
increase overhead involved with variable length records.

All that being said, the overall trend is likely to be that blocked,
fixed length records will result in improved performance at the expense
of increased disk space and memory usage. Obviously, any extreme values
could skew this (such as 10 byte average records with 10,000 byte
largest (or fixed size) records).

In an application using files as large as you describe, it would likely
benefit you to test the alternatives using a small test program. You
may wish to time some known number (say 100,000) of typical record
accesses in a loop, both using fixed length records and using variable
length records. This could also be expanded to include variations on
block size, etc. Considering the size of the data, 100,000 records in a
test file is quite small, but it should be large enough to give you a
fairly good indication of what to expect. Unfortunately, this pretty
much a trial-and-error process from there.

I hope some of these ideas may help. Good luck with your system.

Reply Addr:-->WDavid dot Simon at atl dot frb dot org<--
-------------------De··y@Spa··r.Trasher----------------
```

#### ↳ Re: Variable vs. fixed length - tuning question

- **From:** "scottp4-remove..." <ua-author-2777696@usenetarchives.gap>
- **Date:** 1997-08-03T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0df6bd5a61-p3@usenetarchives.gap>`
- **In-Reply-To:** `<19970804193701.PAA24836@ladder01.news.aol.com>`
- **References:** `<19970804193701.PAA24836@ladder01.news.aol.com>`

```

ta··.@a··.com (Tao36) wrote:

› I am currently trying to tune a rather massive COBOL system. Massive in
› terms of the amount of data passed from program to program. File sizes are
…[13 more quoted lines elided]…
› 

Variable length record files, especially ones with more than one
variable element are absolute disasters for processing. A lot depends
on the reason for creating the file as variable in the first place but
seldom do you find any measurable benefits from file sizes and caching
that aren't destroyed by the additional file overhead to process the
records.

We had a lot of 'unsung' geniuses that coded everything as variable.
We had more 'occurs 0 to 12 times' files than I'd ever believed
possible, all in the name of 'saving space'. Unfortunately, if you
analyzed the files, the average number of occurrances was usually 10
or higher.

This was all based the extreme techniques the resident 'genius' had
developed for processing a customer master file that was so large that
it had to be broken into three pieces because of size limits of VSAM
files. There we legitimately needed to do everything we could just to
keep the file size within three sections. Splitting it into 4 pieces
was politically impossible. All the programmers were taught that
since this technique was good for the master file it was good for all
their files too. This, of course, was totally false. By the time I
arrived at this company this was this was the way they did all files.


Going back to the old VS-COBOL, I found that up to 60% of program
execution time would be in one COBOL service module ILBOVIO (I think)
that handled variable I/O. As far as I know, the way variable records
are handled has not significantly changed in the later products.
Converting some test applications (later production) so that the
needless variable length records were fixed length resulted in 80%
reduction in cpu time and almost halving i/o times.

You need to analyze the data and then take action. Some (but not
really that many) files are legitimately all over the place in size.
Most business processing I've encountered actually vary by very little
once the file matures. My rule of thumb was that if more than half
the file contained counts greater than half the number of occurrances
there was no point in making the file variable.

If you are passing the record to multiple programs, flatten it out in
the working storage of the module doing the I/O that using a copy
member that doesn't have the depending on option. Don't try to
convert it to variable again until you are ready to rewrite it.

If you have any specific questions, you are welcome to contact me
directly.

Scott Peterson
```

#### ↳ Re: Variable vs. fixed length - tuning question

- **From:** "john m. saxton, jr" <ua-author-17071440@usenetarchives.gap>
- **Date:** 1997-08-04T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0df6bd5a61-p4@usenetarchives.gap>`
- **In-Reply-To:** `<19970804193701.PAA24836@ladder01.news.aol.com>`
- **References:** `<19970804193701.PAA24836@ladder01.news.aol.com>`

```

Tao36 wrote:
› 
› I am currently trying to tune a rather massive COBOL system. Massive in
…[20 more quoted lines elided]…
› Kevin
You don't mention the access method, though it may or may not make that
much difference anyway. Based on some of the terms in the email, I am
assuming an IBM Mainframe platform.

I don't think you will see a significant savings to use variable length
records. In fact the extra overhead to handle the records may increase
process time.

Are you using VSAM or DB2 or some forced sequential access method like
QSAM. Is your application processing each file sequentially or can your
application benefit from using random reads?
Return address is John underscore Saxton at ML dot com
```

#### ↳ Re: Variable vs. fixed length - tuning question

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-08-04T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0df6bd5a61-p5@usenetarchives.gap>`
- **In-Reply-To:** `<19970804193701.PAA24836@ladder01.news.aol.com>`
- **References:** `<19970804193701.PAA24836@ladder01.news.aol.com>`

```

ta··.@a··.com (Tao36) wrote:

snip>
› Is it faster to process a variable length file or a fixed length file?
› (For argument's sake, let's say the file in question averages 500 bytes
…[3 more quoted lines elided]…
› Kevin

If you are compute bound go fixed. If you are i/o bound go variable.

Try a small file for testing....

JR



and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
