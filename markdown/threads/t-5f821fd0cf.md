[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Editors

_23 messages · 12 participants · 1999-04 → 1999-05_

---

### Editors

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ed391$d6s$1@news.igs.net>`

```
Every so often, there are questions in here about editors.  I recently
purchased a copy of Vedit, and I like it very much.  Vedit has been around a
long time (since about 1981-82), and was one of the first professional PC
editors.  I used it years ago under DOS, and decided that I liked the
windows version.

It has all the bells and whistles, including templates, syntactical colour
profiles for the major languages (Cobol-85, AcuCobol, and MF net express
included), and one of the most powerful macro languages that I have ever
seen in an editor.  (For Dec people, it includes the full Teco subset).  To
give an indication of how good the macro language is, the install procedure
is written in the edit language.  Also included as examples are a basic word
processing system and a spell checker.

It is extremely fast.  I did a search and replace of 50 files (15-20 page
Cobol source each, using wildcard file specs) and it took 3-4 seconds.(Under
windows95!).

You can toggle between HEX, Octal, Text, Text with visible control
characters, EPCIDIC, and text with visible <CR,LF> only.  It handles tabs
correctly and completely invisibly.  It also allows tabs to be set for
Cobol, on specific columns. The indent/undent work independently from the
tab stops.

Instead of the standard clipboard, it uses as default clipboard number 1.
There are 36 of them (a-z, 0-9) and each can be used as a standard
clipboard, a completely separate file being edited, or contain a macro than
can be edited and executed.

It has all sorts of "goodies" like an ASCII table, 2*16 undo levels, dozens
of macros, etc.

The mouse works well.  Single click to move the cursor.  Double click to
select the Cobol word. Alt double click to select the sentence (period to
period). It is intelligent enough that a double click on a literal will
select from quote to quote.

It comes with a full printed manual, as well as an excellent help system and
tutorial.  Both are written in the macro language, and source is included.
In fact, one of the things I like best about the program is that most of the
utilitiies (and there are dozens) are written in the macro language with
source included.  That is the best help you can get ... look at the existing
macros.  The default initialization file, for example, contains setups for
every option as comments.  To change the setup, I "uncommented" what I
wanted, and "commented" the packaged defaults.  Took about five minutes,
including learning how to do it from the help file.  I am going to change my
setup next so that control click on a copybook will edit the file.

The package is relatively expensive as editors go.  It is US $150.  However,
I firmly believe that ones editor is probably the single biggest factor in
producing fast code.  Worth every penny.

Donald.
```

#### ↳ Re: Editors

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p3uO2.3257$c57.1077157@news2.mia>`
- **References:** `<7ed391$d6s$1@news.igs.net>`

```
Donald Tees wrote:
>
>Every so often, there are questions in here about editors.  I recently
…[3 more quoted lines elided]…
>windows version.
...
>The package is relatively expensive as editors go.  It is US $150.  However,
>I firmly believe that ones editor is probably the single biggest factor in
>producing fast code.  Worth every penny.

I've heard of Vedit, but never used it.  You're right about the importance
of a programmer's editor.  I'm embarrassed to admit that I still use a DOS
based editor, Brief.  But getting a new editor is like getting divorced
and remarried.  Very traumatic. :-)  I have used Brief for so long that
the commands are burned into my synapses.  I bought Multi-Edit a couple
of years ago, and even upgraded it last year to a 32 bit version.  It's
a good editor, I just haven't made myself start using it yet.  But Real
Soon Now. :-)
```

##### ↳ ↳ Re: Editors

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ee1ov$3gm$1@news.igs.net>`
- **References:** `<7ed391$d6s$1@news.igs.net> <p3uO2.3257$c57.1077157@news2.mia>`

```
Judson McClendon wrote in message ...
<big snippage on changing editors>
But Real Soon Now. :-)

<grin>  Well I have to admit to the exact same thing. I have been putting
off getting something new because of the trauma involved.  I have been using
several Mickey-mouse type editors that were shareware, each of which had
zero learning curve, each of which had a couple of features that I needed.

