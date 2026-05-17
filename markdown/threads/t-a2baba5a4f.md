[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Preserving working-storage

_7 messages · 6 participants · 1997-09_

---

### Preserving working-storage

- **From:** "allan pilecki" <ua-author-17073480@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34187C70.5A6322B1@ottawa.com>`

```

I am working at a shop that is currently converting to COBOL II. We
have a job that is proving itself to be somewhat of a bother. It
consists of a clist ... which invokes an EASYTRIEVE program ... which
repeatedly calls a COBOL program ... which in turn calls a database I/O
module driver to access an IDMS 12.01 database.

The job worked fine when the called program was compiled with OS/VS
COBOL and there were no I/O modules (i.e. the called COBOL program
contained the native DML for the database).

However, after compiling with COBOL II, things have changed. The problem
is between the EASYTRIEVE and COBOL. The COBOL working-storage is not
preserved between calls.

We suspect a compile parm will provide the solution. Suggestions?
```

#### ↳ Re: Preserving working-storage

- **From:** "kev" <ua-author-6592768@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2baba5a4f-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34187C70.5A6322B1@ottawa.com>`
- **References:** `<34187C70.5A6322B1@ottawa.com>`

```

On Thu, 11 Sep 1997 19:19:13 -0400, Allan Pilecki
wrote:

› I am working at a shop that is currently converting to COBOL II.  We
› have a job that is proving itself to be somewhat of a bother.  It
…[13 more quoted lines elided]…
› 
I suspect you are now calling it dynamically. In the past, if called
statically, you would have the same version. With Cob II you get a
new version each time it's called dynamically. Solution: call the
program statically. Another option is to pass the "needed
information" in linkage between calls.


Cheers,

Kevin........."Due to SPAM, remove KEV and replace
with KKLT1 when replying by email"
```

##### ↳ ↳ Re: Preserving working-storage

- **From:** "lynchwb" <ua-author-6592517@usenetarchives.gap>
- **Date:** 1997-09-10T20:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2baba5a4f-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-a2baba5a4f-p2@usenetarchives.gap>`
- **References:** `<34187C70.5A6322B1@ottawa.com> <gap-a2baba5a4f-p2@usenetarchives.gap>`

```

Kevin wrote:
› 
› On Thu, 11 Sep 1997 19:19:13 -0400, Allan Pilecki 
…[28 more quoted lines elided]…
›                    with KKLT1 when replying by email"

Another possibility is if the Cobol II program is compiled & linked with
the RENT option - this causes the program to obtain Working-Storage
(with a GETMAIN) every time the program is invoked. If this is the case,
just compile without the RENT option and you should be okay.

Hope this helps,
Bill Lynch
```

#### ↳ Re: Preserving working-storage

- **From:** "a&b dossett" <ua-author-17071730@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2baba5a4f-p4@usenetarchives.gap>`
- **In-Reply-To:** `<34187C70.5A6322B1@ottawa.com>`
- **References:** `<34187C70.5A6322B1@ottawa.com>`

```

The VS/COBOL program may have been compiled with NOENDJOB. Sorry, I don't
know what the COBOL ii equivalent is.

Andy
```

#### ↳ Re: Preserving working-storage

- **From:** "john l. mindock" <ua-author-6588931@usenetarchives.gap>
- **Date:** 1997-09-11T20:00:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2baba5a4f-p5@usenetarchives.gap>`
- **In-Reply-To:** `<34187C70.5A6322B1@ottawa.com>`
- **References:** `<34187C70.5A6322B1@ottawa.com>`

```


Allan Pilecki wrote:
›
Check out NORENT as a compile option. This has inter-relationships with
DYNAM/NODYNAM and RESIDENT/NORESIDENT options, so you can either try to
figure out what it says in the manual (hope you are a PHD in English),
or you can just try some combinations and get done a lot sooner. :)

There may also be a need to change the EASYTRIEVE call or installation
parms, but I doubt it. The deal is that all of these programs may have
to behave the same with respect to reentrancy, dynamic, resident, etc.

John




› I am working at a shop that is currently converting to COBOL II.  We
› have a job that is proving itself to be somewhat of a bother.  It
…[12 more quoted lines elided]…
› We suspect a compile parm will provide the solution.  Suggestions?
```

#### ↳ Re: Preserving working-storage

- **From:** "lars bjerges" <ua-author-6588782@usenetarchives.gap>
- **Date:** 1997-09-12T20:00:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2baba5a4f-p6@usenetarchives.gap>`
- **In-Reply-To:** `<34187C70.5A6322B1@ottawa.com>`
- **References:** `<34187C70.5A6322B1@ottawa.com>`

```

Try using run-time option LIBKEEP.
You probably will have to assemble it into IGZEOPT and
subsequently "force" it into your COBOL load by means of
INCLUDE-ing it in ProgramBinder-SYSIN.

Normally when calling COBOL from non-COBOL the first executed
COBOL program is considered to be "main" and therefore is "in
charge" of establishing the COBOL run-time environment.
As control is passed back to the caller the run-time environment
is terminated (since this was the COBOL main).

If you are code your own (non-COBOL) driver (e.g. assembler)
you can "trick" COBOL by disguising yourself as COBOL main.
The tick here is to LOAD and CALL IGZERRE with proper function
codes to establish (at the beginning) and terminate (at end) the
COBOL environment.

However, when COBOL is called from e.g. Easytrive (or invoked
as a SORT-exit) you will have to use (for example) LIBKEEP.

A last question; Why COBOL II, do you know that it will only
have service till year 2001?

Lars

Allan Pilecki skrev i inlï¿½gg
<341··.@ott··a.com>...
› I am working at a shop that is currently converting to COBOL II.  We
› have a job that is proving itself to be somewhat of a bother.  It
…[14 more quoted lines elided]…
›
```

#### ↳ Re: Preserving working-storage

- **From:** "a&b dossett" <ua-author-17071730@usenetarchives.gap>
- **Date:** 1997-09-14T20:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-a2baba5a4f-p7@usenetarchives.gap>`
- **In-Reply-To:** `<34187C70.5A6322B1@ottawa.com>`
- **References:** `<34187C70.5A6322B1@ottawa.com>`

```

I've just remembered why I can't remember what the COBOL II equivalent of
NOENDJOB is... there isn't one.

When a COBOL program is entered, a COBOL run-time environment is set up.
This environment can then be used by that program and any other COBOL
programs beneath it. When the (first) program ends, so does the run-time
environment. If you compiled the (VS/COBOL) program with NOENDJOB the
run-time environment remains available for when the program is called
again.

What you are experiencing, I believe, is the run-time environment being
deleted as you exit your COBOL II program. When you call it subsequent
times, the run-time environment is re-established and the program started
in its initial state.

The way round this is to expand the scope of the run-time environment. Do
this by simply coding a call to ILBOSTP0 at the start of your CLIST. The
run-time environment is established by this call and remains in effect
until your CLIST terminates. Note that your COBOL program must be
terminated by a GOBACK, not STOP RUN.

See VS COBOL II Application Programming Guide (SC26-4045-05), Section
3.9.5.2.

Andy

Allan Pilecki wrote in article
<341··.@ott··a.com>...
› I am working at a shop that is currently converting to COBOL II.  We
› have a job that is proving itself to be somewhat of a bother.  It
…[14 more quoted lines elided]…
›
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
