[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Static vs Dynamic Linking

_10 messages · 8 participants · 2000-05_

---

### Re: Static vs Dynamic Linking

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-05-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3910C3C0.87ED0DBD@istar.ca>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com>`

```
The suggestion below probably worked well pre Language Environment but
would be a disaster in LE.  For those on the COBOL newsgroup who will be
just joining the discussion, LE is the set of run-time routines for
COBOL, C/C++, PL/I and possibly others that is used by current
compilers.  The use of CALL data-name in COBOL which generates a dynamic
call when the routine is not compiled with the program (COBOL II and
later allows nested programs).  This is faster than EXEC CICS LINK.  The
COBOL programmers guide will tell you how to do it.  One thing that I
found when testing the utility date routine I wrote is that there is a
slight but noticeable overhead for dynamically called modules versus
nested program call.  This would make sense because the compiler can do
some serious
optimization.  Incidentally this overhead is roughly proportional to the
number of calls where the first call loads the routine and it stays in
memory until canceled.

The date subroutine program source mentioned earlier was COPY DATERTN
where DATERTN was the entire sub-routine from PROGRAM-ID to END PROGRAM
statement.  It took advantage of COBOL allowing nested COPY statements. 
Any main program that was to use it as a nested program would have "COPY
DATERTN." as the next to last statement and END PROGRAM
main-program-name as the last statement.  Interestingly enough, if
DATERTN was used as a nested program, the CALL dataname statement where
dataname was defined as "PIC X(8) VALUE 'DATERTN'" used the nested
program and did not cause a load of the separately compiled module.

Clark Morris, CFM Technical Programming Services Inc.,
cfmtech@istar.ca    

"Craddock, Chris" wrote:
> 
> Good points Skip.
…[28 more quoted lines elided]…
> send email to listserv@bama.ua.edu with the message: GET IBM-MAIN INFO
```

#### ↳ Re: Static vs Dynamic Linking

- **From:** Daniel Jacot <djacot@my-deja.com>
- **Date:** 2000-05-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8er7gq$3j0$1@nnrp1.deja.com>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca>`

```
In article <3910C3C0.87ED0DBD@istar.ca>,
  "Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:
> The suggestion below probably worked well pre Language Environment but
> would be a disaster in LE.  For those on the COBOL newsgroup who will
> be just joining the discussion, LE is the set of run-time routines for
> COBOL, C/C++, PL/I and possibly others that is used by current
> compilers

<snip a lot>

> >
> > If application folks are prepared to write a little asm glue code,
…[10 more quoted lines elided]…
> >

No, it is not a desaster in LE. It works fine with COBOL, PL/I and C
as long you do not use DLLs (BTW, does anybody in the world use DLL
linkage?). My shop uses such a 'glue' since decades and we migrated to
LE 3 years ago.
Until now, there were only 3 restrictions with PL/I (no CONTROLLED, no
EXTERNAL, no direct QSAM file-IO).
We are running into troubles now with Visual Age PL/I since this
language uses some sort of DLL linkage. Instead of the LOAD macro and
pure ASSEMBLER, we will have to use LE enabled ASM and CEEFETCH.

Another issue: Chris mentioned IMS transactions that may load modules
via LOAD macro. That's fine as long as you DELETE them at the end of the
transaction, otherwise they remain in memory and the region will abend
in a few minutes due to lack of storage. The 'glue' he mentioned has to
DELETE the modules, but how does the glue know about the end ot the
transaction? There is no 'normal end' exit in IMS, so you have to code a
'terminate' call in every main program.
```

#### ↳ Re: Static vs Dynamic Linking

- **From:** epluta@radiks.net (Ed Pluta)
- **Date:** 2000-05-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391257e3.504741000@news.radiks.net>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca>`

```
On Wed, 03 May 2000 21:26:40 -0300, "Clark F. Morris, Jr."
<cfmtech@istar.ca> wrote:

>The suggestion below probably worked well pre Language Environment but
>would be a disaster in LE.  For those on the COBOL newsgroup who will be
…[23 more quoted lines elided]…
>
Why In the world would you use a static called date routine in a
production environment and force yourself to recompile your whole
system instead of one dynamically called program. Maybe our shop is an
exception but we have thousands of programs calling a date routine
that is dynamically linked written in BAL (Basic Assembly Language).
Something to do with Y2K compliance;)

