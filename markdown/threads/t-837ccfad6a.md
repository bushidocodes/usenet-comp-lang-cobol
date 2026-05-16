[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol->C or Linux Compiler

_14 messages · 7 participants · 1994-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Re: Cobol->C or Linux Compiler

- **From:** draegerr@Informatik.TU-Muenchen.DE (Ralf Draeger)
- **Date:** 1994-12-05T12:59:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com>`

```
mfoley@infinet.com (Mark Foley) writes:

>Pieter Hintjens (pahint@eunet.be) wrote:
>: Realia is probably the best Cobol compiler I ever used, so you know what
…[5 more quoted lines elided]…
>: mean it may not take years.

>I agree with Pieter, "limited aims". My personal goal would be a translator
>which could be used to "port" COBOL programs to a new platform, and use
…[11 more quoted lines elided]…
>we have to buy it, we might as well just buy a COBOL compiler.

Hi there,

I agree with Pieter, too, but why not use the GNU as translation platform?
As far as I know GNO as availible on most systems, so it would be the best
way to make the code portable. Flame me if wrong, but I think, once you
have ported the GCC to a platform all the stuff you need (eg. BISON) is also
availible, and so a COBOL-compiler based on GCC-translation or even some
other GNO-product will be the most easy way to solve the problem.

Btw, if I can do something for the project, tell me, I'd like to help.

CU, Ralf.
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** pahint@eunet.be (Pieter Hintjens)
- **Date:** 1994-12-06T21:12:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D0EqxE.7wB@Belgium.EU.net>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de>`

```
Ralf Draeger (draegerr@Informatik.TU-Muenchen.DE) wrote:
: mfoley@infinet.com (Mark Foley) writes:
: >Pieter Hintjens (pahint@eunet.be) wrote:
: >: a Cobol-to-C convertor, as I see it, has limited aims that are compatible
: >: with a non-optimal solution.  These limited aims (such as a simple syntax)
: >: mean it may not take years.

: Hi there,
: I agree with Pieter, too, but why not use the GNU as translation platform?
: As far as I know GNO as availible on most systems, so it would be the best
: way to make the code portable. Flame me if wrong, but I think, once you
: have ported the GCC to a platform all the stuff you need (eg. BISON) is also
: availible, and so a COBOL-compiler based on GCC-translation or even some
: other GNO-product will be the most easy way to solve the problem.
: Btw, if I can do something for the project, tell me, I'd like to help.
: CU, Ralf.

Ralf, thanks for joining the discussion.

I did not realise so many people were interested in this project.
It seems that the majority are looking for a true-GNU Cobol, and
I have to agree that this is clearly the best solution.  I don't
know how GCC works, so GNO is gnuws to me.  Terrible, I gnow.

My short-term goals remain: to produce a Cobol-to-C translator,
compatible with the C compilers I have on various systems.  First
off, I believe that this is a necessary step on the way to a true
compiler.  Secondly, I think it will be fun in itself.  Thirdly,
it will provide something tangible sooner.  Fourthly I am itching
to prove Robert Dewar wrong.  I don't accept his opinions that
this work is 'much harder than compiling to machine code' and
'years of work'.  Yo, we'll see.

So, the *REAL* problem is... What are we going to call it?
Keith Horowitz suggested various 'cob*' names.  I thought of
a few '*bol' names.  Like: gnubol, freebol, orribol, cbol,
smallbol, cnobol, robol, ...

Send me your opinions, or post here!
```

##### ↳ ↳ Re: Cobol->C or Linux Compiler

- **From:** cgodwin@ibm.net (Charles Godwin)
- **Date:** 1994-12-07T00:21:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c2v66$hho@news-s01.ny.us.ibm.net>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <D0EqxE.7wB@Belgium.EU.net>`

```
>So, the *REAL* problem is... What are we going to call it?

How about naming it BOLUX?

I think that would be a snappy title.


Charles Godwin
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

- **From:** pahint@eunet.be (Pieter Hintjens)
- **Date:** 1994-12-08T19:34:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D0IBp1.I82@Belgium.EU.net>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <D0EqxE.7wB@Belgium.EU.net> <3c2v66$hho@news-s01.ny.us.ibm.net>`

```
Charles Godwin (cgodwin@ibm.net) wrote:
: >So, the *REAL* problem is... What are we going to call it?
: How about naming it BOLUX?
: I think that would be a snappy title.

BOLUX it is, Charles.  I take it you've not trademarked the name?
World, await BOLUX 1.0 with trembling keyboard!!
```

##### ↳ ↳ Re: Cobol->C or Linux Compiler

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-08T15:17:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c7pku$dul@gnat.cs.nyu.edu>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net>`

```
"I am itching to prove Robert Dewar wrong"

fine, by all means try to do so! Just remmeber however, that in ANY
compiler (and a COBOL to C translator is just a compiler that happens
to generate C instead of machine language), syntax is absolutely
trivial compared to semantics, so the idea that simplifying the COBOL
syntax will help is a false path. Now simplifying the SEMANTICS by
taking a severe semantic subset will help. 

Thought: in COBOL there are 9-11 different formats for integers, compared
to only 2 in C -- it is this sort of thing that makes the translation
difficult.
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

- **From:** pahint@eunet.be (Pieter Hintjens)
- **Date:** 1994-12-10T12:31:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D0LHGJ.27n@Belgium.EU.net>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu>`

```
Robert Dewar (dewar@cs.nyu.edu) wrote:
: Thought: in COBOL there are 9-11 different formats for integers, compared
: to only 2 in C -- it is this sort of thing that makes the translation
: difficult.

How do you count 9-11 different types of integer?  Cobol requires DISPLAY
and COMP, plus various formatted fields that are not numeric at all.  COMP
is implementation dependent, so can be pure binary.  That makes 2 types,
unless I missed something.  Also, what are the '2' types of integer in C?
Last time I looked, I saw bytes, words, and longs, plus floating point
which is not integer at all.
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 4)_

