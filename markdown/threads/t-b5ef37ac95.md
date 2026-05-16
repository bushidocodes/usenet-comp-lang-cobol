[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu Linker

_2 messages · 2 participants · 2004-01_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu Linker

- **From:** davewhitehead@bigfoot.com (DaveW)
- **Date:** 2004-01-14T03:26:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4e06385e.0401140326.31524fd4@posting.google.com>`

```
Just loaded the Fujitsu CobolV3 and tried to Link Sample1 for
starters. Received the following message.

NMAKE : fatal error U1077: 'C:\FSC\PCOBOL32\LINK' : return code '0x68'
Stop.

Microsoft (R) 32-Bit Incremental Linker Version 3.00.5270
Copyright (C) Microsoft Corp 1992-1995. All rights reserved.

/OUT:C:\FSC\PCOBOL32\samples\SAMPLE1\Sample1.exe
C:\FSC\PCOBOL32\samples\SAMPLE1\Sample1.OBJ
C:\FSC\PCOBOL32\PROJECT.RES
C:\FSC\PCOBOL32\F3BICIMP.LIB
C:\FSC\PCOBOL32\LIBC.LIB
C:\FSC\PCOBOL32\KERNEL32.LIB
C:\FSC\PCOBOL32\USER32.LIB
LINK : fatal error LNK1561: entry point must be defined
Linking files ended.
Please close the window.

Any suggestion gratefully accepted
```

#### ↳ Re: Fujitsu Linker

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-14T10:24:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401141024.4c70db9b@posting.google.com>`
- **References:** `<4e06385e.0401140326.31524fd4@posting.google.com>`

```
davewhitehead@bigfoot.com (DaveW) wrote

> LINK : fatal error LNK1561: entry point must be defined

You need to specify that the program you are compiling is 'MAIN'. 
This is done with a compiler option.  Either put MAIN in the compiler
options dialog box or add a line to the top of your source code that
is '     @OPTIONS MAIN'.

One program in a link of several programs that are to be linked
together must be marked as MAIN and this is the entry point. Programs
that are CALLed are not marked as MAIN when compiled.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
