[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# compile+link Fujitsu Linux

_81 messages · 8 participants · 2008-01 → 2008-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### compile+link Fujitsu Linux

- **From:** charles.goodman@bell.ca
- **Date:** 2008-01-30T15:00:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com>`

```
I am evaluating Fujitsu NetCOBOL for Linux.
I am having problems getting CALL/CANCEL to work.
Here are two simple programs, first the main program then the called
program:

       IDENTIFICATION DIVISION.
       PROGRAM-ID. MYMAIN.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  ACPT    PIC X.
       PROCEDURE DIVISION.
       OPEN-PARA.
           DISPLAY "BEGIN MYMAIN".
           CALL 'MYSUB1'.
           DISPLAY "THE END - ACCEPTING ONE BYTE".
           ACCEPT ACPT.
           STOP RUN.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. MYSUB1.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  ACPT    PIC X.
       PROCEDURE DIVISION.
       OPEN-PARA.
           DISPLAY "BEGIN MYSUB1 - ACCEPTING ONE BYTE".
           ACCEPT ACPT.
           EXIT PROGRAM.

The two source programs are saved as MYMAIN.CBL and MYSUB1.CBL.
We want dynamic linkage since our real application consists of dozens
of C programs and hundreds of COBOL programs.

I tried compiling with:
cobol -M -dy -WC,"BINARY(BYTE),DLOAD" -o MYMAIN MYMAIN.CBL
cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB1.so MYSUB1.CBL

when I try to execute I see my first DISPLAY and then it crashes:
BEGIN MYMAIN
cobol-rts:: HALT: JMP0015I-U [PID:0000763D TID:002516C0] CANNOT CALL
PROGRAM 'MY
SUB1'. ./MYMAIN: undefined symbol: MYSUB1 PGM=MYMAIN
Aborted

I am running on Red Hat Enterprise, and Fujitsu support say they will
only support:
    * Red Hat Linux 7.2, Locale C
    * Red Hat Linux 7.3, Locale C
    * Red Hat Linux Advanced Server 2.1, Locale C

I am hoping that someone here has figured out how to compile and line
on less ancient versions of Linux.

---Charlie
```

#### ↳ Re: compile+link Fujitsu Linux

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-30T21:38:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com>`

```
On Wed, 30 Jan 2008 15:00:14 -0800 (PST), charles.goodman@bell.ca wrote:

>I am evaluating Fujitsu NetCOBOL for Linux.
>I am having problems getting CALL/CANCEL to work.
…[49 more quoted lines elided]…
>on less ancient versions of Linux.

Try '-l MYSUB1' (lower case el) on the compilation of MYMAIN. As written, MYMAIN has no
way of knowing the library name. Also, make sure your current directory is in
LD_LIBRARY_PATH, either as .: or explicitly.
```

##### ↳ ↳ Re: compile+link Fujitsu Linux

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-30T20:46:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com>`

```
On Jan 31, 4:38 pm, Robert <n...@e.mail> wrote:
> On Wed, 30 Jan 2008 15:00:14 -0800 (PST), charles.good...@bell.ca wrote:
> >I am evaluating Fujitsu NetCOBOL for Linux.
…[53 more quoted lines elided]…
> way of knowing the library name.

I think that you fail to understand what 'Dynamic Load' means.

> Also, make sure your current directory is in
> LD_LIBRARY_PATH, either as .: or explicitly.

Yes, it does need that.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-31T00:23:12-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com>`

```
On Wed, 30 Jan 2008 20:46:28 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Jan 31, 4:38 pm, Robert <n...@e.mail> wrote:

>> >when I try to execute I see my first DISPLAY and then it crashes:
>> >BEGIN MYMAIN
…[17 more quoted lines elided]…
>I think that you fail to understand what 'Dynamic Load' means.

There is no Cobol syntax to specify a library name. You can only specify an entry point
name. When you do a CALL, Unix doesn't search every library in the library path. That
would be hopelessly slow. It searches only the libraries named in the executable's ELF
header. 

Libraries normally contain many programs and entry points. They are not one-for-one like
the example here.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 4)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-31T11:47:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com>`

```
On Jan 31, 7:23 pm, Robert <n...@e.mail> wrote:
> On Wed, 30 Jan 2008 20:46:28 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Jan 31, 4:38 pm, Robert <n...@e.mail> wrote:
…[27 more quoted lines elided]…
> the example here.

Robert, you really should try to understand the problem and its
solution _before_ you show your complete lack of understanding of what
is happening.

I had already said that the code and compiles as given in the first
message _worked_ on my machine and that the only change required was
to the LD_LIBRARY_PATH which is the environment variable used for
_dynamic_ loads.

I had actually compiled and ran these programs to ensure that what I
said was correct and that I was not giving bad or wrong advice. I had
indicated, gently, to you that you were not on the right track.

I have used dynamic loading of Cobol with mainframes, with Micro Focus
since CIS Cobol, on RM, Fujitsu and others since the days of CP/M and
with Unix, DOS, Windows and Linux. I have even done dynamic loading
with C.

You have made several claims above which are FACTUALLY WRONG and show
that you, as I said before, completely fail to understand dynamic
loading, or even that it is possible.

With Fujitsu Cobol the DLOAD directive tells the system that CALLs
might be dynamic. In these cases there is no need for the library
containing the called routine to be known to the ELF binary, there is
no need for a -l, nor for the library to even exist at link (ld) time.

At run time a dynamic call will look for a file called libNAME.so
along the LD_LIBRARY_PATH, where NAME is that in the CALL, and it will
load that and find the required entry point.

As you should be able to tell from the results in charles' 2nd message
your BAD and WRONG advice has meant that his program does not work as
he expected. He statically linked the dynamic library which will cause
the CANCEL to fail to unload it and thus a reload does not find a new
copy but reuses the old.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 5)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-31T21:23:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com>`

```
On Thu, 31 Jan 2008 11:47:51 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Jan 31, 7:23 pm, Robert <n...@e.mail> wrote:
>> On Wed, 30 Jan 2008 20:46:28 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[28 more quoted lines elided]…
>> the example here.

[the usual insults snipped]

>With Fujitsu Cobol the DLOAD directive tells the system that CALLs
>might be dynamic. In these cases there is no need for the library
>containing the called routine to be known to the ELF binary, there is
>no need for a -l, nor for the library to even exist at link (ld) time.

Normal Unix binding, outside Cobol, is to enter the names of called libraries in the
executable's header, using -l . Doing so does NOT mean they are statically linked as the
term is understood by mainframers and others from the Old School. It means the library
files will be loaded (if not already in memory) when the executable starts. If any cannot
be found, the program will not start, which guarantees the program will not abort mid-run
because a called program is missing. It also allows useful diagnostics to be run before
starting a long batch job. 

A Windows dll works almost exactly the same as a Unix library (.so).

Cobol can, and I believe should, use the normal Unix binding mechanism. There are several
advantages and no good reason not to. In addition to the advantages given above, one
specific to Cobol is non-proliferation of program files, which I'll explain below.

Dynamic binding is the alternative. A running program can ask the OS to load an additional
library by specifying its FILE NAME. Technically, this is done with a call to dlopen() (or
LoadLibrary() on Windows). The OS first checks to see whether the library is already
loaded in memory, either because it was in the program's own header or because some other
running process is using it. If not, it searches the library path looking for the file
name and loads it. In either case it returns a handle to THE FILE that the program can use
to search for a specific entry point or the file's default entry point (with the dlsym()
function). 

The problem with dynamic binding in Cobol is that Cobol has no concept of library FILE
NAME, it only knows about entry point names, which are essentially the same as program
names. Thus, Charles' application with "hundreds of COBOL programs", if packaged for
dynamic call, will have HUNDREDS OF LIBRARY FILES, each named libPROGRAM.so. I find that
ugly and, from a deployment point of view, clunky and amateurish. It would be cleaner to
package his hundreds of programs into one or a few libraries that are linked to the main
executable.  

How many third-party apps have you seen that came with hundreds of libraries or dlls? 

>At run time a dynamic call will look for a file called libNAME.so
>along the LD_LIBRARY_PATH, where NAME is that in the CALL, and it will
>load that and find the required entry point.

It will first look for the symbol NAME already loaded. If not found THEN it will load
libNAME.so. 

>As you should be able to tell from the results in charles' 2nd message
>your BAD and WRONG advice has meant that his program does not work as
>he expected. He statically linked the dynamic library which will cause
>the CANCEL to fail to unload it and thus a reload does not find a new
>copy but reuses the old.

Wrong. If Cobol issues a dlclose() on libMYSUB1.so, even though it was 'statically' linked
with -l, it will be unloaded .. and reloaded the next time he calls it. 

If it is packaged in a library with a hundred other programs, the whole library might be
unloaded, because the handle for NAME is the handle for libMYSUBS.so. Or Fujitsu might be
smart enough to know it wasn't dynamically loaded.  If he really needs initial values, he
should use the Cobol INITIAL clause. 

Incidentally, CANCEL is not guaranteed to unload the program your way, either. A
dynamically loaded library can only be unloaded when its user count is zero. If another
developer happens to be using the same called program, CANCEL will fail, and Cobol has no
way of checking for that. If you want to be hackerish, issue the CANCEL 100 times. Each
call to dlopen() subtracts 1 from the user count. Then listen for cursing from the next
cubicle. :)  The reason Windows installers want you to reboot is because they don't have a
reliable way of deleting old dlls they just replaced. The solution is to call FreeLibrary
until it disappears from memory.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 6)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-31T20:41:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com>`

```
On Feb 1, 4:23 pm, Robert <n...@e.mail> wrote:
> On Thu, 31 Jan 2008 11:47:51 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Jan 31, 7:23 pm, Robert <n...@e.mail> wrote:
…[31 more quoted lines elided]…
> [the usual insults snipped]

As usual you think that pointing out where you are wrong and
correcting you is an 'insult'.

> >With Fujitsu Cobol the DLOAD directive tells the system that CALLs
> >might be dynamic. In these cases there is no need for the library
…[6 more quoted lines elided]…
> files will be loaded (if not already in memory) when the executable starts.

I have no idea what "mainframers and others from the Old School" may
understand, but if the library is loaded when the application starts
then it is not 'dynamic' as was required by Charles.


> If any cannot
> be found, the program will not start, which guarantees the program will not abort mid-run
> because a called program is missing.

The CALL can check whether it has failed to find the program with an
ON EXCEPTION, or it can be checked for in other ways, there is no need
for the program to abort.

If there is a requirement to ensure that the libraries do exist at
start of run, then yes, you can statically link them, or do an initial
CALL, but that was _NOT_ the stated requirement, you were, as usual,
answering the wrong question.

The requirement is to have dynamic loading.

> It also allows useful diagnostics to be run before
> starting a long batch job.

Unfortuanatly, as you completely failed to notice, it also makes the
program not work correctly and thus _REQUIRING_ disgnostics.

As Charles discovered, when you link in a shared library it prevents
the CANCEL working. I tested this by taking the working set of
Charles's programs and adding a -l to the ld.  The test then showed
the CANCEL did not work. Removing the -l and retesting showed the CALL
and CANCEL to work correctly.

Your advice was BAD, the results of following your advice was WRONG.

When will you accept that you completely fail to understand dynamic
loading ?


> A Windows dll works almost exactly the same as a Unix library (.so).
>
> Cobol can, and I believe should, use the normal Unix binding mechanism. There are several
> advantages and no good reason not to.

There are some _VERY_GOOD_ reasons why dynamic loading is used. The
fact that you don't understand them does not mean they are not
entirely valid.


> In addition to the advantages given above,

Which are irrelevant.

> one
> specific to Cobol is non-proliferation of program files, which I'll explain below.

Which is also completely irrelevant.


> Dynamic binding is the alternative. A running program can ask the OS to load an additional
> library by specifying its FILE NAME. Technically, this is done with a call to dlopen() (or
…[5 more quoted lines elided]…
> function).

Yeah, yeah, _WE_ know all that.


> The problem with dynamic binding in Cobol is that Cobol has no concept of library FILE
> NAME, it only knows about entry point names, which are essentially the same as program
> names. Thus, Charles' application with "hundreds of COBOL programs", if packaged for
> dynamic call, will have HUNDREDS OF LIBRARY FILES, each named libPROGRAM.so.

I am not sure why you think that is a 'problem'.

It is not a problem to me at all, nor to any of my clients.

> I find that ugly and, from a deployment point of view, clunky and amateurish.

You finding something as 'ugly' is probably a good reason to use it.


> It would be cleaner to
> package his hundreds of programs into one or a few libraries that are linked to the main
> executable.

Only if you fail to understand why dynamic loading is used and the
advantages it bestows on the system.


> How many third-party apps have you seen that came with hundreds of libraries or dlls?

Several, many even.

> >At run time a dynamic call will look for a file called libNAME.so
> >along the LD_LIBRARY_PATH, where NAME is that in the CALL, and it will
…[3 more quoted lines elided]…
> libNAME.so.

> >As you should be able to tell from the results in charles' 2nd message
> >your BAD and WRONG advice has meant that his program does not work as
…[5 more quoted lines elided]…
> with -l, it will be unloaded .. and reloaded the next time he calls it.

Charles results and my testing show that you are WONG once again.

Instead of simply assumnming that what you 'know' is everything that
is possible to know you should actually try testing stuff out.


> If it is packaged in a library with a hundred other programs, the whole library might be
> unloaded, because the handle for NAME is the handle for libMYSUBS.so. Or Fujitsu might be
> smart enough to know it wasn't dynamically loaded.  If he really needs initial values, he
> should use the Cobol INITIAL clause.

A CANCEL is not just for regaining initial values, it also frees the
memory. But not only that it caters for a fresh copy to be loaded.
Actual dynamic is dynamic. I can put a new version of a program into
the directory, get the main program to CANCEL and CALL and the new
code will be running.


> Incidentally, CANCEL is not guaranteed to unload the program your way, either. A
> dynamically loaded library can only be unloaded when its user count is zero. If another
> developer happens to be using the same called program, CANCEL will fail, and Cobol has no
> way of checking for that.

Geez, Robert, don't you _EVER_ test anything before spouting out what
will or will not happen ?

I just ran a test here to confirm what _I_ expected to happen based on
a few decades of using actual dynamic loading in Cobol.

What you completely failed to notice is that the _data_area_ is not
part of the library, but is created in the main program run-unit. When
the CANCEL is done the data areas created in the run-unit are dumped,
a subsequent CALL will recreate a new set of data areas regardless of
whether the code area still exists in a loaded library or a new
library has to be loaded.

In fact I just ran another test.  I started one program until it
CALLed the subroutine. I then on another console changed the source to
add a display, recompiled and ran a 2nd copy. It loaded a new version
even though the first was still in the middle of the subroutine.
Running through the CANCEL and CALL on that loaded the new routine
exactly as _I_ expected.

Your grasp of this is tenuous at best. Probably this is because you've
never done it the right way.

Instead of prattling on with more and more misinformation based on
guesswork just try doing this and see what _actually_ happens.


> If you want to be hackerish, issue the CANCEL 100 times. Each
> call to dlopen() subtracts 1 from the user count.

Geez, Robert, when you are WRONG you do it in spades. The main program
can only reduce the user count if it is _still_connected_ to the
library. The first CANCEL causes a disconnect and the rest do nothing
at all.

> Then listen for cursing from the next
> cubicle. :)  The reason Windows installers want you to reboot is because they don't have a
> reliable way of deleting old dlls they just replaced. The solution is to call FreeLibrary
> until it disappears from memory.

With Windows (which is a completely different issue and unrelated to
this topic) there are _two_ problems. The first is that a file cannot
be deleted or overwritten when it is open (Unix with its inode
structure can unlink a file that is open and it will disappear when it
is closed). Thus if a dll is in use, and it remains open, the
replacement must be deferred until it can be guaranteed that it is not
open, such as during a boot.

The second problem is that a dll in memory will be used in preference
to loading from disk. The FreeLibrary may make it disappear from
memory, but that is irrelevant to this topic.

This discussion is going along exactly as every one with you has:

Robert gives WRONG and/or BAD advise.
I point out it is wrong and show results of testing.
Robert reiterates his BAD and WRONG advice and claims he is right.
I point out where it is wrong and why.
Robert claims I am insulting him and (obviously having researched)
write screeds of irrelevant and obvious material that is mostly
unrelated.
I point out where it is irrelevant and wrong and show results of
testing.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 7)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-01T00:49:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com>`

```
On Thu, 31 Jan 2008 20:41:29 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 1, 4:23 pm, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jan 2008 11:47:51 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[35 more quoted lines elided]…
>correcting you is an 'insult'.

No, I think name calling is insulting.

>> >With Fujitsu Cobol the DLOAD directive tells the system that CALLs
>> >might be dynamic. In these cases there is no need for the library
…[10 more quoted lines elided]…
>then it is not 'dynamic' as was required by Charles.

You are confusing people with the term 'static linking'. Fujitsu's terminology is pretty
good:

static linking                           Old School, everything in one executable
dynamic program structure   Unix style libraries linked with -l
dynamic link structure           Cobol style Load On Demand

>> If any cannot
>> be found, the program will not start, which guarantees the program will not abort mid-run
…[4 more quoted lines elided]…
>for the program to abort.

True. How many programs have a graceful fallback? Ok, if called from a menu, they say
'Function not available'. Makes you wonder why they didn't grey it out.

>If there is a requirement to ensure that the libraries do exist at
>start of run, then yes, you can statically link them, or do an initial
…[3 more quoted lines elided]…
>The requirement is to have dynamic loading.

Why is Cobol the only language with a pressing need for dynamic linking? Huge bodies of
code written in C and other languages get by without it.

>As Charles discovered, when you link in a shared library it prevents
>the CANCEL working. I tested this by taking the working set of
>Charles's programs and adding a -l to the ld.  The test then showed
>the CANCEL did not work. Removing the -l and retesting showed the CALL
>and CANCEL to work correctly.

The NETCobol for Linux User's Guide says the same in Chapter 7.

>> Cobol can, and I believe should, use the normal Unix binding mechanism. There are several
>> advantages and no good reason not to.
…[3 more quoted lines elided]…
>entirely valid.

CANCEL was created in the days of limited memory, same as overlays. Cobol dropped overlays
when they were no longer needed. It should have dropped CANCEL at the same time.

>> The problem with dynamic binding in Cobol is that Cobol has no concept of library FILE
>> NAME, it only knows about entry point names, which are essentially the same as program
…[5 more quoted lines elided]…
>It is not a problem to me at all, nor to any of my clients.

It complicates deployment, makes the system less reliable and slows execution.

>> It would be cleaner to
>> package his hundreds of programs into one or a few libraries that are linked to the main
…[3 more quoted lines elided]…
>advantages it bestows on the system.

The advantage disappeared when we broke the 640K barrier.

>> >As you should be able to tell from the results in charles' 2nd message
>> >your BAD and WRONG advice has meant that his program does not work as
…[7 more quoted lines elided]…
>Charles results and my testing show that you are WONG once again.

I said IF Cobol issues a dlclose().  Fujitsu does not. It could.

>Instead of simply assumnming that what you 'know' is everything that
>is possible to know you should actually try testing stuff out.

Fair enough. If this gets any deeper, I'll install Fujitsu for Linux.

>> If it is packaged in a library with a hundred other programs, the whole library might be
>> unloaded, because the handle for NAME is the handle for libMYSUBS.so. Or Fujitsu might be
…[7 more quoted lines elided]…
>code will be running.

I reload with four keystrokes: esc, ctrl-P, Enter.

>> Incidentally, CANCEL is not guaranteed to unload the program your way, either. A
>> dynamically loaded library can only be unloaded when its user count is zero. If another
…[14 more quoted lines elided]…
>library has to be loaded.

That's not under the control of Unix. If Fujitsu does that, why doesn't it free the data
area of a dynamic program structure the same way?

>In fact I just ran another test.  I started one program until it
>CALLed the subroutine. I then on another console changed the source to
…[3 more quoted lines elided]…
>exactly as _I_ expected.

That's not normal Unix behavior. I'd need hands-on to figure out why it loaded a second
copy.

>Your grasp of this is tenuous at best. Probably this is because you've
>never done it the right way.

My grasp is based on writing large make files and knowledge of Unix internals.

>> If you want to be hackerish, issue the CANCEL 100 times. Each
>> call to dlopen() subtracts 1 from the user count.
…[4 more quoted lines elided]…
>at all.

Unix doesn't know who is connected to a shared library. All it knows is the user count.
Perhaps Fujitsu ignores CANCEL on a program that doesn't have a data segment.

>The second problem is that a dll in memory will be used in preference
>to loading from disk. The FreeLibrary may make it disappear from
>memory, but that is irrelevant to this topic.

Not if the dll is 'bound'.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 8)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-01T12:58:23-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com>`

```
On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:
> On Thu, 31 Jan 2008 20:41:29 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 1, 4:23 pm, Robert <n...@e.mail> wrote:
…[54 more quoted lines elided]…
> You are confusing people with the term 'static linking'.

You may be confused, even though you used the term yourself, but what
evidence do you have that anuone else is ?

> Fujitsu's terminology is pretty
> good:

> static linking                           Old School, everything in one executable

Not 'Old School' at all. Old School would be trying to fit everything
in 640Kb, or even 64Kb of CP/M.

> dynamic program structure   Unix style libraries linked with -l

