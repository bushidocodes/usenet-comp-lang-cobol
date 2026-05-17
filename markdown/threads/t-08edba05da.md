[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New Release Info/24 vs. 31 bit

_6 messages · 6 participants · 1995-09_

---

### New Release Info/24 vs. 31 bit

- **From:** "ehan..." <ua-author-599507@usenetarchives.gap>
- **Date:** 1995-09-08T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<42qth0$j5m@uucp.intac.com>`

```


I'm looking for info on two subjects:

1. Features in the upcoming release of COBOL

2. An explaination of the features of 24 versus 31 bit addressing,
perhaps one that I can make a pointer to, or print out as a reference
for students.

Many thanks.

E-

**********************************************************************
Post office will not deliver without a stamp.
ehancock@intac com e.··.@ing··s.com
http://www.intac.com/â€¾ehancock/eric.html
**********************************************************************
```

#### ↳ Re: New Release Info/24 vs. 31 bit

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1995-09-08T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08edba05da-p2@usenetarchives.gap>`
- **In-Reply-To:** `<42qth0$j5m@uucp.intac.com>`
- **References:** `<42qth0$j5m@uucp.intac.com>`

```
"New release of COBOL?" Are you referring to the announced but as yet not
available (generally at least) IBM COBOL for MVS and VM R2?

If this is the COBOL you are referring to the primary component which it
contains is support for some (?) of the yet to be standardized Object
Oriented COBOL features. Beyond that the features are generally minor
technical improvements.

Some major additions were made by IBM in the separate (but required for
execution) underlying run-time package - LE/370 Release 5. This product
does have an availability date (unlike the COBOL compiler) - September 29,
1995 as I recall.

The LE/370 run time now has added support for FORTRAN components, finally
including the "major" IBM mainframe languages in a single run time
environment, with fair interoperability. With LE Rel 5, COBOL, "C",
PL/I, FORTRAN and "conforming Assembler" can be readily mixed into a
single application stew.

The 24 to 31 bit adressing issue releives mainframe oriented RAM-CRAM,
which has been especially severe in particular cases for years.

In 24 bit mode, it is typical to have a usable addressing range of only 6
MB or so for applications. While this was once considered large, many
problems just will not fit without significant complexity addition. In
one key IBM online system - CICS - all applications share the same address
space, so the problem compounds quickly.

In 31 bit mode, the typical usable addressing range contains the same 6 MB
range (in the 24 bit space), plus an additional usable range of about
2,000 MB in the address range of x01000000 to xFFFFFFFF.

One advantage of very large memory availability to the single program is
the ability to define data structures (of the larger persuasion) diretly
without the need for things such as databases, VSAM files, etc. The
simplicity of being able to pass programs against data rather than data
against programs (reading files) can also make certain class of problems
much simpler.

In the CICS environment, not only can a larger number of applications fit
in the 2000 MB 31-bit space, but the application programs can also be left
in virtual storage, avoiding the high overhead of program loading.

The COBOL/370 (the prior release of COBOL for MVS and VM) General
Information manual has a short explanation with a couple of pictures, but
not much meat. A decent explanation of all the major factors in using
the (1985 vintage) eXtented Architecture (XA) facilities involved in IBM
mainframe 31 bit support takes about 1/2 to 1 hour depending on how much
COBOL orientation is included as opposed to just the operating system /
hardware considerations.

A key factor is that with XA hardware and supporting sofware the function
of all instructions that address memory, and some that manipulate
addresses are now dually defined. The traditional defintion dates to 1964
and defines the behavior in 24 bit mode. The XA definition defines the
behavior when the CPU "gear shift" is in 31 bit mode and addresses are
assumed to be 31 bits long instead of 24.
```

#### ↳ Re: New Release Info/24 vs. 31 bit

- **From:** "7375..." <ua-author-12672612@usenetarchives.gap>
- **Date:** 1995-09-08T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08edba05da-p3@usenetarchives.gap>`
- **In-Reply-To:** `<42qth0$j5m@uucp.intac.com>`
- **References:** `<42qth0$j5m@uucp.intac.com>`

```
When you talk about the "next release of COBOL" - are you asking
about IBM's semi-announced "COBOL for MVS & VM - Release 2" - or
are you talking about the new ANSI/ISO COBOL Standard expected to
be out around 1997?
```

#### ↳ Re: New Release Info/24 vs. 31 bit

- **From:** "gordon...." <ua-author-10958913@usenetarchives.gap>
- **Date:** 1995-09-08T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08edba05da-p4@usenetarchives.gap>`
- **In-Reply-To:** `<42qth0$j5m@uucp.intac.com>`
- **References:** `<42qth0$j5m@uucp.intac.com>`

```
eha··.@in··c.com (Eric D. Hancock) wrote:

› 
› 
…[16 more quoted lines elided]…
› **********************************************************************
I can tell you what will be available in the next release of the Unisys A Series
COBOL85.

We will be getting the National Character Handling Module that is part of the
ANSI standard. We will also get additional support for the interactive debugger.


------------------------------------------------------
Gordon DeGrandis Gor··.@pi··g.be
Contraste Europe S.A. Brussels, Belgium
These are my opinions.
-------------------------------------------------------
Never tell people how to do things. Tell them what to do
and they will surprise you with their ingenuity.
- General George S. Patton
```

#### ↳ Re: New Release Info/24 vs. 31 bit

- **From:** "gl..." <ua-author-3965476@usenetarchives.gap>
- **Date:** 1995-09-12T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08edba05da-p5@usenetarchives.gap>`
- **In-Reply-To:** `<42qth0$j5m@uucp.intac.com>`
- **References:** `<42qth0$j5m@uucp.intac.com>`

```
Eric D. Hancock (eha··.@in··c.com) wrote:


: I'm looking for info on two subjects:

: 1. Features in the upcoming release of COBOL

: 2. An explaination of the features of 24 versus 31 bit addressing,
: perhaps one that I can make a pointer to, or print out as a reference
: for students.

: Many thanks.

: E-

: **********************************************************************
: Post office will not deliver without a stamp.
: ehancock@intac com e.··.@ing··s.com
: http://www.intac.com/â€¾ehancock/eric.html
: **********************************************************************

An earlier reply talked about the 24-bit vs. 31-bit feature, and the
larger address space. Something which you might want to include for your
students is the important consideration that mixing 24-bit and 31-bit
programs can be a very big problem.

Many products written for earlier machines operate in 24-bit mode, or at
least pass parameters, i/o buffers, etc. in the 16-meg protion of the
address space. When compiling and linking a 31-bit capable COBOL you must
know, if you are called or are calling, whether you need to keep linkage
areas in the low/24-bit address area. COBOL-II and beyond give you parameters
to use to force passed areas to be in the low space, and to pass the
addresses in 24-bit format. Without this, your address can get 'wrapped'
from a high space down into the truncated address protion below 16 meg,
with really bad results.

gl··.@mil··m.com
```

##### ↳ ↳ Re: New Release Info/24 vs. 31 bit

- **From:** "r ross-langley" <ua-author-6079657@usenetarchives.gap>
- **Date:** 1995-09-12T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-08edba05da-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-08edba05da-p5@usenetarchives.gap>`
- **References:** `<42qth0$j5m@uucp.intac.com> <gap-08edba05da-p5@usenetarchives.gap>`

```
In article <43584k$3.··.@new··m.COM> gl··.@mil··m.com "Gary Lee" writes:
› Eric D. Hancock (eha··.@in··c.com) wrote:
›› 2. An explanation of the features of 24 versus 31 bit addressing,
…[4 more quoted lines elided]…
› programs can be a very big problem.

'24-bit program' is IBM-speak. Students (especially) should know
that COBOL programs are not measured in bit-lengths; that is just
the object code implementation from a particular compiler.

Reminds me of the IBM habit of referring to '8MB processors' :-)

Richard Ross-Langley
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
