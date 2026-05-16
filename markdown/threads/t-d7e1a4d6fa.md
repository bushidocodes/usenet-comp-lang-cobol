[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help with regard to VSAM file open error RC=39

_4 messages · 3 participants · 2002-03_

**Topics:** [`VSAM, files, sorting`](../topics.md#files) · [`Help requests and how-to`](../topics.md#help)

---

### Help with regard to VSAM file open error RC=39

- **From:** arunprasath420@yahoo.com (Arun Prasath)
- **Date:** 2002-03-08T08:14:20-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3ef804e.0203080814.9ab0290@posting.google.com>`

```
Hi all,

i tried to open a vsam file in a cobol program, but got an open error
message with the file status flag as 39.
On browsing the vsam file using file aid, i found that some key values
had some spaces in them at the end of the key value(some 5 records out
of 5000 had this). However, when i deleted these 5 records and ran the
job, it ran good.

Can anyone explain, how the program threw an open error when there
should have been a read error.

Thanks in advance,
Arun Prasath
```

#### ↳ Re: Help with regard to VSAM file open error RC=39

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2002-03-08T11:39:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a6at00$nlg$1@nntp9.atl.mindspring.net>`
- **References:** `<a3ef804e.0203080814.9ab0290@posting.google.com>`

```
File status of 39 is a "fixed attribute conflict". My guess (and it is only
a GUESS) is that those records (with the spaces at the end of the key)
actually had keys LONGER than that specified in your program's description
of the file.  When those records were removed, the file then had only keys
that matched the SIZE of what you specified in your program.

Other possibilities exist - depending on exactly HOW you deleted the "bad"
records.  It is possible that in the process of deleting them (possibly via
File/AID) you managed to "correct" some other problem in the "fixed
attribute" information for that file.
```

##### ↳ ↳ Re: Help with regard to VSAM file open error RC=39

- **From:** arunprasath420@yahoo.com (Arun Prasath)
- **Date:** 2002-03-11T09:21:56-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a3ef804e.0203110921.e70ff1d@posting.google.com>`
- **References:** `<a3ef804e.0203080814.9ab0290@posting.google.com> <a6at00$nlg$1@nntp9.atl.mindspring.net>`

```
Hi William,

Thanks for the tip. I tried to run the job again with the same type of
'corrupt' records but with fewer records and it ran fine.

Also i discovered a new message in the spool for the last time the job
abended The message was :
R005 FXI030DS INDD - VOLUME COUNT FOR DD EXCEEDED:SPECIFIC- 10
NON-SPECIFIC- 108

,although this step ran with return code 0(this step runs befor the
step where the abend occurs). Could this message be in anyway
connected to the abend.

"William M. Klein" <wmklein@ix.netcom.com> wrote in message news:<a6at00$nlg$1@nntp9.atl.mindspring.net>...
> File status of 39 is a "fixed attribute conflict". My guess (and it is only
> a GUESS) is that those records (with the spaces at the end of the key)
…[27 more quoted lines elided]…
> > Arun Prasath
```

###### ↳ ↳ ↳ Re: Help with regard to VSAM file open error RC=39

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2002-03-12T21:26:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0203122126.3e64b41b@posting.google.com>`
- **References:** `<a3ef804e.0203080814.9ab0290@posting.google.com> <a6at00$nlg$1@nntp9.atl.mindspring.net> <a3ef804e.0203110921.e70ff1d@posting.google.com>`

```
Hi Arun,

Answering your 1st question. This takes me back a bit, but I seem to
remember that OPEN on input primes the buffers. So, it's possible to
get a "READ" type of error on OPEN.

BTW, the last error you encountered seems to indicate that you didn't
specify the correct number of volumes to contain the dataset. Don't
know how that can happen on input, since the OS keeps track of that.

Jack 


arunprasath420@yahoo.com (Arun Prasath) wrote in message news:<a3ef804e.0203110921.e70ff1d@posting.google.com>...
> Hi William,
> 
…[42 more quoted lines elided]…
> > > Arun Prasath
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
