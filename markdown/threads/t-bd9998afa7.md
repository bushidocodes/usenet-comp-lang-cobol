[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MS-COBOL v3.x manuals?

_3 messages · 3 participants · 1999-02_

---

### MS-COBOL v3.x manuals?

- **From:** "Ralph Wade Phillips" <ralphp@techie.com>
- **Date:** 1999-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7a456b$aqv$1@blackhole.shreve.net>`

```
Does anyone out there have a set of the manuals - or at least the switch
settings - for MS Cobol 3.x?  I'd like to be able to automate some of the
compiling I'll be doing.

I'd also like to know how to run the REBUILD to pull out the data
dictionaries for the ISAM files, and to rebuild the current ones (there's
not been a rebuild for at least 5 years - I'll bet that the main 45meg file
is actually more like 15megs in size ... )

RwP
```

#### ↳ Re: MS-COBOL v3.x manuals?

- **From:** "Leif Svalgaard" <lsvalg@ibm.net>
- **Date:** 1999-02-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36c628f1@news3.us.ibm.net>`
- **References:** `<7a456b$aqv$1@blackhole.shreve.net>`

```

Ralph Wade Phillips wrote in message <7a456b$aqv$1@blackhole.shreve.net>...
>Does anyone out there have a set of the manuals - or at least the switch
>settings - for MS Cobol 3.x?  I'd like to be able to automate some of the
>compiling I'll be doing.
>


the bat file below is what I use.
You will have to change directories to fit your setup.

@echo off
if [%1] == [] goto help
if exist %1.cob goto compile
echo %1.cob not found
goto end

:compile
echo Compiling %1...
if exist %1.err del %1.err > nul
debug %mf%\bin\cob.exe %1.cob,%1.obj,nul,nul
use"%etkdir%\d.dir"<%etkdir%\q>nul
if errorlevel 1  goto compile_error
if not exist %1.obj goto compile_error

link %2 %1,,,coblib+cobapi,,; > nul
copy %1.map cobol.map > nul
del %1.map > nul
del %1.obj > nul
if [%1] == [pmenu]  call dosx pmenu
if [%1] == [apgen]  call dosx apgen
if [%1] == [signon] call dosx signon
call $exes
goto end

:help
echo  COBOL program
echo  Compiles and creates an .EXE module from
echo  a source program file.  If there are any
echo  errors a file is left with extension .ERR
goto end

:compile_error
debug %mf%\bin\cob.exe %1.cob,%1.obj,n,n
use"%etkdir%\d.dir"<%etkdir%\q>%1.err
debug %mf%\bin\cob.exe %1.cob,%1.obj,n,n use"%etkdir%\d.dir"<%etkdir%\q
if exist %1.int del %1.int > nul

:end


The d.dir file with my options follows:


01SHUFFLE
ALIGN"4"
NOALTER
NOBOUND
NOCHECKDIV
FASTLINK
FLAG-CHIP
KEYCOMPRESS"5"
IDXFORMAT"4"
REMOVE"PROMPT" "COMP"
OPT"1"
OPTSIZE
OVERRIDE"COMP-5" = "COMP"
NOQUAL
NOQUERY
NOTRICKLE
NOLIST
NOSMALLDD
NOTRUNC
RTNCODE-SIZE"4"
TARGET"386-16"
```

#### ↳ Re: MS-COBOL v3.x manuals?

- **From:** bwspoor@fridaycs.win-uk.net (Brian W Spoor)
- **Date:** 1999-02-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<95@fridaycs.win-uk.net>`
- **References:** `<7a456b$aqv$1@blackhole.shreve.net>`

```
 
In article <7a456b$aqv$1@blackhole.shreve.net>, "Ralph Wade Phillips" (ralphp@techie.com) writes:
>Does anyone out there have a set of the manuals - or at least the switch
>settings - for MS Cobol 3.x?  I'd like to be able to automate some of the
…[9 more quoted lines elided]…
>
What do you specifically want to know?

I have the manuals and compiler here - still in use for 1 system.

To rebuild a data file (.DAT & .IDX) where both files are in tact,
just type REBUILD filename.DAT - take backup first. 

REBUILD has various switches to recreate/modify the index file, but
if this is in tact will use the key information form the .IDX..  All
rebuild does is to create a new clean index file - it does not tidy
the .DAT portion. 

The easiest way that I find to do this is to write a short program
to read the indexed file sequentially and write all valid records
to a sequential work file, clease and re-open the index file in
output mode and write the records back from the sequential file -
this will clean and tidy both the data and index parts. 

To do this, you do need the file layouts, but I don't know of any
other way to tidy/compress the .DAT part. 

COBOL is supposed to reuse deleted record gaps, rather tham just
keep adding to the end of the file, but I don't know how well this
works in practice. 

Brian


-----------------------------------------------------------
Brian W Spoor MBCS
Chartered Information Systems Practitioner
Friday Computer Services          Phone: +44-(0)1803 852625
bwspoor@fridaycs.co.uk            Fax:   +44-(0)1803 854926
-----------------------------------------------------------
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
