[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# LIBKEEP in LE/370?

_2 messages · 2 participants · 1997-07_

---

### LIBKEEP in LE/370?

- **From:** "igor gindler" <ua-author-17071923@usenetarchives.gap>
- **Date:** 1997-07-14T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5qeisl$cde@mid.way.com>`

```

Does anybody use CEELRR (Library Routine Retention macro)
under LE/370? I've tried to invoke CEELRRin/tr from COB2.3.2
and COB for MVS & VM programs to keep a COB/370 subroutine
in memory until the end of run unit, but got RC=16.

Installation uses default value for RTEREUS(OFF). CALL 'CEELRRIN'
is the first command in the Procedure Division, and the main
program does not calls any other assembler routine.

Thanks,

Igor Gindler
AiC

BTW, how to pass the return code from CEELRRin/tr to the
COBOL program?
```

#### ↳ Re: LIBKEEP in LE/370?

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-07-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-1f8eb4b42d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5qeisl$cde@mid.way.com>`
- **References:** `<5qeisl$cde@mid.way.com>`

```

Are you trying to keep a COBOL/370 application routine in storage, or part
of the run-time.

LIBKEEP and RTREUS are both little used, and generally not worth the
trouble.... perhaps a more detailed description of what you are trying to
do will yeild a better solution.
Rex Widmer
Builder of software archeology tools and other strange programs to help survive in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
