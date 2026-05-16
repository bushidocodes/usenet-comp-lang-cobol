[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to let a COBOL program sleep 5 seconds

_26 messages · 14 participants · 2004-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to let a COBOL program sleep 5 seconds

- **From:** "William Cai" <wenliang_cai@yahoo.com.cn>
- **Date:** 2004-09-07T14:18:43+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chjjss$t76$1@mail.cn99.com>`

```
Hi, folks

Anybody can tell me how to let a COBOL program sleep 5 seconds? I am new to
COBOL. Sorry for the stupid question. :)


-William
```

#### ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "William Cai" <wenliang_cai@yahoo.com.cn>
- **Date:** 2004-09-07T14:57:56+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chjm5s$uao$1@mail.cn99.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com>`

```
Update my question:

I list my program as below. But whatever I input, the program will sleep for
a very long time. I am sure not if the program hangs. Anyone can help? Thank
you.

       IDENTIFICATION DIVISION.
       PROGRAM-ID. EXAM1.
       ENVIRONMENT DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 SLEEP-SEC PIC 9.
       PROCEDURE DIVISION.
       S. DISPLAY 'THIS IS COBOL'.
          DISPLAY 'PLEASE INPUT THE SECONDS FOR SLEEP'.
          ACCEPT SLEEP-SEC.
          DISPLAY 'WILL SLEEP ', SLEEP-SEC, ' SECONDS'.
          CALL "sleep" USING SLEEP-SEC;
          STOP RUN.

"William Cai" <wenliang_cai@yahoo.com.cn> wrote in message
news:chjjss$t76$1@mail.cn99.com...
Hi, folks

Anybody can tell me how to let a COBOL program sleep 5 seconds? I am new to
COBOL. Sorry for the stupid question. :)


-William
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-07T10:43:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5u3rj0dugnsgpuapracs2ciure4pt0m8r2@4ax.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <chjm5s$uao$1@mail.cn99.com>`

```
On Tue, 7 Sep 2004 14:57:56 +0800, "William Cai"
<wenliang_cai@yahoo.com.cn> wrote:

>Update my question:
>
…[23 more quoted lines elided]…
>COBOL. Sorry for the stupid question. :)

Sleep is not a *standard* Cobol function; is it a standard C function.
It appears you're calling the C function. If true, change sleep-sec to
binary pic 9(9)  and call using by value sleep-sec.
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** mwojcik@newsguy.com (Michael Wojcik)
- **Date:** 2004-09-09T14:58:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chpr2502703@news2.newsguy.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <chjm5s$uao$1@mail.cn99.com> <5u3rj0dugnsgpuapracs2ciure4pt0m8r2@4ax.com>`

```

In article <5u3rj0dugnsgpuapracs2ciure4pt0m8r2@4ax.com>, Robert Wagner <robert@wagner.net.yourmammaharvests> writes:
> 
> Sleep is not a *standard* Cobol function; is it a standard C function.

It's neither.  "sleep" (lowercase s) is a standard POSIX / SUS function
(see IEEE Std 1003.1-2001 and subsequent editions, Open Group Base
Specifications Issue 6, etc).  "Sleep" (capital S) is a Windows function
(with different syntax), not endorsed by any standards group I'm aware
of.  There may of course be other implementations of "sleep" functions
in other domains.

C does not define a "sleep" function or other reserved identifier.  See
ISO 9899:1990 and subsequent editions.

The POSIX sleep need not be implemented in C, of course.
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-07T11:47:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dh7rj0dq4345k8elipf0re84vq1es8489j@4ax.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <chjm5s$uao$1@mail.cn99.com>`

```
On Tue, 7 Sep 2004 14:57:56 +0800, "William Cai"
<wenliang_cai@yahoo.com.cn> wrote:

>Anybody can tell me how to let a COBOL program sleep 5 seconds? I am new to
>COBOL. Sorry for the stupid question. :)

If my suggested fix works, you might do one or both of the following:

1. Write a prototype of the sleep function in Cobol and put it at the
top of your program. It would have prevented the type mismatch. 
Your instructor probably never saw a Cobol prototype. If your compiler
supports this feature (Micro Focus does), you'll get an A.

2. Tell your instructor he's not teaching Cobol when he has you call a
foreign function. You'll have the satisfaction of being right, even
though you'll get a C.
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-09-07T08:12:06-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<zt6dnQNTLLsDLqDcRVn-pQ@giganews.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <chjm5s$uao$1@mail.cn99.com>`

