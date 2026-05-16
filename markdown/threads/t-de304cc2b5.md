[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Question about functions...and subprograms

_44 messages · 19 participants · 2003-02_

---

### Question about functions...and subprograms

- **From:** yauyau <member23982@dbforums.com>
- **Date:** 2003-02-03T15:23:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2474995.1044285839@dbforums.com>`

```

I am a novice to COBOL and I'm doing an assignment which involves
rewriting a programme in Fortran77 into a COBOL85

However, I have searched a lots of site and documentations, I still
cannot find information on how to self-define a function in COBOL. I dun
know how to declare a user-defined function.  >_<

and also, I get confused because I find 2 versions of declaring
subprogrammes. I DUN KNOW WHAT'S THE DIFFERENCE BETWEEN THEM.

TYPE1:

IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN.
..
PROCEDURE DIVISION.
..
CALL "ABC".
..
STOP RUN.

IDENTIFICATION DIVISION.
PROGRAM-ID.ABC.
..
PROCEDURE DIVISION.
..
EXIT PROGRAM.
-----------------------------------
TYPE2:

IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN.
..
PROCEDURE DIVISION.
..
CALL "ABC".
..
EXIT PROGRAM.

IDENTIFICATION DIVISION.
PROGRAM-ID.ABC.
..
PROCEDURE DIVISION.
..
END-PROGRAM ABC.

END-PROGRAM MAIN.

---------------------------------
THEY ARE VERY SIMILAR.....

may anyone help me?I have already spent a whole day on this problem...
```

#### ↳ Re: Question about functions...and subprograms

- **From:** "Thomas Li" <aizhongli@sprint.ca>
- **Date:** 2003-02-03T13:06:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ehy%9.1497$Wy1.10583@newscontent-01.sprint.ca>`
- **References:** `<2474995.1044285839@dbforums.com>`

```
They are the same in semantics, but the second is better. The first relies
STOP RUN  and EXIT PROGRAM statements to terminate the program, while the
second relies END PROGRAM to terminate the program and it more natural.

You can write as many STOP RUN and EXIT PROGRAM in a program as you need.
But  a END PROGRAM must be paired with a IDENTIFICATION DIVISION.


Thomas Li


yauyau <member23982@dbforums.com> wrote in message
news:2474995.1044285839@dbforums.com...
>
> I am a novice to COBOL and I'm doing an assignment which involves
…[53 more quoted lines elided]…
> Posted via http://dbforums.com
```

##### ↳ ↳ Re: Question about functions...and subprograms

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-04T08:42:01+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1mgnq$4he$1@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <ehy%9.1497$Wy1.10583@newscontent-01.sprint.ca>`

```
Thomas Li wrote:

> They are the same in semantics, 

No they are different.  In the first case they are separate compiles and 
have no connection other than through the CALL statement.  In the second 
case the sub-routine is nested inside main and this makes it private to 
that (though this can be changed) and also data in main can be made 
accessible directly by the nested routine using GLOBAL.

> but the second is better. 

It is only 'better' if that is what you want it to do.  In the first case 
ABC can be sepately compiled and dynamically loadable and can be used by 
other programs independantly of the 'main'.  In the second case the ABC is 
private to main and some other program calling ABC can have a completely 
different routine used, even within the same run unit.

> The first relies
> STOP RUN  and EXIT PROGRAM statements to terminate the program, while the
> second relies END PROGRAM to terminate the program and it more natural.

Nonsense.  STOP RUN always terminates a program, EXIT PROGRAM always exits 
a called routine, and both these actions will occur, as appropriate, when a 
program 'falls off the end' of its source code.  There is no difference at 
all between separate routines and nested programs in this respect.

Note that 'END PROGRAM' is a signal to the compiler of the end of a source 
program.  If 'Type1' is in one source file then it needs an END PROGRAM 
before the second IDENTIFICATION DIVISION header. This is not required if 
the two routines are in their own source files and are presented separately 
to the compiler.

'Relying' on reaching the END PROGRAM or end of source file to exit the 
program is very bad practice regardless of whether it is separate (Type1) 
or nested (Type2).  Later modification may divide the program into 
procedures and this may then 'drop thru' if the necessary EXIT PROGRAM is 
not added.

> You can write as many STOP RUN and EXIT PROGRAM in a program as you need.
> But  a END PROGRAM must be paired with a IDENTIFICATION DIVISION.

An END PROGRAM is only _required_ when there is more than one 
IDENTIFICATION DIVISION in a source file - regardless of whether they are 
nested or not.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2003-02-04T01:21:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1AE%9.3229$go.2231@newssvr16.news.prodigy.com>`
- **References:** `<2474995.1044285839@dbforums.com> <ehy%9.1497$Wy1.10583@newscontent-01.sprint.ca> <b1mgnq$4he$1@aklobs.kc.net.nz>`

```
Be careful when using EXIT PROGRAM.  It behaves like a GOBACK when
encountered in a called program, but behaves like a CONTINUE when not a
called program.  Safer to use GOBACK in all situations.
```

#### ↳ Re: Question about functions...and subprograms

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-03T11:08:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302031108.7ddd7c78@posting.google.com>`
- **References:** `<2474995.1044285839@dbforums.com>`

```
yauyau <member23982@dbforums.com> wrote

> I am a novice to COBOL and I'm doing an assignment which involves
> rewriting a programme in Fortran77 into a COBOL85

Generally Fortran and Cobol are used for quite different applications
and would not translate easily into the other.  OTOH on some older
machines, such as the 1130, Fortran was what they had and business
apps have been written.
 
> However, I have searched a lots of site and documentations, I still
> cannot find information on how to self-define a function in COBOL. I dun
> know how to declare a user-defined function.  >_<

You can't yet.  You may be able to get a sub program to return a value
if your implementation includes 'CALL ... RETURNING ..' and 'EXIT
PROGRAM RETURNING ..'.

This cannot be used inline as Fortran functions can.

> and also, I get confused because I find 2 versions of declaring
> subprogrammes. I DUN KNOW WHAT'S THE DIFFERENCE BETWEEN THEM.
…[18 more quoted lines elided]…
> -----------------------------------

These are separate compiles and are usually in separate source files. 
It is likely that the compiler would produce separate object files
even if the two were in one source file.  They could be linked
together to make one executable or they may be separately linked and
dynamically loaded.  In the latter case the sub-routine 'ABC' may be
called by another program without needing to be compiled again or
linked into it.

> TYPE2:
> 
…[18 more quoted lines elided]…
> ---------------------------------

This is a nested program where one is 'inside' the other.  It will be
in one source file and will produce only one executable. ABC will not
be callable by another program (without changes).  As ABC is 'within'
Main then it can be made to access data within main directly if this
is required using GLOBAL declarations.

> THEY ARE VERY SIMILAR.....

Only superfiscially.
 
> may anyone help me?I have already spent a whole day on this problem...

It is the process of learning, it is continuous and endless.  Welcome
to the first day of the rest of your life   ;-)
```

#### ↳ Re: Question about functions...and subprograms

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-02-03T21:12:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2476675.1044306747@dbforums.com>`
- **References:** `<2474995.1044285839@dbforums.com>`

```

HI, In the first example  there are  2  separate programs

main.cbl   ( the main program)
abc.cbl     ( function or Routine)

all programs you have in your system can use
"ABC"  function  just  use  CALL abc  inside  them
you have to compile and link each one

the second sample

the abc.cbl  doenst exist, they only exist inside the
main program, and only   the main  Program can
use a CALL ABC

you  compile and link  only main.cbl

Carlos  Lages
```

#### ↳ Re: Question about functions...and subprograms

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-03T16:28:46-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<uZ-cnddwOPs9cKOjXTWcjA@giganews.com>`
- **References:** `<2474995.1044285839@dbforums.com>`

```

"yauyau" <member23982@dbforums.com> wrote in message
news:2474995.1044285839@dbforums.com...
>
> I am a novice to COBOL and I'm doing an assignment which involves
…[4 more quoted lines elided]…
> know how to declare a user-defined function.  >_<

You cannot self-define a function in COBOL as is done in FORTRAN and Basic.

The (usual) logical equivalent to a FORTRAN function is "PERFORM
(some-paragraph-name)."

While one of the constructs of the PERFORM command (we call them 'verbs') is
a functional replacement for a DO loop, other constructs include out-of-line
looping and out-of-line computation.
```

#### ↳ Re: Question about functions...and subprograms

- **From:** yauyau <member23982@dbforums.com>
- **Date:** 2003-02-04T14:06:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2479819.1044367578@dbforums.com>`
- **References:** `<2474995.1044285839@dbforums.com>`

```

oh~~~I see. ^^
Thanks for all your replies. I have a better understand of subprogramms
of COBOL now.

If I am going to use the TYPE 2( I guess it's called contained
subprogramms), can I replace all 'END-PROGRAM' in the called programs BY
GOBACK, then only use 'END-PROGRAM MAIN.' in the Main part?
```

##### ↳ ↳ Re: Question about functions...and subprograms

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-04T09:15:58-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1osge$2s33$1@si05.rsvl.unisys.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com>`

```
GOBACK is NOT standard ANSI-1985 COBOL, and it is not available in all
"flavors" of COBOL 85.

Also, GOBACK is analogous to EXIT PROGRAM and STOP RUN in that it is a verb;
END PROGRAM is a marker, not a statement.  And it's END PROGRAM, not
END-PROGRAM.

A STOP RUN will always terminate the run unit.  EXIT PROGRAM is only
meaningful if the program in which it occurs was CALLed, and returns control
to the caller.  GOBACK is sort of a combination of the two, basically "Go
back to where you came from.  That means that if you've been CALLed by
another program, go back to the statement in the caller that immediately
follows the CALL that got you here; if you weren't CALLed, do a STOP RUN."

Personally, I'm not a big fan of GOBACK even in COBOL 2002 (where it *is*
standard).  I believe the same thing can be accomplished in a program, if
you don't know whether it's being executed independently or called, by
coding EXIT PROGRAM followed by STOP RUN.  If it's been CALLed, execution
will follow the EXIT PROGRAM path; if not, the STOP RUN.

Generally a programmer knows whether the program he's writing is going to be
used as a standalone program or as a routine called by some other program.
I prefer the more explicit syntax.

In ANSI-1985 COBOL, according to the standard, the results of "running off
the end of the program" -- attempting to execute the next executable
statement in a program when no next executable statement exists -- are
undefined EXCEPT in the case of a CALLed program, in which case an implicit
EXIT PROGRAM is executed, so any expectation that a standalone program will
do anything particular is vendor-specific.

In the single circumstance in which ANSI-1985 does specify behavior, I'd
still rather see the called program execute an explicit EXIT PROGRAM than
have the caller assume that the called routine has executed such a statement
when what the called routine had actually done is simply fallen off the end
of the program into never-never land (or into an END PROGRAM marker, which
is functionally the same thing) during execution.

        -Chuck Stevens

"yauyau" <member23982@dbforums.com> wrote in message
news:2479819.1044367578@dbforums.com...
>
> oh~~~I see. ^^
…[8 more quoted lines elided]…
> Posted via http://dbforums.com
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-04T12:52:34-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1p266$epl$1@slb5.atl.mindspring.net>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <b1osge$2s33$1@si05.rsvl.unisys.com>`

```
"Chuck Stevens" <charles.stevens@unisys.com> wrote in message
news:b1osge$2s33$1@si05.rsvl.unisys.com...

>
> Personally, I'm not a big fan of GOBACK even in COBOL 2002 (where it *is*
…[4 more quoted lines elided]…
>

Should anyone CARE about "part of the '85 Standard" - just as "GoBack" is
not Standard conforming - so also is it NOT conforming to imediately follow
an "Exit Program" with a "Stop Run" - as the rules of the '85 Standard state
that an "Exit Program" statement must be the last of any "series of
imperative statements".   I think that there are PROBABLY more '85 Standard
compilers that allow this extension than allow GoBack - but both need to be
"flagged as extensions" - when such flagging is in effect for an '85
Standard compiler.  Both are "conforming" in the 2002 Standard.

Personally, I prefer using "GoBack" as (to me - with my IBM background) it
"sounds like" a generic "return me to the invoking entry" statement whether
that is a CALLing program, the operating system (or with the 2002 Standard -
a function or OO invocation).

FYI,
  In a 2002 Standard environment, assuming you use COPY statements for
procedural code, you would probably need to code:

   Exit Program
   Exit Function
   Exit Method
   Stop Run

to "guarantee" the same results as:
  GoBack

This is a NON-issue if you don't use COPY statements for procedural code, as
you would always know what type of entity you were executing by the
paragraph in the Identification Division.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 4)_

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-04T15:02:01-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZXU%9.1908$qQ.623165@news20.bellglobal.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <b1osge$2s33$1@si05.rsvl.unisys.com> <b1p266$epl$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b1p266$epl$1@slb5.atl.mindspring.net...
> FYI,
>   In a 2002 Standard environment, assuming you use COPY statements for
…[9 more quoted lines elided]…
>

And that's why I like the entry point statement allowed by some vendors;
this allows me to use "alternative" entry points in a program that I can
then call from anywhere using a normal call statement.  To get out of the
entry point I need an exit program only.  This way I can create
"subroutines" and, instead of putting them in copybooks I add them all as
entry points into a "utilities" program with many entry points.

Thank you for this!

Calin, TORONTO
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 5)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-04T14:51:35-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LFednYMKUoI5td2jXTWckw@giganews.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <b1osge$2s33$1@si05.rsvl.unisys.com> <b1p266$epl$1@slb5.atl.mindspring.net> <ZXU%9.1908$qQ.623165@news20.bellglobal.com>`

```

"Calin @ Work" <dontemailme@work.com>
>
> And that's why I like the entry point statement allowed by some vendors;
…[4 more quoted lines elided]…
> entry points into a "utilities" program with many entry points.

In that configuration, I "think" you'd be money ahead to end each entry
group with a GO TO QUIT, where QUIT is a paragraph with only GOBACK or EXIT
PROGRAM, viz:

ENTRY "A".
...
GO TO QUIT.
ENTRY "B".
...
GO TO QUIT.

QUIT.
    GOBACK.

Once upon a time, it turned out the above construct was faster and smaller
than having multiple GOBACKs. Your milage may vary.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 6)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-05T11:23:10+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1peh5$o1p$1@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <b1p266$epl$1@slb5.atl.mindspring.net> <ZXU%9.1908$qQ.623165@news20.bellglobal.com> <LFednYMKUoI5td2jXTWckw@giganews.com>`

```
JerryMouse wrote:

> In that configuration, I "think" you'd be money ahead to end each entry
> group with a GO TO QUIT, where QUIT is a paragraph with only GOBACK or
…[13 more quoted lines elided]…
> than having multiple GOBACKs. Your milage may vary.

So you save a couple of millisecs a year and a couple of bytes in an effort 
to make your program ugly and bug-prone.  How many hours of machine time 
did you waste to determine this ?

Note also that 'ENTRY' is _not_ a paragraph or section label.  The ENTRY 
"A" does not terminate the paragraph that is above it.  If that paragraph 
is performed then the ENTRY "A" will not terminate the PERFORM and the code 
after the ENTRY will be within the PERFORM scope - including the GO TO QUIT 
- resulting in incorrect operation of the program.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-02-04T18:34:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<aVSdnXxpDOumwd2jXTWcjw@giganews.com>`
- **References:** `<2474995.1044285839@dbforums.com> <b1p266$epl$1@slb5.atl.mindspring.net> <ZXU%9.1908$qQ.623165@news20.bellglobal.com> <LFednYMKUoI5td2jXTWckw@giganews.com> <b1peh5$o1p$1@aklobs.kc.net.nz>`

```

"Richard Plinston" <riplin@Azonic.co.nz> wrote in message
news:b1peh5$o1p$1@aklobs.kc.net.nz...
> JerryMouse wrote:
>
…[14 more quoted lines elided]…
> > Once upon a time, it turned out the above construct was faster and
smaller
> > than having multiple GOBACKs. Your milage may vary.
>
> So you save a couple of millisecs a year and a couple of bytes in an
effort
> to make your program ugly and bug-prone.  How many hours of machine time
> did you waste to determine this ?

I said "once upon a time!" The time was in the '60s on a 360-30 with 64K of
memory. The 32 bytes of code on each GOBACK was very expensive compared to
the 8 bytes a GO TO generated.

>
> Note also that 'ENTRY' is _not_ a paragraph or section label.  The ENTRY
> "A" does not terminate the paragraph that is above it.  If that paragraph
> is performed then the ENTRY "A" will not terminate the PERFORM and the
code
> after the ENTRY will be within the PERFORM scope - including the GO TO
QUIT
> - resulting in incorrect operation of the program.

Here's a flash, slick: Any abnormal exit from a perform or, for that matter,
any logic flaw can result in the incorrect operation of a program. Even user
error has been known to cause problems.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 8)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-05T14:14:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1poj5$tl0$1@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <LFednYMKUoI5td2jXTWckw@giganews.com> <b1peh5$o1p$1@aklobs.kc.net.nz> <aVSdnXxpDOumwd2jXTWcjw@giganews.com>`

```
JerryMouse wrote:

>> > In that configuration, I "think" you'd be money ahead to end each entry
>> > group with a GO TO QUIT, where QUIT is a paragraph with only GOBACK or
>> > EXIT PROGRAM, viz:

> I said "once upon a time!" The time was in the '60s on a 360-30 with 64K
> of memory. The 32 bytes of code on each GOBACK was very expensive compared
> to the 8 bytes a GO TO generated.

Well exactly, which is why your advocacy of using it today (in your "you'd 
be money ahead to ..") is entirely obsolete.


> Here's a flash, slick: Any abnormal exit from a perform or, for that
> matter, any logic flaw can result in the incorrect operation of a program.
> Even user error has been known to cause problems.

Which is exactly why I raised the issue.  In the code you posted it would 
be advisable to include paragraph or section labels immediately prior to 
each ENTRY statement to protect against such problems.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 6)_

- **From:** "Calin @ Work" <dontemailme@work.com>
- **Date:** 2003-02-04T17:43:10-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0jX%9.2574$CF1.619703@news20.bellglobal.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <b1osge$2s33$1@si05.rsvl.unisys.com> <b1p266$epl$1@slb5.atl.mindspring.net> <ZXU%9.1908$qQ.623165@news20.bellglobal.com> <LFednYMKUoI5td2jXTWckw@giganews.com>`

```
I would still use exit program, even for clarity purposes only, let alone
falling through into a paragraph from an entry.  Plus... go to?  That old
ugly dude that was teaching COBOL some years ago was adamant about
structured programming, it would be a shame to disapoint him now :-)

Calin, TORONTO


"JerryMouse" <nospam@bisusa.com> wrote in message
news:LFednYMKUoI5td2jXTWckw@giganews.com...
>
> "Calin @ Work" <dontemailme@work.com>
…[3 more quoted lines elided]…
> > then call from anywhere using a normal call statement.  To get out of
the
> > entry point I need an exit program only.  This way I can create
> > "subroutines" and, instead of putting them in copybooks I add them all
as
> > entry points into a "utilities" program with many entry points.
>
> In that configuration, I "think" you'd be money ahead to end each entry
> group with a GO TO QUIT, where QUIT is a paragraph with only GOBACK or
EXIT
> PROGRAM, viz:
>
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 4)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-04T12:35:39-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1p86s$2n4$1@si05.rsvl.unisys.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <b1osge$2s33$1@si05.rsvl.unisys.com> <b1p266$epl$1@slb5.atl.mindspring.net>`

```
"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b1p266$epl$1@slb5.atl.mindspring.net...

> Should anyone CARE about "part of the '85 Standard" - just as "GoBack" is
> not Standard conforming - so also is it NOT conforming to imediately
follow
> an "Exit Program" with a "Stop Run" - as the rules of the '85 Standard
state
> that an "Exit Program" statement must be the last of any "series of
> imperative statements".

I'm pretty sure you're thinking of Syntax Rule 1 of the Exit Program
statement in ANSI X3.23-1985, found on page X-33: "If an EXIT PROGRAM
statement appears in a consecutive sequence of imperative statements within
a sentence, it must appear as the last statement in that sequence."

This contrasts markedly (in my opinion) with Page VI-88, 6.14, THE EXIT
STATEMENT, Syntax Rule 1:  "The EXIT statement must appear only in a
sentence by itself and comprise the only sentence in the paragraph."

Thus, it seems to me that there's no problem with a sequence like " ... EXIT
PROGRAM.  STOP RUN ... ".  It's only when you drop the period in the middle
that it becomes non-conforming code.

<< I /think that there are PROBABLY more '85 Standard
> compilers that allow this extension than allow GoBack - but both need to
be
> "flagged as extensions" - when such flagging is in effect for an '85
> Standard compiler.>>

So long as "EXIT PROGRAM" and "STOP RUN" have a separator period between
them -- so that the former occurs at the end of a SENTENCE -- there is no
need to flag the sequence.  I believe it's conforming.   And any program
that allows the sequence WITHOUT the period is non-portable to
implementations that haven't included the extension that allows it.  GOBACK,
if it is allowed at all, should be identified as a vendor-specific extension
to the 1985 standard.

<<Both are "conforming" in the 2002 Standard.>>

Yes, GOBACK is introduced, and the subject syntactic restriction on EXIT
PROGRAM relaxed, in the 2002 standard.

> Personally, I prefer using "GoBack" as (to me - with my IBM background) it
> "sounds like" a generic "return me to the invoking entry" statement
whether
> that is a CALLing program, the operating system (or with the 2002
Standard -
> a function or OO invocation).

The subject is COBOL85, according to the first entry in this thread, and at
no point has the original author given any indication of any particular
platform, much less an IBM one.  There are lots of COBOL extensions I like
using, too, but since they're non-standard I'm hesitant to imply that every
meaningful implementation of ANSI-1985 COBOL includes them!

> FYI,
>   In a 2002 Standard environment, assuming you use COPY statements for
…[10 more quoted lines elided]…
> This is a NON-issue if you don't use COPY statements for procedural code,
as
> you would always know what type of entity you were executing by the
> paragraph in the Identification Division.

There are cases in which it's a non-issue even when you're NOT using COPY
for procedural code.  Offhand I know of no prohibition in the standard
against calling an object code program using IPC when that object code
program is also executable independent of any run unit, so EXIT PROGRAM STOP
RUN can have meaning even without COPY.  You are correct in that GoBack
would have the same result as Exit Program Stop Run in standard COBOL 2002
for such a program.

But it IS indeed an issue if you ARE using COPY for procedural code among
various sorts of Procedure Divisions.  EXIT METHOD may only appear in a
METHOD Procedure Division; EXIT FUNCTION may only appear in a FUNCTION
Procedure Division (Page 447, 14.8.13.2, EXIT statement, SR8 and 9), so the
first sequence you suggest as what you would need to code in COBOL 2002
explicitly violates the syntax rules in any context in which it might
appear, and your suggestion that "you would probably need to code" it that
way would not end up being a particularly productive approach.  GOBACK is
the only real alternative for this fragment in that context.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-05T21:57:53+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1p5vq$jba$1@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <b1osge$2s33$1@si05.rsvl.unisys.com> <b1p266$epl$1@slb5.atl.mindspring.net>`

```
William M. Klein wrote:

> This is a NON-issue if you don't use COPY statements for procedural code,

It is a non-issue, not only if you don't use COPY, but also if you don't 
use any of the EXIT * or a STOP RUN in COPY, or if the COPY for a 
subroutine is not used in a MAIN and vv.

If other words it is a non-issue.

> as you would always know what type of entity you were executing by the
> paragraph in the Identification Division.

Exactly.  I _always_ know whether I am coding a main (I only have a very 
few) or a called program.  For a start my main's don't have LINKAGE and all 
my called programs do.  If a called program, with LINKAGE SECTION, is run 
as a main then it will crash and burn because there is no call parameters 
long before it gets to EXIT PROGRAM.
```

##### ↳ ↳ Re: Question about functions...and subprograms

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-02-04T12:47:55-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0302041247.49d6776a@posting.google.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com>`

```
yauyau <member23982@dbforums.com> wrote in message news:<2479819.1044367578@dbforums.com>...
> oh~~~I see. ^^
> Thanks for all your replies. I have a better understand of subprogramms
…[4 more quoted lines elided]…
> GOBACK, then only use 'END-PROGRAM MAIN.' in the Main part?

END PROGRAM (no '-') and GOBACK/STOP RUN/EXIT PROGRAM are quite
different things and do not replace each other.  The answer is no.

END PROGRAM indicates the end of the source code for that program. 
STOP RUN/GOBACK/etc indicates the end of the execution of a sequence
of operations.

It just happens that if the program 'falls off' the end of its source
code, beyond the end of the last paragraph, then it acts as if a
GOBACK had been coded there, regardless of whether this is a nested
program or not.  If your program is only _single_ paragraph then it
will fall off the end.  If your program is several paragraphs (so that
you can use out of line PERFORM, then falling off the end by dropping
thru the paragraphs is not a good idea.
END PROGRAM is required for nested programs to indicate where the
source code ends. GOBACK/STOP RUN/EXIT PROGRAM is required to indicate
where the execution ends.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-04T13:54:29-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1pcql$5r4$1@si05.rsvl.unisys.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0302041247.49d6776a@posting.google.com...
> It just happens that if the program 'falls off' the end of its source
> code, beyond the end of the last paragraph, then it acts as if a
> GOBACK had been coded there, regardless of whether this is a nested
> program or not.  ...

Not necessarily.  The '85 standard ONLY defines this for a CALLED program,
not for the "main" program.  The 2002 standard is the one that specifies an
implicit GOBACK.  Personally, I think falling off the end of a program
without having indicated what to do is bad style, and would recommend
explicitly doing SOMEthing.

> END PROGRAM is required for nested programs to indicate where the
> source code ends. GOBACK/STOP RUN/EXIT PROGRAM is required to indicate
> where the execution ends.

Yes; the distinction is precisely between where the COMPILER stops compiling
the PROGRAM, and where the PROGRAM stops EXECUTING (and either returns
control to the caller -- GOBACK and the flavors of EXIT -- or takes down the
entire run unit -- STOP RUN).  Two entirely different concepts.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-05T11:59:45+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1pglp$p4q$1@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:

>> It just happens that if the program 'falls off' the end of its source
>> code, beyond the end of the last paragraph, then it acts as if a
…[4 more quoted lines elided]…
> not for the "main" program.  

According to Don Nelson in "COBOL 85 for Programmers":

"In COBOL 85 an implicit STOP RUN is executed if you fall out of the bottom 
of the main program of a run unit.  In COBOL 74 this situation was 
undefined."

I won't argue with Don about this.

> Personally, I think falling off the end of a program
> without having indicated what to do is bad style, and would recommend
> explicitly doing SOMEthing.

Falling off the end of a program implies that it is trivial code that is 
just one paragraph, or that it has a bug and has lost control.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-04T17:15:05-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1phie$9m9$1@slb5.atl.mindspring.net>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz>`

```
Richard,
  I don't usually argue with that book of Don Nelson's as it was/is an
EXCELLENT user's "guide" to COBOL '85.  However, here is the exact text from
the '85 Standard's "undefined language" list - that explains the rule (or
lack thereof),

"(1) Explicit and implicit transfers of control. When there is no next
executable statement and control is not transferred outside the COBOL
program, the program flow of control is undefined unless the program
execution is in the nondeclarative procedures portion of a program under
control of a CALL statement, in which case an implicit EXIT PROGRAM
statement is executed. (See 4.4.2 on page IV-25.)"
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 6)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-04T16:02:06-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1pk9u$aj5$1@si05.rsvl.unisys.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net>`

```

"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b1phie$9m9$1@slb5.atl.mindspring.net...
> Richard,
>   I don't usually argue with that book of Don Nelson's as it was/is an
> EXCELLENT user's "guide" to COBOL '85.  However, here is the exact text
from
> the '85 Standard's "undefined language" list - that explains the rule (or
> lack thereof),
…[6 more quoted lines elided]…
> statement is executed. (See 4.4.2 on page IV-25.)"

I agree, Bill, and was about to respond with text from the other citation
(actually from page IV-26).

Note that a given implementation MAY WELL have treated "main programs" in
this regard as if they had been executed under control of a CALL and thus do
an implicit GOBACK (as the 2002 standard requires).  The compiler
implementor may also have chosen to generate a Halt and Catch Fire opcode at
this point in the program to prevent undetected early exits.

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 7)_

