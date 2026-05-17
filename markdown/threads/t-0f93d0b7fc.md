[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Bull Cobol vs MVS Cobol-II

_6 messages · 5 participants · 1997-08_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Bull Cobol vs MVS Cobol-II

- **From:** "sa..." <ua-author-17072001@usenetarchives.gap>
- **Date:** 1997-08-06T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<33e9893c.2630305@news.mclink.it>`

```

Could anybody tell me something about the differences between Bull
Cobol (GCOSx) and MVS Cobol-II.
I live in MVS environment, but I need to convert some (1-2 hundreds)
programs written in Bull environment.
Thanks in advance
Sergio Sardo - Migra s.r.l. - Italy
< Sergio Sardo - Migra s.r.l. - Italy >
< sa··.@mi··a.it - http://www.migra.it>
```

#### ↳ Re: Bull Cobol vs MVS Cobol-II

- **From:** "bill h." <ua-author-1252963@usenetarchives.gap>
- **Date:** 1997-08-07T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0f93d0b7fc-p2@usenetarchives.gap>`
- **In-Reply-To:** `<33e9893c.2630305@news.mclink.it>`
- **References:** `<33e9893c.2630305@news.mclink.it>`

```

Jeff Raben wrote:
› 
› sa··.@mi··a.it (SergioSardo-Migra s.r.l.-Italy) wrote:
…[17 more quoted lines elided]…
› and stir with a Runcible spoon...

I don't agree on the JCL being a large problem, if you have
access to the text editor on Bull, or something as powerfull
and flexible. You can have it read existing JCL modules and
using the editor execute your own editor script to produce
new JCL. In this case freeform JCL to fixed JCL.
Having converted MVS to Bull GCOS (direction doesn't matter)
your major changes are in the SELECT no big deal. There may
have been some differences also in SEARCH and VARYING .....
AFTER. It was some years ago and those little differences may
not exist anymore. But, as J.R. says, databases will be a
problem. If your programs are just batch apps, that's easier
than apps requiring the screen, that can be a nightmare.
Had a headhunter offer me contract converting Bull GCOS TPS
to MVS CICS just a week ago. (Shudder, may as well re-write
the programs). Bottom line is, it depends what the apps are
doing on the Bull and what you want to convert them to in IBM.
(or vise versa).
Bill H.
```

##### ↳ ↳ Re: Bull Cobol vs MVS Cobol-II

- **From:** "e..." <ua-author-4987403@usenetarchives.gap>
- **Date:** 1997-08-15T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0f93d0b7fc-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0f93d0b7fc-p2@usenetarchives.gap>`
- **References:** `<33e9893c.2630305@news.mclink.it> <gap-0f93d0b7fc-p2@usenetarchives.gap>`

```

I can't say about the GCOS COBOL -- I used the CP-6 Cobol, and it
was quite similar to the older IBM COBOLs, except for which
CP-6 COMP-n was which IBM COMP-m, and the file stuff. One
actually declared files in the CP-6 COBOL source, rather than
declaring a reference to a JCL DD spec with some type info.

All the best.
```

###### ↳ ↳ ↳ Re: Bull Cobol vs MVS Cobol-II

- **From:** "rayg..." <ua-author-1603681@usenetarchives.gap>
- **Date:** 1997-08-16T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0f93d0b7fc-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0f93d0b7fc-p3@usenetarchives.gap>`
- **References:** `<33e9893c.2630305@news.mclink.it> <gap-0f93d0b7fc-p2@usenetarchives.gap> <gap-0f93d0b7fc-p3@usenetarchives.gap>`

```

Concerning Honeywell GCOS COBOL vs. IBM COBOL:

At my shop, we recently converted from Honeywell to IBM, after many
years running both systems. Some important things:

In Honeywell COBOL, a divide by zero will not result in an abend
(IIRC), whereas in IBM, it will.

In Honeywell COBOL, an index can be set to 0 without objection (unless
you try to access a table with it); not possible in IBM.

Also, there are truncation differences in long COMPUTE statements;
these must be *thoroughly* tested.


Raymond F. Greenberg
```

###### ↳ ↳ ↳ Re: Bull Cobol vs MVS Cobol-II

_(reply depth: 4)_

- **From:** "rayg..." <ua-author-1603681@usenetarchives.gap>
- **Date:** 1997-08-16T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0f93d0b7fc-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-0f93d0b7fc-p4@usenetarchives.gap>`
- **References:** `<33e9893c.2630305@news.mclink.it> <gap-0f93d0b7fc-p2@usenetarchives.gap> <gap-0f93d0b7fc-p3@usenetarchives.gap> <gap-0f93d0b7fc-p4@usenetarchives.gap>`

```

On Sun, 17 Aug 1997 17:26:19 GMT, ray··.@po··d.com (Raymond F.
Greenberg) wrote:

› Concerning Honeywell GCOS COBOL vs. IBM COBOL:
 
› At my shop, we recently converted from Honeywell to IBM, after many
› years running both systems.  Some important things:
 
› In Honeywell COBOL, a divide by zero will not result in an abend
› (IIRC), whereas in IBM, it will.
 
› In Honeywell COBOL, an index can be set to 0 without objection (unless
› you try to access a table with it); not possible in IBM.
 
› Also, there are truncation differences in long COMPUTE statements;
› these must be *thoroughly* tested. 

Sorry--forgot to add another difference:

Sort sequences of character sets are different, depending on the
character set used (GBCD/HBCD or ASCII vs. EBCDIC). For example, in
IBM EBCDIC, numbers are last in the sequence, whereas in ASCII, they
are first. This could cause differences in processing if logical
compares of items are done.




Raymond F. Greenberg
```

#### ↳ Re: Bull Cobol vs MVS Cobol-II

- **From:** "jrab..." <ua-author-1103061@usenetarchives.gap>
- **Date:** 1997-08-10T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-0f93d0b7fc-p6@usenetarchives.gap>`
- **In-Reply-To:** `<33e9893c.2630305@news.mclink.it>`
- **References:** `<33e9893c.2630305@news.mclink.it>`

```

sa··.@mi··a.it (SergioSardo-Migra s.r.l.-Italy) wrote:

› Could anybody tell me something about the differences between Bull
› Cobol (GCOSx) and MVS Cobol-II.

JCL is a problem as GCOS does not enque and test file existance
during job processing (and reader processing) as IBM does.
Because of that the possible imbedded utilities and file existance (or
non-existance) rules are different.

However, generally, step-by-execution step is real easy.

JR


and stir with a Runcible spoon...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