And the objects are loaded (statically) at start up time, though the
CALLs are not necessarily linked to the routines.

> dynamic link structure           Cobol style Load On Demand

Exactly, they are _loaded_ dynamically. The requirement was stated as
being the last: "dynamic linkage" which does dynamic loading. You
should have noticed that the DLOAD directive was used and thus the -l
was inappropriate (see table in manual).


> >> If any cannot
> >> be found, the program will not start, which guarantees the program will not abort mid-run
…[7 more quoted lines elided]…
> 'Function not available'.

It would seem to me that Charles' programs may well form an
interactive menu driven application. Gracefull fallback is what these
systems should do.

> Makes you wonder why they didn't grey it out.

Perhaps because that would require searching the disk every time the
menu is  displayed.

> >If there is a requirement to ensure that the libraries do exist at
> >start of run, then yes, you can statically link them, or do an initial
…[6 more quoted lines elided]…
> code written in C and other languages get by without it.

Why do you think that "Cobol is the only language" ? I use several
that also do dynamic loading. I have even done dynamic loading in C.
You seem rather limited.


> >As Charles discovered, when you link in a shared library it prevents
> >the CANCEL working. I tested this by taking the working set of
…[4 more quoted lines elided]…
> The NETCobol for Linux User's Guide says the same in Chapter 7.

I am pleased to see that you are doing some research even if it is
rather belated.


> >> Cobol can, and I believe should, use the normal Unix binding mechanism. There are several
> >> advantages and no good reason not to.
…[6 more quoted lines elided]…
> when they were no longer needed. It should have dropped CANCEL at the same time.

Many would disagree with you.

> >> The problem with dynamic binding in Cobol is that Cobol has no concept of library FILE
> >> NAME, it only knows about entry point names, which are essentially the same as program
…[7 more quoted lines elided]…
> It complicates deployment, makes the system less reliable and slows execution.

What _evidence_, other than 'researching your keyboard', can you
provide for these unsupported assertions. Certainly a dynamic load
takes a few milliseconds when a menu item is selected, but in what way
would it be 'less reliable' ?

Actually, to those that use this, it _simplifies_ deployment,
especially in bespoke systems where I operate. If a single program
requires changes then only that file is tested and redistributed. In
any rational development all deployments would be fully tested. If you
link several programs into one library the all those in the library
need to be retested. If they are all linked to one executable then
everything needs to be retested.

And the CALL dataname feature is invaluable as it means that the menu
program can use a data file to define what is available in a
particular application, or even to the particular user, and this can
be extended by changing the data file (and issuing the programs)
without changing the menu program at all.

'One off' or special programs can be deployed individually and
executed with the application framework by typing their name into the
menu program (given that the user has adequate permissions), there is
no need to redeploy the whole system.

> >> It would be cleaner to
> >> package his hundreds of programs into one or a few libraries that are linked to the main
…[5 more quoted lines elided]…
> The advantage disappeared when we broke the 640K barrier.

Showing once again that you fail to understand why dynamic loading is
used and the
advantages it bestows on the system.


> >> >As you should be able to tell from the results in charles' 2nd message
> >> >your BAD and WRONG advice has meant that his program does not work as
…[9 more quoted lines elided]…
> I said IF Cobol issues a dlclose().  Fujitsu does not. It could.

So, you would agree that your 'Wrong' was Wrong then. Charles and I
both described the results of testing. You said this was 'wrong' on
the basis that it _could_ have been different if Fujitsu did it
differently, but they don't.

You would have to agree that are testing results are 'RIGHT' then.


> >Instead of simply assumnming that what you 'know' is everything that
> >is possible to know you should actually try testing stuff out.
>
> Fair enough. If this gets any deeper, I'll install Fujitsu for Linux.

Wow, forcing you into a situation where you actually test something.
You must have gone past repeating the misinformation more than 3 times
then.


> >> If it is packaged in a library with a hundred other programs, the whole library might be
> >> unloaded, because the handle for NAME is the handle for libMYSUBS.so. Or Fujitsu might be
…[9 more quoted lines elided]…
> I reload with four keystrokes: esc, ctrl-P, Enter.

But that (presumably) reloads the whole application. How inefficient.


> >> Incidentally, CANCEL is not guaranteed to unload the program your way, either. A
> >> dynamically loaded library can only be unloaded when its user count is zero. If another
…[17 more quoted lines elided]…
> area of a dynamic program structure the same way?

Ask them.

> >In fact I just ran another test.  I started one program until it
> >CALLed the subroutine. I then on another console changed the source to
…[6 more quoted lines elided]…
> copy.

Exactly.  Your guesses were just misinformation.

> >Your grasp of this is tenuous at best. Probably this is because you've
> >never done it the right way.
>
> My grasp is based on writing large make files and knowledge of Unix internals.

Which didn't address the area under discussion at all it seems.


> >> If you want to be hackerish, issue the CANCEL 100 times. Each
> >> call to dlopen() subtracts 1 from the user count.
…[6 more quoted lines elided]…
> Unix doesn't know who is connected to a shared library. All it knows is the user count.

What you also failed to notice that you got WRONG with your assertion
is that it isn't "dlopen(name)" that "subtracts 1", that would add 1.
It is dlclose(handle) that would subtract and the handle would be
destroyed by the dlclose() (ie it would be disconnected) and a
subsequent dlclose() would be with an invalid handle.

As I say, you get some things wrong in spades.


> Perhaps Fujitsu ignores CANCEL on a program that doesn't have a data segment.
>
…[4 more quoted lines elided]…
> Not if the dll is 'bound'.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-02T20:31:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com>`

```
On Fri, 1 Feb 2008 12:58:23 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jan 2008 20:41:29 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:

>> Fujitsu's terminology is pretty
>> good:
…[4 more quoted lines elided]…
>in 640Kb, or even 64Kb of CP/M.

That's why CANCEL was created. 

>> dynamic program structure   Unix style libraries linked with -l
>
>And the objects are loaded (statically) at start up time, though the
>CALLs are not necessarily linked to the routines.

Loading at start up time is faster and safer. You can specify -z lazyload to make it load
libraries when first called. 

>> dynamic link structure           Cobol style Load On Demand
>
…[3 more quoted lines elided]…
>was inappropriate (see table in manual).

Fujitsu works with DLOAD and dynamic program structure, because dlopen() finds programs
already resident. If the program is NOT resident then it loads from disk. The only
downside is Fujitsu will not CANCEL programs bound at start up time.

>> >> If any cannot
>> >> be found, the program will not start, which guarantees the program will not abort mid-run
…[16 more quoted lines elided]…
>menu is  displayed.

In Micro Focus, one can say SET procedure-pointer TO ENTRY 'MYPROG1'. 
If the pointer is null, the program doesn't exist. 
Cobol doesn't allow definition of weak externs, so you can either tell  ld -z nodefs to
allow undefined symbols, or put MYPROG1 in a variable. 

Fujitsu has no equivalent feature. You'd have to call all programs at initialization time
and remember which are invalid.

>> >> The problem with dynamic binding in Cobol is that Cobol has no concept of library FILE
>> >> NAME, it only knows about entry point names, which are essentially the same as program
…[12 more quoted lines elided]…
>would it be 'less reliable' ?

There are more files that can be deleted or overwritten.

>Actually, to those that use this, it _simplifies_ deployment,
>especially in bespoke systems where I operate. If a single program
…[4 more quoted lines elided]…
>everything needs to be retested.

There is no reason to re-test an unchanged program just because it is in the same library
with other programs. You could use the same argument to require re-testing every
application on the machine. 

Changes in one program can't cause errors in other programs unless they share global data.
In a rational environment, data is shared between parent and child, not between siblings
and certainly not with stranger programs. You should never make a decision in program A,
store it in an indicator or database, and take action on that decision in program B.
That's bad design. 

If you DO make that mistake, putting programs A and B in separate files is no more
protection than putting them in the same library. Even running them on separate machines,
as remote procedures, is no protection.

>And the CALL dataname feature is invaluable as it means that the menu
>program can use a data file to define what is available in a
>particular application, or even to the particular user, and this can
>be extended by changing the data file (and issuing the programs)
>without changing the menu program at all.

Now you're advocating home-grown security. I've seen hundreds of home-grown security
systems and not one of them was secure. Most can be defeated by editing a cleartext
database or text file.

In any case, this is irrelevant to program load mechanism. The same bad security will work
with dynamic program structure. 

>'One off' or special programs can be deployed individually and
>executed with the application framework by typing their name into the
>menu program (given that the user has adequate permissions), there is
>no need to redeploy the whole system.

Create a few dummy 'stub' programs for this purpose. Or use versioning, so ONEOFF 1.1 does
one repair and ONEOFF 1.2 does another. See documentation for dlvsym().

>> >> >As you should be able to tell from the results in charles' 2nd message
>> >> >your BAD and WRONG advice has meant that his program does not work as
…[14 more quoted lines elided]…
>differently, but they don't.

I'll give you that win. A hardcore programmer would do it by calling dlclose() and
dlopen() directly from Cobol. :)
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 10)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-02T21:33:22-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com>`

```
On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
> On Fri, 1 Feb 2008 12:58:23 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:
…[16 more quoted lines elided]…
> Loading at start up time is faster and safer.

That is your opinion. It doesn't agree with mine at all, and I have
been using dynamic load when required for some some decades.

> You can specify -z lazyload to make it load
> libraries when first called.

It may be that for a batch run checking that all required modules are
available at start-up would be useful. However, for an interactive
system with several applications and many modules it would be _slower_
on start up to load all modules simply because many will not be run on
any particular day.

As for 'safer', you have that completely wrong, too. If a particular
module is missing then it would prevent anyone doing anything if the
startup failed because of that, but it may be a module that is not
actually required that day.

As I never have had an issue where any system was 'unsafe' because I
had separate dynamic loaded programs then I can't see how you can
claim 'safer' than that.

> >> dynamic link structure           Cobol style Load On Demand
>
…[8 more quoted lines elided]…
>

No. The downside is that the user has to completely close the
application, update the libraries, and then restart the application if
a new program, or an updated one, or a one-off, is required.

If it is Windows then the library cannot be replaced until all users
have closed the application because you cannot overwrite an open file.

With dynamic loading, and a suitable framework in place (which I had
developed many years ago), it is only necessary to drop the new
program in and select it.


> >> >> If any cannot
> >> >> be found, the program will not start, which guarantees the program will not abort mid-run
…[21 more quoted lines elided]…
> allow undefined symbols, or put MYPROG1 in a variable.

Actually in MF Cobol since Level II there is a special CALL x"91"
function 15 that will tell you if the program exists.

> Fujitsu has no equivalent feature. You'd have to call all programs at initialization time
> and remember which are invalid.

No, I don't have to do that, I have the menu program tell the user if
a program is unavailable when they actually try to run it.


> >> >> The problem with dynamic binding in Cobol is that Cobol has no concept of library FILE
> >> >> NAME, it only knows about entry point names, which are essentially the same as program
…[14 more quoted lines elided]…
> There are more files that can be deleted or overwritten.

As I have never had a program file "overwritten or deleted" then no
other mechanism can be 'more reliable'.  If you do have a library file
deleted then with your mechanism _no_one_ can do anything with the
system because it fails to load up at all (according to what you have
said).

With my system if a file is deleted or overwritten then unless it is
one of a small number of essential core modules the applications will
run, but possibly one or more modules could become unavailable. Of
course it is possible that module is not required at that time anyway.

How do _you_ measure reliability ?  Let us say one file has been
deleted:

a) NOTHING WORKS AT ALL until the programmer fixes the problem.

b) Applications function as normal except one module is unavailable
(which may not be required)

I would say the b) would rate as 'more reliable'.


> >Actually, to those that use this, it _simplifies_ deployment,
> >especially in bespoke systems where I operate. If a single program
…[7 more quoted lines elided]…
> with other programs.

Yes, there is. Any program that is re-issued must pass testing. It may
be that other programs in that library have been modified (by someone
else) but are not completed and ready for distribution.

If you lump a dozen programs into a library then you need to re-test
and re-issue those dozen.

In fact that is a point against using a library if you are not
retesting because there is a risk that may affect the system's
reliability.

> You could use the same argument to require re-testing every
> application on the machine.

Why ? Are you re-issuing new versions of every application ?


> Changes in one program can't cause errors in other programs unless they share global data.

You are changing one program and then collecting a dozen, or several
dozen into one library file and re-issuing it. How do you ensure that
the other dozens have not been changed but are not ready for issuing
yet ?

> In a rational environment, data is shared between parent and child, not between siblings
> and certainly not with stranger programs. You should never make a decision in program A,
> store it in an indicator or database, and take action on that decision in program B.
> That's bad design.

Why are you talking irrelevancies here ? You are just making up straw
men.

> If you DO make that mistake, putting programs A and B in separate files is no more
> protection than putting them in the same library. Even running them on separate machines,
…[10 more quoted lines elided]…
> database or text file.

'Home-grown' or application security does not prevent other security
systems being used. In fact having each program separately in its own
file can be used to give greater granularity to the security.

In any case, in my systems, users don't have access to the application
security files except by running the application control system and
that is protected. And, no, they can't just edit a text file.

So you are inventing straw man arguments yet again.

If I want some programs, such as month end, to be entirely secure I
can make put them in a special group and only have specific users in
that group. Make them readable by that group only and no one else can
run them even if they break the application security.

With your mechanism:

1) You would have to make the whole library special group only (OK so
you could reorganize and re-issue).

2) the application would fail to start for everyone else because the
library was unavailable.

But thank you for pointing out yet another advantage of how I do the
systems.


> In any case, this is irrelevant to program load mechanism. The same bad security will work
> with dynamic program structure.

Where did the 'bad security' come from ? Oh, I know, you made that up.


> >'One off' or special programs can be deployed individually and
> >executed with the application framework by typing their name into the
…[4 more quoted lines elided]…
> one repair and ONEOFF 1.2 does another. See documentation for dlvsym().

I am quite happy with the way the system works, why are you attempting
to impose your unrequired ideas on my systems when there is no problem
at all ?


> >> >> >As you should be able to tell from the results in charles' 2nd message
> >> >> >your BAD and WRONG advice has meant that his program does not work as
…[17 more quoted lines elided]…
> dlopen() directly from Cobol. :)

So the score remains at about 10 to nothing then ?
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-04T00:35:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com>`
- **References:** `<rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com>`

```
On Sat, 2 Feb 2008 21:33:22 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
>> On Fri, 1 Feb 2008 12:58:23 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:

>> Loading at start up time is faster and safer.
>
…[19 more quoted lines elided]…
>claim 'safer' than that.

It happens to me often, because I frequently change environments. If the right .profile or
.login doesn't get sourced in, the library path will be blank or incorrect. I find it
helpful to know in advance that a program or batch job will not run, instead of having it
abort in the middle. 

Others reached the same conclusion, which is why dynamic program structure is THE NORM in
the Unix and Windows worlds. 

>> >> dynamic link structure           Cobol style Load On Demand
>>
…[12 more quoted lines elided]…
>a new program, or an updated one, or a one-off, is required.

An application can do that with versioning. If it calls foo.1.3 and foo.1.2 is already in
memory, the loader will not use 1.2, it will load 1.3.

The benefit is that you won't accidentally get a library installed by another application.
This a common problem on Windows, known as 'DLL hell'. The disadvantage is inability to
upgrade a library without upgrading the calling program. 

Version binding is normally done by the linker; it is normally not coded into the calling
program, thus you don't have to recompile the caller to change its binding, but you do
have to reload it. However, versioning can be controlled by the program by using the
dlvsym() function. 

>If it is Windows then the library cannot be replaced until all users
>have closed the application because you cannot overwrite an open file.

Dynamically loaded dlls have the same problem. All users have to CANCEL before the dll can
be replaced. 

The Unix solution is to put the version number into the file name. The library name with
no version is a symbolic link to the current library file. You can change symbolic links
at any time because the file system doesn't track whether they are in use.

>With dynamic loading, and a suitable framework in place (which I had
>developed many years ago), it is only necessary to drop the new
>program in and select it.

Sounds like a golden opportunity for hackers. 
mv login.so login.bkp
cp mylogin.so login.so
echo Ready for unauthenticated login.
....
mv login.bkp login.so

>> >Actually, to those that use this, it _simplifies_ deployment,
>> >especially in bespoke systems where I operate. If a single program
…[11 more quoted lines elided]…
>else) but are not completed and ready for distribution.

>> Changes in one program can't cause errors in other programs unless they share global data.
>
…[3 more quoted lines elided]…
>yet ?

That's what version control is for. Untested programs don't get moved to the trunk
(production). 

>> >And the CALL dataname feature is invaluable as it means that the menu
>> >program can use a data file to define what is available in a
…[29 more quoted lines elided]…
>library was unavailable.

My mechanism is oriented around data, not programs. If I want to protect month-end figures
in the accounting system, for example, I protect those numbers in the database.
Unauthorized users cannot change them by running the monthend program, by writing their
own program nor by running a database utility. Your notion of security by controlling
access to programs was obsolete twenty years ago.

If I DID want to limit access to a program function, the security check would be in the
function, not the file it is packaged in nor the calling program. Relying on Unix file
system to do application security is weak. For example, if the setgroupid bit of a program
file is set, it executes under the owner's group id rather than the user's.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 12)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-04T00:04:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com>`
- **References:** `<rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com>`

```
On Feb 4, 7:35 pm, Robert <n...@e.mail> wrote:
> On Sat, 2 Feb 2008 21:33:22 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
…[27 more quoted lines elided]…
> abort in the middle.

Why can't you ensure that the environment is set correctly before it
runs. In any case if the run won't find anything because the paths are
set wrongly (which doesn't happen to me) then my core routines won't
be found either and the program won't start either.

But your point was about files being deleted or corrupted. Now you try
to change to having stuff mixed up.

> Others reached the same conclusion, which is why dynamic program structure is THE NORM in
> the Unix and Windows worlds.

I am not sure why you are attempting to change the way that I (and, it
seems, Charles) have been working for years. The way I do things
things works 100% safe and reliable. You cannot claim anything better
than that, _plus_ I get flexability thay your mechanism doesn't give.

I was was doing batch jobs then maybe I would do that, or even
static.  But I don't so what batch jobs do is of no interest.


> >> >> dynamic link structure           Cobol style Load On Demand
>
…[14 more quoted lines elided]…
> memory, the loader will not use 1.2, it will load 1.3.

<shrug> I don't need multiple concurrent versions. The way I do it
works 100%.


> The benefit is that you won't accidentally get a library installed by another application.

I never will because all my files are held in a structure of
directories that will never be used by anything else.

Why do you keep coming up with entirely spurious arguments and straw-
men ?

> This a common problem on Windows, known as 'DLL hell'. The disadvantage is inability to
> upgrade a library without upgrading the calling program.

Your point being ?

Again you create a spurious argument and a straw-man.

> Version binding is normally done by the linker; it is normally not coded into the calling
> program, thus you don't have to recompile the caller to change its binding, but you do
> have to reload it. However, versioning can be controlled by the program by using the
> dlvsym() function.

Why do you think that relevant ?  I haven't recompiled 'the calling
program' for years.


> >If it is Windows then the library cannot be replaced until all users
> >have closed the application because you cannot overwrite an open file.
>
> Dynamically loaded dlls have the same problem. All users have to CANCEL before the dll can
> be replaced.

You weren't paying attention. I did an _actual_test_ and all users
_did_not_ have to CANCEL before replacement (but then this isn't
Windows).


> The Unix solution is to put the version number into the file name. The library name with
> no version is a symbolic link to the current library file. You can change symbolic links
…[11 more quoted lines elided]…
> mv login.bkp login.so

What makes you think that users have write access to the program
directory ? _I_ can drop in another program.

Just another straw-man.

> >> >Actually, to those that use this, it _simplifies_ deployment,
> >> >especially in bespoke systems where I operate. If a single program
…[61 more quoted lines elided]…
> access to programs was obsolete twenty years ago.

Just change the subject then. You were trying to say that using
libraries was 'more secure'. You tried to say that 'home-grown' was
not secure.

Now you just change the subject to something different because you
failed to establish your unsupported and flawed assertions.

In fact this change seems to be after I pointed out that your
mechanism _couldn't_ use the unix file system security because it
would stop your applications from starting.

There is nothing in using dynamic loading that prevents the
application from using any other security mechanism.

In fact my system does implement field level security within the
system, but I don't run Banks or Stock Exchanges. The level of
security that I use is exactly correct for the businesses that use my
applications.


> If I DID want to limit access to a program function, the security check would be in the
> function, not the file it is packaged in nor the calling program. Relying on Unix file
> system to do application security is weak. For example, if the setgroupid bit of a program
> file is set, it executes under the owner's group id rather than the user's.

Another straw-man. Why would I have setgroupid set ?

But as you _should_ have noticed I don't need to "Rely on Unix file
system". I have the 'home-grown' application security that you said
was useless, and now you say that Unix is useless and you would use
'home-grown'.

You really are struggling (and failing) to score any wins here at all.

The point is that with the high granularity I _can_ use Unix file
system security (and have it work) as well as the application
security.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-04T23:52:01-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com>`
- **References:** `<ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com>`

```
On Mon, 4 Feb 2008 00:04:01 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 4, 7:35 pm, Robert <n...@e.mail> wrote:
>> On Sat, 2 Feb 2008 21:33:22 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:

>> Others reached the same conclusion, which is why dynamic program structure is THE NORM in
>> the Unix and Windows worlds.
…[4 more quoted lines elided]…
>than that, _plus_ I get flexability thay your mechanism doesn't give.

I wasn't trying to change your way of doing things, I was answering Charles' question.

>I was was doing batch jobs then maybe I would do that, or even
>static.  But I don't so what batch jobs do is of no interest.

In my world, Cobol are nearly all in batch jobs. User interface is in Java or occasionally
PowerBuilder.

>> >> >> dynamic link structure           Cobol style Load On Demand
>>
…[26 more quoted lines elided]…
>men ?

YOU brought up replacable files as an advantage. 

>> Version binding is normally done by the linker; it is normally not coded into the calling
>> program, thus you don't have to recompile the caller to change its binding, but you do
…[4 more quoted lines elided]…
>program' for years.

If you're feeding it the program name via database, you could just as easily give it the
version string. That wouldn't require a recompilation either.

>> Sounds like a golden opportunity for hackers.
>> mv login.so login.bkp
…[6 more quoted lines elided]…
>directory ? _I_ can drop in another program.

If they have read access, they can copy your whole directory structure to their home
directory, change permissions all they want, and run their local copy to find out the
boss' salary.

How do you know they can't do that? Is computer illiteracy a job requirement? Are the
tested for lack of knowledge before hiring? 

Security that depends on user ignorance is so 1980s.

>> My mechanism is oriented around data, not programs. If I want to protect month-end figures
>> in the accounting system, for example, I protect those numbers in the database.
…[9 more quoted lines elided]…
>failed to establish your unsupported and flawed assertions.

YOU introduced application security, not I.

>In fact my system does implement field level security within the
>system, but I don't run Banks or Stock Exchanges. The level of
>security that I use is exactly correct for the businesses that use my
>applications.

I worked with a system admin whose first job, after getting a degree in computer science,
was night manager at a Wal-Mart, where he ran the back-office computer. When the help desk
was talking him through a problem, they were giving him the root password on THEIR SERVER.
He knew exactly what that meant. He said, "What a gaping hole. I could have done
anything." He didn't; someone else might have. 

>> If I DID want to limit access to a program function, the security check would be in the
>> function, not the file it is packaged in nor the calling program. Relying on Unix file
…[3 more quoted lines elided]…
>Another straw-man. Why would I have setgroupid set ?

Because a user set it. If it's set on your main menu, every program in the system has the
menu owner's group permission. Unix holds it in Previous Group Perission.

>But as you _should_ have noticed I don't need to "Rely on Unix file
>system". I have the 'home-grown' application security that you said
>was useless, and now you say that Unix is useless and you would use
>'home-grown'.

I said not to use home-grown security. Imagine a shop with 100 applications, each having
its own quirky security. It would be impossible to administer.

>You really are struggling (and failing) to score any wins here at all.
>
>The point is that with the high granularity I _can_ use Unix file
>system security (and have it work) as well as the application
>security.
 
I wonder if that French bank said the same.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 14)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-05T11:29:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com>`
- **References:** `<ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com> <v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com>`

```
On Feb 5, 6:52 pm, Robert <n...@e.mail> wrote:
> On Mon, 4 Feb 2008 00:04:01 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 4, 7:35 pm, Robert <n...@e.mail> wrote:
…[9 more quoted lines elided]…
> I wasn't trying to change your way of doing things, I was answering Charles' question.

