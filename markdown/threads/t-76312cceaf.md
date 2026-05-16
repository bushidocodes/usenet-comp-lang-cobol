[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Dynamic File Allocations in COBOL

_2 messages · 2 participants · 2002-03_

---

### Dynamic File Allocations in COBOL

- **From:** COBOLMAN <member@mainframeforum.com>
- **Date:** 2002-03-20T04:14:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c9852ea$1_3@news.teranews.com>`

```
Someone asked this at work and I have never heard of it so maybe the
MFF can help.

It is my understanding that there is a way to dynamically allocate files
from inside a Cobol program. For example, Lets say I have an input that
needs to be split into a varying number of outputs. Rather than having
hardcoded DD statements for every possible output file, the DDs can be
allocated dynamically from the program itself. On one day there may be
10 output DDs and the next may have 30 output DDs based on the input?

COBOL in use is COBOL II and COBOL for MVS
```

#### ↳ Re: Dynamic File Allocations in COBOL

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-03-20T05:30:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a79rsu$hm$1@nntp9.atl.mindspring.net>`
- **References:** `<3c9852ea$1_3@news.teranews.com>`

```
Not possible (directly) in VS COBOL II or IBM COBOL for MVS & VM  (By using
calls to SVC99 or even ISPF, it can be done with these compilers)

It is available directly, however, with IBM COBOL for OS/390 & VM (V2R2)
   and
IBM Enterprise COBOL for z/OS & OS/390.

See:
 http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igypg205/1.7.3
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
