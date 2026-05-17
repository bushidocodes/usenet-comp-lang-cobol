[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL II calls to OS/VS COBOL programs in batch

_3 messages · 3 participants · 1996-05_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### COBOL II calls to OS/VS COBOL programs in batch

- **From:** "nra..." <ua-author-17086989@usenetarchives.gap>
- **Date:** 1996-05-07T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4mqffo$pl8@charm.magnus.acs.ohio-state.edu>`

```

In a batch call from a COBOL II program to a OS/VS COBOL program we
are getting an S206 abend, invalid parm address.
Has anyone encountered this problem?
```

#### ↳ Re: COBOL II calls to OS/VS COBOL programs in batch

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1996-05-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-56ff3d0da3-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4mqffo$pl8@charm.magnus.acs.ohio-state.edu>`
- **References:** `<4mqffo$pl8@charm.magnus.acs.ohio-state.edu>`

```

There are a large number of possibilities which can cause this symptom. A
total explanation of all of the possibilities takes several hours and
about 100 pages of notes in the "Planning COBOL Migration" course that I
wrote / teach.

Typical problems revolve around the following issues:

1. Both the CALLer and CALLed program must use the same compiler option
that controls binding of run-time modules to compiled code. This option
is the RES/NORES option in both the OS/VS and VS COBOL II compilers.
Recommendation - compile both programs with RES.

2. If a static call is used between the VS COBOL II program and the OS/VS
called program, then the VS COBOL II program MUST be operating in AMODE
24, be resident in the 24 bit space, and pass any parms to the OS/VS COBOL
program in the 24 bit space.

Recommendation - specify DATA(24) on the VS COBOL II compilation, force
AMODE(24) at linkage edit time.

3. If a dynamic call is used between the VS COBOL II program and the
OS/VS COBOL called program, then the VS COBOL II program need only insure
that the data passed to the called program is in the 24 bit space.

Recommendation - specify DATA(24) on the VS COBOL II compilation.

Very Important. You must insure that all run-time components (csects
which start with ILBOxxxx or IGZxxxxx) are from the VS COBOL II or LE/370
run-time libraries. Back level ILBO modules (such as those from OS/VS
COBOL RTL) will cause all sorts of strange results.

Bottom line - this construct will work. There are literally dozens of
permutations of RES/NORES, AMODE, connectivity (static / dynamic), RMODE,
DATA(24/31). Only a limited number will work. The above give some of the
most straight forward cases. A full enumeration of all cases literally
takes hours - I would be happy to teach the course at your location if you
want the long version.

Rex Widmer
Builder of software archeology tools and other strange programs to help
survive in a legacy based world.
```

#### ↳ Re: COBOL II calls to OS/VS COBOL programs in batch

- **From:** "7002..." <ua-author-17086225@usenetarchives.gap>
- **Date:** 1996-05-09T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-56ff3d0da3-p3@usenetarchives.gap>`
- **In-Reply-To:** `<4mqffo$pl8@charm.magnus.acs.ohio-state.edu>`
- **References:** `<4mqffo$pl8@charm.magnus.acs.ohio-state.edu>`

```

On 8 May 1996, Nathan R Rausch
wrote:

› In a batch call from a COBOL II program to a OS/VS COBOL program we
› are getting an S206 abend, invalid parm address.
› Has anyone encountered this problem?


There are many possible causes. What is the return code in
register 15, or two hex digits appended to the abend code in the
message: S206-xx? There may also be a CSV message that gives
more information.

Here's a guess about the likely cause, based on what you told
us. This is apparently a dynamic call (otherwise you wouldn't
get an S206). Is the COBOL II program compiled with the RENT
option? If so, it is running above the 16 meg line, but OS/VS
COBOL cannot access parameters above the line. If this is the
problem, you need to either use NORENT or use the DATA(24)
option when you compile the VS COBOL II program. DATA(24) will
force Working Storage below the line, where OS/VS COBOL can look
at it.


Robert J. Sandler <700··.@com··e.com>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