When I looked at Charles question _I_ saw that it contained the
requirement to get CALL/CANCEL working. _Nothing_ that you have
suggested has been to meet that requirement.


> >I was was doing batch jobs then maybe I would do that, or even
> >static.  But I don't so what batch jobs do is of no interest.
>
> In my world, Cobol are nearly all in batch jobs. User interface is in Java or occasionally
> PowerBuilder.

That may be why your suggestions don't match the requirements.


> >> >> >> dynamic link structure           Cobol style Load On Demand
>
…[27 more quoted lines elided]…
> YOU brought up replacable files as an advantage.

Your claim was: "The benefit is that you won't accidentally get a
library installed by another application.".

In what way does _your_ mechanism do this ? If you libraryize your
programs and version them what is it that prevents another application
choosing the same name and having the same version and 'accidentally
installing that over yours' ?

You make claims about what may happen and seem to completely fail to
notice that the same problem could occur to your system. You claim a
completely spurious 'benefit' for your mechanism without knowing what
my mechanism actually is.


> >> Version binding is normally done by the linker; it is normally not coded into the calling
> >> program, thus you don't have to recompile the caller to change its binding, but you do
…[7 more quoted lines elided]…
> version string. That wouldn't require a recompilation either.

And I could even more easil;y just continue to use what has worked
well for me for decades without your unwanted complexifications.


> >> Sounds like a golden opportunity for hackers.
> >> mv login.so login.bkp
…[3 more quoted lines elided]…
> >> mv login.bkp login.so

The users would _also_ need to have access to a compiler and to the
specifications of the framework, or the source code of that, to know
what 'mylogin' must do when a user logs in.

You may as well claim that "anyone can write their own Unix login and
get root access".

> >What makes you think that users have write access to the program
> >directory ? _I_ can drop in another program.
…[3 more quoted lines elided]…
> boss' salary.

Well, actually, no they couldn't.  I already told you that particular
programs can be set to be owned by the application administrator with
a group id of the trusted group and permissions of 640. It is only if
you are a member of the trusted group that give read access to run (or
copy) that program. Users can be members of several groups so access
can be very granular. Users not a member of that group will get a
'program not found' if they try to select it from the menu.

If the library was required at start up (as in your mechanism) then
the application would fail to do anything for users not in _all_ the
trusted groups. Also you gather several programs into one library so
you have less, or no, usable granularity.

I thought that you claimed to be some sort of Unix guru, yet you seem
to need to have these simple things explained to you.


> How do you know they can't do that? Is computer illiteracy a job requirement? Are the
> tested for lack of knowledge before hiring?
>
> Security that depends on user ignorance is so 1980s.

Your arguments always seem to degrade to the level of drawing
unwarranted conclusions from stuff that you just make up while you
completely ignore what you are told.


> >> My mechanism is oriented around data, not programs. If I want to protect month-end figures
> >> in the accounting system, for example, I protect those numbers in the database.
…[11 more quoted lines elided]…
> YOU introduced application security, not I.

No, that is wrong. I was saying that "the CALL dataname feature is
invaluable ..".

Then, out of the blue, you changed this to: "Now you're advocating
home-grown security."


> >In fact my system does implement field level security within the
> >system, but I don't run Banks or Stock Exchanges. The level of
…[7 more quoted lines elided]…
> anything." He didn't; someone else might have.

The relevance of this little anecdote is ?

> >> If I DID want to limit access to a program function, the security check would be in the
> >> function, not the file it is packaged in nor the calling program. Relying on Unix file
…[5 more quoted lines elided]…
> Because a user set it.

Excuse me, but how did a user get to set this ?

Building straw-men to sit on straw-men's shoulders doesn't win any
arguments here.

> If it's set on your main menu, every program in the system has the
> menu owner's group permission. Unix holds it in Previous Group Perission.

If I had some ham, I'd have ham and eggs, if I had some eggs.


> >But as you _should_ have noticed I don't need to "Rely on Unix file
> >system". I have the 'home-grown' application security that you said
…[12 more quoted lines elided]…
> I wonder if that French bank said the same.

Do you mean is they started with "I don't run Banks or Stock
Exchanges" ?
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-06T00:01:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com>`
- **References:** `<rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com> <v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com>`

```
On Tue, 5 Feb 2008 11:29:58 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 5, 6:52 pm, Robert <n...@e.mail> wrote:
>> On Mon, 4 Feb 2008 00:04:01 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[14 more quoted lines elided]…
>suggested has been to meet that requirement.

The problem was Called Program Not Found. I suggested telling ld where to find it.

>> >I was was doing batch jobs then maybe I would do that, or even
>> >static.  But I don't so what batch jobs do is of no interest.
…[4 more quoted lines elided]…
>That may be why your suggestions don't match the requirements.

Charles was unfamiliar with Fujitsu on Unix. I suggested the NORMAL Unix way of binding
programs .. for all languages, not just Cobol. 

>> >> >> >> dynamic link structure           Cobol style Load On Demand
>>
…[35 more quoted lines elided]…
>installing that over yours' ?

One library file is less likely to be overwritten than one of several hundred. 

If it IS overwritten, the program will not start, because entry points will not match.

>You make claims about what may happen and seem to completely fail to
>notice that the same problem could occur to your system. You claim a
>completely spurious 'benefit' for your mechanism without knowing what
>my mechanism actually is.

I  know how dynamic Cobol calls work.

>> >> Version binding is normally done by the linker; it is normally not coded into the calling
>> >> program, thus you don't have to recompile the caller to change its binding, but you do
…[10 more quoted lines elided]…
>well for me for decades without your unwanted complexifications.

We Have Always Done It That Way (WHADIT).

>> >> Sounds like a golden opportunity for hackers.
>> >> mv login.so login.bkp
…[7 more quoted lines elided]…
>what 'mylogin' must do when a user logs in.

It's probably returning user and group in a structure. Write a stub to call it and look at
the structure returned. 

>You may as well claim that "anyone can write their own Unix login and
>get root access".

No, but you'd be amazed at the percentage of systems where that's not necessary, because
they still have default logins. 

>> >What makes you think that users have write access to the program
>> >directory ? _I_ can drop in another program.
…[11 more quoted lines elided]…
>'program not found' if they try to select it from the menu.

I assumed the files had world read permission. You stopped that approach.

>If the library was required at start up (as in your mechanism) then
>the application would fail to do anything for users not in _all_ the
>trusted groups. Also you gather several programs into one library so
>you have less, or no, usable granularity.

Granularity is in the called programs. It doesn't matter how they are packaged.

>> >> My mechanism is oriented around data, not programs. If I want to protect month-end figures
>> >> in the accounting system, for example, I protect those numbers in the database.
…[17 more quoted lines elided]…
>home-grown security."

You said "invaluable as it means that the menu program can use a data file to define what
is available in a particular application, or even to the particular user." That's
application security, and is irrelevant to dynamic loading. You could do the same if all
programs were in one library. 

Security belongs in the called program, not the menu program. A user could write his own
program that calls the yours. Actually, security belongs on the protected data, but that's
another topic.

>> >In fact my system does implement field level security within the
>> >system, but I don't run Banks or Stock Exchanges. The level of
…[9 more quoted lines elided]…
>The relevance of this little anecdote is ?

The moral is: don't assume users are too dumb to hack your system.

>> >> If I DID want to limit access to a program function, the security check would be in the
>> >> function, not the file it is packaged in nor the calling program. Relying on Unix file
…[7 more quoted lines elided]…
>Excuse me, but how did a user get to set this ?

He would have to trick someone in the group to set it. Are priviliged users' .profiles
world writable? Is root's? How about shell logins?
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 16)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-06T00:19:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com>`
- **References:** `<rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com> <v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com> <ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com>`

```
On Feb 6, 7:01 pm, Robert <n...@e.mail> wrote:
> On Tue, 5 Feb 2008 11:29:58 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 5, 6:52 pm, Robert <n...@e.mail> wrote:

> >In what way does _your_ mechanism do this ? If you libraryize your
> >programs and version them what is it that prevents another application
…[3 more quoted lines elided]…
> One library file is less likely to be overwritten than one of several hundred.

Given that the likelyhood of any of mine being overwritten is zero,
then your assertion is meaningless. If there is (as you said there
was) a likelyhood of yours being overwritten then obviously your is
less reliable.


> If it IS overwritten, the program will not start, because entry points will not match.

Exactly, your users will think that your system is unreliable.

> >You make claims about what may happen and seem to completely fail to
> >notice that the same problem could occur to your system. You claim a
…[19 more quoted lines elided]…
> We Have Always Done It That Way (WHADIT).

We do it that way because it works well.


> >> >> Sounds like a golden opportunity for hackers.
> >> >> mv login.so login.bkp
…[10 more quoted lines elided]…
> the structure returned.

Well, no it doesn't do that. Not even close.  But you still haven't
explained how your mechanism is 'better'. Given equal slackness in
permissions and such and users can access compilers then how is  a
library any different ? Tools can push and pull stuff out of
libraries. Do you think that my program is called
'ThisisaSimpleMindedLogin.so' ?

You claimed that your way was superior and the best that you have come
up with is 'less ugly'.


> >You may as well claim that "anyone can write their own Unix login and
> >get root access".
>
> No, but you'd be amazed at the percentage of systems where that's not necessary, because
> they still have default logins.

Which is irrelevant to mine, whether it applies to yours I do not
know.

> >> >What makes you think that users have write access to the program
> >> >directory ? _I_ can drop in another program.
…[13 more quoted lines elided]…
> I assumed the files had world read permission. You stopped that approach.

So, you would concede then that I have described a mechanism that
would not be able to be used by your system the way that you have it
and that this mechanism does protect the programs.

Thank you for starting to notice that some of us know what we are
doing.


> >If the library was required at start up (as in your mechanism) then
> >the application would fail to do anything for users not in _all_ the
…[3 more quoted lines elided]…
> Granularity is in the called programs. It doesn't matter how they are packaged.

You did not follow that discussion then. If several programs are
packaged together in a library then the group permission restrictions
apply to all in the library.


> >> >> My mechanism is oriented around data, not programs. If I want to protect month-end figures
> >> >> in the accounting system, for example, I protect those numbers in the database.
…[21 more quoted lines elided]…
> application security,

No. Wrong. You may have thought that security was the only reason for
this, but in my framework systems the 'user' identifies sets of data
files as well as applications because the systems are multi-company as
well as multi-user.

One company may have bespoke programs that suit a particular need and
the users in that company may have additional programs that are not
available to the same application run for another company.

> and is irrelevant to dynamic loading. You could do the same if all
> programs were in one library.

Well certainly your library could be used but would provide _no_
advantage and would not provide the advantages that I have already
given.  For example if every program were in one library then that
would include the bespoke programs and a reissue of those would
require _EVERY_PROGRAM_ to be retested everytime to meet adequate
standards of reliability.

> Security belongs in the called program, not the menu program. A user could write his own
> program that calls the yours.

Which is not an advantage for your library because he could call that
too.

> Actually, security belongs on the protected data, but that's
> another topic.

Which is not an advantage for a library because it makes no
difference.

So you started by making claims for your library being better and we
find that, at best, it is merely equal and fails to meet the
requirements that I use.


> >> >In fact my system does implement field level security within the
> >> >system, but I don't run Banks or Stock Exchanges. The level of
…[11 more quoted lines elided]…
> The moral is: don't assume users are too dumb to hack your system.

It seems that you allow them to break your by merely overwriting one
file.


> >> >> If I DID want to limit access to a program function, the security check would be in the
> >> >> function, not the file it is packaged in nor the calling program. Relying on Unix file
…[10 more quoted lines elided]…
> world writable? Is root's? How about shell logins?

And this is different from your library system in what way ?

Instead of addressing your claimed superiority you merely ramble on
about something else entirely unrelated, and straw-men, in the hope
that it may bamboozle. Perhaps that is your normal 'arguing' skills,
you win if they give up so it doesn't matter what the content is.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 17)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-06T21:06:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com>`
- **References:** `<p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com> <v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com> <ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com>`

```
On Wed, 6 Feb 2008 00:19:14 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 6, 7:01 pm, Robert <n...@e.mail> wrote:

>Well, no it doesn't do that. Not even close.  But you still haven't
>explained how your mechanism is 'better'. Given equal slackness in
>permissions and such and users can access compilers then how is  a
>library any different ? Tools can push and pull stuff out of
>libraries.

My security is better because it does not depend on file system permissions. It doesn't
depend on application code, either. 

The goal of security is to prevent unauthorized people from seeing or changing certain
data. I do that by protecting the DATA; you do it by preventing them from running
programs. 

As an analogy, suppose we are parents who want to prevent our kids from watching sex
movies on TV. You would do it by locking up the remote control, which is easily bypassed
with a universal remote. I would do it by telling the cable box to play the movies only
for designated users. 

>You claimed that your way was superior and the best that you have come
>up with is 'less ugly'.

Simpler deployment, can be checked by auditing tools, faster loading, more reliable
because mid-run aborts due to missing program are impossible.

>> >> >What makes you think that users have write access to the program
>> >> >directory ? _I_ can drop in another program.
…[17 more quoted lines elided]…
>and that this mechanism does protect the programs.

My system? I'd like to take credit for inventing Unix and ELF, but I believe Thompson and
Ritchie did it first. 

>Thank you for starting to notice that some of us know what we are
>doing.

Yes, we do.

>> >If the library was required at start up (as in your mechanism) then
>> >the application would fail to do anything for users not in _all_ the
…[7 more quoted lines elided]…
>apply to all in the library.

Oh no, not file permissions again. 

>> >> >> My mechanism is oriented around data, not programs. If I want to protect month-end figures
>> >> >> in the accounting system, for example, I protect those numbers in the database.
…[26 more quoted lines elided]…
>well as multi-user.

I run milti-company, multi-user all day, every day. When I switch to another user id with
su, it runs a script that sets environment variables to that 'user' and company's
directories. The 'user' is typically a development version and stage such as dev,
integration test, system test, UAT, prod. When I start an application, it runs another
script that sets more variables specific to the application.

The important point here is that ALL applications are controlled the same way. If the
environmental stuff were hard coded in the application, each application would be
controlled differently. 

>One company may have bespoke programs that suit a particular need and
>the users in that company may have additional programs that are not
>available to the same application run for another company.

We put the menu (and error messages) in a database, keyed by company, same as you do. 
One off programs and scripts are run by us. If the user needs access to it, it's not a one
timer, it gets added to the menu and library.

>> and is irrelevant to dynamic loading. You could do the same if all
>> programs were in one library.
…[6 more quoted lines elided]…
>standards of reliability.

Nonsense. We have 30,000 developers with their fingers in the pie and we don't do that. It
sounds like you don't have version control, or don't trust it. 

We do run a regression test on the whole system for major releases, which are every two
months. That's automated. 

>> Security belongs in the called program, not the menu program. A user could write his own
>> program that calls yours.
>
>Which is not an advantage for your library because he could call that
>too.

So? The called program issues an Unauthorized message and exits.

>> The moral is: don't assume users are too dumb to hack your system.
>
>It seems that you allow them to break your [security]  by merely overwriting one
>file.

My security isn't in files nor file system directories. It's not even in the passwd file.

>> >> >> If I DID want to limit access to a program function, the security check would be in the
>> >> >> function, not the file it is packaged in nor the calling program. Relying on Unix file
…[17 more quoted lines elided]…
>you win if they give up so it doesn't matter what the content is.

It IS relevant to you, since your security depends on the Unix file system. If I can
change a group member's (hidden) profile or shell login, I can get his group permission,
even though I don't belong to the group. His script could copy the main menu (or ksh) to
my home, give it world execute and setgroupid. Next time I run it, I'm in the privileged
group.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 18)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-06T20:13:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com>`
- **References:** `<p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com> <v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com> <ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com>`

```


Robert wrote:
> On Wed, 6 Feb 2008 00:19:14 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:
>
…[9 more quoted lines elided]…
> depend on application code, either.

You claimed that your mechanism of having all the programs in one
library was better. That is was more reliable, more secure, easier to
deploy and faster.

It may be insignificantly faster in the CALL, but is slower on
startup. Deployment would only be 'easier' if you don't bother to
test. Reliability is worse because a 'missing file' stops the whole
application. Now you simply change the subject to something that is
completely independent of whether it uses libraries or individual
programs.


> The goal of security is to prevent unauthorized people from seeing or changing certain
> data. I do that by protecting the DATA; you do it by preventing them from running
…[11 more quoted lines elided]…
> because mid-run aborts due to missing program are impossible.

These are mere assertions. Having a script to do ZIP up everything is
just as simple as having a list for ld.  Actually the ZIP list can be
*.so, so that is simpler and more reliable because it collects
everything and not just what is in the list of -ls. On unzipping it
won't remove a file that failed to be included in zip, while a library
short of one program will make that unavailable.

'Simple' is 'what you are used to'. It may be simpler for you because
you already have it all set up. My way is simpler for me because I
have mine set up. You are attempting to claim some sort of 'global
universal truth' for your assertions (as usual).

As I say, if you don't test what you are sending out then it _will_ be
less reliable.

I use auditing tools, too. Programs COPY in a 'version.ws' that is
recreated each run of make so that I can check that a deployment to a
site has resulted in the correct versions of all programs, and this
_would_ pick up if anything is missing.

Your assertion that yours is 'more reliable' is complete nonsense.
Mine is 100% and you have previously stated that your stuff goes
missing.

Your claim about faster loading is also nonsense. Your startup will
take longer because you also load the library(s). I load on demand and
only load the one that are actually used. The startup time difference
may be noticable, the load of an individual program is not.


> >> >> >What makes you think that users have write access to the program
> >> >> >directory ? _I_ can drop in another program.
…[20 more quoted lines elided]…
> Ritchie did it first.

I was not referring to your _Operating_System_ but to your system of
assembling programs.


> >> Security belongs in the called program, not the menu program. A user could write his own
> >> program that calls yours.
…[4 more quoted lines elided]…
> So? The called program issues an Unauthorized message and exits.

And why do you think that "A user could write his own program that
calls yours." and have it work ?


> >Instead of addressing your claimed superiority you merely ramble on
> >about something else entirely unrelated, and straw-men, in the hope
…[7 more quoted lines elided]…
> group.

Well they can't.

I don't have 30,000 developers trying to take me down. The level of
security is entirely appropriate for the types of business and clients
that I look after.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 19)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-07T20:55:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com>`
- **References:** `<eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com> <v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com> <ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com>`

