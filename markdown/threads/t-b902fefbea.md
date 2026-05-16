[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL v Other Languages

_15 messages · 11 participants · 1999-08 → 1999-09_

---

### COBOL v Other Languages

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CAC7AC.EC687EAB@home.com>`

```
Through various threads, contributors have said that where necessary
they will use other languages (C, C++, Java etc.) to do things more
effectively than in COBOL.

I don't dispute these claims - but am curious - could you  please give
examples of where you do this in preference to using COBOL, (presuambly
caused by deficiencies in the latter ?)

Jimmy, Calgary AB
```

#### ↳ Re: COBOL v Other Languages

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cad439.6386282@news2.ibm.net>`
- **References:** `<37CAC7AC.EC687EAB@home.com>`

```
On Mon, 30 Aug 1999 17:56:51 GMT, "James J. Gavan" <jjgavan@home.com> wrote:

>Through various threads, contributors have said that where necessary
>they will use other languages (C, C++, Java etc.) to do things more
…[5 more quoted lines elided]…
>

System related high performance functions:  Assembler (S/390)

Processing of arrays comes to mind, it can be way more efficient in PL/I than in COBOL

Also, dynamically growing and shrinking linked lists - it is much easier in Assembler, or
C, or PL/I (in this order, but that is a matter of taste)


Java? Don't know whats good in Java, much less what's better... <eg>

C++?  Oh, come on - I wouldn't write a GUI type OS in COBOL, that's probably where C++
comes in, but given VA COBOL I can write GUI apps in COBOL, and don't have to touch that
ugly sad excuse of a programming language

Interfacing to existing mathematical, statistical, and engineering packages: Fortran,
possibly PL/I

With Kind Regards
Volekr Bandke
with kind regards

Volker Bandke
(BSP GmbH)
```

##### ↳ ↳ Re: COBOL v Other Languages

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1999-08-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cb275e.43907042@news1.ibm.net>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <37cad439.6386282@news2.ibm.net>`

```
On Mon, 30 Aug 1999 19:05:12 GMT, vbandke@ibm.net (Volker Bandke)
wrote:

>On Mon, 30 Aug 1999 17:56:51 GMT, "James J. Gavan" <jjgavan@home.com> wrote:
>
…[12 more quoted lines elided]…
>

The 2.1 COBOL compiler for "This and That" seems to have a MUCH faster
runtime (above the line) on string and table functions than previous
versions.  Have to performed a recent comparison?  Optimization seems
to be particularly good with this compiler.
```

#### ↳ Re: COBOL v Other Languages

- **From:** Mark Framness <framnesso@my-deja.com>
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qjei6$l0t$1@nnrp1.deja.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com>`

```
In article <37CAC7AC.EC687EAB@home.com>,
  "James J. Gavan" <jjgavan@home.com> wrote:
> Through various threads, contributors have said that where necessary
> they will use other languages (C, C++, Java etc.) to do things more
…[3 more quoted lines elided]…
> examples of where you do this in preference to using COBOL,
(presuambly
> caused by deficiencies in the latter ?)

I can not imagine writing device drivers in COBOL.

Also for the most part I feel like doing intensly (e.g. numerically
integrating and such and you don't have to get that complex to feel this
way) mathematical work with COBOL is like a dog walking on its hind
legs, possible but clumsy.

I have a feeling a lot of communications requirements quickly put COBOL
to its limits, maybe not so much on the application side but certainly
on the system side of it all.

While I have done online programming with COBOL (CICS) again I feel that
there are better ways to do online programming.

You need to look at what COBOL means:  COmon Business Oriented Language
and its origin mainframe environments.

COBOL is great for generating reports and for basic business processing
requirements but get out of that environment and you need another tool.

The main problem I have with COBOL is that every variable is global in
scope and that you can not make variables constant (I'm talking about
COBOL II on OS/390 systems) and that you can't break up your source code
into smaller modules.

My favorite feature of COBOL is easily its record oriented I/O approach
which of course comes from the fact that COBOL grew up in a record I/O
hardware environment.
```

##### ↳ ↳ Re: COBOL v Other Languages

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cd5577.38994931@news2.ibm.net>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <7qjei6$l0t$1@nnrp1.deja.com>`

```
On Wed, 01 Sep 1999 14:51:55 GMT, Mark Framness <framnesso@my-deja.com> wrote:

>The main problem I have with COBOL is that every variable is global in
>scope and that you can not make variables constant (I'm talking about
>COBOL II on OS/390 systems) and that you can't break up your source code
>into smaller modules.


Sure you can - Just use nested programs, then you can local and global/shared variables.

Also, you can combine small modules to a large main using the linkage editor.  What is the
problem?


with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: COBOL v Other Languages

- **From:** Mark Framness <framnesso@my-deja.com>
- **Date:** 1999-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qm07p$gp5$1@nnrp1.deja.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <7qjei6$l0t$1@nnrp1.deja.com> <37cd5577.38994931@news2.ibm.net>`

```
In article <37cd5577.38994931@news2.ibm.net>,
  vbandke@bsp-gmbh.com wrote:
> On Wed, 01 Sep 1999 14:51:55 GMT, Mark Framness
<framnesso@my-deja.com> wrote:
>
> >The main problem I have with COBOL is that every variable is global
in
> >scope and that you can not make variables constant (I'm talking about
> >COBOL II on OS/390 systems) and that you can't break up your source
code
> >into smaller modules.
>
> Sure you can - Just use nested programs, then you can local and
global/shared variables.
>
> Also, you can combine small modules to a large main using the linkage
editor.  What is the
> problem?

Well I guess I know not of the intricacies of the COBOL II linker.  We
had "canned" jcl that called a proc that did the linking.  We just
substituted in the name of the object module into a symbolic parm and
then we ran the jcl.  That proc was written by our instructors and I
never looked too deeply into it.  So I guess that is why I thought that
multiple source module cobol programs were not doable.

thanks
```

###### ↳ ↳ ↳ Re: COBOL v Other Languages

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CE8E18.BD05958D@NOSPAMhome.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <7qjei6$l0t$1@nnrp1.deja.com> <37cd5577.38994931@news2.ibm.net> <7qm07p$gp5$1@nnrp1.deja.com>`

```
Mark Framness wrote:

> Well I guess I know not of the intricacies of the COBOL II linker.  We
> had "canned" jcl that called a proc that did the linking.  We just
…[3 more quoted lines elided]…
> multiple source module cobol programs were not doable.

I just created a multiple source module COBOL program in my work place. 
Using our canned procedures, I compiled it, and both programs were
clean.  But when I ran it, the first program could not find the second
program to link to it.  Separating them out solved that problem.

It's usually not a good idea to use compiler options (other than those
used for temporary debugging and for displaying cross-references), which
are different from the production standards.  If they make your program
behave differently, your test is insufficient.
```

###### ↳ ↳ ↳ Re: COBOL v Other Languages

_(reply depth: 4)_

- **From:** vbandke@ibm.net (Volker Bandke)
- **Date:** 1999-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cfa5d5.6330693@news2.ibm.net>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <7qjei6$l0t$1@nnrp1.deja.com> <37cd5577.38994931@news2.ibm.net> <7qm07p$gp5$1@nnrp1.deja.com>`

```
On Thu, 02 Sep 1999 14:05:54 GMT, Mark Framness <framnesso@my-deja.com> wrote:

>
>Well I guess I know not of the intricacies of the COBOL II linker.
Perhaps, because there is no such thing like a COBOL linker?  It' the DFP Binder, formerly
known as MVS Linkage Editor <s>


>>..  We
>had "canned" jcl that called a proc that did the linking.  We just
>substituted in the name of the object module into a symbolic parm and
>then we ran the jcl.  That proc was written by our instructors and I
>never looked too deeply into it.

I am a COBOL instructor, and do exactly this.  Much too little time to teach JCL,
Programming, and COBOL , Binder, et al. in one week, thus pre-canned JCL it is  

>So I guess that is why I thought that
>multiple source module cobol programs were not doable.

Okay, here are two approaches to the problem.  I use TWO modules as an example, but of
course, using induction, you can then use any number of programs

A)  Separately compile the Programs PGMA and PGMB to full grown Program Objects (formerly
known as Load Modules)

