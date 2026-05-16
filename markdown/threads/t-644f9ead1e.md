[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Makefile for Microsoft Nmake V1.2 running under Project Work Bench

_2 messages · 2 participants · 1999-06_

---

### Makefile for Microsoft Nmake V1.2 running under Project Work Bench

- **From:** "Chloe" <greg@primesoft.co.nz>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7kulgv$pud$1@newsource.ihug.co.nz>`

```
Can anyone tell me what the structure of a Makefile is that will compile and
link all .cbls to produce corresponding .exes in the current directory only
for the exes that are out of date?
This should be easy but not being a programmer the manuals are a little
tricky to understand. All makefiles I have been able to automatically
produce with PWB link all .objs to produce a single exe not individual
.exes.
I have experimented with pre-defined inference rule .cbl.exe and pre-defined
macro $< and suspect I have to do something with filename macro $* but can't
get it to work. The current directory contains about 180 .cbls
Any help would be appreciated.
```

#### ↳ Re: Makefile for Microsoft Nmake V1.2 running under Project Work Bench

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-06-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3773858A.6B4287C7@zip.com.au>`
- **References:** `<7kulgv$pud$1@newsource.ihug.co.nz>`

```
Chloe wrote:
> 
> Can anyone tell me what the structure of a Makefile is that will
> compile and link all .cbls to produce corresponding .exes in the
> current directory only for the exes that are out of date?

> This should be easy but not being a programmer the manuals are a
> little tricky to understand. All makefiles I have been able to
> automatically produce with PWB link all .objs to produce a single exe
> not individual .exes.

> I have experimented with pre-defined inference rule .cbl.exe and
> pre-defined macro $< and suspect I have to do something with filename
> macro $* but can't get it to work. The current directory contains
> about 180 .cbls

> Any help would be appreciated.


For a thorough discussion on Make look at the GNU make manual at
http://www.ultranet.com/~pauld/gmake/  (about 122 pages).  It is a
superset but most of what you want is in there just try and keep
things simple.

You can use GNU make though I have not tried it (yet).

To see a multiple source version of make download the parser
project from http://www.zipworlc.com.au/~waratah (yes I finally
got one) and look at it's make file.  It creates different targets
but to create a bank of programs make the default tag (the first
one) contain a list of programs.

I will eventually refine this makefile.  Email me any questions.

Good luck
Ken
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
