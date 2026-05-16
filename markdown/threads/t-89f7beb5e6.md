[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Conversion

_13 messages · 7 participants · 2001-03_

---

### Conversion

- **From:** "G. Feenstra" <gfeenstra@mail.com>
- **Date:** 2001-03-25T17:50:43+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl>`

```
I try to convert a few old cobol programs from Microsoft Cobol Version 1.12
to Fujitsu.
Now I used the "CHAIN" command in the Micorsoft Cobol programs to go from
cobol .exe program to another cobol .exe program passing information thru
the 'Procedure Division chaining ..........'  command.

In Fujitsu there is no "CHAIN" command.

Can anyone tell me how to solve this on a simply manner ?

Thanks.
```

#### ↳ Re: Conversion

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-03-25T17:48:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99l7as$r12$1@news8.svr.pol.co.uk>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl>`

```
Write a control program to CALL the programs you would normally CHAIN.

"G. Feenstra" <gfeenstra@mail.com> wrote in message
news:985536003.6270.0.pluto.d4ee7d82@news.demon.nl...
> I try to convert a few old cobol programs from Microsoft Cobol Version
1.12
> to Fujitsu.
> Now I used the "CHAIN" command in the Micorsoft Cobol programs to go from
…[9 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Conversion

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-03-26T07:30:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<YwHv6.527$aD4.39234@news2.atl>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <99l7as$r12$1@news8.svr.pol.co.uk>`

```
Being sure to immediately CANCEL each one in turn. :-)

    CALL "xxxxx"
    CANCEL "xxxxx"

If you need to make decisions in the modules about which other module
to call next, pass the module a 'signal field'.  For example:

Working-Storage section of calling module:

    01  signal-field    PIC X(?).

Procedure Division of calling module:

    CALL "xxxxx" USING signal-field
    CANCEL "xxxxx"
    IF (signal-field = "???")
        CALL "yyyyy" USING signal-field
        CANCEL "yyyyy"
    ELSE
        CALL "zzzzz" USING signal-field
        CANCEL "zzzzz"
    END-IF

Linkage Section of called module:

    01  signal-field    PIC X(?).

Procedure Division header of called module:

    PROCEDURE DIVISION     USING signal-field.
```

#### ↳ Re: a suggestion

- **From:** Rob LeClaire <RobLec@cinci-rr.com>
- **Date:** 2001-03-25T21:11:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABE1905.DEEC6340@cinci-rr.com>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl>`

```
You might try this:  Write a small program and run it thru the Fujitsu
dialect converter, which is probably on your CD or you can download it
from adtools.com.  See what code the dialect converter substitutes for
your procedure then use that as a guide. 

EG:	Procedure DIvision.
	Begin.
		Call Program "Progname".
		stop run.

"Call Program" is the functional equivalent of CHAIN in ICOBOL, and
Microsoft/Microfocus supports it too thru the $set DG directive, so you
could presumably use either the ICOBOL or Microfocus dialect converter.
```

#### ↳ Re: Conversion

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-03-26T07:15:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABEECA2.E2FBB135@Azonic.co.nz>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl>`

```
G. Feenstra wrote:
> 
> I try to convert a few old cobol programs from Microsoft Cobol Version 1.12
…[7 more quoted lines elided]…
> Can anyone tell me how to solve this on a simply manner ?

Chain was useful for CP/M systems because is completely overwrote memory
leaving the maximum size for the next program.  However, it was
non-standard.  The best way (IMHO) is to have a small base program that
has the interface data in working-storage that calls and cancels each
required program in turn.  Add a Current-Program and Next-Program field
to the interface data so that each program can specify what is to follow
when it EXIT PROGRAMs.  The base program should:

             PERFORM
                 UNTIL Current-Program = "FINISH"

                 CALL Current-Program
                     USING Interface
                 CANCEL Current-Program
                 MOVE Next-Program TO Current-Program
                 MOVE "systmenu"   TO Next-Program
              END-PERFORM
```

##### ↳ ↳ Re: Conversion - a comment

- **From:** Rob LeClaire <RobLec@cinci-rr.com>
- **Date:** 2001-03-25T20:58:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABE15F8.DAC9D41F@cinci-rr.com>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz>`

```


Richard Plinston wrote:
> The best way (IMHO) is to have a small base program that
> has the interface data in working-storage that calls and cancels each
…[11 more quoted lines elided]…
>               END-PERFORM

  If I may make a comment...  I have used this technique on other
platforms (ICOBOL) but had trouble recently attempting to use it with
Microsoft Cobol v3.  A main program calls each "sub" program, passing to
it some parameters as well as the name of the next program for it to
call (usually a return to the main program).  This worked ok in vanilla
DOS and seemed to work ok in Win95's real mode DOS, but it would crash
under Win98 with a stack overflow.  I never figured out exactly why, but
just came up with a different way of getting the job done.

  Please note that in the early days of ICOBOL (I'm talking CS-40 on a
DG Nova), this was the *only* way of moving from program to program. 
And with a 32KB limit on program size, most tasks were broken up into a
number of such small, chained programs.
```

###### ↳ ↳ ↳ Re: Conversion - a comment

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-03-26T12:30:44+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<985567053.1412739851@aklobs.org.nz>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz> <3ABE15F8.DAC9D41F@cinci-rr.com>`

```
On Mon, 26 Mar 2001, Rob LeClaire wrote:
>
>  If I may make a comment...  I have used this technique on other
>platforms (ICOBOL) but had trouble recently attempting to use it with
>Microsoft Cobol v3.  

MS Cobol v3 is fairly old now, 1987 ?

> A main program calls each "sub" program, passing to
> it some parameters as well as the name of the next program for it to
> call (usually a return to the main program).  

What do you mean by 'for it to call' ? Are you saying that each 'sub'  uses a
CALL to get to the next subprogram ?  It should be doing an EXIT PROGRAM to get
back to the main which would then call the next as required.

> This worked ok in vanilla
>DOS and seemed to work ok in Win95's real mode DOS, but it would crash
>under Win98 with a stack overflow.  I never figured out exactly why, but
>just came up with a different way of getting the job done.

MS Cobol v3 on Windows 9x would not surprise me by failing in mysterious ways. 
If, as you indicated, each was calling the next then stack overflow is entirely
possible.

>  Please note that in the early days of ICOBOL (I'm talking CS-40 on a
>DG Nova), this was the *only* way of moving from program to program. 
>And with a 32KB limit on program size, most tasks were broken up into a
>number of such small, chained programs.

I suspect that you are confusing CALL and CHAIN.
```

###### ↳ ↳ ↳ Re: Conversion - a comment

_(reply depth: 4)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-26T04:03:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABEBF6B.222FC949@cinci-rr.com>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz> <3ABE15F8.DAC9D41F@cinci-rr.com> <985567053.1412739851@aklobs.org.nz>`

```

Richard Plinston wrote:
> 
> On Mon, 26 Mar 2001, Rob LeClaire wrote:
…[5 more quoted lines elided]…
> MS Cobol v3 is fairly old now, 1987 ?

Agreed, but I'd perhaps prefer the term 'venerable'.  It has been a very
reliable compiler over the years, and combined with a little assembly,
has in most cases producing highly predictable results.  In addition to
commissioned applications, I have written a number of handy utility
programs which I still use frequently  each day.

Please note that the author of the original post is converting from MS
Cobol v1.12, which even predates Microsoft's repackaged Microfocus
product known as version 3.

> 
> > A main program calls each "sub" program, passing to
…[3 more quoted lines elided]…
> What do you mean by 'for it to call' ? 

Sorry, "Invoke" might have been a better word.  And I should have
referred to "subsequent" programs, not subprograms.

> Are you saying that each 'sub'  uses a
> CALL to get to the next subprogram ?  It should be doing an EXIT PROGRAM to get
> back to the main which would then call the next as required.

Normally a main program would CALL a sub program which would then EXIT
PROGRAM and return to the main calling program (or in some
implementations the verb GOBACK is used).  However, in a CHAINing
methodology, each program completely overwrites the previously executing
module.  In fact, in ICOBOL there was no CALL and no EXIT PROGRAM.  The
verb CALL PROGRAM was the equivalent of CHAIN.

> 
> > This worked ok in vanilla
…[6 more quoted lines elided]…
> possible.

To be honest, this was the first problem I had experienced with code
produced from this compiler.  I suspect that the problem was something I
was not doing properly, as the chaining logic was thrown together
hastily, and when it failed to perform, was abandoned quickly.  Instead,
I have converted these particular modules to Fujitsu COBOL.

> 
> >  Please note that in the early days of ICOBOL (I'm talking CS-40 on a
…[4 more quoted lines elided]…
> I suspect that you are confusing CALL and CHAIN.

Again, "CALL PROGRAM" is the equivalent of CHAIN.  Many implementations
do not support this verb, and I realize that it is non-standard but it
was quite commonly found in small compilers.
 
-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Conversion - a comment

_(reply depth: 5)_

- **From:** Francisco Zelaya <as844@lafn.org>
- **Date:** 2001-03-26T08:19:07-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABF6BFB.D752B5D@lafn.org>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz> <3ABE15F8.DAC9D41F@cinci-rr.com> <985567053.1412739851@aklobs.org.nz> <3ABEBF6B.222FC949@cinci-rr.com>`

```
Hi there,
Very interesting, but I think the original questions was about to invoke two .exe set
of programs instead of calling just objects, which the discussion would apply not so
for .exe type of sets. If somebody has the answer to that would be very helpful.

Regards,

Rob Lec wrote:

> Richard Plinston wrote:
> >
…[68 more quoted lines elided]…
> (To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Conversion - a comment

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-03-30T07:41:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AC438BE.F9BB628F@Azonic.co.nz>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz> <3ABE15F8.DAC9D41F@cinci-rr.com>`

```
Rob LeClaire wrote:
> 
>   If I may make a comment...  I have used this technique on other
…[3 more quoted lines elided]…
> call (usually a return to the main program). 

What do you mean by 'usually' ?  If sub1 is told to call sub2 then how
does sub2 get back to main ?  Does sub2 then call main ?  It should exit
program back to sub1 then sub1 exit program back to main.

> This worked ok in vanilla
> DOS and seemed to work ok in Win95's real mode DOS, but it would crash
> under Win98 with a stack overflow.  I never figured out exactly why, but
> just came up with a different way of getting the job done.

Calling will add to the stack, exit program will subtract from the
stack.  If there are not an equal number of call and exit program then
eventually the stack will overflow.

There is another explanation with MF/MS in that the CALL is by file name
(ie CALL "XYZ" will load file XYZ.xxx where xxx is .INT, .GNT or .EXE or
.DLL) but CANCEL is by PROGRAM-ID.  If XYZ.EXE's Program-id is not "XYZ"
then the CANCEL "XYZ" will not work.  If your Program-IDs do not match
the file name then the numbers of programs in memory may exceed some
internal constraint.
```

###### ↳ ↳ ↳ Re: Conversion - a comment

_(reply depth: 4)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-29T21:38:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AC3AB56.C25787A2@cinci-rr.com>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz> <3ABE15F8.DAC9D41F@cinci-rr.com> <3AC438BE.F9BB628F@Azonic.co.nz>`

```


Richard Plinston wrote:
> 
> Rob LeClaire wrote:
…[10 more quoted lines elided]…
> 

I'm sorry there was so much confusion regarding this post.  I definitely
used the wrong terminology (my mistake).  The original post was about
CHAINing from program to program.  In the ICOBOL implementation, the
verb used to CHAIN is "CALL PROGRAM".  There is no CALL verb (and no
Exit Program either) due to the limited memory available and there is no
mechanism for returning to a calling program.  In other words, EVERY
program is a main program and there are no subprograms.  Please
substitute the term CHAIN where I used CALL, and substitute SUBSEQUENT
PROGRAM for "Sub" program.

The way it works is:

	PROGRAM-ID.  PROGRAM1.
	CALL PROGRAM "PROGRAM2".

	PROGRAM-ID.  PROGRAM2.
	CALL PROGRAM "PROGRAM3".

	PROGRAM-ID.  PROGRAM3.
	CALL PROGRAM "PROGRAM1".


> > This worked ok in vanilla
> > DOS and seemed to work ok in Win95's real mode DOS, but it would crash
> > under Win98 with a stack overflow.  I never figured out exactly why, but
> > just came up with a different way of getting the job done.

The curious thing is why the stack overflow *ONLY* occurs in Win98.

> 
> Calling will add to the stack, exit program will subtract from the
> stack.  If there are not an equal number of call and exit program then
> eventually the stack will overflow.

Again, no CALL was used and no EXIT PROGRAM was used.

> 
> There is another explanation with MF/MS in that the CALL is by file name
…[4 more quoted lines elided]…
> internal constraint.

Good point, and is something to keep in mind, especially for those of us
(like me) who "clone" programs and sometimes forget to change the
internal name.

But in this particular case, each program was compiled as a stand-alone
EXE.  And in the end, I assumed that I had made some erroneous
assumption, as the technique of chaining from program to program was not
the way that Microfocus was intended to be implemented.  

The author of the original post was faced with a similar situation...
that is, converting a system based on CHAINING to a method of CALLng and
RETURNing.  This can be a daunting task, as systems which had been
designed without the call/return constraint may tend to meander about
from one task to another, not necessarily having any main program other
than whatever happened to have been the point of original entry.

-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: Conversion - a comment

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-03-29T19:39:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9a0o4a$nea$1@slb0.atl.mindspring.net>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz> <3ABE15F8.DAC9D41F@cinci-rr.com> <3AC438BE.F9BB628F@Azonic.co.nz> <3AC3AB56.C25787A2@cinci-rr.com>`

```
For those who are reading this thread but are NOT familiar with the "chain"
concept *but* are familiar with CICS,

   CALL is to CHAIN
      as
   EXEC CICS LINK is to EXEC CICS XCTL
     (or even <G>)
   PERFORM is to GO TO

***

I have a *VAGUE* memory that there was discussion EARLY in the revision
process about adding a "CALL but don't return" statement.  I can't remember
why it was not followed up on - but have asked the J4 chair in case he
remembers.
```

###### ↳ ↳ ↳ Re: Exactly!!

_(reply depth: 6)_

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-30T14:12:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AC49430.C07FA65C@cinci-rr.com>`
- **References:** `<985536003.6270.0.pluto.d4ee7d82@news.demon.nl> <3ABEECA2.E2FBB135@Azonic.co.nz> <3ABE15F8.DAC9D41F@cinci-rr.com> <3AC438BE.F9BB628F@Azonic.co.nz> <3AC3AB56.C25787A2@cinci-rr.com> <9a0o4a$nea$1@slb0.atl.mindspring.net>`

```

"William M. Klein" wrote:
> 
>    CALL is to CHAIN
>       as 
>    PERFORM is to GO TO


Excellent analogy!  Thank you.

-------------------------------------------------
(To reply by email change dash to dot in address)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
