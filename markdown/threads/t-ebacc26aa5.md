[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# IBM and COBOL SEARCH ALL

_28 messages · 11 participants · 2006-12 → 2007-01_

---

### IBM and COBOL SEARCH ALL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-11T20:47:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com>`

```
to: comp.lang.cobol and others

In Doc's recent comp.lang.cobol post, he used "SEARCH" in the description (but 
not in his source code).  This made me think that it was time for me to send out 
a reminder to IBM mainframe COBOL shops that IBM has "recently" (last year or 
so) gone back and forth in an attempt to

  - fix a bug in their *previous* "SEARCH ALL" behavior
        and
  - to impact as few existing programs (especially those that don't get 
recompiled) as possible

If you are (or may ever be) working with IBM mainframe COBOL, I suggest you look 
at (and/or distribute at your shop) the information at:

  http://publibfp.boulder.ibm.com/cgi-bin/bookmgr/BOOKS/IGY3MG32/5.4

NOTE WELL:
   Changes/Maintenance to *EITHER* LE or COBOL may result in your needing to 
know about this.
```

#### ↳ Re: IBM and COBOL SEARCH ALL

- **From:** "Robert Jones" <rjones0@hotmail.com>
- **Date:** 2006-12-12T11:32:11-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1165951931.066944.25570@80g2000cwy.googlegroups.com>`
- **In-Reply-To:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com>`

```
Thanks for that
```

#### ↳ Re: IBM and COBOL SEARCH ALL

- **From:** "Roger While" <simrw@sim-basis.de>
- **Date:** 2006-12-13T21:48:32+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<elpov6$rkc$02$1@news.t-online.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com>`

```
Oooh, does that affect a large user base ?

Roger

"William M. Klein" <wmklein@nospam.netcom.com> schrieb im Newsbeitrag 
news:Ztjfh.384042$%j2.255292@fe07.news.easynews.com...
> to: comp.lang.cobol and others
>
…[22 more quoted lines elided]…
>
```

##### ↳ ↳ Re: IBM and COBOL SEARCH ALL

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2006-12-14T00:34:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<n_0gh.23150$9v5.3513@newssvr29.news.prodigy.net>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com>`

```
"Roger While" <simrw@sim-basis.de> wrote in message 
news:elpov6$rkc$02$1@news.t-online.com...
> Oooh, does that [change in SEARCH ALL behavior] affect a large user base ?

Well, you never know.....

About ten years ago I got my first COBOL contracting job for "a major 
corporation" ( 10 figure annual revenues).  (I still do work for its 
successor company).

As you might expect, they assigned an individual to supervise, and to 'sign 
off' on my work. Naturally, this signoff included a check of my source code 
to make sure it was maintainable.

The person assigned to check my source code had been the lead COBOL 
programmer for the subgroup for nine (9) years at the time. Imagine my 
surprise when she told me not only did my code look just fine, but she was 
happy to have reviewed it because it was the *first*  time she had *ever* 
seen the SEARCH verb used!

At least that taught me something important: "Thou Shalt Never Assume Any 
Minimum Level of Experience or Expertise in Thy Clients."

MCM
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-14T07:08:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v8m2o25lm9fplp7ev273t7kda6od7sjt2f@4ax.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <n_0gh.23150$9v5.3513@newssvr29.news.prodigy.net>`

```
On Thu, 14 Dec 2006 00:34:27 GMT, "Michael Mattias"
<mmattias@talsystems.com> wrote:

>The person assigned to check my source code had been the lead COBOL 
>programmer for the subgroup for nine (9) years at the time. Imagine my 
>surprise when she told me not only did my code look just fine, but she was 
>happy to have reviewed it because it was the *first*  time she had *ever* 
>seen the SEARCH verb used!

Weird.    I recently fixed a job that stopped working with our last OS
upgrade.    It read in a 659 line 80 column table that it wrote to a
temporary ISAM file so it could do a look-up for a report.   Nowadays
this is so small that there's no reason not to make it a SEARCH (it's
even already sorted, so SEARCH ALL works).    

Too bad our CoBOL doesn't yet have an internal table sort command.

I worked with someone who worked at a place in the 1970s that did not
have a SORT.   So whenever he needed a sort, he copied a file to ISAM
and back.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 4)_

- **From:** "Michael Mattias" <mmattias@talsystems.com>
- **Date:** 2006-12-14T14:30:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1edgh.30735$wP1.14868@newssvr14.news.prodigy.net>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <n_0gh.23150$9v5.3513@newssvr29.news.prodigy.net> <v8m2o25lm9fplp7ev273t7kda6od7sjt2f@4ax.com>`

```
Howard Brazee" <howard@brazee.net> wrote in message 
news:v8m2o25lm9fplp7ev273t7kda6od7sjt2f@4ax.com...
> Weird.    I recently fixed a job that stopped working with our last OS
> upgrade.    It read in a 659 line 80 column table that it wrote to a
> temporary ISAM file so it could do a look-up for a report.   Nowadays
> this is so small that there's no reason not to make it a SEARCH (it's
> even already sorted, so SEARCH ALL works).

You don't mean... no, it couldn't be.. it's not possible that .... "old code 
never dies?"

Or, even less possible... "we've always done it that way"  is a 'preferred 
technique?'

Say it ain't so, Joe.

MCM
```

##### ↳ ↳ Re: IBM and COBOL SEARCH ALL

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-15T21:03:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f4Egh.505704$kz6.420366@fe08.news.easynews.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com>`

```
Well, there certainly was a fairly larger "furor" when this first happened. 
Part of the problem was that "SEARCH ALL" logic was done in a run-time library 
routine.  Therefore, existing programs that were NOT re-compiled suddenly 
started getting different run-time results.  (For IBM people, this impacted 
"RES" programs when upgrading z/OS because the routines were in LE).

IBM *then* changed the behavior so that the run-time routine CHECKED what 
compiler version was used and only gave the new behavior for "newly" compiled 
programs.  However, it certainly was "controversial".
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-12-24T01:05:13-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1184b$458e189b$d066072d$24830@FUSE.NET>`
- **In-Reply-To:** `<f4Egh.505704$kz6.420366@fe08.news.easynews.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com>`

```
William M. Klein wrote:
> Well, there certainly was a fairly larger "furor" when this first happened. 
> Part of the problem was that "SEARCH ALL" logic was done in a run-time library 
…[7 more quoted lines elided]…
> 
Well, the effect is essentially what you describe, but actually, the new 
compiler with service applied [V3.4] generates calls to a new run-time 
component and the older compilers still use the original run-time 
component.  So, the determination of which logic to use is made at 
compile time, not run-time.  But, maintenance is required to both the 
V3.4 compiler and LE to make it work this way.

Without the maintenance, all code from all compilers [back to OS/VS 
COBOL] using SEARCH ALL will get the new behavior that was introduced in 
base code LE with z/OS V1.7 or service applied to earlier releases to 
support COBOL V3.4.

Carl
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2006-12-24T21:07:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e_Bjh.98206$z_3.52760@fe07.news.easynews.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <1184b$458e189b$d066072d$24830@FUSE.NET>`

```
I suppose one more "comment".  I think (but won't swear to it) that "pre-LE" 
compiled code that was compiled with NORES would not (probably wouldn't?) be 
impacted by the change.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 5)_

- **From:** CG <carl.gehr.RemoveThis@ThisToo.attglobal.net>
- **Date:** 2006-12-24T18:01:59-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e06d1$458f06e7$d066072d$9253@FUSE.NET>`
- **In-Reply-To:** `<e_Bjh.98206$z_3.52760@fe07.news.easynews.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <1184b$458e189b$d066072d$24830@FUSE.NET> <e_Bjh.98206$z_3.52760@fe07.news.easynews.com>`

```
William M. Klein wrote:
> I suppose one more "comment".  I think (but won't swear to it) that "pre-LE" 
> compiled code that was compiled with NORES would not (probably wouldn't?) be 
> impacted by the change.
> 
True, as long as it is not relinked...

Carl
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-12-29T06:26:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<f4Egh.505704$kz6.420366@fe08.news.easynews.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com>`

```


William M. Klein wrote:
> Well, there certainly was a fairly larger "furor" when this first happened. 
> Part of the problem was that "SEARCH ALL" logic was done in a run-time library 
…[7 more quoted lines elided]…
> 

Thursday I encountered this problem unexpectedly.  I had moved a batch 
  COBOL program into a test environment so it could run normally, and 
I got several RUNTIME error messages that looked like this:

"IGZ0194W Search argument 1 in the WHEN phrase of the SEARCH ALL 
statement in program XXXXXXXX on line number NNNN was longer than the 
corresponding key. The excess digit or character positions of the 
argument were not zeros or spaces respectively, and so the argument 
could never match the key in any of the table entries."

This rather long message appeared several times.  The program in 
question has multiple SEARCH ALL statements for several different 
tables, but the one with the problem is a USA State code table where 
each entry is PIC X(02).  The search argument from the input data 
record is a country code of PIC X(03), which can contain either a two 
character USA state code (with a trailing space) or a three-character 
country code.

This implies to me that the current IBM Enterprise COBOL and Language 
Environment (in test, at least) is now using the rules of COBOL for 
unequal length compares in the L/E SEARCH ALL library routine.  I 
assume I am not getting this message every time the SEARCH ALL is 
executed, if the search argument has a blank space in the third column.

The program was originally written over 10 years ago with a linear 
search implemented using PERFORM UNTIL and an IF statement.  It was 
converted to a SEARCH ALL six years ago for a performance improvement. 
  I can fix this by truncating the search argument from 3 bytes to 2 
bytes, but I think I need to be careful about the potential for the 
first two bytes of a country code accidentally matching a 2 byte USA 
state code...
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 4)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-29T10:23:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<en2qbg$632$1@reader2.panix.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>The search argument from the input data 
>record is a country code of PIC X(03), which can contain either a two 
>character USA state code (with a trailing space) or a three-character 
>country code.

[snip]

>  I can fix this by truncating the search argument from 3 bytes to 2 
>bytes, but I think I need to be careful about the potential for the 
>first two bytes of a country code accidentally matching a 2 byte USA 
>state code...

Bingo... DE is both Germany and Delaware, IL is both Illinois and 
Israel... and to complicate matters Israel uses five-digit postal codes, 
as well.

(Me?  Never run across anything like this before, it was just a lucky 
guess.)

Mention this to anyone ignorant enough to bluster 'All ya gotta do is 
check IF CNTRY-ST-CD(3:1) = SPACES OR LOW-VALUES'; you'll need to take a 
leisurely morning runinng some checks against country and state tables... 
and then sniffing through the data to find an indicator to hang your 
SEARCH ALL from.

DD
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-29T07:52:54-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<opaap2tdj8v36u8qllpchik64f84ve8dgi@4ax.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>`

```
On Fri, 29 Dec 2006 06:26:02 GMT, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:

>This rather long message appeared several times.  The program in 
>question has multiple SEARCH ALL statements for several different 
…[4 more quoted lines elided]…
>country code.

I once converted some small Burroughs machine CoBOL programs to a
large Burroughs machine CoBOL.   I had trouble with one program until
I tried adding a filler to the size of the internal sort file.
Apparently there was a minimum record size needed for the internal
sort (it took me a while to figure this out).

I wouldn't think a compiler would have a minimum search all table
record size - but see what happens if you add a filler to these
records.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 4)_

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2006-12-29T07:54:27-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<svaap2lqgdvs7j5eraos1e9286rjf0acc8@4ax.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>`

```
On Fri, 29 Dec 2006 06:26:02 GMT, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:

>This implies to me that the current IBM Enterprise COBOL and Language 
>Environment (in test, at least) is now using the rules of COBOL for 
>unequal length compares in the L/E SEARCH ALL library routine.  I 
>assume I am not getting this message every time the SEARCH ALL is 
>executed, if the search argument has a blank space in the third column.

Oops, never-mind my previous reply.   It doesn't apply to your
compiler.

I'm thinking this is about data, not about CoBOL.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 4)_

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2006-12-30T01:35:08-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dc1c9$4596089e$d066072d$15186@FUSE.NET>`
- **In-Reply-To:** `<_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> 
…[42 more quoted lines elided]…
> state code...

You have exactly the issue that created the need for the change.  To net 
out the 'long message':   The issue was that SEARCH ALL was not 
returning the same results as would have been obtained by using normal 
IF-THEN-ELSE statements to perform the same logic.  The results are only 
different when the argument and the key are different lengths.

If you have not read the FLASH that described the problem, you can find 
it at:
> http://www-1.ibm.com/support/docview.wss?rs=0&q1=%2bPK15432&uid=swg21234541&loc=en_US&cs=utf-8&cc=us&lang=all

If you would like to be able to discover all programs in your inventory 
that contain a SEARCH ALL verb, feel free to contact me off-list using 
E-Mail ID cgehr <at_domain> edge-information.com rather than the 
ID/domain on this posting.  We identify _all_ SEARCH ALL verbs, but we 
do not try to characterize the lengths [equal or not equal] of the 
key/argument.  We also distinguish the compiler level, if it has the 
recommended IBM maintenance and if the required maintenance has been 
applied to LE.

Carl
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 5)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-12-30T08:19:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<dc1c9$4596089e$d066072d$15186@FUSE.NET>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net> <dc1c9$4596089e$d066072d$15186@FUSE.NET>`

```


CG wrote:
> (snip) 
> You have exactly the issue that created the need for the change.  To net 
…[9 more quoted lines elided]…
>>

Thanks for the FLASH.  I have talked with the sysprog that maintains 
our Enterprise COBOL compiler.  Since I'm getting the new diagnostic, 
I think they have the PTF's applied.

> 
> 
…[9 more quoted lines elided]…
> Carl

We have Endevor, and we have multiple tools for scanning COBOL source 
code to find SEARCH ALL.  We don't expect to have very many instances 
of unequal length compares in SEARCH ALL, but it is nice to know that 
runtime diagnostics will alert us.

But in this case we probably don't want to see the runtime 
diagnostics, because this batch program typically processes millions 
of records per daily run.  That gives me an incentive to fix the 
problem in the most correct way.

Looking at it again, I think we will change the USA state code table 
to have PIC X(03) to make the SEARCH ALL comparison on equal length 
operands.  Remember, the input record being edited has a PIC X(03) 
field that contains either a two-character USA state code with 
trailing blank, or a three-character country code, depending on 
context.  All we need to do is ensure that each USA state code table 
entry has a trailing blank like the input record.

Thanks much!
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 6)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-30T13:38:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<en5q40$ql1$1@reader2.panix.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net> <dc1c9$4596089e$d066072d$15186@FUSE.NET> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:

