[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# *OBSCURE* issue in using Procedure-Pointers instead of Dynamic CALLs for IBM "performance" reasons

_1 message · 1 participant · 2003-08_

---

### *OBSCURE* issue in using Procedure-Pointers instead of Dynamic CALLs for IBM "performance" reasons

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-08-23T04:01:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QGB1b.1940$O03.582@newsread2.news.atl.earthlink.net>`

```
There was an OLD thread about using procedure-pointers to improve
performance (over dynamic CALLs) in an IBM mainframe environment.  I found
the comment in GOOGLE at (long URL follows):


http://www.google.com/groups?q=pointer+dynamic+ibm+performance+group:comp.lang.cobol&hl=en&lr=&ie=UTF-8&oe=UTF-8&selm=3D5F709F.89D88CFC%40worldnet.att.net&rnum=2

While looking for something totally unrelated, I found this VERY interesting
(dox) APAR (another long URL),

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/zidocmst/666.1?ACTION=MATCHES&REQUEST=cobol&TYPE=FUZZY&SHELF=&DT=20030816095151&searchTopic=TOPIC&searchText=TEXT&searchIndex=INDEX&rank=RANK&ScrollTOP=FIRSTHIT#FIRSTHIT

If your site has started using PROCEDURE-POINTERs instead of dynamic CALL
statement, I suggest you look at this (pending) change to the Programming
Guide.  This may (or may not) turn out to be a problem for YOUR site, but it
certainly represents (IMHO) a potentially HARD TO DIAGNOSE problem.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