- **From:** Richard_Plinston@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1994-12-11T22:28:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3294344.80915.1448@kcbbs.gen.nz>`
- **References:** `<D0LHGJ.27n@Belgium.EU.net>`

```

>unless I missed something.  Also, what are the '2' types of integer in C?
>Last time I looked, I saw bytes, words, and longs, plus floating point
>which is not integer at all.

short and long, where int is one of these.

bytes are not integer, they are char.
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 4)_

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-12T00:14:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cgm76$38k@gnat.cs.nyu.edu>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu> <D0LHGJ.27n@Belgium.EU.net>`

```
Pieter is puzzled by my note that there are many different formats of 
integer data in COBOL, and further more notes that there are several
different integer formats in C (int, short etc).

Well, where do we start. First in a typical C compiler, all the integer
types are the same format, just different lengths, typically 2's complement
binary, with the natural endianness of the machine.

When I said there were several different formats in COBOL, I was not
talking about size, if you include size, then typical COBOL compilers
implement hundreds of different integer formats.

The typical types are

  COMP (binary)
  COMP (packed decimal)
  COMP (packed decimal unsigned -- different sign nibble in IBM format)
  DISPLAY (unsigned)
  DISPLAY SIGN IS LEADING
  DISPLAY SIGN IS LEADING SEPARATE
  DISPLAY SIGN IS TRAILING
  DISPLAY SIGN IS TRAILING SEPARATE

that's 8. If you would count C's types int and unsigned as separate, then
you should have two entries for COMP binary (signed and unsigned).

In addition, some compilers may support additional COMP formats (for
instance Realia COBOL supports both little endian and big endian
binary formats, signed and unsigned).

A COBOL translator must deal with all these formats. It can be done by
conversion to a canonical format for all types, but that's quite inefficient.

Note that when it come to ADD A B GIVING C
there are something like 500 different format combinations (and this is not
counting different lengths).
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 5)_

