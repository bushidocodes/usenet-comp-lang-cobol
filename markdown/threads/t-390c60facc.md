[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Compiling a COBOL program both as Batch and Online

_5 messages · 5 participants · 1999-07_

---

### Compiling a COBOL program both as Batch and Online

- **From:** "Raghu" <raghubabu@mindspring.com>
- **Date:** 1999-07-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7mq97u$vv7$1@nntp1.atl.mindspring.net>`

```
Hi,

I would like to compile  Cobol programs so that two
load modules (one is batch and other one is Online used
by CICS) are created.

I can modify the JCL to create two load modules. But
are there any specific procedures I need to be aware of.
Because, If I'm calling another program inside my program
online version expects two parms : DFHEIBLK and
DFHCOMMAREA.  I can't have two copies of same program
one for batch and one for online, I would like to achieve
this with one copy of source.
Any suggestions,
Thanks
```

#### ↳ Re: Compiling a COBOL program both as Batch and Online

- **From:** "Steve Beattie" <steve@sbeattie.freeserve.co.uk>
- **Date:** 1999-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7msl0e$vh8$1@news4.svr.pol.co.uk>`
- **References:** `<7mq97u$vv7$1@nntp1.atl.mindspring.net>`

```
I've no doubt someone will correct me if I'm wrong, but why don't you just
use a CALL statement in your CICS program (as long as you're using VS Cobol
II) to invoke the subroutine.  The main program will remain in main storage.
Remember to use a GOBACK or EXIT PROGRAM in the subroutine.

Hope this helps, Steve.

---
Steve@sbeattie.removeme.freeserve.co.uk
http://www.sbeattie.freeserve.co.uk/index.html

To reply remove 'removeme' from email address.

Play Java Asteroids at the above site.


Raghu <raghubabu@mindspring.com> wrote in message
news:7mq97u$vv7$1@nntp1.atl.mindspring.net...
> Hi,
>
…[16 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Compiling a COBOL program both as Batch and Online

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37930F95.697C70EC@zip.com.au>`
- **References:** `<7mq97u$vv7$1@nntp1.atl.mindspring.net> <7msl0e$vh8$1@news4.svr.pol.co.uk>`

```
Steve Beattie wrote:
> 
> I've no doubt someone will correct me if I'm wrong, but why don't you
…[5 more quoted lines elided]…
> Hope this helps, Steve.

The routine must be statically linked and not do anything that is
anti-CICS.
```

###### ↳ ↳ ↳ Re: Compiling a COBOL program both as Batch and Online

- **From:** "Roland Schiradin" <schiradi@tap.de>
- **Date:** 1999-07-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7n0414$2jt$1@black.news.nacamar.net>`
- **References:** `<7mq97u$vv7$1@nntp1.atl.mindspring.net> <7msl0e$vh8$1@news4.svr.pol.co.uk> <37930F95.697C70EC@zip.com.au>`

```
Ken

> The routine must be statically linked and not do anything that is
> anti-CICS.
The sub-prog can be called dynamic (call variable) or staticly.

Roland
```

#### ↳ Re: Compiling a COBOL program both as Batch and Online

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-07-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3791DC69.A6DC5FB0@techie.com>`
- **References:** `<7mq97u$vv7$1@nntp1.atl.mindspring.net>`

```
Options:

1.  Use a front end to the batch program to call the online
program with the two extra parameters.  (Of course, the online
program is smart enough not to try and use them in the batch
environment!)

2.  Use an entry point into the program for the batch invocation. 
This is required if you need the PARM field from the EXEC card as
that comes in the first parameter in batch.

3. If you don't need the PARM field, then you can use the same
entry point.

4.  If you truly do not need any CICS support in the program when
it runs online, compile it twice.  Once with the CICS preprocessor
and one without.  All the preprocessor will do is make one version
receive the two extra CICS parameters in the online version. 

5.  If this is a subroutine, then you don't HAVE to call with the
two extra parameters unless you need them, i.e. are going to
request CICS services.  We have many subroutines (e.g. table
lookups) which are called without the extra two parameters in the
online environment.  Remember that the CICS preprocessor will
tweak you entry points where you receive parameters, but it does
not do anything to the CALLs where you pass parameters.

6.  You can use the SET statement to interchange pointers passed
to you.    There is a pseudo register (special name) for each 01
level in the LINKAGE SECTION.  You can assign the ADDRESS OF one
01 level to another.  I've used this to adjust things at the front
of a program to correct for the different parameters passed in
batch and CICS.

Raghu wrote:
> 
> Hi,
…[13 more quoted lines elided]…
> Thanks
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
