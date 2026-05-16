[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cobol compressor

_2 messages · 2 participants · 2002-11_

---

### cobol compressor

- **From:** priolof@libero.it (Federico)
- **Date:** 2002-11-14T09:50:29-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<fd67e997.0211140950.6c85b7f0@posting.google.com>`

```
Hi, I have written a cobol compressor that uses huffman method to
reduce file.
It run fine and I am very satisfied of this program. 
Is there only a problem. To use it on all platform I have use only
cobol standard (bit algoritms are also performed). But when I read my
source file to compress it I must read it only a character for time
for binary file.
My fd is: 
fd file-input. 
01 rec-in. 
02 car pic x. 
and select is file-input organization is binary sequential. 

This is not very performant for my program that uses many times to
load the file.
Is there another method to run it faster ?. 

Thank you
```

#### ↳ Re: cobol compressor

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2002-11-16T05:51:36-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0211160551.498a838b@posting.google.com>`
- **References:** `<fd67e997.0211140950.6c85b7f0@posting.google.com>`

```
Organization Binary Sequential I have seen only when using AcuCOBOL -
is that your compiler?  If so, look at the C$IO routines for binary
reading.  Alternately you can use a variable length record (in theory)
using Binary Sequential - but I have not yet tried this.

priolof@libero.it (Federico) wrote in message news:<fd67e997.0211140950.6c85b7f0@posting.google.com>...
> Hi, I have written a cobol compressor that uses huffman method to
> reduce file.
…[15 more quoted lines elided]…
> Thank you
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
