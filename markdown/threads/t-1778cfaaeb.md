[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# anybody here use AcuCOBOL?

_4 messages · 3 participants · 2001-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### anybody here use AcuCOBOL?

- **From:** "eRRaTiK" <regulate@hotmail.com>
- **Date:** 2001-05-17T05:58:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5MJM6.57547$ff.449955@news-server.bigpond.net.au>`

```
If so, how do you compile a main program and a subroutine? I tried compiling
one at a time and then running the executable for the main program but I
always get an error message.

I'm also trying to use index files in the program, but the index files are
in two parts ie. STUDENT2.dat and STUDENT2.idx, and the compiler doesn't
like that or I'm doing something wrong.

However, when I run the program under a UNIX compiler (DEC cobol or
something) the program and linking works fine.

Any suggestions?

eRRaTiK
```

#### ↳ Re: anybody here use AcuCOBOL?

- **From:** "Dennis Edward" <temp081100@ipipeline.net>
- **Date:** 2001-05-17T15:21:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_%RM6.1630$5R2.76518687@news1.van.metronet.ca>`
- **References:** `<5MJM6.57547$ff.449955@news-server.bigpond.net.au>`

```
"eRRaTiK" <regulate@hotmail.com> wrote in message
news:5MJM6.57547$ff.449955@news-server.bigpond.net.au...
> If so, how do you compile a main program and a subroutine? I tried
compiling
> one at a time and then running the executable for the main program but I
> always get an error message.
…[9 more quoted lines elided]…
>

1) Tell us what the error message is

2) Be a little more specific, concise, and accurate with your description of
the problem. For instance, the "compiler" doesn't care one way or the other
about the .vix file, although the runtime may choke. And if it chokes, what
*specifically* does it say?
```

##### ↳ ↳ Index Files and Subroutines (using AcuCOBOL)

- **From:** "eRRaTiK" <regulate@hotmail.com>
- **Date:** 2001-05-24T06:56:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lg2P6.74156$ff.570372@news-server.bigpond.net.au>`
- **References:** `<5MJM6.57547$ff.449955@news-server.bigpond.net.au> <_%RM6.1630$5R2.76518687@news1.van.metronet.ca>`

```
I can't get AcuCOBOL to access my index files. The index file "STUDENT" is
in fact two separate physical files -> STUDENT.DAT and STUDENT.IDX.

how can I do it?

...

I also want to know how it is possible to compile a program that calls a
subroutine. Do I compile the main program and then the subroutine
separately, then run the main program? or is there a specific command I must
use in order for the main program to link to the subroutine correctly?

...

Any assistance with these problems would be appreciated.

eRRaTiK
```

###### ↳ ↳ ↳ Re: Index Files and Subroutines (using AcuCOBOL)

- **From:** Gary_guizio@ci.juneau.ak.us (GaryG)
- **Date:** 2001-05-24T13:48:56-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cf4aea75.0105241248.1291ce4@posting.google.com>`
- **References:** `<5MJM6.57547$ff.449955@news-server.bigpond.net.au> <_%RM6.1630$5R2.76518687@news1.van.metronet.ca> <Lg2P6.74156$ff.570372@news-server.bigpond.net.au>`

```
"eRRaTiK" <regulate@hotmail.com> wrote in message news:<Lg2P6.74156$ff.570372@news-server.bigpond.net.au>...
> I can't get AcuCOBOL to access my index files. The index file "STUDENT" is
> in fact two separate physical files -> STUDENT.DAT and STUDENT.IDX.
> 
> how can I do it?

If you are using Acucobol version 4 of the Vision file system I
believe the index portion should be named STUDENT.VIX. This may not be
the problem because the extension, I believe, can be changed using the
"name_ext" configuration variable.
> 
> ...
…[5 more quoted lines elided]…
> 
If you mean by "subroutine" another Acucobol program then you would
compile them separately and call the second program from the first by
using the CALL function as in: CALL "program-name" USING "parameter".

If your "subroutine" is a C program, you must first link the program
in to the runtime and then call it the same way you would if it was
another Acucobol program.
> ...
> 
> Any assistance with these problems would be appreciated.
> 
> eRRaTiK
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
