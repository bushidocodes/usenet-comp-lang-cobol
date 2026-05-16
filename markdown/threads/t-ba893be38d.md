[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Help: COBOL/CICS Re-useable Working-Storage Problem

_3 messages · 2 participants · 1998-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Re: Help: COBOL/CICS Re-useable Working-Storage Problem

- **From:** zberger@ldl.net
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<6t2js6$cph$1@nnrp1.dejanews.com>`
- **References:** `<35EE41E5.AE90123B@powernet.co.uk> <35eff82e.105240@netnews.worldnet.att.net> <35F155DD.79884725@powernet.co.uk> <35F19541.6EA5C8E@powernet.co.uk>`

```
In article <35F19541.6EA5C8E@powernet.co.uk>,
  Phil Davey <davey@powernet.co.uk> wrote:
> Phil Davey wrote:
>
…[5 more quoted lines elided]…
> (Note: Displays are now tolerated in CICS 4.1 )

I thought that was a feature of LE (which my shop just moved to)...we have
been mostly on 4.1 for 2+ years and displays would toast everything...

The evil sysprogs must be at their mischief again...I imagine a parm of
'display=allow' somewhere in the task stream.



-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: Help: COBOL/CICS Re-useable Working-Storage Problem

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-08T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<6t43p6$kh6@sjx-ixn3.ix.netcom.com>`
- **References:** `<35EE41E5.AE90123B@powernet.co.uk> <35eff82e.105240@netnews.worldnet.att.net> <35F155DD.79884725@powernet.co.uk> <35F19541.6EA5C8E@powernet.co.uk> <6t2js6$cph$1@nnrp1.dejanews.com>`

```

zberger@ldl.net wrote in message <6t2js6$cph$1@nnrp1.dejanews.com>...
>In article <35F19541.6EA5C8E@powernet.co.uk>,
>  Phil Davey <davey@powernet.co.uk> wrote:
…[18 more quoted lines elided]…
>http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum

Remember that old game "I doubt you"?

Well, I doubt you - the DISPLAY verb is definitely still a "no-no" with all
releases of COBOL and all releases of LE and all releases of CICS (unless we
are talking about CICS on OS/2 or NT).

If you think there is documentation to the contrary, please point me to it!
```

##### ↳ ↳ Re: Help: COBOL/CICS Re-useable Working-Storage Problem

- **From:** zberger@ldl.net
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<6t6npl$7t7$1@nnrp1.dejanews.com>`
- **References:** `<35EE41E5.AE90123B@powernet.co.uk> <35eff82e.105240@netnews.worldnet.att.net> <35F155DD.79884725@powernet.co.uk> <35F19541.6EA5C8E@powernet.co.uk> <6t2js6$cph$1@nnrp1.dejanews.com> <6t43p6$kh6@sjx-ixn3.ix.netcom.com>`

```
In article <6t43p6$kh6@sjx-ixn3.ix.netcom.com>,
  "William M. Klein" <wmklein@ix.netcom.com> wrote:
>
> zberger@ldl.net wrote in message <6t2js6$cph$1@nnrp1.dejanews.com>...
…[28 more quoted lines elided]…
> If you think there is documentation to the contrary, please point me to it!

I don't know if it is officially supported with CICS (I doubt it), is a
feature of LE (possible) or a creative sysprog put a head patch on the
IGZ{display} module (possible).  I do know that DISPLAY statements executed
under CICS 4.1 with LE and running on OS/390 at my shop send a
'TASK-TRANS-PROG-TIMESTAMP: {displayed data}' to the CSSL log.

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
