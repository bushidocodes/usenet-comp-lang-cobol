[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Read flat file field +123.45 in Cobol2 - How please ?

_1 message · 1 participant · 2004-11_

---

### Re: Read flat file field +123.45 in Cobol2 - How please ?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-11-12T02:32:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LgVkd.4302106$ic1.415727@news.easynews.com>`
- **References:** `<88a0c64a.0411091825.602a6cfa@posting.google.com> <ae83p0tc8o4j6qq1a3c6fci1im0bavavu4@4ax.com> <88a0c64a.0411101819.14b282e0@posting.google.com> <217e491a.0411111002.5f9ba812@posting.google.com> <88a0c64a.0411111712.4226a654@posting.google.com>`

```
To: "Nice4"

For future reference, it is always useful (to avoid mis-communication between 
questions and answers) to provide:

1) The operating system (your "S0C7" implied - MVS, OS/390, z/OS - or VSE or 
VM - or an "emulator")

2) The *exact* compiler (name and release) that you are using, i.e
   VS COBOL II, R4
      or
    IBM Enterprise COBOL, V3R3
      or
    Micro Focus, NetExpress V4.0

3) Any compiler options (directives for some compilers) that you are using that 
seem "relevant" (for example, for S0C7 problems,
    CMPR2 (impacts use of Function NumVal - where available)
    NUMPROC
    ZWB

***

When asking a question, you may not know what "we" need to know to answer your 
question, but if you provide all that you think MIGHT be relevant, then we 
(probably) can reply more quickly and accurately.


 ***

For those interested in "various" solutions to the original problem on IBM 
MVS-type systems (my best guess of the original problem),

 - With VS COBOL II R3.0 or later, with NOCMPR2, then "'85 Standard de-editing" 
is expected.  It may not (probably won't?) work with CMPR2 as that is a '74 
Standard variation

 - With COBOL/370 or later (IBM COBOL for-this-and-that, and Enterprise COBOL), 
again with NOCMPR2, then the NUMVAL and NUMVAL-C intrinsic functions are 
available (as well as de-editing)

 - Various "add-on" tools can help detect (and in some cases "fix") S0C7 (data 
exception - i.e. invalid data for certain numeric instructions).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
