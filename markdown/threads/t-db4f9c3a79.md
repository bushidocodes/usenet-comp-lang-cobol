[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call AcuCobol Program in Unix from Windows and obtain the output

_4 messages · 2 participants · 2006-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Call AcuCobol Program in Unix from Windows and obtain the output

- **From:** martin.olivares@gmail.com
- **Date:** 2006-05-03T13:53:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146689588.693511.181140@g10g2000cwb.googlegroups.com>`

```
Hi, sorry for my english and my Cobol skills. I have a little question,
can i run an Acucobol Program what resides in a Unix Server from a
command line of a PC running windows 2000, and obtain/view the output (
like a DOS command, but using some Cobol Exe ) ?


Thanks, 

Martín Olivares
Córdoba - Argentina
```

#### ↳ Re: Call AcuCobol Program in Unix from Windows and obtain the output

- **From:** ray223@gmail.com
- **Date:** 2006-05-03T14:15:18-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146690918.930590.288560@g10g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1146689588.693511.181140@g10g2000cwb.googlegroups.com>`
- **References:** `<1146689588.693511.181140@g10g2000cwb.googlegroups.com>`

```

martin.olivares@gmail.com wrote:
> Hi, sorry for my english and my Cobol skills. I have a little question,
> can i run an Acucobol Program what resides in a Unix Server from a
> command line of a PC running windows 2000, and obtain/view the output (
> like a DOS command, but using some Cobol Exe ) ?
> Thanks,

Hi Martin,

The quickest and easiest way would be to use the "AcuConnect" product
from AcuCorp.  This is exactly what this product was designed for.

You could also write your own client/server programs using "C$SOCKET"
command.

Regards,

Ray Smith
ray@RaymondSmith.com
```

##### ↳ ↳ Re: Call AcuCobol Program in Unix from Windows and obtain the output

- **From:** martin.olivares@gmail.com
- **Date:** 2006-05-04T11:36:38-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146767798.499110.169340@j33g2000cwa.googlegroups.com>`
- **In-Reply-To:** `<1146690918.930590.288560@g10g2000cwb.googlegroups.com>`
- **References:** `<1146689588.693511.181140@g10g2000cwb.googlegroups.com> <1146690918.930590.288560@g10g2000cwb.googlegroups.com>`

```
Thanks for your help. The Acuconnect alternative did you mention is
using the thin client or another technique (like an EXE) ? I need to
access the program in a synchronously mode from a .Net assembly thats
wraps the programs call.

Regards,

Martín Olivares
```

###### ↳ ↳ ↳ Re: Call AcuCobol Program in Unix from Windows and obtain the output

- **From:** ray223@gmail.com
- **Date:** 2006-05-04T14:43:57-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1146779037.509295.319800@y43g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<1146767798.499110.169340@j33g2000cwa.googlegroups.com>`
- **References:** `<1146689588.693511.181140@g10g2000cwb.googlegroups.com> <1146690918.930590.288560@g10g2000cwb.googlegroups.com> <1146767798.499110.169340@j33g2000cwa.googlegroups.com>`

```

martin.olivares@gmail.com wrote:
> Thanks for your help. The Acuconnect alternative did you mention is
> using the thin client or another technique (like an EXE) ? I need to
> access the program in a synchronously mode from a .Net assembly thats
> wraps the programs call.

Hi Martin,

The Thin Client product and AcuConnect use the same base TCP
communication tools, but AcuConnect has no GUI component.

AcuConnect installs itself as a service on the host computer.  Then any
other computer running AcuCOBOL can "call" any program on the host
computer just as easily as calling a program on the same computer (with
appropriate security and setup details).

Regards,

Ray Smith
ray@RaymondSmith.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
