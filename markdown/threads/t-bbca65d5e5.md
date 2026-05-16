[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Who has had Y2K problems yet?

_26 messages · 21 participants · 1999-12 → 2000-01_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Who has had Y2K problems yet?

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83eq1m0119c@enews2.newsguy.com>`

```
It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half my day
remediating 4 production programs that were apparently 'missed', installing
the Standard Sliding Window.  The jobs were not canceling, but the users
started calling about weird reports.

I'm thinking that when Jan 1st rolls around, things won't crash much at all.
What will probably happen is a bunch of stuff gets screwed up and nobody
will know until the users start calling.

I think we will all be busy for a long time after the new year.

Jeff
Giant Food Inc.
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** "ChrisOsborne" <chris_n_osborne@yahoo.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<#kFnMfRS$GA.292@cpmsnbbsa02>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
At the turn of 1998 to 1999, my last firm experinced 6 date related abends
on the mainframe.  The common date program that calculated system run-dates
accidentally calculated either a day early on the 31st of December, or a day
late on the 3rd and 4th of January, for reasons still unknown.  Since the
problem stopped occuring, no one investigated.  As all data from systems
from that firm have now been transitioned to another firm's systems, that
particular problem won't occur again.


Jeff Baynard <union27@macconnect.com> wrote in message
news:83eq1m0119c@enews2.newsguy.com...
> It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half my
day
> remediating 4 production programs that were apparently 'missed',
installing
> the Standard Sliding Window.  The jobs were not canceling, but the users
> started calling about weird reports.
>
> I'm thinking that when Jan 1st rolls around, things won't crash much at
all.
> What will probably happen is a bunch of stuff gets screwed up and nobody
> will know until the users start calling.
…[4 more quoted lines elided]…
> Giant Food Inc.
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** "David W. Furin" <dfurin@larich.com>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<70E6DDB02DC50756.A3500C6E514DCAFF.FE6DCC6C83B908AE@lp.airnews.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
We had a small number of bugs reported after installing our Y2K
remediated software back in May.  Nothing serious, and all easily
fixed.  I am sure that other bugs (hopefully just as minor) will surface
after year-end.

However, our very first Y2K crisis came in May of 1998.  Our General
Ledger system uses a calendar file to keep track of fiscal period dates
for each of our companies, all of which have fiscal years that do not
start in January.   The financial calendar system knows about "previous"
"current" and "next" fiscal years.  In May 1998, one company was rolling
into the next year which meant that the "current" year became May '98 -
April '99 and NEXT year would become May '99 - April 2000.  Bang!  The
software couldn't cope.

I am embarassed to admit this caught us completely by surprise.
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** bberman@netbox.com (B Berman)
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385c3d7d.12756114@news.ntplx.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
On Fri, 17 Dec 1999 21:03:40 -0500, "Jeff Baynard"
<union27@macconnect.com> wrote:

>It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half my day
>remediating 4 production programs that were apparently 'missed', installing
…[5 more quoted lines elided]…
>will know until the users start calling.

I started seeing problems in the first week of December, in one system
that I inherited this past summer (guaranteed compliant they told me).

One customer, who transmits orders to us from Europe, started
complaining about wierd Specified-Ship-Dates on his Order Review
screen, for orders with ship-dates in January 2000.  Upon
investigating, I found that the order is transmitted with a ship-date
in format DDMMY (single-digit year).  The program that processed the
order converted the date properly and stored it in the database OK,
but the inquiry program could not handle the conversion back to YY.
Ironically, the problem will go away once we roll into January.

The program compared the ship-Y to the current year, and if less,
added 1 to the current decade (if 0 < 9, add 1 to decade(9) allowing
truncation).  Unfortunately, this only worked for the first
transaction in the batch, as the current decade was not reinitialized
in working-storage for subsequent transactions.  The first order
showed a ship-YY of 00 on the screen, the second 10, the third 20,
etc.

Because of the Y2k "code freeze" that has been in effect since Nov. 1,
I am not allowed to fix it until sometime in late January, when the
problem will have gone away until the next decade change.  I can only
field calls from the user, and verify that the order database is OK.
I wonder what they did 10 years ago ?  Did anyone even notice it then
?



----------------------------------------------------------------------
                  Bob Berman   -    West Hartford, CT                 
 mailto:bberman@netbox.com    website: http://www.ntplx.net/~bberman  
                                                                      
                  THE TRUE TERRORISTS IN AMERICA ARE                  
          THE PEOPLE WHO DEMAND TO SEE THE STORE MANAGER !            
----+----+----+----+----+----+----+----+----+----+----+----+----+----+
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** SkippyPB <swiegand@neo.rr.com.nospam>
- **Date:** 1999-12-19T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<64C248EB32DE1C52.9D3CADE143F53C1B.525F5B88E56B04BA@lp.airnews.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <385c3d7d.12756114@news.ntplx.net>`

```
On Sun, 19 Dec 1999 02:31:22 GMT, bberman@netbox.com (B Berman)
enlightened us:

>On Fri, 17 Dec 1999 21:03:40 -0500, "Jeff Baynard"
><union27@macconnect.com> wrote:
…[45 more quoted lines elided]…
>----+----+----+----+----+----+----+----+----+----+----+----+----+----+

It was reported on CNN today (Sunday, 12/19/1999) that the public
water company in Desmoines, Iowa sent out bills where the due date was
01/03/1900.  

The water company informed the public that there would be no problems
with the flow of water and bills were resent with the correct due
date.

Obviously, someone didn't test something!!

Regards,

          ////
         (o o)
-oOO--(_)--OOo-

I don't suffer from insanity, I enjoy every minute of it. 


Remove nospam to email me.

 Steve
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385E5A3C.213433FD@NOSPAMwebaccess.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
We had lots of programmer hours spent doing Y2K work instead of more fun
stuff.  Does that qualify as a problem?
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** "Frank Swarbrick" <infocat@sprynet.com>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83n0l6$5l2$1@nntp3.atl.mindspring.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <385E5A3C.213433FD@NOSPAMwebaccess.net>`

```
Howard Brazee <brazee@NOSPAMwebaccess.net> wrote in message
news:385E5A3C.213433FD@NOSPAMwebaccess.net...
> We had lots of programmer hours spent doing Y2K work instead of more fun
> stuff.  Does that qualify as a problem?

We had a real live Y2K problem on Friday (Dec 17).  The kicker is the
program appeared, at a glance, to be Y2K compliant.  It had date windowing
and everything!  I didn't personally work on it, but here's my
understanding...

We bill customers once a year for a certain item.  We need to notify them in
advance that they will be charged.  (20 days or so prior, I'm not sure on
the exact number.)  So a program goes through each account, checking for a
bill date.  If it's 20 days before that date it generates an entry in NACHA
format (where the day is YYMMDD).  Notices are created on the run date, and
the file itself is intended to be warehoused until the actual bill date.
Program 2 reads the warehouse file daily, and if the date of the entry is
equal to or earlier than today then that entry is sent on to the posting
programs to actually charge the customer.  Here follows some of the code:

ACCEPT CURRENT-YYMMDD FROM DATE.
IF CURRENT-YY > 90
    MOVE 19 TO CURRENT-CC
                            BILL-DATE-CC
ELSE
    MOVE 20 TO CURRENT-CC
                            BILL-DATE-CC.

* After reading a NACHA record
MOVE NACHA-DATE TO BILL-DATE-YYMMDD

IF BILL-DATE <= CURRENT-DATE
   ...write out the NACHA record to the posting file

So what's the problem?  Well, the bill date for this run is 000103
(1/3/2000).  But, because the windowing was based on the *current* date and
not the *bill* date we ended up with BILL-DATE being 19000103.

Yikes!

A simple fix to the program, of course, but we had to go and reverse all the
entries!

(Name of business removed to protect the guilty!)
```

###### ↳ ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991229001118.22112.00001844@ng-cp1.aol.com>`
- **References:** `<83n0l6$5l2$1@nntp3.atl.mindspring.net>`

```
>IF CURRENT-YY > 90
>    MOVE 19 TO CURRENT-CC
…[15 more quoted lines elided]…
>Yikes!

Just fixed the exact same problem today with data being sent to our receivables
system (well - my program had 80 instead of 90) . User paged me to say that the
batch dates were all 1900 instead of 2000 (receivables started their new fiscal
year today).  

Wonder what other programs have the same 'bug'?

Eileen (trying her dangest to be on vacation)
```

###### ↳ ↳ ↳ Re: Who has had Y2K problems yet?

_(reply depth: 4)_

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84e0r9$c9$1@news.igs.net>`
- **References:** `<83n0l6$5l2$1@nntp3.atl.mindspring.net> <19991229001118.22112.00001844@ng-cp1.aol.com>`

```
One at least.  I ran into it Friday, at three.  The customer (gotta love em)
said "hell, we'll just go home until next year", so I lucked out.

YukonMama wrote in message <19991229001118.22112.00001844@ng-cp1.aol.com>...
>>IF CURRENT-YY > 90
>>    MOVE 19 TO CURRENT-CC
…[12 more quoted lines elided]…
>>(1/3/2000).  But, because the windowing was based on the *current* date
and
>>not the *bill* date we ended up with BILL-DATE being 19000103.
>>
>>Yikes!
>
>Just fixed the exact same problem today with data being sent to our
receivables
>system (well - my program had 80 instead of 90) . User paged me to say that
the
>batch dates were all 1900 instead of 2000 (receivables started their new
fiscal
>year today).
>
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Who has had Y2K problems yet?

_(reply depth: 4)_

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 2000-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<_Tyc4.1080$FW.79213@cac1.rdr.news.psi.ca>`
- **References:** `<83n0l6$5l2$1@nntp3.atl.mindspring.net> <19991229001118.22112.00001844@ng-cp1.aol.com>`

```
If running into this problem (Y2K) in 1982 counts, then yes I had a problem.
Problem had been solved since then by downsizing the computer and it's
systems.

Just adding my two cents worth today.

Tim

YukonMama <yukonmama@aol.com> wrote in message
news:19991229001118.22112.00001844@ng-cp1.aol.com...
> >IF CURRENT-YY > 90
> >    MOVE 19 TO CURRENT-CC
…[12 more quoted lines elided]…
> >(1/3/2000).  But, because the windowing was based on the *current* date
and
> >not the *bill* date we ended up with BILL-DATE being 19000103.
> >
> >Yikes!
>
> Just fixed the exact same problem today with data being sent to our
receivables
> system (well - my program had 80 instead of 90) . User paged me to say
that the
> batch dates were all 1900 instead of 2000 (receivables started their new
fiscal
> year today).
>
…[4 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** "Jeff Baynard" <union27@macconnect.com>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83n3v70oum@enews4.newsguy.com>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <385E5A3C.213433FD@NOSPAMwebaccess.net>`

```
yes, Y2K stuff is boring.

Jeff

----------
In article <385E5A3C.213433FD@NOSPAMwebaccess.net>, Howard Brazee
<brazee@NOSPAMwebaccess.net> wrote:


> We had lots of programmer hours spent doing Y2K work instead of more fun
> stuff.  Does that qualify as a problem?
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1999-12-21T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385F7705.276A7344@worldnet.att.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <385E5A3C.213433FD@NOSPAMwebaccess.net>`

```
Howard Brazee wrote:
> 
> We had lots of programmer hours spent doing Y2K work instead of more fun
> stuff.  Does that qualify as a problem?

Only if they didn't get paid for their work, then it's a catastrophe.

Bill Lynch :-)
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<dTC74.39$9B5.5123@cac1.rdr.news.psi.ca>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
I first ran into the Y2K  problem back in 1982.  Not much was done except
that all new date fields had a full year value instead of the two digit
dates.  The existing date fields were not touched.  Too much of a hassle or
cost to fix at the time.  Famous last words repeated over and over again at
work and all over the world.

Tim

Jeff Baynard <union27@macconnect.com> wrote in message
news:83eq1m0119c@enews2.newsguy.com...
> It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half my
day
> remediating 4 production programs that were apparently 'missed',
installing
> the Standard Sliding Window.  The jobs were not canceling, but the users
> started calling about weird reports.
>
> I'm thinking that when Jan 1st rolls around, things won't crash much at
all.
> What will probably happen is a bunch of stuff gets screwed up and nobody
> will know until the users start calling.
…[4 more quoted lines elided]…
> Giant Food Inc.
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** WOB Consulting <wobconsult@my-deja.com>
- **Date:** 1999-12-20T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83kaov$789$1@nnrp1.deja.com>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
In article <83eq1m0119c@enews2.newsguy.com>,
  "Jeff Baynard" <union27@macconnect.com> wrote:
> It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half
my day
> remediating 4 production programs that were apparently 'missed',
installing
> the Standard Sliding Window.  The jobs were not canceling, but the
users
> started calling about weird reports.
>
> I'm thinking that when Jan 1st rolls around, things won't crash much
at all.
> What will probably happen is a bunch of stuff gets screwed up and
nobody
> will know until the users start calling.
>
…[4 more quoted lines elided]…
>

IMHO, the ONLY way to EVER store dates is in a Y2K-Friendly Julian-
Format. Julian-Dates handle year and century turnovers much better that
Gregorian (unless the format is CCYYMMDD). Plus, date calculations in
general as much simpler. When stored as packed-decimal, only 4-bytes
are used as opposed to their Gregorian counterpart, which requires 5-
bytes no matter how you slice it (unless you play games with the data).

Standardized Julian to Gregorian routines are plentiful. If shops that
had taken on Y2K decided to pursue and implement Julian as their
standard format, this silly idea of sliding-century windows (band-aid)
would not have to be re-visited.

However, by the time that rolls around, we'll all be dust in the wind
and someone will be bringing up the 22nd-Century date-dilemma :-)

