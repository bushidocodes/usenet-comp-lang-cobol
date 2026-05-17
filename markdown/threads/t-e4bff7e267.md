[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pass Data Area to Cobol program

_2 messages · 2 participants · 1997-11 → 1998-05_

---

### Pass Data Area to Cobol program

- **From:** "kojo sarkodee" <ua-author-17072296@usenetarchives.gap>
- **Date:** 1997-11-30T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34830A60.1A9E@ozemail.com.au>`

```

Am amending a Cobol program written for IBM SYS36. No Cobol manual
available. Can anyone tell me how to pass a data area to the program and
how to handle it in the program?

Please reply by E-mail to kxs··.@oze··m.au

Thanks in advance,

Marianne Wassmer
```

#### ↳ Re: Pass Data Area to Cobol program

- **From:** "dave johnson" <ua-author-6589126@usenetarchives.gap>
- **Date:** 1998-05-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e4bff7e267-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34830A60.1A9E@ozemail.com.au>`
- **References:** `<34830A60.1A9E@ozemail.com.au>`

```

Usual thing is a PARM='.......' in (MVS) JCL, you need to code a Linkage
sections something like

01 LINKAGE SECTION
03 PARM-LEN PIC S(4) COMP.
03 PARM-DATA PIC X(n).

PROCEDURE DIVISION
IF PARM-LEN > 0
..... pick up your paremeter....

the above is from memory - approach with caution! If you hit the IBM web
site, they have alsmost all their manuals on-line (recommended, but bookmark
the 'manuals' pages!)

regards, DaveJ.

Kojo Sarkodee wrote in message <348··.@oze··m.au>...
› Am amending a Cobol program written for IBM SYS36. No Cobol manual
› available. Can anyone tell me how to pass a data area to the program and
…[6 more quoted lines elided]…
› Marianne Wassmer
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
