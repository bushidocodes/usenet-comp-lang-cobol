[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Mixed 16 bit and 32 bit programming

_3 messages · 3 participants · 1998-11_

---

### Mixed 16 bit and 32 bit programming

- **From:** avi toren <atoren@unique-ltd.co.il>
- **Date:** 1998-11-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365D2422.D0E46EBE@unique-ltd.co.il>`

```
Hi!

Does anyone have any experience with mixed 32 and 16 bit programming. We
have some systems written primarily with 16 bit MF COBOL, but some newer
ones done with the 32 bit version. We have 2 problems:

1) Whenever we open an Sequential ISAM file under 16 bit, then pass
something on to the 32 bit program, the files get locked out and no
other users can get to them until they are release by the 32 bit program
(we have similiar problems going the other way also)

2) We also have a library of routines written in ASM (that we do not
have the sources for) that are in 16 bit and work for use fine. Does
anyone know of a way we can get to these routines from a 32 bit app?

Thanks for any help

Avi Toren
Unique Computer Servicesa
atoren@unique-ltd.co.il
```

#### ↳ Re: Mixed 16 bit and 32 bit programming

- **From:** Frank Pohlmann <Frank.Pohlmann@baeurer.de>
- **Date:** 1998-11-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<365EA853.31D4A957@baeurer.de>`
- **References:** `<365D2422.D0E46EBE@unique-ltd.co.il>`

```
Why don't use the 32 bit compiler for the old programs and only work with 32
bit programs?

avi toren schrieb:

> Hi!
>
…[17 more quoted lines elided]…
> atoren@unique-ltd.co.il
```

##### ↳ ↳ Re: Mixed 16 bit and 32 bit programming

- **From:** Barticus@att.spam.net (Randall Bart)
- **Date:** 1998-11-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3660d73f.34383599@netnews>`
- **References:** `<365D2422.D0E46EBE@unique-ltd.co.il> <365EA853.31D4A957@baeurer.de>`

```
'Twas Fri, 27 Nov 1998 14:25:39 +0100, when Frank Pohlmann
<Frank.Pohlmann@baeurer.de> illuminated comp.lang.cobol thusly:

>Why don't use the 32 bit compiler for the old programs and only work with 32
>bit programs?

>> 2) We also have a library of routines written in ASM (that we do not
>> have the sources for) that are in 16 bit and work for use fine. Does
>> anyone know of a way we can get to these routines from a 32 bit app?

If you have a compiler that can convert sourceless 16-bit ASM objects into
32 bit objects, that tool is worth many millions of dollars.  Even with
the source, converting 16-bit ASM to 32-bit ASM isn't automatic.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