Just my .02 cents.

Cheers,

WOB


Sent via Deja.com http://www.deja.com/
Before you buy.
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** "Judson McClendon" <judmc@bellsouth.net>
- **Date:** 1999-12-25T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8u694.14818$Dj6.172502@news2.mia>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <83kaov$789$1@nnrp1.deja.com>`

```
WOB Consulting wrote:
>
>IMHO, the ONLY way to EVER store dates is in a Y2K-Friendly Julian-
…[4 more quoted lines elided]…
>bytes no matter how you slice it (unless you play games with the data).

The only problem with this is that you display or print dates many
times more often than you calculate with them.  Most dates are never
used in calculations.  If you store dates and display dates in the
same format (ccyymmdd), you never have to convert.  Even if you
display and input dates ac MMDDCCYY, that conversion is much simpler
than to/from Julian format.  But each to his own. :-)
```

###### ↳ ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<38705475.12048880@news.gw.total-web.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <83kaov$789$1@nnrp1.deja.com> <8u694.14818$Dj6.172502@news2.mia>`

```
On Sat, 25 Dec 1999 10:42:36 -0600, "Judson McClendon"
<judmc@bellsouth.net> wrote:

>WOB Consulting wrote:
>>
…[12 more quoted lines elided]…
>than to/from Julian format.  But each to his own. :-)

Agree and besides, there's excellent conversion utilities available if
you should need Julian for some reason.
---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386f5356.11761844@news.gw.total-web.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
Well it's now Friday 31 Dec 1999 at 8:07 pm and we were supposed to
run our batch at 3, and no calls, so...

We did get a thingie where the time a transaction was entered got
shifted.  Turned out it was happening at least since February and
nobody has squawked.  Just the same the boss wanted someone to work
today to fix it.  Luckily, not my area!

On Fri, 17 Dec 1999 21:03:40 -0500, "Jeff Baynard"
<union27@macconnect.com> wrote:

>It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half my day
>remediating 4 production programs that were apparently 'missed', installing
…[10 more quoted lines elided]…
>Giant Food Inc.

---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** "Dave Cawdell" <davecawdell@home.com>
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bfdb4.23826$Fw1.109929@news1.rdc1.az.home.com>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <386f5356.11761844@news.gw.total-web.net>`