- **From:** pahint@eunet.be (Pieter Hintjens)
- **Date:** 1994-12-13T17:35:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D0rFIL.CrK@Belgium.EU.net>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu> <D0LHGJ.27n@Belgium.EU.net> <3cgm76$38k@gnat.cs.nyu.edu>`

```
Robert Dewar (dewar@cs.nyu.edu) wrote:
: Pieter is puzzled by my note that there are many different formats of 
: integer data in COBOL, and further more notes that there are several
: different integer formats in C (int, short etc).

: Well, where do we start. First in a typical C compiler, all the integer
: types are the same format, just different lengths, typically 2's complement
: binary, with the natural endianness of the machine.

 So we agree that in C there is just 1 integer format?

: When I said there were several different formats in COBOL, I was not
: talking about size, if you include size, then typical COBOL compilers
: implement hundreds of different integer formats.

: The typical types are

:   COMP (binary)
:   COMP (packed decimal)
:   COMP (packed decimal unsigned -- different sign nibble in IBM format)
:   DISPLAY (unsigned)
:   DISPLAY SIGN IS LEADING
:   DISPLAY SIGN IS LEADING SEPARATE
:   DISPLAY SIGN IS TRAILING
:   DISPLAY SIGN IS TRAILING SEPARATE

: that's 8. If you would count C's types int and unsigned as separate, then
: you should have two entries for COMP binary (signed and unsigned).

: In addition, some compilers may support additional COMP formats (for
: instance Realia COBOL supports both little endian and big endian
: binary formats, signed and unsigned).

This is for reasons of 'compatibility' with either IBM or x86 systems, and
is not relevant to a Cobol-to-C tool.

: A COBOL translator must deal with all these formats. It can be done by
: conversion to a canonical format for all types, but that's quite inefficient.

Who says we need to deal with all these formats?  Hands-up who needs packed
decimal unsigned...  Hmm, I thought so.  And don't the majority of compilers,
including Realia, convert all numbers to a canonical format (floating point)
for most non-trivial operations?

: Note that when it come to ADD A B GIVING C
: there are something like 500 different format combinations (and this is not
: counting different lengths).

I don't think it is useful to try to overstate the problem here.  It is
true that Cobol is full of wierd things, like SIGN IS SEPARATE LEADING,
but it's quite okay, IMO, that you convert these into a canonical format
so long as the important datatypes like binary are treated with respect.
I've seen comercial compilers which handled a statement 'ADD 1 TO A', where
A was a binary 16-bit word, as:
    
    TAKE A, CONVERT TO FLOATING POINT
    TAKE 1, CONVERT TO FLOATING POINT 
    ADD BOTH FLOATING POINT VALUES
    ROUND-OFF TO 3 DIGITS (A was defined as S9(3) COMP-4)
    CONVERT RESULT TO BINARY
    STORE IN A

If a serious company generates code like this, I'll be happy when my C
code says 'A++'.
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 6)_

- **From:** neth@granda.zk3.dec.com (Craig Neth USG)
- **Date:** 1994-12-14T20:20:57+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cnk39$33u@jac.zko.dec.com>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu> <D0LHGJ.27n@Belgium.EU.net> <3cgm76$38k@gnat.cs.nyu.edu> <D0rFIL.CrK@Belgium.EU.net>`

```

In article <D0rFIL.CrK@Belgium.EU.net>, pahint@eunet.be (Pieter Hintjens) writes:

>Who says we need to deal with all these formats?  Hands-up who needs packed
>decimal unsigned...  Hmm, I thought so.  And don't the majority of compilers,
>including Realia, convert all numbers to a canonical format (floating point)
>for most non-trivial operations?

You might be suprised 'who needs' such things.   Just about _any_
non-trivial COBOL program will use at least one of the DISPLAY formats.

And I think I'd disagree with you that a 'majority' of compilers use
floating-point for non-trivial operations.   

Most serious compilers either use special machine instructions or have
special runtime routines that are hand crafted to work natively on 
the decimal types even if no decimal machine instructions are present. 

