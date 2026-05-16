[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF-COBOL vs ACUCOBOL

_5 messages · 5 participants · 1998-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF-COBOL vs ACUCOBOL

- **From:** dmisamore@discountlabels.com
- **Date:** 1998-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6smrtt$84r$1@nnrp1.dejanews.com>`

```
My company is evaluating a move from ACUCOBOL to MF-COBOL. I am inquiry if
there is much syntax difference between the two and if ACUCOBOL vision files
would be easily portable to the MF-COBOL file system.

We are trying to collect information other than provided by a salesman.

Thanks

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: MF-COBOL vs ACUCOBOL

- **From:** "Sal Cambareri" <sal@lasermax.com>
- **Date:** 1998-09-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KqUI1.9767$f01.7374046@news.teleport.com>`
- **References:** `<6smrtt$84r$1@nnrp1.dejanews.com>`

```
If your company is committed to using the Vision file system you could
license the Vision file system package from Acucobol and link it into your
Microfocus build files.  One caveat: I don't know for sure, but it seems
possible that MF COBOL might not support some of the features of the Vision
file system.  Features such as multiple gigabyte record sizes aren't really
"syntax" issues, and so you should make sure that you verify that the limits
on file structures allowed in MF COBOL at least match what you are using in
your Acucobol programs.

Regards,
Sal

dmisamore@discountlabels.com wrote in message
<6smrtt$84r$1@nnrp1.dejanews.com>...
>My company is evaluating a move from ACUCOBOL to MF-COBOL. I am inquiry if
>there is much syntax difference between the two and if ACUCOBOL vision
files
>would be easily portable to the MF-COBOL file system.
>
…[5 more quoted lines elided]…
>http://www.dejanews.com/rg_mkgrp.xp   Create Your Own Free Member Forum
```

#### ↳ Re: MF-COBOL vs ACUCOBOL

- **From:** "Mike Rochford" <miker@easirun.co.za>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t5u54$46j$1@news01.iafrica.com>`
- **References:** `<6smrtt$84r$1@nnrp1.dejanews.com>`

```

dmisamore@discountlabels.com wrote in message
<6smrtt$84r$1@nnrp1.dejanews.com>...
>My company is evaluating a move from ACUCOBOL to MF-COBOL. I am inquiry if
>there is much syntax difference between the two and if ACUCOBOL vision
files
>would be easily portable to the MF-COBOL file system.

Firstly my question would be WHY ??????
Secondly - If really depends upon what features you have used within
AcuCobol. If you have used their extensions to the cobol language,
particularly within the SCREEN SECTION, then you are going to find it
exceptionally difficult to move. To get the same kind of GUI screens out of
MicroFocus you are going to have to replce the AcuCobol screens with either
MicroFocus's Dialog system or something like SPII from Flexus or COBOL-WOW
from England Technical Services.

The only way I can think of to move the data files would be to write an
AcuCobol program to strip them into sequential format and then a MicroFocus
program to rebuild them.

Whatever you decide to do, I would very carefully assess the reasons before
embarking on this exercise.

We distribute both AcuCobol and MicroFocus (As well as RM) so if you have
any specific questions, you are welcome to e-mail me directly.

Mike.

>
>We are trying to collect information other than provided by a salesman.
>

Are you implying that Salesmen don't always tell the truth ????

That's fighting talk !!!!!

Mike.
```

##### ↳ ↳ Re: MF-COBOL vs ACUCOBOL

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-09-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6t7hhb$9g4@sjx-ixn3.ix.netcom.com>`
- **References:** `<6smrtt$84r$1@nnrp1.dejanews.com> <6t5u54$46j$1@news01.iafrica.com>`

```

Mike Rochford wrote in message <6t5u54$46j$1@news01.iafrica.com>...
>
  <some snippage>

>Firstly my question would be WHY ??????
>Secondly - If really depends upon what features you have used within
…[6 more quoted lines elided]…
>
  <more snippage>

If you are interested in using the AcuCOBOL "windowing" syntax, then contact
your Micro Focus support representative.  At one time they offered an
"integrated preprocessor" which supported most (all?) of the AcuCOBOL
syntax.  I don't remember if this ended up as part of the generally
available product or not - but it should be around MF somewhere.
```

#### ↳ Re: MF-COBOL vs ACUCOBOL

- **From:** "Paul Swartout" <pauls@ftmis5.demon.co.uk>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<905991484.20320.0.nnrp-03.c1eda680@news.demon.co.uk>`
- **References:** `<6smrtt$84r$1@nnrp1.dejanews.com>`

```
Ask about MF NetExpress. The Beta of ver 3 looks very good. Not sure of the
differencies between MF and ACU but NetExpress has the edge as far as I can
see.
Hope this helps.


Cheers,

Paul.

dmisamore@discountlabels.com wrote in message
<6smrtt$84r$1@nnrp1.dejanews.com>...
>My company is evaluating a move from ACUCOBOL to MF-COBOL. .......
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
