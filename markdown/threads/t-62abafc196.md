[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MACRO PRE-PROCESSOR FOR IBM MAINFRAME.

_3 messages · 3 participants · 1997-01_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### MACRO PRE-PROCESSOR FOR IBM MAINFRAME.

- **From:** "john veotzky" <ua-author-17071540@usenetarchives.gap>
- **Date:** 1997-01-12T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bc01d1$3f5ec7a0$7d6304c4@roo00318ceg.co.za.ceg.co.za>`

```

I am looking for a pre-processor to generate code from macros (like
Assembler , and to a certian extent EASYTRIEVE PLUS does). They are
available on PC's (e.g. MICROFOCUS REVOLVE) but I am looking for one to run
on IBM mainframes.
Anybody know of one?
Your help would be appreciated.
```

#### ↳ Re: MACRO PRE-PROCESSOR FOR IBM MAINFRAME.

- **From:** "mikehutchinson" <ua-author-17071774@usenetarchives.gap>
- **Date:** 1997-01-13T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-62abafc196-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bc01d1$3f5ec7a0$7d6304c4@roo00318ceg.co.za.ceg.co.za>`
- **References:** `<01bc01d1$3f5ec7a0$7d6304c4@roo00318ceg.co.za.ceg.co.za>`

```

John Veotzky wrote:
› 
› I am looking for a pre-processor to generate code from macros (like
…[4 more quoted lines elided]…
› Your help would be appreciated.

I've frequently used ISPF EDIT macros, REXX, and sometimes ISPF Dialog
Manager skeleton services as a macro facility. ISPF is an IBM product,
and rates to be available on any MVS system you encounter. In one
application, I even expanded the macro concept to generate entire
programs from 2 simple screens. In five man weeks I wrote the REXX
dialog, converted an existing program to a skeleton, and generated 35
CICS/COBOL-II/VSAM update programs containing 50,000 lines of clean
compiling programs ready for testing.
```

##### ↳ ↳ Re: MACRO PRE-PROCESSOR FOR IBM MAINFRAME.

- **From:** "kiy..." <ua-author-598721@usenetarchives.gap>
- **Date:** 1997-01-13T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-62abafc196-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-62abafc196-p2@usenetarchives.gap>`
- **References:** `<01bc01d1$3f5ec7a0$7d6304c4@roo00318ceg.co.za.ceg.co.za> <gap-62abafc196-p2@usenetarchives.gap>`

```

In <32D··.@con··c.net>, MikeHutchinson writes:
› John Veotzky wrote:
›› 
…[14 more quoted lines elided]…
› compiling programs ready for testing.

I hope you were under contract and were paid a buck or two per line of
code. Fifty or a hundred grand for 5 weeks work sounds fair to me.

The Rexx parse arg construct is an excellent way to generate code.

I have also seen people use the assembler macro processor and the one
built in PL/I to generate source for other languages. These things are
just string processors. If you look at an MVS stage 1, it generates JCL
from assembly language.

Again, charge 'em a couple dollars per generated line, not by the hour
unless you are getting several hundred dollars per hour for 'wizard
time'.

Cory Hamasaki Unemployment starts in 2002, we better have plan-B ready.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