In PGMA you code

	MOVE 'PGMB' TO pgmname
	CALL pgmname USING parm1, parm2 parm3

This constitutes a "dynamic call".  In the JCL for the execution of PGMA you code

//PGMA  EXEC PGM=PGMA
//STEPLIB DD DISP=SHR,DSN=lib.where.PGMA.is.a.member
//         DD DISP=SHR,DSN=lib.where.PGMB.is.a.member

The PGMA will find PGMB and invoke it


B)  Separately compile the programs PGMA and PGMB into Object Modules.  Use JCL similar to
this:
 //COMPILE  PROC MEMBER=MISSING
 //COBOL   EXEC PGM=IGYCRCTL,REGION=2048K
 //SYSPRINT DD  SYSOUT=*
 //SYSLIN   DD  UNIT=SYSDA,DISP=(MOD,PASS),SPACE=(TRK,(3,3,10)),
 //             DCB=(BLKSIZE=3200),DSN=&&TEMPPDS(&MEMBER)
 //SYSUT1   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
 //SYSUT2   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
 //SYSUT3   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
 //SYSUT4   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
 //SYSUT5   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
 //SYSUT6   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
 //SYSUT7   DD  UNIT=SYSDA,SPACE=(CYL,(1,1))
 //SYSIN    DD  DISP=SHR,DSN=YOUR.SOURCE.COB(&MEMBER)
 //SYSLIB   DD  DISP=SHR,DSN=YOUR.SOURCE.COPYBOOK
