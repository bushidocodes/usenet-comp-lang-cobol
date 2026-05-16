[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compiling sndPlaySoundA

_9 messages · 5 participants · 2000-04_

---

### Compiling sndPlaySoundA

- **From:** "Rob Jasken" <robj@twoil.com>
- **Date:** 2000-04-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net>`

```
I'f tring to compile this code.  The linker won't resolve the sndPlaySoundA
api.  I'm compiling using MF cbllink -s plays.cbl.  I would be thankful for
any help.

Rob

 * -------------------------------------------------------------- *
      $SET ANS85 MF OSVS
      $SET OPTSPEED
      $SET WARNING(1)
      $SET PERFORM-TYPE"OSVS"
      $SET CASE
       program-id. plays.
       author. YOUR NAME GOES HERE.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
           SOURCE-COMPUTER. IBM-PC.
           OBJECT-COMPUTER. IBM-PC.
       SPECIAL-NAMES.
           CALL-CONVENTION 74 IS winapi.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01 junk.
           05  wave-file               pic x(33) value
               "c:\winnt\media\chord.wav" & x"00".
           05  sound-bool              pic 9(09)   comp-5.
               88  sound-bool-false                        value 0.
               88  sound-bool-true                         value 1.

           05  ptr-to-mmsystem         procedure-pointer.
           05  badptr                  procedure-pointer.

       procedure division.

           set badptr to entry "guess_this_is_a_pointer".
           set ptr-to-mmsystem to entry "winmm".

           if badptr equals ptr-to-mmsystem
               display "Multimedia sound DLL not present"
           else
               call winapi "sndPlaySoundA" using
                   by reference wave-file
                   by value 1 size 2
                   returning sound-bool
               if sound-bool-false
                   display "Failed"
           .
           exit program
           stop run
           .
```

#### ↳ Re: Compiling sndPlaySoundA

- **From:** "Gael Wilson" <gael.wilson@merant.com>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ck7sk$90o$1@hyperion.mfltd.co.uk>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net>`

```
Rob,

A UINT is SIZE 4. Try that and see if it works. If not, can you post the
error displayed ?


Rob Jasken <robj@twoil.com> wrote in message
news:866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net...
> I'f tring to compile this code.  The linker won't resolve the
sndPlaySoundA
> api.  I'm compiling using MF cbllink -s plays.cbl.  I would be thankful
for
> any help.
>
…[50 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Compiling sndPlaySoundA

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38ee0e98_4@news1.prserv.net>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net> <8ck7sk$90o$1@hyperion.mfltd.co.uk>`

```
Use a call convention of 66 instead of 74.  A 74 denotes that the object
for the API call will be linked into the final executable that is
created.  A 66 denotes that a reference to the module will be included,
and the code is executed in the appropriate Windows DLL.  It also makes
your final executable smaller and more dynamic.

The integer size has nothing to do with the linkage editor error.

Try this:

      $set mf charset(ascii) noparamcountcheck case noibmcomp
       program-id.                     playsnd.
       environment division.
       special-names.
           call-convention 66 is win32nol
           call-convention 74 is win32api.

       data division.
       working-storage section.
       01  load-dll-ptr                usage procedure-pointer.
       01  ws-miscellaneous.
           03  wave-file               pic x(128) value
               'c:\winnt\media\the microsoft sound.wav' & x'00'.
           03  sound-bool              pic s9(09) comp-5.
               88  sound-bool-false               value 0.
               88  sound-bool-true                value 1.

       procedure division.

      * Make Win32 Multimedia support available for use:
           display 'Loading the Multimedia support DLL...'.
           set load-dll-ptr            to entry 'winmm'.

      * Play the specified sound:
           call win32nol 'sndPlaySoundA' using
               by reference    wave-file
               by value        1 size 2
               returning       sound-bool

               on exception
                   display 'Could not play Sound!'
           end-call.

      * Return to caller:
           exit program.
           stop run.

Use a "cob playsnd.cbl -x:cs" to create the .EXE...

Hope this helps - TL
```

###### ↳ ↳ ↳ Still no go

- **From:** "Rob Jasken" <robj@twoil.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BDED582111CEF570.F82D71BA5B55A2B5.0D19D7BE6858D8A5@lp.airnews.net>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net> <8ck7sk$90o$1@hyperion.mfltd.co.uk> <38ee0e98_4@news1.prserv.net>`

```
I'm using MF 4.0.32.  It compiles now and runs, no sound.  If I animate it
the sound works ok.

Thanks Again,
Rob


Lucas, Todd wrote in message <38ee0e98_4@news1.prserv.net>...
>Use a call convention of 66 instead of 74.  A 74 denotes that the object
>for the API call will be linked into the final executable that is
…[126 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Still no go

_(reply depth: 4)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ctc2q$6s$1@slb3.atl.mindspring.net>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net> <8ck7sk$90o$1@hyperion.mfltd.co.uk> <38ee0e98_4@news1.prserv.net> <BDED582111CEF570.F82D71BA5B55A2B5.0D19D7BE6858D8A5@lp.airnews.net>`

```
the       by value 1 size 2

should be
            by value 1 size 4  (or leave size off if default is 4)



kenmullins
```

###### ↳ ↳ ↳ Re: Still no go

_(reply depth: 5)_

- **From:** dlmax@netcom.com (David L Maxwell)
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ctngj$kfr$1@slb6.atl.mindspring.net>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net> <8ck7sk$90o$1@hyperion.mfltd.co.uk> <38ee0e98_4@news1.prserv.net> <BDED582111CEF570.F82D71BA5B55A2B5.0D19D7BE6858D8A5@lp.airnews.net> <8ctc2q$6s$1@slb3.atl.mindspring.net>`

```
The line "by value 1 size 2

should be "by value 2 size 2"

In fact I have used a value of 0 and it still works just fine!

Dave


> KenMullins@mindspring.says...
>
…[11 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Still no go

_(reply depth: 6)_

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38f27645_1@news1.prserv.net>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net> <8ck7sk$90o$1@hyperion.mfltd.co.uk> <38ee0e98_4@news1.prserv.net> <BDED582111CEF570.F82D71BA5B55A2B5.0D19D7BE6858D8A5@lp.airnews.net> <8ctc2q$6s$1@slb3.atl.mindspring.net> <8ctngj$kfr$1@slb6.atl.mindspring.net>`

```
Ok, here it is - it works every time!  It seems to be a bug in the
Windows API when you go to play the sound asynchronously.  If you use a
value of +0 (synchronous play) then it works!  Don't know why though ...

By the way, a C "unsigned integer (or UINT)" is 2 bytes in Micro Focus
32-bit Cobol, or PIC s9(4) comp-5 - just make sure the value you place
into it is always positive...

      $set mf charset(ascii) noparamcountcheck case noibmcomp
       program-id.                     playsnd.
       environment division.
       special-names.
           call-convention 66 is win32nol
           call-convention 74 is win32api.

       data division.
       working-storage section.
       01  load-dll-ptr                usage procedure-pointer.
       01  ws-miscellaneous.
           03  wave-file               pic x(128) value
               'c:\winnt\media\the microsoft sound.wav' & x'00'.
           03  sound-bool              pic s9(09) comp-5.
               88  sound-bool-false               value 0.
               88  sound-bool-true                value 1.

       procedure division.

      * Make Win32 Multimedia support available for use:
           set load-dll-ptr            to entry 'winmm'.

      * Play the specified sound:
           call win32nol 'sndPlaySoundA' using
               by reference    wave-file
               by value        h'00' size 2
               returning       sound-bool

               on exception
                   display 'Could not play Sound!'
           end-call.

      * Return to caller:
           exit program.
           stop run.
```

###### ↳ ↳ ↳ Re: Still no go

_(reply depth: 7)_

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 2000-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ctvnk$i9l$1@slb6.atl.mindspring.net>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net> <8ck7sk$90o$1@hyperion.mfltd.co.uk> <38ee0e98_4@news1.prserv.net> <BDED582111CEF570.F82D71BA5B55A2B5.0D19D7BE6858D8A5@lp.airnews.net> <8ctc2q$6s$1@slb3.atl.mindspring.net> <8ctngj$kfr$1@slb6.atl.mindspring.net> <38f27645_1@news1.prserv.net>`

```
       01 int      is typedef pic s9(9) comp-5.
       01 uint     is typedef pic 9(9) comp-5.
       01 short    is typedef pic s9(4) comp-5.
       01 bool     is typedef pic s9(9) comp-5.
       01 word     is typedef pic s9(4) comp-5.
       01 dword    is typedef pic s9(9) comp-5.
       01 ushort   is typedef pic 9(4) comp-5.
       01 long     is typedef pic s9(9) comp-5.
       01 ulong    is typedef pic 9(9) comp-5.
       01 Handle   is typedef long.
       01 LPARAM   is typedef long.
       01 WPARAM   is typedef int.
       01  char                   pic s9(2)  comp-5 is typedef.
       01  uchar                  pic  9(2)  comp-5 is typedef.
       01  float                  comp-1 is typedef.

kenmullins

Lucas, Todd <todd.lucas@ibm.net> wrote in message
news:38f27645_1@news1.prserv.net...
> Ok, here it is - it works every time!  It seems to be a bug in the
> Windows API when you go to play the sound asynchronously.  If you use a
…[73 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Todd is the Man!

_(reply depth: 7)_

- **From:** "Rob Jasken" <robj@twoil.com>
- **Date:** 2000-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<E92CEA538C68E4CB.62AEDCB6EBC05449.678A619EDAE5FE7A@lp.airnews.net>`
- **References:** `<866BD1F9A5A05809.284643E28226A1AC.3C43580B5BA33AFF@lp.airnews.net> <8ck7sk$90o$1@hyperion.mfltd.co.uk> <38ee0e98_4@news1.prserv.net> <BDED582111CEF570.F82D71BA5B55A2B5.0D19D7BE6858D8A5@lp.airnews.net> <8ctc2q$6s$1@slb3.atl.mindspring.net> <8ctngj$kfr$1@slb6.atl.mindspring.net> <38f27645_1@news1.prserv.net>`

```
Thanks Todd.  I owe you one.

Rob


Lucas, Todd wrote in message <38f27645_1@news1.prserv.net>...
>Ok, here it is - it works every time!  It seems to be a bug in the
>Windows API when you go to play the sound asynchronously.  If you use a
…[73 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
