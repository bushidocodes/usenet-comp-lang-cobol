[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MF Cobol and OS/2 DLLs

_2 messages · 2 participants · 1996-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MF Cobol and OS/2 DLLs

- **From:** "dan..." <ua-author-14520244@usenetarchives.gap>
- **Date:** 1996-07-29T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4tm697$avp@ktk2.smartt.com>`

```

I have a problem with Micro Focus Cobol calling functions in an OS/2 DLL.

I have developed an OS/2 DLL in C for a client. His EXE is written in
Micro Focus Cobol. I understand that he can link with the LIB file I have
provided and successfully call the functions in the DLL.

The problem appears when he uses something called Animator (a visual
debugger of some kind?). He says the functions are not found or not
executed. He has talked with some people at MF and was told that he
cannot call functions in DLLs if he wants to use Animator to debug his app?
(His code is compiled to some sort of p-code?)

If I include debug information in my DLL during compiling and linking, will
the Animator thingie be happy? What is the intermediate p-code my client
mentioned? How (oh, how?!) can a debugger stand in the way of dynamic
linked code?

I'm afraid I don't have a clue when it comes to Cobol, but I'm hoping that
someone here has experience with linking MF Cobol programs to OS/2 DLLs
and might shed some light on this problem.

Many thanks in advance!

//----------------------------------------------------------
// "Daniel Helgason"
//
```

#### ↳ Re: MF Cobol and OS/2 DLLs

- **From:** "dave manton" <ua-author-17087150@usenetarchives.gap>
- **Date:** 1996-07-31T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-393ee6fec2-p2@usenetarchives.gap>`
- **In-Reply-To:** `<4tm697$avp@ktk2.smartt.com>`
- **References:** `<4tm697$avp@ktk2.smartt.com>`

```

I assume the COBOL is compiled to int code in order to Animate it? If
this is the case, then the COBOL runtime needs to be told about the
functions that are available in the C DLL before it can locate and call
them. If we assume that the DLL is called mydll.dll, then this can
be resolved by planting the following 'set .. to entry ..' statement
in the COBOL program before the first call to a function in the DLL:

working-storage section.
01 tmppptr procedure-pointer.
:
procedure division.
set tmppptr to entry "mydll.dll" *> load entry points for this dll

*> now call an entry point/function in the DLL
call "aFunctionInMydll" using ...

Dave.

› dan··.@sma··t.com  (Daniel Helgason) wrote in article
› <4tm697$a.··.@ktk··t.com>...
…[33 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