```
On Wed, 6 Feb 2008 20:13:38 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>
>
…[23 more quoted lines elided]…
>programs.

I talk about packaging called programs, you respond with security concerns. I respond to
those security concerns, you say it is irrelevant to packaging. 

To me, security and packaging ARE unrelated. To you, they are related because you are
using file system permissions as program permissions. So long as you do that, you MUST use
dynamic loading. The security tail is wagging the program loading dog.

>> The goal of security is to prevent unauthorized people from seeing or changing certain
>> data. I do that by protecting the DATA; you do it by preventing them from running
…[18 more quoted lines elided]…
>short of one program will make that unavailable.

It is dangerous to use wildcards when building distribution packages such as zip or
library. You can inadvertantly include an untested version, an experimental test version,
even a trojan. A list guarantees that every component in the distribution package went
through the testing and review process.

The faulty lists I mentioned earlier are fixed in the first test cycle. After that, the
list does not change unless a newer version is linked to a defect report, code review and
test results. 

>'Simple' is 'what you are used to'. It may be simpler for you because
>you already have it all set up. My way is simpler for me because I
>have mine set up. You are attempting to claim some sort of 'global
>universal truth' for your assertions (as usual).

I'm claiming that dynamic program structure is the norm and the default.

>As I say, if you don't test what you are sending out then it _will_ be
>less reliable.

We test every changed program when it is new. We don't retest it because another program
changed. That's a waste of time. If you find retesting necessary, you either have no
version control or hidden linkage between programs.

>I use auditing tools, too. Programs COPY in a 'version.ws' that is
>recreated each run of make so that I can check that a deployment to a
>site has resulted in the correct versions of all programs, and this
>_would_ pick up if anything is missing.

Good. Can you view the differences between ANY two versions, say between 2.2 and 2.4? How
do you propogate an emergency fix to 2.5, now in production, to ALL upstream versions --
say 3.1 in testing and 4.0 in development? That's the acid test for good version control. 

>Your claim about faster loading is also nonsense. Your startup will
>take longer because you also load the library(s). I load on demand and
>only load the one that are actually used. The startup time difference
>may be noticable, the load of an individual program is not.

Load time is about the same per file, independent of size. Loading a big library is almost
as fast as the first dynamic load. 

>> >So, you would concede then that I have described a mechanism that
>> >would not be able to be used by your system the way that you have it
…[6 more quoted lines elided]…
>assembling programs.

It's the ELF system of assembling programs. Microsoft's PE system works the same way.

>> >> Security belongs in the called program, not the menu program. A user could write his own
>> >> program that calls yours.
…[7 more quoted lines elided]…
>calls yours." and have it work ?

 I'd write a called program stub and put it ahead of yours in the library path. The stub
would display the contents of each parameter, then relay the call to the original. After
the boss runs it once, I'd write a menu program that passes the same values. 

>I don't have 30,000 developers trying to take me down. The level of
>security is entirely appropriate for the types of business and clients
>that I look after.

That's what everyone says. Do you expect them to say they have inadequate security? An
intrusion makes that announcement, after it's too late.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 20)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-07T21:22:32-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com>`
- **References:** `<eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com> <8218c22d-f418-42f2-b729-c9c11a81e3e2@m34g2000hsb.googlegroups.com> <v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com> <ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com>`

```
On Feb 8, 3:55 pm, Robert <n...@e.mail> wrote:
> On Wed, 6 Feb 2008 20:13:38 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
>
…[25 more quoted lines elided]…
> I talk about packaging called programs, you respond with security concerns.

No Robert, it was you that started with 'security'.

> I respond to
> those security concerns, you say it is irrelevant to packaging.
…[3 more quoted lines elided]…
> dynamic loading. The security tail is wagging the program loading dog.

Actually I was using dynamic loading long before there were security
concerns, or indeed facilities to do so. Using file system permissions
was a bonus.


> >> The goal of security is to prevent unauthorized people from seeing or changing certain
> >> data. I do that by protecting the DATA; you do it by preventing them from running
…[21 more quoted lines elided]…
> library. You can inadvertantly include an untested version,

As you pointed out when I said that you might include an untested
version in your library: untested versions don't get to the issue
directory.

> an experimental test version,

Won't get to the issue directory.

> even a trojan. A list guarantees that every component in the distribution package went
> through the testing and review process.

But you are packaging up everything in the library, not just a list of
new stuff.

>
> The faulty lists I mentioned earlier are fixed in the first test cycle. After that, the
…[8 more quoted lines elided]…
> I'm claiming that dynamic program structure is the norm and the default.

It may well be that in your cubicle.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 21)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-08T19:33:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com>`
- **References:** `<v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com> <ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com>`

```
On Thu, 7 Feb 2008 21:22:32 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 8, 3:55 pm, Robert <n...@e.mail> wrote:
>> On Wed, 6 Feb 2008 20:13:38 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[3 more quoted lines elided]…
>was a bonus.

I know. You are using MS-DOS (or equivalent) technology. We are no longer limited to 640K;
we have plenty of memory. More to the point, we have sophisticated linkers that did not
exist when the Cobol spec for late binding was written and you started using it. 

>> It is dangerous to use wildcards when building distribution packages such as zip or
>> library. You can inadvertantly include an untested version,
…[7 more quoted lines elided]…
>Won't get to the issue directory.

You keep it out of the issue directory with personal knowledge. You look at the program
name and 'just know' it is a test version.

Your system breaks down when someone other than you is doing builds and deployment. He
checks out everything in the change manager directory without knowing which are ready for
prime time and which aren't. 

Forbidding checkin of test code is a big mistake. You WANT developers to commit inflight
code to the repository for a number of reasons. You distinguish between good and test code
with a list of 'committed code'. That list is used by the make file, its linker and
ultimately the deployment script.

>> even a trojan. A list guarantees that every component in the distribution package went
>> through the testing and review process.
>
>But you are packaging up everything in the library, not just a list of
>new stuff.

Not everything, just code appropriate to the release. 

>> The faulty lists I mentioned earlier are fixed in the first test cycle. After that, the
>> list does not change unless a newer version is linked to a defect report, code review and
…[9 more quoted lines elided]…
>It may well be that in your cubicle.

You are trying to make it sound like I invented the ELF link/load process that is THE NORM
on millions of Unix machines. Readers can confirm by reading any Unix tutorial or manual.

By clinging to an obsolete binding technique, you are confirming what 'they' think about
Cobol being a dinosaur.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 22)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-08T20:10:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com>`
- **References:** `<v6sfq353a2ohftuaetdbf8nqhpmioqendl@4ax.com> <f95c2c8c-6c13-438b-8a3f-3bbd70829fc5@b2g2000hsg.googlegroups.com> <ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com>`

```
On Feb 9, 2:33 pm, Robert <n...@e.mail> wrote:
> On Thu, 7 Feb 2008 21:22:32 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 8, 3:55 pm, Robert <n...@e.mail> wrote:
…[6 more quoted lines elided]…
> I know. You are using MS-DOS (or equivalent) technology.

You fail to understand, once again.

You wrote:

RW>> Why is Cobol the only language with a pressing
RW>> need for dynamic linking? Huge bodies of code
RW>> written in C and other languages get by without it.

Which is flawed and a very limited view, because there are many
languages that use dynamic loading, dynamic linking and late binding.

You want to make a comparison to C, a 30 year old language that has no
concept of late binding. Sure, that does static linking and binding on
library load. But modern languages are increasingly using more
advanced techniques.

For example Objective C:
http://developer.apple.com/documentation/Cocoa/Conceptual/OOP_ObjC/Articles/chapter_5_section_6.html#//apple_ref/doc/uid/TP40005149-CH5-SW19

"Perhaps the most important current benefit of dynamic loading is that
it makes applications extensible."

> We are no longer limited to 640K;
> we have plenty of memory. More to the point, we have sophisticated linkers that did not
> exist when the Cobol spec for late binding was written and you started using it.

You are confused. Dynamic LOADING does not require the programs to be
CANCELed. However, CANCELing may have been a benefit to limited
memory, it is ALSO a benefit where systems can be made more dynamic by
replacement:

"The program can even offer sets of alternative tools to do the same
job--the user then selects one tool from the set and only that tool
would be loaded."

In that particular case one set can be CANCELled and replaced by
another.

I also do dynamic loading in Python and have done it in Java.

Using a mindset that things are 'C or COBOL' is very limiting.


> >> It is dangerous to use wildcards when building distribution packages such as zip or
> >> library. You can inadvertantly include an untested version,
…[10 more quoted lines elided]…
> name and 'just know' it is a test version.

No, it is kept out by procedures, just like your list is kept correct
by procedures.

> Your system breaks down when someone other than you is doing builds and deployment. He
> checks out everything in the change manager directory without knowing which are ready for
> prime time and which aren't.

Are you drawing on your experience for these scenarios ?

> Forbidding checkin of test code is a big mistake. You WANT developers to commit inflight
> code to the repository for a number of reasons. You distinguish between good and test code
> with a list of 'committed code'. That list is used by the make file, its linker and
> ultimately the deployment script.

Just make stuff up, Robert. Create straw-men arguments, they are much
easier than knowing anything about reality.


> >> even a trojan. A list guarantees that every component in the distribution package went
> >> through the testing and review process.
…[5 more quoted lines elided]…
>

Excuse me, you issue a new library with "just code appropriate to the
release.".  What about all the other programs that were in the
previous release of that library ?


> >> The faulty lists I mentioned earlier are fixed in the first test cycle. After that, the
> >> list does not change unless a newer version is linked to a defect report, code review and
…[12 more quoted lines elided]…
> on millions of Unix machines.

No, it is only you doing that. When I said 'your system' it was 'the
system you use'.

While you are quite correct that what you describe is 'the norm' for C
and even C++, it is not used for Java, Python, PERL, and many other,
more modern, languages.

> By clinging to an obsolete binding technique,

In what way is it 'obsolete' if modern languages are adopting it ? You
really should get out more and go beyond 30 year old C.

> you are confirming what 'they' think about
> Cobol being a dinosaur.

Well, I really don't care what 'they' think about anything. Nor do I
care much about what you think. A few years ago about 90% of what I
did was Cobol, now it is less than 10%.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 23)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-09T23:41:57-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com>`
- **References:** `<ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com>`

```
On Fri, 8 Feb 2008 20:10:38 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 9, 2:33 pm, Robert <n...@e.mail> wrote:
>> On Thu, 7 Feb 2008 21:22:32 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[9 more quoted lines elided]…
>You fail to understand, once again.

Not AGAIN. (Flailing self; donning haircloth shirt.)

>You wrote:
>
…[13 more quoted lines elided]…
>http://developer.apple.com/documentation/Cocoa/Conceptual/OOP_ObjC/Articles/chapter_5_section_6.html#//apple_ref/doc/uid/TP40005149-CH5-SW19

It talks as though there are two choices: static and dynamic, early and late binding. It
seems written 20 years ago. There is now a third choice, controlled dynamic, the one used
by Unix and Windows. 

>"Perhaps the most important current benefit of dynamic loading is that
>it makes applications extensible."

Sounds like they're talking about plug-ins. Watch your browser when it starts and you'll
see it "loading plug-ins". It doesn't wait 'till the first call. 

>> We are no longer limited to 640K;
>> we have plenty of memory. More to the point, we have sophisticated linkers that did not
…[12 more quoted lines elided]…
>another.

Replacement is an overload. It isn't necessary to delete the old program from memory in
order to replace it with a new one. All you need to do is change the pointer to the new
program. 

>I also do dynamic loading in Python and have done it in Java.
>
>Using a mindset that things are 'C or COBOL' is very limiting.

C is the lingua franca of programming, the foundation language everyone understands. 

>> >> It is dangerous to use wildcards when building distribution packages such as zip or
>> >> library. You can inadvertantly include an untested version,
…[19 more quoted lines elided]…
>Are you drawing on your experience for these scenarios ?

Yes. For instance, when I was change management administrator at Wal-Mart, my mission was
to move applications to new hardware platforms. Management thought it was simple, 'All ya
gotta do is recompile the programs.' The question became, which of the six slightly
different versions of the programs. There was no way of knowing which was in Production.
In a few cases, none of them compiled without error. A list of committed program versions
would have solved the problem.

>> Forbidding checkin of test code is a big mistake. You WANT developers to commit inflight
>> code to the repository for a number of reasons. You distinguish between good and test code
…[4 more quoted lines elided]…
>easier than knowing anything about reality.

If you don't have a riposte, say nothing. Accusing me of lying doesn't benefit anyone.

>> >> even a trojan. A list guarantees that every component in the distribution package went
>> >> through the testing and review process.
…[9 more quoted lines elided]…
>previous release of that library ?

The list is cumulative. Old programs remain in the list until deleted. 

>> >> The faulty lists I mentioned earlier are fixed in the first test cycle. After that, the
>> >> list does not change unless a newer version is linked to a defect report, code review and
…[15 more quoted lines elided]…
>system you use'.

Now I'm the only one using Unix ELF and Windows PE.

>While you are quite correct that what you describe is 'the norm' for C
>and even C++, it is not used for Java, Python, PERL, and many other,
>more modern, languages.

That's because Java and PERL are compiled Just In Time at execution time. 
It IS used for Python, when compiled to C++ and linked normally. 

The topic here is Cobol, which compiles and links at development time, like C.

>> By clinging to an obsolete binding technique,
>
…[8 more quoted lines elided]…
>did was Cobol, now it is less than 10%.

I find that interesting. I still prefer Cobol over the other languages I know, which do
not include Java and Python, do include lots of scripting languages such as PERL and
PL/SQL.

PERL isn't a single language, it's two languages. Procedural PERL looks like Unix shell
scripts such as ksh; OO PERL looks like C++.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 24)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-10T00:08:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com>`
- **References:** `<ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com>`

```
On Feb 10, 6:41 pm, Robert <n...@e.mail> wrote:

> >You want to make a comparison to C, a 30 year old language that has no
> >concept of late binding. Sure, that does static linking and binding on
…[14 more quoted lines elided]…
> see it "loading plug-ins". It doesn't wait 'till the first call.

While Firefox does load extensions early it is not 'at startup' (ie
before the program starts executing) as your does, but it has actually
started executing which is why it can produce the message. It does
this because the extensions are (mostly) used while browsing, such as
NoScript, and these are required as the browser opens the home page so
they _are_ loaded at 'first call'. Other extensions are only loaded
when required.

Other application plugins, such as used by graphics or CAD programs
are loaded when the function is performed.

> >In that particular case one set can be CANCELled and replaced by
> >another.
…[3 more quoted lines elided]…
> program.

Non OO COBOL doesn't support overload. ANS'85 COBOL doesn't support
pointers.


> >I also do dynamic loading in Python and have done it in Java.
>
> >Using a mindset that things are 'C or COBOL' is very limiting.
>
> C is the lingua franca of programming, the foundation language everyone understands.

How many business application use C ?  C is not OO. While it is used,
as it was originally designed, for operating systems and utilities, it
has some problems for use in business programming.

> >> You are trying to make it sound like I invented the ELF link/load process that is THE NORM
> >> on millions of Unix machines.
>
> >No, it is only you doing that.

Geez, Robert. It is worrying. Do you ever read program specs
correctly ?

No, it is only you doing 'trying to make it sound like I invented the
ELF link/load process'.

> When I said 'your system' it was 'the
> >system you use'.
>
> Now I'm the only one using Unix ELF and Windows PE.

You did a whole pontification on what pronouns stand for then make a
simple mistake by linking 'that' back to a qualifier phrase'.


> >While you are quite correct that what you describe is 'the norm' for C
> >and even C++, it is not used for Java, Python, PERL, and many other,
> >more modern, languages.
>
> That's because Java and PERL are compiled Just In Time at execution time.

And for VB and Ruby and ...

> It IS used for Python, when compiled to C++ and linked normally.

No. Wrong. Very wrong.

You don't know Python then. While there are ways of interfacing Python
and C++ you cannot 'compile Python to C++'. Python is a dynamic
language,


> The topic here is Cobol, which compiles and links at development time, like C.

COBOL has traditionally been used with dynamic loading. Mainframes use
dynamic loading. Micro Focus since 1978 has compiled to .int (later
also .gnt), even when these were built into .exe and .dll they were
dynamically loaded as required,

RM and Accu Cobol were built around dynamic loading and couldn't use
anything else.

You are trying to turn Cobol in C (presumably because of what 'they'
think). If the topic is 'Cobol' then use Cobol and stop ranting about
what is the 'norm for C' (and is not for Cobol).


> >> By clinging to an obsolete binding technique,
>
…[15 more quoted lines elided]…
> scripts such as ksh; OO PERL looks like C++.

Geez, Robert. I have done PERL systems. It is just _one_ language
which has a 'rich and varied' syntax. I have even done what they sort-
of call OO.

I went back to Python as soon as possible.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 25)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-10T22:25:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lqcvq35er05go2391ej4tenk6gh338nono@4ax.com>`
- **References:** `<0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com>`

```
On Sun, 10 Feb 2008 00:08:35 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 10, 6:41 pm, Robert <n...@e.mail> wrote:

>> >In that particular case one set can be CANCELled and replaced by
>> >another.
…[6 more quoted lines elided]…
>pointers.

The Cobol standard has supported pointers for six years, and major compilers have
supported pointers for at least ten years. 

>> >I also do dynamic loading in Python and have done it in Java.
>>
…[6 more quoted lines elided]…
>has some problems for use in business programming.

It is common for most of a large business application to be written in Cobol, but the
parts that interface with the OS and database are written in C. That's because the systems
programmers who design architecture believe the story about C being better for systems
work, and because they don't understand Cobol. The result is slow database access, because
variables are translated twice -- first from database to C, then from C to Cobol. 

>> >While you are quite correct that what you describe is 'the norm' for C
>> >and even C++, it is not used for Java, Python, PERL, and many other,
…[8 more quoted lines elided]…
>No. Wrong. Very wrong.

>You don't know Python then. While there are ways of interfacing Python
>and C++ you cannot 'compile Python to C++'. Python is a dynamic
>language,

You are correct when you say I don't know Python. I do know it is normally compiled to
interpreted byte code, thus not a candidate for ELF/PE binding. 

"Shed Skin is an experimental Python-to-C++ compiler, than can translate pure, but
implicitly statically typed Python programs into optimized C++."
http://mark.dufour.googlepages.com/shedskin

>> The topic here is Cobol, which compiles and links at development time, like C.
>
…[3 more quoted lines elided]…
>dynamically loaded as required,

When compiled to OS standard executables (ELF), they can be loaded the normal way by ld or
dynamically by dlopen. Source code is the same for both. The method of loading is
determined by compiler option and link parameter. 

>RM and Accu Cobol were built around dynamic loading and couldn't use
>anything else.

Micro Focus, Fujitsu, IBM and OC produce OS standard executables.  RM and Acu produce
interpreted byte code. 

>You are trying to turn Cobol in C (presumably because of what 'they'
>think). If the topic is 'Cobol' then use Cobol and stop ranting about
>what is the 'norm for C' (and is not for Cobol).

I'm talking about the norm for OS standard execuables. Besides Cobol and C/C++, other
compiled lanaguages are ALGOL, BASIC, Delphi, PL/I and, increasingly, Java. 

"GCJ is a portable, optimizing, ahead-of-time compiler for the Java Programming Language.
It can compile Java source code to Java bytecode (class files) or directly to native
machine code, and Java bytecode to native machine code."
http://gcc.gnu.org/java/

>> >> By clinging to an obsolete binding technique,
>>
>> >In what way is it 'obsolete' if modern languages are adopting it ? You
>> >really should get out more and go beyond 30 year old C.

There is nothig new about interpreted byte code. It has been re-invented hundreds of
times, because it makes writing a compiler easier. The problem is that programs run too
slowly. As a language matures, its compilers switch to native code, either ahead of time
or JIT.  Micro Focus made the switch when it went from .int to .gnt, later to OS standard
format executables. Recently created languages such as Python, Ruby, Tcl, et al. have not
yet progressed to native code. 

Dynamic loading is the only form of late binding available to interpreted byte code. I'm
saying that when a language advances to OS standard executables, it should also adopt the
OS standard binding technique. "We've always done it that way" is a poor reason to retain
dynamic loading.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 26)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-10T21:29:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<91e4d295-6210-4fb8-8bd3-ca5be45463e0@b2g2000hsg.googlegroups.com>`
- **References:** `<0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com>`

