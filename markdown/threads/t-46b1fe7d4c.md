[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CICS Problem

_2 messages · 2 participants · 1998-05_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### CICS Problem

- **From:** "pat finley" <ua-author-17084518@usenetarchives.gap>
- **Date:** 1998-05-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd8c3e$9156fca0$06755acf@default>`

```

I have a cobol CICS program that has stopped working. It always moved a
value into the CWA area. CICS has recently been upgraded and the program
now abends.

Does anyone know what I can do?
```

#### ↳ Re: CICS Problem

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-05-30T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-46b1fe7d4c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd8c3e$9156fca0$06755acf@default>`
- **References:** `<01bd8c3e$9156fca0$06755acf@default>`

```

In article <01bd8c3e$9156fca0$06755acf@default>, "Pat Finley"
writes:

› I have a cobol CICS program that has stopped working. It always moved a
› value into the CWA area. CICS has recently been upgraded and the program
› now abends.

Does the Common Work Area still exist in the version of CICS you had upgraded
to? (I thought I read someplace that it is scheduled to be dropped from a
future release of CICS.)

If the CWA still exists, is it defined large enough (DFHSIT parameter WRKAREA=)
to hold what you plan on moving into the CWA? (As a Systems Programmer, I know
that if I was confident a certain feature isn't being used, I would eliminate
it to free up additional precious 24-bit storage, and the CWA would be one
place I would be strongly tempted to reduce or eliminate.)

How are you getting the address of the CWA? If it is an ASSIGN statement, are
you checking the resulting value to be sure a value is returned? (My CICS
manuals are at work and I am at home so I cannot look up the returned value
when it is not addressable--it might be something as simple as returning zero.)

Mark A. Young
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
