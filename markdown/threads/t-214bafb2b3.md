[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Time of Day in micro-seconds or nano-seconds

_10 messages · 8 participants · 2008-05 → 2008-06_

---

### COBOL Time of Day in micro-seconds or nano-seconds

- **From:** "don@higgins.net" <don@higgins.net>
- **Date:** 2008-05-29T11:46:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com>`

```
All

Does anyone know of a "standard" or widely accepted way to get COBOL
time of day in micro-seconds or nano-seconds for use in generating
more accurate transaction time-stamp and for use in measuring
transaction turn-around time.

The current-date function only returns hundredth of a second.

Using mainframe assembler the micro-second clock counter can be
accessed but that's not standard COBOL and not portable across
platforms.  In J2SE Java, there is the method System.nanotime() to get
the more accurate time of day in nano-secounds available from the host
system but that's not standard COBOL either.

Don Higgins
don@higgins.net
```

#### ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** Gerry Palmer <gpalmer@pobox.com>
- **Date:** 2008-05-29T21:40:32-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<almu34dh3g926r73neul0d44orf3jj0o2s@4ax.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com>`

```
On Thu, 29 May 2008 11:46:43 -0700 (PDT), "don@higgins.net"
<don@higgins.net> wrote:

>All
>
…[3 more quoted lines elided]…
>transaction turn-around time.

If you're talking IBM mainframe COBOL, the CURRENT-DATE value (the
date and/or time at which the request for the date and/or time was
issued as reported by the system on which the program runs) can be
obtained in several ways: with the COBOL "ACCEPT" statement, through
the COBOL "CURRENT-DATE" Intrinsic Function, and through the LANGUAGE
ENVIRONMENT "CEELOCT" Callable Service.        
                                                            
 The LANGUAGE ENVIRONMENT CEELOCT Callable Service returns the current
local date or time in three formats:           
                                                            
-> LILIAN DATE (number of days since 14 October 1582)  
-> LILIAN SECONDS (number of seconds since 00:00:00 14 October 1582)
-> GREGORIAN character string (format YYYYMMDDHHMISS999)   

The GREGORIAN character string format of the CEELOCT Callable Service
resolves time to thousandth seconds (seconds plus three decimal
digits). The other two options, as best I know, resolve to hundredths
of a second only.

I'm not aware of any standard function that resolves to micro or nano
second granularity in this environment.

And if you're looking for portability across platforms, the LE
Callable Service is unlikely to satisfy your needs.
```

#### ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-29T22:02:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8ru345aidiit7s14rvrdijedg65rhbkej@4ax.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com>`

```
On Thu, 29 May 2008 11:46:43 -0700 (PDT), "don@higgins.net" <don@higgins.net> wrote:

>All
>
…[11 more quoted lines elided]…
>system but that's not standard COBOL either.

GNU C gettimeofday() is available on the most platforms. It returns microsecond
resolution, depending on OS capability of course. You can call it directly from Cobol.
```

##### ↳ ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** Michael Wojcik <mwojcik@newsguy.com>
- **Date:** 2008-05-30T15:12:15-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g1q5t701lfb@news3.newsguy.com>`
- **In-Reply-To:** `<d8ru345aidiit7s14rvrdijedg65rhbkej@4ax.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com> <d8ru345aidiit7s14rvrdijedg65rhbkej@4ax.com>`

```
Robert wrote:
> 
> GNU C gettimeofday()

... is an implementation of the standard gettimeofday(), which is part 
of the Single UNIX Specification v3, aka the Open Group Base 
Specifications Issue 6, which is the unified specification that now 
defines the POSIX base (IEEE 1003.1) and ISO/IEC 9945-1, as well as 
SUS and OGBS.[1]

(Specifically, it's part of the X/Open Systems Interface Extension, 
which includes various APIs that are not part of the ISO C library.)

 > is available on the most platforms.

And more importantly, gettimeofday is also included in other SUSv3 
implementations. It's not defined by or restricted to GNU.

 > It returns microsecond
> resolution, depending on OS capability of course.

This is an important caveat. Many implementations of gettimeofday are 
limited by an OS clock granularity much coarser than a microsecond. 
(In the mid-1990s, for example, 100 Hz - ie, 10 millisecond - 
resolution was used by several Unix implementations. I don't know 
offhand what's typical these days.) For better resolution, you 
generally have to go to platform-specific functions.

 > You can call it directly from Cobol.

Here's an example using Micro Focus Server Express to get milliseconds 
since the beginning of the epoch (midnight 1/1/1970), on 32-bit Solaris:

-----
       $set sourceformat(free)

identification division.
program-id. time-in-ms.

data division.
working-storage section.

    01 timeval-32bit.
       02 seconds      pic x(4) comp-5.
       02 microseconds pic x(4) comp-5.
    77 tzp usage pointer value null.
    77 ms-since-epoch  pic 9(18) display.

procedure division.
    call "gettimeofday" using
       by reference timeval-32bit
       by value     tzp
       end-call
    compute ms-since-epoch = seconds * 1000 + microseconds / 1000
    display ms-since-epoch
    stop run
    .
-----


[1] 
http://www.opengroup.org/onlinepubs/009695399/functions/gettimeofday.html
```

#### ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** "HeyBub" <heybub@NOSPAMgmail.com>
- **Date:** 2008-05-30T09:03:32-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<q5KdnaSk1tKvlN3VnZ2dnUVZ_g6dnZ2d@earthlink.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com>`

```
don@higgins.net wrote:
> All
>
…[12 more quoted lines elided]…
>

On PCs, the best resolution is ghastly, I think it's 16 milliseconds. But 
whatever, you're limited to the resolution of the CPU's timer.

Another tack is to get a start time, process 'n' transactions (where 'n' is 
a large number), get an ending time then compute an average.
```

##### ↳ ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** Robert <no@e.mail>
- **Date:** 2008-05-30T19:13:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bp41449nk3185c2fimhbt05ap2len5hc8t@4ax.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com> <q5KdnaSk1tKvlN3VnZ2dnUVZ_g6dnZ2d@earthlink.com>`

```
On Fri, 30 May 2008 09:03:32 -0500, "HeyBub" <heybub@NOSPAMgmail.com> wrote:

>don@higgins.net wrote:
>> All
…[16 more quoted lines elided]…
>whatever, you're limited to the resolution of the CPU's timer.

The interrupt 10 timer is ancient history. Its resolution was 1/18.2 sec = 56 ms. Intel
and Windows have offered higher resolution timers since the 80386 circa. 1994.

The question seemed oriented to mainframes and/or Cobol. ANS Standard Cobol offers no
solution. The z/OS API does but it's not portable, as stated in the question. So does
POSIX, but it too is tied to one OS family (Unix). I think the best answer is a non-Cobol,
OS-independent one such as GNU C. 

>Another tack is to get a start time, process 'n' transactions (where 'n' is 
>a large number), get an ending time then compute an average.

Yep, that's my preferred way. When trying to time a single event or iteration, the
overhead of GETTING the time can be longer than, or a significant percentage of, the event
being timed. 

But the question was how to get a high resolution transaction timestamp, which would be
used to order events chronologically or detect collisions.
```

##### ↳ ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2008-05-31T11:45:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<sk3344hkcgoan09t1fll83ofcmtipsu6hq@4ax.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com> <q5KdnaSk1tKvlN3VnZ2dnUVZ_g6dnZ2d@earthlink.com>`

```
On Fri, 30 May 2008 09:03:32 -0500, "HeyBub" <heybub@NOSPAMgmail.com>
wrote:

>On PCs, the best resolution is ghastly, I think it's 16 milliseconds. But 
>whatever, you're limited to the resolution of the CPU's timer.

Although with any virtual environment,  asking for better resolution
is kind of moot.
```

#### ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** SkippyPB <swiegand@nospam.neo.rr.com>
- **Date:** 2008-05-30T11:32:13-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<p970441c31kmf4qvd5iqg5qp3vkgj06ug3@4ax.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com>`

```
On Thu, 29 May 2008 11:46:43 -0700 (PDT), "don@higgins.net"
<don@higgins.net> wrote:

>All
>
…[14 more quoted lines elided]…
>don@higgins.net

Here's an alternative way that might work instead of using time of
day.  This is from tek-tips.com and with it you can find the way to
determine the exact amount of used CPU for the current job. It may be
that you have to update the MVS-addresses. You can find them in some
manuals with a description of MVSDATA.

CBL TRUNC(OPT)
       CBL NOSSRANGE
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CPUTIME.
       AUTHOR. CROX.
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SPECIAL-NAMES.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 CPU-TIME-DEF-WORKING-STORAGE.
          03 MICRO-SECONDS                 PIC S9(15) COMP-3.
          03 FW1                           PIC S9(08) COMP.
          03 PTR4      REDEFINES FW1 POINTER.
          03 FW2                           PIC S9(08) COMP.
          03 PTR5      REDEFINES FW2 POINTER.
          03 FW2-ALFA  REDEFINES FW2       PIC  X(04).
          03 BFW2                          PIC S9(18) COMP VALUE ZERO.
          03 BFW2-ALFA REDEFINES BFW2      PIC  X(08).
       LINKAGE SECTION.
       01 CB1.
          03 PTR1 POINTER OCCURS 256.
       PROCEDURE DIVISION.
       MAIN SECTION.
       0000.
           PERFORM GET-MICRO-SECONDS.
       0000.
           GOBACK.

       GET-MICRO-SECONDS SECTION.
       GMS-01.
           SET ADDRESS OF CB1    TO NULL.
           SET ADDRESS OF CB1    TO PTR1(136).
           SET PTR4              TO PTR1(80).
           SET PTR5              TO PTR1(81).
           MOVE FW2-ALFA         TO BFW2-ALFA (5:).
           COMPUTE MICRO-SECONDS  = FW1 * 1048576 +
                                    BFW2 / 4096.
           DISPLAY 'MICRO-SECONDS = ' MICRO-SECONDS.
       GMS-99.
           EXIT.

Regards,
          ////
         (o o)
-oOO--(_)--OOo-

"I never said most of the things I said."
-- Yogi Berra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

#### ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2008-05-30T19:45:54+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SPY%j.873579$us.63503@fe04.news.easynews.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com>`

```
Don,
  Not a "real solution" - but it might BECOME one if enough users on enough 
platforms ask enough COBOL vendors to implement EARLY a feature planned for the 
next revision of the ISO COBOL Standard.

A number of new date and time functions are included in the revision and 
someinclude "fractional portions of a second" and there is a note that says,

 "The implementor defines the maximum number of digit positions that may be 
specified in the decimal fraction
portion of the seconds subfield of a time format; that maximum shall be greater 
than or equal to nine."

Now WHAT information you are supposed to get back when the O/S doesn't support 
this level of detail, I don't know!

(If you are interested in this support on z/OS, get a SHARE member to submit a 
requirement; on VSE, get a WAVV member to do so; elsewhere, ask your "vendor of 
choice").
```

#### ↳ Re: COBOL Time of Day in micro-seconds or nano-seconds

- **From:** "don@higgins.net" <don@higgins.net>
- **Date:** 2008-06-05T17:23:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9cfd5a83-f881-44c4-823a-f50754160c92@a70g2000hsh.googlegroups.com>`
- **References:** `<8a5a1cc8-bd8c-418d-9c6a-9e00a9111ad9@m45g2000hsb.googlegroups.com>`

```
On May 29, 2:46 pm, "d...@higgins.net" <d...@higgins.net> wrote:
> All
>
…[4 more quoted lines elided]…
>

Here is updated documentation on timestamps availabe for COBOL,
Assembler, C, Java, SQL, and XML plus references. In summary there is
new support now available for z390 and Micro Focus COBOL running on
windows to get timestamps in microseconds or nonoseconds for mor
precise timing of events or tranactions:

http://z390.sourceforge.net/z390_Standard_Timestamp_Support.htm

Under the cover Windows API's used include GetSystemTimeAsFileTime,
QueryPerformanceFrequency, and QueryPeformanceCounter.

Don Higgins
don@higgins.net
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