```
On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:
> On Sun, 10 Feb 2008 00:08:35 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 10, 6:41 pm, Robert <n...@e.mail> wrote:
…[27 more quoted lines elided]…
> variables are translated twice -- first from database to C, then from C to Cobol.

So, what are you saying ? Dump COBOL ?

>
> >> >While you are quite correct that what you describe is 'the norm' for C
…[18 more quoted lines elided]…
> implicitly statically typed Python programs into optimized C++."http://mark.dufour.googlepages.com/shedskin

If it is statically typed then it isn't Python, it may look similar
and have some common syntax, but it ain't Python.


> >> The topic here is Cobol, which compiles and links at development time, like C.
>
…[7 more quoted lines elided]…
> determined by compiler option and link parameter.

Well, actually I don't care about whether dlopen is used or not, I
just use CALL.  As it happens I often use CALL dataname.  I have
chosen the compiler options and link parameters that work best for me.

What I don't get is why you want to jam your way of doing things down
my (and Charle's) throat.

People might think that you are arrogant for trying to do that.


> >RM and Accu Cobol were built around dynamic loading and couldn't use
> >anything else.
>
> Micro Focus, Fujitsu, IBM and OC produce OS standard executables.  RM and Acu produce
> interpreted byte code.

Actually Micro Focus can produce byte code too, see OPT(0) compiler
option.


> >You are trying to turn Cobol in C (presumably because of what 'they'
> >think). If the topic is 'Cobol' then use Cobol and stop ranting about
…[3 more quoted lines elided]…
> compiled lanaguages are ALGOL, BASIC, Delphi, PL/I and, increasingly, Java.

It is an implementation issue whether a language compiler produces
byte code or machine code and how the modules are loaded and linked.
Some BASICs run from source, some code it, some go to machine code.
Same with other languages.

> "GCJ is a portable, optimizing, ahead-of-time compiler for the Java Programming Language.
> It can compile Java source code to Java bytecode (class files) or directly to native
> machine code, and Java bytecode to native machine code."http://gcc.gnu.org/java/

Yes, it is sort-of Java and a few versions behind.

"""supports most of the 1.4 libraries plus some 1.5 additions."""

> >> >> By clinging to an obsolete binding technique,
>
…[8 more quoted lines elided]…
> yet progressed to native code.

UCSD Pascal on a 1MHz 6502 was pretty slow, yes.  Python, Ruby, PERL,
Tcl on a 2GHz dual core is not. Certainly you wouldn't write a
database server in those, but for an interactive system there would be
no difference in response - 90% of the time would be db access anyway
and thus the same for both.

> Dynamic loading is the only form of late binding available to interpreted byte code. I'm
> saying that when a language advances to OS standard executables,

It isn't the _language_, it is the _implementation_.

> it should also adopt the
> OS standard binding technique.

Which _I_ adopt is the one that suits me. The implementation offers
several alternatives from which I can evaluate and choose.

If you want to choose a different way then please do so.

> "We've always done it that way" is a poor reason to retain
> dynamic loading.

You are quite right, I have _much_ better reasons than that, in fact
that one wasn't even on the list.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 27)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-11T20:51:29-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<biu1r3t2al1jicfcqhcesk70lpean8o0mt@4ax.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <91e4d295-6210-4fb8-8bd3-ca5be45463e0@b2g2000hsg.googlegroups.com>`

```
On Sun, 10 Feb 2008 21:29:59 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:
>> On Sun, 10 Feb 2008 00:08:35 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
>> >On Feb 10, 6:41 pm, Robert <n...@e.mail> wrote:

>> >> C is the lingua franca of programming, the foundation language everyone understands.
>>
…[10 more quoted lines elided]…
>So, what are you saying ? Dump COBOL ?

I'm saying it would be faster to let Cobol programs do their own SQL. 

>> >> The topic here is Cobol, which compiles and links at development time, like C.
>>
…[11 more quoted lines elided]…
>chosen the compiler options and link parameters that work best for me.

Call dataname does not prevent normal binding. If Cobol finds the target already bound, it
uses a normal call. If the called program is not bound THEN Cobol does a dynamic load. The
programmer doesn't have to change a line of source code. The only difference is in the
make file, and the fact that CANCEL doesn't work, at least on Fujitsu. 

>What I don't get is why you want to jam your way of doing things down
>my (and Charle's) throat.

I keep telling you it's not my way, it's the Unix norm. 

>People might think that you are arrogant for trying to do that.

Explaining one's position is not arrogant. What's arrogant using wordplay to turn other
people's words against them.

>> >RM and Accu Cobol were built around dynamic loading and couldn't use
>> >anything else.
…[5 more quoted lines elided]…
>option.

Micro Focus ALWAYS produces an .int file containing byte code. The back end turns an .int
into machine language. One can compile an .int file, in which case the compiler runs only
its back end.

NOOPT is the option to turn off optimization; OPT(0) is invalid.

>> >You are trying to turn Cobol in C (presumably because of what 'they'
>> >think). If the topic is 'Cobol' then use Cobol and stop ranting about
…[8 more quoted lines elided]…
>Same with other languages.

Right. When using proprietary compiler features such as MF's .gnt format, the compiler can
do whatever it wants. But when using OS standard format such as ELF, one should abide by
the norms of that format and culture.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 28)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-11T20:41:27-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<74d9b8a4-3008-415f-b197-3e62e3fd6b4e@z17g2000hsg.googlegroups.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <91e4d295-6210-4fb8-8bd3-ca5be45463e0@b2g2000hsg.googlegroups.com> <biu1r3t2al1jicfcqhcesk70lpean8o0mt@4ax.com>`

```

Robert wrote:
> On Sun, 10 Feb 2008 21:29:59 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:
>
…[3 more quoted lines elided]…
>

> >> It is common for most of a large business application to be written in Cobol, but the
> >> parts that interface with the OS and database are written in C. That's because the systems
…[6 more quoted lines elided]…
> I'm saying it would be faster to let Cobol programs do their own SQL.

You are unclear whether "the systems programmers who design
architecture" are those in your site (and thus you must call some C
intermediate routines), or whether you are talking about what Micro
Focus, Fujitsu and/or Oracle do with the EXEC SQLs.

In other words it was a non-specific rant that went nowhere.

> >> >> The topic here is Cobol, which compiles and links at development time, like C.
> >>
…[21 more quoted lines elided]…
> I keep telling you it's not my way, it's the Unix norm.

It is the way that you do it, it is 'your way', why do you have such
problems understanding simple statements ?

While you claim it is 'the Unix norm', that is quite irrelevant. It is
actually 'the C norm', not Cobol's, not many other languages. A range
of facilities is available from which a choice can be made. The choice
should be based on objective evaluation of the advantages and
disadvantages.

A 'Brooklyn Bridge' argument is not objective, nor is 'ugly'.

If Unix wants to force a particular way then it should not offer other
alternatives.

> >People might think that you are arrogant for trying to do that.
>
> Explaining one's position is not arrogant. What's arrogant using wordplay to turn other
> people's words against them.

You have gone way beyond "Explaining one's position", you have berated
me with attempts to make me change to using 'the way you do it'.
Mostly with spurious and irrelevant arguments, many of which are
simply incorrect.

> >> >RM and Accu Cobol were built around dynamic loading and couldn't use
> >> >anything else.
…[11 more quoted lines elided]…
> NOOPT is the option to turn off optimization; OPT(0) is invalid.

Then you should tell my MF compiler that it is invalid because it
quite happily accepts 0 as a parameter. In fact the documentation
lists the valid parameters as 0,1,or 2.


> >> >You are trying to turn Cobol in C (presumably because of what 'they'
> >> >think). If the topic is 'Cobol' then use Cobol and stop ranting about
…[12 more quoted lines elided]…
> the norms of that format and culture.

See, once again, you arrogantly try to force your way down my throat.

In fact I am using ELF exactly as it allows me to. There are no
special tricks, it is completely normal for ELF to work the way that I
use it.

Saying that you have a very narrow-minded viewpoint is 'fair comment'.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 29)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-12T21:27:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<62c4r3tggikdm53of17dq8jduvbgun7m2m@4ax.com>`
- **References:** `<fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <91e4d295-6210-4fb8-8bd3-ca5be45463e0@b2g2000hsg.googlegroups.com> <biu1r3t2al1jicfcqhcesk70lpean8o0mt@4ax.com> <74d9b8a4-3008-415f-b197-3e62e3fd6b4e@z17g2000hsg.googlegroups.com>`

```
On Mon, 11 Feb 2008 20:41:27 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>Robert wrote:
>> On Sun, 10 Feb 2008 21:29:59 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:
…[4 more quoted lines elided]…
>>

>> >> >> The topic here is Cobol, which compiles and links at development time, like C.
>> >>
…[30 more quoted lines elided]…
>disadvantages.

 I'll summarize the advantages of link time versus execution time binding. 

Advantages of link time binding (not to be confused with static linking)

.. The linker takes inventory to insure all called programs are available.
.. The execution time loader takes inventory again. If any program or library is missing,
    the main program does not start. 
.. System tools can create where used lists.
.. Fewer files.  Many called programs in a library.

Advantages of execution time binding (aka dynamic load)

.. Missing programs can be (must be) handled with program logic -- ON EXCEPTION.
.. A called program can be CANCELled and reloaded without shutting down the main program.

Disadvantages

.. No automatic inventory. Application can abort mid-run if called program is missing and
   there is no ON EXCEPTION.
.. Many files, one per called program.
.. Version control is more difficult. 

Comments
.. The advantages of execution time binding are no benefit to batch programs.
.. When the number of called programs is large, in the hundreds, the benefit of automatic
    inventory may outweigh the benefit of dynamic load.
.. Both techniques can be used in the same executable. For example, ad hoc programs
   can be bound dynamically (name from database or keyboard) while stable components 
   are bound at link time.

>A 'Brooklyn Bridge' argument is not objective, nor is 'ugly'.

Shop and de facto standards are a form of Brooklyn Bridge argument. If one is a
build/deployment administrator, as I am sometimes, and creates an environment different
from the norm, he better have good reasons. 

>If Unix wants to force a particular way then it should not offer other
>alternatives.

The easy to use default is best for most situations. The non-default is available for
special needs. 

>> >People might think that you are arrogant for trying to do that.
>>
…[6 more quoted lines elided]…
>simply incorrect.

You persist in calling normal binding 'my way,' as though I created it. What I advocate is
not a novel idea, it's the binding method used in every Cobol/Unix shop I've seen, which
includes very large companies who get ideas from many Unix experts. 

You won't find a quote where I tried to make YOU change; I said "one" should change. I've
offered reasons why linker binding is better than the way you advocate, especially for
batch processing, which is the primary use for Cobol at those companies. I worked at one
place that used AcuCobol for Windows GUI; it used linker bound DLLs. 

>Saying that you have a very narrow-minded viewpoint is 'fair comment'.

Readers don't care about the breadth of my thinkig, they want to know about Cobol and
Unix.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 30)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-12T20:41:49-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a876d227-2b19-4b86-90d9-226ed05029c6@q77g2000hsh.googlegroups.com>`
- **References:** `<fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <91e4d295-6210-4fb8-8bd3-ca5be45463e0@b2g2000hsg.googlegroups.com> <biu1r3t2al1jicfcqhcesk70lpean8o0mt@4ax.com> <74d9b8a4-3008-415f-b197-3e62e3fd6b4e@z17g2000hsg.googlegroups.com> <62c4r3tggikdm53of17dq8jduvbgun7m2m@4ax.com>`

```
On Feb 13, 4:27 pm, Robert <n...@e.mail> wrote:
>
> >It is the way that you do it, it is 'your way', why do you have such
> >problems understanding simple statements ?
>
>  I'll summarize the advantages of link time versus execution time binding.

No. Wrong, you will summarize your _claims_. These _may_ be an
advantage to you in your environment, but you spout them as if what
you say is some sort of 'universal truth' (as you usually do).

You obviously haven't listened _at_all_ to what is said to you (as
usual) and merely mindlessly repeat the same claims.


> Advantages of link time binding (not to be confused with static linking)
>
> .. The linker takes inventory to insure all called programs are available.

Not an 'advantage' at all to me.  My client sites have different sets
of programs so some may not be available _deliberately_.

> .. The execution time loader takes inventory again. If any program or library is missing,
>     the main program does not start.

That may be an advantage in your batch systems, but 'not starting' is
not a viable option for an interactive system. Running with reduced
facility is better than not running at all.

I have never had a problem with missing programs, so it would not even
be an 'advantage'.

> .. System tools can create where used lists.

Not if the calls are dynamic. In any case it is not an advantage if
other tools can do the same thing.

Perhaps you don't understand what the word 'advantage' means.

> .. Fewer files.  Many called programs in a library.

Not an 'advantage' to me. As I said, having to issue a whole new
library just for a single updated program is not an 'advantage' at
all. iT is a disadvantage.

> Advantages of execution time binding (aka dynamic load)

> .. Missing programs can be (must be) handled with program logic -- ON EXCEPTION.
> .. A called program can be CANCELled and reloaded without shutting down the main program.

I have a list of other advantages that you either ignore or they never
occurred to you.


> Disadvantages
>
…[3 more quoted lines elided]…
> .. Version control is more difficult.

These are only 'disadvantages' if, for example there _is_ no ON
EXCEPTION.

Many files is not a disadvantage at all, to me or to Unix.

Version control may be different, but is not 'more difficult'.


> Comments
> .. The advantages of execution time binding are no benefit to batch programs.

That may, or may not, be true. Whether it is an advantage is for the
designer of the programs to determine, not you.  For example AWK is a
batch type program and at least one implementation (gawk) uses dynamic
loading to allow for plug-ins.

The alternative to a plug-in is to add the plug-in code to gawk source
and recompile your own special version. This has the possibility of
introducing bugs into the core program, or making other users fail.

I do, in fact, use dynamic loading in Python where the programs have
to deal with various types of data. Once identified the appropriate
module is loaded and the class invoked to process it.


> .. When the number of called programs is large, in the hundreds, the benefit of automatic
>     inventory may outweigh the benefit of dynamic load.

A mere opinion.

> .. Both techniques can be used in the same executable. For example, ad hoc programs
>    can be bound dynamically (name from database or keyboard) while stable components
>    are bound at link time.

Then you will get the disadvantages of _both_ mechanisms. You will
have to have _two_ mechanisms for inventory, for checking, even more
complexifications.

Then someone may decide that an 'ad hoc' is stable and adds it to the
list in the library and you have two versions: one in the library that
probably will be used, and another, older version left unremoved, that
_appears_ to be the one that is used.


> >A 'Brooklyn Bridge' argument is not objective, nor is 'ugly'.
>
> Shop and de facto standards are a form of Brooklyn Bridge argument. If one is a
> build/deployment administrator, as I am sometimes, and creates an environment different
> from the norm, he better have good reasons.

In your shop you should do what they tell you. I am not in your shop.


> >If Unix wants to force a particular way then it should not offer other
> >alternatives.
>
> The easy to use default is best for most situations. The non-default is available for
> special needs.

There is _NO_ 'default' for user routines, except perhaps static
binding. For all user routines the makefile has to be built and
parameters set to how the files are to be created.


> >> >People might think that you are arrogant for trying to do that.
>
…[8 more quoted lines elided]…
> You persist in calling normal binding 'my way,' as though I created it.

It is the way that you do it, it is 'your way', why do you have such
problems understanding simple statements ?

It is the way that you created the makefile, it is the way that you
added the parameters to the link command.

If someone pointed out your car would you think that you were Toyota ?

> What I advocate is
> not a novel idea, it's the binding method used in every Cobol/Unix shop I've seen, which
> includes very large companies who get ideas from many Unix experts.

No, it's not a novel idea, if is the 'norm for C', especially for
utilities and batch stuff.


> You won't find a quote where I tried to make YOU change; I said "one" should change.

Then you do have difficulty with English. 'Should' is compulsion. You
addressed this to those "using OS standard format such as ELF".

> I've
> offered reasons why linker binding is better than the way you advocate, especially for
> batch processing, which is the primary use for Cobol at those companies. I worked at one
> place that used AcuCobol for Windows GUI; it used linker bound DLLs.

You have offered your opinions, while ignoring the reasons that _I_
have for using dynamic loading. You may well be right for batch, but I
don't do that, not in Cobol.


> >Saying that you have a very narrow-minded viewpoint is 'fair comment'.
>
> Readers don't care about the breadth of my thinkig, they want to know about Cobol and
> Unix.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 28)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-12T11:41:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53283fc5-d72f-4abc-9cfa-736c3f8b92d2@n20g2000hsh.googlegroups.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <91e4d295-6210-4fb8-8bd3-ca5be45463e0@b2g2000hsg.googlegroups.com> <biu1r3t2al1jicfcqhcesk70lpean8o0mt@4ax.com>`

```
On Feb 12, 3:51 pm, Robert <n...@e.mail> wrote:

<snip>

> I keep telling you it's not my way, it's the Unix norm.

<snip>

> Right. When using proprietary compiler features such as MF's .gnt format, the compiler can
> do whatever it wants. But when using OS standard format such as ELF, one should abide by
> the norms of that format and culture.

I thought that I would actually see what "the norms of that format and
culture" might _actually_ be.

There is gawak, the GNU AWK. If you are unaware of what this is the
name is an acronym made from the 3 author's surnames. You can't get
more 'Unix culture' than those.

"""Beginning with gawk 3.1 [around 2000], it is possible to add new
built-in functions to gawk using dynamically loaded libraries. This
facility is available on systems (such as GNU/Linux) that support the
dlopen and dlsym functions."""

So _modern_ implementations of [at least some] Unix culture use
dynamic loading.

You are still stuck in last century's culture.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 29)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-12T23:02:13-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7et4r3hjsthetmnb34amb502jgmu0kjvfn@4ax.com>`
- **References:** `<fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <91e4d295-6210-4fb8-8bd3-ca5be45463e0@b2g2000hsg.googlegroups.com> <biu1r3t2al1jicfcqhcesk70lpean8o0mt@4ax.com> <53283fc5-d72f-4abc-9cfa-736c3f8b92d2@n20g2000hsh.googlegroups.com>`

```
On Tue, 12 Feb 2008 11:41:30 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 12, 3:51 pm, Robert <n...@e.mail> wrote:
>
…[25 more quoted lines elided]…
>You are still stuck in last century's culture.

There is a single Unix Standard, now called (fittingly) the Single UNIX Specification,
formerly POSIX. Dlopen is in that spec. Oddly, ld is not.
It was first published in the '90s. ELF became the Standard executable format in 1999.

http://www.opengroup.org/onlinepubs/009695399/
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 26)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-10T23:30:01-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f84d84fe-b1fc-4bd6-87dc-1a4cf61f435b@l16g2000hsh.googlegroups.com>`
- **References:** `<0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com>`

```
On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:

> compiled lanaguages are ALGOL, BASIC, Delphi, PL/I and, increasingly, Java.

ALGOL is a 50 year old language. On Linux Algol 68 Genie is a
scripting language, _not_ compiled. A60 is an Algol 60 interpreter,
not a compiler.

BASIC is a 40 year old language. Several implementations on Linux,
such as GamBAS, MonoBasic, HBasic are interpreters or byte code.

Delphi is a 20 year old language. Kylix on Linux does produce native
code. I don't think that it is widely used, or even much at all.

PL/I is 40 year old. There is an 'gcc PL/I project' but "Currently
there is still no codegeneration taking place, so don't run out and
uninstall your production PL/I compiler, just yet."

There are some Java native code compilers, or should I say were. see
http://schmidt.devlib.org/java/native-compilers.html and note how many
are discontinued, this hardly makes it 'increasingly'.

gjc is both a source-code-to-bytecode compiler and a native compiler,
so its use does not imply native linking.

You may also want to look at the benchmarks at
http://www.ibm.com/developerworks/library/j-native.html and see why
people don't bother with native code.

Also native code Java does not necessarily mean that it uses what you
call 'the norm' as it may just be producing the result of a JIT.

Note that most popular frameworks, such as Tomcat do dynamic class
loading and require one of the java vms to be used.

C# is a more modern language and it uses ...  the CLI. ie it is byte
coded.

Just making stuff up may impress the clueless newies around you.


> "We've always done it that way" is a poor reason to retain
> dynamic loading.

"What 'they' think" is a worse one.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 27)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-11T20:51:32-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vvn1r3hqjka5emudcra591k73crmi9ognc@4ax.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <f84d84fe-b1fc-4bd6-87dc-1a4cf61f435b@l16g2000hsh.googlegroups.com>`

```
On Sun, 10 Feb 2008 23:30:01 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:
>
…[14 more quoted lines elided]…
>uninstall your production PL/I compiler, just yet."

This Cobol forum is not a good place to disparage old languages.

>There are some Java native code compilers, or should I say were. see
>http://schmidt.devlib.org/java/native-compilers.html and note how many
>are discontinued, this hardly makes it 'increasingly'.

Reduced number of compilers seems like normal shakeout/consolidation for maturing
software. 

Notably absent from the list are Eclipse Compiler for Java (ECJ),  GNU Compiler for Java
(GCJ). 

>gjc is both a source-code-to-bytecode compiler and a native compiler,
>so its use does not imply native linking.

2.3 Why does GCJ use CNI?

        We use CNI because we think it is a better solution, especially for a Java
implementation that is based on the idea that Java is just another programming language
that can be implemented using standard compilation techniques. Given that, and the idea
that languages implemented using Gcc should be compatible where it makes sense, it follows
that the Java calling convention should be as similar as practical to that used for other
languages, especially C++, since we can think of Java as a subset of C++. CNI is just a
set of helper functions and conventions built on the idea that C++ and Java have the
*same* calling convention and object layout; they are binary compatible. (This is a
simplification, but close enough.)

http://gcc.gnu.org/java/faq.html#2_3

>You may also want to look at the benchmarks at
>http://www.ibm.com/developerworks/library/j-native.html and see why
>people don't bother with native code.

They're all native code. The three compared to gcj are JIT compilers.

>Also native code Java does not necessarily mean that it uses what you
>call 'the norm' as it may just be producing the result of a JIT.

That's true.  Most of them require a JVM at run time. 

>Note that most popular frameworks, such as Tomcat do dynamic class
>loading and require one of the java vms to be used.
>
>C# is a more modern language and it uses ...  the CLI. ie it is byte
>coded.

You forgot to mention that CIL *must* be JIT compiled. Neither MS nor Mono will run it as
interpreted byte code.  Also that it is statically typed.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 28)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-11T20:49:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0e4f3b9-d617-4fe5-9f3d-e7a1a4446096@i12g2000prf.googlegroups.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <f84d84fe-b1fc-4bd6-87dc-1a4cf61f435b@l16g2000hsh.googlegroups.com> <vvn1r3hqjka5emudcra591k73crmi9ognc@4ax.com>`