I was finally shamed into committing to a specific one because I hired
someone, and was ashamed of the tools I was using.
```

##### ↳ ↳ Re: Editors

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1999-04-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ee3ne$4gl$1@news.igs.net>`
- **References:** `<7ed391$d6s$1@news.igs.net> <p3uO2.3257$c57.1077157@news2.mia>`

```
Judson McClendon wrote in message ...

P.S. to that last.  Vedit claims to be able to emulate most text editors.
It include a Brief emulation.  Her are the docs.


  BRIEF 3.1 KEYBOARD LAYOUT FOR VEDIT PLUS
  ----------------------------------------

Major Differences:
------------------

1.  <F10> pops up the menu system.

3.  Many functions which Brief implements with macros via the <F9> and <F10>
    keys, e.g. "Center Line Horizontal" and "Change Directory", VEDIT
    implements with built-in menu functions. Since VEDIT uses external
macros
    far less than Brief, this Brief emulation uses <F9> and <F10> for
VEDIT's
    normal assignments. Use {MISC, Load/Execute macro} and {MISC, Execute
    macro} to load and execute VEDIT's external macros. Commonly used macros
    can be built-in as "Keystroke Macros".

4.  While the Brief block functions are closely emulated, it is often easier
    to directly copy/move a block with <Ctrl-F9> and <Alt-F9> than to use
    the "scrap".

5.  <F11>, <Ctrl-F11> and <Alt-F11> are used to access VEDIT's Text
Registers
    via the functions [T-REG INSERT], [T-REG COPY] and [T-REG MOVE].

6.  Brief's "scrap" is emulated with Text Register "0", also called the
    "scratchpad" available in the {EDIT} menu. VEDIT has many other
available
    Text Registers.

7.  Instead of blindly toggling configuration parameters (e.g. "Backup File
    Toggle" and "Case Sensitivity Toggle") the parameter is toggled and you
    are left in the {CONFIG} menu to see the resulting value. Press <Esc>
    twice or tap <Alt> to exit the menus.

8.  Brief's "Compile Buffer" <Alt-F10> is emulated by starting up VEDIT's
    integrated compiler support.


Notes:
------

1.  BRIEF.KEY has the command "Config(E_LINE_MODE,5)" to make the <Home> and
    <End> keys properly emulate Brief.

2.  {HELP, Keyboard layout} will display the keyboard layout listed on the
    next page. However, the screen for "Built-in Keystroke Macros" will not
    be correct. This can be corrected by editing the beginning of VHELP.HLP
    (VEDIT PLUS: VPHELP.HLP) which is an explanation of the built-in
    keystroke macros.


    KEYBOARD LAYOUT

Assignments to VEDIT's functions:
--------------------------------

"+" indicates functions not available in Brief
"!" indicates functions which operate differently from Brief

[BACKSPACE]  <Backspace>
[BACKTAB]  <Shft-Tab>
[CANCEL]    ! <Ctrl-\>
[CURSOR UP]  <Up Arrow>
[CURSOR DOWN]  <Down Arrow>
[CURSOR RIGHT]  <Right Arrow>
[CURSOR LEFT]  <Left Arrow>
[DELETE]  <Del>
[DEL PREV WORD]  <Ctrl-Bksp>
[DEL NEXT WORD]  <Alt-Bksp> <Ctrl-Y>
[ENTER CTRL]  <Alt-Q>  <Ctrl-^>
[ERASE TO BOL]      <Ctrl-K>
[ERASE TO EOL]      <Alt-K>
[ERASE LINE]  <Alt-D>  <Ctrl-L>
[ESCAPE]     <Esc>
[FORMAT PARA]  <Ctrl-F>
[HELP]     ! <Alt-H>
[LINE BEGIN]  <Home>
[LINE END]  <End>
[MENU]     + <F10>  <Alt>
[NEXT PARA]    + <Ctrl-Down Arrow>
[NEXT TAB STOP]    ! <Ctrl-Tab>
[NEXT WORD]  <Ctrl-Right Arrow>
[PAGE UP]  <PgUp>
[PAGE DOWN]  <PgDn>
[PREVIOUS PARA]    + <Ctrl-Up Arrow>
[PREVIOUS WORD]  <Ctrl-Left Arrow>
[REPEAT]  <Ctrl-R>
[SCROLL UP]  <Alt-Up Arrow>  <Ctrl-D>
[SCROLL DOWN]  <Alt-Down Arrow> <Ctrl-E>
[SCROLL RIGHT]    + <Alt-Right Arrow>
[SCROLL LEFT]    + <Alt-Left Arrow>
[TAB CHARACTER]  <Tab>
[T-REG COPY]    + <Ctrl-F11>
[T-REG MOVE]    + <Alt-F11>
[T-REG INSERT]    + <F11>
[VISUAL ESCAPE]    + <Alt-\>
[VISUAL EXIT]    + <Ctrl-O>  <Ctrl-F10>

Goto Matching ()    ! <Alt-F3> and <Ctrl-]>
Set text marker (bookmark) <Ctrl-S>
Goto text marker  <Ctrl-G> and <Alt-J>
Goto block beginning    + <Alt-[>
Goto block end     + <Alt-]>

Replace (translate)  <F6> and <Alt-T>
Search forwards   <F5> and <Alt-S>
Search/replace next    ! <Shift-F5> and <Shift-F6>
Incremental search    +    <Ctrl-I>
Search all buffers    +    <Ctrl-F2>
Compare buffers     +    <Ctrl-F3>

Open (edit) new file    +    <Alt-F2> (Same buffer)
Open (edit) new file    ! <Alt-E>  (New buffer, full window)
Open (edit) new file    + <Alt-Y>  (New buffer, split window)
Switch windows     ! <Alt-F4>
Resize/move window     <F2>

Toggle display mode    + <Ctrl-V>
Toggle binary/text mode    + <Ctrl-J>
Toggle hex-mode split    + <Alt-=>
Toggle VGA 25/28/50 lines  + <Alt-.>

Start up Compiler Support  + <Alt-F10>
Command mode window    +    <Alt-/>

Cut (move) to scratchpad   ! <Shft-Del>
Copy to scratchpad    ! <Ctrl-Ins>
Paste scratchpad    ! <Shft-Ins>
Copy block to cursor    + <Ctrl-F9>
Move block to cursor    + <Alt-F9>

Indent (margin/block)    ! <F8>  <Tab>
Undent (margin/block)    ! <Alt-F8> <Shft-Tab>

Assignments to emulate Brief:
-----------------------------

Back Tab  Shft-Tab Also used in dialog boxes.
     Also undents a block of text.
Backspace  Backspace Always deletes the previous char
     including a "newline".
Backup File Toggle Ctrl-W  Accesses {CONFIG, File Handling} item.
Beginning of Line Home
Border Toggle    Similar function implemented.
Buffer List  Alt-B  Allows point and shoot selection
Case Sensitive Toggle Ctrl-F5  Accesses {CONFIG, Search options} item.
Center Line Horizontal   Use {EDIT, Center} instead.
Center Line in Window Ctrl-C
Change Directory   Change from Point & Shoot dialog box
Change Output File Alt-O
Change Window  F1  You then enter the window #.
Color     Use {MISC, Color toggle} to change the
     text color. Use {CONFIG, Color) to
     change other colors.
Column Mark  Alt-C
Compile Buffer  Alt-F10  Use the Integrated Compiler support.
Copy to Scrap  Numpad+
Create Key Assignment   Use {CONFIG,Keyboard layout,Add macro}
Create Window  F3  Only accesses the {WINDOW} menu.
Cut to Scrap  Numpad-
Delete   Del
Delete Current Buffer Ctrl-_
Delete File    Not implemented. Use {MISC, DOS shell}
     or VEDIT PLUS's File_Delete() instead.
Delete Line  Alt-D
Delete Macro File   Not implemented; not needed.
Delete Next Word Alt-Bksp or Ctrl-Y
Delete Previous Word Ctrl-Bksp
Delete to Begin of Line Ctrl-K
Delete to End of Line Alt-K or Ctrl-L
Delete Window  F4  Implemented as {WINDOW, Close}.
Display File Name Alt-F  Displays on bottom screen line.
Display Version ID Alt-V  Accesses {HELP, Status}.
Down   Down-Arrow
Drop Bookmark  Alt-1 .. Alt-0
Edit File  Alt-E  Accesses {FILE, Open, New buffer}.
End of Buffer  End End End
   Ctrl-PgDn
End of Line  End
End of Window  End End  Similar operation.
   Ctrl-End
Enter   Enter
Escape   Esc
Execute Command    Not implemented; use {MISC, Load/
     Execute macro} or {MISC, Execute
     macro} instead.
Exit   Alt-X
Go to Line  Alt-G
Go to Routine    Not implemented. Use CFUNC.VDM insead.
Halt   Ctrl-C  This is the similar [CANCEL] function.
Help   Alt-H
Incremental Search   Use {SEARCH, Incremental search}.
Indent Block  F8 Alt-F8 Accesses {EDIT, Indent}, {EDIT, Undent}.
   Tab Shift-Tab
Insert Mode Toggle Alt-I  Use blinking/not blinking cursor.
Jump to Bookmark Alt-J and Ctrl-G
Left   Left-Arrow It can move to the previous line.
Left Side of Window   Not implemented.
Line Mark  Alt-L
Line to Bottom Window Ctrl-B
Line to Top Window Ctrl-T
Load Keystroke Macro   See {MISC, Keyboard layout, Load}
Load Macro File    Not implemented; use {MISC, Load/
     Execute macro} or {MISC, Execute
     macro} instead.
Lower Case Block   Use {EDIT, Edit/Translate, Lower case}
Margin     Use {CONFIG, Word processing} instead.
Mark   Alt-M  VEDIT has additional ways of copying/
     moving blocks using {BLOCK, Copy/move
     to cursor}.
Next Buffer  Alt-N  May also switch to another window.
Next Char  Right Arrow
Next Error    Implemented only within the Integrated
     Compiler Support.
Next Word  Ctrl-Right Arrow
Noninclusive Mark Alt-A
Open Line  Ctrl-Enter
Outdent Block  Alt-F8  VEDIT's [UNDENT] does this.
Page Down  PgDn
Page Up   PgUp
Paste from Scrap Ins  Similar operation.
Pause Recording Toggle   Not implemented.
Pause On Error    Not needed; the Integrated Compiler
     Support lets you view errors.
Playback    Press the key to which you assigned
     the previously defined Keystroke Macro.
Pop-Up Errors    Implemented only within the Integrated
     Compiler Support.
Pop-Up menu  F10  Accesses VEDIT's menu system.
Previous Buffer  Alt--  May also switch to another window.
Previous Char  Left Arrow
Previous Word  Ctrl-Left Arrow
Print Block  Alt-P  Highlights and prints the block.
Quick Window Switch   Not implemented.
Quote   Alt-Q  Also quotes ALT keys
Read File into Buffer Alt-R
Redo   Ctrl-U  Accesses {EDIT, Undo, Redo}.
Reformat Paragraph Ctrl-F
Regular Expr. Toggle Ctrl-F6  Accesses {SEARCH, Option} item.
Remember  F7  You can record more than one Keystroke
     Macro.
Repeat   Ctrl-R
Resize Window  F2  Its easier to use the mouse.
Right   Right Arrow Can also move to next line.
Right Side of Window   Not implemented.
Save Keystroke Macro   See {MISC, Keyboard layout, Save}.
Scroll Buffer Down Ctrl-D
Scroll Buffer Up Ctrl-E
Search Again  Shft-F5
Search Backward  Alt-F5
Search Block Toggle   Not needed.
Search Forward  F5 and Alt-S
Suspend Brief  Alt-Z
Swap Cursor and Mark   Not implemented.
Tab   Tab  Also indents a block of text.
Tab Stops    Use {CONFIG, Tab stops} instead.
Top of Buffer  Home Home Home
   Ctrl-PgUp
Top of Window  Home Home
   Ctrl-Home
Translate Again  Shft-F6  Same as Shft-F5; both are the
     function {SEARCH, Next}.
Translate Backward Alt-F6
Translate Forward F6 and Alt-T
Undo   Alt-U  Accesses {EDIT, Undo, Edit}. You can
   Numpad*  also undo line-by-line.
Up   Up Arrow
Upper Case Block   Use {EDIT, Edit/Translate, Upper case}
Use Tab Characters   Use {CONFIG, Emulation, Expand <Tab>
     key with spaces} instead.
Write   Alt-W  It emulates Brief, but selecting
     either {FILE, Save and Continue} or
     {BLOCK, Write to Disk} might be more
     straightforward.
Write All and Exit Ctrl-X  Seems to us like a dangerous key!
Zoom Window Toggle Alt-F2 and Ctrl-Z
```

