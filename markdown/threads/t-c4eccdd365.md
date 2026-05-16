[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RM/Cobol-85 and Windows NT

_2 messages · 2 participants · 1999-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### RM/Cobol-85 and Windows NT

- **From:** linalm@ibm.net
- **Date:** 1999-05-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7hpges$lq7$1@nnrp1.deja.com>`

```
Hi there!

We have been working with RM/Cobol-85 for a long time and now we are
facing a problem that we don't understand. We wonder if any one of you
have had a similar problem or can give us ideas about what it can be
causing the problem and how we can solve it. Thanks in advance for your
time and comments. Here is the description of the situation:

The program with the problem is run by an application that handles
about 80 different files, most of them being indexed. By the time the
program is executed, approximately 15 files are already opened. The
program opens 30 files, 15 of which are opened in I/O mode. One of
those files, the main one that is used in the process, has 22 keys, 640
bytes per record, and approximately 5 megabytes in total disk space.
The program can be executed either under Unix or under Windows. When
the program is executed under UNIX, everything works fine, and when we
run it under Windows, the performance is terrible, processing time
increase over 10 times the time we get under UNIX! ! . The user has
Windows 95 on his workstation and Windows NT as the software for the
network. The Windows NT is optimized. To alleviate the problem a little
bit, we have moved the files to another disk and that has helped for
just a few days, then, everything goes back to a bad performance. Since
the same program with the same data, works very well under UNIX and the
Windows NT is optimized, we don�t really know what it can be causing
the problem and how we can solve it. The machine where the software
runs under Windows is a Compaq proliant 1600 Pentium II with 450 MHz,
192 Megabytes RAM, raid 5 disks and a total of 27 gigabytes in disk
space.

We think that the problem can be with the NT, due to some restrictions
that may apply and we don�t know. Does anyone of you have any idea or
knows something about problems executing a RM/Cobol-85 program under
Windows NT 4.0? The RM/Cobol version we use is 6.5.

Thanks very much.

Lina Maria Londono




--== Sent via Deja.com http://www.deja.com/ ==--
---Share what you know. Learn what you don't.---
```

#### ↳ Re: RM/Cobol-85 and Windows NT

- **From:** Gerald Logan <loganj@bellsouth.net>
- **Date:** 1999-05-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<374D924F.20A0F97A@bellsouth.net>`
- **References:** `<7hpges$lq7$1@nnrp1.deja.com>`

```
The problem is most likely due to doing file i-o across the network.  Where
do the files actually reside?  I suspect that the files are on the unix
server where the cobol does not have to go across the network to retrieve
the data.  When running under windows each i-o to the file has to transfer
the data across the network before the program can do anything with it.

linalm@ibm.net wrote:

> Hi there!
>
…[37 more quoted lines elided]…
> ---Share what you know. Learn what you don't.---
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