[snip]

>Looking at it again, I think we will change the USA state code table 
>to have PIC X(03) to make the SEARCH ALL comparison on equal length 
…[3 more quoted lines elided]…
>context.

So... you've determined the mechanism altready in place which prevents the 
three-character field from containing two-character country codes like 
Germany's and Argentina's and Canada's and Israel's?  Would I be asking 
for Trade Secrets were I to inquire into this mechanism's details?

>All we need to do is ensure that each USA state code table 
>entry has a trailing blank like the input record.

All ya gotta do, indeed!  Glad it went that smoothly.

DD
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-12-30T20:34:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<en5q40$ql1$1@reader2.panix.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net> <dc1c9$4596089e$d066072d$15186@FUSE.NET> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net> <en5q40$ql1$1@reader2.panix.com>`

```


docdwarf@panix.com wrote:
> (snip)
> So... you've determined the mechanism altready in place which prevents the 
> three-character field from containing two-character country codes like 
> Germany's and Argentina's and Canada's and Israel's?  Would I be asking 
> for Trade Secrets were I to inquire into this mechanism's details?

My company uses its own coding scheme for three character country 
codes, and none of them have a trailing space.  I doubt that the 
actual code values would be trade secrets.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 8)_

- **From:** docdwarf@panix.com ()
- **Date:** 2006-12-31T01:42:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<en74ih$7jl$1@reader2.panix.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net> <en5q40$ql1$1@reader2.panix.com> <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net>`

```
In article <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>
>
…[9 more quoted lines elided]…
>actual code values would be trade secrets.

