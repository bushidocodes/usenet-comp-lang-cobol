[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF V3.1 COBOL Problem

_3 messages · 3 participants · 1996-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF V3.1 COBOL Problem

- **From:** "anek" <ua-author-11422993@usenetarchives.gap>
- **Date:** 1996-04-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<316D06CD.3EFC@hol.gr>`

```
Currently working Micro Focus COBOL V3.1 on a ICL TEAMSERVER (Spark-Risc)
running Unix SVR4 7.8.3 X/OPEN XPG4.

At peak hours when reaching the maximum number of the system users ( which is
about 32 ) we get across a very anoying problem. Certain COBOL files are
actually loosing all of their contents by getting a zero file size.

We suspect it is a COBOL problem although we are not sure yet.

All our providers have been informed and are looking into the problem, no
anwers yet.

Does anyone have any idea of what can the problem be ??

Has anyone experience the same or similar problem when working with MF COBOL
??

We would appreciate any help.
```

#### ↳ Re: MF V3.1 COBOL Problem

- **From:** "peter mcclure" <ua-author-17087236@usenetarchives.gap>
- **Date:** 1996-04-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f78cfe1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<316D06CD.3EFC@hol.gr>`
- **References:** `<316D06CD.3EFC@hol.gr>`

```
You give few details, but it sounds similar to a problem for which there
has been a fix for some time. Assuming that you have a current
maintenance agreement, and that you have hit a known problem, you can get
fix tapes via your Support contact.

Regards
Sue Edwards
(+44 1344 472044)
```

#### ↳ Re: MF V3.1 COBOL Problem

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1996-04-11T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-aa4f78cfe1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<316D06CD.3EFC@hol.gr>`
- **References:** `<316D06CD.3EFC@hol.gr>`

```
In message <<316··.@h··.gr>> anek writes:
› running Unix SVR4 7.8.3 X/OPEN XPG4. 
› 
› At peak hours when reaching the maximum number of the system users ( which is 
› about 32 ) we get across a very anoying problem. Certain COBOL files are 
› actually loosing all of their contents by getting a zero file size. 

Just off the top of my head, how about:

At peak times the system is reaching some limit on file opens and
a program, attempting to open a non-optional file I-O fails to
open it. The program, because it doesn't check _why_ it failed
tries to correect the problem by opening it output.

This time the open succeeds.

Solution: recode to use optional files and only open I-O.

Just a guess.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
