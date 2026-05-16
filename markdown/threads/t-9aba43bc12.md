[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# URGENT - Error 114 (Signal 11)

_3 messages · 3 participants · 2002-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### URGENT - Error 114 (Signal 11)

- **From:** cstrm@yahoo.com.br (Wueislly)
- **Date:** 2002-05-07T12:24:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1717d0ac.0205071124.64f0f0ff@posting.google.com>`

```
Hi,

I need some help with an error that I'm receiving in cobol.

Well, first some information about the system:

Cobol/HP-UX HP35326 B.13.26
V4.1 revision 10 build 10/10/2 G; 33697. Run Time System
OXUPR/BMB/013260

I'm running a C program that calls a Cobol program and this cobol
calls many other cobol programs and c programs ...
The error is:

Execution error: file 'blbn_olnrc'
error code: 114, pc=0, call=1, seg=0
114 Attempt to access item beyond bounds of memory (Signal 11)

This error is not occuring every time, sometimes when it occurs and we
try to run again with the same data it finish successfully.

Anyone knows what can cause this type of error ?

Thankx
Wueislly
```

#### ↳ Re: URGENT - Error 114 (Signal 11)

- **From:** "kurimao" <kelpogs@singnet.com.sg>
- **Date:** 2002-05-10T23:23:52+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<abgomm$8g1$1@dahlia.singnet.com.sg>`
- **References:** `<1717d0ac.0205071124.64f0f0ff@posting.google.com>`

```
Hi,
In the OS/390 environment, we use to get the same error but flagged as
U4038. This is usually
caused by tables being accessed beyond it's max occurence. Try checking some
file data
being loaded into the tables without bounds-checking.

Hope this helped you a little.

"Wueislly" <cstrm@yahoo.com.br> wrote in message
news:1717d0ac.0205071124.64f0f0ff@posting.google.com...
> Hi,
>
…[22 more quoted lines elided]…
> Wueislly
```

#### ↳ Re: URGENT - Error 114 (Signal 11)

- **From:** "Reason" <steveno@nocfs.com.au>
- **Date:** 2002-05-13T14:08:22+10:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x%GD8.15$t06.2080@nsw.nnrp.telstra.net>`
- **References:** `<1717d0ac.0205071124.64f0f0ff@posting.google.com>`

```
Possible causes from my experience:
- A runaway index in Cobol.
- A bug in the C program.
- Wrong parameter or parm sequence.

"Wueislly" <cstrm@yahoo.com.br> wrote in message
news:1717d0ac.0205071124.64f0f0ff@posting.google.com...
> Hi,
>
…[22 more quoted lines elided]…
> Wueislly
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
