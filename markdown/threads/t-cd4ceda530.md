[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Internal vs External SORTs

_174 messages · 29 participants · 2003-01 → 2003-09_

---

### Internal vs External SORTs

- **From:** Ubiquitous <weberm@polaris.net>
- **Date:** 2003-01-10T17:58:56+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<avn1kv$n9j$6@news.utelfla.com>`

```
I'm curious; is it better to perform a SORT within a COBOL
program or better to perform it in the JCL, or does it
depend on what one is sorting?
```

#### ↳ Re: Internal vs External SORTs

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-10T18:06:48+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<avn23o$t09$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com>`

```

On 10-Jan-2003, Ubiquitous <weberm@polaris.net> wrote:

> I'm curious; is it better to perform a SORT within a COBOL
> program or better to perform it in the JCL, or does it
> depend on what one is sorting?

Depends.

Some people curse anybody who does internal sorts, some people never do external
sorts.   IMHO, I believe many small steps are easier to maintain than one
complicated step, so I evaluate to see if there is a particular need for an
internal sort - if not, then I do external sorts.


I don't use performance as an element of my decision - I use maintainability.  
After all both sorts use the same sort program anyway.
```

##### ↳ ↳ Re: Internal vs External SORTs

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-11T17:29:53+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000000b.01a21d9f@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <avn23o$t09$1@peabody.colorado.edu>`

```
Howard,

> I don't use performance as an element of my decision - I use maintainability.  

Good man.

> After all both sorts use the same sort program anyway.

Yup.


Doug
```

#### ↳ Re: Internal vs External SORTs

- **From:** docdwarf@panix.com
- **Date:** 2003-01-10T13:24:18-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<avn34i$ku3$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com>`

```
In article <avn1kv$n9j$6@news.utelfla.com>,
Ubiquitous  <weberm@polaris.net> wrote:
>I'm curious; is it better to perform a SORT within a COBOL
>program or better to perform it in the JCL, or does it
>depend on what one is sorting?

The answer is predicated on the criteria one uses for 'better'.

DD
```

#### ↳ Re: Internal vs External SORTs

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2003-01-10T12:38:53-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<avn3vv$3s9$1@slb9.atl.mindspring.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com>`

```
(Assuming an IBM mainframe environment - from "context")

If you use the FASTSRT compiler option, there is probably little performance
difference.  Probably the *most* important thing to "look into" is what is
most commonly used in *YOUR* shop - so that other programmers can "maintain"
(easily) whatever you create.

I have read several (semi-internal) posts between the IBM COBOL and SORT
developers and they both find reasonable "justification" for each approach.

My *personal* opinion - is that it depends on what "processing" of input or
output records you use.  I (again personally) don't really like creating and
maintaining E15 and E35 exits - and much prefer COBOL Input/Output
procedures. (If the only "processing" of your input/output can be done via
SORT control cards, then this issue doesn't apply)  Similarly, if you
have/use COBOL report writer, I find that a GREAT tool in Output
Procedures - as opposed to the DFSort (or SyncSort) "reporting" facilities.
On the other hand,  if you  have a basic

   - process an entire file (to get it ready to SORT)
  - sort that file
  - process the output file (often in multiple different ways)

type logic,  I (again personally) see this as an EXCELLENT target for an
"external sort".

OBVIOUSLY, if you happen to be a "contractor" (as many CLC readers are),
then it is CRITICAL that you find out what the "shop standard) is (if any).
```

#### ↳ Re: Internal vs External SORTs

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-10T19:44:38+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E1F250C.3070600@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com>`

```

Ubiquitous wrote:
> I'm curious; is it better to perform a SORT within a COBOL
> program or better to perform it in the JCL, or does it
> depend on what one is sorting?
> 

What I've experienced is it depends on the shop.  One place 
I worked at "required" all sorts to be external in a 
preceding JCL step.  Since their JCL streams were miles 
long, it made for restarts after an abend much easier.  (The 
JCL steps were performed based upon return codes from 
previous step).

Other places don't care and so what ever makes the most 
sense in the given situation is the way I go.  I have never 
seen any shop question the performance of either sort.  You 
can get very creative with external sorts, but why fill your 
mind with all the little tricks of SyncSort when it is just 
as easy, if not more easy, in COBOL.  Especially if you want 
to filter the data in any way.
```

##### ↳ ↳ Re: Internal vs External SORTs

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-01-10T17:48:40-08:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8a2d426e.0301101748.a824729@posting.google.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E1F250C.3070600@nycap.rr.com>`

```
From what I understand, if the internal sort uses fastsrt and
using/giving instead of input/output procedures, the performance is
comperable. Otherwise, external wins hands down, because sort i/o is
much faster than cobol's.

Jack 


Robert Graham <rgraham2@nycap.rr.com> wrote in message news:<3E1F250C.3070600@nycap.rr.com>...
> Ubiquitous wrote:
> > I'm curious; is it better to perform a SORT within a COBOL
…[17 more quoted lines elided]…
> to filter the data in any way.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-01-11T22:50:45+02:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<rq012v000ig1u3iovafejnj08ldd2b9nvn@4ax.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E1F250C.3070600@nycap.rr.com> <8a2d426e.0301101748.a824729@posting.google.com>`

```
On 10 Jan 2003 17:48:40 -0800 jacksleight@hotmail.com (Jack Sleight) wrote:

:>From what I understand, if the internal sort uses fastsrt and
:>using/giving instead of input/output procedures, the performance is
:>comperable. Otherwise, external wins hands down, because sort i/o is
:>much faster than cobol's.

If one is using/giving, one is really doing an external sort under the covers.

:>Robert Graham <rgraham2@nycap.rr.com> wrote in message news:<3E1F250C.3070600@nycap.rr.com>...
:>> Ubiquitous wrote:
:>> > I'm curious; is it better to perform a SORT within a COBOL
:>> > program or better to perform it in the JCL, or does it
:>> > depend on what one is sorting?
:>> > 
:>> 
:>> What I've experienced is it depends on the shop.  One place 
:>> I worked at "required" all sorts to be external in a 
:>> preceding JCL step.  Since their JCL streams were miles 
:>> long, it made for restarts after an abend much easier.  (The 
:>> JCL steps were performed based upon return codes from 
:>> previous step).
:>> 
:>> Other places don't care and so what ever makes the most 
:>> sense in the given situation is the way I go.  I have never 
:>> seen any shop question the performance of either sort.  You 
:>> can get very creative with external sorts, but why fill your 
:>> mind with all the little tricks of SyncSort when it is just 
:>> as easy, if not more easy, in COBOL.  Especially if you want 
:>> to filter the data in any way.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** jacksleight@hotmail.com (Jack Sleight)
- **Date:** 2003-01-12T12:32:26-08:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<8a2d426e.0301121232.56f9624f@posting.google.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E1F250C.3070600@nycap.rr.com> <8a2d426e.0301101748.a824729@posting.google.com> <rq012v000ig1u3iovafejnj08ldd2b9nvn@4ax.com>`

```
No quite. There's 1 less step executed. It may also facilitate logical
interplay between the pgm code and the sort that may prove clumsy when
executing separate steps.





Binyamin Dissen <postingid@dissensoftware.com> wrote in message news:<rq012v000ig1u3iovafejnj08ldd2b9nvn@4ax.com>...
> On 10 Jan 2003 17:48:40 -0800 jacksleight@hotmail.com (Jack Sleight) wrote:
> 
…[27 more quoted lines elided]…
> :>> to filter the data in any way.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-01-13T14:53:50+02:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<bkd52vgbpenveqd8vbje92p3682ep47pdd@4ax.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E1F250C.3070600@nycap.rr.com> <8a2d426e.0301101748.a824729@posting.google.com> <rq012v000ig1u3iovafejnj08ldd2b9nvn@4ax.com> <8a2d426e.0301121232.56f9624f@posting.google.com>`

```
On 12 Jan 2003 12:32:26 -0800 jacksleight@hotmail.com (Jack Sleight) wrote:

:>No quite. There's 1 less step executed. 

Not relevant.

:>                                        It may also facilitate logical
:>interplay between the pgm code and the sort that may prove clumsy when
:>executing separate steps.

I fail to see a case where doing a SORT USING/GIVING would gain anything over
an external sort.

:>Binyamin Dissen <postingid@dissensoftware.com> wrote in message news:<rq012v000ig1u3iovafejnj08ldd2b9nvn@4ax.com>...
:>> On 10 Jan 2003 17:48:40 -0800 jacksleight@hotmail.com (Jack Sleight) wrote:
:>> 
:>> :>From what I understand, if the internal sort uses fastsrt and
:>> :>using/giving instead of input/output procedures, the performance is
:>> :>comperable. Otherwise, external wins hands down, because sort i/o is
:>> :>much faster than cobol's.
:>> 
:>> If one is using/giving, one is really doing an external sort under the covers.
:>> 
:>> :>Robert Graham <rgraham2@nycap.rr.com> wrote in message news:<3E1F250C.3070600@nycap.rr.com>...
:>> :>> Ubiquitous wrote:
:>> :>> > I'm curious; is it better to perform a SORT within a COBOL
:>> :>> > program or better to perform it in the JCL, or does it
:>> :>> > depend on what one is sorting?
:>> :>> > 
:>> :>> 
:>> :>> What I've experienced is it depends on the shop.  One place 
:>> :>> I worked at "required" all sorts to be external in a 
:>> :>> preceding JCL step.  Since their JCL streams were miles 
:>> :>> long, it made for restarts after an abend much easier.  (The 
:>> :>> JCL steps were performed based upon return codes from 
:>> :>> previous step).
:>> :>> 
:>> :>> Other places don't care and so what ever makes the most 
:>> :>> sense in the given situation is the way I go.  I have never 
:>> :>> seen any shop question the performance of either sort.  You 
:>> :>> can get very creative with external sorts, but why fill your 
:>> :>> mind with all the little tricks of SyncSort when it is just 
:>> :>> as easy, if not more easy, in COBOL.  Especially if you want 
:>> :>> to filter the data in any way.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-13T11:26:14-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<v25pi2l3fpiqc0@corp.supernews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E1F250C.3070600@nycap.rr.com> <8a2d426e.0301101748.a824729@posting.google.com> <rq012v000ig1u3iovafejnj08ldd2b9nvn@4ax.com> <8a2d426e.0301121232.56f9624f@posting.google.com> <bkd52vgbpenveqd8vbje92p3682ep47pdd@4ax.com>`

```

Binyamin Dissen <postingid@dissensoftware.com> wrote in message
news:bkd52vgbpenveqd8vbje92p3682ep47pdd@4ax.com...
[...]
>
> I fail to see a case where doing a SORT USING/GIVING would gain anything
over
> an external sort.

It is not a typical mainframe, business application; but
I have an optimization solution that makes multiple
passes on partial solutions from the input file. Each pass
and for each partial solution, the program works on it for
a limited time generating more partial solutions, then
writes these to the output file. At the end of input, the
output file is sorted to become the input file for the next
pass. The program terminates after a predetermined
number of passes even though many partial solutions
are untried.

With SORT USING/GIVING, it is not necesary to exit the
program between passes.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-01-13T13:33:28-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<avv4ab$6c0$1@slb1.atl.mindspring.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E1F250C.3070600@nycap.rr.com> <8a2d426e.0301101748.a824729@posting.google.com> <rq012v000ig1u3iovafejnj08ldd2b9nvn@4ax.com> <8a2d426e.0301121232.56f9624f@posting.google.com> <bkd52vgbpenveqd8vbje92p3682ep47pdd@4ax.com>`

```
Binyamin,
  A couple of points:

1) COBOL uses "native" SORT for I/O when FASTSRT is specified, if *either*
the USING or GIVING phrase is specified.  Therefore, if you have
     USING ... OUTPUT PROCEDURE
        or
     INPUT PROCEDURE ... GIVING
then SORT will do the I/O for one - but not both of the phases (similar to
using either an E15 or an E35 exit - but not both)

2) The other "advantage" of using a COBOL internal SORT (with FASTSRT
specified and both USING/GIVING) is if the "program logic" does "common"
things both before *and* after the actual SORT.  Although you (the
programmer) *COULD* break this up into 3 steps Program-Logic-1 then SORT
then Program-Logic-2, if the actual "code" has common logic in the before
and after sections, (which often happens) then keeping to an internal SORT
allows for "performed" common procedure - without having to maintain it in 2
different programs.  (Obviously, this "assumes" that although there is SOME
common logic, not ALL the logic is identical in the "before" and "after"
portions of the application.

    ***

My *guess* is that this isn't REAL common - but I would also guess that
almost every "large" system has at least one example of this type of
situation.

Bottom-Line (as stated before):
  I don't think that the original question has ANY "hard and fast" answer -
but there are things that can be considered "if all else is equal".
```

#### ↳ Re: Internal vs External SORTs

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-10T16:00:57-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<mo-dnSwlUblX34KjXTWciw@giganews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com>`

```

"Ubiquitous" <weberm@polaris.net> wrote in message
news:avn1kv$n9j$6@news.utelfla.com...
> I'm curious; is it better to perform a SORT within a COBOL
> program or better to perform it in the JCL, or does it
> depend on what one is sorting?


With an internal sort you can control WHAT sub-set gets sorted.

That is, in a 1 million-record file, you may be creating a report of only
500 records. Instead of an external sort shuffling these 500 to the front,
you can select only the 500 in which you're interested and sort them.

Related topic:
One of the rules (attributed to Moses, but the file was truncated after ten
records): "Thou shalt not sort the master file."
```

##### ↳ ↳ Re: Internal vs External SORTs

- **From:** Frank Yaeger <fyaeger@vnet.ibm.com>
- **Date:** 2003-01-10T16:18:36-08:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E1F62DC.8040500@vnet.ibm.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com>`

```
JerryMouse wrote:

>With an internal sort you can control WHAT sub-set gets sorted.
>
…[7 more quoted lines elided]…
>
If I understand what you're saying, you can, in fact, do that with 
DFSORT by using an INCLUDE or OMIT statement to remove the records you 
don't want to sort.  INCLUDE or OMIT processing takes place before SORT 
processing, so you will only sort the records you include.   DFSORT also 
has a SKIPREC=n option that removes the first n records before sorting. 
  Sure, there's things you can do with a COBOL program that you can't do 
with DFSORT, but there are plenty of things that you can do with DFSORT.

I know this is a COBOL group and you guys like to write programs for 
everything, but I think you'd be surprised if you actually looked at the 
DFSORT books to see ALL of the many things you can do with DFSORT 
without writing a program.  I'm not saying that an external sort is 
better or worse than an internal sort, only that you shouldn't assume 
that you can't do things with DFSORT that you can do with an internal 
sort without actually finding out.   Even an "internal sort" can use 
DFSORT control statements (like INCLUDE) very easily via a DFSPARM data 
set, e.g.

//DFSPARM DD *
   INCLUDE COND=(...)
/*

All of the DFSORT books are online.  You can access them from:

http://www.storage.ibm.com/software/sort/mvs/srtmpub.html

In particular, you might want to look at the "Summary of Changes" for 
all of the DFSORT Releases and PTFs to see how much we've put into 
DFSORT over the years that you might not be aware of.  Here's the URL 
for the Summary of Changes on the DFSORT website:

http://www.storage.ibm.com/software/sort/mvs/summary_changes/srtmsocc.html

Note that I'm not looking to start a fight here - just providing 
information for those who want to know.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-10T19:33:10-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<asidneFm1unX6YKjXTWckA@giganews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <3E1F62DC.8040500@vnet.ibm.com>`

```

"Frank Yaeger" <fyaeger@vnet.ibm.com> wrote in message
news:3E1F62DC.8040500@vnet.ibm.com...
> JerryMouse wrote:
>
…[3 more quoted lines elided]…
> >500 records. Instead of an external sort shuffling these 500 to the
front,
> >you can select only the 500 in which you're interested and sort them.
> >
> >Related topic:
> >One of the rules (attributed to Moses, but the file was truncated after
ten
> >records): "Thou shalt not sort the master file."
> >
…[34 more quoted lines elided]…
> information for those who want to know.

Your point is well taken. I'll amend my opening statement to read:

"With an internal sort you have _more_ control over WHAT gets sorted."

As for "I'm not looking to start a fight..." Statements like "you guys like
to write programs for  everything..." and "you shouldn't assume that you
can't do things ..." assume facts not in evidence.

Of course the last external sort I used was in 1976 on a 370-165; whatcha
got for a PC, Frank?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-11T17:29:54+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000000d.01a220b6@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <3E1F62DC.8040500@vnet.ibm.com> <asidneFm1unX6YKjXTWckA@giganews.com>`

```
JerryMouse,

> Of course the last external sort I used was in 1976 on a 370-165; whatcha
> got for a PC, Frank?

It's bigger than that :-)

But nowhere near as fast.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-01-10T22:58:05-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E1F883D.C69D7418@istar.ca>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <3E1F62DC.8040500@vnet.ibm.com>`

```
If you think that DFSORT can do a lot, you should see SYNCSORT for
UNIX.  As someone who successfully argued against using the competitor
SYNCSORT's Report writing functions on the mainframe for production, I
would have no qualms about using properly written UNIX SYNCSORT report
written functions.  Among other things, that sort knows what to do with
a COBOL record description and field names are native to it.

Frank Yaeger wrote:
> 
> JerryMouse wrote:
…[50 more quoted lines elided]…
> => DFSORT/MVS is on the WWW at http://www.ibm.com/storage/dfsort/
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-13T15:09:04+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<avukqg$9rn$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <3E1F62DC.8040500@vnet.ibm.com> <3E1F883D.C69D7418@istar.ca>`

```

On 10-Jan-2003, "Clark F. Morris, Jr." <cfmtech@istar.ca> wrote:

> If you think that DFSORT can do a lot, you should see SYNCSORT for
> UNIX.  As someone who successfully argued against using the competitor
…[3 more quoted lines elided]…
> a COBOL record description and field names are native to it.

Over the years, DFSORT has matched what SYNCSORT had when I used it.   It can
use COBOL record names (but I haven't).
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-13T15:07:31+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<avuknj$9rg$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <3E1F62DC.8040500@vnet.ibm.com>`

```

On 10-Jan-2003, Frank Yaeger <fyaeger@vnet.ibm.com> wrote:

> If I understand what you're saying, you can, in fact, do that with
> DFSORT by using an INCLUDE or OMIT statement to remove the records you
…[4 more quoted lines elided]…
> with DFSORT, but there are plenty of things that you can do with DFSORT.

That last line is a reason I often use CoBOL sorts.  Usually this involves
lookups to a database to determine which records to include, but occasionally it
will involve a complex calculation.   The other reason I use CoBOL sorts is when
the sort order depends upon a user parm.

Also, when programmers are unfamiliar with the more complex DFSORT options, my
tendency will be to use a tool (such as CoBOL), that they are more familiar with
- unless I am simply extracting test data for myself.
```

##### ↳ ↳ Re: Internal vs External SORTs

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-11T17:29:54+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000000c.01a21f62@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com>`

```
JerryMouse,

> With an internal sort you can control WHAT sub-set gets sorted.

Well, most sorts give you selection criteria so that's not usually a 
show-stopper.

> Related topic:
> One of the rules (attributed to Moses, but the file was truncated after ten
> records): "Thou shalt not sort the master file."

Scott's maintenance corollary:

"The master file shall always be sortable."



---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-12T13:46:42+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E21743F.9060507@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk>`

```


Doug Scott wrote:
> JerryMouse,
> 
…[25 more quoted lines elided]…
> 

Perhaps he intended to say "The shalt not sort the master 
file AND REWRITE IT" .  One should be able to sort anything 
he darn well pleases.

As two someone else's pointed out, lots can be done with 
DFSORT and SyncSort - you just have to know how, and lots of 
places seem to shred all manuals except one set kept in the 
systems programmer's locked closet.  I've used both for one 
shot file fixes and had good results.  If you are going to 
use "USING/GIVING" you might as well use an external sort as 
it is just a couple of JCL lines as opposed to having to 
write all the COBOL code.  The only real reason not to use 
external is to change the file in some way that not possible 
(or at least EASY) in an external sort.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-12T15:32:47+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000011.006306a1@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com>`

```
Robert,

> One should be able to sort anything he darn well pleases.

If the keys are in the same place in every record.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-13T12:26:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E22B2E1.4000709@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <VA.00000011.006306a1@nildram.co.uk>`

```


Doug Scott wrote:
> Robert,
> 
…[5 more quoted lines elided]…
> 

If they are not then the file designer should have been 
demoted to the mail room, preferably at the branch office in 
some third world country.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** sanghabum@aol.comjunkless (Sanghabum)
- **Date:** 2003-01-13T13:37:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030113083719.15035.00000458@mb-fs.aol.com>`
- **References:** `<3E22B2E1.4000709@nycap.rr.com>`

```
>> If the keys are in the same place in every record.
>
…[3 more quoted lines elided]…
>some third world country.

The file designer may never have envisioned the data sort now being attempt.
there are many cases I can think of (and have implemented some of them) where
the key field(s) for the next sort are not simply a known offset within a
record.

* I might be trying to sort by ISO week number from a file that contains only
yyyy-mm-dd dates. The key is only visible after I reduce yyyy-mm-dd to yyyy-ww;

* I might be trying to sort by total-balance where that is the sum of
cleared-balances and uncleared-balances for account type "5" (and more fiddly
math for account type "7"). The key doesn't exist until I do the math.

* I might be attempting to sort by last part of name. (Keeping things simple)
that means finding the last non-terminal space in the name field and making
that the sort key.

*I might be writing a mini special-purpose reporting tool. The order of the
data depends on a parameter supplied by the user. My program doesn't know the
exact key (though it knows the range of possibilities) until it runs.

Colin.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 7)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-13T14:24:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E22CE9F.7040800@nycap.rr.com>`
- **References:** `<3E22B2E1.4000709@nycap.rr.com> <20030113083719.15035.00000458@mb-fs.aol.com>`

```
"KEY" is a term than may be being applied two ways here.  If 
by key you are referring to a KSDS or and indexed file of 
some sort, I would think the KEYS have to be in the same 
place on every record.  If on the other hand you are 
referring to fields that you want to sort on for some reason 
or other, they can be anywhere in the record, as long as 
they are all in the same place within all the records.  They 
don't necessarily have to be the original key.

A sort doesn't care where the sort keys of a flat file are 
(often the  kind of file a master file is).  You just tell 
it what positions to use as the sort key.  If the file is a 
VSAM file then create an alternate key, or read sequentially 
in the INPUT procedure and sort your selected records in a 
sort file for use within the program.

Sanghabum wrote:
>>>If the keys are in the same place in every record.
>>
…[26 more quoted lines elided]…
> Colin.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 8)_

- **From:** sanghabum@aol.comjunkless (Sanghabum)
- **Date:** 2003-01-13T16:41:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030113114149.01900.00000157@mb-fq.aol.com>`
- **References:** `<3E22CE9F.7040800@nycap.rr.com>`

```
>"KEY" is a term than may be being applied two ways here.  If 
>by key you are referring to a KSDS or and indexed file of 
…[5 more quoted lines elided]…
>don't necessarily have to be the original key.

I think the orignal poster meant your second case, and got ticked off by the
other poster who read it as the first case.

I was trying to show some examples that go beyond the second case -- where the
key/sort fields do not exist *directly* in the data. They emerge after
massaging.

If the massaging is of the sort (pun intended) that an exernal utility sort can
handle, then the jobstreams designer has a choice. If  not, it looks like an
internal sort is the best way forward. Failing that: three jobsteps: 1. create
temporay copy of master file wth massaged key fields 2. Sort externally 3.
Process.

>A sort doesn't care where the sort keys of a flat file are 
>(often the  kind of file a master file is).  You just tell 
>it what positions to use as the sort key. 

Absolutely -- provided the sort key fields are in fixed positions. Try, for
example, sorting this posting into paragraphs by length with DFSORT -- shortest
paragraph first. The data is there, but explicit sort fields are not.

Colin.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-01-13T14:30:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g4AU9.7481$qU5.5760266@newssrv26.news.prodigy.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <VA.00000011.006306a1@nildram.co.uk> <3E22B2E1.4000709@nycap.rr.com>`

```
"Robert Graham" <rgraham2@nycap.rr.com> wrote in message
news:3E22B2E1.4000709@nycap.rr.com...
>
> If [sort keys from multiple input files ] are not [at the same offset in
the input records ] then
> the file designer should have been demoted to the mail room, preferably at
the branch office in
> some third world country.

What? You've never seen this situation?  I've seen it a lot: it occurs when
an application has to be upgraded to add feautures not anticipated when the
application was originally created. (But that hardly *ever* happens, right?)

Methinks thou dost castigate and case aspersions on this circumstance too
quickly.

Besides, this is the kind of situation tailor-made for the internal sort.
You can format the sort records from multiple inputs and RELEASE them all,
then get them back into a single file with a simple GIVING. That is, the
ability to 'mix and match'  RELEASE-RETURN (INPUT| OUTPUT PROCEDURE IS ...)
with USING-GIVING is a very powerful tool.

MCM
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-12T09:36:21-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<7rWdnVocsaTUFryjXTWchQ@giganews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com>`

```
A few imbedded observations:

"Robert Graham" <rgraham2@nycap.rr.com>

> >>With an internal sort you can control WHAT sub-set gets sorted.
> >
…[6 more quoted lines elided]…
> >>One of the rules (attributed to Moses, but the file was truncated after
ten
> >>records): "Thou shalt not sort the master file."
> >
…[7 more quoted lines elided]…
> he darn well pleases.

Just because you CAN doesn't mean you SHOULD. I would argue that records of
interest should be extracted from the master and these extracted records
sorted. It may turn out that ALL the records from the master are extracted,
but that's not really the same as sorting the master. Although, to be fair,
there are jobs that sort the master file just because they can.

I've seen programs designed to terminate at the first control break (whether
five records or 100M) and depend upon an external sort to get the records of
interest to the front of the file. This is particularily disheartening when,
after a 10-reel input file (and a 10-reel output file), the program
terminates normally after reading five records of the sorted output.

It gets worse. In shops with a 'let's sort the master file' mentality, all
manner of additional work is mandated. I once got a project that included a
file layout sheet. "In what order is the master file?" I asked. "Oh, that
depends on what was done to it last," I was informed. "(moan)."  Turns out,
every program that touched that file (or that would touch the file) had to
sort the file first because there was no definition about the record order.

>
> As two someone else's pointed out, lots can be done with
…[8 more quoted lines elided]…
> (or at least EASY) in an external sort.

You're right about the manuals - and bricklayers seldom want to know how to
make their own bricks. That's just the way it is.

There are other considerations, too. Here's a big one: By keeping the sort
control logic inside a program it is relatively immune to diddling by people
who don't know what the shit they're doing. At one shop wher I once worked,
a JCL deck got rearranged such that the necessary (external) sort was placed
AFTER the module needing  the sorted file. Days and deadlines passed before
the error was found.

When deciding between USING/GIVING and an external sort, my view focuses on
whether the sort parameters are job dependent. If the parameters are the
same, job after job, month after month, use USING/GIVING, thereby avoiding
the vulnerbility of meddling fingers. If the job is a quick-and-dirty, use
an external sort.

There are many reasons for using/not using and internal sort - efficiency,
turn-around (not the same as efficiency), security, availability of
resources, ease of use, knowledge of how to use, yadda-yadda. All will
probably agree the decision is not automatic.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-12T19:19:55+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000012.0132f899@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <7rWdnVocsaTUFryjXTWchQ@giganews.com>`

```
JerryMouse,

> Turns out,
> every program that touched that file (or that would touch the file) had to
> sort the file first because there was no definition about the record order.

I thought we'd shot all those guys back in the sixties.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-01-12T17:45:37-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<EVSdnfXwlImbY7yjXTWcjw@giganews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <7rWdnVocsaTUFryjXTWchQ@giganews.com> <VA.00000012.0132f899@nildram.co.uk>`

```

"Doug Scott" <dwscott@nildram.co.uk> wrote in message
news:VA.00000012.0132f899@nildram.co.uk...
> JerryMouse,
>
> > Turns out,
> > every program that touched that file (or that would touch the file) had
to
> > sort the file first because there was no definition about the record
order.
>
> I thought we'd shot all those guys back in the sixties.

This WAS back in the '60s (Or maybe the '70s - I forget. What year is it now
anyway? Oh, early evening. Never mind, it's turtles all the way down.)
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 7)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-13T20:46:56+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000013.0028fac9@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <7rWdnVocsaTUFryjXTWchQ@giganews.com> <VA.00000012.0132f899@nildram.co.uk> <EVSdnfXwlImbY7yjXTWcjw@giganews.com>`

```
JerryMouse,

> Never mind, it's turtles all the way down

BT,DT :-)

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-13T12:36:21+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E22B542.1040501@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <7rWdnVocsaTUFryjXTWchQ@giganews.com>`

```


JerryMouse wrote:

<SNIP>

> 
> There are other considerations, too. Here's a big one: By keeping the sort
…[4 more quoted lines elided]…
> the error was found.

That's true, but most of the mainframe places I've worked at 
keep the production JCL away from those kind of people. 
You'd have to be pretty creative to do JCL overrides that 
would reorder the steps. ... by the way, how long ago did 
that "DECK" get rearranged?  I haven't seen a punch card in 
almost 20 years. ;)

> 
> When deciding between USING/GIVING and an external sort, my view focuses on
…[4 more quoted lines elided]…
> 

Most of the externals i've used were for quick-and-dirty 
(though nothing "I" write is ever really "dirty"!) :) 
Whenever I've needed to include a sort it is because I 
usually neet to extract and/or filter the file to create a 
sub-set for the program in question.  So... I make it 
interanl to keep those meddling fingers off.

> There are many reasons for using/not using and internal sort - efficiency,
> turn-around (not the same as efficiency), security, availability of
…[3 more quoted lines elided]…
> 

I've found that when depending on the "automatic" you are 
likely to "automatically fail".
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** Frank Yaeger <fyaeger@vnet.ibm.com>
- **Date:** 2003-01-13T08:26:58-08:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E22E8D2.9050803@vnet.ibm.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com>`

```


Robert Graham wrote:

> As two someone else's pointed out, lots can be done with DFSORT and 
> SyncSort - you just have to know how, and lots of places seem to shred 
> all manuals except one set kept in the systems programmer's locked 
> closet. 


This isn't a problem for DFSORT, because all of the manuals are 
available online.  You can access them from:

http://www.storage.ibm.com/software/sort/mvs/srtmpub.html

Frank Yaeger - DFSORT Team  (IBM) - yaeger@us.ibm.com           
Specialties: ICETOOL, OUTFIL, Symbols, Migration                
=> DFSORT/MVS is on the Web at http://www.ibm.com/storage/dfsort
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-13T17:29:42+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E22F9FB.1030700@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <3E22E8D2.9050803@vnet.ibm.com>`

```


Frank Yaeger wrote:
> 
> 
…[17 more quoted lines elided]…
> 

Lots of mainframe shops don't like people going on the 
internet for any reason, even to do research, or get e-mail. 
  They seem to still measure productivity based upon how 
many lines of code you enter per day, rather than how well 
the program works.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** Frank Yaeger <fyaeger@vnet.ibm.com>
- **Date:** 2003-01-13T11:25:19-08:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E23129F.3060304@vnet.ibm.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <3E22E8D2.9050803@vnet.ibm.com> <3E22F9FB.1030700@nycap.rr.com>`

```


Robert Graham wrote:

>
> Frank Yaeger wrote:
…[5 more quoted lines elided]…
>
Yes, I imagine that's true, but I posted the URL for the DFSORT books on 
THIS list and presumably somebody who is reading this list has access to 
the internet (at least at home if not at work).   At any rate, the 
DFSORT books are available online for those who CAN access them.   
Others can obtain hardcopies of the DFSORT books just as they can obtain 
hardcopies of COBOL books.    Not sure why one would be more of a 
problem then another in that kind of shop.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 7)_

- **From:** Frank Yaeger <fyaeger@vnet.ibm.com>
- **Date:** 2003-01-13T11:30:20-08:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2313CC.6040908@vnet.ibm.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <3E22E8D2.9050803@vnet.ibm.com> <3E22F9FB.1030700@nycap.rr.com> <3E23129F.3060304@vnet.ibm.com>`

```


Frank Yaeger wrote:

>
>
…[17 more quoted lines elided]…
>
I should also mention that the DFSORT books are included on the z/OS 
CDs, so that's another way to access them for people who aren't allowed 
to access the Internet.  
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-13T13:18:22-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<avuvte$71k$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <3E22E8D2.9050803@vnet.ibm.com>`

```
In article <3E22E8D2.9050803@vnet.ibm.com>,
Frank Yaeger  <fyaeger@vnet.ibm.com> wrote:
>
>
…[11 more quoted lines elided]…
>http://www.storage.ibm.com/software/sort/mvs/srtmpub.html

Thanks for the URL... but I've worked in shops where 
consultants/contractors/hired guns were not allowed to have Web access.

(In one of them it was a bit... difficult, as timesheets were maintained 
on a website; when I pointed this out I was told to 'use someone else's 
signon'.)

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-13T21:20:59+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000014.00482b97@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <3E22E8D2.9050803@vnet.ibm.com> <avuvte$71k$1@panix1.panix.com>`

```
> (In one of them it was a bit... difficult, as timesheets were maintained 
> on a website; when I pointed this out I was told to 'use someone else's 
> signon'.)

ROFL!

I'm at a site where they wouldn't let a contractor work from home, but 
quite happily allow software house staff they've never met log in from 
India and do overnight support.

It only takes a few hours the next day to sort out the mess.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 7)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-13T21:05:28-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<avvr98$538$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E22E8D2.9050803@vnet.ibm.com> <avuvte$71k$1@panix1.panix.com> <VA.00000014.00482b97@nildram.co.uk>`

```
In article <VA.00000014.00482b97@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> (In one of them it was a bit... difficult, as timesheets were maintained 
>> on a website; when I pointed this out I was told to 'use someone else's 
…[6 more quoted lines elided]…
>India and do overnight support.


Actually that makes *perfect* sense... you see, the contractor is paid an 
hourly rate and there's no way to manage him directly to make sure that 
he's not cheating the company ('manage' here being used in the crudest 
Industrial Era eyes-on sense of counting noses/assholes/keystrokes) while 
the Indian company is paid a fixed rate so it doesn't matter whether they 
do their jobs or not.

>
>It only takes a few hours the next day to sort out the mess.

Keeps some folks employed, aye.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 8)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-14T06:41:16+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000016.003cb7f3@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E22E8D2.9050803@vnet.ibm.com> <avuvte$71k$1@panix1.panix.com> <VA.00000014.00482b97@nildram.co.uk> <avvr98$538$1@panix2.panix.com>`

```
> ('manage' here being used in the crudest 
> Industrial Era eyes-on sense of counting noses/assholes/keystrokes)

I always thought telecommuting wouldn't take off for that reason. But I 
was wrong - many managers work from home at the drop of a hat, but 
nobody else can.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-14T05:47:58-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b00psu$ps9$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000014.00482b97@nildram.co.uk> <avvr98$538$1@panix2.panix.com> <VA.00000016.003cb7f3@nildram.co.uk>`

```
In article <VA.00000016.003cb7f3@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> ('manage' here being used in the crudest 
>> Industrial Era eyes-on sense of counting noses/assholes/keystrokes)
…[3 more quoted lines elided]…
>nobody else can.

I don't know about 'many'... it has been my experience that frequently a 
manager will be more 'hands-on' than I would deem necessary - after all, 
there must be a Very Good Reason for stopping by my cube every 42 minutes 
and breezily asking 'So... how's it going?' - in order to give... 
*someone* the impression that whatever-it-is-that-they-do is Most 
Valuable, Indeed.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 10)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-14T14:02:03+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E241ADE.4030900@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000014.00482b97@nildram.co.uk> <avvr98$538$1@panix2.panix.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com>`

```


docdwarf@panix.com wrote:
> In article <VA.00000016.003cb7f3@nildram.co.uk>,
> Doug Scott  <dwscott@nildram.co.uk> wrote:
…[17 more quoted lines elided]…
> 

Isn't that style of management based upon a book by Tom 
Peters (I think he wrote it) "The Search for Excellence" 
where he suggests that "management by walking about" is how 
it people should be "managed".

I also stand in wonder not just at the help desk people 
located in India who can telecommute, but also the flavor of 
the week web/internet people - the ones who have two weeks 
experience in developing web sites.  With over twenty years 
of programming experience, you'd think I could be out of 
their sight for a day or two and still be productive without 
their constant "input".
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-14T10:03:50-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b018sm$9mj$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com>`

```
In article <3E241ADE.4030900@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[23 more quoted lines elided]…
>it people should be "managed".

Well, there should be moderation in all things... including moderation, of 
course.  A manager who stays far removed from the actual work being done 
will miss out on a good bit of the 'what is going on' that is part of 
getting work done since part of diagnosing a difficulty is a 'getting the 
smell of' the situation; a manager who is so close underfoot that people 
trip over her will impede progress.

>
>I also stand in wonder not just at the help desk people 
…[5 more quoted lines elided]…
>their constant "input".

Pfoo... *you* can't know anything of value; if you did then *you'd* be a 
manager.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-14T15:21:32+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b019ts$kt1$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com> <b018sm$9mj$1@panix1.panix.com>`

```

On 14-Jan-2003, docdwarf@panix.com wrote:

> Pfoo... *you* can't know anything of value; if you did then *you'd* be a
> manager.

It's irritating when you are recognized for your skill and get offered the
ultimate reward - a chance to become one of them.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-14T10:46:57-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b01bdh$ln8$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E241ADE.4030900@nycap.rr.com> <b018sm$9mj$1@panix1.panix.com> <b019ts$kt1$1@peabody.colorado.edu>`

```
In article <b019ts$kt1$1@peabody.colorado.edu>,
Howard Brazee <howard.brazee@cusys.edu> wrote:
>
>On 14-Jan-2003, docdwarf@panix.com wrote:
…[5 more quoted lines elided]…
>ultimate reward - a chance to become one of them.  

That is a behavior which seems to be manifested by most human groups; the 
ultimate compliment is to become One Of Us.  ('We', of course, are 'The 
Human Beings'.)  In the case in question (technical to management) it may 
also be an unspoken acknowledgement of one of the laws from the Book of 
Leviticus... the one that says 'Thou shalt not pay a good programmer more 
than a bad manager.'

In my own case it gets kind of sad... but perhaps that deserves another 
thread, entire, one dealing with 'What happens (at a variety of levels) 
when an offer is made to a consultant/contractor/hired gun to become a 
full-time employee?'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-14T21:37:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000019.0052aa80@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E241ADE.4030900@nycap.rr.com> <b018sm$9mj$1@panix1.panix.com> <b019ts$kt1$1@peabody.colorado.edu> <b01bdh$ln8$1@panix1.panix.com>`

```
> What happens (at a variety of levels) 
> when an offer is made to a consultant/contractor/hired gun to become a 
> full-time employee?'

To an extent it depends on your age. But most independents I know simply 
cannot work as employees - it's too constricting.

A mate of mine did it. He'd been contracting there for years, and they 
offered to take him on board. He said from the moment he joined permanent 
staff, their attitude towards him changed. No longer a contractor, they 
felt they could treat him like dirt (jeez, he thought he was already 
treated like dirt, but this was different). Rules and regulations became 
his guiding principles rather than getting a job done, and nobody 
expected anything else.

He lasted two years, resigned, and went back contracting with the same 
company.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-14T22:09:32-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b02jdc$132$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b019ts$kt1$1@peabody.colorado.edu> <b01bdh$ln8$1@panix1.panix.com> <VA.00000019.0052aa80@nildram.co.uk>`

```
In article <VA.00000019.0052aa80@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> What happens (at a variety of levels) 
>> when an offer is made to a consultant/contractor/hired gun to become a 
…[3 more quoted lines elided]…
>cannot work as employees - it's too constricting.

'Oh, you are such a wonderful, task-oriented, technically-sophisticated 
programming Free Spirit... how would you like to be enchained into a 
structure inimical to all you hold dear?'

'Well, I'm *always* willing to consider an offer... how much are you 
offering?'

'How much?  This is not a matter of Mere Money, it is one of Lifestyle and 
Philosophical Change!'

'I see... and what are these driving Changes?'

'We want to Change into a company that pays less money for your services.'

>
>A mate of mine did it. He'd been contracting there for years, and they 
…[8 more quoted lines elided]…
>company.

That last part is *very* surprising; usually it is said that when you 
leave Paradise (and many organisations, no matter how 'sick', consider 
themselves to be Paradise) the gates clang behind you, permanently closed.  
He must have had some very unusual skills or idiosyncratic knowledge.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 16)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-15T20:51:52+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000001b.001e4512@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b019ts$kt1$1@peabody.colorado.edu> <b01bdh$ln8$1@panix1.panix.com> <VA.00000019.0052aa80@nildram.co.uk> <b02jdc$132$1@panix2.panix.com>`

```
> 'We want to Change into a company that pays less money for your services.'

:-) That sound right.

> That last part is *very* surprising; usually it is said that when you 
> leave Paradise (and many organisations, no matter how 'sick', consider 
> themselves to be Paradise) the gates clang behind you, permanently closed.

Come to think of it, he might just have joined a competitor. 

> He must have had some very unusual skills or idiosyncratic knowledge.

He's in Switzerland, and he's got the ideal marriage - she's an agent. It's 
small enough that she probably knows every company he could work for. Does 
that count as idiosyncratic knowledge?

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-15T16:12:48-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b04isg$2jt$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000019.0052aa80@nildram.co.uk> <b02jdc$132$1@panix2.panix.com> <VA.0000001b.001e4512@nildram.co.uk>`

```
In article <VA.0000001b.001e4512@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> 'We want to Change into a company that pays less money for your services.'
>
>:-) That sound right.

Usually does... it is Entirely Permissible for a company to make a 
decision based on the Merely Financial - just Good Business, you know - 
and Utterly Unforgiveable for an employee/contractor to do the same.

>
>> That last part is *very* surprising; usually it is said that when you 
…[3 more quoted lines elided]…
>Come to think of it, he might just have joined a competitor. 

That makes more sense, aye.

>
>> He must have had some very unusual skills or idiosyncratic knowledge.
…[3 more quoted lines elided]…
>that count as idiosyncratic knowledge?

How he 'knows' his wife is no concern of mine, thanks.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 18)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-15T22:06:05+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000020.00623b04@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000019.0052aa80@nildram.co.uk> <b02jdc$132$1@panix2.panix.com> <VA.0000001b.001e4512@nildram.co.uk> <b04isg$2jt$1@panix1.panix.com>`

```
> Usually does... it is Entirely Permissible for a company to make a 
> decision based on the Merely Financial - just Good Business, you know - 
> and Utterly Unforgiveable for an employee/contractor to do the same.

You noticed that too? Well, of course, it just shows that you don't have 
their interests at heart, and therefore a Bad Supplier.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 19)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-15T22:24:14-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b058ku$g9b$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.0000001b.001e4512@nildram.co.uk> <b04isg$2jt$1@panix1.panix.com> <VA.00000020.00623b04@nildram.co.uk>`

```
In article <VA.00000020.00623b04@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> Usually does... it is Entirely Permissible for a company to make a 
>> decision based on the Merely Financial - just Good Business, you know - 
…[3 more quoted lines elided]…
>their interests at heart, and therefore a Bad Supplier.

It is not in the company's best interests to have someone working on 
sensitive systems who feels cheated or underpaid... so I do my meager best 
to avoid allowing this to happen.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 20)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-16T20:49:18+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000022.02be76d9@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.0000001b.001e4512@nildram.co.uk> <b04isg$2jt$1@panix1.panix.com> <VA.00000020.00623b04@nildram.co.uk> <b058ku$g9b$1@panix2.panix.com>`

```
> It is not in the company's best interests to have someone working on 
> sensitive systems who feels cheated or underpaid... so I do my meager best 
> to avoid allowing this to happen.
>
During contract negotiations, I always make the point that this is only a 
brief period of aggragvation, because when I'm working I don't want to have 
to worry about money. That same argument works when arguing about late 
payments as well.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 20)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2003-01-16T23:38:27+02:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<fh9e2v8lbvn09qo48qvd37mr7gvrojm1ks@4ax.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.0000001b.001e4512@nildram.co.uk> <b04isg$2jt$1@panix1.panix.com> <VA.00000020.00623b04@nildram.co.uk> <b058ku$g9b$1@panix2.panix.com>`

```
On 15 Jan 2003 22:24:14 -0500 docdwarf@panix.com wrote:

:>In article <VA.00000020.00623b04@nildram.co.uk>,
:>Doug Scott  <dwscott@nildram.co.uk> wrote:

:>>> Usually does... it is Entirely Permissible for a company to make a 
:>>> decision based on the Merely Financial - just Good Business, you know - 
:>>> and Utterly Unforgiveable for an employee/contractor to do the same.

:>>You noticed that too? Well, of course, it just shows that you don't have 
:>>their interests at heart, and therefore a Bad Supplier.

:>It is not in the company's best interests to have someone working on 
:>sensitive systems who feels cheated or underpaid... so I do my meager best 
:>to avoid allowing this to happen.

As seen in "Jurassic Park"?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 21)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-16T21:02:01-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b07o6p$9ij$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000020.00623b04@nildram.co.uk> <b058ku$g9b$1@panix2.panix.com> <fh9e2v8lbvn09qo48qvd37mr7gvrojm1ks@4ax.com>`

```
In article <fh9e2v8lbvn09qo48qvd37mr7gvrojm1ks@4ax.com>,
Binyamin Dissen  <postingid@dissensoftware.com> wrote:
>On 15 Jan 2003 22:24:14 -0500 docdwarf@panix.com wrote:
>
…[14 more quoted lines elided]…
>As seen in "Jurassic Park"?

As seen in many places at many times by a variety of folks.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 22)_

- **From:** SkippyPB <swiegand@NOSPAM.neo.rr.com>
- **Date:** 2003-01-17T12:48:48-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<080E7655FE5AF2FE.7D78E38A430030A8.3648C255BD504FC6@lp.airnews.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000020.00623b04@nildram.co.uk> <b058ku$g9b$1@panix2.panix.com> <fh9e2v8lbvn09qo48qvd37mr7gvrojm1ks@4ax.com> <b07o6p$9ij$1@panix1.panix.com>`

```
On 16 Jan 2003 21:02:01 -0500, docdwarf@panix.com enlightened us:

>In article <fh9e2v8lbvn09qo48qvd37mr7gvrojm1ks@4ax.com>,
>Binyamin Dissen  <postingid@dissensoftware.com> wrote:
…[20 more quoted lines elided]…
>DD

But probably not with the same consequences as witnessed in "Jurassic
Park".

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

A conference is a gathering of important people who singly
can do nothing, but together can decide that nothing can
be done. - Fred Allen 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove nospam to email me.

Steve
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 23)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-17T12:54:29-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b09g0l$b34$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <fh9e2v8lbvn09qo48qvd37mr7gvrojm1ks@4ax.com> <b07o6p$9ij$1@panix1.panix.com> <080E7655FE5AF2FE.7D78E38A430030A8.3648C255BD504FC6@lp.airnews.net>`

```
In article <080E7655FE5AF2FE.7D78E38A430030A8.3648C255BD504FC6@lp.airnews.net>,
SkippyPB  <swiegand@NOSPAM.neo.rr.com> wrote:
>On 16 Jan 2003 21:02:01 -0500, docdwarf@panix.com enlightened us:
>
…[25 more quoted lines elided]…
>Park".

Perhaps... I can barely speak of the consequences of what I have seen, let 
alone others.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** "Don Leahy" <xdb2imsN@nospam.whatever.net>
- **Date:** 2003-01-14T14:06:55-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<kdZU9.6762$fK.514668@news20.bellglobal.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com> <b018sm$9mj$1@panix1.panix.com> <b019ts$kt1$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard.brazee@cusys.edu> wrote in message
news:b019ts$kt1$1@peabody.colorado.edu...
>
> On 14-Jan-2003, docdwarf@panix.com wrote:
…[5 more quoted lines elided]…
> ultimate reward - a chance to become one of them.

My advice is:  Run.... run as fast as you can!

I accepted such a 'reward' once (at the time it was the only way to move up
the $ ladder) and regretted it.  I had to leave the company and become a
consultant in order to get my sanity back (such as it is).
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-14T20:05:05+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3E246FF6.3000404@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com> <b018sm$9mj$1@panix1.panix.com> <b019ts$kt1$1@peabody.colorado.edu> <kdZU9.6762$fK.514668@news20.bellglobal.com>`

```


Don Leahy wrote:
> "Howard Brazee" <howard.brazee@cusys.edu> wrote in message
> news:b019ts$kt1$1@peabody.colorado.edu...
…[17 more quoted lines elided]…
> 


I believe it was Groucho Marx that said "I wouldn't join any 
club that would have me as a member."  The same goes for me 
regarding a company that operates on a "direct to hire" basis.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-14T22:20:35-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b02k23$489$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b019ts$kt1$1@peabody.colorado.edu> <kdZU9.6762$fK.514668@news20.bellglobal.com> <3E246FF6.3000404@nycap.rr.com>`

```
In article <3E246FF6.3000404@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[25 more quoted lines elided]…
>regarding a company that operates on a "direct to hire" basis.

I have seen such contracts (commonly referred to as 'try before you buy', 
or 'try/buy') and two things have struck me as odd about them:

1) The rate for contracting during the 'try' period is usually a fair 
amount higher - even accounting for benefits and such - than it is for 
salaried.  For example: the contracting rate (W2, or agency-employee) is 
US$40 - US$45/hr and the fulltime salary is US$60,000/yr.

Now many folks will tell you that 'benefits' make up another 25 - 33% of 
salary... to which, of course, I say 'Oh really... now show me the cost 
breakdown of US$15,000 - US$20,000 worth of benefits given.'

'Well, there's Two Whole Weeks of vacation... after you work here for a 
full year, that is.'

'I see... and there's every other week carrying a beeper for on-call 
starting the day I show up.  That's at most an even wash... what else?'

'Ummmmmm... there's insurance.'

'You mean the insurance that you want me to 'contribute' US$100/wk to or 
else I won't get it?  Fine, I'll keep my present policy, that's a wash... 
what else?'

'Ummmmm... there's all the training we'll lavish upon you.'

'Oh really... I've been contracting here for a while, now, and the only 
people I've seen go to training of any kind are folks who inhabit 
offices... won't I be living on the cube-farm?'

'Ummmmm... yes.'

'Fine... on-call, pay for my own insurance, no training... what else?'

'Ummmmmm... well, being a full-time employee has security...'

... and let the curtain close, mercifully, on this scene.

2) So... the 'try' period is over and the client comes up and says 'All 
right, we like you, next week you come on the payroll fulltime.'  What 
prevents you from saying 'I don't want to do that... catch you later'?

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 16)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2003-01-15T03:54:10+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<CX4V9.65047$DN6.2195893@twister.austin.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b019ts$kt1$1@peabody.colorado.edu> <kdZU9.6762$fK.514668@news20.bellglobal.com> <3E246FF6.3000404@nycap.rr.com> <b02k23$489$1@panix2.panix.com>`

```
I don't know Doc. I do the full time thing for my primary pay, and right now I manage a wild bunch of contract programmers as well.
I basically get them the jobs, work out the details, arrange for them to
(mostly) work at home, get the requirements ironed out, and then I take a small, a *very* small cut of the hourly fee. It is
rewarding and a lot of fun to do that, but then I pay my mortgage out of salary. :)

Especially since every once in a while (about once a week) some client will be a slow pay. I cover the guys who need it, and charge
late fees to clients who do not pay, but still and all...

It seems I have never been able to get a work from home consulting gig that did not involve a continual nuisance of getting paid,
something that makes me very uncomfortable... :/

-Paul


<docdwarf@panix.com> wrote in message news:b02k23$489$1@panix2.panix.com...
> In article <3E246FF6.3000404@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[72 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 17)_

- **From:** Donald Tees <Donald_Tees@Sympatico.ca>
- **Date:** 2003-01-15T08:00:13-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3E25858D.8020105@Sympatico.ca>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b019ts$kt1$1@peabody.colorado.edu> <kdZU9.6762$fK.514668@news20.bellglobal.com> <3E246FF6.3000404@nycap.rr.com> <b02k23$489$1@panix2.panix.com> <CX4V9.65047$DN6.2195893@twister.austin.rr.com>`

```
Paul Raulerson wrote:
> 
> It seems I have never been able to get a work from home consulting gig that did not involve a continual nuisance of getting paid,
> something that makes me very uncomfortable... :/
> 
> -Paul


Aye, there's the rub.

Donald  <--off spending the day on receivables.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 16)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-15T14:52:55+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b03sk7$3s1$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b019ts$kt1$1@peabody.colorado.edu> <kdZU9.6762$fK.514668@news20.bellglobal.com> <3E246FF6.3000404@nycap.rr.com> <b02k23$489$1@panix2.panix.com>`

```
I work at a location I used to contract for.  I don't earn as much money, work
more hours, but my pension is much better.  I value the pension a lot.  I also
like living close to my work.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-14T21:37:07+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000018.0052a7f5@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000014.00482b97@nildram.co.uk> <avvr98$538$1@panix2.panix.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com>`

```
Robert,

> With over twenty years 
> of programming experience, you'd think I could be out of 
> their sight for a day or two and still be productive without 
> their constant "input".

Sigh. You just don't understand. In the Internet world, a week is a 
year. (That's how long it takes to clean it up).

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-01-15T13:57:17+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<f2qa2v87fbmg2hkchb0kraen29n95br2hd@4ax.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000014.00482b97@nildram.co.uk> <avvr98$538$1@panix2.panix.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com>`

```
Robert Graham <rgraham2@nycap.rr.com> wrote:

>
>
…[25 more quoted lines elided]…
>it people should be "managed".

Robert:

The book is "In Search of Excellence" and you are correct that it was
written by Tom Peters.  A few years ago, it was the bible for MBA's.

>I also stand in wonder not just at the help desk people 
>located in India who can telecommute, but also the flavor of 
…[4 more quoted lines elided]…
>their constant "input".


Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-15T09:26:52-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b03r3c$skq$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com> <f2qa2v87fbmg2hkchb0kraen29n95br2hd@4ax.com>`

```
In article <f2qa2v87fbmg2hkchb0kraen29n95br2hd@4ax.com>,
Bob Wolfe  <rtwolfe.removethis@flexus.com> wrote:
>Robert Graham <rgraham2@nycap.rr.com> wrote:

[snip]

>>Isn't that style of management based upon a book by Tom 
>>Peters (I think he wrote it) "The Search for Excellence" 
…[6 more quoted lines elided]…
>written by Tom Peters.  A few years ago, it was the bible for MBA's.

'A few years ago'?  Time sure flies when you're having fun... it came out 
in 1988.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2003-01-16T04:46:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20030115234618.14588.00000010@mb-mw.aol.com>`
- **References:** `<b03r3c$skq$1@panix1.panix.com>`

```
Let's see - in the last 9 years I've written one COBOL program with an internal
sort. For the life of me I can't remember why I did it that way either :) 
There is one other program in the system I support that has an internal sort
and maybe a dozen all together in the entire shop.  External sort is Syncsort
(and not a manual to be found). Come to think of it I don't think I've worked
at a shop that's had DFSORT (I don't think I've worked at a shop with sort
manuals either :) ).

When I was taught about internal sorts I was also told that they were
discouraged because they weren't 'structured' (PLEASE! let's not get into that
debate again here :D) The definition of 'structured' was top-down and no GOTO's
(and not this debate again either :D) and being an internal sort required one
GOTO it wasn't 'structured'.  I later learned how to code one without a GOTO
(and was told at that time in the distant past that the technique ony worked on
IBM machines - and no the person who said that was not a person associated in
anyway with IBM).

As for the 'other' discussion taking place... :)

I've been a hired gun for almost 10 years now - a bit over 7 at my current
location.  I was asked at one point about 3 years ago if I would like to become
'direct'.  I declined. The reason?  Well when I started at this location it was
company A.  Company A had marvelous benefits (one of the best educational
benefits I've ever seen was part of it), salaries were good, raises not too
bad, and good bonuses.  Company culture was laid back and moral was high.  Then
the parent company of Company A decided it wasn't profitable enough for them
(parent company does a lot of government contracts and Company A had nothing to
do with the government so wasn't raking in the bucks like the other divisions)
so it was sold.  Company B had lousy benefits, salaries were the same but
raises and bonuses sucked.  I did some math and decided that staying where I
was was a better deal and told them so.  Had they remained with the parent
company I would have jumped at the chance to go direct.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** Pat Hall <phall@certcoinc.com>
- **Date:** 2003-01-16T07:43:51-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3E26B717.534C9608@certcoinc.com>`
- **References:** `<b03r3c$skq$1@panix1.panix.com> <20030115234618.14588.00000010@mb-mw.aol.com>`

```


YukonMama wrote:

> Let's see - in the last 9 years I've written one COBOL program with an internal
> sort. For the life of me I can't remember why I did it that way either :)
…[4 more quoted lines elided]…
> manuals either :) ).

That's funny.  Our shop is just the opposite.  All of our stuff is internal sort
except for a few jobs.  Just a matter of personal preference I guess.  Maybe it was
determined by the type of data base we were using.  We are/were a Total/Supra shop
as opposed to DB2.  Maybe it is because we have had only one programmer for the
last 28 years and I'm more comfortable with internal sorts<G>  I'm probably doing
it the wrong way but hey who is there to tell me I'm wrong.  LOL

PatH...self taught some of the time but the job gets done

>
>
…[23 more quoted lines elided]…
> company I would have jumped at the chance to go direct.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2003-01-16T13:42:51+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<oedd2vobo5037g9au2l1gs1ki2lfgebf49@4ax.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b00psu$ps9$1@panix2.panix.com> <3E241ADE.4030900@nycap.rr.com> <f2qa2v87fbmg2hkchb0kraen29n95br2hd@4ax.com> <b03r3c$skq$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:

>In article <f2qa2v87fbmg2hkchb0kraen29n95br2hd@4ax.com>,
>Bob Wolfe  <rtwolfe.removethis@flexus.com> wrote:
…[17 more quoted lines elided]…
>DD

Doc:

Please forgive me for my lack of precision.  I should have said that
it was the bible for MBA's for a few years after it was published.







Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-16T09:28:38-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b06fim$po7$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <f2qa2v87fbmg2hkchb0kraen29n95br2hd@4ax.com> <b03r3c$skq$1@panix1.panix.com> <oedd2vobo5037g9au2l1gs1ki2lfgebf49@4ax.com>`

```
In article <oedd2vobo5037g9au2l1gs1ki2lfgebf49@4ax.com>,
Bob Wolfe  <rtwolfe.removethis@flexus.com> wrote:
>docdwarf@panix.com wrote:
>
>>In article <f2qa2v87fbmg2hkchb0kraen29n95br2hd@4ax.com>,
>>Bob Wolfe  <rtwolfe.removethis@flexus.com> wrote:

[snippimente]

>>>The book is "In Search of Excellence" and you are correct that it was
>>>written by Tom Peters.  A few years ago, it was the bible for MBA's.
…[8 more quoted lines elided]…
>it was the bible for MBA's for a few years after it was published.

Not to worry, old boy... it is a symptom of Getting Older.  I knew a
fellow who was hospitalised for an injury during World War II... and then
in the mid-1980s underwent a hip replacement.  I visited him while he was
recovering and he complained about the fuzziness that was induced by the
narcotics they were giving him for the pain; when I pointed out that they
were jolting him with a fair amount of dope we had the following
interchange:

'Well... yeah, they're giving me some drugs... but they didn't used to
affect me this way.'

(snort and giggle) 'Old Man, when was 'used to'?'

'Oh... forty years ago.'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 10)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-14T21:37:06+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000017.0052a45b@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000014.00482b97@nildram.co.uk> <avvr98$538$1@panix2.panix.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com>`

```
> there must be a Very Good Reason for stopping by my cube every 42 minutes 
> and breezily asking 'So... how's it going?'

Hmmm. ADH is a good reason.

> Most Valuable, Indeed.

Communication. Progress Monitoring. 

From the "Little Book of Management Bollocks":-

Willing
Able
Neat
Knowledgable
Enthusiastic
Resourceful

A good acronym.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-14T22:22:27-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b02k5j$4k9$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <VA.00000017.0052a45b@nildram.co.uk>`

```
In article <VA.00000017.0052a45b@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> there must be a Very Good Reason for stopping by my cube every 42 minutes 
>> and breezily asking 'So... how's it going?'
>
>Hmmm. ADH is a good reason.

What did you say?  Sorry, I wasn't paying attention.

>
>> Most Valuable, Indeed.
>
>Communication. Progress Monitoring. 

I communicated that it was interfering with my progress, aye.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-15T20:51:53+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000001c.001e4aaa@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <VA.00000017.0052a45b@nildram.co.uk> <b02k5j$4k9$1@panix2.panix.com>`

```
> >> there must be a Very Good Reason for stopping by my cube every 42 minutes 
> >> and breezily asking 'So... how's it going?'
…[3 more quoted lines elided]…
> What did you say?  Sorry, I wasn't paying attention.

So how's it going?

> I communicated that it was interfering with my progress, aye.

Still, apart from that, how's it going? ;-)

There's a TV show in the UK called The Office. It only ran for three series, 
and stopped. I never watched more than ten minutes of any episode, because it 
was so gut-wrenchingly real. It was a comedy, but it was like Dilbert with the 
incompetents as the heroes, and only the camera (and the viewer) knew what the 
real truth was.

I can't recommend it (because of the above), but I can say it's the real truth 
- and they were poking fun at the whole thing.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-15T16:14:35-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b04ivr$310$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000017.0052a45b@nildram.co.uk> <b02k5j$4k9$1@panix2.panix.com> <VA.0000001c.001e4aaa@nildram.co.uk>`

```
In article <VA.0000001c.001e4aaa@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> >> there must be a Very Good Reason for stopping by my cube every 42 minutes 
>> >> and breezily asking 'So... how's it going?'
…[5 more quoted lines elided]…
>So how's it going?

Same as it went the last time you asked, only 42 minutes later.

>
>> I communicated that it was interfering with my progress, aye.
>
>Still, apart from that, how's it going? ;-)

Same as it went the first time you asked, only an hour and twenty-four 
minutes later.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-15T22:06:06+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000021.00623e11@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000017.0052a45b@nildram.co.uk> <b02k5j$4k9$1@panix2.panix.com> <VA.0000001c.001e4aaa@nildram.co.uk> <b04ivr$310$1@panix1.panix.com>`

```
> Same as it went the first time you asked, only an hour and twenty-four 
> minutes later.

Hmm I left you alone for an hour and 24 minutes, and nothing's changed!??

[Thinks: Must keep a closer watch]

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-15T22:25:55-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b058o3$gre$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.0000001c.001e4aaa@nildram.co.uk> <b04ivr$310$1@panix1.panix.com> <VA.00000021.00623e11@nildram.co.uk>`

```
In article <VA.00000021.00623e11@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> Same as it went the first time you asked, only an hour and twenty-four 
>> minutes later.
>
>Hmm I left you alone for an hour and 24 minutes, and nothing's changed!??

No... now please go away and let me Do My Job.

>
>[Thinks: Must keep a closer watch]

I do not see how it would change the task at hand if you kept it so tight 
that your fingers turned purple and fell off... now please go away and let 
me Do My Job.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 16)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-16T20:49:23+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000023.02be8733@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.0000001c.001e4aaa@nildram.co.uk> <b04ivr$310$1@panix1.panix.com> <VA.00000021.00623e11@nildram.co.uk> <b058o3$gre$1@panix2.panix.com>`

```
> I do not see how it would change the task at hand if you kept it so tight 
> that your fingers turned purple and fell off... now please go away and let 
> me Do My Job.

Geez, that guy over there has a real hangup about progress monitoring. I';m 
not sure if we can handle a guy with an attitude like that.


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 17)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-16T21:03:11-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b07o8v$9t6$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000021.00623e11@nildram.co.uk> <b058o3$gre$1@panix2.panix.com> <VA.00000023.02be8733@nildram.co.uk>`

```
In article <VA.00000023.02be8733@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> I do not see how it would change the task at hand if you kept it so tight 
>> that your fingers turned purple and fell off... now please go away and let 
…[3 more quoted lines elided]…
>not sure if we can handle a guy with an attitude like that.

If my attitude is all that you have to be concerned about then my Work 
must be very good... now please go away and let me Do My Job.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 18)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-17T02:09:00+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E276847.8060802@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000021.00623e11@nildram.co.uk> <b058o3$gre$1@panix2.panix.com> <VA.00000023.02be8733@nildram.co.uk> <b07o8v$9t6$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <VA.00000023.02be8733@nildram.co.uk>,
> Doug Scott  <dwscott@nildram.co.uk> wrote:
…[13 more quoted lines elided]…
> 

You know, if you want us to just go away so you can just do 
your job, all you have to do is say so.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 19)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-16T21:37:29-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b07q99$qis$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000023.02be8733@nildram.co.uk> <b07o8v$9t6$1@panix1.panix.com> <3E276847.8060802@nycap.rr.com>`

```
In article <3E276847.8060802@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[17 more quoted lines elided]…
>your job, all you have to do is say so.

Good... consider this my saying so.  Now please go away and let me Do My 
Job.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 20)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-17T11:21:36+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E27E9CD.5060509@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000023.02be8733@nildram.co.uk> <b07o8v$9t6$1@panix1.panix.com> <3E276847.8060802@nycap.rr.com> <b07q99$qis$1@panix2.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E276847.8060802@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[9 more quoted lines elided]…
> 

Considering the number of posts with your name on them, one 
would suspect that your job is POSTING to these groups. :)
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 21)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-17T10:38:27-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0981j$1ol$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E276847.8060802@nycap.rr.com> <b07q99$qis$1@panix2.panix.com> <3E27E9CD.5060509@nycap.rr.com>`

```
In article <3E27E9CD.5060509@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[15 more quoted lines elided]…
>would suspect that your job is POSTING to these groups. :)

Suspicions are curious things, indeed... and those who sign my timesheets 
appear to be rather satisfied with how I do my job, aye.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 20)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-17T14:57:47+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b095la$2t4$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000023.02be8733@nildram.co.uk> <b07o8v$9t6$1@panix1.panix.com> <3E276847.8060802@nycap.rr.com> <b07q99$qis$1@panix2.panix.com>`

```

On 16-Jan-2003, docdwarf@panix.com wrote:

> >> If my attitude is all that you have to be concerned about then my Work
> >> must be very good... now please go away and let me Do My Job.
…[5 more quoted lines elided]…
> Good... consider this my saying so.  Now please go away and let me Do My

OK, I'm stepping away so that you can Do Your Job.
....

Why did you Do Your Job that way?   Shouldn't you have done it This Way?  It's
hard supervising from behind your back.   Maybe you should accept a promotion so
that you can supervise as well, instead of insulting us by preferring to
accomplish stuff.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 21)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-17T10:44:30-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b098cu$33l$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E276847.8060802@nycap.rr.com> <b07q99$qis$1@panix2.panix.com> <b095la$2t4$1@peabody.colorado.edu>`

```
In article <b095la$2t4$1@peabody.colorado.edu>,
Howard Brazee <howard.brazee@cusys.edu> wrote:
>
>On 16-Jan-2003, docdwarf@panix.com wrote:
…[13 more quoted lines elided]…
>Why did you Do Your Job that way?

Because it seemed to be a good idea at the time.

>Shouldn't you have done it This Way?

No.

>It's
>hard supervising from behind your back.

If it were easy than *anyone* could do it; since not anyone can do it then 
it is *your* job.

>Maybe you should accept a promotion so
>that you can supervise as well, instead of insulting us by preferring to
>accomplish stuff.

If someone of sufficient authority asks me out for a meal I just *might* 
have an appetite.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 18)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-19T21:31:46+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000024.047775f4@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000021.00623e11@nildram.co.uk> <b058o3$gre$1@panix2.panix.com> <VA.00000023.02be8733@nildram.co.uk> <b07o8v$9t6$1@panix1.panix.com>`

```
> If my attitude is all that you have to be concerned about then my Work 
> must be very good... now please go away and let me Do My Job.

:-) 100% for effort.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 19)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T18:14:48-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0fbh8$7gb$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000023.02be8733@nildram.co.uk> <b07o8v$9t6$1@panix1.panix.com> <VA.00000024.047775f4@nildram.co.uk>`

```
In article <VA.00000024.047775f4@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> If my attitude is all that you have to be concerned about then my Work 
>> must be very good... now please go away and let me Do My Job.
>
>:-) 100% for effort.

I am a consultant; I get paid for results, not efforts... now please go 
away and let me Do My Job.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 20)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-20T20:22:08+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000025.002657c1@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000023.02be8733@nildram.co.uk> <b07o8v$9t6$1@panix1.panix.com> <VA.00000024.047775f4@nildram.co.uk> <b0fbh8$7gb$1@panix1.panix.com>`

```
> I am a consultant; I get paid for results, not efforts...

You don't charge by the hour then? I'd LOVE to be paid by results.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 21)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-20T15:27:55-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0hm4b$6et$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000024.047775f4@nildram.co.uk> <b0fbh8$7gb$1@panix1.panix.com> <VA.00000025.002657c1@nildram.co.uk>`

```
In article <VA.00000025.002657c1@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> I am a consultant; I get paid for results, not efforts...
>
>You don't charge by the hour then? I'd LOVE to be paid by results.

What I charge by and what I get paid for might not always be the same 
thing.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 22)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-20T22:01:37+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000027.00816c36@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000024.047775f4@nildram.co.uk> <b0fbh8$7gb$1@panix1.panix.com> <VA.00000025.002657c1@nildram.co.uk> <b0hm4b$6et$1@panix1.panix.com>`

```
> What I charge by and what I get paid for might not always be the same 
> thing.

I'm still trying to get one particular company to accept a fixed-price 
maintenance agreement for a set of systems. I've got the staff to do it 
(with many years' experience on those systems), but they'd rather give 
the work to outsourcers. Groan!

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 23)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-20T17:06:58-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0hru2$3e3$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000025.002657c1@nildram.co.uk> <b0hm4b$6et$1@panix1.panix.com> <VA.00000027.00816c36@nildram.co.uk>`

```
In article <VA.00000027.00816c36@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> What I charge by and what I get paid for might not always be the same 
>> thing.
…[4 more quoted lines elided]…
>the work to outsourcers.

I've heard that this is All the Latest Fashion.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 24)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-21T21:24:54+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000028.0057779c@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000025.002657c1@nildram.co.uk> <b0hm4b$6et$1@panix1.panix.com> <VA.00000027.00816c36@nildram.co.uk> <b0hru2$3e3$1@panix1.panix.com>`

```
> I've heard that this is All the Latest Fashion.

These are from the sub-continent. They needed to use one of my guys but 
wouldn't let him work from home (he's 100 miles from the site). 

No problems if they're 8,000 miles away, though.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 25)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T20:09:33-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0kr0d$85g$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000027.00816c36@nildram.co.uk> <b0hru2$3e3$1@panix1.panix.com> <VA.00000028.0057779c@nildram.co.uk>`

```
In article <VA.00000028.0057779c@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> I've heard that this is All the Latest Fashion.
>
>These are from the sub-continent.

Das Bootland?

>They needed to use one of my guys but 
>wouldn't let him work from home (he's 100 miles from the site). 
>
>No problems if they're 8,000 miles away, though.

Of course not... you see, 8,000 is eighty times one hundred.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 26)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-22T21:12:06+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000002c.00375c7d@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000027.00816c36@nildram.co.uk> <b0hru2$3e3$1@panix1.panix.com> <VA.00000028.0057779c@nildram.co.uk> <b0kr0d$85g$1@panix1.panix.com>`

```
> >These are from the sub-continent.
> 
> Das Bootland?

India/Pakistan.

> Of course not... you see, 8,000 is eighty times one hundred.

Um.... 

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 27)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-22T22:01:16-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0nlts$i5b$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000028.0057779c@nildram.co.uk> <b0kr0d$85g$1@panix1.panix.com> <VA.0000002c.00375c7d@nildram.co.uk>`

```
In article <VA.0000002c.00375c7d@nildram.co.uk>,
Doug Scott  <dwscott@nildram.co.uk> wrote:
>> >These are from the sub-continent.
>> 
>> Das Bootland?
>
>India/Pakistan.

Ah, that clarifies things... I was not sure because I am not a 
sub-scriber.

>
>> Of course not... you see, 8,000 is eighty times one hundred.
>
>Um.... 

Putting it that simply can leave one speechless, aye.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** weberm@polaris.net (Ubiquitous)
- **Date:** 2003-01-21T20:03:43-06:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<dsGcnQZwi41iZrCjXTWcpQ@comcast.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <VA.00000016.003cb7f3@nildram.co.uk> <b00psu$ps9$1@panix2.panix.com> <VA.00000017.0052a45b@nildram.co.uk> <b02k5j$4k9$1@panix2.panix.com> <VA.0000001c.001e4aaa@nildram.co.uk>`

```
In article <VA.0000001c.001e4aaa@nildram.co.uk>, dwscott@nildram.co.uk wrote:

>There's a TV show in the UK called The Office. It only ran for three series, 
>and stopped. I never watched more than ten minutes of any episode, because it 
>was so gut-wrenchingly real. It was a comedy, but it was like Dilbert with the 
>incompetents as the heroes, and only the camera (and the viewer) knew what the 
>real truth was.

That reminds me of a little movie called "Office Space"...
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-13T13:15:51-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<avuvon$608$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com>`

```
In article <3E21743F.9060507@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:

[snip]

>As two someone else's pointed out, lots can be done with 
>DFSORT and SyncSort - you just have to know how, and lots of 
…[7 more quoted lines elided]…
>(or at least EASY) in an external sort.

Well... I've seen what I would call 'incredibly complex and intricate' 
DFSORT and SyncSort jobs and in keeping with the 'two-year programmer' 
rule for maintenance I try to avoid doing such things.  If it requires 
more than an OMIT/INCLUDE and a SUM FIELDS I'll do an extractive sort step 
and follow it with a COBOL program that does the 'heavy lifting'.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-13T18:41:49+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<avv19d$epr$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com>`

```

On 13-Jan-2003, docdwarf@panix.com wrote:

> Well... I've seen what I would call 'incredibly complex and intricate'
> DFSORT and SyncSort jobs and in keeping with the 'two-year programmer'
> rule for maintenance I try to avoid doing such things.  If it requires
> more than an OMIT/INCLUDE and a SUM FIELDS I'll do an extractive sort step
> and follow it with a COBOL program that does the 'heavy lifting'.

Or if I can't comment each command with a couple of words to the right.

With people using different languages the displacement/position problem occurs -
so I like typing in the name of each field that I reference.

e.g.
SORT FIELDS=(01,09,CH,A)            STUDENT ID
SUM FIELDS=NONE                     ELIMINATE DUPLICATES
DEBUG ABEND                         ABORT IF ERRORS
RECORD TYPE=F,LENGTH=80             CONTINUE WITH EMPTY INPUT FILE
END
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** Frank Yaeger <fyaeger@vnet.ibm.com>
- **Date:** 2003-01-13T11:17:58-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3E2310E6.4010406@vnet.ibm.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <avv19d$epr$1@peabody.colorado.edu>`

```
Howard Brazee wrote:

>With people using different languages the displacement/position problem occurs -
>so I like typing in the name of each field that I reference.
…[8 more quoted lines elided]…
>
DFSORT allows the use of Symbols for fields and constants in DFSORT and 
ICETOOL statements, so you could use them for "doc" if you like, e.g.

//SYMNAMES DD *
Student_Id,1,9,CH
//SYSIN DD *
  SORT FIELDS=(Student_Id,A)
/*

DFSORT also allows full line comments (* comment) and blanks before or 
after each statement, and remarks (like you show above) on each 
statement.  So you can get pretty descriptive.

For more information on DFSORT Symbols, see:

http://publibz.boulder.ibm.com/cgi-bin/bookmgr_OS390/BOOKS/ICECA109/7.0?DT=20020722140254

For a tool to convert COBOL COPYs to DFSORT symbols, see:

http://taz.vv.sebank.se/cgi-bin/pts3/pow/kampanjer/it_partner/
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 5)_

- **From:** Harald Hinz <harald.hinz@ewetel.net>
- **Date:** 2003-01-18T12:48:03+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<jteb0b.0n7.ln@news.hinznet.home>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com>`

```
docdwarf@panix.com schrieb in news:avuvon$608$1@panix1.panix.com:

> Well... I've seen what I would call 'incredibly complex and intricate' 
> DFSORT and SyncSort jobs and in keeping with the 'two-year programmer' 
> rule for maintenance I try to avoid doing such things.  If it requires 
> more than an OMIT/INCLUDE and a SUM FIELDS I'll do an extractive sort step 
> and follow it with a COBOL program that does the 'heavy lifting'.

Ack. In 20 years in MVS environment I had only one exception to this. I had 
to fix a 7 year old production job doing silly things an a mission critical
path every day. It was obvious, that the input file had to be sorted before
calling the program, but....

JCL: available
LoadModule: available
COBOl source: you're kidd'n (lost somewhere)
Former sort pre-step: dunno....
Input file: long, very long, incredibly long and sorted 'very special'
documentation: see->documentation

It's 17 years ago but I still remember the job's name: X55110T

I never made it run - and, like others, found it easier to redesign the whole 
process from scratch.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 6)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-18T10:44:58-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0bspq$2jf$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home>`

```
In article <jteb0b.0n7.ln@news.hinznet.home>,
Harald Hinz  <harald.hinz@ewetel.net> wrote:
>docdwarf@panix.com schrieb in news:avuvon$608$1@panix1.panix.com:
>
…[8 more quoted lines elided]…
>path every day.

It has been said that 'every situation has an exception' is inviolably 
true, just as 'all things are relative' is absolutely correct.

On the other hand... never believe anything you read on UseNet, including 
this statement.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 7)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-01-18T18:56:48+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<1fac2PBwNaK+EwX8@ld50macca.demon.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com>`

```
In article <b0bspq$2jf$1@panix2.panix.com>, docdwarf@panix.com writes
>It has been said that 'every situation has an exception' is inviolably
>true, just as 'all things are relative' is absolutely correct.
>DD
If you follow Bertrand Russell's criticisms of set logic then your 
statement that
>'every situation has an exception' is inviolably
>true
must, itself, have an exception which violates the self evident 
axiomatic truth.

I think that is two nil to me so far.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-18T16:02:27-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<v2jfik3jr8nbae@corp.supernews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk>`

```

Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in message
news:1fac2PBwNaK+EwX8@ld50macca.demon.co.uk...
> In article <b0bspq$2jf$1@panix2.panix.com>, docdwarf@panix.com writes
> >It has been said that 'every situation has an exception' is inviolably
…[7 more quoted lines elided]…
> axiomatic truth.

I think ths may be explained in terms of knowledge; that is,
the known versus the unknown.

When we describe a 'situation' we use the known. The 'exception'
is the unknown.

Once the formerly unknown is incorporated into the 'situation'
(the known), The 'exception' remains the unknown. There is
no violation!

'All crows are black.' until someone finds a crow that is white.
'Most crows are black. Some are white.' until someone finds
a crow that is green.
'Most crows are black. Some are white or green.' until someone
finds a crow that is ....
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-18T21:56:22-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0d44m$5is$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <v2jfik3jr8nbae@corp.supernews.com>`

```
In article <v2jfik3jr8nbae@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
>Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in message
…[13 more quoted lines elided]…
>the known versus the unknown.

... or it might be that someone has a bit of difficulty seeing what should 
be the readily obvious absurdity and contradiction of '... 'all things are 
relative' is absolutely correct.'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 8)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-18T18:46:29-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<v2jp67k1o1rr9b@corp.supernews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk>`

```

Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in message
news:1fac2PBwNaK+EwX8@ld50macca.demon.co.uk...
> In article <b0bspq$2jf$1@panix2.panix.com>, docdwarf@panix.com writes
> >It has been said that 'every situation has an exception' is inviolably
…[9 more quoted lines elided]…
> I think that is two nil to me so far.

In my earlier response, I mistook exception to statement as
exception to exception. I then recalled "Russell's paradox."

Russell provided an answer. I quote Antony Flew, "A Dictionary
of Philosophy";

"Russell's solution to the paradox was to say that self-refering
statements are without meaning, and in particular, to speak of
'all statements' is meaningless. Instead we must speak of sets
of statements that form a genuine totality. A statement refering
to other statements must, Russell says, be of a different type
from, a higher order than, the statements it is about. So we
must say that the class of all first order classes which are not
members of themselves is a second order class, and hence it
will be 'obvious nonsense' to say of a class either that it is or
that it isn't a member of itself. Thus the paradox disappears."
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-18T22:00:34-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0d4ci$6fl$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <v2jp67k1o1rr9b@corp.supernews.com>`

```
In article <v2jp67k1o1rr9b@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
>Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in message
…[22 more quoted lines elided]…
>'all statements' is meaningless.

In other words... Russell seems to have said 'If my system cannot account 
for it then it must have no meaning'.

This may be a reason why Wittgenstein tended to refer to 'meaning' as the 
result of 'interpretation', rather than something standing, distinct and 
alone, and of which a circumstance 'partook' as things did of the Socratic 
Forms (that which is 'good' is such because it partakes of the 
Form/Essence/Gr. 'eidos' of The Good.)

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 10)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-19T07:20:22-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<v2l5cec2jtmoaa@corp.supernews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <v2jp67k1o1rr9b@corp.supernews.com> <b0d4ci$6fl$1@panix2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b0d4ci$6fl$1@panix2.panix.com...
> In article <v2jp67k1o1rr9b@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
…[33 more quoted lines elided]…
> Form/Essence/Gr. 'eidos' of The Good.)

Perhaps, I am missing something; but I see no great distinction
between these two. If a circumstance partakes of the essence
'meaningless', Wittgenstein might include the circumstance; but
be unable to do more with it. Russell would exclude the
circumstance because nothing more can be done with it.

This, of course, assumes that one's purpose is the analysis of
a circumstance.

I have not read either author, which may explain why I may be
missing something.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T09:18:23-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0ec3f$6us$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <v2jp67k1o1rr9b@corp.supernews.com> <b0d4ci$6fl$1@panix2.panix.com> <v2l5cec2jtmoaa@corp.supernews.com>`

```
In article <v2l5cec2jtmoaa@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:b0d4ci$6fl$1@panix2.panix.com...
…[41 more quoted lines elided]…
>circumstance because nothing more can be done with it.

Not quite... for Russell 'meaning' appears to exist outside of the 
condition to which the term is applied while for Wittgenstein 'meaning' 
exists only as the result of 'interpretation' (which is an activity).  
What you posit as Russell's 'exclud(ing) the circumstance because nothimg 
more can be done with it' then becomes, in Wittgenstein's view, Russell's 
excluding because *Russell* can do nothing more with it.

>
>This, of course, assumes that one's purpose is the analysis of
…[3 more quoted lines elided]…
>missing something.

You've not read Wittgenstein?  I envy your ability to go through his works 
for the first time.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-19T11:36:20-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<v2lkbtio6qv199@corp.supernews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <v2jp67k1o1rr9b@corp.supernews.com> <b0d4ci$6fl$1@panix2.panix.com> <v2l5cec2jtmoaa@corp.supernews.com> <b0ec3f$6us$1@panix2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b0ec3f$6us$1@panix2.panix.com...
> In article <v2l5cec2jtmoaa@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:b0d4ci$6fl$1@panix2.panix.com...
> >> In article <v2jp67k1o1rr9b@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[3 more quoted lines elided]…
> >> >> In article <b0bspq$2jf$1@panix2.panix.com>, docdwarf@panix.com
writes
> >> >> >It has been said that 'every situation has an exception' is
inviolably
> >> >> >true, just as 'all things are relative' is absolutely correct.
> >> >> >DD
…[19 more quoted lines elided]…
> >> In other words... Russell seems to have said 'If my system cannot
account
> >> for it then it must have no meaning'.
> >>
> >> This may be a reason why Wittgenstein tended to refer to 'meaning' as
the
> >> result of 'interpretation', rather than something standing, distinct
and
> >> alone, and of which a circumstance 'partook' as things did of the
Socratic
> >> Forms (that which is 'good' is such because it partakes of the
> >> Form/Essence/Gr. 'eidos' of The Good.)
…[12 more quoted lines elided]…
> excluding because *Russell* can do nothing more with it.

Ok! [After reviewing Flew's entry on Wittgenstein.] Then, with
respect to the terms 'binary computer' and 'binary weapon'. For
Russell, the meanings might be 'a machine using two states as
its basis for operation' and 'a device using two chemicals as its
basis for operation'. For Wittgenstein, the meanings might be
'a facinating machine' and 'a dangerous device'.

And, for 'self-refering statements', Russell says 'meaningless'
while Wittgenstein might say 'someone is playing tricks with the
language'.

Is that about right?

> >
> >This, of course, assumes that one's purpose is the analysis of
…[6 more quoted lines elided]…
> for the first time.

The only philosophy I have read in depth is Sartre's "Being
and Nothingness". I am concerned that one day I may actually
understand what Sartre is saying!
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T11:59:35-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0elhn$k99$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <v2l5cec2jtmoaa@corp.supernews.com> <b0ec3f$6us$1@panix2.panix.com> <v2lkbtio6qv199@corp.supernews.com>`

```
In article <v2lkbtio6qv199@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:b0ec3f$6us$1@panix2.panix.com...
…[60 more quoted lines elided]…
>'a facinating machine' and 'a dangerous device'.

These might be reasonable conclusions... but it might also be that a bit 
more study than a reference to a secondary source could reveal that things 
would be categorised in a less facile manner.

>
>And, for 'self-refering statements', Russell says 'meaningless'
…[3 more quoted lines elided]…
>Is that about right?

Ummmmm... a bit more study, as mentioned before.  Consider the statement 
of 'One part of this sentence is written in English und das zweite Teil 
wird auf Deutsch geschrieben.'

(Wittgenstein also asked about where 'truth' is in the circumstance of a 
parrot saying 'I don't understand a word that I'm saying'... but that 
might be saved for later studies.)

>
>> >
…[11 more quoted lines elided]…
>understand what Sartre is saying!

'Understanding' and another phenomenon, entire; Ol' Davey Hume wrote an 
entire Critique about it.  Consider a possible interchange with a Pouting 
Adolescent:

'But you just don't *understand*!'

'I *do* understand... I just do not agree.'

'But... if you *understood* then you'd *have* to agree!'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-01-19T14:58:48-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<v2m07ide9bku7d@corp.supernews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <v2l5cec2jtmoaa@corp.supernews.com> <b0ec3f$6us$1@panix2.panix.com> <v2lkbtio6qv199@corp.supernews.com> <b0elhn$k99$1@panix2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b0elhn$k99$1@panix2.panix.com...
> In article <v2lkbtio6qv199@corp.supernews.com>,
> Rick Smith <ricksmith@mfi.net> wrote:
> >
> ><docdwarf@panix.com> wrote in message
news:b0ec3f$6us$1@panix2.panix.com...
> >> In article <v2l5cec2jtmoaa@corp.supernews.com>,
> >> Rick Smith <ricksmith@mfi.net> wrote:
…[8 more quoted lines elided]…
> >> >> >> In article <b0bspq$2jf$1@panix2.panix.com>, docdwarf@panix.com
writes
> >> >> >> >It has been said that 'every situation has an exception' is
inviolably
> >> >> >> >true, just as 'all things are relative' is absolutely correct.
> >> >> >> >DD
> >> >> >> If you follow Bertrand Russell's criticisms of set logic then
your
> >> >> >> statement that
> >> >> >> >'every situation has an exception' is inviolably
…[16 more quoted lines elided]…
> >> >> In other words... Russell seems to have said 'If my system cannot
account
> >> >> for it then it must have no meaning'.
> >> >>
> >> >> This may be a reason why Wittgenstein tended to refer to 'meaning'
as the
> >> >> result of 'interpretation', rather than something standing, distinct
and
> >> >> alone, and of which a circumstance 'partook' as things did of the
Socratic
> >> >> Forms (that which is 'good' is such because it partakes of the
> >> >> Form/Essence/Gr. 'eidos' of The Good.)
…[10 more quoted lines elided]…
> >> What you posit as Russell's 'exclud(ing) the circumstance because
nothimg
> >> more can be done with it' then becomes, in Wittgenstein's view,
Russell's
> >> excluding because *Russell* can do nothing more with it.
> >
…[20 more quoted lines elided]…
> wird auf Deutsch geschrieben.'

Hmm! A bit more study in German!

> (Wittgenstein also asked about where 'truth' is in the circumstance of a
> parrot saying 'I don't understand a word that I'm saying'... but that
> might be saved for later studies.)

Hmm! A bit more study in parrotese! <g>

> >> >
> >> >This, of course, assumes that one's purpose is the analysis of
…[5 more quoted lines elided]…
> >> You've not read Wittgenstein?  I envy your ability to go through his
works
> >> for the first time.
> >
…[12 more quoted lines elided]…
> 'But... if you *understood* then you'd *have* to agree!'

A reasonable conclusion from one point of view! <g>

I am in a similar situation in the role of the Pouting Adolescent.
The other party is a reluctant member of Congress.

With my first letter, I received a cordial response.
With my second letter, I received no response.
My third letter will go to an outside agency, with a 'cc' to
the member of Congress.
And, I am preparing for an 'end run' through Federal Court,
if necessary.

If a reluctant member of Congress won't agree, maybe an
impartial Federal judge will.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T18:25:20-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0fc50$8ub$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <v2lkbtio6qv199@corp.supernews.com> <b0elhn$k99$1@panix2.panix.com> <v2m07ide9bku7d@corp.supernews.com>`

```
In article <v2m07ide9bku7d@corp.supernews.com>,
Rick Smith <ricksmith@mfi.net> wrote:
>
><docdwarf@panix.com> wrote in message news:b0elhn$k99$1@panix2.panix.com...
>> In article <v2lkbtio6qv199@corp.supernews.com>,
>> Rick Smith <ricksmith@mfi.net> wrote:

[die kleine snippigkeit]

>> >The only philosophy I have read in depth is Sartre's "Being
>> >and Nothingness". I am concerned that one day I may actually
…[12 more quoted lines elided]…
>A reasonable conclusion from one point of view! <g>

When such 'reason' equates 'understanding' with 'agreement', perhaps.

>
>I am in a similar situation in the role of the Pouting Adolescent.
…[10 more quoted lines elided]…
>impartial Federal judge will.

'But it is readily apparent, Your Honor, that the plaintiff has no cause 
for complaint... he's received more than a form letter!'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-01-19T23:05:17+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<AnNRIeBt8yK+Ewy3@ld50macca.demon.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <v2jp67k1o1rr9b@corp.supernews.com> <b0d4ci$6fl$1@panix2.panix.com> <v2l5cec2jtmoaa@corp.supernews.com> <b0ec3f$6us$1@panix2.panix.com>`

```
In article <b0ec3f$6us$1@panix2.panix.com>, docdwarf@panix.com writes
>You've not read Wittgenstein?  I envy your ability to go through his works
>for the first time.
>
>DD
>
How can you type that without a smiley emoticon?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T18:26:23-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0fc6v$94d$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <v2l5cec2jtmoaa@corp.supernews.com> <b0ec3f$6us$1@panix2.panix.com> <AnNRIeBt8yK+Ewy3@ld50macca.demon.co.uk>`

```
In article <AnNRIeBt8yK+Ewy3@ld50macca.demon.co.uk>,
Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
>In article <b0ec3f$6us$1@panix2.panix.com>, docdwarf@panix.com writes
>>You've not read Wittgenstein?  I envy your ability to go through his works
…[4 more quoted lines elided]…
>How can you type that without a smiley emoticon?

Why... just the way that I did it,  right above.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-01-19T23:03:05+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<fn8WY6Ap6yK+Ewwy@ld50macca.demon.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <v2jp67k1o1rr9b@corp.supernews.com>`

```
In article <v2jp67k1o1rr9b@corp.supernews.com>, Rick Smith 
<ricksmith@mfi.net> writes
>
>In my earlier response, I mistook exception to statement as
…[15 more quoted lines elided]…
>
And that sounds like the philosophical notion that all chairs refer to a 
universal model of chairs which must in turn refer to a universal model 
of models. Or is that an explanation of object oriented programming?

BTW, I know that the model theory is no longer current.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T18:30:38-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0fceu$9jg$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <v2jp67k1o1rr9b@corp.supernews.com> <fn8WY6Ap6yK+Ewwy@ld50macca.demon.co.uk>`

```
In article <fn8WY6Ap6yK+Ewwy@ld50macca.demon.co.uk>,
Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
>In article <v2jp67k1o1rr9b@corp.supernews.com>, Rick Smith 
><ricksmith@mfi.net> writes
…[20 more quoted lines elided]…
>of models.

'(T)he philosophical notion' to which you refer, Mr MacLean, was 
addressed in an earlier posting (Socrates referred to such a thing as an 
'eidos').

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 9)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-01-20T03:54:18+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2B72E7.1030301@optonline.NOSPAM.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <v2jp67k1o1rr9b@corp.supernews.com>`

```
Rick Smith wrote:
> Alistair Maclean <alistair@ld50macca.demon.co.uk> wrote in message
> news:1fac2PBwNaK+EwX8@ld50macca.demon.co.uk...
…[33 more quoted lines elided]…
> that it isn't a member of itself. Thus the paradox disappears."

This Russell guy was pretty clever, wasn't he?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-18T21:54:33-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0d419$543$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk>`

```
In article <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk>,
Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
>In article <b0bspq$2jf$1@panix2.panix.com>, docdwarf@panix.com writes
>>It has been said that 'every situation has an exception' is inviolably
…[7 more quoted lines elided]…
>axiomatic truth.


If you read the sentence in its entirety you might see that not only 
is 'every situation has an exception' is not 'my' statement - in that 
it is labelled, clearly and unambiguously, as something which 'has been 
said' - but you could learn that its purported inviolable veracity is of 
the same fashion  - 'just as' - as another statement.

>
>I think that is two nil to me so far.

It may be that you would wish to reconsider this conclusion in light of 
what has just been pointed out to you.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 9)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-01-19T23:12:31+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<IGBDABCfDzK+EwBA@ld50macca.demon.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <b0d419$543$1@panix2.panix.com>`

```
In article <b0d419$543$1@panix2.panix.com>, docdwarf@panix.com writes
>In article <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk>,
>Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
…[24 more quoted lines elided]…
>DD

The use of a smoking gun belonging to another does not absolve you of 
the crime.
I did read the sentence in it's entirety and have re-read it several 
times since. What is your case for denouncing that all things are 
relative?

>
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T18:49:24-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0fdi4$cjn$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <b0d419$543$1@panix2.panix.com> <IGBDABCfDzK+EwBA@ld50macca.demon.co.uk>`

```
In article <IGBDABCfDzK+EwBA@ld50macca.demon.co.uk>,
Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
>In article <b0d419$543$1@panix2.panix.com>, docdwarf@panix.com writes
>>In article <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk>,
…[28 more quoted lines elided]…
>the crime.

It appears to take a curious sense of logic - and justice - to not see 
that pointing out that others have held smoking guns does not, in any way, 
implicate me in their crimes.

>I did read the sentence in it's entirety and have re-read it several 
>times since. What is your case for denouncing that all things are 
>relative?

My most sincere and abject apologies, Mr MacLean; I did not realise that I 
was, once again, waxing so obscure that the point which I was trying to 
make was hidden.  I thought that this 'denounciation' was readily 
apparent from the formulation I employed; permit me to be a bit more 
explicit.

I wrote 'It has been said that 'every situation has an exception' is 
inviolably true, just as 'all things are relative' is absolutely correct.'

Now consider the formulation ''All things are relative' is absolutely 
correct.'  This statement is either true or not true.

If 'all things are relative' is not true then the statement is 
not absolutely correct.

If 'all things are relative' is true then there are no absolutes; if there 
are no absolutes then nothing can be absolutely correct.  If nothing can 
be absolutely correct then 'all things are relative' cannot be absolutely 
correct, therefore the statement is not true.

So... if 'something' is said to be as 'inviolably true' as 'all things are 
relative' is 'absolutely correct' then it just might be possible that 
someone is trying to make a small joke which will have to be explained.

Have I been able to make myself suitably clear, Mr Maclean?

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** Alistair Maclean <alistair@ld50macca.demon.co.uk>
- **Date:** 2003-01-20T20:05:35+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<twUqdwBPaFL+EwOL@ld50macca.demon.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <1fac2PBwNaK+EwX8@ld50macca.demon.co.uk> <b0d419$543$1@panix2.panix.com> <IGBDABCfDzK+EwBA@ld50macca.demon.co.uk> <b0fdi4$cjn$1@panix1.panix.com>`

```
In article <b0fdi4$cjn$1@panix1.panix.com>, docdwarf@panix.com writes
>>The use of a smoking gun belonging to another does not absolve you of
>>the crime.
…[4 more quoted lines elided]…
>
I'll concede that point.

>If 'all things are relative' is not true then the statement is
>not absolutely correct.
…[13 more quoted lines elided]…
>
Yes, thanks for the philosophy lesson.

That's three - two to you.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T14:59:30-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0k8r2$b8r$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <IGBDABCfDzK+EwBA@ld50macca.demon.co.uk> <b0fdi4$cjn$1@panix1.panix.com> <twUqdwBPaFL+EwOL@ld50macca.demon.co.uk>`

```
In article <twUqdwBPaFL+EwOL@ld50macca.demon.co.uk>,
Alistair Maclean  <alistair@ld50macca.demon.co.uk> wrote:
>In article <b0fdi4$cjn$1@panix1.panix.com>, docdwarf@panix.com writes
>>>The use of a smoking gun belonging to another does not absolve you of
…[6 more quoted lines elided]…
>I'll concede that point.

Most gracious of you.

>
>>If 'all things are relative' is not true then the statement is
…[14 more quoted lines elided]…
>Yes, thanks for the philosophy lesson.

Philosophy?  It seems to be more an explanation involving grammar and 
logic.

>
>That's three - two to you.

It is to be hoped that this system of accounting is sensible to someone.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 7)_

- **From:** "Peter E.C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2003-01-19T10:19:54
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3e2a7c2e_11@news.newsgroups.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com>`

```

<docdwarf@panix.com> wrote in message news:b0bspq$2jf$1@panix2.panix.com...
> In article <jteb0b.0n7.ln@news.hinznet.home>,

>
> It has been said that 'every situation has an exception' is inviolably
…[4 more quoted lines elided]…
>
Very sound advice, Doc <G> (And the subtlety of your first paragraph was not
lost on me...<G>)

I saw the extensions of this into Bertrand Russell and Wittgenstein later in
the thread and marvelled at the powerful minds who are happy to come to CLC
for a little diversion...<G>.

In passing, I wanted to mention (for those lesser mortals who may not have
philosophical references on their bookcases) that the people who say "Oh,
that's the exception that proves the rule..." should be slapped around the
face with a wet fish.

For the benefit of these deluded souls, the verb "to prove" has an original
and much earlier meaning than the one we use today. It originally meant "to
test". Hence, "proof" was the accumulated evidence from a test.

Obviously, if a rule has exceptions, then it needs modifying. It is totally
incorrect to state that the exceptions prove it is a correct rule (as I have
heard often in pub discussions...).

If the word "tests" is substituted for "proves", then the original meaning
of the statement "the exception that proves the rule" becomes clear.

I'm sure many here already knew that and would not use such a device for
argument, but there are some...<G>

Pete.




-----------== Posted via Newsfeed.Com - Uncensored Usenet News ==----------
   http://www.newsfeed.com       The #1 Newsgroup Service in the World!
-----= Over 100,000 Newsgroups - Unlimited Fast Downloads - 19 Servers =-----
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 8)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T09:22:28-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0ecb4$7q4$1@panix2.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <3e2a7c2e_11@news.newsgroups.com>`

```
In article <3e2a7c2e_11@news.newsgroups.com>,
Peter E.C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
>
><docdwarf@panix.com> wrote in message news:b0bspq$2jf$1@panix2.panix.com...
…[10 more quoted lines elided]…
>lost on me...<G>)

Gosh, you'se jes' easily amused.

>
>I saw the extensions of this into Bertrand Russell and Wittgenstein later in
>the thread and marvelled at the powerful minds who are happy to come to CLC
>for a little diversion...<G>.

Powerful minds?  Where?  If it's not too much trouble I'd like an 
introduction to them, please!

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 9)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-19T22:53:58+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2B2F18.7050201@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <3e2a7c2e_11@news.newsgroups.com> <b0ecb4$7q4$1@panix2.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3e2a7c2e_11@news.newsgroups.com>,
> Peter E.C. Dashwood <dashwood@nospam.enternet.co.nz> wrote:
…[10 more quoted lines elided]…
> 

"Allow me to introduce myself, I'm a man of wealth and 
fame."  However, this powerful mind is much too busy for 
trivial discussions on the writings of dead white 
philosophers, even when reading them on a Sunday.
:)
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 10)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T18:53:39-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0fdq3$d73$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3e2a7c2e_11@news.newsgroups.com> <b0ecb4$7q4$1@panix2.panix.com> <3E2B2F18.7050201@nycap.rr.com>`

```
In article <3E2B2F18.7050201@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[14 more quoted lines elided]…
>fame."

Don't forget the 'modest', too!

>However, this powerful mind is much too busy for 
>trivial discussions on the writings of dead white 
>philosophers, even when reading them on a Sunday.
>:)

Business interaction number 8,253:

Boss: 'Well, I *could* do my job in order to make your life a bit 
easier... but I really cannot do my job just now, I am Very Busy.'

Underling: 'Oh, of course, that's right, you are Very Busy... Very Busy 
doing *what*, pray tell?'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-20T03:29:44+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2B6FB6.3060708@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3e2a7c2e_11@news.newsgroups.com> <b0ecb4$7q4$1@panix2.panix.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2B2F18.7050201@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[39 more quoted lines elided]…
> 

Boss:  'If, Underling, you want to keep YOUR job, "please go
away and let me Do My Job."' ;)
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-19T22:40:48-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0fr40$pk1$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B6FB6.3060708@nycap.rr.com>`

```
In article <3E2B6FB6.3060708@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[44 more quoted lines elided]…
>away and let me Do My Job."' ;)

Underling: 'But... you just said 'I really cannot do my job just now, I am 
Very Busy'... and so I was wondering, Very Busy doing *what*?'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-20T15:25:28+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2C177D.5090703@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B6FB6.3060708@nycap.rr.com> <b0fr40$pk1$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2B6FB6.3060708@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[57 more quoted lines elided]…
> 

Boss:  Obviously, Very Busy trying to get you to "please go 
away and let me Do My Job."
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-20T15:29:23-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0hm73$75r$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B6FB6.3060708@nycap.rr.com> <b0fr40$pk1$1@panix1.panix.com> <3E2C177D.5090703@nycap.rr.com>`

```
In article <3E2C177D.5090703@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[61 more quoted lines elided]…
>away and let me Do My Job."

Underling: 'Ahhhh... so if I go away then I won't have to do the part of 
your job that you were too Busy to do and you'll be able to do it, then... 
so I'll go away and not do the part of your job you want me to do because 
now you'll have time.'

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T12:56:37+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D4619.5040003@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B6FB6.3060708@nycap.rr.com> <b0fr40$pk1$1@panix1.panix.com> <3E2C177D.5090703@nycap.rr.com> <b0hm73$75r$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2C177D.5090703@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[78 more quoted lines elided]…
> 

Boss:  In all this discussion, I don't recall asking you to 
do any part of my job.  If you have so much time on your 
hands that you presume to find it necessary to do MY job as 
well as yours, then may be you should stop working overtime 
and billing us for work that is not your responsibility nor 
assignment to do.  Now, "please go away and let me Do My 
Job" and go do your assigned tasks.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T08:31:22-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0ji3a$k68$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2C177D.5090703@nycap.rr.com> <b0hm73$75r$1@panix1.panix.com> <3E2D4619.5040003@nycap.rr.com>`

```
In article <3E2D4619.5040003@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[89 more quoted lines elided]…
>Job" and go do your assigned tasks.

Underling: Our memories are, it seems, rather different and my timesheets 
which you sign and have copies of show no overtime; you may consider this 
discussion to be completed.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 17)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T14:32:14+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D5C80.7090609@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2C177D.5090703@nycap.rr.com> <b0hm73$75r$1@panix1.panix.com> <3E2D4619.5040003@nycap.rr.com> <b0ji3a$k68$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2D4619.5040003@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[107 more quoted lines elided]…
> 

Boss:  Finally!  Now perhaps you will "please go away and 
let me Do My Job."
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T10:16:05-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0jo7l$cmv$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D4619.5040003@nycap.rr.com> <b0ji3a$k68$1@panix1.panix.com> <3E2D5C80.7090609@nycap.rr.com>`

```
In article <3E2D5C80.7090609@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[111 more quoted lines elided]…
>let me Do My Job."

Underling: The discussion is completed; there is no need for you to waste 
both our times with your input.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 19)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T15:22:37+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D684F.8020107@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D4619.5040003@nycap.rr.com> <b0ji3a$k68$1@panix1.panix.com> <3E2D5C80.7090609@nycap.rr.com> <b0jo7l$cmv$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2D5C80.7090609@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[129 more quoted lines elided]…
> DD

Boss:  If it is complete, why are you still here responding 
instead of doing your job?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T10:36:23-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0jpdn$iau$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D5C80.7090609@nycap.rr.com> <b0jo7l$cmv$1@panix1.panix.com> <3E2D684F.8020107@nycap.rr.com>`

```
In article <3E2D684F.8020107@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[134 more quoted lines elided]…
>instead of doing your job?

Underling: Because you are keeping me Very Busy.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 11)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-01-20T04:06:04+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2B75A9.2090103@optonline.NOSPAM.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3e2a7c2e_11@news.newsgroups.com> <b0ecb4$7q4$1@panix2.panix.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <3E2B2F18.7050201@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[16 more quoted lines elided]…
> Don't forget the 'modest', too!

Oh, show him a little sympathy.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 12)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-20T08:29:58-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0gtkm$mr2$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net>`

```
In article <3E2B75A9.2090103@optonline.NOSPAM.net>,
Liam Devlin  <LiamD@optonline.NOSPAM.net> wrote:
>docdwarf@panix.com wrote:
>> In article <3E2B2F18.7050201@nycap.rr.com>,
…[19 more quoted lines elided]…
>Oh, show him a little sympathy.

That's all he'll get from me... he should be used to it, he's been around 
for long, long years.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 13)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-20T15:27:57+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2C1811.6070504@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2B75A9.2090103@optonline.NOSPAM.net>,
> Liam Devlin  <LiamD@optonline.NOSPAM.net> wrote:
…[32 more quoted lines elided]…
> 

Sympathy?  What about respect.  This present generation has 
no respect for its "elders".  And because of that, "I can't 
get no satisfaction."
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** Harald Hinz <harald.hinz@ewetel.net>
- **Date:** 2003-01-20T21:26:06+01:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<u0mh0b.fc1.ln@news.hinznet.home>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com>`

```
Robert Graham <rgraham2@nycap.rr.com> schrieb in
news:3E2C1811.6070504@nycap.rr.com: 

> Sympathy?  What about respect.  This present generation has 
> no respect for its "elders".  And because of that, "I can't 
> get no satisfaction."
 
Maybe it helps if you'll present jumping jack flash to Lady Jane?

Its a gas, gas, gas....

SCNR
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T13:02:15+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D476B.7060408@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com> <u0mh0b.fc1.ln@news.hinznet.home>`

```


Harald Hinz wrote:
> Robert Graham <rgraham2@nycap.rr.com> schrieb in
> news:3E2C1811.6070504@nycap.rr.com: 
…[11 more quoted lines elided]…
> SCNR

I am shocked, simply SHOCKED!  What are you suggesting here? 
  That "I" should be involved in something illegal?  And to 
the Sweet Lady Jane?  Of all things.  Shocking! OH! Gimmy 
Shelter from such atrocities!
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-20T15:30:27-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0hm93$7e2$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com>`

```
In article <3E2C1811.6070504@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[37 more quoted lines elided]…
>get no satisfaction."

Respect is earned, not granted as a condition of existence.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T12:59:32+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D46C8.4060708@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com> <b0hm93$7e2$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2C1811.6070504@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[51 more quoted lines elided]…
> 

When one is all powerful, one doesn't have to earn anything. 
  One can simply DEMAND it, or else.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 16)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T08:32:15-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0ji4v$kc0$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2C1811.6070504@nycap.rr.com> <b0hm93$7e2$1@panix1.panix.com> <3E2D46C8.4060708@nycap.rr.com>`

```
In article <3E2D46C8.4060708@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[55 more quoted lines elided]…
>  One can simply DEMAND it, or else.

When one is all powerful one need not 'demand'; a desire should be 
sufficient.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 17)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T14:38:16+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D5DEA.9000500@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2C1811.6070504@nycap.rr.com> <b0hm93$7e2$1@panix1.panix.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2D46C8.4060708@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[71 more quoted lines elided]…
> 

You can't always get what you want (or desire), but if you 
try, sometimes, you get what you need.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T10:17:31-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0joab$e75$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com> <3E2D5DEA.9000500@nycap.rr.com>`

```
In article <3E2D5DEA.9000500@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[75 more quoted lines elided]…
>try, sometimes, you get what you need.

If you try hard enough you'll get a reputation as a tough judge.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 19)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T15:26:38+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D693F.20700@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com> <3E2D5DEA.9000500@nycap.rr.com> <b0joab$e75$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
>>
>>You can't always get what you want (or desire), but if you 
…[6 more quoted lines elided]…
> 

"Tough judge" is a relative term, it depends on which side 
of the political fence you are on - one man's "tough judge" 
is another man's "turn 'em loose" judge.  It also depends on 
who is really in charge.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 20)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T10:37:26-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0jpfm$iil$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D5DEA.9000500@nycap.rr.com> <b0joab$e75$1@panix1.panix.com> <3E2D693F.20700@nycap.rr.com>`

```
In article <3E2D693F.20700@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[14 more quoted lines elided]…
>who is really in charge.

Isn't 'all things are relative' absolutely true?

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 21)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T15:40:36+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D6C85.3010308@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D5DEA.9000500@nycap.rr.com> <b0joab$e75$1@panix1.panix.com> <3E2D693F.20700@nycap.rr.com> <b0jpfm$iil$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2D693F.20700@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[22 more quoted lines elided]…
> 

Wait, we're not going to get back into that "philosophy" 
thread again, are we?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 22)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T10:45:19-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0jpuf$kkh$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D693F.20700@nycap.rr.com> <b0jpfm$iil$1@panix1.panix.com> <3E2D6C85.3010308@nycap.rr.com>`

```
In article <3E2D6C85.3010308@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[27 more quoted lines elided]…
>

Answering a question with a question is no answer at all.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 23)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T18:41:13+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D96DA.9060204@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D693F.20700@nycap.rr.com> <b0jpfm$iil$1@panix1.panix.com> <3E2D6C85.3010308@nycap.rr.com> <b0jpuf$kkh$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <3E2D6C85.3010308@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[37 more quoted lines elided]…
> 

Jesus often answered questions from self-righteous Pharisees 
with a question of His own, requiring their answer before He 
would answer them.  Thus, the practice is at least 2000 
years old.  Besides, sometimes questions are answers if they 
are rhetorical.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 24)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T13:46:10-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b0k4hi$fem$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D6C85.3010308@nycap.rr.com> <b0jpuf$kkh$1@panix1.panix.com> <3E2D96DA.9060204@nycap.rr.com>`

```
In article <3E2D96DA.9060204@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[44 more quoted lines elided]…
>are rhetorical.

The last time I looked... you are not the Christ, I am not a Pharisee, it 
is now, not 2000 years ago and the situation is not one of rhetoric.  
Answering a question with a question is no answer at all.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 24)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-21T20:40:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b0kb77$rgk$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D693F.20700@nycap.rr.com> <b0jpfm$iil$1@panix1.panix.com> <3E2D6C85.3010308@nycap.rr.com> <b0jpuf$kkh$1@panix1.panix.com> <3E2D96DA.9060204@nycap.rr.com>`

```

On 21-Jan-2003, Robert Graham <rgraham2@nycap.rr.com> wrote:

> Jesus often answered questions from self-righteous Pharisees
> with a question of His own, requiring their answer before He
> would answer them.  Thus, the practice is at least 2000
> years old.  Besides, sometimes questions are answers if they
> are rhetorical.

Well, if it worked for Plato 4 centuries earlier, why wouldn't it work for
Jesus?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 25)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T16:06:58-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b0kcpi$41o$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b0jpuf$kkh$1@panix1.panix.com> <3E2D96DA.9060204@nycap.rr.com> <b0kb77$rgk$1@peabody.colorado.edu>`

```
In article <b0kb77$rgk$1@peabody.colorado.edu>,
Howard Brazee <howard.brazee@cusys.edu> wrote:
>
>On 21-Jan-2003, Robert Graham <rgraham2@nycap.rr.com> wrote:
…[8 more quoted lines elided]…
>Jesus?

It might work as well... or as badly; Nietzsche called Christianity 
'Platonism for the masses'.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 26)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T21:47:18+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3E2DC26C.5080500@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b0jpuf$kkh$1@panix1.panix.com> <3E2D96DA.9060204@nycap.rr.com> <b0kb77$rgk$1@peabody.colorado.edu> <b0kcpi$41o$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <b0kb77$rgk$1@peabody.colorado.edu>,
> Howard Brazee <howard.brazee@cusys.edu> wrote:
…[18 more quoted lines elided]…
> 

Nietzsche-ism is dead, Christianity lives - as does Jesus.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 27)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-21T20:10:45-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b0kr2l$8hr$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b0kb77$rgk$1@peabody.colorado.edu> <b0kcpi$41o$1@panix1.panix.com> <3E2DC26C.5080500@nycap.rr.com>`

```
In article <3E2DC26C.5080500@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[21 more quoted lines elided]…
>Nietzsche-ism is dead, Christianity lives - as does Jesus.

Lovely weather, isn't it?

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 28)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-22T13:34:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3E2EA068.10208@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <b0kb77$rgk$1@peabody.colorado.edu> <b0kcpi$41o$1@panix1.panix.com> <3E2DC26C.5080500@nycap.rr.com> <b0kr2l$8hr$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> 
> Lovely weather, isn't it?
> 
> DD
> 

Well, I hope that you are writing from Hawaii or the Costa 
del Sol.  Here in New England, even the polar bears are 
staying in by the fire place.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 29)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-22T09:24:40-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b0m9j8$sv$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2DC26C.5080500@nycap.rr.com> <b0kr2l$8hr$1@panix1.panix.com> <3E2EA068.10208@nycap.rr.com>`

```
In article <3E2EA068.10208@nycap.rr.com>,
Robert Graham  <rgraham2@nycap.rr.com> wrote:
>
>
…[7 more quoted lines elided]…
>staying in by the fire place.

Here in Maryland it is clear and cold... but that happens this time of 
year.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 30)_

- **From:** "Howard Brazee" <howard.brazee@cusys.edu>
- **Date:** 2003-01-22T15:29:44+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b0mdd8$rtc$1@peabody.colorado.edu>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2DC26C.5080500@nycap.rr.com> <b0kr2l$8hr$1@panix1.panix.com> <3E2EA068.10208@nycap.rr.com> <b0m9j8$sv$1@panix1.panix.com>`

```

On 22-Jan-2003, docdwarf@panix.com wrote:

> >Well, I hope that you are writing from Hawaii or the Costa
> >del Sol.  Here in New England, even the polar bears are
…[3 more quoted lines elided]…
> year.

I had Monday off, so I played golf in Colorado.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 31)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-22T10:42:38-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b0me5e$pjo$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2EA068.10208@nycap.rr.com> <b0m9j8$sv$1@panix1.panix.com> <b0mdd8$rtc$1@peabody.colorado.edu>`

```
In article <b0mdd8$rtc$1@peabody.colorado.edu>,
Howard Brazee <howard.brazee@cusys.edu> wrote:
>
>On 22-Jan-2003, docdwarf@panix.com wrote:
…[8 more quoted lines elided]…
>I had Monday off, so I played golf in Colorado.

I had Monday off, as well; I spent time being amused by a puppy's 
ferocity.

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 18)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-01-22T10:02:58+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2E6C52.3050202@optonline.NOSPAM.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2C1811.6070504@nycap.rr.com> <b0hm93$7e2$1@panix1.panix.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com> <3E2D5DEA.9000500@nycap.rr.com>`

```
Robert Graham wrote:
> 
> 
…[76 more quoted lines elided]…
> sometimes, you get what you need.

'Scuse me, anyone want anything from the drugstore?
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 19)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-22T13:35:30+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2EA0BB.9050105@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2C1811.6070504@nycap.rr.com> <b0hm93$7e2$1@panix1.panix.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com> <3E2D5DEA.9000500@nycap.rr.com> <3E2E6C52.3050202@optonline.NOSPAM.net>`

```


Liam Devlin wrote:
> Robert Graham wrote:
> 
…[92 more quoted lines elided]…
> 

One can always use a little help from my friends.  Oh, 
wait...that's another thread altogether now.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 17)_

- **From:** "Gazaloo" <gaz@a.loo>
- **Date:** 2003-01-26T06:28:21+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<DdLY9.40481$6G4.8697@sccrnsc02>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2C1811.6070504@nycap.rr.com> <b0hm93$7e2$1@panix1.panix.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com>`

```
> When one is all powerful one need not 'demand'; a desire should be
> sufficient.

Tao-on DD.

Gazaloo.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 18)_

- **From:** docdwarf@panix.com
- **Date:** 2003-01-26T09:23:25-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<b10r0t$8kj$1@panix1.panix.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com> <DdLY9.40481$6G4.8697@sccrnsc02>`

```
In article <DdLY9.40481$6G4.8697@sccrnsc02>, Gazaloo <gaz@a.loo> wrote:
>> When one is all powerful one need not 'demand'; a desire should be
>> sufficient.
>
>Tao-on DD.

Perhaps it is not wise to meditate madly... but isn't there a song which 
encourages one to ommmm, ommmm on, deranged?

DD
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 19)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-26T21:50:14+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E34581C.30905@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2D46C8.4060708@nycap.rr.com> <b0ji4v$kc0$1@panix1.panix.com> <DdLY9.40481$6G4.8697@sccrnsc02> <b10r0t$8kj$1@panix1.panix.com>`

```


docdwarf@panix.com wrote:
> In article <DdLY9.40481$6G4.8697@sccrnsc02>, Gazaloo <gaz@a.loo> wrote:
> 
…[10 more quoted lines elided]…
> 

Om, sweet Om. :)
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-01-22T10:01:45+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2E6C08.4090400@optonline.NOSPAM.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com> <b0hm93$7e2$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <3E2C1811.6070504@nycap.rr.com>,
> Robert Graham  <rgraham2@nycap.rr.com> wrote:
…[48 more quoted lines elided]…
> Respect is earned, not granted as a condition of existence.

"Those who want respect, give respect"

A. Soprano
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-20T21:55:57+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.00000026.007c3c2b@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com>`

```
Robert,

> Sympathy?  What about respect.  This present generation has 
> no respect for its "elders".  And because of that, "I can't 
> get no satisfaction."

Is that all we have, these days?

---

Doug (trying to remember why he chased women so much)

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-21T13:03:14+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2D47A6.3070304@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com> <VA.00000026.007c3c2b@nildram.co.uk>`

```


Doug Scott wrote:
> Robert,
> 
…[14 more quoted lines elided]…
> 

I believe the implication is that we DON'T have it these days.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 16)_

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-21T21:36:55+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000002a.006276de@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com> <VA.00000026.007c3c2b@nildram.co.uk> <3E2D47A6.3070304@nycap.rr.com>`

```
Robert,

> I believe the implication is that we DON'T have it these days.

.. And my implication was that it was all we cared about. Sad, but...

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 14)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-01-22T10:01:13+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2E6BE8.6050803@optonline.NOSPAM.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com>`

```
Robert Graham wrote:
> 
> docdwarf@panix.com wrote:
…[33 more quoted lines elided]…
> for its "elders".  And because of that, "I can't get no satisfaction."

Was that you on HBO Saturday night?

I caught some of the rebroadcast of the Stones' concert on HBO2 Tuesday 
night - pretty scary IMHO.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 15)_

- **From:** Robert Graham <rgraham2@nycap.rr.com>
- **Date:** 2003-01-22T13:37:34+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2EA137.6070709@nycap.rr.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E2B2F18.7050201@nycap.rr.com> <b0fdq3$d73$1@panix1.panix.com> <3E2B75A9.2090103@optonline.NOSPAM.net> <b0gtkm$mr2$1@panix1.panix.com> <3E2C1811.6070504@nycap.rr.com> <3E2E6BE8.6050803@optonline.NOSPAM.net>`

```


Liam Devlin wrote:
> Robert Graham wrote:
> 
…[47 more quoted lines elided]…
> 

Disclaimer:  all Stones quotes pre 1971.
```

###### ↳ ↳ ↳ Re: Internal vs External SORTs

_(reply depth: 8)_

- **From:** Liam Devlin <LiamD@optonline.NOSPAM.net>
- **Date:** 2003-01-20T04:05:09+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E2B7572.1040905@optonline.NOSPAM.net>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <3E21743F.9060507@nycap.rr.com> <avuvon$608$1@panix1.panix.com> <jteb0b.0n7.ln@news.hinznet.home> <b0bspq$2jf$1@panix2.panix.com> <3e2a7c2e_11@news.newsgroups.com>`

```
Peter E.C. Dashwood wrote:
> <docdwarf@panix.com> wrote in message news:b0bspq$2jf$1@panix2.panix.com...
> 
…[34 more quoted lines elided]…
> argument, but there are some...<G>

Is this going to be on the final?
```

###### ↳ ↳ ↳ Manual availability and Re: Internal vs External SORTs

_(reply depth: 4)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2003-01-16T21:22:31-04:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<3E275AD7.596E9E75@istar.ca>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <mo-dnSwlUblX34KjXTWciw@giganews.com> <VA.0000000c.01a21f62@nildram.co.uk> <3E21743F.9060507@nycap.rr.com>`

```
Normally only one manual comes with the software, the rest are
chargeable.  These days there normally is a machine readable version of
the manual.  

In the IBM mainframe world and I suspect the same is true of other
mainframe platforms, the internal sort would probably be more
inefficient due to real (as opposed to virtual) memory constraints. 
This is because of the amount of memory taken by the program.  With the
large amount of real memory available in most environments as well as
the large virtual spaces, this becomes irrelevant in most situations.  I
would still CLOSE all files OPENED in an INPUT or OUTPUT PROCEDURE in
the respective procedure and not have any files open over the execution
of the SORT other than files used by the INPUT or OUTPUT procedure.  In
this case as in so many others, hardware advances have made a difference
in what good practice can be.  My personal preference is to use internal
sorts when they make sense.  They certainly are more self documenting
than SORT FIELDS=(131,4,PD,A,5,4,CH,A) and INCLUDE
FIELDS=(8,4,CH,EQ,C'BLOB')

Robert Graham wrote:
> 
> Doug Scott wrote:
…[42 more quoted lines elided]…
> (or at least EASY) in an external sort.
```

#### ↳ Re: Internal vs External SORTs

- **From:** Angel <angel@smart.net>
- **Date:** 2003-01-23T21:54:11-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<Pine.LNX.4.21.0301232147520.13222-100000@smarty.smart.net>`
- **In-Reply-To:** `<avn1kv$n9j$6@news.utelfla.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com>`

```

A software designer once told me he avoided external sorts
because he focused on portability.  He saw his platform 
yanked out and ordered to port to another several times
in one decade. 

Now that everything is within Cobol, he's ready.

Will you ever need to port your applications from Unix 
to an IBM mainframe?  You might think that you'll never
have to port.  But almost none of those forced to port 
thought that either.  

The more things change, the more they remain the same. 


On Fri, 10 Jan 2003, Ubiquitous wrote:

> Date: Fri, 10 Jan 2003 17:58:56 +0000 (UTC)
> From: Ubiquitous <weberm@polaris.net>
…[7 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Internal vs External SORTs

- **From:** Doug Scott <dwscott@nildram.co.uk>
- **Date:** 2003-01-24T20:33:30+00:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<VA.0000002f.00853647@nildram.co.uk>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com> <Pine.LNX.4.21.0301232147520.13222-100000@smarty.smart.net>`

```
Angel,

> Now that everything is within Cobol, he's ready.

Neat point. But mainframers never think their programs will ever run on 
PCs, or even Unix.

---

Doug

dwscott@ieee.org
```

#### ↳ Re: Internal vs External SORTs

- **From:** "Bob Milk" <robert_milk@alum.wpi.edu>
- **Date:** 2003-09-27T22:04:43-05:00
- **Newsgroups:** comp.lang.cobol,alt.cobol
- **Message-ID:** `<vncjukeii3b1bd@corp.supernews.com>`
- **References:** `<avn1kv$n9j$6@news.utelfla.com>`

```
Depends on what is meant by better.

Given that the same person codes all the examples to remove the differences
for that point.

From an execution point of view, Execute sort with E15 and E35 Exits.  Given
that these exits imply 2 different programs, the on-going maintenance of
using the exits may also be the easier.

With that said, since many folks have limited or no exposure to exits within
sort, a COBOL program with INPUT and OUTPUT procedures should have better
run-time as you remove 2 sets of I-O.

From a maintenance perspective, I would write two  COBOL program , The
pre-sort program, then sort, and finally a post-sort program.

Like I and others have said, it depends on point of view of better.

Bob Milk




"Ubiquitous" <weberm@polaris.net> wrote in message
news:avn1kv$n9j$6@news.utelfla.com...
> I'm curious; is it better to perform a SORT within a COBOL
> program or better to perform it in the JCL, or does it
> depend on what one is sorting?
>
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
