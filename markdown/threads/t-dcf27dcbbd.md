[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# EVALUATE - odd behaviour

_7 messages · 6 participants · 2003-06_

**Topics:** [`Language features and syntax`](../topics.md#syntax)

---

### EVALUATE - odd behaviour

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-23T16:34:22+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef68056_1@corp-news.newsgroups.com>`

```
I wondered if anyone might care to comment on the following EVALUATE...

It gives a compiler error at the point indicated, saying that a conditional
statement is found where an imperative statement is required. If I cut the
code to a separate paragraph/section and PERFORM it from the Evaluate it,
compiles and runs correctly.

I don't understand why EVALUATE in general actually doesn't allow a
conditional statement and was hoping someone who is up with the standards
could elucidate. If this behaviour is correct, why doesn't it grizzle about
the IF under the first WHEN?

Why have countless EVALUATEs all worked OK woth IF statements in them and
then this one decides to adhere tot he letter of the Law <G>?

Here's the code...


     evaluate TRUE
        when HV-BkgStatus  < 2
* User has cancelled out and left the DB hanging... Give them 30 minutes...
             if lnk-yyyymmdd NOT > today-yyyymmdd
                if lnk-yyyymmdd < today-yyyymmdd
                   move zero to getHOURS
                                getMINS
                end-if
                compute ticks-row = (getHOURS * 3600) + (getMINS * 60)
                if (ticks-row + 1800) < ticks-now
                   perform drop-it
                   add 1 to total-drop-s1
                   subtract 1 from total-rows-after
                end-if
             end-if
        when HV-BkgStatus = 2
* Check that this unconfirmed Booking has not exceeded the hours we hold
* such a Booking for...(User configurable)

At this point the Fujitsu 97 Compiler packs a sad and goes off in a
huff...<G>

If I cut the code from here:
             if holdForHours NOT = 9999
                add getHours to holdForHours
                divide holdForHours by 24
                          giving holdForDays remainder holdForHours
                end-divide
                if holdForDays NOT = zero
                   move lnk-yyyymmdd to digits-8
                   compute digits-8 = function date-of-integer
                        (function integer-of-date (digits-8) + holdForDays)
                   move digits-8 to lnk-yyyymmdd
                   move holdForHours to getHours
                   move zero to getMINS
                end-if
                if lnk-yyyymmdd < today-yyyymmdd
                   perform drop-it
                   add 1 to total-drop-s2
                   subtract 1 from total-rows-after

                else
                   compute ticks-row = (getHOURS * 3600) + (getMINS * 60)
                   if ticks-row NOT > ticks-now
                   perform drop-it
                   add 1 to total-drop-s2
                   subtract 1 from total-rows-after
                end-if
             end-if
...to here, and replace it with a PERFORM, the whole lot compiles and runs
perfectly...


        when HV-BkgStatus  = 3
* If it's after the departure date, delete it. (Time period is user
configurable...)
             continue
     end-evaluate

I'm simply too busy at the moment to investigate deeply or worry about this,
but it is interesting and I thought someone might see it immediately...

Pete.
```

#### ↳ Re: EVALUATE - odd behaviour

- **From:** "Rick Smith" <ricksmith@mfi.net>
- **Date:** 2003-06-23T00:52:57-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vfd1uesibb0fe7@corp.supernews.com>`
- **References:** `<3ef68056_1@corp-news.newsgroups.com>`

```

Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote in message
news:3ef68056_1@corp-news.newsgroups.com...
> I wondered if anyone might care to comment on the following EVALUATE...
>
> It gives a compiler error at the point indicated, saying that a
conditional
> statement is found where an imperative statement is required. If I cut the
> code to a separate paragraph/section and PERFORM it from the Evaluate it,
…[4 more quoted lines elided]…
> could elucidate. If this behaviour is correct, why doesn't it grizzle
about
> the IF under the first WHEN?
>
…[8 more quoted lines elided]…
> * User has cancelled out and left the DB hanging... Give them 30
minutes...
>              if lnk-yyyymmdd NOT > today-yyyymmdd
>                 if lnk-yyyymmdd < today-yyyymmdd
…[26 more quoted lines elided]…
>                         (function integer-of-date (digits-8) +
holdForDays)
>                    move digits-8 to lnk-yyyymmdd
>                    move holdForHours to getHours
…[8 more quoted lines elided]…
>                    compute ticks-row = (getHOURS * 3600) + (getMINS * 60)
=====
It looks like the following 'if' is not terminated. Based on indentation.
>                    if ticks-row NOT > ticks-now
>                    perform drop-it
>                    add 1 to total-drop-s2
>                    subtract 1 from total-rows-after
=====
>                 end-if
>              end-if
…[10 more quoted lines elided]…
> I'm simply too busy at the moment to investigate deeply or worry about
this,
> but it is interesting and I thought someone might see it immediately...
>
> Pete.
>
>
```

#### ↳ Re: EVALUATE - odd behaviour

- **From:** "William M. Klein" <wmklein@ix.netcom.com>
- **Date:** 2003-06-22T23:57:45-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd61f9$ptl$1@slb5.atl.mindspring.net>`
- **References:** `<3ef68056_1@corp-news.newsgroups.com>`

```
Can we say "indentation" ???  Look at the line with

    "if ticks-row NOT > ticks-now"

and try and find an END-IF for it ???

You may have as "deeply" nested IF statements as you want in the WHEN phrase
of an EVALUATE - but you need to make certain that they are ALL "made
imperative" with END-IF's.
```

#### ↳ Re: EVALUATE - odd behaviour

- **From:** Richard Plinston <riplin@Azonic.co.nz>
- **Date:** 2003-06-23T20:02:33+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd6c6u$sdb$1@aklobs.kc.net.nz>`
- **References:** `<3ef68056_1@corp-news.newsgroups.com>`

```
Peter E.C. Dashwood wrote:

> It gives a compiler error at the point indicated, saying that a
> conditional statement is found where an imperative statement is required.
…[6 more quoted lines elided]…
> about the IF under the first WHEN?

This was covered a few weeks ago here.  A conditional statement can be 
turned into an imperitive statement by having it correctly terminataed.

Conditional statement:

          IF ( x )
              do something

Imperitive statement:

          IF ( x )
              do something
          END-IF


> At this point the Fujitsu 97 Compiler packs a sad and goes off in a
> huff...<G>
…[23 more quoted lines elided]…
>                    if ticks-row NOT > ticks-now
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                   
>                    perform drop-it
>                    add 1 to total-drop-s2
…[4 more quoted lines elided]…
> perfectly...


The statement has a missing END-IF - therefore conditional not imperitive.

Within an IF or a separate paragraph a conditional is OK.
```

#### ↳ Re: EVALUATE - odd behaviour. THANKS to all...

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-06-24T00:29:26+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ef6f31b_9@news.athenanews.com>`
- **References:** `<3ef68056_1@corp-news.newsgroups.com>`

```
Thank you to Rick, Bill, and Richard who all spotted it correctly (in no
time flat...<G>)

My face is red, but I deserve it.

I had totally missed the offending IF and that is why it wasn't indented. I
do normally indent carefully and use scope terminators always.

I looked at this for some thirty minutes before posting it...<G> Mea Culpa.

Good job all, and thanks again.

Pete.



"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote in message
news:3ef68056_1@corp-news.newsgroups.com...
> I wondered if anyone might care to comment on the following EVALUATE...
>
> It gives a compiler error at the point indicated, saying that a
conditional
> statement is found where an imperative statement is required. If I cut the
> code to a separate paragraph/section and PERFORM it from the Evaluate it,
…[4 more quoted lines elided]…
> could elucidate. If this behaviour is correct, why doesn't it grizzle
about
> the IF under the first WHEN?
>
…[8 more quoted lines elided]…
> * User has cancelled out and left the DB hanging... Give them 30
minutes...
>              if lnk-yyyymmdd NOT > today-yyyymmdd
>                 if lnk-yyyymmdd < today-yyyymmdd
…[26 more quoted lines elided]…
>                         (function integer-of-date (digits-8) +
holdForDays)
>                    move digits-8 to lnk-yyyymmdd
>                    move holdForHours to getHours
…[25 more quoted lines elided]…
> I'm simply too busy at the moment to investigate deeply or worry about
this,
> but it is interesting and I thought someone might see it immediately...
>
> Pete.
>
>
```

##### ↳ ↳ Re: EVALUATE - odd behaviour. THANKS to all...

- **From:** docdwarf@panix.com
- **Date:** 2003-06-23T10:54:44-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bd74bk$f22$1@panix1.panix.com>`
- **References:** `<3ef68056_1@corp-news.newsgroups.com> <3ef6f31b_9@news.athenanews.com>`

```
In article <3ef6f31b_9@news.athenanews.com>,
Peter E.C. Dashwood <dashwood@enternet.co.nz> wrote:
>Thank you to Rick, Bill, and Richard who all spotted it correctly (in no
>time flat...<G>)
>
>My face is red, but I deserve it.

The technique employed here seems to be a variant of 'Four-eyed 
debugging'... sometimes the Olde Wayse still work, aye.

DD
```

##### ↳ ↳ Re: EVALUATE - odd behaviour. THANKS to all...

- **From:** Colin Campbell <cmcampb@attgloabl.net>
- **Date:** 2003-06-23T09:34:06-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3EF72BFE.5D01295D@attgloabl.net>`
- **References:** `<3ef68056_1@corp-news.newsgroups.com> <3ef6f31b_9@news.athenanews.com>`

```
Peter,
It seems as if there's a lesson here:
Believe your compiler!

Since it tells you that not all of the statements are imperative, you can
immediately zero in on the "IF's" as a starting point.  If those had not been
the offenders, you would start looking for things like "ON OVERFLOW", "ON SIZE
ERROR", etc.

Your workaround reinforces the fact that the compiler told you what you needed
to know.  It is obvious that the offending statement was in the chunk code that
that you moved into a PERFORM'ed procedure.

I don't use Fujitsu's compiler, but the IBM mainframe and VA COBOL compilers
give you a helpful little goodie by showing the subordination level on the left
side of the listing.  Within a procedure, all statements at the "top level" have
a blank in this column.  When you code an IF, EVALUATE, PERFORM, etc, the
subordinate statements are assigned a "1", and so on.  If you have that, you can
use it to help you see failures to indent.  But really, you didn't need to go
that far....
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
