[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# New topic

_11 messages · 7 participants · 1998-11_

---

### New topic

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72a6u1$jlr$1@news.igs.net>`

```
You know, over the last year I have read in this echo
how to call Java from Cobol, how to call assembler
from Cobol, how to call Pascal from Cobol, how to call
C from Cobol, how to call Basic from Cobol, how to call
excel from Cobol, how to call DB2 from Cobol, plus a
couple that I am probably missing.

The one thing that I have *not* read, is how to call one
Cobol from another. For example, how to I call a Fujitsu
DLL from Micro Focus?  Or vice-versa?  If I cannot,
why not?  Ninety-nine percent of all conversion problems
would go away if I could.  All Cobol data would then be created
equal.

Perhaps the new standard should require the ability for
a compiler to call at least one other Cobol on the same platform;
of course since a subroutine can call a subroutine I could then
take the most common, write a whole bunch of calls that simply
call another language, stick them in a library ... naw that
would be too simple ...
```

#### ↳ Re: New topic

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-5MnoutHLS0kk@Dwight_Miller.iix.com>`
- **References:** `<72a6u1$jlr$1@news.igs.net>`

```
On Tue, 10 Nov 1998 20:17:10, "Donald Tees" <donald@willmack.com> 
wrote:

> The one thing that I have *not* read, is how to call one
> Cobol from another. For example, how to I call a Fujitsu
…[4 more quoted lines elided]…
> 

I created an EXTFH caller from Realia COBOL - and it did not work.  
Crashed the machine any time.  However - this was Realia calling MF - 
I think you could get your docs out for EXTFH and create a program 
from Fujitsu (16 bit for Windows 3.1) to call the Windows 3.1 DLL from
MF.
```

##### ↳ ↳ Re: New topic

- **From:** redsky@ibm.net (Thane Hubbell)
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Jl0PnHJ5PvPd-pn2-JZWzHc5wLEZ7@Dwight_Miller.iix.com>`
- **References:** `<72a6u1$jlr$1@news.igs.net> <Jl0PnHJ5PvPd-pn2-5MnoutHLS0kk@Dwight_Miller.iix.com>`

```
On Tue, 10 Nov 1998 22:58:53, redsky@ibm.net (Thane Hubbell) wrote:

> On Tue, 10 Nov 1998 20:17:10, "Donald Tees" <donald@willmack.com> 
> wrote:
…[15 more quoted lines elided]…
> 

PS - the reason I did not suggest 32 bit is that I know Don does not 
have NetExpress - but if he did .... 32 bit with 32 bit Fujitsu would 
be an option.
```

#### ↳ Re: New topic

- **From:** "Warren G. Simmons" <warrens@inficad.com>
- **Date:** 1998-11-10T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3648BCB5.6E57F132@inficad.com>`
- **References:** `<72a6u1$jlr$1@news.igs.net>`

```
Right on, Donald!

Warren

Donald Tees wrote:
> 
----<snip>-----
> 
> Perhaps the new standard should require the ability for
…[4 more quoted lines elided]…
> would be too simple ...
```

#### ↳ Re: New topic

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364a0799.0@news3.uswest.net>`
- **References:** `<72a6u1$jlr$1@news.igs.net>`

```

Donald Tees wrote in message <72a6u1$jlr$1@news.igs.net>...
>You know, over the last year I have read in this echo
>how to call Java from Cobol, how to call assembler
…[18 more quoted lines elided]…
>

I don't know how easy it would be in most languages, but doesn't IBM
OS/390's (et al older versions) assembly language support calling COBOL
programs?

Could PL/I call a COBOL program?
```

##### ↳ ↳ Called COBOL

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-11-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364A0BEC.95D1695E@home.com>`
- **References:** `<72a6u1$jlr$1@news.igs.net> <364a0799.0@news3.uswest.net>`

```
I am sure that the vast majority of us can say the following:

I have had COBOL programs call other COBOL programs all the time.  I
have had the called programs be in different ANSI versions, but not
different manufacturers.

I have had COBOL programs call assembly language programs and C
programs.  Obviously I have had pre-compilers call assembly programs.

So what's the question?  Once you know how a language wants its parms to
be passed, can't any language call any other language?  It's all machine
language once compiled anyway.

I suppose it's more complex when the called program is interpreted or OS
based, such as REXX, CLISTs or DOS commands.

I think I am missing something in this thread.
```

###### ↳ ↳ ↳ Re: Called COBOL

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72eq46$h5p$1@news.igs.net>`
- **References:** `<72a6u1$jlr$1@news.igs.net> <364a0799.0@news3.uswest.net> <364A0BEC.95D1695E@home.com>`

```
Howard Brazee wrote in message <364A0BEC.95D1695E@home.com>...
>I am sure that the vast majority of us can say the following:
>
>I have had COBOL programs call other COBOL programs all the time.  I
>have had the called programs be in different ANSI versions, but not
>different manufacturers.


Yes, that is the point.  Why not?
```

##### ↳ ↳ Re: New topic

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72epvp$h3h$1@news.igs.net>`
- **References:** `<72a6u1$jlr$1@news.igs.net> <364a0799.0@news3.uswest.net>`

```
Chris Osborne wrote in message <364a0799.0@news3.uswest.net>...

>I don't know how easy it would be in most languages, but doesn't IBM
>OS/390's (et al older versions) assembly language support calling COBOL
>programs?
>
>Could PL/I call a COBOL program?


As far as I can see, *Cobol* is the only language Cobol
cannot call.
```

###### ↳ ↳ ↳ Re: New topic

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<364BABB8.9FD287CD@att.net>`
- **References:** `<72a6u1$jlr$1@news.igs.net> <364a0799.0@news3.uswest.net> <72epvp$h3h$1@news.igs.net>`

```
Donald Tees wrote:
> 
> Chris Osborne wrote in message <364a0799.0@news3.uswest.net>...
…[8 more quoted lines elided]…
> cannot call.

Huh? I have many COBOL programs, some of which call other COBOL
programs. Did I miss a transition or something?

Bill Lynch
```

###### ↳ ↳ ↳ Re: New topic

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72hagm$fju$1@news.igs.net>`
- **References:** `<72a6u1$jlr$1@news.igs.net> <364a0799.0@news3.uswest.net> <72epvp$h3h$1@news.igs.net> <364BABB8.9FD287CD@att.net>`

```

William Lynch wrote in message <364BABB8.9FD287CD@att.net>...

>> As far as I can see, *Cobol* is the only language Cobol
>> cannot call.
>
>Huh? I have many COBOL programs, some of which call other COBOL
>programs. Did I miss a transition or something?


How about Fujitsu 4 calling MicroFocus 3.5?  Or netexpress
using a Fujitsu DLL?  Why should those be more difficult than
Fujitsu or Netexpress calling Visual Basic?  If all Cobol compilers
on a given platform could call all *other Cobol* subroutines on
that platform, regardless of compiler, then conversions would
be a 1000 times easier, all Isams would be equal, all screen
sections available, etc., etc., etc.,
```

###### ↳ ↳ ↳ Re: New topic

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<72htr2$97g@sjx-ixn5.ix.netcom.com>`
- **References:** `<72a6u1$jlr$1@news.igs.net> <364a0799.0@news3.uswest.net> <72epvp$h3h$1@news.igs.net> <364BABB8.9FD287CD@att.net> <72hagm$fju$1@news.igs.net>`

```

Donald Tees wrote in message <72hagm$fju$1@news.igs.net>...
>
>William Lynch wrote in message <364BABB8.9FD287CD@att.net>...
…[16 more quoted lines elided]…
>

There was an interesting J4 interpretation about this a few years ago.  The
bottom-line is that one COBOL compiler can treat another vendor's compiler
as a "foreign" language.  In fact, this is made explicit in the draft of the
next Standard.  It means that often a COBOL program *CAN* call another
vendor's COBOL program - but only using the non-COBOL rules (such as not
sharing DISPLAY output, EXTERNAL data, etc).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
