[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol calling C

_2 messages · 2 participants · 1999-04_

---

### Cobol calling C

- **From:** 9416617@my-dejanews.com
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ej1am$uak$1@nnrp1.dejanews.com>`

```
I have a program written in Borland C. I wish to call this from a COBOL
program written in Microfocus Netexpress. Where do I start. Do I create a dll
with the c program and link this to the cobol program in a new project or
what?

Can some one please tell me how I go about this starting from the start with
just the two files cobolprogram.cbl and cprogram.cpp.

Please help as this is a crisis!!
Cheers,
Dec.

-----------== Posted via Deja News, The Discussion Network ==----------
http://www.dejanews.com/       Search, Read, Discuss, or Start Your Own
```

#### ↳ Re: Cobol calling C

- **From:** Kevin Digweed <ked@mfltd.co.uk>
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370DDA77.2583EC7B@mfltd.co.uk>`
- **References:** `<7ej1am$uak$1@nnrp1.dejanews.com>`

```
9416617@my-dejanews.com wrote:
> 
> I have a program written in Borland C. I wish to call this from a COBOL
…[5 more quoted lines elided]…
> just the two files cobolprogram.cbl and cprogram.cpp.

It depends on what you want the architecture of your deliverables to
be, but here are three basic ways:

1) Link the C and COBOL objects together.
   Create a .obj from the .cpp file and include the .obj in your
   COBOL project. Your project must obviously create a .EXE or .DLL
   for this to work. 

2) Dynamically load the C DLL.
   Create a DLL from the C code and load it in COBOL using:
   01 pptr USAGE PROCEDURE-POINTER.
   PROCEDURE DIVISION.
        SET pptr TO ENTRY "DLLNAME.DLL"

   The entry points in the DLL should now be visible to your COBOL
   code. This will work from .INT and .GNT code also.

3) Import the C DLL.
   Create a DLL from the C code and link the COBOL project with the
   import library for that DLL (the same way as option 1).
   You may need to compile your COBOL code with the LITLINK option
   (or use the equivalent call convention on those CALLs).
   
This will work for Microsoft VC++ - so unless there are any Borland
specific issues, you should be OK. Note that the default NetExpress
COBOL calling convention is equivalent to Microsoft's __cdecl (the
default for C, also).

Cheers, Kev.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
