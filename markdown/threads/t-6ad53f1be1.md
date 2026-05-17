[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# OS/VS COBOL intermixed with Y2K remediation

_2 messages · 2 participants · 1998-03_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k) · [`Compilers and vendors`](../topics.md#compilers)

---

### OS/VS COBOL intermixed with Y2K remediation

- **From:** "william m. klein" <ua-author-3041905@usenetarchives.gap>
- **Date:** 1998-03-26T19:00:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6fhgcd$bsu@dfw-ixnews11.ix.netcom.com>`

```

In a separate thread, there was a question about doing an OS/VS COBOL to
COBOL for this-and-that conversion. In this post, I am going to
provide three responses. The first is a somewhat facetious response from
me; the second is a more serious response from me; the third is a response
from a "usually reliable" source who has not given me permission to state
his/her name/title, but it is such that I certainly vouch for the authority.

1) First response (facetious)
If you are just now starting to think about and plan both a migration
from OS/VS COBOL to a supported compiler WHILE also doing a complete Y2K, my
suggestion is
alternate between crying and praying - you can't get there from here in
only 21 months!

2) Second response (medium serious)


A) Move to an LE run-time environment as quickly as possible. (Lots of
planning and testing required - also probably other products will need
upgrading)

B) Check whether or not you are running Y2K compliant releases of all the
other software (IBM and non-IBM) that you rely on. (Pay special attention to
MVS, CICS, IMS, DB2 - any 3rd party databases and applications). Moving to
OS/390 will "solve" item 1 above, but will require more coordination.
(Depending on how downlevel you are on your various products, just the step
of getting to all Y2K products requires MAJOR coordination, planning, and
testing)

C) Stop ANY thought of trying to convert all of your existing OS/VS COBOL
code to COBOL for this-and-that while doing everything else. Instead try to
identify the MINIMUM number of programs to convert. (Profiler or other
software should help with this). The goal should be to ONLY convert those
COBOL programs

A) that require 4-digit years (must convert these)
B) that store years (probably need to convert these)
C) that pass data back-and-forth to those above (probably need to
convert)

D) You *can* use windowing and keep with OS/VS COBOL - if you are aware that
there are LOTS of risks in doing this (and running an unsupported COBOL
compiler). Depending on how many unsupported" features of OS/VS COBOL your
applications are relying on, this MAY be the most cost-effective way to go

E) Once you have figured out which COBOL programs to convert, make certain
that you REALLY understand what and how they interact with other COBOL
programs. You may need to convert, or at least re-link lots of other
programs. (Pay particular attention to the RES/NORES issues and the passing
of data above and below the line). Make certain that you allow time for
stress-testing as system testing may not show up performance issues.

F) Given how late this is, consider hiring specialists - for the planning
and testing stages as well as the implementation stages.

NOTE: All of the above is dealing SOLELY with the software side of your
COBOL migration. Data migration, 3rd party application upgrades, and
non-COBOL conversions will each require as significant an effort - but
wasn't part of the original question.

>>>>>>>

3) Third (usually reliable source) response
Note: The following "article" was written before COBOL for OS/390 & VM -
and before - LE for OS/390 & VM. Those products should be taken as "better"
than the "MVS & VM" older variations.

There are no known problems with older IBM COBOL products related to the
Year 2000. There are only 2 issues to be concerned with for COBOL
applications and the Year 2000:

1) Date Related Logic
2) Service support from IBM

You can get service support for OS/VS COBOL and VS COBOL II programs
indefinitely by using the Language Environment run-time library with just a
run-time migration. This is described in the next section.

As a result, an application with NO DATE RELATED LOGIC could be run in a
supported environment beyond the turn of the century by a run time migration
only, with no source changes or recompiles necessary.

Repeat, no source code changes or recompiles and your OS/VS COBOL and VS
COBOL II programs can be running with full IBM service support and no Year
2000 problems if they are running under Language Environment and have no
date-related logic problems!