###### ↳ ↳ ↳ Re: Editors

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370B5C3F.1092B8B6@NOSPAMhome.com>`
- **References:** `<7ed391$d6s$1@news.igs.net> <p3uO2.3257$c57.1077157@news2.mia> <7ee3ne$4gl$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Judson McClendon wrote in message ...
> 
> P.S. to that last.  Vedit claims to be able to emulate most text editors.
> It include a Brief emulation.  Her are the docs.

Multi-Edit can also be set up to emulate Brief.
```

##### ↳ ↳ Re: Editors

- **From:** areymond@csi.com (Alain Reymond)
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370b030e.1023558@news.skynet.be>`
- **References:** `<7ed391$d6s$1@news.igs.net> <p3uO2.3257$c57.1077157@news2.mia>`

```
Judson,

Like you, I have been working for year with Brief. I bought SlickEdit
for Unix (for a SCO Unix) and Visual SlickEdit for my Win95 system.
The Brief emulation of both products is quite perfect. It is a very
nice editor much more powerful than Brief with all the
finctionnalities of Brief. Worth a buying.

Have a nice day,

Alain Reymond


On Tue, 06 Apr 1999 20:23:49 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:


>I've heard of Vedit, but never used it.  You're right about the importance
>of a programmer's editor.  I'm embarrassed to admit that I still use a DOS
…[6 more quoted lines elided]…
>--
```

