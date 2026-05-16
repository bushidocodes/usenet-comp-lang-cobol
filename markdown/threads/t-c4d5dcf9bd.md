[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Report Writer

_28 messages · 17 participants · 1998-10_

---

### Report Writer

- **From:** "Dr���. Emilia Coelho" <ecoelho@edinfor.pt>
- **Date:** 1998-10-09T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<361E1AFB.3378D75A@edinfor.pt>`

```
       Does anyone know if IBM supports Report Writer for COBOL for
OS/390?
      Thanks very much for any help.

                                            Emilia Coelho
```

#### ↳ Re: Report Writer

- **From:** theodp@aol.com (Theo DP)
- **Date:** 1998-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981011135516.17653.00006790@ng31.aol.com>`
- **References:** `<361E1AFB.3378D75A@edinfor.pt>`

```

><HTML><PRE>Subject: Report Writer
>From: "Drï¿½. Emilia Coelho" <ecoelho@edinfor.pt>
…[9 more quoted lines elided]…
></PRE></HTML>

Report Writer was dropped with the introduction of COBOL II.
```

##### ↳ ↳ Re: Report Writer

- **From:** Rex Widmer <rwidmer@sound.net>
- **Date:** 1998-10-11T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36211A12.6A72@sound.net>`
- **References:** `<361E1AFB.3378D75A@edinfor.pt> <19981011135516.17653.00006790@ng31.aol.com>`

```
Yes REPORT WRITER was dropped from the compiler with the introduction of
VS COBOL II in 1984 or so, but the SPC Systems REPORT WRITER PRECOMPILER
was released with an IBM part number in about 1985, and supports all of
the VS COBOL II, COBOL/370, COBOL for MVS and VM and COBOL for OS/390
and VM compilers.  This can be used as either a transparent compiler
shell or as a "get rid of report writer syntax, give me just equivalent
COBOL" tool.

Check IBMLINK or your IBM rep for details.

The pre-compiler works quite well
Theo DP wrote:
> 
> ><HTML><PRE>Subject: Report Writer
…[12 more quoted lines elided]…
> Report Writer was dropped with the introduction of COBOL II.
```

###### ↳ ↳ ↳ Re: Report Writer

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36222169.0@news2.uswest.net>`
- **References:** `<361E1AFB.3378D75A@edinfor.pt> <19981011135516.17653.00006790@ng31.aol.com> <36211A12.6A72@sound.net>`

```
Good thing Report Writer will come back in the next standard.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 4)_

- **From:** scomstock@aol.com (S Comstock)
- **Date:** 1998-10-12T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981012130155.16096.00000095@ng107.aol.com>`
- **References:** `<36222169.0@news2.uswest.net>`

```

Chris Osborne writes ...

>Good thing Report Writer will come back in the next standard.

Well, that's in the eye of the beholder, I guess. I personally not only never
liked it, I despised it. But, hey, this is from a guy who's favorite language
is Assembler.

Cheers,


Steve Comstock
Telephone: 303-393-8716
www.trainersfriend.com
email: steve@trainersfriend.com
256-B S. Monaco Parkway
Denver, CO 80224
USA
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 5)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36236210.0@news3.uswest.net>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com>`

```
S Comstock wrote in message <19981012130155.16096.00000095@ng107.aol.com>...
>
>Chris Osborne writes ...
…[3 more quoted lines elided]…
>Well, that's in the eye of the beholder, I guess. I personally not only
never
>liked it, I despised it. But, hey, this is from a guy who's favorite
language
>is Assembler.
>
>Cheers,
>
<snip>

That practically begs me to ask you to detail the nature of your dislike.
So I'll ask: Why do you dislike Report Writer?
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 6)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36237636.B27716@home.com>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net>`

```
> 
> That practically begs me to ask you to detail the nature of your dislike.
> So I'll ask: Why do you dislike Report Writer?

I also dislike Report Writer.  I think this is mainly because
programmers don't think about it the same way as they do the rest of
Cobol IO.  It is almost a different language.  Why not use a different
language optimized for that task?

Maintenance programmers have to know standard COBOL.  But they are often
unfamiliar with Report Writer.  This unfamiliarity causes problems.  So
why not standardize on doing output for reports the same way all of the
time - using the same type of logic used for all the rest of the output!
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7004dv$hhh@sjx-ixn6.ix.netcom.com>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com>`

```

Howard Brazee wrote in message <36237636.B27716@home.com>...
>>
>> That practically begs me to ask you to detail the nature of your dislike.
…[10 more quoted lines elided]…
>time - using the same type of logic used for all the rest of the output!

As a strong proponent of Report Writer, I do want to add my understanding of
WHY so many programmers (and entire programming staffs) HATE report writer.
In my opinion (at least for IBM mainframe shops), it is because:

1) The original OS/VS COBOL (ANS COBOL?) implementation was quite "buggy"

2) The original documentation was almost entirely incomprehensible

3) The original compiler interface would give you a compiler error for the
1st error - and then stop checking.  This meant repeated compiles (in the
days of punched decks - no less) to get a clean compile.

4) There were originally almost no "debugging" tools that were targeted at
report writer code.

This, along with the above mentioned fact that training of IBM mainframe
COBOL programmers almost always omitted report writer, made this a little
used, little understood, and little desired feature.  Furthermore, this
became a "viscous circle" as new programmers came along, there were no
experienced programmers to help them with report writer, so new programmers
didn't learn it and thought it must be "bad" and/or "hard".

All of these technical problems SHOULD be fixed by now - but (like COBOL
itself among "academics") report writer has such a poor reputation that few
COBOL programmers look at its power and usefulness.

I will be MOST happy when it becomes required (and enhanced) via the
Standard and more and more new COBOL programmers become familiar with it.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-10-13T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<r5QU1.329$DN2.3456214@storm.twcol.com>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com>`

```
I was taught report writer in college and I hated learning it, using it and
maintaining it. I have worked in many shops and none use report writer. The
same code in COBOL can be written in a report writing utility, such as
EZtrieve, Dyl280, and even DF/SyncSort in just a few lines. Building it in
to COBOL will simply make already long and complicated programs longer and
even more complicated.
Leave report writing to a language built for it.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3624b66d.0@news2.uswest.net>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com> <r5QU1.329$DN2.3456214@storm.twcol.com>`

```

Jeff wrote in message ...
>I was taught report writer in college and I hated learning it, using it and
>maintaining it. I have worked in many shops and none use report writer. The
…[6 more quoted lines elided]…
>

Syncsort's Sortwriter facility can be very powerful, but has it's own
limitations.   One of the biggest is internal maintenance.  Just looking at
any type of Syncsort instruction tells you nothing about the data, only
where Syncsort itself has been told to look for that data.  There is no way
to tell what any field is (at least not in the version we have).

EZtrieve is a massive CPU hog (but not as bad as SAS), and I haven't seen
Dyl280.  I'll admit SAS is even faster to code than report writer, and from
what I've seen of EZtrieve, it is also faster to code in.

I'm going to have to say that I find Report Writer far closer to COBOL that
either EZtrieve or SAS.  Both of these languages require a higher learning
curve than Report Writer, especially SAS (okay, writing a PROC PRINT
statement to do basic printouts is a breeze, but learning enough about SAS
to reliably control everything . . ., well, I did it on my own, so I had a
tough time of it).

There are tons of places that use ordinary COBOL to do report generation,
and do not have report writing tools to help them out.  When Report Writer
becomes standard again (and hoping that it won't be as buggy as the
original; though that's a compiler vendor issue), everyone who goes to the
new COBOL (admitting that there will be many who won't go to it) will have a
report writing tool.

Although I'm getting into the issue of modularization of code, using Report
Writer directly in your COBOL program allows you to generate report details
lines in the same read-to-write pass that will encompass all other
processing.  If you finish processing a file, and then start a separate
report writing package, a completely new set of I/O is required.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 10)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3624C0CF.FD35CF6@home.com>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com> <r5QU1.329$DN2.3456214@storm.twcol.com> <3624b66d.0@news2.uswest.net>`

```
It was easy to learn EZtrieve without being taught.  I failed to learn
SAS without being taught.  I don't bother with Report Writer because as
long as I'm using COBOL, I can write just as quickly with standard
COBOL, and everybody who knows it will be able to maintain it.  Standard
COBOL is easy.  Report Writer may be slightly easier, but not
sufficiently.


> I'm going to have to say that I find Report Writer far closer to COBOL that
> either EZtrieve or SAS.  Both of these languages require a higher learning
…[3 more quoted lines elided]…
> tough time of it).
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** stevewie@apk.net (SkippyPB)
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3627c2db.6771817@news.apk.net>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com> <r5QU1.329$DN2.3456214@storm.twcol.com>`

```
On Tue, 13 Oct 1998 18:01:02 -0400, "Jeff" <a@a.com> enlightened us:

>I was taught report writer in college and I hated learning it, using it and
>maintaining it. I have worked in many shops and none use report writer. The
…[5 more quoted lines elided]…
>

I had the same experience.  That is, I learned it in college, but I've
never seen it used outside of school.  I didn't hate it, but I
certainly concur that using Eztrieve or Dyl280 is much easier if all
you want to do is read a file and report its contents.

Regards,

          ////
         (o o)
-oOO--(_)--OOo-
Todays tip to annoy people:  Practice making fax and modem noises.
 Steve
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 10)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3624D515.1E881E75@home.com>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com> <r5QU1.329$DN2.3456214@storm.twcol.com> <3627c2db.6771817@news.apk.net>`

```
What's interesting is that there are lots of shops which have standards
which actively discourage or even ban COBOL sorts.  I understand the
extract/sort/report methodology and approve of it, and understand the
problems of integrating too many functions together.  That's part of the
reason I am a Cobol apologist against the OO crowd.  But COBOL sorts
don't seem complicated - maybe they use the same arguments I have
against Report Writer.


> I had the same experience.  That is, I learned it in college, but I've
> never seen it used outside of school.  I didn't hate it, but I
> certainly concur that using Eztrieve or Dyl280 is much easier if all
> you want to do is read a file and report its contents.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** B W Spoor <bwspoor@fridaycs.co.uk>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3624E032.312FE8E8@fridaycs.co.uk>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com> <r5QU1.329$DN2.3456214@storm.twcol.com> <3627c2db.6771817@news.apk.net> <3624D515.1E881E75@home.com>`

```
Howard Brazee wrote:

> What's interesting is that there are lots of shops which have
> standards
…[13 more quoted lines elided]…
> > you want to do is read a file and report its contents.

I make quite extensive use of both the COBOL Sort verb and Report Writer
for print/report programs. The in-house standard is to use Report Writer
for ALL reports.

Once you get the hang of it, it is very quick and easy to create a
report program, complete with headings, footings, sub-totals & totals in
a very few lines of procedure division. The Report Section does take a
bit of writing, but IMHO far less than is required in the Procedure
Division to handle page breaks, control breaks, totals etc.

I found the manual very hard to understand (and I am far from a novice
programmer - 25 years this summer just past, mainly Cobol), but
perservered and have now been using it for about 8 years - I wouldn't
like to write a report without it.

It does have it's drawbacks and can be a little inflexible, but most
things can be handled with a little ingenuity, similar to writing it the
'standard way' - you just need to look at it differently, basically from
the data/output required aspect rather than from how to process the
data.

Combined with the SORT verb, it is extremely powerful - Extract, Sort
Report. I find that I can create short, easily readable code for reports
that require data manipulation.

I can't answer for the relative effeciency/inefficiency of the internal
sort and report writer,  but I believe that with the power of the target
machines, speed & maintainabilty of code is generally more important.

There will be exceptions to this, I remember years ago testing a
report/file rebuild where we estinmated it's run time to be 4 days from
extrapolating the test data - this needed to run as part of the
overnight batch in one night - it had to be rewritten for run time
rather than nice code.

Brian
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** scottp4.removethis@ibm.net (Scott Peterson)
- **Date:** 1998-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36255fb1.14607736@news3.ibm.net>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com> <r5QU1.329$DN2.3456214@storm.twcol.com> <3627c2db.6771817@news.apk.net> <3624D515.1E881E75@home.com>`

```
Howard Brazee <NOSPAMbrazee@home.com> wrote:

>What's interesting is that there are lots of shops which have standards
>which actively discourage or even ban COBOL sorts.  I understand the
>extract/sort/report methodology and approve of it, and understand the
>problems of integrating too many functions together. 

Most of the COBOL sort standards like that date back to VS/COBOL Even
with the using/giving options it was much slower than a JCL sort. 

What most people missed was that you could write a JCL SORT with
e15/e35 exits written in COBOL to handle the extract and reporting and
produce the needed output with extremely simple COBOL routines.

			Scott Peterson
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 12)_

- **From:** "Chris Osborne" <chris_n_osborne@yahoo.com>
- **Date:** 1998-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36260420.0@news3.uswest.net>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com> <7004dv$hhh@sjx-ixn6.ix.netcom.com> <r5QU1.329$DN2.3456214@storm.twcol.com> <3627c2db.6771817@news.apk.net> <3624D515.1E881E75@home.com> <36255fb1.14607736@news3.ibm.net>`

```
Scott,

I looked up the MODS statement in Syncsort.  I think I'll try it out.

Scott Peterson wrote in message <36255fb1.14607736@news3.ibm.net>...
>Howard Brazee <NOSPAMbrazee@home.com> wrote:
>
…[12 more quoted lines elided]…
> Scott Peterson
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298286.67869.7697@kcbbs.gen.nz>`
- **References:** `<7004dv$hhh@sjx-ixn6.ix.netcom.com>`

```
In message <<7004dv$hhh@sjx-ixn6.ix.netcom.com>> "William M. Klein" <wmklein@ix.netcom.com> writes:

> 
> All of these technical problems SHOULD be fixed by now - but (like COBOL
…[4 more quoted lines elided]…
> Standard and more and more new COBOL programmers become familiar with it.

Nah, it is too much like an RPG thing to any use to real
programmers       ;-)
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 7)_

- **From:** riplin@kcbbs.gen.nz (Richard Plinston)
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3298286.67086.6935@kcbbs.gen.nz>`
- **References:** `<36237636.B27716@home.com>`

```
In message <<36237636.B27716@home.com>> Howard Brazee <NOSPAMbrazee@home.com> writes:
> > That practically begs me to ask you to detail the nature of your dislike.
> > So I'll ask: Why do you dislike Report Writer?
…[9 more quoted lines elided]…
> time - using the same type of logic used for all the rest of the output!

I dislike Report Writer for an entirely different reason,
it is still code.  If the user wants a small change in 
the report it still has to be recoded and recompiled.
Even report generators that spit out Cobol source need
to have compilations.  This removes the user from 
control of the process.

I developed my own reporting program in Cobol that
reads a script and outputs a report based on that
script.  It has limits but will do two file (master/
transaction eg) and 4 levels of control breaks, will
output in the order of any field(s), has 20 selelection
control.

Or use Chrystal Reports.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<df9V1.695$DN2.4126254@storm.twcol.com>`
- **References:** `<36237636.B27716@home.com> <3298286.67086.6935@kcbbs.gen.nz>`

```
>I dislike Report Writer for an entirely different reason,
>it is still code.  If the user wants a small change in
…[3 more quoted lines elided]…
>control of the process.


I whole heartedly agree. When users want small changes you may have to
recompile the entire program and continue to test. Using soemthing akin to
your program such as DF/Syncsort, EZtrieve, or DYL280 you simplify the
entire process. Users rarely have any comprehension as to what their changes
are going to do to the entire report process. They ask for small changes and
those small changes take days to implement in COBOL: sort sequences, adding
fields to a report, or even adding "PAGE 1 OF 20". These changes look simple
to the average human being, but imagine if it took you a week to develop the
COBOL report and now you have to rexamine the entire process to figure out
how to implement what seems like a simple change.

EXTRACT
FILTER
SORT
REPORT

I will believe it is the only way until someone proves there is an easier
way.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<703hff$odr$1@news.igs.net>`
- **References:** `<36237636.B27716@home.com> <3298286.67086.6935@kcbbs.gen.nz>`

```

Richard Plinston wrote in message <3298286.67086.6935@kcbbs.gen.nz>...

>I developed my own reporting program in Cobol that
>reads a script and outputs a report based on that
…[3 more quoted lines elided]…
>control.

In my current conversion, the existing reports will be the last.
The approach for me, in the future, will to simply export collections
of data into Excel, and let the user do whatever they want with it.
I plan to supply a couple of standard templates for the basics,
but that will be about it.  Even something like a customer listing
can be done that way for anything under 3 or 4 thousand customers.
100 megabytes of memory does make a difference.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** theodp@aol.com (Theo DP)
- **Date:** 1998-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19981015020915.08985.00000912@ng71.aol.com>`
- **References:** `<703hff$odr$1@news.igs.net>`

```
><HTML><PRE>Subject: Re: Report Writer
>From: "Donald Tees" <donald@willmack.com>
…[23 more quoted lines elided]…
></PRE></HTML>

Unfortunately, deciding to go with Excel virtually guarantees your reports will
soon exceed the 16K row limit.   :-)
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 10)_

- **From:** "Donald Tees" <donald@willmack.com>
- **Date:** 1998-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<704p1p$lbd$1@news.igs.net>`
- **References:** `<703hff$odr$1@news.igs.net> <19981015020915.08985.00000912@ng71.aol.com>`

```

Theo DP wrote in message <19981015020915.08985.00000912@ng71.aol.com>...

>Unfortunately, deciding to go with Excel virtually guarantees your reports
will
>soon exceed the 16K row limit.   :-)

Murphy's law? ;<)
The type of thing I do lends itself to the approach well, though
I will grant it would not work for numerous systems. The reports
on my systems seldom go over a dozen pages.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 11)_

- **From:** "Rick Smith" <ricksmith@aiservices.com>
- **Date:** 1998-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D2oV1.63$SQ4.1077313@news1.atlantic.net>`
- **References:** `<703hff$odr$1@news.igs.net> <19981015020915.08985.00000912@ng71.aol.com> <704p1p$lbd$1@news.igs.net>`

```

Donald Tees wrote in message <704p1p$lbd$1@news.igs.net>...
>
>Theo DP wrote in message <19981015020915.08985.00000912@ng71.aol.com>...
…[9 more quoted lines elided]…
>
Finagle's Law! Unless the choice of Excel is wrong!

Finagle's Law: <http://www.netmeg.net/jargon/terms/f/finagle_s_law.html>

Murphy's Law: <http://www.netmeg.net/jargon/terms/m/murphy_s_law.html>
-------------------------------
Rick Smith
e-mail: < ricksmith@aiservices.com >
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "Jeff" <a@a.com>
- **Date:** 1998-10-14T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<AA2W1.84$IF6.940659@storm.twcol.com>`
- **References:** `<36237636.B27716@home.com> <3298286.67086.6935@kcbbs.gen.nz>`

```
>I dislike Report Writer for an entirely different reason,
>it is still code.  If the user wants a small change in
…[3 more quoted lines elided]…
>control of the process.


I whole heartedly agree. When users want small changes you may have to
recompile the entire program and continue to test. Using soemthing akin to
your program such as DF/Syncsort, EZtrieve, or DYL280 you simplify the
entire process. Users rarely have any comprehension as to what their changes
are going to do to the entire report process. They ask for small changes and
those small changes take days to implement in COBOL: sort sequences, adding
fields to a report, or even adding "PAGE 1 OF 20". These changes look simple
to the average human being, but imagine if it took you a week to develop the
COBOL report and now you have to rexamine the entire process to figure out
how to implement what seems like a simple change.

EXTRACT
FILTER
SORT
REPORT

I will believe it is the only way until someone proves there is an easier
way.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** Howard Brazee <NOSPAMbrazee@home.com>
- **Date:** 1998-10-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<362B65D0.401B156D@home.com>`
- **References:** `<36237636.B27716@home.com> <3298286.67086.6935@kcbbs.gen.nz> <AA2W1.84$IF6.940659@storm.twcol.com>`

```
It is awful nice to use CA-SORT to do the first 3 steps for you though.

> EXTRACT
> FILTER
…[4 more quoted lines elided]…
> way.
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 9)_

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 1998-10-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<57h6YLAEzNL2EwNw@ld50macca.demon.co.uk>`
- **References:** `<36237636.B27716@home.com> <3298286.67086.6935@kcbbs.gen.nz> <AA2W1.84$IF6.940659@storm.twcol.com>`

```
If you don't tell your clients how long a change is going to take then
how can you expect them to realise the impact upon you of their
'trivial' changes?

I had this problem and took pains to explain how long changes were going
to take and cost. Eventually the users apologised for asking for complex
changes which only took me 5 minutes to do. Talk to them (if you are
allowed to do so).

In article <AA2W1.84$IF6.940659@storm.twcol.com>, Jeff <a@a.com> writes
>>I dislike Report Writer for an entirely different reason,
>>it is still code.  If the user wants a small change in
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 8)_

- **From:** "Russell Strope" <RussStrope@worldnet.att.net>
- **Date:** 1998-10-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<01bdfa39$4b7b65e0$15cf430c@RussStrope>`
- **References:** `<36237636.B27716@home.com> <3298286.67086.6935@kcbbs.gen.nz>`

```
I beleive in keeping your programs simple and minimizing the number of
functions that are being performed.  I do not recommend having a program
perform a bunch of tasks and then do an internal sort and have report
writer create a report.   It is tough enough to find good programmers, let
alone finding ones who know report writer.

I have my shop use a report generator, Easytreive, to produce all reports. 
Even rookie programmers can produce complex control break reports in a day.
 They enjoy using it and do not even want to code report logic in a
program.  Easytreive is just not limited to report generation. You can also
create programs to update sequential, VSAM, and DB2 and do it in a fraction
of the time it would take in cobol. 

I even have the users sit down with the programmers to help create the
reports and the breaking.  This utility allows you move fields around,
alter the control breaks with little effort.  The programs can run as
instream sysin so you don't have to wait for a compile to show the results
to the user sitting right there.  TRY THAT IN COBOL!!!!!

UTILITIES SAVE YOU TIME, EFFORT AND MONEY....USE THEM TO YOUR
ADVANTAGE!!!!!!!!!!!!!!!!!!!!!!!!
```

###### ↳ ↳ ↳ Re: Report Writer

_(reply depth: 7)_

- **From:** as999@torfree.net (Adrian Boldan)
- **Date:** 1998-10-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<F0w260.4nB.0.bloor@torfree.net>`
- **References:** `<36222169.0@news2.uswest.net> <19981012130155.16096.00000095@ng107.aol.com> <36236210.0@news3.uswest.net> <36237636.B27716@home.com>`

```
We are converting to COBOL II. It either doesn't have Report writer, or 
this shop doesn't want to buy it. So... together with the Y2k conversion 
we rewrite about 20 programs to eliminate the Report writer. 
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
