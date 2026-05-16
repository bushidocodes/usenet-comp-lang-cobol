[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Reentrant programs in Cobol

_6 messages · 3 participants · 2002-04_

---

### Reentrant programs in Cobol

- **From:** menonshyam@yahoo.com (shyam menon)
- **Date:** 2002-04-16T20:43:48-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10986fae.0204161943.1a2c630f@posting.google.com>`

```
Hi,
  I am unable to understand some topics regarding reentrancy in Cobol
program.

1. A reentrant program is made by using RENT compiler option.
   So this program can be used by multiple users.But this will require
a driver like IMS or CICS to handle the MVS tasks right?

2. Is a separate copy of Working Storage alloted to each user who uses
the program or is it common for all?
Can any changes be made to the data in the working storage variables
and if so how will it impact the multiple users who are executing the
program?

3.There is a lot of stuff about the program not being able to modify
itself?
 What is the exact meaning of this?

4. Is there any restriction on changing the constant data declared in
the WS for such programs?

Thanks in advance,
Shyam.
```

#### ↳ Re: Reentrant programs in Cobol

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-04-16T23:13:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9isp4$qju$1@slb4.atl.mindspring.net>`
- **References:** `<10986fae.0204161943.1a2c630f@posting.google.com>`

```
The bottom-line is that if you use an IBM compiler from VS COBOL II on (eg.
IBM COBOL for this-and-that) *and* compile with the RENT compiler option
*and* link-edit with the RENT link-edit attribute (which will be your
default if you don't override things), then you need do NOTHING special in
your program to insure that it is "truly" re-entrant.  If you run the
program in any MVS (OS/390 or z/OS) environment that supports reentrant
programs, then everything should work "fine".

HOWEVER, there was a restriction in VS COBOL II (and early versions of IBM
COBOL for this-and-that) on "multiple" copies of SEPARATE run-units under
the same "task".  See

http://publib.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/igy3mg00/1.2.4

and look at the topics
  "Support to |run in  multiple threads"
and
  "Support for multiple tasks"

NOTE: For the "new" multi-thread support, you need to use PL/I, Assembler,
or USS services to "start" the simultaneous threads.
```

##### ↳ ↳ Re: Reentrant programs in Cobol

- **From:** menonshyam@yahoo.com (shyam menon)
- **Date:** 2002-04-18T20:54:04-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<10986fae.0204181954.71dd7146@posting.google.com>`
- **References:** `<10986fae.0204161943.1a2c630f@posting.google.com> <a9isp4$qju$1@slb4.atl.mindspring.net>`

```
Hi,
  I am not sure i understand what you said about the reentrant
programs.From what i gathered the program has to be run in an
environment that supports reentrant programs.So does it have to be run
under CICS  or IMS or can it be run simply on MVS.But i dont think
multithreading is supported in cobol on os/390.We are using VS Cobol 2
and not Enterprise cobol.
  Also is there any compulsion to initialize the working storage
variables beforehand by using value clause in the WS or move
statements in the procedure division because that is one is the
changes we are doing to the code as instructed to make it reentrant.
  And i also did not understand the phrase that the program cannot
modify itself.Are they talking to some run time changes made in the
code by the program itself?
 Please throw some light on these topics,
Thanking You in advance,
Shyam Menon.






"William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message news:<a9isp4$qju$1@slb4.atl.mindspring.net>...
> The bottom-line is that if you use an IBM compiler from VS COBOL II on (eg.
> IBM COBOL for this-and-that) *and* compile with the RENT compiler option
…[47 more quoted lines elided]…
> > Shyam.
```

###### ↳ ↳ ↳ Re: Reentrant programs in Cobol

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-04-19T04:43:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c1e75c$c933b0a0$3f93f243@chottel>`
- **References:** `<10986fae.0204161943.1a2c630f@posting.google.com> <a9isp4$qju$1@slb4.atl.mindspring.net> <10986fae.0204181954.71dd7146@posting.google.com>`

```
Rentrant and mutithreading are related but somewhat different topics. A
reentrant Cobol program gives each user their own copy of working storage
without you having to worry about the details of how it does it.  The
compiler could generate code to do it, or the runtime environment could do
it, or they could both work together to do it.  Basically your original
working storage is kept somewhere and never modified.  For each user,
storage is dynamically acquired and intialized from the original copy. MVS
supplies the GETMAIN and STORAGE macros to support this and they can be
used by subsystems such as CICS or IMS or whatever to support reentrant
programs. Each user interacts with your program but modifies only their
copy of working storage.  Also your program cannot modify its code with
nasty things like ALTER GO TO. If you were coding in assembler you would
have to worry about all these issues, but COBOL is a higher level language
and all you need is the proper compiler and link edit options and you get a
reentrant program. No muss no fuss.

The lastest IBM compiler does support some forms of mulitasking for
interacting with JAVA. Some versions on the PROGRAM-ID clause let you add
"AS INITIAL" but that is used more often for serially reueable programs. 
You might also read up on the LOCAL-STORAGE SECTION.  I beleive the
programmers guide has an example of a recursive program that uses local
storage.  All of these are somewaht related but different.

Some older compilers used with CICS required extra coding to support
reentrancy. IIRC something like "SERVICE RELOAD".

shyam menon <menonshyam@yahoo.com> wrote in article
<10986fae.0204181954.71dd7146@posting.google.com>...
> Hi,
>   I am not sure i understand what you said about the reentrant
…[21 more quoted lines elided]…
> "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote in message
news:<a9isp4$qju$1@slb4.atl.mindspring.net>...
> > The bottom-line is that if you use an IBM compiler from VS COBOL II on
(eg.
> > IBM COBOL for this-and-that) *and* compile with the RENT compiler
option
> > *and* link-edit with the RENT link-edit attribute (which will be your
> > default if you don't override things), then you need do NOTHING special
in
> > your program to insure that it is "truly" re-entrant.  If you run the
> > program in any MVS (OS/390 or z/OS) environment that supports reentrant
> > programs, then everything should work "fine".
> > 
> > HOWEVER, there was a restriction in VS COBOL II (and early versions of
IBM
> > COBOL for this-and-that) on "multiple" copies of SEPARATE run-units
under
> > the same "task".  See
> > 
…[7 more quoted lines elided]…
> > NOTE: For the "new" multi-thread support, you need to use PL/I,
Assembler,
> > or USS services to "start" the simultaneous threads.
> > 
…[10 more quoted lines elided]…
> > >    So this program can be used by multiple users.But this will
require
> > > a driver like IMS or CICS to handle the MVS tasks right?
> > >
> > > 2. Is a separate copy of Working Storage alloted to each user who
uses
> > > the program or is it common for all?
> > > Can any changes be made to the data in the working storage variables
…[12 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Reentrant programs in Cobol

- **From:** "Charles Hottel" <chottel@cpcug.org>
- **Date:** 2002-04-19T05:02:31+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01c1e75f$61d14aa0$3f93f243@chottel>`
- **References:** `<10986fae.0204161943.1a2c630f@posting.google.com> <a9isp4$qju$1@slb4.atl.mindspring.net> <10986fae.0204181954.71dd7146@posting.google.com>`

```
Here is a thread from bit.listserv.ibm-main that discusses this subject
(retrieved from google).  Tom Ross is IBM's Cobol expert.

All messages from thread	

Message 1 in thread	
From: Tom Ross (tomross@VNET.IBM.COM) Subject: Fw: help running OS390 cobol
code from java  Newsgroups: bit.listserv.ibm-main	
View this article only	
Date: 2001-10-26 15:20:19 PST  	
<hightek@home.com> wrote in message
news:<PT0B7.314104$j65.83369192@news4.rdc1.on.home.com>...
> Hi there...I am new to this newsgroup, but thought I would post a problem
> that has recently come up at a work site.  The problem appears to be
…[6 more quoted lines elided]…
> and COBOL programs), and the problems with multi-threading, or making
them
> thread-safe (?), but I don't fully understand the problem.  I know the
Java
> world running under OS390 is very multithreaded....what happens to this
when
> running these COBOL modules?  I am a little unsure of the resource
> requirements of these programs and how they are actually executed (ie;
under
> the USS side, via HTTP and/or WebSphere servers, or MVS?).

I know this is an older post, but I have been very busy working on our new
COBOL compiler which supports multi-threading!  Thread-safe means that
multiple copies of a program can run in the same run unit (or enclave) and
share a single run-time library.  Things like control blocks and storage
must be allocated on a per invocation basis, rather than per program.

Anyway, current COBOL cannot run in more than one thread today, so we
diagnose
this at run time, thus the 'COBOL found in multiple threads' message.

The good news is that soon you will be able to run COBOL programs in
multiple threads.  WebSphere and Java are multi-thread environments, and
COBOL needs to be able to play those games too, so that's what we have
been working on!  Coming soon to an IBM stand near you...

Cheers,
TomR              >> COBOL is the Language of the Future! <<

----------------------------------------------------------------------
For IBM-MAIN subscribe / signoff / archive access instructions,
send email to listserv@bama.ua.edu with the message: GET IBM-MAIN INFO
Search the archives at http://bama.ua.edu/archives/ibm-main.html

Message 2 in thread	
From: Charles Hottel (chottel@cpcug.org) Subject: Re: Fw: help running
OS390 cobol code from java  Newsgroups: bit.listserv.ibm-main	
View this article only	
Date: 2001-10-26 20:05:23 PST  	
Can anyone explain to me how "thread-safe" differs from "reentrant"?

My understanding of reentrant is one copy of the code and constants with
separate dynamically acquired storage and registers for each invocation,
which I have always thought of as a "thread".  Thanks.
```

###### ↳ ↳ ↳ Re: Reentrant programs in Cobol

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-04-19T16:33:16-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a9q2et$470$1@slb4.atl.mindspring.net>`
- **References:** `<10986fae.0204161943.1a2c630f@posting.google.com> <a9isp4$qju$1@slb4.atl.mindspring.net> <10986fae.0204181954.71dd7146@posting.google.com>`

```
I think one of your problems is that you don't understand the difference
between the *COBOL code* not modifying itself versus the *generated OBJECT
code* not modifying itself.  From VS COBOL II on (even though the VS COBOL
II compiler - your compiler - is no longer supported by IBM), the RENT
compiler option makes the COMPILER create (no matter WHAT your source code
does) ASSEMBLER code (more accurately object code) that meets all the
requirements of the RENT link-edit option.

As far as the "need" to use IMS or CICS - or something else, I guess, I
don't know "where you are coming from".  Why do you care about re-entrant
code?
 - Do you have an environment  (such as CICS) that requires this for your
program?
 - Do you have a "user requirement" that makes you THINK you need to know
about this?
 - or is this just an "education" process that you want to understand about?

    ***

Bottom-Line: If you don't "know" about reentrant code, then the chances are
you don't NEED to know about it.  If you have a requirement to produce
re-entrant code, then let the compiler do it for you - and you don't need to
modify your COBOL source code at all.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
