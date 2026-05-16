[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# SAS sucks

_18 messages · 11 participants · 2000-02 → 2000-03_

---

### Re: SAS sucks

- **From:** hancock4@bbs.cpcn.com (Lisa nor Jeff)
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89fcen$q3f@netaxs.com>`

```
SAS gets a bad rap for performance primarily because
managers think it can be written by anybody, not necessarily a
professional SAS programmer..


Therein lies a big problem with SAS right there.  Everybody knows
COBOL, and most programmers have lots of experience in it.  The
advantage of COBOL is that it's a universal language.

Like it or not, SAS is a specialized language.  Not everyone
knows it, certainly not to the level you speak of to use it
properly.  Unless an organization standardizes on SAS and trains
everyone in it _thoroughly_, the organization won't develop the
expertise.



Regarding your comment of coding complex routines, my point is
that if coding is required, you might as well code in COBOL
rather than SAS.
```

#### ↳ Re: SAS sucks

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2000-02-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<D7Ru4.4503$JL3.1968267@news4.mia>`
- **References:** `<89fcen$q3f@netaxs.com>`

```
Lisa nor Jeff wrote:
>SAS gets a bad rap for performance primarily because
>managers think it can be written by anybody, not necessarily a
>professional SAS programmer..

Is it not true that SAS is marketed as a tool that can be used by
non professional programmers?  If SAS is marketed that way, then is
it not fair to assess SAS in that environment? :-)
```

##### ↳ ↳ Re: SAS sucks

- **From:** theodp@aol.com (Theo DP)
- **Date:** 2000-03-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000229212636.05847.00001592@ng-fa1.aol.com>`
- **References:** `<D7Ru4.4503$JL3.1968267@news4.mia>`

```
>Subject: Re: SAS sucks
>From: "Judson McClendon" judmc@bellsouth.net 
…[18 more quoted lines elided]…
>

Unfortunately, as many companies have found out via lawsuits (e.g., McDonald's
coffee), there are limits to genius, but seemingly none on stupidity...

Even among software "professionals", I've seen some doozies that have been
written off as SAS performance problems:

1. One VP dropped SAS after complaining about performance problems with their
datamart, the design of which (by non-SAS programmers) included huge data base
tables (millions of rows) with thousands of variables per table that were
rebuilt from scratch every single time a report request was made...

2. A consulting company recommended that SAS be dropped (for performance
reasons of course!) after programmers, ignoring hundreds of warning messages,
deleted all of the client's source code and complained that the system couldn't
magically regenerate the source code (because they also discovered they failed
to make any backups)...

3. A Big Six firm recommended that a major insurance company drop SAS in favor
of an Oracle, Peoplesoft, Hyperion, Essbase, NT, Unix combination to speed up
turnaround...Scores of millions of  dollars later, reports that took an hour
with SAS could now be produced in five days with the new "state of the art"
system...  

4. A former IT VP expressed his outrage to me after SAS Institute declined to
jump to his demands for free tuning of his (self-developed) marketing reporting
system. I had to fight back the laughter when he showed me the "outrageous"
letter he had received from the (too easy going to a fault IMHO) SAS Technical
Suport folks - "Dear Sir...we are afraid that we will be unable to respond to
your demand for free consulting services...However, we did notice that you have
defined more than 7,000 separate variables (e.g., AK9801,
AK9802,...AK9912...WY9801...WY9912..) in your program...If your budget cannot
support training or consulting services at this time, perhaps you could have
someone in your IT department take some time to demonstrate the use of tables
or arrays..."... 

In most cases (there are horrific COBOL implementations as well!), SAS will
consume more CPU conservative than a comparable COBOL-based solution. However,
IMHO it will be developed much faster, be much easier to maintain, and have a
much better chance of being correct. In the absence of an off-the-wall internal
chargeback system (unfortuanately, there are way still too many!), the CPU
requirements should not pose a real obstacle for most business systems.

HTH
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** dgrampsas@aol.com (DGrampsas)
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000314231336.01692.00002557@ng-bg1.aol.com>`
- **References:** `<20000229212636.05847.00001592@ng-fa1.aol.com>`

```
Recently, a COBOL programmer in my company decided it would be wise to convert
a SAS program that processes masterfile data into an equivalent COBOL program.
Keep in mind that the SAS program produced one-way frequency tables  and was
only 15 pages or so. He completed the COBOL program (several hundred lines
long) and proclaimed, "I just saved the company $3000 dollars in processing
costs!" He was asked to adapt his COBOL program to produce two-way frequencies
and promptly dusted off the SAS program and abandoned his COBOL program.


Sometimes CPU throughput isn't everything...
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 4)_

