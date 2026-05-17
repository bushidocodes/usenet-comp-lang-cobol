[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS Spool

_3 messages · 3 participants · 1997-02 → 1997-03_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS Spool

- **From:** "richard halim" <ua-author-17072709@usenetarchives.gap>
- **Date:** 1997-02-28T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3318916F.458E@ttuvm1.ttu.edu>`

```

Anyone out there knows how to call CICS SPOOL?.

CICS manual showed a only a fragment sample.
There was no explanation of the parms being
passed (their values etc.) prior to doing
EXEC CICS SPOOL.

thanks
```

#### ↳ Re: CICS Spool

- **From:** "thane hubbell" <ua-author-1728640@usenetarchives.gap>
- **Date:** 1997-03-02T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9cc6a497d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3318916F.458E@ttuvm1.ttu.edu>`
- **References:** `<3318916F.458E@ttuvm1.ttu.edu>`

```



Richard Halim wrote in article
<331··.@ttu··u.edu>...
› Anyone out there knows how to call CICS SPOOL?.
› 
…[3 more quoted lines elided]…
› EXEC CICS SPOOL.

Spool sets the characteristics of a virtual printer, reader or punch. I
have no idea of the actual use for it, having never used it. Sorry, that'
s not much help. I *think* you use it to set your settings for the virtual
device then use it any way you normally would.
```

#### ↳ Re: CICS Spool

- **From:** "hans chr. enevoldsen" <ua-author-6589041@usenetarchives.gap>
- **Date:** 1997-03-02T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-b9cc6a497d-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3318916F.458E@ttuvm1.ttu.edu>`
- **References:** `<3318916F.458E@ttuvm1.ttu.edu>`

```

Richard Halim wrote:
› 
› Anyone out there knows how to call CICS SPOOL?.
…[6 more quoted lines elided]…
› thanks

The functionality is something like this:
EXEC CICS SPOOLOPEN...
perform until no more lines to write
move something-or-other to an 80 character line
EXEC CICS SPOOLWRITE...
end-perform
EXEC CICS SPOOLCLOSE...
You must consult a manual, maybe the Systems Programming Reference?
One use for this is to write to the INTRDR (internal reader) on MVS, and
so build up a JCL "deck" to be submitted from a CICS application.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
