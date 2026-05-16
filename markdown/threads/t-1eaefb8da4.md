[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compiling in MicroSOFT COBOL 4.5

_6 messages · 5 participants · 2000-08_

---

### Compiling in MicroSOFT COBOL 4.5

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-08-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39a7c957.122682459@207.126.101.100>`

```
Query - I'm trying to help someone compile.

I want to compile then link with MicroSoft 4.5 - and create a 16 Bit
Windows application, including calls to an external C program in a LIB
file.  

Does anyone have the command lines for compile and link?

Does MicroSoft COBOL 4.5 even create Windows 3.1 executables?
---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Compiling in MicroSOFT COBOL 4.5

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-08-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8o8nhh$1802$1@news.hitter.net>`
- **References:** `<39a7c957.122682459@207.126.101.100>`

```
Microsoft COBOL 4.5 is equivalent to Micro Focus COBOL 2.5.

The Micro Focus 2.5 reference manuals do not mention Microsoft
Windows, at all. (OS/2 and Presentation Manager are mentioned.)

I think it unlikely that MS COBOL 4.5 could be used to create
Windows executable, directly. IIRC, MS COBOL 5.0, equivalent to
MF COBOL 3.0, was the first to have the ability to create Windows
executables, directly. (Actually, IIRC, it was called Microsoft COBOL
for Windows, 5.0.)
------------------
Rick Smith

Thane Hubbell wrote in message <39a7c957.122682459@207.126.101.100>...
>Query - I'm trying to help someone compile.
>
…[9 more quoted lines elided]…
>My personal web site: http://www.geocities.com/Eureka/2006/
```

##### ↳ ↳ Re: Compiling in MicroSOFT COBOL 4.5

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 2000-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ocfhj$2bns$1@news.hitter.net>`
- **References:** `<39a7c957.122682459@207.126.101.100> <8o8nhh$1802$1@news.hitter.net>`

```
[posted and mailed]

I located an MSDN article that addresses your request. A copy
of the article is attached to the e-mail only!

The article is titled "How to Pass Parameters Between COBOL
and C". Among the sample code given is a COBOL 4.5 Quickwin
program calling a MS C 6.0 DLL for Windows 3.0. Other samples
include calling C and linking COBOL and C. Code and command
lines for compiling and linking are also provided. (15 pages ).
------------------
Rick Smith

Rick Smith wrote in message <8o8nhh$1802$1@news.hitter.net>...
[...]
>I think it unlikely that MS COBOL 4.5 could be used to create
>Windows executable, directly.

Oops! I proved myself wrong.
[...]
>
>Thane Hubbell wrote in message <39a7c957.122682459@207.126.101.100>...
…[8 more quoted lines elided]…
>>Does MicroSoft COBOL 4.5 even create Windows 3.1 executables?
```

#### ↳ Re: Compiling in MicroSOFT COBOL 4.5

- **From:** jay_moseley@attglobal.net (Jay Moseley, CCP)
- **Date:** 2000-08-26T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39a7f3f8.6703429@news1.attglobal.net>`
- **References:** `<39a7c957.122682459@207.126.101.100>`

```
On Sat, 26 Aug 2000 13:44:22 GMT, thaneH@softwaresimple.com (Thane
Hubbell) wrote:

>Query - I'm trying to help someone compile.
>
…[6 more quoted lines elided]…
>Does MicroSoft COBOL 4.5 even create Windows 3.1 executables?

I have MicroSoft COBOL 5.0, so I don't know how much changed between
the two versions, but here is the blurb for compiling Windows programs
from the included samples.txt file:

======================================================================
WINDOWS API SAMPLES
See Programming for Windows

\cobol\samples\windows\compress.cbl
\cobol\samples\windows\sysmets.cbl
\cobol\samples\windows\wincalc.cbl
\cobol\samples\windows\winhello.cbl

Compile:
  cobol foo target(286) deffile deffiletype"windows" nodll;

Link:
 Static-linked run-time system Windows API:
   link foo+cblwina,,,lcobolw+lcobol+libw/nod/noe;

 Shared run-time system Windows API:
   link foo+cblwina,,,coblibw+coblib+libw/nod/noe;

======================================================================
WINDOWS API CALLING WINDOWS DLL SAMPLE
See Programming for Windows, Chapter 2, and windll.bat

\cobol\samples\windows\winmain.cbl
\cobol\samples\windows\cobdll.cbl

Compile:
  cobol winmain target(286) deffile deffiletype"windows" nodll;
  cobol cobdll target(286) deffile deffiletype"windows" dll;

Explicitly Link:
  link winmain+cblwina,winmain.exe,,lcobolw+lcobol+libw,
 winmain.def/nod/noe;
  link cobdll+cblwinl+libinit,cobdll.dll,,lcobolw+lcobol+libw,
 cobdll.def/nod/noe;
======================================================================

If I can look up specific questions in my manuals, let me know.

Regards,

Jay Moseley, CCP

http://jaymoseley.jumpcomputers.com/
```

##### ↳ ↳ R: Compiling in MicroSOFT COBOL 4.5

- **From:** "Pasquale Fusco" <pafusc@tin.it>
- **Date:** 2000-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ob7er$t95$1@nslave1.tin.it>`
- **References:** `<39a7c957.122682459@207.126.101.100> <39a7f3f8.6703429@news1.attglobal.net>`

```
Jay Moseley, CCP <jay_moseley@attglobal.net
>wrote in message 39a7f3f8.6703429@news1.attglobal.net...
> On Sat, 26 Aug 2000 13:44:22 GMT, thaneH@softwaresimple.com (Thane
> Hubbell) wrote:

Jay,
I believe that Thane is trying to the responses also for me;
also if it as is not, I am much interested to this matter.
I use Microsoft Cobol 4.5 from around 10 years,
but I have not ever used the relative Windows 3.0 support,
since I had carried my Tool of development,
realized in the preceding releases of Cobol.
Now, that I am about to do new choices, I have met this
problem.
===================================================
Windows 3.0 Support (.. of MS Cobol 4.5)
CBLSSEG.DLL    Support DLL used by all COBOL Windows programs
CBLWINB.OBJ    Startup module for batch programs running under Windows
CBLWINC.OBJ    Startup module for QuickWin applications
CBLWING.OBJ    Startup module for COBOL GUI applications
CBLWINL.OBJ    Startup module for Dynamic Link Libraries
COBAPIDW.LIB   Link library for QuickWin applications
COBAPIW.LIB    Link library for GUI applications and DLLs
DWSKEL.DEF     .DEF file for QuickWin applications
LIBW.LIB       Link library for Windows applications
LLIBCEW.LIB    Link library for Windows applications
LDLLCEW.LIB    Link library for Windows DLLs
LIBENTRY.OBJ   Needed for Windows DLLs
WINSTUB.EXE    Needed for Windows applications
RC.EXE         Windows Resource Compiler
RCPP.EXE
RCPP.ERR
SDKPAINT.EXE   Windows Icon, Cursor and Bitmap painter
SDKPAINT.DAT

CLBWINA.obj is missing respect to 5.0.

> ======================================================================
> WINDOWS API SAMPLES  (of 5.0)
…[17 more quoted lines elided]…
> ======================================================================
The directives:  foo  deffiletype"windows"  nodll
they didn't exist on 4.5
===================================================
WINDOWS API DEMO
\cobol\demo\windows\sysmets.cbl
\cobol\demo\windows\wincalc.cbl
\cobol\demo\windows\winhello.cbl

I don't have the documentation more for see the commands
for the compilation and link of these programs.
Maybe in past I have proven them also, but now not
here I succeed more.
Last proof:
cobol winhello,,,,;
link winhello+cblwinl,,,libw+lcobol,winhello;
(winhello.def is in the package)

There are not errors, but no "sign of life"
in execution.
===================================================
If I don't resolve the problem with MS Cobol 4.5
 (I thought that pits the last intervention of Microsoft
on the Cobol!!) I would should procure me a copy of MS 5.0.
Do it locate still in commerce?

You excuse the along message.
Pasquale Fusco
```

#### ↳ Re: Compiling in MicroSOFT COBOL 4.5

- **From:** B W Spoor <bwspoor@fcs.eu.com>
- **Date:** 2000-08-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39A94412.ECC171E1@fcs.eu.com>`
- **References:** `<39a7c957.122682459@207.126.101.100>`

```
Thane,

MicroSoft COBOL 4.5 allows you to compile and link 16 bit programs for
Windows 3.0 (ISTR facility introduced in this version) as well as for
OS/2.

This version also allows mixed language programming with MS-C v6 modules
- you need MS-C0BOL v5 to work with MS-C v7 (the reason that I was
looking for a copy of the v5 compiler to test some mixed COBOL/C code).

I still use this compiler for maintaining DOS systems, but have never
tried to create windows programs (well maybe the examples when I first
got it, but ISTR that I never got them to work) and still have the full
manual set etc.

You need to look at Chapter 3 of the "Advanced TRopics and Utilities
Reference". I have emailed some further detailed information direct to
you, so as not to clog the newsgroup with it.

Brian


Thane Hubbell wrote:
> 
> Query - I'm trying to help someone compile.
…[10 more quoted lines elided]…
> My personal web site: http://www.geocities.com/Eureka/2006/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
