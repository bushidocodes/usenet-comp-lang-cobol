[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help!!! How to access vision version 3 format using acucobol

_2 messages · 2 participants · 2003-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Help!!! How to access vision version 3 format using acucobol

- **From:** amits_77@yahoo.com (Amit Sawhney)
- **Date:** 2003-04-22T02:48:40-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<71939fd6.0304220148.4e6a4ca7@posting.google.com>`

```
Hello,

I am having a major problem accessing vision version 3 format files
using acucobol as i am new to acucobol and this vision format thing.I
have got a deadline to meet,it would be really kind of you ppl to help
me in anyway possible.Please post a sample program where i can get an
idea of how to read vision V3 files from acucobol(Also i am not having
the key information of the files).

Over to you guys
TIA
Amit Sawhney
Software Engineer
Keane India Limited
```

#### ↳ Re: Help!!! How to access vision version 3 format using acucobol

- **From:** ray@rays-web.com (Ray Smith)
- **Date:** 2003-04-22T16:24:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5654fff9.0304221524.313994b5@posting.google.com>`
- **References:** `<71939fd6.0304220148.4e6a4ca7@posting.google.com>`

```
Hi Amit,

The AcuCOBOL runtime will read a vision file of any version.  
(Each file obviously has the vision version stored in it.)

From what it sounds like you don't have select and file definitions for the 
file(s) your trying to access??  In which case the only known way to look 
at the data is dump it out to text files using the "vutil" file utility.

Regards,

Ray Smith
ray@rays-web.com

 

amits_77@yahoo.com (Amit Sawhney) wrote in message news:<71939fd6.0304220148.4e6a4ca7@posting.google.com>...
> Hello,
> 
…[11 more quoted lines elided]…
> Keane India Limited
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