```
On Feb 12, 3:51 pm, Robert <n...@e.mail> wrote:
> On Sun, 10 Feb 2008 23:30:01 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:
…[17 more quoted lines elided]…
> This Cobol forum is not a good place to disparage old languages.

There is nothing disparaging about stating facts about a language.

What were you saying about 'using wordplay' ?

Once again you use feined insult as deflection from your
misinformation.

> >There are some Java native code compilers, or should I say were. see
> >http://schmidt.devlib.org/java/native-compilers.htmland note how many
…[34 more quoted lines elided]…
> That's true.  Most of them require a JVM at run time.

So your attempt to show that Java (aside from all the other languages)
is 'increasingly' using 'the norm for C' fails completely.


> >Note that most popular frameworks, such as Tomcat do dynamic class
> >loading and require one of the java vms to be used.
…[5 more quoted lines elided]…
> interpreted byte code.  Also that it is statically typed.

I may have mentioned that if it had been in any way relevant. As it is
it is merely enough to show that it doesn't follow 'the norm for C'.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 29)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-12T22:39:54-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fso4r3lgi3p9cnhr9k8gmgj9un42ih1g5t@4ax.com>`
- **References:** `<fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <f84d84fe-b1fc-4bd6-87dc-1a4cf61f435b@l16g2000hsh.googlegroups.com> <vvn1r3hqjka5emudcra591k73crmi9ognc@4ax.com> <f0e4f3b9-d617-4fe5-9f3d-e7a1a4446096@i12g2000prf.googlegroups.com>`

```
On Mon, 11 Feb 2008 20:49:40 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 12, 3:51 pm, Robert <n...@e.mail> wrote:
>> On Sun, 10 Feb 2008 23:30:01 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[32 more quoted lines elided]…
>> software.

This web page that talks about why Java native code compilers fell out of favor, without
reaching a conclusion.

http://www.bearcave.com/software/java/comp_java.html

>> >C# is a more modern language and it uses ...  the CLI. ie it is byte
>> >coded.
…[5 more quoted lines elided]…
>it is merely enough to show that it doesn't follow 'the norm for C'.

Here's a hack that could theoretically turn OC into a Cobol-to-CIL compiler.

http://gcc-cil.blogspot.com/
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 28)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-12T12:10:00-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<628dd3b4-d6e4-459a-ad11-0254855165f1@v4g2000hsf.googlegroups.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <f84d84fe-b1fc-4bd6-87dc-1a4cf61f435b@l16g2000hsh.googlegroups.com> <vvn1r3hqjka5emudcra591k73crmi9ognc@4ax.com>`

```
On Feb 12, 3:51 pm, Robert <n...@e.mail> wrote:
>
> >There are some Java native code compilers, or should I say were. see
…[7 more quoted lines elided]…
> (GCJ).

On of the noticeable aspects of your 'arguments' is that you seem to
throw in random comments as if they support your viewpoint. It is as
if you grab a Google search but don't bother to read the articles.

What makes you think that "Eclipse Compiler for Java" is relevant to
the list that you think supports your claim of 'the norm for C'
including 'increasingly Java' ?

Eclipse compiler is found in the list of "List of Java bytecode
compilers".

In fact Eclipse does dynamic loading of plug-ins.

"Users can extend its capabilities by installing plug-ins written for
the Eclipse software framework,"

As for "Notably absent ... GNU Compiler for Java (GCJ)" it is not even
absent:

gcj

This is both a source-code-to-bytecode compiler and a native compiler.
See the gcj description on the bytecode compiler page for details.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 29)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-13T00:09:08-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8j05r390ajqk150irh24kkco19m5lerse2@4ax.com>`
- **References:** `<fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <f84d84fe-b1fc-4bd6-87dc-1a4cf61f435b@l16g2000hsh.googlegroups.com> <vvn1r3hqjka5emudcra591k73crmi9ognc@4ax.com> <628dd3b4-d6e4-459a-ad11-0254855165f1@v4g2000hsf.googlegroups.com>`

```
On Tue, 12 Feb 2008 12:10:00 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 12, 3:51 pm, Robert <n...@e.mail> wrote:
>>
…[19 more quoted lines elided]…
>compilers".

I thought ECJ Native Version produced native code. No, it is compiled to native code by
GCJ.
http://packages.debian.org/etch/ecj-bootstrap-gcj 

>In fact Eclipse does dynamic loading of plug-ins.

Eclipse and plug-ins have been compiled to native using GCJ. They kept loads dynamic using
dlopen because of internal complexity.
http://www.linuxjournal.com/article/7413

>"Users can extend its capabilities by installing plug-ins written for
>the Eclipse software framework,"

One of the plugins can be GCJ. When installed, an Eclipse compilation produces a native
executable. Ok, it doesn't turn ECJ into a native compiler, it replaces ECJ with GCJ.
http://gcjbuilder.sourceforge.net/
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 26)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-11T13:08:51-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e107d6c1-9e88-44f0-9be7-ae0de25cdfb2@p69g2000hsa.googlegroups.com>`
- **References:** `<0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com>`

```
On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:


> "We've always done it that way" is a poor reason to retain
> dynamic loading.

I should also point out that, while you have quoted that phrase as if
it was something that I said, it was entirely a reason that you made
up.

I hope that this will help:

http://en.wikipedia.org/wiki/Straw_man
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 27)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-11T21:12:18-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9j32r3h3qd9mt1pvsdlr4lrk50ihi2atl8@4ax.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <e107d6c1-9e88-44f0-9be7-ae0de25cdfb2@p69g2000hsa.googlegroups.com>`

```
On Mon, 11 Feb 2008 13:08:51 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:
>
…[6 more quoted lines elided]…
>up.
 
You said, "And I could even more easil;y just continue to use what has worked
well for me for decades without your unwanted complexifications."
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 28)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-11T21:11:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c274736c-a515-4512-98fd-acd6414a64bc@i29g2000prf.googlegroups.com>`
- **References:** `<lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com> <2438bd38-7328-4f27-b3f9-17a7fd4add32@q77g2000hsh.googlegroups.com> <lqcvq35er05go2391ej4tenk6gh338nono@4ax.com> <e107d6c1-9e88-44f0-9be7-ae0de25cdfb2@p69g2000hsa.googlegroups.com> <9j32r3h3qd9mt1pvsdlr4lrk50ihi2atl8@4ax.com>`

```
On Feb 12, 4:12 pm, Robert <n...@e.mail> wrote:
> On Mon, 11 Feb 2008 13:08:51 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 11, 5:25 pm, Robert <n...@e.mail> wrote:
…[9 more quoted lines elided]…
> well for me for decades without your unwanted complexifications."

That is correct. The reason that I see no need to change is _not_
merely because of your misrepresentation of what I said as "We've
always done it that way" but because it continues to work well, it is
less complex (for me).


Whereas you want me to change for change's sake.

Or perhaps because of "what 'they' think".

Or perhaps because _you_ think it is "ugly".


RW>> one should abide by the norms of that format and culture.

I 'abide by' Cobol's format and culture, and other language's format
and culture when I write in those languages.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 24)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2008-02-10T15:16:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WyErj.10871$Ej5.5151@newssvr29.news.prodigy.net>`
- **References:** `<ie6iq3l4vrbnh5c6f14dj6tuooil8enu00@4ax.com> <448a68cb-6492-47c9-99c1-f6678525675d@e4g2000hsg.googlegroups.com> <0rmkq3p6mjlbeoqlo3pslj40uk9uvkld58@4ax.com> <8f5ebda9-7761-4dd9-8e41-ace915d0b51a@e25g2000prg.googlegroups.com> <lt9nq3trmv01qmh9g4okaipg2443jshfp6@4ax.com> <29a1d043-fe37-4583-838e-1f1725123d87@e4g2000hsg.googlegroups.com> <fftpq35t7ku5ts9ejqaa5eptn3ssjqb4qa@4ax.com> <cd11d9ba-7af0-4386-af6e-e708e9c7089e@i12g2000prf.googlegroups.com> <muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:muusq31uos5jkrmeh5qg5l0o8c40a33nr6@4ax.com...
> It talks as though there are two choices: static and dynamic, early and 
> late binding. It
> seems written 20 years ago. There is now a third choice, controlled 
> dynamic, the one used
> by Unix and Windows.

Late, early, controlled, hybrid.. who the hell cares?

Methinks someone is hung up on the "how," forgetting the true objective is 
the "what."

MCM
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 12)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-06T21:22:03-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ed78c6e8-acd3-430b-8bfe-c81bb379a457@i12g2000prf.googlegroups.com>`
- **References:** `<rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <f24e2aeb-e23b-42ed-b935-66bf3c964224@i72g2000hsd.googlegroups.com> <eqocq3ps2pmcvj9pd0c6tmnetdtrj6p5rt@4ax.com>`

```
On Feb 4, 7:35 pm, Robert <n...@e.mail> wrote:
>
> My mechanism is oriented around data, not programs. If I want to protect month-end figures
…[3 more quoted lines elided]…
> access to programs was obsolete twenty years ago.

It seems that just a couple of years ago you were advocating the
virtues of C-ISAM and Access.  Were you only 16 years obsolete then ?
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 10)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-05T15:19:28-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com>`

```
On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
> On Fri, 1 Feb 2008 12:58:23 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:

> >Actually, to those that use this, it _simplifies_ deployment,
> >especially in bespoke systems where I operate. If a single program
…[7 more quoted lines elided]…
> with other programs.

Yes there is. If you rebuild a library from one changed program and
several unchanged you are still distributing the whole library and
this replaces the one that is currently in use. There may have been an
error in the build. For example one program may have been unavailable
at the time of the build, or omitted in some other way.

It is the _library_ that is to be tested as well as the changed
program, it is necessary to test that the library contains all that it
should, and in the appropriate condition, before causing your
application to fail with a missing program.

You claim 'greater reliability' for libraries and then fail to deliver
reliability to your users.

> Changes in one program can't cause errors in other programs unless they share global data.

Or data in parameters to the CALL of that program or in CALLs that
program makes.

> In a rational environment, data is shared between parent and child, not between siblings
> and certainly not with stranger programs. You should never make a decision in program A,
> store it in an indicator or database, and take action on that decision in program B.
> That's bad design.

What nonsense you talk.  One program can decide that a customer is to
be put on 'stop supply', it stores this indicator in a database.
Another program takes action based on that descision.

> If you DO make that mistake, putting programs A and B in separate files is no more
> protection than putting them in the same library. Even running them on separate machines,
> as remote procedures, is no protection.

Creating straw-man arguments is no support for your assertions.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-06T00:39:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com>`
- **References:** `<rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com>`

```
On Tue, 5 Feb 2008 15:19:28 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
>> On Fri, 1 Feb 2008 12:58:23 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[17 more quoted lines elided]…
>at the time of the build, or omitted in some other way.

If a program is unavailable, the build fails. 

The loader checks again at execution startup time.

>It is the _library_ that is to be tested as well as the changed
>program, it is necessary to test that the library contains all that it
>should, and in the appropriate condition, before causing your
>application to fail with a missing program.

Dynamic loading fails mid-run due to a missing program. That's why it is not normal
practice. 

>> Changes in one program can't cause errors in other programs unless they share global data.
>
>Or data in parameters to the CALL of that program or in CALLs that
>program makes.

That's global data, which is bad practice.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 12)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-06T00:34:14-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e8e12c99-d6e2-4da7-a4cb-23e207c1f1a6@i29g2000prf.googlegroups.com>`
- **References:** `<rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com> <b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com>`

```
On Feb 6, 7:39 pm, Robert <n...@e.mail> wrote:
> On Tue, 5 Feb 2008 15:19:28 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
…[30 more quoted lines elided]…
> practice.

That may be a problem with batch jobs, but for interactive systems it
is merely a slightly reduced functionality which may, or may not, be
important. The user just gets a 'program not available', makes a call
and gets on with other stuff until the problem is fixed. He doesn't
even have to close down, let alone needing to make all the other users
close down too.

I don't know how you manage to make stuff go missing, but it just
doesn't happen to me.

Well actually I can see that if you fail to include a program in the
list to be put in the library (by screwing up the editing), then
overwriting the previous library will make that program fail to be
CALLed, but the startup found the library OK.

But you don't test the libraries so you wouldn't notice that until the
batch run failed halfway through when it tried to CALL what is now
missing.


> >> Changes in one program can't cause errors in other programs unless they share global data.
>
…[3 more quoted lines elided]…
> That's global data, which is bad practice.

Excuse me, but parameters to a CALL are now 'global data' ?

I'll also mention to OO users that 'object data' should not be used
because it is 'global' to the methods.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-06T21:06:55-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7vrkq3psmtrfluttalhinmmpaoq4437997@4ax.com>`
- **References:** `<ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com> <b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com> <e8e12c99-d6e2-4da7-a4cb-23e207c1f1a6@i29g2000prf.googlegroups.com>`

```
On Wed, 6 Feb 2008 00:34:14 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 6, 7:39 pm, Robert <n...@e.mail> wrote:

>I don't know how you manage to make stuff go missing, but it just
>doesn't happen to me.

We frequently build new environments.  Populating them is controlled by component lists,
we don't just cp *.  New files can be missing from the list. Files thought to be obsolete
might still be in use.

>Well actually I can see that if you fail to include a program in the
>list to be put in the library (by screwing up the editing), then
>overwriting the previous library will make that program fail to be
>CALLed, but the startup found the library OK.

Startup doesn't just check for the library's existance, it resolves all externs.

>But you don't test the libraries so you wouldn't notice that until the
>batch run failed halfway through when it tried to CALL what is now
>missing.

We check batch jobs hours BEFORE they are run, by executing ldd. If there is going to be a
problem, we fix it BEFORE the job starts, or change the schedule. The Unix loader checks
again at startup time.

Dynamic loading is the only way a program can fail halfway through. That's why it is not
THE NORM.

>> >> Changes in one program can't cause errors in other programs unless they share global data.
>>
…[5 more quoted lines elided]…
>Excuse me, but parameters to a CALL are now 'global data' ?

If you pass a structure to program A (by reference) and then pass the same structure to
program B, that structure is global data. The scope of the globe may be smaller than other
globes. 

>I'll also mention to OO users that 'object data' should not be used
>because it is 'global' to the methods.

Object data is local to the object instance or class. OO was created to get away from
sharing data between 'programs'. The word is encapsulation.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 14)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-06T20:45:53-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<151a7e05-5943-4cf8-9c64-0d1cf9bffe39@c4g2000hsg.googlegroups.com>`
- **References:** `<ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com> <b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com> <e8e12c99-d6e2-4da7-a4cb-23e207c1f1a6@i29g2000prf.googlegroups.com> <7vrkq3psmtrfluttalhinmmpaoq4437997@4ax.com>`

```
On Feb 7, 4:06 pm, Robert <n...@e.mail> wrote:
> On Wed, 6 Feb 2008 00:34:14 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 6, 7:39 pm, Robert <n...@e.mail> wrote:
…[12 more quoted lines elided]…
> Startup doesn't just check for the library's existance, it resolves all externs.

That requires all CALLs to be CALL literal.

> >But you don't test the libraries so you wouldn't notice that until the
> >batch run failed halfway through when it tried to CALL what is now
> >missing.

> We check batch jobs hours BEFORE they are run, by executing ldd. If there is going to be a
> problem, we fix it BEFORE the job starts, or change the schedule. The Unix loader checks
> again at startup time.

> Dynamic loading is the only way a program can fail halfway through. That's why it is not
> THE NORM.

But my applications don't 'fail'.

If I ran batch programs then I might care about that problem.
Obviously you have set up your runs of ldd because reliability has
been a problem in the past (as you discussed previously), yet you
claim 'more reliable'.

It is only 'as reliable' (because mine have not failed) because you
needed to do more than just make stuff in a library to stop it
failing.


> >> >> Changes in one program can't cause errors in other programs unless they share global data.
>
…[15 more quoted lines elided]…
> sharing data between 'programs'. The word is encapsulation.

And in an application there is usually an 'Application class', the
object of which holds the application object data, or interfaces to
objects holding it, which may need to be accessed by some of the other
objects within the application.

Each object in the application has its own object data which may
correspond to W-S in sub-programs (ie it is encapsulated). Methods in
the objects may use getters and setters to the application data or may
access the application attributes directly via the object pointer
(depending on language).

In fact the way that OO works in Cobol is that the methods are nested
programs and the object data is GLOBAL in the object's W-S (without
the need for the GLOBAL keyword).
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-07T20:55:26-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dtenq3h1ltuioho0561ct05dvoh8q6uhjd@4ax.com>`
- **References:** `<rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com> <b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com> <e8e12c99-d6e2-4da7-a4cb-23e207c1f1a6@i29g2000prf.googlegroups.com> <7vrkq3psmtrfluttalhinmmpaoq4437997@4ax.com> <151a7e05-5943-4cf8-9c64-0d1cf9bffe39@c4g2000hsg.googlegroups.com>`

```
On Wed, 6 Feb 2008 20:45:53 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 7, 4:06 pm, Robert <n...@e.mail> wrote:
>> On Wed, 6 Feb 2008 00:34:14 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[15 more quoted lines elided]…
>That requires all CALLs to be CALL literal.

That's the simplest way. Alternatively, you can list the symbols following -u. After the
first link, you can use the previous generation's symbol  table as an --auxiliary.

>> >But you don't test the libraries so you wouldn't notice that until the
>> >batch run failed halfway through when it tried to CALL what is now
…[14 more quoted lines elided]…
>claim 'more reliable'.

That's like saying locking your door is proof you've been burglarized in the past; I don't
have to lock my door because I've never burglarized. Therefore, my home is more secure
than yours.

>> >> >> Changes in one program can't cause errors in other programs unless they share global data.
>>
…[20 more quoted lines elided]…
>objects within the application.

Only the top program should have update permission on the application class. Others should
read individual fields, not the whole structure, through their individual methods. 

If you pass the whole structure to every program, that structure is global data, which is
anethma to OO principles. 

>Each object in the application has its own object data which may
>correspond to W-S in sub-programs (ie it is encapsulated). Methods in
…[6 more quoted lines elided]…
>the need for the GLOBAL keyword).

I'm not worried about methods of the class, I'm saying methods in other classes shouldn't
be able to see the whole structure, and all setting should be done in one place.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 16)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-07T20:51:50-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19ce2626-c568-4e2e-984a-5b6cbdd467e8@e23g2000prf.googlegroups.com>`
- **References:** `<rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <beb516f3-a38f-4b81-8b6f-213b3216ed9c@n20g2000hsh.googlegroups.com> <p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com> <b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com> <e8e12c99-d6e2-4da7-a4cb-23e207c1f1a6@i29g2000prf.googlegroups.com> <7vrkq3psmtrfluttalhinmmpaoq4437997@4ax.com> <151a7e05-5943-4cf8-9c64-0d1cf9bffe39@c4g2000hsg.googlegroups.com> <dtenq3h1ltuioho0561ct05dvoh8q6uhjd@4ax.com>`

```
On Feb 8, 3:55 pm, Robert <n...@e.mail> wrote:
> On Wed, 6 Feb 2008 20:45:53 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 7, 4:06 pm, Robert <n...@e.mail> wrote:
…[43 more quoted lines elided]…
> than yours.

You analogy is wrong.

You have had problems with missing programs in the past because your
batch jobs fails.

RW>> The problem is jobs aborting because of missing programs.

My applications do not fail should a program be missing, it simply
says that it is unavailable at this time, logs the problem and the
user carries on. Because each program is an individual file a reissue
will either leave a program completely alone, or will overwrite it
with a new one.  That mechanism does not cause a program to 'go
missing'. I can see how a library could do that because it overwrites
a whole collection with another collection. A 'missing' program with
my would only (and has only) occur during system testing because once
issued it will not 'disappear'.


> >> >> >> Changes in one program can't cause errors in other programs unless they share global data.
>
…[25 more quoted lines elided]…
> If you pass the whole structure to every program,

One passes the handle to the object.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 17)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-08T19:33:06-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m10qq3tnu2i2hiqr14sq4ta3ubfq22j3cm@4ax.com>`
- **References:** `<p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com> <b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com> <e8e12c99-d6e2-4da7-a4cb-23e207c1f1a6@i29g2000prf.googlegroups.com> <7vrkq3psmtrfluttalhinmmpaoq4437997@4ax.com> <151a7e05-5943-4cf8-9c64-0d1cf9bffe39@c4g2000hsg.googlegroups.com> <dtenq3h1ltuioho0561ct05dvoh8q6uhjd@4ax.com> <19ce2626-c568-4e2e-984a-5b6cbdd467e8@e23g2000prf.googlegroups.com>`