- **From:** Steve Thompson <s_thompson#NO#SPAM_@ix.netcom.com>
- **Date:** 2003-02-04T23:34:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E40945E.7BB66D41@ix.netcom.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com>`

```
Chuck Stevens wrote:
<snip>
> Note that a given implementation MAY WELL have treated "main programs" in
> this regard as if they had been executed under control of a CALL and thus do
> an implicit GOBACK (as the 2002 standard requires).  The compiler
> implementor may also have chosen to generate a Halt and Catch Fire opcode at
> this point in the program to prevent undetected early exits.
<snip>

Personally, I like the "Back Space and Punch Operator"
instruction myself. Then there is that old, "Read Backward,
Write Forward and Shread Tape" (generally seen used on the
IBM Data Cell, aka Noodle snatcher) instruction.

Were these to be implemented for when you fall out the
bottom of a program, I'd bet the next night they got run in
batch production, they'd get fixed.
```

###### ↳ ↳ ↳ Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 8)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-02-05T09:06:39-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E410C5F.9D1A358F@istar.ca>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com>`

```
On the old RCA 301, if you had one of their drum printers, you could
code a 2 instruction sequence that would literally print and blow
fuses.  It was space fill the print translate table followed by print. 
We also manually corrected parity errors on tape by reading the
offending block in with alarm inhibit off.  

Steve Thompson wrote:
> 
> Chuck Stevens wrote:
…[25 more quoted lines elided]…
> attorney's fees) for collecting this fee.
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 9)_

- **From:** robert@wagner.net (Robert Wagner)
- **Date:** 2003-02-07T01:11:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e42fec1.97068695@news.optonline.net>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com> <3E410C5F.9D1A358F@istar.ca>`