>: Note that when it come to ADD A B GIVING C
>: there are something like 500 different format combinations (and this is not
…[5 more quoted lines elided]…
>so long as the important datatypes like binary are treated with respect.

There is a large body of COBOL code out there that does NOT use binary at
all (a lot of it was written for IBM machines).   Still, it's a reasonable
assumption to make that you can use your canonical form for some of the
myriad of combinations.   

FWIW, If you want your translator to be useful/used, it will need to support
a big pile of stuff you probably don't even know exists yet.  There are
lots of weird nooks and crannies in this language. Just wait 'till you 
start looking at CANCEL :-)

I wish you a lot of luck, but even doing a reasonable job on a subset
of this language is, IMHO, a big job.   

Craig (who worked on and was project/technical lead on a serious COBOL 
       compiler team for 8 years)
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 6)_

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-14T23:25:03-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cogev$8rb@gnat.cs.nyu.edu>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu> <D0LHGJ.27n@Belgium.EU.net> <3cgm76$38k@gnat.cs.nyu.edu> <D0rFIL.CrK@Belgium.EU.net>`

```
Pieter, if you really think that it is OK to use floating-point as the
universal intermediate form, there is *really* a lot you don't understand
(and I certainly trust that there aren't compiler companies around that
would make this elementary mistake).

On most machines (the PC is really the sole exception), IEEE floating-point
provides only 53 mantissa digits, which of course is not enough to 
accomodate the required maximum COBOL precision. Even converting shorter
values that fit is fraught with round off errors (since IEEE typically
rounds to nearest even for example).

No doubt you will say (who needs anything but a PC anyway?) but I do seem
to rememberr *something* was said about the reason for COBOL-to-C being
interesting was that it was portable, which presumably means it runs on
more than one machine :-)

As for the integer types, I merely pointed out that there were lots of
different integer formats, unlike C.

Your response seems to be, true there are, but we will simply ignore some
of them.

I thought the idea was COBOL to C here, if on the other hand it is
whatever-subset-of-COBOL-I-can-figure-out-how-to-translate-easily to C
then the project does become simpler, in fact it becomes arbitrarily
much easier, but don't advertise it as COBOL to C!

I think it is even a mistake to ignore commonly supported COMP types,
since they are widely used.

As for unsigned packed decimal (that is for example

    05  COUNT  PIC 999 COMP-3.

maybe you write VERY different COBOL code than I do, but this is pretty
common usage in both programs I have written, and those that I have looked
at.

SIGN IS TRAILING SEPARATE is also widely used. Indeed it is hard for me
to really decide that ANY of the formats are useless. Probably
SIGN IS LEADING (with no SEPARATE) is rarely used, but I have seen
it used in real programs.

I guess the fundamental point is to understand the scope of the 
intended project. Tiny subsets of COBOL are easy enough to implement,
they are also of extermely dubious utility in my view. What are we talking
about here? A tool that allows dealing with existing COBOL programs, or
a tool that allows new programs to be written in a small COBOL subset. The
latter does not seem terribly interesting to me, although it is undoubtedly
an interesting project to *work* on!
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 6)_

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-14T23:27:49-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cogk5$8s2@gnat.cs.nyu.edu>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu> <D0LHGJ.27n@Belgium.EU.net> <3cgm76$38k@gnat.cs.nyu.edu> <D0rFIL.CrK@Belgium.EU.net>`

```
By the way Pieter, you label binary as an "important COBOL datatype", but
actually COBOL has no such datatype. It allows for the possibility of an
implementation adding such types, via COMP (IBM calls big-endian binary
COMP-4), but this is not standard COBOL at all, and this is why a lot of
programs stay away from binary completely, it's not portable. So if your
goal is high portability, I wonder why you would bother with non-portable
stuff!
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 4)_

- **From:** 6848830@LMSC5.IS.LMSC.LOCKHEED.COM
- **Date:** 1994-12-14T14:22:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1708CCA3CS86.6848830@LMSC5.IS.LMSC.LOCKHEED.COM>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu> <D0LHGJ.27n@Belgium.EU.net>`

```
In article <D0LHGJ.27n@Belgium.EU.net>
pahint@eunet.be (Pieter Hintjens) writes:
 
