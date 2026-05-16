[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MERANT Netexpress 3.0 cannot find...

_2 messages · 2 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### MERANT Netexpress 3.0 cannot find...

- **From:** Juergen@bop99.ping.de (Juergen Vetter)
- **Date:** 1999-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7TNi-7aWOtB@bop99.ping.de>`

```

I'm having several problems with netexpress version 3.0.

Problem 01:
===========
several compiler directives won't work with the baseinstallation.
This is a set of directives:
----------------------------
echo TESTPGM.OBJ                            > TEMPFILE.RSP
echo TESTPGM.LST, TESTPGM.GRP              >> TEMPFILE.RSP
echo CONFIRM                               >> TEMPFILE.RSP
rem echo MAKESYN "COMP-5" = "COMP"         >> TEMPFILE.RSP
rem echo LITLINK(1)                        >> TEMPFILE.RSP
rem echo CASE                              >> TEMPFILE.RSP
rem echo ASSIGN "EXTERNAL"                 >> TEMPFILE.RSP
rem echo OUTDD "SYSOUT.TXT" AREACHECK      >> TEMPFILE.RSP
rem echo DEFAULTBYTE "0" NOQUERY IBMCOMP   >> TEMPFILE.RSP
COBOL.EXE H:\VETTER\DIENST\DATA2\UP4000\TESTPGM, @TEMPFILE.RSP

Problem 02:
===========
WebSync

There is a serive pack out. But this file (30 MB) is corrupted.
After 23 mb download ended normally. If you want to install the service pack
you got the error: file is corrupted :(

Problem 03:
===========
i use the dos-script at the top in windows98 and it works fine (it's a  
workaround to me to check the linker) but the linker does not work

It tells me:
error (11) c runtime library not found

Which library does the linker need?
I look at the path and add some directories like  
c:\;c:\windows;c:\windows\system.
It does not work

I copied all c++ DLLs in the local directory
It does not work

I copied link.exe from netexpress\base\bin to the local directory
It does not work

Sure, i installed netexpress very well without errors in c:\netexpress.
I used the Netexpress commandline shell
=========================================================================
Micro Focus NetExpress V3
Version 3.0.14 Copyright (C) 1984-1998 Micro Focus Ltd.
URN AXCGG/AA0/00000
* Accepted - CONFIRM
* Compiling H:\VETTER\DIENST\DATA2\UP4000\TESTPGM.cbl
* Checking complete with no errors - starting code generation
* Generating H:\VETTER\DIENST\DATA2\UP4000\TESTPGM
* Data:         384     Code:         440     Literals:         124
Micro Focus NetExpress - CBLLINK utility
Version 3.0.14 Copyright (C) 1984-1998 Micro Focus Ltd.

Executing:cblnames /N /FS /V /S /DTESTPGM.def TESTPGM.obj

Scanning object files:-
TESTPGM.obj
        found public -> TESTPGM
        Creating cbllds.obj
        Creating TESTPGM.def
        Creating cbllds.lnk
        CBLNAMES completed

ERROR: (11) Cannot find C runtime library



=========================================================================
Who can help me?
```

#### ↳ Re: MERANT Netexpress 3.0 cannot find...

- **From:** "Ian Marshall" <Ian.Marshall@merant.com>
- **Date:** 1999-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<81fd72$vj2$1@hyperion.mfltd.co.uk>`
- **References:** `<7TNi-7aWOtB@bop99.ping.de>`

```

WRT problem #2 - the service pack on WebSync has been updated and should
download OK now.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
