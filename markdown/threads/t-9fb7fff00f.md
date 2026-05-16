[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Capex Module Running

_3 messages · 3 participants · 2003-04_

---

### Capex Module Running

- **From:** mwhandi@hotmail.com (chiTownVet)
- **Date:** 2003-04-11T06:14:42-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5cc91e47.0304110514.1ac0a0df@posting.google.com>`

```
Hello.  I have a module that is showing it was compiled with the Capex
Optimizer back in 1988.  This module is running as part of a daily job
and the module that calls it was compiled last in 1997.  What troubles
me is that we no longer have the Capex runtime environment installed
anywhere in our sysplex.  Accordingly, Capex modules should not be
able to run.  Any ideas how this can be happening?  Thanks.
```

#### ↳ Re: Capex Module Running

- **From:** charles.godwin@ca.com (Charles Godwin)
- **Date:** 2003-04-11T10:13:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c8035ce7.0304110913.3749bf76@posting.google.com>`
- **References:** `<5cc91e47.0304110514.1ac0a0df@posting.google.com>`

```
I work for Computer Associates, the company that bought Capex many,
many years ago. I did some research for you. Here's what I learned.

Your program was probably compiled using an old Capex release, one
that was licensed by the customer before CA acquired Capex, back when
there was no run time library requirement.  Just because it was
compiled in 1988 doesn't mean the optimizer release is from 1988.

Charles Godwin
Computer Associates
Development Manager
Advantage CA-Realia II Workbench (COBOL)


mwhandi@hotmail.com (chiTownVet) wrote in message news:<5cc91e47.0304110514.1ac0a0df@posting.google.com>...
> Hello.  I have a module that is showing it was compiled with the Capex
> Optimizer back in 1988.  This module is running as part of a daily job
…[3 more quoted lines elided]…
> able to run.  Any ideas how this can be happening?  Thanks.
```

#### ↳ Re: Capex Module Running

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-04-11T18:32:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<PSDla.631$ug7.355220@newssrv26.news.prodigy.com>`
- **References:** `<5cc91e47.0304110514.1ac0a0df@posting.google.com>`

```
"chiTownVet" <mwhandi@hotmail.com> wrote in message
news:5cc91e47.0304110514.1ac0a0df@posting.google.com...
> Hello.  I have a module that is showing it was compiled with the Capex
> Optimizer back in 1988.  This module is running as part of a daily job
…[3 more quoted lines elided]…
> able to run.  Any ideas how this can be happening?  Thanks.

(from one who had never heard of Capex Optimizer before now)

Perhaps the Capex runtime is used only when a program is optimized; that is,
it is not required to execute a program which has already been
"Capex-optimized."

MCM
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
