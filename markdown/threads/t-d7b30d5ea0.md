[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How do I build an EXE of a C program calling NetExpress COBOL

_3 messages · 3 participants · 1998-12_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How do I build an EXE of a C program calling NetExpress COBOL

- **From:** pitchl@tdbank.ca (Lew Pitcher)
- **Date:** 1998-12-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36659f61.3892095@news21.bellglobal.com>`

```
NetExpress 2 comes with (sparse) online documentation which mentions it's ability
to be used in a mixed-language environment. The examples extracted from the
documentation (like pulling teeth, without Novocain) all relate to COBOL calling
C, but the notes refer to a C-calling-COBOL scenario as well.

The *closest* I can get to C-calling-COBOL is to build a .OBJ of my C code, and
an .OBJ of my COBOL code, then use CBLLINK to link them statically together.
CBLLINK doesn't like my C code having a main() function, so I had to rename it
and use the -M option to get it to accept. I built an EXE, but it fails on
trying to initialize \.....\CBLRTSM.DLL.

What I want is to be able to build a C-only EXE file that calls a COBOL DLL.
I'm using Microsoft Visual C++ v5 to build the C program, but LINK complains
about missing externals (_cobolprogramname). There's *no* information in regards
to using DEF files to resolve the name, nor is there any information in VC++
as to how to import the COBOL DLL/entrypoint (yes, I've looked at _declspec(dllimport),
but all it does is change the missing external name to _imp_cobolprogramname).

Can a C program (EXE or DLL) call a NetExpress COBOL program (without resorting to
LoadLibrary()/GetProcAddress() calls)? What do I have to do to make it so (
_declspec or #pragma in the C code, changes to the cobol.DEF file, parameters to
LINK or CBLLINK)?

Does anyone have experience here?



Lew Pitcher
System Consultant, Delivery Systems Architecture
Toronto Dominion Bank

(pitchl@tdbank.ca)


(Opinions expressed are my own, not my employer's.)
```

#### ↳ Re: How do I build an EXE of a C program calling NetExpress COBOL

- **From:** "David Sands" <davs@mfltd.co.uk>
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7460ac$ajn@hyperion.mfltd.co.uk>`
- **References:** `<36659f61.3892095@news21.bellglobal.com>`

```
Hi Lew,

I think you are almost there with the _declspec(dllimport).

You will need to link with a LIB file which is created when the COBOL DLL is
built.

If you use use CBLLINK -D -K COBSUB.CBL this will create COBSUB.DLL and also
a COBSUB.LIB that you need to use when linking the C module.

Using the following commands on MS VC4 work fine on my system.

    CBLLINK -D -K COBSUB.CBL
    CL CCALLER.C COBSUB.LIB

Hope this helps.
David.


Lew Pitcher wrote in message <36659f61.3892095@news21.bellglobal.com>...
>NetExpress 2 comes with (sparse) online documentation which mentions it's
ability
>to be used in a mixed-language environment. The examples extracted from the
>documentation (like pulling teeth, without Novocain) all relate to COBOL
calling
>C, but the notes refer to a C-calling-COBOL scenario as well.
>
>The *closest* I can get to C-calling-COBOL is to build a .OBJ of my C code,
and
>an .OBJ of my COBOL code, then use CBLLINK to link them statically
together.
>CBLLINK doesn't like my C code having a main() function, so I had to rename
it
>and use the -M option to get it to accept. I built an EXE, but it fails on
>trying to initialize \.....\CBLRTSM.DLL.
>
>What I want is to be able to build a C-only EXE file that calls a COBOL
DLL.
>I'm using Microsoft Visual C++ v5 to build the C program, but LINK
complains
>about missing externals (_cobolprogramname). There's *no* information in
regards
>to using DEF files to resolve the name, nor is there any information in
VC++
>as to how to import the COBOL DLL/entrypoint (yes, I've looked at
_declspec(dllimport),
>but all it does is change the missing external name to
_imp_cobolprogramname).
>
>Can a C program (EXE or DLL) call a NetExpress COBOL program (without
resorting to
>LoadLibrary()/GetProcAddress() calls)? What do I have to do to make it so (
>_declspec or #pragma in the C code, changes to the cobol.DEF file,
parameters to
>LINK or CBLLINK)?
>
…[11 more quoted lines elided]…
>(Opinions expressed are my own, not my employer's.)
```

#### ↳ Re: How do I build an EXE of a C program calling NetExpress COBOL

- **From:** john@watkins.cix.[nospam]co.uk (John Watkins)
- **Date:** 1998-12-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<memo.19981203220911.136G@john.watkins.cix.co.uk>`
- **References:** `<36659f61.3892095@news21.bellglobal.com>`

```
> Can a C program (EXE or DLL) call a NetExpress COBOL program (without 
> resorting to LoadLibrary()/GetProcAddress() calls)? 

That's what we had to do in WorkBench v4.0 - I wrote a COBOL.DLL and my 
colleague wrote the C/C++ program and used GetProcAddress().


+--------------+------------------------------------+
| John Watkins | mailto:john@watkins_dot_cix.co.uk  |
|              | http://www_dot_cix.co.uk/~watkins/ |
+--------------+------------------------------------+
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
