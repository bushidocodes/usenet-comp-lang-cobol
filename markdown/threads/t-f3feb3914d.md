[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP: acucobol on m88k, cannot compile new runcbl

_2 messages · 2 participants · 1998-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### HELP: acucobol on m88k, cannot compile new runcbl

- **From:** "pavl..." <ua-author-12384986@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34eae1d3.25891940@news2.ibm.net>`

```

I want to include a new routine in the cobol runtime. But when I try
to make the new runtime, the linker says that the following symbols
are undefined:
__gh_mvw
__gh_mvh
__gh_mvb
__assert


The C compiler is a Green Hills Ansi C compiler v 1.8.5m16. The system
is a Motorola Unix System VR32V3. The acucobol is v1.5.3

The standard makefile also used with no modifications of the sub85.c
file, creates the same error, so the error is not produced by the
extra code.


Thanks in advance for all who take
the time to reply. Please reply also by
e-mail, due to problems we have (constantly
unsolved in IBM) to news servers, so I will not miss it.
For the unbelievers, read the news at
ibmnet.general.


To avoid spam, remove the "cosmos." from the address below.

Savas Pavlidis

pav··.@cos··m.net
```

#### ↳ Re: HELP: acucobol on m88k, cannot compile new runcbl

- **From:** "daniel maltes" <ua-author-1025739@usenetarchives.gap>
- **Date:** 1998-02-17T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f3feb3914d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34eae1d3.25891940@news2.ibm.net>`
- **References:** `<34eae1d3.25891940@news2.ibm.net>`

```

Savas,
Contact Acucobol support at http://www.acucobol.com/Services/Technical/

Dan Maltes
Applied Systems Technology

Savas Pavlidis wrote in message <34e··.@new··m.net>...
› I want to include a new routine in the cobol runtime. But when I try
› to make the new runtime, the linker says that the following symbols
…[27 more quoted lines elided]…
› pav··.@cos··m.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
