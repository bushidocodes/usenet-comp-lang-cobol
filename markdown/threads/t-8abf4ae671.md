[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus compilation error "Load failure (165) on file LBROPEN.GNT"

_2 messages · 2 participants · 2002-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus compilation error "Load failure (165) on file LBROPEN.GNT"

- **From:** b_chat_123@yahoo.co.in (B Chat)
- **Date:** 2002-07-15T22:51:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<454bea81.0207152151.6a2a9524@posting.google.com>`

```
I needed to reinstall my Micro Focus compiler. But after the
installation if I try to Build a new Cobol Program, it is giving an
error message :

"Load failure (165) on file LBROPEN.GNT"

and the .OBJ is not getting built. If I supply the .OBJ from my
backup, it is building the .EXE alright. I searched for the
LBROPEN.GNT file in my HDD but could not find one. I reinstalled the
COBOL with no improvement.

Can any body with running Micro Focus Cobol tell me if there is a
LBROPEN.GNT file in the compiler directory. Or is it some other
problem. I attach the complete error screen that it is throwing :

+++ PWB  [E:\COBOL\BINR] Rebuild

        NMAKE  /z /a /f C:\WINDOWS\TEMP\pwb.mak
        echo EDITOR"MS" NOQUERY ANIM OPT"0" > .\FIRST.DIR
        cobol FIRST.CBL, .\FIRST.obj
DIRECTIVES".\FIRST.DIR";
Microsoft (R) COBOL Optimizing Compiler Version 4.5

COBOL software by Micro Focus
Copyright (C) Microsoft Corporation 1984,1991.  All rights reserved.
Copyright (C) Micro Focus Ltd. 1984,1991.  All rights reserved.


Load failure (165) on file LBROPEN.GNT
```

#### ↳ Re: Micro Focus compilation error "Load failure (165) on file LBROPEN.GNT"

- **From:** Carlos Lages <clages@attglobal.net>
- **Date:** 2002-07-17T21:30:57-03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D360C40.7197B2AD@attglobal.net>`
- **References:** `<454bea81.0207152151.6a2a9524@posting.google.com>`

```
165  means that  you have some programs or libs etc in differents
version of runtime, may be   LBROPEN is embebed in another .EXE program
already linked

Carlos  Lages


B Chat gravada:

> I needed to reinstall my Micro Focus compiler. But after the
> installation if I try to Build a new Cobol Program, it is giving an
…[25 more quoted lines elided]…
> Load failure (165) on file LBROPEN.GNT
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
