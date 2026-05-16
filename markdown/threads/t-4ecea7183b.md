[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# [OT] Mainframe Software Prices?

_8 messages · 5 participants · 2001-02_

**Topics:** [`Mainframe, z/OS, JCL, CICS`](../topics.md#mainframe)

---

### [OT] Mainframe Software Prices?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-02-21T19:13:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net>`

```

So here's the deal... my present client is a goodly-sized shop, multiple
regions, CICS/DB2, 24/7 uptime requirements (that are almost met, at
times!)... but no FileAid for DB2.  I made a bit of conversation with one
of the Systems Guys and there would be two immediate responses:

1) Is there a Business Justification for it?

(this is answered by 'as much of one as there is for the regular FileAid
you got... it'd cut down on folks coding SPUFIs, too!')

2) How Much?

... and that's where my knowledge ends.  I am sure that if someone
broached the subject with the site's CA rep the response would be
(number)... and then, of course, the comeback would be 'Come *on*, we
already lease the sun and the stars from you guys... you can do us this
little asteroid for closer to (smaller number).'

... and so my question: any ideas what (number) and (smaller number) might
be?

Thanks much!

DD
```

#### ↳ Re: [OT] PC DB2 Prices - WAS :Mainframe Software Prices?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-02-22T01:43:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A94709F.46573D3A@home.com>`
- **References:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net>`

```


NA wrote:

> So here's the deal... my present client is a goodly-sized shop, multiple
> regions, CICS/DB2, 24/7 uptime requirements  <snip>

> ... and so my question: any ideas what (number) and (smaller number) might
> be?
…[3 more quoted lines elided]…
> DD

Kinda glad you asked that question, 'cos I'm considering another possibility.
Maybe, (still maybe at the moment), I might just switch from COBOL flat files
on a PC to DB2.

So not wishing to divert from the Doc's question - PC-wise any pitfalls,
what's it going to cost me to have DB2, (used with Net Express) and what would
it cost my end-user.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: [OT] PC DB2 Prices - WAS :Mainframe Software Prices?

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-02-22T02:50:38+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<28%k6.209572$KP3.51673263@news3.rdc1.on.home.com>`
- **References:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net> <3A94709F.46573D3A@home.com>`

```
The last time I checked IBM UDB was available in a number of packages with
different pricing options. Your best bet is to visit their website to check
out the combinations then call IBM Direct to inquire about pricing.

If you choose Microsoft SQL Server then there's a package called Microsoft
Data Engine (MSDE) which is the equivalent of a free sample. It'll support 5
users and is available for distribution with some restrictions. I think you
require a licensed copy of a development product like VB. The idea is you
can distribute a 'lite' version of your product and Microsoft makes
additional money selling SQL Server when your clients scale up.

The database can do a lot of the work for you so you'll save some
maintenance effort in the long run because you can carve out tons of file
navigation code. You'll also get improved ad-hoc query capabilities and
direct support for MS Office products like Excel and Access with no effort
on your part.

Your third option is the Microsoft Jet database. It'll theoretically support
255 users although the practical limit is more like 20. It's highly biased
toward Visual Basic and the SQL datatypes are very non-standard but it too
is available for distribution.

The pitfalls are you need to become familiar with configuration and
maintenance issues for the database product. As well, you've added another
vendor to your mix of dependent products.


- Karl

"James J. Gavan" <jjgavan@home.com> wrote in message
news:3A94709F.46573D3A@home.com...
>
>
…[5 more quoted lines elided]…
> > ... and so my question: any ideas what (number) and (smaller number)
might
> > be?
> >
…[4 more quoted lines elided]…
> Kinda glad you asked that question, 'cos I'm considering another
possibility.
> Maybe, (still maybe at the moment), I might just switch from COBOL flat
files
> on a PC to DB2.
>
> So not wishing to divert from the Doc's question - PC-wise any pitfalls,
> what's it going to cost me to have DB2, (used with Net Express) and what
would
> it cost my end-user.
>
> Jimmy, Calgary AB
>
```

###### ↳ ↳ ↳ Re: [OT] PC DB2 Prices - WAS :Mainframe Software Prices?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-02-22T03:19:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A948728.C104C5EF@home.com>`
- **References:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net> <3A94709F.46573D3A@home.com> <28%k6.209572$KP3.51673263@news3.rdc1.on.home.com>`

```


"Oscar T. Grouch" wrote:

> The last time I checked IBM UDB was available in a number of packages with
> different pricing options. Your best bet is to visit their website to check
> out the combinations then call IBM Direct to inquire about pricing. <snip>

Thanks Karl, succinct as usual.

Jimmy
```

##### ↳ ↳ Re: [OT] PC DB2 Prices - WAS :Mainframe Software Prices?

- **From:** Paul Raulerson <praul@isot.com>
- **Date:** 2001-02-23T22:17:23-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<v9de9tgj74v6ogk4l60b1an0rtpu1tbn7e@4ax.com>`
- **References:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net> <3A94709F.46573D3A@home.com>`

```
Well, last time I looked, your development cost with DB/2 (exclusive
of any compilers you choose to use) is less than $200. For a Workgroup
Server, DB/2 is highly competitive, falling in there at something like
$699 before any discounts. 

DB/2 does get more expensive if you move up to multi platform 
enterprise wide servers, but if you are talking oh - 100 people on a 
server per location, DB/2 can't be beat. :) 

You also have some really nice options given eh Web with DB/2.

-Paul


On Thu, 22 Feb 2001 01:43:46 GMT, "James J. Gavan" <jjgavan@home.com>
wrote:

>
>
…[20 more quoted lines elided]…
>Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: [OT] PC DB2 Prices - WAS :Mainframe Software Prices?

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-02-24T19:50:32+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3A981262.957B0471@home.com>`
- **References:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net> <3A94709F.46573D3A@home.com> <v9de9tgj74v6ogk4l60b1an0rtpu1tbn7e@4ax.com>`

```
Thanks Paul -  Jimmy

Paul Raulerson wrote:

> Well, last time I looked, your development cost with DB/2 (exclusive
> of any compilers you choose to use) is less than $200. For a Workgroup
> Server, DB/2 is highly competitive, falling in there at something like
> $699 before any discounts <snip>
```

#### ↳ Re: [OT] Mainframe Software Prices?

- **From:** yukonmama@aol.com (YukonMama)
- **Date:** 2001-02-22T03:32:39+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010221223239.02281.00000209@ng-cn1.aol.com>`
- **References:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net>`

```
Sounds like the shop I'm in right now.  I believe we just installed FileAid for
DB2 so I'll ask around tomorrow and get back to you.
```

##### ↳ ↳ Re: [OT] Mainframe Software Prices?

- **From:** docdwarf@clark.net ( NA)
- **Date:** 2001-02-22T10:42:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<u26l6.18561$Sl.801229@iad-read.news.verio.net>`
- **References:** `<erUk6.18463$Sl.797118@iad-read.news.verio.net> <20010221223239.02281.00000209@ng-cn1.aol.com>`

```
In article <20010221223239.02281.00000209@ng-cn1.aol.com>,
YukonMama <yukonmama@aol.com> wrote:
>Sounds like the shop I'm in right now.  I believe we just installed FileAid for
>DB2 so I'll ask around tomorrow and get back to you.

Greatly appreciated, old girl... standing by.

DD
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
