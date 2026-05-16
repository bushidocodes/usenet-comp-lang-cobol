[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Conversion of assembler to cobol

_7 messages · 7 participants · 2001-10_

---

### Conversion of assembler to cobol

- **From:** david.i.smith@farmersinsurance.com (David Smith)
- **Date:** 2001-10-09T09:36:16-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<98bf16f9.0110090836.219ae0a3@posting.google.com>`

```
Is there any software out there that will do some rudimentary
conversion of assembler to COBOL under OS/390.  I have already done
some research
on the Web, and the pickings seem slim.  Have I simply not looked 
sufficiently, or does the animal not exist?
```

#### ↳ Re: Conversion of assembler to cobol

- **From:** Charles <nospam@newsranger.com>
- **Date:** 2001-10-09T16:45:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<OQFw7.21751$ev2.30234@www.newsranger.com>`
- **References:** `<98bf16f9.0110090836.219ae0a3@posting.google.com>`

```
In article <98bf16f9.0110090836.219ae0a3@posting.google.com>, David Smith
says...
>
>Is there any software out there that will do some rudimentary
…[3 more quoted lines elided]…
>sufficiently, or does the animal not exist?

Hire a programmer.
```

#### ↳ Re: Conversion of assembler to cobol

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-10-09T12:32:19-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9pvccf$i3$1@slb0.atl.mindspring.net>`
- **References:** `<98bf16f9.0110090836.219ae0a3@posting.google.com>`

```
Is this a "native" Assembler program that you want to convert to COBOL - or
is it actually "object code" assembler from an older COBOL program - that
you have lost the COBOL source code for?  If it is the latter, then there is
(at least one) company that does this.  If it is the former, then I think
that the "hire a programmer" is your best bet.
```

#### ↳ Re: Conversion of assembler to cobol

- **From:** "Ira D. Baxter" <idbaxter@semdesigns.com>
- **Date:** 2001-10-09T14:17:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bc34ffe$1_1@feed1.realtime.net>`
- **References:** `<98bf16f9.0110090836.219ae0a3@posting.google.com>`

```
If you have BAL Source and want it converted to COBOL or C,
I think Software Migrations might be what you are looking for.
http://www.smltd.com/

If they don't offer what you need, we offer custom conversion tools and
services
based on generalized compiler technology, and our tools already
know the COBOL side of the equation.
See http://www.semdesigns.com/Products/DMS/DMSToolkit.html.
```

#### ↳ Re: Conversion of assembler to cobol

- **From:** Steve Burns <stephen.d.burns2@boeing.com>
- **Date:** 2001-10-10T15:27:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC468FA.86EB27DC@boeing.com>`
- **References:** `<98bf16f9.0110090836.219ae0a3@posting.google.com>`

```
Try http://www.raincode.com

They have a 4gl system that may be of use.  Unless you have a tone of
code to convert, it probably will be easier to have programmer do it
manually, though.  (It is possible that raincode has already done
something like thins, in which case, they may have 4gl code all ready to
use.  Raincode will also bid on doing the conversion for you.

One of my first jobs (decodes ago) was to convert IBM assembler programs
to cobol.  It ws not a difficult technical job, but understanding
exactly what the code did was tough.  Some of my code contained comments
to say that I had no idea what portions of the code actually
accomplished, but I was pretty sure that the cobol translation
duplicated the assembler stuff.....

David Smith wrote:
> 
> Is there any software out there that will do some rudimentary
…[3 more quoted lines elided]…
> sufficiently, or does the animal not exist?
```

#### ↳ Re: Conversion of assembler to cobol

- **From:** Greg Ferro <gferro@sprynet.com>
- **Date:** 2001-10-14T09:39:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BC9A3BC.648BCA16@sprynet.com>`
- **References:** `<98bf16f9.0110090836.219ae0a3@posting.google.com>`

```
The following is from the FAQ for the RETIRE conversion product from
Source Recovery at  www.source-recovery.com

5.  Can SRC convert IBM Assembler or PL/1programs into COBOL?  It
depends.   SRC can convert certain types of business-oriented Assembler
or PL/1 programs to COBOL.   For example, SRC can normally convert to
Assembler programs that primarily use the following macros/SVCs:
OPEN/CLOSE, GET/PUT, READ/WRITE, SAVE/RETURN, and DCB.  Often, however,
Assembler programs cannot be automatically converted to anything
remotely approaching hand written COBOL.

If your assembler programs are doing any bit manipulation or dealing
with exotic data formats (e.g., unsigned packed decimal), you will
probably be forced to do a manual conversion.


David Smith wrote:

> Is there any software out there that will do some rudimentary
> conversion of assembler to COBOL under OS/390.  I have already done
> some research
> on the Web, and the pickings seem slim.  Have I simply not looked
> sufficiently, or does the animal not exist?
```

#### ↳ Re: Conversion of assembler to cobol

- **From:** "Wolf Grossi" <X-news@magro-soft.com>
- **Date:** 2001-10-18T17:44:06+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1003416191.123029@hagakure.utanet.at>`
- **References:** `<98bf16f9.0110090836.219ae0a3@posting.google.com>`

```
Hi David,
    I've done this for a customer in germany.
Just send the bal-source-code to bal@magro-soft.com  including all
macros/procs used, and give it a try.

Regards
Wolf
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