```
The RCA 301 an April Fool joke. It had a disk drive made by Wurlitzer which
functioned exactly like a juke box. It selected a disk from a rack and put it on
a turntable, from which you could read it. It had a three-speed card reader. You
had to up-shift to get to higher speeds and down-shift when nearing the end (you
knew because operator inserted card saying end is near). On tape error, it
stopped and a red light came on. The human operator was expected to correct the
block in memory (how?) or move the current instruction pointer back to
re-execute the read. 

The best joke, though, was how you mounted and dismounted tapes. It had a
hook-and-eye system which did not work. Operators would routinely use scissors
to dismount a tape and splicing tape to mount one. 

It was a CADET (can't add, doesn't even try) which kept its arithmetic table in
unprotected memory. Changing he table made arithmetical instuctions function
incorrectly. What a slap on the knee!

Bring back the good old days.

"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:

>On the old RCA 301, if you had one of their drum printers, you could
>code a 2 instruction sequence that would literally print and blow
…[9 more quoted lines elided]…
>> > this regard as if they had been executed under control of a CALL and thus
do
>> > an implicit GOBACK (as the 2002 standard requires).  The compiler
>> > implementor may also have chosen to generate a Halt and Catch Fire opcode
at
>> > this point in the program to prevent undetected early exits.
>> <snip>
…[18 more quoted lines elided]…
>> attorney's fees) for collecting this fee.
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 10)_

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-07T07:40:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302070740.3f76014d@posting.google.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com> <3E410C5F.9D1A358F@istar.ca> <3e42fec1.97068695@news.optonline.net>`