###### ↳ ↳ ↳ Re: Editors

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370B5DA8.6B24352B@NOSPAMhome.com>`
- **References:** `<7ed391$d6s$1@news.igs.net> <p3uO2.3257$c57.1077157@news2.mia> <370b030e.1023558@news.skynet.be>`

```
Alain Reymond wrote:
> 
> Judson,
…[5 more quoted lines elided]…
> finctionnalities of Brief. Worth a buying.

The nice thing about SlickEdit is that it supports several operating
sytems.  The bad thing is that you have to pay full price for each
version you get, even on the same machine.  I'd buy it if I could
install the Windows, OS/2, Unix, & DOS versions in the same FAT
directory and use the same settings without paying for more than a
couple of hundred dollars.

Instead, I use the DOS version of Multi-Edit much more often than the
Windows version, giving up long file name in my various operating
systems.  Kind of a pain when I need batch files to rename files down,
edit, then rename back (.HTM to .HTML).  I also find it much easier to
open a file where I want it by typing ME file.ext on the command line
over using the GUI version.   For all of the advantages GUIs have, they
can be a pain sometimes too.
```

#### ↳ Re: Editors

- **From:** dwledet@worldnet.att.net (Douglas J. Woods-Ledet)
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370c0e10.4062279@netnews.worldnet.att.net>`
- **References:** `<7ed391$d6s$1@news.igs.net>`

