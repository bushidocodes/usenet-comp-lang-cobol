[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Selecting a compiler

_3 messages · 3 participants · 2003-02_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Selecting a compiler

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-02-07T19:30:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b21mjq$hk1$1@slb0.atl.mindspring.net>`

```
I just thought that I would raise some "questions" as a follow-on to another
thread in CLC.  These are some of the questions that I think people *might*
consider when selecting a COBOL compiler:

1) Are there more than one compiler vendor who actually sells a "supported"
compiler for the environment that you plan on developing upon? How about
running on?  (These may or may not have the same answer.)

2) Are you looking for a compiler to "learn" on? create production code
with?  create software that you plan on selling?  (The answers to these
questions may influence such issues as to whether you care about "run-time
fees"? run-time performance? debugging tools?  easy to find samples?  easy
to find maintenance programmers? etc)

3) Do you think that you might EVER need to "port" your source code to
another compiler? to another run-time environment? to an "upgraded"
operating system/environment?

4) How important is ILC (inter-language communication) to your expected use?
If at all important to what type of "languages"?  C?  C++? Java? PL/I?
Assembler (which variety)? etc?

5) What type of non-COBOL "things" might you need/want to interface with?
SQL? printers (and what type)? proprietary systems such as IMS or CICS or
Windows API's or Oracle etc?

6) Are there contractual issues for your expected applications e.g. "must
conform to ANSI Standard for US government contract?)  Must provide
user-documentation or source code in escrow?  Must maintain at least 3
back-levels of source code?

7) Do you have any "internationalization" issues expected for your COBOL
programs? for "things" that your COBOL program must interact with?  If so,
are there Unicode or similar issues that your COBOL compiler must deal with?

8) What type of support do you "need" from your compiler vendor?  (24x7?
email responses within 2-3 business days?  open-source?)

9) What are your cost constraints on the compiler? on the run-time? on
run-time distribution?

   ***

Probably LOTS of other questions arise to others.  The chances are that if
you are in a "mainframe" environment, you have no "individual" choice in
what compiler you use - on the other hand, if you are looking for a
"workstation" compiler, you (usually) get what you pay for - and need to
worry about what you plan on doing with your compiler output (if anything).
```

#### ↳ Re: Selecting a compiler

- **From:** "Merlin Moncure" <merlin@rcsonline.com>
- **Date:** 2003-02-21T15:46:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v5d3u46373o68f@corp.supernews.com>`
- **References:** `<b21mjq$hk1$1@slb0.atl.mindspring.net>`

