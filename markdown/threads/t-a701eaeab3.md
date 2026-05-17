[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# ?? Linking MVS COBOL with Fortran subs in CICS ??

_2 messages · 2 participants · 1998-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### ?? Linking MVS COBOL with Fortran subs in CICS ??

- **From:** "wat..." <ua-author-7774064@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34dc7b24.383184630@news.mindspring.com>`

```

We are presently converting from the VSE environment where we have
COBOL calling Fortran subs in CICS. We have had little or no success
with getting them to run under MVS/CICS. Has anyone else had any
success?

Ken Watts
Commonwealth Industries, Inc.
wat··.@mai··y.com
```

#### ↳ Re: ?? Linking MVS COBOL with Fortran subs in CICS ??

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-03T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a701eaeab3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34dc7b24.383184630@news.mindspring.com>`
- **References:** `<34dc7b24.383184630@news.mindspring.com>`

```


Ken Watts wrote in message <34d··.@new··g.com>...
› We are presently converting from the VSE environment where we have
› COBOL calling Fortran subs in CICS.  We have had little or no success
…[5 more quoted lines elided]…
› wat··.@mai··y.com

My first question would be whether you are realy doing CALLs or if you are
doing EXEC CICS LINKs. I think you have a pretty good chance of getting the
later to work - and almost no chance for the former. (Call do work fine in
MVS -between COBOL and FORTRAN - but only in batch).

My suggestion to you would be to look at

http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/CEEA403/9.0
(but take out the line break). This is a chapter called

"9.0 Chapter 9. Communicating between COBOL and Fortran"

in the LE for OS/390 ILC Programming Guide

Note: The actual information will depend on what COBOL and what run-time
system you are using. LE is different from VS COBOL II which is WAY
different than OS/VS COBOL.

P.S. Have you checked what the support is for FORTRAN under CICS without any
COBOL? I know that this has been "up and down" over the years and I don't
know where it stands today.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
