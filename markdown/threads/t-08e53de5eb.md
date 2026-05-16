[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# what is the best way to debug a cobol program

_21 messages · 14 participants · 2003-02 → 2003-03_

---

### what is the best way to debug a cobol program

- **From:** "Paul" <paulhbliu@hotmail.com>
- **Date:** 2003-02-28T11:38:33-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com>`

```
Hi

what is the best EASY or BEST way to debug a cobol program

thanks
Paul
```

#### ↳ Re: what is the best way to debug a cobol program

- **From:** docdwarf@panix.com
- **Date:** 2003-02-28T11:57:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3o4d4$bg$1@panix1.panix.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com>`

```
In article <egM7a.7762$kf7.1072047@news20.bellglobal.com>,
Paul <paulhbliu@hotmail.com> wrote:
>Hi
>
>what is the best EASY or BEST way to debug a cobol program

The best EASY and best BEST ways are the same: find someone who knows how 
to do it and pay them well for their work.

Now please do your own homework.

DD
```

##### ↳ ↳ Re: what is the best way to debug a cobol program

- **From:** "Paul" <paulhbliu@hotmail.com>
- **Date:** 2003-02-28T12:04:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<TEM7a.7769$kf7.1078145@news20.bellglobal.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com>`

```
Paying to people = less fun to yrself

I mean to debug a javascript you can use a alert to debug step by step
what will be suitable way in cobol ?

thanks.Paul

<docdwarf@panix.com> wrote in message news:b3o4d4$bg$1@panix1.panix.com...
> In article <egM7a.7762$kf7.1072047@news20.bellglobal.com>,
> Paul <paulhbliu@hotmail.com> wrote:
…[9 more quoted lines elided]…
> DD
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

- **From:** docdwarf@panix.com
- **Date:** 2003-02-28T12:43:50-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3o74m$ikt$1@panix1.panix.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com>`

```
In article <TEM7a.7769$kf7.1078145@news20.bellglobal.com>,
Paul <paulhbliu@hotmail.com> wrote:
>Paying to people = less fun to yrself
>
>I mean to debug a javascript you can use a alert to debug step by step
>what will be suitable way in cobol ?

Ahhhh... that depends on the platform and version of the language you are 
using.  Details, please?

DD

><docdwarf@panix.com> wrote in message news:b3o4d4$bg$1@panix1.panix.com...
>> In article <egM7a.7762$kf7.1072047@news20.bellglobal.com>,
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 4)_

- **From:** "Paul" <paulhbliu@hotmail.com>
- **Date:** 2003-02-28T13:31:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gWN7a.7930$kf7.1093268@news20.bellglobal.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <b3o74m$ikt$1@panix1.panix.com>`

```
I use Cygwin and open-cobol 0.9.7 for cygwin, I don't have preveledge use
the cobol legacy system

for example:
----- first one -------
IDENTIFICATION DIVISION.
PROGRAM-ID.    hello.

ENVIRONMENT DIVISION.

INPUT-OUTPUT SECTION.
FILE-CONTROL.
 SELECT INP-DATA ASSIGN TO "input.dat".
** SELECT RESULT-FILE ASSIGN TO OUTPUT.

DATA DIVISION.

FILE SECTION.
FD INP-DATA
**   LABEL RECORD IS STANDARD.
01 ITEM-PRICE.
 02 ITEM PIC X(30).
** 02 PRICE PIC 9999v99.
** 02 FILLER PIC X(50).

WORKING-STORAGE SECTION.
01 PROMPT-1 PIC X(9) VALUE "First".
01 DISPLAY-W PIC X(30).
01 PROMPT-1 PIC X(9) VALUE "Second".
01 PROMPT-1 PIC X(9) VALUE "Third".

01 YES-NO PIC X.
01 ENTRY-OK PIC X.
01 END-OF-FILE PIC X.
01 SCREEN-LINES PIC 99.
01 A-DUMMY PIC X.

