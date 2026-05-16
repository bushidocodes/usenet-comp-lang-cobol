[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Y2K

_18 messages · 13 participants · 1999-12 → 2000-01_

**Topics:** [`Y2K and Year-2000 remediation`](../topics.md#y2k)

---

### Y2K

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-16T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83b3av$mdd$1@news.igs.net>`

```
Well, I just sent out a last batch of CD's (a screen defaulting to the wrong
century), and a letter to each and every user reminding them to review
backup/restore procedures next week, and to be sure to do at least two
backups between Christmas and New Years.

I took our largest customer, closed December (to-date), redated Novembers
transactions, and set up a machine with January's date, then did a full
months run on all systems. Everything balanced.  All ageing was correct.

I think we are as ready as we can get.  Any last minute
ideas/precautions/caveats that anyone can think of?
```

#### ↳ Re: Y2K

- **From:** "Ib Tanding" <ib@tanding.dk>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83bsrd$4de$1@news.inet.tele.dk>`
- **References:** `<83b3av$mdd$1@news.igs.net>`

```
Congratulations!
Last minute checks:

February (29th),
External data (Crazy date-formats, validations etc.)
Links to other systems (ole,odbc,dde)

Hopefully not.
Regards
Ib
donald tees skrev i meddelelsen <83b3av$mdd$1@news.igs.net>...
>Well, I just sent out a last batch of CD's (a screen defaulting to the
wrong
>century), and a letter to each and every user reminding them to review
>backup/restore procedures next week, and to be sure to do at least two
…[10 more quoted lines elided]…
>
```

##### ↳ ↳ Re: Y2K

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83dc4g$f4$1@news.igs.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <83bsrd$4de$1@news.inet.tele.dk>`

```
Yes the 29th is worth a note of warning to people.

Ib Tanding wrote in message <83bsrd$4de$1@news.inet.tele.dk>...
>Congratulations!
>Last minute checks:
…[25 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Y2K

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<83dkk9$pe0$1@nntp4.atl.mindspring.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <83bsrd$4de$1@news.inet.tele.dk> <83dc4g$f4$1@news.igs.net>`

```

donald tees <donald@willmack.com> wrote in message
news:83dc4g$f4$1@news.igs.net...
> Yes the 29th is worth a note of warning to people.
>

And by extension the 366th day of the year.  (When everyone will once again
be saying "This time we can celebrate the REAL change of Millennium - and no
computer problem to worry about - but forgetting that the START of Dec 31,
2000 may find some YYDDD problems.)
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 4)_

- **From:** "MStiles" <mstiles@dialnet.net>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Edw64.453$XC1.79630@news1.primary.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <83bsrd$4de$1@news.inet.tele.dk> <83dc4g$f4$1@news.igs.net> <83dkk9$pe0$1@nntp4.atl.mindspring.net>`

```
Sure, but that's over a year from now so why worry :)

>And by extension the 366th day of the year.  (When everyone will once again
>be saying "This time we can celebrate the REAL change of Millennium - and
no
>computer problem to worry about - but forgetting that the START of Dec 31,
>2000 may find some YYDDD problems.)
…[6 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 5)_

- **From:** petwir@saif.com (Pete Wirfs)
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<MPG.12c43423c653d3198968c@news.transport.com>`
- **References:** `<83b3av$mdd$1@news.igs.net> <83bsrd$4de$1@news.inet.tele.dk> <83dc4g$f4$1@news.igs.net> <83dkk9$pe0$1@nntp4.atl.mindspring.net> <Edw64.453$XC1.79630@news1.primary.net>`

```
In article <Edw64.453$XC1.79630@news1.primary.net>, mstiles@dialnet.net 
says...
> Sure, but that's over a year from now so why worry :)
> 
…[14 more quoted lines elided]…
> 

Because your computer systems may need to store 12/31/2000 long before we 
get there.

We ran into the 02/29/2000 problem quite some time ago when storing 
expiration dates for insurance policies, and that date is still a long 
way off too.

Pete
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 6)_

