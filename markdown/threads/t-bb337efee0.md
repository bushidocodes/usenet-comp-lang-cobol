[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Fujitsu V4.0 slower than MF NetExpress?

_3 messages · 2 participants · 1998-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Fujitsu V4.0 slower than MF NetExpress?

- **From:** dlmax@netcom.com (David L Maxwell)
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dlmaxF0FAKM.BL6@netcom.com>`

```
I received my copy of Fujitsu COBOL V4.0 a few days ago, and have been
running compiler timing tests to determine if Fujitsu COBOL V4.0 is
faster than Microfocus NetExpress or Visual Object COBOL.

I was shocked to find that Fujitsu V4.0 COBOL was running 6 to 7 times
slower than either NetExpress or Visual Object COBOL.

My results (300Mhz Micron Pentium II / Windows 95):

NetExpress V1.0             9.39  secs  size of exe:  5632

Fujitsu V4.0                65-70 secs  size of exe:  41472

I later discovered that when the Fujitsu version was run from either
the "RUN" command line, or WINEXEC the run time is 8.89 sec.

Can anyone explain why there is such a large difference?  When the Fujitsu
version is run from the MS-DOS Prompt, it completes in anywhere between
65 and 70 seconds. The NetExpress and Visoc versions run in the same times
regardless of where they were launched.

David Maxwell
```

#### ↳ Re: Fujitsu V4.0 slower than MF NetExpress?

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-10-06T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-IYDQsH6oXhsG@Dwight_Miller.iix.com>`
- **References:** `<dlmaxF0FAKM.BL6@netcom.com>`

```
On Tue, 6 Oct 1998 20:36:21, dlmax@netcom.com (David L Maxwell) wrote:

> I received my copy of Fujitsu COBOL V4.0 a few days ago, and have been
> running compiler timing tests to determine if Fujitsu COBOL V4.0 is
…[18 more quoted lines elided]…
>

I SUSPECT it is excess overhead as the DOS box emulator tries to load 
the runtime DLL files - there are more associated with Fujitsu than 
with Netexpress.  

If you create an ICON on the desktop for the application, how does it 
perform?

Did you compile with optimization?  That can significantly speed up 
execution.
```

##### ↳ ↳ Re: Fujitsu V4.0 slower than MF NetExpress?

- **From:** dlmax@netcom.com (David L Maxwell)
- **Date:** 1998-10-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dlmaxF0FoGx.75y@netcom.com>`
- **References:** `<dlmaxF0FAKM.BL6@netcom.com> <Jl0PnHJ5PvPd-pn2-IYDQsH6oXhsG@Dwight_Miller.iix.com>`

```
In article <Jl0PnHJ5PvPd-pn2-IYDQsH6oXhsG@Dwight_Miller.iix.com>, 
redsky@ibm.net says...
>
>On Tue, 6 Oct 1998 20:36:21, dlmax@netcom.com (David L Maxwell) wrote:
…[29 more quoted lines elided]…
>

It runs in 8.89 seconds.

>Did you compile with optimization?  That can significantly speed up 
>execution.

Yes, Global optimization was on.

I created a seperate directory for the application and loaded all
the runtime files there.  I then rebooted the system to eliminate
the possibility of DLL's hanging around.  I started the application
from the DOS prompt and it ran in 9.02 seconds.  I started it again,
and again it ran in 8.92 seconds.  On the third and subsequent runs
the times ranged from 75 seconds to 90 seconds.

I have an old 100Mhz 486 running windows 95, so I tried running the
application there with the same results.  However the run times were
very much longer.

I have noticed one other strange behavior.  While waiting for the 
application to finish I clicked repeatedly on the Icon in the
Windows start bar, and this causes tha application to finish
much earlier than the 75 to 90 seconds.  Sometimes it will complete
in under 20 seconds.  It all depends upon when the clicking begins.

Strange Huh?

David Maxwell
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