```
An interesting post!  I recently got a new job and inherited a huge cobol
source code library.  My project does it all, accounting, inventory, factory
manangement, you name it.  I never used cobol previously, having worked
mostly in c++.   My company uses AcuCorp cobol, the only one I know, so my
answers will be based on my perspectives gained using that platform.

To me, the #1 issue with COBOL is vendor lock in.  Just as an example,
AcuCorp's compiler costs 1000$, when you can download any number of free C
compilers off the internet.  To avoid lock in you have to avoid using any
vendor specific tools but these very tools are required to make a 'modern'
looking application in COBOL.  I like freedom to be able to migrate my
applciation to different platforms with minimal effort.


"William M. Klein" <wmklein@ix.netcom.com> wrote in message
news:b21mjq$hk1$1@slb0.atl.mindspring.net...
> I just thought that I would raise some "questions" as a follow-on to
another
> thread in CLC.  These are some of the questions that I think people
*might*
> consider when selecting a COBOL compiler:
>
> 1) Are there more than one compiler vendor who actually sells a
"supported"
> compiler for the environment that you plan on developing upon? How about
> running on?  (These may or may not have the same answer.)

AcuCobol runs on most windows/unix platforms.  A lot of the GUI stuff only
works on windows.  Vanilla cobol should run just about anywhere, but
personally I wouldn't suggest starting a new project in vanilla cobol.
There are some free compilers you can download which are pretty functional,
but I don't see a use for them beyond academic purposes.

>
> 2) Are you looking for a compiler to "learn" on? create production code
…[7 more quoted lines elided]…
> operating system/environment?

Never, ever say no to this answer. Otherwise you are looking at a rewrite at
some later date.

>
> 4) How important is ILC (inter-language communication) to your expected
use?
> If at all important to what type of "languages"?  C?  C++? Java? PL/I?
> Assembler (which variety)? etc?

This is extrememly important to me. COBOL can no longer be counted on to
deliver every aspect of an application.  It is simply one tool in a toolkit.
COBOL has some very useful contructs for expressing business rules and will
therefore always have a use, but being able to introduce different languages
will make you a more versatile programmer.  Without ILC, you have to wait
for your vendor to deliver new technologies (for example, xml-edi) and that
is not a good thing.

Assembler has no place in a business application anymore.  C is terrible at
business apps but is good at performing workhorse tasks like dynamic
allocation.  C++ is a good general purpose lanugage, but is complex.  I
think C# is a beautiful language, (never used java) but as of Feb '03 thats
only on windows.

AcuCorp cobol has a very elegant syntax for calling DLLs (in windows), you
just CALL the dll to load it, then you can CALL its procedures.  This is one
of the best things about that platform.

>
> 5) What type of non-COBOL "things" might you need/want to interface with?
> SQL? printers (and what type)? proprietary systems such as IMS or CICS or
> Windows API's or Oracle etc?

SQL is a replacement for COBOL I/O operations, namely read, write, rewite,
open, close, and start.  One SQL statement can replace literally hundreds of
lines of code in a program.  Another benefit of sql is that it is 'set'
based programming (some call it declarative programming).  It is proven that
errors are easier to catch and fix at the set based level and set level
programs have a much smaller recurring cost than procedural programs.  SQL
statements are also much friendlier to database transactions.

If your platform has an elegant syntax for executing sql statements from
within a cobol program, congratulations.  You enjoy the best of both worlds.
Expect to pay top dollar for this from a commercial vendor.  Performance is
an issue here, too.  Some sql->cobol solutions are real dogs in the
performance arena and should be avoided.

>
> 6) Are there contractual issues for your expected applications e.g. "must
> conform to ANSI Standard for US government contract?)  Must provide
> user-documentation or source code in escrow?  Must maintain at least 3
> back-levels of source code?

I've never done such work, but CVS is an excellent choice for managing
historical source code revisions.  I installed it here at the office and it
has already paid off in a big way,  catching strange bugs introduced
inadvertantly by developers.

>
> 7) Do you have any "internationalization" issues expected for your COBOL
> programs? for "things" that your COBOL program must interact with?  If so,
> are there Unicode or similar issues that your COBOL compiler must deal
with?
>
> 8) What type of support do you "need" from your compiler vendor?  (24x7?
…[3 more quoted lines elided]…
> run-time distribution?

Solutions for these problems are highly vendor specific.  Just do your
research and keep your options open.  At this point in the game, I think
there are few reasons to start a new project in cobol.  One thing I have
noticed about cobol is that everything seems to cost more, all the way
through the development process.  One good thing about cobol is that there a
lot of developers who have business app experience to draw from.   There
might be some reasons to choose cobol  at the enterprise level.  Generally,
though, I would only choose cobol only if there was no other alternative.

However, I would recommend that every programmer learn cobol.  At first
glance it seems very outdated, but it has a certain charm that comes through
after a while.  Even the early standards were very ahead of their time in
certain respects.  If you program in the business world the chances are very
good you will run across some cobol code sooner or later.   It is quite
common these days that businesses are porting their cobol programs to
another language/platform.  Knowing cobol would be an crucial skill in
getting hired for those projects.

Merlin
merlin.moncure@rcsonline.com
>
>    ***
…[5 more quoted lines elided]…
> worry about what you plan on doing with your compiler output (if
anything).
>
> --
…[3 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Selecting a compiler

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-02-24T15:42:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<02fk5vk7vo9q8ubensevd6008709r7mo97@4ax.com>`
- **References:** `<b21mjq$hk1$1@slb0.atl.mindspring.net> <v5d3u46373o68f@corp.supernews.com>`

```
Merlin:

I agree wholeheartedly with your assessment that the #1 issue is
vendor lock in.

That's why you should take a look at the Flexus COBOL tools.

Because we employ the use of COBOL CALL USING statements for our
tools, they are COBOL compiler independent, operating system
independent and even character mode to GUI independent.

Our tools work GREAT with the Acucorp line of compilers, from the
older ones to the GT compiler to the newer Extend compilers.  But they
also work with Micro Focus compilers, Fujitsu compilers, Liant/RM
COBOL compilers, ICOBOL compilers, CA-Realia COBOL compilers and IBM
Visual Age COBOL compilers.  We still have customers who use our tools
on compilers which are no longer supported by the compiler vendor,
such as mbp Visual COBOL.

If you have any questions at all, please send a private e-mail to me.
I'll be happy to assist.

"Merlin Moncure" <merlin@rcsonline.com> wrote:

>An interesting post!  I recently got a new job and inherited a huge cobol
>source code library.  My project does it all, accounting, inventory, factory
…[146 more quoted lines elided]…
>


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
