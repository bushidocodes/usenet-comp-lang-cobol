[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Object code efficiency - COBOL vs C.

_1 message · 1 participant · 2003-04_

---

### Re: Object code efficiency - COBOL vs C.

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-04-10T15:11:24-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E95B3CC.C56259E7@istar.ca>`
- **References:** `<200304101642.h3AGgWtu163860@westrelay04.boulder.ibm.com>`

```
Tom Ross wrote:
> 
> >I know that this is comparing apples to oranges (or maybe apples to horse
…[31 more quoted lines elided]…
> with the TRUNC(OPT) compiler option.

I have seen the code referred to by John when compiling using TRUNC(OPT)
with COBOL for MVS and VM.  I think that the double precision code is
generated to cater for the general case of ADD A B C D TO E where A B
and C have values of +900,000,000 while D and E have values of
-901,000,000.  I believe that I found a circumvention by defining
WS-FULLWORD as S9(8) BINARY.  

> 
> Cheers,
> TomR              >> COBOL is the Language of the Future! <<
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