- **From:** "Brian Maher" <maher@progress.com>
- **Date:** 2000-03-15T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8ansvf$7jq$1@progress.progress.com>`
- **References:** `<20000229212636.05847.00001592@ng-fa1.aol.com> <20000314231336.01692.00002557@ng-bg1.aol.com>`

```
I have to add a comment to this thread.  Years ago I wrote SAS in a bank
down south
and the other developers were complaining that a particular program I wrote
used 4,096K
of memory and sucked down around 80% of the CPU cycles of an IBM 3090.  They
wanted
us to use an Easytrieve program that they wrote that used only 200K and
around 2 to 3% of
the CPU resources of the machine.  We ended up taking the argument to the
head of Technical
Services (i.e. the guy who managed the mainframe).  I'll never forget his
response after looking
over the job logs for both programs.  His response was "the SAS program ran
in 5 minutes & the
Easytrieve program ran for 1 hour.  I'll take the program that sits in the
machine for the smallest
amount of time anyday & I don't give a darn how much memory or CPU the SAS
program uses
because it still is more efficient for overall thru-put than the Easytrieve
program".

The Easytrieve programmers were not happy.
```

##### ↳ ↳ Re: SAS sucks

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38BDF16C.36E09D8A@mediaone.net>`
- **References:** `<89fcen$q3f@netaxs.com> <D7Ru4.4503$JL3.1968267@news4.mia>`

```
Judson,

It is true for those products that SI supplies with GUI, for instance,
SAS/Insight. They are marketed in about the same way as a spreadsheet or
word processor would be marketed. In such cases, the emphasis is
naturally off procedural programming. However, SI does not market Base
SAS, SAS Language, and Macro Language this way. This is serious stuff
intended for serious programmers, and SI keeps improving, streamlining,
and enriching the language. The current Version 8 has received a myriad
of enhancements. For COBOL NG folks touching SAS sporadically, the most
notable ones would perhaps be:

* The limit on the identifier name is SAS has been raised from 8 to 32.
* The maximum length of a character variable has been expanded from 200
to 32767.
* About 50 new functions and call routines have been added.
* ODS (Output Delivery System) has been introduced. In a nutshell, now,
instead of directing a reporting output straight to a print file, one can
create an "output object", edit it at will, and spit the object to a
print file, RTF, HTML, etc.

Generally, it appears to me that even if SI did market SAS as a tool
"even a non-programmer could use" it would be as poor an excuse for
writing crappy SAS programs as for writing horrible COBOL code just
because there is a book offering one to teach himself COBOL in 24 hours.
Such claims, as every rational person of course understands, are simply
marketing (and fully legitimate) means to attract attention, while
becoming either professional COBOL or SAS programmer demands plenty of
hard work, dedication, and practical coding. To become a "guru", one
should add obsession with the subject and a lot of insatiable curiosity.

Kind regards,
=====================
Paul M. Dorfman
Jacksonville, Fl
=====================

Judson McClendon wrote:

> Lisa nor Jeff wrote:
> >SAS gets a bad rap for performance primarily because
…[10 more quoted lines elided]…
> whoever believes in Him should not perish but have everlasting life."
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38BE7435.D1593973@cusys.edu>`
- **References:** `<89fcen$q3f@netaxs.com> <D7Ru4.4503$JL3.1968267@news4.mia> <38BDF16C.36E09D8A@mediaone.net>`

