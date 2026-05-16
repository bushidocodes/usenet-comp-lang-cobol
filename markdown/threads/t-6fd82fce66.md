[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# In search of a PL/I - COBOL for OS/390 comparison

_2 messages · 2 participants · 1999-10_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Re: In search of a PL/I - COBOL for OS/390 comparison

- **From:** robin <robin_v@bigpond.com>
- **Date:** 1999-10-11T00:00:00
- **Newsgroups:** comp.lang.pl1,comp.lang.cobol
- **Message-ID:** `<nGuM3.2730$_4.4950@newsfeeds.bigpond.com>`

```
From: "William M. Klein" <wmklein@nospam.netcom.com>, 
MindSpring EnterprisesDate: Sat, 9 Oct 1999 11:38:48 -0500
robin <robin_v@bigpond.com> wrote in message
news:CpIL3.1233$_4.2153@newsfeeds.bigpond.com...
>> "William M. Klein" <wmklein@nospam.netcom.com> writes:
>> > Also note that the copyright date on that book is 1977.  This is 8 years
…[10 more quoted lines elided]…
>> > PL/I

"few" years?  Surely you're not referring to X3.74 of 1987,
some ten years later?

> - and said that it was "functionally" frozen as a programming
>> >language
…[9 more quoted lines elided]…
> Mainframe PL/I compilers.

There's nothing new in this.  IBM's OS PL/I Version 2 object code was
incompatible with Version 1 object code, owing to changes with certain
library functions.

Also, different interfaces with various operating systems required
different object code for each different version.

>  Also, as far as I know, this NEW (incompatible)
> version of IBM's mainframe PL/I compiler

AFAIK, it's a new compiler, not a new version of the existing IBM Mainframe
compiler.

> finally has support for ANSI/ISO
> conforming PL/I (conforming to the now functionally stabilized compiler) even
> though most IBM PL/I programmers "hate" having PL/I behave (or limited) to
> Standard syntax and functionality.

That's their preference, of course.

> Even so, I still would say that there have been MORE significant changes to
> the IBM mainframe COBOLs than to the IBM mainframe PL/I compilers - since
> 1977.

What changes to IBM COBOL since 1977 do you think would affect Tucker's
ratings of COBOL vs PL/I ?  Bearing in mind that PL/I was then streets
ahead of COBOL in the areas cited.

>  However, that is a matter of opinion - but whatever you think about
> the amount or type of change, it is certainly true that any comparison made
> in 1977 has little to do with the language advantages, structure, or uses
>today.

See above.

---
Bill Klein
```

#### ↳ Re: In search of a PL/I - COBOL for OS/390 comparison

- **From:** "John W. Kennedy" <rri0189@attglobal.net>
- **Date:** 1999-10-12T00:00:00
- **Newsgroups:** comp.lang.pl1,comp.lang.cobol
- **Message-ID:** `<38037DE8.2C7E6468@attglobal.net>`
- **References:** `<nGuM3.2730$_4.4950@newsfeeds.bigpond.com>`

```
robin wrote:
> There's nothing new in this.  IBM's OS PL/I Version 2 object code was
> incompatible with Version 1 object code, owing to changes with certain
> library functions.

That was not generally true, although some PLRSHR configurations,
including ours, had problems.  I wrote a high-speed delinker program
that stripped the runtime from all our load modules and relinked them
with the V2 library; we ran it one Sunday afternoon and were up again
with no problems on Monday morning, except for one group of programs
that someone had, for no particular reason, linked with the NOEDIT
option (which discards all the ESD information and consolidates
everything into one large control section); those, naturally, had to be
recompiled.
 
> AFAIK, it's a new compiler, not a new version of the existing IBM Mainframe
> compiler.

Yes.  It uses the Toronto compiler engine that was already being used by
C and C++ for MVS, OS/2 and Windows and by PL/I for OS/2 and Windows. 
Some of us have been expecting the MVS PL/I version for five years or
longer.
 
> What changes to IBM COBOL since 1977 do you think would affect Tucker's
> ratings of COBOL vs PL/I ?  Bearing in mind that PL/I was then streets
> ahead of COBOL in the areas cited.

COBOL 85 at least makes a decent attempt at structured code.  However,
just as with COBOL 59->COBOL 60, COBOL 60->COBOL 68, and COBOL 68->COBOL
74 before, COBOL 74->COBOL 85 entails radical incompatibilities with the
prior dialect (including many cases where the same valid source has a
different meaning), and, without the aid of a translation program, can
be used only with code written de-novo.  My old employer was still using
99% COBOL 68 in 1995 or so, since no-one wanted to make a new COPY
library.

The COMPUTE statement also remains, in effect, a random-number
generator, since intermediate precision is undefined.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