```
On Thu, 7 Feb 2008 20:51:50 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 8, 3:55 pm, Robert <n...@e.mail> wrote:
>> On Wed, 6 Feb 2008 20:45:53 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:

>> >But my applications don't 'fail'.
>>
…[12 more quoted lines elided]…
>batch jobs fail.

They NEVER fail because of missing libraries. I explained how we prevent that from
happening. 

>
>> >> >> >> Changes in one program can't cause errors in other programs unless they share global data.
…[28 more quoted lines elided]…
>One passes the handle to the object.

You are avoiding the question. If some method returns the entire structure when invoked
with the handle, as I suspect is the case, you've found a way to write old style programs
under color of OO.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 18)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-08T20:13:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<425dace5-8c55-4c57-be08-eaf7899dc149@q21g2000hsa.googlegroups.com>`
- **References:** `<p4v9q39lr667kf84l22uco54baiveseb0k@4ax.com> <7346ddc9-f9ce-4e1d-958c-63299246551d@n20g2000hsh.googlegroups.com> <b4liq3p1lsljonaq3m8in0umj9p5tj9du6@4ax.com> <e8e12c99-d6e2-4da7-a4cb-23e207c1f1a6@i29g2000prf.googlegroups.com> <7vrkq3psmtrfluttalhinmmpaoq4437997@4ax.com> <151a7e05-5943-4cf8-9c64-0d1cf9bffe39@c4g2000hsg.googlegroups.com> <dtenq3h1ltuioho0561ct05dvoh8q6uhjd@4ax.com> <19ce2626-c568-4e2e-984a-5b6cbdd467e8@e23g2000prf.googlegroups.com> <m10qq3tnu2i2hiqr14sq4ta3ubfq22j3cm@4ax.com>`

```
On Feb 9, 2:33 pm, Robert <n...@e.mail> wrote:

> >> If you pass the whole structure to every program,
>
> >One passes the handle to the object.
>
> You are avoiding the question.

There was no question, you were merely pontificating.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 8)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-01T14:46:35-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com>`

```
On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:
> On Thu, 31 Jan 2008 20:41:29 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 1, 4:23 pm, Robert <n...@e.mail> wrote:
…[38 more quoted lines elided]…
> No, I think name calling is insulting.

You leave me mystified, I went back through the message looking for
where I did any "name calling".

I had said that you made statements that were factually wrong, where
you made errors, and that you misunderstood as well as misinformed.

None of that is "name calling".

You seem to use the claim of "ad hominem" or "insults" as a means of
deflecting the very real criticism of your wrong and bad advice.

I am reminded of a self-assessment survey at the company I worked for
some decades ago. It was set by some trick-cyclist and for each
question gave two extreme statements and the employee had to put a
grade of 1 to 5 where 1 was agreeing with the left hand statement and
5 agreed with the right hand.

One of the '1' statements was "Takes criticism of work done as a
personal affront".
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 9)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2008-02-02T12:36:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<60hoo5F1r71s5U1@mid.individual.net>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com>`

```


"Richard" <riplin@azonic.co.nz> wrote in message 
news:5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com...
> On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jan 2008 20:41:29 -0800 (PST), Richard <rip...@azonic.co.nz> 
…[72 more quoted lines elided]…
>
I have followed this thread with interest, and learned a few things.

Maybe the problem here is that you both are experts with in-depth knowledge 
and experience, but it may be in different areas.

Certainly what Richard has outlined matches my understanding (and use of) 
dynamic linkage with Fujitsu, but I claim no expertise whatsoever with Unix 
or derivatives thereof.

If it's any consolation Robert, I haven't issued a COBOL CANCEL for decades, 
on ANY platform, and I haven't seen any for a long time, either.

Nevertheless, different folks use different strokes and there may well be 
places where CANCEL is still used.

I have to admit that my first impulse was also to suggest using INITIAL but 
I stifled it and did some thinking instead :-). I came to the same 
conclusion that Richard did: INITIAL does not meet exactly the same 
requirement as CANCEL

Robert, on this occasion I don't believe Richard was using ad hominem 
attacks; in fact, considering his frustration over what certainly looked 
like "bad" advice, I think he was quite restrained :-)

Given that Richard actually took the trouble to do compiles and tests and 
published the results here, it might have been wise to pay some attention to 
the results...:-)

Having said that, I know that Robert was actually trying to help. Sometimes, 
when we are really close to things the old adage about not seeing the wood 
for the trees can be applied. I couldn't help wondering how much Robert's 
recent immersion and experience with ELF headers and Unix in general, was 
affecting his perception and judgement of what was properly a COBOL problem.

My opinion remains that both of you are extremely valuable people to have in 
this forum :-)

Pete.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 10)_

- **From:** C Goodman <foxgrove@shaw.ca>
- **Date:** 2008-02-02T00:41:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B_Ooj.35971$ow.32802@pd7urf1no>`
- **In-Reply-To:** `<60hoo5F1r71s5U1@mid.individual.net>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <60hoo5F1r71s5U1@mid.individual.net>`

```
Pete Dashwood wrote:
>
Big Snip

> My opinion remains that both of you are extremely valuable people to have in 
> this forum :-)
> 
> Pete.

Well said Pete.

I have found the discussion of great value.  Thanks to all who have 
participated.

The original application was written for mini-computers that have long 
since disappeared.  Much of the code is also written in C.

The application is considered to be of very great value to our clients.

A little background....

The application I am working with has an installed base of hundreds of 
installations.  Almost all are using executables compiled with an old 
version of MicroFucus and are running within an old version of SCO.

We need to modernize to a more recent Unix.  Obvious choice is some 
variety of Linux.  We have experimented with AcuCOBOL and are now 
experimenting with Fujitsu NetCOBOL.  We are keeping a single code base. 
  All programs must compile and function correctly, without source 
changes, on both MF and the new compiler.

---Charlie
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-01T20:41:03-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78l7q31m44hor4t6qo41ld6fc4tt6r7fej@4ax.com>`
- **References:** `<15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <60hoo5F1r71s5U1@mid.individual.net> <B_Ooj.35971$ow.32802@pd7urf1no>`

```
On Sat, 02 Feb 2008 00:41:05 GMT, C Goodman <foxgrove@shaw.ca> wrote:

>Pete Dashwood wrote:
>>
…[24 more quoted lines elided]…
>variety of Linux. 

I concur.

> We have experimented with AcuCOBOL

Bad choice, soon to be obsolete and unsupported.

> and are now 
>experimenting with Fujitsu NetCOBOL. 

That's reasonable. Micro Focus would be a better choice. It is supported on Red Hat and
SuSE.

> We are keeping a single code base. 
>  All programs must compile and function correctly, without source 
>changes, on both MF and the new compiler.

Your clients did not say no source changes; they said modernize. No source changes was
your decision and seems contrary to the project objective of modernizing.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 12)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-03T10:26:16-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ab6c6d44-ed9e-4933-994c-2f62f9463629@c23g2000hsa.googlegroups.com>`
- **References:** `<15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <60hoo5F1r71s5U1@mid.individual.net> <B_Ooj.35971$ow.32802@pd7urf1no> <78l7q31m44hor4t6qo41ld6fc4tt6r7fej@4ax.com>`

```
On Feb 2, 3:41 pm, Robert <n...@e.mail> wrote:
> On Sat, 02 Feb 2008 00:41:05 GMT, C Goodman <foxgr...@shaw.ca> wrote:
> >Pete Dashwood wrote:
…[44 more quoted lines elided]…
> your decision and seems contrary to the project objective of modernizing.

My understanding of what Charles said differs from yours.

It appears to me that no one said "the current source must not be
changed" as you seem to think. The 'single code base' will be the
modernized system and this must not change between being compiled to
run on  the old SCO/old MF and being compiled on the new OS/Compiler.

I do have systems that can be compiled for either MF or Fujitsu, but I
have a pre-process step that changes the comments on a small number of
lines of code that are marked (in columns 1-6) as being specific to
one or the other compiler.

These programs are Web-based or SP2 based for their user interactions
so didn't present a problem that use of ADIS would give.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-04T00:35:09-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u3lcq3tjode3upv4oapb6j3nfmdf0jmls1@4ax.com>`
- **References:** `<a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <60hoo5F1r71s5U1@mid.individual.net> <B_Ooj.35971$ow.32802@pd7urf1no> <78l7q31m44hor4t6qo41ld6fc4tt6r7fej@4ax.com> <ab6c6d44-ed9e-4933-994c-2f62f9463629@c23g2000hsa.googlegroups.com>`

```
On Sun, 3 Feb 2008 10:26:16 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 2, 3:41 pm, Robert <n...@e.mail> wrote:
>> On Sat, 02 Feb 2008 00:41:05 GMT, C Goodman <foxgr...@shaw.ca> wrote:
…[60 more quoted lines elided]…
>so didn't present a problem that use of ADIS would give.

MF offers conditional compilation with syntax close to the '02 standard. Fujitsu does not,
although it will ignore conditional compilation statements (it thinks they are debugging
lines).  Thus, conditional compilation can exclude Fujitsu-specific source code from a MF
compilation, but not to exclude MF-specific code from a Fujitsu compilation.

I think your precompiler approach is a good one. Another would be to put the MF code in
copyboods that are empty during a Fujitsu compilation.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 11)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-01T20:19:59-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<753012a0-457b-4571-9a42-ecfe3149a29f@q21g2000hsa.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <60hoo5F1r71s5U1@mid.individual.net> <B_Ooj.35971$ow.32802@pd7urf1no>`

```
On Feb 2, 1:41 pm, C Goodman <foxgr...@shaw.ca> wrote:
> Pete Dashwood wrote:
>
…[27 more quoted lines elided]…
> changes, on both MF and the new compiler.

Generally it is possible to get the code between Micro Focus and
Fujitsu to be the same, BUT NetCobol for Linux 7 does not have SCREEN
SECTION or any of the X/Open Screen Handling.

If your programs have been using ACCEPT/DISPLAY .. AT or ACCEPT/
DISPLAY FROM/UPON CRT or similar then NetCobol 7 for Linux won't do
that.

It seems that NetCobol 9 for SPARC does have X/Open that will do Micro
Focus style ACCEPT/DISPLAY. It would be nice if Fujitsu did a NetCobol
9 for Linux.

In the meantime Fujitsu on Linux is fine where the front end is
something else, eg: Web Server or SP/2.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 10)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-02T20:31:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<45s9q3d9dsb96dpdv1gb1m2e8kng8b4ag7@4ax.com>`
- **References:** `<15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <60hoo5F1r71s5U1@mid.individual.net>`

```
On Sat, 2 Feb 2008 12:36:36 +1300, "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
wrote:


>I have followed this thread with interest, and learned a few things.
>
>Maybe the problem here is that you both are experts with in-depth knowledge 
>and experience, but it may be in different areas.

We have different approaches to problem solving. An analogy is scientists, who are divided
into theoriticians and experimenters. A theoritician predicts outcomes based on abstract
principles; an experimenter observes outcomes in reality. 

When I want to know what a program is doing, I instinctively read source code. Some of my
colleagues' first approach is to run test cases. I wonder how they WRITE programs. Do they
use a million monkeys generating random code, then find the one that works by eliminating
the ones that don't?

I find it troubling when a programmer regards the program as a black box.  Testers are
supposed to think that way, not programmers. 

>Certainly what Richard has outlined matches my understanding (and use of) 
>dynamic linkage with Fujitsu, but I claim no expertise whatsoever with Unix 
…[3 more quoted lines elided]…
>on ANY platform, and I haven't seen any for a long time, either.

Neither have I. I've only used CANCEL when the machine was short on memory. 

I have long advocated late binding. In VSE days, I wrote my own memory manager to get it
under CICS because IBM's functionality was inadequate. But, when I wanted to replace a
program in memory with a fresh copy, I did it with a system tool, not with a Cobol CANCEL.

>Nevertheless, different folks use different strokes and there may well be 
>places where CANCEL is still used.

Application code shouldn't be managing memory or versioning; that's the domain of systems
software.

>I have to admit that my first impulse was also to suggest using INITIAL but 
>I stifled it and did some thinking instead :-). I came to the same 
>conclusion that Richard did: INITIAL does not meet exactly the same 
>requirement as CANCEL

It seems wrong to use the loader for initialization. I don't use VALUE and often
allocate/initialize working-storage structures at execution time. In OO terms,
working-storage is like making every object static. 

>Robert, on this occasion I don't believe Richard was using ad hominem 
>attacks; in fact, considering his frustration over what certainly looked 
…[4 more quoted lines elided]…
>the results...:-)

I pay attention, but test results do not ALWAYS prove a general rule. In this case, they
reflect a configuration error.

>Having said that, I know that Robert was actually trying to help. Sometimes, 
>when we are really close to things the old adage about not seeing the wood 
>for the trees can be applied. I couldn't help wondering how much Robert's 
>recent immersion and experience with ELF headers and Unix in general, was 
>affecting his perception and judgement of what was properly a COBOL problem.

INITIALIZE is the Cobol way to initialize structures, not CANCEL. Unfortunately, it
doesn't load VALUEs and the '02 option to do so has not been implemented on most
compilers.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 11)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-02T22:45:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8f2ea4e1-a334-454f-a0ec-df1c02433a1e@k2g2000hse.googlegroups.com>`
- **References:** `<15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <60hoo5F1r71s5U1@mid.individual.net> <45s9q3d9dsb96dpdv1gb1m2e8kng8b4ag7@4ax.com>`

```
On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
> On Sat, 2 Feb 2008 12:36:36 +1300, "Pete Dashwood" <dashw...@removethis.enternet.co.nz>
> wrote:
…[8 more quoted lines elided]…
> principles; an experimenter observes outcomes in reality.

If hypotheses are not tested then it is not science.


> When I want to know what a program is doing, I instinctively read source code. Some of my
> colleagues' first approach is to run test cases. I wonder how they WRITE programs. Do they
…[4 more quoted lines elided]…
> supposed to think that way, not programmers.

I find it troubling when a programmer doesn't test.


> >Certainly what Richard has outlined matches my understanding (and use of)
> >dynamic linkage with Fujitsu, but I claim no expertise whatsoever with Unix
…[6 more quoted lines elided]…
>

Exactly, you haven't investigated its other benefits.

> I have long advocated late binding. In VSE days, I wrote my own memory manager to get it
> under CICS because IBM's functionality was inadequate. But, when I wanted to replace a
…[6 more quoted lines elided]…
> software.

When an application framework has been created it is the 'system
software' for the underlying applications and their programs. The
framework can be portable and independent of what system it is running
on.


> >I have to admit that my first impulse was also to suggest using INITIAL but
> >I stifled it and did some thinking instead :-). I came to the same
…[5 more quoted lines elided]…
> working-storage is like making every object static.

In OO Terms Working-Storage is the object attributes and the performed
paragraphs may be the methods (depending on how it is written).


> >Robert, on this occasion I don't believe Richard was using ad hominem
> >attacks; in fact, considering his frustration over what certainly looked
…[17 more quoted lines elided]…
> compilers.

'initializing structures' is another straw-man.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 9)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-02T20:31:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com>`

```
On Fri, 1 Feb 2008 14:46:35 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jan 2008 20:41:29 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[47 more quoted lines elided]…
>None of that is "name calling".

People come here seeking information about Cobol. They don't care about me, you nor any
other individual. If a fact is wrong, in your opinion, state the correct fact, preferably
with substantiation. 

Flaming is disrespectful not only to the target but even more to other readers, because
you're wasting their time.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 10)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-02T21:58:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fb24a783-153c-4097-9d64-1089d056d413@f47g2000hsd.googlegroups.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com>`

```
On Feb 3, 3:31 pm, Robert <n...@e.mail> wrote:
> On Fri, 1 Feb 2008 14:46:35 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 1, 7:49 pm, Robert <n...@e.mail> wrote:
…[52 more quoted lines elided]…
> with substantiation.

And where have I _not_ done that ?

Where is your substantiation for  "insults", "name calling" or, in
fact, where I have not "stated the correct fact _with_
substantiation" ?

> Flaming is disrespectful not only to the target

In what way is saying that you are wrong, and providing the correct
facts, with substantiation, considered to be 'flaming' ?

OK, granted, _you_ call it that, but who else would ?

> but even more to other readers, because
> you're wasting their time.

No, Robert, what _is_ a waste of time is when bad advice is given and
factual inaccuracies are repeated. This is especially a waste of time
when the 'answers' don't even address the problem requirements.
```

###### ↳ ↳ ↳ FW again (was: compile+link Fujitsu Linux

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-02-03T06:08:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4Tcpj.31526$kw6.26930@fe10.news.easynews.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <15a33feb-f988-4e67-9497-3be90ca04da9@i7g2000prf.googlegroups.com> <rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com>`

```
"Robert" <no@e.mail> wrote in message 
news:qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com...
> On Fri, 1 Feb 2008 14:46:35 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:
<snip>
>>None of that is "name calling".
>
…[9 more quoted lines elided]…
>
Robert,
   As you have been told (by some of us) time and time again, it is the way that 
YOU phrase your "facts" that causes so much negative reaction.

I no close to nothing about the topic of linking and searches with specific 
Unix/Linux environments.  However, Richard (may posts ago) indicated that he had 
run tests showing that what he claimed was "true".  In none of your posts since 
then have you indicated that you have run tests showing that your view is 
correct (and that his is wrong).  As someone with little or no knowledge in this 
area, I would tend to BELIEVE the person who had tested his "facts" and provided 
responses that actually reflect the original posters question/environment, 
rather than your (unsupported) facts.
```

###### ↳ ↳ ↳ Re: FW again (was: compile+link Fujitsu Linux

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-03T14:58:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2j8cq3pf881uts747o2pmjpurm3h6mmtr3@4ax.com>`
- **References:** `<rfp2q31j633c95tsmspmt98ju9dno4p4c4@4ax.com> <a7b8bde3-9bc2-43df-bcf2-d1a9a6f944d6@k39g2000hsf.googlegroups.com> <ieu4q3p7dq5s9gln10kv9hb2bt389fgp93@4ax.com> <bd840d49-d33e-4c09-8a7c-c456ff6bc80a@b2g2000hsg.googlegroups.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com> <4Tcpj.31526$kw6.26930@fe10.news.easynews.com>`

```
On Sun, 03 Feb 2008 06:08:00 GMT, "William M. Klein" <wmklein@nospam.netcom.com> wrote:

>"Robert" <no@e.mail> wrote in message 
>news:qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com...
…[25 more quoted lines elided]…
>rather than your (unsupported) facts.

You can read about the topic in chapter 7 of the NETCobol for Linux Users Guide:
http://www.adtools.com/download/v7manuals/NetCOBLinuxUsersGuide.zip

And also in the relevant Linux loader manuals:
http://linux.die.net/man/1/ld  (see -l)
http://linux.die.net/man/3/dlopen

In short, they say both approaches work. They do not say which is Normal Practice in the
Unix world, nor which is 'better'. This is not a question of right and wrong, it's a
question of style. So too is flaming, which disparages a person rather than his statement.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-02-03T07:29:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fo3qh5$rh$1@reader2.panix.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com>`

```
In article <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com>,
Robert  <no@e.mail> wrote:

[snip]

>If a fact is wrong, in your opinion, state the correct fact, preferably
>with substantiation. 

This is fascinating.  Given that a fact is 'a done/made thing' (factum) 
under what circumstances could it be wrong?  To use definitions from 
http://m-w.com : how can 'something that has actual occurrence' have 'the 
state of being mistaken or incorrect'?

'Under conditions called 'one earth normal' and in the absence of opposing 
forces this object was measured as falling with an acceleration caused by 
gravity of 32ft/sec/sec.'

'No, that measurement was mistaken or incorrect.  Here is the correct 
fact:...'

Now... what would 'the correct fact' look like?

DD
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 11)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-03T14:03:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b35cq35fcshvv49jdft98vn0k2viob8mqf@4ax.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <rt95q3lp3lia7q60fciinqejia56or5d9f@4ax.com> <5da53026-0d26-49cf-8951-3b001fa65b84@l32g2000hse.googlegroups.com> <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com> <fo3qh5$rh$1@reader2.panix.com>`

```
On Sun, 3 Feb 2008 07:29:41 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com>,
>Robert  <no@e.mail> wrote:
…[9 more quoted lines elided]…
>state of being mistaken or incorrect'?

A general principle inferred from an anomalous fact is incorrect. For instance, the
assertion  that LD_LIBRARY_PATH is not used to search for called programs is incorrect
99.9% of the time. 

>'Under conditions called 'one earth normal' and in the absence of opposing 
>forces this object was measured as falling with an acceleration caused by 
…[5 more quoted lines elided]…
>Now... what would 'the correct fact' look like?

 At sea level, vt ~= 90 * d**.5, where vt is terminal velocity and d is diameter.  It
shows that a mouse can survive a fall from any height but a human cannot.  Mass is also a
factor. vt ~= mg / b shows that a motorcycle coasts downhill faster than a bicycle (b is
the viscosity of air).
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 12)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-02-04T15:16:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fo7a8h$c1o$1@reader2.panix.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com> <fo3qh5$rh$1@reader2.panix.com> <b35cq35fcshvv49jdft98vn0k2viob8mqf@4ax.com>`