Ahhhhh... so instead of being ISO- (or whoever deems it-) compliant and 
use DE your code for Germany is something like GER... and Argentina is 
ARG, not AR, Canada CAN, not CA, et and cetera.  If that is the case then 
perhaps you might wish to consider a reference-modification test of the 
third character for SPACE, followed by a SEARCH ALL which compares the 
first two positions of the code with the full field on the State table, 
along the lines of:

IF INFILE-CODE(3:1) = SPACES OR LOW-VALUES
   SEARCH ALL COPYBOOK-STATE-TBL
      WHEN INFILE-CODE(1:2) = COPYBOOK-STATE-CODE(ST-IDX)

... cet and etera.  Speed being of the essence with your kind of 
processing the IF will generate two CLIs... I'm not sure what kind of 
overhead the reference-modification will add to the SEARCH ALL.

DD
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 9)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2007-01-03T06:16:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<en74ih$7jl$1@reader2.panix.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net> <en5q40$ql1$1@reader2.panix.com> <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net> <en74ih$7jl$1@reader2.panix.com>`

```


docdwarf@panix.com wrote:
> (snip) 
> Ahhhhh... so instead of being ISO- (or whoever deems it-) compliant and 
…[16 more quoted lines elided]…
> 

Thanks for the suggestion, Doc.  And also thanks to Clark F Morris who 
suggested a similar solution.

