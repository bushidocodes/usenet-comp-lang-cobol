[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ABEND-Handling under LE - Examples?

_2 messages · 2 participants · 2004-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: ABEND-Handling under LE - Examples?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-05-13T20:13:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UFQoc.19035$Hs1.18600@newsread2.news.pas.earthlink.net>`
- **References:** `<c807pb$i3$1@panix5.panix.com>`

```
For DD - or anyone else interested in an "intro to LE condition handlers" - may
I suggest STARTING at:

  http://ew.share.org/proceedingmod/abstract.cfm?abstract_id=5804

which is the "proceedings" from the last share for a session called,

  8234 - Writing User Condition Handler Routines for Language Environment

     ***

I don't know if it will give you exactly what you are looking for, but it would
certainly be a good (IMHO) place to start.

You might (also) want to look at:
  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea2140/3.6.6.4

which shows how to handle a "divide-by-zero" condition - not what you are after,
but some what similar.
```

#### ↳ Re: ABEND-Handling under LE - Examples?

- **From:** docdwarf@panix.com
- **Date:** 2004-05-14T05:27:38-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c823ea$t2$1@panix5.panix.com>`
- **References:** `<c807pb$i3$1@panix5.panix.com> <UFQoc.19035$Hs1.18600@newsread2.news.pas.earthlink.net>`

```
In article <UFQoc.19035$Hs1.18600@newsread2.news.pas.earthlink.net>,
William M. Klein <wmklein@nospam.netcom.com> wrote:
>For DD - or anyone else interested in an "intro to LE condition handlers" - may
>I suggest STARTING at:
>
>  http://ew.share.org/proceedingmod/abstract.cfm?abstract_id=5804

How curious... a PowerPoint presentation which appears to actually contain 
something of value!  Greatly appreciated, Mr Klein; I'll give it a whack 
and see what comes of it.

[snip]

>You might (also) want to look at:
>  http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ceea2140/3.6.6.4
>
>which shows how to handle a "divide-by-zero" condition - not what you are after,
>but some what similar.

Ahhhhh, the IBM-sample coding-style with which I'm familiar... it should 
be interesting to see how the COPY statements resolve, or don't.

Thanks greatly, Mr Klein... and it is interesting that there's such a 
paucity of response on this matter.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
