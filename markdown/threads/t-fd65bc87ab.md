[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu NetCOBOL runtime error

_2 messages · 1 participant · 2003-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu NetCOBOL runtime error

- **From:** "Alex Harris" <nu@nu.nu>
- **Date:** 2003-11-03T19:41:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vqdv33j03sn233@corp.supernews.com>`

```
Getting this error:

[code]
cobol-rts: HALT: JMP0311I-U [PID:00000F65 TID:00000001] MISSING ALLOCATION.
FILE=DOCIN. PGM=PROGRAM-3-2
Abort
[/code]

It's a cobol main program, which inputs from a Line Sequential data file and
then calls a C++ function.  I'll post the code if necessary.
```

#### ↳ Re: Fujitsu NetCOBOL runtime error

- **From:** "Alex Harris" <nu@nu.nu>
- **Date:** 2003-11-03T20:00:20-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vqe06vfj2pje2b@corp.supernews.com>`
- **References:** `<vqdv33j03sn233@corp.supernews.com>`

```
Sorry everyone.  Figured it out.  Wrong file name.  Doh!

"Alex Harris" <nu@nu.nu> wrote in message
news:vqdv33j03sn233@corp.supernews.com...
> Getting this error:
>
> [code]
> cobol-rts: HALT: JMP0311I-U [PID:00000F65 TID:00000001] MISSING
ALLOCATION.
> FILE=DOCIN. PGM=PROGRAM-3-2
> Abort
> [/code]
>
> It's a cobol main program, which inputs from a Line Sequential data file
and
> then calls a C++ function.  I'll post the code if necessary.
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
