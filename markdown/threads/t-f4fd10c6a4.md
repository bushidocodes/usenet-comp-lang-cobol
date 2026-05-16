[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Ok..making this right..or..my little cbl file...

_4 messages · 4 participants · 1998-12_

---

### Ok..making this right..or..my little cbl file...

- **From:** Green <new@at.cbl>
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3687F657.D236C55@at.cbl>`

```
Ok, this was a small program that I typed in that should have simple
output. I tried to compile it threw Fuiji's WINCOB. The MSG file gives a
bunch of errors, and I am uncertain of how to correct it.

Ok..here is the cbl source.....

IDENTIFICATION DIVISION.
PROGRAM-ID. ReRose.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 Flower.
 05 Rose PIC X(20).
66 Nasturtium RENAMES Rose.
PROCEDURE DIVISION.
INIT.
 MOVE "sweet" TO Rose.
 DISPLAY Nasturtium.
 DISPLAY Rose.
 STOP RUN.

well...looks like I lost some indention from pasting, but I entered it
exactly(I thought), from the book.

Is anyone else able to use Fujitsu to compile and run this? Any tips on
how it should be entered in?
```

#### ↳ Re: Ok..making this right..or..my little cbl file...

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<368813E1.5FB21BAF@home.com>`
- **References:** `<3687F657.D236C55@at.cbl>`

```
> well...looks like I lost some indention from pasting, but I entered it
> exactly(I thought), from the book.
> 
> Is anyone else able to use Fujitsu to compile and run this? Any tips on
> how it should be entered in?

That's interesting.  I don't know anything about your editor or Fujitsu
Cobol, but if I were doing any language which is column sensitive, I
would set up my editor to convert tabs to spaces.  It might not make any
difference this time (I don't know), but it probably will bite in a
different environment.
```

#### ↳ Re: Ok..making this right..or..my little cbl file...

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981228172827.25338.00000895@ngol02.aol.com>`
- **References:** `<3687F657.D236C55@at.cbl>`

```

In article <3687F657.D236C55@at.cbl>, Green <new@at.cbl> writes:

>Ok, this was a small program that I typed in that should have simple
>output. I tried to compile it threw Fuiji's WINCOB. The MSG file gives a
…[24 more quoted lines elided]…
>

I had no problem with this.  I cut/paste the code from your post into an editor
workspace. (I use the Project Management facility and selected 'Editor' from
the 'Tools' drop down list.)
I did a few alignment changes to fit my rules for positoning and formatting of
code. No changes to any of the acutal verbiage.
Saved the file as rerose.cbl.
Selected 'Compile' from the 'Tools' pull-down menu.
*** Note I use this list of options which match reasonably close to the
mainframe requirements of my current work environment.
[Compile Options]
COPY=Yes
DLOAD=Yes
FLAG=I
FLAGSW=No STDH
GEN=No
LANGLVL=85
LIB=g:\source\cbl\cpy
LINECOUNT=60
MAIN=Yes
MODE=STD
NUMBER=No
OBJECT=Yes g:\source\cbl\obj
PRINT=Yes g:\source\cbl\lst
QUOTE=APOST
RSV=ALL
SDS=No
SOURCE=Yes
SRF=FIX,FIX
SSIN=SYSIN
SSOUT=SYSOUT
STD1=JIS2
TEST=Yes g:\source\cbl\svd
TRACE=No
TRUNC=Yes
ZWB=Yes


Everything compiled fine. LINK worked and EXECute ran fine as well 
reporting the two display lines reporting the content of ROSE as 'sweet'
and the renamed reference of NASTURTIUM as 'sweet'.

HTH
```

#### ↳ Re: Ok..making this right..or..my little cbl file...

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7694di$mbc$1@news.igs.net>`
- **References:** `<3687F657.D236C55@at.cbl>`

```

Green wrote in message <3687F657.D236C55@at.cbl>...
>Ok, this was a small program that I typed in that should have simple
>output. I tried to compile it threw Fuiji's WINCOB. The MSG file gives a
…[3 more quoted lines elided]…
>
Space this to column 8.
>IDENTIFICATION DIVISION.
>PROGRAM-ID. ReRose.
>DATA DIVISION.
>WORKING-STORAGE SECTION.
>01 Flower.
space this to column 12
> 05 Rose PIC X(20).
>66 Nasturtium RENAMES Rose.
column 8.
>PROCEDURE DIVISION.
>INIT.
column 12.
> MOVE "sweet" TO Rose.
> DISPLAY Nasturtium.
> DISPLAY Rose.
> STOP RUN.
>
Also, put the program id into quotes for Fujitsu. (IE: "ReRose".)
That is compiler specific.

>well...looks like I lost some indention from pasting, but I entered it
>exactly(I thought), from the book.
…[3 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
