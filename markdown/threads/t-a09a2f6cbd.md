[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# File Limitation

_3 messages · 3 participants · 1999-02_

---

### File Limitation

- **From:** "stcheong" <stcheong@mbox2.singnet.com.sg>
- **Date:** 1999-02-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<796ado$pm1$1@mawar.singnet.com.sg>`

```
It had been more than a month since I encounter the error code 34,01 in
RM/COBOL-85.
During this period, I have
a.    increase the disk block size from 1024 to 4094 so that the file would
be able to grow bigger.
b.    perform a reorganisation of the old file to the new disk.
c.    I had get my hardware vendor to increase the hard limit of my
ystem( which runs on ATT Unix System V) to 0x70000000 and my soft limit of
the system from 4194304 to 8192000.
d.    when I re-run my Month End Program, I alway stop at 1.07GB. It alway
stopped at the same byte size.
I believe that there are some setting in the unix system that restrict the
size of my file to 1.07GB but my vendor seems to run out of idea on how to
proceed from here.
If I multiple 4194304 * 256, I end up with the byte size 1073741824. This is
where it stopped.
Can some expert out there able to offer some form of fruitful advice?
Thank You.
```

#### ↳ Re: File Limitation

- **From:** "Jeff" <a@a.com>
- **Date:** 1999-02-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<i1St2.2452$fz.8417932@storm.twcol.com>`
- **References:** `<796ado$pm1$1@mawar.singnet.com.sg>`

```

>Can some expert out there able to offer some form of fruitful advice?
>Thank You.


Never used a UNIX system to do COBOL, but here is my uninformed guess.

Under MVS I have run into a similar problem and it was due to the number of
extensions of the file. Under MVS when a file is allocated there is a
primary and a secondary allocation amount. When the file is first allocated
the primary amount is used. When the that primary extension is exhausted,
extension allocations are added to the file in the secondary increment. This
can be done up to 16 times. Thus this may be your problem. There may be a
similar secondary allocation setting on your system.

The block size you mentioned, doesn't seem quite right. Increasing block
size should be dependant on the disk drive unit being used, not simply
increasing it. All disk units I have used had a block size of somewhere
around 27000. I believe you need to determine this before re-sizing your
block size.

If all else fails, run the report to a tape drive then determine the actual
file size. Then copy it back to the disk drive forcing it to an appropriate
block size.

That is just my uninformed opinion. I may be wrong.
```

#### ↳ Re: File Limitation

- **From:** Chris Carroll <ccadmin@idis.com.au>
- **Date:** 1999-02-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36BC53FA.7CCF@idis.com.au>`
- **References:** `<796ado$pm1$1@mawar.singnet.com.sg>`

```
On Unix, 2 Gig is the limit as I recall.
You'll more than likely end up splitting the file up into 2, 4, etc
hunks and have an I/O handler program routine to cater for a huge file.
Why you have a 1 Gig limit I don't know but this I suspect to be a Unix
setup issue as you suggest. Another trick is to try the COMMIT command
during processing, say after every record, 10,000 records or what you
feel is reasonable.    
Personally, I'd give AT&T a rev up and get some support that I'm sure
you're already paying for.
Chris.

stcheong wrote:
> 
> It had been more than a month since I encounter the error code 34,01 in
…[16 more quoted lines elided]…
> Thank You.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