```
Editors are more "personal" than one's love for your first language.

IBM Mainframers who use PC, normally use Command Technologies SPF/PC,
a DOS based tool or the windows version, SPF/PRO.

Each acts and functions very near to the IBM mainframe editor,
ISPF/PDF.  Each supports MACROs, colorization, most other editting
feature, and major COBOL compilers on the PC.

Now I am switching to the negative.  I have been "waiting" for this
opportunity.  Please take my following comments with this in mind.

I upgraded to their new product, SPF/SE.

Their support of IBM M/F macro has been removed.  They now support
interpreted C macros.

Their product no longer functions as a near perfect image of the IBM
M/F product AND they are proud of this!!  They are converting it to
just another PC Windows product.  They say their marketing research
shows no market for a IBM near perfect image.

Worse of all, they have discontinued SPF/PC and SPF/PRO completely.

Command Technology has no regard for their loyal customers who use the
product because of the near zero learning cycle, i.e. you use it on
the M/F, you use it on the PC, it is the same.

Command Technology has no idea that their "new" product is to much
like every other PC editor and therefore, I believe, will not attract
any one who currently uses any other Editor.

OK, so I know I am baised, but I am upset that yet another "perfect"
niche product is gone and replaced by just another Windows program.

Doug
```

##### ↳ ↳ Re: Editors

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370C707A.DF2B1024@zip.com.au>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net>`

```
I just got a copy of Vi for the PC.  It has cobol highlighting and is
fast.

