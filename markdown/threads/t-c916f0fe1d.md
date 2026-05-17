[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# NORES linked program under IBM LE/370 or COBOL for MVS & VM

_2 messages · 2 participants · 1997-12_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### NORES linked program under IBM LE/370 or COBOL for MVS & VM

- **From:** "bob strating" <ua-author-17072665@usenetarchives.gap>
- **Date:** 1997-12-08T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<881702586.10230.0.rover.c30bfff5@news.demon.nl>`

```

Hi,

Does anybody have experience with relinking NORES modules with LE/370?

We still have NORES modules and we don't want to recompile every program
with the RES option. Some are very old programs and we are not sure that we
have all the right source components. According to the migration manual it
would be a simple relink and afterwards most release combinations in the
call structure should be possible.

We already know that we have to rewrite assembler (sub)programs which were
written in the past to create our own dynamic call feauture. The assembler
programs use load/delete macro's that are not supported in LE/370.

Does anybody have success stories or worse horror stories?
```

#### ↳ Re: NORES linked program under IBM LE/370 or COBOL for MVS & VM

- **From:** "rwi..." <ua-author-3315823@usenetarchives.gap>
- **Date:** 1997-12-09T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-c916f0fe1d-p2@usenetarchives.gap>`
- **In-Reply-To:** `<881702586.10230.0.rover.c30bfff5@news.demon.nl>`
- **References:** `<881702586.10230.0.rover.c30bfff5@news.demon.nl>`

```

Valid OS/VS COBOL programs can be migrated to LE/370 versions of the run-time
modules. RES programs just need to be STEPLIBed to the new run-time. NORES
programs will require relink with REPLACE of all ILBOxxxx modules.

Biggest issue is "valid" - i.e. no mix of RES/NORES, no assembler subroutines
that are not LE compliant (biggest example is dynamic loader written in
assembler).

How to procede? Characterize what you have. Several ways to do this, all
relate to doing software archaelogy on existing load modules. Easiest method
that I know of (Warning - here comes blatant commercial) is to use the Edge
Portfolio Analyzer which will extract structure and attributes of compiled code
from the load modules. Then one can build relink jobs where appropriate. Of
course if you have the Portfolio Analyzer this task in done for you by an
"external analyzer" that digests the inventory / structure / connection data
produced by the initial analysis.

Once one has completed the initial analysis and relink, the remaining major
factor is behavior change. The best example is what happens when a
dd-statement is missing or mis-spelled. The behavior in this case - when no
FILE STATUS checking is in the program is affected by run-time options, which
are either ZAP changes to the run-time modules, or install options. An example
might be a U295 abend with the old run-time, a return code of 4000 or ? with
the new run time.

The real isssue here is not the inability to acheive acceptable behavior with
old code and new run-time. It is simply the fact that the new run-time
(LE/370) has perhaps 200 or more parameter to be set. A relatively small set
of well structured tests can be used to characterize old code with old
run-time, and old code with new run-time. This technique is described in "HLL
Predictability Testing" (published in both SHARE and GUIDE proceedings).

Bottom line - what you propose to do is quite acheivable. Plan and configure
first, then examine each case that you want to process, then relink them.
Rex Widmer
Builder of software archeology tools and other strange programs to help survive
in a legacy based world.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
