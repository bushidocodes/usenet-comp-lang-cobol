[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Calculation Errors - Machine Dependent?

_7 messages · 7 participants · 2005-02_

---

### Calculation Errors - Machine Dependent?

- **From:** "Mark K." <mark.mkingston@gmail.com>
- **Date:** 2005-02-07T12:42:09-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com>`

```
Hello,

We are running Micro Focus Net Express 3.0 and Application Server 3.0.
on Windows 2000 Server.

We have an executable (compiled using Micro Focus NE 3.0) which is
called by a DOS batch file and performs arithmetic calculations.

We discovered a calculation error in the output when this program is
run on our production server but could not replicate the problem on
similarly configured test and backup servers.  The really baffling part
is that when we tried to step through the program using the Animate
function on the Production Server, the output is correct!

Has anyone run into this type of problem?  Could the errors be caused
by hardware or operating system patch levels?  If so, why does the
error disappear when using the Animate function??

Thanks for your help.

Mark K.
```

#### ↳ Re: Calculation Errors - Machine Dependent?

- **From:** "Steve.T" <steve_t@ix.netcom.com>
- **Date:** 2005-02-07T13:21:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107811308.846235.180740@f14g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com>`
- **References:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com>`

```
Do the different machines have a single CPU or multiple? Are the
machines  the same speed or different? Are the CPU manufacturers the
same between all the machines?

Since I do not know for sure which CPU you are using, might I suggest
that this could be due to parallel support? In otherwords, the system
may fail to obtain results from cache but obtain them from memory
before cache has been flushed to memory (this can be a cache controller
microcode bug). This can also happen if you are running a dual CPU
machine, where you get dispatched on the one processor, and then
dispatched on a different one before the dispatcher correctly causes a
flush of cache to memory for your task (this is a long story to
explain).

Meanwhile, because of the way Animate functions, there is time injected
from calculation step to calculation step. So the cache information
would be flushed to memory before fetch from memory. That is, things
would happen in such a way that almost everything would be fetched from
RAM, processed, stored to RAM before the next fetch takes place (from
your program's perspective).

Now the above is all very general. Different architectures implement
cache fetch, flush, interlocked update of RAM, etc. differently. The
above is only intended to give you some ideas as to where to look.

Regards,
Steve.T
```

#### ↳ Re: Calculation Errors - Machine Dependent?

- **From:** "Richard" <riplin@Azonic.co.nz>
- **Date:** 2005-02-07T13:44:24-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107812664.134207.237080@c13g2000cwb.googlegroups.com>`
- **In-Reply-To:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com>`
- **References:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com>`

```
> The really baffling part is that when we tried to step
> through the program using the Animate function on
> the Production Server, the output is correct!

The Animator should be using the .int intermediate code versions of the
compiled programs.  There may be some minor differences between
truncating values between the .int and the .gnt (or .exe) versions of
the compiled code.  Add 'ON SIZE ERROR' to all calculations to loacte
the problem.

One possibility is that there is an older buggy version of the program
that is earlier in the PATH that is being loaded instead of the one you
expect.

Check the files on your production serve doing a 'find' for all files
of that name with any extension.

Add a display to the program (or write a log record) with a version
number and check that this is output when the DOS batch runs it.  If it
isn't then it is running the wrong program.
```

#### ↳ Re: Calculation Errors - Machine Dependent?

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2005-02-07T21:57:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<VuRNd.1135412$B07.160154@news.easynews.com>`
- **References:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com>`

```
My *guess* is that

A) the two different versions have different settings for the ARITHMETIC 
compiler directive (which controls how some arithmetic is done)

   And/or

B) there are different settings for the +/-F run-time switch and you have "some" 
bad data being set to zero in one case but not the other.
```

##### ↳ ↳ Re: Calculation Errors - Machine Dependent?

- **From:** Mic <mic0@eircom.net>
- **Date:** 2005-02-08T08:58:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<04%Nd.47112$Z14.32269@news.indigo.ie>`
- **In-Reply-To:** `<VuRNd.1135412$B07.160154@news.easynews.com>`
- **References:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com> <VuRNd.1135412$B07.160154@news.easynews.com>`

```
Had the same problem with another compiler a couple of year ago turned 
out to be the debugger was cleaning up incorrectly initialised 
variables, presumably in order to allow their values to be inspected.
As far as I recall, the problem was with data items that are not usage 
display, which would not be correctly initialised with a plain vanilla 
initialize statement.

William M. Klein wrote:
> My *guess* is that
> 
…[7 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Calculation Errors - Machine Dependent?

- **From:** j6vflbl6vy6g8o001@sneakemail.com
- **Date:** 2005-02-08T17:49:15-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1107913755.069549.143080@l41g2000cwc.googlegroups.com>`
- **References:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com> <VuRNd.1135412$B07.160154@news.easynews.com> <04%Nd.47112$Z14.32269@news.indigo.ie>`

```
We've had exactly this same experience (as described by "Mic" above).

When you run Animator, it "cleans up" some stuff and/or implicitly uses
different compiler options.

Likely it's the uninitialized variables issue.  What we've done in
extreme cases is had to resort to the old tried and true method of
putting display statements throughout the program.  Ugh.  But, get's
the job done.

A few times throughout the years have also run into compiler bugs where
this was necessary because they wouldn't reveal themselves via
Animator, but as soon as you compiled to .exe or .dll, blamo!
```

#### ↳ Re: Calculation Errors - Machine Dependent?

- **From:** Peter Lacey <lacey@mb.sympatico.ca>
- **Date:** 2005-02-07T23:12:07-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42084A26.4079BF3A@mb.sympatico.ca>`
- **References:** `<1107808928.968053.86680@o13g2000cwo.googlegroups.com>`

```
"Mark K." wrote:
> 
> 
…[9 more quoted lines elided]…
> 


This is a long shot but - with a very old compiler I found that the
interface with the the GUI handler had to be loaded even though the
program was purely batch; the problem was the same as yours! 
Calculations going wrong!  If you animate the program, the GUI portion
is obviously loaded.

PL
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