```
Just had a close call - my pager just went off!
Wrong Number - nothing wrong at American Express


"Paul Knudsen" <pknudsen@gw.total-web.net> wrote in message
news:386f5356.11761844@news.gw.total-web.net...
> Well it's now Friday 31 Dec 1999 at 8:07 pm and we were supposed to
> run our batch at 3, and no calls, so...
…[9 more quoted lines elided]…
> >It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half my
day
> >remediating 4 production programs that were apparently 'missed',
installing
> >the Standard Sliding Window.  The jobs were not canceling, but the users
> >started calling about weird reports.
> >
> >I'm thinking that when Jan 1st rolls around, things won't crash much at
all.
> >What will probably happen is a bunch of stuff gets screwed up and nobody
> >will know until the users start calling.
…[7 more quoted lines elided]…
> SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386D8184.B4ECD3F3@zip.com.au>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
Jeff Baynard wrote:
> 
> It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half my day
…[11 more quoted lines elided]…
> Giant Food Inc.

My PC just fired up with 4th Jan 1980.  I reset it to 2000 and it is
all OK now.  This box is disposable though, if it breaks it is no
great loss.

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20000101143843.22398.00000661@ng-fd1.aol.com>`
- **References:** `<386D8184.B4ECD3F3@zip.com.au>`