```
In article <b35cq35fcshvv49jdft98vn0k2viob8mqf@4ax.com>,
Robert  <no@e.mail> wrote:
>On Sun, 3 Feb 2008 07:29:41 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[13 more quoted lines elided]…
>A general principle inferred from an anomalous fact is incorrect.

Mr Wagner, your statement - and my question which followed it - are about 
a fact, not a principle or an inference.

DD
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 13)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-04T12:17:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tileq3lh7q6tr6dqk2bekguc46mcmgkrbt@4ax.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <qv6aq3l08m7r14k0jsvpiqf4ftkvi8up9t@4ax.com> <fo3qh5$rh$1@reader2.panix.com> <b35cq35fcshvv49jdft98vn0k2viob8mqf@4ax.com> <fo7a8h$c1o$1@reader2.panix.com>`

```
On Mon, 4 Feb 2008 15:16:33 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <b35cq35fcshvv49jdft98vn0k2viob8mqf@4ax.com>,
>Robert  <no@e.mail> wrote:
…[18 more quoted lines elided]…
>a fact, not a principle or an inference.

It is unclear which fact you are referring to. I stated the fact I was referring to in the
next sentence. "For instance, the assertion  that LD_LIBRARY_PATH is not used to search
for called programs is incorrect 99.9% of the time. "
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 14)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-02-04T19:23:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fo7omv$h1u$1@reader2.panix.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <b35cq35fcshvv49jdft98vn0k2viob8mqf@4ax.com> <fo7a8h$c1o$1@reader2.panix.com> <tileq3lh7q6tr6dqk2bekguc46mcmgkrbt@4ax.com>`

```
In article <tileq3lh7q6tr6dqk2bekguc46mcmgkrbt@4ax.com>,
Robert  <no@e.mail> wrote:
>On Mon, 4 Feb 2008 15:16:33 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[22 more quoted lines elided]…
>It is unclear which fact you are referring to.

I am referring to the fact which is defined as 'a done/made thing' 
('factum' or the result of 'facere').

DD
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 15)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-04T20:27:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<608fq3tn20i0l1erbmnu8iurcvdd856p3n@4ax.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <b35cq35fcshvv49jdft98vn0k2viob8mqf@4ax.com> <fo7a8h$c1o$1@reader2.panix.com> <tileq3lh7q6tr6dqk2bekguc46mcmgkrbt@4ax.com> <fo7omv$h1u$1@reader2.panix.com>`

```
On Mon, 4 Feb 2008 19:23:11 +0000 (UTC), docdwarf@panix.com () wrote:

>In article <tileq3lh7q6tr6dqk2bekguc46mcmgkrbt@4ax.com>,
>Robert  <no@e.mail> wrote:
…[27 more quoted lines elided]…
>('factum' or the result of 'facere').

Your question that followed it was this:


>'Under conditions called 'one earth normal' and in the absence of opposing 
>forces this object was measured as falling with an acceleration caused by 
>gravity of 32ft/sec/sec.'

>'No, that measurement was mistaken or incorrect.  Here is the correct 
>fact:...'

>Now... what would 'the correct fact' look like?

I was told in school that Galileo stood on top of the Tower of Pisa, dropped a cannon ball
and musket ball (bullet), observed they hit the ground at the same time This proved the
acceleration of gravity was invariant to mass. 

Did you believe that?

There are a few problems with the story:

.. The answer is simply wrong. The heavier ball lands first.

.. Galileo never said they landed at the same time; he said the heavier ball lands first.

.. The experiment probably never happened in the way described. Galileo was blind at the
time. Galileo never said it happened, one of his biographers did. Galileo described
similar experiments conducted in a lab decades earlier. Again, he reported the heavier
ball landed first. 

Today I asked  Russian and Yugoslavian colleagues whether they had been taught this fable.
Both said no. The Russian said they had been told that happens in a vacuum. 

The first artificial vacuum was created by Torricelli in 1643, one year after Galileo's
death.

Technically the smaller ball initially pulls ahead because it has a lower coefficient of
drag. When it reaches terminal velocity, the heavier ball passes it. It is well known to
bicycle racers that a heavier rider will pass a lighter one when descending a hill, no
matter how streamlined the lighter one. The difference need be only 10-20 pounds.

That's what a correct fact looks like.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 16)_

- **From:** docdwarf@panix.com ()
- **Date:** 2008-02-05T10:24:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fo9dhh$e5s$1@reader2.panix.com>`
- **References:** `<rcg2q39kisuh6o8oucvif85m6gg9n4pvuo@4ax.com> <tileq3lh7q6tr6dqk2bekguc46mcmgkrbt@4ax.com> <fo7omv$h1u$1@reader2.panix.com> <608fq3tn20i0l1erbmnu8iurcvdd856p3n@4ax.com>`

```
In article <608fq3tn20i0l1erbmnu8iurcvdd856p3n@4ax.com>,
Robert  <no@e.mail> wrote:
>On Mon, 4 Feb 2008 19:23:11 +0000 (UTC), docdwarf@panix.com () wrote:
>
…[49 more quoted lines elided]…
>Did you believe that?

I believe you just stated you were told this, yes... as to what Galileo 
did or said I was not there and I've not read his report on the incident.

I also believe that were Galileo to have done this the condition of 
'absence of opposing forces' would not have been met unless there happened 
to have been a rather... severe atmospheric disturbance at that time.

[snip]

>Today I asked  Russian and Yugoslavian colleagues whether they had been
>taught this fable.
>Both said no. The Russian said they had been told that happens in a vacuum. 

How interesting... this might have something to do with the 'opposing 
force' one might incounter in the resistance caused by a gas.

[snip]

>It is well known to
>bicycle racers that a heavier rider will pass a lighter one when
…[4 more quoted lines elided]…
>That's what a correct fact looks like.

If 'descending a hill' requires contact with said hill... or there is a 
gaseous atmosphere surrounding the riders... then the condition of 
'absence of opposing forces' is not met due to friction; what you've 
posited is an experiment which contains forces to show what a 'correct 
fact' of an experiment that specifies an absence of forces looks like.

'How does an empty jug behave?'

'Well, here's how a full one works.'

DD
```

#### ↳ Re: compile+link Fujitsu Linux

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-30T20:44:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<26b6fd86-05b6-4b71-8acb-8d08b4116d84@y5g2000hsf.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com>`

```
On Jan 31, 12:00 pm, charles.good...@bell.ca wrote:
> I am evaluating Fujitsu NetCOBOL for Linux.
> I am having problems getting CALL/CANCEL to work.
…[40 more quoted lines elided]…
> Aborted

I tried that and it worked fine on my machine.

All it seems to need is the directory where the .so is located to be
on the LS_LIBRARY_PATH

Either add this to the LD_LIBRARY_PATH (eg:

LD_LIBRARY_PATH=./:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH
MYMAIN

or put the .so into one of the directories in that list.

> I am running on Red Hat Enterprise, and Fujitsu support say they will
> only support:
…[5 more quoted lines elided]…
> on less ancient versions of Linux.

I have no problem on Mandrake.
```

#### ↳ Re: compile+link Fujitsu Linux

- **From:** charles.goodman@bell.ca
- **Date:** 2008-01-31T09:48:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<40a8786a-d8db-4ae4-80bc-4813bfd8b155@d21g2000prf.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com>`

```
Thanks for the tips.
Yes I needed to add my curent directory to LD_LIBRARY_PATH
I also nneded to add "-L./" to the cobol command to compile the main
program.
My compile commands, that work are:
cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB1.so MYSUB1.cbl
cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB2.so MYSUB2.cbl
cobol -M -dy -WC,"BINARY(BYTE),DLOAD" -o MYMAIN -L./ -lMYSUB1 -lMYSUB2
MYMAIN.cbl

I am able to compile and execute.  My simple programs are designed to
allow me to see the functioning of CALL and CANCEL.....

However the results is NOT exactly what I want.  Using -l does not
allow for proper functioning of the CANCEL verb (see pg 77 of user's
guide).  Once a subprogram is loaded with a CALL statement, it remains
in memory regardless of CANCEL statements.  The working-storage of the
sub-program is not reinitialized upon a second CALL.

---Charlie
```

##### ↳ ↳ Re: compile+link Fujitsu Linux

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-31T11:14:26-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<78874b11-3136-4835-9629-225088872a78@e6g2000prf.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <40a8786a-d8db-4ae4-80bc-4813bfd8b155@d21g2000prf.googlegroups.com>`

```
On Feb 1, 6:48 am, charles.good...@bell.ca wrote:
> Thanks for the tips.
> Yes I needed to add my curent directory to LD_LIBRARY_PATH
…[15 more quoted lines elided]…
> sub-program is not reinitialized upon a second CALL.

Robert is completely wrong. You do not need a -l or a -L. These will
turn the CALLs into a static load and, as you say, the CANCEL will not
work as expected.

Go back to using your original compiles and links _without_ the -l or -
L.
It was only the LD_LIBRARY_PATH change that was required.

I am not sure how you determined that the CANCEL did not work but I
modified your programs to add a 2nd CALL and a CANCEL followed by a
3nd CALL in MYMAIN and then added a check for 'first time in' into
MYSUB1 and it worked as _I_ expected.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. MYMAIN.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  ACPT    PIC X.
       PROCEDURE DIVISION.
       OPEN-PARA.
           DISPLAY "BEGIN MYMAIN".
           CALL 'MYSUB1'.
           CALL 'MYSUB1'.
           CANCEL 'MYSUB1'.
           CALL 'MYSUB1'.
           DISPLAY "THE END - ACCEPTING ONE BYTE".
           ACCEPT ACPT.
           STOP RUN.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. MYSUB1.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  ACPT    PIC X.
       01  FIRST-IN     PIC X VALUE "Y".
       PROCEDURE DIVISION.
       OPEN-PARA.
           IF FIRST-IN = "Y"
               DISPLAY "First Time In"
           ELSE
               DISPLAY "Been here before"
           END-IF
           MOVE "N"   TO FIRST-IN

           DISPLAY "BEGIN MYSUB1 - ACCEPTING ONE BYTE".
           ACCEPT ACPT.
           EXIT PROGRAM.

As expected I got (ignoring your displays and accepts):

First Time In
Been here before
First Time In

So the CANCEL worked exactly as it should.
```

##### ↳ ↳ Re: compile+link Fujitsu Linux

- **From:** Robert <no@e.mail>
- **Date:** 2008-01-31T21:33:48-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9845q3dkorj3e4hhskj0rm20m5f4qqt1o0@4ax.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <40a8786a-d8db-4ae4-80bc-4813bfd8b155@d21g2000prf.googlegroups.com>`

```
On Thu, 31 Jan 2008 09:48:48 -0800 (PST), charles.goodman@bell.ca wrote:

>Thanks for the tips.
>Yes I needed to add my curent directory to LD_LIBRARY_PATH
>I also nneded to add "-L./" to the cobol command to compile the main
>program.

-L is used to override the user's LD_LIBRARY_PATH. It shouldn't be necessary on your own
machine. 

>My compile commands, that work are:
>cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB1.so MYSUB1.cbl
…[11 more quoted lines elided]…
>sub-program is not reinitialized upon a second CALL.

I answered Richard before reading this reply. Failure of the CANCEL means Fujitsu figured
out the library (.so) had not been dynamically loaded, so did not issue a dlclose(). If
you want the program initialized every time, use the INITIAL clause on PROGRAM-ID.

See my comments to Richard about the disadvantage of hundreds of little libraries.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-01-31T21:02:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<93b174f4-b55e-4af5-b630-f63c99181f49@v67g2000hse.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <40a8786a-d8db-4ae4-80bc-4813bfd8b155@d21g2000prf.googlegroups.com> <9845q3dkorj3e4hhskj0rm20m5f4qqt1o0@4ax.com>`

```
On Feb 1, 4:33 pm, Robert <n...@e.mail> wrote:
> On Thu, 31 Jan 2008 09:48:48 -0800 (PST), charles.good...@bell.ca wrote:
> >Thanks for the tips.
…[5 more quoted lines elided]…
> machine.

Geez, Robert, yet more misinformation. You are _WRONG_ yet again. ld
does _NOT_ follow the LD_LIBRARY_PATH. It follows the LIBPATH. You can
add the current directory to LIBPATH or use the -L _IF_ you want to
link the dynamic libraries statically.

I actually ran a _test_ (you may want to look up what this word might
refer to) by adding the -l MYSUB1 without the -L while having the
LD_LIBRARY_PATH. As I expected it failed, just as Charles reported.



> >My compile commands, that work are:
> >cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB1.so MYSUB1.cbl
…[16 more quoted lines elided]…
> you want the program initialized every time, use the INITIAL clause on PROGRAM-ID.

The INITIAL clause is _also_ BAD and WRONG advice. The INITIAL clause
means that the subprogram is reset on _EVERY_ CALL. It is not a
substitute for CANCEL.

If you want CANCEL to work then don't do stupid stuff like statically
linking a dynamic library. If you want to statically link then do so
with -c on the compile and -o NAME.o then link that.

> See my comments to Richard about the disadvantage of hundreds of little libraries.

The only 'disadvantage' that you could dream up was an entirely
subjective 'it is ugly' and similar.  There are no _actual_
disadvantages and many significant advantages.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 4)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-01T02:13:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<t8j5q3dtb9f9kvlvcpovl54nfv05sq7emp@4ax.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <40a8786a-d8db-4ae4-80bc-4813bfd8b155@d21g2000prf.googlegroups.com> <9845q3dkorj3e4hhskj0rm20m5f4qqt1o0@4ax.com> <93b174f4-b55e-4af5-b630-f63c99181f49@v67g2000hse.googlegroups.com>`

```
On Thu, 31 Jan 2008 21:02:58 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 1, 4:33 pm, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jan 2008 09:48:48 -0800 (PST), charles.good...@bell.ca wrote:
…[15 more quoted lines elided]…
>LD_LIBRARY_PATH. As I expected it failed, just as Charles reported.

In the bad old days, each flavor of Unix had its own name for the library path searched by
ld and dlopen. AIX used LIBPATH (same as z/OS), HPUX used SHLIB_PATH, OS X used
DYLD_LIBRARY_PATH. 

In the late '90s POSIX became the Unix standard. The POSIX  name, LD_LIBRARY_PATH, works
on all versions of Unix. 

For badkward compatibility, the various Unixen merge their old name with LD_LIBRARY_PATH,
eliminating duplicates, and use the result. 

If your test failed, you ran it on an obsolete AIX. Charles reported that LD_LIBRARY_PATH
worked for him. 

>> >My compile commands, that work are:
>> >cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB1.so MYSUB1.cbl
…[23 more quoted lines elided]…
>linking a dynamic library. 

It's not a static link; it's a dynamic program structure. 

>If you want to statically link then do so
>with -c on the compile and -o NAME.o then link that.

That would be turning the clock back 20 years. Some vendors, such as Micro Focus, have
dropped support for static linking.

>> See my comments to Richard about the disadvantage of hundreds of little libraries.
>
>The only 'disadvantage' that you could dream up was an entirely
>subjective 'it is ugly' and similar.  There are no _actual_
>disadvantages and many significant advantages.

User memory management makes it easy to return to MS-DOS. Is that the advantage?
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 5)_

- **From:** Richard <riplin@azonic.co.nz>
- **Date:** 2008-02-01T13:24:40-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c6d6a30e-4d82-4a57-bee4-f2e4865efc76@s12g2000prg.googlegroups.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <40a8786a-d8db-4ae4-80bc-4813bfd8b155@d21g2000prf.googlegroups.com> <9845q3dkorj3e4hhskj0rm20m5f4qqt1o0@4ax.com> <93b174f4-b55e-4af5-b630-f63c99181f49@v67g2000hse.googlegroups.com> <t8j5q3dtb9f9kvlvcpovl54nfv05sq7emp@4ax.com>`

```
On Feb 1, 9:13 pm, Robert <n...@e.mail> wrote:
> On Thu, 31 Jan 2008 21:02:58 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
> >On Feb 1, 4:33 pm, Robert <n...@e.mail> wrote:
…[29 more quoted lines elided]…
> worked for him.

You are confused yet again.

LD_LIBRARY_PATH is used to load dynamic libraries at run time. When
Charles _ran_ MYMAIN originally (with no -l), it failed to find
libMYSUB1.so until its directory was on the LD_LIBRARY_PATH. I
confirmed this with my tests.

When the -l MYSUB1 was added to the compile it failed to find "-
lMYSUB1" _even_with_ the current directory on the LD_LIBRARY_PATH.  My
testing showed this to be the case.  Charles added -L . to get ld to
look in the current directory.

I tested this and found exactly that. In a shell script I changed
LD_LIBRARY_PATH to point to the current directory as :.:./: and
explictly with the full path and ld failed to find MYSUB1.  Adding -
L . (as Charles did) made it work.

ls, as I said, does not use LD_LIBRARY_PATH.

And BTW Mandrake is Red Hat based and not on 'an obsolete AIX'.


> >> >My compile commands, that work are:
> >> >cobol -dy -shared -WC,"BINARY(BYTE)" -o libMYSUB1.so MYSUB1.cbl
…[39 more quoted lines elided]…
> User memory management makes it easy to return to MS-DOS. Is that the advantage?

It is not done for "User memory management", that is why you fail to
understand the advantages.
```

###### ↳ ↳ ↳ Re: compile+link Fujitsu Linux

_(reply depth: 6)_

- **From:** Robert <no@e.mail>
- **Date:** 2008-02-02T20:31:19-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<rm7aq3tu2oamcapm4vrthtpfpjf0uq681o@4ax.com>`
- **References:** `<2e14eba3-4871-42f8-a169-bac736f12960@b2g2000hsg.googlegroups.com> <40a8786a-d8db-4ae4-80bc-4813bfd8b155@d21g2000prf.googlegroups.com> <9845q3dkorj3e4hhskj0rm20m5f4qqt1o0@4ax.com> <93b174f4-b55e-4af5-b630-f63c99181f49@v67g2000hse.googlegroups.com> <t8j5q3dtb9f9kvlvcpovl54nfv05sq7emp@4ax.com> <c6d6a30e-4d82-4a57-bee4-f2e4865efc76@s12g2000prg.googlegroups.com>`

```
On Fri, 1 Feb 2008 13:24:40 -0800 (PST), Richard <riplin@azonic.co.nz> wrote:

>On Feb 1, 9:13 pm, Robert <n...@e.mail> wrote:
>> On Thu, 31 Jan 2008 21:02:58 -0800 (PST), Richard <rip...@azonic.co.nz> wrote:
…[47 more quoted lines elided]…
>L . (as Charles did) made it work.

The general rule is that Unix, both ld and dlopen, searches LD_LIBRARY_PATH. If yours
isn't doing that, there is something abnormal in your configuration.

Do you have an ld configuration file? To find out, run crle or look at /etc/ld.so.conf.

Are you using Linux Security? If so, it will only search secure directories in
LD_LIBRARY_PATH. Your home directory is not one of them.

Did you forget to export or setenv LD_LIBRARY_PATH? If so, ld running as a child process
of your script, doesn't see it.

 Here's a quote from the ld man page:

"The default set of paths searched (without being specified with -L) depends on which
emulation mode ld is using, and in some cases also on how it was configured."

    The linker uses the following search paths to locate required shared libraries: 
    1.

    Any directories specified by -rpath-link options.

    2.

    Any directories specified by -rpath options. The difference between -rpath and
-rpath-link is that directories specified by -rpath options are included in the executable
and used at runtime, whereas the -rpath-link option is only effective at link time.
Searching -rpath in this way is only supported by native linkers and cross linkers which
have been configured with the --with-sysroot option.

    3.

    On an ELF system, if the -rpath and "rpath-link" options were not used, search the
contents of the environment variable "LD_RUN_PATH". It is for the native linker only.

    4.

    On SunOS, if the -rpath option was not used, search any directories specified using -L
options.

    5.

    For a native linker, the contents of the environment variable "LD_LIBRARY_PATH".

    6.

    For a native ELF linker, the directories in "DT_RUNPATH" or "DT_RPATH" of a shared
library are searched for shared libraries needed by it. The "DT_RPATH" entries are ignored
if "DT_RUNPATH" entries exist.

    7.

    The default directories, normally /lib and /usr/lib.

    8.

    For a native linker on an ELF system, if the file /etc/ld.so.conf exists, the list of
directories found in that file. 

http://linux.die.net/man/1/ld

Actually, it's more complicated than that. There 4-6 obscure environment variables that
can 'front end' the search path. They are used to 'overload' system libraries.

>ls, as I said, does not use LD_LIBRARY_PATH.

It should have. Every Unix machine I've ever worked on did.

>And BTW Mandrake is Red Hat based and not on 'an obsolete AIX'.

I suspect you got LIBPATH from this erroneous man page:

If ld is called with any number of occurrences of -L, as
         in:

           ld ... -Lpath1 ... -Lpathn ...

         then the search path ordering is:

           dirlist1 path1 ... pathn dirlist2 LIBPATH
http://compute.cnr.berkeley.edu/cgi-bin/man-cgi?ld+1
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