>
>Robert Dewar (dewar@cs.nyu.edu) wrote:
…[12 more quoted lines elided]…
>Pieter A. Hintjens
 
Oh yeah?  Well how about comp-3.  There are native assemler instructions
that beg for comp-3 variables, such as ZAP, (zero add packed).  And
on the intel side, comp-5, reverse-byte integers.  And then there's
(drum roll please) on the IBM floating point!  comp-4 and comp-8.
And with cobol-85, you get the packed-decimal keyword, the binary or
native keyword.
 
But to get back to the original thread, It probably is harder to do a cobol
compiler since it has so many syntax options and is wordy.  While C has
few syntax options and relies heavily on function calls.  For example,
in cobol, to read a sequential file you would:  (some stuff excluded for
brevity, I want to finish typeing before I loose all my hair)
 
identification division.
program-id.
author. chris mason.
date-compiled.
environment division.
select gerbils-file
  assign to "cute-little-mammal-external"
   file status is ws-file-status.
data division.
file section.
fd  gerbils-file
    data record is gerbils-rec.
01  gerbils-rec   pic x(100).
working-storage section.
01  ws-file-status pic x(02).
a000-main.
    open input gerbils-file.
    Read next record gerbils-file.
    close gerbils-file.
    stop run.
 
versus:
#include <stdio.h>
main()
{
   char buffer_in[101];
   FILE *gerbils_file;
   gerbils_file = fopen("input.txt", "rt");
   fgets(gerbils_file,100, buffer_in);
   fclose(gerbils_file);
}
 
Notice that most of the C stuff is function calls.  While modern COBOL
compilers probably produce function calls after translation, the translation
is harder, since it isn't just a function call, but parsing the syntax
to figure out which cobol runtime library calls to do...
 
For example, in C the compiler produces this in the object module:
    _fopen and stuff. A call to _fopen which is a subroutine in a library.
 
But cobol produces the call:
    _opensezme  (okay, i don't know what the exact run time module is)
And it produces this after it performs (no pun intended) the translation
    of open input gerbils-file.
Here it has to keep track of tokens open, input and gerbils-file.  In
C you merely call the function as named and pass the parms.  IN cobol
you translate keywords such as input to form the parms you will pass
to the functions.
 
You could almost say the the cobol compiler has to do more translation
and work than the C compiler does.  After all, there are several more
keywords and different contexts for then than in C.
 
Chris Mason
"The Unknown COBOL Programmer"
The opinions expressed are mine, not my Employers.
      6848830@lmsc5.is.lmsc.lockheed.com
LMSC5:  Tons of Beautiful Big Blue Iron...
```

###### ↳ ↳ ↳ Re: Cobol->C or Linux Compiler

_(reply depth: 5)_

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-14T23:29:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cogo2$8t1@gnat.cs.nyu.edu>`
- **References:** `<S1070235.45.2ED12195@cedarville.edu> <3auf3l$i6h@news.halcyon.com> <3b8utm$r41@rigel.infinet.com> <CzxLHJ.8s6@Belgium.EU.net> <3bf9cr$5qq@gnat.cs.nyu.edu> <D01I1z.8y7@Belgium.EU.net> <3bh545$h27@rigel.infinet.com> <3bv2qq$a94@hpsystem1.informatik.tu-muenchen.de> <D0EqxE.7wB@Belgium.EU.net> <3c7pku$dul@gnat.cs.nyu.edu> <D0LHGJ.27n@Belgium.EU.net> <1708CCA3CS86.6848830@LMSC5.IS.LMSC.LOCKHEED.COM>`

```
Chris reminds me that the latest COBOL standard HAS added PACKED DECIMAL
and BINARY, I forgot that, so my list of integer formats was too small, it
was the old fashioned COBOL 74 list, and the current version is larger.

Of course it is still the case that the use of BINARY is potentially
non-portable.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
