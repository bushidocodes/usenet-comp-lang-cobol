[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM COBOL II option settings

_3 messages · 3 participants · 1996-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### IBM COBOL II option settings

- **From:** "tur..." <ua-author-525017@usenetarchives.gap>
- **Date:** 1996-05-19T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4nqs48$l1@netaxs.com>`

```

Has anyone tinkered with the Options for COBOL II compiles?

Any suggestions to opitmize performance?
```

#### ↳ Re: IBM COBOL II option settings

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-05-20T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8d591bcdfe-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4nqs48$l1@netaxs.com>`
- **References:** `<4nqs48$l1@netaxs.com>`

```

I have only tinkered with these for 10 or 11 years.

A more complete discussion of this aspect of VS COBOL II, COBOL/370 and
COBOL for MVS and VM is contained "Planning COBOL Migration", a 3.5 day
class offered thru Edge Information Group (e-mail for details).

A short summary....

For best performance - OPTIMIZE, NOTEST, NOSSRANGE, FASTSRT

Avoid the complements of these - NOOPTIMIZE, TEST, SSRANGE, NOFASTSRT

SSRANGE should certainly be used if you need to fix subscript / index
problems.

TRUNC(BIN) performs worse than TRUNC(OPT). TRUNC in general is more of a
"what answers do I want", you should carefully understand the differences
between OPT, STD and BIN before changing this option.

NUMPROC like TRUNC is a trinary option, and can significantly affect
results in certain cases. Some performace affects can be found in this
option, but one needs to be very carefull as to results side effects. My
recommendation is to stick with NUMPROC(MIG).

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

##### ↳ ↳ Re: IBM COBOL II option settings

- **From:** "keith farndon" <ua-author-17086118@usenetarchives.gap>
- **Date:** 1996-05-26T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8d591bcdfe-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-8d591bcdfe-p2@usenetarchives.gap>`
- **References:** `<4nqs48$l1@netaxs.com> <gap-8d591bcdfe-p2@usenetarchives.gap>`

```

RWidmer wrote:
› 
› I have only tinkered with these for 10 or 11 years.
…[25 more quoted lines elided]…
› survive in a legacy based world.

Two things I would mention, SSRANGE can inhibit some coding techniques,
and OPTIMIZE WILL cause problems with products such as Expediter.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
