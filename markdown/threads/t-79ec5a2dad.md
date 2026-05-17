[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL and VB

_1 message · 1 participant · 1996-06_

---

### COBOL and VB

- **From:** "ant..." <ua-author-15649371@usenetarchives.gap>
- **Date:** 1996-06-02T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4ou255$cc7@tst.hk.super.net>`

```

I have a COBOL program that will be called from a VB program. I compiled the
cobol code by MS-COBOL 5.0 to a Windows 3.1 DLL. However, the DLL does not
work properly.

The COBOL program used COMP-3 for some numeric data. I wrote an interface
program that will accept single/double numeric from VB and convert it to
COMP-3 format and then pass it to my old COBOL program. However, when my
interface program try to convert the binary numeric data to COMP-3 format, the
system crashed. The error message is floating number not supported. I checked
that and assured that the floating library for windows has been linked during
the COBOL compilation and linking. I also check that the WINEN87.DLL has been
loaded when VB is lanuched.

I tried to change the COMP-3 of my old COBOL to COMP-1 for accepting single
from VB, but, the precision does not match the output that generate the
output. I think that the tail of COMP-3 is truncated but the tail of COMP-1
doesn't. Does my claim right?

DO anyone can help me to solve
1. without changing the COBOL program, ie remain using COMP-3 not to change
its format, how can I compile it as DLL that can commnunicate with VB ?

2. if I changed COMP-3 to other binary representation, how can I retain the
precision as previous, ie the calculation in COBOL is truncated to some
defined decimal point ?

Looking to hearing from you.
Thank a lots.


ant··.@hk.··r.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