PROCEDURE DIVISION.
    DISPLAY "hello," WITH NO ADVANCING
    DISPLAY "world!"
 PERFORM OPEN-PROCEDURE.
 PERFORM READ-NEXT-RECORD.

 PERFORM DISPLAY-RECORDS

 PERFORM CLOSE-PROCEDURE.
    STOP RUN.

OPEN-PROCEDURE.
 OPEN EXTEND INP-DATA.

CLOSE-PROCEDURE.
 CLOSE INP-DATA.

READ-NEXT-RECORD.
 READ INP-DATA
 AT END
 MOVE "Y" TO END-OF-FILE.
 DISPLAY INP-DATA.

DISPLAY-RECORDS.
 PERFORM DISPLAY-FIELDS.
 PERFORM READ-NEXT-RECORD.


DISPLAY-FIELDS.
** IF SCREEN-LINES = 15
  PERFORM PRESS-ENTER.
 MOVE ITEM TO DISPLAY-W.
 DISPLAY DISPLAY-W.
 DISPLAY ITEM.
 DISPLAY "OK".

PRESS-ENTER.
 DISPLAY "Press enter to continue ... ".
 ACCEPT A-DUMMY.
 MOVE ZEROS TO SCREEN-LINES.
------- end of first one ---------

The compile running result :
$ cobc hello.cbl
hello.cbl:15: warning: keyword `LABEL RECORD' is obsolete
parser.y:2753: invalid type cast from `#<unknown 10 0x100b2c70>'
Aborted (core dumped)

=======================
Or Do you have any suggestion that what kind of enviroment and cobol
compiler I can choose
will be suitable for windows NT

Thank you !!
Paul
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-28T13:10:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3oc7n$9p5$1@slb9.atl.mindspring.net>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <b3o74m$ikt$1@panix1.panix.com> <gWN7a.7930$kf7.1093268@news20.bellglobal.com>`

```
Your note may or may not have an English language problem - but what you
have shown is a problem with the COMPILER and not with your program. (Or at
least the compiler isn't giving you any "useful" information when it has an
error).

The "other hints" about debugging assumed that you got a "clean compile" but
weren't getting the expected output.  Your message:

 "parser.y:2753: invalid type cast from `#<unknown 10 0x100b2c70>'
    Aborted (core dumped)"

indicates that the compiler itself is having a problem.  (You may or may not
have a "logic" problem in your program causing the problem - but no "good"
compiler should leave you with this type of message.)

Looking at the web page (and pointed to pages) at:
  http://www.open-cobol.org/

It looks like there are NEWER releases of open-cobol that you might want to
try and see if they fix the problem.  If you still have problems, you might
want to ask the group doing that "open-cobol" project about it.
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-02T22:24:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e6284a5.88031160@news.optonline.net>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <b3o74m$ikt$1@panix1.panix.com> <gWN7a.7930$kf7.1093268@news20.bellglobal.com>`

```
"Paul" <paulhbliu@hotmail.com> wrote:

>I use Cygwin and open-cobol 0.9.7 for cygwin, I don't have preveledge use
>the cobol legacy system
…[21 more quoted lines elided]…
>** 02 FILLER PIC X(50).

>
>The compile running result :
…[3 more quoted lines elided]…
>Aborted (core dumped)

The fact that you get a warning about LABEL RECORD indicates that your
commenting style is not working. Try changing all the commented lines to *>
or removing them. My guess is the compiler is choking on result-file.

Robert
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

- **From:** "Don Leahy" <xdb2imsN@nospam.whatever.net>
- **Date:** 2003-02-28T13:21:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8NN7a.13935$os6.1058798@news20.bellglobal.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com>`

```
"Paul" <paulhbliu@hotmail.com> wrote in message
news:TEM7a.7769$kf7.1078145@news20.bellglobal.com...
> Paying to people = less fun to yrself
>
…[4 more quoted lines elided]…
>
Many (perhaps all) Cobol platforms have source level debuggers (even the
mainframe), so it depends.

If you don't have access to such a tool, then your next best bet is to add
temporary DISPLAY messages to the code near the area where the problem might
be.  (I am assuming that you've at least inspected the code looking for
obvious causes).
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 4)_

