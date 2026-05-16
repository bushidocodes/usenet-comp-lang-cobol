[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Migrating to COBOL for OS390

_14 messages · 8 participants · 1999-07 → 1999-08_

**Topics:** [`Migration and conversion`](../topics.md#migration) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### Migrating to COBOL for OS390

- **From:** Peter Marshall <marshall.peter@canadatrust.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379D9BF5.B56A6C2D@canadatrust.com>`

```
Hello all!

We are in the process of evaluating a move from our current COBOL, VS
COBOL II (version 1.3.0), to the new COBOL for OS390 (version 2.1).  Our
shop has some 16,000 programs and are currently running under LE version
1.5 (we are also looking to change that to version 1.8).

We are curious to know if anyone else has done this type of migration
and if so, have run across any problems/pitfalls.

IBM recommended that we regression test ALL programs, however, we simply
cannot afford to do so both from a time perspective, as well as money.
If the business plan gets too expensive we will have to remain at our
current unsupported version.

Any advice/tips are greatly appreciated.

Thanks,
Peter Marshall
Senior Systems Analyst
Canada Trust
```

#### ↳ Re: Migrating to COBOL for OS390

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nkllg$dii@dfw-ixnews11.ix.netcom.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com>`

```
The first thing I would say is why Oh WHY - would you want to recompile all
your existing programs?  There is no reason that you can't have VS COBOL II
and COBOL for OS/390 & VM object code "happily" co-existing for as long as
you want.  Therefore, my first suggestion would be to NOT do a "mass
recompilation" - but instead to gradually recompile your programs with the
newer compiler - as your resources allow (including appropriate testing).
Often it does make (business-internal) sense to recompile an entire
application at one time - but almost never to recompile all the programs in
your shop.

The next thing I want to say is that you are on a VERY old version of VS
COBOL II.  I can't remember when release 3.0 went out of service, but it was
IBM's very 1st attempt at providing an ANSI'85 compiler - and there have
been many, MANY bugs "fixed" since that product.  (VS COBOL II, R4 is the
currently supported product - and it is scheduled to go out of service March
of 2001.)

If you were using VS COBOL II, R4, then I would say that you could
"reasonably" expect most (almost all) of your existing programs to recompile
fine and run as expected with the newer compiler.  But from where you are
coming, I would definitely expect some "problems".

The next question for you is whether you are using RES, NORES, or MIXRES in
your current VS COBOL II environment.  If you are already RES, then this
will significantly reduce your migration effort getting to COBOL for
this-and-that.  If you are NORES *and* have been using the LE library
(SCEELKED) in your link-edit step, then this too should reduce (but not as
much) your migration effort.  If your are currently using MIXRES - or you
have been using the VS COBOL II run-time library (rather than the LE one)
either at run-time or link-edit time, then you are in for some SIGNIFICANT
migration issues (often sever performance impacts if you don't do everything
exactly right).

Again, just so you know, IBM does *fully* support VS COBOL II (even OS/VS
COBOL) object code that uses the LE run-time library - even after March
2001.  So I just don't understand the "goal" of your planned migration.
Therefore, my recommendations are:

1) Do NOT migrate (recompile) all your programs at once.

2) Do make certain that all your VS COBOL II programs are compiled (and
tested) as RES and use the LE library (and 2nd choice are NORES and use the
LE library for link-edit).

3) Do plan for a "phased-in" migration to COBOL for OS/390 & VM - by
recompiling programs (or applications) when you actually NEED to change them
(and when you have the resources to test them).  Pay particular attention to
"performance" issues and compile and run-time options.
```

##### ↳ ↳ Re: Migrating to COBOL for OS390

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379DE632.5A15BEA4@NOSPAMhome.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <7nkllg$dii@dfw-ixnews11.ix.netcom.com>`

```
William M. Klein wrote:
> 
> The first thing I would say is why Oh WHY - would you want to recompile all
…[7 more quoted lines elided]…
> your shop.

You should have a strategy for making sure that called programs and
calling programs work together though.  Cobol II can be compiled above
or below the line.  I have seen COBOL II programs stop short when
calling a COBOL for MVS program - plan your gradual conversion with this
in mind.   Eventually, converting the remaining programs can simplify
maintenance and control though.

Changing compilers, operating systems versions, and even compiler
options can break programs - sort of like changing Java libraries.  And
running in test environments may not catch all of the socket and other
interface needs which are pointing to production, unless you are
carefully looking for these.
```

###### ↳ ↳ ↳ Re: Migrating to COBOL for OS390

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nlals$f5c@dfw-ixnews21.ix.netcom.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <7nkllg$dii@dfw-ixnews11.ix.netcom.com> <379DE632.5A15BEA4@NOSPAMhome.com>`

```
Howard Brazee <brazee@NOSPAMhome.com> wrote in message
news:379DE632.5A15BEA4@NOSPAMhome.com...
  <snip>
>
> You should have a strategy for making sure that called programs and
…[5 more quoted lines elided]…
>

Actually, this is true for VS COBOL II calls to VS COBOL II; COBOL for
this-and-that CALL to other COBOL for this-and-that programs; OR any
combination of the 2.

You to need to understand both the AMODE and RMODE link-edit attributes of
both the programs you are using - as well as the DATA compiler setting - and
for the COBOL for this-and-that the RMODE compiler setting (which can be
different from the RMODE link-edit attribute).  When you understand all of
these AND know whether your calls are dynamic or static, you can "easily"
predict whether they will work or not.  If you don't know all of this- you
are in for problems - even without a change in compilers.
```

#### ↳ Re: Migrating to COBOL for OS390

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 1999-07-27T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com>`

```
Peter, I agree with William.  There's no need to recompile all your programs
at once.  As long as you still have your old runtime for the programs, you
should be find.  As to the other things that William said those I don't know
too much.  3 yrs ago , I worked at one place where we just started to move
to Cobol II.  I wasn't involved with that.  At my current job the complier
is at OS390, and I wasn't around during that conversion.  I don't know what
little changes are required.

If this is in relation to Y2K, you could be finding a few more problems than
need be.  What you could do is convert a few of your major/main programs and
test those against your production programs.  If everything looks ok, then
do another bunch of programs.  You could test those and then do some more or
if you feel confident with the first batch of compling and testing, then
just do your conversions.  From experience sometimes that works and
sometimes it doesn't.  It's your call.  Best bet, convert those that must be
done and do the others when normal maintenace is required.

The unsupport complier should still run after 2001.

Tim.

Peter Marshall <marshall.peter@canadatrust.com> wrote in message
news:379D9BF5.B56A6C2D@canadatrust.com...
> Hello all!
>
…[19 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Migrating to COBOL for OS390

- **From:** Peter Marshall <marshall.peter@canadatrust.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379EF791.178B8C7@canadatrust.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net>`

```
I thank you all for your answers and concerns.

We do not want to recompile all of our programs and are looking at a 'phased-in'
approach as each of you suggest.  I probably did not state it well initially,
but it was IBM who suggested we recompile the shop.  Not exactly what we wanted
to hear.

We have an interesting environment where we currently use LE in our online CICS
world, but a mix of LE and COBOL II run times in batch.  We are RES as well.

Over the past few months we have taken a few of our more monster programs and
have recompiled and experimented with them.  This includes chains of programs
where Assembler calls COBOL, COBOL calling Assembler, Fortran, etc.

The feeback I have gotten from this newsgroup has been great!!  Keep it coming!!

Thanks,
Peter Marshall
Senior Systems Analyst
Canada Trust

Tim Hillock wrote:

> Peter, I agree with William.  There's no need to recompile all your programs
> at once.  As long as you still have your old runtime for the programs, you
…[42 more quoted lines elided]…
> >
```

###### ↳ ↳ ↳ Re: Migrating to COBOL for OS390

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7nnqqi$54k@dfw-ixnews8.ix.netcom.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net> <379EF791.178B8C7@canadatrust.com>`

```
If you have RACF (or ACF or any other comparable product), I would say that
your next step is to put the VS COBOL II run-time libraries into "warn"
mode, so you can get an ACCURATE report on exactly which
programs/applications are still using it (in batch).  Those are the
applications that I would be targeting first.  Get them into using the LE
run-time library (killing off the VS COBOL II library as QUICKLY as you can)
and you should be in pretty good shape. (If nothing else, this will have you
"supported by IBM" even after March 2001.)

If you (or someone in your shop) has access to IBMLink, I would get them to
search ALL (and it is large number) of APARs that closed DOC or PER
(documentation change or code change) after VS COBOL II, R3.0.  This list
will give you an idea (database) of what type of "changes" in either
behavior or "supported syntax" you can expect between VS COBOL II R3.0 and
IBM COBOL for OS/390 & VM.  When I wrote my book ("OldBOL to NewBOL: An IBM
COBOL Migration Tutorial") there were many, MANY, pages of such APARs that I
included in an Appendix - that was several years ago, so things can only
have gotten worse since then.

It is worth noting that the IBM COBOL for OS/390 & VM Migration Guide (from
IBM) *does* include a little information on migrating from VS COBOL II (not
just from OS/VS COBOL) - so I would sure make certain that you have looked
at/read that too.
```

###### ↳ ↳ ↳ Re: Migrating to COBOL for OS390

_(reply depth: 4)_

- **From:** Pete Wirfs <petwir@saif.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379F9C71.2F3@saif.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net> <379EF791.178B8C7@canadatrust.com> <7nnqqi$54k@dfw-ixnews8.ix.netcom.com>`

```
<massive snip!>

For our phased in approach, we added a home-grown source code converter
into the checkout phase of our change control system.  After running
this way for almost 2 years, we found that most of our stuff was
converted, and we kicked off a small project to complete the job.  But
then, we only have 2,000 programs. :-)  Developers did not enjoy those
two years, but hey, it HAS to be done.

Another reason for wanting to upgrade, is that OS/VS and COBOL-II
applications can not co-exist under a TSO session in split-screen
without causing memory management problems.  I ran into this last week
with two vendor products that have not been upgraded to OS390 yet.  :-(

Some of the conversion issues we had were;

* Working storage no longer initialized itself or initializes
differently.  You have to code VALUE statements where you didn't need to
before.

* The new SSRANGE compiler option is wonderful and should always be
turned on, but some old code can't run with it.  In some cases we
re-engineered the application, but usually we turned off this compile
option for these programs.

* The JCL PARM card under LE now assumes the last slash(/) is a
delimiter between your program parm and LE parms.  So PARM=(01/01/99)
would only pass "01/01" into the application.

* As mentioned before by others, we had to upgrade subroutines to 31/ANY
before the application could be upgraded to 31/ANY.

* "NEXT SENTENCE" behaves differently.  We convered them all to
"CONTINUE" to maintain consistent behavior.

This list is just off the top of my head....  I've probably missed some.

Pete Wirfs
Salem Oregon
```

###### ↳ ↳ ↳ Re: Migrating to COBOL for OS390

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7noa6s$3jb@dfw-ixnews12.ix.netcom.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net> <379EF791.178B8C7@canadatrust.com> <7nnqqi$54k@dfw-ixnews8.ix.netcom.com> <379F9C71.2F3@saif.com>`

```
See comments below (about differences and non-differences in a COBOL
migration).

Note:
  Much of the note to which I am replying was talking about a migration from
OS/VS COBOL to VS COBOL II.  The original note in this thread was talking
about VS COBOL II to COBOL for OS/390 & VM.  These 2 migrations have VERY
different concerns and issues (although the "methodology," planning, and
testing are often quite similar).
```

###### ↳ ↳ ↳ Re: Migrating to COBOL for OS390

_(reply depth: 5)_

- **From:** "Bill Turner, WB4ALM" <wb4alm@gte.net>
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A08820.DC7339C1@gte.net>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net> <379EF791.178B8C7@canadatrust.com> <7nnqqi$54k@dfw-ixnews8.ix.netcom.com> <379F9C71.2F3@saif.com>`

```
I agree with most of the hints that have been listed above - been there, saw
what happened, and had to argue for days on why it happened. (Programmers
shooting themselves in THEIR feet, while trying to get mine.)

We are "mostly" converted away from VS COBOL II, but still find some people
having problems.

Many are caused by OLD linkedit JCL that people hardcoded AMODE=24 or
RMODE=24 into the Linkedit parm statement.

If you don't know that you need to "force" a particular AMODE/RMODE, than do
nothing - and let the binder do its job.
I still have to tell people to remove "defaulted" parameters from compiler
and link edit PARM= statements, unless they
really know that the MUST specify that particular value.

/s/ Bill Turner, wb4alm



Pete Wirfs wrote:

> <massive snip!>
>
…[36 more quoted lines elided]…
> Salem Oregon
```

###### ↳ ↳ ↳ Re: Migrating to COBOL for OS390

_(reply depth: 6)_

- **From:** Jared Thomas <jared@techie.com>
- **Date:** 1999-07-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A12191.93E13904@techie.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net> <379EF791.178B8C7@canadatrust.com> <7nnqqi$54k@dfw-ixnews8.ix.netcom.com> <379F9C71.2F3@saif.com> <37A08820.DC7339C1@gte.net>`

```
I strongly agree --- Let the Binder do Its Job!

But look at the cross reference for a couple of things...

some old csects have no AMODE/RMODE specification with them.  This
makes them 24/24 which might not be true.  Check them out as they
may be the only thing which is keeping your load module 24/24.

For example, I found one shop carring around a DFHxxx module which
is just glue to reach the CICS routines.  Can't remeber the exact
name, but its only a handfull of bytes and in always needed for
Command Level CICS.  Anyway, this guy was from CICS V3 (or was it
V2?) and had no amode/rmode.  The module form CICS V4 had exactly
the same instructions, plus any/any as it could run anywhere in
any mode.  After I got it out of the library, a lot of COBOL
online programs suddenly moved above the line.

Also look for some old ILB0xxx stuff and see if they are residules
from old COBOL.  There are replacements in newer runtimes for
them.  Better yet, change the source to call the IGZxxxx modules. 
The new ILBxxx replacements are just glue to the IGZ stuff.

Bill Turner, WB4ALM wrote:
> 
> I agree with most of the hints that have been listed above - been there, saw
…[15 more quoted lines elided]…
> /s/ Bill Turner, wb4alm
```

###### ↳ ↳ ↳ Re: Migrating to COBOL for OS390

- **From:** Peter Marshall <marshall.peter@canadatrust.com>
- **Date:** 1999-07-28T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<379EF8FB.C199A4DC@canadatrust.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <o1rn3.188$m%3.457565@NewsRead.Toronto.iSTAR.net> <379EF791.178B8C7@canadatrust.com>`

```
I forgot to mention that this conversion is not for Y2K.  We are compliant and were
so last November by using windowing and altering and retesting our code.

Peter

Peter Marshall wrote:

> I thank you all for your answers and concerns.
>
…[65 more quoted lines elided]…
> > >
```

#### ↳ Re: Migrating to COBOL for OS390

- **From:** Daniel Jacot <daniel.jacot@winterthur.ch>
- **Date:** 1999-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7o3k2a$74i$1@nnrp1.deja.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com>`

```
In article <379D9BF5.B56A6C2D@canadatrust.com>,
  Peter Marshall <marshall.peter@canadatrust.com> wrote:
> Hello all!
>
> We are in the process of evaluating a move from our current COBOL, VS
> COBOL II (version 1.3.0), to the new COBOL for OS390 (version 2.1).

<snip>

> We are curious to know if anyone else has done this type of migration
> and if so, have run across any problems/pitfalls.

<snip the rest>

Peter,

In addition to what the other persons wrote about your question (and to
whom I fully agree), I can give you some hints about problems you
can get when you recompile existing VS COBOL II R3 code to a newer
compiler (thanks to Sabine Lauterbach from DATEV, Germany!):

1. The period in area A is not tolerated anymore
   (ISPF: change '.' 8 11 '     .' all)

2. A field defined as 'PIC X' may not been compared with 'NOT ZERO',
   only with 'NOT = ZERO'. NOT ZERO is interpreted as Sign-Condition,
   NOT = ZERO as a Figurative Constant.

3. You may not SET and INDEX to 0 (and then add 1 in a loop). This
   was never allowed, but COBOL II accepted this. If you don't want
   to change your existing logic, you can SET the index to 1 and then
   SET it DOWN BY 1.
```

##### ↳ ↳ Re: Migrating to COBOL for OS390

- **From:** Howard Brazee <brazee@NOSPAMhome.com>
- **Date:** 1999-08-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<37A599F3.68A7D471@NOSPAMhome.com>`
- **References:** `<379D9BF5.B56A6C2D@canadatrust.com> <7o3k2a$74i$1@nnrp1.deja.com>`

```
Daniel Jacot wrote:

> 3. You may not SET and INDEX to 0 (and then add 1 in a loop). This
>    was never allowed, but COBOL II accepted this. If you don't want
>    to change your existing logic, you can SET the index to 1 and then
>    SET it DOWN BY 1.

I never knew that COBOL II had this improvement over this silly
standard.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
