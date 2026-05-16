[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL II compile options for MVS

_11 messages · 8 participants · 1998-11_

**Topics:** [`Compilers and vendors`](../topics.md#compilers) · [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### COBOL II compile options for MVS

- **From:** "Gregory Desyatnik" <grigory@concentric.net>
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<736tg2$plv@chronicle.concentric.net>`

```
The company I work for is trying to standardize on compile procedures for
Y2K project.  One would expect they should already have something in place
for a long time, but...

My question is: should they use RENT option for COBOL II batch programs to
make them run above 16 Mb line (assuming they do not mix COBOL II with the
VS/COBOL programs)?
I have noticed the size of the load modules gets much smaller when using
that option (I think RENT forces another option - RES, which causes dynamic
calls to COBOL II system modules).

IBM documentation does not tell much, thus I am not quite comfortable with
all the options for batch, online, main programs, sub-programs etc.
I would appreciate any insight information on the issue.

Thanks,

Greg
```

#### ↳ Re: COBOL II compile options for MVS

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36572426.0@news2.uswest.net>`
- **References:** `<736tg2$plv@chronicle.concentric.net>`

```
The book COBOL II, but Harvey Bookman, from McGraw-Hill, ISBN 0-07-006533-0,
contains an extensive discussion of the compiler options in an IBM context.


Gregory Desyatnik wrote in message <736tg2$plv@chronicle.concentric.net>...
>The company I work for is trying to standardize on compile procedures for
>Y2K project.  One would expect they should already have something in place
…[19 more quoted lines elided]…
>
```

#### ↳ Re: COBOL II compile options for MVS

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73794b$15m@dfw-ixnews4.ix.netcom.com>`
- **References:** `<736tg2$plv@chronicle.concentric.net>`

```

Gregory Desyatnik wrote in message <736tg2$plv@chronicle.concentric.net>...
>The company I work for is trying to standardize on compile procedures for
>Y2K project.  One would expect they should already have something in place
…[17 more quoted lines elided]…
>

First,  if you are doing Y2K work, then using VS COBOL II is the WRONG
compiler.  You should be using IBM COBOL for OS/390 & VM (or the slightly
older IBM COBOL for MVS & VM).  Many of the IBM provided features for Y2K
are ONLY available in the newer compilers (and the one you are using is
going out of service early in 2001).

OK, now for compiler options.

Are you already using RES for most programs?  If not moving to it is
important but is NOT easy.  (You should look at the MIXRES option to help -
but even with that, there is some work involved with the move to RES and
some "unpredictable" run-time results may occur.)  FYI, once you go to one
of the new compilers, this isn't even a decision to make ONLY "RES" type
behavior is supported.

Indeed, you probably DO want to go to RENT (once you have already gone to
RES) - because this will give you VSCR (Virtual Storage Constraint Relief).
The change from NORENT to RENT shouldn't cause many programming/application
problems - with one exception.  If you try to pass data from  a RENT program
to an "older" program - still running below the 16M line, then make certain
that you use the DATA(24) compiler option.  This will lose some of the VSCR,
but will let the other program access your passed data.
```

##### ↳ ↳ Re: COBOL II compile options for MVS

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3657C39C.1126375D@worldnet.att.net>`
- **References:** `<736tg2$plv@chronicle.concentric.net> <73794b$15m@dfw-ixnews4.ix.netcom.com>`

```
William M. Klein wrote:
> 
> Gregory Desyatnik wrote in message <736tg2$plv@chronicle.concentric.net>...
…[25 more quoted lines elided]…
> going out of service early in 2001).

I would argue that this is not such a bad choice.  Some shops have
issues that make it difficult to migrate to Language Environment runtime
libraries.  Generally, source code changes are required to migrate OS/VS
COBOL programs to either COBOL II or an LE-enabled compiler.  Once
you're on COBOL II, no source code changes are required to move to an
LE-enabled compiler, and recompiling should not be necessary to turn on
Language Environment.

A common reason for delaying LE migration is having one or more
third-party software products that you haven't yet upgraded to LE
versions.  One disadvantage to COBOL II is there is no native way to
obtain current date with 4-digit year, unless you have the IGZEDT4
runtime routine (available by APAR/PTF), or by writing your own
assembler routine.

> 
> OK, now for compiler options.
…[6 more quoted lines elided]…
> behavior is supported.

Absolutely.  Do NOT use the NORES option.  It will only cause problems
later.  

> 
> Indeed, you probably DO want to go to RENT (once you have already gone to
…[5 more quoted lines elided]…
> but will let the other program access your passed data.

This is good information.  My own preferences are
OFFSET,DATA(31),RES,NUMPROC(NOPFD),TRUNC(OPT)

TRUNC(OPT) is somewhat controversial, but I've been using it in CICS for
a couple of years now with no problems.  For my purposes, it's the
closest option to the old OS/VS NOTRUNC.  Similarly, NUMPROC(NOPFD)
seems to give the fewest S0C7 abends and is closest to the arithmetic
behavior I expected with OS/VS COBOL.  

I don't see any need for RENT in batch COBOL, but if you like the
smaller load modules I don't suppose re-entrant code will hurt
anything.  Just make sure all programs in a run-unit are RENT.  The RENT
option is required for CICS programs.

I also liked the other suggestion referring to Harvey Bookman's work on
COBOL options.  If you have his book there's lots of good information
there.
```

###### ↳ ↳ ↳ Re: COBOL II compile options for MVS

- **From:** d.s.kirk@ix.netcom.com (David)
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3659758e.12579586@nntp.ix.netcom.com>`
- **References:** `<736tg2$plv@chronicle.concentric.net> <73794b$15m@dfw-ixnews4.ix.netcom.com> <3657C39C.1126375D@worldnet.att.net>`

```
On 22 Nov 1998 07:53:57 GMT, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:

>William M. Klein wrote:
>> 
…[81 more quoted lines elided]…
>there.

just a few comments: 
- cobol ii is 'y2k irrelevant' -- ibm will support for a couple more
years, but it has no y2k tools. that is the main reason to leave it.
newer versions have intrinsic functions for windowing and for 4-digit
years. but -- cobol ii has no inherent y2k problems of its own.   
- RENT is still good for cobol ii to ensure the 31-bit addressability.
removes virtual storage constraints for reduced runtime costs  
- NUMPROC(MIGVS) is my preference as it's more efficient by far than
NOPFD and S0C7's are equivalent to os/vs cobol.   
- TRUNC(OPT) is great if you are managing all your data fields to fit
within the pic clause. for example, I see CICS applications with data
areas exceeding the half-word size field of 9999. That demands
TRUNC(BIN) for application to work.  
- i'm currently on a Y2K project and cobol/mvs has reduced coding and
testing considerably for y2k windowing. 
david
```

###### ↳ ↳ ↳ Re: COBOL II compile options for MVS

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<73a450$597@dfw-ixnews6.ix.netcom.com>`
- **References:** `<736tg2$plv@chronicle.concentric.net> <73794b$15m@dfw-ixnews4.ix.netcom.com> <3657C39C.1126375D@worldnet.att.net> <3659758e.12579586@nntp.ix.netcom.com>`

```

David wrote in message
  <much snippage>
>- TRUNC(OPT) is great if you are managing all your data fields to fit
>within the pic clause. for example, I see CICS applications with data
>areas exceeding the half-word size field of 9999. That demands
>TRUNC(BIN) for application to work.

  <more snippage>

IBM has indicated that they HOPE to improve the performance of TRUNC(BIN) in
'99 - but at this time, it really REALLY is a poor performer.  There are two
types of problems that you can have with TRUNC(OPT):

1) Application binary fields that you move "large" numbers to (larger than
the PIC clause).  If this is the case, I really think you have an
application logic problem and should fix your program.  (I am not saying
that these don't exist, but from what I have heard, they really are NOT that
common - and can be fixed)

2) CICS used/controlled binary fields (fields that are either used or
updated by CICS in EXEC CICS statements).  From what IBM has said (and
researched), it really seems as if these fields do not (in the normal course
of applications) get invalid data (data larger than the PIC clause).  This
isn't to say it doesn't happen, but that it rather that it doesn't happen
with sufficient frequency to warrant the overhead of using TRUNC(BIN) for
all applications.

Bottom-Line:  IBM now recommends the use of TRUNC(OPT) for CICS (and also
DB2) applications  - as the default - but to keep your eyes out for specific
programs that need TRUNC(BIN).  And to even try to re-code those
applications when possible to still keep with TRUNC(OPT).
```

###### ↳ ↳ ↳ Re: COBOL II compile options for MVS

_(reply depth: 4)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 1998-11-23T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3658E378.92CFF071@worldnet.att.net>`
- **References:** `<736tg2$plv@chronicle.concentric.net> <73794b$15m@dfw-ixnews4.ix.netcom.com> <3657C39C.1126375D@worldnet.att.net> <3659758e.12579586@nntp.ix.netcom.com>`

```
David wrote:
> 
> On 22 Nov 1998 07:53:57 GMT, Arnold Trembley
…[3 more quoted lines elided]…
> >there.

For readers of comp.lang.cobol, I heartily recommend David Shelby Kirk's
book "MVS COBOL II, Power Programmer's Desk Reference".  I also have his
book on COBOL/370 at the office, but the exact title escapes me at the
moment.  I learned a lot from his books.

> 
> just a few comments:
…[3 more quoted lines elided]…
> years. but -- cobol ii has no inherent y2k problems of its own.

That's certainly true.  I've executed both the OS/VS COBOL and VS COBOL
II compilers in a time machine LPAR.  OS/VS COBOL thinks the year is
1900!  I've even had e-mail from people who intend to patch the compiler
to force it to say 2000 for compile date.

The old compilers don't break, but neither one has any native function
to return current date with four digit year.

> - RENT is still good for cobol ii to ensure the 31-bit addressability.
> removes virtual storage constraints for reduced runtime costs

I can't really disagree with that.  Most batch COBOL programs will run
fine with NORENT.  Very few will actually need RENT.  

> - NUMPROC(MIGVS) is my preference as it's more efficient by far than
> NOPFD and S0C7's are equivalent to os/vs cobol.

I agree NUMPROC(MIG) is more efficient than NUMPROC(NOPFD).  I use
NUMPROC(NOPFD) all the time because I have seen programs that will abend
with S0C7 with MIG, but will run fine and produce correct results with
NOPFD.  In this case I'm willing to trade a very slight decrease in
calculation speed for additional sign fixup.

> - TRUNC(OPT) is great if you are managing all your data fields to fit
> within the pic clause. for example, I see CICS applications with data
> areas exceeding the half-word size field of 9999. That demands
> TRUNC(BIN) for application to work.

Here I've taken the opposite position.  TRUNC(BIN) is very inefficient
compared to TRUNC(OPT), and I haven't found any benefit or need to use
TRUNC(BIN).  So I've chosen to use TRUNC(OPT).  That doesn't necessarily
mean it's the best choice for your situation.  Reasonable people do
disagree about this.

> - i'm currently on a Y2K project and cobol/mvs has reduced coding and
> testing considerably for y2k windowing.
> david

There's no question that COBOL/MVS has much better support for date
handling than COBOL II.  My problem was that my shop could not convert
to LE due to conflicts with a third party database that would not run
with LE.  So we had to do our Y2K code changes in COBOL II (and some
departments had never converted from OS/VS COBOL).  When you are
migrating from OS/VS COBOL, I think the pain of source conversion is
about the same whether you're going to COBOL II or directly to
COBOL/MVS.  It's much easier to move from COBOL II to COBOL/MVS than
from OS/VS COBOL to COBOL/MVS.

COBOL/MVS is where you want to be.

Again, if you can find David's books on COBOL, they are well worth your
money.
```

#### ↳ Re: COBOL II compile options for MVS

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981121173738.24149.00000748@ng132.aol.com>`
- **References:** `<736tg2$plv@chronicle.concentric.net>`

```

You _are_ getting the size difference from the RES.  If you like that, stay
with it. Independently, the later compilers (after COBOL II), will virtually
compel RES.

However, you should compile a larger portion of your system, before concluding
that you have a viable overall strategy.  

The use of combinations of CALL 'literal' and CALL YOUR-NAME syntax can collide
with your generalized preference on the DYNAM/NODYNAM option.

Decisions about RES/NORES and RENT/NORENT can compel DYNAM, which can make the
compiler bark when it sees programs with certain combinations of
literal/data-name CALLS.

A critical issue here is the shop date routines.  Some shops will try to get
you to statically link date routines, so that emmergency fixes to particular
programs will not put all other programs in jeopardy.  The static link will
necessitate a static call and NODYNAM, which may not work with the (NO)RES
(NO)RENT combination you otherwise might favor.

Be sure to survey lots of code, and try the obvious combinations of modules
with literal/data-name CALLs.

You may need alternative PROCs, and a little more documentation for batch
application projects, then in the past.

Generally RES is a good idea for the future with LE.  It can compel a policy
change in some shops.  It is harder to generate your system with static links
(not impossible, just harder). This tiny technical area causes lots of
discussion. The basic reason is that the compiler technology and its supporting
runtime modules are not from a static link culture. The discussions really
involve a change in mind set. That transition can cause a project to loose time
in discussions. 

Best Wishes,






Robert Rayhawk
RKRayhawk@aol.com
```

##### ↳ ↳ Re: COBOL II compile options for MVS

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<737fk0$99h@sjx-ixn5.ix.netcom.com>`
- **References:** `<736tg2$plv@chronicle.concentric.net> <19981121173738.24149.00000748@ng132.aol.com>`

```

RKRayhawk wrote in message
  <snip>
>
>Decisions about RES/NORES and RENT/NORENT can compel DYNAM, which can make
the
>compiler bark when it sees programs with certain combinations of
>literal/data-name CALLS.
>
  <more snip>

This is incorrect (or at best misleading).  What you chose for RES/NORES or
RENT/NORENT will *never* force you to use DYNAM.

The reverse, however, is true.  When you chose DYNAM, then you are forced to
use RES.
```

#### ↳ Re: COBOL II compile options for MVS

- **From:** WOB@my-dejanews.com
- **Date:** 1998-11-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<737jn1$js1$1@nnrp1.dejanews.com>`
- **References:** `<736tg2$plv@chronicle.concentric.net>`

```
In article <736tg2$plv@chronicle.concentric.net>,
  "Gregory Desyatnik" <grigory@concentric.net> wrote:
> The company I work for is trying to standardize on compile procedures for
> Y2K project.  One would expect they should already have something in place
…[17 more quoted lines elided]…
>

Be wary of the TRUNC option, which affects BINARY (COMP) data. If you're
unsure of which subset to use, TRUNC(BIN) will save you from early morning
pages, although it brutally inefficient.
```

#### ↳ Re: COBOL II compile options for MVS

- **From:** William Lynch <wblynch@att.net>
- **Date:** 1998-11-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36576107.3DE05B54@att.net>`
- **References:** `<736tg2$plv@chronicle.concentric.net>`

```
Gregory Desyatnik wrote:
> 
> The company I work for is trying to standardize on compile procedures for
…[8 more quoted lines elided]…
> calls to COBOL II system modules).

You're a little confused here. The RENT option makes the load module
smaller because the memory for WORKING-STORAGE is obtained at run time,
so the load module contains only enough data to initialize
WORKING-STORAGE, instead of all the empty areas defined but which don't
have VALUE clauses. This has no bearing on the load module's RMODE
(residence mode). If RMODE is "ANY" the program can (and will) be loaded
above the 16MB line; otherwise not.

I didn't see any real advantage to running our batch programs above the
line (we had no virtual storage constraints in batch), but I did set our
compile procedures to specify RENT to save the loadlib space (some
programs were *much* smaller, e.g., x'10000' bytes).

I'm not clear on the relationship between the RENT & RES options, but
it's pretty standard to compile batch COBOL programs, of any flavour,
with the DYNAM option. Email back if you're not sure why.

Bill Lynch
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
