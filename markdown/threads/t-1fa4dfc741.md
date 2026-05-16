[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Call QBASIC from COBOL...?

_15 messages · 7 participants · 1999-10_

---

### Call QBASIC from COBOL...?

- **From:** "Steve Kalemkiewicz" <senseisk@hotmail.com>
- **Date:** 1999-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yT5L3.4620$0l6.8798@news.flash.net>`

```
Is it possible to CALL a QBASIC program (compiled) and pass data to it? then
get data passed back..

Or to Call a COBOL program with a QBASIC program and pass data to it?  (More
of a QBASIC question that COBOL but related nonetheless)  I know one would
probably use PEEK and POKE however I am not real familiar with these
commands...

Then link both (using either of the above) making an EXE?

-Steve Kalemkiewicz
```

#### ↳ Re: Call QBASIC from COBOL...?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<h1bL3.2501$7p6.28079@dfiatx1-snr1.gtei.net>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net>`

```
First off, QBasic is the INTERPRETER, not the compiler. QuickBASIC is the
compiler which produces EXE files.

Second, No, you can't. You can get data *to* the BASIC program via
command-line arguments, but you can't get it back into your COBOL program
(AFAIK). Same problem in reverse.

Second, you could create OBJ files with QuickBASIC, OBJ files with your
COBOL compiler and link those together with any linker to create an exe.
Note that with BOTH lanagugae products, you would need to specify the
compile/link options which allow you to create "standalone" programs, i.e.,
no run-time support required. Not that the run time would not work - I don't
have a clue - but I have to believe asking both language products to load
run-time support might make things a tad dicey vis-a-vis any spare memory in
"the lower 640."

Better idea (?): You could have the BASIC/COBOL program write a disk file
before exiting, and read that file after returning to your calling
COBOL/BASIC program.
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** gvwmoore@spam.ix.netcom.com (G Moore)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38004682.7294149@nntp.ix.netcom.com>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <h1bL3.2501$7p6.28079@dfiatx1-snr1.gtei.net>`

```
On Fri, 08 Oct 1999 00:37:33 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>Second, No, you can't. You can get data *to* the BASIC program via
>command-line arguments, but you can't get it back into your COBOL program
>(AFAIK). Same problem in reverse.

this is true. you cannot pass the variables back and forth. however,
you can use the address of and pointer variable, i think, to put the
address of a variable into a command line argument. beware, though,
that passing might change the memory location.
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** gvwmoore@spam.ix.netcom.com (G Moore)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37fd6b96.143244@nntp.ix.netcom.com>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <h1bL3.2501$7p6.28079@dfiatx1-snr1.gtei.net>`

```
On Fri, 08 Oct 1999 00:37:33 GMT, "Michael Mattias"
<michael.mattias@gte.net> wrote:

>Better idea (?): You could have the BASIC/COBOL program write a disk file
>before exiting, and read that file after returning to your calling
>COBOL/BASIC program.

i'm sorta drunk right now, so excuse me if my answer sounds stupid,
but you are right. i mean, saving to a file is umm just another disk
access, and assuming you have a cache program, it will only need to
access that file you pass parameters, and, it's only another disk
access, and since this is not mainframe work, milliseconds don't
count.
```

#### ↳ Re: Call QBASIC from COBOL...?

- **From:** gvwmoore@spam.ix.netcom.com (G Moore)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38043c0c.4723989@nntp.ix.netcom.com>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net>`

```
On Thu, 07 Oct 1999 18:45:50 GMT, "Steve Kalemkiewicz"
<senseisk@hotmail.com> wrote:

>Is it possible to CALL a QBASIC program (compiled) and pass data to it? then
>get data passed back..

qbasic cannot be compiled. i assume you mean a quickbasic program.

>Or to Call a COBOL program with a QBASIC program and pass data to it?  (More
>of a QBASIC question that COBOL but related nonetheless)  I know one would
>probably use PEEK and POKE however I am not real familiar with these
>commands...

no, the command in qbasic is call absolute. i don't know the command
in quickbasic (but i'll look it up and followup the thread). as for
which cobol command to use, it depends on the compiler. i know in
microfocus cobol in the samples directly, doscmd.cbl describes calling
an exe.

>Then link both (using either of the above) making an EXE?

no, just make one call another. linking would require more coding, and
programming cost is more a premium than a few milliseconds disk access
time.
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** gvwmoore@spam.ix.netcom.com (G Moore)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37ff4621.7197866@nntp.ix.netcom.com>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <38043c0c.4723989@nntp.ix.netcom.com>`

```
On Fri, 08 Oct 1999 00:45:46 GMT, gvwmoore@spam.ix.netcom.com (G
Moore) wrote:

>i know in
>microfocus cobol in the samples directly, doscmd.cbl describes calling
>an exe.

also addem*.cbl in the samples directory describes calling an
assembler routine, if you want to get deep into passing variables back
and forth.
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** gvwmoore@spam.ix.netcom.com (G Moore)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38014824.7540872@nntp.ix.netcom.com>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <38043c0c.4723989@nntp.ix.netcom.com>`

```
On Fri, 08 Oct 1999 00:45:46 GMT, gvwmoore@spam.ix.netcom.com (G
Moore) wrote:

>On Thu, 07 Oct 1999 18:45:50 GMT, "Steve Kalemkiewicz"
><senseisk@hotmail.com> wrote:
…[12 more quoted lines elided]…
>in quickbasic (but i'll look it up and followup the thread).

the commands in quickbasic you need to look up are cdecl, call, calls,
byval, command$

that's the best references i can get. if you need more help, for
quickbasic calling cobol, you might want to try the basic newsgroup.
but if you tell us the coobl compiler, we can write up some quick code
which passes variables, via command line, into an exe.
```

###### ↳ ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** "Steve Kalemkiewicz" <senseisk@hotmail.com>
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NqdL3.4967$0l6.9575@news.flash.net>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <38043c0c.4723989@nntp.ix.netcom.com> <38014824.7540872@nntp.ix.netcom.com>`

```
I have the Fujitsu COBOL85 version 3 Compiler for Win9x...

THANK YOU SO MUCH
-Steven Kalemkiewicz
```

###### ↳ ↳ ↳ Re: Call QBASIC from COBOL...?

_(reply depth: 4)_

- **From:** gvwmoore@spam.ix.netcom.com (G Moore)
- **Date:** 1999-10-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37fd8f39.9129963@nntp.ix.netcom.com>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <38043c0c.4723989@nntp.ix.netcom.com> <38014824.7540872@nntp.ix.netcom.com> <NqdL3.4967$0l6.9575@news.flash.net>`

```
On Fri, 08 Oct 1999 03:21:17 GMT, "Steve Kalemkiewicz"
<senseisk@hotmail.com> wrote:

>I have the Fujitsu COBOL85 version 3 Compiler for Win9x...


http://www.adtools.com/download/v3samples/index.htm

look up cblexec and cmdline sample programs.
```

#### ↳ Re: Call QBASIC from COBOL...?

- **From:** AnhMy Tran <anhmytran@hotmail.com>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s0cl8q9hu276@corp.supernews.com>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net>`

```
NO.  Absolutely NO.

1- All kind of BASIC (not Visual BASIC by MS) are interpreters.
   They cannot make EXEs. User should run the source code within
   BASIC environment. Outside BASIC environment, the programs are
   merely text files.

2- In Object Oriented Design, the system memory can store variables
   back and forth from DLL or API processing. 
   There are no system memory storage for COBOL and BASIC processing.
   So COBOL EXEs and BASIC cannot call or be called from any EXEs.
   In COBOL, there is LINKAGE SECTION that declare variables as global
   to pass between calling and called programs. Called program should
   be compiled prior to calling programs being compiled.
   After the calling programs compiled, they make EXEs there.
   Differ from EXEs in OO design, they are always big, for they contain
   all called programs inside them. (In OO design, the calling EXEs are
   small, just enough to call others, not to contain them.)

------------------  Posted via CNET Help.com  ------------------
                      http://www.help.com/
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ygwN3.3635$LW6.58148@news2.mia>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <s0cl8q9hu276@corp.supernews.com>`

```
Actually, statment #2 is incorrect.

ALL COBOLs have memory storage, its just that all memory within a 'run unit'
is USUALLY
STATIC for the duration.

ALL COBOLs can be called from other Object Modules (Compiled BASIC,
assembler exes, etc)
ALL COBOLs can 'call' other Object Modules as long as each use the same
interface.


AnhMy Tran wrote in message ...
>NO.  Absolutely NO.
>
…[18 more quoted lines elided]…
>                      http://www.help.com/
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<UfvN3.1405$Ba1.29407@dfiatx1-snr1.gtei.net>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <s0cl8q9hu276@corp.supernews.com>`

```
I think you are about, oh, six to eight years behind the times.

AnhMy Tran wrote in message ...
>NO.  Absolutely NO.
>
…[3 more quoted lines elided]…
>   merely text files.



There are numerous compiled BASICs: Microsoft, PowerBASIC, XBasic,
TrueBASIC; even BBx Business Basic is compiled into p-code, depending only
on the availablility of the correct run-time on the target system.

>2- In Object Oriented Design, the system memory can store variables
>   back and forth from DLL or API processing.
…[4 more quoted lines elided]…
>   be compiled prior to calling programs being compiled.

Huh? DLL's are written to effect linkage within an address space under
Windows;it's a little different 16-bit vs. 32-bit, but eminently do-able.
COBOL programs can call DLL's, no problem.

Under MS-DOS, TSR programs responding to an interrupt may be used. If the
COBOL program can generate a software interrupt, sha-zam! you're in
business. Although usually in this environment, you would just have the
BASIC compiler generate an OBJ file and static-link it to the COBOL program.

Now, the original question was specifically about QBasic, an interpreted
product, in which case communications is not possible. Although either
program may shell the other, and pass data to it, it cannot get the
(modified) data back.

MCM
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3806b19c.49038553@news2.ibm.net>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <s0cl8q9hu276@corp.supernews.com>`

```
On Thu, 14 Oct 1999 22:11:38 GMT, AnhMy Tran <anhmytran@hotmail.com> wrote:

>NO.  Absolutely NO.
>
…[3 more quoted lines elided]…
>   merely text files.

Wrong.  I had my first BASIC Compiler about 10 years agi
>
>2- In Object Oriented Design, the system memory can store variables
>   back and forth from DLL or API processing. 
>   There are no system memory storage for COBOL and BASIC processing.
>   So COBOL EXEs and BASIC cannot call or be called from any EXEs.

Wrong again, on all counts.  COBOL program can call other programs, can CALL DLLs.  COBOL
Programs can be called by other programs.  COBOL Programs can be made into DLLs and be
called by other programs


>   In COBOL, there is LINKAGE SECTION that declare variables as global
>   to pass between calling and called programs. 

This one is more or less correct
>   Called program should
>   be compiled prior to calling programs being compiled.

Why should THAT be?  The CALLED program (and the CALLING program) must be COMPILED 
before the LINKER creates the EXE module, and this is only true if we are talking
about STATIC calls.  On DYNAMIC call, the sequence of COMPILE/LINK is irrelevant

     With kind Regards            |\      _,,,---,,_
                            ZZZzz /,`.-'`'    -.  ;-;;,
     Volker Bandke               |,4-  ) )-,_. ,\ (  `'-'
      (BSP GmbH)                '---''(_/--'  `-'\_)

         All generalizations are false, including this one.
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** "Steve Kalemkiewicz" <senseisk@hotmail.com>
- **Date:** 1999-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<wCDN3.781$4w1.50949@news.flash.net>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <s0cl8q9hu276@corp.supernews.com>`

```
Regarding the interpreter Vs. compiler issue for BASIC...  I was speaking
about the COMPILER QuickBasic not the interpreter QBAISC...  My error for
using the wrong name..

-SPK
```

##### ↳ ↳ Re: Call QBASIC from COBOL...?

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7u71u0$h3o$2@news.igs.net>`
- **References:** `<yT5L3.4620$0l6.8798@news.flash.net> <s0cl8q9hu276@corp.supernews.com>`

```
You are about fifteen years out of date.

AnhMy Tran wrote in message ...
>NO.  Absolutely NO.
>
…[18 more quoted lines elided]…
>                      http://www.help.com/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