```
Well I've fired up my PC at home and it came up with the right date.  Signed on
to work and played with my systems.  All looks to be fine with the on-lines. 
Won't know too much more about the batch stuff until tomorrow night when they
run the first schedule of the year.

As for things out of my control <g> there were 4 water main breaks on the other
side of town (and it wasn't that cold either), there were some minor power
outages in the suburbs after the bars closed and the drunks hit the road and
power poles, and my next door neighbor is trying to figure out how to get all
the left over guests out of her livingroom :)

Happy New Year all :)
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** "Terry Heinze" <terryheinze@prodigy.net>
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84lrkn$3nu6$1@newssvr04-int.news.prodigy.com>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <386D8184.B4ECD3F3@zip.com.au>`

```

> My PC just fired up with 4th Jan 1980.  I reset it to 2000 and it is
> all OK now.  This box is disposable though, if it breaks it is no
…[4 more quoted lines elided]…
> http://www.zipworld.com.au/~waratah/
My old (W3.1) PC did the same (1/4/80).  The new one (W98) did okay though.
```

##### ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386EBB68.3FE17F74@home.com>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <386D8184.B4ECD3F3@zip.com.au>`

```


Ken Foskey wrote:
> 
> Jeff Baynard wrote:
…[18 more quoted lines elided]…
>
Phew ! You had me worried for a second. Hadn't bothered to look,
(there's faith for you). While reading your message I just took a gander
at the Windows clock and all is honky dory.

Jimmy

PS: TV coverage of Y2K - Best :- impromptu dancing to the Blue Danube
waltz in Vienna - Lousy :- firstly an Abbo playing on a long pipe, (that
was OK), then some artsy-fartsy art director got in on the act and we
had what, non-asians, non-polynesians, God knows what they were,
squirming around in red earth. If you've got one of the artsy-fartsy
types lined-up for the Games - fire the SOB before they happen !
```