>Clark Morris, CFM Technical Programming Services Inc.,
>cfmtech@istar.ca    
…[5 more quoted lines elided]…
>> > I agree with others who feel that dynamic linking is best,
Ditto
>> > but there may be battles to fight to get there.
>> 
…[5 more quoted lines elided]…
>> blew out their response time objectives.
This is not true If your are talking about CICS on MVS/ESA. If your
programs are defined in the CSD with resident(yes) [Systems Definition
Guide, pg 59]  they will only be loaded the first time they are needed
then just a logical call is needed. (Probably a lookup in a data table
and a BASR.) After that (all programs are truly reentrant, right) you
should not have many problems, provided your regions are sized right
and you have a machine capable of handling your workload. We do this
for litterally milllions of transactions a day with a less than three
second response time and many are processed sub-second.

Talk to your CICS gods.
>> 
>> If application folks are prepared to write a little asm glue code, they can
…[6 more quoted lines elided]…
>>
If you want to get a little goofy (about 6 bud lts) try this:
Define a user-maintained data table with an eight byte key, followed
by a fullword. When the table is loaded it contains all the programs
that will could possibly execute in a region followed by a fullword of
binary zeros. 
Step two, write a small, fully reentrant, amode(31), rmode(24),
utility program, in assembler of course, to read and update this
table. When you need a link call this program with a parmlist of
program you want to call followed by the actual parmlist for the
program. (This could be implemented via macros.) Once the utility is
called all it will do is a read on the table via the eight byte
program name/parm passed (table key) then see if there is an address.
If there is one it will simply reset R1 accordingly then BASR there
and go on its merry way. If not it will load the program and update
the table with the loaded address and proceed as above.

This will allow all programs in a region to execute the same reentrant
programs without the constant load/ deletes, massive load modules or
large quantity of recompiles.

Because this is a data table it is an incredibly fast read, all in
core. Also this method should only require the program to be loaded
only once. This method would allow over 4200 programs, averaging 12k,
to be loaded at the same time into 50M. Not including CICS tables
working storage areas or any other system areas. I think the above
method is sounding preferable. 
If any one actully tries this let me know I would be greatly
interested in knowing how it turns (helping) out.
>> This sort of thing is trivial to do, but I guess most application folks
>> would freak out if you suggested it. "Oh well". If they feel more
>> comfortable linking everything into one gonzo module I guess there's no
>> saving them.
>
Dynamic linking supports the "object oriented" way of thinking, so I
can't see how people get away with static linking (sarcasim highly
intened ;l) ) 
>> Chris
>> 
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Static vs Dynamic Linking

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 2000-05-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39138CDB.A0650EE6@worldnet.att.net>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca> <391257e3.504741000@news.radiks.net>`

```
Ed Pluta wrote:
> 
(honking snip)
> >>
> This will allow all programs in a region to execute the same reentrant
> programs without the constant load/ deletes, massive load modules or
> large quantity of recompiles.

