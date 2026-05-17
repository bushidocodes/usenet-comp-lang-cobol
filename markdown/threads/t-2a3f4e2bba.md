[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# HELP! Microfocus COBOL V4.0 Thunking Kit

_1 message · 1 participant · 1996-04_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### HELP! Microfocus COBOL V4.0 Thunking Kit

- **From:** "fco..." <ua-author-17087129@usenetarchives.gap>
- **Date:** 1996-04-25T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4lpj5t$mg1@maggie.clear.co.nz>`

```

I'm working on 16-bit to 32-bit COBOL migration
using Microfocus COBOL v4.0 and I have a couple
of issues regarding this matter:

ISSUE #1
---------
I've been going through the documentation about this process.
Chapter 8 of the reference manual MicroFocus
Object COBOL Programmer's Guide to Writing Programs
discusses interfacing between 16-bit and 32-bit modules.
I noticed however, in the sample script to build the modules
on pages 8-24 to 8-25 the following:

A) To create the thunk entry table support DLL,
the object module MFGET16.OBJ is required, which
I DON'T FIND IN THE V4.0 package.

B) Linking of the COBOL program cblswap contains a
reference to MFTHUNK.LIB and MFGET16.LIB which I cannot
find in the v4.0 package

I know that these modules existed in an earlier demo copy of
a 32-bit SDK, but I just can't find them in the v4.0 package.

I'm just wondering if the thunking kit was not included in the
COBOL V4.0 package I received or I'm just missing something.

ISSUE #2
--------
Since I don't have the modules MFTHUNK.LIB and MFTHUNK.DLL,
I decided to do the thunking by writing a 32-bit C DLL (compiled using IBM CSet++ 2.1)
that calls the 16-bit C support module DLL (compiled using Microsoft C 6.0).
Everything worked fine AS LONG AS THE COBOL PROGRAM IS COMPILED TO AN INTERMEDIATE CODE (.INT).
Once I compile it to a GNT or create an EXE, then the COBOL program falls over after a couple of
successful calls to the 32-bit thunk DLL. The error code is 114 - attemp to access item
beyond bounds of memory.

Why is my .INT code working but not the .GNT or .EXE codes?
By the way, I used CBLLINK to link-edit the COBOL program.

I sent this same mail to the company that supports us about four days ago but haven't got
a response yet, so I decided to post this here hoping to get a response.

I would very much appreciate any form of assistance on this matter.

Ferdinand Contreras
IS Specialist
CLEAR Communications Ltd.
49 Symonds St.
Private Bag 92143
Auckland, NZ

ph: 64 9 912-4886
email: fco··.@cle··o.nz
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