###### ↳ ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<oGSb4.359$jG2.5263@nnrp1.rcsntx.swbell.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <386D8184.B4ECD3F3@zip.com.au> <386EBB68.3FE17F74@home.com>`

```

James J. Gavan <jjgavan@home.com> wrote in message
news:386EBB68.3FE17F74@home.com...
>
> PS: TV coverage of Y2K - Best :- impromptu dancing to the Blue
Danube
> waltz in Vienna - Lousy :- firstly an Abbo playing on a long pipe,
(that
> was OK), then some artsy-fartsy art director got in on the act and
we
> had what, non-asians, non-polynesians, God knows what they were,
> squirming around in red earth. If you've got one of the artsy-fartsy
> types lined-up for the Games - fire the SOB before they happen !

Some worthy said "All cultures are NOT equal! There is a fundamental
difference in being able to put a man on the moon and being able
to put a bone in your nose."
```

###### ↳ ↳ ↳ Re: Who has had Y2K problems yet?

_(reply depth: 4)_

- **From:** Howard Brazee <brazee@NOSPAMwebaccess.net>
- **Date:** 2000-01-04T00:00:00
- **Newsgroups:** comp.lang.cobol,bit.listserv.idms-1
- **Message-ID:** `<38720373.B230C41C@NOSPAMwebaccess.net>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <386D8184.B4ECD3F3@zip.com.au> <386EBB68.3FE17F74@home.com> <oGSb4.359$jG2.5263@nnrp1.rcsntx.swbell.net>`

