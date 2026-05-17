[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# UNIX MF COBOL -- Tape I/O Via Byte-Stream Functions

_5 messages · 3 participants · 1995-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### UNIX MF COBOL -- Tape I/O Via Byte-Stream Functions

- **From:** "d..." <ua-author-14212488@usenetarchives.gap>
- **Date:** 1995-04-26T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3no60g$k49@access5.digex.net>`

```
I need to come up with a hopefully MF COBOL solution to the
need for COBOL programs on UNIX systems to be able to read
and write 9-track tapes in IBM mainframe formats, such as
FBS, V, VB, VS, VBS, U, etc. Many of these create tape
blocks of varying sizes. I do not see how the External
File Handler can be coerced into doing this and am looking
at the byte-stream functions. However, the CBL_READ_FILE
function does not return the number of bytes retrieved (!)
and the number of bytes requested at the end of a disk file
must exactly match the number of bytes remaining or an
error occurs. Does anyone have any ideas for solving this
problem without resorting to a C subroutine that will give
me access to read(2) and write(2)?

I requested CBL_READ_FILE be enhanced to provide the bytes
read datum a year ago but have heard nothing from them as
to when or if it will be implemented. You can't use
CBL_READ_FILE for piped files, either.
```

#### ↳ Re: UNIX MF COBOL -- Tape I/O Via Byte-Stream Functions

- **From:** "k..." <ua-author-17073840@usenetarchives.gap>
- **Date:** 1995-04-26T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a35aa18e0e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3no60g$k49@access5.digex.net>`
- **References:** `<3no60g$k49@access5.digex.net>`

```

In article <3no60g$k.··.@acc··x.net>, d.··.@acc··x.net (David L. Craig) writes:
› I requested CBL_READ_FILE be enhanced to provide the bytes
› read datum a year ago but have heard nothing from them as
› to when or if it will be implemented.

Have you been given a PDR reference number for this enhancement request ?
email me it, and I'll check to see what the status of the PDR is ....

› You can't use CBL_READ_FILE for piped files, either.

I believe (unofficially :)) that this may well be addressed with current
development.

Kev.

Kevin.			 Micro Focus, Newbury, UK.    (k.··.@mfl··o.uk)
These views are strictly my own.
I doubt very much that anyone else would want them.
```

##### ↳ ↳ Re: UNIX MF COBOL -- Tape I/O Via Byte-Stream Functions

- **From:** "d..." <ua-author-14212488@usenetarchives.gap>
- **Date:** 1995-04-30T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a35aa18e0e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a35aa18e0e-p2@usenetarchives.gap>`
- **References:** `<3no60g$k49@access5.digex.net> <gap-a35aa18e0e-p2@usenetarchives.gap>`

```
In article <3nof3a$i.··.@ice··o.uk>,
Kev Digweed wrote:
› 
› In article <3no60g$k.··.@acc··x.net>, d.··.@acc··x.net (David L. Craig) writes:
…[11 more quoted lines elided]…
› 
I never got any kind of a number for that particular request.

I gather the byte-stream functions map into stdio's fopen
family of functions, thus, I assume there is no way to
control the device level blocking through CBL_WRITE_FILE.
I don't know if a good enough case could be made for a set
of call-by-name functions that would map into open, close,
read, write, fcntl, etc.
```

#### ↳ Re: UNIX MF COBOL -- Tape I/O Via Byte-Stream Functions

- **From:** "fr..." <ua-author-6381038@usenetarchives.gap>
- **Date:** 1995-04-27T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a35aa18e0e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<3no60g$k49@access5.digex.net>`
- **References:** `<3no60g$k49@access5.digex.net>`

```
David L. Craig (d.··.@acc··x.net) wrote:
: I need to come up with a hopefully MF COBOL solution to the
: need for COBOL programs on UNIX systems to be able to read
: and write 9-track tapes in IBM mainframe formats, such as
: FBS, V, VB, VS, VBS, U, etc. Many of these create tape
: blocks of varying sizes. I do not see how the External
: File Handler can be coerced into doing this and am looking
: at the byte-stream functions. However, the CBL_READ_FILE
: function does not return the number of bytes retrieved (!)
: and the number of bytes requested at the end of a disk file
: must exactly match the number of bytes remaining or an
: error occurs. Does anyone have any ideas for solving this
: problem without resorting to a C subroutine that will give
: me access to read(2) and write(2)?

: I requested CBL_READ_FILE be enhanced to provide the bytes
: read datum a year ago but have heard nothing from them as
: to when or if it will be implemented. You can't use
: CBL_READ_FILE for piped files, either.

In other COBOLs under UNIX, I used the program to create or read binary
files on disk and used the UNIX utility dd to transfer them between
disk and tape. I found it difficult at best to try a direct approach.

Lawrence A. Free | Email: fr··.@m··.com
A.F.Software Services, Inc. | Your MS/DOS, UNIX
(708) 232-0790 | business software developer
```

#### ↳ Re: UNIX MF COBOL -- Tape I/O Via Byte-Stream Functions

- **From:** "d..." <ua-author-14212488@usenetarchives.gap>
- **Date:** 1995-04-30T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a35aa18e0e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<3no60g$k49@access5.digex.net>`
- **References:** `<3no60g$k49@access5.digex.net>`

```
In article <3nr496$c.··.@mar··s.com>,
Lawrence Free/ A.F. Software Services wrote:
›
› In other COBOLs under UNIX, I used the program to create or read binary
› files on disk and used the UNIX utility dd to transfer them between
› disk and tape. I found it difficult at best to try a direct approach.
›
You can go directly to tape when you read or write by
using the "Setting Up Pipes" feature discussed in the
chapter "External File-name Mapping" of the "System
Reference" manual. For example, given the code:

SELECT TAPEOUT ASSIGN "TAPE"

use the following Bourne shell code:

set DD_TAPE=">dd of=/dev/tape obs=32k"
export DD_TAPE

and your COBOL WRITEs are piped into a dd process
spawned when you OPEN TAPEOUT. dd blocks the byte-
stream at the obs value. My problem is that the
tape blocks of a VB file vary, so dd is unsuitable.
As there is no universal UNIX utility that creates
VB tape files, I am forced to use C unless Micro
Focus can pull a rabbit out of their generally
available hat.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
