[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# index vs subscript performance

_22 messages · 12 participants · 2001-03 → 2001-04_

---

### index vs subscript performance

- **From:** Charles Haatvedt Jr. <clastname@nospam.com>
- **Date:** 2001-03-26T02:10:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.1528611fcf33ddff989685@news>`

```
as a member of an application performance tuning team I am interested in 
the relative performance difference between using indexes vs subscripts. 
I have written a few very short programs to test this and I would 
speculate that the difference is nearly a factor of 4  (actually 
subscripts use 3.75 times as much CPU time).  Time is MONEY and we are 
analyzing some of our largest resource "hogs" in an attempt to reduce 
them. We are using STROBE to do the analysis...

=====>>>  Cobol II rel 4
=====>>>  OS/390
=====>>>  IBM's largest mainframes...

ps...   we are migrating to Cobol/390...  will recompiling generate any 
performance savings ???
```

#### ↳ Re: index vs subscript performance

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-03-25T20:38:16-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99ma30$sca$1@slb5.atl.mindspring.net>`
- **References:** `<MPG.1528611fcf33ddff989685@news>`

```
I suggest that you check out the IBM "tuning" paper at:

 http://www-4.ibm.com/software/ad/cobol/library/booksabc/cobpf120.pdf

that talks specifically about this issue.

P.S.  That tuning paper is a "couple of releases" out of date, but should
give you some guidance.

VS COBOL II goes out of service (in the US) at the end of next week, so I
hope/assume that when you talk about going to "COBOL/390" - you actually
mean IBM COBOL for OS/390 & VM V2R2 - which is the "latest and greatest"
release and DOES include some binary data "performance improvements"
```

#### ↳ Re: index vs subscript performance

- **From:** "Peet Grobler" <peetg@absa.co.za>
- **Date:** 2001-03-26T07:57:39+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abee29b$0$228@hades.is.co.za>`
- **References:** `<MPG.1528611fcf33ddff989685@news>`

```
In my experience, and I'm pretty sure everyone will agree, when moving to
better hardware, it's always recommended to re-compile everything. The
Cobol/390 compiler is probably better than the one you're using now, and
performance-tuned for the hardware. It will be worth the effort to
re-compile.

Charles Haatvedt Jr. wrote in message ...

<SNIP>
>ps...   we are migrating to Cobol/390...  will recompiling generate any
>performance savings ???
…[5 more quoted lines elided]…
>          email ===>>>  chaatvedt  at  home dot com
```

#### ↳ Re: index vs subscript performance

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-03-26T07:50:30-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<WPHv6.536$aD4.40142@news2.atl>`
- **References:** `<MPG.1528611fcf33ddff989685@news>`

```
"Charles Haatvedt Jr." <clastname@nospam.com> wrote:
> as a member of an application performance tuning team I am interested in
> the relative performance difference between using indexes vs subscripts.
…[4 more quoted lines elided]…
> them. We are using STROBE to do the analysis...

Here are a few of points to consider.

1. The relative difference is very dependant on the compiler and
   hardware platform.  For example, because the COBOL standard does
   not specify how indexes are to be constructed, some compilers
   default to simple numeric pointers, identically equivalent to
   subscripts.

2. Whether to use subscripting or indexing in a particular situation
   is a complex issue, and the answer depends primarily on these
   factors:
   a. Cost of setting/incrementing/decrementing index vs. subscript
   b. Cost of reference using index vs. subscript
   c. Ratio of times index/subscript is set/inc/dec vs. reference
   d. Frequency of conversion between index and numeric field

In general, a program that does many references to a table for every
time the index/subscript is set, indexing will tend to be faster.
But if the ratio of table references to times the index/subscript is
lowered, particularly if an index is often converted to/from numeric
data fields, subscripting can be faster, even much faster (e.g. set
index to numeric variable, reference table only once.)

Another thing to consider is, in the tests we have done here in the
newsgroup, if you are using either indexing or subscripting to scan
a field character by character, it will probably be faster if you
use a numeric field and reference modification.  The difference can
be sigbificant.  But again, it very much depends on the compiler and
platform. :-)
```

##### ↳ ↳ Re: index vs subscript performance

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-03-26T11:04:43-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<xGKv6.608$tG3.42424@news1.atl>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <WPHv6.536$aD4.40142@news2.atl>`

```
"Judson McClendon" <judmc@bellsouth.net> wrote:
>
> 2. Whether to use subscripting or indexing in a particular situation
…[5 more quoted lines elided]…
>    d. Frequency of conversion between index and numeric field

The above is concerned purely with efficiency.  In practice, other
considerations such as readability and shop standards must always be
considered.  Just didn't want anyone to think I'm a 'Performance is
the Only Thing' programmer. :-)
```

#### ↳ Re: index vs subscript performance

- **From:** "WOB" <wobconsult@sprynet.com>
- **Date:** 2001-03-26T18:07:48-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99ohjr$va7$1@slb7.atl.mindspring.net>`
- **References:** `<MPG.1528611fcf33ddff989685@news>`

```
IHMO, indices will always outperform subscripts, simply because register
notation and usage is used primarily with indices. The only subscripts that
will even come close, are the ones defined as fullword binary, which in IBM
speak is S9(08) S9(09) BINARY, coupled with the TRUNC(OPT) compiler option.
The WORST data type you could use for subscripts is Display Numeric,
followed by Packed-Decimal. However, usage of fullwords and compile options
TRUNC(STD) or TRUNC(BIN) will reduce any possibility of efficiency to that
of the BRUTAL inefficiency of Display Numeric.

HTH....

Bill

"Charles Haatvedt Jr." <clastname@nospam.com> wrote in message
news:MPG.1528611fcf33ddff989685@news...
> as a member of an application performance tuning team I am interested in
> the relative performance difference between using indexes vs subscripts.
…[17 more quoted lines elided]…
>           email ===>>>  chaatvedt  at  home dot com
```

##### ↳ ↳ Re: index vs subscript performance

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-03-27T03:50:23+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net>`

```

"WOB" <wobconsult@sprynet.com> wrote in message
news:99ohjr$va7$1@slb7.atl.mindspring.net...
> IHMO, indices will always outperform subscripts, simply because
register
> notation and usage is used primarily with indices. ...

I just performed an experiment:

PERFORM 100000 TIMES
   SET INDX TO 0
    PERFORM VARYING J FROM 1 BY 1 UNTIL J > 10000
      SET INDX UP BY 1                            [Line 'x']
      MOVE 'A' TO A-ARRAY(INDX)        [Line 'y']
      MOVE 'B' TO B-ARRAY(J)                 [Line 'z']
      END-PERFORM
   END-PERFORM


With Lines 'x'  'y'  and 'z' commented (no MOVEs executed), the
overhead averaged 5.98 seconds.

With Line 'x' and 'y' commented, such that we move by SUBSCRIPT,
average execution time 11.22 seconds

With Line 'z' alone commented, such that we move by INDEX, average
execution time 11.55 seconds.


Conclusions:
1. Subscripting is faster by 0.33 seconds for 100 million single bytes
moved, 3.3 seconds per gigabyte.
2. It is doubtful whether anyone cares.


The tests were run using the Fujitsu compiler (debug mode) on an
900MHz PC.

Your results may vary, but as for me, I say to hell with indexes; they
should be banned from COBOL.  Where do I write?
```

###### ↳ ↳ ↳ Re: index vs subscript performance

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-03-27T14:02:22+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net>`

```
On Tue, 27 Mar 2001 03:50:23 GMT "Jerry P" <jerryp@bisusa.com> wrote:

:>"WOB" <wobconsult@sprynet.com> wrote in message
:>news:99ohjr$va7$1@slb7.atl.mindspring.net...

:>> IHMO, indices will always outperform subscripts, simply because
:>register
:>> notation and usage is used primarily with indices. ...

:>I just performed an experiment:

:>PERFORM 100000 TIMES
:>   SET INDX TO 0
:>    PERFORM VARYING J FROM 1 BY 1 UNTIL J > 10000
:>      SET INDX UP BY 1                            [Line 'x']
:>      MOVE 'A' TO A-ARRAY(INDX)        [Line 'y']
:>      MOVE 'B' TO B-ARRAY(J)                 [Line 'z']
:>      END-PERFORM
:>   END-PERFORM

:>With Lines 'x'  'y'  and 'z' commented (no MOVEs executed), the
:>overhead averaged 5.98 seconds.

:>With Line 'x' and 'y' commented, such that we move by SUBSCRIPT,
:>average execution time 11.22 seconds

:>With Line 'z' alone commented, such that we move by INDEX, average
:>execution time 11.55 seconds.


:>Conclusions:
:>1. Subscripting is faster by 0.33 seconds for 100 million single bytes
:>moved, 3.3 seconds per gigabyte.
:>2. It is doubtful whether anyone cares.


:>The tests were run using the Fujitsu compiler (debug mode) on an
:>900MHz PC.

:>Your results may vary, but as for me, I say to hell with indexes; they
:>should be banned from COBOL.  Where do I write?

What are the sizes of A-ARRAY and B-ARRAY? Could the subscript be converted
into an index by a shift?

Does debug mode remove all optimizations? I would expect that the compiler
would internally create a "shadow" index for B-ARRAY.

Try inserting a CALL statement right after the perform so that some
optimization will be lost.
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 4)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-03-27T13:20:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com

>
> What are the sizes of A-ARRAY and B-ARRAY?

OCCURS 10000 PIC X.

> Could the subscript be converted
> into an index by a shift?

Sure. the subscript is defined as PIC S9(7) COMP-5. But so what? It
shouldn't matter if subscripts are converted to indexes or bananas;
unless we're trying to find a case - however constructed - to justify
the dogma of using indexes instead of subscripts (or vice-versa).

>
> Does debug mode remove all optimizations? I would expect that the
compiler
> would internally create a "shadow" index for B-ARRAY.

Possibly. But I can't imagine the un-optimized assembly code in this
example being different from the optimized.

>
> Try inserting a CALL statement right after the perform so that some
> optimization will be lost.

Better idea: I'll leave that to others. I've demonstrated to myself
that - in at least one common case - that indexing and subscripting
are indistinguishable. I think next I'll have a look at the SEARCH
verb. Maybe, just maybe, we can define indexes as 'archaic' (or at
least 'silly').


>
> --
…[5 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 5)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-03-27T16:25:05+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<mh81ctseo5hovj163i676679a8pf04koid@4ax.com>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com> <Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net>`

```
On Tue, 27 Mar 2001 13:20:36 GMT "Jerry P" <jerryp@bisusa.com> wrote:

:>"Binyamin Dissen" <postingid@dissensoftware.com

:>> What are the sizes of A-ARRAY and B-ARRAY?

:>OCCURS 10000 PIC X.

In which case the subscript is the same as the index.

:>> Could the subscript be converted
:>> into an index by a shift?

:>Sure. the subscript is defined as PIC S9(7) COMP-5. But so what? It
:>shouldn't matter if subscripts are converted to indexes or bananas;
:>unless we're trying to find a case - however constructed - to justify
:>the dogma of using indexes instead of subscripts (or vice-versa).

The case of one byte elements is an exception.

No conversion is required to convert the subscript to an index.

:>> Does debug mode remove all optimizations? I would expect that the
:>compiler
:>> would internally create a "shadow" index for B-ARRAY.

:>Possibly. But I can't imagine the un-optimized assembly code in this
:>example being different from the optimized.

If data is retained in registers ....

:>> Try inserting a CALL statement right after the perform so that some
:>> optimization will be lost.

:>Better idea: I'll leave that to others. I've demonstrated to myself
:>that - in at least one common case - that indexing and subscripting
:>are indistinguishable. I think next I'll have a look at the SEARCH
:>verb. Maybe, just maybe, we can define indexes as 'archaic' (or at
:>least 'silly').

You have proven it in the case where subscripts and indexes are identical.

In other words, you have proven nothing.
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 6)_

- **From:** "Jerry P" <jerryp@bisusa.com>
- **Date:** 2001-03-28T13:19:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9xlw6.4394$aP5.356855@newsread2.prod.itd.earthlink.net>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com> <Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net> <mh81ctseo5hovj163i676679a8pf04koid@4ax.com>`

```

"Binyamin Dissen" <postingid@dissensoftware.com
>
> You have proven it in the case where subscripts and indexes are
identical.
>
> In other words, you have proven nothing.
>

As you say, I proved the case that "subscripts and indexes are
identical". Substantially more than nothing.

If someone can generate a common programming case where the timing
results between S & I are substantially different, I'd certainly like
to know about it.

So far, all I've seen is an IBM technical paper asserting that
subscripting could be 400%+ slower. It could be, however, that
advances in compiler technology since the publication of the paper
have diminished the differences. If I remember correctly, IBM timed
various data representations of the subscript variable (packed,
display, etc.). But that's not a fair test of S vs. I; let's see a
timing test of S vs. I with only the logic at issue. That is, define
the subscript as a COMP variable.
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 7)_

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2001-03-28T20:13:25+02:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g6a4ctg65t1s7g1qrfn2d1fmd88d4n2e8r@4ax.com>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com> <Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net> <mh81ctseo5hovj163i676679a8pf04koid@4ax.com> <9xlw6.4394$aP5.356855@newsread2.prod.itd.earthlink.net>`

```
On Wed, 28 Mar 2001 13:19:01 GMT "Jerry P" <jerryp@bisusa.com> wrote:

:>"Binyamin Dissen" <postingid@dissensoftware.com

:>> You have proven it in the case where subscripts and indexes are
:>identical.

:>> In other words, you have proven nothing.

:>As you say, I proved the case that "subscripts and indexes are
:>identical". Substantially more than nothing.

Perhaps I wasn't clear.

With a table entry size of one byte, the subscript really doesn't require
manipulation to be converted into an index. In the case of a one byte table
entry one would not expect to find a difference between a subscript or an
index.

If the table entry was two bytes, the subscript would have to be doubled to
become and index. This would probably be done via shift.

If the table entry was 243 bytes, the subscript would have to be multiplied to
be converted into an index. Now we are talking some additional processing
time.

:>If someone can generate a common programming case where the timing
:>results between S & I are substantially different, I'd certainly like
:>to know about it.

A longer table entry (assuming that the implementation of INDEX is good).

:>So far, all I've seen is an IBM technical paper asserting that
:>subscripting could be 400%+ slower. It could be, however, that
:>advances in compiler technology since the publication of the paper
:>have diminished the differences. If I remember correctly, IBM timed
:>various data representations of the subscript variable (packed,
:>display, etc.). But that's not a fair test of S vs. I; let's see a
:>timing test of S vs. I with only the logic at issue. That is, define
:>the subscript as a COMP variable.

Multiplying costs. Depending how many fields are in each table entry you might
have a bit of work.
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-03-28T14:50:17-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oXsw6.2188$aD4.120762@news2.atl>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com> <Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net> <mh81ctseo5hovj163i676679a8pf04koid@4ax.com> <9xlw6.4394$aP5.356855@newsread2.prod.itd.earthlink.net> <g6a4ctg65t1s7g1qrfn2d1fmd88d4n2e8r@4ax.com>`

```
"Binyamin Dissen" <postingid@dissensoftware.com> wrote:
>
> With a table entry size of one byte, the subscript really doesn't require
…[5 more quoted lines elided]…
> become and index. This would probably be done via shift.

Pardon me if I missed something, but the above is only true on some
hardware platforms.  If the computer memory is word addressed (e.g.
Unisys A Series) what you say above would not be accurate. :-)

On other platforms (e.g. the now [AFAIK] defunct B1x00 series), it
takes precisely as long to do an integer multiply as it does to add,
subtract or divide.
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 9)_

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2001-03-29T23:20:30-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9a11ce$5gjk$1@newssvr06-en0.news.prodigy.com>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com> <Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net> <mh81ctseo5hovj163i676679a8pf04koid@4ax.com> <9xlw6.4394$aP5.356855@newsread2.prod.itd.earthlink.net> <g6a4ctg65t1s7g1qrfn2d1fmd88d4n2e8r@4ax.com> <oXsw6.2188$aD4.120762@news2.atl>`

```
Judson McClendon judmc@bellsouth.net  wrote:

>Pardon me if I missed something, but the above is only true on some
>hardware platforms.  If the computer memory is word addressed (e.g.
>Unisys A Series) what you say above would not be accurate. :-) <

Amen!  Having worked on both IBM and Unisys Mainframes, it didn't take me
long to realize that we need to be careful what we assume.  I have found
that subscripting on the Unisys platform is as quick or generally quicker
than indexing was on the IBM platform.  And subscripts are much easier to
find in Unisys memory dumps, than indexes. :~)

Denny
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 10)_

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-03-30T06:52:00-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gl%w6.2945$aD4.184654@news2.atl>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com> <Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net> <mh81ctseo5hovj163i676679a8pf04koid@4ax.com> <9xlw6.4394$aP5.356855@newsread2.prod.itd.earthlink.net> <g6a4ctg65t1s7g1qrfn2d1fmd88d4n2e8r@4ax.com> <oXsw6.2188$aD4.120762@news2.atl> <9a11ce$5gjk$1@newssvr06-en0.news.prodigy.com>`

```
"Denny Brouse" <denden@prodigy.net> wrote:
> Judson McClendon judmc@bellsouth.net  wrote:
> >
…[8 more quoted lines elided]…
> find in Unisys memory dumps, than indexes. :~)

Yes, reading an A Series memory dump is, shall we say ... interesting. ;-)
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 7)_

- **From:** Keith Odam <0dam-k@iname.com>
- **Date:** 2001-04-05T07:25:56+09:30
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ACB986C.F94A3E8F@iname.com>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com> <Es0w6.603$Uw.74978@newsread1.prod.itd.earthlink.net> <mh81ctseo5hovj163i676679a8pf04koid@4ax.com> <9xlw6.4394$aP5.356855@newsread2.prod.itd.earthlink.net>`

```
Jerry P wrote:
> "Binyamin Dissen" <postingid@dissensoftware.com
> > You have proven it in the case where subscripts and
> > indexes are identical.
[ ... ]
> As you say, I proved the case that "subscripts and
> indexes are identical". Substantially more than nothing.

  I think it helps to be clear about your terminology.
A table entry has an occurrence number and an offset.
A subscript is an explicit occurrence number and is
converted to an offset value for addressing and not
"converted into an index". (Your compiler may maintain
an index item in the background, but doesn't need to).  

  The timing values of Jerry's example are not surprising,
as both cases include the arithmetic to increment the data
item (J) used as a subscript while only the indexing case
includes the arithmetic to increment the index.
  "PERFORM 10000 TIMES" can be faster than incrementing
and testing an otherwise unused data item.
  (Binyamin has noted that the example uses the special
case of a single character table element.)

  It seems to me that indexes offer performance differences
that can be large on different platforms while both should
work on all.  As always, code for correct results with
allowance to tune for performance.
```

###### ↳ ↳ ↳ Re: index vs subscript performance

_(reply depth: 4)_

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2001-03-27T10:42:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99qfur$5o1$1@slb2.atl.mindspring.net>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <99ohjr$va7$1@slb7.atl.mindspring.net> <36Uv6.16278$ue1.1378062@newsread2.prod.itd.earthlink.net> <f201ct8h7slmdmhnolcn8g4dcdag7h8ql3@4ax.com>`

```
As someone who is familiar with at least one PC "optimization" and one IBM
mainframe "optimization" - let me say that they tend to work VERY
differently when it comes to "subscripts" versus "indexing".  In fact, there
is even an option in Micro Focus to "guarantee" that indexes *are* stored as
"subscripts".  (I believe one other PC compiler *only* stored them that
way.)

Bottom-Line:
  Deciding when to use subscripting versus indexing FOR PERFORMANCE reasons,
requires testing in "your environment" - with code that is identical (or at
least similar) to the code in question.
  Deciding when to use subscripting versus indexing for "maintainability" or
"readability" reasons, requires that you know what your "shop" standards
are - or at least what may or may not "reasonably" be expected of those who
will be working on the program at any time in the future.
```

#### ↳ Re: index vs subscript performance

- **From:** John H Sleight Jr <John_member@newsranger.com>
- **Date:** 2001-03-27T04:36:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<pNUv6.3249$fy.5332@www.newsranger.com>`
- **References:** `<MPG.1528611fcf33ddff989685@news>`

```
Hi Chuck,

Some other points you may want to consider:

1) I remember reading somewher that the breakeven pint is at about 70 elements,
beyond that, indexing is the preferred method.

2) index v subs isn't the only performance consideration. The distribution
of access into the table can also be a big consideration. To take a loaded
example to illustrate the point: 
You have a table of 100 entries accessed a million times; of that million 900
thousand access the three entries of the table the other 100 thou are evenly
distributed. Whether you use indexes or subs, three if statements before the
search will save tons of CPU.

3) If the pgm does a lot of calculations, etc. after finding the entry in the
table, CPU savings can be realized by moving the element to a work area
(unindexed, of course) and doing the calcs with the work field saving all the
CPU required to translate the index and moves to save areas, etc. 

Just my 2c, Jack.     



In article <MPG.1528611fcf33ddff989685@news>, Charles Haatvedt Jr. says...
>
>as a member of an application performance tuning team I am interested in 
…[18 more quoted lines elided]…
>          email ===>>>  chaatvedt  at  home dot com
```

#### ↳ Re: index vs subscript performance

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 2001-03-27T19:32:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ac0e91b.64834306@news.open.org>`
- **References:** `<MPG.1528611fcf33ddff989685@news>`

```
After reading the threads that this subject has generated, I think I
see a common opinion that regarding performance, the only appropriate
generic answer is "it depends".  Even on the same platform it still
depends because the nature of what you are doing with the table will
significantly impact performance, and in some cases can make
subscripts perform better than indexes.

If "it depends" is the final answer, then can we ever really justify a
standard regarding subscripts vs. indexes?

By the way, my mainframe shop here has no standard.  The developer
gets to code it either way, and no one really cares as long as the
results are correct.  Regarding the "Time is MONEY" statement, we have
a philosophy that the machines are so fast today that it would be very
wasteful of programmer time to force a programmer to use indexes when
they are uncomfortable doing so.

Pete


On Mon, 26 Mar 2001 02:10:32 GMT, Charles Haatvedt Jr.
<clastname@nospam.com> wrote:

>as a member of an application performance tuning team I am interested in 
>the relative performance difference between using indexes vs subscripts. 
…[17 more quoted lines elided]…
>          email ===>>>  chaatvedt  at  home dot com
```

##### ↳ ↳ Re: index vs subscript performance

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-03-28T11:03:33-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RCpw6.1976$aD4.114968@news2.atl>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <3ac0e91b.64834306@news.open.org>`

```
"Pete Wirfs" <petwir@saif.com> wrote:
>
> After reading the threads that this subject has generated, I think I
…[14 more quoted lines elided]…
> they are uncomfortable doing so.

That's about it, Pete.  Good programmers understand the tradeoffs
between indexing and subscripting and will choose the one they feel
is best for the situation.  If the programmer is any good, they will
probably be correct most of the time, with very little extra penalty
on the times they aren't.

As far as shop standards, I believe it would be better to educate
the programmers on the issues discussed in this thread, and let them
use their own judgment in practice. :-)
```

#### ↳ Re: index vs subscript performance

- **From:** Colin Campbell <cmcampb@attglobal.net>
- **Date:** 2001-04-04T14:08:10-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ACB8D39.9703B746@attglobal.net>`
- **References:** `<MPG.1528611fcf33ddff989685@news>`

```
I have done optimizations of COBOL programs for many years, generally on
the IBM mainframe.  In addition, I have written COBOL compilers.  Of the
many answers offered below, I would say first, that we have found it
possible to save enough money (in the form of reduced CPU time) to
justify keeping an eye on our expensive jobs, and second, that it is
dangerous to generalize about the subject of index items vs. subscripts.

In the COBOL compilers I worked on, I am willing to admit that we kept
index values as binary integers (the same as a "good" subscript).  Thus,
very little performance advantage could be gained from using index
items, unless the programmer was so unwary as to use USAGE DISPLAY, or
omit an operational sign, etc., on the subscript definition.

On the other hand, IBM compilers maintain an index item as the offset
from the start of a table.  In a simple example, with 5 character
entries, the subscript 1 equates to an index value 0, subscript 2 =
index 5, etc.  A subscript, when used, must be loaded into a register,
have 1 subtracted from it, and then be multiplied by the table item
length (at which time it is equal to the index item, if there is one).
Then, either the index item of the computed subscript is added to the
address of the table, and the program is pointing at the right item in
the table.

I have personally optimized programs where I did not touch the Procedure
Division, but only changed USAGE and PICTURE in the Data Division, and
the program ran in only 50% of the original CPU time.

I believe that good standards can be developed in this area, depeneding
on the platform, compiler, etc.  A shop would be foolhardy to ignore the
chance to save run time dollars.

Much more to the point, programmers are capable of making bad code.  In
another example, we found a program that runs in 8 different jobs,
adding rates to records in a sequential data set.  When it was
originally coded, it looked up the rates in a table that was read into
memory.  As time went on, the table could no longer hold all of the rate
info, so code was added to check for table overflow, and if that
occurred, get the information from a DB2 table.  Now, a 9 million record
file does 9 million DB2 accesses.  The number of different keys for
which rates are looked up proves to be under 10,000.  So, a little
rethinking says:
1.  Is the key I want the same as the last key I wanted?  If so, I have
the answer.
2.  Is the key I want in a table I've built of all the answers?  If so,
I have the answer.
3.  If neither of the above cases is true, I need to get the answer from
DB2, and add it to the table (in sequence, so that I can do a SEARCH
ALL).

The net result was a savings of well over $11,000 each time these jobs
run -- a 97% reduction.

A similar case occurred years ago.  A program was reading a sequential
data set and making an IMS call for every record.  We found that the IMS
data base was being unloaded three steps earlier in the job, so we
changed to a sequential two file match, and cut the cost over 90%.

A final word about index vs. subscript:
Improper table handling leads to some of the toughest to find errors
when programs abend.  A shop is well advised to promote and require good
table loading techniques to ensure that little things like table
overflow don't occur.

The smart answer is that you should never get complacent.  Always look
for problems.  You'll usually find something that can be improved.
Colin Campbell
```

##### ↳ ↳ Re: index vs subscript performance

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 2001-04-05T11:44:37-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Th1z6.106$be.8857@news1.atl>`
- **References:** `<MPG.1528611fcf33ddff989685@news> <3ACB8D39.9703B746@attglobal.net>`

```
"Colin Campbell" <cmcampb@attglobal.net> wrote:
>
> On the other hand, IBM compilers maintain an index item as the offset
…[7 more quoted lines elided]…
> the table.

There is no need of subtracting 1 from the subscript in cases where the
table begins at least the length of 1 entry from address 0.  You simply
apply the calculated offset from Table - EntryLength.

> Much more to the point, programmers are capable of making bad code.  In
> another example, we found a program that runs in 8 different jobs,
…[14 more quoted lines elided]…
> ALL).

Do a frequency analysis on the items in the database and load the table
with only the entries that have the highest hit-rate.  Assuming, of
course, that there is a pattern in the hit-rate.  Such data might be
generated from each run, and used to load the table for the next run.
This would allow for gradually changing patterns in the hit-rate.

> The smart answer is that you should never get complacent.  Always look
> for problems.  You'll usually find something that can be improved.

Something can *always* be improved. ;-)  'Optimization' is a misnomer,
for it is actually an iterative approach toward 'optimum', which is
virtually never reached in practice, for any complex procedure.  You
eventually reach a point of diminishing returns where you must begin
to sacrifice efficiency in one area to gain in another. :-)

A few years ago someone posted a simple, elegant string operation.
For fun we worked on it for a while and wound up with code that was
less elegant, but about 100 times faster than the original, elegant
code.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
