[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Pointers in VAX Cobol: Help!

_9 messages · 5 participants · 1997-06_

---

### Pointers in VAX Cobol: Help!

- **From:** "wer..." <ua-author-17072351@usenetarchives.gap>
- **Date:** 1997-06-22T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5omqm6$80n$1@mars.njcc.com>`

```

Does anyone know the syntax/rules of using pointers and dynamic
addressing on VAX Cobol v5? I've got a PL/1 program that is calling a
COBOL program, passing (by reference) the address of a data structure
that will map nicely into a COBOL '01' level.

I thought this would be a simple issue:
1-declare 'MY-POINTER' in linkage section
2-declare 'MY-STRUCTURE' in working storage;
3-PROCEDURE DIVISION USING MY-POINTER
4-SET ADDRESS OF MY-STRUCTURE TO MY-POINTER.

however, the VAX compiler does not support 'SET ADDRESS OF'!!
All documentation I can find shows how to accept data by reference; set
pointers and pass pointers OUT of a COBOL program, but not how to use
pointers passed IN to a COBOL program.

Does the compiler actually support pointers?

What am I doing wrong??

Thanks in advance .......


/Andrew (awe··.@prn··t.com)
```

#### ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-06-22T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p2@usenetarchives.gap>`
- **In-Reply-To:** `<5omqm6$80n$1@mars.njcc.com>`
- **References:** `<5omqm6$80n$1@mars.njcc.com>`

```

Andrew Werden wrote:
› 
› Does anyone know the syntax/rules of using pointers and dynamic
…[8 more quoted lines elided]…
› 4-SET ADDRESS OF MY-STRUCTURE TO MY-POINTER.

A pointer should not even be necessary to use a data structure passed by
reference to a COBOL subprogram:

1-declare 'MY-STRUCTURE' in LINKAGE SECTION of the subprogram
2-PROCEDURE DIVISION USING MY-STRUCTURE

Upon entry to the COBOL subprogram, the linkage section is automatically
mapped in. You can reference any field in MY-STRUCTURE by its local COBOL
definition.

I don't have experience with PL/1, but if the calling program were COBOL you
would say CALL 'SUBPROG' USING MY-STRUCTURE. I also don't have experience in
a VAX environment, but call by reference should not require pointers in
COBOL.

I hope that helps.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

##### ↳ ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "wer..." <ua-author-17072351@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e461bd1ad0-p2@usenetarchives.gap>`
- **References:** `<5omqm6$80n$1@mars.njcc.com> <gap-e461bd1ad0-p2@usenetarchives.gap>`

```

Problem is, the calling program is not passing the data structure, but
rather the address of the data structure. i.e it is doing something like:

CALL 'MYPROG' USING MY-POINTER

I can receive MY-POINTER in linkage section, but then need to use it to
set the base address of MY-STRUCTURE to where the calling program left
it. In IBM-Land, I could do something like

SET ADDRESS OF MY-STRUCTURE TO MY-POINTER (haven't done it in 4 years so
forgive the fuzziness)

How do I do something like this in Vax COBOL??

thanks....
```

#### ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "michael c. kasten" <ua-author-6589049@usenetarchives.gap>
- **Date:** 1997-06-23T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p4@usenetarchives.gap>`
- **In-Reply-To:** `<5omqm6$80n$1@mars.njcc.com>`
- **References:** `<5omqm6$80n$1@mars.njcc.com>`

```

Andrew Werden wrote:
› 
› Does anyone know the syntax/rules of using pointers and dynamic
…[21 more quoted lines elided]…
› /Andrew        (awe··.@prn··t.com)

On an IBM mainframe in Cobol II, you would have to put MY-STRUCTURE in
the LINKAGE SECTION, not in WORKING-STORAGE. Don't pass or receive it
as
a parameter, just declare it in the LINKAGE SECTION.

I suspect the same is true on the VAX, if it can be made to work at all.
Think about it. If something is in WORKING-STORAGE, it already has an
address. The compiler puts it in some particular place, and you can't
move it somewhere else.

In the LINKAGE SECTION, by contrast, nothing has a fixed address.
Everything
is just an empty ghost of an object until you bind it to an address --
either
by receiving it as a parameter or by SET ADDRESS.

As Arnold Trembley has already pointed out, you may not need to do even
this
much, depending on what PL/I is really doing. You say it is passing an
address
by reference. Literally that means it is passing a double pointer, i.e.
the
address of the address of the object. Is that what you really meant?

Michael C. Kasten mc··.@swb··l.net
```

#### ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-06-24T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p5@usenetarchives.gap>`
- **In-Reply-To:** `<5omqm6$80n$1@mars.njcc.com>`
- **References:** `<5omqm6$80n$1@mars.njcc.com>`

```

In article <5omqm6$80n$1.··.@mar··c.com>,
wer··.@plu··c.com (Andrew Werden) wrote:
› 
› I've got a PL/1 program that is calling a COBOL program, passing (by
…[7 more quoted lines elided]…
› Does the compiler actually support pointers?

Different vendors have different ideas about what constitutes supporting
pointers, and VAX CoBOL is rather grudging about it. To the best of my
knowledge, there is no way to dereference a pointer in the language
itself.

This compiler was developed for the VMS environment, and what VMS wants
you to do in this case is simply to put the 01-LEVEL in the LINKAGE
SECTION and pass the pointer by value instead of by reference.

If for some reason, such as not having the source of the calling program,
you can't follow the VMS standard, there is, as I said, no fallback
within the language itself, but what you can do (and it happens often
with C calling programs) is dereference the pointer with an extra CALL,
something like this:

IDENTIFICATION DIVISION.
PROGRAM-ID. DO-SOMETHING.
DATA DIVISION.
LINKAGE SECTION.
01 IN-RECORD-PTR-LS POINTER.
PROCEDURE DIVISION USING IN-RECORD-PTR-LS.
0000-MAIN.
CALL "INTERNAL-ROUTINE" USING BY VALUE IN-RECORD-PTR-LS.
EXIT PROGRAM.

IDENTIFICATION DIVISION.
PROGRAM-ID. INTERNAL-ROUTINE.
DATA DIVISION.
LINKAGE SECTION.
01 IN-RECORD-LS.
05 ...
PROCEDURE DIVISION USING IN-RECORD-LS.
0000-MAIN.
...
9999-EXIT.
EXIT PROGRAM.

END PROGRAM INTERNAL-ROUTINE.
END PROGRAM DO-SOMETHING.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

#### ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-06-24T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p6@usenetarchives.gap>`
- **In-Reply-To:** `<5omqm6$80n$1@mars.njcc.com>`
- **References:** `<5omqm6$80n$1@mars.njcc.com>`

```

Andrew Werden wrote:
› 
› Does anyone know the syntax/rules of using pointers and dynamic
…[21 more quoted lines elided]…
› /Andrew        (awe··.@prn··t.com)

I sent one reply by e-mail, but I am including this posting in the thread.

If MY-POINTER is being passed by reference, then you have the address of an
address. If that's the case, then I believe you should try this:

1-declare 'MY-WS-POINTER' in WORKING-STORAGE as USAGE POINTER.
2-declare 'MY-POINTER' in linkage section as USAGE POINTER.
3-declare 'MY-STRUCTURE' in linkage section
4-PROCEDURE DIVISION USING MY-POINTER, MY-STRUCTURE.
5-SET MY-WS-POINTER TO MY-POINTER
6-SET ADDRESS OF MY-STRUCTURE TO MY-WS-POINTER

This approach is how I would do it in an IBM Mainframe CICS environment.
I don't know how much of this is the same in a VAX environment.

POINTERs can be SET or compared EQUAL to other pointers. There's not much
else you can do with them. If we need to do pointer arithmetic, we redefine
them as PIC S9(9) COMP, but I don't know what the pointer size would be in a
VAX environment. The legal pointer SET statements would be: SET pointer-2
TO pointer-1, SET ADDRESS OF linkage-section-record TO pointer, SET pointer
TO ADDRESS OF linkage-section-record, SET pointer TO NULL.

In my experience (could be wrong, could be specific to IBM environment) the
POINTER used in a SET ADDRESS statement has to reside in the working-storage
section, not the linkage section. The data structure referenced by
"ADDRESS OF" must reside in the linkage section.

If it's legal to directly use a pointer in the linkage section, then the
process would be simpler:

1-declare 'MY-POINTER' in linkage section as USAGE POINTER.
2-declare 'MY-STRUCTURE' in linkage section
3-PROCEDURE DIVISION USING MY-POINTER, MY-STRUCTURE.
4-SET ADDRESS OF MY-STRUCTURE TO MY-POINTER

In either case, MY-STRUCTURE should be an 01 record, and MY-POINTER must be
in a different 01 record, which is the first object in your procedure
division using list. MY-STRUCTURE has to be defined in linkage section,
because you need to address a piece of storage that is not part of your
subprogram.

I don't know if this helps. If "ADDRESS OF" is not supported in your
compiler, I'm open to suggestions for alternate techniques.

Let us know if you find a solution that works.

Arnold Trembley
Software Engineer I (just a job title, still a puzzled programmer)
MasterCard International
St. Louis, Missouri
```

##### ↳ ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "cwes..." <ua-author-13502721@usenetarchives.gap>
- **Date:** 1997-06-25T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e461bd1ad0-p6@usenetarchives.gap>`
- **References:** `<5omqm6$80n$1@mars.njcc.com> <gap-e461bd1ad0-p6@usenetarchives.gap>`

```

In article <33B··.@wor··t.net>,
Arnold Trembley wrote:
› 
› In article <5omqm6$80n$1.··.@mar··c.com>,
…[10 more quoted lines elided]…
› 3-PROCEDURE DIVISION USING MY-POINTER, MY-STRUCTURE.

The USING phrase of the PROCEDURE DIVISION header tells the compiler
which 01-LEVELS in the LINKAGE SECTION will be supplied by the caller.
The compiler then emits code to load the corresponding BLL cell.

The code generated from this USING phrase will always expect two
arguments from the caller, MY-POINTER and MY-STRUCTURE, when in fact you
know that only MY-POINTER will ever be supplied by the caller.

It's true that the generated code can handle missing arguments at run
time, but why specify an argument you know will never be provided? Also,
at a site that uses a tool to match the USING phrases of callers and
callees (which is extremely helpful) this code would be rejected.

A better way is PROCEDURE DIVISION USING MY-POINTER. In addition to the
small run-time savings, it lets the reader know that MY-STRUCTURE is not
an argument supplied by the caller but a DSECT whose BLL cell you intend
to load yourself with a SET ADDRESS statement.


› 4-SET ADDRESS OF MY-STRUCTURE TO MY-POINTER

Unfortunately, VAX CoBOL does not have SET ADDRESS.


Christopher Westbury, Midtown Associates, 15 Fallon Place, Cambridge, MA 02138
```

###### ↳ ↳ ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1997-06-26T20:00:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-e461bd1ad0-p7@usenetarchives.gap>`
- **References:** `<5omqm6$80n$1@mars.njcc.com> <gap-e461bd1ad0-p6@usenetarchives.gap> <gap-e461bd1ad0-p7@usenetarchives.gap>`

```

Chris Westbury wrote:
› 
› The USING phrase of the PROCEDURE DIVISION header tells the compiler
…[10 more quoted lines elided]…
› callees (which is extremely helpful) this code would be rejected.

Please accept my apology for a less-than-accurate posting.

What I intended to emphasize was that, since MY-STRUCTURE was not part of
the subprogram, it had to be defined in the linkage section (because it is a
DSECT). Adding it to the Procedure Division USING list is not correct,
because it is not one of the parameters passed by the calling program. I
should have realized this just by looking at my own CICS programs.

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
St. Louis, Missouri
```

#### ↳ Re: Pointers in VAX Cobol: Help!

- **From:** "gtru..." <ua-author-1163276@usenetarchives.gap>
- **Date:** 1997-06-24T20:00:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-e461bd1ad0-p9@usenetarchives.gap>`
- **In-Reply-To:** `<5omqm6$80n$1@mars.njcc.com>`
- **References:** `<5omqm6$80n$1@mars.njcc.com>`

```

On 23 Jun 1997 21:43:34 GMT, wer··.@plu··c.com (Andrew Werden)
wrote:

› Does anyone know the syntax/rules of using pointers and dynamic 
› addressing on VAX Cobol v5? I've got a PL/1 program that is calling a 
…[18 more quoted lines elided]…
› 
If I understand what you want to do then you're making the problem too
hard, you don't actually have to use pointers in the COBOL program.

Define the structure in the Linkage section, not working-storage. Call
passing the structure by reference from the PL/I program and just use
the data.

George Trudeau, Town of Falmouth
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