//               PEND
//PGMA   EXEC  COMPILE,MEMBER=PGMA
//PGMB   EXEC  COMPILE,MEMBER=PGMB
//LKED    EXEC PGM=HEWL,COND=(4,LT),REGION=4096K
//SYSLIB   DD  DISP=SHR,DSN=CEE.SCEELKED   or whatever your LE370 libs are called
//OBJLIB   DD  DISP=(OLD,DELETE,DELETE),DSN=&&TEMPPDS
//ANOTHER DD DISP=SHR,DSN=SOME.OTHER.OBJ.OR.LOADLIB
//SYSPRINT DD  SYSOUT=*
//SYSLIN   DD  DDNAME=SYSIN
//SYSLMOD  DD  DISP=SHR,DSN=YOUR.PGM.LOADLIB
//SYSUT1   DD  UNIT=SYSDA,SPACE=(TRK,(10,10))
//SYSIN DD *
 INCLUDE OBJLIB(PGMA)
 INCLUDE OBJLIB(PGMB)
 INCLUDE ANOTHER(PGMC)
 INCLUDE SYSLMOD(BIGMODUL)
 NAME BIGMODUL(R)

Please keep in mind that I am writing this off the top of my head, without being near a
mainframe.  But this should give you the general idea



Perhaps this sample will help you to create multi-source COBOL modules

//COBCOMP PROC MEMBER=MISSING
//COB      
with kind regards

Volker Bandke
(BSP GmbH)
```

###### ↳ ↳ ↳ Re: COBOL v Other Languages

_(reply depth: 4)_

- **From:** William Lynch <WBLynch@att.net>
- **Date:** 1999-09-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37D080BA.8816178C@att.net>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <7qjei6$l0t$1@nnrp1.deja.com> <37cd5577.38994931@news2.ibm.net> <7qm07p$gp5$1@nnrp1.deja.com>`

```
Mark Framness wrote:
> 
(snip)
> >
> > Also, you can combine small modules to a large main using the linkage
…[3 more quoted lines elided]…
> Well I guess I know not of the intricacies of the COBOL II linker.

(IBM mainframe disclaimer) For openers, there's no COBOL II linker. MVS
has had a linkage editor since its birth, called the Binder in its
current implementation. It's used to create load modules from object
code compiled by anything.

Bill Lynch
```

#### ↳ Re: COBOL v Other Languages

