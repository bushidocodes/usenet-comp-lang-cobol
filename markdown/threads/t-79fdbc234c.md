[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# variable record-length in COBOL

_1 message · 1 participant · 2000-12_

---

### Re: variable record-length in COBOL

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 2000-12-09T15:13:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<90u3pd02mh1@enews3.newsguy.com>`
- **References:** `<8vqg13$mmn$05$1@news.t-online.com> <90aoeq$2am$1@nnrp1.deja.com> <3A2BA4FA.CB89CCDA@brazee.net> <lm9X5.7426$2P3.548626@bgtnsc06-news.ops.worldnet.att.net>`

```
Let's not forget that some environments have compression.

So if I have a 1500 byte fixed length record, but only use, on average, 80
bytes of that record, the rest of the record has some arbitrary values.
Like low values or spaces.

In our OS390 environment, at least when I write to tape, CA-1 compresses the
data (COMP=TRTCH).  So it may seem wasteful to use a fixed length record in
a situation like this, but in reality it is highly efficient.

In some instances, it may be helpful to use RECFM=VB.  For instance, weekly
our shop pulls back a 3 gigabyte (total) file from our stores.  This file
originates from a PC based environment (4690 OS) that produces variable
length records.  It is pulled back from the stores, then concatenated on one
of our SP nodes.  But we want the data stored on the mainframe.  At times,
our shop does not have 3 gigabytes readily available (mostly because of our
15 extent per volume, 3 volume standard; you know the drill, request too
much space and no volumes get selected, request too little and you go past
15*3 extents).  And I can't write to tape, because our FTP2 does not support
it (AFAIK).  So, by using RECFM=VB, I can get the FTP job to run more
reliably and use less space.  Obviously after the file is FTPed, I make a
fixed length dataset on tape and uncatalog the DASD space.

Of course, there are certainly better ways to go about the above example.
Why not pull back one file per store and keep them as seperate datasets
(instead of one 3-gig dataset).  This was certainly contemplated.  But we
didn't have the time to write some dynamic allocation stuff to do the
FTPing.  Plus one file is easier to manage than 184 files.  So at the time,
the one 3-gig file was a better choice.  By going to RECFM=VB, I was able to
make it work.

So this goes full circle back to the point that there are always many
different ways to do something.  As long as it is reliable, clear and
reasonably speedy than there's nothing wrong with doing something a certain
way.  In some cases, variable length records may be the best way to do
something.

Jeff
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
