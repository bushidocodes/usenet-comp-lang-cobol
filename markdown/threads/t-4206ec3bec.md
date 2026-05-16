[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IDLE LOOP (win95).

_5 messages · 4 participants · 1998-09_

---

### IDLE LOOP (win95).

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6trmbm$84l$1@news.igs.net>`

```
Does anybody have a subroutine for Windows95 that calls
the idle API?  I need to put it into a wait for file lock loop.

I am planning to use it with Fujitsu, but if anyone has one for
another compiler, I will convert it and post it back. There
should not be much of a difference.
```

#### ↳ Re: IDLE LOOP (win95).

- **From:** "Leif Svalgaard" <leif@ibm.net>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<360163b7.0@news1.ibm.net>`
- **References:** `<6trmbm$84l$1@news.igs.net>`

```
Donald Tees wrote in message <6trmbm$84l$1@news.igs.net>...
>Does anybody have a subroutine for Windows95 that calls
>the idle API?  I need to put it into a wait for file lock loop.
…[3 more quoted lines elided]…
>should not be much of a difference.


Donald,
The etk2syst.dll from http://www.etk.com/products/etkf32a has a sleep
routine that sleeps a number of milliseconds.
Alternatively you can call Sleep using milliseconds in the WIN32 API.
```

#### ↳ Re: IDLE LOOP (win95).

- **From:** Karl Wagner <kwagner@sympatico.ca>
- **Date:** 1998-09-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3601723C.6A1B7F9C@sympatico.ca>`
- **References:** `<6trmbm$84l$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Does anybody have a subroutine for Windows95 that calls
…[4 more quoted lines elided]…
> should not be much of a difference.

Here's how to call the API directly from MF COBOL.

SPECIAL-NAMES.
    CALL-CONVENTION 74 IS APIENTRY.

* Wait 100 microseconds
    CALL APIENTRY "Sleep" USING
       BY VALUE 100 SIZE 4 
    END-CALL

I think it looks something like this in Fujitsu but I haven't had much
chance to look at their implementation yet so I could be messed up about
byte ordering and the syntax for a STDCALL.
      
        01  SLEEP-MICROSECONDS       PIC 9(9) BINARY.

	CALL "_Sleep" USING BY CONTENT SLEEP-MICROSECONDS 

All that aside, you should probably use a Mutex or Semaphore and
WaitForSingleObject() instead of coding a polling loop.
```

#### ↳ Re: IDLE LOOP (win95).

- **From:** "Fujitsu Software" <cobol@adtools.com>
- **Date:** 1998-09-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6tuj6c$elr$1@news.fujitsu.com>`
- **References:** `<6trmbm$84l$1@news.igs.net>`

```
Donald,

In Fujitsu COBOL you would call the WIN32 Sleep function as follows:

              CALL "SleepEx" WITH STDCALL USING
                                  BY VALUE SLEEP-MICROSECONDS
                                  BY VALUE 1
              END-CALL

Fujitsu Software Corporation
Developer Tools Group
Phone: (408) 428-0500
FAX:    (408) 428-0600
Email:  cobol@adtools.com
Web:   http://www.adtools.com



Donald Tees wrote in message <6trmbm$84l$1@news.igs.net>...
>Does anybody have a subroutine for Windows95 that calls
>the idle API?  I need to put it into a wait for file lock loop.
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IDLE LOOP (win95).

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-09-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6ue41q$qip$1@news.igs.net>`
- **References:** `<6trmbm$84l$1@news.igs.net> <6tuj6c$elr$1@news.fujitsu.com>`

```

Fujitsu Software wrote in message <6tuj6c$elr$1@news.fujitsu.com>...
>Donald,
>In Fujitsu COBOL you would call the WIN32 Sleep function as follows:
…[3 more quoted lines elided]…
>              END-CALL

Mmm.  Does not work ... it will not link under Version 4.0. Perhaps
I should just create a powercobol form in a DLL with nothing but
a timer in it, and call that.  Seems like overkill though.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
