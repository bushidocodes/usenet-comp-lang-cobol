[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu compiler 3 problem for beginner

_2 messages · 2 participants · 2001-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Tutorials, books, learning`](../topics.md#learning)

---

### Fujitsu compiler 3 problem for beginner

- **From:** merfair@aol.com (MERfair)
- **Date:** 2001-01-18T02:37:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010117213738.16178.00000732@ng-ca1.aol.com>`

```
Can anyone tell me where I can put my input files so that they will be read by
my program. I'm not sure how to "attach" them.
```

#### ↳ Re: Fujitsu compiler 3 problem for beginner

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-01-18T06:42:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010118014220.25954.00001083@nso-fm.aol.com>`
- **References:** `<20010117213738.16178.00000732@ng-ca1.aol.com>`

```
In article <20010117213738.16178.00000732@ng-ca1.aol.com>, merfair@aol.com
(MERfair) writes:

>
>Can anyone tell me where I can put my input files so that they will be read
…[3 more quoted lines elided]…
>

You should be able to place them in any directory and 
then point to them via the RunTimeEnvironment setup.
It really depends on how you have defined the files in
your program.  Have you coded the filenames on the select
or in WS?  Or did you use an implementor name that 
can be 'fed' the real file name via environment variables
created/provided thru the Run-Time Environment setup.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