- **From:** "MStiles" <mstiles@dialnet.net>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JGx64.456$XC1.80701@news1.primary.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <83bsrd$4de$1@news.inet.tele.dk> <83dc4g$f4$1@news.igs.net> <83dkk9$pe0$1@nntp4.atl.mindspring.net> <Edw64.453$XC1.79630@news1.primary.net> <MPG.12c43423c653d3198968c@news.transport.com>`

```
Pete,
    Of course your right, I was just kinda kidding.


>Because your computer systems may need to store 12/31/2000 long before we
>get there.
…[5 more quoted lines elided]…
>Pete
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 5)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1999-12-18T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<385B5618.E1540281@worldnet.att.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <83bsrd$4de$1@news.inet.tele.dk> <83dc4g$f4$1@news.igs.net> <83dkk9$pe0$1@nntp4.atl.mindspring.net> <Edw64.453$XC1.79630@news1.primary.net>`

```
MStiles wrote:
> 
> Sure, but that's over a year from now so why worry :)

Right, most of the "legacy" software will have been replaced by then.

Bill Lynch :-)
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 6)_

- **From:** stevenln@aol.comnospam (Steve Newton)
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991222014540.23435.00001245@ng-fx1.aol.com>`
- **References:** `<385B5618.E1540281@worldnet.att.net>`

```
>Right, most of the "legacy" software will have been replaced by then.
>
>Bill Lynch :-)

Isn't that how we got into this mess?? ::))
Asimov, Heinlein, and Zappa
Still the best
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 7)_

- **From:** Bill Lynch <wblynch@worldnet.att.net>
- **Date:** 1999-12-22T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3860D666.EBF2C85B@worldnet.att.net>`
- **References:** `<385B5618.E1540281@worldnet.att.net> <19991222014540.23435.00001245@ng-fx1.aol.com>`

```
Steve Newton wrote:
> 
> >Right, most of the "legacy" software will have been replaced by then.
…[3 more quoted lines elided]…
> Isn't that how we got into this mess?? ::))

Indeed, that's why I stuck the smiley after my name.

> Asimov, Heinlein, and Zappa
> Still the best

No argument.

Bill Lynch
```

###### ↳ ↳ ↳ Re: Y2K

_(reply depth: 4)_

- **From:** "Tim Hillock" <hillock@istar.ca>
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a4z64.1310$0M4.56354@cac1.rdr.news.psi.ca>`
- **References:** `<83b3av$mdd$1@news.igs.net> <83bsrd$4de$1@news.inet.tele.dk> <83dc4g$f4$1@news.igs.net> <83dkk9$pe0$1@nntp4.atl.mindspring.net>`

```
William M. Klein <wmklein@nospam.netcom.com> wrote in message
news:83dkk9$pe0$1@nntp4.atl.mindspring.net...
>
> donald tees <donald@willmack.com> wrote in message
…[4 more quoted lines elided]…
> And by extension the 366th day of the year.  (When everyone will once
again
> be saying "This time we can celebrate the REAL change of Millennium - and
no
> computer problem to worry about - but forgetting that the START of Dec 31,
> 2000 may find some YYDDD problems.)
…[5 more quoted lines elided]…
>

 And the 20th Century ends on December 31, 2000 as well.

People just still don't understand this new math (which has been going on
for about 30-40 years).

That Last Y2K problem is that a century that ends in 00 and divides evenly
by 400 is considered a leap year, thus 366 days in a year.  1900 was not a
leap year.
```

#### ↳ Re: Y2K

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 1999-12-17T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3859bb7b.191547172@news1.attglobal.net>`
- **References:** `<83b3av$mdd$1@news.igs.net>`

```
The system I wrote for my friends Bowling center has been compliant
from the beginning.  I always used 4 digit dates (Written initially in
1991).  However, I am concerned about the current date on the machines
getting off, so I will be sending him a patch that checks for a year <
90 and > 80 - screamin if it finds one.  I'm putting it in the main
menu.

On Thu, 16 Dec 1999 11:26:34 -0500, "donald tees"
<donald@willmack.com> wrote:

>Well, I just sent out a last batch of CD's (a screen defaulting to the wrong
>century), and a letter to each and every user reminding them to review
…[11 more quoted lines elided]…
>