- **From:** Dave Polzin <dlpolzin@coredcs.com>
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CDDC0F.53B4@coredcs.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com>`

```
** James J. Gavan wrote:
** ... they will use other languages (C, C++, Java etc.)
** to do things more effectively than in COBOL.
** ... examples of where you do this in preference to using COBOL, 

Admitting that I don't know much about either C/C++ or Java, let me pass
on a couple of comments I overheard at last week's SHARE conference
anyway --

"C/C++ is not a very good candidate for business applications because it
does not support fixed decimal arithmetic (e.g. dollars and cents) which
is what most business applications require."

"Java, being an interpretive language, is much too slow for most
mainframe (i.e. os/390) applications."

"There is no Inter-Language Communication facility to connect Java to
COBOL applications." (COBOL calling Java or vice versa)

On the other hand: "1/3 of the os/390 system components require the LE
runtime libraries, primarily because they are written in C."

So I guess what it boils down to is choose the language that fits the
application.  Don't try to fit all applications to a single language.

================================
Dave Polzin  <dlpolzin@coredcs.com>
================================
```

##### ↳ ↳ Re: COBOL v Other Languages

- **From:** "Warren Simmons" <w.g.simmons@worldnet.att.net>
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qkt0c$q47$1@bgtnsc01.worldnet.att.net>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <37CDDC0F.53B4@coredcs.com>`

```
A number of people in this NG are or have expressed a sensible opinion about
choosing a programming language.

I think that's good thinking.

Then there is the sub-thread that dwells on the range of a language is good
for as as a means for choosing the programming language.

I feel some people are missing a very important point.

Documentation.

How long does it take to learn to read and write the language?

Will the language make a clear statement of the problem being solved?

Do you need to be a rocket scientist to understand the problem solution?

Will the changes in technology be reflected in the language?

In my opinion, in 1960 it was important to restrict a common language to
business applications because selling a replacement for Fortran, Assembly,
Comtran, etc. was/are remains a difficult sell.  It is much easier to
demonstrate the programming language range of applications than to tout it
as a do all end all tool. An example might be the Communications Section and
it's poor reception yet TCP/IP is or can be done with todays Business or
otherwise application languages if it is desired.

If there is a problem with languages, it is that not enough work has gone
into generalizing the funtions required except in a GLOBAL way.  Global is
good in a way, or it is bad but how do you learn this, and what are the plus
and minus
results of going one way or another.  We are talking about intra-program,
inter-application, and intra-company interfaces.  Computer operating system
development is not usually approached on a network basis. Much is also being
done inter-and-intra-industry.

In my view, there is only the need for one basic set of key words with
defined attributes and results.  We are not yet willing to look at it that
way so we have several sets of words (loosely speaking) many of which
intersect partially or completely.  Who would want to try to merge them and
clarify them into a single set?  Webster or others have done it.  Yet for
the subset we need, it's still an infant.

Warren Simmons
```

##### ↳ ↳ Re: COBOL v Other Languages

- **From:** "Gazaloo" <gaz@home.com>
- **Date:** 1999-09-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f9oz3.1137$C74.8959@news1.frmt1.sfba.home.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <37CDDC0F.53B4@coredcs.com>`

```
i know they are just hearsay, but here's some input anyway!

Dave Polzin <dlpolzin@coredcs.com> wrote:
> "Java, being an interpretive language, is much too slow for most
> mainframe (i.e. os/390) applications."

for most platforms, Just In Time (JIT) Java compilers do exist (including
the 390). these do offer performance improvements over purely interpreted
code (but i don't know if it's enough). don't know what the story is wrt
(static) native Java compilers (a la C/C++/COBOL). anyone?

> "There is no Inter-Language Communication facility to connect Java to
> COBOL applications." (COBOL calling Java or vice versa)

you can use the Java Native Interface (JNI) to mix/connect COBOL & Java in
the same application. this is certainly the case with MERANT Micro Focus
compilers (Net Express for NT and Server Express for UNIX).

> So I guess what it boils down to is choose the language that fits the
> application.  Don't try to fit all applications to a single language.