```
robert@wagner.net (Robert Wagner) wrote in message news:<3e42fec1.97068695@news.optonline.net>...
<snip>
> It had a three-speed card reader. You
> had to up-shift to get to higher speeds and 
> down-shift when nearing the end (you knew
> because operator inserted card saying end is near). 

Did they call those repent cards???
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 11)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-07T11:05:44-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E440388.20900@Sympatico.ca>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com> <3E410C5F.9D1A358F@istar.ca> <3e42fec1.97068695@news.optonline.net> <dcedb8d0.0302070740.3f76014d@posting.google.com>`

```

Joe Zitzelberger wrote:
> robert@wagner.net (Robert Wagner) wrote in message news:<3e42fec1.97068695@news.optonline.net>...
> <snip>
…[7 more quoted lines elided]…
> Did they call those repent cards???

The holy cards of yesteryear ...

Donald
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-02-07T12:36:57-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b20qrp$2pk$1@panix1.panix.com>`
- **References:** `<2474995.1044285839@dbforums.com> <3e42fec1.97068695@news.optonline.net> <dcedb8d0.0302070740.3f76014d@posting.google.com> <3E440388.20900@Sympatico.ca>`

```
In article <3E440388.20900@Sympatico.ca>,
Donald Tees  <Donald_Tees@Sympatico.ca> wrote:
>
>Joe Zitzelberger wrote:
…[11 more quoted lines elided]…
>The holy cards of yesteryear ...

Ahhhhh, for the Oldene Dayse... when a card could have sanctity such as 
*ten* cards cannot, today!

DD
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 13)_

- **From:** Pat Hall <phall@certcoinc.com>
- **Date:** 2003-02-07T11:57:22-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E43F382.376EE592@certcoinc.com>`
- **References:** `<2474995.1044285839@dbforums.com> <3e42fec1.97068695@news.optonline.net> <dcedb8d0.0302070740.3f76014d@posting.google.com> <3E440388.20900@Sympatico.ca> <b20qrp$2pk$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:

> In article <3E440388.20900@Sympatico.ca>,
> Donald Tees  <Donald_Tees@Sympatico.ca> wrote:
…[18 more quoted lines elided]…
> DD

Hey I still got about 10 cases (100,000) of these "blessed" cards in the back room.  I've got grocery
lists for life<G>

PatH
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 14)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-02-09T05:32:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E45E7DE.3060607@optonline.NOSPAM.net>`
- **References:** `<2474995.1044285839@dbforums.com> <3e42fec1.97068695@news.optonline.net> <dcedb8d0.0302070740.3f76014d@posting.google.com> <3E440388.20900@Sympatico.ca> <b20qrp$2pk$1@panix1.panix.com> <3E43F382.376EE592@certcoinc.com>`

