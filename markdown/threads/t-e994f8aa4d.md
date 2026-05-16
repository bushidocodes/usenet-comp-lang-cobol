[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Which language pays most -- C++ vs. Java?

_4 messages · 4 participants · 1999-07_

---

### Re: Which language pays most -- C++ vs. Java?

- **From:** bill@cafe.net (Kaz Kylheku)
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.java.misc,comp.lang.c,comp.lang.c++,comp.lang.fortran,comp.lang.cobol,comp.lang.smalltalk,comp.lang.ada
- **Message-ID:** `<6atbro$jnd$1@brie.direct.ca>`
- **References:** `<6at330$7uj$1@mainsrv.main.nc.us> <34D22794.1DEE0535@platinum.brooks.af.mil>`

```
In article <34D22794.1DEE0535@platinum.brooks.af.mil>,
Charles W. Hall <charles.hall@platinum.brooks.af.mil> wrote:
>Having worked with assembly code, operating systems internals, and done
>high level programming, I don't think it is relevant for programmers to
>know these sort of things anymore.  There is no reason to program in
>assembler directly anymore except for highly specialized cases.   The

Just because you don't use something doesn't mean that you derive no benefit
from knowing it.

>internals of generated code have nothing to do with designing a
>correctly running program in FORTRAN, COBOL, C, or anyother high level
>language.  The operating system software is designed by experts to
>properly handle the compiled code and to perform tasks as paging,
>swapping, and scheduling.  These are not the domain of the programmer.

Not knowing how the paging works could lead the programmer to make
poor choices for accessing some large structure.

Scheduling is often the domain of the programmer; if you are working
with threads, it is useful to know what priority inversion is and
what strategies can be used to alleviate it.

>Criticizing a programmer for not knowing the internals of the operating
>system is like criticizing an automobile owner for not understanding the
>internals of the car's motor.  It is not necessary for successful
>operation of the car or computer system.

That is a poor analogy, because the operator of the car is a mere user.  He or
she is not constructing components to be added to the car.

If someone were adding an air-conditioning system to the car, I might
well expect them to be familiar with the electrical system.
```

#### ↳ Re: Which language pays most -- C++ vs. Java?

- **From:** "Edwin Purvee" <epurvee@mail.snu.edu>
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.java.misc,comp.lang.c,comp.lang.c++,comp.lang.fortran,comp.lang.cobol,comp.lang.smalltalk,comp.lang.ada
- **Message-ID:** `<7nqoqm$j0b$1@ins22.netins.net>`
- **References:** `<6at330$7uj$1@mainsrv.main.nc.us> <34D22794.1DEE0535@platinum.brooks.af.mil> <6atbro$jnd$1@brie.direct.ca>`

```

Kaz Kylheku wrote in message <6atbro$jnd$1@brie.direct.ca>...
>In article <34D22794.1DEE0535@platinum.brooks.af.mil>,
>Charles W. Hall <charles.hall@platinum.brooks.af.mil> wrote:
…[5 more quoted lines elided]…
>Just because you don't use something doesn't mean that you derive no
benefit
>from knowing it.
>

There is still great use for assembler in the video game industry.  For high
intensive graphics it is sometimes necessary to optimize functions that are
creating bottlenecks to make sure that the graphics are rendured fast
enough.

Ed
epurvee@mail.snu.edu
```

##### ↳ ↳ Re: Which language pays most -- C++ vs. Java?

- **From:** kaz@ashi.FootPrints.net (Kaz Kylheku)
- **Date:** 1999-07-30T00:00:00
- **Newsgroups:** comp.lang.java.misc,comp.lang.c,comp.lang.c++,comp.lang.fortran,comp.lang.cobol,comp.lang.smalltalk,comp.lang.ada
- **Message-ID:** `<slrn7q1sc2.9bu.kaz@ashi.FootPrints.net>`
- **References:** `<6at330$7uj$1@mainsrv.main.nc.us> <34D22794.1DEE0535@platinum.brooks.af.mil> <6atbro$jnd$1@brie.direct.ca> <7nqoqm$j0b$1@ins22.netins.net>`

```
On Thu, 29 Jul 1999 18:41:23 -0500, Edwin Purvee <epurvee@mail.snu.edu> wrote:
>
>>Just because you don't use something doesn't mean that you derive no
…[7 more quoted lines elided]…
>enough.

Please don't reply to this thread. It is year old articles that have been
reposted by someone's broken MS Exchange server.
```

###### ↳ ↳ ↳ Re: Which language pays most -- C++ vs. Java?

- **From:** usurper@euronet.nl (Paul Mesken)
- **Date:** 1999-07-30T00:00:00
- **Newsgroups:** comp.lang.java.misc,comp.lang.c,comp.lang.c++,comp.lang.fortran,comp.lang.cobol,comp.lang.smalltalk,comp.lang.ada
- **Message-ID:** `<37a4623e.3275746@news.euronet.nl>`
- **References:** `<6at330$7uj$1@mainsrv.main.nc.us> <34D22794.1DEE0535@platinum.brooks.af.mil> <6atbro$jnd$1@brie.direct.ca> <7nqoqm$j0b$1@ins22.netins.net> <slrn7q1sc2.9bu.kaz@ashi.FootPrints.net>`

```
On Fri, 30 Jul 1999 00:27:45 GMT, kaz@ashi.FootPrints.net (Kaz
Kylheku) wrote:

>On Thu, 29 Jul 1999 18:41:23 -0500, Edwin Purvee <epurvee@mail.snu.edu> wrote:
>>
…[11 more quoted lines elided]…
>reposted by someone's broken MS Exchange server.

Yeah, but it's still true. There's still a great use for Assembly :-)
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
