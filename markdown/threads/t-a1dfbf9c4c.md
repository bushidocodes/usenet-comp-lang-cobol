[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cics cobol calling cics java

_2 messages · 2 participants · 2004-04_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### cics cobol calling cics java

- **From:** bqui001@yahoo.com (bevyn quiding)
- **Date:** 2004-04-04T17:10:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<957af941.0404041610.139472d9@posting.google.com>`

```
Hello all,

We have acquired a system written into cics cobol and we are trying to 
integrate some of the sections into our j2ee system.

There are tons of examples and documentation about communcating to a backend
cics system from a j2ee system, unfortunately that is not what i have been 
asked to do.

we want it to work the other way around.

so the cics module calls our j2ee server and the server replies.

the version of cics we have is cics version 2.2 (soon to be upgraded to 2.3)
running on os/390 (soon to be upgraded to z/os).

we dont have mqseries and would rather not get it, if we can help it.

I understand that websphere runs as a part of cics and can be called by a cics
program using the commarea? or something like that.

the only part we are having problems with is that bit.

has any one done this? i don't have any experience with cics or cobol.
so I was hoping someone could give me a few pointers.

cheers
Bevyn
```

#### ↳ Re: cics cobol calling cics java

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-04-05T02:37:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7E3cc.16050$lt2.12136@newsread1.news.pas.earthlink.net>`
- **References:** `<957af941.0404041610.139472d9@posting.google.com>`

```
Are you using Enterprise COBOL?  If so, you probably want to look at "INVOKE"
from COBOL rather than "CALL".

Check out:
   http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/igy3pg20/6.1

and following
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