```
William Cai wrote:
> Update my question:
>
…[23 more quoted lines elided]…
> new to COBOL. Sorry for the stupid question. :)

Assuming "sleep" in your example is a routine provided by somebody, the
problem probably lies in the passed variable.

COBOL does not pass the value you specify, it passes the address of the
location of the value. Assume the user enters "5." If "sleep" is expecting a
5-digit value, it may very well get

   51234

where "1234" is the contents of the next four bytes in memory.

The fix is to find out what format "sleep" is expecting and adjust your
program to match.
```

#### ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2004-09-07T08:09:37+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9knqj09fqkaf5o9goflj1i2qd9oqnc3i25@4ax.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com>`

```
On Tue, 7 Sep 2004 14:18:43 +0800, "William Cai"
<wenliang_cai@yahoo.com.cn> wrote:

>Hi, folks
>
…[5 more quoted lines elided]…
>

You need to tell us which COBOL vendor and which OS you are using
(looks like Windows/DOS but...)

Each vendor will have it's own way of doing things.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "William Cai" <caiwenliang@gmail.com>
- **Date:** 2004-09-09T20:07:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chr5q5$9i0@odbk17.prod.google.com>`
- **In-Reply-To:** `<9knqj09fqkaf5o9goflj1i2qd9oqnc3i25@4ax.com>`

```
I am using Microfocus COBOL suite. Thanks.

-William
```

#### ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "wahlers" <ahlers_wim@hotmail.com>
- **Date:** 2004-09-07T07:57:23-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2d2625a6560fa6e43ab719fc2b4143aa@localhost.talkaboutprogramming.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com>`

```
To add to Frederico Fonseca's answer:

COBOL does not include a "sleep" function up to and including COBOL-85.

