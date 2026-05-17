[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP: Runtime error 163.

_3 messages · 3 participants · 1995-04 → 1995-05_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### HELP: Runtime error 163.

- **From:** "i92..." <ua-author-11185545@usenetarchives.gap>
- **Date:** 1995-04-30T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3o1nls$equ@sheoak.bendigo.latrobe.edu.au>`

```
Hi,
I have been having problems with CICS Option under windows. When I try
to move a numeric field that has been group initialised to spaces, into
another numeric field I consistently recieve an error 163 - invalid
numeric data. I am compiling for OSVS compat with the cics
preprocessor. To date I have tried many compiler options and
host-compatibility options (including the early release host-nummove)
but nothing seems to solve the problem.
Currently I am using release 43 of MFCobol. Any
ideas/suggestions would be greatly appreciated.

Thanks,.
Adrian Holland.

p.s. please reply by mail if it is at all possible.
i92··.@red··u.au
```

#### ↳ Re: HELP: Runtime error 163.

- **From:** "marty..." <ua-author-17073867@usenetarchives.gap>
- **Date:** 1995-05-01T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3ecca09e62-p2@usenetarchives.gap>`
- **In-Reply-To:** `<3o1nls$equ@sheoak.bendigo.latrobe.edu.au>`
- **References:** `<3o1nls$equ@sheoak.bendigo.latrobe.edu.au>`

```

AD> I have been having problems with CICS Option under windows.
AD> When I try to move a numeric field that has been group
AD> initialised to spaces, into another numeric field I
AD> consistently recieve an error 163 - invalid numeric data.

SPACES are NOT valid numeric data.
Initialize your fields to NUMERIC values.
---
* SLMR 2.1a * T#H#E#F#T##R#E#S#I#S#T#A#N#T##T#A#G#L#I#N#E#!
```

#### ↳ Re: HELP: Runtime error 163.

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1995-05-02T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3ecca09e62-p3@usenetarchives.gap>`
- **In-Reply-To:** `<3o1nls$equ@sheoak.bendigo.latrobe.edu.au>`
- **References:** `<3o1nls$equ@sheoak.bendigo.latrobe.edu.au>`

```
In message <<3o1nls$e.··.@she··u.au>> i92··.@red··u.au writes:
› I have been having problems with CICS Option under windows.  When I try
› to move a numeric field that has been group initialised to spaces, into
…[6 more quoted lines elided]…
› ideas/suggestions would be greatly appreciated.

Use compiler option SPZERO
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