One thing we do differently is we place the indexed element on the 
left side of the equal sign, like this:

SEARCH ALL COPYBOOK-STATE-TBL
     WHEN COPYBOOK-STATE-CODE(ST-IDX) = INFILE-CODE(1:2)

I wanted to keep it this way, to make it obvious just what indexed 
item is being searched, although I haven't tested it to determine if 
there is a performance difference.  It's possible to do reference 
modification on an indexed/subscripted data item, but I dislike the 
number of parentheses involved.  It just looks too complicated.

With kindest regards,
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 10)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-01-03T22:41:36+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<501c2iF1e79taU1@mid.individual.net>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net> <en5q40$ql1$1@reader2.panix.com> <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net> <en74ih$7jl$1@reader2.panix.com> <GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net>`

```

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net...
>
<snip>

> One thing we do differently is we place the indexed element on the left 
> side of the equal sign, like this:
…[9 more quoted lines elided]…
>

I'm surprised to hear you say that, Arnold.

Refmodded indexing is a very useful tool and is less complex even than using 
a multi-dimensional array.

(See the original sample program I posted under the "productivity" thread 
for an example of refmodded indexing. (try a search on NVPARM)).

Everything looks strange and complicated until you become familiar with it. 
If you never become familiar with it, you are simply depriving your toolbox 
of powerful tools. It's like using a Mediaeval auger when you could have a 
cordless drill...

