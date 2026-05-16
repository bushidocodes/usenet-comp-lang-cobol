[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Batch file for Fujitsu COBOL

_6 messages · 6 participants · 1999-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Batch file for Fujitsu COBOL

- **From:** ba600@FreeNet.Carleton.CA (Mike Kenzie)
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80f85s$ssh@freenet-news.carleton.ca>`

```


Has anyone run fujitsu Cobol from a batch file?
I have the free version and the version 4, but I need a DOS/win3.1 based
compiler for next week!
Cobol97 compiles from a command prompt but I can't get it to link.

Looking to produce simple EXE's.

I tried the COB650 but it puts up an annoying message and fails to compile.

Does anyone know of a free DOS based COBOL?

Can I distribute the realia educational version that came with a text?
```

#### ↳ Re: Batch file for Fujitsu COBOL

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382b96a9.11204723@news1.attglobal.net>`
- **References:** `<80f85s$ssh@freenet-news.carleton.ca>`

```
On 11 Nov 1999 20:15:56 GMT, ba600@FreeNet.Carleton.CA (Mike Kenzie)
wrote:

>
>
…[3 more quoted lines elided]…
>Cobol97 compiles from a command prompt but I can't get it to link.

If you get my book, Sams Teach Yourself COBOL in 24 Hours, you get the
v3 Fujitsu and also their 16 Bit Windows version.  (Windows 3.1) on
the same CD with the book.  It won't work for DOS, but will work for
Windows 3.1.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Batch file for Fujitsu COBOL

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991111193215.15739.00000111@ngol07.aol.com>`
- **References:** `<80f85s$ssh@freenet-news.carleton.ca>`

```
In article <80f85s$ssh@freenet-news.carleton.ca>, ba600@FreeNet.Carleton.CA
(Mike Kenzie) writes:

>
>Has anyone run fujitsu Cobol from a batch file?
…[12 more quoted lines elided]…
>

I am certain that Fujitsu is not a DOS based compiler, but it is/was possible
to use batch files for compiling / linking from the DOSPrompt with Fujitsu.
I would have to defer to the work that Lief Svelgaard (sp?) has done with 
ETK which is distributed with v3.0 and a couple batch files for compiling 
as Sub or Main and subsequent Linking.
I would defer to Lief regarding posting the content of his batch files.
```

##### ↳ ↳ Re: Batch file for Fujitsu COBOL

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<382b7982_3@news3.prserv.net>`
- **References:** `<80f85s$ssh@freenet-news.carleton.ca> <19991111193215.15739.00000111@ngol07.aol.com>`

```

Sff5ky <sff5ky@aol.comxxx123> wrote in message
> (Mike Kenzie) writes:
> >Has anyone run fujitsu Cobol from a batch file?
> I am certain that Fujitsu is not a DOS based compiler, but it is/was
possible
> to use batch files for compiling / linking from the DOSPrompt with
Fujitsu.
> I would have to defer to the work that Lief Svelgaard (sp?)
[Leif Svalgaard] has done with
> ETK which is distributed with v3.0 and a couple batch files for compiling
> as Sub or Main and subsequent Linking.
> I would defer to Lief regarding posting the content of his batch files.

Here are the batch files I use. You will have to tweak them re directories
and the the like:
---------------------------
cobolm.bat:

@echo off
::   COBOLM - compilation using FUJITSU COBOL
::   Date-Written:  97/03/09    Leif Svalgaard
::       -Revised:  97/09/22    Leif Svalgaard

if '%1' == '' goto help

:repeat
if exist %1.err del %1.err
if exist %1.COB goto exists

:error
call warblex
%lib%\cobol32 -M -i %etkdir%\cobol85.cbi %1.cob > %1.err
type %1.err|more

:testdesk
if '%desk%' == 'on' pause
goto loop

:exists
if exist %1.obj del %1.obj > nul
echo Compiling  %1...
%lib%\cobol32 -M -i %etkdir%\cobol85.cbi %1.cob > nul

:test
if errorlevel 1 goto error
if not exist %1.obj goto error
call linkupm  %1

:loop
shift
if not '%1' == '' goto repeat
goto end

:help
echo ������������������������������������������������������ͻ
echo � COBOLM program [program]...                          �
echo ������������������������������������������������������͹
echo � Compiles a Main program using FUJITSU Cobol.  If the �
echo � program contains errors, these are displayed as they �
echo � are detected.                                        �
echo � If errors were found, the file with extension .err   �
echo � is left as evidence.                                 �
echo ������������������������������������������������������ͼ
if '%desk%' == 'on' pause
:end


---------------------------

linkupm.bat

@echo off
::   LINKUPM  - link a root program to EXE
::
::   Date-Written:  97/03/09    Leif Svalgaard
::       -Revised:  98/11/23    Leif Svalgaard
::
if '%1' == '' goto help

:loop
if '%1' == '' goto end

if exist %1.obj goto link
echo %1.obj not found
goto end

:link
echo making EXE %1...
%lib%\link /nologo %1.obj @%etkdir%\f3libs /out:%1.exe
if exist %1.obj del %1.obj > nul

shift
goto loop

:help
echo ����������������������������������������������������ͻ
echo � LINKUPM {program}...                               �
echo ����������������������������������������������������͹
echo � Create .EXE modules from one or more .OBJ files.   �
echo � This procedure is normally only used to link the   �
echo � ETK main program.                                  �
echo � Example - LINKUPM etk                              �
echo ����������������������������������������������������ͼ

:end

```

#### ↳ Re: Batch file for Fujitsu COBOL

- **From:** "TomShafer" <tshafer@home.com>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2uYX3.11963$HU2.28490@news.rdc1.az.home.com>`
- **References:** `<80f85s$ssh@freenet-news.carleton.ca>`

```
DOS cobol....
Microsoft used to have a DOS COBOL.
I remember it came on one diskette.
Check....
http://www.cetus-links.org/oo_cobol.html#oo_cobol_major_anchor_cobol_compile
rs_interpreters


Mike Kenzie wrote in message <80f85s$ssh@freenet-news.carleton.ca>...
>
>
…[13 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Batch file for Fujitsu COBOL

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 1999-11-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tN%X3.1507$UX1.57010@cac1.rdr.news.psi.ca>`
- **References:** `<80f85s$ssh@freenet-news.carleton.ca> <2uYX3.11963$HU2.28490@news.rdc1.az.home.com>`

```
Micro$oft Cobol 4.5 came on 9 720k diskettes.

TomShafer <tshafer@home.com> wrote in message
news:2uYX3.11963$HU2.28490@news.rdc1.az.home.com...
> DOS cobol....
> Microsoft used to have a DOS COBOL.
> I remember it came on one diskette.
> Check....
>
http://www.cetus-links.org/oo_cobol.html#oo_cobol_major_anchor_cobol_compile
> rs_interpreters
>
…[11 more quoted lines elided]…
> >I tried the COB650 but it puts up an annoying message and fails to
compile.
> >
> >Does anyone know of a free DOS based COBOL?
…[5 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