```
In our shop, we have SAS as option 2 on our TSO menu.  As far as I know, the
only thing people have done with it here is to accidentally go into
interactive TSO when they meant to be in ISPF option 2, then try to figure
out what is EXIT in SAS, to get out.

I've been in shops which used SAS for reporting (normally not the best tool
for that), but interactive SAS seems designed for what SAS is designed for -
statistics.  But I haven't seen it used.
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 4)_

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38BF65E2.94F2810A@mediaone.net>`
- **References:** `<89fcen$q3f@netaxs.com> <D7Ru4.4503$JL3.1968267@news4.mia> <38BDF16C.36E09D8A@mediaone.net> <38BE7435.D1593973@cusys.edu>`

```
Howard Brazee wrote:

> In our shop, we have SAS as option 2 on our TSO menu.  As far as I know, the
> only thing people have done with it here is to accidentally go into
> interactive TSO when they meant to be in ISPF option 2, then try to figure
> out what is EXIT in SAS, to get out.

Since you have now digressed into the anecdotal domain of the discussion, let me
not take myself too seriously and explain to those poor lads unfortunate to have
accidentally entered SAS Display Manager System that it is not necessary to call
the operator asking for killing the TSO session. Simply type BYE or ENDSAS in
the command line and hit ENTER.

> I've been in shops which used SAS for reporting (normally not the best tool
> for that),

Yeah, but maybe abnormally, it is?

> but interactive SAS seems designed for what SAS is designed for -
> statistics.  But I haven't seen it used.

"Interactrive SAS" (to a SAS professional, sounds similar to calling CICS
something like "interactive mainframe" but let us not be picky here) is designed
exactly what "batch SAS" is designed for. The difference is the same as running
a DB2 query from a SPUFI panel interactively or as DSN batch - the same program
is running, only in the first case, your terminal gets locked until the program
is done, in the second - you do whatever else you want while it is executing in
the background. However, additionally, there are SAS product, such as FSP, IML,
or Insight,  specifically designed to be run interactively, in a GUI manner.
Lastly, to say that SAS is designed for statistics is the same as to say that
COBOL is designed to calculate the number of records in a flat file.

Kind regards,
===================
Paul M. Dorfman
Jacksonville, FL
===================
```

#### ↳ Re: SAS sucks

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38BDFCCD.794996D1@mediaone.net>`
- **References:** `<89fcen$q3f@netaxs.com>`

```
Lisa nor Jeff wrote:

> SAS gets a bad rap for performance primarily because
> managers think it can be written by anybody, not necessarily a
…[3 more quoted lines elided]…
> COBOL, and most programmers have lots of experience in it.

Therein lies a sizable stretch right there. Not _everybody_ knows COBOL,
and as a matter of fact, _most_ programmers have no vaguest idea how a
COBOL program looks like. This is one of the reasons why experienced
COBOL programmers dictate premium compensation on the market and are
highly sought after.

>  The
> advantage of COBOL is that it's a universal language.

Define "universal". If it is in the sense that "everybody knows COBOL",
see above. If it is in the sense that COBOL can be used to program just
about anything, it is true, for it is a Turing complete language!
However, the tradition of its usage and the intent with which it was
created limit its versatility pretty much to standard business
applications.

> Like it or not, SAS is a specialized language.

Define "specialized". In fact, because of the breadth of its
applications, it is much less specialized than other languages, say
COBOL and FORTRAN _specifically_ aimed at business and
scientific/engineering computations, respectively. And its syntax is no
more specialized than that of PL/I from which it has been derived.

> Not everyone
> knows it, certainly not to the level you speak of to use it
> properly.  Unless an organization standardizes on SAS and trains
> everyone in it _thoroughly_, the organization won't develop the
> expertise.

This is absolutely true. However, you might be surprised how many
organizations standardize on SAS. For a small change, it pertains to
_all_ pharmaceutical companies. For a number of reasons, there SAS is
Language One. These are big players, and they invest gobs of money and
time in SAS training. SAS enjoyes the same status in any marketing,
credit policy, modelling, forecasting, data warehousing, in other words,
decision support or trend setting department of any large organization
serious about keeping to do business. 4000 SAS people from all around
the world do not assemble for their annual SUGI Conference for
nothing.

> Regarding your comment of coding complex routines, my point is
> that if coding is required, you might as well code in COBOL
> rather than SAS.