The whole reason I posted the code (which I VERY rarely do in CLC) is 
because Frank stated that he hoped he would never use a complex PERFORM. (I 
don't think he would have any trouble using one, and his first attempt at a 
complex UNSTRING was excellent.)

Complexity and complication is all relative. The answer is education and 
practice, not standards that emasculate the COBOL language.

Pete.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 11)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2007-01-04T06:31:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mb1nh.326420$Fi1.264966@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<501c2iF1e79taU1@mid.individual.net>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net> <en5q40$ql1$1@reader2.panix.com> <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net> <en74ih$7jl$1@reader2.panix.com> <GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net> <501c2iF1e79taU1@mid.individual.net>`

```


Pete Dashwood wrote:
> "Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
> news:GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net...
…[20 more quoted lines elided]…
> a multi-dimensional array.

I went back and found your example, which included a line with 
indexing and reference modification:

MOVE INPUT-DATA (INPUT-DATA-POS:1) TO ARG-NAME (ARGS-X1) (J:1)

This is neither encouraged nor prohibited in my shop standards, and 
I've only seen it used in one production program.  It's more of a 
personal style preference on my part.  I'm not saying I would never 
use this construct, but rather that I prefer to accomplish the same 
effect without refmodding an indexed item (if I can), simply because 
it seems more readable to me without so many parentheses.

