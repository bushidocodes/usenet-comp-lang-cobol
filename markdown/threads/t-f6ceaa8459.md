[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# unix printing using lpd

_3 messages · 3 participants · 1998-11_

---

### unix printing using lpd

- **From:** "Paulo" <c.m@mail.telepac.pt>
- **Date:** 1998-11-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<731rku$vnd$1@duke.telepac.pt>`

```
Hi !

how can i send something to printer using unix lpd ?

TIA

Paulo
c.m@mail.telepac.pt
```

#### ↳ Re: unix printing using lpd

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1998-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36553ECB.8F0C30A4@mfltd.co.uk>`
- **References:** `<731rku$vnd$1@duke.telepac.pt>`

```
Paulo wrote:
> 
> Hi !
> 
> how can i send something to printer using unix lpd ?

If you're using Micro Focus COBOL (and really, these are OS issues
not COBOL issues you are raising so you should be stating which
compiler and version you are using as it will have a strong bearing
on whether you get a useful response) you should check out the
response I gave yesterday about using DD_ mapping - this will let you
write directly to a print scheduler in the COBOL program. Alternatively
write the data to a LINE-SEQUENTIAL file and then do something like:

CALL "SYSTEM" USING "lpr filename" & x"00".

Cheers, Kev.
```

##### ↳ ↳ Re: unix printing using lpd

- **From:** g1dlc@Radix.Net (David L. Craig)
- **Date:** 1998-11-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<733stk$8th$1@saltmine.radix.net>`
- **References:** `<731rku$vnd$1@duke.telepac.pt> <36553ECB.8F0C30A4@mfltd.co.uk>`

```
In article <36553ECB.8F0C30A4@mfltd.co.uk>,
Kevin Digweed  <ked@mfltd.co.uk> wrote:
>Paulo wrote:
>> 
…[10 more quoted lines elided]…
> write directly to a print scheduler in the COBOL program.

For example, in your program:

   SELECT PRT-FILE ASSIGN EXTERNAL "PRTOUT"

and in your shell script:

   DD_PRTOUT='>lpr'   ; export DD_PRTOUT

See the COBOL System Reference Manual chapter "External
File Name Mapping" for details, especially the section
"Setting Up Pipes."
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
