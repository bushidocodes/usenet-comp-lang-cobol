[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Record Length Inconsistency - Cause of corruption unknown

_7 messages · 5 participants · 2000-01_

---

### Record Length Inconsistency - Cause of corruption unknown

- **From:** Mark Fletcher <spanna2000@my-deja.com>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<865586$km0$1@nnrp1.deja.com>`

```


We have reports of a problem which we find very difficult to understand.

A MicroFocus COBOL/2 (V1.3) for SCO Unix compliled application has been
running happily for years but we receive reports a random key length
inconsistency errors at which point the file is unusable until the data
element is re-sorted.

The error is caused by the random insertion of records intended for
other files. E.g. We have an indexed file which holds the menu
structure. The file is static once installation has been completed,
only a licence upgrade or addition of a new module will change this
file. After months of operation without software change the customer
reported a 3,9 error on the file (record length). On investigation we
find that a record intended for a work file (also indexed) has been
written in the *middle* of the data part of the menu file.

To my knowledge you can't do this manually with COBOL. Therefore we're
ruling out application coding errors.

Currently we suspect a) the compiler was not intended for use on
OpenServer machines - perhaps this is the reason, b) the RTS system has
a flaw and is misbehaving, c) the hardware is faulty.

c has been ruled out because it's happening on all kinds of kit. a & b
are still on the suspect list.

Has anyone else experienced similar? The compiler and RTS are now
ancient retired products. Converting to a supported version of the
compiler means code changes to make the product work with the new
version. I think we're going to have to do this (and quite look forward
to using some newer tools) but I don't want to commit customers to the
RTS upgrade costs if there is an alternative solution.

Any ideas?
```

#### ↳ Re: Record Length Inconsistency - Cause of corruption unknown

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 2000-01-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<866b4e$485$1@ssauraaa-i-1.production.compuserve.com>`
- **References:** `<865586$km0$1@nnrp1.deja.com>`

```
    How about makeing certain that all opens are input (No open IO), and
flagging
the file(s) read only.  When upgrading, unflag.

    If it still happens, and the file is still read only, than what -
operating system?




"Mark Fletcher" <spanna2000@my-deja.com> wrote in message
news:865586$km0$1@nnrp1.deja.com...
>
>
…[42 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Record Length Inconsistency - Cause of corruption unknown

- **From:** Mark Fletcher <spanna2000@my-deja.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<867elp$a6v$1@nnrp1.deja.com>`
- **References:** `<865586$km0$1@nnrp1.deja.com> <866b4e$485$1@ssauraaa-i-1.production.compuserve.com>`

```
The error is picked up when the file is opened (of course) so there is
no mileage in reworking the io of the corrupted file - I don't think I
mentioned that the corrupted file appears to be random - The process
that is corrupting the file is presumably happening somewhere else in
the application and its not practical to make all those processes read
only.

The problem is certainly low level. (RTS, OS or HW)

I'm hoping someone else has seen this and can throw us a lifeline.

Rgds


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Re: Record Length Inconsistency - Cause of corruption unknown

- **From:** dxmixxer@netdirect.net (Douglas Miller)
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9QFh4.517$Rw3.10786104@news.netdirect.net>`
- **References:** `<865586$km0$1@nnrp1.deja.com>`

```
In article <865586$km0$1@nnrp1.deja.com>, Mark Fletcher <spanna2000@my-deja.com> wrote:
>
>
…[14 more quoted lines elided]…
>written in the *middle* of the data part of the menu file.

Possibly cross-linked files? Perhaps a corrupted disk directory erroneously 
associates the same physical area of disk with two or more files.
```

#### ↳ Re: Record Length Inconsistency - Cause of corruption unknown

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KDNh4.260$JB.3679@nnrp2.rcsntx.swbell.net>`
- **References:** `<865586$km0$1@nnrp1.deja.com>`

```

Mark Fletcher <spanna2000@my-deja.com> wrote in message
news:865586$km0$1@nnrp1.deja.com...

We've seen (very rare) a bad disk controller card (or bad disk with
built-in controller) slinging trash to random places on the disk.
```

#### ↳ Re: Record Length Inconsistency - Cause of corruption unknown

- **From:** "Rick Price" <rick@hpd.co.uk>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<866j5a$7r7$1@starburst.uk.insnet.net>`
- **References:** `<865586$km0$1@nnrp1.deja.com>`

```
Are any files really large?   Unix using the standard I/O can only handle
files <= 2GB.

Maybe your versions of MF Cobol thinks it can handle larger files.   An old
manual here said something like 'no limit on unix file sizes',  which fooled
us until we started getting problems on large files.

I'm wondering if the MF Cobol thinks its updating an area in one file but
that area belongs to another?

However you mention a work file.   I guess its unlikely for a work file to
get really large.

Rick

Mark Fletcher <spanna2000@my-deja.com> wrote in message
news:865586$km0$1@nnrp1.deja.com...
>
>
…[42 more quoted lines elided]…
> Before you buy.
```

##### ↳ ↳ Re: Record Length Inconsistency - Cause of corruption unknown

- **From:** Mark Fletcher <spanna2000@my-deja.com>
- **Date:** 2000-01-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<867eov$a83$1@nnrp1.deja.com>`
- **References:** `<865586$km0$1@nnrp1.deja.com> <866j5a$7r7$1@starburst.uk.insnet.net>`

```
The files aren't really that large. The whole database is rarely >1Gb.

There could be something in your suggestion though. OpenServer
introduced larger file size limits.


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
