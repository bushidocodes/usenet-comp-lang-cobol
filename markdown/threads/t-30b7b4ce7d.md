[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF 3.4 Animator bug using Report Writer with nested copy-procs

_1 message · 1 participant · 1999-07_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### MF 3.4 Animator bug using Report Writer with nested copy-procs

- **From:** renfrew@erols.com (Dave Miner)
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nib3v$t0m$1@autumn.news.rcn.net>`

```
(Environment: Novell Netware 4.11 server, with WIN98 client, using Micro-Focus level 3.4)
 
(Note:  This is an FYI, and is unrelated to my previous inquiry about ghost breakpoints.) 

While trying to animate a rather large program, the Animator kept totally freezing up.  I was 
forced to kill the dos session after each attempt, and it was driving me absolutely bonkers.  But 
after many hours of progressively whittling down the code, I was finally able to isolate the 
problem.  THE BUG IS AS FOLLOWS:  If a program uses the same copy-proc in more than one RD, and 
if that copy-proc itself uses one or more subordinate copy-procs, then Animator goes into a 
coma.

Once I understood it, I was then able to work around it.  Victory is mine!...Bwa Ha Ha...!

Don't know if this bug also exists in earlier or newer versions.  Don't know if I can justify the 
time to find out.  But if I ever do I will be glad to post the results.  

DaveM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
