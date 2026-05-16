[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Micro Focus User-Written File Handler Problems

_4 messages · 3 participants · 1999-08 → 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Micro Focus User-Written File Handler Problems

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cae3a8@news1.us.ibm.net>`

```
To anyone that can help,

I have written a callable file handler for use with Micro Focus Workbench
and Netexpress.

The problem I am having is getting it to work correctly when compiled to a
.DLL.  When I animate through the code (source calling the file handler and
the file handler itself) it works fine.  I am using a CBL_ERROR_PROC call in
the file handler, but do have the priority flag set to 200.  The error that
I receive is "200 - Internal Logic Error".

I am currently testing with Cobol Workbench 4.0.26, using "cob.exe
filehand.cbl -x:csd" command-line to create a .DLL that utilizes the MF
Dynamic Run-Time System environment.

Does anyone have any ideas?

If so could you please e-mail me at Todd.Lucas@ibm.net, as I do not check
this message board very often...

Thanks - Todd
```

#### ↳ Re: Micro Focus User-Written File Handler Problems

- **From:** "Ken Mullins" <KenMullins@mindspring.com>
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qeqi1$cnf$1@nntp2.atl.mindspring.net>`
- **References:** `<37cae3a8@news1.us.ibm.net>`

```
.....To anyone that can help,

.....I have written a callable file handler for use with Micro Focus
Workbench
.....and Netexpress.

.....The problem I am having is getting it to work correctly when compiled
to a
......DLL.  When I animate through the code (source calling the file handler
and
.....the file handler itself) it works fine.  I am using a CBL_ERROR_PROC
call in
.....the file handler, but do have the priority flag set to 200.  The error
that
.....I receive is "200 - Internal Logic Error".

.....I am currently testing with Cobol Workbench 4.0.26, using "cob.exe
.....filehand.cbl -x:csd" command-line to create a .DLL that utilizes the MF
.....Dynamic Run-Time System environment.

.....Does anyone have any ideas?

.....If so could you please e-mail me at Todd.Lucas@ibm.net, as I do not
check
.....this message board very often...

.....Thanks - Todd

MF has a problem with being able to handle duplicate entry points within a
module and a dll being called by that module...Is the normal MF file handler
loaded also?

I discovered the problem when trying to call a DLL from a program when both
modules had a duplicate entry point...for ex the root called a calc routine
and the dll calls the same calc routine...I received internal logic
error...The runtime doesn't know what do do in this case...

kenmullins
```

##### ↳ ↳ Re: Micro Focus User-Written File Handler Problems

- **From:** "Lucas, Todd" <todd.lucas@ibm.net>
- **Date:** 1999-09-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37cd24f5@news1.us.ibm.net>`
- **References:** `<37cae3a8@news1.us.ibm.net> <7qeqi1$cnf$1@nntp2.atl.mindspring.net>`

```
Ken,

Thanks for the response - I figured it out.  Just for your knowledge, when
using a calling-convention of 74 (win32api) you must use an "exit program
returning" statement instead of a "goback" in any subroutines that are
called.  This is the only thing that I changed in my program, and it fixed
the problem.  Weird, huh?

Thanks again for taking the time.

TL

>MF has a problem with being able to handle duplicate entry points within a
>module and a dll being called by that module...Is the normal MF file
handler
>loaded also?
>
…[9 more quoted lines elided]…
>
```

#### ↳ Re: Micro Focus User-Written File Handler Problems

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-08-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7qf83m$brm@dfw-ixnews6.ix.netcom.com>`
- **References:** `<37cae3a8@news1.us.ibm.net>`

```
Have you looked at using the CALLFH directive? It has been a while, but my
memory is that this is used to determine WHAT file-handler is called?
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