extremely sound advice.
```

#### ↳ Re: COBOL v Other Languages

- **From:** dnalor@my-deja.com
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qj1g4$bbh$1@nnrp1.deja.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com>`

```
Hi Jimmy,
your question is extremly important, more exactly: it eventully starts
religion wars.
The point of EVERY(!) Programming language is, that it was designed for
a very specific group of applications. That means it is the wrong way
to take a language, no matter which, and say, okay, lets write a
program that solves problem X for us. U must go the opposite way.
Consider ur problem, specify it, and THEN decide which language.
This is the reason why there are lots of languages, you know.
If u have to travel through trees (least-cost-way-seeking problem)
COBOL is definitley the most inperformant approach, because it does not
support recursion (MF-Cobol does, but not really useful).
I think u got the clue. Be careful to consider opinions from 1-language-
freaks!!!

In article <37CAC7AC.EC687EAB@home.com>,
  "James J. Gavan" <jjgavan@home.com> wrote:
> Through various threads, contributors have said that where necessary
> they will use other languages (C, C++, Java etc.) to do things more
…[3 more quoted lines elided]…
> examples of where you do this in preference to using COBOL,
(presuambly
> caused by deficiencies in the latter ?)
>
> Jimmy, Calgary AB
>


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

##### ↳ ↳ Re: COBOL v Other Languages

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37CD28FC.D3577E24@NOSPAMhome.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <7qj1g4$bbh$1@nnrp1.deja.com>`

```
dnalor@my-deja.com wrote:
> 
> Hi Jimmy,
…[6 more quoted lines elided]…
> Consider ur problem, specify it, and THEN decide which language.

There are several criteria to consider in any problem though.  One need
may push to one tool, another to a different tool.  Some criteria
include:
1.  Does that tool solve the problem most accurately.
2.  Can you find people who are skilled in using that tool.
3.  Will you need to have that tool around a long time in the future?
3a. Will you find people/support for that tool in the future?
4.  How much does that tool cost?  
5.  Is maintenance easy or hard for that tool?
6.  How stable is that tool's environment?

> This is the reason why there are lots of languages, you know.

While there are thousands of languages, only a few are cost effective
for a typical environment though.  A typical workplace would be silly to
evaluate each programming need and purchase the language which is best
for that individual program.  And even if the workplace decides that the
best all around language is PL/1, it might find that the local labor
market dictates COBOL is better.  Or maybe it needs LISP - does the cost
of training & keeping LISP programmers still make it the best?  Or if it
likes ADA - does it figure ADA tools will be available in 5 years to
match its changing environment?
```

##### ↳ ↳ Re: COBOL v Other Languages

- **From:** DACatHome@aol.com
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qjg9a$mgr$1@nnrp1.deja.com>`
- **References:** `<37CAC7AC.EC687EAB@home.com> <7qj1g4$bbh$1@nnrp1.deja.com>`

```
In article <7qj1g4$bbh$1@nnrp1.deja.com>,
  dnalor@my-deja.com wrote:
> Hi Jimmy,
> your question is extremly important, more exactly: it eventully starts
> religion wars.
> The point of EVERY(!) Programming language is, that it was designed
for
> a very specific group of applications. That means it is the wrong way
> to take a language, no matter which, and say, okay, lets write a
…[4 more quoted lines elided]…
> COBOL is definitley the most inperformant approach, because it does
not
> support recursion (MF-Cobol does, but not really useful).
> I think u got the clue. Be careful to consider opinions from
1-language-
> freaks!!!
>
…[6 more quoted lines elided]…
> > I don't dispute these claims - but am curious - could you  please
give
> > examples of where you do this in preference to using COBOL,
> (presuambly
…[7 more quoted lines elided]…
>

Inperformant? Is that a word? I assume ineffective could be inserted
there. In any case, I agree with the gist of what you are saying. There
is language overlap though. That's why, for instance, the Java people
and the Smalltalk people go at it. The Java people would also say that
it can handle everything Cobol can do, only better.


Sent via Deja.com http://www.deja.com/
Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
