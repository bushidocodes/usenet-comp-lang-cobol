[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# power cobol

_5 messages · 2 participants · 1998-11 → 1998-12_

---

### power cobol

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73pmjr$k6s$1@news.igs.net>`

```
Has anybody figured out a way for a power Cobol program
to either:  1.  return an error code (as an exe module)
                 2. accept an input argument (as a linkable [DLL or
otherwise] subroutine).
or              3. produce an output argument (ditto to number 2).

The only way that I can seem to pass data either into or
out of a power Cobol program is as a global external area
and that simply will not work in my application.  I can get data
into an exe module produced by power Cobol by introducing
it on the command line, but there appears to be no way to get
an answer back as the PROGRAM-STATUS register is used
internally and never makes it back to the starting program.

There also appears to be no way to write a power Cobol
subroutine, as all power Cobol programs *are* subroutines
started by the "opensheet" subroutine, and you cannot vary
the opensheet arguments.
```

#### ↳ Re: power cobol

- **From:** "DENNIS A BROUSE" <DENDEN@prodigy.net>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73u13a$4tlu$1@newssvr04-int.news.prodigy.com>`
- **References:** `<73pmjr$k6s$1@news.igs.net>`

```
Donald,
   Although I'm a novice at Powercobol, I have a Powercobol application that
communicates both ways with another application using DDE.  I realize that
this is not exactly what you are looking for, but the use of DDE in itself
implies that Powercobol can handle passing data between to different
applications.  If I have some time at work today, I'll see if I can dig into
it a little deeper.  Of course, it IS Monday!  Good luck.

Denny
```

##### ↳ ↳ Re: power cobol

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73u8pm$16m$1@news.igs.net>`
- **References:** `<73pmjr$k6s$1@news.igs.net> <73u13a$4tlu$1@newssvr04-int.news.prodigy.com>`

```

DENNIS A BROUSE wrote in message <73u13a$4tlu$1@newssvr04-

Yes, I have DDE working too.  It and global data both seem to work fine
as a "speak" method.  What I cannot seem to do is write a subroutine.

int.news.prodigy.com>...
>Donald,
>   Although I'm a novice at Powercobol, I have a Powercobol application
that
>communicates both ways with another application using DDE.  I realize that
>this is not exactly what you are looking for, but the use of DDE in itself
>implies that Powercobol can handle passing data between to different
>applications.  If I have some time at work today, I'll see if I can dig
into
>it a little deeper.  Of course, it IS Monday!  Good luck.
>
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: power cobol

- **From:** "DENNIS A BROUSE" <DENDEN@prodigy.net>
- **Date:** 1998-11-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73vn27$3444$1@newssvr04-int.news.prodigy.com>`
- **References:** `<73pmjr$k6s$1@news.igs.net> <73u13a$4tlu$1@newssvr04-int.news.prodigy.com> <73u8pm$16m$1@news.igs.net>`

```
Donald,
     Looked in my notes today regarding Fujitsu Powercobol "called"
subroutines and it looks like the "global external data/opensheet"
environment is the only way to do it unless there's an undocumented feature
laying around somewhere.  I could have sworn that I read something on
creating custom controls that might fit the bill here, but I'll be darned if
I could find it today.  I'm in the process of re-writing our MicroFocus
COBOL programs into Fujitsu Powercobol, and I have a BBS program that will
need this feature to update the BBS database.  I may call Fujitsu support
when I get to that point and just ask.  Right now I'm still finishing up the
custom DDE interface to our mainframe terminal emulation program.  At least
for that application, we're communicating just fine and dandy.  It just
seems weird that you can call a Powercobol subroutine from regular Fujitsu
COBOL, but can't  call one from another Powercobol program.  If you get it
to work, it would be great if you could post how you did it.  I'll certainly
do the same, if I happen upon it relatively soon.

Denny
```

###### ↳ ↳ ↳ Re: power cobol

_(reply depth: 4)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-12-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<740tue$r1c$1@news.igs.net>`
- **References:** `<73pmjr$k6s$1@news.igs.net> <73u13a$4tlu$1@newssvr04-int.news.prodigy.com> <73u8pm$16m$1@news.igs.net> <73vn27$3444$1@newssvr04-int.news.prodigy.com>`

```
Yes, I have found it a bit weird as well.  The other thing I have
been attempting (and not able to do) is return an error-code.
The program-status register is used internally, and always
seems to get reset back to zero.

DENNIS A BROUSE wrote in message
<73vn27$3444$1@newssvr04-int.news.prodigy.com>...
>Donald,
>     Looked in my notes today regarding Fujitsu Powercobol "called"
…[3 more quoted lines elided]…
>creating custom controls that might fit the bill here, but I'll be darned
if
>I could find it today.  I'm in the process of re-writing our MicroFocus
>COBOL programs into Fujitsu Powercobol, and I have a BBS program that will
>need this feature to update the BBS database.  I may call Fujitsu support
>when I get to that point and just ask.  Right now I'm still finishing up
the
>custom DDE interface to our mainframe terminal emulation program.  At least
>for that application, we're communicating just fine and dandy.  It just
>seems weird that you can call a Powercobol subroutine from regular Fujitsu
>COBOL, but can't  call one from another Powercobol program.  If you get it
>to work, it would be great if you could post how you did it.  I'll
certainly
>do the same, if I happen upon it relatively soon.
>
>Denny
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