Sure, as well as any other tongue. If an entire application is written
in COBOL, it is silly to stick a SAS piece there just for the heck of
it. However, if it reduces the number of JCL steps from 20 to 1, or NLOC
from 20,000 to 200, it may be well worth it. Many SAS procs have become
so prolific and well-known even to non-SAS programmers (e.g. PRINT,
FREQ, SUMMARY, SQL) that most folks know what they do and recognize them
with an unaided eye. You may of course disagree, but I am sure that
several lines of TABULATE or SQL are much more self-explanatory and
infinitely easier to maintain than 10,000 lines of COBOL program they
supplant. In fact, sinful as I am, I have convinced more than one COBOL
programmer that it is faster to take time to learn the entire TABULATE
than even to sketch a COBOL program that would implement maybe 1 per
cent of TABULATE's functionality.

Kind regards,
===================
Paul M. Dorfman
Jacksonville, FL
===================
```

##### ↳ ↳ Re: SAS sucks

- **From:** Howard Brazee <howard.brazee@cusys.edu>
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38BE7611.74EB7F4E@cusys.edu>`
- **References:** `<89fcen$q3f@netaxs.com> <38BDFCCD.794996D1@mediaone.net>`

```
"Paul M. Dorfman" wrote:

> Sure, as well as any other tongue. If an entire application is written
> in COBOL, it is silly to stick a SAS piece there just for the heck of
> it. However, if it reduces the number of JCL steps from 20 to 1, or NLOC
> from 20,000 to 200, it may be well worth it.

The big problem with this is that it can become costly to use the best tool
for a task - instead we use the best tool for the job because we can't find
or build programmers who are competent with all tools.  So most shops have
one primary language (nowadays shops are often split into segments - the
Unix/Oracle/C box, the IBM/IMS/COBOL box, the NT/Pearl/Java box...) which a
programmer needs to be competent, and a couple or few other languages which
they can get by in.  Often SAS is one of these "get by" languages.  But if a
programmer already works in COBOL, ADS/O, Easytrieve, and Java (my shop),
adding another tool can cost valuable competence.
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38beb799.61921658@news.transport.com>`
- **References:** `<89fcen$q3f@netaxs.com> <38BDFCCD.794996D1@mediaone.net> <38BE7611.74EB7F4E@cusys.edu>`

```
My shop is COBOL/Easytreive/JCL/CICS/DB2/TSO/Roscoe on the mainframe,
and Powerbuilder/Oracle/+AnythingMicrosoft on the network.  There is
PLENTY for us to have to know without SAS.

We just de-installed SAS last month after I spent a few hours in 1999
re-writing our remaining SAS applications.  We were primarily using it
for extraction of SMF data.  I replaced these SAS programs with some
IBM share-ware assembler programs.

Pete


On Thu, 02 Mar 2000 07:09:22 -0700, Howard Brazee
<howard.brazee@cusys.edu> wrote:

>"Paul M. Dorfman" wrote:
>
…[14 more quoted lines elided]…
>
```

##### ↳ ↳ Re: SAS sucks

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2000-03-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<89n0os$r2u$2@nntp5.atl.mindspring.net>`
- **References:** `<89fcen$q3f@netaxs.com> <38BDFCCD.794996D1@mediaone.net>`

```
Paul M. Dorfman <sashole@mediaone.net> wrote in message
news:38BDFCCD.794996D1@mediaone.net...

> >  The
> > advantage of COBOL is that it's a universal language.
…[6 more quoted lines elided]…
> applications.

It may not have been the original poster's intent, but I read this as meaning
that COBOL (as a "language") is available across operating systems (both
"proprietary" and "open").  This is because there are ANSI/ISO Standards for
it and NO specific vendor "owns" the language definition.  I know that over
the years, SAS has been ported to more systems, but I still don't think that
it is available on NEARLY as many platforms as COBOL is (and certainly not
with the same "universal" semantics).
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** theodp@aol.com (Theo DP)
- **Date:** 2000-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000302223710.03805.00000113@ng-bj1.aol.com>`
- **References:** `<89n0os$r2u$2@nntp5.atl.mindspring.net>`

```
>Subject: Re: SAS sucks
>From: "William M. Klein" wmklein@nospam.netcom.com 
…[26 more quoted lines elided]…
>    wmklein <at> ix dot netcom dot com

