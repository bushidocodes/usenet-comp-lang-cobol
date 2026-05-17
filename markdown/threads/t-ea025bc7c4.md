[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# PC COBOL Compiler Quality (not what it used to be)

_5 messages · 5 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### PC COBOL Compiler Quality (not what it used to be)

- **From:** "norcom" <ua-author-615725@usenetarchives.gap>
- **Date:** 1998-07-15T05:33:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5K5r1.2$rL1.119189@binary.alaska.net>`

```
Maybe it's just me, but back in the days of yore, the PC compilers that we
used were pretty usable... Maybe that was because they were written by
COBOL guys who understood what COBOL application programming was all about.

Today, they are not-so-swell. For example:

The CA-Realia 16-bit Windows debugger CARCWIND, while efficient to use, only
works on half of the machines around here, and is prone to crash on all of
them from time-to time.

The CA-Realia 32-bit Workbench debugger is, to say the least, far more
cumbersome to use than the old REALDBUG DOS debugger was.

Micro Focus Animator (and their runtimes) are quirky at best, new releases
are frequently buggy or, worse yet, use different defaults than the previous
release so that you have to debug the installation before you can get back
to work. Plus, their documentation always seems to be at odds with the
software they are shipping.

Fujitsu COBOL (the version that we have, at least), won't compile a program
that has anything in columns 73-80, or that has sequence numbers that aren't
in order.

All of the new Windows compilers offer environments that seem to think that
programmers only work on one system, and that there's only one main
executable in that system.

If the compiler vendors keep this up, they'll kill COBOL without any help
from the C and VB guys.

Has anyone else noticed this?
```

#### ↳ Re: PC COBOL Compiler Quality (not what it used to be)

- **From:** "leif svalgaard" <ua-author-6445756@usenetarchives.gap>
- **Date:** 1998-07-14T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea025bc7c4-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5K5r1.2$rL1.119189@binary.alaska.net>`
- **References:** `<5K5r1.2$rL1.119189@binary.alaska.net>`

```

Leif Svalgaard wrote in message <35a··.@new··m.net>...
› I'm attaching a zip file to this post (sorry for you folks that canNOT
› access
› binary
› attachments - I guess your ISP is trying to prevent you from downloading
› pictorial sex
```

#### ↳ Re: PC COBOL Compiler Quality (not what it used to be)

- **From:** "rip..." <ua-author-6589535@usenetarchives.gap>
- **Date:** 1998-07-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea025bc7c4-p3@usenetarchives.gap>`
- **In-Reply-To:** `<5K5r1.2$rL1.119189@binary.alaska.net>`
- **References:** `<5K5r1.2$rL1.119189@binary.alaska.net>`

```
In message <<5K5r1.2$rL1··.@bin··a.net>> "NORCOM" writes:
› used were pretty usable...  Maybe that was because they were written by
› COBOL guys who understood what COBOL application programming was all about.
…[5 more quoted lines elided]…
› them from time-to time.
 
› Yeah, but that is Windows, thank you Microsoft.
 
› Fujitsu COBOL (the version that we have, at least), won't compile a program
› that has anything in columns 73-80, or that has sequence numbers that aren't
› in order.

I used to find sequence numbers (cols 1-6) useful - in the early
70s when the batch editor read a card pack of changes and used them
to amend and insert source code lines.

I have no idea why Fujitsu thinks there is any point to them
for the last 20 years or so.

However you can get it to use free format or not, so col 73-80 can
be resolved.
›
› All of the new Windows compilers offer environments that seem to think that
› programmers only work on one system, and that there's only one main
› executable in that system.
```

#### ↳ Re: PC COBOL Compiler Quality (not what it used to be)

- **From:** "cad..." <ua-author-6589178@usenetarchives.gap>
- **Date:** 1998-07-17T12:03:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea025bc7c4-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5K5r1.2$rL1.119189@binary.alaska.net>`
- **References:** `<5K5r1.2$rL1.119189@binary.alaska.net>`

```
In article <5K5r1.2$rL1··.@bin··a.net>,
"NORCOM" wrote:
› Maybe it's just me, but back in the days of yore, the PC compilers that we
› used were pretty usable...  Maybe that was because they were written by
› COBOL guys who understood what COBOL application programming was all about.
› 
› Today, they are not-so-swell.  For example:
[SNIP]

(Warning - completely shameless plug follows)

Take a look at Acucobol-GT. I've been doing fairly extensive COBOL
development using our tools & have found our compiler to be extremely
reliable. I've had some problems with the runtime (which isn't surprising
given the differences in complexity between the two) but very few are with
non-beta versions & those have been quickly fixed.

The usual information and eval copies can be obtained from
http://www.acucorp.com.
```

#### ↳ Re: PC COBOL Compiler Quality (not what it used to be)

- **From:** "cobol frog (huib klink)" <ua-author-4414632@usenetarchives.gap>
- **Date:** 1998-07-18T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ea025bc7c4-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5K5r1.2$rL1.119189@binary.alaska.net>`
- **References:** `<5K5r1.2$rL1.119189@binary.alaska.net>`

```
NORCOM wrote:

› Maybe it's just me, but back in the days of yore, the PC compilers that we
› used were pretty usable... Maybe that was because they were written by
› COBOL guys who understood what COBOL application programming was all about.

The best compilers I see, were on mainframes. They run, do almost never abend,
showe readable error messages and al this lightning fast

› Today, they are not-so-swell.  For example:
› 
› The CA-Realia 16-bit Windows debugger CARCWIND, while efficient to use, only
› works on half of the machines around here, and is prone to crash on all of
› them from time-to time.

PC's are just like Ferraris, but with Volkswagen motor, chassis and steer. Don't
drive them fast!

› The CA-Realia 32-bit Workbench debugger is, to say the least, far more
› cumbersome to use than the old REALDBUG DOS debugger was.
 
› 32 bit is like a super ferrari.
 
› Micro Focus Animator (and their runtimes) are quirky at best, new releases
› are frequently buggy or, worse yet, use different defaults than the previous
› release so that you have to debug the installation before you can get back
› to work.  Plus, their documentation always seems to be at odds with the
› software they are shipping.

Noticed the release numbering scheme of MF? Three parts, like 3.14.15. With the
third part varying like the decimal digits on the money/liter counters at the
tank stop.

› Fujitsu COBOL (the version that we have, at least), won't compile a program
› that has anything in columns 73-80, or that has sequence numbers that aren't
› in order.
 
› Thats nut compliant to the Current Standard. Some extension switched on?
 
› All of the new Windows compilers offer environments that seem to think that
› programmers only work on one system, and that there's only one main
› executable in that system.

Yeah. As if a COBOL app that servers primary business processes is one big exe
like word or excel or msaccess. Too bad.

› If the compiler vendors keep this up, they'll kill COBOL without any help
› from the C and VB guys.

No, they'll not kill COBOL. But they will keep it from coming to full strength
on non-mainframe platforms, sure. (Unix may be an exception).

› Has anyone else noticed this?
 
› Yes. To many of us.
 
› 
› 
› --
› Kevin J. Hansen
› NORCOM

The COBOL Frog--
Dut: Vandaag is de eerste dag van de rest van je leven! Maak er wat van!
Eng: Today is de first day of the rest of your life! Use it!
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
