[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Q: Error Handling

_9 messages · 8 participants · 1999-10_

---

### Q: Error Handling

- **From:** "Desmond Johnson" <crud-mucosa@worldnet.att.net>
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
Greetings,

  I am a mid-level COBOL programmer still trying to learn this language. I
am working on a project where I need to have my program return an error code
number so that the JCL that runs it can selectively execute other programs
associated with it. My question: How do I get COBOL to return a programmer
defined error code number?

  Thanks,
 Crud
```

#### ↳ Re: Q: Error Handling

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991024135911.06363.00000209@ngol07.aol.com>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
In article <7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>, "Desmond Johnson"
<crud-mucosa@worldnet.att.net> writes:

> I am a mid-level COBOL programmer still trying to learn this language. I
>am working on a project where I need to have my program return an error code
…[3 more quoted lines elided]…
>

In the IBM MainFrame environment there is a 'special register/reserved field'
RETURN-CODE that you can move a number to which is passed to the 
JCL as the closing COND CODE.   The interla definition of the field S9(4) Comp.

Would this be what you are looking for?
```

#### ↳ Re: Q: Error Handling

- **From:** Clark Morris <morrisc@nbnet.nb.ca>
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<381360BB.5A3D9325@nbnet.nb.ca>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
If you are using an IBM COBOL on MVS, OS390 or VM, MOVE value to
RETURN-CODE where RETURN-CODE is an IBM extension defined as S9(4) COMP
(or BINARY in COBOL II and beyond).  Value can be either a constant or a
numeric field.

Clark Morris, CFM Technical Programming Services  

Desmond Johnson wrote:
> 
> Greetings,
…[8 more quoted lines elided]…
>  Crud
```

#### ↳ Re: Q: Error Handling

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38136905.56984985@news1.attglobal.net>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
On Sun, 24 Oct 1999 12:29:42 -0400, "Desmond Johnson"
<crud-mucosa@worldnet.att.net> wrote:

>Greetings,
>
…[5 more quoted lines elided]…
>

Just move a number to the reserved word Return-Code.

For example, in some jobs I have :  Move 12 to Return-Code

This sets the condition code to 12 for the program execution step.

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Error Handling

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-10-24T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v00gq$2ts$1@news.igs.net>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
If you are running Fujitsu, you move the error to the variable
"program-status" immediately before your goback.

Desmond Johnson wrote in message <7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>...
>Greetings,
>
>  I am a mid-level COBOL programmer still trying to learn this language. I
>am working on a project where I need to have my program return an error
code
>number so that the JCL that runs it can selectively execute other programs
>associated with it. My question: How do I get COBOL to return a programmer
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Error Handling

- **From:** "Russell Styles" <RWSTYLES@COMPUSERVE.COM>
- **Date:** 1999-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v1tqf$cs1$1@ssauraac-i-1.production.compuserve.com>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
    On MF, dos/win, "STOP RUN 1." will return error code "01".

Desmond Johnson <crud-mucosa@worldnet.att.net> wrote in message
news:7uvc4c$1c6$1@bgtnsc03.worldnet.att.net...
> Greetings,
>
>   I am a mid-level COBOL programmer still trying to learn this language. I
> am working on a project where I need to have my program return an error
code
> number so that the JCL that runs it can selectively execute other programs
> associated with it. My question: How do I get COBOL to return a programmer
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Error Handling

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v022a$g4c$1@news.inet.tele.dk>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
Before you go into a great number of different return-codes, check the
installation standards. Cond codes can be used to control the batch-flow,
and each installation can be different in their use of CC's.

I know of installations, where CC= 4 is a warning (the program handled the
error) while CC=4 in other installations simply stops the flow.

regards
Ib
Desmond Johnson skrev i meddelelsen
<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>...
>Greetings,
>
>  I am a mid-level COBOL programmer still trying to learn this language. I
>am working on a project where I need to have my program return an error
code
>number so that the JCL that runs it can selectively execute other programs
>associated with it. My question: How do I get COBOL to return a programmer
…[5 more quoted lines elided]…
>
```

#### ↳ Re: Q: Error Handling

- **From:** postingid@dissensoftware.com (Binyamin Dissen)
- **Date:** 1999-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gk181sgp3p3r8uj9cn27qcfplgc0jmpp0o@4ax.com>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net>`

```
On Sun, 24 Oct 1999 12:29:42 -0400 "Desmond Johnson"
<crud-mucosa@worldnet.att.net> wrote:

:>  I am a mid-level COBOL programmer still trying to learn this language. I
:>am working on a project where I need to have my program return an error code
:>number so that the JCL that runs it can selectively execute other programs
:>associated with it. My question: How do I get COBOL to return a programmer
:>defined error code number?

From: Language Reference COBOL for OS/390 & VM (SC26-9046-00)

1.1.3.5 RETURN-CODE
 
The RETURN-CODE special register can be used to pass information between
separately-compiled programs.
 
You can set the RETURN-CODE special register to pass a return code to the
program or the system before executing a STOP RUN statement.  It has the
implicit definition:
 
  01  RETURN-CODE GLOBAL PICTURE S9(4) USAGE BINARY VALUE ZERO
 
The following are examples of how to set the RETURN-CODE special register:
 
  COMPUTE RETURN-CODE = 8
 
or
 
  MOVE 8 to RETURN-CODE.
 
When control returns to the operating system, the special register contents
are returned as a user return code.  When used in nested programs, this
special register is implicitly defined in the outermost program.
```

##### ↳ ↳ Re: Q: Error Handling

- **From:** "Desmond Johnson" <crud-mucosa@worldnet.att.net>
- **Date:** 1999-10-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7v2jm3$juc$1@bgtnsc02.worldnet.att.net>`
- **References:** `<7uvc4c$1c6$1@bgtnsc03.worldnet.att.net> <gk181sgp3p3r8uj9cn27qcfplgc0jmpp0o@4ax.com>`

```
I got a good number of responses to this question.  Thanks to all who
took time to respond to me, you helped me find what I was looking for.

Thanks again,
--Crud
Binyamin Dissen <postingid@dissensoftware.com> wrote in message
news:gk181sgp3p3r8uj9cn27qcfplgc0jmpp0o@4ax.com...
> On Sun, 24 Oct 1999 12:29:42 -0400 "Desmond Johnson"
> <crud-mucosa@worldnet.att.net> wrote:
>
> :>  I am a mid-level COBOL programmer still trying to learn this language.
I
> :>am working on a project where I need to have my program return an error
code
> :>number so that the JCL that runs it can selectively execute other
programs
> :>associated with it. My question: How do I get COBOL to return a
programmer
> :>defined error code number?
>
…[21 more quoted lines elided]…
> When control returns to the operating system, the special register
contents
> are returned as a user return code.  When used in nested programs, this
> special register is implicitly defined in the outermost program.
…[6 more quoted lines elided]…
> Director, Dissen Software, Bar & Grill - Israel
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