1) Date Related Logic
------------------------
Of course, an application that DOES have date related logic must be examined
to see if it has a Year 2000 problem. If it does, then programs will have
to be changed, which means at the very least a compile, link and test. At
this point you can combine source upgrade (compiler migration) with Year
2000 conversion. IBM does not provide any way for OS/VS COBOL programs to
obtain a 4-digit year date, so you must compile with at least VS COBOL II in
order to use IBM provided services for obtaining a 4-digit year date.
If you want to use COBOL language to get 4-digit year dates, then the only
COBOL compilers you can use are the newest ones:
COBOL for MVS & VM, COBOL for OS/390 & VM, and COBOL for VSE.
VS COBOL II programs can get access to the LE date/time routines via dynamic
CALL statements if they are running under LE.

2) Service support for programs compiled with OS/VS COBOL or VS COBOL II
---------------------------------------------------------------------
IBM will continue to provide service support for the execution of programs
compiled with the OS/VS COBOL and VS COBOL II compilers as long as these
programs are using the Language Environment for MVS & VM (5688-198) versions
of the COBOL library routines. (This also holds true for programs compiled
with the DOS/VS COBOL and VS COBOL II compilers running on VSE, except that
the strategic run-time library for VSE is Language Environment for VSE
(5686-094).)

Every COBOL program requires library routines in order to execute.
They may be statically linked to the load modules or dynamically accessed at
execution time. If the library routines that are being used are supported
by IBM service, then you can call IBM when there is a problem and get the
problem fixed. For example, the library routines for OS/VS COBOL programs
exist in the OS/VS COBOL run-time library, the VS COBOL II run-time library,
and in the Language Environment run-time library. If your OS/VS COBOL
programs are running using the OS/VS COBOL library, then they are not
supported by IBM service. If your OS/VS COBOL programs are running using
the Language Environment run-time library, then your programs are supported
by IBM service, and will be supported well into the 21st century.

If you are starting with load modules consisting of programs compiled with
the NORES option and link-edited with the OS/VS COBOL library or the VS
COBOL II library, then you will need to use REPLACE linkage editor control
statements to replace the old library routines with the Language Environment
versions. If you start with object programs (non-linked) then you just need
to link edit with Language Environment If the programs are compiled with
RES, then you can just make the Language Environment library routines
available at execution time in place of the OS/VS COBOL or VS COBOL II
library routines by using LNKLST, or STEPLIB on MVS, and GLOBAL statements
on VM.

A recompile is NOT required to complete your migration.
-------------------------------------------------------
The ideal state is that programs should be compiled with a supported
compiler (recommended is COBOL for MVS & VM) running with a supported
run-time library (Language Environment for MVS & VM). However this ideal
state can be reached gradually in a fully supported manner:
1) Run-time migration followed OPTIONALLY at some future date by
2) Compiler migration

What if I need to make a change to an OS/VS COBOL program?
-----------------------------------------------------------

The OS/VS COBOL compiler is not supported, although the programs that were
generated by it are supported under Language Environment.

Once you have completed the run-time migration, if a change needs to be made
to a COBOL program (for maintenance or enhancement) you only need to run the
source though a source conversion tool such as CCCA (5785-ABJ) or the
Conversion feature of VisualAge for COBOL and then compile using the COBOL
for MVS & VM compiler. This way you can gradually convert your source with a
minimum cost to your company.

For complete information on both run-time migration and source conversion,
see the COBOL Migration Guide, GC26-4764, and the LE Migration Guide,
SC28-1944. You can view both on the Web from the bookshelf at:
www.software.ibm.com/year2000
```

#### ↳ Re: OS/VS COBOL intermixed with Y2K remediation

- **From:** "marvin l.jones" <ua-author-17075454@usenetarchives.gap>
- **Date:** 1998-03-27T19:00:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-6ad53f1be1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<6fhgcd$bsu@dfw-ixnews11.ix.netcom.com>`
- **References:** `<6fhgcd$bsu@dfw-ixnews11.ix.netcom.com>`

```

In comp.software.year-2000 William M. Klein
wrote: .... a lot of 'good stuff'!

Thanks, Bill, for this golden nugget.
It's a sight for sore eyes in amongst all the other drivel appearing
in comp.software.year-2000.

Jonesy
MainFrame since 1966

Marvin Jones  jonzrmi.net
Gunnison, Colorado
643 days to go until the Year 2000
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