For the most part, interactive and batch SAS code can run * unchanged * on the
MVS, UNIX, PC, and yes, Internet platforms with no need to even compile the
source.  

Much more platform independent than the various COBOL dialects, IMHO.
```

###### ↳ ↳ ↳ Re: SAS sucks

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-03-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38BF60B0.47486E79@mediaone.net>`
- **References:** `<89fcen$q3f@netaxs.com> <38BDFCCD.794996D1@mediaone.net> <89n0os$r2u$2@nntp5.atl.mindspring.net>`

```
Bill,

I have been under the impression that SAS has been an undisputed portability
champion. Usually, if I need to test a piece of code and S/390 is kind of busy, I
cut and paste the code and run it under NT; or if it is too slow to my taste, I
do the same in UNIX. However, I may be wrong, and indeed SAS is not available on
_nearly_ as many platforms as COBOL. Just for my information, let me list the
operating systems SAS currently runs under, and I implore you to expand the list
by telling me on what operating systems, in addition to ones listed below, COBOL
is capable of running:

 1. OS/390 (TSO and CICS shells)
 2. VM/VSE
 3. CMS
 4. Open VMS
 5. VAX
 6. OS/400
 7. DOS
 8. Windows (3.x, 95, 98, NT, NT Server, 2000)
 9. OS/2 (any version)
10. Mac (any version)
11. UNIX

You are correct in SAS being _very_ proprietory. However, from the standpoint of
standards, I am not sure it is all that bad. There is just one, and only one, SAS
standard, namely the one set by The SAS Institute, and all changes and
enhancements to the standard are thoroughly documented by SI. The situation when
an implementation may be different from vendor to vendor is simply non-existent.
I do not really understand the argument of "universal semantics" since within the
accuracy of OS specifics like file name conventions, the semantics of the entire
SAS Software is precisely the same. SAS's SQL implementation completely conforms
to the ANSI standard _and_ additionally allows for use of all functions, formats,
and informats available in SAS.

Kind regards,
====================
Paul M. Dorfman
Jacksonville, Fl
====================

"William M. Klein" wrote:

> Paul M. Dorfman <sashole@mediaone.net> wrote in message
> news:38BDFCCD.794996D1@mediaone.net...
…[21 more quoted lines elided]…
>     wmklein <at> ix dot netcom dot com
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 4)_

- **From:** rich0850@aol.com (RICH0850)
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000304194507.02603.00000103@ng-fs1.aol.com>`
- **References:** `<38BF60B0.47486E79@mediaone.net>`

```
I have found SAS to be *my* ultimate scripting language. One time shot and
such.

Along the lines of "I need an answer now!"
Very few can match SAS.

It also scales well when I have to process HUGE amounts of data (gigabytes
here).

SAS is great if you need fast results in a dynamic environment.  Sometimes not
so good if CPU load is a factor (although I think with good programming, speed
will improve).  Most examples of SAS being poor in relation to other languages
(in terms of speed) are usually due to lousy design.

It's a very powerfull language.  My only regret is that others don't know about
it.  And the fact that it is so expensive.

One of the problems I've seen is that new programmers have a problem with the
"table" nature of SAS.  The fact of the dataset.  The idea that observations
are dealt with automagically.

--Richard
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 5)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C1B55A.562A2DC5@home.com>`
- **References:** `<38BF60B0.47486E79@mediaone.net> <20000304194507.02603.00000103@ng-fs1.aol.com>`

