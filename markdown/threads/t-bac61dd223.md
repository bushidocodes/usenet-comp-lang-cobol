[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Nested/Stacked programs

_3 messages · 3 participants · 2000-01_

---

### Nested/Stacked programs

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4Gpb4.562$W41.5943@dfiatx1-snr1.gtei.net>`

```
I woudl like some opinions. (Can I get those here?)

Environment: IBM mainframe, mostly batch-sequential processing, latest
COBOL/390 (COBOL for VM) compiler, exclusively QSAM/VSAM (i.e., no DB2) .

I have been using multiple programs per COBOL source file to, essentially,
accomplish user-defined functions. I have been doing this using what I will
call "stacked" construction.

ID DIVISION.
PROGRAM-ID. PROG1
...
END PROGRAM PROG1.
ID DIVISION.
PROGRAM-ID. PROG2.
...
END PROGRAM PROG2.
ID DIVISION.
PROGRAM-ID. PROG3.
...
END PROGRAM PROG3.

However, I see that an option is "nested" construction:

ID DIVISION.
PROGRAM-ID. PROG1
...
ID DIVISION.
PROGRAM-ID. PROG2.
...
END PROGRAM PROG2.
ID DIVISION.
PROGRAM-ID. PROG3.
...
END PROGRAM PROG3.
END PROGRAM PROG1.

My question is this: why would I choose "stacked" versus "nested"
architecture? The only differences I see are in the way data are shared
among stacked v nested programs; but I tend to use multiple programs per
source file specifically to avoid (inadvertent) data sharing.

All ideas/comments welcome.

Michael Mattias
Tal Systems
Racine WI USA
michael.mattias@gte.net
```

#### ↳ Re: Nested/Stacked programs

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84lpoq$d9n$1@nntp5.atl.mindspring.net>`
- **References:** `<4Gpb4.562$W41.5943@dfiatx1-snr1.gtei.net>`

```
IMHO,
  The *only* reason to use nested programs if you want (or are used to - or
think you SHOULD want) "data encapsulation" via GLOBAL vs local data.  With
IBM's compilers (which is what the question referenced) there is some pretty
reliable information that CALLing a nested program "performs better" than a
CALL to a "separately compiled program" (which would include those in a
sequence of programs such as you show - in other words, any program that has
a separate "load/object" module).  This last does point out something that
you may not know (it isn't ALL that clear in the IBM documentation), nested
programs do NOT get separate load/object modules - while a series of programs
in the same compilation run do.

The other "issue" is whether you have "common" programs that are called by
multiple other programs.  Such programs should NOT (IMHO) ever be handled as
nested programs.  It *is* possible to do so, but using a COPY statement just
before the END PROGRAM header of you "main" program - but that means that you
need to recompile every program that CALLs them, whenever anything changes.
(For that matter, I would never include such "common subroutines" in a series
of compiles - for the same reason.)
```

#### ↳ Re: Nested/Stacked programs

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 2000-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84po2p$rsq$1@nnrp1.deja.com>`
- **References:** `<4Gpb4.562$W41.5943@dfiatx1-snr1.gtei.net>`

```
In article <4Gpb4.562$W41.5943@dfiatx1-snr1.gtei.net>,
  "Michael Mattias" <michael.mattias@gte.net> wrote:
> I woudl like some opinions. (Can I get those here?)
>
…[6 more quoted lines elided]…
> using what I will call "stacked" construction.

<snip>

> My question is this: why would I choose "stacked" versus "nested"
> architecture? The only differences I see are in the way data are
…[9 more quoted lines elided]…
> michael.mattias@gte.net

The use of 'nested' programs is a matter of your personal programming
style. If you are a PL/I or C programmer and have to design a new COBOL
program, you may use nested programs instead of procedures and functions
with the same advantages and disadvantages:
- loss of performance (very few)
- advantage of 'local' varibles
- disadvantage of global varables
I see only one real sense for the need of a nested program: To build an
address of a field definded in the working storage section.

The use of what you called 'stacked' sources may or may not be usefull,
it depends on how you manage the version control and the maintenance. As
long as you are the only person, it's OK.
The use of multiple little 'functions' is supported with the new 'DLL
linkage'. You might find it usefull to use this kind of calls (including
long names).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
