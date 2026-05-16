[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# FCOBOL calc in batch vs CICS

_5 messages · 5 participants · 1999-07 → 1999-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### FCOBOL calc in batch vs CICS

- **From:** Dale Easley <easley@ix.netcom.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379C8822.9ADCBD1@ix.netcom.com>`

```
My applications people have been trying to track down a nasty little 1 (that's ONE) penny
calculation problem between an Online CICS/VSE program and a VSE Batch program.

Is there any difference between FCOBOL Batch and Online that could possibly create this ?
```

#### ↳ Re: FCOBOL calc in batch vs CICS

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379CF997.7438480E@techie.com>`
- **References:** `<379C8822.9ADCBD1@ix.netcom.com>`

```
If you have switched compilers and/or run time, it is possable. 
Of course, you are calculationg everything in pennys, right? 
Turns out the MVS COBOL has a better arithmetic runtime, but this
will only apply to mathematical things in floating point (and
possibly some display to comp binary conversions).  Don't forget
the old options TRUNC and NUMPROC...
```

#### ↳ Re: FCOBOL calc in batch vs CICS

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ni393$7q2@dfw-ixnews4.ix.netcom.com>`
- **References:** `<379C8822.9ADCBD1@ix.netcom.com>`

```
Dale Easley <easley@ix.netcom.com> wrote in message
news:379C8822.9ADCBD1@ix.netcom.com...
> My applications people have been trying to track down a nasty little 1
(that's ONE) penny
> calculation problem between an Online CICS/VSE program and a VSE Batch
program.
>
> Is there any difference between FCOBOL Batch and Online that could
possibly create this ?
> --
> Dale Easley (Systems Administrator)
…[3 more quoted lines elided]…
>

I pride myself on my knowledge of "obscure" and "obsolete" IBM mainframe
COBOLs - but COBOL-F under VSE is beyond me.  The obvious thing to check out
is that your "steplib" search is finding the same run-time modules - and/or
that your link-edits pointed to the same libraries.
```

#### ↳ Re: FCOBOL calc in batch vs CICS

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19990726213027.13700.00001485@ngol03.aol.com>`
- **References:** `<379C8822.9ADCBD1@ix.netcom.com>`

```
In article <379C8822.9ADCBD1@ix.netcom.com>, Dale Easley <easley@ix.netcom.com>
writes:

>
>My applications people have been trying to track down a nasty little 1
…[6 more quoted lines elided]…
>

I can't imagine where you might find such a difference.  Especially if the two
modes are using the same routines.
It sounds more like one side is using rounding and the other is truncating.
```

#### ↳ Re: FCOBOL calc in batch vs CICS

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 1999-08-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7omik1$hen$1@nntp9.atl.mindspring.net>`
- **References:** `<379C8822.9ADCBD1@ix.netcom.com>`

```
Are they using the same TRUNC Compiler Option?

WOB

Dale Easley <easley@ix.netcom.com> wrote in message
news:379C8822.9ADCBD1@ix.netcom.com...
> My applications people have been trying to track down a nasty little 1
(that's ONE) penny
> calculation problem between an Online CICS/VSE program and a VSE Batch
program.
>
> Is there any difference between FCOBOL Batch and Online that could
possibly create this ?
> --
> Dale Easley (Systems Administrator)
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
