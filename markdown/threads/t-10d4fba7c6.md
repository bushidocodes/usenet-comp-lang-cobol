[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# cics and batch

_3 messages · 3 participants · 2004-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### cics and batch

- **From:** "Janek" <neuros@polbox.com>
- **Date:** 2004-09-27T15:39:07+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cj95cr$ill$1@nemesis.news.tpi.pl>`

```
Hi,

I have a cics program called ex. progcics.
I want to call it in batch program.

in batch program:
call "progcics" ommited struct

When progcics doesnt use db2 its ok.
When progcics uses db2 I have dump :
CEE3201S The system detected an operation exception (System Completion
Code=0C1).

Is it possible to use the same program (when uses db2) in cics and batch?
```

#### ↳ Re: cics and batch

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-27T20:43:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-1DEB5B.20431527092004@knology.usenetserver.com>`
- **References:** `<cj95cr$ill$1@nemesis.news.tpi.pl>`

```
In article <cj95cr$ill$1@nemesis.news.tpi.pl>,
 "Janek" <neuros@polbox.com> wrote:

> Hi,
> 
…[13 more quoted lines elided]…
> 

Yes, it is.  But you will need to link it differently, so you need two 
load modules.

The difference is in the DB2 stub that you add to your program -- if 
memory serves it is DSNELI and DSNALI that would be different.
```

#### ↳ Re: cics and batch

- **From:** "Don Leahy" <leahydon@nospamplease.netscape.net>
- **Date:** 2004-09-27T22:23:34-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BW36d.4589$tT2.565962@news20.bellglobal.com>`
- **References:** `<cj95cr$ill$1@nemesis.news.tpi.pl>`

```
I believe it is possible, but you have to be careful what version of the DB2 
language interface (DSNHLI) that you call.
"Janek" <neuros@polbox.com> wrote in message 
news:cj95cr$ill$1@nemesis.news.tpi.pl...
> Hi,
>
…[13 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
