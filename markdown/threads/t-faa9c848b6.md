[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Microfocus - please help

_5 messages · 4 participants · 1998-07_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Help requests and how-to`](../topics.md#help)

---

### Microfocus - please help

- **From:** "scot..." <ua-author-6992932@usenetarchives.gap>
- **Date:** 1998-07-22T08:44:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6p4mr1$bod$1@nnrp1.dejanews.com>`

```
I'm having a small problem with Micro Focus Cobol. For some reason, I am
unable to open an organizer window from the Advanced Workbench. I cannot
determine why it is no longer work, the only thing I can see if that I get a
'The Call Failed!' when I try to open the organizer for a job that I have been
working on the previous day. This happened once before and the only way to
solve it was to reload my entire operating system (WinNT).

Has anyone else had this happen and were you able to correct it?


Thanks,
Scott

-----== Posted via Deja News, The Leader in Internet Discussion ==-----
http://www.dejanews.com/rg_mkgrp.xp Create Your Own Free Member Forum
```

#### ↳ Re: Microfocus - please help

- **From:** "as-..." <ua-author-17074031@usenetarchives.gap>
- **Date:** 1998-07-21T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-faa9c848b6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6p4mr1$bod$1@nnrp1.dejanews.com>`
- **References:** `<6p4mr1$bod$1@nnrp1.dejanews.com>`

```
sco··.@bel··h.net schrieb:

› I'm having a small problem with Micro Focus Cobol.  For some reason, I
› am
…[18 more quoted lines elided]…
› Forum

I think, it is a problem since 1988 from MF, so they don't close all
theire open files.

Try to increase the open files in your os, and the failure will come
later, but it will...

No chance up to now.

Greatings
AS
```

##### ↳ ↳ Re: Microfocus - please help

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-07-22T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-faa9c848b6-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-faa9c848b6-p2@usenetarchives.gap>`
- **References:** `<6p4mr1$bod$1@nnrp1.dejanews.com> <gap-faa9c848b6-p2@usenetarchives.gap>`

```
In article <6p5o36$eoo$2.··.@new··g.de>, AS-.··@t-o··e.de says...
› 
› sco··.@bel··h.net schrieb:
…[6 more quoted lines elided]…
› theire open files.

Nope. Advanced Organizer first saw light of day in 1996. Adv. Organiser is OO.
The persistant data in the databse has probably become corrupt because of a
power outage during use or some other crash.

As to not closing open files, the only one I know of that used to cause
problems was a DLL which was left running. Not important but annoying. It
couldn't corrupt data files. If the runtime is not running, all files will be
closed.

› Try to increase the open files in your os, and the failure will come
› later, but it will...

Not a problem with the 32bit product as it's Windows/OS2 based. FILES= has no
importance.

Shaun
```

###### ↳ ↳ ↳ Re: Microfocus - please help

- **From:** "s..." <ua-author-3115375@usenetarchives.gap>
- **Date:** 1998-07-22T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-faa9c848b6-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-faa9c848b6-p3@usenetarchives.gap>`
- **References:** `<6p4mr1$bod$1@nnrp1.dejanews.com> <gap-faa9c848b6-p2@usenetarchives.gap> <gap-faa9c848b6-p3@usenetarchives.gap>`

```
In article ,
red··.@i··.net says...
› While I'm in a OO bashing mood... I get ALL THIS AMMUNITION!
›
› So, what's the recovery from "Corrputed persistant data due to OO
› design and a power outage or some other crash"?

It's not really an OO design problem. The files in this case used to store
persistant data are index sequential, or at least they were at one point if I
recall correctly. The solution is therefore like any other. In this case I
don't believe MF supply the file format so if REBUILD doesn't work or MF don't
supply a tool to reconstruct the organizer database, it's a problem. I used to
regularly trash a project database file working directly with the data whilst I
was adding in the compiler options tool (COMPOPT). Usually I just deleted the
project and started again. I wasn't a big fan of Organizer so rarely used it.
Still aren't. Animator2 and the OS associations/directory structure was enough
for me. I didn't see the point in essentially duplicating Windows Program
manager/Explorer.

I used to work at MF in the Workbench team, if you hadn't gathered by now,
though thankfully haven't been there for the last two years.

Advanced Organizer was pretty much beta when I was working on it and I don't
think there was any rollback/roll forward recovery of persistant data or
transaction logging at that time. It may of changed.

Shaun
```

###### ↳ ↳ ↳ Re: Microfocus - please help

- **From:** "m..." <ua-author-1148957@usenetarchives.gap>
- **Date:** 1998-07-23T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-faa9c848b6-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-faa9c848b6-p3@usenetarchives.gap>`
- **References:** `<6p4mr1$bod$1@nnrp1.dejanews.com> <gap-faa9c848b6-p2@usenetarchives.gap> <gap-faa9c848b6-p3@usenetarchives.gap>`

```
The original poster didn't say what version of Workbench was being
used. Please pass that information plus the project and system
definiion files on to your support representative to look into your
problem.

Although it's always fun (and easy!) to bash OO, it's not really
relevant here as Advanced Organizer, and later versions of Organizer
V1, do NOT use OO. Both are procedural COBOL. The databases used are
regular ISAM files, these can be corrupted due to power outages and
the like, although can often be recovered using Rebuild.


red··.@i··.net (Thane Hubbell) wrote:

› On Thu, 23 Jul 1998 14:37:05, s.··.@ent··e.net (Shaun C. Murray) 
› wrote:
…[20 more quoted lines elided]…
› 

Regards,
Mark Warren
Micro Focus
Micro Focus Ltd., The Lawn, Old Bath Rd., Newbury, Berks. UK RG14 1QN
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
