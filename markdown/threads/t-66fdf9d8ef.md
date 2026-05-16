[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need help with program structure

_9 messages · 6 participants · 2001-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### Need help with program structure

- **From:** "John Slagle" <jrslagle.removeme@mindspring.com>
- **Date:** 2001-09-23T00:45:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9ok07v$11b$1@slb6.atl.mindspring.net>`

```
I am using Fujitsu v3 85.
I am trying to put multiple, non nested programs in a single source file.
Eventually, I would like to get the various programs to have some shared
data.  Then I want to build a .DLL that would be callable from VB.

I appear to be going down the wrong road.

Mainprg1.OBJ : error LNK2001: unresolved external symbol _SUBPRG3
Mainprg1.OBJ : error LNK2001: unresolved external symbol _SUBPRG2

Source Module SUBPRG1:

  IDENTIFICATION DIVISION.
  PROGRAM-ID.  SUBPRG1.
  PROCEDURE DIVISION.
  0100-MAIN.
      DISPLAY 'EXECUTING SUB PROGRAM 1'.
   EXIT PROGRAM.
  END PROGRAM SUBPRG1.

  IDENTIFICATION DIVISION.
  PROGRAM-ID.  SUBPRG2.
  PROCEDURE DIVISION.
  0100-MAIN.
   DISPLAY 'EXECUTING SUB PROGRAM 2'.
  EXIT PROGRAM.
 END PROGRAM SUBPRG2.

  IDENTIFICATION DIVISION.
  PROGRAM-ID.  SUBPRG3.
  PROCEDURE DIVISION.
  0100-MAIN.
   DISPLAY 'EXECUTING SUB PROGRAM 3'.
   EXIT PROGRAM.
 END PROGRAM SUBPRG3.

Source Module MAINPRG1:

  IDENTIFICATION DIVISION.
  PROGRAM-ID.  MAINPRG1.
  PROCEDURE DIVISION.
  0100-MAIN.
      DISPLAY 'BEGIN MAIN PROGRAM'.
      CALL 'SUBPRG1'.
      CALL 'SUBPRG2'.
      CALL 'SUBPRG3'.
      DISPLAY 'END OF MAIN PROGRAM'.
      STOP RUN.
 END PROGRAM MAINPRG1.

I've tried adding ENTRYs to SUBPRG1 and then doing delegate calls to
SUBPRG2 and SUBPRG3, but that doesn't work either.
```

#### ↳ Re: Need help with program structure

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-09-23T10:43:03+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<at3rqt8re4fnpubka9hkmvf0k23pnrc17j@4ax.com>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net>`

```
On Sun, 23 Sep 2001 00:45:03 -0600 "John Slagle"
<jrslagle.removeme@mindspring.com> wrote:

:>I am using Fujitsu v3 85.
:>I am trying to put multiple, non nested programs in a single source file.
:>Eventually, I would like to get the various programs to have some shared
:>data.  Then I want to build a .DLL that would be callable from VB.

:>I appear to be going down the wrong road.

:>Mainprg1.OBJ : error LNK2001: unresolved external symbol _SUBPRG3
:>Mainprg1.OBJ : error LNK2001: unresolved external symbol _SUBPRG2

As it is not objecting to SUBPRG1 it might be as simple as telling the
compiler that there are multiple source decks in the input, i.e., that you are
"batching" the compiles.

:>Source Module SUBPRG1:
:>
:>  IDENTIFICATION DIVISION.
:>  PROGRAM-ID.  SUBPRG1.
:>  PROCEDURE DIVISION.
:>  0100-MAIN.
:>      DISPLAY 'EXECUTING SUB PROGRAM 1'.
:>   EXIT PROGRAM.
:>  END PROGRAM SUBPRG1.
:>
:>  IDENTIFICATION DIVISION.
:>  PROGRAM-ID.  SUBPRG2.
:>  PROCEDURE DIVISION.
:>  0100-MAIN.
:>   DISPLAY 'EXECUTING SUB PROGRAM 2'.
:>  EXIT PROGRAM.
:> END PROGRAM SUBPRG2.
:>
:>  IDENTIFICATION DIVISION.
:>  PROGRAM-ID.  SUBPRG3.
:>  PROCEDURE DIVISION.
:>  0100-MAIN.
:>   DISPLAY 'EXECUTING SUB PROGRAM 3'.
:>   EXIT PROGRAM.
:> END PROGRAM SUBPRG3.
:>
:>Source Module MAINPRG1:
:>
:>  IDENTIFICATION DIVISION.
:>  PROGRAM-ID.  MAINPRG1.
:>  PROCEDURE DIVISION.
:>  0100-MAIN.
:>      DISPLAY 'BEGIN MAIN PROGRAM'.
:>      CALL 'SUBPRG1'.
:>      CALL 'SUBPRG2'.
:>      CALL 'SUBPRG3'.
:>      DISPLAY 'END OF MAIN PROGRAM'.
:>      STOP RUN.
:> END PROGRAM MAINPRG1.
:>
:>I've tried adding ENTRYs to SUBPRG1 and then doing delegate calls to
:>SUBPRG2 and SUBPRG3, but that doesn't work either.
:>
```

#### ↳ Re: Need help with program structure

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-09-24T01:19:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010923211924.01328.00000175@nso-mb.aol.com>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net>`

```
In article <9ok07v$11b$1@slb6.atl.mindspring.net>, "John Slagle"
<jrslagle.removeme@mindspring.com> writes:

>
>I am using Fujitsu v3 85.
…[52 more quoted lines elided]…
>

I have seen nested programs created this way on both on the IBM and Unisys
platforms.  I would suggest putting the code for your main program FIRST, and
make sure that the END PROGRAM MAINPRG1 is AFTER all the subprograms.
This should work.
```

#### ↳ Re: Need help with program structure

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-09-24T07:55:11+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BAED8CF.7BCE6372@Azonic.co.nz>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net>`

```
John Slagle wrote:
> 
> I am using Fujitsu v3 85.
…[9 more quoted lines elided]…
> Source Module SUBPRG1:

You cannot put multiple non-nested programs in one source file.  The
compiler is most likely compiling the first and then ignoring everything
after the first 'END PROGRAM' (which is an outer ending).

You need to have these as three separate source files.  Mark the first
as 'MAIN', but not the other two. In project Manager create the .DLL
entry then add the three source files.  When you build it will compile
all three then link then together as the DLL.
```

##### ↳ ↳ Re: Need help with program structure

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-23T18:35:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9olrna$qmr$1@slb7.atl.mindspring.net>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net> <3BAED8CF.7BCE6372@Azonic.co.nz>`

```
"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:3BAED8CF.7BCE6372@Azonic.co.nz...
> John Slagle wrote:
> >
 <snip>
>
> You cannot put multiple non-nested programs in one source file.  The
> compiler is most likely compiling the first and then ignoring everything
> after the first 'END PROGRAM' (which is an outer ending).
>

If you have a compiler that does NOT support  "multiple non-nested programs
in one source file" - then you have a compiler that does not support the
(high-level) ANSI/ISO '85 Standard.  As I believe that Fujitsu *does* meet
that Standard, I suspect that there is dome directive or other issue that is
required.  Hopefully one of the Fujitsu users will "jump in" with the
solution.
```

##### ↳ ↳ Re: Need help with program structure

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-09-25T08:08:49+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BB02D81.65C8A7C9@Azonic.co.nz>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net> <3BAED8CF.7BCE6372@Azonic.co.nz>`

```
Sff5ky wrote:
> I have seen nested programs created this way on both on the IBM and Unisys
> platforms.  I would suggest putting the code for your main program FIRST, and
> make sure that the END PROGRAM MAINPRG1 is AFTER all the subprograms.
> This should work.

Yes, but he doesn't want nested programs (he said this) because he wants
the 3 subroutines to be visible in the .DLL for access from VB.
```

#### ↳ Re: Need help with program structure

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2001-09-24T05:18:56-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9on1dq$v0n$1@slb6.atl.mindspring.net>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net>`

```
As no one seems to have provided you with the correct answer, I would
SUGGEST that you look at the
   NAME
compiler option.  I haven't used this myself, but the description in the
programming guide that I have says,

"NAME (whether object files should be output for each separately compiled
program)
   ...
