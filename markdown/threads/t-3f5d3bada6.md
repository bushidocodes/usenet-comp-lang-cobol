[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migration to LE (Language Environment)

_3 messages · 3 participants · 1998-02_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Migration to LE (Language Environment)

- **From:** "jim van sickle" <ua-author-6589079@usenetarchives.gap>
- **Date:** 1998-02-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<34DF684D.5B24C211@ibm.net>`

```

Greetings...
Our service provider is planning on upgrading from MVS/ESA SP5.2.0 to OS/390
2.4. We are a COBOL/COBOL II shop running batch JES2 and CICS/ESA 4.1, as well
as IDMS 12.01. I need to get a feel for what's involved in getting our
applications to run under OS/390 (and LE). I have some specific questions:

1. Do we have to use LE or can we still (selectively) run with COBOL(II)
run-time (supported or un-supported) once we go to OS/390?

2. If we cannot use COBOL(II) run-time under OS/390, can we start using LE in
addition to COBOL(II) run-time with MVS/ESA 5.2? Would this be a better
migration path?

3. Do we need to re-link our load modules compiled and linked as COBOL(II)
modules to use LE? Do we need to re-compile?

4. Do assembler subprograms and/or main programs need to be re-assembled and/or
relinked to run under LE? (The migration guide suggests that LE macros need to
be used)

5. If we can selectively run programs with COBOL(II) run-time, how 'bout under
CICS? Can we run LE and non-LE programs in the same region?

6. The IBM guides are (believe it or not) not much help! Anywhere else to look?

Signed: Nervous in NJ
***********************************************
*   Jim Van Sickle     *
*    Manager, Operations and Tech Support     *
*             United Retail, Inc.             *
*---------------------------------------------*
*         visit my meager web site at:        *
*       *
***********************************************
```

#### ↳ Re: Migration to LE (Language Environment)

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-02-09T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f5d3bada6-p2@usenetarchives.gap>`
- **In-Reply-To:** `<34DF684D.5B24C211@ibm.net>`
- **References:** `<34DF684D.5B24C211@ibm.net>`

```

For a cpi[;e pf days I have kept marking this note as "undread" and hoped
that someone else would answer it. But has no one else has, let me put out
a couple of ideas:

1) Your questions are pretty deailed and take more than a NG reply (I
think). What's more, there are some questions that you haven't even come up
with yet.

2) The best place to start is the IBM published "Migration Guides" - one for
COBOL and one for the latest LE. I suggest that you get these in
hard-copy - because of where you are in your migration.

3) To look up specific issues (and to get an overview of all the issues), I
suggest you look online at:

"Compiler and Run-Time Migration Guide"
Document Number: GC26-4764-04 - URL is:
http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/IGYMG200/CCONT
ENTS

and

"OS/390 V2R4.0 Lang Env for OS/390 & VM Migration Gde"
Document Number: SC28-1944-03 - URL is
http://ppdbooks.pok.ibm.com/cgi-bin/bookmgr/bookmgr.cmd/BOOKS/CEEA603/CCONTE
NTS

I hope that this helps.

Jim Van Sickle wrote in message <34D··.@i··.net>...
› Greetings...
› Our service provider is planning on upgrading from MVS/ESA SP5.2.0 to
…[39 more quoted lines elided]…
› ***********************************************
```

#### ↳ Re: Migration to LE (Language Environment)

- **From:** "arnold trembley" <ua-author-6588869@usenetarchives.gap>
- **Date:** 1998-02-10T19:00:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-3f5d3bada6-p3@usenetarchives.gap>`
- **In-Reply-To:** `<34DF684D.5B24C211@ibm.net>`
- **References:** `<34DF684D.5B24C211@ibm.net>`

```

Jim Van Sickle wrote:
› 
› Greetings...
…[3 more quoted lines elided]…
› applications to run under OS/390 (and LE). I have some specific questions:

I'll take a stab at this. We just upgraded from MVS 4.3 to 5.2.2 last
September, and we're in the process of converting to LE/MVS and COBOL
for MVS and VM. We were already running a mix of OS/VS COBOL and COBOL
II. We're also upgrading from CICS 2.1.2 and 3.3 to CICS 4.1. For a
number of reasons my company decided to install LE/MVS, but not as the
default runtime environment. We're backleveled on our CICS 3.3
maintenance and we have a third party database product that is not LE
compliant. Most of our software upgrades are driven by Y2K, naturally.

I don't have any experience with IDMS, so I don't know if it has any
problems with LE.

›
› 1. Do we have to use LE or can we still (selectively) run with COBOL(II)
› run-time (supported or un-supported) once we go to OS/390?

You should be able to selectively run batch jobs with COBOL II runtime
libraries just by adding JOBLIB DD's, even if LE/MVS is set up as the
default runtime environment. CICS is a little trickier. If LE/MVS is
installed as the default runtime per IBM's instructions, CICS 3.3 and
higher will not complete initialization without the LE runtime
libraries. It is possible to configure MVS to allow the runtime
libraries to be specified in the CICS startup JCL. One CICS region
could have LE runtimes and another CICS region could have COBOL II
runtimes.

›
› 2. If we cannot use COBOL(II) run-time under OS/390, can we start using LE in
› addition to COBOL(II) run-time with MVS/ESA 5.2? Would this be a better
› migration path?

Yes to the first question, especially for batch COBOL. To the second
question, probably yes as well.

But I think you can probably run COBOL II runtime libraries under
OS/390. If LE is installed as the default runtime environment, you may
not be able to use COBOL II runtime libraries in CICS.

In my experience, LE completely replaces the COBOL II runtime libraries,
and COBOL II should not have any problems.

›
› 3. Do we need to re-link our load modules compiled and linked as COBOL(II)
› modules to use LE? Do we need to re-compile?

No, you do not need to recompile or relink your COBOL II programs for
Language Environment/MVS. You may need to recompile or re-link some
OS/VS COBOL programs for LE, if they were compiled with the NORES
option.

In my own limited experience I have *never* had a problem running a
batch COBOL II program with LE. It's seamless. I should warn you that
I'm in applications, not technical services, and I understand that there
are a large number of configuration parameters to be set when installing
LE.

Even in CICS, I haven't had any problems running COBOL II programs with
LE. Installing LE in a CICS region can be a big problem for technical
services, however.

›
› 4. Do assembler subprograms and/or main programs need to be re-assembled and/or
› relinked to run under LE? (The migration guide suggests that LE macros need to
› be used)

It depends on what those assembler programs are doing. Many will run
fine because they don't use LE services. I am not an assembler expert,
but I believe it's possible that some assembler programs might require
changes for OS/390 or HLASM. I am not aware of any specific assembler
requirements to use LE.

›
› 5. If we can selectively run programs with COBOL(II) run-time, how 'bout under
› CICS? Can we run LE and non-LE programs in the same region?

No, a CICS region should use either LE or COBOL II runtime libraries.
It's not really possible to use both runtime libraries in the same CICS
region. But COBOL II programs should run great in CICS with LE. We did
find that LE used more memory in a CICS region, and we had to adjust our
region sizes.

We're doing Y2K testing right now in a time machine LPAR. All our time
machine regions are CICS 4.1 with LE, but the application programs were
all compiled for CICS 3.3 and COBOL II. We did not recompile any of
them, and they work just fine in CICS 4.1 with LE/MVS.

› 
› 6. The IBM guides are (believe it or not) not much help! Anywhere else to look?
…[10 more quoted lines elided]…
› ***********************************************

Arnold Trembley
Software Engineer I (just a job title, still a programmer)
MasterCard International
"Y2K? Because Centuries Happen!"
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