```
Pat Hall wrote:
> 
> docdwarf@panix.com wrote:
…[24 more quoted lines elided]…
> lists for life<G>

The 5081's are still unmatched as note paper. You're a lucky guy.
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 9)_

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2003-02-07T23:59:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E449CC5.CCF0E6C7@mb.sympatico.ca>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com> <3E410C5F.9D1A358F@istar.ca>`

```
"Clark F. Morris, Jr." wrote:

> On the old RCA 301, if you had one of their drum printers, you could
> code a 2 instruction sequence that would literally print and blow
…[3 more quoted lines elided]…
>

Honeywell had one called "rewind the printer"!

PL
```

###### ↳ ↳ ↳ Re: Odd instructions was Re: Question about functions...and subprograms

_(reply depth: 10)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-02-08T10:10:54-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E45482E.7030600@Sympatico.ca>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com> <3E410C5F.9D1A358F@istar.ca> <3E449CC5.CCF0E6C7@mb.sympatico.ca>`

```
Peter Lacey wrote:
> "Clark F. Morris, Jr." wrote:
> 
…[12 more quoted lines elided]…
> 
Reminds me of a bug in the CYBER-64 OS that drove me nuts
for about two days as a young beginner in the trade.  A batch
mode set of JCL was required to make two cpies of a disk
file, and while the first one worked fine, the second absolutely
refused to work.  After two days of experiments, I discovered
you had to rewind the disk before you do the second copy
statement.

