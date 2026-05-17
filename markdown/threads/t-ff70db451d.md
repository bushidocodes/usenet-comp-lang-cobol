[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL-2 equivalent of STATE option?

_2 messages · 2 participants · 1997-07_

---

### COBOL-2 equivalent of STATE option?

- **From:** "mr..." <ua-author-4512326@usenetarchives.gap>
- **Date:** 1997-07-28T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5rlnjb$jmg$1@apakabar.cc.columbia.edu>`

```

Does anyone know what the COBOL 2 equivalent is for the "STATE" compiler
option that was used in VS COBOL?
(With the STATE compiler option, if the program ABENDs
(such as division by zero), the run-time listing will show the actual
COBOL statement number where the ABEND occurred).

I tried using "FDUMP", but it didn't seem to tell me which statement it
was. I also tried "TEST" which yielded nothing new.
Finally I tried "TEST(ALL,SYM)" and "TEST(STMT)", and the compiler
rejected them as invalid compiler options.

Anyone know?

...
```

#### ↳ Re: COBOL-2 equivalent of STATE option?

- **From:** "j lenz" <ua-author-17071373@usenetarchives.gap>
- **Date:** 1997-07-28T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ff70db451d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5rlnjb$jmg$1@apakabar.cc.columbia.edu>`
- **References:** `<5rlnjb$jmg$1@apakabar.cc.columbia.edu>`

```

Michael R Linn wrote:
› 
› Does anyone know what the COBOL 2 equivalent is for the "STATE" compiler
…[12 more quoted lines elided]…
› ...


If you are using FDUMP and OPTIMIZE, then you will not get a line number
for the ABEND, but rather the HEX address (offset, perhaps) of where the
error occurred. Use that address to compare to you compile listing, and
you should be able to locate the line within the compile listing where
the error occurred. Also, FDUMP will display the value of program
variables at the time the ABEND occurred. We are a VSE/ESA shop.

Joseph Lenz
TTI, Inc.
Fort Worth, TX
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
