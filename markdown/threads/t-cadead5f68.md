[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# RMCOBOL under UNIX

_3 messages · 2 participants · 1999-09_

**Topics:** [`Compilers and vendors`](../topics.md#compilers)

---

### Re: RMCOBOL under UNIX

- **From:** "Albert Ratzlaff R." <albert@conexion.com.py>
- **Date:** 1999-09-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E61FBA.918D5C9D@conexion.com.py>`
- **References:** `<7rtsi1$hde$1@nnrp1.deja.com>`

```
Tom Wymer wrote:
> 
>  Anybody familiar with running  an RMCOBOL program under UNIX?  I need
…[11 more quoted lines elided]…
> Share what you know. Learn what you don't.

Your distribution diskettes should include a program call
"rmmapinx.cob", which lets you look at the index file structure: keys,
offsets, record lengths, etc. With that information, you could write a
program to show you the contents of the file.
As for locking, it seems that RM/COBOL uses the Unix operating system
locks, one for every opened file. You almost allways have to reconfigure
the OS to add more locks to the kernel if you have more than a few
users. But that's about all I can tell. Why worry about locks?

Regards
Albert Ratzlaff
```

#### ↳ Re: RMCOBOL under UNIX

- **From:** trblshtr <trblshtr@my-deja.com>
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7s860a$e3v$1@nnrp1.deja.com>`
- **References:** `<7rtsi1$hde$1@nnrp1.deja.com> <37E61FBA.918D5C9D@conexion.com.py>`

```
In article <37E61FBA.918D5C9D@conexion.com.py>,
  "Albert Ratzlaff R." <albert@conexion.com.py> wrote:
> Tom Wymer wrote:
> >
> >  Anybody familiar with running  an RMCOBOL program under UNIX?  I
need
> > help understanding how ISAM files ure locked in a multi-user/multi-
site
> > environment and if anybody knows of a way to view ISAM files?
> > Pleas email me at twymer@hotmail.com
…[13 more quoted lines elided]…
> program to show you the contents of the file.
------------------this is essentially correct but if I recall there are
2 utilities for this purpose and the dependency is file size(?)
> As for locking, it seems that RM/COBOL uses the Unix operating system
> locks, one for every opened file. You almost allways have to
reconfigure
> the OS to add more locks to the kernel if you have more than a few
Suggest you read the RM documentation regarding file handling to
understand record vs file level locking. It might also be covered under
the "Open" verb. Either is available and each has a specific purpose.
While it is true that the kernel level lock resources may need to be
increased it is just as possible that they can be decreased -- this is
a matter of standard UNIX system tuning and really has nothing to do
with whether you are talking about RM or any other language used for
development.
> users. But that's about all I can tell. Why worry about locks?
>
Let's hope that when developing applications for a multiuser/site
environment that he *does* "worry about locks" regardless of the
language used.  Failure to do so *can be* and *usually is* a formula
for disaster.  This is particularly true when dealing with critical
information.

> Regards
> Albert Ratzlaff
>

Cordially,
trblshtr
```

##### ↳ ↳ Re: RMCOBOL under UNIX

- **From:** "Albert Ratzlaff R." <albert@conexion.com.py>
- **Date:** 1999-09-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37E800B8.C4CD48BB@conexion.com.py>`
- **References:** `<7rtsi1$hde$1@nnrp1.deja.com> <37E61FBA.918D5C9D@conexion.com.py> <7s860a$e3v$1@nnrp1.deja.com>`

```
trblshtr wrote:
> 
> In article <37E61FBA.918D5C9D@conexion.com.py>,
…[22 more quoted lines elided]…
> 2 utilities for this purpose and the dependency is file size(?)

In my distribution(s) there is only one utility for looking at indexed
file structures. There are 2 utilities for converting relative files
from previous versiones, depending on record size.

> > As for locking, it seems that RM/COBOL uses the Unix operating system
> > locks, one for every opened file. You almost allways have to reconfigure
…[8 more quoted lines elided]…
> development.

When responding to the original message I had the impresion the sender
was looking for operating specific information on how locks are
implemented. After re-reading the post, I'm not so sure. But of course
you are right about worrying about file and record locking in general.

> > users. But that's about all I can tell. Why worry about locks?
> >
…[16 more quoted lines elided]…
> Share what you know. Learn what you don't.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
