[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calling "C" DLLs from MF Cobol Programs

_2 messages · 2 participants · 1995-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Calling "C" DLLs from MF Cobol Programs

- **From:** "maco..." <ua-author-17087929@usenetarchives.gap>
- **Date:** 1995-09-11T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83@macross.win-uk.net>`

```
I am evaluating a vendor supplied DLL (With minimal technical
documentation) and am attempting to build a MF Cobol (3.2) program
in Windows to call it. The DLL has multiple entry points which are
listed in a supplied .DEF file.

I've had a look at the documentation supplied by MF and at their
forum on Compuserve and I've used some of the examples there related
to DLLs. However, I've been unable to get access to the specified
entry points in the .DLL. From my look at these various sources it
would appear I should perform a "CALL" with the DLL name. If this
completes successfully the DLL should be loaded into memory. The
various entry points can then be "CALL"ed using their entry point
names. Is this correct or is there something I've missed (Such as
WINAPI) ???

The only other problem is that the documentation specifies that
the "far" option will be required to access the DLL. Is this
relevant to cobol programs as I can find no reference to it in the
many MF cobol manuals and if so is there any way round it?

Any help would be appreciated
```

#### ↳ Re: Calling "C" DLLs from MF Cobol Programs

- **From:** "684..." <ua-author-5610386@usenetarchives.gap>
- **Date:** 1995-09-11T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-fceb3e2dab-p2@usenetarchives.gap>`
- **In-Reply-To:** `<83@macross.win-uk.net>`
- **References:** `<83@macross.win-uk.net>`

```
In article <8.··.@mac··k.net>
mac··.@mac··k.net (Charles Maconachie) writes:

› 
› I am evaluating a vendor supplied DLL (With minimal technical
…[11 more quoted lines elided]…
› 
Hi:
I tried this a few years ago. You are right. You need (probably)
to call using Winapi, since the windows standard passes parms like
Pascal, instead of the COBOL standard like C.

thus CALL Winapi "__TheDllentry" using by value etc...

The far pointer stuff will be solved if you compile your cobol
as large model program. That way the address will be far, i.e. 32 bit.

Another possibility besides calling the library name to load it
would be call the windows API function LoadLibrary.

01 ws-handlelib pic s9(04) comp-5.
Call winapi "__LoadLibrary" using by reference "thestuff.dll"
returning ws-handlelib
Later, after library has been finished with, use freelibary...
Call winapi "__FreeLibrary" using by value ws-handlelib.
Good luck,

Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
684··.@lms··d.com
LMSC5: Tons of Beautiful Big Blue Iron...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
