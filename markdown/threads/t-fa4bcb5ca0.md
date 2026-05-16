[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol run time library not installed

_6 messages · 5 participants · 1998-07_

---

### Cobol run time library not installed

- **From:** "Renaat Casteels" <lmfocus@skynet.be>
- **Date:** 1998-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6o2ps7$ltj$1@news0.skynet.be>`

```
I wan't to run MF Cobol in a dos box on Nt 4.0.
I get the message cobol run time library not installed

Could anybody please help me !!!
With friendly regards
Renaat Casteels
```

#### ↳ Re: Cobol run time library not installed

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a4f05f.0@news1.ibm.net>`
- **References:** `<6o2ps7$ltj$1@news0.skynet.be>`

```

Renaat Casteels wrote in message <6o2ps7$ltj$1@news0.skynet.be>...
>I wan't to run MF Cobol in a dos box on Nt 4.0.
>I get the message cobol run time library not installed

Depending on what versions and other things, this could easy or hard.
Here are some things that I do:


You need to do something like this (in autoexec for the box)
where you change MF to point to where the compiler

@echo off
REM  The following lines should be placed in a DOS CONFIG.SYS
REM  FILES=100
REM  BUFFERS=10
REM
REM  The following lines should be placed in AUTOEXEC.BAT
SET MF=%ETKDIR%\MF
PATH=%MF%\BIN;%PATH%
SET COBDIR=%MF%\BIN
SET LIB=%MF%\LIB
SET INCLUDE=%MF%\SOURCE;
SET HELPFILES=%MF%\HELP;
SET INIT=%MF%\INIT;


MF does some nasty stuff trying to prevent you from using dos compilers
under Windows. If you get a complaint that a certain windows module is
not found, make a bat file (e.g. mycob.bat) like this:

@echo off
echo Compiling %1...
debug %cobdir%\cob.exe %1.cob,%1.obj,nul,nul
use"%etkdir%\d.dir"<%etkdir%\q>nul
if errorlevel 1  goto compile_error
goto end

:compile_error
debug %cobdir%\cob.exe %1.cob,%1.obj,nul,nul use"%etkdir%d.dir"<%etkdir%\q
echo error > %1.err
if exist %1.int del %1.int > nul
:end



----------------
where the little file q must contain:
g
q


This works because the dos debug program pretends that windows is not
present.
```

##### ↳ ↳ Re: Cobol run time library not installed

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-07-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35a4f1ab.0@news1.ibm.net>`
- **References:** `<6o2ps7$ltj$1@news0.skynet.be> <35a4f05f.0@news1.ibm.net>`

```
Leif Svalgaard wrote in message <35a4f05f.0@news1.ibm.net>...
>
>Renaat Casteels wrote in message <6o2ps7$ltj$1@news0.skynet.be>...
…[9 more quoted lines elided]…
>use"%etkdir%\d.dir"<%etkdir%\q>nul

I just saw that (at least on my news reader) the previous line was split in
two.
The use... stuf must be on the line above it. %etkdir% is just where I have
stored the 'q' file...


>if errorlevel 1  goto compile_error
>goto end
…[19 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Cobol run time library not installed

- **From:** "Gael Wilson" <gw@mfltd.co.uk>
- **Date:** 1998-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdabd6$f3c70760$905481c1@gw-nt>`
- **References:** `<6o2ps7$ltj$1@news0.skynet.be> <35a4f05f.0@news1.ibm.net> <35a4f1ab.0@news1.ibm.net>`

```
Leif,

I assume that you are using a 16-bit version of Micro Focus COBOL eg 3.2 or
3.4. Correct ? If so, the problem is likely to be because the EXEs are
dual-mode DOS-OS/2 executables and NT will attempt to run the OS/2 part.
So, to get it to work you need to add the directory containing your
executables eg \cobol\exedll to the Os2LibPath environment variable. Once
you have done that it should work. Alternatively you could use FORCEDOS to
run the DOS part of the executable.

I hope this helps.


Leif Svalgaard <leif@ibm.net> wrote in article
<35a4f1ab.0@news1.ibm.net>...
> Leif Svalgaard wrote in message <35a4f05f.0@news1.ibm.net>...
> >
…[12 more quoted lines elided]…
> I just saw that (at least on my news reader) the previous line was split
in
> two.
> The use... stuf must be on the line above it. %etkdir% is just where I
have
> stored the 'q' file...
> 
…[5 more quoted lines elided]…
> >debug %cobdir%\cob.exe %1.cob,%1.obj,nul,nul
use"%etkdir%d.dir"<%etkdir%\q
> >echo error > %1.err
> >if exist %1.int del %1.int > nul
…[17 more quoted lines elided]…
>
```

#### ↳ Re: Cobol run time library not installed

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-ee7xpUF6EvC8@Dwight_Miller.iix.com>`
- **References:** `<6o2ps7$ltj$1@news0.skynet.be>`

```
On Thu, 9 Jul 1998 16:17:16, "Renaat Casteels" <lmfocus@skynet.be> 
wrote:

> I wan't to run MF Cobol in a dos box on Nt 4.0.
> I get the message cobol run time library not installed
…[5 more quoted lines elided]…
> 

I've had good success doing 2 things.

1.  Modify CONFIG.DOS to increase FILES=

2.  Type FORCEDOS before every command.  

You must do both.
```

#### ↳ Re: Cobol run time library not installed

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-07-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298190.75903.15574@kcbbs.gen.nz>`
- **References:** `<6o2ps7$ltj$1@news0.skynet.be>`

```
In message <<6o2ps7$ltj$1@news0.skynet.be>> "Renaat Casteels" <lmfocus@skynet.be> writes:
[MF Cobol in NT DOS box]
> I get the message cobol run time library not installed
> 

MF Cobol 2.x and 3.x supports DOS, Win3.x and OS/2 1.x 16bit.
When run in an NT DOS box it detects availability of protected
mode and tries to start up as if it were OS/2.  This then
fails when the run time goes belly up.

Try using FORCEDOS to run it.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