I don't know if this is DOS info or stale info, but it's not the case in
CICS/ESA & later. The first LOAD/LINK/XCTL brings the program into
memory (almost said "core" <g>). Subsequent LOAD/LINK/XCTL's do NOT
bring in another copy, but simply get the address of the program from
the PPT & do what's been asked. Programs are subject to being deleted
from memory if CICS goes into program compression, but I haven't seen
this happen since we moved to CICS/ESA 3.1 years ago. The Monitor's
stats for LOADs & LINKs showed zero time when it tabulated where the
task waited (too small to matter on modern CPU's). You can safely forget
any ASM code & UMT's, it works fine.

Whatever you do, please don't link CICS programs with static calls
(except for the CICS stub, of course).

Bill Lynch

(I know that a program may be reloaded under certain conditions,
refresh?; but in general it's not a real world concern)
```

##### ↳ ↳ Re: Static vs Dynamic Linking

- **From:** Charles F Hankel <noos@hankel.freedombird.net>
- **Date:** 2000-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.137e0837e5bf3ead98972d@news.freedombird.net>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca> <391257e3.504741000@news.radiks.net>`

```
I noticed that Ed Pluta as epluta@radiks.net said...

> Why In the world would you use a static called date routine in a
> production environment and force yourself to recompile your whole
…[3 more quoted lines elided]…
> Something to do with Y2K compliance;)

Much the same question came to my mind as well, especially as I wrote a 
couple of this type of date routine nearly thirty years ago, and that 
are still in use today because they were Y2K compliant way back when I 
spread fingers to hand punch buttons.
```

###### ↳ ↳ ↳ Re: Static vs Dynamic Linking

- **From:** frlsfly@aol.com (FRLSFLY)
- **Date:** 2000-05-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000507154351.02281.00001623@ng-fx1.aol.com>`
- **References:** `<MPG.137e0837e5bf3ead98972d@news.freedombird.net>`

```
I think that most arguments about dynamic linking are actually about code
re-use.  

Shared Run-time libraries are very effective in implementing basic atomic
functions that are truely global to an operating system or application, (like
deciding what day it is).
 
Utility functions of that type can be built with very clear and stupid
interfaces, and should be dynamically called or linked.  

The problem is that these are, in my experience, a relatively small number of
functions.  One reason Microsoft apps go into "DLL Hell" is because MSFT do not
clearly delineate between Operating system functions and application functions,
and overuse the concept. 

Using large numbers of shared DLLs means that you cannot actually test and
install a module and say that it can be counted on to perform reliably.  The
next generation of DLL installed could blow it sky-high.  

I think user-level dynamically linked shared code should be used sparingly, and
only after a great deal of thought and discussion. 


>I noticed that Ed Pluta as epluta@radiks.net said...
>
…[13 more quoted lines elided]…
>Charles F Hankel


Nathan Meyer
Berkeley, CA
"Big Endian" is what I like.
```

##### ↳ ↳ Nested Program vs Dynamic was Re: Static vs Dynamic Linking

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2000-05-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391B5200.F6A0CBAB@istar.ca>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca> <391257e3.504741000@news.radiks.net>`

```
The date routine was done that way to minimize overhead in a high volume
environment.  Any changes to the output of the date routine other than
bug correction (and there was one, a change to the spelling of July in
French), would require changes to the input thus the caller would have
to be recompiled anyway.  The nested program is faster than a static
link which is what would be used in CICS programs for CALL 'datertn' as
opposed to CALL DATE-ROUTINE-NAME where DATE-ROUTINE-NAME is PIC X(8)
VALUE 'datertn'.  The CALL DATE-ROUTINE-NAME is normally a dynamic load
at run-time unless 'datertn' has been compiled as a nested program
within the caller.  This latter exception boggled my mind when I
discovered it during testing.
 
Analysis is needed for what a routine is doing, the costs of the dynamic
overhead both initial and per CALL execution, and the maintenance
tradeoffs. There is no one right answer.  In the case of the date
routine usage at the shop where I wrote it and put it into production,
90+ percent of the usage is via dynamic call.  The batch standard is
dynamic call except where required by subsystems.  

Clark Morris, CFM Technical Programming Services Inc.,
cfmtech@istar.ca     

Ed Pluta wrote:
> 
> On Wed, 03 May 2000 21:26:40 -0300, "Clark F. Morris, Jr."
…[113 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Nested Program vs Dynamic was Re: Static vs Dynamic Linking

- **From:** epluta@radiks.net (Ed Pluta)
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391bb6e7.6781000@news.radiks.net>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca> <391257e3.504741000@news.radiks.net> <391B5200.F6A0CBAB@istar.ca>`

```
On Thu, 11 May 2000 21:36:16 -0300, "Clark F. Morris, Jr."
<cfmtech@istar.ca> wrote:

>The date routine was done that way to minimize overhead in a high volume
>environment.
We process tens of millions of trans per day and still dynamic link
between all programs.
 Any changes to the output of the date routine other than
>bug correction (and there was one, a change to the spelling of July in
>French), would require changes to the input thus the caller would have
>to be recompiled anyway.
we have several call types to the date routine (ie. convert julian
date to gregorian,  gregorian to julian, compare today to last
thursday. etc.) so the input may not have a efect on the output.
>The nested program is faster than a static
>link 
(I assume you mean a dynamic link!?)
>which is what would be used in CICS programs for CALL 'datertn' as
>opposed to CALL DATE-ROUTINE-NAME where DATE-ROUTINE-NAME is PIC X(8)
>VALUE 'datertn'.  
Why? In a high volume environment hundreds, if not thousands of
modules could be staticly linked to this date routine which,
especially if coded in cobol, is probably thousands of bytes worth of
duplicate code. Whereas in a dynamically linked environment the module
is always occuping only the needed amount of storage for the code
with, at most, a couple hundred bytes of transaction storage, which
can be freed once it returns to the calling module. Basically its a
trade off. If you can afford t have huge regions with nanosecond
faster response time go with the static, or nested link. If you want
to make maintenance easier and get by with smaller regions and have
the cpu to spare the time it took me to type this s then please, for
the love of something holy, use dynamic linking.
>The CALL DATE-ROUTINE-NAME is normally a dynamic load
>at run-time unless 'datertn' has been compiled as a nested program
>within the caller.  This latter exception boggled my mind when I
>discovered it during testing.
I knew this after three months on the job. why was this a suprise?
> 
>Analysis is needed for what a routine is doing, the costs of the dynamic
>overhead both initial and per CALL execution, and the maintenance
>tradeoffs. There is no one right answer.
In a huge volume system the ONLY answer is dynamic linking. We run at
least 14 top of the line IBM boxes pushing out at least 1.2BIPS each
over four JESs and the mandate in ALL subsystems is dynamic linking
becuase the .00001 seconds it takes to load a module (which is usually
already loaded and can just be BASRed to) is trivial compared to the
cost of missing a recompile and holding cycle for even a half an hour
while someone crawls out of bed to go dah at four A.M.
> In the case of the date
>routine usage at the shop where I wrote it and put it into production,
>90+ percent of the usage is via dynamic call.  The batch standard is
>dynamic call except where required by subsystems.  
We do have one program that uses static linking. It processes about
300 million accounts, on tape, and several million transactions to any
and all of those accounts. This is the only program I know of in our
shop that can use static linking. It is also the only program I have
seen the uses less wall time than CPU time. Bless those programs
written in the sixties.
>
>Clark Morris, CFM Technical Programming Services Inc.,
…[120 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Nested Program vs Dynamic was Re: Static vs Dynamic Linking

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-05-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8fglgh$s9i$1@slb6.atl.mindspring.net>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca> <391257e3.504741000@news.radiks.net> <391B5200.F6A0CBAB@istar.ca> <391bb6e7.6781000@news.radiks.net>`

```
If you are in favor of dynamic CALLs (and I do agree that they have their
place), then it is CRITICAL that you understand how to keep the COBOL
environment "up and running" between calls.

This was certainly a major (the major?) inhibitor to many shops as they moved
from OS/VS COBOL to VS COBOL II and then to IBM COBOL for this-and-that.
(especially for shops where the "main" program in their application was
non-COBOL and one or more COBOL subroutines were repeated called and -
effectively - cancelled)

If your "dynamically" called subroutine (and this assumes that it is called
repeatedly in the same application - not from many different applications)
happens to "require" that you set up and destroy a "higher-level" run-time
environment than your main application requires, the impact on run-time
performance will NOT be nano-seconds but lots of real "billable" time.

There are DEFINITELY ways of making certain that the "higher-level run-time
environment" is only set up once (and not destroyed until the end of the
application) - but for the uninformed (or unprepared) making this "simple"
mistake can EASILY make dynamic CALLs look like a "disaster".
```

###### ↳ ↳ ↳ Re: Nested Program vs Dynamic was Re: Static vs Dynamic Linking

_(reply depth: 5)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-05-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<391D176D.505FC06A@zip.com.au>`
- **References:** `<B6200F7A96BCD211864900A0C9D81738051349A0@es01-hou.bmc.com> <3910C3C0.87ED0DBD@istar.ca> <391257e3.504741000@news.radiks.net> <391B5200.F6A0CBAB@istar.ca> <391bb6e7.6781000@news.radiks.net> <8fglgh$s9i$1@slb6.atl.mindspring.net>`

```
"William M. Klein" wrote:
> 
> If you are in favor of dynamic CALLs (and I do agree that they have their
> place), then it is CRITICAL that you understand how to keep the COBOL
> environment "up and running" between calls.

A real example of this was we took a five minute non cobol program,
put a cobol exit in and ran for 2 hours before cancelling it.  (there
were literally thousands of calls).

Language Environment apparently fixes this (we went to assembler at
the time).

Outside LE there is a module you call before entering the non cobol
environment and this establishes the environment once for cobol II.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
