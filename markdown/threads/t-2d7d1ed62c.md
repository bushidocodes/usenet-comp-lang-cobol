[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# accepting record and block sizes

_3 messages · 3 participants · 2000-04_

---

### accepting record and block sizes

- **From:** John Roberts <puck@bestweb.net>
- **Date:** 2000-04-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38F5A95D.BF20C4B8@bestweb.net>`

```
I'm working with IBM Cobol for VSE/ESA 1.1.0 on a IBM mainframe.
We have programs written in assembler that receive the record and block
sizes of input or output files from parameter cards and modify the dtf
accordingly.
Is there a way to accomplish this in Cobol?
```

#### ↳ Re: accepting record and block sizes

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-04-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8dg5vm$bp6$1@nntp9.atl.mindspring.net>`
- **References:** `<38F5A95D.BF20C4B8@bestweb.net>`

```
I know MVS (OS/390) rather than VSE - but you PROBABLY can pass the FD name
to your assembler program.  This works on MVS for QSAM but *not* VSAM files.
My guess is that it will also work for SAM (?) on VSE - but won't swear to
it.
```

##### ↳ ↳ Re: accepting record and block sizes

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-04-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38FC5FE5.4EFBB356@zip.com.au>`
- **References:** `<38F5A95D.BF20C4B8@bestweb.net> <8dg5vm$bp6$1@nntp9.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> I know MVS (OS/390) rather than VSE - but you PROBABLY can pass the
…[13 more quoted lines elided]…
> > Is there a way to accomplish this in Cobol?

I heard somewhere that you could read any file by using the clause
block contains zero records and record contain zero characters. You
define your record to the largest possible size.

I have never tried it and I cannot remember where this thought came
from, caveat a emptor.  I have kept this concept to try when and if I
needed to.  If you try let me know the results.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
