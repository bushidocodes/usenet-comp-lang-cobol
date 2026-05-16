[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Executable files

_7 messages · 5 participants · 2001-05_

---

### Executable files

- **From:** <yotch27@hotmail.com>
- **Date:** 2001-05-16T17:30:09
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tg5e91kb0pbh61@corp.supernews.com>`

```
How do you convert a cobol program from source code to an executable file? 
I wrote the code, but say I wanted to give the program to someone, how 
would I convert it so they couldn't actually read my code?
```

#### ↳ Re: Executable files

- **From:** "Robert Heady" <r.heady@liant.com>
- **Date:** 2001-05-16T14:28:14-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<80BM6.66$kc4.1735@nnrp1.sbc.net>`
- **References:** `<tg5e91kb0pbh61@corp.supernews.com>`

```
Uh, compile it?

yotch27@hotmail.com wrote in message ...
>How do you convert a cobol program from source code to an executable file?
>I wrote the code, but say I wanted to give the program to someone, how
…[4 more quoted lines elided]…
>http://www.help.com/
```

##### ↳ ↳ Re: Executable files

- **From:** "Calin Macrinici" <cmac@pathcom.com>
- **Date:** 2001-05-16T22:27:47+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D9DM6.38211$yw.990349@news20.bellglobal.com>`
- **References:** `<tg5e91kb0pbh61@corp.supernews.com> <80BM6.66$kc4.1735@nnrp1.sbc.net>`

```
That's very smart, but you're probably gonna have to link it, too!

The linkers are (usually) separate from the COBOL packages (i.e. on Windows
you would use the Microsoft linker), although in most cases the COBOL
vendors include the correct linker for your environment with their product.
Also, depending on the COBOL environment you're using, you will probably
have to link some libraries in your exe.

In some cases (as with Merant, for example, when you put more functionality
than "hello world" in your program), you will probably have to ship your exe
and some auxilliary files (they're called run-time components, and they can
be libraries, dlls, or proprietary format files).

That's about it, enjoy!

Calin, TORONTO

"Robert Heady" <r.heady@liant.com> wrote in message
news:80BM6.66$kc4.1735@nnrp1.sbc.net...
> Uh, compile it?
>
> yotch27@hotmail.com wrote in message ...
> >How do you convert a cobol program from source code to an executable
file?
> >I wrote the code, but say I wanted to give the program to someone, how
> >would I convert it so they couldn't actually read my code?
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Executable files

- **From:** <yotch27@hotmail.com>
- **Date:** 2001-05-17T16:30:09
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tg7v4hqkp6vaab@corp.supernews.com>`
- **References:** `<tg5e91kb0pbh61@corp.supernews.com> <80BM6.66$kc4.1735@nnrp1.sbc.net> <D9DM6.38211$yw.990349@news20.bellglobal.com>`

```
You don't happen to know how to link a cobol program that was written 
using microfocus?
Calin Macrinici wrote:
> 
> 
> That's very smart, but you're probably gonna have to link it, too!
> 
> The linkers are (usually) separate from the COBOL packages (i.e. on 
Windows
> you would use the Microsoft linker), although in most cases the COBOL
> vendors include the correct linker for your environment with their 
product.
> Also, depending on the COBOL environment you're using, you will probably
> have to link some libraries in your exe.
> 
> In some cases (as with Merant, for example, when you put more 
functionality
> than "hello world" in your program), you will probably have to ship your 
exe
> and some auxilliary files (they're called run-time components, and they 
can
> be libraries, dlls, or proprietary format files).
> 
…[20 more quoted lines elided]…
> 
```

##### ↳ ↳ Re: Executable files

- **From:** <yotch27@hotmail.com>
- **Date:** 2001-05-17T16:30:09
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<tg7v4h5s38t4a9@corp.supernews.com>`
- **References:** `<tg5e91kb0pbh61@corp.supernews.com> <80BM6.66$kc4.1735@nnrp1.sbc.net>`

```
Uh, I did compile it, I didn't want to know how to make it run, I wanted 
to know how I could transfer it so it would be almost like a software 
package. Comiling it only allows it to run.  I want to know how I can give 
it to someone else without them being able to actually view the code, but 
thanks for the useless smart ass answer though.  I appreciate it.
Robert Heady wrote:
> 
> 
…[3 more quoted lines elided]…
> >How do you convert a cobol program from source code to an executable 
file?
> >I wrote the code, but say I wanted to give the program to someone, how
> >would I convert it so they couldn't actually read my code?
…[5 more quoted lines elided]…
> 
```

###### ↳ ↳ ↳ Re: Executable files

- **From:** "Alister Munro" <alister@specsoft.freeserve.co.uk>
- **Date:** 2001-05-18T01:30:29+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9e1mla$p8v$1@news6.svr.pol.co.uk>`
- **References:** `<tg5e91kb0pbh61@corp.supernews.com> <80BM6.66$kc4.1735@nnrp1.sbc.net> <tg7v4h5s38t4a9@corp.supernews.com>`

```
When you compile the program it is converted into the machines own
language which results in an object file which can then be 'link'ed to
produce the final executable version. Neither the obj or the exe produced
from these process's resembles the source code that you wrote.

<yotch27@hotmail.com> wrote in message
news:tg7v4h5s38t4a9@corp.supernews.com...
> Uh, I did compile it, I didn't want to know how to make it run, I wanted
> to know how I could transfer it so it would be almost like a software
…[23 more quoted lines elided]…
> http://www.help.com/
```

###### ↳ ↳ ↳ Re: Executable files

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2001-05-18T19:35:50+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3B056B86.F682BB0E@Azonic.co.nz>`
- **References:** `<tg5e91kb0pbh61@corp.supernews.com> <80BM6.66$kc4.1735@nnrp1.sbc.net> <tg7v4h5s38t4a9@corp.supernews.com>`

```
yotch27@hotmail.com wrote:
> 
> Uh, I did compile it, I didn't want to know how to make it run, I wanted
…[3 more quoted lines elided]…
> thanks for the useless smart ass answer though.  I appreciate it.

'Compile it' is the actual answer to your question and wasn't being
'smart ass'.

Most compilers read the source code and write an executable file that
may be name.EXE or name.INT or somesuch.  Sometimes these can be
completely stand-alone but some cobol systems require a 'run-time' in
order for these to execute.  This run-time may require to be purchased,
in other cases free distribution may be possible.

It all depends on the compiler that you use.  As you omitted this vital
piece of information then it becomes impossible to be any more specific
than 'compile it' or 'RTFM'.

If I were to make a guess then I would hazard that you use MF's student
edition of Cobol.  This product has no means of creating a distributable
executable, nor would distributing the compiler itself be legal.  This
is a deliberate restriction of the student edition.

Now start again, this time giving adequate information to get a useful
answer.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
