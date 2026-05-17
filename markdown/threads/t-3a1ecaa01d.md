[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Old MS-COBOL PF keyes vs. MF-COBOL PF keyes

_1 message · 1 participant · 1997-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Old MS-COBOL PF keyes vs. MF-COBOL PF keyes

- **From:** "zat..." <ua-author-15183000@usenetarchives.gap>
- **Date:** 1997-04-24T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3360ef16.1280735079@client1.news.psi.net>`

```


I am converting an old system written in MS-COBOL, to MF-COBOL. the
documentation is poor and, when exists, many times is inaccurate. I
did manage to REBUILD my ISAM files (thnks to all of you who've jumped
to the rescue) and to linkedit my 'chained' program so they flow
correctly (I had to use quite a bizanitine, manual procedure since it
refused to work as 'advertised' - BUT - it works now).
My problem is the PFKeys in conjunction with SCREEN SECTION. The OLD
MS-COBOL seems to view the as if it was and does not
understand it as an ACCEPT Terminator untill you are on the last field
of the DISPLAYed SCREEN, so our user interface assumes typing data and
for every field. and are used as an ACCEPT
Terminators for update or back off.
MF COBOL view as an ACCEPT Terminator, but my users refuse
(rightly so) to alter their user interface.
Also, the keys are mapped to different values and handling them
require a bizare interface (x'AF') with one of the system modules.
But this seems to be much less of a problem.
Does any body know how to overide the so it will not be
rendered as an ACCEPT Terminator, but just will skip to the next field
untill the end of the DISPLAYed SCREEN?
Thanks
Ze'ev Atlas
TACT Software
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
