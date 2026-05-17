[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CONVERT INDEXED FILES FROM ICOBOL TO MICROFOCUS

_2 messages · 2 participants · 1997-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration) · [`VSAM, files, sorting`](../topics.md#files)

---

### CONVERT INDEXED FILES FROM ICOBOL TO MICROFOCUS

- **From:** "euromercante" <ua-author-6588952@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bd048c$d420e4e0$3dc841c2@p200>`

```


WE HAVE A PROBLEM WITH FIELDS WITH SIGN, FOR EX. PIC S9(05)
OR PIC S9(05).
WE MAKE A REORG WITH ICOBOL TO CONVERT INDEXED FILE TO SEQUENTIAL
FILE AND AFTER WE RUN A MICROFOCUS COBOL PROGRAM TO READ THE
SEQUENTIAL FILE AND WRITE A NEW INDEXED FILE.
THE ONLY WAY WE FIND UNTIL NOW TO SOLVE THIS PROBLEM IS USING SIGN"EBCDIC"
DIRECTIVE,
BUT WE ARE NOT SURE THAT THIS IS THE WRITE WAY.

Thanks very much.
```

#### ↳ Re: CONVERT INDEXED FILES FROM ICOBOL TO MICROFOCUS

- **From:** "judson mcclendon" <ua-author-18805@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-8db392de1c-p2@usenetarchives.gap>`
- **In-Reply-To:** `<01bd048c$d420e4e0$3dc841c2@p200>`
- **References:** `<01bd048c$d420e4e0$3dc841c2@p200>`

```

If you define all your numeric fields in the sequential file as DISPLAY, and
also use SIGN IS LEADING/TRAILING SEPARATE, where LEADING/TRAILING is the
same for programs creating and reading the file, it should work between any
two COBOL systems.
Judson McClendon          This is a faithful saying and worthy of all
Sun Valley Systems        acceptance, that Christ Jesus came into the
jud··.@min··g.com   world to save sinners  (1 Timothy 1:15)
(please remove zzz from email id to respond)

EUROMERCANTE  wrote:
> 
> WE HAVE A PROBLEM WITH FIELDS WITH SIGN, FOR EX. PIC S9(05) 
…[8 more quoted lines elided]…
> Thanks very much.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