Donald
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-05T09:40:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1ri9v$1kk3$1@si05.rsvl.unisys.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com>`

```
"Steve Thompson" <s_thompson#NO#SPAM_@ix.netcom.com> wrote in message
news:3E40945E.7BB66D41@ix.netcom.com...

> Personally, I like the "Back Space and Punch Operator"
> instruction myself. Then there is that old, "Read Backward,
> Write Forward and Shread Tape" (generally seen used on the
> IBM Data Cell, aka Noodle snatcher) instruction.

Oh, my.  Somebody else with experience with the Data Cell.  My first job out
of college was as a computer operator at a federal bureaucracy site that had
three of these.   This was in the days of DOS Release 23 and OS/MFT, which
were the two main operating systems we ran at the time.  In their infinite
wisdom the systems analysts decided this was an ideal machine for a
large-scale high-activity batch run using ISAM.  Three bins held the keys,
the other seven the data.  When we finally went into production on this
application, by the end of the month we had yet to complete the first day's
processing.  As quickly as they were able they replaced each of the data
cell drives with two 2314 disk pack arrays.  During the couple of years I
was there I don't think we went a week without at least one strip crash.


> Were these to be implemented for when you fall out the
> bottom of a program, I'd bet the next night they got run in
> batch production, they'd get fixed.

True enough.  And I have some experience there.

The control logic for PERFORM in Unisys MCP/AS COBOL dialects involves
placing a PCW and a literal on the stack when doing the PERFORM; the literal
identifies the end of the PERFORM range, and the PCW points to the return
point.  If the programmer does the no-no of branching around the end of the
PERFORM range, the most likely ultimate result is falling out the end of the
program.  COBOL(68) and COBOL74 generated an NVLD instruction, whose sole
purpose was to cause the program to crash with an "INVALID OPERATOR" fault,
and the most likely scenario in which one would see such a failure is that
the programmer branched out of a PERFORM.  Our COBOL users have gotten used
to this "safety net".  For reasons of consistency, COBOL85 took a slightly
different approach and generates what amounts to a GOBACK; the result is
that a program which would encounter a DS-or-DP condition in COBOL74 or
COBOL(68) goes to a normal (if early) EOT when compiled with COBOL85.  As a
result, users who want the behavior from COBOL85 that they've come to know
and love over the last few decades from earlier dialects have to take the
extra step of putting their own "suicide code" at the end of the source..

So what the older dialects of COBOL do on Unisys MCP/AS systems is not too
far from generating "Halt and Catch Fire".

    -Chuck Stevens
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 8)_

