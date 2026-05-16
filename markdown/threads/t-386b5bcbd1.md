[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Work problem: cobol signed numerics to SAS

_4 messages · 4 participants · 2001-02_

---

### Work problem: cobol signed numerics to SAS

- **From:** blambert@broughton-sys.com (Bob Lambert)
- **Date:** 2001-02-08T00:53:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3a81ed77.20647930@news.interramp.com>`

```
Does anyone know how to import numerics with embedded signs into SAS.
Unfortunately we are working with a file produced with a Cobol program
but do not have quick enough access to Cobol resources to read in and
write a different format using Cobol
Any advice?
Thanks!
```

#### ↳ Re: Work problem: cobol signed numerics to SAS

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-02-08T11:47:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Hvg6.105$Hj2.13355@paloalto-snr1.gtei.net>`
- **References:** `<3a81ed77.20647930@news.interramp.com>`

```
I have a Windows 32-bit DLL whci can be used to convert COBOL signed
numerics to other formats. It's mostly free (it costs you the time to
commetn on it or I bug the crap out of you).

Write if interested and I'll send you a conversion package. It is NOT an
"end-user tool" as is.
```

#### ↳ Re: Work problem: cobol signed numerics to SAS

- **From:** "Ron" <NoSoy@swbell.net>
- **Date:** 2001-02-10T19:14:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<964p0s$rs4$1@sshuraaa-i-1.production.compuserve.com>`
- **References:** `<3a81ed77.20647930@news.interramp.com>`

```
Assuming you're on a mainframe, what little I remember about SAS
I don't see why this should be a problem. SAS handles IBM standard
Zoned Decimal format which I think is what you're talking about.
It even handles packed decimal I believe. Defining the fields as
zoned decimal in SAS should allow it to read them.


===================================================================
> Does anyone know how to import numerics with embedded signs into SAS.
> Unfortunately we are working with a file produced with a Cobol program
…[3 more quoted lines elided]…
> Thanks!
```

#### ↳ Re: Work problem: cobol signed numerics to SAS

- **From:** mel5133928@aol.com (MEl5133928)
- **Date:** 2001-02-16T00:03:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010215190323.04900.00000193@ng-cd1.aol.com>`
- **References:** `<3a81ed77.20647930@news.interramp.com>`

```
For signed packed decimal representation on OS/390, use SAS informat PDw.d
(where w=width of the field and d is a representation of the number of decimal
places to assume). For zoned decimal data, use informat ZDw.d. You can use
BZw.d to convert blanks to zeroes (except leading ones).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
