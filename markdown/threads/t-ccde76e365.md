[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migration to LE (NOCMPR2)

_4 messages · 4 participants · 2000-07_

**Topics:** [`Migration and conversion`](../topics.md#migration)

---

### Migration to LE (NOCMPR2)

- **From:** "Brian Reader" <bri@london.com>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8kh87d$ei1$1@supernews.com>`

```
Greetings everyone,

I work at a site where they are currently debating whether to upgrade from
an old version of IBM COBOL (COBOL II rel 2 or 4) to COBOL for OS/390 with
LE. Half the code is hand crafted, the other half comes from a code
generator (either TELON or an old version of MetaCOBOL).

It is understood that IBM will stop support after March 2001. Because of the
vast amount of info available (from IBM and others) it's difficult to know
what the approach should be for upgrading, or what the main issues are (if
any). Hence your views of the following would be most welcome:

With over 20,000 COBOL modules, should we be trawling through source code to
look for COBOL statements that potentially will behave differently? Do we
just recompile with new compiler, fix any compile errors/warnings, then test
everything? Or is there something else we need to do?

Any views or help on this would be most welcome.

Brian Reader
```

#### ↳ Re: Migration to LE (NOCMPR2)

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<396C6E94.E9FC247D@cusys.edu>`
- **References:** `<8kh87d$ei1$1@supernews.com>`

```


Brian Reader wrote:
> 
> Greetings everyone,
…[18 more quoted lines elided]…
> Brian Reader

Run things through its converter if you want.  I'm not sure it is
necessary, it is just as easy to fix things by hand.  After getting
clean code, the only problems which I found were where default
initializations were different (make sure that you initialize variables
before you use them), and blocksize was handled differently.   Oh, you
also need to change your JCL, adding to the steplibs.
```

#### ↳ Re: Migration to LE (NOCMPR2)

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8khs7p$jba$1@slb3.atl.mindspring.net>`
- **References:** `<8kh87d$ei1$1@supernews.com>`

```
What you don't say is whether you are using the LE run-time (that is bundled
into OS/390) as the run-time for your existing VS COBOL II programs.  This
should be a MAJOR issue in making this decision.  LE does (and has since it
first began) included all the run-time support required for VS COBOL II (and
even OS/VS COBOL - for that matter).

Therefore, if you are already EITHER running your VS COBOL II compiled
programs with LE - using the RES compiler option or by using the NORES
compiler option and using the LE library at Link-Edit time, then your life
will be relatively quick and painless moving to IBM COBOL for OS/390 & VM -
from VS COBOL II, R4.

If, on the other hand, you are still using the VS COBOL II libraries as your
run-time library for your VS COBOL II programs, (either RES or NORES), you
have some MAJOR work ahead of you.  This is because there are LOTS of
performance, debugging, and other issues in switching to LE itself (even if
you never change your COBOL source code or object code).

As far as VS COBOL II, R2 programs go, this is another "issue" that you need
to deal with separately.  Even the newest IBM compilers (on the Mainframe -
but NOT VisualAge COBOL on Workstations) include the "CMPR2" compiler option
which BASICALLY works like VS COBOL II, R2.  HOWEVER, there are a reasonable
number of "gotchas" and hidden migration issues for such source code.

Recommendation:

Step 1 - "run" do not "walk" to killing off the VS COBOL II run-time (and
link-edit) library.  If you haven't done this already, then try and work out
a plan (allowing for LOTS of testing and tuning - both unit testing and
STRESS testing) to get to a "comparably" performing system - same object
code, new run-time library.

Step 2 - If your existing VS COBOL II programs are compiled with NORES - or
you are using the VS COBOL II "MIXRES" run-time option, develop a plan to get
to RES as quickly as possible.  (This isn't "technically" required before
moving to the newer compilers and/or LE - but it is something that will make
the rest of your migration much, MUCH, easier.)

Step 3 - Work on moving any VS COBOL II, R2 programs to a newer compiler
(PROs and CONs on whether this should be VS COBOL II, R4  - or COBOL for
this-and-that) with the CMPR2 compiler option.  If you are "daring," you can
try moving directly to NOCMPR2, but this "scares" me personally.  (The IBM
CCCA product will help with the source code changes required for this.)

Step 4 - Do *not* plan on any "mass" migration of source *or* object code.
LE really DOES fully support all your existing object code.  There is no real
reason that you can't keep existing VS COBOL II object code *THAT USES THE LE
RUN-TIME LIBRARY* well past March 2001.  IBM supports this and all "should"
be fine.  You *should* however, be looking at moving your VS COBOL II code to
the new compiler *as* you maintain each module, program, application.  For
your existing VS COBOL II, R4 programs, this should be EASY (even if they use
CMPR2).  There are very, VERY, few syntax or semantic differences between the
two.  Only "normal" testing should be required for such applications as you
"upgrade" compilers.

Step 5 - Any remaining CMPR2 programs should be "migrated" to NOCMPR2
(possibly using CCCA - or comparable product) as resources (for programming
AND testing) allow.  This certainly should be a "goal" - but it isn't as high
a priority as the other items (unless you plan on using VisualAge COBOL - in
which case it is required).

Step ???  - IBM (and others) provide migration assistance (for a FEE).  If
you are still using many VS COBOL II, R2 programs and/or lots of NORES or
MIXRES programs *and* still using the VS COBOL II run-time libraries, I would
strongly recommend looking at "paid" migration assistance - at least at the
planning stage.  If on the other hand, you are already using NOCMPR2 and RES
and the LE run-time library (for most of your applications), the migration
should be pretty easy and easy to manage - and you should be able to handle
it "in house".

   ***

Does this help?
```

##### ↳ ↳ Re: Migration to LE (NOCMPR2)

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 2000-07-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000712101330.18275.00000216@ng-cm1.aol.com>`
- **References:** `<8khs7p$jba$1@slb3.atl.mindspring.net>`

```
I agree with everything that Bill wrote, and also suggest 

(<advert_on>) 

TRAINING! What a concept. There are just a ton of changes in COBOL and new
facilities in LE that are available to the COBOL programmer. In addition, LE
produces a new dump format and debugging techniques will probably have to
change.

There are a variety of training sources for these topics (come to my talk at
SHARE in BOSTON) although, of course, I'm rather attached to our offerings. For
a high-level overview, see below; for more details, see the website in my
signature. All these courses have lots of hands-on labs.

Beyond COBOL II - 2 days; covers changes introduced in COBOL II (but that were
not taught to most programmers even though it's been over 15 years), and the
new COBOL compilers (COBOL/370, COBOL for MVS & VM, COBOL for OS/390 & VM);
also has a brief introduction to LE.

Application Design Using LE Services - 3 days; a thorough introduction to LE,
including a survey of all the services, and how to use them in applications;
this course is actually multi-lingual and you can run labs in COBOL, PL/I, C,
or Assembler. This is the course IBM teaches in its ed centers in the US and
around the world; we have taught it under IBM auspices in Kuwait, Denmark, and
the US; we have also taught it on our own in over a dozen companies and
organizations around the US.

Application Design Using LE Services + Beyond COBOL II - 4 days; obviously a
combination of the first two courses; by combining overlapping content we can
fit it all in 4 rather busy days.

COBOL Debugging and Maintenance in the LE Environment - 2 days; debugging COBOL
batch programs using LE dumps and COBOL language facilities. Also includes
discussions on the Linkage Editor, Program Binder, subroutines (static and
dynamic calls), and alternative ways of passing and receiving parameters.

COBOL Debugging and Maintenance in OS/390 - 3 days; debugging COBOL batch
programs using OS/390 SYSUDUMPS, LE dumps, and COBOL language facilities. Also
includes discussions on the Linkage Editor, Program Binder, subroutines (static
and dynamic calls), and alternative ways of passing and receiving parameters.

We also have various debugging classes for CICS; coming soon: using Debug Tool,
a multi-language debugging course using the LE Debug Tool.

InterLanguage Communications in OS/390 - 3 days; an advanced look at calling
between programs, especially programs written in different languages (COBOL,
PL/I, C, Assembler). Includes discussions of sharing external data, alternate
entry points, dynamic linkages, and DLL support in OS/390.

(<advert_off>)

Well, just a thought.

Regards,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
