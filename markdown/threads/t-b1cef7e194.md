[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Wanted - Dynamic Allocation Routine for MVS ??

_10 messages · 5 participants · 2000-08_

**Topics:** [`Jobs, careers, recruiting, salary`](../topics.md#jobs) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe) · [`Help requests and how-to`](../topics.md#help)

---

### Wanted - Dynamic Allocation Routine for MVS ??

- **From:** Bill <wfsent@bellatlantic.net>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39953B05.A54F57DE@bellatlantic.net>`

```
Hi All,
    sorry if this message is a little off topic, but does anyone have a
dynamic allocation routine, that is cabable of allocating members of a
PDS. The routine must be callable from COBOL (MVS)

TIA

Bill
```

#### ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000812110839.18738.00000428@ng-cv1.aol.com>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net>`

```
Bill Sent writes...

>Hi All,
>    sorry if this message is a little off topic, but does anyone have a
>dynamic allocation routine, that is cabable of allocating members of a
>PDS. The routine must be callable from COBOL (MVS)

You can call a TSO service routine from a COBOL program to issue almost any TSO
command, including ALLOCATE.

We cover how to do that sort of thing in our course Advanced TSO REXX Workshop.
Unfortunately, I'm on the road right now and don't have access to my course
book to look it up. But you can probably figure it out if you go to the TSO
Services Programming Guide.

Regards,



Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

##### ↳ ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

- **From:** Bill <wfsent@bellatlantic.net>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3995C9A1.563BD28C@bellatlantic.net>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net> <20000812110839.18738.00000428@ng-cv1.aol.com>`

```
Hi Steve,
    sorry, I forgot to mention that I need to invoke it from a COBOL Stored
Procedure. So the SP address space doesn't have access to the TSO libs. The
sysprogs wont add it to the steplib

Bill

S Comstock wrote:

> Bill Sent writes...
>
…[21 more quoted lines elided]…
> USA
```

##### ↳ ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n47uf$7n4qe$1@ID-39920.news.cis.dfn.de>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net> <20000812110839.18738.00000428@ng-cv1.aol.com>`

```

S Comstock <scomstock@aol.com> wrote in message
news:20000812110839.18738.00000428@ng-cv1.aol.com...
> Bill Sent writes...
>
…[5 more quoted lines elided]…
> You can call a TSO service routine from a COBOL program to issue almost
any TSO
> command, including ALLOCATE.
>
> We cover how to do that sort of thing in our course Advanced TSO REXX
Workshop.
> Unfortunately, I'm on the road right now and don't have access to my
course
> book to look it up. But you can probably figure it out if you go to the
TSO
> Services Programming Guide.
>

You can also do this in Assembler using SVC 99.  It is actually fairly easy
to use, but there isn't a lot of good documentation on it.
```

###### ↳ ↳ ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

- **From:** Bill <wfsent@bellatlantic.net>
- **Date:** 2000-08-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3995C9E6.5FF79B08@bellatlantic.net>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net> <20000812110839.18738.00000428@ng-cv1.aol.com> <8n47uf$7n4qe$1@ID-39920.news.cis.dfn.de>`

```
Hi DBuck,
    I'm don't write MVS assembler, so I was hoping to get a working routine
from some kind sole...

Bill

DBuck wrote:

> S Comstock <scomstock@aol.com> wrote in message
> news:20000812110839.18738.00000428@ng-cv1.aol.com...
…[21 more quoted lines elided]…
> to use, but there isn't a lot of good documentation on it.
```

###### ↳ ↳ ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

_(reply depth: 4)_

- **From:** "DBuck" <dbuck@prairieinet.net>
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n6a6n$7org7$1@ID-39920.news.cis.dfn.de>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net> <20000812110839.18738.00000428@ng-cv1.aol.com> <8n47uf$7n4qe$1@ID-39920.news.cis.dfn.de> <3995C9E6.5FF79B08@bellatlantic.net>`

```
I will try to remember to post the code tomorrow (it's at work, of
course)...


Bill <wfsent@bellatlantic.net> wrote in message
news:3995C9E6.5FF79B08@bellatlantic.net...
> Hi DBuck,
>     I'm don't write MVS assembler, so I was hoping to get a working
routine
> from some kind sole...
>
…[9 more quoted lines elided]…
> > > >    sorry if this message is a little off topic, but does anyone have
a
> > > >dynamic allocation routine, that is cabable of allocating members of
a
> > > >PDS. The routine must be callable from COBOL (MVS)
> > >
> > > You can call a TSO service routine from a COBOL program to issue
almost
> > any TSO
> > > command, including ALLOCATE.
…[5 more quoted lines elided]…
> > > book to look it up. But you can probably figure it out if you go to
the
> > TSO
> > > Services Programming Guide.
> > >
> >
> > You can also do this in Assembler using SVC 99.  It is actually fairly
easy
> > to use, but there isn't a lot of good documentation on it.
>
```

###### ↳ ↳ ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

_(reply depth: 5)_

- **From:** Bill <wfsent@bellatlantic.net>
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3996EE45.3875DFCB@bellatlantic.net>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net> <20000812110839.18738.00000428@ng-cv1.aol.com> <8n47uf$7n4qe$1@ID-39920.news.cis.dfn.de> <3995C9E6.5FF79B08@bellatlantic.net> <8n6a6n$7org7$1@ID-39920.news.cis.dfn.de>`

```
Thanks

Bill



DBuck wrote:

> I will try to remember to post the code tomorrow (it's at work, of
> course)...
…[41 more quoted lines elided]…
> >
```

#### ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

- **From:** tscoffey@my-deja.com
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8n53l1$ctk$1@nnrp1.deja.com>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net>`

```
I wrote an entire interface to all of the dynamic allocation
functions in COBOL 5 years ago. it works great. You can do ANYTHING
SVC 99 can do - but from COBOL using COBOL copybooks instead of that
dreaded assembler SVC 99 interface code.

E-mail me at Timothy_S_Coffey@mail.bankone.com and I will send
you a copy of the code.


In article <39953B05.A54F57DE@bellatlantic.net>,
  Bill <wfsent@bellatlantic.net> wrote:
> Hi All,
>     sorry if this message is a little off topic, but does anyone have
a
> dynamic allocation routine, that is cabable of allocating members of a
> PDS. The routine must be callable from COBOL (MVS)
…[5 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

#### ↳ Wanted - Dynamic Allocation Routine for MVS ??

- **From:** "Lucas, Todd" <Todd.Lucas@C-Cubed.net>
- **Date:** 2000-08-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8IKl5.14025$H14.30343@newsfeed.slurp.net>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net>`

```
Check out this link at MVSHELP.COM bulletin board - I think it will do
exactly what you want.  It contains an assembler program to do the
SVC99, as well as Cobol call copybook.  Hope it helps ...

http://mvshelp.com/ubb/Forum1/HTML/000304.html

Todd Lucas
E-Mail:  Todd.Lucas@C-Cubed.net
Web:   http://www.c-cubed.net

Bill <wfsent@bellatlantic.net> wrote in message
news:39953B05.A54F57DE@bellatlantic.net...
> Hi All,
>     sorry if this message is a little off topic, but does anyone have
a
> dynamic allocation routine, that is cabable of allocating members of a
> PDS. The routine must be callable from COBOL (MVS)
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Wanted - Dynamic Allocation Routine for MVS ??

- **From:** Bill <wfsent@bellatlantic.net>
- **Date:** 2000-08-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3999BFAE.ECBE37C1@bellatlantic.net>`
- **References:** `<39953B05.A54F57DE@bellatlantic.net> <8IKl5.14025$H14.30343@newsfeed.slurp.net>`

```
Thanks Todd.

Bill

"Lucas, Todd" wrote:

> Check out this link at MVSHELP.COM bulletin board - I think it will do
> exactly what you want.  It contains an assembler program to do the
…[19 more quoted lines elided]…
> >
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
