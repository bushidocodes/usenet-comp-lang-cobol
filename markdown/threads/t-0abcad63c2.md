[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Can MVS COBOL2 co-exist with VS/COBOL?

_2 messages · 2 participants · 1995-06 → 1995-07_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Can MVS COBOL2 co-exist with VS/COBOL?

- **From:** "brie..." <ua-author-17088172@usenetarchives.gap>
- **Date:** 1995-06-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<020571LPNODCYWKMACDT@nascom.com>`

```

I am running jobs using VS/COBOL and I need to know if I can keep the
execution time modules (called by COBOL programs) of both COBOL2 and
VS/COBOL on the system at the same time? Maybe one of you has already
done the conversion to COBOL2 and could give me some insight on what I
should avoid. Thank you.
Peter Briedis
Huntley, IL.

Provided by NaSPA, Inc., The Association for Corporate Computing Technical
Professionals. Located in Milwaukee, Wi 53220, with over 20,000 members in 58
different countries. First four months of membership free. call (414) 423-2420
or send Email to mbr··.@nas··m.com and leave name, address and phone number!
```

#### ↳ Re: Can MVS COBOL2 co-exist with VS/COBOL?

- **From:** "marty..." <ua-author-17073867@usenetarchives.gap>
- **Date:** 1995-07-01T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0abcad63c2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<020571LPNODCYWKMACDT@nascom.com>`
- **References:** `<020571LPNODCYWKMACDT@nascom.com>`

```

BR> Subject: Can MVS COBOL2 co-exist with VS/COBOL?


BR> I am running jobs using VS/COBOL and I need to know if I can keep the
BR> execution time modules (called by COBOL programs) of both COBOL2 and
BR> VS/COBOL on the system at the same time? Maybe one of you has already
BR> done the conversion to COBOL2 and could give me some insight on what I
BR> should avoid. Thank you.

It's a definite maybe.
Are both libraries in the system linklist?
[BEST BEST: Allocate the libs in the run-time JCL for the older,
VS/COBOL jobs. Put the *newer* COBOL2 libs in linklist.]
---
* SLMR 2.1a * I try not to sniff the help. * Dan Conner (Roseanne)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
