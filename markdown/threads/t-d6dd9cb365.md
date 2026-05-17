[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol->C or Linux Compiler

_13 messages · 5 participants · 1994-11 → 1994-12_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Migration and conversion`](../topics.md#migration)

---

### Cobol->C or Linux Compiler

- **From:** "s107..." <ua-author-107590@usenetarchives.gap>
- **Date:** 1994-11-21T17:39:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```

I just read the FAQ and it says that there is no Linux Compiler available...
well that sucks. It also doesnt mention any Cobol to C converters or any
other language for Linux.
I am a student in COBOL (uhhh yes they still teach it in schools,
unfortunatly for those of us taking it) and I want to be able to write some
scripts for my Linux machine for my WWW Server. At the moment we dont have
a Cobol compiler or a Cobol translater. Could someone direct me to where I
can get such a thing or find out what I can do to get my cobol programs to
run on Linux?

-Tyler
/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥/¥
| s10··.@ced··e.edu Member of the Electronic Frontier Foundation |
| A Small Christian College Computer Information Systems Major |
| In The Middle of Ohio. Aka: Gecko, The Highlander, Timber Wolf |
| URL: http://www.cedarville.edu/DPMA/Cedarville.html <-- Try it! |
|Views Expressed Are My Own And Not Necessarily The Schools. PGP-Key Avail.|
+--------------------------------------------------------------------------+
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-11-27T09:56:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p2@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Mark Foley (mfo··.@inf··t.com) wrote:
: Another poster (I don't know who), mentioned that they were interested
: in looking into developing a COBOL to C translator "in a year or 5". I
: too have thought about this. The advantage with this is that it would
: "run" on any platform, including Linux (although source level debugging
: would be a nighmare). Also, 3rd party ISAM routines could be bolted in
: later depending on what was used on a given platform: Btrieve, c-tree,
: etc. I am still mildly interested in pursuing this....

T'was I. I do a lot of work in Cobol and am usually frustrated by the
(lack of) quality of the various compilers I have to use. I started a
Cobol-to-C convertor, and got as far as a limited parser using Lex/Yacc.

My own needs for Cobol are limited to a subset of ANSI 74, with some way
to access sequential files, and 3rd party ISAM, as you say.

If anyone thinks they can contribute to such a project, let's organise.
Cobol to C is probably the simplest way to provide some kind of Cobol
support for Linux and other machines that have great C compilers.
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "chr..." <ua-author-9632510@usenetarchives.gap>
- **Date:** 1994-11-27T16:32:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p3@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
In article , wrote:

› : At the moment we dont have a Cobol compiler or a Cobol translater.
› : Could someone direct me to where I can get such a thing or find out what
› : I can do to get my cobol programs to run on Linux?

The best bet at moment looks like running an MSDOS compiler in DOSEMU or
a UNIX/386 one with iBCS2: I tried the MF Cobol/2 v1.3 for UNIX a few
months ago which seemed to work. Of course you don't save any money.

In article <3b8utm$r.··.@rig··t.com>, Mark Foley
wrote:

› Another poster (I don't know who), mentioned that they were interested
› in looking into developing a COBOL to C translator "in a year or 5". I
…[5 more quoted lines elided]…
› folks would be willing to collaborate? 

If anyone is thinking of writing a COBOL->anything translator, can
I throw in a nearly working parser, which will at least save some
typing. I started it a few years ago, intending to do better
checking than the compiler did (using un-initialised variables
etc.) It parses some programs OK, others not, but I never had time
to sort it out & the compilers are better now :-)

I've offered it privately to a couple of people: if anyone is interested
mail me -- I'd like to see some use made of it!

› Here's a thought to get started:
› One of the biggest thorns-in-the-side would be translating the COBOL
› perform statment to *something* in C:
›

Since I wrote most of the code in my company, I know the parser
won't have to cope with this sort of thing :-) But wouldn't be
easier to keep a similar structure:

while( horrible_condition ) {
funct1();
funct2();
funct3();
funct4();
...
functn();
}

Of course all the variables have to be global .... mmmm it would end up
looking like lowercase COBOL.


Chris Benson
Work: chr··.@stu··o.uk
Home: chr··.@jes··o.uk
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-11-28T14:37:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p4@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Mark Foley (mfo··.@inf··t.com) wrote:
: I'm no lex/yacc expert, but I think a Cobol grammer would be really tough
: to do with lex/yacc. But then again, I'm no lex/yacc expert. Any experts
: out there who want to give it a shot? Pieter - perhaps you could email me
: your parser, or put it on some ftp site (a Linux site?) so that the throngs
: of people waiting to participate in this project could look at what you've
: got.
: Anybody know of or have access to a PD packed decimal library? (or want to
: write one?)

I'm going over my parser, which I wrote for MKS lex/yacc, to be sure it
works okay with GNU bison/flex and Unix lex/yacc. I think a *full* Cobol
grammar is close to impossible with lex/yacc, but I think I cracked the
tricky problems of the 88 conditions and weird tests (IF A = B OR C OR
D = F). Also, I don't intend to support GOTO, not for philosophical
reasons, but because it is a real pain. Idem for PERFORM THRU. If you
allow these, you have to play with end-of-procedure return addresses.
If you don't, you can do everything with straight function calls. (Most
compilers generate much nicer code if you never use these constructs.)

I reckon the output of any Cobol->C tool would look a lot like lower-case
Cobol. This is okay, IMHO. I can also think of nice extensions like
embedded 'C' code (in-line assembler?) to add arbitrary functionality.

Right now I do not have an ftp address to post to. Any suggestions? I'm
also willing to email my parser, as soon as it's decent.
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-11-29T12:32:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p5@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
: YOu will never get a good COBOL compiler by following a COBOL-to-C route
: on Linux, no matter how "great" the C compiler is on the target machine.
: The trouble is that COBOL has a much richer semantics at the primitive
: operation level than C. As an indication of this, the Realia COBOL compiler
: uses every instruction in the 286 set, whereas a typical C compiler will use
: only a fraction of these instructions.
... stuff deleted
: Actually if you do want to do a COBOL-to-X translator, it is MUCH easier
: to do COBOL-to-Ada/9X than to do COBOL-to-C.

Realia is probably the best Cobol compiler I ever used, so you know what
you're taking about. I disagree in some respects, though. I don't have
Ada running on my Linux clone, for one thing. Also, Ada practically
includes Cobol as a subset, so it would be *too* easy. Furthermore,
a Cobol-to-C convertor, as I see it, has limited aims that are compatible
with a non-optimal solution. These limited aims (such as a simple syntax)
mean it may not take years.

Probably the ultimate is a true GNU Cobol which uses the existing code
generators. Heck, one step at a time.
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "khor..." <ua-author-17073973@usenetarchives.gap>
- **Date:** 1994-11-30T10:39:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p6@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
This sounds like a project I would be willing to put some time into...
Perhaps a Linux/Dos Cobol interpreter/C converter.
But we need a catchy name for it to be a real project?
Any ideas? (And remeber 'WINE' is taken).
Checking /usr/dict/words for 'cob' I find:
cobalt
cobble
cobblestone
cobra
cobweb
Any sound decent?

[insert standard 'my opinions, not my company' prose]
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "he..." <ua-author-13994185@usenetarchives.gap>
- **Date:** 1994-12-04T05:25:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p7@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```

Hi,

nice to see people thinking about a free
COBOL-compiler/translator.

››››› "Robert" == Robert Dewar writes:

Robert> At the very least I think you would be much better off
Robert> trying to build a new front end for GCC rather than
Robert> doing a COBOL-to-C translator. This has several
Robert> advantages:

You may get in contact with OGOSHI Masami
, who started writing GNU-COBOL some
time ago. I said that progress is slow, but he still may have
some suggestions.

Jochen

   The one good thing about repeating mistakes is you know when to cringe.
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-04T06:50:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p8@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
: While it is true that COBOL can be written in a highly portable way, it is
: a mis-characterization to think of it as a highly portable language.
(...deleted...)
: So I think if you find that COBOL in practice is portable, you are commenting
: on the implementations, rather than on the language itself.

Sorry, Robert, but I gotta disagree. I have written complex programs, like
editors and code generators, parsers, and query/report systems, in Cobol,
which certainly use COMPUTE and signed numbers, and which run on many Cobol
platforms, including: Vax, Realia, Micro-Focus (MS-DOS and Unix), IBM Cobol
II, IBM VS/Cobol, IBM Cobol/400, DG/MV Cobol, Wang VS Cobol, and Bull DPS7.

The portability of Cobol, like any language, depends on the way you use it.
Know what to avoid and what to encapsulate. Of course, it may just be a
coincidence that my software runs on all these platforms; however, if a
language encourages portable implementations, that is just the same as it
being a portable language...
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-06T16:12:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p9@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Ralf Draeger (dra··.@Inf··n.DE) wrote:
: mfo··.@inf··t.com (Mark Foley) writes:
: >Pieter Hintjens (pah··.@eu··t.be) wrote:
: >: a Cobol-to-C convertor, as I see it, has limited aims that are compatible
: >: with a non-optimal solution. These limited aims (such as a simple syntax)
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
I have to agree that this is clearly the best solution. I don't
know how GCC works, so GNO is gnuws to me. Terrible, I gnow.

My short-term goals remain: to produce a Cobol-to-C translator,
compatible with the C compilers I have on various systems. First
off, I believe that this is a necessary step on the way to a true
compiler. Secondly, I think it will be fun in itself. Thirdly,
it will provide something tangible sooner. Fourthly I am itching
to prove Robert Dewar wrong. I don't accept his opinions that
this work is 'much harder than compiling to machine code' and
'years of work'. Yo, we'll see.

So, the *REAL* problem is... What are we going to call it?
Keith Horowitz suggested various 'cob*' names. I thought of
a few '*bol' names. Like: gnubol, freebol, orribol, cbol,
smallbol, cnobol, robol, ...

Send me your opinions, or post here!
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-08T14:34:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p10@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Charles Godwin (cgo··.@i··.net) wrote:
: >So, the *REAL* problem is... What are we going to call it?
: How about naming it BOLUX?
: I think that would be a snappy title.

BOLUX it is, Charles. I take it you've not trademarked the name?
World, await BOLUX 1.0 with trembling keyboard!!
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-10T07:31:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p11@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
: Thought: in COBOL there are 9-11 different formats for integers, compared
: to only 2 in C -- it is this sort of thing that makes the translation
: difficult.

How do you count 9-11 different types of integer? Cobol requires DISPLAY
and COMP, plus various formatted fields that are not numeric at all. COMP
is implementation dependent, so can be pure binary. That makes 2 types,
unless I missed something. Also, what are the '2' types of integer in C?
Last time I looked, I saw bytes, words, and longs, plus floating point
which is not integer at all.
```

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-13T12:35:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p12@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
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

: COMP (binary)
: COMP (packed decimal)
: COMP (packed decimal unsigned -- different sign nibble in IBM format)
: DISPLAY (unsigned)
: DISPLAY SIGN IS LEADING
: DISPLAY SIGN IS LEADING SEPARATE
: DISPLAY SIGN IS TRAILING
: DISPLAY SIGN IS TRAILING SEPARATE

: that's 8. If you would count C's types int and unsigned as separate, then
: you should have two entries for COMP binary (signed and unsigned).

: In addition, some compilers may support additional COMP formats (for
: instance Realia COBOL supports both little endian and big endian
: binary formats, signed and unsigned).

This is for reasons of 'compatibility' with either IBM or x86 systems, and
is not relevant to a Cobol-to-C tool.

: A COBOL translator must deal with all these formats. It can be done by
: conversion to a canonical format for all types, but that's quite inefficient.

Who says we need to deal with all these formats? Hands-up who needs packed
decimal unsigned... Hmm, I thought so. And don't the majority of compilers,
including Realia, convert all numbers to a canonical format (floating point)
for most non-trivial operations?

: Note that when it come to ADD A B GIVING C
: there are something like 500 different format combinations (and this is not
: counting different lengths).

I don't think it is useful to try to overstate the problem here. It is
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

#### ↳ Re: Cobol->C or Linux Compiler

- **From:** "pah..." <ua-author-13876471@usenetarchives.gap>
- **Date:** 1994-12-16T13:18:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-d6dd9cb365-p13@usenetarchives.gap>`
- **In-Reply-To:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`
- **References:** `<ua-fallback-bzW88nbBpx0@usenetarchives.gap>`

```
Robert Dewar (de··.@cs.··u.edu) wrote:
: By the way Pieter, you label binary as an "important COBOL datatype", but
: actually COBOL has no such datatype. It allows for the possibility of an
: implementation adding such types, via COMP (IBM calls big-endian binary
: COMP-4), but this is not standard COBOL at all, and this is why a lot of
: programs stay away from binary completely, it's not portable. So if your
: goal is high portability, I wonder why you would bother with non-portable
: stuff!

We probably write very different Cobol, Robert. In the ANSI 74 book, as
far as I remember, it states that COMP is implemented as the most efficient
datatype on the machine. This may be packed decimal, but is most often
binary, as understood by anyone working in assembler or C. So, it's
really no big deal. If I am interested in efficiency, I use COMP. If
I start calculating with display fields or packed decimal in an inner
loop, I have only myself to blame. Only a few biggoted compilers dare
to implement COMP as anything non-optimal. And these (in my experience)
always have a way out via COMP-4 or BINARY.

I'll restate my goal. To compile a useful subset of Cobol which by
coincidence supports the 1,000,000 or so lines of Cobol I manage, and
this via an ANSI C compiler. If operations on display or packed numbers
are slow, I really don't care too much. So long as - I repeat - work
with binary data is fast. As a future goal, a GNU Cobol compiler.

Now you'll have to excuse me, but I don't have as much free time as
you to debate such esoterica. Over and out.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