Works better than the Fujitsu V3 editor and is free.

(hint: for those who have not used it Vi's command set is arcane at
best.)

Ken
```

###### ↳ ↳ ↳ Re: Editors

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370d5d05.959024462@news1.ibm.net>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au>`

```
On Thu, 08 Apr 1999 19:01:46 +1000, Ken Foskey <waratah@zip.com.au>
wrote:

>I just got a copy of Vi for the PC.  It has cobol highlighting and is
>fast.
…[4 more quoted lines elided]…
>best.)

Where does one get Vi?

My favorite feature of the Fujjitsu editor is one I have not seen with
others ----  Block Mode for selection.
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370DED87.2FCBC0AF@zip.com.au>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net>`

```
Thane Hubbell wrote:
> 
> Where does one get Vi?
> 
> My favorite feature of the Fujjitsu editor is one I have not seen with
> others ----  Block Mode for selection.

ftp://uiarchive.uiuc.edu/pub/packages
vim
pc

vim53rt.zip  (runtime)
gvim53.zip   (windows 95)

It is totally free.

It is not bad either.  You will need to trick it to highlight cobol but
the highlighter is defined (columns 8-72 only)

here is my set up file

   set nocompatible
   set expandtab
   source $VIM/vimrc_example
   source $VIM/mswin.vim
   autocmd BufRead *.cob,*.cbl source $VIM/syntax/cobol.vim

the syntax highlighter is predefined, must take a look at it one day..

Ken
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370DFB24.6E65ED08@NOSPAMhome.com>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net>`

```
> My favorite feature of the Fujjitsu editor is one I have not seen with
> others ----  Block Mode for selection.

Multi-Edit alows either block mode or stream mode selection.
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 5)_

- **From:** areymond@csi.com (Alain Reymond)
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370f2bd0.391293@news.skynet.be>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com>`

```
So does Slick Edit also.

Alain Reymond

>> My favorite feature of the Fujjitsu editor is one I have not seen with
>> others ----  Block Mode for selection.
>
>Multi-Edit alows either block mode or stream mode selection.
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 6)_

- **From:** "Charles Goodman" <cgoodman@mbnet.mb.ca>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nFGP2.2528$rv1.197602@typhoon.mbnet.mb.ca>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be>`

```
Anybody remember FAST EDDIE?
Used it with original IBM COBOL for PC.
You could also buy a tablet where you could press on words and phrases while
composing code.
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<KOMP2.7079$w6.1889881@news4.mia>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be>`

```
Alain Reymond wrote:
>Alain Reymond
>>
>>Multi-Edit alows either block mode or stream mode selection.
>
>So does Slick Edit also.

I can't imagine a programmer's editor without block mode.  To me, this
is the single most important distinction between programmer's editors
and normal text editors.  If my memory serves correctly, my first PC
programmer's editor, WordMaster in late 70's from MicroPro the WordStar
people, had block mode.  It had a macro capability that, in some ways,
was more powerful than Brief's.  Anyone who is professionally writing
COBOL code without block mode is not nearly as productive as they could
be.
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 7)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37101be0.504662@news1.ibm.net>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be> <KOMP2.7079$w6.1889881@news4.mia>`

```
On Sat, 10 Apr 1999 18:32:10 GMT, "Judson McClendon"
<judmc123@bellsouth.net> wrote:


>I can't imagine a programmer's editor without block mode.  To me, this
>is the single most important distinction between programmer's editors
…[5 more quoted lines elided]…
>be.

I've used many editors, but the Fujitsu is the first with block mode.


I liked MicroFocus Text mode editor a lot - but it didn't have block
mode. 

I wonder if we are defining block mode in the same way?  I mean, not a
block of lines but actually being able to define the upper left corner
and lower right corner of an edit block ANYWHERE in the source and
then operate on that block.  Cut it, paste it, delete it etc..
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-04-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7ep9rf$9lm@sjx-ixn4.ix.netcom.com>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be> <KOMP2.7079$w6.1889881@news4.mia> <37101be0.504662@news1.ibm.net>`