---
Try a better search engine:  http://www.google.com
My personal web site: http://www.geocities.com/Eureka/2006/
```

#### ↳ Re: Y2K

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<19991229002213.22112.00001849@ng-cp1.aol.com>`
- **References:** `<83b3av$mdd$1@news.igs.net>`

```
>From: "donald tees" donald@willmack.com 
>Date: Thu, 16 December 1999 11:26 AM EST

>I think we are as ready as we can get.  Any last minute
>ideas/precautions/caveats that anyone can think of?
>

You got batteries? bubbly? asprin? antacids? prozac? last will and testament
updated? 

Eileen (who intends to be off the streets when the shooting starts)
```

##### ↳ ↳ Re: Y2K

- **From:** "donald tees" <donald@willmack.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<84e0ss$ku$1@news.igs.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <19991229002213.22112.00001849@ng-cp1.aol.com>`

```
How about a great big hole in the ground, and a good staff?
<G>

YukonMama wrote in message <19991229002213.22112.00001849@ng-cp1.aol.com>...
>>From: "donald tees" donald@willmack.com
>>Date: Thu, 16 December 1999 11:26 AM EST
…[5 more quoted lines elided]…
>You got batteries? bubbly? asprin? antacids? prozac? last will and
testament
>updated?
>
>Eileen (who intends to be off the streets when the shooting starts)
```

##### ↳ ↳ Re: Y2K

- **From:** "Jerry P" <bismail@bisusa.com>
- **Date:** 1999-12-29T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8wya4.248$_j1.4802@nnrp3.rcsntx.swbell.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <19991229002213.22112.00001849@ng-cp1.aol.com>`

```
1. Note what your neighbors are hoarding.
2. Stock up on ammunition.

YukonMama <yukonmama@aol.com> wrote in message
news:19991229002213.22112.00001849@ng-cp1.aol.com...
> >From: "donald tees" donald@willmack.com
> >Date: Thu, 16 December 1999 11:26 AM EST
…[5 more quoted lines elided]…
> You got batteries? bubbly? asprin? antacids? prozac? last will and
testament
> updated?
>
> Eileen (who intends to be off the streets when the shooting starts)
```

###### ↳ ↳ ↳ Re: Y2K

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386e5031.10957295@news.gw.total-web.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <19991229002213.22112.00001849@ng-cp1.aol.com> <8wya4.248$_j1.4802@nnrp3.rcsntx.swbell.net>`

```
Why aren't you out in the woods with the rest of the nut-rolls?

On Wed, 29 Dec 1999 19:25:24 -0600, "Jerry P" <bismail@bisusa.com>
wrote:

>1. Note what your neighbors are hoarding.
>2. Stock up on ammunition.
>
>
---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

##### ↳ ↳ Re: Y2K

- **From:** Ken Foskey <waratah@zip.com.au>
- **Date:** 1999-12-30T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386A95FD.A3AED265@zip.com.au>`
- **References:** `<83b3av$mdd$1@news.igs.net> <19991229002213.22112.00001849@ng-cp1.aol.com>`

```
YukonMama wrote:
> 
> >From: "donald tees" donald@willmack.com
…[9 more quoted lines elided]…
> Eileen (who intends to be off the streets when the shooting starts)

You forgot a car that does not have a computer chip in it.  Everyone
knows that all cars will stop working on the change of the century :-}

Thanks
Ken Foskey
http://www.zipworld.com.au/~waratah/
```

##### ↳ ↳ Re: Y2K

- **From:** pknudsen@gw.total-web.net (Paul Knudsen)
- **Date:** 2000-01-01T00:00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<386d4e9a.10550215@news.gw.total-web.net>`
- **References:** `<83b3av$mdd$1@news.igs.net> <19991229002213.22112.00001849@ng-cp1.aol.com>`

```
On 29 Dec 1999 05:22:13 GMT, yukonmama@aol.com (YukonMama) wrote:



>You got batteries? bubbly? asprin? antacids? prozac? last will and testament
>updated? 

Nope. Nope.  I think somewhere.  Does Pepto count?  Nope.  Nope.

>Eileen (who intends to be off the streets when the shooting starts)

Good.  Less traffic to worry about when we come home from the club.
---------------------------------------------------------------
SuSE Linux Users meet at: http://clubs.yahoo.com/clubs/suselinuxusers
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
