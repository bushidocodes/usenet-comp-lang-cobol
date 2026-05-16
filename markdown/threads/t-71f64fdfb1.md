[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOL Problem

_10 messages · 6 participants · 2000-10_

---

### COBOL Problem

- **From:** "anthony.corrall" <anthony.corrall@ntlworld.com>
- **Date:** 2000-10-28T18:55:53+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com>`

```
I am a student and part of our course requires us to study COBOL
programming. I have to write a program that will read from a file saved on
disk then print out the data. The data takes the form of a Sales Log. The
problem is that I need to program the said program so that for each
different sales person it starts a new sheet, printing the Sales person
total at the bottom of the corresponding page as well as a grand total at
the bottom of the last page. I have the basic program that will print it is
just getting to start a new page and calculate the totals that I am stuck
on. Can Anyone Help?
```

#### ↳ Re: COBOL Problem

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2000-10-28T18:32:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39fb1b7f.193171694@207.126.101.100>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com>`

```
Pos your code showing where exactly you think the problem is.  Also,
please tell us which compiler on what platform you are using - it will
help.

On Sat, 28 Oct 2000 18:55:53 +0100, "anthony.corrall"
<anthony.corrall@ntlworld.com> wrote:

>I am a student and part of our course requires us to study COBOL
>programming. I have to write a program that will read from a file saved on
…[8 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: COBOL Problem

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-10-28T23:30:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tfnhl$dnj$1@nnrp1.deja.com>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com>`

```
In article <9rEK5.65759$sE.112514@news6-win.server.ntlworld.com>,
  "anthony.corrall" <anthony.corrall@ntlworld.com> wrote:
> I am a student and part of our course requires us to study COBOL
> programming.

Hi:

The problem you are faced with is just about the most typical
problem in commercial systems development.

The logical solution to this problem should be taught in the
most elementary business programming course (without regard
to language).

You are now realizing that there is more to programming than
knowing COBOL. (Some people think that because they know COBOL,
they know how to program.)

Because it appears that your course is deficient, here are some
of the things you must consider if you are to write a good
dependable program:

1. Printing page heading on every page - don't forget to have
a page number on the report. The date and time would be nice too.

2. Breaking control on each Sales thing. This requires that you
keep the Sales thing from the current record to compare it with
the next one. Depending on how you code it, you may have a problem
not breaking control on the first record.

3. Don't forget to print the total for the last sales thing before
you print the grand total.

4. In effect, you have to check the sequence of the file in order
to know when the sales thing changes. So, you should detect
an out-of-sequence condition and stop.

5. Your program should also work if there is only one record in the
file.

6. It should also give the user a message if there are NO records
in the file.

7. You need stuff in working-storage to keep the current sales
thing so as to compare it to the current sales thing. You also
need two counters to add sales for the current sales thing and
the grand total.

8. Don't forget to reset your sales thing counter after you have
printed the total for it.

9. Is this a summary or detail report? I.E., do you print every
record or just a total by sales thing. I guess that it is a detail
which prints every record because it wouldn't make sense to go
to a new page on each sales thing if all you printed was a total.
If it is a detail report, you must check the line count every time
you print a record and skip to a new page when the page is full in
case there are lots of records for each sales thing.

10. The user should also have the option not to run the report
after invoking the program.

You will run into this sort of thing no matter where you go. Every
commercial application has tons of reports in them. They are all
basically the same.

As a student, you might want to read the thread called 'The Big
Picture'.

You should try drawing a flow chart, too.

A lot of people in CLC think that flowcharting is for sissies, don't
pay any attention to them.

Some other person wanted to know what platform. The platform is
basically irrelevant unless you are using a particular platform
for some particular reason, which, as a student, I would guess
not be the case.

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: COBOL Problem

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-28T19:15:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tfq0q$mj9$1@slb6.atl.mindspring.net>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com> <8tfnhl$dnj$1@nnrp1.deja.com>`

```
Unlike many of his posts, I do NOT disagree (particularly) with what is
suggested below.  I do, however, caution you (as a "student" rather than a
"professional programmer") that SOME of the things mentioned below may be
"outside the scope" of your current assignment - in fact, making such
enhancements in the future may well be your next assignment.  There is
NOTHING wrong with thinking about them - when you are first starting. (They
may actually impact how you design your program for future "enhancements")
On the other hand, don't get "discouraged" (or waste time) on things that
you are not being asked to do at this time.
```

###### ↳ ↳ ↳ Re: COBOL Problem

- **From:** Foodman <foodman123@aol.com>
- **Date:** 2000-10-29T01:15:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tftn0$i9r$1@nnrp1.deja.com>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com> <8tfnhl$dnj$1@nnrp1.deja.com> <8tfq0q$mj9$1@slb6.atl.mindspring.net>`

```
In article <8tfq0q$mj9$1@slb6.atl.mindspring.net>,
  "William M. Klein" <wmklein@nospam.ix.netcom.com> wrote:
> Unlike many of his posts, I do NOT disagree (particularly) with what
is
> suggested below.  I do, however, caution you (as a "student" rather
than a
> "professional programmer") that SOME of the things mentioned below
may be
> "outside the scope" of your current assignment - in fact, making such
> enhancements in the future may well be your next assignment.  There is
> NOTHING wrong with thinking about them - when you are first starting.
(They
> may actually impact how you design your program for
future "enhancements")
> On the other hand, don't get "discouraged" (or waste time) on things
that
> you are not being asked to do at this time.

Hi:

Those are valid points.

On the other hand; my impression, based on comments in CLC "they gave
us a program and told us to type it in", "my teacher basically told me
to F-off when I had questions", and so on, I would wonder if any course
taken would ever get to the level of detail which I suggested. Based
on the elementary nature of some of the posts; I wonder at the
competence of the instructors.

Further, that level of detail should be the basic starting-point for
the Report Programmer. Whether you build up to it or not doesn't matter,
but the Report Programmer is going to HAVE to know about them sooner
or later, so let's make it sooner. It should be emphasized to the
newcomer that Report Programs are the essence of commercial systems
and that they will, more than likely, get sick and tired of writing
them sooner or later because they are all the same. Writing Report
Programs is the essence of their trade. (A Report Program being a
program which presents information to the user, period.)

I wouldn't let a programmer loose without knowing these essentials.
Let's teach them that elementary 'Report Engine' in the level of
detail suggested and which can be used in any application.  If we
don't, who will? Will they? Do you know? I don't, How could we
find out?

Thanks

Tony Dilworth


Sent via Deja.com http://www.deja.com/
Before you buy.
```

###### ↳ ↳ ↳ Re: COBOL Problem

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2000-10-29T00:41:26-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tgd6i$n0o$1@slb0.atl.mindspring.net>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com> <8tfnhl$dnj$1@nnrp1.deja.com> <8tfq0q$mj9$1@slb6.atl.mindspring.net> <8tftn0$i9r$1@nnrp1.deja.com>`

```
Almost all (but not all) of the "issues" that you raise are "automatic" if
you use COBOL Report-Writer.  I would prefer that "COBOL 101" courses all
included support for this (especially as it will be required in the nest
COBOL Standard).  As far as "real world" goes - for the BRIEF period of time
that I was a "contractor" - I had a skeleton program with an Internal Sort -
using Report Writer in the Output Procedure (with optional VSAM, IMS, etc
"input procedures") and found that having such a skeleton in my "toolbox"
really did solve many of the "quick and dirty" as well as "production"
applications that I was asked to produce.

I think that giving such a "skeleton" to students toward the end of their
1st COBOL course and asking them to produce a "report" given an input file
layout and a report design would SHOW the use of both of these facilities of
COBOL.  ON THE OTHER HAND, I am aware of "shop standards" (not an issue for
Foodman) that would cause programmers to be prohibited from using either or
both.

Learning how to handle BOTH "shop standards" and "application design"
(including what to ask the "end user" who doesn't think of a "requirement"
by him/herself) should be an absolute requirement before trying to move from
academia to "real world".
```

###### ↳ ↳ ↳ Re: COBOL Problem

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-30T07:39:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD881F.437E855E@brazee.net>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com> <8tfnhl$dnj$1@nnrp1.deja.com> <8tfq0q$mj9$1@slb6.atl.mindspring.net> <8tftn0$i9r$1@nnrp1.deja.com> <8tgd6i$n0o$1@slb0.atl.mindspring.net>`

```


"William M. Klein" wrote:

> Almost all (but not all) of the "issues" that you raise are "automatic" if
> you use COBOL Report-Writer.  I would prefer that "COBOL 101" courses all
> included support for this (especially as it will be required in the nest
> COBOL Standard).

Yes, but first have them write the report program the other (more common) way.
Then next week, have them do the same report using report writer.  They HAVE to
know the first way, but they will appreciate the advantages of report writer all
the more.
```

###### ↳ ↳ ↳ Re: COBOL Problem

_(reply depth: 5)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-30T07:42:28-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD88D3.67184E9@brazee.net>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com> <8tfnhl$dnj$1@nnrp1.deja.com> <8tfq0q$mj9$1@slb6.atl.mindspring.net> <8tftn0$i9r$1@nnrp1.deja.com> <8tgd6i$n0o$1@slb0.atl.mindspring.net>`

```
"William M. Klein" wrote:

> I think that giving such a "skeleton" to students toward the end of their
> 1st COBOL course and asking them to produce a "report" given an input file
…[3 more quoted lines elided]…
> both.

I have had skeletons in the past, but I find it quicker to just code simple
stuff like this.  I do cut and paste code such as:

display              ' Started ' FUNCTION CURRENT-DATE (5:2)
                     '/' FUNCTION CURRENT-DATE (7:2)
                     '/' FUNCTION CURRENT-DATE (1:4)
                     ' ' FUNCTION CURRENT-DATE (09:2)
                     ':' FUNCTION CURRENT-DATE (11:2)
                     ':' FUNCTION CURRENT-DATE (13:2)

but for the most part, it is very fast work to type in a simple program.  And
complex programs won't work from a skeleton.
```

##### ↳ ↳ Re: COBOL Problem

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2000-10-30T07:34:43-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<39FD8703.CEEACDD7@brazee.net>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com> <8tfnhl$dnj$1@nnrp1.deja.com>`

```
One thing which isn't obvious to a beginner is the following:

01   LINE-COUNT           PIC 9(03)     VALUE 100.
01   LINES-PER-PAGE   PIC 9(03)     VALUE 65.

...


PRINT-ROUTINE.
     IF LINE-COUNT > LINES-PER-PAGE
         PERFORM NEW-PAGE
     END-IF.
     WRITE DETAIL-LINE.
      ADD 1                 TO LINE-COUNT.

NEW-PAGE.
      WRITE HEADER-LINE-1 AFTER ADVANCING PAGE.
      WRITE HEADER-LINE-2 AFTER ADVANCING 1.
       MOVE 2             TO LINE-COUNT.

This has a nice advantage in that it automatically prints the first
header based upon the initial value of LINE-COUNT.  Where it falls short
in your case, is that it doesn't handle your subtotals. (I don't want to
do your homework for you).  There are a couple of ways of adding a
PERFORM WRITE-FOOTERS to your logic which should work.
```

#### ↳ Re: COBOL Problem

- **From:** "Bloggs" <bloggs@neil-1234.freeserve.co.uk>
- **Date:** 2000-10-29T10:55:16
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8tgvno$trr$1@news7.svr.pol.co.uk>`
- **References:** `<9rEK5.65759$sE.112514@news6-win.server.ntlworld.com>`

```
Sounds like a problem I had to answer on my course at Computeach.
If your on the same course try page 4.35 of the Stage 3 manual to find out
about
report formats, this will show you how to get a new page with a new heading
at the top
and including the date and page number in the heading shouldnt be too
difficult to work out.
Also in the same manual, page 3.8 describes reading records. If you are not
a Computeach
student please accept my appologies, its just that your question is
identical to a question I had
during my course.
   Regards,
       Bloggs
"anthony.corrall" <anthony.corrall@ntlworld.com> wrote in message
news:9rEK5.65759$sE.112514@news6-win.server.ntlworld.com...
> I am a student and part of our course requires us to study COBOL
> programming. I have to write a program that will read from a file saved on
…[4 more quoted lines elided]…
> the bottom of the last page. I have the basic program that will print it
is
> just getting to start a new page and calculate the totals that I am stuck
> on. Can Anyone Help?
>
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