- **From:** "Paul" <paulhbliu@hotmail.com>
- **Date:** 2003-02-28T13:42:39-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<A4O7a.7952$kf7.1094850@news20.bellglobal.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <8NN7a.13935$os6.1058798@news20.bellglobal.com>`

```
Hi Don

I use cygwin and open-cobol 0.9.7  inmy windows NT, sorry I don't have
access to mainframe, which makes it urgly to me

besides the example mentioned before,
another problem
------- begin of prog --------
   IDENTIFICATION DIVISION.
       PROGRAM-ID.    hello.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
         COPY CSCSCD00.

       PROCEDURE DIVISION.
           DISPLAY "hello ," WITH NO ADVANCING
           DISPLAY "world!"
           STOP RUN
------- end of prog --------

I got result:
$ cobc aa.cbl
CSCSCD00:2: parse error before `ok'

the cscscd00 begin part like this
000010*==============================================================*
00001000
000020* THat COPY CODE ok THE CONTROL BLOCK
*  00002000
000030* PROGRAM PSCSCD.                                              *
00003000
000040*==============================================================*
00004000
000050
00005000
000100 01 CSCSCD00.
00010000
000110
00011000
000200    02 CSCSCD00-PUBLIC-AREA.
00020000
000201
00020100
000210       05 CSCSCD00-INPUT-COMMON.
00021000
000300          10  CSCSCD00-EYECATCH        PIC X(8).
00030000
000400          10  CSCSCD00-CB-VERSION-NUM  PIC X(2).
00040000
000500              88 CSCSCD00-CURRENT-VERSION VALUE X'0100'.
00050000
000600          10  CSCSCD00-API-VERSION-NUM PIC X(2).
00060000
000700              88 CSCSCD00-API-VER0100     VALUE X'0100'.
00070000
... ....

I'm not sure if it's because the number probelm front and trail number (like
00070000 )
what's the error message tell me ?

thank you
Paul


"Don Leahy" <xdb2imsN@nospam.whatever.net> wrote in message
news:8NN7a.13935$os6.1058798@news20.bellglobal.com...
> "Paul" <paulhbliu@hotmail.com> wrote in message
> news:TEM7a.7769$kf7.1078145@news20.bellglobal.com...
…[11 more quoted lines elided]…
> temporary DISPLAY messages to the code near the area where the problem
might
> be.  (I am assuming that you've at least inspected the code looking for
> obvious causes).
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-28T14:35:41-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302281435.283988c5@posting.google.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <8NN7a.13935$os6.1058798@news20.bellglobal.com> <A4O7a.7952$kf7.1094850@news20.bellglobal.com>`

```
"Paul" <paulhbliu@hotmail.com> wrote

> another problem
> 
> I got result:
> $ cobc aa.cbl
> CSCSCD00:2: parse error before `ok'

Not having used Open-Cobol I would guess that this is complaining
about line 2 of CSCSCD00 at some point before it has found 'ok'
somewhat later.
 
> the cscscd00 begin part like this
> 000010*==============================================================*
> 00001000
        ^^  what is this ? 

> 000020* THat COPY CODE ok THE CONTROL BLOCK

I suggest that you remove all the line number in columns 1-6 and leave
these blank (they don't do anything useful) and ensure that you don't
have spurious characters in cols 7 and 8 (which seems to be the case).
 Also make sure that the lines are correctly terminated, especially if
you have moved them from another machine.
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 6)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-03-03T16:06:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3vuin$2qb$1@peabody.colorado.edu>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <8NN7a.13935$os6.1058798@news20.bellglobal.com> <A4O7a.7952$kf7.1094850@news20.bellglobal.com> <217e491a.0302281435.283988c5@posting.google.com>`

```

On 28-Feb-2003, riplin@Azonic.co.nz (Richard) wrote:

> I suggest that you remove all the line number in columns 1-6 and leave
> these blank (they don't do anything useful) and ensure that you don't
> have spurious characters in cols 7 and 8 (which seems to be the case).

Line numbers can be useful in environments which use lots of copy members.  
That way we can cross reference a line in the compiler listing with a source
code line.


  002002         050800     IF CC-UPDATE-SW = 'Y'
PP 5648-A25 IBM COBOL for OS/390 & VM  2.2.1                   SIPR486   Date 02
  LineID  PL SL  ----+-*A-1-B--+----2----+----3----+----4----+----5----+----6---
  002003      1  050900         DISPLAY 'READYING AREAS IN UPDATE MODE'
  002004         051000*        READY IASAR102-REGION USAGE-MODE UPDATE
  002005      1                   MOVE 2 TO DML-SEQUENCE
  002006      1                   CALL 'IDMS' USING SUBSCHEMA-CTRL
  002007      1                           IDBMSCOM (36)
  002008      1                           IASAR102-REGION
  002009      1                     PERFORM IDMS-STATUS;
  002010         051100*        READY IASAR108-REGION USAGE-MODE UPDATE
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-03-03T15:08:57-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0303031508.676783cd@posting.google.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <8NN7a.13935$os6.1058798@news20.bellglobal.com> <A4O7a.7952$kf7.1094850@news20.bellglobal.com> <217e491a.0302281435.283988c5@posting.google.com> <b3vuin$2qb$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> > I suggest that you remove all the line number in columns 1-6 and leave
> > these blank (they don't do anything useful) and ensure that you don't
> > have spurious characters in cols 7 and 8 (which seems to be the case).

I later realised that the lines had been wrapped and the cols 73-80
were appearing on the next line.
 
> Line numbers can be useful in environments which use lots of copy members.  
> That way we can cross reference a line in the compiler listing with a source
> code line.

Maybe.  But you are using it on Linux which has different tools. In
fact the line numbers, cols 73-80 and the comments are in fact the
problem.  The Open Cobol documentation has:

""" -----------------------------------------------------------
Source Format

OpenCOBOL supports both fixed and free source format.

The format can be explicitly specified by giving one of the following
options to cobc:

-free
    Free format.
-fixed
Fixed format.

If non of these options is given, the format is automatically
determined by the following rule.

The compiler inspects the first six characters of the first line in
the source file. If the characters are all digits or spaces, the
format is considered to be fixed format. Otherwise, it is free format.
----------------------------------------------- """

Compile with -fixed option, or put '000000' in cols 1-6 of the first
line of the program.
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

_(reply depth: 5)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-03-02T22:44:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e62895e.89240127@news.optonline.net>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o4d4$bg$1@panix1.panix.com> <TEM7a.7769$kf7.1078145@news20.bellglobal.com> <8NN7a.13935$os6.1058798@news20.bellglobal.com> <A4O7a.7952$kf7.1094850@news20.bellglobal.com>`

```
"Paul" <paulhbliu@hotmail.com> wrote:

>Hi Don
>
…[57 more quoted lines elided]…
>what's the error message tell me ?

It tells you the compiler is not recognizing comment lines. It should not be
parsing comment lines. The old, fixed-form, notation for comments was * in
column 7; the new, free-form, is *>

Because you are switching from free-form, in the main program, to fixed-form, in
the copybook, you need a compiler directive before and after the copybook. In
the compiler's manual, look for options named something like FIXED and FREE,
then figure out how to imbed them in your program. Every compiler does it
differently; most use a character such as $ or @, often followed by as word such
as SET or OPTIONS. 

Alternatively, change the copybook to free-form by removing line numbers and
numbers at the ends of lines. While you are at it, delete 'eyecatch'. It is an
obsolete holdover from the Good Old Days, when COBOL programmers debugged by
reading memory dumps. 

Robert
```

#### ↳ Re: what is the best way to debug a cobol program

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-02-28T17:17:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3o5ir$s3v$1@peabody.colorado.edu>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com>`

```

On 28-Feb-2003, "Paul" <paulhbliu@hotmail.com> wrote:

> what is the best EASY or BEST way to debug a cobol program

Depends.
```

##### ↳ ↳ Re: what is the best way to debug a cobol program

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-02-28T18:41:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3O7a.30$3g.21046@newssrv26.news.prodigy.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o5ir$s3v$1@peabody.colorado.edu>`

```
> On 28-Feb-2003, "Paul" <paulhbliu@hotmail.com> wrote:
>
>  what is the best EASY or BEST way to debug a cobol program

Easiest way is to slap a 'Microsoft' label on it. Those programs aren't
debugged.

MCM
```

##### ↳ ↳ Re: what is the best way to debug a cobol program

- **From:** "Thomas Li" <ali2481spam@rogers.com>
- **Date:** 2003-02-28T21:47:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<BNQ7a.15382$em1.8442@news04.bloor.is.net.cable.rogers.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <b3o5ir$s3v$1@peabody.colorado.edu>`

```
I think the best way to debug COBOL programs is to find the BEST compiler
with easy to use IDE, such as Microsoft Visual Studio. Try IBM or Microfocus
COBOL compiler.
```

#### ↳ Re: what is the best way to debug a cobol program

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-03-02T17:26:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E623EC2.9010107@optonline.NOSPAM.net>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com>`

```
Paul wrote:
> Hi
> 
> what is the best EASY or BEST way to debug a cobol program

Sacrifice a virgin goat & pray to Baal.
```

##### ↳ ↳ Re: what is the best way to debug a cobol program

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-03-02T20:22:42+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fui46v401hrbcllu8lg1p1r11tp2njvf7c@4ax.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <3E623EC2.9010107@optonline.NOSPAM.net>`

```
On Sun, 02 Mar 2003 17:26:12 GMT Liam Devlin <LiamD@optonline.NOSPAM.net>
wrote:

:>Paul wrote:
 
:>> what is the best EASY or BEST way to debug a cobol program

:>Sacrifice a virgin goat & pray to Baal.

Give a virgin and some barbecued goat to the systems programmer.
```

###### ↳ ↳ ↳ Re: what is the best way to debug a cobol program

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2003-03-02T20:14:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E626684.CB90F071@shaw.ca>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com> <3E623EC2.9010107@optonline.NOSPAM.net> <fui46v401hrbcllu8lg1p1r11tp2njvf7c@4ax.com>`

```


Binyamin Dissen wrote:

> On Sun, 02 Mar 2003 17:26:12 GMT Liam Devlin <LiamD@optonline.NOSPAM.net>
> wrote:
…[8 more quoted lines elided]…
>

> and Liam also replied :-

> Sacrifice a virgin goat & pray to Baal.

Surely that has to be more than just a *coincidence* ? Are the 'Israelite'
and 'Paddy' quoting from the same source <G>.

On the topic of virgins - and our fundamentalist friends who think it's OK to
blow themselves up and kill a few Jews or Yanks in the process - gives them a
quick pass to  Allah where they can enjoy their 70 virgins. It is my fervent
wish that they find that each of the *virgins* inherited a social disease !

Jimmy, Calgary AB
```

#### ↳ Re: what is the best way to debug a cobol program

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-03-02T14:03:56-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uR2cnXn-w_2M-f-jXTWciQ@giganews.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com>`

```

"Paul" <paulhbliu@hotmail.com> wrote in message
news:egM7a.7762$kf7.1072047@news20.bellglobal.com...
> Hi
>
…[3 more quoted lines elided]…
> Paul

Being a mathematician by training, I do it the same way I cure occasional
constipation:

I work it out with a pencil.

Your results may vary.
```

#### ↳ Re: what is the best way to debug a cobol program

- **From:** mfcobol2002 <marcos_as@terra.com.br>
- **Date:** 2003-03-04T11:36:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2601464.1046777806@dbforums.com>`
- **References:** `<egM7a.7762$kf7.1072047@news20.bellglobal.com>`

```

Microfocus Cobol (netexpress) it uses the debbuger ANIMATOR.
you can execute line to line , blocks of instructions, to do
demarcations and to see and to alter the content of the variables during
the debug.

Marcos A.S.
Brazil
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
