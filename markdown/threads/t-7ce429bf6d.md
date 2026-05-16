[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM Enterprise COBOL for z/OS V3R4: RECORD CONTAINS 0

_5 messages · 4 participants · 2006-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### IBM Enterprise COBOL for z/OS V3R4: RECORD CONTAINS 0

- **From:** "charles hottel" <chottel@earthlink.net>
- **Date:** 2006-08-19T02:47:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ZuFg.7946$Qf.7033@newsread2.news.pas.earthlink.net>`

```
I am interested in writing a program that can process "any" fixed length 
record, sequential file via QSAM.  By "any" I specifically mean that on 
different runs of the program, different files, that have different logical 
record lengths, could be processed successfully, without recompiling the 
program for the new record size.  If it is possible, how would you code the 
FD?

The  programmer's guide for V3R4 says that if I code "BLOCK CONTAINS 0"  I 
can avoid record length conflicts and not get file status 39 errors. So then 
what should I code for the description of the 01 level record?  I am 
thinking the maximum logical record size of  PIC X(32760).

Well I am just researching the feasibility/possibility and I have not had a 
chance to experiment as yet. But supposing that it does work, at run time 
how would I know what the actual record length is of the file that I am 
processing? I have posted a COBPTR program on this newsgroup before that 
goes through control blocks and retrieves this information from the DCB, but 
I am wondering if anyone has a better solution.

Does anyone have any experience at trying this? Thanks.
```

#### ↳ Re: IBM Enterprise COBOL for z/OS V3R4: RECORD CONTAINS 0

- **From:** "Alistair" <alistair@ld50macca.demon.co.uk>
- **Date:** 2006-08-19T04:23:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1155986585.968258.86840@h48g2000cwc.googlegroups.com>`
- **In-Reply-To:** `<6ZuFg.7946$Qf.7033@newsread2.news.pas.earthlink.net>`
- **References:** `<6ZuFg.7946$Qf.7033@newsread2.news.pas.earthlink.net>`

```

charles hottel wrote:
> I am interested in writing a program that can process "any" fixed length
> record, sequential file via QSAM.  By "any" I specifically mean that on
…[17 more quoted lines elided]…
> Does anyone have any experience at trying this? Thanks.

You could code the FD as having a one byte record length and build the
true record in working storage.

For your solution, when you read the second record would Cobol
reposition the pointer to the start of the true record or to the start
of the logicaslly defined to the program record (ie at the start of the
next block)?
```

##### ↳ ↳ Re: IBM Enterprise COBOL for z/OS V3R4: RECORD CONTAINS 0

- **From:** "charles hottel" <chottel@earthlink.net>
- **Date:** 2006-08-19T14:46:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<QuFFg.8106$Qf.1729@newsread2.news.pas.earthlink.net>`
- **References:** `<6ZuFg.7946$Qf.7033@newsread2.news.pas.earthlink.net> <1155986585.968258.86840@h48g2000cwc.googlegroups.com>`

```

"Alistair" <alistair@ld50macca.demon.co.uk> wrote in message 
news:1155986585.968258.86840@h48g2000cwc.googlegroups.com...
>
> charles hottel wrote:
…[34 more quoted lines elided]…
>
I do not know until I try it. Thanks for your idea it might be better.
```

#### ↳ Re: IBM Enterprise COBOL for z/OS V3R4: RECORD CONTAINS 0

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-08-19T21:47:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fGLFg.425255$1Q1.422752@fe03.news.easynews.com>`
- **References:** `<6ZuFg.7946$Qf.7033@newsread2.news.pas.earthlink.net>`

```
Usually, this does NOT work well with COBOL on z/OS. FS=39 problems can (will?) 
occur much of the time.  I think (but am not positive) that if you pass the FD 
name (not the record) to a subprogram, you can get access to the DCB and "play 
with it" there to avoid FS=39.

Otherwise, I would look at using ISPF Library services, an Assembler subroutine, 
or some other way of doing this.

COBOL is really DESIGNED to know at compile time the "fixed file attributes" of 
all files.  Some vendors have extensions to get around this, but not IBM.
```

#### ↳ Re: IBM Enterprise COBOL for z/OS V3R4: RECORD CONTAINS 0

- **From:** "Grzegorz Mazur" <news@gregu.cjb.net>
- **Date:** 2006-08-20T00:52:52+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ec8ble.3a8.1@hamster.gregu.cjb.net>`
- **References:** `<6ZuFg.7946$Qf.7033@newsread2.news.pas.earthlink.net>`

```
charles hottel wrote:
>I am interested in writing a program that can process "any" fixed length 
>record, sequential file via QSAM.  By "any" I specifically mean that on 
…[17 more quoted lines elided]…
> Does anyone have any experience at trying this? Thanks.

Actually I've been doing this three weeks ago :) I was writing a program 
that had to handle two different files. For this to work I declared an input 
file with the RECORD CONTAINS 0 and BLOCK CONTAINS 0 clauses and assigned it 
a maximum logical record length (in my case it was 300 chars, but of course 
you can take any allowed value you want). It worked fine for any file I 
opened - no 39's.

The big problem that I had with this solution (and it made me switch to 
declaring two different input files for each of the formats) was ARC 
restartability of the program - after working storage was restored by 
ARC/AES and the file was repositioned, read failed on the next record. So if 
you're not planning on using ARC/AES, go ahead. If you are - sorry...

Hope this helps :)

Greg.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
