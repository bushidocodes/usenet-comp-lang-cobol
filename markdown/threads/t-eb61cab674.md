[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT: JCL Emulators

_7 messages · 4 participants · 2010-09_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Off-topic and spam`](../topics.md#spam)

---

### OT: JCL Emulators

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-09-08T13:10:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com>`

```
Being an IBMer; does anyone know of a free to private use JCL
emulator? Ditto for CICS emulators...

I expect a negative so anything non-Hercules based will be a positive.
```

#### ↳ Re: JCL Emulators

- **From:** "Charles Hottel" <chottel@earthlink.net>
- **Date:** 2010-09-08T20:17:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BfednR9rfsHpuhXRnZ2dnUVZ_jqdnZ2d@earthlink.com>`
- **References:** `<bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com...
> Being an IBMer; does anyone know of a free to private use JCL
> emulator? Ditto for CICS emulators...
>
> I expect a negative so anything non-Hercules based will be a positive.

I do not know of a JCL emulator.

Z/COBOL has some EXEC CICS support: 
http://www.z390.org/z390_EXEC_CICS_Compatible_Assembler_Support.htm
```

##### ↳ ↳ Re: JCL Emulators

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-09-09T05:27:17-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2df552ab-934c-4978-ac0d-7f61e5bc3017@q9g2000vbd.googlegroups.com>`
- **References:** `<bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com> <BfednR9rfsHpuhXRnZ2dnUVZ_jqdnZ2d@earthlink.com>`

```
On Sep 9, 1:17 am, "Charles Hottel" <chot...@earthlink.net> wrote:

>
> Z/COBOL has some EXEC CICS support:http://www.z390.org/z390_EXEC_CICS_Compatible_Assembler_Support.htm

I had forgotten about the z390 Assembler project. Thanks.
```

#### ↳ Re: JCL Emulators

- **From:** "Bill Klein" <wmklein@noreply.ix.netcom.com>
- **Date:** 2010-09-08T19:36:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<O_Vho.88275$MG3.75956@en-nntp-16.dc1.easynews.com>`
- **References:** `<bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com>`

```
I guess that RDz-ut doesn't count as "free" < VERY big grin>
"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com...
> Being an IBMer; does anyone know of a free to private use JCL
> emulator? Ditto for CICS emulators...
>
> I expect a negative so anything non-Hercules based will be a positive.
```

##### ↳ ↳ Re: JCL Emulators

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-09-09T05:25:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6e1f90dd-e52c-4903-95ff-e74fc01a2186@l17g2000vbf.googlegroups.com>`
- **References:** `<bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com> <O_Vho.88275$MG3.75956@en-nntp-16.dc1.easynews.com>`

```
On Sep 9, 1:36 am, "Bill Klein" <wmkl...@noreply.ix.netcom.com> wrote:
> I guess that RDz-ut doesn't count as "free" < VERY big grin>"Alistair"

Not free but it has some merit regarding maintenance documentation
which may answer my other query.
```

#### ↳ Re: OT: JCL Emulators

- **From:** PR <paul.raulerson@gmail.com>
- **Date:** 2010-09-14T13:39:00-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6b7e4012-fe4f-4782-832c-162ead697057@j2g2000vbo.googlegroups.com>`
- **References:** `<bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com>`

```
On Sep 8, 3:10 pm, Alistair <alist...@ld50macca.demon.co.uk> wrote:
> Being an IBMer; does anyone know of a free to private use JCL
> emulator? Ditto for CICS emulators...
>
> I expect a negative so anything non-Hercules based will be a positive.

If you are just wanting it to play with, you can load a copy of OS/2
in a VM, and pick up an old copy of IBM VisualAge COBOL off ebay.
Voila - instant CICS environment, including development. I wrote a LOT
of CICS code on that exact same setup. :)

Indeed, I had a customer still running it until November of last year,
with I think, 30 terminals. I moved them to a iSeries machine, and
ported all their custom code, but I sure loved that little CICS
environment.

-Paul
```

##### ↳ ↳ Re: OT: JCL Emulators

- **From:** Alistair <alistair@ld50macca.demon.co.uk>
- **Date:** 2010-09-15T07:50:53-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2c2e98a3-d4a5-400e-8476-1693c7eceb7f@c21g2000vba.googlegroups.com>`
- **References:** `<bcb0280a-5058-459f-a57a-115f8a306c7a@i5g2000yqe.googlegroups.com> <6b7e4012-fe4f-4782-832c-162ead697057@j2g2000vbo.googlegroups.com>`

```
On Sep 14, 9:39 pm, PR <paul.rauler...@gmail.com> wrote:
> On Sep 8, 3:10 pm, Alistair <alist...@ld50macca.demon.co.uk> wrote:
>
…[15 more quoted lines elided]…
> -Paul

Thanks Paul.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