```
I had a problem, but it wasn't COBOL, but was ADS/O.

Three dialogs had weirdly formatted dates.  We were lucky to find one,
as it was a delete transaction for the first - only by looking at the
data after performing the transaction did we see a delete date which was
messed up.  

I picked the first program:
I checked the code and could not find a problem, and then decided to
generate (compile) the code with an option to allow me to use a
debugger.  It worked fine.  So I generated it without that option, it
worked fine.  I migrated all three to production, they failed.  I had
the DBA generate the dialogs in production and they worked fine.
```

###### ↳ ↳ ↳ Re: Who has had Y2K problems yet?

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2000-01-03T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<duj07ss49ui73fqmon7toau9a24smq5i7r@4ax.com>`
- **References:** `<83eq1m0119c@enews2.newsguy.com> <386D8184.B4ECD3F3@zip.com.au> <386EBB68.3FE17F74@home.com>`

```
"James J. Gavan" <jjgavan@home.com> wrote:

>
>
…[24 more quoted lines elided]…
>at the Windows clock and all is honky dory.

strangely enough, my windows clock crashed today for the first time. i
had just installed a new graphics driver, and i believe resources were
running low, but i guess it had to happen sometimes (the odds are
megabytes to the clocks app size of <64k)


using alternate news server source.
reply to email gvwmoore@spam.ix.netcom.com remove the spam
```

#### ↳ Re: Who has had Y2K problems yet?

- **From:** shine98@my-deja.com
- **Date:** 2000-01-02T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84mhg6$2u$1@nnrp1.deja.com>`
- **References:** `<83eq1m0119c@enews2.newsguy.com>`

```
I went into ACE Hardware and the display on the cash register led's read
1/1/1900. but the receipt was correct.

In article <83eq1m0119c@enews2.newsguy.com>,
  "Jeff Baynard" <union27@macconnect.com> wrote:
> It's Friday 12/17/99 (or is that 12/17/1999?) and today I spent half
my day
> remediating 4 production programs that were apparently 'missed',
installing
> the Standard Sliding Window.  The jobs were not canceling, but the
users
> started calling about weird reports.
>
> I'm thinking that when Jan 1st rolls around, things won't crash much
at all.
> What will probably happen is a bunch of stuff gets screwed up and
nobody
> will know until the users start calling.
>
…[4 more quoted lines elided]…
>


Sent via Deja.com http://www.deja.com/
Before you buy.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