I can see where it has advantages in your example.

> 
> (See the original sample program I posted under the "productivity" thread 
…[10 more quoted lines elided]…
> complex UNSTRING was excellent.)

Please don't hesitate to post code examples simply because of my style 
preferences.  How can we learn if we never see anything new and 
different?

> 
> Complexity and complication is all relative. The answer is education and 
> practice, not standards that emasculate the COBOL language.
> 
> Pete.

I don't think a shop standard should prohibit refmodding an indexed 
item (or using SEARCH ALL).  But I would have no problem with a shop 
standard that prohibited comparing unequal length data items.  It's 
still pretty hard to catch that in a code walkthrough.

With kindest regards,
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 12)_

- **From:** "Pete Dashwood" <dashwood@removethis.enternet.co.nz>
- **Date:** 2007-01-05T11:34:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<505do1F1efplcU1@mid.individual.net>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net> <en5q40$ql1$1@reader2.panix.com> <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net> <en74ih$7jl$1@reader2.panix.com> <GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net> <501c2iF1e79taU1@mid.individual.net> <mb1nh.326420$Fi1.264966@bgtnsc05-news.ops.worldnet.att.net>`

```

"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote in message 
news:mb1nh.326420$Fi1.264966@bgtnsc05-news.ops.worldnet.att.net...
>
>
…[37 more quoted lines elided]…
> I can see where it has advantages in your example.

Excellent. Thank you for doing that; I helps me feel my time wasn't wasted. 
(Actually, it wasn't wasted anyway because I thoroughly enjoyed the exercise 
and both Frank and I probably gained something from it. But if a posted 
example is seen to be of use to people then it encourages more posting of 
examples (not just from me, but hopefully from all here... I hesitate to 
post code because in the past, arguments have raged over style (and mine is 
far from perfect), rather than addressing the techniques involved. On this 
occasion that hasn't happened and there was one post (from Rick Smith) who 
pointed out a very cool way to get long strings into COBOL.)
>
>>
…[15 more quoted lines elided]…
>

Precisely.

If yours was the attitude exhibited by most here, we would probably have 
many more code samples being posted.
>>
>> Complexity and complication is all relative. The answer is education and 
>> practice, not standards that emasculate the COBOL language.
>>

> I don't think a shop standard should prohibit refmodding an indexed item 
> (or using SEARCH ALL).  But I would have no problem with a shop standard 
> that prohibited comparing unequal length data items.  It's still pretty 
> hard to catch that in a code walkthrough.
>

That's interesting... I've never had a problem with that. Maybe you could 
give us an exmple :-)?

Pete.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 10)_

- **From:** docdwarf@panix.com ()
- **Date:** 2007-01-03T10:09:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<enfvdk$ev0$1@reader2.panix.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net> <en74ih$7jl$1@reader2.panix.com> <GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net>`

```
In article <GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net>,
Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
>
>
>docdwarf@panix.com wrote:

[snip]

