[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Any Suggestions? (Extreme Programming)

_7 messages · 6 participants · 1999-12_

---

### Re: Any Suggestions? (Extreme Programming)

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83iiqo$1s0n$1@news.hitter.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <3842BDE8.942020E7@NOSPAMhome.com> <822ah5$1gc$1@nntp5.atl.mindspring.net> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia>`

```

Judson McClendon wrote in message ...
[...]
>And there is also an often overlooked serious penalty to that approach.
>One of the things in C/C++ and many other languages that contribute most
…[3 more quoted lines elided]…
>other logical bugs combined.

The implementation of pointers in COBOL is much closer
to PL/I than it is to C.

>  Up until now, COBOL has been free of this
>particular problem, significantly contributing to COBOL's well deserved
>reputation for reliability.  I am very concerned about this issue and
>the future of COBOL.

To see the future of COBOL with pointers, look at more
than 27 years of pointer use in PL/I. Does PL/I have a
reputation for unreliable programs?

>  If these features are implemented widely in COBOL,
>before long, COBOL programmers are going to be shooting their feet off,
…[4 more quoted lines elided]…
>personally I don't think so.

COBOL needs a means for implementing dynamic data
structures. Two paths are being offered: OO and dynamic
memory allocation with pointers. Some of the features
for implementing dynamic data structures within OO
(collections) will not be available, in the standard, for
about five years after approval of the current draft.

>  After many years of writing code in COBOL
>and many other languages, I believe COBOL's main advantage, and why it
…[4 more quoted lines elided]…
>more from the added complexity and subtleties,

The added complexity, to the language, is ALLOCATE,
FREE, POINTER, BASED [ON], and additional formats
for SET.

The subtleties are really no different than working with
temporary files. If you create a temporary file, don't
lose the reference to it. If you create a linked list using
dynamically allocated memory, don't lose the reference
to the head of the list. The difference between temporary
files and dynamically allocated memory is that memory,
that is no longer required must be freed by the program.
This is similar to deleting every record, in a temporary
indexed (or relative) file, by its key (when the data is
no longer needed).

> and I believe the
>overwhelming majority of COBOL applications really doesn't need them.

I have suggested the same of OO, which is more complex
than dynamic memory allocation and pointers.

It is unfair to imply that prior lack of reliability in C and C++
programs necessarily implies the same lack of reliability
in COBOL programs. This is because, during the late 80s
and throughout the 90s, there was a large demand for C
and C++ programmers. This demand was so large it could
only be filled by inexperienced programmers (rookies).
Rookie programmers in any language will make mistakes.

Again, the implementation of dynamic memory allocation
and pointers, in COBOL, is much closer to PL/I than C.

If experienced PL/I programmers use dynamic memory
allocation and pointers well, then experienced COBOL
programmers will use dynamic memory allocation and
pointers well.
------------------
Rick Smith
```

#### ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83n4d3$54i$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <822ah5$1gc$1@nntp5.atl.mindspring.net> <3ex14.6774$Ic5.79616@news3.mia> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <83iiqo$1s0n$1@news.hitter.net>`

```
<SNIP>

> The subtleties are really no different than working with
> temporary files. If you create a temporary file, don't
…[8 more quoted lines elided]…
>

<SNIP>

    We also need to consider the compilers. Whether it is
a matter of cuture or skill, the choices that the compiler
writers make effect us.  When you do a memory allocation
in MF cobol, a stop run, or a cobol runtime error will
automatically release ALL allocated memory, even if the
program has lost track of it.

    Is this true with C/C++ ?  Most of the magazine articles I
have seen (not recently) comparing various C compilers focused
on speed, not maintainablilty or reliablity of the program.  Adding
this addtional layer to the software costs speed.  I feel that it is
well worth it.

    We have seen the same thing with cars.  Writers compare
2 or 3 cars, and give us the 0-60 acceleration.  Now we have
cars that are sluggish unless you drive like an idiot (or reviewer,
same thing).
```

##### ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385F6B5F.285A906B@zip.com.au>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <83iiqo$1s0n$1@news.hitter.net> <83n4d3$54i$1@ssauraac-i-1.production.compuserve.com>`

```
Russell Styles wrote:

>     We also need to consider the compilers. Whether it is
> a matter of cuture or skill, the choices that the compiler
…[9 more quoted lines elided]…
> well worth it.

With virtual memory your program run's in it's own address space. 
When your program ceases then the address space disappears as well.

This really is the responsibility of the operating system.  It must
realize that the program has ceased and free up all resources as a
result.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

- **From:** Ralph Jones <leclay@ibm.net>
- **Date:** 1999-12-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3868DF3E.64104482@ibm.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <826dpi$fpk$1@nntp3.atl.mindspring.net> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <83iiqo$1s0n$1@news.hitter.net> <83n4d3$54i$1@ssauraac-i-1.production.compuserve.com> <385F6B5F.285A906B@zip.com.au>`

```
C has no defined memory allocation in the language.  The ANSI malloc and
it's derivatives are separately compiled functions (sub-routines).  The
major C compilers will automatically free runtime memory allocations when
the program ends for what ever reason.

In C++ it is strictly up to the programmer to free all dynamic memory
using object destructors.  This is the Achilles heel of C++.

C++ has be been grafted onto C, kind of like grafting a Mack truck on top
of a 2 seat Honda Del Sol.

Reliability is up to the programming team, not the language.

True, C tends to be a write-only language.  However.  most C programs are
broken down into much smaller files than a monolithic COBOL program and as
a result, a C program becomes somewhat readable.

After doing C for a couple of years I finally came across a readable C
program.  It was code generated by the GNU fast lexical analyzer, flex.
After that I tried to code C using flex style.  Flex was written by
Vern Paxson.

Cheers,
Ralph Jones


Ken Foskey wrote:

> Russell Styles wrote:
>
…[22 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 4)_

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386A9B4A.E00D935E@zip.com.au>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <3846C4A5.C1A66591@NOSPAMwebaccess.net> <826slb$peq$1@aklobs.kc.net.nz> <3847487c.537138075@news1.attglobal.net> <827r49$tb$1@aklobs.kc.net.nz> <3847D524.4FE1ADBA@NOSPAMwebaccess.net> <829ct3$cuo$1@aklobs.kc.net.nz> <3848725F.D1A0FA7C@att.net> <38488E05.35632487@home.com> <3849017F.B8D940BF@zip.com.au> <384CA162.C7B5367D@home.com> <82ja74$5ej$1@nntp8.atl.mindspring.net> <Sva34.2737$Ze7.107325@news3.mia> <82jcc6$7aj$1@nntp8.atl.mindspring.net> <3853c3f1.43035700@news1.attglobal.net> <3853F9A2.ADBA8CA6@home.com> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <83iiqo$1s0n$1@news.hitter.net> <83n4d3$54i$1@ssauraac-i-1.production.compuserve.com> <385F6B5F.285A906B@zip.com.au> <3868DF3E.64104482@ibm.net>`

```
Ralph Jones wrote:
> 
> C has no defined memory allocation in the language.  The ANSI malloc and
> it's derivatives are separately compiled functions (sub-routines).  The
> major C compilers will automatically free runtime memory allocations when
> the program ends for what ever reason.

This is not really valid.  All applications will have the library
functions except washing machines.

> In C++ it is strictly up to the programmer to free all dynamic memory
> using object destructors.  This is the Achilles heel of C++.

You can use NEW and DELETE as well as malloc.  The OO concept enables
a cleaner implementation of the clean up.  If you code your allocation
code in the constructor (the routine that does an initialize of a new
instance) and your deallocation in the destructor (the routine that
does the clean up of a disappearing instance).

You can create an instance of an object that lasts for a routine
(paragraph).  You do not code for creation and deletion in the same
way that working storage just appears and disappears if you use the
recursive compiler directive in Cobol.

> C++ has be been grafted onto C, kind of like grafting a Mack truck on top
> of a 2 seat Honda Del Sol.

Hmm...   Kind of,  there are far better environments.  To learn OO on
top of a procedural language is very difficult, it is better to lean a
pure environment.  This is my concern with OO cobol.   Learn the OO
concepts very well first, then be surprised when you do not really
understand.   Small talk appears to be the language of choice, though
this is strongly debated.

> Reliability is up to the programming team, not the language.

Yes,  I trust my vendor to give me reliable compilers.  In 15 years I
have found one error with the cobol compiler for MVS and one
'documentation' change (I still consider it a bug).

> True, C tends to be a write-only language.  However.  most C programs are
> broken down into much smaller files than a monolithic COBOL program and as
…[5 more quoted lines elided]…
> Vern Paxson.

It is MUCH easier to write crap code in C than cobol.  I have seen
many write only programs in Cobol as well, nothing replaces a good
style guide.  I personally have my own guidelines, I now DO NOT remove
any letters from words in variables in code unless it is a corporate
standard.   Craft takes time to develop and we all constantly learn.

> Cheers,
> Ralph Jones

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 5)_

- **From:** Richard Plinston <riplin@kcbbs.gen.nz>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84gfv3$u15$1@aklobs.kc.net.nz>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <83iiqo$1s0n$1@news.hitter.net> <83n4d3$54i$1@ssauraac-i-1.production.compuserve.com> <385F6B5F.285A906B@zip.com.au> <3868DF3E.64104482@ibm.net> <386A9B4A.E00D935E@zip.com.au>`

```
: Ralph Jones wrote:
:> 
:> C has no defined memory allocation in the language.  The ANSI malloc and
:> it's derivatives are separately compiled functions (sub-routines).  The
:> major C compilers will automatically free runtime memory allocations when
:> the program ends for what ever reason.

This is simply not true.  When a program terminates the _operating_system_
will normally recover all memory used by the process, the C compiler
will not do so at all, the C runtime library may or may not bother
to relase the whole heap back to the OS, it certainly will _not_
issue any 'free()'s automatically.

On some systems there may be memory allocations that survive the
program termination, depending on how the allocation was done and
which OS and library is used.

:> In C++ it is strictly up to the programmer to free all dynamic memory
:> using object destructors.  This is the Achilles heel of C++.

Simply not true.  As above, when a program terminates the operating
system may recover all allocated memory regardless of how it was
allocated or if it was released or destructed (or it may not
recover certain types of allocation).  Destructors do not have
to be explicitly called by the programmer.


:> Reliability is up to the programming team, not the language.

The language provides the tools (or does not) that the programmers
can use.  For example Cobol does not allow a condition to create a
side effect whereas C does.  When a complex condition is short-
circuited the side effect may be missed.  This may make the program
less reliable because the C language allows this, whereas Cobol
disallows it and prevents the programmers making mistakes of this
type.

:> True, C tends to be a write-only language.  However.  most C programs are
:> broken down into much smaller files than a monolithic COBOL program and as
:> a result, a C program becomes somewhat readable.

Not all Cobol is in monolithic programs.  Many Cobol systems are
written using smaller code modules that are statically or
dynamically linked.  However, size of source files has no bearing
on 'readability'.  Some people can cope with very large and 
complex code blocks and find them perfectly readable, others
cannot cope and can only deal with 'bite' sized blocks without
getting confused.
```

###### ↳ ↳ ↳ Re: Any Suggestions? (Extreme Programming)

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 1999-12-31T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xTSa4.1197$Gj5.26382@dfiatx1-snr1.gtei.net>`
- **References:** `<81t7ol$sos$1@husk.cso.niu.edu> <HuV44.16154$Dk.242231@news1.mia> <38545683.EA71B1B3@home.com> <38547457.88200718@news1.attglobal.net> <832pt1$b81$1@news.igs.net> <w0854.182$Sj6.9231@dfiatx1-snr1.gtei.net> <833qc5$r7r$1@news.igs.net> <9Je54.949$Sj6.26677@dfiatx1-snr1.gtei.net> <Gtu54.2727$DC6.28547@news2.mia> <83iiqo$1s0n$1@news.hitter.net> <83n4d3$54i$1@ssauraac-i-1.production.compuserve.com> <385F6B5F.285A906B@zip.com.au> <3868DF3E.64104482@ibm.net> <386A9B4A.E00D935E@zip.com.au> <84gfv3$u15$1@aklobs.kc.net.nz>`

```
Richard Plinston wrote in message <84gfv3$u15$1@aklobs.kc.net.nz>...
>: Ralph Jones wrote:
>:>
…[5 more quoted lines elided]…
>to be explicitly called by the programmer.


Almost. MS-DOS, 32-bit Windows (except as below) , every *nix I've worked
with and IBM MF OSs clean up.

16-Bit Windows does not clean up memory allocated with GlobalAlloc until
Windows terminates. This includes 16-bit software running under Win 9x
32-bit OS. There is a single 16Mb (max) memory area allocated to "be shared
by all 16-bit applications." GlobalAllocs from this pool must be explictly
released or they remain allocated until all 16-bit applications terminate,
which on Win 9x never happens because GDI is 16-bit. 16-bit apps running
under NT is different.

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
