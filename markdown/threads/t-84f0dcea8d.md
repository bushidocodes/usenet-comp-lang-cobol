[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to interrupt/terminate(cntl-c) an executing program?

_4 messages · 4 participants · 2002-09_

**Topics:** [`Help requests and how-to`](../topics.md#help)

---

### How to interrupt/terminate(cntl-c) an executing program?

- **From:** "Garry D." <garry_dalgarno@telus.net>
- **Date:** 2002-09-06T23:23:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GNae9.274$_J3.40331@news0.telusplanet.net>`

```
Fujitsu 6.1
Windows2000

Periodically, we want to stop one of our programs, mid execution! (Executed
from a CMD window)

It's a fairly simple program that won't respond, when we want to CNTL-C it
and terminate/interrupt/stop it's execution.

This program doesn't require the user to key any data into the systems, so
no regular input is required.

Unfortunately, it would appear the program isn't listening for any input
whatsoever, even a user request to stop executing.  We must CNTL-ALT-DEL and
end the task... ouch.

I've scanned the Fujitsu PDF's (and online reference) for interrupt, break,
and CNTL-C... can't spot anything that would help?

Has anybody ran into this problem?
```

#### ↳ Re: How to interrupt/terminate(cntl-c) an executing program?

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-09-07T05:59:50+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<qBge9.15425$jG2.1129320@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<GNae9.274$_J3.40331@news0.telusplanet.net>`

```

"Garry D." <garry_dalgarno@telus.net> wrote in message
news:GNae9.274$_J3.40331@news0.telusplanet.net...
> Fujitsu 6.1
> Windows2000
>
> Periodically, we want to stop one of our programs, mid execution!
(Executed
> from a CMD window)
>
…[7 more quoted lines elided]…
> whatsoever, even a user request to stop executing.  We must CNTL-ALT-DEL
and
> end the task... ouch.
>
> I've scanned the Fujitsu PDF's (and online reference) for interrupt,
break,
> and CNTL-C... can't spot anything that would help?
>
> Has anybody ran into this problem?
>

    With Microfocus, I found that this can happen if the program does not
make
any system calls.  Try putting something in.  For example, check the
keyboard
status, accept time, something of that sort.

    Even disk access can be enough.  Be sure to limit the frequency of
whatever you do,
since even checking the system date or time can be slower than you might
think.
```

##### ↳ ↳ Re: How to interrupt/terminate(cntl-c) an executing program?

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-09-08T08:18:21+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D7AF9BD.C8846731@Azonic.co.nz>`
- **References:** `<GNae9.274$_J3.40331@news0.telusplanet.net> <qBge9.15425$jG2.1129320@bgtnsc05-news.ops.worldnet.att.net>`

```
Russell Styles wrote:
> 
>     With Microfocus, I found that this can happen if the program does not
…[8 more quoted lines elided]…
> think.

That, of course, ensures that the program tries to use and waste the
maximum amount of processor time doing something that would usually not
use any.  It was not an acceptable mechanism when single-tasking DOS was
used and certainly isn't with multi-tasking systems.  Windows sometimes
struggles when programs are being nice.

There are 'dispatch' calls, even under DOS, that release the current
time slice.  So even if the program is just cycling waiting for a
keystroke it can do so minimising the CPU time used by dispatching.
```

#### ↳ Re: How to interrupt/terminate(cntl-c) an executing program?

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-09-07T12:42:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gvme9.230279$On.9058867@bin3.nnrp.aus1.giganews.com>`
- **References:** `<GNae9.274$_J3.40331@news0.telusplanet.net>`

```

"Garry D." <garry_dalgarno@telus.net> wrote in message
news:GNae9.274$_J3.40331@news0.telusplanet.net...
> Fujitsu 6.1
> Windows2000
>
> Periodically, we want to stop one of our programs, mid execution!
(Executed
> from a CMD window)
>
…[7 more quoted lines elided]…
> whatsoever, even a user request to stop executing.  We must CNTL-ALT-DEL
and
> end the task... ouch.
>
> I've scanned the Fujitsu PDF's (and online reference) for interrupt,
break,
> and CNTL-C... can't spot anything that would help?
>
> Has anybody ran into this problem?

Here's how we interrupt a running program in PowerCOBOL:

1. Add a "Pause" button to the form. It's click event has one instruction:
    MOVE "Y" TO PAUSE-JOB

2. In the processing code, we have the following:

    (every 100 records)
   INVOKE POW-SELF 'THRUEVENTS'
   IF PAUSE-JOB = "Y"
      ask user if he wants to abandon the job
      etc

The trick is the THRUEVENTS method (q.v.). This processes the pending
Windows message queue.

In a strict COBOL-only program, you'll probably have to read the keyboard
yourself at regular intervals (see CBL_GET_KBD_STATUS and
CBL_READ_KBD_CHAR).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