>> If that is the case then 
>> perhaps you might wish to consider a reference-modification test of the 
…[14 more quoted lines elided]…
>suggested a similar solution.

I cannot speak for Mr Morris, of course... but as for me, I figure my 
suggestion was worth at least double what I asked to be paid for it.

>
>One thing we do differently is we place the indexed element on the 
…[7 more quoted lines elided]…
>there is a performance difference.

My gut says there is no performance degradation, it says that the 
subscript gets incremented/decremented and a CLC is performed... but my 
gut's been wrong before and that's why the PMAP... errrrr, LIST compiler 
option was invented.

DD
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 11)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2007-01-04T06:35:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<1f1nh.326434$Fi1.272490@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<enfvdk$ev0$1@reader2.panix.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <v3Alh.608930$QZ1.491646@bgtnsc04-news.ops.worldnet.att.net> <en74ih$7jl$1@reader2.panix.com> <GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net> <enfvdk$ev0$1@reader2.panix.com>`

```


docdwarf@panix.com wrote:

> In article <GSHmh.320910$Fi1.228057@bgtnsc05-news.ops.worldnet.att.net>,
> Arnold Trembley  <arnold.trembley@worldnet.att.net> wrote:
…[17 more quoted lines elided]…
> DD

I think it should not make a difference either, but it's possible that 
it is more efficient to put then indexed item to the left of the equal 
  sign in the WHEN clause.  I can't promise I will get time for it 
soon, but I would like to try both with the LIST option, and see how 
the generated assembler differs, if it differs at all.
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 6)_

- **From:** CG <Carl.Gehr.ButNoSPAMStuff@MCGCG.Com>
- **Date:** 2006-12-30T13:43:52-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2b89$4596b36b$d066072d$16633@FUSE.NET>`
- **In-Reply-To:** `<6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net> <dc1c9$4596089e$d066072d$15186@FUSE.NET> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net>`

```
Arnold Trembley wrote:
> 
> 
…[35 more quoted lines elided]…
 ><Snip>
Just for point of clarity, we do not use source code.  We scan 
object/load modules.  In this case, we look at the actual code pattern 
to determine the presence of a SEARCH ALL and the level of LE in use.

But, you know your requirements best.  Good luck!
Carl
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 7)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2006-12-30T20:37:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<x6Alh.302335$Fi1.66670@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<a2b89$4596b36b$d066072d$16633@FUSE.NET>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net> <dc1c9$4596089e$d066072d$15186@FUSE.NET> <6iplh.605537$QZ1.180391@bgtnsc04-news.ops.worldnet.att.net> <a2b89$4596b36b$d066072d$16633@FUSE.NET>`

```


CG wrote:

> (snip) 
> Just for point of clarity, we do not use source code.  We scan 
…[4 more quoted lines elided]…
> Carl

That is a horse of a different color.  Our sysprogs have their own 
tools for scanning a loadlib and identifying the release of COBOL that 
each program was compiled with, and the compile-time options.

Thank you very much!
```

###### ↳ ↳ ↳ Re: IBM and COBOL SEARCH ALL

_(reply depth: 4)_

- **From:** Clark F Morris <cfmpublic@ns.sympatico.ca>
- **Date:** 2007-01-01T23:33:27+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pf6jp2p7bo8oec41o4j5l79b0dvjhoq6mu@4ax.com>`
- **References:** `<Ztjfh.384042$%j2.255292@fe07.news.easynews.com> <elpov6$rkc$02$1@news.t-online.com> <f4Egh.505704$kz6.420366@fe08.news.easynews.com> <_x2lh.598321$QZ1.166670@bgtnsc04-news.ops.worldnet.att.net>`

```
On Fri, 29 Dec 2006 06:26:02 GMT, Arnold Trembley
<arnold.trembley@worldnet.att.net> wrote:

>
>
…[42 more quoted lines elided]…
>state code...

I would do the truncation but before doing the search test the third
character for space and executing the NOT FOUND condition for
non-blank.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
