[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# How to do GO TO in AN

_11 messages · 7 participants · 1994-12_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### Re: How to do GO TO in AN

- **From:** marty.tabnik@greatesc.com (Marty Tabnik)
- **Date:** 1994-12-07T21:55:00+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<941207153032107@greatesc.com>`

```

> Message-ID: <3c0nh6$5fn@elan.cs.umd.edu>

> Not using GOTOs is the same kind of extremism as drinking
> decaffeinated coffee (what a name!).  Mr. Dewar has a valid point
> here, that state machines do need GOTOs.  I've written several lexical
> analyzers which all happen to be state machines, and they all use
> GOTOs.  Programming them without GOTOs would be a real disaster.

As would programming them in COBOL -- a language designed for
BUSINESS-oriented applications and not for "lexical analyzers".
---
 * SLMR 2.1a * Flowers!!  Is there a John-Luck-Pickerd here?
```

#### ↳ Re: How to do GO TO in AN

- **From:** vadik@cs.umd.edu (Vadim Maslov)
- **Date:** 1994-12-08T18:52:38-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3c8686$1bv@elan.cs.umd.edu>`
- **References:** `<941207153032107@greatesc.com>`

```
In article <941207153032107@greatesc.com>,
Marty Tabnik <marty.tabnik@greatesc.com> wrote:
>
>> Message-ID: <3c0nh6$5fn@elan.cs.umd.edu>
…[10 more quoted lines elided]…
> * SLMR 2.1a * Flowers!!  Is there a John-Luck-Pickerd here?


You are right. The next question to ask is: Should we really be
programming business applications in COBOL. Too many aspects of 
the language are sick. Too many important concepts (like that
of procedure or functions) are missing from the language.
Why use it at all?

I think this question is being answered by the fact that some
(or many) shops are moving away from COBOL and to more structured
rapod development tools (like PowerBuilder, IEF) or even C++.


Vadim Maslov
```

##### ↳ ↳ Re: How to do GO TO in AN

- **From:** Richard_Plinston@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1994-12-10T02:29:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3294343.8952.13228@kcbbs.gen.nz>`
- **References:** `<3c8686$1bv@elan.cs.umd.edu>`

```
>
>You are right. The next question to ask is: Should we really be
>programming business applications in COBOL. Too many aspects of 
>the language are sick. Too many important concepts (like that
>of procedure or functions) are missing from the language.

In what way are procedures 'missing' ?  Or haven't you heard of
CALL / CANCEL yet ?

>Why use it at all?

It works, it suits the problem set, it is usable by programmers
more interested in the applications than in the inner workings of
the computer.

>
>I think this question is being answered by the fact that some
>(or many) shops are moving away from COBOL and to more structured
>rapod development tools (like PowerBuilder, IEF) or even C++.

Programming departments have been 'moving away from Cobol in droves'
for the last 3 decades.  To PL/I, to 4GLs, to CASE, to the other
latest trendy languages.  Yawn, yet another imminent death notice.
```

##### ↳ ↳ Re: How to do GO TO in AN

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-09T22:46:27-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cb8aj$7hj@gnat.cs.nyu.edu>`
- **References:** `<941207153032107@greatesc.com> <3c8686$1bv@elan.cs.umd.edu>`

```
of course COBOL has procedures, what are you talking about? Never heard
of the CALL verb???
```

###### ↳ ↳ ↳ Re: How to do GO TO in AN

- **From:** ked@mfltd.co.uk (Kev Digweed)
- **Date:** 1994-12-10T14:08:27
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cccor$gfr@icebox.mfltd.co.uk>`
- **References:** `<941207153032107@greatesc.com> <3c8686$1bv@elan.cs.umd.edu> <3cb8aj$7hj@gnat.cs.nyu.edu>`

```

In article <3cb8aj$7hj@gnat.cs.nyu.edu>, dewar@cs.nyu.edu (Robert Dewar) writes:
> of course COBOL has procedures, what are you talking about? Never heard
> of the CALL verb???

Robert - is there any chance that you can include the comments to which you are
responding ? There are about 4 threads with this same title, and you are
responding to them all. It's very confusing!

Cheers,
Kev.
```

###### ↳ ↳ ↳ Re: How to do GO TO in AN

- **From:** vadik@cs.umd.edu (Vadim Maslov)
- **Date:** 1994-12-10T14:38:54-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cd04e$9tq@elan.cs.umd.edu>`
- **References:** `<941207153032107@greatesc.com> <3c8686$1bv@elan.cs.umd.edu> <3cb8aj$7hj@gnat.cs.nyu.edu>`

```
In article <3cb8aj$7hj@gnat.cs.nyu.edu>, Robert Dewar <dewar@cs.nyu.edu> wrote:
>of course COBOL has procedures, what are you talking about? Never heard
>of the CALL verb???
>


I heard, I heard. The problem is I don't see CALLs used in COBOL code
a lot. That is, AFAIK, CALLs and procedures are part of Chapter 10:
Interprogram communication or something like this. My understanding
is, they are used for connecting whole programs and they are more 
close to system/exec calls in C.

What I see used in COBOL code is PERFORMs, paragraphs and sections.
And they strongly encourage writing unstructured code.
So, as I say, the absence of light-weight program units (functions
or procedures) is what really hurts COBOL.

Also, isn't it true that CALL can call only the whole other program,
that is, a PROCEDURE DIVISION of the other program?

Vadim Maslov
```

###### ↳ ↳ ↳ Re: How to do GO TO in AN

_(reply depth: 4)_

- **From:** mgphl@crl.com (Michael G. Phillips)
- **Date:** 1994-12-10T12:55:30-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cd4k2$hjr@crl5.crl.com>`
- **References:** `<941207153032107@greatesc.com> <3c8686$1bv@elan.cs.umd.edu> <3cb8aj$7hj@gnat.cs.nyu.edu> <3cd04e$9tq@elan.cs.umd.edu>`

```
Vadim Maslov (vadik@cs.umd.edu) wrote:
: In article <3cb8aj$7hj@gnat.cs.nyu.edu>, Robert Dewar <dewar@cs.nyu.edu> wrote:
: >of course COBOL has procedures, what are you talking about? Never heard
: >of the CALL verb???
: >


: I heard, I heard. The problem is I don't see CALLs used in COBOL code
: a lot. That is, AFAIK, CALLs and procedures are part of Chapter 10:
: Interprogram communication or something like this. My understanding
: is, they are used for connecting whole programs and they are more 
: close to system/exec calls in C.

	No.  CALLs are (nearly) exactly like C function call, but
	you are always passing the parms by reference (address) instead
	of by value.  The CALLed routine must also be given a parameter
	with which to return any result(s).
	
: What I see used in COBOL code is PERFORMs, paragraphs and sections.
: And they strongly encourage writing unstructured code.
: So, as I say, the absence of light-weight program units (functions
: or procedures) is what really hurts COBOL.

: Also, isn't it true that CALL can call only the whole other program,
: that is, a PROCEDURE DIVISION of the other program?

	Generally, subprograms begin with PROCEDURE DIVISION USING ....
	with a list of data items described in the LINKAGE SECTION.
	You can also use  ENTRY 'SOMENAME' USING ....
	and create a subprogram that contains multiple, CALLable routines.

	Hope this helps,
	-michael
```

###### ↳ ↳ ↳ Re: How to do GO TO in AN

_(reply depth: 5)_

- **From:** vadik@cs.umd.edu (Vadim Maslov)
- **Date:** 1994-12-10T21:01:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cdmi9$a8a@elan.cs.umd.edu>`
- **References:** `<941207153032107@greatesc.com> <3cb8aj$7hj@gnat.cs.nyu.edu> <3cd04e$9tq@elan.cs.umd.edu> <3cd4k2$hjr@crl5.crl.com>`

```
In article <3cd4k2$hjr@crl5.crl.com>,
Michael G. Phillips <mgphl@crl.com> wrote:
>Vadim Maslov (vadik@cs.umd.edu) wrote:
>: What I see used in COBOL code is PERFORMs, paragraphs and sections.
…[13 more quoted lines elided]…
>	-michael

That's what I've read in COBOL standard: you can CALL program and you
are interfacing to PROCEDURE DIVISION USING or ENTRY name USING.
Since a program can have only one PROCEDURE DIVISION (I guess, that's
true), this effectively means that CALL mechanism is for *interprogram
communication* and that it hardly helps in creating a structured
single program. Within a program you only have PERFORM
section/paragraph/sequence of sections/paragraphs.

Using several entry points in one program is equivalent to 
performing paragraphs. Since it does not increase structuredness,
nobody uses it, everybody's using good old PERFORM.

My complaints about absence of procedures in COBOL are not as
groundless as COBOL (that was, that is, and that is coming) advocates
here suggest. There is some effort out there to rationalize COBOL.
As I said before, Intersolv APS S-Cobol takes steps towards
procedural COBOL. However, since they translate to regular COBOL,
their "procedures" prove to be just sections or paragraphs
with a little bit more restrictive semantics.

Vadim Maslov
```

###### ↳ ↳ ↳ Re: How to do GO TO in AN

_(reply depth: 4)_

- **From:** Richard_Plinston@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1994-12-11T22:19:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3294344.80342.1366@kcbbs.gen.nz>`
- **References:** `<3cd04e$9tq@elan.cs.umd.edu>`

```
>
>I heard, I heard. The problem is I don't see CALLs used in COBOL code
…[4 more quoted lines elided]…
>
That depends on how they are used.  They can be used to CALL whole
programs and/or they can be used to CALL utility routines.  I use
both.

Typically, one of my applications will consist of a small control
routine which sits in a CALL / CANCEL loop calling the next program
in turn, at least one of these is a menu program that allows the
user to choose the next functional program.  eg order entry, invoice
print, sales report etc.  These programs then call utility routines
to access common code  eg procedures.

The main routine calls with a common block of data that is easily
accessed by any program that requires it.

As the Call/Cancel gives dynamic loading of routines it is far more 
flexible than C type procedure calling, and allows complete systems
to run in small amounts of memory.

>What I see used in COBOL code is PERFORMs, paragraphs and sections.
>And they strongly encourage writing unstructured code.

In what way do PERFORMs of paragraphs "strongly encourage" unstructured
code ? It may allow gotos and unstructured code, but I don't see it
encouraging it.

>So, as I say, the absence of light-weight program units (functions
>or procedures) is what really hurts COBOL.
>

Try looking at Nested Programs sometime.

>Also, isn't it true that CALL can call only the whole other program,
>that is, a PROCEDURE DIVISION of the other program?
>
One can have other ENTRYs, but in general one would call the
PROCEDURE DIVISION of another routine.  But then the PD has no
minimum size.  Some of my routines are only a few lines long.
```

##### ↳ ↳ Re: How to do GO TO in AN

- **From:** pahint@eunet.be (Pieter Hintjens)
- **Date:** 1994-12-10T12:43:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D0LI0y.2rx@Belgium.EU.net>`
- **References:** `<941207153032107@greatesc.com> <3c8686$1bv@elan.cs.umd.edu>`

```
Vadim Maslov (vadik@cs.umd.edu) wrote:
: ... The next question to ask is: Should we really be
: programming business applications in COBOL. Too many aspects of 
: the language are sick. Too many important concepts (like that
: of procedure or functions) are missing from the language.
: Why use it at all?

The simple truth is that Cobol is an adequate tool for the job, if
used well, and you can use mediocre developers and still produce
applications that run correctly.  The language is (can be) simple
and easily learnt.  Like it or not, it is often more economical
to build an application using Cobol and some simple tools than to
try to build a client-server system using C++ or PowerBuilder.  
IMHO, this says more about the complexity and instability of 
most politically-correct 'modern' development methods than about
the qualities of Cobol.
```

#### ↳ Re: How to do GO TO in AN

- **From:** dewar@cs.nyu.edu (Robert Dewar)
- **Date:** 1994-12-09T17:05:04-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3cakag$sv5@gnat.cs.nyu.edu>`
- **References:** `<941207153032107@greatesc.com>`

```
I beg to differ with Marty who thinks writing lexical analyzers in COBOL would
be a disaster. Realia COBOL is entirely written in COBOL. The code is very clean
and *very* fast. No sign of disaster in the lexical analyzer or anywhere else.
On the contrary writing Realia COBOL in COBOL worked out very well and we 
consider it a real success story.

If you think COBOL is limited to business applications, you either don't know
COBOL, or you have no imagination. Sure it has features that make it poarticularly
useful for fiscal applications, but it is a great mistake not to recognize COBOL
as a wide area language.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
