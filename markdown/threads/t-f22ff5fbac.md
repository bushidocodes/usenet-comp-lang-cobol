[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL for MVS question

_4 messages · 4 participants · 1998-08_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL for MVS question

- **From:** "davidm" <ua-author-896320@usenetarchives.gap>
- **Date:** 1998-08-16T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<35D859C9.2366@cyburban.com>`

```
Can the COBOL for MVS compiler be set to include all COBOL subroutines
in the load module? I have not been able to figure out how to do this.
The NORES compiler option, which was the old way to achieve this, no
longer works.

We need this because we deliver our programs to sites that do not use
COBOL for MVS, and the COBOL for MVS compiler is the only COBOL compiler
on out P390 machine.

Please remove 's' from email address when replying.
```

#### ↳ Re: COBOL for MVS question

- **From:** "the..." <ua-author-96015@usenetarchives.gap>
- **Date:** 1998-08-17T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f22ff5fbac-p2@usenetarchives.gap>`
- **In-Reply-To:** `<35D859C9.2366@cyburban.com>`
- **References:** `<35D859C9.2366@cyburban.com>`

```
› Subject: COBOL for MVS question
› From: DavidM 
…[13 more quoted lines elided]…
› 

I'm afraid you're in for an eye opener my friend...

OS/390 was just installed at our site on the Y2K LPAR that's being used for
development. As promised, the install went smoothly and everything ran as
promised - ON THE Y2K LPAR THAT IS!

When we went to try things out in the production LPAR, EVERY SINGLE PROGRAM
FAILED with an FCC ABEND!

Someone at IBM apparently took a page from Microsoft's book of twisted logic -
under OS/390, COBOL programs compiled using the current version of LE may not
run on any other IBM mainframe that's at a lower level of maintenance!

On their web site, IBM notes that they are still looking for a possible
long-term solution to the problems created by this "strategic change" to their
approach to backwards compatibility. In the meantime, their short-term solution
is to develop using the most obsolete LE environment that your application will
ever be run on!

As if Y2K isn't difficult enough...
```

#### ↳ Re: COBOL for MVS question

- **From:** "danie..." <ua-author-6589640@usenetarchives.gap>
- **Date:** 1998-08-18T09:04:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f22ff5fbac-p3@usenetarchives.gap>`
- **In-Reply-To:** `<35D859C9.2366@cyburban.com>`
- **References:** `<35D859C9.2366@cyburban.com>`

```
In article <35D··.@cyb··n.com>,
dm··.@cyb··n.com wrote:
› Can the COBOL for MVS compiler be set to include all COBOL subroutines
› in the load module? I have not been able to figure out how to do this.
…[8 more quoted lines elided]…
› 

No Chance!

In the 'Compiler and Run-Time Migration Guide' for COBOL for OS/390 & VM
Version 2 Release 1 and COBOL for MVS & VM Version 1 Release 2, Document
Number GC26-4764-04, you can read:

NORES Environment Not Available: IBM COBOL does not provide the NORES
compiler option. All IBM COBOL programs are RES. Existing NORES
applications are not affected; they continue to run and provide the same
results.

The Runtime is LE/370. also called LE/MVS or LE/390 which is allways
delivered with OS/390 at no further cost!

Cheers

Daniel

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

#### ↳ Re: COBOL for MVS question

- **From:** "george young" <ua-author-1947495@usenetarchives.gap>
- **Date:** 1998-08-18T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-f22ff5fbac-p4@usenetarchives.gap>`
- **In-Reply-To:** `<35D859C9.2366@cyburban.com>`
- **References:** `<35D859C9.2366@cyburban.com>`

```
DavidM wrote:
› 
› Can the COBOL for MVS compiler be set to include all COBOL subroutines
…[8 more quoted lines elided]…
› Please remove 's' from email address when replying.

I believe that COBOL for MVS & VM requires at least LE/370 1.5 (also
known as Language Environment for MVS & VM) or above. To build the load
module, you need the linkedit library (SCEELKED). For either you or your
customer to run it, you/they need the runtime library (SCEERUN).

The general rule is that your runtime library must be at the same level
or higher than your linkedit library (so, if you link at 1.5, your
customer needs the 1.5 or higher runtime).

I believe LE/370 is an addon to MVS/ESA systems and comes with OS/390
systems (at least enough for COBOL, I believe until recently C++
required additional libs unless the builder made special provisions).

So, you'll need to find out what level of LE you are linking at, and
require your customer to be at that level or higher.

As an aside, I think the newer COBOL for OS/390 and VM will require
LE/370 1.8.

George
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
