[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# (IBM) SHARE - LNGC requirements

_1 message · 1 participant · 2004-03_

---

### Re: (IBM) SHARE - LNGC requirements

- **From:** robin <robin_v@bigpond.mapson.com>
- **Date:** 2004-03-23T13:49:04+00:00
- **Newsgroups:** comp.lang.cobol,comp.lang.pl1,ibm.software.cobol,ibm.software.le,ibm.software.pli
- **Message-ID:** `<kfX7c.121441$Wa.101936@news-server.bigpond.net.au>`

```
From: "John W. Kennedy" <jwkenne@attglobal.net>, Optimum Online
Date: Mon, 22 Mar 2004 04:20:32 GMT

| Mark Yudkin wrote:
| > Executable ON statements also exist in other languages - e.g. Visual Basic.
…[6 more quoted lines elided]…
| offhand think of any occasion when it would even have simplified things. 
.
The ON statement is one of the most important and useful
statements in PL/I.
.
Can you guarantee that all your programs had absolutely no
hidden bugs?
.
The error handler in PL/I is used for all sorts of applications,
including extended range floating-point, complex acos,
and typical run-time data conditions such as fixed-point overflow,
floating-point overflow, division by zero (yes, you can include
a specific test for zero divisor in every division),
and so on.
.
Makes life a lot easier.
.
At the very least, you can obtain a snapshot of the
variables at the time of an error, without having to re-run
the program.  And it gives you a traceback listing the
statement numbers of who called what.
.
|   I regard it as as nasty as COBOL ALTERed GO TO, for the same reason: 
| it alters the state of the program with no visible datum.
| -- 
| John W. Kennedy
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