```
Thane Hubbell wrote in message <37101be0.504662@news1.ibm.net>...

>
>
…[7 more quoted lines elided]…
>

What you describe is certainly a feature that is available in the Micro
Focus GUI editor (and has been since its first release).
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 9)_

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3710a6db.36088809@news1.ibm.net>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be> <KOMP2.7079$w6.1889881@news4.mia> <37101be0.504662@news1.ibm.net> <7ep9rf$9lm@sjx-ixn4.ix.netcom.com>`

```
On Sat, 10 Apr 1999 23:52:21 -0500, "William M. Klein"
<wmklein@nospam.netcom.com> wrote:

>Thane Hubbell wrote in message <37101be0.504662@news1.ibm.net>...
>
…[12 more quoted lines elided]…
>Focus GUI editor (and has been since its first release).

Yep.  But Split and Join lines went away (it may have come back
since).  

One of the guys where I used to work, could not type worth beans.  He
did about 5 WPM, but he could program up a storm using Copy line,
split line, join line, delete line, restore line etc.  It was amazing
to watch.  He can't use the GUI editor at all.
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 10)_

- **From:** The COBOL Frog <H.Klink@IMN.nl>
- **Date:** 1999-04-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3710FCCE.C1D98EE2@IMN.nl>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be> <KOMP2.7079$w6.1889881@news4.mia> <37101be0.504662@news1.ibm.net> <7ep9rf$9lm@sjx-ixn4.ix.netcom.com> <3710a6db.36088809@news1.ibm.net>`

```
Thane Hubbell wrote:

> One of the guys where I used to work, could not type worth beans.  He
> did about 5 WPM, but he could program up a storm using Copy line,
> split line, join line, delete line, restore line etc.  It was amazing
> to watch.  He can't use the GUI editor at all.

You can't blame the editor for that :): Give the guy a type course.
There are by the way lots of people not typing with the 10-finger-blind
system not with some three/four-finger self-learnde system. Personally I
have spotted even the eagle system, especially under end-users. The
eagle-system is quit easily recognized: the tip of one (1) the right-hand
finger circles in eight-like movements for some seconds some 20 centimeter
above the keyboard, until the wanted key is detected. Then with an straight
downward fall, the finger "falls" in that key. Just imaging an eagle
circling until it sees some food ...

Seriously: in version 3 of NetExpress, something has been added around
split/join, so that works nice now too.

Frog. (*Jumps* on keys)
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc123@bellsouth.net>
- **Date:** 1999-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<XjmQ2.271$CU.79579@news4.mia>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be> <KOMP2.7079$w6.1889881@news4.mia> <37101be0.504662@news1.ibm.net>`

