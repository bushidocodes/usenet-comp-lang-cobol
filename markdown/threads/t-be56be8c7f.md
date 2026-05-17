[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OT -- What is r-code, p-code?

_4 messages · 3 participants · 1998-05_

**Topics:** [`Off-topic and spam`](../topics.md#spam)

---

### OT -- What is r-code, p-code?

- **From:** "mark..." <ua-author-15183209@usenetarchives.gap>
- **Date:** 1998-05-09T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6j5jfn$8mu@Mercury.mcs.net>`

```

Not just the twelve-word glossary answer, but...seriously. I read a lot
but I've never run across a detailed explanation.

My speculative inference would be that r-code is run-time code that
is intermediate between source and binary object code, and that it
requires the presence of a licensed parser/library module to run.

As to p-code, my guess would be about the same.

BTW, thanks for the responses to my earlier question re. screen
painters and the Progress language.

Mark Twenhafel
```

#### ↳ Re: OT -- What is r-code, p-code?

- **From:** "donald tees" <ua-author-44233@usenetarchives.gap>
- **Date:** 1998-05-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be56be8c7f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6j5jfn$8mu@Mercury.mcs.net>`
- **References:** `<6j5jfn$8mu@Mercury.mcs.net>`

```

The term pseudo-code refers to an op-code set for an invented
theoretical machine. You compile to that, then use an emulator
to execute the code.

The idea behind it is three-fold. First of all, the compiler does not
have to be re-written for each new machine on the market. Instead,
one simply re-writes the interpret. Secondly, the code itself is
transportable across platforms in the same manner.

Last but not least, the "machine" can be optimised for a specific
language, and if desirable, "real" hardware designed for it.
```

##### ↳ ↳ Re: OT -- What is r-code, p-code?

- **From:** "mark..." <ua-author-15183209@usenetarchives.gap>
- **Date:** 1998-05-16T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be56be8c7f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-be56be8c7f-p2@usenetarchives.gap>`
- **References:** `<6j5jfn$8mu@Mercury.mcs.net> <gap-be56be8c7f-p2@usenetarchives.gap>`

```

Thanks to Donald and Mark Young for your lesson. Mark Twenhafel


"Donald Tees" writes:

› The term pseudo-code refers to an op-code set for an invented
› theoretical machine. You compile to that, then use an emulator
› to execute the code.
```

#### ↳ Re: OT -- What is r-code, p-code?

- **From:** "mark0..." <ua-author-750539@usenetarchives.gap>
- **Date:** 1998-05-10T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-be56be8c7f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<6j5jfn$8mu@Mercury.mcs.net>`
- **References:** `<6j5jfn$8mu@Mercury.mcs.net>`

```

In article <6j5jfn$8.··.@Mer··s.net>, mar··.@M··.COM (Mark Twenhafel)
writes:

› As to p-code, my guess would be about the same.

Many years ago "p code" meant pseudo-code, which was compiled code, the output
from the UCSD Pascal compiler and possibly a couple other UCSD compilers. It
was not native code, but instead had to be interpreted by a runtime
environment. The code tended to be more compact than native code of the
processor it ran on (when space on floppies were limited, and floppy diskettes
were the mass storage available in the early '80s PCs), but because the p-code
had to be interpreted, it ran slower than native machine code.

I can't place "r-code", but maybe it means "relocatable", such as output from a
compiler (more typically an .OBJ) that can be relocated when linked to form an
executable program (PCs: a .COM or an .EXE).

Mark A. Young
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
