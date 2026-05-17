[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Disk error in dos

_5 messages · 3 participants · 1998-08_

---

### Disk error in dos

- **From:** "grgr..." <ua-author-17074661@usenetarchives.gap>
- **Date:** 1998-08-12T20:21:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6qtbi4$5b4$1@nnrp1.dejanews.com>`

```
Help

We have users on a network that are getting "disk error on drive p: abort
retry etc. and there does not seem to be any recovery method

This seems to be an error in the external file handler.

Is there any catch this error so the files are not damaged (file structure
errors)?

This seems to be a problem when writting to an indexed file. It doesn't seem
to be going to the declaratives section.


Thanx

Greg Rogers

mailto:grg··.@ya··o.com

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

#### ↳ Re: Disk error in dos

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbd3d9254e-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6qtbi4$5b4$1@nnrp1.dejanews.com>`
- **References:** `<6qtbi4$5b4$1@nnrp1.dejanews.com>`

```
› We have users on a network that are getting "disk error on drive p: abort
› retry etc. and there does not seem to be any recovery method

What Cobol? Dos or Windows or Win95?
```

##### ↳ ↳ Re: Disk error in dos

- **From:** "grgr..." <ua-author-17074661@usenetarchives.gap>
- **Date:** 1998-08-13T11:14:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbd3d9254e-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cbd3d9254e-p2@usenetarchives.gap>`
- **References:** `<6qtbi4$5b4$1@nnrp1.dejanews.com> <gap-cbd3d9254e-p2@usenetarchives.gap>`

```
In article <6quejo$7l7$1.··.@new··s.net>,
"Donald Tees" wrote:
›› We have users on a network that are getting "disk error on drive p: abort
›› retry etc. and there does not seem to be any recovery method
…[3 more quoted lines elided]…
›

It is microfocus cobol 2.2.59 running on windows/win95 platform in a DOS
window. The application also uses the XM DOS extender.

Thanx

Greg Rogers

mailto:grg··.@ya··o.com

feel free to email me directly

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

###### ↳ ↳ ↳ Re: Disk error in dos

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbd3d9254e-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-cbd3d9254e-p3@usenetarchives.gap>`
- **References:** `<6qtbi4$5b4$1@nnrp1.dejanews.com> <gap-cbd3d9254e-p2@usenetarchives.gap> <gap-cbd3d9254e-p3@usenetarchives.gap>`

```
› It is microfocus cobol 2.2.59 running on windows/win95 platform in a DOS
› window. The application also uses the XM DOS extender.

One thing that will produce that error is a second DOS window
that uses NET commands. If you are starting the process with
a batch file that hooks into P with a NET USE P: command, that
may be your problem.
```

#### ↳ Re: Disk error in dos

- **From:** "as-..." <ua-author-17074031@usenetarchives.gap>
- **Date:** 1998-08-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-cbd3d9254e-p5@usenetarchives.gap>`
- **In-Reply-To:** `<6qtbi4$5b4$1@nnrp1.dejanews.com>`
- **References:** `<6qtbi4$5b4$1@nnrp1.dejanews.com>`

```
grg··.@my-··s.com schrieb:

› Help
› 
…[23 more quoted lines elided]…
› Forum

pls. tell us more about your environment:
- NOS (NT Netware UNIX)
-WS OS (DOS, WIN ??, UNIX)
-Database (DB/2 COBOL BTRIEVE ORACLE INFORMIX ....)
-circumstance of error generating

Greatings

AS
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