- **From:** "Chuck Stevens" <charles.stevens@unisys.com>
- **Date:** 2003-02-05T12:37:02-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1rsle$1rmp$1@si05.rsvl.unisys.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com>`

```
Another Data Cell query:

"Steve Thompson" <s_thompson#NO#SPAM_@ix.netcom.com> wrote in message
news:3E40945E.7BB66D41@ix.netcom.com...

> Then there is that old, "Read Backward,
> Write Forward and Shread Tape" (generally seen used on the
> IBM Data Cell, aka Noodle snatcher) instruction.

My recollection was that reading and writing were done in the same
direction, which of course was the same direction as snatching the strip.
The snatch operation, in my experience, was rarely the problem, as I recall
it.  The hope that reversing the drum and allowing air currents and momentum
to hurl the magnetic strip back into place without getting pleated might
have been a bit less than reasonable.  Seems to me NCR's aptly-named CRAM
device may have been a predecessor, and was arguably a better design in that
it didn't try to CRAM the strip back in the exact location whence it came!

Wasn't the model number of the Data Cell Drive 2321?

    -Chuck Stevens
```

###### ↳ ↳ ↳ Data Cells -- Was: Question about functions...and subprograms

_(reply depth: 9)_

- **From:** "William Bub" <fathafluff@hotmail.com>
- **Date:** 2003-02-06T02:10:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6uj0a.59113$iK4.21985@twister.nyroc.rr.com>`
- **References:** `<2474995.1044285839@dbforums.com> <2479819.1044367578@dbforums.com> <217e491a.0302041247.49d6776a@posting.google.com> <b1pcql$5r4$1@si05.rsvl.unisys.com> <b1pglp$p4q$1@aklobs.kc.net.nz> <b1phie$9m9$1@slb5.atl.mindspring.net> <b1pk9u$aj5$1@si05.rsvl.unisys.com> <3E40945E.7BB66D41@ix.netcom.com> <b1rsle$1rmp$1@si05.rsvl.unisys.com>`

```
>
> Wasn't the model number of the Data Cell Drive 2321?
>
Absolutely.

In my first career I used to service 2321's for IBM. New York DMV had 8 of
them. They were cool to watch. I remember, there were seven "nevers" in
servicing them. It was easy to do something in the wrong order, and a very
powerful torsion spring could destroy most of the picker mechanism. Anyone
remember Bib Bin Cylinder Cylinder Head Head?

In my second career (5 years now) I program in COBOL.
```

#### ↳ Re: Question about functions...and subprograms

- **From:** Carlos lages <member129@dbforums.com>
- **Date:** 2003-02-04T14:28:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2479877.1044368886@dbforums.com>`
- **References:** `<2474995.1044285839@dbforums.com>`

```

If you decide  to use Type  2
you dont need  END PROGRAM

just  use  CALL  "ABC"
               CANCEL  "ABC"

do release  ABC from memory

Carlos  lages
```

##### ↳ ↳ Re: Question about functions...and subprograms

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-05T22:30:56+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1p7tp$kfj$1@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <2479877.1044368886@dbforums.com>`

```
Carlos lages wrote:


> If you decide  to use Type  2

'Type2' is nested programs.  

> you dont need  END PROGRAM

Nested programs _do_ require the END PROGRAM.

> just  use  CALL  "ABC"
>                CANCEL  "ABC"
> 
> do release  ABC from memory

Nested programs do not get released from memory when CANCELed.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-04T14:46:45-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1p8rn$ijg$1@slb9.atl.mindspring.net>`
- **References:** `<2474995.1044285839@dbforums.com> <2479877.1044368886@dbforums.com> <b1p7tp$kfj$1@aklobs.kc.net.nz>`

```
Releasing memory for *ANY* program when a CANCEL is done is "implementor
defined" and work differently from compiler to compiler - and even for the
same compiler under different operating system.

What CANCEL  is "guaranteed" to do (in an ANSI conforming environment) is to
place the program in "initial state" rather than last-used state - the next
time it is called.  How a compiler vendor does this is totally up to them.
Many (but certainly NOT ALL) do "release" the storage of that program.  This
includes (for some - not all vendors) releasing the Working-Storage of a
nested program.  It *never* releases the storage of EXTERNAL data (again in
an ANSI conforming environment).

To give readers an idea of the "variables" I will talk briefly about IBM
mainframe environments.

1) Using STATIC calls (as they define it) is explicitly NOT ANSI
conforming - and a CANCEL of a subprogram does *not* put it in initial state
(the next time it is called) and does not free storage.

2) Using DYNAMIC calls (defined as ANSI conforming) does release storage and
does put it in initial state the next time it is called.

3) CANCEL of an "entry-point" (extension)  has its own rules and they do
have variations.

4) CANCEL after both CALL "literal" and CALL identifier "pointing to" a
nested program work the same (as I recall - I am not positive of this) and
*do* release Working-Storage of the nested program.

  ***

Bottom-Line:
  Do *not* confuse "CANCEL" with a generic "storage management system".   If
freeing storage is important to you (your application) find out how YOUR
vendor handles it and whether CANCEL (or some other "freemain" facility)
exists and can be used by an application programmer.  If getting a program
into "initial state" is important, then look at the "IS INITIAL" attribute
on the Program-ID paragraph *and* at the CANCEL statement.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

_(reply depth: 4)_

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-05T11:16:07+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1pe3u$ns8$1@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <2479877.1044368886@dbforums.com> <b1p7tp$kfj$1@aklobs.kc.net.nz> <b1p8rn$ijg$1@slb9.atl.mindspring.net>`

```
William M. Klein wrote:

> Releasing memory for *ANY* program when a CANCEL is done is "implementor
> defined" and work differently from compiler to compiler - and even for the
> same compiler under different operating system.

and even for the same compiler and operating system but different linking 
mechanism.

> Many (but certainly NOT ALL) do "release" the storage of that program. 

Maybe, but a nested program is not 'released from memory' in the same way 
that it could be if it was a dynaically loaded separate program.  Carlos 
was making a distinction between 'Type 1' separate compilation and 'Type2' 
nested and got this aspect the wrong way around.

With separate compilation it can be (given appropriate compiling and 
linking) that the whole sub-program is released from memory, it can be 
reloaded for the next CALL by loading its executable file.

With a nested program it is usual for the code to just be another set of 
segments in the nesting program, this means that it could not be reloaded 
by itself and therefore cannot be entirely released from memory because if 
it was a subsequent CALL would fail.

Actually he got both things he said the wrong way around.
```

#### ↳ Re: Question about functions...and subprograms

