[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# MicroFocus: how to compile executables using gcc without cob

_5 messages · 4 participants · 2002-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### MicroFocus: how to compile executables using gcc without cob

- **From:** ronald.goeggel@atosorigin.com (Ronald)
- **Date:** 2002-08-12T07:47:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61b71612.0208120647.26fe2e4d@posting.google.com>`

```
Hi,

I want to compile a COBOL Runtime into my C programs.

All seems to be fine but I have a problem with creating ldtab.s

This file will be generated between the two link phases of cob.

Does anyone have a work around for this problem?


Thanx

Ronald
```

#### ↳ Re: MicroFocus: how to compile executables using gcc without cob

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2002-08-13T07:09:31+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D58A29B.B11CF488@Azonic.co.nz>`
- **References:** `<61b71612.0208120647.26fe2e4d@posting.google.com>`

```
Ronald wrote:
 
> I want to compile a COBOL Runtime into my C programs.

Dunno, but I think that you would still need to pay a run-time licence
if you distributed this.
```

##### ↳ ↳ Re: MicroFocus: how to compile executables using gcc without cob

- **From:** ronald.goeggel@atosorigin.com (Ronald)
- **Date:** 2002-08-13T01:17:49-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<61b71612.0208130017.e0d63a9@posting.google.com>`
- **References:** `<61b71612.0208120647.26fe2e4d@posting.google.com> <3D58A29B.B11CF488@Azonic.co.nz>`

```
Hi Richard,

our customers still have run-time licences. And we have a devellopper
licence.

Our problem is: If a customer buys a new machine we have to have to
generate a runtime for this machine. So we have to buy such a machine
too.

We wanna try to cross compile our runtime. So the first step is to
replace cob by gcc.

We figured out, that after the first link phase, the cob command
generates an assembler file (ldtab.s) that differs on various machines
(Linux, aix, HP).

I think, it is not easy for me to generate this assembler source.

So I'm looking for help to bypass this.

Any ideas or suggestions?

Ronald

Richard Plinston <riplin@Azonic.co.nz> wrote in message news:<3D58A29B.B11CF488@Azonic.co.nz>...
> Ronald wrote:
>  
…[3 more quoted lines elided]…
> if you distributed this.
```

###### ↳ ↳ ↳ Re: MicroFocus: how to compile executables using gcc without cob

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-08-13T12:13:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8K669.2055$yt3.695858@newssrv26.news.prodigy.com>`
- **References:** `<61b71612.0208120647.26fe2e4d@posting.google.com> <3D58A29B.B11CF488@Azonic.co.nz> <61b71612.0208130017.e0d63a9@posting.google.com>`

```
"Ronald" <ronald.goeggel@atosorigin.com> wrote in message
news:61b71612.0208130017.e0d63a9@posting.google.com...
> Hi Richard,
>
> Our problem is: If a customer buys a new machine we have to have to
> generate a runtime for this machine. So we have to buy such a machine
> too.

Not to be too tacky here, but if you are in the business of developing
software marketed for use on multiple hardware products, that seems a cost
of doing business.

MCM
```

###### ↳ ↳ ↳ Re: MicroFocus: how to compile executables using gcc without cob

- **From:** Stephen Gennard <Stephen.Gennard@MicroFocus.com>
- **Date:** 2002-08-13T16:25:19+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D5924DF.9000508@MicroFocus.com>`
- **References:** `<61b71612.0208120647.26fe2e4d@posting.google.com> <3D58A29B.B11CF488@Azonic.co.nz> <61b71612.0208130017.e0d63a9@posting.google.com>`

```
First trying to create emulate what "cob" does, will be
a never ending task... trust me... I know...  don't do it!

Why do you need to link your runtime into a exe?

Why don't you create a shared library/object.... these can
either be linked into the COBOL program on the machine or
loaded dynamically from COBOL directly or indirectly (see
checker directive INITCALL).
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