```
Thane Hubbell wrote:
>Judson McClendon wrote:
>>
…[17 more quoted lines elided]…
>then operate on that block.  Cut it, paste it, delete it etc..

Yep, that's 'block mode'. :-)  Below is an example of one reason why I
believe block mode to be so important in writing COBOL, copied from an
earlier post of mine.  It is a description of how to create a series of
MOVE statements to move a series of fields from one record to another, as
opposed to using MOVE CORRESPONDING.

============
1. Using your nifty-gee-whiz programmer's editor create a line with just
   'MOVE' in the appropriate column, then duplicate it at least as many times
   as you have fields to be inserted (see next step).  The result will look
   like this:

           MOVE
           MOVE
           MOVE
           ...
           MOVE

2. Use your editor's 'column copy' command to copy the names of the 'from'
   fields from the record description (01) immediately to the right of the
   MOVE's.  After you insert all the field names, you may need to delete any
   names which aren't needed.  The result will look like this:

           MOVE TRAN-FIELD-ONE
           MOVE TRAN-FIELD-TWO
           MOVE TRAN-FIELD-THREE
           ...
           MOVE TRAN-FIELD-NNN

3. Use a 'column insert' or macro to place 'TO XXXX-' after the field names,
   where 'XXXX-' is the prefix of the receiving fields.  You now have this:

           MOVE TRAN-FIELD-ONE   TO MAST-
           MOVE TRAN-FIELD-TWO   TO MAST-
           MOVE TRAN-FIELD-THREE TO MAST-
           ...
           MOVE TRAN-FIELD-NNN   TO MAST-

4. Now use your editor's 'column copy' to copy the part of the data names
   after the prefix from the left to the right.  The result should look
   like this:

           MOVE TRAN-FIELD-ONE   TO MAST-FIELD-ONE
           MOVE TRAN-FIELD-TWO   TO MAST-FIELD-TWO
           MOVE TRAN-FIELD-THREE TO MAST-FIELD-THREE
           ...
           MOVE TRAN-FIELD-NNN   TO MAST-FIELD-NNN

5. When I want periods after each move, I make sure to copy a space at the
   end of each data name, so each line will end with at least one space.
   I now do a 'regular expression' search and replace on those lines,
   replacing all ending spaces with a period.  (In Brief that regular
   expression syntax would be: replace ' +>' with '.'.)  You now have:

           MOVE TRAN-FIELD-ONE   TO MAST-FIELD-ONE.
           MOVE TRAN-FIELD-TWO   TO MAST-FIELD-TWO.
           MOVE TRAN-FIELD-THREE TO MAST-FIELD-THREE.
           ...
           MOVE TRAN-FIELD-NNN   TO MAST-FIELD-NNN.

Though this took a while to describe, with practice you can do it in just
a few seconds.  To start with, I would have the records I am moving from
and to, open in separate windows, and another window open on the area where
I am inserting the new code.  So it takes only a keystroke to swap between
them.  An additional benefit is that, since you use the editor to copy the
data names directly from the record description itself and you only type a
few text characters, the result is not likely to contain typing errors.

If you are not using techniques such as this, you are not anywhere near as
productive as you could be by using them.  If you don't have a programmer's
editor that can do the above kind of thing, then get one! :-)
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 8)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-04-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3711F73E.843D7C82@NOSPAMhome.com>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net> <370DFB24.6E65ED08@NOSPAMhome.com> <370f2bd0.391293@news.skynet.be> <KOMP2.7079$w6.1889881@news4.mia> <37101be0.504662@news1.ibm.net>`

```
> I wonder if we are defining block mode in the same way?  I mean, not a
> block of lines but actually being able to define the upper left corner
> and lower right corner of an edit block ANYWHERE in the source and
> then operate on that block.  Cut it, paste it, delete it etc..

That's the way Multi-Edit defines it.
```

###### ↳ ↳ ↳ Re: Editors

_(reply depth: 4)_

- **From:** kownby@humboldt1.com (Kindrick Ownby)
- **Date:** 1999-04-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<370e501d.15728048@news2.humboldt1.com>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net> <370C707A.DF2B1024@zip.com.au> <370d5d05.959024462@news1.ibm.net>`

```
In all the "editor" threads I have read in this group I have never
seen mention of the Codewright editor from Premia Corp.

I have been using it for several years - anybody else?

Kindrick
```

##### ↳ ↳ Re: Editors

- **From:** WDS@WDS.WDS.5 (WDS)
- **Date:** 1999-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3738d592.1642971@news1.frb.gov>`
- **References:** `<7ed391$d6s$1@news.igs.net> <370c0e10.4062279@netnews.worldnet.att.net>`

```
On Thu, 08 Apr 1999 03:50:46 GMT, Douglas J. Woods-Ledet wrote:

[snip discussion of various versions of SPF]

>Command Technology has no regard for their loyal customers who use the
>product because of the near zero learning cycle, i.e. you use it on
>the M/F, you use it on the PC, it is the same.

>Command Technology has no idea that their "new" product is to much
>like every other PC editor and therefore, I believe, will not attract
>any one who currently uses any other Editor.

[...]

I can agree with you, and I am viewing it from the opposite
perspective.  I am not an IBM mainframe user, and I tried SPF/PC a few
years ago.  While I did not find the learning curve to be very
difficult at all, I did not see that SPF/PC provided anything that
would particularly attract me as a new user.

Couple that expreience with the changes to make it more like other
generic Windows PC editors, and I find it even less attractive.

Just my opinion, of course; YMMV.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