```


RICH0850 wrote:
> 
> I have found SAS to be *my* ultimate scripting language. One time shot and
> such.
> 
I'm always intrigued by the various innovations; I know nothing of SAS
nor SQL - but isn't the latter another attempt to do the former, or by
comparison is SQL hard coded ?

Some 30 years ago on an NCR mainframe I recall an analyst taking the A/R
element of a system, (don't know the specific details), but you could
flag which fields you wanted, in which order, plus ranges - users
checked off boxes on the request form, key-punched and hey presto,
customized report produced. Do these 'glittering' packages do more than
that analyst was doing 30 years ago ?

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 6)_

- **From:** "Paul M. Dorfman" <sashole@mediaone.net>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C2037B.684E9664@mediaone.net>`
- **References:** `<38BF60B0.47486E79@mediaone.net> <20000304194507.02603.00000103@ng-fs1.aol.com> <38C1B55A.562A2DC5@home.com>`

```
"James J. Gavan" wrote:

> RICH0850 wrote:
> >
…[5 more quoted lines elided]…
> comparison is SQL hard coded ?

No. SQL is a self-sustained part of Base SAS. In SAS, a programmer has the
lattitude of achieving the same result by a variety of very different means. The
choice may be dictated by performance considerations, personal choice, or both.
Those coming to SAS with procedural language experience tend to code in SAS DATA
step - the closest SAS equivalent of a COBOL, PL/I, or whatever,  program.
People with DBA background naturally tend to code in SQL. Professional SAS
programmers use both and/or a variety of SAS procedures (from the standpoint of
SAS, SQL is a SAS proc, too). Additionally, SAS allows to run programs
"external" to SAS, say IBM Utilities, from within a SAS program as if they were
native SAS procs, e.g.

PROC IDCAMS; RUN;

The control cards required by an external program, if any,  can be supplied
either in JCL or via SAS's intrinsic FILENAME statements. Likewise, any OS
commands can be issued from within a SAS program, etc. As far as SQL goes, one
may think of it as more 'hard coded' than DATA step which is simply a full
procedural programming language (admittedly, with a myriad of automatic features
built into it - contrary to the popular belief, they can always be 'turned off',
if the programmer so desires). However, I do not think it is a correct way of
putting things. SQL concentrates on relations between the objects like files or
tables and operates on those relations - it is up to the SQL optimizer to figure
out how to implement the query; so it builds the program by deduction.
Procedural philosophy is rather inductive in comparison. SAS allows both to
coexist peacefully within the same package.


> Some 30 years ago on an NCR mainframe I recall an analyst taking the A/R
> element of a system, (don't know the specific details), but you could
…[3 more quoted lines elided]…
> that analyst was doing 30 years ago ?

Judge for yourself. To erect a building, SAS gives one all the traditional tools
and pieces (bricks, sand, cement, shovels, nails,...); also, it provides
preassembled blocks of every imaginable shape along with very well designed,
unified way of meshing them together; and, finally, a myriad of automatic tools,
machinery from light to heavy, portable powerstation, etc. How to use all these
tools, is up to the programmer. In the hands of an experienced master, they
become a programming miracle, and a beautiful building is erected in a very
short time within the budget allotted. In the hands of a dumb ass, they become
dangerous. One who uses a bulldozer where only a shovel is needed will surely
produce a lousy result and waste gobs of materials and fuel for no reason. One
who, having failed to learn how to match blocks, uses bricks only, runs out of
the bricks, cement, and time. In such cases, a CIO receives a report about SAS
being a "resource hog". If CIO's intellectual capabilities match the ones of the
"resource hog" culprit, SAS gets cursed, uninstalled, etc.; otherwise, the dumb
ass guilty of raping SAS gets "uninstalled", and a professional SAS programmer
is hired to do the job the way it should be done, i.e. right.

Kind regards,
==================
Paul M. Dorfman
Jacksonville, FL
==================
```

###### ↳ ↳ ↳ Re: SAS sucks

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-03-05T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38C2093D.677289C@home.com>`
- **References:** `<38BF60B0.47486E79@mediaone.net> <20000304194507.02603.00000103@ng-fs1.aol.com> <38C1B55A.562A2DC5@home.com> <38C2037B.684E9664@mediaone.net>`

```


"Paul M. Dorfman" wrote:
> 
> "James J. Gavan" wrote:
…[11 more quoted lines elided]…
> lattitude of achieving the same result by a variety of very different means. <snip>......

Many Thanks Paul for the explanation. I always enjoy reading your
insightful messages.

Jimmy, Calgary AB
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