- **From:** yauyau <member23982@dbforums.com>
- **Date:** 2003-02-04T14:40:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2480042.1044369600@dbforums.com>`
- **References:** `<2474995.1044285839@dbforums.com>`

```

I see.^^
Thanks you.
```

#### ↳ Re: Question about functions...and subprograms

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-04T11:00:04-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302041100.a18dfc5@posting.google.com>`
- **References:** `<2474995.1044285839@dbforums.com>`

```
yauyau <member23982@dbforums.com> wrote in message news:<2474995.1044285839@dbforums.com>...
> I am a novice to COBOL and I'm doing an assignment which involves
> rewriting a programme in Fortran77 into a COBOL85
…[6 more quoted lines elided]…
> subprogrammes. I DUN KNOW WHAT'S THE DIFFERENCE BETWEEN THEM.

There are two ways to do functions in Cobol.  But neither will provide
you with a "function", but you will be able to get the same effect.

The lightweight style of function is the out-of-line "perform".  It
has full access to all program storage and resources, takes no
arguments and returns no results except modifying global storage.  It
is quite easy to write, e.g:


Function Def --->   Calc-Age-In-Days.
                         Compute WS-Age = WS-Today - WS-Some-Date
Hard To See Period -->   .

Anywhere in your program you can now say:

Function Call --->  Perform Calc-Age-In-Days
 
and know that WS-Age will be populated afterwards.


The heavyweight style of function is your Type-2 example.  Something
called a nested program.   It is identical in most respects to a
separate program (your Type-1) but the compiler will roll it into the
main program at compile time for you.  To continue the simple example
from above:


IDENTIFICATION DIVISION.
PROGRAM-ID. MAIN.
..
PROCEDURE DIVISION.
..
CALL "Calc-Age-In-Days" using WS-Today WS-Some-Date WS-Age.
..
EXIT PROGRAM.

IDENTIFICATION DIVISION.
PROGRAM-ID.Calc-Age-In-Days.
..
PROCEDURE DIVISION using Local-First-Date Local-Last-Date Result-Age.
     Compute Result-Age = Local-First-Date - Local-Last-Date
	Goback.
END-PROGRAM Calc-Age-In-Days.


This usage isolates your function from having global access to the
main programs storage and allows you to have a well defined parameter
list.

It is worth noting that you could take the above nested program and
make it a totally separate program and still call it in the identical
manner.


Mostly it is a judgement call on the part of the programmer.  I
usually use the following rules:


    - If only one program needs it AND it is simple, make it a
paragraph and perform it.

    - If you need to perform the same operation on several different
data items make it a nested subprogram.  This will allow you to write
and test the logic in a single place, making your overall workload
smaller.

    - If only one program needs it AND it is complex, make it a nested
subprogram.  This protects the storage of the main program from side
effects.  It also allows you to write and test it separately and plug
it in.

    - If more than one program will need it then it should be a
separate (type-1) program or COPYed into the using programs as a
nested program.  The COPY to nested program can be used to improve
speed but otherwise should not alter usage.  There are some simple
rules that you should follow if you do use the second form.  Make sure
that all of your source units have an "END PROGRAM pgmname.", while
not required you will not easily be able to include separate programs
with a copy statement if you don't have them.  Also, speaking only for
the IBM mainframes, STOP RUN wrecks the entire environment when
executed -- use GOBACK instead.


Finally there is a CALL/RETURNING style that lets you specify your
output parameters, it is similar to the above example where the last
argument is actually the return value, but you actually specify the
return value on the call statement and the procedure division
statement.


Hope this helped.

Joe Zitzelberger
```

##### ↳ ↳ Re: Question about functions...and subprograms

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-02-05T22:02:50+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b1p692$jba$2@aklobs.kc.net.nz>`
- **References:** `<2474995.1044285839@dbforums.com> <dcedb8d0.0302041100.a18dfc5@posting.google.com>`

```
Joe Zitzelberger wrote:

> There are two ways to do functions in Cobol.  But neither will provide
> you with a "function", but you will be able to get the same effect.

They are not 'functions' but are 'procedures' and do not give the same 
effect.

In Fortran, C, Pascal, and may others a 'function' will supply a value that 
is used within an expression.  In Cobol there are intrinsic functions which 
are functions but you cannot write your own with '85 compilers.
```

###### ↳ ↳ ↳ Re: Question about functions...and subprograms

- **From:** jzitzelb@tsys.com (Joe Zitzelberger)
- **Date:** 2003-02-05T08:59:52-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dcedb8d0.0302050859.1184e6b9@posting.google.com>`
- **References:** `<2474995.1044285839@dbforums.com> <dcedb8d0.0302041100.a18dfc5@posting.google.com> <b1p692$jba$2@aklobs.kc.net.nz>`

```
Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<b1p692$jba$2@aklobs.kc.net.nz>...
> Joe Zitzelberger wrote:
> 
…[8 more quoted lines elided]…
> are functions but you cannot write your own with '85 compilers.


Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<b1p692$jba$2@aklobs.kc.net.nz>...
> Joe Zitzelberger wrote:
> 
…[8 more quoted lines elided]…
> are functions but you cannot write your own with '85 compilers.

I'm reminded of the old joke about a helicopter pilot lost in a
Seattle fog.

He flies up to a building and writes up a sign that says "Where Am
I?".  Several people in the building quickly hold a white board up to
a window that says "You are in a helicopter."

The pilot then flies to the airport without delay.

Once safely on the ground the confused customer asks the pilot how
that answer helped the pilot, who explained that the answer, while
being technically correct, was less than useless to the user.

Thus, the pilot knew he was at the Micro$oft campus.


I could have said "You can't do user defined functions" and been
technically correct.  But Yauyau was asking how to convert another
into Cobol.

However, the useful answer is "You use Cobol subprograms to fit the
same problem space as functions and procedures from other languages. 
Since you cannot simulate the functions or procedures of other
languages with Cobol functions.  You must fall back to subprograms,
possibly with an output parameter or the returning style to simulate a
function, or with nothing to simulate a procedure.  The programmer in
all cases is responsible for recovering the subprogram (function)
result and using it in a meaningful way."

In this case the terminology is unfortunate.  If Cobol had
user-defined functions widely available yet, then they would indeed be
a fine solution for converting a Fortran program.  But most likely
Yauyau will need to convert those functions into some form of called
subprogram, or inline them  In this case it does no good to say Cobol
'functions' are different.  What is being asked is 'how do I make
Cobol behave like Fortran functions?'
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
