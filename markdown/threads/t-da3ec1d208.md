[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Elementary 0C4

_2 messages · 2 participants · 1999-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: Elementary 0C4

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<egaj3.10526$qw.61471@news2.mia>`
- **References:** `<7m4jdh$prr@dfw-ixnews13.ix.netcom.com>`

```
The E35 Routine is the COBOL SORT EXIT ROUTINE (Sort passes control to the
E35 Routine
AFTER it returns each record in the final phase.

MOST LIKELY - YOU FAILED to retrieve ALL the SORTED Records

R Teutsch wrote in message <7m4jdh$prr@dfw-ixnews13.ix.netcom.com>...
>Code
>
…[26 more quoted lines elided]…
>
```

#### ↳ Re: Elementary 0C4

- **From:** gah@ugcs.caltech.edu (glen herrmannsfeldt)
- **Date:** 1999-07-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n185a$n83@gap.cco.caltech.edu>`
- **References:** `<7m4jdh$prr@dfw-ixnews13.ix.netcom.com> <egaj3.10526$qw.61471@news2.mia>`

```
"James King" <mangogwr@bellsouth.net> writes:

(snip)
>>
>>Abend 0C4 in IGZESMG
…[5 more quoted lines elided]…
>>

Is R10 odd, or is the parameter list really an odd address?
I thougth it should be at least halfword aligned, though I would word
align it.

-- glen
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
