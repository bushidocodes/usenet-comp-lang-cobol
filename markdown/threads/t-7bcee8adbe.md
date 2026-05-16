[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Cobol/DB2 Question

_6 messages · 4 participants · 2005-06_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Cobol/DB2 Question

- **From:** Houman Ghahremanlou <houmi1@gmail.com>
- **Date:** 2005-06-10T10:48:18-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11ajd9gb4q6pj4f@corp.supernews.com>`

```
Hi Everyone,

I had a question:

If a COBOL/DB2 program calls a COBOL/DB2 module, once the module changes 
do we need to recompile/rebind the calling program?

Thanks,
Houman
```

#### ↳ Re: Cobol/DB2 Question

- **From:** Frederico Fonseca <real-email-in-msg-spam@email.com>
- **Date:** 2005-06-10T18:32:09+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vgjja1do2veaoa3ss8oji6j5jhblgbdeq2@4ax.com>`
- **References:** `<11ajd9gb4q6pj4f@corp.supernews.com>`

```
On Fri, 10 Jun 2005 10:48:18 -0500, Houman Ghahremanlou
<houmi1@gmail.com> wrote:

>Hi Everyone,
>
…[3 more quoted lines elided]…
>do we need to recompile/rebind the calling program?
What OS and what COBOL version.

Depending on the above, and on whether you are using dynamic calls
(late binding) or static calls (early binding) you will or not need to
recompile it.

You MUST recompile it if the parameters used to call the module have
changed.



Frederico Fonseca
ema il: frederico_fonseca at syssoft-int.com
```

##### ↳ ↳ Re: Cobol/DB2 Question

- **From:** Houman Ghahremanlou <houmi1@gmail.com>
- **Date:** 2005-06-11T20:06:35-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11an2grlr2iu043@corp.supernews.com>`
- **In-Reply-To:** `<vgjja1do2veaoa3ss8oji6j5jhblgbdeq2@4ax.com>`
- **References:** `<11ajd9gb4q6pj4f@corp.supernews.com> <vgjja1do2veaoa3ss8oji6j5jhblgbdeq2@4ax.com>`

```
Frederico,

Thank you, This is a dynamic call. So I basically don't need
to recompile it, how about rebinding it ?

Thanks,
Houman

Frederico Fonseca wrote:
> On Fri, 10 Jun 2005 10:48:18 -0500, Houman Ghahremanlou
> <houmi1@gmail.com> wrote:
…[21 more quoted lines elided]…
> ema il: frederico_fonseca at syssoft-int.com
```

#### ↳ Re: Cobol/DB2 Question

- **From:** docdwarf@panix.com
- **Date:** 2005-06-10T14:32:11-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8cmbb$qaq$1@panix5.panix.com>`
- **References:** `<11ajd9gb4q6pj4f@corp.supernews.com>`

```
In article <11ajd9gb4q6pj4f@corp.supernews.com>,
Houman Ghahremanlou  <houmi1@gmail.com> wrote:
>Hi Everyone,
>
…[3 more quoted lines elided]…
>do we need to recompile/rebind the calling program?

That depends on what has been changed and how it is linked.

DD
```

#### ↳ Re: Cobol/DB2 Question

- **From:** bo774@FreeNet.Carleton.CA (Kelly Bert Manning)
- **Date:** 2005-06-12T17:02:25+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<d8hpr1$6a3$1@theodyn.ncf.ca>`
- **References:** `<11ajd9gb4q6pj4f@corp.supernews.com>`

```

Houman Ghahremanlou (houmi1@gmail.com) writes:
> Hi Everyone,
> 
…[6 more quoted lines elided]…
> Houman

What OS? Which Rebind?

On OS/390 and z/OS Rebind is ambiguous in a DB2 context, since BIND can
be either a DB2 Command, or something involving the System Binder used
to create load modules. I tend to use the term "linking" for load modules.
I see someone already commented on static versus dynamic relink needs.

For IBM DB2 on MVS, OS/390 and z/OS I told developers to bind DBRMs as
Packages in Collections, never directly with a DB2 Plan, even for main
programs. This worked regardless of whether the called module was a separate
load module or linked with the calling program for static reference.

DB2 Collections allow you to have more than 1 version of the same DBRM in
the DB2 catalog at a time. This simplifies module migration and backout.
```

##### ↳ ↳ Re: Cobol/DB2 Question

- **From:** Houman Ghahremanlou <houmi1@gmail.com>
- **Date:** 2005-06-13T15:49:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<11ars2kmjritea9@corp.supernews.com>`
- **In-Reply-To:** `<d8hpr1$6a3$1@theodyn.ncf.ca>`
- **References:** `<11ajd9gb4q6pj4f@corp.supernews.com> <d8hpr1$6a3$1@theodyn.ncf.ca>`

```
Thank you, the OS is 390... So if I understand it correctly:

So... If I recompile/rebind a cobol/db2 program which calls another
cobol/db2 program dynamically, does the called program get recompiled ?

Thanks,
Houman

Kelly Bert Manning wrote:
> Houman Ghahremanlou (houmi1@gmail.com) writes:
> 
…[25 more quoted lines elided]…
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
