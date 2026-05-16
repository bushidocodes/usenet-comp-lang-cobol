[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# new use of section numbers ??

_7 messages · 5 participants · 1999-11_

**Topics:** [`Language features and syntax`](../topics.md#syntax) · [`Help requests and how-to`](../topics.md#help)

---

### new use of section numbers ??

- **From:** Dirk Munk <munk@bart.nl>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38260BAF.F382D59D@bart.nl>`

```
Section numbers were used for overlay purposes in the old times, but
with today's computers overlay is something of the past and section
numbers are quite often just a kind of comment.

I seem to remember that there was talk about re-using the section
numbers for a kind of parallel processing, meaning that sections with
the same number could run in parallel with other sections with other
numbers. For instance if you have to do a read at 3 disks at about the
same time in the program, you would be able to do these reads in 3
different sections with different section numbers, effectively in
parallel. Assuming every read takes the same time, this would mean that
instead of having to wait for 3 disk io's, we only have to wait for 1
disk io.

Does anyone know if such a scheme will be part of the new cobol standard
?
```

#### ↳ Re: new use of section numbers ??

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<805487$abf$1@nntp8.atl.mindspring.net>`
- **References:** `<38260BAF.F382D59D@bart.nl>`

```
Easy answer - NO, this will not be part of the next Standard.  In fact, as
the "SEGMENTATION" feature was placed in the OBSOLETE category in the '85
Standard, the next Standard will *not* support any numbers on SECTION headers
(now called "markers").

Early in the work on the next Standard, there was talking about what would be
needed to make COBOL more "friendly" for parallel processing.  This idea was
not deemed of sufficient import to be followed up on.  I think (but won't
swear to it) that it is still on the candidate list for the standard *after*
this one.  But I sure wouldn't count on that.

FYI,
  I know that Micro Focus provided a "parallel" processing compiler for some
platform.  Some others may also have provided this too - but it is all done
"under the covers" without any syntax support for "encapsulated" code to be
run in parallel.
```

#### ↳ Re: new use of section numbers ??

- **From:** "James King" <mangogwr@bellsouth.net>
- **Date:** 1999-11-07T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<eeqV3.16151$aS6.185874@news4.mia>`
- **References:** `<38260BAF.F382D59D@bart.nl>`

```
Never heard of any such thing, also as far a I know, its not possible within
one PROGRAM,
as COBOL is SINGLE-THREADED.  You can NOT execute different 'sections' at
the same time
within one RUN-UNIT.

Dirk Munk wrote in message <38260BAF.F382D59D@bart.nl>...
>Section numbers were used for overlay purposes in the old times, but
>with today's computers overlay is something of the past and section
…[13 more quoted lines elided]…
>?
```

#### ↳ Re: new use of section numbers ??

- **From:** Alistair Maclean <LD50Macca@ld50macca.demon.co.uk>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<M7+3oEAyFtJ4EwjZ@ld50macca.demon.co.uk>`
- **References:** `<38260BAF.F382D59D@bart.nl>`

```
If such were available, your saving would not be a reduction of 66% over
three reads. Certainly, in the IBM mainframe environment blocking
factors, seek times and time sharing/prioritising of partitions would
all affect the result. Anybody care to guess what the real saving would
be?

In article <38260BAF.F382D59D@bart.nl>, Dirk Munk <munk@bart.nl> writes
>Section numbers were used for overlay purposes in the old times, but
>with today's computers overlay is something of the past and section
…[13 more quoted lines elided]…
>?
```

##### ↳ ↳ Re: new use of section numbers ??

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<806r66$ocp$1@nntp3.atl.mindspring.net>`
- **References:** `<38260BAF.F382D59D@bart.nl> <M7+3oEAyFtJ4EwjZ@ld50macca.demon.co.uk>`

```
I am probably NOT the best person to explain what Parallel processing CAN do,
but let me take a stab at it.  The following are VERY simple examples. It is
really used (most often) in HIGHLY numeric-crunching environments (weather
prediction, petroleum industry, etc).

Assume that you had a COBOL program with:

  Compute F1 = (F2 + F3) * (F4 + F5)

If your compiler were "smart enough" (or your programming language had the
tools to do it),  there is really no reason that you couldn't have one
processor doing the add of F2 + F3 *at the  same time* as another processor
was doing the add of F4 + F5.  Then one of these processors (or another
processor) could multiply the results - once both original adds were
completed.

Extending this a little (and using THEORETICAL COBOL code - not currently
allowed code). Now assume you had something like:

   Compute Elem1 (all) = (elem2 (all) + elem3 (all)) * (elem4 (all) + elem5
(all))

(or possibly some syntax with CORRESPONDING)

where you told the compiler to add each element in one table to each
corresponding element in another table - meanwhile (and this could be done in
one or more "independent" computers/processors) you could do the ADDs of each
element in the 3 and 4 tables.  As each "appropriate" pair became available -
some other processor would multiply them and place the results into the final
table.

  ***

Another way to think of this (more at the programmers control) would be a
case like:

  001-Mainline.
      Perform Para1
          and at the same time
      Perform Para2
      Stop Run
        .
 Para1.
      Move A to B
         .
  Para2.
     Move C to D
          .

(where A, B, C, and D have no overlapping storage and no other dependencies).

   ***

Both the processors where "parallel processing" occurs and the compilers that
are optimized to take advantage of this technique are "specialized" for this
task.  The bottom-line is that the "application algorithm" must be broken up
into things that can happen simultaneously (or not) without impacting the
final results.  This "break up" can be done explicitly by the programmer - or
by the compiler - or both.

   ***

I hope this help explains what the original question was asking about and
what it would offer (if/where available).
```

##### ↳ ↳ Re: new use of section numbers ??

- **From:** Dirk Munk <munk@bart.nl>
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38271C84.A924BACF@bart.nl>`
- **References:** `<38260BAF.F382D59D@bart.nl> <M7+3oEAyFtJ4EwjZ@ld50macca.demon.co.uk>`

```


Alistair Maclean wrote:
> 
> If such were available, your saving would not be a reduction of 66% over
…[3 more quoted lines elided]…
> be?

This 66% saving was based on the assumption that the disks are in use
for this particular program only, and on a normal average disk access
time of about 8 to 10 milliseconds.
If other files are using the same disk(s) or other programs are using
the same file(s) everything changes of course, but this idea is based on
the wish to be able to make a very fast Cobol program that can use as
many disks in parallel as possible. What is the use of having many
parallel disks if the program can only handle one at the time.

Of course there is a solution to this problem, and that is to use
external data in global areas in memory. This way a single program can
read/write data to one or more global areas, where other programs can
write/read this same data and access the database files. So you would
have 1 'central' program, and 1 program for every database disk. It is
just a bit more cumbersome to program.  

> 
> In article <38260BAF.F382D59D@bart.nl>, Dirk Munk <munk@bart.nl> writes
…[24 more quoted lines elided]…
> out how strong they are.
```

#### ↳ Re: new use of section numbers ??

- **From:** stephen_j_spiro@my-deja.com
- **Date:** 1999-11-08T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<807825$ec5$1@nnrp1.deja.com>`
- **References:** `<38260BAF.F382D59D@bart.nl>`

```
It is NOT in the proposed standard. It could be done, but the number of
operating systems that would support it are few... I can think of ways
of doing it, but the problem is synchronicity: when each of
the "simultaneous" sections are finished, they have to wait until ALL
are finished, so that the mainline code can continue.  There are very
few systems that provide this feature in ANY language.  Calls, links,
invocations to separate simultaneous modules (objects?) would seem to
be a better way to code.
Implementors are free to add this feature, however.

Stephen J Spiro
President, Wizard Systems
Member, J4 COBOL Committee

In article <38260BAF.F382D59D@bart.nl>,
  Dirk Munk <munk@bart.nl> wrote:
> Section numbers were used for overlay purposes in the old times, but
> with today's computers overlay is something of the past and section
…[8 more quoted lines elided]…
> parallel. Assuming every read takes the same time, this would mean
that
> instead of having to wait for 3 disk io's, we only have to wait for 1
> disk io.
>
> Does anyone know if such a scheme will be part of the new cobol
standard
> ?
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