These options are specified when one source file is compiled where two or
more compiling units (PROGRAM) are described. The NAME option shows the
output to the object files by
separating each compiling unit. The NONAME option shows the output to a
single object file."

This sounds to me to be what you are looking for.
```

#### ↳ Re: Need help with program structure

- **From:** Thane Hubbell <nospam@newsranger.com>
- **Date:** 2001-09-24T20:17:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MxMr7.3460$ev2.4192@www.newsranger.com>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net>`

```
I'm not certain how much of this is supported in v3 -

With v6.1 at least you can combine multiple source programs (separatly
compiled!) into a single DLL.  Additionally, there are entry convetions you can
specify that will allow easy calling from other languages.

These (if available) are documented in the v3 WUG document.

In article <9ok07v$11b$1@slb6.atl.mindspring.net>, John Slagle says...
>
>I am using Fujitsu v3 85.
…[52 more quoted lines elided]…
>
```

#### ↳ Re: Need help with program structure

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-09-25T08:31:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BB032BC.B0C9BD54@Azonic.co.nz>`
- **References:** `<9ok07v$11b$1@slb6.atl.mindspring.net>`

```
William M. Klein wrote:
> As no one seems to have provided you with the correct answer, I would
> SUGGEST that you look at the
…[13 more quoted lines elided]…
> This sounds to me to be what you are looking for.

While that may actually allow him to compile 3 programs in one source
file, it won't actually solve his problem, which is to gather the 3
subroutines into one usable DLL.

With the NONAME option the resulting single file cannot be used in the
LINK program.

The NAME option cannot be used in conjunction with the Project Manager
as this will fail to link the 3 objects, or more specifically it will
fail to notice the extra 2 .OBJ files being created and add them to the
link command, which will lead to exactly the problem described via a
different route.

If you want to provide a _useful_ answer based on the use of NAME then
you might want to construct the LINK command for him that would be
necessary and which the project manager would not provide.

Or just have him split the file into three and have project manager do
the work.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
