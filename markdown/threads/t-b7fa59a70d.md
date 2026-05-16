[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL performance

_6 messages · 5 participants · 1999-09_

---

### Re: COBOL performance

- **From:** "M. Lenz" <Mogens.Lentz@sas.dk>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sftk7$jka$1@news.dknet.dk>`
- **References:** `<7rut5q$ivi@netaxs.com>`

```

This is machine-specific.  On 3090 mainframe, do NOT use comp as these are
converted to Comp-3 by the compiler anyway!

Phil
Lisa or Jeff wrote in message <7rut5q$ivi@netaxs.com>...
>Per the question on performance, if you are processing a high volume
>of records and/or doing a lot of CPU intensive work with each
…[19 more quoted lines elided]…
>handling.
```

#### ↳ Re: COBOL performance

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sfvtt$cr8@dfw-ixnews6.ix.netcom.com>`
- **References:** `<7rut5q$ivi@netaxs.com> <7sftk7$jka$1@news.dknet.dk>`

```
M. Lenz <Mogens.Lentz@sas.dk> wrote in message
news:7sftk7$jka$1@news.dknet.dk...
>
> This is machine-specific.  On 3090 mainframe, do NOT use comp as these are
> converted to Comp-3 by the compiler anyway!
>
> Phil

Used to be true for S/390 (S/370)  - not true with latest COBOL for
this-and-that compilers (if you use the correct compiler options).

Still a good warning that what happens with COMP is
compiler/operating-system dependent.
```

##### ↳ ↳ Re: COBOL performance

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37F00394.18D7E6B0@nbnet.nb.ca>`
- **References:** `<7rut5q$ivi@netaxs.com> <7sftk7$jka$1@news.dknet.dk> <7sfvtt$cr8@dfw-ixnews6.ix.netcom.com>`

```
Huh: Going back to COBOL 63 on DOS releases 18 - 26 and COBOL F on OS360
MFT/MVT COMP was binary and SYNC was advisable when using COMP.  I used
those compilers and those statements hold true for all of the MVS
compilers I have used since then.

Clark Morris, CFM Technical programming Services morrisc@nbnet.nb.ca	

"William M. Klein" wrote:
> 
> M. Lenz <Mogens.Lentz@sas.dk> wrote in message
…[11 more quoted lines elided]…
> --
```

###### ↳ ↳ ↳ Re: COBOL performance

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-09-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sp43a$kmo@dfw-ixnews19.ix.netcom.com>`
- **References:** `<7rut5q$ivi@netaxs.com> <7sftk7$jka$1@news.dknet.dk> <7sfvtt$cr8@dfw-ixnews6.ix.netcom.com> <37F00394.18D7E6B0@nbnet.nb.ca>`

```
I *think* that this was referring to the fact that (historically) IBM
mainframe COBOLs have converted binary (USAGE COMP/COMP-4) items to
"packed-decimal" INTERNALLY before doing many operations on them -
especially when comparing/working with other fields that may be other
USAGEs.  In other words, the compiler generated the packed-decimal
instructions - rather than the binary ones (in many/some cases).
```

#### ↳ Re: COBOL performance

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37EB7DAA.27EEAC12@zip.com.au>`
- **References:** `<7rut5q$ivi@netaxs.com> <7sftk7$jka$1@news.dknet.dk>`

```
"M. Lenz" wrote:
> 
> This is machine-specific.  On 3090 mainframe, do NOT use comp as these
> are converted to Comp-3 by the compiler anyway!
> 

Phil

This is wrong.  Integer maths should be done with COMP.  If you mix
COMP and COMP-3 you will get conversion (don't know if one wins, it
might be COMP-3).

If you use subscripts then use COMP.  This is stated in the MVS
programmers guide on efficiency.

If you are adding small integers together then use COMP it will be
handled in direct machine instructions and not handed to the maths
unit.

The main problem is when you convert from one to another.  I have
often seen WS variables defined as display (not COMP or COMP-3) that
were never written to a terminal, whenever an ADD was done it was
converted into some internal representation and then back out again.

Ken
```

##### ↳ ↳ Re: COBOL performance

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7sglt6$ksk$1@nnrp1.deja.com>`
- **References:** `<7rut5q$ivi@netaxs.com> <7sftk7$jka$1@news.dknet.dk> <37EB7DAA.27EEAC12@zip.com.au>`

```
In article <37EB7DAA.27EEAC12@zip.com.au>,
  Ken Foskey <waratah@zip.com.au> wrote:
> "M. Lenz" wrote:
> >
> > This is machine-specific.  On 3090 mainframe, do NOT use comp as
these
> > are converted to Comp-3 by the compiler anyway!
> >
…[20 more quoted lines elided]…
>
In general you are correct.  However, in my experience this is a
machine, compiler, and OS specific issue. Therefore, if "efficiency" is
truly an issue I think it behooves the developer to understand the
relationship. For example: is sign an overpunch or separate?, does the
processor require conversion or not?, do the OS components care?.  Good
of you to point out that it is worthwhile to check documentation for
pointers on efficiency, or lack thereof.

As for the WS variables of which you speak...I recently worked on a
contract where management (VP software dev) *insisted* that *all* WS
numerics be pictured *display*.  Go figure...
-trblshtr-
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