There might(!) be a COBOL intrinsic standard function that performs this
function (I don't know...check yourself).

There might(!) be a COBOL standard "sleep" function in the COBOL-2002
standard (or beyond). I don't know!

Assuming there is no standard "sleep" function then do the following:

1. Write a COBOL function (within OOCOBOL: a COBOL static function),
calling a system dependent(!) "sleep" routine.
2. Let your program call this (static) COBOL function when required.

This 2-phase call structure will accomplish the following:

It will prevent a massive recompile of many COBOL programmes in case you
have to change the environment or "sleep" routine.

Thus:

COBOL programs (many) -- calls -> COBOL "sleep" routine (independent) --
calls -> "sleep" routine (system dependent)

Notice that in the worst case scenario the system dependent "sleep"
routine must be replaced and maybe the COBOL "sleep" routine must be
modified (calling a different system dependent "sleep" routine name and/or
parameters).

There is, and will be, only one COBOL "sleep" routine.

The call structure relationship is thus as follows:
many COBOL programs calling 1 COBOL "sleep" routine calling 1 system
dependent "sleep" routine.

Using a construction as described as above makes your system more robust
and more adaptable for change.

I hope I was clear enough...regards, Wim Ahlers.

P.S. I don't care what the system dependent sleep routine looks like
(assembler, C++, LE routines (C), or whatever...).
```

#### ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2004-09-07T08:21:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8eWdnak1I60jOqDcRVn-ig@comcast.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com>`

```
Although it is not very efficient from a CPU perspective (and not exact,
although many OS sleep's are not exact either), you could do something like:

....
WORKING-STORAGE SECTION.
01 THE-TIME.
     03 THE-TIME-HH             PIC 99.
     03 THE-TIME-MM            PIC 99.
     03 THE-TIME-SS             PIC 99.
01 FIVE-SECONDS-LATER   PIC 99.
...
...
PROCEDURE DIVISION.
...
...
ACCEPT THE-TIME FROM TIME.
ADD THE-TIME-SS, 5 GIVING FIVE-SECONDS-LATER.
IF FIVE-SECONDS-LATER >= 60
  SUBTRACT 60 FROM FIVE-SECONDS-LATER.
PERFORM UNTIL THE-TIME-SS = FIVE-SECONDS-LATER
     ACCEPT THE-TIME FROM TIME
END-PERFORM.

I did this off the top of my head with no testing (and I don't use this
method in practice), so you may need to tweak....

(The reason this is not exact is ACCEPT FROM TIME could execute in the
middle of a second.)

"William Cai" <wenliang_cai@yahoo.com.cn> wrote in message
news:chjjss$t76$1@mail.cn99.com...
> Hi, folks
>
> Anybody can tell me how to let a COBOL program sleep 5 seconds? I am new
to
> COBOL. Sorry for the stupid question. :)
>
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-07T12:03:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409071103.7bbbaeea@posting.google.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com>`

```
"JJ" <jj@nospam.com> wrote

> ...
> ACCEPT THE-TIME FROM TIME.
…[5 more quoted lines elided]…
> END-PERFORM.

This is _not_ a 'sleep' function. It is a 'use_all_the
CPU_time_available' function.

On multi-user or multi-tasking machines this is not being friendly. On
poor multi-taskers such as Windows it will affect the running of the
whole system.
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-09-07T14:29:25-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x6qdnYOZU9SRkaPcRVn-pw@giganews.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com> <217e491a.0409071103.7bbbaeea@posting.google.com>`

```
Richard wrote:
> "JJ" <jj@nospam.com> wrote
>
…[14 more quoted lines elided]…
> whole system.

Ah, not exactly. Starting with Win98 (and all the NT variants, 2K, XP),
Windows has preemptive multi-tasking and will interrupt a CPU bound job to
give cycles to other applications.
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

_(reply depth: 4)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-07T21:22:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4b9sj0h5ou2llae3p32s9csipie48e516e@4ax.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com> <217e491a.0409071103.7bbbaeea@posting.google.com> <x6qdnYOZU9SRkaPcRVn-pw@giganews.com>`

```
On Tue, 7 Sep 2004 14:29:25 -0500, "JerryMouse" <nospam@bisusa.com>
wrote:

>Ah, not exactly. Starting with Win98 (and all the NT variants, 2K, XP),
>Windows has preemptive multi-tasking and will interrupt a CPU bound job to
>give cycles to other applications.

Correction: starting with Win95. 

http://www.microsoft.com/ntworkstation/ProductInformation/ProductOverview/FeatureList/Windows95/techdiff.asp
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

_(reply depth: 4)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2004-09-07T22:58:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<92r%c.8808$ZC7.5151@newssvr19.news.prodigy.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com> <217e491a.0409071103.7bbbaeea@posting.google.com> <x6qdnYOZU9SRkaPcRVn-pw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote in message
news:x6qdnYOZU9SRkaPcRVn-pw@giganews.com...
> Ah, not exactly. Starting with Win98 (and all the NT variants, 2K, XP),
> Windows has preemptive multi-tasking and will interrupt a CPU bound job to
> give cycles to other applications.

As you noted in your correction, pre-emptive multi-tasking was a feature
starting with Win/95.

However, also since Win/95, only a dork would would suggest this
do-nothing-but-check-the-current-time-loop code is "OK"  because of
pre-emptive multi-tasking; anyone paying attention would know to use the
vastly more efficient WaitForSingleObject function with a five-second (or
whatever) timeout value. (Just create an event which is never signalled).
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

_(reply depth: 4)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-09-07T21:59:09-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-36A093.21590907092004@knology.usenetserver.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com> <217e491a.0409071103.7bbbaeea@posting.google.com> <x6qdnYOZU9SRkaPcRVn-pw@giganews.com>`

```
In article <x6qdnYOZU9SRkaPcRVn-pw@giganews.com>,
 "JerryMouse" <nospam@bisusa.com> wrote:

> Richard wrote:
> > "JJ" <jj@nospam.com> wrote
…[21 more quoted lines elided]…
> 

And they might get it working correctly in time for Win 2008...
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-07T19:36:41-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409071836.74eb5c62@posting.google.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com> <217e491a.0409071103.7bbbaeea@posting.google.com> <x6qdnYOZU9SRkaPcRVn-pw@giganews.com>`

```
"JerryMouse" <nospam@bisusa.com> wrote 

> > This is _not_ a 'sleep' function. It is a 'use_all_the
> > CPU_time_available' function.
…[7 more quoted lines elided]…
> give cycles to other applications.

They may give cycles to other jobs, based on the usual timeslicing,
but that is no excuse to chew up complete timeslices doing nothing.

In fact Windows gives more timeslices to forgound programs so if this
is a foreground task it will waste more CPU cycles than is given to
background programs.

A good multi-tasking system (such as some that I have used) will
actually detect such waste-time loops and will give it less cycles. 
This is useful when multi-tasking DOS programs where clueless
programmers seemed to never consider that other programs could use the
CPU.  Loops checking for keyhit() while using 100% CPU were typical. 
Windows running 2 or 3 of these would be brought to its knees while a
_good_ multi-tasker intercepted those and/or 'niced' them to a lower
priority.

DOS did have a 'despatch' function which truncated the timeslice. 
Adding this in the 'sleep' loop would minimise the CPU access while
having no effect on the program itself, yet I found few DOS
programmers who even knew it existed, let alone why they would care.
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

_(reply depth: 5)_

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-08T08:47:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<s9htj01ilu71l9hm3dvplfl7a8ievetd5m@4ax.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com> <217e491a.0409071103.7bbbaeea@posting.google.com> <x6qdnYOZU9SRkaPcRVn-pw@giganews.com> <217e491a.0409071836.74eb5c62@posting.google.com>`

```
On 7 Sep 2004 19:36:41 -0700, riplin@Azonic.co.nz (Richard) wrote:

>In fact Windows gives more timeslices to forgound programs so if this
>is a foreground task it will waste more CPU cycles than is given to
…[9 more quoted lines elided]…
>priority.

I anticipated that in my text editor by providing a multi-tasking
option. If off, it runs in a loop looking for a keystroke, mouse
event, possible garbage collection, etc. If on, it runs one of each
test, then Yields the rest of its timeslice. 

On every Windows since 95, it has not hogged CPU time whether the
option was on or off. When 'in focus' and idling, it uses less than 1%
of CPU time.
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "JJ" <jj@nospam.com>
- **Date:** 2004-09-07T20:41:03-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m4OdnZCACeSDyKPcRVn-oQ@comcast.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <8eWdnak1I60jOqDcRVn-ig@comcast.com> <217e491a.0409071103.7bbbaeea@posting.google.com>`

```
> This is _not_ a 'sleep' function. It is a 'use_all_the
> CPU_time_available' function.

Hence the very first line of my post (perhaps you didn't read it):

"Although it is not very efficient from a CPU perspective"

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0409071103.7bbbaeea@posting.google.com...
> "JJ" <jj@nospam.com> wrote
>
…[14 more quoted lines elided]…
> whole system.
```

#### ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-09-07T18:01:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RHm%c.931682$y4.164407@news.easynews.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com>`

```
What compiler and operating system are you running on?  I know how to do this on 
a few, but it is NOT portable across systems and compilers.
```

#### ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** Vaclav Snajdr <vsn@snajdr.de>
- **Date:** 2004-09-08T09:30:18+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chmbl9$ql2$04$1@news.t-online.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com>`

```
I use:
                                                
01 SLEEP-TIME           PIC 9(9)        COMP VALUE 500000.

(OS LINUX IN MY CASE, MF-COBOL)

ACCEPT SOME-NUM-FIELD AT 2479 WITH SIZE 1 AUTO TIMEOUT SLEEP-TIME.



William Cai wrote:

> Hi, folks
> 
…[4 more quoted lines elided]…
> -William
```

#### ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "William Cai" <caiwenliang@gmail.com>
- **Date:** 2004-09-09T20:24:23-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<chr6p7$bk0@odbk17.prod.google.com>`
- **In-Reply-To:** `<chjjss$t76$1@mail.cn99.com>`

```
Hi, list

I am looking for the solution. Could anybody please tell me how to code
instead of discussing if sleep is a Cobol standard function? Though
your dicussion also helps me. :P

Repeat my question.
I wanna develop a COBOL program. The program will sleep several seconds
according to user's input.

I have no instructor. So you are all my instructors. Many thanks for
your help.

William
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2004-09-10T07:37:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d9WdneayZLi5PdzcRVn-pg@giganews.com>`
- **References:** `<chr6p7$bk0@odbk17.prod.google.com>`

```
William Cai wrote:
> Hi, list
>
…[9 more quoted lines elided]…
> your help.

1. Get the time of day.
2. Compute end-time by adding five seconds to the current time.
3. Loop checking the time of day until end-time is reached, viz:

   PERFORM UNTIL SECONDS-NOW > END-TIME
      ACCEPT ...
      COMPUTE SECONDS-NOW = ...
   END-PERFORM
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** Robert Wagner <robert@wagner.net.yourmammaharvests>
- **Date:** 2004-09-10T16:03:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4hg3k0p66975p65d8mhn2fu1n5aouscd9b@4ax.com>`
- **References:** `<chjjss$t76$1@mail.cn99.com> <chr6p7$bk0@odbk17.prod.google.com>`

```
On 9 Sep 2004 20:24:23 -0700, "William  Cai" <caiwenliang@gmail.com>
wrote:

>Hi, list
>
…[6 more quoted lines elided]…
>according to user's input.

There are two kinds of sleep:

1. Run in a loop until n seconds have elapsed.
2. Tell the operating system to mark you asleep and wake you in n
seconds.

In human terms, 1. would not be called sleep, it would be called
wasting time. Unfortunately,  it is the best you can do in standard
Cobol.

working-storage section.
01  time-now.
     10  hours                   pic  9(02).
     10  minutes                 pic  9(02).
     10  seconds                 pic  9(02).
     10  hundredths              pic  9(02).
01  time-integer             pic  9(09).
01  wakeup-integer       pic  9(09).
linkage section.
01  sleep-duration        pic 9.

procedure division using sleep-duration.
    perform read-clock
    compute wakeup-integer = time-integer + (sleep-duration * 100)
    perform read-clock until time-integer > wakeup-integer
    goback.
read-clock.
    accept time-now from time
    compute time-integer = 
     ((((hours * 60) + minutes) * 60) + seconds) * 100) + hundredths).

If your compiler supports Events or MultiThreading, find the Wait
function, have the program wait for an event that will never happen or
return an error in n seconds. That would be true sleep, type 2. above.
```

##### ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-09-10T12:08:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0409101108.2e7659d3@posting.google.com>`
- **References:** `<chr6p7$bk0@odbk17.prod.google.com>`

```
"William  Cai" <caiwenliang@gmail.com> wrote 

> I am looking for the solution. Could anybody please tell me how to code
> instead of discussing if sleep is a Cobol standard function? Though
> your dicussion also helps me. :P

If sleep was a standard Cobol function then it would be easy to tell
you exactly how to do it. It isn't.

It isn't even a standard C function, though it may be in a C library. 
It may be possible to call a C library depending on your compiler and
the system you are running on. (yes I know it is MF now, but not the
OS).

> Repeat my question.
> I wanna develop a COBOL program. The program will sleep several seconds
> according to user's input.

You have been told this.  The actual answer is that 'sleep' requires a
parameter that is S9(9) COMP-5 and that this be passed BY VALUE.

         01  Sleep-Seconds              PIC S9(9) COMP-5.

             CALL "sleep" USING BY VALUE Sleep-Seconds

To get the value into that use a single digit input:

         01  Sleep-Input                PIC 9.

             DISPLAY "How many seconds"
             ACCEPT Sleep-Input
             MOVE Sleep-Input TO Sleep-Seconds
             CALL ...
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

- **From:** "William Cai" <caiwenliang@gmail.com>
- **Date:** 2004-09-12T22:39:36-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ci3bqo$11l@odak26.prod.google.com>`
- **In-Reply-To:** `<217e491a.0409101108.2e7659d3@posting.google.com>`

```
thanks a lot. :)

-William
```

###### ↳ ↳ ↳ Re: How to let a COBOL program sleep 5 seconds

_(reply depth: 4)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2004-09-13T14:54:08-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a2d426e.0409131354.606e59b3@posting.google.com>`
- **References:** `<ci3bqo$11l@odak26.prod.google.com>`

```
For those of you lurking and looking for an IBM mainframe solution,
the following from a sister forum may help:
 
http://groups.google.com/groups?q=ilbowat0&start=10&hl=en&lr=&ie=UTF-8&selm=MABBIHGFPKHEHJLAPIPPIEDLCMAA.wmklein%40ix.netcom.com&rnum=11

It was authored by Bill Klein, a regular contributor here. 




"William  Cai" <caiwenliang@gmail.com> wrote in message news:<ci3bqo$11l@odak26.prod.google.com>...
> thanks a lot. :)
> 
> -William
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
