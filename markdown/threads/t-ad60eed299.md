[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Need Help VA COBOL Compiler

_3 messages · 2 participants · 2001-10_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Need Help VA COBOL Compiler

- **From:** "Denis A. Chesnokov" <ches@tercom.ru>
- **Date:** 2001-10-17T17:05:42+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9qjvmv$2atl$1@news.spbu.ru>`

```
Hello all. How change working directory from current to MyDirectory for VA
Cobol compiler (cob2.exe) if i work from command-line?
Denis
```

#### ↳ Re: Need Help VA COBOL Compiler

- **From:** Gary Mazo <mazoi@yahoo.com>
- **Date:** 2001-10-17T15:25:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3BCE0567.89ED0C7C@yahoo.com>`
- **References:** `<9qjvmv$2atl$1@news.spbu.ru>`

```
Denis,
It depends on what you mean by "working directory".  There are
many files in many directories used by cob2.  Location of some
can be controlled by environment variables, some cannot be controlled at all.
The compiler listing (starting with Version 3 of the compiler) can be
controlled
by COBLSTDIR variable.  Object file goes into the current directory and there
is no way to
control that. Location for the executable file could be controlled with the
/OUT option
for the linker.
Compiler work files go into the path specified in the TEMP
environment variable or the current directory if TEMP is not specified or is
invalid.

The best way to do what you want
is to cd into MyDirectory and execute the cob2 from there.

Uspehov - Good luck.

Gary

"Denis A. Chesnokov" wrote:

> Hello all. How change working directory from current to MyDirectory for VA
> Cobol compiler (cob2.exe) if i work from command-line?
> Denis
```

##### ↳ ↳ Re: Need Help VA COBOL Compiler

- **From:** "Denis A. Chesnokov" <ches@tercom.ru>
- **Date:** 2001-10-18T12:31:05+03:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9qm3vt$6ot$1@news.spbu.ru>`
- **References:** `<9qjvmv$2atl$1@news.spbu.ru> <3BCE0567.89ED0C7C@yahoo.com>`

```
Thank you Gary Mazo, you give me answer for my question.

Yours sincerely. Denis A Chesnokov
"Gary Mazo" <mazoi@yahoo.com> wrote in message
news:3BCE0567.89ED0C7C@yahoo.com...
> Denis,
> It depends on what you mean by "working directory".  There are
> many files in many directories used by cob2.  Location of some
> can be controlled by environment variables, some cannot be controlled at
all.
> The compiler listing (starting with Version 3 of the compiler) can be
> controlled
> by COBLSTDIR variable.  Object file goes into the current directory and
there
> is no way to
> control that. Location for the executable file could be controlled with
the
> /OUT option
> for the linker.
> Compiler work files go into the path specified in the TEMP
> environment variable or the current directory if TEMP is not specified or
is
> invalid.
>
…[9 more quoted lines elided]…
> > Hello all. How change working directory from current to MyDirectory for
VA
> > Cobol compiler (cob2.exe) if i work from command-line?
> > Denis
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
