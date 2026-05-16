[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# CoBOL moved to OO

_259 messages · 25 participants · 2003-12 → 2004-01_

**Topics:** [`Object-oriented COBOL`](../topics.md#oo)

---

### CoBOL moved to OO

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-18T14:47:19+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<brseln$6t5$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca>`

```
We have a lot of PeopleSoft software in our shop.   I'm told that their move to
OO is by encapsulating much of their existing CoBOL code and using tags and such
to call it in an OO setup.

How common is this with big mainframe applications?
```

#### ↳ Re: CoBOL moved to OO

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-18T15:32:16+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000369.019ccad7@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu>`

```
Howard,

> How common is this with big mainframe applications?

It's commonly proposed as a solution, but this is the first time I've 
heard that it can be made to work.

Since the latest major upgrade, Cobol has OO constructs which I've 
looked at and seem OK, but I've had no personal involvement.

Non-I/O routines can be objectified fairly easily, but since Cobol is 
all about I/O, I can't imagine genuine legacy code written for serial 
files and converted to simple databases can easily be objectified.

And anyway, the managers who want to do this want shiny new systems.

I've been involved with a team investigating automatic objectifying, 
but I can certainly offer one observation: my business users were 
nonplussed - they have a working system, and we wanted to spend 
millions of pounds with /no/ change in behaviour! Where's the business 
benefit in that?

---

Doug

dwscott@ieee.org
```

##### ↳ ↳ Re: CoBOL moved to OO

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-22T16:19:11+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bs75hv$hm1$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org>`

```

On 18-Dec-2003, Doug Scott <dwscott@ieee.org> wrote:

> 've been involved with a team investigating automatic objectifying,
> but I can certainly offer one observation: my business users were
> nonplussed - they have a working system, and we wanted to spend
> millions of pounds with /no/ change in behaviour! Where's the business
> benefit in that?

The business advantage to PeopleSoft may be primarily in marketing.   They sell
a "state-of-the-art OO system", but still keep their valuable business code
developed over years.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-22T17:02:09+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<22b3dcd54cff07a52f959b3cd483727d@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
> Doug Scott <dwscott@ieee.org> wrote:
> >
…[8 more quoted lines elided]…
> developed over years.

In other words, their customers get to pay through the nose for no benefit
to the customer. Typical OO 'benefit', I see this every day. Our industry
seems to have forgotten the concept of ROI.

I view the procedural vs. OO issue as closely analogous to the issue of
iterative vs. recursive logic. Iterative logic (procedural) is better for the
vast number of applications, in clarity, simplicity and efficiency. But there
is a small class of tasks where recursive (OO) logic is simpler and clearer.
But recursive (OO) is never more efficient than iterative (procedural),
except in programmer time in those cases where it is simpler and clearer.
IMHO, going exclusively OO is closely comparable to using recursive
logic for every loop situation.  I.e. It's nuts.  It costs a fortune to implement,
and makes programming, debugging and maintenance far more complex,
costly and time consuming, and the result is less reliable. Pretty much
what we see today in OO, with a 45%+ failure rate in implementing new
systems. :-)

Don't worry, I have my asbestos pants on. ;-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 4)_

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2003-12-22T17:53:40+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<EcGFb.121015$ea%.20283@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com>`

```
I think OO vs procedural is something like packaging vs wrapping.

With packaging, using standard class pattern, it is possible to know the
content with opening it.

With wrapping, you can use anything to wrap up the same stuff in any way you
like, but it is not easy to know the content without opening it/breaking it.
And another problem is to put your wrap into another container.

For standard packaging, there are special designed trailers, car... They
need investment at the beginning for long time saving.


"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:22b3dcd54cff07a52f959b3cd483727d@news.teranews.com...
> "Howard Brazee" <howard@brazee.net> wrote:
> > Doug Scott <dwscott@ieee.org> wrote:
…[7 more quoted lines elided]…
> > The business advantage to PeopleSoft may be primarily in marketing.
They
> > sell a "state-of-the-art OO system", but still keep their valuable
business code
> > developed over years.
>
…[5 more quoted lines elided]…
> iterative vs. recursive logic. Iterative logic (procedural) is better for
the
> vast number of applications, in clarity, simplicity and efficiency. But
there
> is a small class of tasks where recursive (OO) logic is simpler and
clearer.
> But recursive (OO) is never more efficient than iterative (procedural),
> except in programmer time in those cases where it is simpler and clearer.
> IMHO, going exclusively OO is closely comparable to using recursive
> logic for every loop situation.  I.e. It's nuts.  It costs a fortune to
implement,
> and makes programming, debugging and maintenance far more complex,
> costly and time consuming, and the result is less reliable. Pretty much
…[10 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 4)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-22T13:30:48-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<QNGFb.3949$d%1.866120@news20.bellglobal.com>`
- **In-Reply-To:** `<22b3dcd54cff07a52f959b3cd483727d@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com>`

```
Judson McClendon wrote:
> "Howard Brazee" <howard@brazee.net> wrote:
> 
…[30 more quoted lines elided]…
> Don't worry, I have my asbestos pants on. ;-)

I think you are right that there may be little benefit to attempting 
retrofit, but in terms of architecture OOP (Cobol OOP that is) is a much 
more logical structure for maintainence.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-22T19:59:15+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<a51378743c9a3a120a2b2c888e9ca502@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <QNGFb.3949$d%1.866120@news20.bellglobal.com>`

```
"Donald Tees" <donald_tees@nospam.sympatico.ca> wrote:
> Judson McClendon wrote:
> > I view the procedural vs. OO issue as closely analogous to the issue of
…[14 more quoted lines elided]…
> more logical structure for maintainence.


No kidding. If you only implement a bit more than half the applications
you try to implement, that is going do wonders for reducing maintenance. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-22T15:48:56-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<jPIFb.4317$d%1.930897@news20.bellglobal.com>`
- **In-Reply-To:** `<a51378743c9a3a120a2b2c888e9ca502@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <QNGFb.3949$d%1.866120@news20.bellglobal.com> <a51378743c9a3a120a2b2c888e9ca502@news.teranews.com>`

```
Judson McClendon wrote:
> "Donald Tees" <donald_tees@nospam.sympatico.ca> wrote:
> 
…[12 more quoted lines elided]…
> you try to implement, that is going do wonders for reducing maintenance. :-)

New Cobol systems have a 50% failure rate when OOP methodology is used? 
  May I have a cite of that?

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-23T17:02:56+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<55542762013017c91efb47281855d090@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <QNGFb.3949$d%1.866120@news20.bellglobal.com> <a51378743c9a3a120a2b2c888e9ca502@news.teranews.com> <jPIFb.4317$d%1.930897@news20.bellglobal.com>`

```
"Donald Tees" <donald_tees@nospam.sympatico.ca> wrote:
> Judson McClendon wrote:
> > "Donald Tees" <donald_tees@nospam.sympatico.ca> wrote:
…[16 more quoted lines elided]…
>   May I have a cite of that?


Valid point, Donald. I have seen it a number of times over several years,
but I will attempt to pin down some specifics and post them. However,
one source I happened to have at hand is an article titled "Pulling the
Plug" on the front page of the Wall Street Journal, Thursday, April 30,
1998. That article quotes a 1996 survey by Standish Group International,
Inc., and states a 42% failure rate. More recent figures I have seen are
around 45% or so. I will try to find and post some.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-22T21:30:32+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000037b.02f6b119@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <QNGFb.3949$d%1.866120@news20.bellglobal.com> <a51378743c9a3a120a2b2c888e9ca502@news.teranews.com>`

```
Judson,

> No kidding. If you only implement a bit more than half the applications
> you try to implement, that is going do wonders for reducing maintenance. :-)

Assertion alert!

Facts omitted.


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-24T19:16:24+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bscom7$gut$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <QNGFb.3949$d%1.866120@news20.bellglobal.com>`

```

On 22-Dec-2003, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:

> I think you are right that there may be little benefit to attempting
> retrofit, but in terms of architecture OOP (Cobol OOP that is) is a much
> more logical structure for maintenance.

It could be.   But an interdependent structure requires a more logical
structure.   The more independence a program has, the less likely a mistake or
change will effect other applications.

For some uses, maintenance likes it if you make one simple change that is reused
everywhere.

But for other uses, rigorous testing and "don't touch my program" makes
maintenance harder.   Every time you stick in a change with exceptions (keep
program A running the old way), this interdependence does not make maintenance
easier.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 4)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-22T20:30:06+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000375.02bf5c97@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com>`

```
Judson,

> Don't worry, I have my asbestos pants on. ;-)
>
No need. I'm continually amazed that OO, which relies of side-effects, 
can be conceived as a solution to a large system problem.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-22T15:49:34-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VPIFb.4318$d%1.931294@news20.bellglobal.com>`
- **In-Reply-To:** `<VA.00000375.02bf5c97@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org>`

```
Doug Scott wrote:
> Judson,
> 
…[13 more quoted lines elided]…
> 

Absolute nonsense.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-23T11:08:43+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3fe76bd1_6@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com>`

```

"Donald Tees" <donald_tees@nospam.sympatico.ca> wrote in message
news:VPIFb.4318$d%1.931294@news20.bellglobal.com...
> Doug Scott wrote:
> > Judson,
…[17 more quoted lines elided]…
>
Yes Don, it is.

But you are arguing with people who have no idea what they're talking about,
have never been involved in successful OO implementation, do not understand
the basic fundamentals, (witness Judson's post equating "iterative" to
"procedural"), and are resisting to the last ditch anything that looks like
it might threaten their comfortable little world, predicated on "What we
know", "What we have always done", and "Best practice (as we perceive
it)...".

Those of us who have taken the trouble to understand OO, realise what a
powerful tool it is. Those of us who have gone further and realised that OO
components can be wrapped and re-used in a way that called modules never
could, are unlikely to ever return to the "Procedural COBOL" fold (except,
maybe, for Batch Processing...).

For my own part, I'm tired of arguing it. I don't really care whether people
use OO or not.

I care about young people losing their COBOL jobs to Java programmers, and
that is one reason I strongly advocate them learning OO (even Java...). But
for the dyed-in-the-wool Fortress COBOLlers, I reckon they'll get what they
deserve. It is just a matter of time...

I remember similar resistance to Djykstra's paper when it was first
published..."What?! The whole of computer programming can be resolved down
to THREE operations?!!! Rubbish!!".

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-23T08:08:49-06:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<zOadnUYWTYrx0XWi4p2dnA@giganews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
>
> I remember similar resistance to Djykstra's paper when it was first
> published..."What?! The whole of computer programming can be resolved
> down to THREE operations?!!! Rubbish!!".

Get, Mull, Put?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2003-12-23T15:20:46+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<i3ZFb.14380$aw2.8116612@newssrv26.news.prodigy.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <zOadnUYWTYrx0XWi4p2dnA@giganews.com>`

```
> Peter E.C. Dashwood wrote:
 >
…[3 more quoted lines elided]…
>

I had always heard that as four (4) operations:

Add
Compare
Store
Jump

MCM
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-24T11:48:15+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3fe8c692_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <zOadnUYWTYrx0XWi4p2dnA@giganews.com>`

```

"JerryMouse" <nospam@bisusa.com> wrote in message
news:zOadnUYWTYrx0XWi4p2dnA@giganews.com...
> Peter E.C. Dashwood wrote:
> >
…[5 more quoted lines elided]…
>
That too...<G>

It was SEQUENCE
          SELECT
          ITERATE

just for the record...

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-23T17:24:28+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b15f52de7cc255400373dfa35846ecab@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> But you are arguing with people who have no idea what they're talking about,
…[5 more quoted lines elided]…
> it)...".

You cannot be referring to me, because I have a completely different
set of reasons for objecting to an "OO and nothing else" mentality. I
have said before, and I reiterate, simply show me some statistical data
that show an *across the board* improvement in development time,
development costs, maintenance costs and training costs, and I will be
happy to endorse an *across the board* move to OO. Without that, you
argue simply from personal opinion, as you accuse others of doing.
Within 10 years after structured techniques were in use, I could have
buried you under tons of such statistics in support of structured
techniques. Structured techniques were clearly and decisively superior
to previous techniques in every measurable way, except possibly in
total lines of code. In fact, contrary to the trend we discuss, significant
such data was available BEFORE the push toward structured. Now,
after much longer trials, I have yet to see any such objective data to
confirm a wholesale move toward OO. Perhaps I've been overlooking
it, so kindly point me to it. :-)

Please note that none of the above involves "understanding the basic
concepts", "resisting to the last ditch", threatening any "comfortable
little world", or any "supposed knowledge". If OO is as good as you
say, then fine, show me the statistical data to back it up, based on
data obtained from real world projects. Considering the truly vast
expenditures in money and manpower that have been invested in a
wholesale move toward OO, everyone should be constantly tripping
over such data, because investing that kind of resources in anything
less than clearly demonstrably superior is, as I have been saying,
nuts. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Gary" <IDontThink@so.com.so>
- **Date:** 2003-12-23T23:51:23+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<%x4Gb.463547$275.1354316@attbi_s53>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote:

<snip>

Good post Judson.

Don't expect consistency though. (Most) Everyone has their own piece of
"enlightenment" that appears to contradict themselves. Difficult to digest
though when it's so judgmental.

Gary.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-24T12:14:36+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53>`

```
"Gary" <IDontThink@so.com.so> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
>
…[6 more quoted lines elided]…
> though when it's so judgmental.

Thank you, Gary. I apologize if I am being 'judgmental', I don't mean to be.
I agree I am being blunt but, for better or worse, it seems to be a part of
my personality. I do have very strong opinions and a high emotional stake
in these issues, for what I believe to be very good reasons, that I will try
to explain below. I hope this helps those of you who strongly disagree
with me to at lease understand where I'm coming from. :-)

It may seem that I am "resisting new technology" because of personal
reasons, such as not wanting to learn it, or being threatened by it. Though
I do not learn or enjoy learning as much as I did 30 years ago, that has
nothing to do with my position. I like new technology, and enjoy using new
things. I love the WSIWYG interface in my word processor, where it is
vastly superior to any character based interface. Windows GUI interface
is nice in many ways, but clunky in others, requiring a console interface
for things such as creating a text file listing all files named "???0716*.*"
on partition "D:". GUI simply is not always better. PC based client/server
systems are fine, one I wrote has been running since 1987. But PC based
C/S is not the best way to approach every situation. I don't dislike OO, I
can see certain advantages to that approach. I don't dislike the C/C++ type
languages, they are okay for writing system level software, for which C
was originally created, but crummy for writing business apps, for which
they are ill-suited. Sure, you can do it, but why? No fixed point scaled
data type, cryptic syntax and dangerous constructs like =/==, or pointers
and indirection, which business applications rarely or never require. I
won't argue the issue here, except to point out that my reasons are very
objective.

The bottom line of why I am so adamant on these issues, and why I feel
so strongly about them is simple and clear. There is an attitude in our
industry today that I view as almost a mass insanity, because it is not
logical, it goes against long established business practices, and it has
been highly unproductive to the point of disaster in every single situation
with which I am personally familiar. This insane attitude can be stated
clearly as "Mainframes are always bad, dump them all for PC based
client/server. Character interfaces are always bad, dump them all for
GUI. Procedural code is bad, dump it all for OO. And do all of this
IMMEDIATELY! No thinking required, and especially don't ask what it
costs, or what the specific benefits are." I have seen this attitude grow
and grow in management, and watched in horror as shop after shop has
been devastated by it. Millions and millions of dollars spent as if it
were water, and for all the benefit the users derived, it might as well
have been piled up and set on fire. I see this happening FOR REAL
every single day, and it makes me sick to my stomach. It's not the
technology per se that bothers me, it is this blind adherence to a position
that is stupid and indefensible, and clearly demonstrably so, in every
case where I have seen it happen. No exceptions, not one. No 'partial
successes'. Just pure unadulterated failures, one after another. One of
my clients has spent in excess of $20 million and four years trying to
do exactly what I describe above. The users have yet to see even one
benefit, and none is remotely close. Not one application has been taken
from the mainframe, and no significant (non trivial) application has yet
to be brought up on client/server. None. Nada. Zip. It is virtually certain
that this will be the situation a year from now. Some shops can benefit
from dumping the mainframe and going PC based C/S. Some apps can
benefit from GUI interfaces. Some tasks are better handled with OO.
But not ALL of them!

Now, am I unique in that the experiences I have seen are only the rare
exceptions? I don't know, but I would be immensely relieved if I saw
proof that they were. Several local disasters are better than industry
wide disasters. But the reasons for the failures I have seen are logical
and obvious, at least to me. And, from what I can tell, it seems this
same attitude that has caused these disasters is being propounded and
defended in this forum. I have seen with my own eyes lots of serious,
undeniable, objective proof of why this attitude can bring disaster. If
I am asked to believe my completely consistent experiences are the
exception, then I need to see equally believable, serious, undeniable,
and objective proof of this. If that proof exists, fine, give it to me and
I'll listen. But do not expect me to except an opinion without concrete
evidence that what I clearly see happening around me is not also
happening industry wide. From my perspective, this seems a very
reasonable position to take, under the circumstances. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-25T12:10:23+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3fea1d45_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com...
> "Gary" <IDontThink@so.com.so> wrote:
> > "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[5 more quoted lines elided]…
>

OK, bring it on...<G>

> It may seem that I am "resisting new technology" because of personal
> reasons, such as not wanting to learn it, or being threatened by it.
Though
> I do not learn or enjoy learning as much as I did 30 years ago, that has
> nothing to do with my position. I like new technology, and enjoy using new
…[3 more quoted lines elided]…
> for things such as creating a text file listing all files named
"???0716*.*"
> on partition "D:".

This can be done with a GUI interface; it is just that the way you choose to
do it is more familiar to you.

>GUI simply is not always better. PC based client/server
> systems are fine, one I wrote has been running since 1987. But PC based
> C/S is not the best way to approach every situation. I don't dislike OO, I
> can see certain advantages to that approach.

I contend that you are not qualified to judge.

It would be much more honest if you simply said: "I don't like watching
installations rushing to embrace OO simply because of fashion...", rather
than getting into a discussion on the merits of OO, or otherwise, without
having used it. Theoretical knowledge is one thing; practical experience is
quite another.

> I don't dislike the C/C++ type
> languages, they are okay for writing system level software, for which C
…[6 more quoted lines elided]…
>

A series of platitudes, that "everybody knows", without much substance...

You start by saying you "don't dislike"... then proceed to give reasons why
you DO dislike...<G>

The fact is that you prefer COBOL. It's OK. Just say that.

> The bottom line of why I am so adamant on these issues, and why I feel
> so strongly about them is simple and clear. There is an attitude in our
> industry today that I view as almost a mass insanity, because it is not
> logical, it goes against long established business practices, and it has
> been highly unproductive to the point of disaster in every single
situation
> with which I am personally familiar. This insane attitude can be stated
> clearly as "Mainframes are always bad, dump them all for PC based
…[3 more quoted lines elided]…
> costs, or what the specific benefits are."

Yes, there are some places where that would be true, and I agree with you,
it is stupid.

It staggers me that this has been the UNIVERSAL experience, for you.

>I have seen this attitude grow
> and grow in management, and watched in horror as shop after shop has
…[4 more quoted lines elided]…
> technology per se that bothers me, it is this blind adherence to a
position
> that is stupid and indefensible, and clearly demonstrably so, in every
> case where I have seen it happen. No exceptions, not one. No 'partial
> successes'. Just pure unadulterated failures, one after another.

Frankly, unbelievable...

Given this is true, I can understand your horror.

So, what would you do about it? Avoid new technology? Not a very good
solution, is it? (Like throwing the baby out with the bathwater...)

Obviously, the sites where this has occurred are suffering from much more
than just failure to cope with new technology. I am immediately tempted to
wonder how they managed their existing COBOL projects, and whether these
were invariably successful...


>One of
> my clients has spent in excess of $20 million and four years trying to
…[3 more quoted lines elided]…
> to be brought up on client/server. None. Nada. Zip. It is virtually
certain
> that this will be the situation a year from now. Some shops can benefit
> from dumping the mainframe and going PC based C/S. Some apps can
> benefit from GUI interfaces. Some tasks are better handled with OO.
> But not ALL of them!

The conclusion you reach is debatable. It is certainly true that THIS shop
needs some severe overhauling before it even attempts to implement new
technology. It looks to me like some "culture change" could be in order.
There isn't much point in sowing good seed on stony ground, never watering
it, then deciding it was crap seed because it didn't grow...

Some tilling, cultivation, and removal of rocks, would provide a more level
playing field...

>
> Now, am I unique in that the experiences I have seen are only the rare
> exceptions? I don't know, but I would be immensely relieved if I saw
> proof that they were.

No, there are many failures when COBOL shops attempt to implement this
technology, especially if they do so using the existing practices and
procedures that haven't changed for 40 years. (Sometimes existing Local
Standards are not conducive to new ways of doing things, and this in itself,
can provide a source of conflict, before you even START getting into doing
what needs to be done...)

However, it certainly isn't a case of UNIVERSAL failure. As I mentioned
elsewhere, I have seen COBOL programmers successfully implement these new
technologies, when properly managed, supported,  and motivated. The
resistance seems to be more political than practical. I have been trying for
some years now to get my head round WHY it is so... It still isn't clear.

The results of it are pretty devastating though. Every day we see more COBOL
jobs disappearing. COBOL is simply being overtaken by events. The total
inability to adapt and change to the new IT wave is placing it under
sentence of death. It's like watching the light in the sky that is the
approaching comet, getting bigger every day, and nobody is prepared to build
a spaceship...

> Several local disasters are better than industry
> wide disasters. But the reasons for the failures I have seen are logical
…[10 more quoted lines elided]…
> reasonable position to take, under the circumstances. :-)

So, you believe the failures are because of an attitude?

I believe they are because of a lack of understanding of what is involved,
and the need for change. I have no doubt whatsoever that I could implement a
successful OO project on these sites, given the support of Senior
Management, and some time for "education" that was not assessed as being
part of the "project schedule".

Even leaving that aside, I believe they could improve their existing
productivity using the technology they know and love, just by managing
change better within their IT organisation.

Programmers are generally bright people and they like doing stuff that is
different (especially if it enhances their CV...<G>).

And it wouldn't cost $20 million.

I am genuinely sorry that your first hand exposure to new technology has
been so negative.

It is not the fault of the technology. (It is used with great success by the
REST of the World...who are unfettered by considerations about how things
have always worked.)

Thanks for your explanation as to why you feel the way you do.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-26T22:09:17+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000038a.02dfce21@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com>`

```
Peter,

> Theoretical knowledge is one thing; practical experience is
> quite another.

For a discussion relating to the difficulty in working with objects in 
the modern world, see http://www.artima.com/intv/abstractP.html - 
Anders talking about .NET and C# in a networking world. Many of the 
problems he's addressing are due the hidden infrastructure and 
attempting to maintain a consistent class structure over multiple 
instances of an object.

Procedural is easier.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Gary" <IDontThink@so.com.so>
- **Date:** 2003-12-29T03:25:49+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<19NHb.504247$275.1417469@attbi_s53>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com>`

```
"Judson McClendon" wrote:

<snip>

Judson, thanks for describing your perspective. Generally, without
nitpicking, I agree with it. I have seen many enterprises embark on "new
technology" solutions to resolve perceived problems with existing systems.
Almost all fail. Often, the existing systems problems are solvable, but the
"desire" to take a pragmatic approach is erased by ego. My observation is
that such emotional drivers (often expressed as "enlightenment" and/or
"vision" -- i.e. "I see it but the rest of you are blind") are an unlikely
foundation for progress nor the "right" decision.

"Peter E.C. Dashwood" wrote:

<snip>

Pete, I agree that (in the bigger picture) the continued success of COBOL is
largely dependent on the ability of its eco-system to embrace "new
technology". Many of the facilities provided by non-mainframe COBOL vendors
today, do provide the tools necessary for that work (and many application
providers do exploit those functions, either by extending their existing
COBOL applications or by building composite applications).

I don't believe that OO is necessarily the essential basis though. This is
your "enlightenment", but I'm really not sure it is so totally applicable to
COBOL as you seem to (want to) assert. COBOL is (upon comparison) a very odd
beast. It (like SQL) was built for a specific purpose and IMO I believe
that's why it has persevered for so long (and also why, perhaps, it has been
stigmatized by the rest of the industry for nearly as long). In staying true
to its original purpose the language has evolved by exploiting "new
technology" at a higher level than a "typical" programming language. We talk
of OO as (multiple) layers of abstraction, but I think it's interesting to
consider that COBOL has always provided just that (e.g. datatypes).

Gary.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-29T09:32:16+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000398.00a3316a@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <19NHb.504247$275.1417469@attbi_s53>`

```
Gary,

> I have seen many enterprises embark on "new
> technology" solutions to resolve perceived problems with existing systems.
> Almost all fail.

Of course, it was ever thus. Remember Jackson Sructured Programming? I was 
appalled at the way some sites implemented it, only to find myself working 
at a site which used it as their standard! Eventually it was dropped.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T15:27:00+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<45d6c75d2bfd245ea2f5abac64be711d@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <19NHb.504247$275.1417469@attbi_s53> <VA.00000398.00a3316a@ieee.org>`

```
"Doug Scott" <dwscott@ieee.org> wrote:
> Gary,
> >
…[6 more quoted lines elided]…
> at a site which used it as their standard! Eventually it was dropped.


Remember Decision Tables? We were told that everything before had
become obsolete, and if we didn't adopt Decision Tables immediately,
we would surely become obsolete too. Remember when the academic
community was promoting Pascal as the be-all-end-all language, much
as OO proponents do now? One of the advantages of long experience
is that you get to see the cycles of trends. They come and most go. A
careful nose can usually spot the ones that will stay. My nose has a
pretty good long term track record. I was amused at the Decision Table
brouhaha, and didn't bother to pursue it. I learned Pascal because it is
useful for printing algorithms (what Wirth intended anyway, and was
horrified at what people wanted to use it for) but never developed a
system in it. I studied 4GLs a bit, and decided they were on the wrong
side of the point of diminishing return. Meanwhile, I gobbled up a
number of assembly languages, a group of other languages, and jumped
into structured programming after one trial program, all of which have
been good decisions. Some people are telling me my nose is off base
on OO, but this has often happened in the past when it turned out that
my nose was right. Time will tell, sniff, sniff. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-29T16:27:11+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bspkku$l1c$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <19NHb.504247$275.1417469@attbi_s53> <VA.00000398.00a3316a@ieee.org> <45d6c75d2bfd245ea2f5abac64be711d@news.teranews.com>`

```

On 29-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> . I learned Pascal because it is
> useful for printing algorithms (what Wirth intended anyway, and was
…[7 more quoted lines elided]…
> my nose was right. Time will tell, sniff, sniff. :-)

As with Pascal, there are very good usages for OO.

But my nose tells me that panaceas for all problems are hard to find.

We should pick the tools that work best for solving our needs.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-29T22:13:19+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000039c.0073dd16@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <45d6c75d2bfd245ea2f5abac64be711d@news.teranews.com>`

```
Judson,

> Remember Decision Tables?

I have the very book here, from the "Computer Monographs" series - 
"Programs from Decision Tables" which I found faintly interesting at the 
time, but thought it was technology over-applied: one of the original 
hammers looking at nails. The rest of the series is within the same vein 
- "List Processing", Recursive Techniques" (we've already discussed 
that)...

> Remember when the academic
> community was promoting Pascal as the be-all-end-all language, much
> as OO proponents do now?

Pascal was (is) a great language, but I found the typing overly strong 
for my liking - I couldn't prototype very well, even though I'd come 
from an Algol-derived commercial language (CLEO).

> I studied 4GLs a bit, and decided they were on the wrong
> side of the point of diminishing return.

Yes, I remember that. I also remember ICL Australia deciding that RPG 
was THE language of the future, and declaring that all programs would 
have to be developed using RPG. It only lasted a year or two, but I was 
caught in the crossfire and had to develop one commercial program using 
it :-(

> Some people are telling me my nose is off base
> on OO, but this has often happened in the past when it turned out that
> my nose was right.

My guess is that you're going to be bypassed on this one, for the simple 
reason that all modern development platforms are OO - unless you're 
talking Assembler/C. It's similar to the triumph of Cobol over the other 
language contenders at the time - the snowball effect. And if you go to 
buy a set of tools now for a new shop, it'll be OO, because all the 
language development toolwriters were brought up using OO. And that's 
what they'll provide for their customers. It doesn't matter now about 
the merits or otherwise of Cobol, or indeed OO.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-30T14:05:13+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<7cdc9dc9c63fee7b835c6267c047f0b0@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <45d6c75d2bfd245ea2f5abac64be711d@news.teranews.com> <VA.0000039c.0073dd16@ieee.org>`

```
"Doug Scott" <dwscott@ieee.org> wrote
>
> My guess is that you're going to be bypassed on this one, for the simple
…[6 more quoted lines elided]…
> the merits or otherwise of Cobol, or indeed OO.

I'm sure you are correct, Doug. I was thinking more in terms of a 'post
mortem' analysis that going all OO had been a bad decision. Much like
when the EPA admitted that spending $ billions ripping all the asbestos
from all old buildings had been a bad idea. Doesn't help anything, but at
least you can have a sense of vindication that you thought it was a bad
idea all along. Everybody likes to say "I told you so!" :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-31T11:08:02+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff1f7af_9@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <45d6c75d2bfd245ea2f5abac64be711d@news.teranews.com> <VA.0000039c.0073dd16@ieee.org> <7cdc9dc9c63fee7b835c6267c047f0b0@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:7cdc9dc9c63fee7b835c6267c047f0b0@news.teranews.com...
> Doesn't help anything, but at
> least you can have a sense of vindication that you thought it was a bad
> idea all along. Everybody likes to say "I told you so!" :-)

No, Judson, not everybody...

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T01:06:58+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231200658.11149.00001915@mb-m11.aol.com>`
- **References:** `<45d6c75d2bfd245ea2f5abac64be711d@news.teranews.com>`

```

In hyperbolic mode, and on the fly 

 "Judson McClendon" judmc@sunvaley0.com 
Date: 12/29/03 10:27 AM EST
Message-id: <45d6c75d2bfd245ea2f5abac64be711d@news.teranews.com>

quickly jots in 
 
<<
...
 Remember when the academic
community was promoting Pascal as the be-all-end-all language, much
as OO proponents do now?
...
>>

Actually, I don't remember that. The academic community was very level-headed
about Pascal.  By and large, their spin on Pascal was that it is an excellent
teaching language.  And I think that has not been challenged.

For example, you yourself might agree that C# is absurd as an entry point for
the uninitiated.  I found COBOL a great early language, but if I recall my
course work way back when, I think my first language at school was actually
FORTRAN, which I found easy, (except interestingly enough COMMON).

Truthfully, I fould Pascal the easiest language I ever did learn as far as
basic productivity. I do not claim to be expecially good with it. I never used
its OO variations.

But I would agree that the academic community has made a mistake to abandon the
more proven technologies. Their job however has paradoxes. A good school really
cannot afford to emphasize what is best, it has to emphasize what produces
marketable skill sets. We must be forgiving in some respects. Espcially if we
are considering training for use in business environments where practicality is
the issue not superiority of the tools. VB sells as a skill set, for example;
love it or hate it. Your a teacher, train 'em in what sells after graduation.

But I do not recall the academics thinking Pascal was the most effective
language for mainstream production in DP.

You ought to cut out that teacher bashing down there, now.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T16:11:29+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > Windows GUI interface
…[5 more quoted lines elided]…
> do it is more familiar to you.

I agree that this is not a necessary limitation of any GUI. But I am very
curious, how would you do the above using the Windows GUI? I wait
with bated breath. ;-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-30T16:19:19+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com>`

```
Pete, this isn't a challenge. If you know how to do this, please tell me,
I could really use the technique. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-31T11:25:36+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff1fbcf_9@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com...
> Pete, this isn't a challenge. If you know how to do this, please tell me,
> I could really use the technique. :-)

I do know how to do it, and anyone who is familiar with the use of OO
components and controls could work out how to do it in a few minutes. It can
be done by combining standard Windows components on a standard Windows Form.

For my own part, I would then wrap the result as a component and the
functionality can then be deployed in Windows applications or on Web Pages
using OO web scripting (ASP, f'r'instance).

You are expecting to see a block of procedural code that you can use.

It COULD be done that way too, but it is tedious and I wouldn't waste time
on it. The OO solution can be assembled in minutes, using quick build
products like Fujitsu PowerCOBOL.

If you seriously want this functionality under Windows or the web, I can
provide it for you. My rates are very reasonable.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-31T20:24:13+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[11 more quoted lines elided]…
> You are expecting to see a block of procedural code that you can use.


No, I was expecting a series of steps. I was referring to the Windows
GUI, not the Windows API. :-)  Here is the exchange:

Pete:
> Jud:
> > Windows GUI interface
…[5 more quoted lines elided]…
> do it is more familiar to you.

Perhaps we were just mis-communicating. Doing this in a program is
no problem. But I have been unable to find a way to do it using the
Windows GUI without reverting to the commend prompt. It's trivially
easy using the command prompt:

    dir "d:\???0716*.*" /a/b >files.txt

If you can do this ad hoc from the GUI, I will be truly impressed. :-)

Here's another one. You can do this file by file in the GUI, but if there
are lots of files, it is a pain:

    ren *.txt *.doc

Try this. In a WinXP Explorer window select several (disposable!) files,
press F2, and change the name of one. I'm not sure what they are trying to
do, but I haven't found it useful. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-01-01T02:56:34+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3FF38C51.A3AE0361@shaw.ca>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com>`

```


Judson McClendon wrote:

> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
…[43 more quoted lines elided]…
> do, but I haven't found it useful. :-)

Well the obvious thing with your Drive D search would be to tell you - "Do your own
homework" <G>.

Anyway, just this once you get lucky, because it's something I had written a while
back - you have to RESEARCH tools  based on current NEED - so unfair to expect Pete
to pull a rabbit out of his hat when he doesn't have a current need..

I'm glad you clarified your original search Drive D using a wildcard to :-

    dir "d:\???0716*.*" /a/b >files.txt
    ren *.txt *.doc

Read below - you can achieve both the above.

Using the Demo GUI samples create a dialog with an entry field for your wildcard,
(including your drive D), and a Listbox, (Ordered not Sorted) if you want to to
display the result of the "search". Depending on what you want - single or
multi-select  from the Listbox and use Pushbuttons for your choices, 'Copy",
"Delete", 'Rename" etc.

Alternatively write the collection elements to your text file with a Callback (see
below). Note the following code does NOT use GUIs - that's for you to do as
described above.

I've written an OO trigger program to get you started : -

*>--------------- startwildcard.cbl--------------------------

Program-id. StartWildcard.

Class-control.          Filenames2  is class "filenam2"
                        .

WORKING-STORAGE SECTION.
01 charx                    pic x.
01 ws-length                pic x(4) comp-5.
01 Pathname pic x(18) value "C:\ucs\1-bin\*.bak".

*>***** substitute your wildcards as appropriate

*> OBJECTS
01 os-Filenames         object reference value null.
01 os-SortedCollection  object reference value null.

Procedure Division.

compute ws-Length = function length (Pathname)

*> 1 - Do the Delete first

invoke FileNames2 "new" returning os-Filenames
invoke os-FileNames "deleteUsingWildcard"
       using ws-Length, Pathname

*> 2 - return a list of filenames

inspect Pathname replacing all "bak" by "cpy"
invoke os-FileNames "getFilenamesWithWildcard"
       using ws-Length, Pathname
       returning os-SortedCollection

if os-SortedCollection <> null
   invoke os-SortedCollection "display"
   *> gives you a DOS text window with names wrapped around -
   *> useful for testing only

else display "No files found"
End-if

accept charx
invoke os-Filenames "finalizeObjects"

if os-SortedCollection <> null
   invoke os-SortedCollection "deepfinalize"
   returning os-SortedCollection
End-if

STOP RUN.
*>-----------------------------------------------------------

*>------------------ filenam2.cbl --------------------------

*> Some Notes on what's going on :-

*> Although I'm using both Ordered and Sorted Collections I
*> make no reference to the first in Class-control. It is the M/F
*> class 'Filename' that establishes a link to Ordered
*> Collection. I now have within this class (Filename2)
*> the properties/methods for an OrderedCollection.
*> The SortedCollection class is listed so that I can invoke to
*> create a SortedCollection and then fill it with elements
*> from the OrderedCollection.
*>
*> When deleting files I could use "perform varying n from 1
*> by 1 until n > CollectionSize'; instead I use Callbacks.

*> Callbacks can be used with collecions, GUI classes or the
*> ExceptionManager. When used with collections there are four
*> method names that allow selectivity :-

*> invoke aCollection "do" using Methodname(obj ref)
*>                    "select"
*>                    "reject"
*>                    "collect"

*> Having created a reference to a callback method (which could
*> be generated in another class), I then 'invoke
*> aCollection "do" using Methodname'. Alredy knowing the
*> size of the collection (elements) the Callback iterates
*> through each element. If I want to 'break out of the
*> callback' :-

*>      if this is not condition I want
*>           invoke aCollection "quitIteration"
*>           EXIT METHOD
*>      end-if
*>
*> The "quitIteration" is triggerd on the CollectionObject,
*> NOT the callback method
*>
*> I'm using Collections 'ofReferences'. In the case of
*> method "getFilenamesUsingWildcard" the elements in the collec-
*> tion are objects for displaying in a Listbox - the altenative
*> is to 'translate' them to text 'strings', if you wanted
*> to include a set of files to be zipped.

*>--------------------------------------------------------------

Class-id.       FileNames2
                inherits from Base.

Class-control.  FileNames2           is class "filenam2"

                Callback             is class "callback"
                CharacterArray       is class "chararry"
                FileName             is class "filename"
                SortedCollection     is class "srtdclln"
.

*> Coded as a separate class so that more methods can be
*> added later

*>--------------------------------------------------------------
FACTORY.
*>--------------------------------------------------------------
Method-id. "new".
*>--------------------------------------------------------------
Linkage Section.
01 lnk-self                     object reference.
Procedure Division returning lnk-self.
  invoke super "new" returning lnk-self
End Method "new".
*>-------------------------------------------------------------
END FACTORY.
*>-------------------------------------------------------------
OBJECT.
*>--------------------------------------------------------------
WORKING-STORAGE SECTION.
01 charx                    pic x.
01 ws-length                pic x(4) comp-5.
01 ws-size                  pic x(4) comp-5.
01 ws-WildCardName.
   05 pic x occurs 1 to 100 depending on ws-length.

*> OBJECTS

01 os-CallbackDefaultSort      object reference value null.
01 os-CallbackDeleteFile       object reference value null.
01 os-SortedCollection         object reference value null.
01 os-TempCollection           object reference value null.

*> NOTE : Methods are listed in alphabetical order

*>-------------------------------------------------------------
Method-id. "CallbackDefaultSort".
*>-------------------------------------------------------------
Local-storage section.
01 ls-bytes                  pic x(4) comp-5.
01 ls-string                 object reference.
01 ls-text1                  pic x(100).
01 ls-text2                  pic x(100).

Linkage Section.
01 lnk-Element                      object reference.

Procedure Division using lnk-Element.

   invoke lnk-element "sizeinbytes" returning ls-bytes
   invoke lnk-element "getValue"    returning ls-text1
   move ls-text1(1:ls-bytes)        to ls-text2
   invoke CharacterArray "withLengthValue"
          using     ls-bytes, ls-text2
          returning ls-string
   invoke os-SortedCollection "add" using ls-string

*> Rather than above coding - you would have thought the
*> following would work - but it doesn't !

*>   invoke os-SortedCollection "add" using lnk-element

*> When querying lnk-element with the Animator it shows
*> 'search criteria' used with the wildcard ????

End Method "CallbackDefaultSort".
*>-------------------------------------------------------------
Method-id. "CallbackDeleteFile".
*>-------------------------------------------------------------
Local-storage section.
01 ls-filename                      pic x(100).
01 ls-StatusCode                    pic x(4) comp-5.
Linkage Section.
01 lnk-Element                      object reference.
Procedure Division using lnk-Element.

invoke lnk-Element "getValueZ" returning ls-filename
call "CBL_DELETE_FILE" using     ls-filename
                       returning ls-StatusCode

*> I could check the ls-StatusCode and as necessary do a
*> "quiteIteration"

End Method "CallbackDeleteFile".
*>-------------------------------------------------------------
Method-id. "checkFiles".
*>-------------------------------------------------------------
Local-storage section.
01 ls-size                          pic x(4) comp-5.
01 ls-string                        object reference.

Procedure Division.

invoke CharacterArray "withLengthValue"
        using     ws-length
                  ws-WildCardName
        returning ls-string

invoke FileName "expandwildcards"
       using     ls-string
       returning os-TempCollection

invoke os-TempCollection "size" returning ws-size

if   ws-size <> zeroes
     display "This is the Ordered Collection"
     invoke os-TempCollection "display"
     accept charx

     invoke SortedCollection "ofReferences"
         using     ws-size
         returning os-SortedCollection
     invoke Callback "new"
         using     self "CallbackDefaultSort "
         returning os-CallbackDefaultSort
     invoke os-TempCollection "do" using os-CallbackDefaultSort

*>   As yet the next line doesn't work - it was another attempt at
*>  a shortcut
*>   invoke os-SortedCollection "addAll" using os-TempCollection
     display "This is the Sorted Collection"
     invoke os-SortedCollection "display"
     accept charx

End-if

*> Invoking the collections to 'display' is really only useful
*> to test - all you get is a wrap-around in a DOS text window

End Method "checkFiles".
*>-------------------------------------------------------------
Method-id. "deleteUsingWildcard".
*>-------------------------------------------------------------
Linkage section.
01 lnk-length                pic x(4) comp-5.
01 lnk-WildCardName.
   05 pic x occurs 1 to 100 depending on lnk-length.

Procedure Division using lnk-length lnk-WildCardName.

move lnk-length       to ws-Length
move lnk-WildcardName to ws-WildcardName
invoke self "checkFiles"

if   ws-size <> zeroes
     invoke Callback "new"
            using     self "CallbackDeleteFile "
            returning os-CallbackDeleteFile
     invoke os-SortedCollection "do"
            using os-CallbackDeleteFile
End-if

End Method "deleteUsingWildcard".
*>---------------------------------------------------------------
Method-id. "finalizeObjects".
*>-------------------------------------------------------------
*> os-CallbackDefaultSort
*> os-CallbackDeleteFile
*> os-SortedCollection........finalized in Business Logic
*> os-TempCollection


if os-CallbackDefaultSort <> null
   invoke os-CallbackDefaultSort "finalize"
   returning os-CallbackDefaultSort
End-if

if os-CallbackDeleteFile <> null
   invoke os-CallbackDeleteFile "finalize"
   returning os-CallbackDeleteFile
End-if


if os-TempCollection <> null
   invoke os-TempCollection "finalize"
   returning os-TempCollection
End-if

End Method "finalizeObjects".
*>-------------------------------------------------------------
Method-id. "getFilenamesWithWildcard".
*>-------------------------------------------------------------
Linkage section.
01 lnk-length                pic x(4) comp-5.
01 lnk-WildCardName.
   05 pic x occurs 1 to 100 depending on lnk-length.
01 lnk-SortedCollection      object reference.

Procedure Division using     lnk-length
                             lnk-WildCardName
                   returning lnk-SortedCollection.

 move lnk-Length       to ws-Length
 move lnk-WildcardName to ws-WildcardName
 invoke self "checkFiles"

 if ws-Size <> zeroes
    set lnk-SortedCollection to os-SortedCollection

 else set lnk-SortedCollection to null
 End-if

End Method "getFilenamesWithWildcard".
*>---------------------------------------------------------------

End OBJECT.
End CLASS FileNames2.

*>--------------------------------------------------------------

I made minor changes to the above and would have liked to write the conversion from
Ordered to Sorted Collectiuon in shorthand - whichever I tried, didn't work. Doesn't
mean the M/F support classes don't work - just that yours truly hasn't got the hang
of it. So we are back to the researching of new tools - and I'll be making some
queries in Answer Exchange to resolve my gaffes.

To finish, using one of BIll's pet phrases, "And having said that.....".,  I think I
would be likely to have more luck in converting you to Catholicisim than converting
you from Procedural to OO COBOL !!!

Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 16)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T11:25:21+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b2e38a507e568e392a5247245d73c262@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca>`

```
Thanks for the code Jimmy, it's very interesting and I saved it for future
reference. :-)

But I have not communicated well. I am not seeking a program, module,
component, or any created thing, either OO, procedural or spaghetti
source code, or binary machine language. ;-) I can easily write source
code to do this programmatically. What I am asking for (with good
reason) is *a series of manual steps I can do at the keyboard* to
produce, using only the Windows GUI, the same effect as entering a
command similar to this from the command prompt:

    dir "d:\???0716*.*" /a/b >files.txt

(If the answer is "you can't do that", then don't bother reading further. :)

That particular wildcard is only an example, in use it would vary. In fact,
I believe it is essentially impossible to produce *any* 'text file consisting
of a list of file names' by using the Windows GUI and the keyboard alone
with no programming, wildcards or no. I can produce a graphic file, or a
printed listing of file names, by displaying them in an Explorer window,
pressing 'Print Screen', pasting the clipboard into a picture editor, then
printing or saving the image. One could, I suppose, use OCR to take the
image and convert to text, but that is extreme clunky, limited number of
file names and no wildcards. Creating a file of file names is a very useful
thing that I do quite a lot. Not in systems, where I would write code to do
it, but ad hoc from the keyboard when I am using the PC for various tasks.
I know of no way to do this, other than using the command prompt or
writing a program or using an already written program of some sort to do
the same thing. I made the comment initially as an example of when the
Windows GUI isn't sufficient. And in the same vein,  I also suggested
another common and useful thing the Windows GUI cannot do, AFAIK.
To produce the same effect as entering a command similar to this from the
command prompt:

    ren *.txt *.doc

These examples of what (I believe) the Windows GUI simply cannot be
used to achieve (from the keyboard, without additional programming), are
such common and useful tasks that, if it CAN be done using the Windows
GUI, I would really like to know how. Others have asked me this same
question on several occasions, so I know I'm not the only one who could
use such a method.

The reason I ask here is that, when I mentioned these as insufficiencies
in the Windows GUI, Pete responded that it could be done, only I was
using different methods. I'm not challenging Pete's comments, but it
would be very useful to me if it can be done. So, can it be done, and
how? I would really, really like to know. :-)

Whew! Was I clear this time? :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 17)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-01-01T12:02:48-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-7F0FCC.12024801012004@corp.supernews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com>`

```
In article <b2e38a507e568e392a5247245d73c262@news.teranews.com>,
 "Judson McClendon" <judmc@sunvaley0.com> wrote:

> But I have not communicated well. I am not seeking a program, module,
> component, or any created thing, either OO, procedural or spaghetti
…[8 more quoted lines elided]…
> (If the answer is "you can't do that", then don't bother reading further. :)


1 - Hit the meta key for the "Start" menu -- whatevery that is, 
Shift-Alt-S-F27 or something like that.

2 - Up arrow to the "Run..." option.

3 - Enter 'cmd /k dir d:\???0716*.* /a/b >files.txt' in the resulting 
imput box.

4 - Hit "enter" or click "ok".
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 17)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2004-01-01T17:26:37+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3FF45886.5735321E@shaw.ca>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com>`

```


Judson McClendon wrote:

>
> Whew! Was I clear this time? :-)

Yes, and has nothing to do with OO or GUIs. You had better contact the U. of Bellingham
,Wa for an enhancement to Windows Explorer, (to get a file listing), or the 'Run' box. to
recognize the old DOS commands..

 From the desktop I tried Start--->Run----> "dir c:\ucs\1-bin\*.cpy > files.txt" ---->
<Enter>  - replied, "Can't find program DIR".

As a rider - using the MS PWB Editor that came with MS COBOL versions 4 and 5 (re-badged
MF V 3), within the Editor I can bring up a command line that let's me do "dir
c:\ucs\1-bin\*.cpy > files.txt" - but again it's text not GUI.

Jimmy
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 18)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T22:00:52+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<5800b7f44bd7dc05640f31fbe772ecfd@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <3FF45886.5735321E@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote:
> Judson McClendon wrote:
> >
> > Whew! Was I clear this time? :-)
>
> Yes, and has nothing to do with OO or GUIs.

Not OO, no. But it does have to do with limitations of the Windows GUI,
and probably just about *any* GUI. It is hard for me to imagine a 'true GUI'
solution to this particular problem. My point was that GUI is not suitable
for everything. Generally true of all tools, including OO, IMHO. :-)

> You had better contact the U. of Bellingham,Wa for an enhancement
> to Windows Explorer, (to get a file listing), or the 'Run' box. to
> recognize the old DOS commands.

As Joe pointed out, you can do it from the Start/Run dialog box by
adding 'cmd /k' before the 'dir'. But that is still not a GUI solution, it is
simply a shortcut to the command line. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 19)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-01-02T09:33:40-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-101E25.09333902012004@corp.supernews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <3FF45886.5735321E@shaw.ca> <5800b7f44bd7dc05640f31fbe772ecfd@news.teranews.com>`

```
In article <5800b7f44bd7dc05640f31fbe772ecfd@news.teranews.com>,
 "Judson McClendon" <judmc@sunvaley0.com> wrote:

> "James J. Gavan" <jjgavan@shaw.ca> wrote:
> > Judson McClendon wrote:
…[16 more quoted lines elided]…
> simply a shortcut to the command line. :-)

How can you have a GUI solution to a problem that is not a GUI problem?  
That is why you have shortcut access to the command line -- to address 
command line problems.

GUIs are not everything.  They can be great for providing visual clues 
to users about what is possible -- but they also impose some annoying 
problems about creating repeatable processes.

That is why every OS offers a complementary command line shell to 
perform functions like "mv *.txt *.doc".  

It is just using the right tool for the job.

There are other places that are quite solidly "command line" issues:  

Macros, for example, are completely unportable when done with a GUI 
recording tool -- unless the other user has all icons in exactly the 
same place, and all application windows open at exactly the same 
coordinants, the the recorded mouse clicks will fail and break the macro 
-- text command files (*.bat, *.cmd) do not have this problem.  

Compiles are the same -- a user might enjoy dragging little windows and 
buttons around to create applications.  But when building an application 
with a team, or for use on different machines, an automated, repeatable, 
command line type build of the product is almost a must, and cannot be 
easily done with GUI tools.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 20)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-02T15:22:29+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8f73127ef6334116d921887c7c9e3bf8@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <3FF45886.5735321E@shaw.ca> <5800b7f44bd7dc05640f31fbe772ecfd@news.teranews.com> <joe_zitzelberger-101E25.09333902012004@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > "James J. Gavan" <jjgavan@shaw.ca> wrote:
…[9 more quoted lines elided]…
> > for everything. Generally true of all tools, including OO, IMHO. :-)

Let me disagree with my own statement. :-) It is simple to use the search
dialog of Explorer to display a list of such file names in a window. You
just can't 'cut and paste' the file names, only the files themselves. But an
implementation of this facility could be done in the Windows GUI, by
adding a feature where you could highlight file names displayed in an
Explorer window, right click on the selected names, and be presented
with an option 'copy file names to clipboard' would do the trick, and in
a completely 'GUI way'. So I humbly withdraw my comments in the
above paragraph. :-)

> > As Joe pointed out, you can do it from the Start/Run dialog box by
> > adding 'cmd /k' before the 'dir'. But that is still not a GUI solution, it is
…[4 more quoted lines elided]…
> command line problems.

I think my comments just above in this post show this to be a 'GUI
problem' with a 'true GUI solution'. If I can copy and paste a file into
a document, why can't I copy and past the name of the file? There is
nothing about these two things that make one a 'GUI problem' and the
other 'not a GUI problem'. :-)

> GUIs are not everything.  They can be great for providing visual clues
> to users about what is possible -- but they also impose some annoying
…[19 more quoted lines elided]…
> easily done with GUI tools.

Well stated. What you describe above is exactly the kind of thing I am
doing when I want a file containing a list of file names.

Here's my point of all this: How can some people say that we should
drop character based interfaces altogether for application programming,
considering that GUIs are not sufficient for the tasks we programmers
do frequently? When you do time and motion studies, it is clear that
character interfaces can be considerably better than GUIs for some
tasks, such as most data entry tasks, in just about every measurable
way. Once I obtain a tool, I don't throw it away just because a newer
tool comes along. Powered screwdrivers and drills did not entirely
eliminate the need for manual ones for some purposes. That doesn't
mean you shouldn't use newer tools, just don't discard the old ones.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 21)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-01-05T17:57:20-06:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<vvjubi8dna34f7@corp.supernews.com>`
- **In-Reply-To:** `<8f73127ef6334116d921887c7c9e3bf8@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <3FF45886.5735321E@shaw.ca> <5800b7f44bd7dc05640f31fbe772ecfd@news.teranews.com> <joe_zitzelberger-101E25.09333902012004@corp.supernews.com> <8f73127ef6334116d921887c7c9e3bf8@news.teranews.com>`

```
Judson McClendon wrote:
> Here's my point of all this: How can some people say that we should
> drop character based interfaces altogether for application programming,
> considering that GUIs are not sufficient for the tasks we programmers
> do frequently?

Anyone who says that shouldn't be believed in anything else they say. 
(They're probably a salesman for "tool du jour, inc." anyway...) 
Dropping character-based interfaces for -users- would be OK, and in 
fact, probably preferable in today's world, if feasible.  However, a 
programmer or system admin MUST have control over what they are doing - 
and, as this thread has illustrated, the tool most apropos for the job 
is often a command-line-interfaced one.  (I -still- use Notepad on a 
regular basis, and I've only recently changed from dropping to DOS and 
saying "edit blah.txt" - "notepad blah.txt" works just as well.)

The worst programming experience I've had in my life was with something 
from Oracle.  It looked like it was a rapid-development data entry tool. 
  We were trying to make a dropdown box with values A, B, or C, and 
couldn't do it without binding the box to a table/column.  We couldn't 
put event code in, to do things before the page was submitted.

Luckily, this was in a learning environment, so we didn't actually have 
to make any working deliverables.  They said they chose it because it 
was the least common denominator; and, having used it, I must say I 
agree.  :)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 22)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-01-05T20:16:08-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<u2oKb.4604$k_.554802@news20.bellglobal.com>`
- **In-Reply-To:** `<vvjubi8dna34f7@corp.supernews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <3FF45886.5735321E@shaw.ca> <5800b7f44bd7dc05640f31fbe772ecfd@news.teranews.com> <joe_zitzelberger-101E25.09333902012004@corp.supernews.com> <8f73127ef6334116d921887c7c9e3bf8@news.teranews.com> <vvjubi8dna34f7@corp.supernews.com>`

```
LX-i wrote:
> Judson McClendon wrote:
> 
…[27 more quoted lines elided]…
> 

You know what I find annoying, Judson?

Everyone talks about OOP like it was a bloody religion, when in fact you 
have about ten new constructs that can be learnt in five minutes, can be 
used in all sorts of neat ways that are effective, simple, and better 
organized than the old ways.

So based on the fact it has to be capital O capital O capital P, people 
refuse to learn the syntax of a dozen new Cobol statement types. Seems 
like refusing to use divison cause division by zero is still undefined.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 23)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-06T20:34:52+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<btf65b$hhj$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <u2oKb.4604$k_.554802@news20.bellglobal.com>`

```

On  5-Jan-2004, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:

> Everyone talks about OOP like it was a bloody religion, when in fact you
> have about ten new constructs that can be learnt in five minutes, can be
…[5 more quoted lines elided]…
> like refusing to use divison cause division by zero is still undefined.

If one uses OO CoBOL commands without thinking in OO, what is gained?

Changing how we think is hard.  Adding new commands to think the old way is
easy.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 24)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-01-06T16:43:21-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<C0GKb.15324$BA6.468791@news20.bellglobal.com>`
- **In-Reply-To:** `<btf65b$hhj$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <u2oKb.4604$k_.554802@news20.bellglobal.com> <btf65b$hhj$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  5-Jan-2004, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:
> 
…[14 more quoted lines elided]…
> easy.


How would anybody know?  They refuse to try it based on theory based on 
other languages.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 25)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-07T21:07:54+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bthsf9$ps0$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <C0GKb.15324$BA6.468791@news20.bellglobal.com>`

```

On  6-Jan-2004, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:

> >>So based on the fact it has to be capital O capital O capital P, people
> >>refuse to learn the syntax of a dozen new Cobol statement types. Seems
…[10 more quoted lines elided]…
> other languages.

What is this theory?   What are these other languages upon which this theory is
based?

I infer that you think that using OO commands from within CoBOL is useful even
for people who don't "get" OO.    Do you have examples of when you would
recommend using these in such a manner?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 26)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-01-07T17:17:22-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<DC%Kb.51172$BA6.1062058@news20.bellglobal.com>`
- **In-Reply-To:** `<bthsf9$ps0$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <C0GKb.15324$BA6.468791@news20.bellglobal.com> <bthsf9$ps0$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  6-Jan-2004, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:
> 
…[5 more quoted lines elided]…
> based?

Dmaned if I know.  However, I continue to read, on a daily basis, posts 
from peolpe inpthis group that have concluded OPP willnot work based on 
the fact they learnt it from (Java C++, fill in the language).  I hardly 
think it unexpected, since most of them concluded that the procedural 
versions of the same languages were also unsuitable and would also fail 
(in some cases years ago).
> 
> I infer that you think that using OO commands from within CoBOL is useful even
> for people who don't "get" OO.    Do you have examples of when you would
> recommend using these in such a manner?

Sure.  In fact, there are a whole class of programs that I would 
restructure using the OOP commands.

Consider the traditional Cobol system based on a main menu, with each 
program being a subroutine, and the common setup data being read by the 
menu.  Structurally, it normally looks as follows.

	Main program
		call read setup stuff
		menu loop
			choose program
			call program using setup-data
		end menu loop
		stop.

In addition, there will be many standardized methods set up as 
copybooks, normally one for working storage and one for the procedure 
division.  Either that or a bunch of standard subroutine code.

It makes far more sense to organize the same system as follows.

	system object.
		setup stuff
		read-setup method.
		run menu method.
			invoke self read-menu method.
			menu loop.
				choose program
				invoke program-method.
			end menu loop
			stop
		common method one.
		common method two.
		program method one.
		program method two.
etc.

The only real changes made to the old programs at all would be to change 
the program-id to a method-id, add a start-method and an end-method 
statement to the ends of each, and copy them into the new object as a 
copy statement.

The menu would have to change each "call name using" to a "invoke self 
"name" using"

If you simply do that, you gain arguement checking for all system stuff. 
However, if you want to go further, you can.

Since the setup data is now up at the top of the main object, in it's 
own working storage, you could eliminate all the passed arguements 
completely.  Just eliminate the using statements and the linkage sections.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 27)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-07T19:10:54-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401071910.68c63337@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <C0GKb.15324$BA6.468791@news20.bellglobal.com> <bthsf9$ps0$1@peabody.colorado.edu> <DC%Kb.51172$BA6.1062058@news20.bellglobal.com>`

```
Donald Tees <donald_tees@nospam.sympatico.ca> wrote 

> >>How would anybody know?  They refuse to try it based on theory based on
> >>other languages.
> > 
> > What is this theory?   What are these other languages upon which this theory
> > is based?
 
> Dmaned if I know.  

It was your claim, now you say you've no idea why you claimed it ?

> However, I continue to read, on a daily basis, posts 
> from peolpe inpthis group that have concluded OPP willnot work based on 
> the fact they learnt it from (Java C++, fill in the language).

Which is really strange because I read all of this group and have
never seen that.

> I hardly 
> think it unexpected, since most of them concluded that the procedural 
> versions of the same languages were also unsuitable and would also fail 
> (in some cases years ago).

or that.

> Sure.  In fact, there are a whole class of programs that I would 
> restructure using the OOP commands.
…[11 more quoted lines elided]…
> 		stop.

That is not how any of my systems have worked at all.  I do have menu
programs but they are not the 'main loop' but are merely selection
programs that are used when other, better, means of selection fail.

> In addition, there will be many standardized methods set up as 
> copybooks, normally one for working storage and one for the procedure 
> division.  Either that or a bunch of standard subroutine code.
 
> It makes far more sense to organize the same system as follows.
> 
…[14 more quoted lines elided]…
> etc.
 
> The only real changes made to the old programs at all would be to change 
> the program-id to a method-id, add a start-method and an end-method 
> statement to the ends of each, and copy them into the new object as a 
> copy statement.

This doesn't 'make far more sense' at all.  You are building the whole
system into one huge lump of source code that gets compiled all at
once.  The antithesis of OO design.

You have also lost all the dynamics from the system, taking it from a
flexible modular system into a fixed static monolith.
 
> The menu would have to change each "call name using" to a "invoke self 
> "name" using"

> If you simply do that, you gain arguement checking for all system stuff. 

That's no gain at all for a working system.

> However, if you want to go further, you can.
 
> Since the setup data is now up at the top of the main object, in it's 
> own working storage, you could eliminate all the passed arguements 
> completely.  Just eliminate the using statements and the linkage sections.

That is hugely retrograde, why not go further and dump the ID and WS
sections and just PERFORM instead of invoking ?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 27)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-08T16:19:30+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<btjvui$b1d$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <DC%Kb.51172$BA6.1062058@news20.bellglobal.com>`

```

On  7-Jan-2004, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:

> Consider the traditional Cobol system based on a main menu, with each
> program being a subroutine, and the common setup data being read by the
…[8 more quoted lines elided]…
> 		stop.

On mainframes that I have worked on, the menu programs have been outside of
CoBOL programs.   But it seems that menus are pretty much thinking in OO anyway.

Do you have any non-interactive examples where OO commands are useful to people
who don't "think" in OO?

Or maybe I misunderstand - that you are recommending it to replace all called
programs.   From reading your post, I think this may be the case - that you
think passed arguments are a pain, and that programmers should learn to use
"invoke" as a way of avoiding passing arguments.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 28)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-01-08T12:19:33-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<plgLb.73134$BA6.1484427@news20.bellglobal.com>`
- **In-Reply-To:** `<btjvui$b1d$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <DC%Kb.51172$BA6.1062058@news20.bellglobal.com> <btjvui$b1d$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On  7-Jan-2004, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:
> 
…[23 more quoted lines elided]…
> "invoke" as a way of avoiding passing arguments.


Not at all.  I am saying that any standard Cobol program is actually a 
method within the class of programs "standard Cobol Program", and can be 
treated as such at a source code level.

Treatment in those terms allows me to define such a thing as a standard 
Cobil compile method that works in conjunction with a standard platform 
property.  Neither of those are neccessarily linked to "arguements" per se.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 29)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-08T22:30:05+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000402.01816552@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <plgLb.73134$BA6.1484427@news20.bellglobal.com>`

```
Donald,

> Not at all.  I am saying that any standard Cobol program is actually a 
> method within the class of programs "standard Cobol Program",

That's only true if you encapsulate all the functionality of the Cobol 
program into a single object - like "Handle_all_mortgage_processing". Not 
particularly OO, is it?


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 30)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-01-09T07:57:59-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8CxLb.107236$BA6.1917239@news20.bellglobal.com>`
- **In-Reply-To:** `<VA.00000402.01816552@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <plgLb.73134$BA6.1484427@news20.bellglobal.com> <VA.00000402.01816552@ieee.org>`

```
Doug Scott wrote:
> Donald,
> 
…[16 more quoted lines elided]…
> 

No.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 28)_

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2004-01-08T17:27:13+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<RpgLb.33165$IM3.25948@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<btjvui$b1d$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <DC%Kb.51172$BA6.1062058@news20.bellglobal.com> <btjvui$b1d$1@peabody.colorado.edu>`

```
As a follow-up to Howard's comment,

On the online/interactive mainframe systems I've worked on,  They've all 
been too large  to be contained in 1 program.  What a headache that 
would be.  (These systems were CICS and ADS/Online (similar to 
CICS/COBOL, the difference being one is program centric (CICS/COBOL) and 
the other is  map centric (ADS/Online).  Any COBOL programmer could 
follow an ADS/Online program easily.)

In any case, the basic operating of these systems is
1.  Grab a chunk of storage dedicated to an individual user (the storage 
is bound checked such that if anything is "written" over the end of the 
storage the transaction would terminate.)
2.  Display the menu map.
3.  Based on the response of the menu, relinquish control (pick your 
verb) to another program to accomplish the desired function.
4.  Program to accomplish desired function  executes and calls or 
transfers to any number of programs (sub-programs) to accomplish it's 
functions.
5.  At function termination, give control to the menuing program and 
start over.
6.  All screen interaction is pseudo-conversationsl .  (Note for the 
un-initiated:  pseudo-conversational means that control is returned to 
the operating system upon screen display.  A new program is initiated 
upon completion of activity on the screen.)

All "common" data is put into the "chunk" of storage obtained initially. 
  (Obviously, intermediate "chunks" of storage may be obtained as needed 
throughout the process.)

"Conversational" programs (which apparently is what OOP is all about 
based on Donald Tees explanations( are IMHO) more appropriate for those 
systems where all processing is done locally (ie on an individual's 
machine.)  A "conversational" program on a mainframe would cause all 
users of the system involved to wait until an individual actually 
interacted with the program - a performance nightmare!

Functionally, to me, mainframe online processing as I describe it above, 
  seems to me to be what OOP is all about.  Granted, code within the 
modules are procedural (as is code within the individual OOP modules as 
far as I can tell.)

Donald, (or any other OOP guru) what am I missing?  I mean,  display map 
(paint screen), get database info,  modify database info, handle menuing 
tasks etc all seem to be "objects" to me.   It's been a looooooooooooong 
time (early 70's) since I actually had to write terminal code (put this 
character at terminal byte "A", but this character at byte "DC" etc.) to 
display information on a screen.  And I never had to write code to 
actually read or write data to a database.

Dick - who wrote his first program in 1967.

Howard Brazee wrote:
> On  7-Jan-2004, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:
> 
…[23 more quoted lines elided]…
> "invoke" as a way of avoiding passing arguments.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 28)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-08T22:30:06+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000404.018168d7@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <btjvui$b1d$1@peabody.colorado.edu>`

```
Howard,

> Do you have any non-interactive examples where OO commands are useful to people
> who don't "think" in OO?

OO [as its name implies] is based on the Object, which is essentially 
data-oriented rather than procedure-oriented. So you create a system which is 
based on Objects (entities or even records, if you like) with the code attached 
to those objects. The phrase "object-action instead of action-object" reflects 
this. A normal Cobol program will define all the data entities, followed by the 
procedural code which will work with those entities and update/create new ones. 
In OO, you'd define, for each Object, all the code needed to process that Object 
entirely (some calls may not be required in any particular program). Then you 
link the objects together with a framework. Instead of calling a module which 
updates a record with parameter data, you invoke the Object itself with the same 
parameters. This ensures data integrity - the only thing that changes an object 
is the object itself, through its calls. An object can then declare which changes 
it permits and which it doesn't - you may not be able to delete an object, for 
instance, if it's an audit object, and there won't be a method declared for that 
- it is impossible.


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 27)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-08T22:30:05+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000403.01816746@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <DC%Kb.51172$BA6.1062058@news20.bellglobal.com>`

```
Donald,

> If you simply do that, you gain arguement checking for all system stuff. 
> However, if you want to go further, you can.
>
And the advantage of doing this is...?

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 24)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-07T11:07:38+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ffb3229_4@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <u2oKb.4604$k_.554802@news20.bellglobal.com> <btf65b$hhj$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:btf65b$hhj$1@peabody.colorado.edu...
>
<snip>
>
> Changing how we think is hard.  Adding new commands to think the old way
is
> easy.

This is profound and accurate.

Nicely stated, Howard.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 18)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-01T19:30:54-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401011930.31c50ff8@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com> <3FF45886.5735321E@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote 

> Yes, and has nothing to do with OO or GUIs. You had better contact the U. of Bellingham
> ,Wa for an enhancement to Windows Explorer, (to get a file listing), 

Yes it is to do with GUIs, or specifically with the way MS chose to
implement their GUI and the whole of Windows.

They wanted to make commands lines as difficult as possible to get at
and use to make everyone use clicky-pointy things.

eg they hid DOSKEY away and didn't even mention that it could be used
to make the command line usable.

> or the 'Run' box. to recognize the old DOS commands..

It does, but you have to know what a command is.
 
>  From the desktop I tried Start--->Run----> "dir c:\ucs\1-bin\*.cpy > files.txt" ---->
> <Enter>  - replied, "Can't find program DIR".

That is because DIR is not a 'program', but a built-in command in
command.com.  You can do it with other file listing programs (usually
somewhat better) or with:

      "command /c dir c:\...  >files.txt
 
 
> As a rider - using the MS PWB Editor that came with MS COBOL versions 4 and 5 (re-badged
> MF V 3), within the Editor I can bring up a command line that let's me do "dir
> c:\ucs\1-bin\*.cpy > files.txt" - but again it's text not GUI.

That is a DOS program that is already running under a copy of
command.com as a DOS box.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 17)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-01T14:04:09-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401011404.10579cf1@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com> <3fea1d45_5@news.athenanews.com> <7f5ad04ce94262331a8bde1f53d2ba83@news.teranews.com> <590889dc0ffd0cdbe5cc4a6e3e2b0cb6@news.teranews.com> <3ff1fbcf_9@news.athenanews.com> <8377f8b9bdd2531fbc0c5c2c5c5c46ec@news.teranews.com> <3FF38C51.A3AE0361@shaw.ca> <b2e38a507e568e392a5247245d73c262@news.teranews.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote

> What I am asking for (with good
> reason) is *a series of manual steps I can do at the keyboard* to
…[3 more quoted lines elided]…
>     dir "d:\???0716*.*" /a/b >files.txt

Windows has a different approach to operating on files from the way
that you are asking for it to work.  This seems to indicate that
Windows is the wrong tool for how you want to work.  This is something
that I decided years ago, but fortunately I had been using
multi-user/multi-tasking systems since the late 70s and so had no need
for any of the 'good' stuff in Windows as compared to MS-DOS (ie
multi-tasking and networking).

You are illustrating another 'different' way of working.  In this case
you are wanting 'manual' control because you want to do it your way
rather than having some automatic mechanism choose how your gears
should be changed.
 
> That particular wildcard is only an example, in use it would vary. In fact,
> I believe it is essentially impossible to produce *any* 'text file consisting
> of a list of file names' by using the Windows GUI and the keyboard alone
> with no programming, wildcards or no.

> Creating a file of file names is a very useful
> thing that I do quite a lot. 

Perhaps you would be happier with, say, Linux where the whole shell
operation is based around such things as lists of files easily
generated.


> The reason I ask here is that, when I mentioned these as insufficiencies
> in the Windows GUI, Pete responded that it could be done, only I was
> using different methods. I'm not challenging Pete's comments, but it
> would be very useful to me if it can be done. So, can it be done, and
> how? I would really, really like to know. :-)

I recall back in the very early 80.  I had modified and compiled
'VFILE' to get it working on my Concurrent-CP/M system.  This worked
like a very early and crude version of the later 'XTree'. ie select
files then decide what to do with them.  Then along came 'FM' which I
was assured was the best of all things.  It had more features, more
functions, more everything.  But it worked by selecting the function
and _then_ picking the files to work on.  After 5 minutes I thought
'what a f**king stupid way to design a program' and threw it out.  To
me, Windows is mostly like that.

There seem to be those who like working in Windows, or an IDE, and may
have been happy to use FM. They work that way. It is not wrong, it is
just different. They may not see the point of creating a file containg
a list of files selected by particular criteria.  Their tools wouldn't
do anything useful with a list of files, they have different ways of
getting the job done.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-25T00:29:53+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000383.00fc775f@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <%x4Gb.463547$275.1354316@attbi_s53> <bc32a74c7d0fea9dc6ad89517ef5bd5d@news.teranews.com>`

```
Judson,

> Now, am I unique in that the experiences I have seen are only the rare
> exceptions?

No, they match mine as well. Having been Chief Architect reporting to 
the Strategy Manager for a large UK financial, I can report identical 
experiences.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-25T00:09:46+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3fe97460_2@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:b15f52de7cc255400373dfa35846ecab@news.teranews.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > But you are arguing with people who have no idea what they're talking
about,
> > have never been involved in successful OO implementation, do not
understand
> > the basic fundamentals, (witness Judson's post equating "iterative" to
> > "procedural"), and are resisting to the last ditch anything that looks
like
> > it might threaten their comfortable little world, predicated on "What we
> > know", "What we have always done", and "Best practice (as we perceive
…[8 more quoted lines elided]…
> argue simply from personal opinion, as you accuse others of doing.

All (non-academic) argument stems from personal opinion and there is nothing
wrong with that. I don't mind you having an opinion, I mind when you set it
up as Holy Writ.

And, for the last time, I DON'T CARE whether you use OO or not! I care that
you denigrate it from an uninformed position.

When you have actually implemented a true OO project, when you have
implemented ANY project that isn't governed by the "Waterfall",

I really have no idea why you would do this, but I respect your right to do
so.

To keep harping about how you will be persuaded by the statistics is just
sad. You won't be. Your mind is closed on it. I could show you sets of
statistics regarding OO, based on my own experience, both with my own
software development and on other commercial installations. It wouldn't make
a jot of difference, any more than I care about your statistics for the
"superiority" of Procedural Code. It is irrelevant to both of us, so there
is no point in continuing this discussion.

> Within 10 years after structured techniques were in use, I could have
> buried you under tons of such statistics in support of structured
> techniques. Structured techniques were clearly and decisively superior
> to previous techniques in every measurable way, except possibly in
> total lines of code. In fact, contrary to the trend we discuss,
significant
> such data was available BEFORE the push toward structured. Now,
> after much longer trials, I have yet to see any such objective data to
> confirm a wholesale move toward OO. Perhaps I've been overlooking
> it, so kindly point me to it. :-)
>

No, I absolutely agree with you on that. OO has been firmly rejected by the
COBOL establishment. I find that sad, but I am enough of a Realist to
recognize that such is the case.

However, If you look OUTSIDE COBOL, you find a completely different story.
The REST of the World accepts OO as necessary and fundamental for the
systems of tomorrow. So much so that the Operating systems, Network
software, and Web Scripting languages are ALL OO. It is taken as read, and
nobody outside of this forum would even bother to argue it whether it is
superior or not. (I am probably one of the last, and I am heartily sick of
it...<G>).

> Please note that none of the above involves "understanding the basic
> concepts", "resisting to the last ditch", threatening any "comfortable
> little world", or any "supposed knowledge".

Yes it does. It involves all of the above.  But, like I said, I really don't
care and this will be my last post on it.


> If OO is as good as you
> say, then fine, show me the statistical data to back it up, based on
> data obtained from real world projects.

Why? I DON'T CARE!!!

You have missed the whole point of my argument which is only incidentally
about the "superiority" of OO. My "defense" of OO is based on an attack on
it by someone who is unqualified to make such an attack.  You have never
learned it or used it, yet you can dismiss it due to lack of statistics
regarding its superiority, or the fact that most COBOL installations don't
use it, so it must be crap.

I believe the lack of uptake of OO by COBOL installations says more about
the people running such installations than it does about Object Oriented
Programming. I have run more than half a dozen successful pilot projects
using OO on sites that were "COBOL shops". Not one of them decided to move
to it, DESPITE the fact that their own programmers wanted to do so, DESPITE
the fact that there were measurable productivity gains, and DESPITE the fact
that all these projects were on-time and on-budget. (To be fair, they all
used RAD  type techniques for PM, as well as OO  for programming, and it is
very likely that the results were not just entirely because of OO.) In every
case the decisions to maintain the Staus Quo were based on politics. (One
Senior Manager admitted as much to me over a few beers.) I have no
complaints; I was well paid for what I did, but I still feel sorry no real
progress was made.

I don't hold you personally responsible for these problems, Judson, neither
am I venting my frustration on you<G>.  But I would sure like it a lot
better if you had actually worked with OO before you start slagging it off.

> Considering the truly vast
> expenditures in money and manpower that have been invested in a
…[3 more quoted lines elided]…
> nuts. :-)

I'm sure the rest of world will turn around one day and say: "Judson was
right. We are all nuts..."

Fortunately I'll be dead by then.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-29T14:30:32+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bspdq7$oui$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <3fe97460_2@news.athenanews.com>`

```

On 24-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> However, If you look OUTSIDE COBOL, you find a completely different story.
> The REST of the World accepts OO as necessary and fundamental for the
…[4 more quoted lines elided]…
> it...<G>).

Some needs are suited for OO, with high levels of interactivity.   Your examples
above are interactive.   Complicated examples such as Windows XP couldn't be
written any other way - but we have to expect that there are bugs that effect
more than their small portion of the code.

Most of these needs aren't suited for CoBOL, OO or not.


Some needs are suited for isolation of programs with low levels of
interactivity.

Those latter needs are often also suited for CoBOL.    Most of the interactivity
with CoBOL is by calling the same database.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-29T22:53:17+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<xf2Ib.25285$Pg1.14806@newsread1.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <3fe97460_2@news.athenanews.com> <bspdq7$oui$1@peabody.colorado.edu>`

```
Oh, really???

As Chuck would say when people think that "Mainframe"means "IBM mainframe" ...

How many PL/I sites/programmers (part of the "rest of the world) think that OO
is either "necessary or fundamental for the systems of tomorrow"?  For that
mater, how many RPG sites (still QUITE common in the OS/400 world) would agree
with this??? What about all those non-IBM mainframes?  There *might* be a TANDEM
OO solution (that I simply haven't heard of) - but I am pretty certain that OO
on HP mainframes is not seen as the "future".  Any comments from Unisys or DEC
(or any other part of HP)?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-30T12:49:29+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff0bdf8_4@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <3fe97460_2@news.athenanews.com> <bspdq7$oui$1@peabody.colorado.edu> <xf2Ib.25285$Pg1.14806@newsread1.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:xf2Ib.25285$Pg1.14806@newsread1.news.pas.earthlink.net...
> Oh, really???

Yes, really...<G>

>
> As Chuck would say when people think that "Mainframe"means "IBM mainframe"
...
>

NOT the same thing at all...

> How many PL/I sites/programmers (part of the "rest of the world) think
that OO
> is either "necessary or fundamental for the systems of tomorrow"?  For
that
> mater, how many RPG sites (still QUITE common in the OS/400 world) would
agree
> with this??? What about all those non-IBM mainframes?  There *might* be a
TANDEM
> OO solution (that I simply haven't heard of) - but I am pretty certain
that OO
> on HP mainframes is not seen as the "future".  Any comments from Unisys or
DEC
> (or any other part of HP)?
>

Come on, Bill. It's a bit thin isn't it?

What percentage of the "Rest of the World" would be represented by PL/1 or
RPG sites, in this day and age?

If the response to your post elicits more than 5% of ALL the sites that are
NOT COBOL, I'll stand corrected and withdraw my comment. (I'd then have to
modify it to "...95% of the Rest of the World" <G>).

Will you withdraw your objection if it doesn't <G>?

Are you seriously suggesting that OO WON'T sweep the board within the next
10 - 15 years?

(I am not including COBOL sites, as they were explicitly excluded from my
"rest of the world"...)

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T01:54:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231205422.11149.00001923@mb-m11.aol.com>`
- **References:** `<xf2Ib.25285$Pg1.14806@newsread1.news.pas.earthlink.net>`

```

"William M. Klein" wmklein@nospam.netcom.com 
Date: 12/29/03 5:53 PM EST
Message-id: <xf2Ib.25285$Pg1.14806@newsread1.news.pas.earthlink.net>

mulls 

<<

but I am pretty certain that OO
on HP mainframes is not seen as the "future".

>>

HP sees non mainframes as the future, and will finance that hope with any
surviving product line. There is plenty of OO on HP machines of the Intel
variety, and many HP small devices are encoded with OO strategies. HP
definitely has a future.  But it ain't mainframes.


Forgive me for taking things out of sequence but, the poster, to whom we are so
indebted for so many august contributions, asks in part ...

<< ...
How many PL/I sites/programmers (part of the "rest of the world) think that OO
is either "necessary or fundamental for the systems of tomorrow"? 

... >>

I am thinking, Bill, that  PL/1 folks are having no problem whatsoever with OO!
We are catching up with the data structures, and programatic paradigms that
they dream in at night. We are tardy.

PL/1 folks know some things about data instances, and multiple occurences. I am
on thin ice, but they have a thing called BASED data.  I may decent into the
chilly depths, but my hunch is they ain't intimidated hereabouts.


Best Wishes,
Bob Rayhawk
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-24T07:28:03-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<FFfGb.9678$d%1.1966673@news20.bellglobal.com>`
- **In-Reply-To:** `<b15f52de7cc255400373dfa35846ecab@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com>`

```
Judson McClendon wrote:

<a whole bunch>

Judson, I was going to respond, and will in the new year.

However, it is christamms eve, 7 in the morning, and my kids are coming 
home this evening. I am going to the store for butter and stuff, and 
plan on spending the day making cookies for them.  They be real pissed 
off if I did not.

Have a happy holiday, and with luck Santa will open your eyes to oop by 
the time it is over.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-24T08:13:03-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bsc3cv$gh9$1@panix1.panix.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <FFfGb.9678$d%1.1966673@news20.bellglobal.com>`

```
In article <FFfGb.9678$d%1.1966673@news20.bellglobal.com>,
Donald Tees  <donald_tees@nospam.sympatico.ca> wrote:

[snip]

>Have a happy holiday, and with luck Santa will open your eyes to oop by 
>the time it is over.

With all due respect, Mr Tees, it is this 'open your eyes' language which 
might make it difficult for some to deal with Object Oriented Programming.

Numbers speak for themselves (to those who are familiar with 
mathematics)... 'opening the eyes' is language reserved, quite 
frequently, for religious relevations.

In programming, according to my experience, religion is usually reserved 
for invocations like 'Oh *god*, please let this work!'

DD
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-24T08:14:45-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<vlgGb.9849$d%1.1989799@news20.bellglobal.com>`
- **In-Reply-To:** `<bsc3cv$gh9$1@panix1.panix.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <FFfGb.9678$d%1.1966673@news20.bellglobal.com> <bsc3cv$gh9$1@panix1.panix.com>`

```
docdwarf@panix.com wrote:
> In article <FFfGb.9678$d%1.1966673@news20.bellglobal.com>,
> Donald Tees  <donald_tees@nospam.sympatico.ca> wrote:
…[18 more quoted lines elided]…
> DD


Doc, go make some cookies, and I'll get back to you on Friday.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** docdwarf@panix.com
- **Date:** 2003-12-24T08:28:05-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bsc495$oto$1@panix1.panix.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <FFfGb.9678$d%1.1966673@news20.bellglobal.com> <bsc3cv$gh9$1@panix1.panix.com> <vlgGb.9849$d%1.1989799@news20.bellglobal.com>`

```
In article <vlgGb.9849$d%1.1989799@news20.bellglobal.com>,
Donald Tees  <donald_tees@nospam.sympatico.ca> wrote:
>docdwarf@panix.com wrote:
>> In article <FFfGb.9678$d%1.1966673@news20.bellglobal.com>,
…[21 more quoted lines elided]…
>Doc, go make some cookies, and I'll get back to you on Friday.

Your return will be eagerly awaited, Mr Tees... and your imperatives given 
all the consideration they deserve.

('Happy Holidays... and that's an *order*, soldier!')

DD
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** Habitant <berlutte@sympatico.ca>
- **Date:** 2003-12-24T16:05:48-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<pivjuv4148s319celrllje2iqhpp366k0c@4ax.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <3fe76bd1_6@news.athenanews.com> <b15f52de7cc255400373dfa35846ecab@news.teranews.com> <FFfGb.9678$d%1.1966673@news20.bellglobal.com> <bsc3cv$gh9$1@panix1.panix.com> <vlgGb.9849$d%1.1989799@news20.bellglobal.com>`

```
On Wed, 24 Dec 2003 08:14:45 -0500, Donald Tees
<donald_tees@nospam.sympatico.ca> wrote:

>Doc, go make some cookies, and I'll get back to you on Friday.

I have urged him fer ages to fly some kites along the Cheese-a-Peak's
shores. 

To no avail obviously!
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-23T17:35:27+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8c4fc40322b80ab862b4248ce69c7bb9@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> I remember similar resistance to Djykstra's paper when it was first
> published..."What?! The whole of computer programming can be resolved down
> to THREE operations?!!! Rubbish!!".

Which paper is that? Dijkstra's famous "Go To Statement Considered
Harmful" paper? It was Alan Turing, IIRC, that defined the minimum
necessary instructions for computability.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2003-12-23T19:39:52+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<cS0Gb.231852$Ec1.8204762@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <8c4fc40322b80ab862b4248ce69c7bb9@news.teranews.com>`

```

Judson McClendon <judmc@sunvaley0.com> wrote in message news:8c4fc40322b80ab862b4248ce69c7bb9@news.teranews.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
…[6 more quoted lines elided]…
> necessary instructions for computability.

A bare minimum instruction set would contain
addition, branching, store and load operations,
all written in an eight-instruction Turing-complete
programming language called Brainfuck.

http://www.muppetlabs.com/~breadbox/bf/
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** cristofd@hevanet.com (Daniel.)
- **Date:** 2003-12-27T02:30:09-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<474b22da.0312270230.21d45a01@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <8c4fc40322b80ab862b4248ce69c7bb9@news.teranews.com> <cS0Gb.231852$Ec1.8204762@bgtnsc05-news.ops.worldnet.att.net>`

```
"Hugh Candlin" <no@spam.com> wrote in message news:<cS0Gb.231852$Ec1.8204762@bgtnsc05-news.ops.worldnet.att.net>...
> Judson McClendon <judmc@sunvaley0.com> wrote in message news:8c4fc40322b80ab862b4248ce69c7bb9@news.teranews.com...
> > "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
…[14 more quoted lines elided]…
> http://www.muppetlabs.com/~breadbox/bf/

...which uses only two of the three "bare minimum" control structures
mentioned: sequencing and iteration. You can synthesize selection out
of iteration.
-Daniel Cristofani.
 >>>++[<++++++++[<[<++>-]>>[>>]+>>+[-[->>+<<<[<[<<]<+>]>[>[>>]]]<[>>[-]]>[>[-
 <<]+<[<+<]]+<<]<[>+<-]>>-]<.[-]>>]http://www.hevanet.com/cristofd/brainfuck/
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-25T00:33:45+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3fe979fc_6@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <8c4fc40322b80ab862b4248ce69c7bb9@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:8c4fc40322b80ab862b4248ce69c7bb9@news.teranews.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > I remember similar resistance to Djykstra's paper when it was first
> > published..."What?! The whole of computer programming can be resolved
down
> > to THREE operations?!!! Rubbish!!".
>
> Which paper is that? Dijkstra's famous "Go To Statement Considered
> Harmful" paper? It was Alan Turing, IIRC, that defined the minimum
> necessary instructions for computability.

No, I was confused.  It was Boehm & Jacopini's paper in 1966 that
established the three operations I was referring to . My confusion arose
because they also did some work on "GOTO-less" programming at around the
same time as Dijkstra. That was what I recalled and incorrectly assigned to
Dijkstra.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-25T23:30:08+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000387.0376cab3@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com>`

```
Peter,

> But you are arguing with people who have no idea what they're talking about,
> have never been involved in successful OO implementation, do not understand
> the basic fundamentals

And I don't need you to tell me what sort of experience I've got. I HAVE 
implemented OO using C++ and Java. I went through the "Paradigm shift" and 
learned how to think through the implications. Encapsulation is a great idea, 
but it pre-dates OO by many years, loose coupling similarly comes from 
structured programming/design.

OO is useful as an approach to implementation, but it doesn't perform 
miracles. Good design can be done in both OO and structured approaches. My 
complaint was that, within OO, particularly when using C++, side-effects 
become sanctified rather than frowned on, making maintenance and fault finding 
difficult because it works against encapsulation.

I've never implemented OO using Cobol, that's true. But the constructs seem to 
me to be an  effective way of doing OO if that's what you want to do. But the 
fundamental disjunction of an OO model and an E/R implementation remains. For 
straight commercial data processing, procedural code works fine - and it's 
quick in execution.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-28T08:28:28+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3fedddc6_2@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org>`

```

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.00000387.0376cab3@ieee.org...
> Peter,
>
> > But you are arguing with people who have no idea what they're talking
about,
> > have never been involved in successful OO implementation, do not
understand
> > the basic fundamentals
>
> And I don't need you to tell me what sort of experience I've got. I HAVE
> implemented OO using C++ and Java.

OK, was your OO implementation successful?


> I went through the "Paradigm shift" and
> learned how to think through the implications. Encapsulation is a great
idea,
> but it pre-dates OO by many years, loose coupling similarly comes from
> structured programming/design.
…[4 more quoted lines elided]…
> become sanctified rather than frowned on, making maintenance and fault
finding
> difficult because it works against encapsulation.
>

Then the way in which the OO is being implemented needs to be reviewed.

> I've never implemented OO using Cobol, that's true. But the constructs
seem to
> me to be an  effective way of doing OO if that's what you want to do. But
the
> fundamental disjunction of an OO model and an E/R implementation remains.
For
> straight commercial data processing, procedural code works fine - and it's
> quick in execution.

Yes, I agree, if by "straight commercial data processing" you mean Batch.

I can't argue that one because it is axiomatic. (And has been so for the
last 40 years...<G>)

Unfortunately, I never intended to argue that OO is perfect, but I do
believe it is the best approach we have.

I use OO COBOL to build commercial components and I find it "perfect" for
this particular task.

I further believe that component based design and implementation is the way
for software development for the future, and THAT is why I support OO.

BTW, my comments were not intended to be personal or specific to any
individual (that's why I used the term "people", rather than "Doug Scott");
if I offended you, I'm sorry. Please understand I have been defending this
position here for the last four years and, frankly, I'm tired of it. I guess
my frustration is starting to show...<G>)

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-27T22:30:16+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000391.0304c1f1@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com>`

```
Peter,

> For
> > straight commercial data processing, procedural code works fine - and it's
> > quick in execution.
> 
> Yes, I agree, if by "straight commercial data processing" you mean Batch.

> I can't argue that one because it is axiomatic. (And has been so for the
> last 40 years...<G>)

Actually, I didn't only mean batch. Event-driven procedural code is not 
unknown. And there have been attempts at batch OO. Not entirely successful, it 
must be said, but the guys learned a lot :-)

> I use OO COBOL to build commercial components and I find it "perfect" for
> this particular task.

I believe OO Cobol avoids some of the criticisms I have, but I haven't 
implemented anything using it.

> BTW, my comments were not intended to be personal or specific to any
> individual (that's why I used the term "people", rather than "Doug Scott");


Ah well, the original comment was a rather broad dismissal following a post 
I'd made. And since I'm included by what I posted, then I do have an interest 
in replying.

> if I offended you, I'm sorry.

Nah, it takes much more than that :-)



---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-27T22:30:17+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.00000392.0304c6c1@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com>`

```
Peter,

> OK, was your OO implementation successful?

Yes, it was, but it needed a whole lot of resources, and the programmers 
had difficulty debugging it because of the massive infrastructure - they 
didn't quite understand what the system was doing and why it was going 
wrong. The abstraction provided by OO was fine for modelling, but got in 
the way of problem determination. A  lot of programmers aren't good at 
debugging anyway, and OO made it worse.

> Then the way in which the OO is being implemented needs to be reviewed.

Oh dear. I detect religious conviction here. No point in continuing. 

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-12-29T00:43:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031228194319.19959.00001142@mb-m01.aol.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org>`

```

In mid-thread responding to a questiong 


Doug Scott dwscott@ieee.org 
Date: 12/27/03 5:30 PM EST
Message-id: <VA.00000392.0304c6c1@ieee.org>


makes a powerful point ...

<<

> OK, was your OO implementation successful?

Yes, it was, but it needed a whole lot of resources, and the programmers 
had difficulty debugging it because of the massive infrastructure - they 
didn't quite understand what the system was doing and why it was going 
wrong. The abstraction provided by OO was fine for modelling, but got in 
the way of problem determination. A  lot of programmers aren't good at 
debugging anyway, and OO made it worse.


>>

It is not unusual for Dough Scott to publish more than one nugget of wisdom at
once. But this phrasing really struck me as very sage.

I can transform it to other words, and I do not mean to put words in his mouth.
So this is more of a set of question.  

If we have succeeded by encapsulating, then are we not failing by
encapsulating?  Debugging is where you try to find IT. If  IT is inside of a
capsule then IT may be harder to find.  If it is inside of a capsule that is
inside of a capsule the is inside of a very heavily inherited Matroshka Doll,
is it not that much more difficult to find IT?  Are we not making things
difficult to find by encapsulating them, be IT a data specification or a data
manipulation?

Aliasing of things is also a problem in debugging in final system exercises
during development and debugging under pressure in production. Polymorphism is
so utterly subtle and flexible that it seems beyond reproach. Yet rather than
your name or my name, the polymorphic name is an _anyName_ that might be
invoking _anyVariation_ of a routine and we are not sure which.

Debugging challenges are an excellent vista from which to review the plusses
and minuses of a new technology.

Is there not something about Flatlander COBOL that tended to relegate
abstraction to the design process and keep it out of the coding process?  This
surmise is as hard to put into words as an explanation of the new technology,
yet somehow it is true.  The old old old COBOL capabilities (or limitations if
you want to use that word, it would be okay too), lead the last portion of
system and program design processes to be rather non abstract in the
recordation at pseudo code and actual programms.  But I am not sure just
exactly why.

it seems like the new stuff allows the designer to remain cerebral right into
the edit session of the program coding. That is why it is powerful, and
probably has something to do with why that which is left behind is harder to
transfer to the next person, (that is, it does not sell well, even if it flies
like a bat out of heaven).

Best Wishes,
Bob Rayhawk
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-12-28T20:51:25-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vuv5lu7bq1122f@corp.supernews.com>`
- **In-Reply-To:** `<20031228194319.19959.00001142@mb-m01.aol.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com>`

```
RKRayhawk wrote:

>>>OK, was your OO implementation successful?
>> 
…[19 more quoted lines elided]…
> manipulation?

This is why component-based software engineering (CBSE) is, I believe, 
what will subsume both structured and object-oriented.  Researchers, 
professors, scientists, and other academics are defining this (CBSE) as 
an engineering discipline, just as civil or electrical engineering 
would.  These components do very little in and of themselves.

Take civil engineering, for example.  A brick does very little.  A piece 
of rebar does very little.  Mortar does very little.  All these object 
are pretty lame by themselves.  But, when the proper architecture, 
design, and structured process in applied to tie these components 
together, you get houses and skyscrapers and bridges and roads; all very 
different, but made from the same humble components.

CBSE is the key to simplifying the whole structured vs. OO debate - and, 
in CBSE, there's room for experts in both.  A component is very simple. 
  For example, Pete Dashwood has one out on aboutlegacycoding.com that 
you can download, install, and play with - it takes a string, parses it 
to a number, tells you if it is a number or not, and returns it in 5 or 
6 different formats.  It's very simple - not much to it, but it could be 
very valuable functionality.

If I need this functionality in my program, I've already got it.  It 
doesn't matter if I'm writing in COBOL, C, ForTran, Java - all I have to 
do is instantiate it (an OO term, but not an OO-type instantiation - 
it's more like a call).  This doesn't obscure things within 
ever-increasing layers of complicated inheritance.  The larger the 
system, the more complex a purely OO design will be.  CBSE allows you to 
create objects, wrap them with a standard interface (just as standard 
bricks are 90-degree cornered rectangles), and utilize them within a 
structured process.

Structured works well because it is fairly intuitive - stepping through 
a process is the way business works.  By using simple, reliable, 
easily-tested components, you get the benefits of OO with the simplicity 
of structured.

(I'm reading a great book about CBSE - this is some of the stuff just 
from the first chapter.  I'm trying to incorporate this as much as I 
can, as I believe it's the key to allowing our current static mainframe 
system to become more agile, flexible to customer change requests, and 
standardize many of our disparate processes.  No man is an island, but 
I'm doing what I can...)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T16:05:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5839a628f9762d542fde0617c64c4412@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com>`

```
"LX-i" <lxi0007@netscape.net> wrote:
>
> This is why component-based software engineering (CBSE) is, I believe,
…[3 more quoted lines elided]…
> would.  These components do very little in and of themselves.

Pardon me, but I think this misses the point. In a procedural system, if
the supplied functions to access data fail, it can be relatively easy to
code around, because the data behind the functions isn't completely
hidden. But when you completely encapsulate that data into an 'object',
and you have a supplied component fail (it may be purchased and
inaccessible), or you need to access the data in a way not supported
by the supplied methods, you are up the creek without a paddle.
Programming around the problem can be extremely difficult, even
impossible. Wearing seat belts can protect vehicle passengers in an
accident. But if the vehicle goes into water or catches on fire, a
seatbelt that won't unlock can kill you. But such simple locks can be
made very reliable, pretty close to foolproof. Now, what if you force
passengers to wear well secured straight jackets? You might save
more lives sometimes, but you are certainly going to cause so many
problems that it would never be accepted. Extreme encapsulation
can do the same thing. For any good thing, there is a point of
diminishing return, beyond which more of it becomes bad. This is
true for data encapsulation, logical abstraction, or anywhere else. It
is not just knowing the rules, it is also knowing when you can and
must break them. Because no rule ever made by man is perfect, and
there are times for any such rule when it cannot be applied, or
perhaps, further applied, to benefit.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-30T11:49:43+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff0aff8$1_1@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:5839a628f9762d542fde0617c64c4412@news.teranews.com...
> "LX-i" <lxi0007@netscape.net> wrote:
> >
…[12 more quoted lines elided]…
> by the supplied methods, you are up the creek without a paddle.

No, you are simply used the WRONG component.

You select components based on their specified Properties, Methods, and
Events. You know BEFORE you implement them WHAT they will do. (You may never
know HOW they do it, any more than you may know the intimate details of
exactly HOW electricity is delivered to your house.(Does it affect the use
of it, if it was generated from a wind farm, a nuclear  plant, a geothermal
bore, a hydro dam, or a solar panel?)).

I have used third party components for over four years now and NEVER had one
fail. They do what they are specified to do, just as a brick does what it is
specified to do. On one occasion I requested an extension to the existing
functionality of a particular Method. The writer gave it to me within 2 days
and never charged for it as he said it "enhanced the marketability" of his
component.

To procedural programmers the idea of not being able to maintain code is
anathema. It requires a large mental adjustment to get over the "not invente
d here" syndrome and trust other people's work as you trust your own. Yet
the benefits of doing so are manifold.

I have one lifetime. I do not expect to become expert in EVERY field of
endeavour which I may need to draw upon in order to create useful computer
systems. By using previously debugged and tested encapsulated components I
can not only obtain the functionality I require, I can get it "in spades"...
Very often a given component (which may be provided by someone who has spent
say, 20 years, in a particular area of specialist expertise) will provide
facilites (Methods and Properties) that I could never have envisaged. I
don't HAVE to use these facilities but it is  nice to know they are there if
I want them (now or later...).

It is you, Judson, who have missed the point. The point is that encapsulated
components can provide functionality that does NOT REQUIRE
maintenance...ever. If the system requirements change radically, the
component may be replaced; it is seldom modified (in the case of third party
components you don't have the source code, and probably neither know nor
care what it is written in anyway, so you COULDN'T maintain it.)

The reason these components can provide such fail safe functionality is
because they ARE encapsulated and nobody gets to mess with them. In other
words, they are stable and their capabilities are KNOWN.

(This is a foreign and alarming concept to most procedural programmers, who
are orking in an environment where things require "maintenance" every
day...)

Guess which one is most cost effective?

> Programming around the problem can be extremely difficult, even
> impossible.

Not in my experience.

>Wearing seat belts can protect vehicle passengers in an
> accident. But if the vehicle goes into water or catches on fire, a
…[5 more quoted lines elided]…
> can do the same thing.

The above is such total rubbish that I won't dignify it by refuting it.

> For any good thing, there is a point of
> diminishing return, beyond which more of it becomes bad.

What about sex and drugs and Rock 'n' Roll <G>?

>This is
> true for data encapsulation, logical abstraction, or anywhere else. It
…[3 more quoted lines elided]…
> perhaps, further applied, to benefit.

Hmmmm...food for thought there...

Here's a rule, made by man, which can be applied without exception and is
always true...

"A fart in a bottle can never be rattled."

Here's another one...

"If you hang your arse out the window, you cannot go down the street and
throw stones at it."

Finally...

"Beware of people who tell you rules are made to be broken, and should be,
but only when THEY say so."

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-12-29T17:58:11-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vv1fta7dc7q6f6@corp.supernews.com>`
- **In-Reply-To:** `<5839a628f9762d542fde0617c64c4412@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com>`

```
Judson McClendon wrote:
> "LX-i" <lxi0007@netscape.net> wrote:
> 
…[15 more quoted lines elided]…
> impossible.

That's why you make the compenents do very little.  How many times do 
contractors have a broken brick?  I'm not saying it's as exact a science 
as brickmaking, but it can approach that.  If you find that this 
component does not do what you want it to do, you write or acquire one 
that will.  With each component containing limited functionality, you're 
going to be writing very much, even if you rewrite the whole thing.

> Wearing seat belts can protect vehicle passengers in an
> accident. But if the vehicle goes into water or catches on fire, a
> seatbelt that won't unlock can kill you. But such simple locks can be
> made very reliable, pretty close to foolproof.

Do you not envision a world where such precision is possible?  Look at 
textbook COBOL exercises.  These examples are so simple that a novice 
programmer can code them (assuming they actually try, etc.).  I'm not 
advocating taking a complex system and wrapping it as a component - I'm 
advocating breaking it up into little pieces, eliminating redundancy, 
and have a complex structured system that uses common functionality.

> Now, what if you force
> passengers to wear well secured straight jackets? You might save
…[8 more quoted lines elided]…
> perhaps, further applied, to benefit.

Are you saying CBSE isn't worth it?  A DLL can be a component - you swap 
out the common code, and you don't have to risk opening up a whole lot 
more code to get the new functionality.  I don't see how that's a bad thing.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-30T21:31:15+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff13844_1@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message
news:vv1fta7dc7q6f6@corp.supernews.com...
> Judson McClendon wrote:
> > "LX-i" <lxi0007@netscape.net> wrote:
…[51 more quoted lines elided]…
> more code to get the new functionality.  I don't see how that's a bad
thing.
>
>

I don't either, Daniel.

(I was starting to think it must be me...<G>)

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-30T12:58:55+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7fad810b0239beb065fe81158c0869f0@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com> <3ff13844_1@news.athenanews.com>`

```
Now I can clearly see why you fellows don't see the potential problems
with OO! You are so optimistic that you don't visualize how your OO
scenarios can break down. You assume you can always obtain a working
component if the one you purchased for the project fails to work properly,
halfway into implementation. And you assume that you can envision, to
the minutest detail, every pitfall that could possibly happen before you
begin coding. If you can do that, your skills are truly breathtaking. I can't
come close to doing either of those things. Perhaps that's why I am much
more pessimistic, and believe those things do happen, in spite of our (my)
best efforts. I suppose I just don't like putting all my eggs in a basket that
I can't keep from breaking because someone else created and maintains it,
and if it does break, I can't fix it because I can't get to what's behind it.
Perhaps I am simply insecure, but I really, really hate, and avoid like the
plague, anything smelling of an "I can't get there from here" situation. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 16)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-30T16:32:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lcmIb.5849$Vl6.1492181@news20.bellglobal.com>`
- **In-Reply-To:** `<7fad810b0239beb065fe81158c0869f0@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com> <3ff13844_1@news.athenanews.com> <7fad810b0239beb065fe81158c0869f0@news.teranews.com>`

```
Judson McClendon wrote:
> Now I can clearly see why you fellows don't see the potential problems
> with OO! You are so optimistic that you don't visualize how your OO
…[11 more quoted lines elided]…
> plague, anything smelling of an "I can't get there from here" situation. :-)

How is that different from *any* purchased package, OOP or not?  I just 
finished using an OCX object to add faxing capabilities to an 
established package.  The points you note would have been true 
regardless of whether it had been OOP or subroutine calls, and I can 
code around the problems in the same manner regardless of whether it is 
an OCX or a DLL with subroutine calls.

All the fact that it is "OOP" does is standardize the methodology. I 
cannot really see that as a detriment.

Or are you proposing that a Cobol coder should NEVER buy software, and 
always code everything from the binary level up?

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-31T12:05:35+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff2052f_3@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com> <3ff13844_1@news.athenanews.com> <7fad810b0239beb065fe81158c0869f0@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:7fad810b0239beb065fe81158c0869f0@news.teranews.com...
> Now I can clearly see why you fellows don't see the potential problems
> with OO! You are so optimistic that you don't visualize how your OO
> scenarios can break down.

Yes, I prefer to be an optimist than the alternative.

I also find it is not conducive to success, to visualise failure from day
one.

>You assume you can always obtain a working
> component if the one you purchased for the project fails to work properly,
> halfway into implementation.

You're pretending to be dumb, right?

Every third party component is tested for compliance with its spec. when it
is delivered, and it is delivered (on approval)  long BEFORE
"implementation" or even development has begun. We are satisfied that the
components do what they are supposed to, BEFORE we deploy them. The system
design knows what functionality is required; checking that any third party
components meet these criteria is simply routine.


>And you assume that you can envision, to
> the minutest detail, every pitfall that could possibly happen before you
> begin coding. If you can do that, your skills are truly breathtaking.

Yep. Hadn't thought about it like that but I guess it IS pretty
outstanding...<G>

The fact is you don't need to do that because the development process (at
least on the projects I manage) is ITERATIVE. We don't expect to have
EVERYTHING working, "every pitfall" covered, or even normal error exits in
place on the first cut. We simply need to establish the mainline
functionality. Once that is done the process iterates towards other
prioritized goals. All development is timeboxed so it can never slip, and
all timeboxes are required to produce prioritized deliverables (goals)
(these can change by agreement, even during development, but it is limited
by the timebox). I have described the whole process at length elsewhere and
have no intention of doing so again here (besides, it is WAY beyond the
scope of this forum). Suffice to say, I do NOT advocate "waterfall"
development, where the bogeys you raise are very real indeed and DO
contribute to project failure.


>I can't
> come close to doing either of those things. Perhaps that's why I am much
> more pessimistic, and believe those things do happen, in spite of our (my)
> best efforts. I suppose I just don't like putting all my eggs in a basket
that
> I can't keep from breaking because someone else created and maintains it,
> and if it does break, I can't fix it because I can't get to what's behind
it.

So the only programmer you have faith in is yourself? I understand it, but I
don't agree with it. Guess it comes down to personalities in the end.

> Perhaps I am simply insecure, but I really, really hate, and avoid like
the
> plague, anything smelling of an "I can't get there from here" situation.
:-)

Sometimes if you "can't get there from here" it is because you can't think
outside the road you are on.

Tried cutting across the fields, for instance?

Us optimists are confident that we can ALWAYS "get there from here" because
we planned several strategies to do so before we left home. Even if the
unthinkable happened and ALL of these strategies were curtailed, we have
such confidence we KNOW we can deal with whatever arises.

I have NEVER (in 38 years) been in a situation where everything had to stop
because of an unforeseen problem... (apart from things like suppliers not
being able to deliver disk drives in the required timeframes, after saying
they could, and stuff like that...Never because of oversight in system or
program design.). "Fall back" positions are a standard part of system
design, or they should be...

I DO believe in spending time on design (no matter WHAT the Management
pressure to "produce") and I DO believe in "paper models" of systems and
subsystems that are seen to work with identified objects and properties long
before we start coding. Not being constrained by the waterfall (and its
consequent required progressive sign offs), coding is NOT a separate "phase"
of development and users are involved on a regular basis to check that what
we have is what they need (NOW, not three months ago during "Requirements
Gathering"). If they see flaws that are serious we all re-prioritize and fix
(recode) them, within the constraints of the timebox.

It works. But, like OO, it is completely foreign to your experience.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 17)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-31T19:50:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<4f79b6af993f34689866d469c165469b@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com> <3ff13844_1@news.athenanews.com> <7fad810b0239beb065fe81158c0869f0@news.teranews.com> <3ff2052f_3@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> >I suppose I just don't like putting all my eggs in a basket that
…[4 more quoted lines elided]…
> don't agree with it. Guess it comes down to personalities in the end.

I make mistakes too. But if I made the mistake, I can fix it. If someone else
made the mistake, and I can't get them to fix it, and I can't code around it
(it is object code, and I can't get to the data directly), I am screwed. :-)

> > Perhaps I am simply insecure, but I really, really hate, and avoid like the
> > plague, anything smelling of an "I can't get there from here" situation. :-)
>
> Sometimes if you "can't get there from here" it is because you can't think
> outside the road you are on.

No, it's because you weren't cautious enough to avoid the road at the start. ;-)

By "can't get there from here" I didn't mean you can never, ever get there
under any circumstances. I meant that you have, by relying on components
that you cannot fix, and that inhibit you easily coding around them, made
yourself vulnerable to being put in a situation that cannot be corrected
within satisfactory time and monetary constraints. Yes, you can always
get it done eventually. But when payroll blows, you don't have unlimited
time to fix it. :-)  Just because it hasn't happened to you does not mean
that it cannot happen. You may just be very lucky. :-)

Reminds me of a call I received once. It was a man I had never heard of,
the manager of a small, one man IS department, and he was frantic to the
point of a nervous breakdown. He had been processing for over 20 years
without doing backups, and never lost any data. Someone suggested that
he should start backing up, so he did. Unfortunately, on his first attempt
he copied in the wrong direction and overwrote all his data. Sorry, but
you can't get there from here. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 18)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-01T14:01:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff371d9_1@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com> <3ff13844_1@news.athenanews.com> <7fad810b0239beb065fe81158c0869f0@news.teranews.com> <3ff2052f_3@news.athenanews.com> <4f79b6af993f34689866d469c165469b@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:4f79b6af993f34689866d469c165469b@news.teranews.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> > "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > >I suppose I just don't like putting all my eggs in a basket that
> > > I can't keep from breaking because someone else created and maintains
it,
> > > and if it does break, I can't fix it because I can't get to what's
behind it.
> >
> > So the only programmer you have faith in is yourself? I understand it,
but I
> > don't agree with it. Guess it comes down to personalities in the end.
>
> I make mistakes too. But if I made the mistake, I can fix it. If someone
else
> made the mistake, and I can't get them to fix it, and I can't code around
it
> (it is object code, and I can't get to the data directly), I am screwed.
:-)
>

But you don't need to place yourself in that situation in order to develop
component based systems.

> > > Perhaps I am simply insecure, but I really, really hate, and avoid
like the
> > > plague, anything smelling of an "I can't get there from here"
situation. :-)
> >
> > Sometimes if you "can't get there from here" it is because you can't
think
> > outside the road you are on.
>
> No, it's because you weren't cautious enough to avoid the road at the
start. ;-)
>
> By "can't get there from here" I didn't mean you can never, ever get there
…[3 more quoted lines elided]…
> within satisfactory time and monetary constraints.

This indicates that you either haven't read, or chose to ignore my previous
post. There IS no such vulnerability. It is in YOUR head and your
insecurity.

You rely on components you had no control in the manufacture of, every time
you drive your car. Yet you consider the "risk" of failure to be acceptable
enough that you will take your wife and kids in the vehicle.

Why is software any different?

Because you have a background of solving software problems that were caused
by program errors in programs written by other people. (Your own code, of
course, is beyond reproach and thoroughly trustworthy...<G>).

Even with the methodologies used to trap and repair bugs before software is
deployed, you are still suspicious and distrusting.
(Actually, you have every right to be...the usual waterfall methodology
simply doesn't do what it should and it is no wonder that computer systems
developed with it are regarded with suspicion...)

I completely understand that you will have difficulty in embracing a system
where I am saying: "Trust this. We have checked it out and it works.".

(I wouldn't mind betting you've never crowd surfed at a rock concert,
either, right <G>.)

Unless you are able to make a complete shift in your current thinking you
will never successfully implement component based systems. As these systems
are for the most part predicated on OO, you will never accept that either.

There is nothing wrong with you having the attitudes you do, your world
works for you, and it would be a sad world if we all agreed on everything.
But there is little point in pursuing this discussion.

>Yes, you can always
> get it done eventually. But when payroll blows, you don't have unlimited
> time to fix it. :-)  Just because it hasn't happened to you does not mean
> that it cannot happen. You may just be very lucky. :-)
>

Believe it or not, but there IS a world where Payroll DOESN'T blow. It just
goes on, week after week, month after month, year after year, doing
precisely what it is specified to do. Never fails, never chokes, all its
component parts passing information and processing it, exactly as they were
designed to do, with NOBODY doing any messing with it. (Maybe some
re-configuration for new tax tables, or deductions, carried out by users who
understand Payroll, even if they don't have indepth knowledge of hexadecimal
or computer programming.)

Has it ever occurred to you that one of the reasons systems need "ongoing
maintenance" is because the system has received "ongoing maintenance"
throughout its lifetime from a variety of programmers who were told to "Fix
it, NOW!!"?

I was surprised that some of the early component based systems I produced
seemed to need far less maintenance than their procedural predecessors; then
I realized it is because a large proportion of the actual code is NOT
accessible and CANNOT be "tinkered" with. This tends to focus whatever
maintenance IS required into areas where it can be readily reversed or
amended.

As for me being very lucky, I am reminded of a comment my ex-wife once made
when someone said: "It's all right for you , Pete, you just walk in the sun.
I wish I had your luck."  She fixed him with her baby blues and remarked:
"Yes, it is amazing how lucky he gets when he works hard...".

(That same hard work was a serious contributing factor to the breakdown of
the marriage, but that's another story...)

> Reminds me of a call I received once. It was a man I had never heard of,
> the manager of a small, one man IS department, and he was frantic to the
…[4 more quoted lines elided]…
> you can't get there from here. :-)

Yes you can. You rebuild the system from its last known state, using hard
copy.

Tedious, but possible. (Because it is not an IT solution, this one often
gets overlooked...)

Of course, us IT professionals wouldn't be in that situation in the first
place...<G>

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 19)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T10:14:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<fa069a3ad4c04b29089e74823a2d90fe@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com> <3ff13844_1@news.athenanews.com> <7fad810b0239beb065fe81158c0869f0@news.teranews.com> <3ff2052f_3@news.athenanews.com> <4f79b6af993f34689866d469c165469b@news.teranews.com> <3ff371d9_1@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> Believe it or not, but there IS a world where Payroll DOESN'T blow. It just
…[6 more quoted lines elided]…
> or computer programming.)

Yes, I know, this is the world I live in. It is unusual for me to get more
than one bug call per year, and usually not even one. I have had two in
the last four years, and both were from code written by others. I have
gone several years in a row with none. After I deliver the first new
system for a new client, it never fails to provoke surprised, even amazed,
comments from the client that it worked correctly, right out of the gate.
Once a system has been running for a few weeks, my clients only call me
for changes or something new, with questions, or to chat. Never once
have I received a complaint that anything I ever wrote was less than what
the client wanted. A typical comment I receive, surprisingly almost word
for word the same every time, is "You took what I asked for and made it
better." You don't have to take my word for this, I'll be happy to supply
the names of every client I have ever had and you can ask them. This is
also why, in over 23 years of consulting, I have only approached potential
clients twice, both times on invitation from others. The result of both was
long term clients. I do not advertise and my business phone number is
unlisted. Every other client has approached me because they heard about
my work by word of mouth, and it's been many years since I earned less
than six figures, net. But it didn't get that way because I casually assumed
everything would work the way it should. It got that way, at least in part,
because I worked very hard to make it happen, and because I took nothing
for granted, or left anything to chance, that I could avoid. It is what I see
when others don't do it this way that prompted my comments. :-)

> > Reminds me of a call I received once. It was a man I had never heard of,
> > the manager of a small, one man IS department, and he was frantic to the
…[10 more quoted lines elided]…
> gets overlooked...)

That's precisely what I told him to do. But for the days or weeks that it took
to get it done, their computer system was of no use to them, and it must have
cost a fortune to do it, and the errors introduced by that much off-the-cuff,
unanticipated data entry undoubtedly caused lots of ongoing problems.
There is no way that company 'got there' (where they wanted to be, running
the next day) 'from here' (where they were, with no online data). I call this
a preventable failure, not quite total failure, but failure nonetheless. And if
it took so long to recover the data that the company went out of business, it
was a total failure. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 19)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-02T15:57:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bt44cq$l90$1@peabody.colorado.edu>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <5839a628f9762d542fde0617c64c4412@news.teranews.com> <vv1fta7dc7q6f6@corp.supernews.com> <3ff13844_1@news.athenanews.com> <7fad810b0239beb065fe81158c0869f0@news.teranews.com> <3ff2052f_3@news.athenanews.com> <4f79b6af993f34689866d469c165469b@news.teranews.com> <3ff371d9_1@news.athenanews.com>`

```

On 31-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> Believe it or not, but there IS a world where Payroll DOESN'T blow. It just
> goes on, week after week, month after month, year after year, doing
…[10 more quoted lines elided]…
> it, NOW!!"?

The primary reason the Payroll Program needs ongoing maintenance is because
business rules change.   Think of anything to do with the Tax Code.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-30T12:38:40+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff0bb75_8@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message
news:vuv5lu7bq1122f@corp.supernews.com...
> RKRayhawk wrote:
>
> >>>OK, was your OO implementation successful?
> >>
> >> Yes, it was, but it needed a whole lot of resources, and the
programmers
> >> had difficulty debugging it because of the massive infrastructure -
they
> >> didn't quite understand what the system was doing and why it was going
> >> wrong. The abstraction provided by OO was fine for modelling, but got
in
> >> the way of problem determination. A  lot of programmers aren't good at
> >> debugging anyway, and OO made it worse.
> >
> > It is not unusual for Dough Scott to publish more than one nugget of
wisdom at
> > once. But this phrasing really struck me as very sage.
> >
> > I can transform it to other words, and I do not mean to put words in his
mouth.
> > So this is more of a set of question.
> >
> > If we have succeeded by encapsulating, then are we not failing by
> > encapsulating?  Debugging is where you try to find IT. If  IT is inside
of a
> > capsule then IT may be harder to find.  If it is inside of a capsule
that is
> > inside of a capsule the is inside of a very heavily inherited Matroshka
Doll,
> > is it not that much more difficult to find IT?  Are we not making things
> > difficult to find by encapsulating them, be IT a data specification or a
data
> > manipulation?
>
…[5 more quoted lines elided]…
>

This is exactly my position also. I see OO as a necessary prerequisite to
build components; not as an end in itself.

> Take civil engineering, for example.  A brick does very little.  A piece
> of rebar does very little.  Mortar does very little.  All these object
…[22 more quoted lines elided]…
>

Yes, this is a very important capability of components; they can be used in
both procedural and OO programming, or even web scripting.

> Structured works well because it is fairly intuitive - stepping through
> a process is the way business works.  By using simple, reliable,
…[9 more quoted lines elided]…
>

I was encouraged by this post, Daniel. You have obviously seized the
essential ideas of component technology and been able to apply them to your
particular environment. (If anything I said anywhere influenced this, then I
consider my time well spent...<G>)

Pete.



>
> -- 
…[9 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-12-29T20:59:31-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vv1qgn2ogf423f@corp.supernews.com>`
- **In-Reply-To:** `<3ff0bb75_8@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:

> "LX-i" <lxi0007@netscape.net> wrote in message
> news:vuv5lu7bq1122f@corp.supernews.com...
…[10 more quoted lines elided]…
> build components; not as an end in itself.

This is what I was trying to get across.  The components are limited in 
scope (and, as might follow, in complexity) - therefore, you don't have 
a "complex OO system", you have OO pieces tied together with the mortar 
of structured programming.  (Geez, these civil engineering analogies are 
getting pretty deep!  ;>  )

>>Structured works well because it is fairly intuitive - stepping through
>>a process is the way business works.  By using simple, reliable,
…[15 more quoted lines elided]…
> consider my time well spent...<G>)

You should - you're the one that got the wheels turning in my head. 
Then, I go to work and there's this book on the shelf (this quite LARGE 
book) that covered many of the key concepts not only of CBSE, but 
software engineering as it compares with other engineering disciplines.

Put this together with some of the Unisys-specific technologies I was 
learning, and you've got a believer in CBSE.  :)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-30T21:34:04+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff138ea_9@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com> <vv1qgn2ogf423f@corp.supernews.com>`

```

"LX-i" <lxi0007@netscape.net> wrote in message
news:vv1qgn2ogf423f@corp.supernews.com...
> Peter E.C. Dashwood wrote:
>
…[11 more quoted lines elided]…
> > This is exactly my position also. I see OO as a necessary prerequisite
to
> > build components; not as an end in itself.
>
…[21 more quoted lines elided]…
> > essential ideas of component technology and been able to apply them to
your
> > particular environment. (If anything I said anywhere influenced this,
then I
> > consider my time well spent...<G>)
>
…[7 more quoted lines elided]…
>

Excellent! I think I can benefit from reading this book. Can you give us a
reference?

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2003-12-30T19:24:36-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vv49bgorieok3c@corp.supernews.com>`
- **In-Reply-To:** `<3ff138ea_9@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com> <vv1qgn2ogf423f@corp.supernews.com> <3ff138ea_9@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:
>>You should - you're the one that got the wheels turning in my head.
>>Then, I go to work and there's this book on the shelf (this quite LARGE
…[9 more quoted lines elided]…
> reference?

Sure.  It's called "Component-Based Software Engineering:  Putting the 
Pieces Together", by George T. Heineman and William T. Councill (may be 
credited as editors), published by Addison-Wesley in 2001.  The ISBN is 
0-201-70485-4.

Here's how it's laid out...

Part 1 - Component Definition
	Chapter 1 - Definition of a software component and its elements
	Chapter 2 - The component industry metaphor
	Chapter 3 - Component models and component services:  concepts and 
principles
	Chapter 4 - An example specification for implementing a temperature 
regulator software component

Part 2 - The Case for Components
	Chapter 5 - The business case for components
	Chapter 6 - COTS myths and other lessons learned from component-based 
software development
	Chapter 7 - Planning team roles for CBD
	Chapter 8 - Common high-risk mistakes
	Chapter 9 - CBSE success factors:  integrating architecture, process, 
and organization

Part 3 - Software Engineering Practices
	Chapter 10 - Practices of software engineering
	Chapter 11 - From subroutines to subsystems:  component-based software 
development
	Chapter 12 - Status of CBSE in Europe
	Chapter 13 - CBSE in Japan and Asia

Part 4 - The Design of Software Component Infrastructures
	Chapter 14 - Software components and the UML
	Chapter 15 - Component infrastructures:  placing software components in 
context
	Chapter 16 - Business components
	Chapter 17 - Components and connectors:  catalysis techniques for 
designing component infrastructures
	Chapter 18 - An OPEN process for component-based development
	Chapter 19 - Designing models of modularity and integration

Part 5 - From Software Component Infrastructres to Software Systems
	Chapter 20 - Software architecture
	Chapter 21 - Software architecture design principles
	Chapter 22 - Product-line architectures

Part 6 - The Management of Component-Based Software Systems
	Chapter 23 - Measurement and metrics for software components
	Chapter 24 - Implementing a practical reuse program for software components
	Chapter 25 - Selecting the right COTS software:  why requirements are 
important
	Chapter 26 - Building instead of buying:  a rebuttal
	Chapter 27 - Software component project management
	Chapter 28 - The trouble with testing components
	Chapter 29 - Configuration management and component libraries
	Chapter 30 - The evolution, maintenance, and management of 
component-based systems

Part 7 - Component Technologies
	Chapter 31 - Overview of the CORBA component model
	Chapter 32 - Overview of COM+
	Chapter 33 - Overview of the Enterprise JavaBeans component
	Chapter 34 - Bonobo and free software GNOME components
	Chapter 35 - Choosing between COM+, EJB, and CCM
	Chapter 36 - Software agents as next-generation software components

Part 8 - Legal and Regulatory Component Issues
	Chapter 37 - Component-based software engineering as a unique 
engineering discipline
	Chapter 38 - The future of software components:  standards and 
certification
	Chapter 39 - Commercial law applicable to component-based software
	Chapter 40 - The effects of UCITA on software component development and 
marketing

Part 9 - Conclusion
	Chapter 41 - Summary
	Chapter 42 - The near-term future of component-based software engineering

The glossary begins on page 777 - it's a pretty hefty book.  With the 
different parts, it's structured so that you can read parts that 
interest you, not just read them straight through.  Of course, they want 
you to start with part 1, just so you understand some of the terms and 
working definitions they establish.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 16)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-01T14:04:34+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff37293_2@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com> <vv1qgn2ogf423f@corp.supernews.com> <3ff138ea_9@news.athenanews.com> <vv49bgorieok3c@corp.supernews.com>`

```
Thanks Daniel.

I'll try and get it from Amazon.

The topics look great.

Pete.

"LX-i" <lxi0007@netscape.net> wrote in message
news:vv49bgorieok3c@corp.supernews.com...
> Peter E.C. Dashwood wrote:
> >>You should - you're the one that got the wheels turning in my head.
…[9 more quoted lines elided]…
> > Excellent! I think I can benefit from reading this book. Can you give us
a
> > reference?
>
…[48 more quoted lines elided]…
> Chapter 24 - Implementing a practical reuse program for software
components
> Chapter 25 - Selecting the right COTS software:  why requirements are
> important
…[45 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 17)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-01-03T21:53:24-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vvf3e5bkojdq6c@corp.supernews.com>`
- **In-Reply-To:** `<3ff37293_2@news.athenanews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com> <vv1qgn2ogf423f@corp.supernews.com> <3ff138ea_9@news.athenanews.com> <vv49bgorieok3c@corp.supernews.com> <3ff37293_2@news.athenanews.com>`

```
Peter E.C. Dashwood wrote:

> Thanks Daniel.
> 
> I'll try and get it from Amazon.
> 
> The topics look great.

No problem.  You'll probably make faster time through it than I have. 
And now, I've got a promotion test to study for - gotta get that extra 
money!  :)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T14:24:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bss1qi$shg$1@peabody.colorado.edu>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com>`

```

On 29-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> This is exactly my position also. I see OO as a necessary prerequisite to
> build components; not as an end in itself.

I can see other ways of building components - but OO based standards work well,
and some type of standards are necessary for component based design.

But that doesn't mean my design should embrace all OO features.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-30T16:35:24-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<SemIb.5857$Vl6.1493406@news20.bellglobal.com>`
- **In-Reply-To:** `<bss1qi$shg$1@peabody.colorado.edu>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com> <bss1qi$shg$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On 29-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> 
…[8 more quoted lines elided]…
> But that doesn't mean my design should embrace all OO features.


When should any design embrace all the features of any language?

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-31T15:14:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bsup4g$pap$1@peabody.colorado.edu>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <vuv5lu7bq1122f@corp.supernews.com> <3ff0bb75_8@news.athenanews.com> <bss1qi$shg$1@peabody.colorado.edu> <SemIb.5857$Vl6.1493406@news20.bellglobal.com>`

```

On 30-Dec-2003, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:

> > But that doesn't mean my design should embrace all OO features.
>
>
> When should any design embrace all the features of any language?

OO is not a language.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T03:13:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231221304.11149.00001933@mb-m11.aol.com>`
- **References:** `<vuv5lu7bq1122f@corp.supernews.com>`

```
LX-i lxi0007@netscape.net 
Date: 12/28/03 9:51 PM EST
Message-id: <vuv5lu7bq1122f@corp.supernews.com>

<<
I'm reading a great book about CBSE - this is some of the stuff just 
from the first chapter.
>>

It is okay to reference the book specifically. Don't be surprise if we
ultimately hold your reposible for all of it's contents. bu tit ain't like we
will trounce you for just naming it with author and stuff. Your enthusiasm is
valued.  Read on. Cite on!

How far are you so far on this holiday weekend?

Best Wishes
Bob Rayhawk

P.S. More than one contributor takes a slight turn at 'component' along this
'object' pathway. Y'all intrigue me.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** LX-i <lxi0007@netscape.net>
- **Date:** 2004-01-03T21:59:37-06:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<vvf3ps6fdmn824@corp.supernews.com>`
- **In-Reply-To:** `<20031231221304.11149.00001933@mb-m11.aol.com>`
- **References:** `<vuv5lu7bq1122f@corp.supernews.com> <20031231221304.11149.00001933@mb-m11.aol.com>`

```
RKRayhawk wrote:

> LX-i lxi0007@netscape.net 
> Date: 12/28/03 9:51 PM EST
…[10 more quoted lines elided]…
> valued.  Read on. Cite on!

:)  Well, you've probably seen the table of contents that I posted earlier.

> How far are you so far on this holiday weekend?

Doing fairly well.  We're now the proud owners of a 2003 Chrysler Town & 
Country (after our Plymouth Grand Voyager died a horrid death a few 
months back), so we're back to 2 cars.  However, my laptop (the one that 
replaced the one that was stolen back in October) has started acting up. 
  I must be bad luck to laptops...  :)

> P.S. More than one contributor takes a slight turn at 'component' along this
> 'object' pathway. Y'all intrigue me.

Good!  I've been able to implement a couple (all in the Unisys mainframe 
environment, not the CORBA or COM+ paradigm), but even with that, 
they've saved a lot of time.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T15:44:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<13774e40ce9b92e344177eae2ff50176@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com>`

```
"RKRayhawk" <rkrayhawk@aol.com> wrote:
>
> If we have succeeded by encapsulating, then are we not failing by
…[5 more quoted lines elided]…
> manipulation?

Wow! You have beautifully described one of the reasons why OO is on
the wrong side of the point of diminishing return. What may appear good
in theory sometimes fails miserably in real world situations, where clean
purity of application is the rare exception, and messy, complicated human
imposed rules and illogical practicalities are the norm. Scientific and
engineering programming can be models of logic and elegance. But in the
world of business, programming can be anything but. Have you ever
written code to process rules based on law? Legal logic is an oxymoron.
The Illinois legislature came extremely close to passing a law to make
pi = 3 in the state of Illinois. Look it up, it's a fact.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-29T16:37:45+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bspl8o$o3k$1@peabody.colorado.edu>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <13774e40ce9b92e344177eae2ff50176@news.teranews.com>`

```

On 29-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> Legal logic is an oxymoron.
> The Illinois legislature came extremely close to passing a law to make
> pi = 3 in the state of Illinois. Look it up, it's a fact.

http://www.snopes.com/religion/pi.htm

Actually, saying pi=3 is not necessarily less accurate than saying
pi=3.1415926535897932384626433832795.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T20:24:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6f7843359e43a78fa46828749e5ba6ad@news.teranews.com>`
- **References:** `<VA.00000392.0304c6c1@ieee.org> <20031228194319.19959.00001142@mb-m01.aol.com> <13774e40ce9b92e344177eae2ff50176@news.teranews.com> <bspl8o$o3k$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[5 more quoted lines elided]…
> http://www.snopes.com/religion/pi.htm

Yeah, that's a funny, not true. It is true about Illinois. Really. Such a
boneheaded idea struck me as being beyond even politicians to
accept (an unwarranted assumption, as it turned out), so I researched
it. What happened is that this charlatan, the kind who are always
inventing perpetual motion machines and squaring circles, went to
the Illionois legislature in the 1800's, IIRC, and convinced them he
had made this tremendous discovery. If you made pi = 3 instead of
3.142592653689703..., it made arithmetic much easier for school
children to learn. He even graciously offered to permit Illinois (only
Illinois, mind you) to have this discovery for free. Overjoyed at
such a windfall, the legislature began rapidly drawing up a bill. But
the procedures were fortunately discovered by credible academics
in time. They were horrified, of course, and ran to the legislature to
inform them they were about to make themselves and Illionis a
laughingstock. Though they still did not understand the problem
(had they possessed that much wit, the problem wouldn't have come
about in the first place), politicians are as sensitive to bad publicity
as the eye is to grit, so they backed off. Unfortunately, I could not
learn what they said or did to the perpetrator. No doubt, they felt
that the less publicity the better, and buried it, happy to let him
perpetrate the same fraud on another legislature. At one time I knew
the date and name of the perpetrator, but time and more weighty
matters have overwritten the memory. :-)

> Actually, saying pi=3 is not necessarily less accurate than saying
> pi=3.1415926535897932384626433832795.

Reminds me of a favorite semantical topic of mine, the difference between
'accurate' and 'precise'. Saying that pi = 3 is 'accurate' but not 'precise'.
OTOH, saying that pi = 3.55555555555555555555555 is 'precise' but
not 'accurate'.  Saying that pi = 3.1415926535897932384626433832795 as
you do, is both 'accurate' and 'precise'. Saying that pi = 9 is not 'accurate'
and not 'precise'. 'Accurate' is how 'true' it is. 'Precise' is to what degree of
exactness it is stated.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T03:57:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231225756.11149.00001938@mb-m11.aol.com>`
- **References:** `<bspl8o$o3k$1@peabody.colorado.edu>`

```
Pi ain't Amuricun so cain't be useful. It is as foraign as all dhat other east
europian sewrage. Commie Pinkoes, one and all!

Ta hades with 'em. Dem greeeks an' matemetician. I het dhem intellecuwals,
anyhow.

Three it is. And if ya cain't understand three point zera than tha heck with
ya.

And another dhing. If they sez theyze want that object stuff. whall, dhen ya'
tell 'em weeze is going to reorient them and instance upon it. I am sure about
not only the accuracy of it but the precijion of it, now.

Listen here.  We don't need no foraign alphbits here. This pi thing is
subversive and insidious, likely to threaten our children and degrade our ever
reknown schools and sich.  Why, heck, just this last week we had a fund raiser
to pruvide pensils for dha students at the school just up tha road a peace.

Now, community spirit, dhat's dha way.  We dun need no objects, anyhow.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T03:41:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231224107.11149.00001937@mb-m11.aol.com>`
- **References:** `<13774e40ce9b92e344177eae2ff50176@news.teranews.com>`

```
<<The Illinois legislature came extremely close to passing a law to make
pi = 3 in the state of Illinois. Look it up, it's a fact.
>>

This sort of thing ought to be illegal or unconstitutional in the land of
Lincoln and all  elsewhere.

Why, Heather, what would we programers be without exceptions.

Heaven's sake!

Best of wishes and may the New Year find us as safe in the South as at all
other points of view.

God Love Govenor RIch and the other silent heroes!
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T15:31:23+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> "Doug Scott" <dwscott@ieee.org> wrote:
…[4 more quoted lines elided]…
> OK, was your OO implementation successful?


If your trial of OO succeeds, then you did it right, if it didn't do well,
then you didn't do it right. Whether OO was at fault is never considered.
Beautiful circular reasoning. ;-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-29T16:44:09+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bsplkp$q0r$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com>`

```

On 29-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> If your trial of OO succeeds, then you did it right, if it didn't do well,
> then you didn't do it right. Whether OO was at fault is never considered.
> Beautiful circular reasoning. ;-)

Even so - there are many ways of measuring success.   If your goal is to build
quickly using components, OO has a much better chance of succeeding than if your
goal is to maintain for 30 years without effecting other programs.

Building complex systems quickly is a valid goal - and one which is more and
more popular.   We are in a disposable society.

Some of the other goals of OO such as reusability have achieved less universal
acclaim and success.   A widely used component means interdependencies and
results in compromises in testing.    But it is perfectly valid to use OO tools
without using all of the abilities of OO.    Some pretty impressive systems have
been built using OO with minimal or zero reuse of new components.

Still no tool fits all needs.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-29T22:13:20+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000039d.0073e04b@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu>`

```
Howard,

> Building complex systems quickly is a valid goal - and one which is more and
> more popular.   We are in a disposable society.

It is a better way to do things, but it's expensive. If IT management could 
bring realistic budgets to the party, then systems could be worked like the 
Forth Bridge - always undergoing minor repair and refurbishment, without ever 
being closed.

> Some pretty impressive systems have
> been built using OO with minimal or zero reuse of new components.

I really don't believe re-use is the magic solution originally promised. 
Itcosts ten times as much to make a routine truly reusable, and only software 
publishers can afford that sort of trade-off.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T14:31:58+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bss28u$jo$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <VA.0000039d.0073e04b@ieee.org>`

```

On 29-Dec-2003, Doug Scott <dwscott@ieee.org> wrote:

> > Building complex systems quickly is a valid goal - and one which is more and
> > more popular.   We are in a disposable society.
…[4 more quoted lines elided]…
> being closed.

It may be better, and it may be more expensive.   But neither is a truism.

There can be cost advantages in disposable tools.   Hospitals use disposable
syringes because they're cheaper than the maintenance required to sterilize
reusable syringes.    (not to mention toilet paper).

If your requirement changes are simple, then maintenance may be cheaper.  If
they are complex, it may be cheaper to throw out your old components and replace
them.

People (and companies) periodically search for the One True Tool.   This may be
a management style, a programming style, a sales style, or whatever.    But I
want to use all of the clubs in my golf bag.
```

###### ↳ ↳ ↳ OT Golf WAS Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-31T12:30:25+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff20b01_2@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <VA.0000039d.0073e04b@ieee.org> <bss28u$jo$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bss28u$jo$1@peabody.colorado.edu...
>
> On 29-Dec-2003, Doug Scott <dwscott@ieee.org> wrote:
>
> People (and companies) periodically search for the One True Tool.   This
may be
> a management style, a programming style, a sales style, or whatever.
But I
> want to use all of the clubs in my golf bag.

My handicap (apart from all the obvious ones...<G>) is "officially" 20. (I
have never analysed or tried to seriously improve my golf game, because I
don't play often enough and the wonderful handicapping system ensures
players of wildly different abilities can have enjoyable matches against
each other. On the increasingly rare occasions when I get to play, I simply
enjoy it...)

But your comment did remind me of something that happened many years ago on
a public course in Auckland. I had decided to have a round, and none of the
pool of "usual partners" that I played with was available, so I decided to
simply turn up and get paired off with a stranger.

The man I was paired with seemed fairly affable and unprepossessing. He
asked me my handicap and I truthfully said "24" (it was the maximum
allowable and I was just learning...). His was "4". I was in awe as I had
never played with anyone that good before. Anyway, he asked me if I would
like him to give me advice as we progressed (which I thought then and still
think, was a very civilized and polite way to offer help). I eagerly
accepted and we played the first hole. He birdied it and I was 2 over. On
the next tee, he started to explain about timing...

"If you get the timing right and adjust your stance properly, you can get
huge milage from any of your clubs." he said.

"But what about the different lofts and weights of different clubs?", I
asked.

"Irrelevant, at a fundamental level. It is all in the timing. Look, we have
17 holes to play. I'll play ALLof them using ONLY a putter, just to
demonstrate what I am saying...".

While I was a novice, I realised that the putter has NO loft whatsoever with
a plain flat face, and little or no weight.

He drove off the tee with his putter and made around 250 yards; I drove with
a 2 wood and was under 200...

That pattern was repeated throughout the day. His drives, approaches, chips,
and putts were all made solely with his putter and he ended up something
like 15 over par for the course. ( I think I was pleased to be 35 over,
after adjusting for handicap...<G>)

I have never forgotten the "lesson" I received from that unknown golfer. For
the cost of a jug of beer, which I gladly bought at the 19th, I learned that
if you are really good at something, so good that you really "understand"
and recognise it's underlying essence, the "received wisdom" may not apply
to you...

There is also no doubt that having a 4 handicap inspires confidence and
dispels doubt...<G>

Pete.
```

###### ↳ ↳ ↳ Re: OT Golf WAS CoBOL moved to OO

_(reply depth: 14)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-31T11:42:06+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003ba.0070f2db@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <VA.0000039d.0073e04b@ieee.org> <3ff20b01_2@news.athenanews.com>`

```
Peter,

> I learned that
> if you are really good at something, so good that you really "understand"
> and recognise it's underlying essence, the "received wisdom" may not apply
> to you...

That's a lovely story, and it resonates truth.


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: OT Golf WAS Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-31T15:21:09+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bsuph5$q0u$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <VA.0000039d.0073e04b@ieee.org> <bss28u$jo$1@peabody.colorado.edu> <3ff20b01_2@news.athenanews.com>`

```

On 30-Dec-2003, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> The man I was paired with seemed fairly affable and unprepossessing. He
> asked me my handicap and I truthfully said "24" (it was the maximum
> allowable and I was just learning...). His was "4". I was in awe as I had
> never played with anyone that good before.

In the U.S. handicap indices above 36 get calculated but generally aren't 
counted.    It is a good learning practice to play 3 club tournaments.  One
learns to use the tools we have better.    Heck I once wrote a program in DCL
that emulated assembler - even doing left and right shifts for multiplication
and division.   Good practice.


> I have never forgotten the "lesson" I received from that unknown golfer. For
> the cost of a jug of beer, which I gladly bought at the 19th, I learned that
…[5 more quoted lines elided]…
> dispels doubt...<G>

A good golfer/programmer can use whatever tools we have available - and do a
better job than poor golfers/programmers.

But when they want to do their best (let's say in a Major golf championship),
they make sure they have all of their tools.
```

###### ↳ ↳ ↳ Re: OT Golf WAS Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-31T19:54:27+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<0655f31ed515d487546198d169decbca@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <VA.0000039d.0073e04b@ieee.org> <bss28u$jo$1@peabody.colorado.edu> <3ff20b01_2@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> I have never forgotten the "lesson" I received from that unknown golfer. For
…[3 more quoted lines elided]…
> to you...

As they say, "It's not the brush, but the artist." :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-31T19:30:03+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003bc.021d5cd9@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <VA.0000039d.0073e04b@ieee.org> <bss28u$jo$1@peabody.colorado.edu>`

```
Howard,

> There can be cost advantages in disposable tools.

Yes indeed. I'm not sure of the equivalence between hardware and software at this 
stage - each iteration of software has an element of redesign in it, and 
disposable tools don't.

> If your requirement changes are simple, then maintenance may be cheaper.  If
> they are complex, it may be cheaper to throw out your old components and replace
> them.

This argument stood at its strongest with the advent of APL. It was so complex to 
understand that the Given Wisdom was that you shouldn't try to modify an APL 
program, but simply rewrite it. The trouble is that any implementation reflects 
not just the algorithm but the testing and refinement of the algorithm, and the 
changes arising from those activities were rarely reflected back into the spec, so 
a rewrite meant an entire new development, with its attendant costs. I've lost 
contact with any APL programmers I knew, but I doubt they'll subscribe to it 
nowadays. Legacy code is precious because it works exactly the way the company 
wants it to, warts and all.

> People (and companies) periodically search for the One True Tool.   This may be
> a management style, a programming style, a sales style, or whatever.    But I
> want to use all of the clubs in my golf bag.

On this point we're agreed.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-29T20:20:26-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0312292020.5cf5dd0@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote

> We are in a disposable society.

You may be, but I certainly am not.  I haven't thrown anything away
for years. The last time I did, I needed it the very next day, so I
won't be doing that again.

Disposal and planned obsolescence are merely tricks by manufactureres
via their marketing droids that attempts to create the desire to buy
something new.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T14:34:19+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bss2db$us$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <217e491a.0312292020.5cf5dd0@posting.google.com>`

```

On 29-Dec-2003, riplin@Azonic.co.nz (Richard) wrote:

> > We are in a disposable society.
>
> You may be, but I certainly am not.  I haven't thrown anything away
> for years. The last time I did, I needed it the very next day, so I
> won't be doing that again.

Toilet paper?

> Disposal and planned obsolescence are merely tricks by manufactureres
> via their marketing droids that attempts to create the desire to buy
> something new.

Welcomed by consumers.   Do you pay $120 to have someone look at your $100
ink-jet printer?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-30T10:54:58-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0312301054.5998405f@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <bsplkp$q0r$1@peabody.colorado.edu> <217e491a.0312292020.5cf5dd0@posting.google.com> <bss2db$us$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> > You may be, but I certainly am not.  I haven't thrown anything away
> > for years. The last time I did, I needed it the very next day, so I
> > won't be doing that again.
> 
> Toilet paper?

Paper ?  What's wrong with the brush ?    ;-)

 
> > Disposal and planned obsolescence are merely tricks by manufactureres
> > via their marketing droids that attempts to create the desire to buy
…[3 more quoted lines elided]…
> ink-jet printer?

I don't use ink-jet printers.  I have stacks of old lasers and matrix
printers discarded by customers that do the job fine when I need a
printout.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-30T12:10:26+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff0b4cf_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > "Doug Scott" <dwscott@ieee.org> wrote:
> > >
> > > And I don't need you to tell me what sort of experience I've got. I
HAVE
> > > implemented OO using C++ and Java.
> >
…[6 more quoted lines elided]…
> -- 

My original statement, to which the poster objected, included the phrase
"...have never successfully implemented an OO system."

In examining the poster's objection it is therefore right and proper that I
should understand whether or not he objects to the whole position or only
part of it.

Taking something out of context and imparting your own spin to it, is
unworthy and unnecesssary.

My position is not as you state.

(Although it is certainly true that ALL of the pilot projects I have been
involved with were considered "successful". I would therefore want to
analyse one that wasn't, in order to find out what was done
differently...Having eliminated the Scientific method as not contributing to
the failure, it would then be proper to investigate OO itself as possibly
being inadequate. BUT, this would not be my FIRST assumption.)

However, even if it were, I am not sure this is a circular argument.

If indeed the OO trial was not correctly and properly undertaken, then by
any objective Scientific definition, the experiment (as an experiment) MUST
be doomed to failure. At the very least (even if it succeeded under these
conditions) it could not be considered a successful experiment.

What is "circular" about that?

We need to know whether it was "properly" conducted in order to determine
the value of the outcome. Nothing more.

Pete.






> Judson McClendon      judmc@sunvaley0.com (remove zero)
> Sun Valley Systems     http://sunvaley.com
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-30T13:53:42+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<7ed535db83b5f34cb55ad70f02f81ace@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <3ff0b4cf_5@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> > "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
…[19 more quoted lines elided]…
> unworthy and unnecesssary.

Didn't you see my 'winky' after 'reasoning'? Your statement just made a
tempting target and I rattled your cage a bit in fun. Sorry if I offended. :-)

Pete, I respect your position. Though I disagree with you, it is clear that
you have thought it through and believe strongly in it, and you are obviously
experienced and competent. I suppose you and I will continue to disagree
on this issue until either OO fails so miserably you recant (ha! ha!), or I
'see the light' and jump on the bandwagon with you OO proponents (oh!
oh!). Not sure what the relative probabilities are. ;-)

These discussions have, if nothing else, provoked me into delving farther
into OO, and writing a small OO based system; probably but not necessarily
in COBOL. The one I am thinking of will duplicate a small part of that
vehicle license system I have discussed. My associate, who worked with
me in writing the current mainframe system, and myself are exploring the
possibility of writing a C/S based PC version, either GUI or maybe HTML.
I'm thinking Flexus sp2 is the way to go for flexibility here (Thanks again
Bob Wolfe, I haven't forgotten! :). For maximum flexibility (in an already
enormously flexible system) we will use a high degree of abstraction in
the design. The business logic will be defined softly (not hard coded) as
much as possible. If the client continues with their plan to eventually buy
a C/S package to replace the one we wrote, they're going to drop a few
million on somebody for it. It might as well be us. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T15:03:40+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bss44c$69f$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <3ff0b4cf_5@news.athenanews.com> <7ed535db83b5f34cb55ad70f02f81ace@news.teranews.com>`

```

On 30-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> Pete, I respect your position. Though I disagree with you, it is clear that
> you have thought it through and believe strongly in it, and you are obviously
…[3 more quoted lines elided]…
> oh!). Not sure what the relative probabilities are. ;-)

Or there continues to be a split in applications/systems where OO is appropriate
and where OO is not appropriate and each of you see that in your view of your
world, your position is correct.

What I fear though is that we make decisions for the wrong reasons - in which
case one methodology can win out without convincing antagonists that the
protagonists are right for their case.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-31T20:30:03+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003bd.02544bc4@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <3ff0b4cf_5@news.athenanews.com> <7ed535db83b5f34cb55ad70f02f81ace@news.teranews.com>`

```
Judson,

> The business logic will be defined softly (not hard coded) as
> much as possible.

I'd issue a caution here. We went through this some years ago, and 
there are some considerations over and above business flexibility.

We believed that the users owned the data, and therefore should be able 
(with proper authority) to change it. So we implemented full 
data-driven systems - or as full as we could make it.

What we hadn't thought through is the way programmers test out business 
changes, many of which established the selling price of goods. When a 
programmer does a change he tests it against predicted results, 
compares against previous versions, and so on. When an end user does 
it, he simply applies the change and goes home - perhaps to discover 
that he'd got the price wrong.

It was then that we realised that users would need the full testbed set 
of tools which programmers always had - to be able to simulate changes 
to the rules and run through the whole business cycle, to understand 
the consequences of the change. Users weren't interested in doing that, 
but on one system they did assign one poor chap who was responsible for 
all changes to all parts of the system. He didn't know the full 
ramifications - he was just a changer/tester - so the result was a 
degree of chaos in pricing which continued for a couple of years.

So beware!

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-31T22:21:01+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<b0b9224fe6586248cb40d3219c549eef@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <VA.00000375.02bf5c97@ieee.org> <VPIFb.4318$d%1.931294@news20.bellglobal.com> <3fe76bd1_6@news.athenanews.com> <VA.00000387.0376cab3@ieee.org> <3fedddc6_2@news.athenanews.com> <acce5cd310d1009cbc1ce12411a0ab2d@news.teranews.com> <3ff0b4cf_5@news.athenanews.com> <7ed535db83b5f34cb55ad70f02f81ace@news.teranews.com> <VA.000003bd.02544bc4@ieee.org>`

```
Your points are well taken, Doug. This is what we have observed in
the six years or so the current system has been running. The current
system is very table driven in the tax calculations, it has to be. The
Revenue Department (who sells the licenses) can create a whole new
tag type, and specify when it is to be effective, all by themselves. In
1977 Alabama had over 200 tag types. Not only normal types like
passenger automobiles, big trucks, busses, trailers, etc., but special
school plates, environmental, etc. And you can get a certain number
of signatures on a petition and the state will issue a new tag type for
you, say a club or football team. I haven't checked, but there may be
twice that number by now. Each tag type has a unique numbering
scheme that is changed every year, though this is not required by the
system; tag type and year tells the system all it has to know to find the
tag definition, and then it knows how to handle the number. This
turned out to be non-trivial to implement, and for them to maintain.
It's the most complicated part of the system for the users who maintain
the tables. Consider that a tag number could be any sequence of alpha
or numeric fields, and each field can have it's own valid range. And
the numbers do not all increment the rightmost field, then the next to
the left, and so on, as you might expect. The number fields might be
incremented in any sequence of low order to high order within the
number. You MUST know this to order tag numbers. I had to create a
table structure to define this, and write the code to validate numbers
by it, and also code to increment numbers so we could check for tag
numbers missing on file. The code to do all this is complex, enough so
to not be immediately intuitively obvious. There had to be (logically)
indirect pointers and such, which many COBOL jocks are not very
familiar with. I prefer not to leave very complex code for clients to
maintain, but the code's got to do what the code's got to do. ;-)

Sorry for the digression, but it was a bit if a rude awakening when the
user department had to start maintaining these tables. They did want to
control this stuff, but it was much simpler and easier for them to simply
tell the staff programmer what they wanted. The client has a separate
machine to test it on before it is made live. They had the test machine
anyway for general application testing, but it was a lifesaver for this. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 4)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-12-24T15:39:13-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0312241539.1607c8f0@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com>`

```
Seeing as you might be cold - I'm going to try to warm you up a bit.

OO is a DIFFERENT way of thinking from procedural.  Procedural is
like:

you do this 
you do that
you take this there
Now do this with it

OO is like:

I need this done - you handle this exclusively - you do it and tell me
about the results.

It's also like:

I need information with which to modify MY data - I'll go get it!

OO is highly efficient and properly implemented very protective of the
data - and this is one key benefit - it's protective of the data.

COBOLers don't see this as quickly as users of some other procedural
languages - because COBOL has always been protective of the data. 
COBOL and OO are a great fit.

What's lacking presently is an implementation of the standard.  Once
we have a vendor who has completely implemented OO I think you will
realize the difference - once you grasp the concept.

I too once didn't understand it.  I strongly strongly strongly
recommend the folowing:

http://www.amazon.com/exec/obidos/ASIN/0672326116/thanesonlinecobo

It's a great read and helps to easily grasp the concepts.

I actually never truly understood OO until I used the Fujitsu OO COBOL
implementation - once you have that "light bulb" experience, the
simplicity and elegence of OO is clear.


"Judson McClendon" <judmc@sunvaley0.com> wrote in message news:<22b3dcd54cff07a52f959b3cd483727d@news.teranews.com>...
> "Howard Brazee" <howard@brazee.net> wrote:
> > Doug Scott <dwscott@ieee.org> wrote:
…[28 more quoted lines elided]…
> Don't worry, I have my asbestos pants on. ;-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-25T03:49:18+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com>`

```
Thane,
  I still don't (fully?) understand (internalize) the difference between your
OO:

> I need this done - you handle this exclusively - you do it and tell me
> about the results.
…[3 more quoted lines elided]…
> I need information with which to modify MY data - I'll go get it!

and "traditional" MODULARIZED COBOL programming where you:

Call do-something  routine passing it something (or not) and asking it to do
what "do-something" does

  or

Call (perform) some-routine to return (in a parameter or even a RETURNED or
EXTERNAL variable) the information that "some-routine" is expected to know
about.

With Call-prototypes in the 2002 Standard, there is even "protection" from
passing a module something that it shouldn't get - or requesting returned
information that you shouldn't see.

I am *not* trying to "fight" OO "philosophy" for applications that are designed
(from initial concept) for such, I simply (still) don't really "GET" what the
fundamental difference is.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-25T09:00:45-06:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<sKqdnQyMBMoLZneiRVn-hg@giganews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`

```
William M. Klein wrote:
> Thane,
>   I still don't (fully?) understand (internalize) the difference
…[28 more quoted lines elided]…
>

It's WORDS, man. It's NAMES.

It's like the difference between "Medicine" and "Medication."
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2003-12-25T15:27:46+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<SlDGb.8684$IM3.8466@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`

```
I agree with Bill.  From Thane's description of OO, I've been thought, 
have thought, seen and done OO in COBOL since 1972.   It was called 
"Structured Programming" where initially you would call a 
subprogram(routine - machines weren't big enough to handle a large 
procedural program (32K (yes K not Meg) was a LARGE machine - 8K and 
maybe 16K more typical with some only 4K).  Later you would perform a 
routine that did what you want.   This was what is now called 
encapsulated code - or object code.  There is really no difference. 
SOMEONE has to do the procedural code to get the data - be it the 
application programmer or the "guy" that wrote the compiler - it is not 
magic.  To call the concept new is misleading.  What IS new is the tools 
and the GUI.

On the topic of GUI,  I've seen many instances of GUI that, while 
looking nice, take twice as long to either enter or review the 
information that was contained on the old green screens.  The biggest 
advantage of GUI (IMHO) is all the "new" people starting to work in the 
outlying departments have never seen a green screen with all of the data 
smooshed (is that a word?) together.  YES, green screen was ugly! 
However, processor speed was SLOW as was data transmission speeds.  Put 
the data out there once - only send data down the line once rather than 
multiple times.  Another BIG ADVANTAGE of GUI (however, I'm not sure how 
often it's implemented) is the capability of adding true help text to 
individual data fields.  By "true help text" I mean explanations of what 
the data field (column) means, not just what data is allowed (text box).

Forgive my rant, but I keep seeing OO proponents keep stating how NEW OO 
is and how much better it is than the old COBOL model without really 
understanding how the old system worked (or should have worked).

Dick

Remember, there is NO language existing such that you CANNOT program a 
HORRID program.

William M. Klein wrote:
> Thane,
>   I still don't (fully?) understand (internalize) the difference between your
…[29 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2003-12-25T17:22:59-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0312251722.7e916753@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`

```
Well - I was at risk of oversimplification and I did.

Your reply directly illustrates my point:

> > COBOLers don't see this as quickly as users of some other procedural
> > languages - because COBOL has always been protective of the data.
> > COBOL and OO are a great fit.

Please take a look at the book reference - it's a great one really.  I
don't want to reiterate it here - just read the book if you want to
understand this.  Once you DO understand it you won't look at things
the same way any more.

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message news:<27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>...
> Thane,
>   I still don't (fully?) understand (internalize) the difference between your
…[111 more quoted lines elided]…
> > > Don't worry, I have my asbestos pants on. ;-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-27T15:43:42+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<a05ced08fbce023d776b6295c1a40b55@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`

```
Bill, the difference is in the way the programming model is abstracted.
Pardon my digression, but I think it may be informative to many here.

Abstraction is generally a good thing. In fact, a necessary thing in most
cases, because we simply could not deal with our world without it.
The very words I write are abstractions of what they represent. If you
watch a child learning to tie his shoes, he is intent on every move he
makes. Later, when he has tied his shoes a thousand times, he no longer
even thinks consciously about the individual moves. His brain has
'abstracted' all the movements necessary into one concept: tying my
shoes. Now, instead of his conscious mind occupying itself with the
many details of the process, it can deal with a single abstraction. At
some point, the whole 'getting dressed in the morning' may become an
abstraction. If our brains didn't do this, we would be overwhelmed in
detail, and simply couldn't cope with it.

In programming, our abstractions are much more formal and clearly
defined. The first compilers (assemblers) did not abstract the process
very far, since each machine instruction was coded one by one. Only
the labels to the procedures and data were really abstractions. But as
compiler technology grew higher and higher levels of abstraction were
called into play. APL, for example, is abstracted to a very high degree.
If you consider the attributes of good structured design/programming
you can see that the forms we use are an aid to further abstraction of
the process, making it easier and more accurate for us to deal with
mentally. At bottom line, this is the essence and purpose of structured
technique. But there are many different ways complex processes can
be abstracted, not only in degree, but in kind. Every programming
language is an attempt to abstract the process in particular ways, each
with its advantages and disadvantages.

Because abstraction is generally a good idea, we are constantly trying
to improve our abstraction models. So called 'Fourth Generation'
languages are such an attempt. Why are we not all using 4GLs for all
purposes? I believe that, from a theoretical standpoint, 4GLs do not
improve the overall process, because for every benefit in one area,
you suffer compensating disadvantages in another. To create any
system, there are a certain number of what you might call 'decision
points', or places where the desired action or condition must be
specified. 4GLs are an effort to 'anticipate' what you might want to
do and make the process shorter. Fine if that decision fits what you
are trying to do (which is why 4GLs have seen success in vertical
application areas), but can be very bad when it doesn't. Increasing
abstraction is not always a good idea because you can reach a point
of diminishing returns where further abstraction is of no benefit, or
must be in a different direction to benefit. This should not surprise
us, because we encounter such points of diminishing return in
virtually every area where humans try to make things work better.

Now, back to the differences in procedural vs. OO. OO is an
approach to make programming more abstract than traditional
methods, and also to abstract in different ways. At bottom level OO,
like all abstractions, is a way to conceptualize a thing or process,
in this case the programming process. For example, in traditional
programming languages, variables are viewed as storage locations
where data may be stored. In OO, the concept of 'data' becomes an
entity (object) type, with certain attributes that can be invoked to
create individual instances of this type. Similarly, procedures also
become entities (objects) with attributes and methods to do things
on data entities. Indeed, they become one. A database object is not
only the data, but the methods that may be invoked to use the data.
Other ideas, such as 'overloading' are often associated with OO,
but are not actually part of OO proper (An example of 'overloading'
might be the redefinition of the 'add' function several times, so that
the same command can be used to do similar or analogous operations
on multiple types of data, such as complex numbers). In this case,
'add' becomes a method provided by several kinds of data objects.
This involves a very considerable paradigm shift for procedural
programmers, far greater than the shift from 'unstructured' code to
'structured' code. Some people find this paradigm shift much more
difficult to make than others. People introduced to it initially will
usually find it easier than those used to procedural methods.

But the question we should be asking, the question I am always
asking on this issue, is "what are the tangible benefits, and what are
the costs?" The costs are easy to see for anyone who cares to look.
I find the tangible, measurable benefits far less than obvious. I'm
still waiting for statistics documenting easier and/or quicker and/or
cheaper development and maintenance costs and/or better overall
performance. Instead of evidence, I am supplied with comments
like "You're stuck in the mud" or "You're too stupid to understand
OO" or "You are getting old and afraid of change" or "You don't
understand OO because you haven't written a half dozen systems
using OO" and so on, ad finitum. Actually, I only need to see some
clear and objective evidence. Can't get anyone to show me that. ;-)
IMHO OO has, like 4GLs, abstracted pass the point of diminishing
return, except for certain types of use. If not, the objective benefits
would be clear and easy to show in decreased overhead and/or
better productivity/reliability.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-27T20:30:23+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000038e.029700dc@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com>`

```
Judson,

> and so on, ad finitum.

You left out "Users /think/ in objects." Meiler Page-Jones (an OO 
advocate if ever there was one) swears that next time he hears someone 
say that, he'll reach for his gun.

> If not, the objective benefits
> would be clear and easy to show in decreased overhead and/or
> better productivity/reliability.

We finally concluded in our Strategy team that OO was a design method. 
It eased the design process, but complicated the programming process 
and required a significant increase in machine resource to implement. 
So an OO design rendered onto an E/R database, leading THEN to a 
procedural implementation, was our choice of methods. There wasn't much 
tool support for it, but some of the transitional tools allowed both OO 
and E/R for the same data dictionary.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T16:42:27+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<0f814fb5004880699dc9a660a8746294@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org>`

```
"Doug Scott" <dwscott@ieee.org> wrote:
>
> You left out "Users /think/ in objects." Meiler Page-Jones (an OO
> advocate if ever there was one) swears that next time he hears someone
> say that, he'll reach for his gun.


I hadn't heard that one, but I never once in my career encountered a
user who thought in 'objects'. Most users would turn glassy-eyed if
'objects' were described  to them. :-)  I see lots of users who can
only think in the form of procedure. "What does ... mean?" "Well,
for those I use the ... and put the ... with the ... ." :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-29T22:13:20+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000039e.0073e178@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com>`

```
Judson,

> I see lots of users who can
> only think in the form of procedure.

Yes, they think in terms of process because that's how they understand 
the job. Even data (which is what they work with) is poorly understood.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-29T18:54:54-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<Kb3Ib.3832$Vl6.983919@news20.bellglobal.com>`
- **In-Reply-To:** `<VA.0000039e.0073e178@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org>`

```
Doug Scott wrote:
> Judson,
> 
…[14 more quoted lines elided]…
> 

And you think there are no methods involved in OOP?  In fact, the kind 
of stuff you have been doing for years can be viewed as methods within 
system objects.  That is, an ordinary cobol program is simply an 
instance of the generic class "cobol program".

Cobol always has had data items defined as instances of three general 
classes.(alphabetic, alphanumeric, and numeric).  Data names have 
properties, defined by their picture clause, which in itself is a 
property. Most of those properties are available at run time (LENGTH OF 
for example) The "MOVE" statement is a polymorphic method that is 
completely different depending on the class(s) of the operands.

In the past, I could think in those terms, but I could not code in them. 
Now, with the new syntax, I can.  I love it.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-30T14:32:17+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003ad.013e526b@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com>`

```
Donald,

> In the past, I could think in those terms, but I could not code in them. 
> Now, with the new syntax, I can.  I love it.

It's nice to see commitment ;-)

What I see when I read your para is a whole load of stuff which, in Cobol, 
is within the realm of the compiler (Length of, in your example) is now 
flexible and defined at run time. This is extremely costly in terms of 
resources, and explains why software is now faster nowadays than ten years 
ago, despite the significant improvements in machine performance. 
Inheritance, in particular, takes a lot of power at the time of 
instantiation.

Bottom line: IMHO a proper design would determine a lot of these things at 
design time, not at run time. The design of Cobol predefines the length of 
any field; postponing that definition to run-time whenever a string is 
being referenced is extremely costly (I would contend that it's wasteful), 
considering the number of occasions when the length of a string would 
better be left as fixed. There are, of course, occasions when string length 
is unknown, but IMHO it is the task of whichever accepts that string in the 
first place to set it to a known quantity and allow the rest of the system 
to run speedily and freely. 

I might add that if such a discipline had been in place in much current 
software, then buffer overflows wouldn't cause the chaos they're currently 
doing - and have done ever since C came out with a construct which freely 
accepted infinite length strings.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-30T14:52:09+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003b0.015081be@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <VA.000003ad.013e526b@ieee.org>`

```
Doug,

> explains why software is now faster

That should be "software is NO faster...!"

Sheesh!

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-30T16:54:11-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<vwmIb.5925$Vl6.1500752@news20.bellglobal.com>`
- **In-Reply-To:** `<VA.000003ad.013e526b@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com> <VA.000003ad.013e526b@ieee.org>`

```
Doug Scott wrote:
> Donald,
> 
…[16 more quoted lines elided]…
> design time, not at run time. The design of Cobol predefines the length of 

Nice idea.  Unfortunately, most of the Cobol systems I work on were 
designed twenty years ago. Adding something like an OCX object that 
allows invoices to be faxed as part of the batch run, rather than 
printed, might take two weeks the first time.  Redesigning the basic 
print routines to do the same thing in Cobol would probably take closer 
to a year.

> any field; postponing that definition to run-time whenever a string is 
> being referenced is extremely costly (I would contend that it's wasteful), 
…[4 more quoted lines elided]…
> to run speedily and freely. 

In fact, the exact opposite is true regarding passed parameters in 
Cobol.  The only way that an arguement *can* be checked against a 
calling sequence is at run time. If you use OOP, the symbol table of the 
called program is passed in the repository to the calling program, and 
incompatablities are checked during compile. They will generate compile 
time errors.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-30T22:31:46+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<m1nIb.12341$lo3.9191@newsread2.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com> <VA.000003ad.013e526b@ieee.org> <vwmIb.5925$Vl6.1500752@news20.bellglobal.com>`

```
"Donald Tees" <donald_tees@nospam.sympatico.ca> wrote in message
news:vwmIb.5925$Vl6.1500752@news20.bellglobal.com...
<snip>
>
> In fact, the exact opposite is true regarding passed parameters in
…[7 more quoted lines elided]…
>

Not true in the 2002 COBOL Standard with "call prototypes" and "repositories".
In such cases, you explicitly tell it what "call prototype" to use for a CALL
statement and parameters are checked AT COMPILE TIME to see if you are "passing"
the correct type of fields.  With strong typing (also added in the 2002
Standard) this can be QUITE specific checking - or it can be just "length and
category" checking.  It is "up to you" when you create your call prototype.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-31T13:02:55+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff2129d_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com> <VA.000003ad.013e526b@ieee.org> <vwmIb.5925$Vl6.1500752@news20.bellglobal.com> <m1nIb.12341$lo3.9191@newsread2.news.pas.earthlink.net>`

```

"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:m1nIb.12341$lo3.9191@newsread2.news.pas.earthlink.net...
> "Donald Tees" <donald_tees@nospam.sympatico.ca> wrote in message
> news:vwmIb.5925$Vl6.1500752@news20.bellglobal.com...
…[12 more quoted lines elided]…
> Not true in the 2002 COBOL Standard with "call prototypes" and
"repositories".
> In such cases, you explicitly tell it what "call prototype" to use for a
CALL
> statement and parameters are checked AT COMPILE TIME to see if you are
"passing"
> the correct type of fields.  With strong typing (also added in the 2002
> Standard) this can be QUITE specific checking - or it can be just "length
and
> category" checking.  It is "up to you" when you create your call
prototype.
>

OK, so has ANYBODY committed to producing a compiler that complies with this
standard?

When?

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-31T04:36:45+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<xnsIb.27098$Pg1.19458@newsread1.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com> <VA.000003ad.013e526b@ieee.org> <vwmIb.5925$Vl6.1500752@news20.bellglobal.com> <m1nIb.12341$lo3.9191@newsread2.news.pas.earthlink.net> <3ff2129d_5@news.athenanews.com>`

```
I don't know about a "full" 2002 compiler (which Micro Focus *did* commit to),
but they already support

  Program-ID  ... Prototype

as "format 4" of the "program-id" paragraph in their NE V4 LRM at:


http://supportline.microfocus.com/supportline/documentation/books/nx40/lrpubb.htm

Support for call prototypes and compile-time parameter checks was just recently
submitted to IBM as a SHARE requirement.  We should get a response from IBM in
February as to how this "user requested" feature fits into their development
plans.

I would suggest that Fujitsu customers might be able to speak to the status of
this feature in their product line.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T02:48:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231214821.11149.00001931@mb-m11.aol.com>`
- **References:** `<m1nIb.12341$lo3.9191@newsread2.news.pas.earthlink.net>`

```

William M. Klein, the encyclopedia,  states
 
<<
Not true in the 2002 COBOL Standard with "call prototypes" and "repositories".
In such cases, you explicitly tell it what "call prototype" to use for a CALL
statement and parameters are checked AT COMPILE TIME to see if you are
"passing"
the correct type of fields.  With strong typing (also added in the 2002
Standard) this can be QUITE specific checking - or it can be just "length and
category" checking.  It is "up to you" when you create your call prototype.


>>

Definitely news, and good news.

Thanks!
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-31T15:22:48+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bsupk8$q66$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com> <VA.000003ad.013e526b@ieee.org> <vwmIb.5925$Vl6.1500752@news20.bellglobal.com>`

```

On 30-Dec-2003, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:

> Nice idea.  Unfortunately, most of the Cobol systems I work on were
> designed twenty years ago. Adding something like an OCX object that
…[3 more quoted lines elided]…
> to a year.

How many hundreds (thousands?) of print routines are you talking about?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-31T11:30:08-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VSCIb.9816$Vl6.1939829@news20.bellglobal.com>`
- **In-Reply-To:** `<bsupk8$q66$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com> <VA.000003ad.013e526b@ieee.org> <vwmIb.5925$Vl6.1500752@news20.bellglobal.com> <bsupk8$q66$1@peabody.colorado.edu>`

```
Howard Brazee wrote:
> On 30-Dec-2003, Donald Tees <donald_tees@nospam.sympatico.ca> wrote:
> 
…[9 more quoted lines elided]…
> How many hundreds (thousands?) of print routines are you talking about?

About 150 reports
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-31T17:32:09+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003bb.01b16d3e@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <vwmIb.5925$Vl6.1500752@news20.bellglobal.com>`

```
Donald,

> Adding something like an OCX object that 
> allows invoices to be faxed as part of the batch run, rather than 
> printed, might take two weeks the first time.  Redesigning the basic 
> print routines to do the same thing in Cobol would probably take closer 
> to a year.

Well, you wouldn't do that, would you? It depends on your print routines, 
but I'd try to intercept the printed forms after the program had created 
them rather than modify the programs at all. They don't print direct to a 
printer do they? That was a bad idea even thirty years ago.


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-31T16:10:51-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3_GIb.10446$Vl6.2055617@news20.bellglobal.com>`
- **In-Reply-To:** `<VA.000003bb.01b16d3e@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <vwmIb.5925$Vl6.1500752@news20.bellglobal.com> <VA.000003bb.01b16d3e@ieee.org>`

```
Doug Scott wrote:
> Donald,
> 
…[20 more quoted lines elided]…
> 

That is what the OCX object was for.  The cruncher, though, is that the 
FAX number has to come out of the system database, and whether they 
actually got there has to go back into the the data base after the fax 
queue empties.  That sort of back and/forth interaction is where OOP shines.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T02:36:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231213619.11149.00001929@mb-m11.aol.com>`
- **References:** `<vwmIb.5925$Vl6.1500752@news20.bellglobal.com>`

```
 Donald Tees donald_tees@nospam.sympatico.ca 
Date: 12/30/03 4:54 PM EST
Message-id: <vwmIb.5925$Vl6.1500752@news20.bellglobal.com>

opins with great force

<<
(snips) ...
In fact, the exact opposite is true regarding passed parameters in 
Cobol.  The only way that an arguement *can* be checked against a 
calling sequence is at run time. If you use OOP, the symbol table of the 
called program is passed in the repository to the calling program, and 
incompatablities are checked during compile. They will generate compile 
time errors.

Donald


>>


Donald is on a tack here that is money money money. We need to do a better job
for the workers in COBOL enviroments.  We need to get the standard into the
modern world. We need the declaration capability.

We need to think through the USING clauses at both ends of the CALLS and
INVOKES.

We have a problem.  We do not enumerate _items_ in our interfaces in vast
portions of the legacy code.  

We could implement type checking in the compilers for itemized lists in the
USING clauses, if the programmer will itemize. Not done yet, can be done. That
is work for the compiler writers, not to be trivialized.

That is work, but the intellectual challenge is to deal with big fat
interafaces at 01 levels in legacy code, and how to provide anything like type
checking for new code that intends to expoit the wide bandwidth interface
coding techniques of olde. This is not a small problem.

We are up to this tasks but we need to look at it as our prolem that we own. We
are the one's who interface with structs. How the heck do you type check that?
Especially if it has the efficiency magnifying aspects of ODOs and REDEFINES,
and soon, arbitrary precision decimal? 

Not a small consideration really. But it is worth being the champion of rather
than the victim of.  After all COBOL is venerable, as are it's practicioners.

Pray tell, how to do this stuff.

Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-30T14:32:20+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003af.013e5b38@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <VA.0000039e.0073e178@ieee.org> <Kb3Ib.3832$Vl6.983919@news20.bellglobal.com>`

```
Donald,

> And you think there are no methods involved in OOP?

I don't know where you got that from. I have studied and implemented OO 
systems, so I do know the methods involved on both sides - and I see 
little significant difference in the techniques. Different names, 
different emphases, but nothing of great significance, if you're doing 
the job right.

> That is, an ordinary cobol program is simply an 
> instance of the generic class "cobol program".

I don't know how such a definition can contribute to any debate.



---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T02:11:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231211152.11149.00001927@mb-m11.aol.com>`
- **References:** `<Kb3Ib.3832$Vl6.983919@news20.bellglobal.com>`

```

 Donald Tees
has it when he says

<<
The "MOVE" statement is a polymorphic method that is 
completely different depending on the class(s) of the operands.
>>

Spin it as polymorphic or operator override, or 'we will take care of it for
you', the thing about a Hopper machine is it has it built in so that you can
just DO IT.

We want programmers to do it!

Get it done. Don't theorize. Do it.

Override it, polymoriphizise it, or gizmosisize it. Just get it done on time.

The best tool is a tool that allows individual human persons to think clearly
and in a way that relates to the problem. And the problem in most cases of
business applications ain't fancy. But it is sometimes fancy. We got no problem
with this kind of distinction, ya' seez.  'Cause and all we is COBOLers we got
a flatlander tool and  recursur (my koind mind ya'), and an objectifier. We can
do it all, and there just aint' a compiler like ours.

So, dummies. Do not resist the extension of our productivity tools to the
_laborers_ who can think frigin' object, that is what the flow is from da
universities and all.  Let 'em code. Just finish on time. And don't  "wrap"
things so deep that we can't find 'em at two in the mornin'. Verstands Thee.

Now off with ya'.  Da veep has called me to discuss somethin' in-portant.

Have a really good nu years.

Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-29T23:07:44+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<4t2Ib.25296$Pg1.21058@newsread1.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com>`

```
For some "studies" on this question, see some IBM publications from when they
introduced "CUA" (Common User Access) to replace the (then almost universal in
IBM shops) ISPF-like interfaces.

If you search IBM studies for
   "IBM"
   "object-action"
   "action-object"

You will see a lot of discussions of how BOTH "end users" and "programmers"
(were THOUGH to?) prefer thinking in
   Select an Object first, and then the action you want to perform on it (new
paradigm)
        rather than
   Select an action you want to perform and then decide which object you want to
perform this upon (old paradigm)

All these years later and IBM mainframe programmers (and green screen end-users)
STILL tend to prefer (as far as I know) the "Action-Object" paradigm.  However,
my GUESS is that this is (like so much of this discussion) "what I am used to"
and NOT what "should be".
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-30T14:32:19+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003ae.013e58f3@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <4t2Ib.25296$Pg1.21058@newsread1.news.pas.earthlink.net>`

```
William,

> my GUESS is that this is (like so much of this discussion) "what I am used to"
> and NOT what "should be".

I think "Object/Action" works eminently well at a higher level. The attraction 
of OO for me lay in that concept of design refinement, breaking down an 
object/action pair to lower and lower levels.

But at the lowest level, the machine works Action/Object, and it is that 
translation which causes so many problems, particularly when automatically done, 
say by a compiler. That's why I suggest that a more efficient use of the OO 
paradigm is within design, rather than implementation.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2003-12-30T16:58:33-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<BAmIb.5971$Vl6.1502367@news20.bellglobal.com>`
- **In-Reply-To:** `<VA.000003ae.013e58f3@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <VA.0000038e.029700dc@ieee.org> <0f814fb5004880699dc9a660a8746294@news.teranews.com> <4t2Ib.25296$Pg1.21058@newsread1.news.pas.earthlink.net> <VA.000003ae.013e58f3@ieee.org>`

```
Doug Scott wrote:
> William,
> 
…[20 more quoted lines elided]…
> 

Now that I would agree with.  Which is precisely why I made the 
statement that a standard program is a method within a class of 
"programs".   The system architecture of most VAR systems that I have 
seen in the last thirty years is far closer to the standard OOP model 
than it is to the traditional top down menu program calling sub-modules 
and passing system parameters methodolgy that I have seen/used in the past.

Donald
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** Kevin Hansen <khansen@screenio.com>
- **Date:** 2003-12-28T00:08:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com>`

```
On Sat, 27 Dec 2003 15:43:42 GMT, "Judson McClendon"
<judmc@sunvaley0.com> wrote:

>Bill, the difference is in the way the programming model is abstracted.
>Pardon my digression, but I think it may be informative to many here.
…[12 more quoted lines elided]…
>detail, and simply couldn't cope with it.

(snip)
============
Exceedingly well put, Judson.

You know, the major problem with adopting OO is that it's, well, too
hard to grasp.  There's too high a degree of abstraction, if you will.

OO is shrouded in (my opinion) obscure concepts and terminology, and
requires a fair bit of effort to get your brain wrapped around it.
You can't simply start writing OO, you need to "see the world in a
different way" before you can use it.  It requires a radical shift in
your thinking to use it.  You can't gradually adopt OO, it's an
all-or-nothing commitment.  

View any of the threads where folks try to explain it.  You simply
cannot explain OO easily.  This is a major obstacle to adopting OO.
If the benefits were obvious, everyone would use it.  But, they're not
at all obvious, even to experienced and open-minded developers.

Just about any programmer can see the benefits of structured
programming; it's simple and easy to understand.  The paradigm is
obvious.
 
Good paradigms need to be both simple and obvious.  Regardless of how
wonderful it is - and it surely is for some applications - OO is
neither simple, nor obvious.  That's why we're not all rushing to
adopt it.

Or, maybe I'm just getting too old to learn new tricks.  ;-)

Kevin

Develop Windows(tm) Applications - in COBOL!
http://www.ScreenIO.com
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-29T10:34:29+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3fef4cd8_7@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com>`

```

"Kevin Hansen" <khansen@screenio.com> wrote in message
news:hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com...
> On Sat, 27 Dec 2003 15:43:42 GMT, "Judson McClendon"
> <judmc@sunvaley0.com> wrote:
>
<snip>
> Exceedingly well put, Judson.
>
(I'm not so sure I totally agree with Judson's treatise on abstraction, but
don't disagree strongly enough to bother arguing it. It is certainly true
that abstraction is necessary to implement OO, but it is to implemnet good
COBOL systems too...)

> You know, the major problem with adopting OO is that it's, well, too
> hard to grasp.  There's too high a degree of abstraction, if you will.
>

Yes, I agree that is so, for the majority of COBOL programmers. It isn't
necessarily the degree of abstraction that makes it hard; it is the fact
that it is a whole new way of looking at things.

> OO is shrouded in (my opinion) obscure concepts and terminology, and
> requires a fair bit of effort to get your brain wrapped around it.

Agreed. And I regret this necessity. There IS too much terminology (jargon,
if you like)  attached to it. This is historical and is necessary so
acadamics can argue esoteric points of computer programming. The fact is
that there ARE some different concepts (and some subtle, but very important
changes to existing ones...), and they have to have names so they can be
discussed. Unfortunately, it was CS scholars who got to name them <G>. I
avoid using the jargon when introducing people to OO and show the concepts
by example instead. Once people have implemented a successful OO system they
can THEN relate these terms to the respective areas of what they did.


> You can't simply start writing OO, you need to "see the world in a
> different way" before you can use it.  It requires a radical shift in
> your thinking to use it.  You can't gradually adopt OO, it's an
> all-or-nothing commitment.
>

Yes. Very well put. However, you don't "forget" what you previously knew, so
you now have an option to use your new OO knowledge AND/OR apply your
previous knowledge, accepting that they are separate and distinct paradigms.

> View any of the threads where folks try to explain it.  You simply
> cannot explain OO easily.  This is a major obstacle to adopting OO.
> If the benefits were obvious, everyone would use it.  But, they're not
> at all obvious, even to experienced and open-minded developers.
>

I know this from experience. Please see my post in this thread which
mentions eagles...

> Just about any programmer can see the benefits of structured
> programming; it's simple and easy to understand.  The paradigm is
> obvious.
>
> Good paradigms need to be both simple and obvious.

No, I disagree here. It would appear so on first glance but think a little
more about what you said. What if the "good" paradigm simply ISN'T simple OR
obvious? You would then argue that it isn't a good paradigm. But it might
offer benefits far beyond anything previous. (Consider General Relativity,
f'r'instance...Compared to Newton's simple Laws (which were adequate enough
to land men on the moon and send probes into deep space) it is neither
simple, nor obvious. Yet it is more comprehensive than Newton and explains
the creeping shift in the orbit of Mercury (for example) that Newton's Laws
could not...Would you wipe Einstein because it is complex, or different from
what came before?). I would restate your position as: "It is helpful if good
paradigms are simple and obvious; but being so is not a necessity for a good
paradigm."

In OO terms, people who have no previous experience of programming DO find
it simple and obvious. It is all relative.


> Regardless of how
> wonderful it is - and it surely is for some applications - OO is
> neither simple, nor obvious.  That's why we're not all rushing to
> adopt it.
>

I'm sure that is one of the major reasons, and you have expressed it
succinctly. It has bothered me for some time why there is such resistance on
the part of the COBOL establishment; I believe this is probably the nub of
it. Not everybody rushes to accept new challenges or acquire new knowledge,
and if this task is perceived to be "difficult",  there is even less
enthusiasm for it.

> Or, maybe I'm just getting too old to learn new tricks.  ;-)
>

Whether that is true or not, Kevin, thank you for an excellent post.

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** Kevin Hansen <khansen@screenio.com>
- **Date:** 2003-12-29T05:44:17+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<jrbvuv4p85c9njii0vho6nljvm1ftt4pgr@4ax.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com>`

```
On Mon, 29 Dec 2003 10:34:29 +1300, "Peter E.C. Dashwood"
<dashwood@enternet.co.nz> wrote:

>> Just about any programmer can see the benefits of structured
>> programming; it's simple and easy to understand.  The paradigm is
>> obvious.
>>
>> Good paradigms need to be both simple and obvious.

(snip)

>No, I disagree here.  I would restate your position as: "It is helpful if good
>paradigms are simple and obvious; but being so is not a necessity for a good
…[3 more quoted lines elided]…
>it simple and obvious. It is all relative.
-------
HI, Pete,

Your restatement is fair enough.  I was thinking in terms of the Real
World.  (It's really a matter of how you define "good," isn't it?)

Therefore, I'll suggest that in _practical_ terms a "good" paradigm is
one that is capable of being understood - and willingly adopted - by
the majority of the target group - in this case, COBOL programmers.
OO, for a variety of reasons, is not.

I must confess that I find it odd - and a bit frustrating after 30
years of being, I think, a reasonably motivated and competent
programmer - that OO remains elusive.  

I imagine that if we were embarking on a Major New Project that we
would very likely look at OO.  As Judson pointed out, however, we'd
want to be convinced of the benefits of OO before we spent months
learning how it all works and then trying to implement our first OO
application.

You're undoubtedly correct regarding people with no previous
programming experience finding OO simple and obvious.  It's all about
your frame of reference, isn't it?

Interesting discussion, at any rate.

Regards,
Kevin

Develop Windows(tm) Applications - in COBOL!
http://www.ScreenIO.com
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** Arnold Trembley <arnold.trembley@worldnet.att.net>
- **Date:** 2003-12-29T07:02:41+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lkQHb.253198$Ec1.8774246@bgtnsc05-news.ops.worldnet.att.net>`
- **In-Reply-To:** `<jrbvuv4p85c9njii0vho6nljvm1ftt4pgr@4ax.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <jrbvuv4p85c9njii0vho6nljvm1ftt4pgr@4ax.com>`

```


Kevin Hansen wrote:

> (snip) 
> I must confess that I find it odd - and a bit frustrating after 30
> years of being, I think, a reasonably motivated and competent
> programmer - that OO remains elusive.

That's exactly the position I am in, although I have only been 
programming in COBOL for 25 years.  I don't "get" what an "object" is, 
and I certainly don't get what a "class hierarchy" is.

I certainly cannot argue against program re-use.  We re-use code all 
the time, with copybooks, called subprograms, and even by cloning 
programs (although I suppose this wrecks inheritance and polymorphism).

I am deeply suspicious of recursion, and I have read that almost any 
recursion algorithm can be adapted to simple iteration.  One of the 
most intelligent programmers I ever met (who also had mainframe 
experience) told me that it would be far better to study 
object-oriented analysis & design and then code in a procedural 
language than to jump into coding in an OO Language without the 
background in OO analysis & design.

At my age, the bosses seem to think my time is too valuable to spend 
in coding.  Naturally, I think they're wrong about that.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T17:45:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<7258afb54b163acc96b1cc53a5e0e3a5@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <jrbvuv4p85c9njii0vho6nljvm1ftt4pgr@4ax.com> <lkQHb.253198$Ec1.8774246@bgtnsc05-news.ops.worldnet.att.net>`

```
"Arnold Trembley" <arnold.trembley@worldnet.att.net> wrote:
>
> I am deeply suspicious of recursion, and I have read that almost any
> recursion algorithm can be adapted to simple iteration.

All recursive algorithms can be coded iteratively, and vice versa. I
like recursion where it fits well. Parts explosion (decomposing a
product into all its component parts) is a good example. I wrote one
recursively in COBOL once, and it was beautifully simple and
elegant. The client's COBOL programmers, who hadn't been exposed
to recursion before, marveled at the simplicity. Examine Ackermann's
Function (an artificial function created to be massively recursive) in
the small program below. It is very simple and elegant in recursive
form but, while not particularly difficult to code, looks like crud in
iterative form. :-)

(PS- If you don't believe that little sucker is *massively* recursive,
just compile and execute the program. It will run a little while and
blow the stack, doesn't matter what you run it on. It's not a bug, the
algorithm will theoretically run to completion every time, given an
infinite stack, infinite time, and maybe infinite parameter size. :)

/*
 *    **************************************************
 *    *                                                *
 *    *                   ACKER1.C                     *
 *    *                                                *
 *    *         Classical Ackermann's Function         *
 *    *                                                *
 *    *              Judson D. McClendon               *
 *    *              Sun Valley Systems                *
 *    *              4522 Shadow Ridge Pkwy            *
 *    *              Pinson, AL 35126-2192             *
 *    *                 205-680-0460                   *
 *    *                                                *
 *    **************************************************
 */

#include "stdio.h"
unsigned long Ackermann(unsigned long, unsigned long);
unsigned long m,n;

int main(void)
{
   printf("                       *** Ackermann's Function ***\n\n");
   printf("    N:   0      1      2      3      4      5      6      7      8      9\n");
   printf("M:\n");

   for (m = 0; m < 10; m++) {
      printf("  %d", m);
      for (n = 0; n < 10; n++) {
         printf(" %6u", Ackermann(m,n) );
         }
      printf("\n");
      }
   printf("\f");
}

unsigned long Ackermann(unsigned long m, unsigned long n)
{
   if (m == 0)
      return(n + 1);
   else if (n == 0)
      return(Ackermann(m-1,(unsigned long) 1) );
   else
      return(Ackermann(m-1,Ackermann(m,n-1) ) );
}
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T01:37:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231203708.11149.00001921@mb-m11.aol.com>`
- **References:** `<7258afb54b163acc96b1cc53a5e0e3a5@news.teranews.com>`

```
Waxing into the utter ether of computer science

"Judson McClendon" judmc@sunvaley0.com 
Date: 12/29/03 12:45 PM EST
Message-id: <7258afb54b163acc96b1cc53a5e0e3a5@news.teranews.com>

entertains that 

<<...
All recursive algorithms can be coded iteratively,
...>

Yeah.? Well maybe, but not by all persons. The issue is the labor force. Are
there algorithms that can be coded more easily as recursive expressions versus
iterative expressions?  Is it the case that some folks can indeed see the
algorithm at long last when they are thinking in recursive paradigms, whereas
they is utterly blind to it in flatlanderese?

Dijkstra asserted that bubble sort became 'visible' to the author (who was not
Dijkstra by the way) because of the recursive aspect of the programming surface
available in ALGOL, and that it was particularly recursion which made that
happen. 

I would assert, in opposition to your thought, that some folks can think the
algorithm in recursion and not think it in iteration and that is why the
availability of the tools of that genre matter. We need to make those workers
productive, and rip down the walls that would exclude them from business data
processing work. And that will begin to happen now in COBOL, and it is likely
to count since folks have money in front of them when they have the COBOL
compiler in front of them.

Although the RECURSIVE program ID has been around, there is not much literature
promoting it. There is a great deal of literature, and academic activity,
prompting use and study of all of the OO stuff, which happens to include
recursivity intrinsically.

Tools that can do recursion, and help the programmer think recursion are money
makers.  

But most application requirements are not recursive in the problem domain. Some
that are, .... and easily admitted ... can be and have been implemented by
iteration.  On the other side of the coin, and it is a money thing, there are
requirements that are better implemented as recursion. 

Apps with deep interst rate and return on investment challenges are really
recursive. We would be doing harm to businesses if we in anyway discouraged
recursion in these application areas, ... financial harm. Recursion is a
significant construct. Valuable! A money maker. Use it! Cathect it whenever
possible.

Recurse!

Best Wishes
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T11:34:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3ef6eaaa9e45664dc27e0ba792dbcd1@news.teranews.com>`
- **References:** `<7258afb54b163acc96b1cc53a5e0e3a5@news.teranews.com> <20031231203708.11149.00001921@mb-m11.aol.com>`

```
"RKRayhawk" <rkrayhawk@aol.com> wrote:
> "Judson McClendon" judmc@sunvaley0.com
> >
…[6 more quoted lines elided]…
> they is utterly blind to it in flatlanderese?

Yes, I agree. :-)

> I would assert, in opposition to your thought, that some folks can think the
> algorithm in recursion and not think it in iteration and that is why the
> availability of the tools of that genre matter.

I agree with you , I agree with your whole post.

Sorry if I gave another impression :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T01:18:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231201818.11149.00001917@mb-m11.aol.com>`
- **References:** `<lkQHb.253198$Ec1.8774246@bgtnsc05-news.ops.worldnet.att.net>`

```
Drawing our attention ever more deeply into the matter 

Arnold Trembley arnold.trembley@worldnet.att.net 
Date: 12/29/03 2:02 AM EST
Message-id: <lkQHb.253198$Ec1.8774246@bgtnsc05-news.ops.worldnet.att.net>

states 

<<
...

I am deeply suspicious of recursion,
...
>>

But are your recursively suspicious?

My concern would be rather, just exactly how is it that recursion is
suspicious, ... anyway?

Suspicious?

At any rate, I will take it on faith that you are only iteratively suspicious
of recursion. And rest ever so much more comfortably this new years eve.

Best Wishes,
Bob Rayhawk
RKRayhawk@aol.com
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T17:11:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c56bcaed067933d38e61b95c602f6a56@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> "Kevin Hansen" <khansen@screenio.com> wrote:
…[6 more quoted lines elided]…
> that it is a whole new way of looking at things.

I haven't pointed this out, and rarely do, because I don't want to offend
anyone. But all of us know COBOL programmers who, while fairly
productive in their little niche, simply would never, could never, master
the subtleties of C, not to mention the whole OO thing. They would quit
in frustration if required to do it. I consider this one of COBOL's best
attributes; simplicity. When you make programming tools so complex
and difficult to master (I think few would argue that OO does not have
a much steeper learning curve) that fewer and fewer people understand
them, you are reducing the pool of potential programmers, and taking
up more and more of their time in mastering their tools. In and of itself,
this is not a good thing. Observe the trend of technological innovation
and maturity. You see that new technology tends to be complex and only
utilized by a few fervent experimenter types. As the technology develops,
it eventually becomes simpler and simpler to use until it is considered
a consumer item (e.g. radio, the automobile, personal computers). You
have to know less to start and drive the latest Ferrari than you did to start
and drive a model T Ford, and considerably less than a Stanley Steamer.
Don't look now, but we aren't heading that way in IT, folks. While using
a PC for common tasks is much easier, our programming tools are
becoming much more difficult. How can we continue to produce more
and more complex and larger applications, on shorter and shorter time
frames, if at the same time our tools are becoming more and more
difficult? There is a wall there somewhere that we're going to hit if we
continue this trend. People are not getting smarter. If you doubt it, read
the Federalist Papers sometime and consider the authors were common
farmers of the late 18th century. So, if OO is a lot more complicated,
and it is a lot more difficult, than it had better be considerably more
productive, or we have gone backward.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-29T18:14:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bspquo$n88$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com>`

```

On 29-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

>  You
> have to know less to start and drive the latest Ferrari than you did to start
…[11 more quoted lines elided]…
> productive, or we have gone backward.

I'm not sure I agree here.   OO is a tool that can handle problems we didn't try
to handle in the old days.   We don't simplify how we use our cars so that we
can drive them to the moon, but instead we find more complex tools to go to the
moon.   Complex tasks often require complex tools.

On the other hand, just because someone has fallen in love with the capacities
of a moon rocket doesn't mean he should use it to take the kids to the park.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T20:31:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<707196c58ce60372abbe66514aca5aea@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <bspquo$n88$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> I'm not sure I agree here.   OO is a tool that can handle problems we didn't try
…[5 more quoted lines elided]…
> of a moon rocket doesn't mean he should use it to take the kids to the park.

Good point, I agree. Undoubtedly, OO is good for some things. It is this
lemming like stampede to "OO and nothing else or die" that concerns me.
I wouldn't vote to stamp OO out. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-29T15:07:46-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0312291507.42879223@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote 

> You
> have to know less to start and drive the latest Ferrari than you did to start
> and drive a model T Ford, and considerably less than a Stanley Steamer.

That's just not true.  What has to known is _different_, but I would
say that the Ferrari would be far more complex, more confusing with
more dials and controls than the other two.  The Stanley would be far
simpler to drive, it does not have gears.  The Ferrari has 3 controls
just for the gear box and is only 'obvious' if you already know how
they will work.

> Don't look now, but we aren't heading that way in IT, folks. While using
> a PC for common tasks is much easier, our programming tools are
…[3 more quoted lines elided]…
> difficult? 

Why exactly are your tools becoming more 'difficult', mine aren't.

Certainly the more complex and larger applications are more difficult
to do, but the tools are just the same.  They built the Panama canal
with shovels and wheelbarrows, if new tools are too difficult then
don't use them.

> So, if OO is a lot more complicated,
> and it is a lot more difficult, than it had better be considerably more
> productive, or we have gone backward.

As I may have briefly mentioned a few times before: much of the OO
features of C++ were designed to overcome problems in C that Cobol
never had.  Some of the original OO features (eg in Simula) were also
to abstract programming problems that do not occur in most business
applications (eg simulations).

OO also has a very real place in systems that require arbitrary
multiple instances of the same or similar objects.  Such things as
GUIs where many controls are required and these have specific
behaviours.

In systems that do repeated iteration though a single instance (eg
transactions processed sequentially) then OO is not necessarily
applicable.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-30T15:00:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote
>
…[9 more quoted lines elided]…
> they will work.

Perhaps 'Ferrari' was a bad example. Substitute 'automobile' instead,
it is a better analogy anyway. But you don't have to know ALL the
controls to start and drive either one. :-)

Stanley Steamer: You don't have to obtain water and fuel, fire up the
thing and wait for steam every time you start a modern vehicle. You
must know that these things are required, and how to do them, in order
to start a Stanley Steamer.

In a modern automobile, you only need to know how to start the
engine (insert and turn key), put it in gear (move gearshift lever)
and what the accelerator, brakes and steering wheel do. You have
to know all this except the starter to start and run a model T, plus
you have to know how to (literally) crank the engine, set the spark
and do a manual shift. If you don't understand how to set the spark,
you will likely get a broken arm when the engine backfires while
you are cranking it. A common injury in those days. Many people
now don't even know how to drive a manual shift transmission. :-)

> > Don't look now, but we aren't heading that way in IT, folks. While using
> > a PC for common tasks is much easier, our programming tools are
…[10 more quoted lines elided]…
> don't use them.

Mastering C++ or VB or Java is orders of magnitude more difficult
than mastering COBOL, even as a first language. Not to write a
"Hello World" program, but mastering them. Using them, once they
are mastered, is not necessarily more difficult, but requires more
ongoing research to answer questions like "what component does
this function?" A brief glance at the MFC manuals should assure
anyone of that (if anyone has the complete MFC, Win32 API and
all the characteristics of all the objects they are likely to have to
deal with down pat, I admire their stunning accomplishment :). And,
at least in the volatile Windows environment, your target API gets
rewritten every few years by Microsoft. This and other rapidly
changing tool definitions require significantly more time and effort
to maintain your skill level. More time learning means less time
producing. Surely, few would debate this. :-)

It's not a question of the tools being "too difficult," it is a question
of the cost of this extra overhead compared to the benefits gained.
The business world should always make decisions based on ROI.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T16:03:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bss7jp$hbt$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com>`

```

On 30-Dec-2003, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> Mastering C++ or VB or Java is orders of magnitude more difficult
> than mastering COBOL, even as a first language. Not to write a
> "Hello World" program, but mastering them.

How many commands/words do we have to know for CoBOL, not counting in-house
calls?

How many commands/words do we have to know any library based language not
counting in-house objects?

There's no comparison.   And the word "STRING" will always have the same meaning
with CoBOL, no matter how it is compiled or run.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-12-30T21:47:23-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-452F1C.21472330122003@corp.supernews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <bss7jp$hbt$1@peabody.colorado.edu>`

```
In article <bss7jp$hbt$1@peabody.colorado.edu>,
 "Howard Brazee" <howard@brazee.net> wrote:

> How many commands/words do we have to know for CoBOL, not counting in-house
> calls?

Only one.

When running on IBM iron with Cobol wither "Quickref" or "BookRead".

When running on Win32 I recommend "MSDN".
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-30T11:39:48-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0312301139.27aca7a7@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote

> Perhaps 'Ferrari' was a bad example. Substitute 'automobile' instead,

Well I am sure that you can switch to something else yet again to try
to maintain your argument.

> it is a better analogy anyway. But you don't have to know ALL the
> controls to start and drive either one. :-)

Don't you ?  Which ones don't you need to know and how do you tell
whether it is needed or not ?  You are merely using your familiarity
to assume that what you know is 'easy' and what you don't know is
'hard'.
 
> Stanley Steamer: You don't have to obtain water and fuel, fire up the
> thing and wait for steam every time you start a modern vehicle. 

I didn't know that a Ferrari didn't need fuel.

But you did not need those with the more recent Standley Steamers
which were fitted with flash boilers.  Compared to contemporary
automobiles they were easier to drive and started within 30 seconds
using fuel from the fuel tank. They weren't wood fired you know.

> You
> must know that these things are required, and how to do them, in order
> to start a Stanley Steamer.

I actually have some technical documentation from the 50s about
Stanley and other steam cars.  My father was interested in building
one at the time.
 
> In a modern automobile, you only need to know how to start the
> engine (insert and turn key), put it in gear (move gearshift lever)
> and what the accelerator, brakes and steering wheel do. 

Do you ?  How do you _know_ that ? -->  experience.

Why do you think a Stanley or Model T is hard ? --> inexperience.

> You have
> to know all this except the starter to start and run a model T, plus
> you have to know how to (literally) crank the engine, set the spark
> and do a manual shift. 

No. Wrong.  Model Ts did not have 'manual', they had a planetary
gearbox with a change pedal and automatic clutch.  No harder to use
than knowing to put the autoshift to 'D' rather than 'R', or not
knowing that it was not one of the controls that could be ignored and
leaving it in 'P'.

Model Ts were designed to be used by people who had never driven
before and could be taught by the dealer to drive away after 5
minutes.

> If you don't understand how to set the spark,
> you will likely get a broken arm when the engine backfires while
> you are cranking it. A common injury in those days. Many people
> now don't even know how to drive a manual shift transmission. :-)

And if you don't know not to put the gear in 'P' when moving ...

Starting a Model-T is just a sequence of operations: move this lever
here, operate this toggle (fuel pump) 3 times, turn on key, turn crank
once slowly, then pull hard.

For your car you don't need a written sequence of what to do, you
probably don't even notice you are doing it: gear to Neutral, key in,
seat belt on, press accelerator down (to set auto-choke), turn key to
start.

It is just a sequence, you just learn it.

I don't drive automatics.  When I have had to use them in the past I
founded them 'hard' to use (due entirely to unfamiliarity).

However I have, in my youth, had a car with a Wilso pre-selector
planetary gearbox and automatic cluth that did, from time to time,
need crank starting and had advance/retard and hand thottle.

I would find a Modsel T easy to drive.

> Mastering C++ or VB or Java is orders of magnitude more difficult
> than mastering COBOL, even as a first language. 

Again you are basing this on your experience.  Cobol is 'easy' because
you done it for xx years.  You may well find C++ hard, until you've
done it for a while.

Over the last week I've had to write a complete cgi application in
Perl/MySQL because the hosting site does not run my preferred
Python/PostgreSQL.  I've avoided Perl in the past, but it is just
another language.  Languages one is familiar with are easy, ones
unknown are hard.

It may well be that moving from Cobol to C++ (or Java) is really hard
because it includes unlearning all the Cobolish things that clutter
one up.  But starting without pre-conceived ideas about how a language
_should_ work would make most of them equally hard/easy.

> Not to write a
> "Hello World" program, but mastering them. Using them, once they
…[5 more quoted lines elided]…
> deal with down pat, I admire their stunning accomplishment :). 

All those APIs are _not_ part of the language and are used equally
whatever language is used.  I have written extensive Windows API
programs in Cobol, and not just dialog boxes but graphical
representations of container ships and stability and strength curves,
even with 'the view from the helm' in perspective over the actual
container loading taking into account the trim of the ship (actually
the view could be from anywhere and there was a 'cookie' that changed
viewpoint from 1000 metres aft and off to one side to do a 'flyby').

Yes, Java is huge too, but if you wanted to do all those things in
Cobol it would be just the same.  How do you do EMails ? run ftp ?
create spreadsheets ? access distributed databases ?

Or are you saying that Cobol is easy because it only does batch
updates and the odd report to a line printer ?

> And,
> at least in the volatile Windows environment, your target API gets
…[3 more quoted lines elided]…
> producing. Surely, few would debate this. :-)

But Windows API is not C++ nor Cobol, nor Java, nor Python.  It is
something that any of those can use.  Or it is something that need not
be used.
 
> It's not a question of the tools being "too difficult," it is a question
> of the cost of this extra overhead compared to the benefits gained.
> The business world should always make decisions based on ROI.

Of course.  I would agree that for business applications (ie
accounting) the Windows API is not required.  It is better to have a
decent text mode environment.  IMHO CICS is not.  I also think that it
would be much harder to master CICS (which I never used but I do know
how it works) than, say, VB.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2003-12-30T20:40:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bssnrr$1ts$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <217e491a.0312301139.27aca7a7@posting.google.com>`

```

On 30-Dec-2003, riplin@Azonic.co.nz (Richard) wrote:

> Of course.  I would agree that for business applications (ie
> accounting) the Windows API is not required.  It is better to have a
> decent text mode environment.  IMHO CICS is not.  I also think that it
> would be much harder to master CICS (which I never used but I do know
> how it works) than, say, VB.

I've worked with CICS before (not recently), but never learned how it works.  
It seemed to break some rules as far as I could tell.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-31T21:04:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5663465d0f6725af9810e600b4ea92ad@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <217e491a.0312301139.27aca7a7@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote
> > Perhaps 'Ferrari' was a bad example. Substitute 'automobile' instead,
>
> Well I am sure that you can switch to something else yet again to try
> to maintain your argument.

Just a poor selection of vehicles, Richard, not a change in position. :-)

> > it is a better analogy anyway. But you don't have to know ALL the
> > controls to start and drive either one. :-)
…[4 more quoted lines elided]…
> 'hard'.

I don't believe you HAVE to know how to use the cigarette lighter or
the radio to start and drive the thing 100 feet across an empty parking
lot, but what do I know? You're being picky, Richard. ;-)

It seems I did not make myself clear, so I will try to be make a specific
example. Imagine you have two automobiles, sitting side by side, both
oriented in the same direction, at one end of an otherwise empty, level,
paved, parking lot. One of these vehicles is a typical modern automobile
with an automatic transmission, the other is a model T Ford or a Stanley
Steamer (take your pick). Both vehicles are in good operating condition,
have fuel, oil and any other expendables, but have been sitting parked
for 24 hours. You have an adult person standing there who understands
your language, but knows nothing about how to start or drive an automobile.
You want the person to move one of the vehicles to the other end of the
parking lot using this procedure: start vehicle, drive vehicle to other end
of lot, park vehicle. You only need to tell them enough to do this one task.
I submit that you would have to do less instruction for them to do the task
with the modern automobile than with either the model T or Stanley.

> > Stanley Steamer: You don't have to obtain water and fuel, fire up the
> > thing and wait for steam every time you start a modern vehicle.
>
> I didn't know that a Ferrari didn't need fuel.

Not that you have to chop down, chop up, haul, place in a firebox,
and ignite, no. :-)

> But you did not need those with the more recent Standley Steamers
> which were fitted with flash boilers.  Compared to contemporary
> automobiles they were easier to drive and started within 30 seconds
> using fuel from the fuel tank. They weren't wood fired you know.

I understood that the early ones were. I knew about the flash boilers.
Even using fuel from a tank, would you not have to know to, and how
to, turn the fuel on and off? I'm not attacking the thing, Richard, I just
said automibiles today are simpler to operate. :-)

> > In a modern automobile, you only need to know how to start the
> > engine (insert and turn key), put it in gear (move gearshift lever)
> > and what the accelerator, brakes and steering wheel do.
>
> Do you ?  How do you _know_ that ? -->  experience.

Yes, I have just taught my youngest daugther how to drive, so I have
recent experience. :-)

> Why do you think a Stanley or Model T is hard ? --> inexperience.

I didn't say it was 'hard', I said you have to know more. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-01T13:13:38-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0401011313.78a5dd8d@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <217e491a.0312301139.27aca7a7@posting.google.com> <5663465d0f6725af9810e600b4ea92ad@news.teranews.com>`

```
"Judson McClendon" <judmc@sunvaley0.com> wrote 

> > Don't you ?  Which ones don't you need to know and how do you tell
> > whether it is needed or not ?  You are merely using your familiarity
…[5 more quoted lines elided]…
> lot, but what do I know? You're being picky, Richard. ;-)

No. I am not being picky (or no more so than I usually am).  How do
you know that you don't need to use that knob marked with bit of smoke
? or what it is ?  You are using your experience to claim that one
thing is easy and the other is hard, but that 'hard' bit is purely
inexperience.
 
> It seems I did not make myself clear, so I will try to be make a specific
> example. Imagine you have two automobiles, sitting side by side, both
…[11 more quoted lines elided]…
> with the modern automobile than with either the model T or Stanley.

And I disagree that, especially for the Model T, there would be any
significant difference to get them _safely_ to the other side.

But your conditions are meaningless.  This is like a test to se which
language can display 'hello world' in the fewest source code lines.

> Not that you have to chop down, chop up, haul, place in a firebox,
> and ignite, no. :-)

I think that what you imagine a Stanley Steamer to be is confused.

> I understood that the early ones were. I knew about the flash boilers.
> Even using fuel from a tank, would you not have to know to, and how
> to, turn the fuel on and off? 

In exactly the same way that you would need to know, say, how to move
from 'P' to 'N' and to 'D' at the appropriate times.  You
_already_know_that_.

> I'm not attacking the thing, Richard, I just
> said automibiles today are simpler to operate. :-)

It is always 'simpler' to use things that you know how to use.

If I tried to drive your car I would find it (initially) complex and
difficult, partly because I don't drive automatics, but mostly because
it would have controls and dials in different places than I am used to
and I wouldn't know which were relevant.

> I didn't say it was 'hard', I said you have to know more. :-)

No. You don't have to know 'more', you have to know 'different'.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T22:07:48+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<363f5209eb5d20eee079385eba2f663b@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <217e491a.0312301139.27aca7a7@posting.google.com> <5663465d0f6725af9810e600b4ea92ad@news.teranews.com> <217e491a.0401011313.78a5dd8d@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote
> >
…[19 more quoted lines elided]…
> language can display 'hello world' in the fewest source code lines.

Most benchmarks are meaningless, Richard. They are contrived situations
narrowly tailored to measure specifically the areas of interest. :-)

> > Not that you have to chop down, chop up, haul, place in a firebox,
> > and ignite, no. :-)
>
> I think that what you imagine a Stanley Steamer to be is confused.

You may be right there. I am not an expert on early 20th century
automobiles. I have disassembled and reassembled significant parts
of late 20th century automobiles, but no Stanley Steamers. :-)

> > I didn't say it was 'hard', I said you have to know more. :-)
>
> No. You don't have to know 'more', you have to know 'different'.

Having to know 5 things is having to know more than having to know
4 things. ;-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 12)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-12-30T21:44:43-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-B7489D.21444230122003@corp.supernews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com>`

```
In article <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com>,
 "Judson McClendon" <judmc@sunvaley0.com> wrote:
<snip>
> Mastering C++ or VB or Java is orders of magnitude more difficult
> than mastering COBOL, even as a first language. Not to write a
…[11 more quoted lines elided]…
> producing. Surely, few would debate this. :-)

It sounds like you are confusing apples and skateboards.

MFC and the Win32 API have no more relationship to C++, VB and Java than 
Cobol has to BMS maps and the CICS API.

I would strongly disagree -- more time learning means a more productive 
programmer in the future, including the immediate future next-few-days.

At the very least, a programmer should always take the time to read the 
"what is new" bullet list in the compiler / tools / operating system 
documentation.  So they can avoid the problem of "productivly" spending 
days or weeks creating things that an OS or language facility provides 
with a simple call.
  
Two real world examples from my day at work:

   - a programmer in an mostly IBM Mainframe with LE shop spent hours  
"productively" exaustively coding file status checks, only to find that 
something was just out of wack.  Had she read the fine manual and simply  
removed the file status checking, LE would have identified her problem 
and suggested corrective action very quickly.  Instead she 
"productively" reinvented the wheel all day long.

   - another programmer in the same neck of the woods was looking to 
"rewrite" a well-written, well-tested, high-performance collection 
class.  The stated reason for the rewrite was to allow the code that was 
already leveraging the collection class in an IMS/BMP environment to be 
used in a CICS/TS environment.  Again, had said programmer checked the 
fine manual they would have found that said collection class was 
available, tested and functional in said CICS/TS environment for almost 
a decade, saving a 3 hour design meeting.

Just two little stories where a very little bit of time spent "learning" 
could have prevented hours of "productivity".
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-31T21:12:35+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<c09ef0959aa3017b711788f8948d270b@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote:
> "Judson McClendon" <judmc@sunvaley0.com> wrote:
> <snip>
…[18 more quoted lines elided]…
> Cobol has to BMS maps and the CICS API.

True, but all are 'programming tools' used in the vast majority of currrent
programming environments, are they not? :-)

> I would strongly disagree -- more time learning means a more productive
> programmer in the future, including the immediate future next-few-days.
…[5 more quoted lines elided]…
> with a simple call.

I'm not saying that anyone should skimp on learning what they need to
know, Joe. I am saying that the newer 'programming tools' require
*more* study to achieve and maintain the *same* level of proficiency.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2003-12-31T19:39:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-C58612.19391131122003@corp.supernews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com>`

```
In article <c09ef0959aa3017b711788f8948d270b@news.teranews.com>,
 "Judson McClendon" <judmc@sunvaley0.com> wrote:

> > I would strongly disagree -- more time learning means a more productive
> > programmer in the future, including the immediate future next-few-days.
…[9 more quoted lines elided]…
> *more* study to achieve and maintain the *same* level of proficiency.

I just think you have it backwards.

Newer tools tend to have more pre-tested, out-of-the-box functionality.  
Thus they require less effort on the part of the programmer to 
accomplish the same result.  The end result is that the *same* level of 
proficiency generates orders of magnitude *more* productivity.

I was noticing this today as I tuned a .NET application -- network 
performance was ok, but some files were kinda dragging.  My fix was to 
squeeze a nicely abstracted buffered stream object in between my custom 
streams parent and the file stream object.  About a 20 character fix.

Now you could argue that the few hours or so I spent learning about the 
.NET (or Java) IO model were "unproductive".  But consider the 
alternative.  I could have tweaked the OS to grab a few unused bytes for 
another buffer, then squeezed a patch in next to the OS code that 
operates the  stepper motors on the disk drives to make use of my new, 
expanded, buffers?  That was the solution to the same problem 20 years 
ago.

Several days of productively doing things the old way?  Or several hours 
of learning followed by a few seconds of productively doing things the 
new way.

All of todays tools are better than they were yesteryear, and huge leaps 
and bounds better than yesterdecade.  To not stay proficient in those 
things will cost you more in productivity.

<Dragging back to a Cobol-like topic/>
I often find myself explaining what a "Function" is to otherwise 
proficient Cobol programmers.  And this newsgroup erupts pretty 
frequently with discussions of the usefulness of "Evaluate"-vs-"nested 
ifs"***.

Sure, those folks can write just fine without those -- but they are 
cheating themselves of the time savings and ease of use offered by the 
new features.  OO is a great example of this.




***(Just think how much productive time the readers of this group have 
saved by not having to wade through the unmached-endif thread from few 
months ago)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 15)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T11:58:34+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a85c350e6a7b57908feb824c303367f2@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com> <joe_zitzelberger-C58612.19391131122003@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote:
>  "Judson McClendon" <judmc@sunvaley0.com> wrote:
> >
…[9 more quoted lines elided]…
> proficiency generates orders of magnitude *more* productivity. ...

Perhaps you are correct, Joe. But the productivity and effectiveness
statistical data I have seen don't really support what you say. A
failure rate in developing and implementing new systems of near
50% (42%-45%) because of "cost and time overruns and failures to
meet design goals" is *not* impressive. Even a 10% failure rate from
technical deficiencies is unacceptable, IMHO. If this is a distortion,
I would be happy to see better statistics to prove it. :-)

Understand, when you say what you do above, I'm sure you believe it.
And you may be right. But how do you or I know for sure that your
impression, from your own anecdotal evidence, is correct or even
reflects the situation industry wide? Have you inadvertently omitted
other evidence to the contrary? It is a universal human characteristic
to tend to see evidence that supports our view more clearly than
evidence to the contrary. It takes a real conscious effort to be objective.
The *only* way to know this *for sure* is to gather productivity and
effectiveness statistics on a broad range of actual projects using both
new and older tools. Believe me, I am open. I just want to see some
real and clear evidence to contradict that I have seen, before I bite
the bullet. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 16)_

- **From:** Joe Zitzelberger <joe_zitzelberger@nospam.com>
- **Date:** 2004-01-02T09:51:42-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<joe_zitzelberger-9EFB50.09514202012004@corp.supernews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com> <joe_zitzelberger-C58612.19391131122003@corp.supernews.com> <a85c350e6a7b57908feb824c303367f2@news.teranews.com>`

```
In article <a85c350e6a7b57908feb824c303367f2@news.teranews.com>,
 "Judson McClendon" <judmc@sunvaley0.com> wrote:

> "Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote:
> >  "Judson McClendon" <judmc@sunvaley0.com> wrote:
…[31 more quoted lines elided]…
> the bullet. :-)

Why do you assume the 50% of new implementations is all "OO"?  There are 
plenty of new systems being developed in plain procedural styles even 
yet.  Do they not figure into that number?

Even without full "OO", plenty of things use occasional "OO" mixed with 
lots of procedural.  Two of the most successful software products of the 
current age come to mind -- Linux and Apache, both built on a C++ 
enabled C compiler with some modules and extensions written using a full 
"OO" style and others using a full procedureal style.  Which catagory do 
those fall into?

And I'm not sure how "technical deficiencies" can kill a project -- it 
might make some dates slip while code is written to work around the 
problems.  IMNSH experience, projects fail because the market for them 
disappears, or it never existed in the first place, or there is a 
failure on the part of the customer to properly define the 
market/software interaction.

Cost and time overruns and design goal failures are very flexible things.

If I decide that I want a program that will telepathicly kidnap all the 
worlds coffee makers and allow them to only produce decaf until the 
governments of the world pay me 1 billon dollars -- that is a design 
goal.

If I call your consulting firm and ask you to create this program for 
me, won't your answer of "Cobol doesn't do telepathy" put that project 
into the "technical deficiency of the Cobol caused project to miss 
requirements"?

Or if your firm decides to take the project -- won't it eventually get 
canceled for "cost overruns" after I realize that I'm paying and paying 
and seeing no hijacked coffee machines?

These two groups are so broad that everything can be blamed on at least 
one of them.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 17)_

- **From:** Ian Dalziel <iandalziel@lineone.net>
- **Date:** 2004-01-02T15:59:40+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ra5bvv0v9tkijgb1a8lhnn90irm7ip6lvh@4ax.com>`
- **References:** `<3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com> <joe_zitzelberger-C58612.19391131122003@corp.supernews.com> <a85c350e6a7b57908feb824c303367f2@news.teranews.com> <joe_zitzelberger-9EFB50.09514202012004@corp.supernews.com>`

```
On Fri, 02 Jan 2004 09:51:42 -0500, Joe Zitzelberger
<joe_zitzelberger@nospam.com> wrote:

>If I call your consulting firm and ask you to create this program for 
>me, won't your answer of "Cobol doesn't do telepathy" put that project 
>into the "technical deficiency of the Cobol caused project to miss 
>requirements"?

I thought it was in the 2002 standard?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 18)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-01-02T20:27:19+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<HukJb.16426$lo3.12719@newsread2.news.pas.earthlink.net>`
- **References:** `<3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com> <joe_zitzelberger-C58612.19391131122003@corp.supernews.com> <a85c350e6a7b57908feb824c303367f2@news.teranews.com> <joe_zitzelberger-9EFB50.09514202012004@corp.supernews.com> <ra5bvv0v9tkijgb1a8lhnn90irm7ip6lvh@4ax.com>`

```
Yes - but it is in the "processor dependent list" <G>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 17)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-02T16:15:24+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0087b72e8ebaad97747276c2857d2879@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com> <joe_zitzelberger-C58612.19391131122003@corp.supernews.com> <a85c350e6a7b57908feb824c303367f2@news.teranews.com> <joe_zitzelberger-9EFB50.09514202012004@corp.supernews.com>`

```
"Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote:
>
> Why do you assume the 50% of new implementations is all "OO"?  There are
> plenty of new systems being developed in plain procedural styles even
> yet.  Do they not figure into that number?

Yes, the 50% that work. ;-)

I don't say all of those failures are due to OO, but primarily due to the
almost exclusive use of three relatively new technologies for most new
development: GUI, Client/Server, and OO. In all three, complexity is
significantly increased, development costs are much higher, and in the
case of the first two at least, reliability is considerably poorer. Beyond
that, the reasoning goes:

A. Traditional methods applied toward new system development have
historically never shown even remotely such a failure rate industry wide.

B. Virtually all movement in the industry is toward the three technologies
above, nearly all education and media presentations in the last decade are
oriented that way, resulting in a mindset, not only that these are the 'newer'
technologies,but that they 'are the' technologies. The result is a significant
majority of new systems employ at least one or two of those technologies.

C. Any time there is a change, it is clearly obvious that the primary
suspect(s) should be the thing(s) that changed. Given A and B, it is
also clearly obvious that those are the primary suspects here.

D. We resolve the issue by examining system development overhead
(cost, time, etc) for industry wide (or as close as you can get) projects
using them compared to similar projects using traditional technologies.

E. The only such statistics I have seen are negative, that the newer
technologies are costlier, take longer, are more fragile, and more
complex and difficult to apply, in a given situation.

My whole point in these posts is to express my dismay that we (our
industry) have spent billions of dollars and man-hours, over more
than the last decade, on technologies that have serious disadvantages.
It can be argued that GUI and client/server provide capabilities not
available using traditional technologies. But I don't see that as a
significant argument in the case of OO, other than in limited areas.
And for these tools our industry is hell bent on abolishing the older
development tools, character based interfaces, procedural methods
and mainframes.

I'm simply saying that we should use the best tools for the job, be it
old or new, and that a new tool almost never completely obviate the
need for the old tool, it merely reduces the need.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 18)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-02T19:30:20+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bt4gsb$b6r$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com> <0087b72e8ebaad97747276c2857d2879@news.teranews.com>`

```

On  2-Jan-2004, "Judson McClendon" <judmc@sunvaley0.com> wrote:

> I don't say all of those failures are due to OO, but primarily due to the
> almost exclusive use of three relatively new technologies for most new
…[3 more quoted lines elided]…
> that, the reasoning goes:

I'm not that sure development costs are much higher - except for the fact that
development goals tend to be much bigger.


> I'm simply saying that we should use the best tools for the job, be it
> old or new, and that a new tool almost never completely obviate the
> need for the old tool, it merely reduces the need.

The trouble with this is defining "the job".
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-01T14:19:57+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff3762c_6@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <a05ced08fbce023d776b6295c1a40b55@news.teranews.com> <hb3suvkh2mkml29dai96n157bs91ttqrdc@4ax.com> <3fef4cd8_7@news.athenanews.com> <c56bcaed067933d38e61b95c602f6a56@news.teranews.com> <217e491a.0312291507.42879223@posting.google.com> <06da5a1090038b98b39b074dd8bcfd1f@news.teranews.com> <joe_zitzelberger-B7489D.21444230122003@corp.supernews.com> <c09ef0959aa3017b711788f8948d270b@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:c09ef0959aa3017b711788f8948d270b@news.teranews.com...
> "Joe Zitzelberger" <joe_zitzelberger@nospam.com> wrote:
> > "Judson McClendon" <judmc@sunvaley0.com> wrote:
<snip>>
> I'm not saying that anyone should skimp on learning what they need to
> know, Joe. I am saying that the newer 'programming tools' require
> *more* study to achieve and maintain the *same* level of proficiency.
>

So it's not like cars, then...<G>?

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-28T09:36:57+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3fededd4_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`

```
At least your post is an honest one, Bill.

Comments below...


"William M. Klein" <wmklein@nospam.netcom.com> wrote in message
news:27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net...
> Thane,
>   I still don't (fully?) understand (internalize) the difference between
your
> OO:
>
…[9 more quoted lines elided]…
> Call do-something  routine passing it something (or not) and asking it to
do
> what "do-something" does
>
>   or
>
> Call (perform) some-routine to return (in a parameter or even a RETURNED
or
> EXTERNAL variable) the information that "some-routine" is expected to know
> about.

This comes down (in COBOL terms) to the difference between CALL and INVOKE.
(We've hammered this many times here...)

Unfortunately, if I take specific instances of how OO differs from COBOL, it
does NOT explain why I consider OO to be "better". Instead, the COBOL
programmer just relates it to what he knows and misses the subtle
distinctions that the "newbie" catches. That is why it is easier to teach OO
to people who have never programmed in a procedural language, than it is to
teach people who have, and have already pre-formed concepts in their minds.

For a procedural programmer to REALLY understand OO, it isn't enough to just
learn Java or C++ and write a few clumsy programs with them; it is necessary
to CLEAR the mind of existing concepts (or at least move them to the back of
the head and avoid trying to match the new data against them) and see things
as if for the FIRST TIME, freshly. This is EXTREMELY difficult to do (I
know, I had to do it...), but it IS worth the effort, because when you
finish you will have new understandings and concepts that are quite "mind
blowing".(Note: Your previous concepts don't get "erased" or "overwritten"
but you now have an extended "toolbox" of other options, as well.)

Anyway, I'll take the current instance and maybe some of what I'm saying
will filter through somewhere...<G>

If I use INVOKE, I can have any number of "copies" of the same  encapsulated
code, all in different states (or not), and I can manage any or all of them
very simply and easily. Not only that, but it is efficient in machine terms
as well. To do this with CALL I would need to contrive different module
names for the same duplicated source code. I can never process these copies
in parallel (I can with INVOKE), without writing special facilities to let
my Operating System multi-task them.

Now, the usual reaction from a Procedural programmer on reading this is:
"But WHY would I need to do that? I've CALLed modules for years and had no
problems with it. Can't see how these "added benefits" of OO are really so
great..."

And they're not. In this particular instance. Because the DESIGN process is
intended to NOT be procedural.

This is the problem that OO supporters ALWAYS run into. Although you CAN
equate OO processes with Procedural processes, the benefits of OO are not
then immediately obvious and some of the benefits are not realised at all.

It requires the famous "paradigm shift" before the scales fall from your
eyes.

So, as far as this discussion is concerned, there is little benefit in using
INVOKE over CALL and OO is simply not worth the effort...


>
> With Call-prototypes in the 2002 Standard, there is even "protection" from
> passing a module something that it shouldn't get - or requesting returned
> information that you shouldn't see.
>

OO problem solving is NOT about the mechanics of Linkage.

In my opinion, far too much is made of the jargon like "encapsulation", and
"polymorphism". These are just sterile clinical terms for certain facilities
that are inherent in OO. Unless you actually implement a successful OO
system, these terms are not REAL, they are just "intellectual property" that
can be used to express a concept for the sake of academic argument. Not only
that, but they are "off-putting" to people coming from COBOL who are
unfamiliar with them.

When you actually see your objects being created and interacting with each
other, and other objects which you never even wrote, all working together to
provide facilities you could not dream of developing in the same time-frame
with Procedural Programming, when you realize the deluge of benefits that
iterated development by extending Class inheritance can bestow, THEN you can
say "Oh yes, encapsulation is a fantastic thing." or "I LOVE
polymorphism...saves me SO much development time...", or "Wow! I can extend
ONE Class and add a whole new bunch of facilities to my system WITHOUT
having to Regression test it, and KNOW that no previous code CAN be affected
by the change...<G>"... at this point, you may decide to drop Procedural
programming (except for Batch...)...or not....

> I am *not* trying to "fight" OO "philosophy" for applications that are
designed
> (from initial concept) for such, I simply (still) don't really "GET" what
the
> fundamental difference is.

This is refreshing honesty and prompts me to respond.

The reason the "fundamental differences" are not readily apparent is because
the vehicle being used for examination, is Procedural Programming.

You are saying: "I can do this with procedural code, how would I do it with
OO?". It's a fair question.

(When given the "answer" you are totally "underwhelmed", and fail to see
what all the fuss is about...<G>)

Because it is the WRONG question.

It's like saying to an eagle: "Quail are better at running than you are,
swallows can fly faster and are more manouevrable, seagulls are less
threatened by extinction, you're not really much of a bird, are you?"

To which the eagle replies: "I can catch and eat all of them...".
(He doesn't mention that he can spot a mouse moving from 20,000 feet, or can
soar for hours without expending energy like other birds, or the fact that
he is privy to sights and sensations that none of the aforementioned are,
because it is not pertinent to the conversation...)

A better question would be: "How does OO approach problems in data
processing?"

Thane has suggested that you read the book he posted links to. I think this
is a good approach. I haven't read the book in question, but if Thane
recommends it, that would be good enough for me.

It is pretty certain that none of the OO supporters here will persuade
anybody. (On reflection, neither should we try...).

"Ain't nobody else, gonna' walk it for you, you gotta walk it by yo'self..."
<G>

Pete.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2003-12-29T00:23:21+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031228192321.19959.00001141@mb-m01.aol.com>`
- **References:** `<3fededd4_5@news.athenanews.com>`

```


In one of his many fine and generous posts

 "Peter E.C. Dashwood" dashwood@enternet.co.nz 
Date: 12/27/03 3:36 PM EST
Message-id: <3fededd4_5@news.athenanews.com>


offered an expression that I would like the privilege of disagreeing with


snips infront

<<

If I use INVOKE, I can have any number of "copies" of the same  encapsulated
code, all in different states (or not), and I can manage any or all of them
very simply and easily. Not only that, but it is efficient in machine terms
as well. To do this with CALL I would need to contrive different module
names for the same duplicated source code. I can never process these copies
in parallel (I can with INVOKE), without writing special facilities to let
my Operating System multi-task them.


>>

snips behind


Actually, the single thing that distinguishes old old old COBOL from all of the
languages that descend from ALGOL is that COBOL resisted recursion until very
recently.  But it is notable that RECURSIVE program ID syntax enters COBOL with
COBOL 85 (I think), and therefore before OO COBOL.  In any event, you can have
recursive programs without having classes.


Programming with any language that allows recursion is definitely a paradigm
shift when compared to old old old COBOL which did not allow a program to CALL
itself directly or indirectly.  In RECURSIVE call sequences, each occurence of
a program recieves its own complete working storage (speaking in COBOLese).

That is one of the ways that you can have distinct copies of vast lists of data
items 'in parallel'.  But there is not much literature out there encouraging
folks to go off and design differently with that new COBOL capability. Yet lots
of new things are possible with that alone (way short of use of the new syntax
infused into modern COBOL 2002 for object orientation).

Recursive design of procedures in program design is distinct from object
oriented programming. Bubble sort is a recursive algorithm. That is doable with
COBOL 85 and the RECURSIVE syntactic element. You would _not_ 
'...need to contrive different module names for the same 
duplicated source code ...'


Furthermore, with ordinary COBOL a single program can have multiple copies of
records and handle them in parallel, simultaneously, as we all do with two-file
match routines.  The use of OF/IN phrases are not utterly unrelated to object
syntax, it is just coded a little in reverse (think about that for a while).


Object methods are recursive.  Interestingly, Class methods are procedurally
recursive but the Class data (FACTORY data in COBOLese) is not recursive in its
deployment (that is, it ain't instance data, there is only one copy of the
FACTORY).  Yet Class methods and data are part of object orientation.


The only way in COBOL to wake up a method is the syntax of INVOKE, simply
because the language standards folks have not devined an easy way to allow for
referential activation.  There are some experimental syntaxes that allow for
the specification of some methods with INVOKED AS syntax that approaches that,
but it is mounds of stuff ontop of big heaps of stuff.  This is really a shame,
and I think relates to what this thread is all about (In a small way).  

The invocation of the method is exactly where most of us get that Aha!
experience and the ease of seeing it is going to be denied to COBOLers probably
forever.  INVOKE syntax is okay, but the new world would be a little easier to
see if things were more fluid on the surface of the language as they are in the
ALGOL descendants.

Which brings me to my larger point.   If I understand this thread, it is as
though we have two groups of people.  One says I have been to the mountain and
seen it and it is a revelation.  Others say they have been there but didn't do
that.

These interactions are happening between honest people who are taking a lot of
time to explicate their ideas.  I believe that we can now begin to make a new
kind of conclusion.

First, the old conclusion that is available already.  Object Orientation works,
and scales up to some level of development effort. Second, the new conclusion
that is arriving about now is that Object Orientation does not sell the way
previous development methodologies sold.

Stating the matter in my own terms, I think the issue is the labor markets.
Flatlander COBOL has been used because it works with the very large and very
diverse programming community engaged in commercial information system
development, and because many persons were trained in COBOL.

We have a problem arising here. The future flow of programmers is going to be
heavily proportioned with Object Oriented professionals, and the supply of
COBOLers is rather obviously declining.

The intermediate future is probably one where most of the managers are
Flatlanders and most of the programmers are mixed and then soon enough
pretty much all Objectifiers by preference.

The discussions occuring here are simply a prologue for what is going to
continue for a while. Honesty.  Detail. Agreement to disagree.  No resolution.

The new methodology is not likely to displace the old in any wholesale fashion.
We will get mix, and probably the ability to mix is what current job posting
that list _both_ Java and COBOL are indicating.

What we really should be talking about is how to mix. That is what will sell,
as job skills and as solutions.


Best Wishses,
Bob Rayhawk
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-29T04:26:52+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<g2OHb.23620$Pg1.14501@newsread1.news.pas.earthlink.net>`
- **References:** `<3fededd4_5@news.athenanews.com> <20031228192321.19959.00001141@mb-m01.aol.com>`

```
RECURSION was added in the 2002 Standard (not the '85 Standard).  To the best of
my knowledge (and I could be mistaken) there was no vendor that even added it as
an extension to the '85 Standard *until* the first release where they also
provided OO syntax (also as an extension).  This is NOT intended to "imply" that
recursion is "only" useful for OO programs, but rather that the "effort" to add
support to it for COBOL (as an extension to the '85 Standard language) was only
"cost justified" by the compiler vendors when they "needed" it for OO support.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T18:00:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b687c7ea2b99ed280811d129dbc67800@news.teranews.com>`
- **References:** `<3fededd4_5@news.athenanews.com> <20031228192321.19959.00001141@mb-m01.aol.com> <g2OHb.23620$Pg1.14501@newsread1.news.pas.earthlink.net>`

```
"William M. Klein" <wmklein@nospam.netcom.com> wrote
> RECURSION was added in the 2002 Standard (not the '85 Standard).  To the best of
> my knowledge (and I could be mistaken) there was no vendor that even added it as
…[4 more quoted lines elided]…
> "cost justified" by the compiler vendors when they "needed" it for OO support.


True if you say so on IBM compilers. But Burroughs/Unisys mainframe
COBOL compilers were always code (not data, because of COBOL
syntax limitations) recursive. In general, this is easier to do with stack
machines than to enforce non-recursion. The Burroughs/Unisys Large
Systems (B5xxx through A series) were designed from the ground up
as not only recursive, but fully and completely reentrant. You would
have to work at it (not even sure if it's possible) to write a program
that was not so. Code and data segments are segregate, as well as the
data and procedure stacks, at the hardware level. I just mentioned in
another post writing a recursive parts explosion routine about the time
COBOL 85 was being finalized, on a Burroughs (B1700). Had to make
a 'stack' to handle the data recursion.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 10)_

- **From:** rkrayhawk@aol.com (RKRayhawk)
- **Date:** 2004-01-01T04:09:43+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20031231230943.11149.00001941@mb-m11.aol.com>`
- **References:** `<b687c7ea2b99ed280811d129dbc67800@news.teranews.com>`

```


<< The Burroughs/Unisys Large
Systems (B5xxx through A series) were designed from the ground up
as not only recursive, but fully and completely reentrant. You would
have to work at it (not even sure if it's possible) to write a program
that was not so. Code and data segments are segregate, as well as the
data and procedure stacks, at the hardware level. I just mentioned in
another post writing a recursive parts explosion routine about the time
COBOL 85 was being finalized, on a Burroughs (B1700). Had to make
a 'stack' to handle the data recursion.
>>

There is a subtlety here that Intel practitioners do not see.  For 'tis true
that althogh the devices purport to be Harvard architecture, the programming
foundation software make utterly no attempt at all to isolate 'data and
procedure stack'.  And I guarantee that Itanium is more violative of the
sanctatity of the procedures. 

A lot of money is on the line. I do not believe that the Val Kids are really
yet awake.

I want my data safe, Dumbells! And it ain't safe if frigin' buffer overruns
penetrate my procedures. Wake up slow pokes!

Regards!
Bob Rayhawk
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2003-12-30T12:25:54+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff0b870_1@news.athenanews.com>`
- **References:** `<3fededd4_5@news.athenanews.com> <20031228192321.19959.00001141@mb-m01.aol.com>`

```
Good post, Ray.

I found your conclusions excellent and don't really mind you disagreeing
over recursion <G> (Please note that I never used the term in my original
post, as it is not what I was trying to demonstrate...it is the difficulty
of using OO "equivalents" to procedural processes, that really fails to sell
OO....- that was the point I was TRYING to make <G>)

I think you are right about the "mix" and I endorse 100% your indication
that we shopuld be considering how to help COBOL people bridge the gap.

Pete.

"RKRayhawk" <rkrayhawk@aol.com> wrote in message
news:20031228192321.19959.00001141@mb-m01.aol.com...
>
>
…[14 more quoted lines elided]…
> If I use INVOKE, I can have any number of "copies" of the same
encapsulated
> code, all in different states (or not), and I can manage any or all of
them
> very simply and easily. Not only that, but it is efficient in machine
terms
> as well. To do this with CALL I would need to contrive different module
> names for the same duplicated source code. I can never process these
copies
> in parallel (I can with INVOKE), without writing special facilities to let
> my Operating System multi-task them.
…[7 more quoted lines elided]…
> Actually, the single thing that distinguishes old old old COBOL from all
of the
> languages that descend from ALGOL is that COBOL resisted recursion until
very
> recently.  But it is notable that RECURSIVE program ID syntax enters COBOL
with
> COBOL 85 (I think), and therefore before OO COBOL.  In any event, you can
have
> recursive programs without having classes.
>
>
> Programming with any language that allows recursion is definitely a
paradigm
> shift when compared to old old old COBOL which did not allow a program to
CALL
> itself directly or indirectly.  In RECURSIVE call sequences, each
occurence of
> a program recieves its own complete working storage (speaking in
COBOLese).
>
> That is one of the ways that you can have distinct copies of vast lists of
data
> items 'in parallel'.  But there is not much literature out there
encouraging
> folks to go off and design differently with that new COBOL capability. Yet
lots
> of new things are possible with that alone (way short of use of the new
syntax
> infused into modern COBOL 2002 for object orientation).
>
> Recursive design of procedures in program design is distinct from object
> oriented programming. Bubble sort is a recursive algorithm. That is doable
with
> COBOL 85 and the RECURSIVE syntactic element. You would _not_
> '...need to contrive different module names for the same
…[3 more quoted lines elided]…
> Furthermore, with ordinary COBOL a single program can have multiple copies
of
> records and handle them in parallel, simultaneously, as we all do with
two-file
> match routines.  The use of OF/IN phrases are not utterly unrelated to
object
> syntax, it is just coded a little in reverse (think about that for a
while).
>
>
> Object methods are recursive.  Interestingly, Class methods are
procedurally
> recursive but the Class data (FACTORY data in COBOLese) is not recursive
in its
> deployment (that is, it ain't instance data, there is only one copy of the
> FACTORY).  Yet Class methods and data are part of object orientation.
…[3 more quoted lines elided]…
> because the language standards folks have not devined an easy way to allow
for
> referential activation.  There are some experimental syntaxes that allow
for
> the specification of some methods with INVOKED AS syntax that approaches
that,
> but it is mounds of stuff ontop of big heaps of stuff.  This is really a
shame,
> and I think relates to what this thread is all about (In a small way).
>
> The invocation of the method is exactly where most of us get that Aha!
> experience and the ease of seeing it is going to be denied to COBOLers
probably
> forever.  INVOKE syntax is okay, but the new world would be a little
easier to
> see if things were more fluid on the surface of the language as they are
in the
> ALGOL descendants.
>
> Which brings me to my larger point.   If I understand this thread, it is
as
> though we have two groups of people.  One says I have been to the mountain
and
> seen it and it is a revelation.  Others say they have been there but
didn't do
> that.
>
> These interactions are happening between honest people who are taking a
lot of
> time to explicate their ideas.  I believe that we can now begin to make a
new
> kind of conclusion.
>
> First, the old conclusion that is available already.  Object Orientation
works,
> and scales up to some level of development effort. Second, the new
conclusion
> that is arriving about now is that Object Orientation does not sell the
way
> previous development methodologies sold.
>
> Stating the matter in my own terms, I think the issue is the labor
markets.
> Flatlander COBOL has been used because it works with the very large and
very
> diverse programming community engaged in commercial information system
> development, and because many persons were trained in COBOL.
>
> We have a problem arising here. The future flow of programmers is going to
be
> heavily proportioned with Object Oriented professionals, and the supply of
> COBOLers is rather obviously declining.
…[6 more quoted lines elided]…
> continue for a while. Honesty.  Detail. Agreement to disagree.  No
resolution.
>
> The new methodology is not likely to displace the old in any wholesale
fashion.
> We will get mix, and probably the ability to mix is what current job
posting
> that list _both_ Java and COBOL are indicating.
>
> What we really should be talking about is how to mix. That is what will
sell,
> as job skills and as solutions.
>
…[21 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Call prototype vs Invoke was Re: CoBOL moved to OO

_(reply depth: 6)_

- **From:** "Clark F. Morris, Jr." <cfmtech@istar.ca>
- **Date:** 2004-01-17T22:18:23-04:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bue0gg$ihn$1@news.eusc.inter.net>`
- **In-Reply-To:** `<27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net>`

```
William M. Klein wrote:
> Thane,
>   I still don't (fully?) understand (internalize) the difference between your
…[29 more quoted lines elided]…
> 
What is the advantage of having both CALL prototype and the INVOKE
construct?
```

###### ↳ ↳ ↳ Re: Call prototype vs Invoke was Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2004-01-19T00:38:30+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aGFOb.17935$zj7.4010@newsread1.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <bue0gg$ihn$1@news.eusc.inter.net>`

```
A method may have a CALL statement within it and a Sub-program may have a CALL
statement within it.  Although there are some who don't "like" mixing
"paradigms", it is still my belief that even in a (fully) OO environment, that
there may be some "functionality" that is best served by making a CALL to a
"stand alone" subprogram (that is not an OBJECT).

Similarly, I suspect that introducing OO (INVOKE) statements into individual
"modules" (called subprograms) of an application MAY be an appropriate (and some
time INappropriate) way to transition to OO.

If you do continue to have CALL statements, then it is useful to have CALL
prototypes; if you are "moving toward" allowing (if not encouraging) OO
methodology, you MUST have INVOKE syntax.

Therefore, it is "reasonable" to include both facilities (IMHO)

P.S.  There have been some "calls" to ONLY enhance the OO side of COBOL in the
future.  There have also been "calls" to "separate" the procedural from the OO
parts of the language (similar to C vs C++).  I *strongly* doubt that either of
these will ever happen, but who knows?
```

###### ↳ ↳ ↳ Re: Call prototype vs Invoke was Re: CoBOL moved to OO

_(reply depth: 7)_

- **From:** thaneh@softwaresimple.com (Thane Hubbell)
- **Date:** 2004-01-18T21:38:46-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bfdfc3e8.0401182138.241ef37f@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com> <27tGb.5203$lo3.1347@newsread2.news.pas.earthlink.net> <bue0gg$ihn$1@news.eusc.inter.net>`

```
"Clark F. Morris, Jr." <cfmtech@istar.ca> wrote in message news:<bue0gg$ihn$1@news.eusc.inter.net>...
> William M. Klein wrote:
> > Thane,
…[32 more quoted lines elided]…
> construct?


These are really different animals.  They allow you to "prototype"
your calls for "extra" compliance checking.  That's a readers digest
version.  For using some new contstructs format 3 calls (prototyped
calls, declared in the repository) are required.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2003-12-29T16:34:34+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<f490c636d421b2e64bfc4181720db32e@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com>`

```
"Thane Hubbell" <thaneh@softwaresimple.com> wrote:
>
> I too once didn't understand it.  I strongly strongly strongly
> recommend the folowing:
>
> http://www.amazon.com/exec/obidos/ASIN/0672326116/thanesonlinecobo

I will, thanks. :-)

> I actually never truly understood OO until I used the Fujitsu OO COBOL
> implementation - once you have that "light bulb" experience, the
> simplicity and elegence of OO is clear.

Believe me, I do see the elegance, though I admit that extensive use
of OO could give me a better view. But as I posted earlier, recursive
logic can have the same kind of beautiful simplicity and elegance
when it fits. But it doesn't fit all needs well, and iterative is normally
better, even though iterative logic is not particularly elegant or
beautiful.

My objections to OO are of two kinds, both are based on practical
considerations. An example of one kind is that it is clear to me how
increasing encapsulation to the degree necessary for an object has
serious negative side effects in certain situations currently under
discussion elsewhere in this thread. Also, I am not kidding about
wanting to see real statistical data, from real world applications,
where OO has an across the board benefit in the many costs of
developing and maintaining systems. I have never seen any, and
when I ask for it, I am given a couple of anecdotes. I have never
questioned that OO would work, or that it has appeal from certain
intellectual considerations. It is only that I am seriously doubtful
that the enormous time, energy and money we have put into it will
ever be repaid in benefits. The only way to answer this is real data
from real projects, in comparison to similar data from structured
procedural approaches. If it's real, it will show up in the data, if
it ain't in the data, it ain't real. And opinion won't matter when it
comes to the bottom line. OO would be far from the first thing that
appears good in theory, but is not so good in real world use. :-)
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** "William M. Klein" <wmklein@nospam.netcom.com>
- **Date:** 2003-12-29T23:02:28+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8o2Ib.25292$Pg1.1159@newsread1.news.pas.earthlink.net>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu> <22b3dcd54cff07a52f959b3cd483727d@news.teranews.com> <bfdfc3e8.0312241539.1607c8f0@posting.google.com>`

```
Thane (or anyone else in this group),

  Have I got an "interesting" <G> assignment for you (Pete, Jimmy, any of you OO
enthusiasts who I know and respect) ...

As many of you know, I am visually impaired.  I can work at a "large" screen,
but I no longer can really READ printed material (longer than a page or so).  (I
access both the old and new Standards  and various LRM's  "electronically" on my
large screen).

SO ...
  Does anyone have a "good" OO concepts book that they know of that has been
"recorded on tape" (cassette, CD, whatever)?  I haven't checked with the
"recordings for the blind" group yet (as they do sometimes record "college text
books") but I certainly can't find anything from my local (inter-)library
listings.

I am quite serious in being interested in any RECOMMENDED OO "theory" books that
anyone might know of that are recorded.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2003-12-22T21:30:31+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.0000037a.02f6ad08@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <VA.00000369.019ccad7@ieee.org> <bs75hv$hm1$1@peabody.colorado.edu>`

```
Howard,

> The business advantage to PeopleSoft may be primarily in marketing.   They sell
> a "state-of-the-art OO system", but still keep their valuable business code
> developed over years.
>
A colleague of mine always complained that software was like hardware - things 
don't wear out, but applications drift away from requirements, which is 
equivalent. So, he argued, applications should have a declared life time and they 
should be rewritten when that time has expired - the system has "worn out". I 
find his arguments persuasive, but I've never propounded them myself.

In this case, all I see, from a technical point of view, is that and old system 
is being pressed further into action to serve new, disparate needs. And it may or 
may not be appropriate. Techniques and technology move on, and an old system is 
just that - old and probably obsolete.

---

Doug

dwscott@ieee.org
```

#### ↳ Re: CoBOL moved to OO

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2003-12-20T03:45:36+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu>`

```
It is an idea, but I doubt it is a long time solution.

Why don't go to Java/C++/C#?
Patch after patch onto Cobol, sooner or later, the code will be difficult to
maintain.


A Cobol2Java programmer


"Howard Brazee" <howard@brazee.net> wrote in message
news:brseln$6t5$1@peabody.colorado.edu...
> We have a lot of PeopleSoft software in our shop.   I'm told that their
move to
> OO is by encapsulating much of their existing CoBOL code and using tags
and such
> to call it in an OO setup.
>
> How common is this with big mainframe applications?
```

##### ↳ ↳ Re: CoBOL moved to OO

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2003-12-20T08:24:27-06:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<KdmdnVz_0LQPxnmiRVn-iQ@giganews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com>`

```
Thomas A. Li wrote:
> It is an idea, but I doubt it is a long time solution.
>
> Why don't go to Java/C++/C#?

Because Cx is not well-suited to commercial applications and Java is for
making flames.

> Patch after patch onto Cobol, sooner or later, the code will be
> difficult to maintain.

Yeah, they've been saying that for over forty years now.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

- **From:** "Thomas A. Li" <tli@corporola.com>
- **Date:** 2003-12-22T18:09:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com>`

```
All of them are equal in computability.
Most of the OS now are written in C, eg. Unix and Windows.
Cobol program will call C routines for OS resources underneath at runtime.

Why Shakespeare's English is replace with modern English?
It is not decided by anyone. Maybe it is a long time trend.

The fitter survives.

Happy new year

"JerryMouse" <nospam@bisusa.com> wrote in message
news:KdmdnVz_0LQPxnmiRVn-iQ@giganews.com...
> Thomas A. Li wrote:
> > It is an idea, but I doubt it is a long time solution.
…[13 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 4)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-23T10:29:08-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0312231029.dca8178@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com>`

```
"Thomas A. Li" <tli@corporola.com> wrote

> All of them are equal in computability.

No. Not equal.

> Most of the OS now are written in C, eg. Unix and Windows.

C was developed with the needs for rewriting Unix in C.  That is, Unix
was originally written in assembler and it was decided to rewrite into
C.  Features were added to C to enable this, such as struct.

C is a language for writing OSes and system tools, it is excellent for
this.  It is less well suited for other tasks, such as business
applications.

> Cobol program will call C routines for OS resources underneath at runtime.

What's your point ?  The OS interfacing is based on C.

> Why Shakespeare's English is replace with modern English?

You seem to want to relate COBOL==Olde English.  C==Modern English.

These are different languages, English is still English.  Your analogy
is best likened as "Cobol 2002 replaces Cobol '61", and also "ANSI C
replaces Standard C".

"C (or C++, Java) replaces Cobol" would be equivalent to "Esperanto
replaces English".

> It is not decided by anyone. Maybe it is a long time trend.

Well certainly not by you.

> The fitter survives.

You seem to think that this means there should only be one animal
species.  If Lions are 'fitter' that Antelopes then why are there
still Antelopes ?
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** "Gary" <IDontThink@so.com.so>
- **Date:** 2003-12-23T23:37:27+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<Xk4Gb.463503$275.1354096@attbi_s53>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <217e491a.0312231029.dca8178@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:

> These are different languages, English is still English.

Not if you've ever been in a pub in Glasgow, Newcastle, Leeds, ... :-)

> > It is not decided by anyone. Maybe it is a long time trend.
>
> Well certainly not by you.

Hmmm. 'nuff said.

Gary.

PS. A Merry Xmas & prosperous New Year to all.
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 4)_

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2003-12-23T23:31:43+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com>`

```
Be aware that C (and C+ etc) are set up so that no type checking takes 
place.  This is one of the big reasons the security holes in the various 
systems exist.  The language wars were fought 15 - 20 years ago and C 
(and it's derivatives) won.

And, IMHO, COBOL is the language for data manipulation.  "C" is a macro 
assembler and should be used for other functions.  Business functions 
are not easily accomplished in "C".

Dick

Thomas A. Li wrote:

> All of them are equal in computability.
> Most of the OS now are written in C, eg. Unix and Windows.
…[32 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: CoBOL moved to OO

_(reply depth: 5)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2003-12-31T19:00:21-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0312311900.7e1c2e1d@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net>`

```
Pierra <pierra@sprynet.com> wrote

> Be aware that C (and C+ etc) are set up so that no type checking takes 
> place. 

That is just not true.  Both C and C++ do type checking extensively. 
The compiler will add automatic coersion as required.

> This is one of the big reasons the security holes in the various 
> systems exist. 

You may be thinking of 'bound checking' rather than 'type checking'
which are completely different things.  _Some_ security holes arise
from carefully contrived buffer overflows.

Cobol may also be susceptable to buffer overflow in exactly the same
way (eg CALL subroutine USING 80_byte_array where subroutine writes
200 bytes.

>  The language wars were fought 15 - 20 years ago and C 
> (and it's derivatives) won.

Nonsense. The areas in which C and C++ dominate (ie 'computer science'
based arenas) are a continuous war that has moved from Algol through
Pascal, Ada, Modula2, C and C++ and is now moving on to Java and C#. 
In another few years it will another few different or derived
languages vying for attension.

Meanwhile businesses will still use Cobol and scientists will use
Fortran.
```

###### ↳ ↳ ↳ (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 6)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-01T21:29:37+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff3daf0_2@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0312311900.7e1c2e1d@posting.google.com...
<snip>
>
> >  The language wars were fought 15 - 20 years ago and C
…[9 more quoted lines elided]…
> Fortran.

As you know, I disagree with this, but your post made me think.

I agree completely with your analysis of the "computer science" wars, so I
need to re-evaluate why I don't share your view regarding COBOL and Fortran.

After some consideration I have reached the following conclusions:

1. SOME businesses will continue to use COBOL (I believe it will be mainly
for Batch processing.). I also believe that there will not ALWAYS be a need
for Batch processing. (I know it's hard to believe in the current
"state-of-the-art"). As online transaction rates increase and online systems
become ever more efficient, there is no conceivable need for overnight
updates. Distributed systems through Client Server and the Corporate
Intranet will remove the need for Report runs off a central mainframe.

Some reasons why I believe that serious in-house development won't use
COBOL:

    (a) There are cheaper, better, faster alternatives becoming available.
"In-house development" is likely to be distributed back to individual
departments within the organisation and they will use standard tools to meet
their local needs. The Corporate systems will be based around standard
packages like SAP and Siebel, and the role of "bespoke software generation"
will decline to the point where it will simply involve plugging a few
standard components from the Corporate component repository into standard
desktop software. (OO, which COBOL seems to have missed the boat on, is one
of the major facilitators of this capability.)

    (b) Because (without OO) it is a closed system and cannot easily
communicate with all the "standard" desktop tools that users are coming more
and more to take for granted. (Like Spreadsheets, Word Processors,
Databases, etc.). When another report is required, most Businesses are not
going to accept that a COBOL programmer is required to write it. As skill
levels of users inevitably increase, they will simply use standard software
and do it themselves.

(By "standard software" I do not necessarily imply ONLY MS, although that is
certainly the de facto standard for most businesses at the moment. I think
we will see more businesses looking to remove their dependency on MS by
installing Linux and Unix (at least for trials...) and it will be
interesting to see what MS does to counter this. COBOL cannot (without OO)
be part of this, whether it goes Unix or MS, so that means that COBOL is
likely to be confined to the last bastions of procedural code, the
mainframes. I am not confident that mainframes will continue to be used for
any real length of time, UNLESS the WAY in which they are used changes. It
is interesting to see IBM advocating WEBSPHERE and Java and even component
use for mainframes. Again, without OO, COBOL will play what must be
essentially a "rearguard" action in this arena. Because of tradition, these
sites will support COBOL, but as the pressure comes on from cheaper
alternatives, they will slowly disappear (or transmute into something other
than what they are today...)

    (c) Fewer and fewer Businesses are going to invest in expensive in-house
IT development when they can cost-effectively outsource it, or use packages
that provide standard functionality and can be maintained (configured) by
users rather than programmers.

    (d) Many CEOs are wanting to get back to the Business they are in, and
resent the huge budgets we have seen for in-house IT departments. If your
business is Insurance  (for instance...) you may resent spending 15% of your
turnover on maintaining in house IT facilities, when you could buy the same
service for 2%. (I know of one major Australian Insurer who did exactly this
some years ago; it was devasting to the COBOL staff, but it was a "right"
Business decision.)

    (e) None of the above even considers the impact and effect of "fashion"
which, whether we like it or not, DOES colour Board level decisions. COBOL
is perceived as being outmoded, old-fashioned, and, in some cases, downright
dangerous. Despite modern facilities being provided by vendors, the uptake
by the user base has simply tended to confirm the "conservative" perception
of COBOL and COBOLlers. I am persuaded that it is now too late to do
anything significant about this, but I hope I'm wrong.

2. Scientists will use FORTRAN.

This is not in quite the same category as COBOL because the users tend to be
a very small base within a given organization.It is not "visible" to the
organization at large. FORTRAN is easily learned and a very useful tool for
many scientific applications. (I remember meeting FORTRAN evangelists during
my time with CDC (in the 1970s), where we were dealing mainly with
Scientific applications. It was (is?) adequate to the task and nobody had
any problems with it. I think the "new" generation of laboratory people will
probably prefer VB, and I have seen some stunning scientific stuff written
in Java, but I have to admit, FORTRAN is likely to outlive COBOL.)

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 7)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T12:22:42+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<8d0d85c747fb98025744b236a42b06d7@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> After some consideration I have reached the following conclusions:
…[7 more quoted lines elided]…
> Intranet will remove the need for Report runs off a central mainframe.

No batch? What about payroll, end of month, end of quarter and end of year
processing, to name a few cyclic, time-not-transaction, triggered processes.
Not to mention the 'zillions' of government mandated time or otherwise not
transaction triggered reports. It would be interesting to learn how you see
these in a 'no batch' scenario. :-)
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 8)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-01T12:52:10+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003c0.006c5d05@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com>`

```
Judson,

> It would be interesting to learn how you see
> these in a 'no batch' scenario. :-)

I did a lot of work on this. You can do most updates in real time, but 
reporting is by its very nature a batch process.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-01T22:22:30+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<d084e95d71481c0ded3bedb002a816da@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org>`

```
"Doug Scott" <dwscott@ieee.org> wrote:
> Judson,
>
…[4 more quoted lines elided]…
> reporting is by its very nature a batch process.

Real time updates for most things, maybe, but probably not payroll. You
have to know the totals before you can calculate the details. And all the
checks will probably need to be printed at the same time.

Even when things can be done real time you may not want to, because it
complicates the rounding error problem, for example. For those of you
not familiar, you can get very different results by rounding each of
100,000 transactions then summing them, as opposed to summing
100,000 transactions then rounding once. You can mitigate this in some,
but not all, situations by using more decimal places at certain levels.

I guess you could say that some things process incrementally, and those
can be done completely real time. But there are other things that process
in some larger quantum, and those may not suitable for real time
processing, at least completely.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T00:27:34+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003c5.02e905e3@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <d084e95d71481c0ded3bedb002a816da@news.teranews.com>`

```
Judson,

> Even when things can be done real time you may not want to, because it
> complicates the rounding error problem, for example.

Nah - since you have to carry an error from one calculation to the next, 
that can be held on a database or somewhere convenient. But I'm not 
suggesting real time for /everything/ as a practical solution, come to 
think of it - it's one of my beefs about some of the newer kids on the 
block that they try to do it all online and end up with hideous designs, 
simply because of lack of expertise in designing batch systems. They 
have their own rules, but they have the magnificent feature that a batch 
run is 100% repeatable - if designed properly.

I picked up an insurance system (HUON) at one stage, and it regularly 
used to update DB/2 databases in batch without any commits at all, until 
the end of program. If a program failed for any reason (and they did 
regularly), all updates were backed out and the program could be rerun 
without any database restore.

Of course, it might have been better to design the system so that such a 
huge consumption of resources could be better used, but it was good for 
the standby programmers.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-02T13:33:25+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff4bcd3_9@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <d084e95d71481c0ded3bedb002a816da@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:d084e95d71481c0ded3bedb002a816da@news.teranews.com...
> "Doug Scott" <dwscott@ieee.org> wrote:
> > Judson,
…[10 more quoted lines elided]…
>

Still printing checks? How quaint...

What about the employees who demand gold coins or livestock <G>?

Moving numbers between the Bank and your employees is something Banks have
dealt with for many years now. In Europe it is called BACS...


> Even when things can be done real time you may not want to, because it
> complicates the rounding error problem, for example. For those of you
…[4 more quoted lines elided]…
>

"Computer Fraud 101..."

> I guess you could say that some things process incrementally, and those
> can be done completely real time. But there are other things that process
> in some larger quantum, and those may not suitable for real time
> processing, at least completely.

Bollocks!

Your ability to complicate essentially simple processes never ceases to
astound me...

If something has "granularity" your real time system must recognise that.
There are standard practices and procedures for doing this. You can adjust
the "sample rate" or adjust the tolerances. The only time I ever encountered
this was in control of an oil refinery; the application of it to Business is
improbable, but, even if it were, the same techniques would solve the
problem.

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T11:52:06+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003c8.008c8e53@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd3_9@news.athenanews.com>`

```
Peter,

> Moving numbers between the Bank and your employees is something Banks have
> dealt with for many years now. In Europe it is called BACS...

And it's done using batch processing! Generating a serial file for 
transmission to BACS is not a real time function.

> The only time I ever encountered
> this was in control of an oil refinery; the application of it to Business is
> improbable, but, even if it were, the same techniques would solve the
> problem.

I wrote a program twenty years ago to address this precise problem, and it 
cannot have been unique at all in the financial industries. It is to do with 
reinsurance, where hundreds of companies shared in a bunch of risks (e.g Piper 
Alpha). Each had a percentage share of the premium income and claims 
expenditure, and the net premium income had to be distributed according to 
share amongst these companies. Some may only have 1% of the contract, some 
might have as much as 8.3333%. The revenue split had to be precise, and it all 
had to add up to the total revenue from the contract. And you couldn't have 
two reinsurers chatting over a glass at some stage, discovering that although 
they held the same percentage share, their revenue was different. That 
requires dealing with rounding errors, without sampling and with a tolerance 
of ï¿½0.01.

It's not difficult, but it is a significant business problem.


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-02T16:32:11+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<9d5230037f8e55023f8fce89c614f31b@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <d084e95d71481c0ded3bedb002a816da@news.teranews.com> <3ff4bcd3_9@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> Your ability to complicate essentially simple processes never ceases to
> astound me...

Your ability to overlook potential pitfalls astounds me... ;-)

> If something has "granularity" your real time system must recognise that.
> There are standard practices and procedures for doing this. You can adjust
…[3 more quoted lines elided]…
> problem.

If that 'granularity' requires processing a million transactions at once,
you are going to have fun implementing that 'real time. :-)

Pete, you can't use your own experiences as the criteria for what can't
happen, only what can. It is a truism in science that you cannot prove a
negative. There are situations out there that you and I have never even
imagined. I'm saying "Be flexible, and allow for the fact that you can't
know everything." You are saying "I know everything I could possibly
need to know, and it can't happen." It is a good bet which position is
going to get steamrollered when the unforseen does happen. Just
because you or I haven't witnessed it is no proof that it can't happen in
circumstances we haven't encountered. I have seen programs run 20
years before bombing on a bug that was there all along. :-)
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-02T13:20:26+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff4bcd1_9@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org>`

```

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.000003c0.006c5d05@ieee.org...
> Judson,
>
…[6 more quoted lines elided]…
> ---

Yes, it certainly is today...

But, let's look at it from another angle...

There was a time when corporations had a mainframe and that was all there
was.

I remember running end-of-month processing for a household name motor parts
manufacturer in Auckland in the late '60s. Tapes (disks weren't invented)
were sorted for around 6 hours and then "The Reports" were run. (this took
another 4 hours as stock movements and levels of over 100,000 parts were
produced for several hundred branches.)

A mountain of green lineflo (anyone remember that <G>?...) was manually
split up on the Branch control breaks and distributed by post to the various
Branches.

After some time and numerous complaints from the Branches, we realized that
all this effort was really wasted because the reports sat in a corner
gathering dust until they went to the "pulping" bin (today that would be
"recycling"; the money obtained from this was used to help fund the staff
Xmas party at each Branch...)

The fact was that it was easier to go to a bin and check the stock level
than it was to wade through the report and see what the computer "thought"
should be there. So the report was really pretty useless.

The EDP manager suggested that this report should simply be summarized (he
saw a chance to get some of the tension out of his already stretched
budget). There were howls of outrage from the Branch managers who
vociferously asserted that this report was fundamental to their operation
and they couldn't live without it...(Human nature is beyond the scope of
this discussion <G>...)

The report stayed. It was produced for years and ignored for years until
online processing was implemented and the stock levels (and consequent back
order status, where applicable) were available on a green screen at the
touch of a button.

It is interesting that the ability to know whether an "out of stock" item
had been back ordered and when it was due to arrive, added enough value to
the system that it was now preferable to enquire online, than to walk to the
bin and check a card...

Here are the points I am trying to make:

1. The purpose of producing a report is to provide "information". (This is
NOT the same as "data", but we won't go into the distinctions, or sidetrack
to Marshall McLuhan, or investigate the finer points of Information Theory,
even though that is what CLC LOVES to do...<G>. For this post, let's just
stay with the NEED for reporting...<G>).

2. There are alternative ways in which information can be presented.
Reporting is an arguably archaic one. Even if you decide that reports are
"good", they are certainly NOT the ONLY way to present information. One of
the cited advantages of reports was that they could be filed and referenced
later. Nowadays,  a decently designed transaction system can reproduce a
report from up to 7 years ago, in seconds, with no requirements for
microfiche readers, storehouses or reinforced flooring...

3. Modern managers have grown up with spreadsheets and databases and are
used to visualizing information in the form of graphic models. Lines of
"print" are not as informative for summarized data. Colour and graphics are
becoming a necessary part of modern Management Information Systems.
EVERYTHING is on a screen; if hard copy is required, it can be obtained at
the touch of a button. The concept of Batch "listings" will progressively
disappear as more immediate forms of information presentation replace it.
(Think about the last time you used a quill pen...Now think about the last
time you retrieved information from the Internet...)

4. Government (and similar Legal) requirements for information on duly
filled out forms are being met by EDI, so there is no need to get a listing
and transcribe the data to a hard form.

5. New media (PDAs, cell phones, etc.) are coming on line and information
can be (and in an increasing number of progressive businesses, IS BEING...)
retrieved anywhere, any time. CEOs who want to know the top performing
Branches World wide can get it on their cell phones with "bottom lines"
updated every few minutes.

Why would you go "back to the office" to consult a listing, when you can
have it reproduced on your phone or PDA at the restaurant where you are
lunching clients?

6. Much of the current "Reporting Requirements" in Corporations are based
around Batch Hard Copy because that is cheap and effective, doesn't strain
the system, and is "traditional" (especially on mainframe-centric sites).

As these systems are replaced by more Network oriented solutions (and,
believe me, they WILL be...), questions will legitimately be raised over
exactly WHAT information is really required to run the business, HOW
AVAILABLE should it be (there are issues of security around listings; anyone
who can read can have access to it if they get hold of it. Displayed data is
easier to control.), HOW TIMELY does it need to be (Batch reports can only
reflect the situation as it WAS at the time the report was run...), and
finally, the sheer resistance to using paper (large amounts of it) for a
questionable benefit.(The rising generation are much more environment aware
than we were...)

I know the "paperless office" we were promised years ago has failed to
eventuate, and it is unlikely to, but the need for Batch Reporting can
certainly be challenged and I hope the above will persuade you that it can.

I do not see "Reporting" as being the reason we will perpetuate Batch
Processing.

(In fact, I don't see Batch Processing being perpetuated at all, and that is
where we came in...)

Pete.








>
> Doug
…[3 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T13:12:03+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003cb.00d5c12f@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com>`

```
Peter,

> 1. The purpose of producing a report is to provide "information".

Yes, and printing it is only one way of presenting the data. Your objection 
seems to revolve around printing stuff, which I'll agree is largely 
unnecessary. But the numbers still have to be crunched, and it's still more 
efficient to crunch monthly figures once and store them for later retrieval 
rather than crunch them whenever an individual wants to glance at them.

> 2. There are alternative ways in which information can be presented.
> .... Nowadays,  a decently designed transaction system can reproduce a
> report from up to 7 years ago, in seconds, with no requirements for
> microfiche readers, storehouses or reinforced flooring...

True, and has been true for years. Again, printing should be distinguished 
from processing. Presentation doesn't require massive database activity - it 
requires the data to be there in a form which allows presentation - thus the 
Data Warehouse.

> 3. Modern managers have grown up with spreadsheets and databases

Yes, this point is about hard copy print again. Same arguments.

> 4. Government (and similar Legal) requirements for information on duly
> filled out forms are being met by EDI, so there is no need to get a listing
> and transcribe the data to a hard form.

Agreed. But EDI is a /batch/ process.

> CEOs who want to know the top performing
> Branches World wide can get it on their cell phones with "bottom lines"
> updated every few minutes.

As at that instant? For a large company, the cost would be prohibitive for 
such a fanciful thought. CEOs should be working on a three-month to ten-year 
timeline, not minute by minute. That is the province of the sales department, 
so it's much more localised. I know online insurance companies will vary the 
rates by time of day depending on sales targets for the day, but to be 
honest, people became slightly manic and that generated customer resistance.

Instant ain't good for statistics - you need some form of perspective. 

> 6. Much of the current "Reporting Requirements" in Corporations are based
> around Batch Hard Copy

Well, that is certainly a surprise to me. Back in 1975 I justified the cost 
of a County Council stock control system purely on the stationery savings. If 
the rest of the world hasn't caught up, then I'm faintly surprised, and maybe 
that's due to IT rather than the business.

> As these systems are replaced by more Network oriented solutions

Well, you're talking real time versus batch. I thought that argument was won 
years ago. Let's focus our discussions:

1. The points you made against batch are really points against hard copy. 
That is almost incontestable, I'd have thought, and I wouldn't dream of 
arguing otherwise.

2. What you call "the network" isn't particularly new because the points are 
based on real time processing, which will improve the timeliness of the data; 
online access to the results improves the service to the users and is also 
Goodness. But that has nothing to do with Batch, which is merely a method of 
crunching the numbers.

Batch processing will survive because it's more efficient to extract periodic 
figures once rather than many times. The /presentation/ of these figures is 
distinct from extraction, and will change according to the technology 
available.





---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-02T16:32:16+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bt46eg$rmo$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <VA.000003cb.00d5c12f@ieee.org>`

```

On  2-Jan-2004, Doug Scott <dwscott@ieee.org> wrote:

> > 1. The purpose of producing a report is to provide "information".
>
…[4 more quoted lines elided]…
> rather than crunch them whenever an individual wants to glance at them.

And often more meaningful.   Real-time doesn't give the same type of picture as
scheduled snapshots.


> Batch processing will survive because it's more efficient to extract periodic
> figures once rather than many times. The /presentation/ of these figures is
> distinct from extraction, and will change according to the technology
> available.

And it gives different information.   Batch is designed to do a lot of
processing at an instant in time.  (sure it takes longer - but our coding is
designed to make it work as if it were for an instant).
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 12)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T17:02:03+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003d9.01a8537c@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <bt46eg$rmo$1@peabody.colorado.edu>`

```
Howard,

> Batch is designed to do a lot of
> processing at an instant in time.  (sure it takes longer
>
I'm not sure it does. With batch, you usually don't journalise updates 
(you'd have a single dump/restore point for the entire batch run) so it 
ought to be a lot quicker if you're selecting by the same criteria.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-02T19:38:35+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bt4hbr$d14$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <bt46eg$rmo$1@peabody.colorado.edu> <VA.000003d9.01a8537c@ieee.org>`

```

On  2-Jan-2004, Doug Scott <dwscott@ieee.org> wrote:

> > Batch is designed to do a lot of
> > processing at an instant in time.  (sure it takes longer
…[3 more quoted lines elided]…
> ought to be a lot quicker if you're selecting by the same criteria.

It depends on how you measure.   Taking 100 cars across the ocean in a cargo
ship is much slower than putting one car in an airplane and flying it across.  
But taking 100 cars across the ocean with 100 airplane trips is probably slower
than the cargo ship.

The difference between batch and non-batch transactions is that in batch
transactions, you start a process and don't sit around waiting for a response.
You go ahead and do something else.

I can compile a program using a batch process, and I can do so using an on-line
process.  They both take about the same time - sure this time is less than a
minute.   But the batch compile is done in background, and I need to be notified
or to check to see when it is finished.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 13)_

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2004-01-03T01:19:02+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<aMoJb.5637$6B.5059@newsread1.news.atl.earthlink.net>`
- **In-Reply-To:** `<VA.000003d9.01a8537c@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <bt46eg$rmo$1@peabody.colorado.edu> <VA.000003d9.01a8537c@ieee.org>`

```
With the database I use (mainframe network DB) ALL of our batch update 
programs are either:
1.  Journalize the updates along with the existing online transactions.
  or
2.  Back up the database prior to the batch run, run the batch run, and 
backup the database again after the batch run terminates.

# 2 is allowed ONLY if it is faster than # 1 - NO exceptions.

(Also, with "my" database, I can back out transactions (using the 
journal files) to a point in time, as well as restore the database and 
re-run the transactions.  (Why, as some have asked, do you want/need to 
back out transactions (from a completed/check pointed system?  Because 
some dumb **** ran payroll twice.  Since I only have time to back up the 
database prior to the start of the online activity in the morning, and 
payroll is run at 8 PM, I do not want to restore the database and re-run 
ALL of the daily online transactions as well as all of the subsequent 
batch transactions until the second payroll job is run.)

Many modern databases that only "journal" the results of a transaction 
cannot back these transactions out of a completed transaction.  It's a 
shame, but we have progressed to the past.

Dick

Doug Scott wrote:
> Howard,
> 
…[15 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 14)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-03T21:30:06+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003ea.02bbfa8b@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <aMoJb.5637$6B.5059@newsread1.news.atl.earthlink.net>`

```
Pierra,

> Many modern databases that only "journal" the results of a transaction 
> cannot back these transactions out of a completed transaction.  It's a 
> shame, but we have progressed to the past.

Yes, but that's what the Commit verb does - it ends the transaction. 
There are some 4GLs which try to avoid the explicit Commit, but there are 
usually ways around it.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 15)_

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2004-01-06T17:39:03+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<XoCKb.28472$IM3.8856@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<VA.000003ea.02bbfa8b@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <aMoJb.5637$6B.5059@newsread1.news.atl.earthlink.net> <VA.000003ea.02bbfa8b@ieee.org>`

```
Doug -

Agreed, the commit or  "end" verb does end the transaction.  The problem 
comes about when you need to get back to a point BEFORE (caps for 
emphasis, not yelling :)  ) a particular point in time.

Going back to my example.  Say I ran Billing at 7:00 PM,  and at 8:00 PM 
I inadvertently ran it again.  Both program(s) went to normal end.  The 
problem is that the 8:00 run should not have run.  Because only 
transactions are journaled or logged, I cannot go back to the start of 
the 8:00 PM run by "backing out" transactions.   I must restore from 
backup and re-apply all transactions from the backup time until 8:00 PM. 
   If you only backup (probably because of time constraints) at the 
start of the business day, all transactions initiated during the day 
until 8:00 PM must be re-applied.

My "problem" is not with the Commit verb.  My "problem" is not being 
able to "roll back" committed transactions to a point in time.  And that 
is a "feature" of "modern" database systems.

Dick

Doug Scott wrote:
> Pierra,
> 
…[16 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 16)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-06T18:32:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003f3.025ffe8a@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <XoCKb.28472$IM3.8856@newsread3.news.atl.earthlink.net>`

```
Pierra,

> My "problem" is not with the Commit verb.  My "problem" is not being 
> able to "roll back" committed transactions to a point in time.  And that 
> is a "feature" of "modern" database systems.

Sure; if your company is willing to put up with the cost of journalising 
every transaction all the time, that's fine. You must be in the financial 
services area, where money is like water :-)


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 17)_

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2004-01-06T19:59:02+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<asEKb.28664$IM3.14271@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<VA.000003f3.025ffe8a@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <XoCKb.28472$IM3.8856@newsread3.news.atl.earthlink.net> <VA.000003f3.025ffe8a@ieee.org>`

```
Nope, it was in a public utility.  The database product in question is 
(and has been) used in all industries.  Having your data protected is 
out of fashion these days because (many of) the current vendors 
can't/won't provide the journalizing function.  It's not a question of 
cost, it's a question of how important your data is.

(by-the-by, what do you do when the backup media becomes corrupted and 
you can no longer restore and 'roll forward" the executed transactions? 
  Having the capability to restore your data both ways (forwards and 
backwards) is something that no dba should be without.  Another 
interesting sidelight, when I attended a MS-SQL Server presentation a 
number of years ago, and asked about the "roll-back" capability, the 
presenter said "Why would you want to do that?"  He apparently didn't 
have data integrity in the forefront of his product."

   JMHO - Dick

ps, what is the cost of journaling compared to up-time of your database? - d

Doug Scott wrote:

> Pierra,
> 
…[17 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 18)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-06T21:35:00+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003f6.03076cea@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <asEKb.28664$IM3.14271@newsread3.news.atl.earthlink.net>`

```
Pierra,

> Nope, it was in a public utility.

Uh huh. My taxes at work ;-)

> It's not a question of 
> cost, it's a question of how important your data is.

You can secure your data without full journalising batch processes. I'll 
agree that real time should be journalised, so that recovery time is 
minimised.

> (by-the-by, what do you do when the backup media becomes corrupted and 
> you can no longer restore and 'roll forward" the executed transactions?

? You go back further to a working version and roll that forward. You DO 
keep multiple backups, don't you? If data's critical, you should have 
copies of the backup anyway - one copy onsite, one offsite at the very 
least.

> a MS-SQL Server presentation a 
> number of years ago, and asked about the "roll-back" capability, the 
> presenter said "Why would you want to do that?"

Yeah. I didn't know they couldn't do it, but it's no surprise. They're 
hackers.



---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 19)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-06T17:59:48-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401061759.2482c563@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <asEKb.28664$IM3.14271@newsread3.news.atl.earthlink.net> <VA.000003f6.03076cea@ieee.org>`

```
Doug Scott <dwscott@ieee.org> wrote 

> > a MS-SQL Server presentation a 
> > number of years ago, and asked about the "roll-back" capability, the 
…[3 more quoted lines elided]…
> hackers.

'MS' SQL Server is actually Sybase SQL that MS bought the product
outright and rebadged it.  Sybase has now written a new 'clean room'
replacement.

I have no doubt that Sybase/SQLServer is a full featured product, but
the presenter probably came from a PC/Access background rather that
from the corporate server end of the market.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 20)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-07T20:30:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003f9.0080ff12@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <asEKb.28664$IM3.14271@newsread3.news.atl.earthlink.net> <VA.000003f6.03076cea@ieee.org> <217e491a.0401061759.2482c563@posting.google.com>`

```
Richard,

> I have no doubt that Sybase/SQLServer is a full featured product, but
> the presenter probably came from a PC/Access background rather that
> from the corporate server end of the market.
>
:-)

And certainly not from production support!

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-03T11:21:48+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff5ef72_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <VA.000003cb.00d5c12f@ieee.org> <bt46eg$rmo$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bt46eg$rmo$1@peabody.colorado.edu...
>
> On  2-Jan-2004, Doug Scott <dwscott@ieee.org> wrote:
…[3 more quoted lines elided]…
> > Yes, and printing it is only one way of presenting the data. Your
objection
> > seems to revolve around printing stuff, which I'll agree is largely
> > unnecessary. But the numbers still have to be crunched, and it's still
more
> > efficient to crunch monthly figures once and store them for later
retrieval
> > rather than crunch them whenever an individual wants to glance at them.
>
> And often more meaningful.   Real-time doesn't give the same type of
picture as
> scheduled snapshots.
>

There is no reason why a real time system CAN'T produce scheduled snapshots.
The two are NOT mutually exclusive.

<snip>

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 13)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-03T13:23:06+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003e2.00fe1f25@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <3ff5ef72_5@news.athenanews.com>`

```
Peter,

> There is no reason why a real time system CAN'T produce scheduled snapshots.
> The two are NOT mutually exclusive.

[Puzzled] True. It would be a nonsense to expend real-time resources to do it, 
but I do know systems where it's done - they dynamically lower the run 
priority, if they're at all clever.

But it's a batch process.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-05T15:29:25+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<btbvsl$30b$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <VA.000003cb.00d5c12f@ieee.org> <bt46eg$rmo$1@peabody.colorado.edu> <3ff5ef72_5@news.athenanews.com>`

```

On  2-Jan-2004, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> > And often more meaningful.   Real-time doesn't give the same type of
> > picture as scheduled snapshots.
…[3 more quoted lines elided]…
> The two are NOT mutually exclusive.

I suppose one can press an icon and then wait 20 minutes while the system
calculates the snapshot.   That's real-time.

Or one can press an icon to start the report/extract job, and then 20 minutes
later, the snapshot has been saved and anybody can look at it without waiting.
That's batch.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 14)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-05T10:25:31-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401051025.69983a23@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <VA.000003cb.00d5c12f@ieee.org> <bt46eg$rmo$1@peabody.colorado.edu> <3ff5ef72_5@news.athenanews.com> <btbvsl$30b$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote 

> I suppose one can press an icon and then wait 20 minutes while the system
> calculates the snapshot.   That's real-time.

And two people can press the icon (either because both think they
should, or by mistake thinking that the pretty picture meant something
else) and what a mess that could lead to.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-02T16:20:15+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bt45nv$p5t$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com>`

```

On  1-Jan-2004, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> 3. Modern managers have grown up with spreadsheets and databases and are
> used to visualizing information in the form of graphic models. Lines of
…[6 more quoted lines elided]…
> time you retrieved information from the Internet...)

As with your objection to "printed checks", it doesn't matter that the form is
different.   People want snapshots of the data at a particular time.   Money
flows from the payroll account to the workers' accounts at the end of the pay
period.   This month's spread sheet needs to reflect the end-of-month data.   
Batch processing says "do everything at this point".

Sure there's a need to know whether John Doe paid his bill five minutes ago.   
But decision makers also want to know what the total picture was Friday midnight
- and compare that to the total picture a week earlier.   Broad based snapshots
are useful - even if they are saved in forms other than printed listings.

Heck, I do batch processing under Windows.   I have .BAT files that find
particular selected data that I want to back-up to the LAN and/or copy to a
memory card for me to take home.   I put my card in the reader, click on the
icon, and this batch program runs.   I know exactly when the data are
synchronized to.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-02T17:05:41+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<ffc20e012f43e715bd306ad98668f636@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <bt45nv$p5t$1@peabody.colorado.edu>`

```
"Howard Brazee" <howard@brazee.net> wrote:
>
> Sure there's a need to know whether John Doe paid his bill five minutes ago.
> But decision makers also want to know what the total picture was Friday midnight
> - and compare that to the total picture a week earlier.   Broad based snapshots
> are useful - even if they are saved in forms other than printed listings.

Good point, Howard. Accounting practices, some of which predate
computers by millennia, and which are not going to be fundamentally
altered by anything we do in IS, dictate such. Accountants (who run the
companies, BTW) want to see accurate and timely reports EXACTLY
in the form they see them now. They may well want them to be online,
but they will never want them to changed in kind. Accounting is even
more conservative than engineering, a comparably ancient profession.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 12)_

- **From:** Donald Tees <donald_tees@nospam.sympatico.ca>
- **Date:** 2004-01-02T12:36:44-05:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<t1iJb.14155$Vl6.3179913@news20.bellglobal.com>`
- **In-Reply-To:** `<ffc20e012f43e715bd306ad98668f636@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <bt45nv$p5t$1@peabody.colorado.edu> <ffc20e012f43e715bd306ad98668f636@news.teranews.com>`

```
Judson McClendon wrote:
> "Howard Brazee" <howard@brazee.net> wrote:
> 
…[12 more quoted lines elided]…
> more conservative than engineering, a comparably ancient profession.

Nor are they interested in "real time". They are interested in 
conglomerate figures gathered into fiscal periods. Why would anybody do 
something like year end tax statements one transaction at a time, or be 
interested in a financial positions on a minute by minute basis 20 
minutes before midnight on new-year's eve?

Donald
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 13)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-03T11:34:09+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff5f259_8@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <bt45nv$p5t$1@peabody.colorado.edu> <ffc20e012f43e715bd306ad98668f636@news.teranews.com> <t1iJb.14155$Vl6.3179913@news20.bellglobal.com>`

```

"Donald Tees" <donald_tees@nospam.sympatico.ca> wrote in message
news:t1iJb.14155$Vl6.3179913@news20.bellglobal.com...
> Judson McClendon wrote:
> > "Howard Brazee" <howard@brazee.net> wrote:
> >
<snip>

> Why would anybody do
> something like year end tax statements one transaction at a time, or be
> interested in a financial positions on a minute by minute basis 20
> minutes before midnight on new-year's eve?
>

In 1904 the Editor of the London Times, when shown the newly invented
telephone, said: "Why would I buy that when I can send a copy boy?"

If transactions attain speeds that are unthinkable by today's standards (and
the indications are that they will...) then there is no reason not to have a
real time system.

Such a system models reality. As events occur in the Real world, they are
mirrored on the system. It makes sense.

The objections raised here have studiously avoided (or maybe not seen) the
post I made that says transactions can be scheduled whenever you want them
scheduled (in addition to mirroring random events as they happen).

There is NO problem with achieving synchronicity in a transaction based
real-time system. It can achieve everything currently achieved  by Batch
Processing, and then some. The only problem is that (at the moment) the
technology is not quite powerful enough to ensure that ALL transactions
(both random and scheduled) are processed immediately.

My speculation is predicated on that changing.

Pete.
 main argument for having a real time system is that it models reality

> Donald
>
>
>
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 14)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-03T13:23:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003e3.00fe2386@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <VA.000003c0.006c5d05@ieee.org> <3ff4bcd1_9@news.athenanews.com> <3ff5f259_8@news.athenanews.com>`

```
Peter,

> The objections raised here have studiously avoided (or maybe not seen) the
> post I made that says transactions can be scheduled whenever you want them
> scheduled (in addition to mirroring random events as they happen).

Well, I thought it was obviously true that a transaction could /initiate/ a 
batch process at any time, and it could be scheduled.

Peter, I've been working with this mechanism for over ten years. There are 
several other mechanisms which you need to put into place - dynamic 
prioritisation, feedback to the users saying "This will take ten hours to 
produce - do you really want this report?" And so on. And it's bullshit to 
say that batch processes will at some future date run on zero time; it all 
takes time and resources.

That enquiry system used to be given to the users as part of normal systems 
support - it saved writing reports and got them out of our hair. A change in 
IT management decided to charge the users for them, and all hell broke loose 
when they received bills for thousands of pounds because they were 
initiating reports in peak time. They could have done them overnight, but 
they insisted that they wanted them *now* and they didn't want to pay for 
them. The particular report I'm thinking of only reported end of day figures 
anyway (because of mail delivery), so it was a nonsense to do it in real 
time.

> The only problem is that (at the moment) the
> technology is not quite powerful enough to ensure that ALL transactions
> (both random and scheduled) are processed immediately.

Twas ever thus.
---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-02T12:20:58+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff4abd0_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:8d0d85c747fb98025744b236a42b06d7@news.teranews.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > After some consideration I have reached the following conclusions:
> >
> > 1. SOME businesses will continue to use COBOL (I believe it will be
mainly
> > for Batch processing.). I also believe that there will not ALWAYS be a
need
> > for Batch processing. (I know it's hard to believe in the current
> > "state-of-the-art"). As online transaction rates increase and online
systems
> > become ever more efficient, there is no conceivable need for overnight
> > updates. Distributed systems through Client Server and the Corporate
> > Intranet will remove the need for Report runs off a central mainframe.
>
> No batch?

Precisely.

> What about payroll, end of month, end of quarter and end of year
> processing, to name a few cyclic, time-not-transaction, triggered
processes.
> Not to mention the 'zillions' of government mandated time or otherwise not
> transaction triggered reports. It would be interesting to learn how you
see
> these in a 'no batch' scenario. :-)

OK, here's how...

Modern transaction systems can be triggered to fire off transactions at any
time you want.

It doesn't have to be "Batch" as we currently understand it. What you
suggest is "cyclic" ("time-not-transaction" based)  is simply a transaction
that must occur at a certain time.

As the capacity of systems increases, periodic transaction loads that occur
at regular intervals will be dealt with by load levelling and distribution
around the Network.(In exactly the same way as the Network caters for any
other bottlenecks or unexpected loads...).

You still show difficulty in grasping that the NETWORK will be King, rather
than your centralised mainframe.

(I expected more from you...<G>)

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T00:51:57+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003c6.02ff5815@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com>`

```
Peter,

> You still show difficulty in grasping that the NETWORK will be King, rather
> than your centralised mainframe.

Uh... Have you forgotten the Business? 

Users do expect some synchronisation of their data.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-02T14:32:32+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff4caa6_2@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <VA.000003c6.02ff5815@ieee.org>`

```

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.000003c6.02ff5815@ieee.org...
> Peter,
>
> > You still show difficulty in grasping that the NETWORK will be King,
rather
> > than your centralised mainframe.
>
> Uh... Have you forgotten the Business?

Nope. On the contrary, I believe commercial computer systems mstsupport the
business; that is what they are there for...

>
> Users do expect some synchronisation of their data.
>

OK, so where is the problem? If I want to see everything as at 1701
yesterday, my transaction processing system can do it; in fact it can do it
for ANY time point I select. (My databases have all the transactions, as
well as the master data...)

If Charlie, in the Accounts department wants to know what I spent on company
travel in the last X days, the system can provide data synchronised to THAT
criterion, just as easily as it can data synchronised to NOW. Not only that,
but it can instantly load it into a Spreadsheet and transmit that to him, so
he can manipulate it however he wants to.

For a properly designed Network system, synchronisation is NOT a problem.

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T13:22:12+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003cd.00df09c4@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <VA.000003c6.02ff5815@ieee.org> <3ff4caa6_2@news.athenanews.com>`

```
Peter,

> For a properly designed Network system, synchronisation is NOT a problem.

Sure. Ignoring cost and time delays. Instant information is expensive and 
needs to be cost-justified in any sane organisation (mind you there aren't 
too many of those around).


---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-03T11:36:16+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff5f2de$1_6@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <VA.000003c6.02ff5815@ieee.org> <3ff4caa6_2@news.athenanews.com> <VA.000003cd.00df09c4@ieee.org>`

```

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.000003cd.00df09c4@ieee.org...
> Peter,
>
> > For a properly designed Network system, synchronisation is NOT a
problem.
>
> Sure. Ignoring cost and time delays. Instant information is expensive and
> needs to be cost-justified in any sane organisation (mind you there aren't
> too many of those around).
>

The current trends are for processing power to increase and transaction
costs to decrease. I am speculating on a FUTURE, not what is current.

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 13)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-03T13:23:07+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003e4.00fe2535@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <VA.000003c6.02ff5815@ieee.org> <3ff5f2de$1_6@news.athenanews.com>`

```
Peter,

> The current trends are for processing power to increase and transaction
> costs to decrease. I am speculating on a FUTURE, not what is current.

Sure. We're doing now what we couldn't do in the past. It still requires 
non-zero resource utilisation.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 14)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-05T15:34:10+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<btc05i$4e5$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <VA.000003c6.02ff5815@ieee.org> <3ff5f2de$1_6@news.athenanews.com> <VA.000003e4.00fe2535@ieee.org>`

```

On  3-Jan-2004, Doug Scott <dwscott@ieee.org> wrote:

> > The current trends are for processing power to increase and transaction
> > costs to decrease. I am speculating on a FUTURE, not what is current.
>
> Sure. We're doing now what we couldn't do in the past. It still requires
> non-zero resource utilisation.

Also - batch output can be shared without re-creating it.   A batch snapshot
that is created is out there and has different security and conflict
requirements.   Some users just don't have the privilege to get to the source
data - but have authority to look at the results of a batch process.   Sure,
there are ways around this - but they are generally a pain.

Another comparison between batch and on-line is in incremental and full backups.
  Will we ever stop doing both?
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-01T19:57:13-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401011957.332689cc@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote

> You still show difficulty in grasping that the NETWORK will be King, rather
> than your centralised mainframe.
> 
> (I expected more from you...<G>)

Or he _grasped_ it but simply thinks that you are _WRONG_.

You appear to think that if one is not frothing at the mouth in a
frenzy to buy into the latest Microsoft technospeak trend that they
are trying to force everywhere, then one must be spoken down to as
being slightly backward.

The network (as web services) may be 'king' for _some_ uses. For other
applications having a large central server, or a cluster of server
blades, may be exactly the correct solution.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Gary" <IDontThink@so.com.so>
- **Date:** 2004-01-02T07:42:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yh9Jb.192239$8y1.622466@attbi_s52>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com>`

```
"Richard" <riplin@Azonic.co.nz> wrote:
> The network (as web services) may be 'king' for _some_ uses. For other
> applications having a large central server, or a cluster of server
> blades, may be exactly the correct solution.

Yep, I agree. No one single "application stack" will prevail.

To me, one of the most compelling aspects of "Web services" (or
architecturally, "Service Oriented Architectures") is that it embraces that
very position. It couldn't care less about the "application stack" behind a
SOAP request (it is, in principle at least, completely agnostic and
universal).

Gary.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-02T21:17:25+13:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ff5298c_9@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com> <yh9Jb.192239$8y1.622466@attbi_s52>`

```

"Gary" <IDontThink@so.com.so> wrote in message
news:yh9Jb.192239$8y1.622466@attbi_s52...
> "Richard" <riplin@Azonic.co.nz> wrote:
> > The network (as web services) may be 'king' for _some_ uses. For other
…[6 more quoted lines elided]…
> architecturally, "Service Oriented Architectures") is that it embraces
that
> very position. It couldn't care less about the "application stack" behind
a
> SOAP request (it is, in principle at least, completely agnostic and
> universal).
>

Sadly, my post was completely misunderstood (certainly by Richard) and I
never disputed any of this.

It isn't arguable.

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-02T21:05:33+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff526c5_8@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0401011957.332689cc@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
> > You still show difficulty in grasping that the NETWORK will be King,
rather
> > than your centralised mainframe.
> >
…[3 more quoted lines elided]…
>

Yes, I know that, but this is a rhetorical debate.

> You appear to think that if one is not frothing at the mouth in a
> frenzy to buy into the latest Microsoft technospeak trend that they
> are trying to force everywhere, then one must be spoken down to as
> being slightly backward.

Huh?! Please show where ANYTHING I have EVER posted would support that
conclusion.

That's unfair and unnecessary, Richard. I am not a fervent supporter of MS
and have indicated as much on numerous occasions. I use MS at the moment
because that is what my client is using. We find it adequate, so I am fairly
neutral on this one.

I think you are so abhorrent of MS Corporation that you are seeing MSophiles
under every rock and reacting to them instead of considering your posts. You
already said that something I wrote could have been written by JerryMouse
which shows you completely misunderstood it. (I have no issue with Jerry's
posts, for the most part, but it just wasn't pertinent.)

Neither am I speaking down to people as being backward. (Although I do
consider that some of the entrenched attitudes encountered here ARE
backward; I still respect the right of people to have an opinion, and
therefore take the time to attempt a reasoned argument, expecting and
enjoying fair debate.)

I am expressing an opinion, and I have tried to support it with reasoned,
unemotional, argument that is based on what I observe and not on any leaning
towards, or away from, MicroSoft or any other Company.

If you read the Subject you will see that what was expressed is OPINION and
it is open to debate.

How is that promoting MicroSoft or expecting people to be foaming at the
mouth for MS products?

Look to your own prejudices before you make personal attacks.

>
> The network (as web services) may be 'king' for _some_ uses. For other
> applications having a large central server, or a cluster of server
> blades, may be exactly the correct solution.

Please show where I ever referred to "the Network (as web services)". I
didn't and I don't. I had a misunderstanding about Web Services which has
since been corrected.

When I use the term NETWORK I am referring to the local LAN, the IntraNet,
and the Internet. Obviously, I agree completely with your last paragraph,
where a central server or cluster of server blades is simply part of "the
Network".  Furthermore, I believe that in the future (and that is what I am
discussing, not the immediate present), the distinction between what is
currently considered LAN, ClientServer, IntraNet and Internet, will all
become blurred and companies will simply refer to "The Network".  This is
what will be "King".

(Unless of course, my assessment is completely wrong; then it won't be <G>)

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T12:42:08+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003c9.00ba5bd1@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com> <3ff526c5_8@news.athenanews.com>`

```
Peter,

> (Unless of course, my assessment is completely wrong; then it won't be <G>)

I agree that "the network" will certainly become almost homogeneous, but not 
quite. You can't ignore the performance penalties: even with broadband, I'd 
prefer to access data locally if it's available, /even/ if I don't back it up 
as often as the network does (I'm making a big assumption here!).

But I'm looking at a system for a startup florist's shop at the moment, and I 
think it's /just/ possible to outsource the accounting functions onto a 
web-based system. Security is a primary consideration, and we probably won't 
do it, but it's becoming possible.

Yes, there are lots of florists who do web-based ordering. I wanted to move 
the whole shebang there so that we could have thin clients, with the 
infrastructure being maintained as part of the service. And, of course, the 
early adopters will have to pay through the nose - it's the way of the world.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-02T11:38:07-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401021138.427f56b8@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com> <3ff526c5_8@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote 

> > > You still show difficulty in grasping that the NETWORK will be King,
>  rather
> > > than your centralised mainframe.
> > >
> > > (I expected more from you...<G>)

> > You appear to think that if one is not frothing at the mouth in a
> > frenzy to buy into the latest Microsoft technospeak trend that they
…[4 more quoted lines elided]…
> conclusion.

It was a combination of the put-down, left as a quote at the top where
you imply cognitive difficulty, and a previous quote where you
specified that web-servives was _dependent_ on Microsoft's .NET.

> Neither am I speaking down to people as being backward. (Although I do
> consider that some of the entrenched attitudes encountered here ARE
> backward; 

Maybe they are not 'entrenched' but are 'considered' and just take
into account issues that you have not addressed in their context.

> I still respect the right of people to have an opinion, and
> therefore take the time to attempt a reasoned argument, expecting and
> enjoying fair debate.)

Stating that the reason they don't agree with you is because they have
cognitive difficulty is not 'reasoned argument'.
 
> Please show where I ever referred to "the Network (as web services)". I
> didn't and I don't. I had a misunderstanding about Web Services which has
> since been corrected.

Granted.  You did, however, appear to be talking _against_ the large
central server. Most do have some form of dumb access or client/server
access.  In fact it is the large central servers that drive the
internet.
 
> When I use the term NETWORK I am referring to the local LAN, the IntraNet,
> and the Internet. Obviously, I agree completely with your last paragraph,
> where a central server or cluster of server blades is simply part of "the
> Network".  

The network and the large central server(s) are not alterrnatives. 
Both need each other.  The alternative (which you were implying) to
large central servers is distributed services, surely.

> Furthermore, I believe that in the future (and that is what I am
> discussing, not the immediate present), the distinction between what is
> currently considered LAN, ClientServer, IntraNet and Internet, will all
> become blurred and companies will simply refer to "The Network".  

Hmmmm.  It seems to me that they already do.  But there are technical
issues about actually making these into one mechanism.  For example,
latency can be appalling on the internet.  The way to overcome this is
with VPNs which, while using the same ISPs actually run over the
network somewhat differently and separately.

> This is what will be "King".

'King' implies that it will have control.  The network on its own will
do nothing.  It needs large servers, or millions of small servers, or
both.  In some areas the large (central) servers will be the best
solution, in others lots of small servers will be the solution.  The
network is just a mechanism to connect thing together.  It will become
so ubitquitous that it will be like electricity.

Now I suppose there were people claiming a hundred years ago or so
that 'electricity' will be "King".  At the time there were small local
'networks' and competing services (such as hydraulic) and personal
generators. They were right and we still have massive central
'servers' and also small personal 'servers'. We just get on with what
we are doing and ignore that network because it is just there.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 12)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-03T11:13:22+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff5ed83_8@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com> <3ff526c5_8@news.athenanews.com> <217e491a.0401021138.427f56b8@posting.google.com>`

```

"Richard" <riplin@Azonic.co.nz> wrote in message
news:217e491a.0401021138.427f56b8@posting.google.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote
>
…[5 more quoted lines elided]…
>

Richard, this is simple rhetoric. It isn't intended to be offensive or taken
literally, and I don't think Judson did so...(Well, he's still talking to me
<G>)

Besides, if anyone should have a problem with it, that would be Judson. Do
you think he needs your intervention?

> > > You appear to think that if one is not frothing at the mouth in a
> > > frenzy to buy into the latest Microsoft technospeak trend that they
…[8 more quoted lines elided]…
> specified that web-servives was _dependent_ on Microsoft's .NET.

I didn't "specify" it; I believed it. I certainly didn't endorse it as being
desirable.

I was wrong about that and was corrected on it.

>
> > Neither am I speaking down to people as being backward. (Although I do
…[5 more quoted lines elided]…
>

Well, that is why we have a forum and open debate...

> > I still respect the right of people to have an opinion, and
> > therefore take the time to attempt a reasoned argument, expecting and
…[4 more quoted lines elided]…
>

No it isn't. In this instance it was purely a rhetorical device. (I don't
REALLY think that Judson, or anyone else, is some kind of backward Cretin
who cannot grasp my all-compelling argument. You are taking the whole thing
much too seriously. I question your right to do this, especially when you
make it personal.)

> > Please show where I ever referred to "the Network (as web services)". I
> > didn't and I don't. I had a misunderstanding about Web Services which
has
> > since been corrected.
>
…[4 more quoted lines elided]…
>

And you seriously think I don't know that? I was talking against the large
central mainframe, not its role as a Network Server.

I believe you also missed my intended meaning of NETWORK.

> > When I use the term NETWORK I am referring to the local LAN, the
IntraNet,
> > and the Internet. Obviously, I agree completely with your last
paragraph,
> > where a central server or cluster of server blades is simply part of
"the
> > Network".
>
> The network and the large central server(s) are not alterrnatives.

I didn't say they were, and you have totally misinterpreted what I DID say.
I think your usually acute vision is impaired by your loathing of MicroSoft
and your perception that I was somehow promoting them.

> Both need each other.  The alternative (which you were implying) to
> large central servers is distributed services, surely.

Nope. I "implied" no such thing. You have confused my use of the word
"mainframe" with the phrase "large central server". Many mainframes are NOT
large central servers (yet...), and THAT is what I was alluding to.

 I am saying that in the future the Network will be ubiquitous and ALL
corporate computers will be connected to it. Companies will buy a slice of
the action.

>
> > Furthermore, I believe that in the future (and that is what I am
…[9 more quoted lines elided]…
>

It really doesn't matter, and I'm not going to labour this further, but the
word "future" is pretty important in what I wrote. Given that I changed the
topic to what it is, I think I could reasonably expect people to understand
that I am speculating on what is to come, not what we have currently.

Incidentally, you might be right about VPNs...I am currently looking at
this.

> > This is what will be "King".
>
> 'King' implies that it will have control.

It will. Life without it  will be inconceivable. I believe it will permeate
our lives in ways we haven't even begun to conceive yet.

I am not saying the Network per se will have "control" (hopefully, Humans
will retain that) but it will be "King" when it comes to need for
information.


>The network on its own will
> do nothing.

Not true. It will enable the flow of information and data into every walk of
our lives.


>It needs large servers, or millions of small servers, or
> both.

Ah, we are talking at cross purposes. My use of "NETWORK" includes all the
devices attached to it, from the supercomputers, to the "intelligent
jewellery" that tells you the name of the person approaching you and what
his wife's name, kid's name, and dog's name is...<G>

>In some areas the large (central) servers will be the best
> solution, in others lots of small servers will be the solution.  The
> network is just a mechanism to connect thing together.  It will become
> so ubitquitous that it will be like electricity.
>

Yes, I agree completely with the last sentence. (Don't disagree with the
previous ones; it is just that the mechanics of how it works are irrelevant
to the discussion I am trying to have.)


> Now I suppose there were people claiming a hundred years ago or so
> that 'electricity' will be "King".  At the time there were small local
…[3 more quoted lines elided]…
> we are doing and ignore that network because it is just there.

OK. We can agree on the end position <G>.

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T11:42:06+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003c7.00836528@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com>`

```
Richard,

> The network (as web services) may be 'king' for _some_ uses. For other
> applications having a large central server, or a cluster of server
> blades, may be exactly the correct solution.

There's nothing cheaper to operate than a big black box with thousands 
of wires coming out of it. If you're talking big iron, IBM can supply 
Linux as well as OSz or whatever it's called nowadays. Minimal support 
costs, maximal compatibility. We did all the figures - a client/server 
network is hideously expensive to manage and difficult to maintain 
UNLESSS you ties the users down to a standard configuration - and then 
you lose the benefits of user choice.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** "Gary" <IDontThink@so.com.so>
- **Date:** 2004-01-02T19:57:53+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<53kJb.260699$_M.1208289@attbi_s54>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <217e491a.0401011957.332689cc@posting.google.com> <VA.000003c7.00836528@ieee.org>`

```
"Doug Scott" <dwscott@ieee.org> wrote:
> There's nothing cheaper to operate than a big black box with thousands
> of wires coming out of it. If you're talking big iron, IBM can supply
…[4 more quoted lines elided]…
> you lose the benefits of user choice.

What's happening now is that the "big black box" is no longer the realm of
IBM alone (and IBM have known this for years now). The UNIX/Windows & Linux
systems (hardware, o/s, applications, people, ...) have continued to mature
to the point where they represent very competitive alternatives to the
mainframe. However, by and large, my observation is that when enterprises do
select an alternative, they choose a single (multi-processor) box. The only
networked aspect is (typically) browser clients (pretty much analagous to
the 3270/mainframe model). The primary reasons have been (a) greatly reduced
recurring operating cost and (b) platform agility.

Difficult to say if these "new mainframes" will ever (fully) co-operate in
distributed processing to the point where it is considered "industry
mainstream". For a while yet, IMO, the "single box" (whatever it is) will be
a strong preference for running the business.

Gary.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-02T16:34:16+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bt46i8$s30$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com>`

```

On  1-Jan-2004, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> OK, here's how...
>
…[5 more quoted lines elided]…
> that must occur at a certain time.

How do we currently understand "Batch"?

If a complex program is triggered and runs without interaction - that's not
batch as we currently understand it?

Maybe a better question is who's "we"?
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-03T11:42:17+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff5f43f_6@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <bt46i8$s30$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bt46i8$s30$1@peabody.colorado.edu...
>
> On  1-Jan-2004, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
…[3 more quoted lines elided]…
> > Modern transaction systems can be triggered to fire off transactions at
any
> > time you want.
> >
> > It doesn't have to be "Batch" as we currently understand it. What you
> > suggest is "cyclic" ("time-not-transaction" based)  is simply a
transaction
> > that must occur at a certain time.
>
> How do we currently understand "Batch"?
>

Something that is an independent job step that will repetitively process a
set of files (OPEN- PROCESS-CLOSE) ?

You are right that I may be assuming a definition of "Batch" that is not
shared by others.

> If a complex program is triggered and runs without interaction - that's
not
> batch as we currently understand it?
>

I don't see "interaction" as being necessary to the definition of either
"transaction" or "Batch". Maybe that's where we differ.



> Maybe a better question is who's "we"?

OK, I accept I didn't specifically define my usage of "Batch" <G>

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-03T13:23:08+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003e5.00fe273e@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <bt46i8$s30$1@peabody.colorado.edu> <3ff5f43f_6@news.athenanews.com>`

```
Peter,

> I don't see "interaction" as being necessary to the definition of either
> "transaction" or "Batch". Maybe that's where we differ.

I think it's crucial. For me, a batch process runs against a set of 
transactions (the set may be zero or more transactions) without human 
intervention. An interactive one processes a single transaction. Both may 
process to completion, or require further (batch) processing to complete 
the business logic. For "real time" read "interactive" in my earlier 
posts, since were talking commerce here rather than all computing.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** "Judson McClendon" <judmc@sunvaley0.com>
- **Date:** 2004-01-02T16:41:04+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<9b71e6385cf1685aa570ebbb14b7956e@news.teranews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com>`

```
"Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
>
> You still show difficulty in grasping that the NETWORK will be King, rather
> than your centralised mainframe.

You still show difficulty in understanding my position, because you make
unwarranted assumptions about my lack of experience and/or ability to
understand. :-)

I totally agree that use of mainframes is declining and will continue to
do so. I just think throwing them all away immediately when the system
that replaces it may be no better, or even inferior, is dumb.

> (I expected more from you...<G>)

That's because you constantly underestimate where I am. ;-)
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-03T11:47:29+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff5f577_3@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <8d0d85c747fb98025744b236a42b06d7@news.teranews.com> <3ff4abd0_5@news.athenanews.com> <9b71e6385cf1685aa570ebbb14b7956e@news.teranews.com>`

```

"Judson McClendon" <judmc@sunvaley0.com> wrote in message
news:9b71e6385cf1685aa570ebbb14b7956e@news.teranews.com...
> "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:
> >
> > You still show difficulty in grasping that the NETWORK will be King,
rather
> > than your centralised mainframe.
>
…[3 more quoted lines elided]…
>

I make no such assumptions in reality, although I may appear to do so for
the sake of argument.

I have nothing but respect for both your experience and your competence.

Nevertheless, we both hold diametrically opposed positions on many things.


> I totally agree that use of mainframes is declining and will continue to
> do so. I just think throwing them all away immediately when the system
> that replaces it may be no better, or even inferior, is dumb.

So do I. That's why I am not advocating that, have never advocated that, and
will not advocate that.

(But you know that is not my position and it is you are using rhetoric in
this instance...<G>)
>
> > (I expected more from you...<G>)
>
> That's because you constantly underestimate where I am. ;-)

Maybe...<G>

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 7)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-01T12:52:09+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003bf.006c5817@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com>`

```
Peter,

> After some consideration I have reached the following conclusions:

We went through a similar line of reasoning ten years ago is determining the strategy for a large UK 
financial. However, the conclusions differed:

> 1. SOME businesses will continue to use COBOL (I believe it will be mainly
> for Batch processing.).

As I've said, the tools industry has moved on, and I doubt that even OO COBOL will be able to provide a 
resource-rich development environment which people like MS and Borland do.

Cobol does batch processing very well. C does it very poorly, so you might well be right there. 

Batch processing may not continue to be done in Cobol, though. With the provision of large online 
databases, the only uses of batch processing will be for analytical purposes, and something like SAS is 
better suited to that.

> Distributed systems through Client Server and the Corporate
> Intranet will remove the need for Report runs off a central mainframe.

Well, we were already there twenty years ago. And a change in management /centralised/ everything again 
(there's nowt so queer as folk).

If you have to produce monthly statements, then by definition it's a batch run to print them. And if 
you're doing that, the most efficient way to do bulk printing is to centralise it.

Finally, distributed systems are over-complex to manage and an incredible waste of users' time and money. 
Who manages a computer better - an amateur user or a professional operator? How many operators do you need 
to run a billion-dollar site? Compare that to the estimate of, say, an hour a day for 10,000 users.

> the role of "bespoke software generation"
> will decline to the point where it will simply involve plugging a few
> standard components from the Corporate component repository into standard
> desktop software.

I remember an engineer tell me back in 1964 that this was going to happen, except that he said it would be 
hardware-based. It never arrived, but I'm willing to concede that the large ERP products are managing to 
sell their message to senior management more and more. The trouble is that they require an awful lot of 
tailoring because every company works differently, and there could be a reaction to the inordinate amount 
of learning and twiddling to get a package into a useful state. I don't know - it could work, or there 
could be a reaction saying "dammit, I paid for all that functionality I never needed, and never will 
need."

But I don't think it will ever be a  case of plugging in software to a base package. Businesses, even 
within the same industry, are too different. I've seen these packages be adopted, and then quietly 
abandoned to be replaced by in-house developed stuff.

> (OO, which COBOL seems to have missed the boat on, is one
> of the major facilitators of this capability.)

Well, XML is a better contender for interoperability, and it doesn't mandate OO.

> When another report is required, most Businesses are not
> going to accept that a COBOL programmer is required to write it.

You're really going back into the ark with that one. We haven't used programmers to prepare reports for 
years - we use a report program generator which allows users to select fields from a data dictionary and 
report on them, with the reports automatically formatted.

> Because of tradition, these
> sites will support COBOL, but as the pressure comes on from cheaper
> alternatives, they will slowly disappear (or transmute into something other
> than what they are today...)

I don't know what you mean by "cheaper alternatives", but I will agree that Cobol is fighting a rearguard 
action which it could well lose, regardless of its merits.

> (d) Many CEOs are wanting to get back to the Business they are in, and
> resent the huge budgets we have seen for in-house IT departments. If your
> business is Insurance  (for instance...) you may resent spending 15% of your
> turnover on maintaining in house IT facilities

Wow. 15% of their turnover! The IT department deserved to be sacked. Most UK insurance companies spend 
between 3% and 7% of turnover on IT - and 7% was a waste.




---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-02T14:14:11+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff4c74a_5@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <VA.000003bf.006c5817@ieee.org>`

```

"Doug Scott" <dwscott@ieee.org> wrote in message
news:VA.000003bf.006c5817@ieee.org...
> Peter,
>
> > After some consideration I have reached the following conclusions:
>
> We went through a similar line of reasoning ten years ago is determining
the strategy for a large UK
> financial. However, the conclusions differed:
>
> > 1. SOME businesses will continue to use COBOL (I believe it will be
mainly
> > for Batch processing.).
>
> As I've said, the tools industry has moved on, and I doubt that even OO
COBOL will be able to provide a
> resource-rich development environment which people like MS and Borland do.

Agree completely. Not only has the tools industry moved on, but the next
generation of tools will be even better. I see OO COBOL as useful for
component manufacture (of Business Components). However, it is NOT
essential.
>
> Cobol does batch processing very well. C does it very poorly, so you might
well be right there.
>
> Batch processing may not continue to be done in Cobol, though. With the
provision of large online
> databases, the only uses of batch processing will be for analytical
purposes, and something like SAS is
> better suited to that.
>

I have reason to believe that Batch Processing will be rendered redundant
within 20 years. (See my post in this thread).

> > Distributed systems through Client Server and the Corporate
> > Intranet will remove the need for Report runs off a central mainframe.
>
> Well, we were already there twenty years ago. And a change in management
/centralised/ everything again
> (there's nowt so queer as folk).
>

Yes, I agree there has been a see-saw between centralised and distributed
systems. (I have been part of both camps and realise the benefits and
pitfalls of both approaches.) However, the Networks of twenty years ago were
not the Networks of today, and the Networks of today are a pale precursor of
the Networks of tomorrow. The die is now cast and distributed systems will
win.

(There is too much behind this to go into here, but, basically, people want
control of their own areas (including the data and processing of it). They
have the ability and tools to give them what they want, and this obviates
the need for a centralised IT facility, other than for clerical,
administration, and Network maintenance, (most of which will be outsourced
anyway...). Corporate reporting will be achieved via the Intranet (a simple
subset of the Network) and everything will be real time.

Networked Management is proving more effective than the old hierarchical
model, and modern Managers are capable of letting departments have
responsibility for their own data and the processing of it, provided it is
also available to Central Management. The Network facilitates this on a
Global basis which we certainly couldn't envisage 20 years ago.


> If you have to produce monthly statements, then by definition it's a batch
run to print them. And if
> you're doing that, the most efficient way to do bulk printing is to
centralise it.
>

That one is arguable in the future. I agree that currently it is the case
for many corporations.

(I already receive statements from three Companies by e-mail, and it is
efficient and effective. My Banks (both here and in Europe) support online
banking and I can produce a statement from them any time I want one, as well
as being able to view transactions up to the current date, and control
transfers, Direct Debits, etc. It wouldn't bother me if they never mailed a
monthly statement (they do, but it is purley because that is
traditional...How much longer?)

> Finally, distributed systems are over-complex to manage and an incredible
waste of users' time and money.
> Who manages a computer better - an amateur user or a professional
operator? How many operators do you need
> to run a billion-dollar site? Compare that to the estimate of, say, an
hour a day for 10,000 users.
>

I disagree. Besides, even if you were right, who is to say they will ALWAYS
be "over-complex to manage and an incredible waste of users' time and
money"?

(I remember EXACTLY the same criticisms being levelled at "computerization"
back in the '60s when mainframes started to proliferate. Whether they were
expensive and wasteful (compared to the highly underpaid teams of clerks who
did the job previously) was completely irrelevant. If your competition had
one, you had to get one. What price competitive advantage <G>?)

Many corporations are finding it isn't so.


> > the role of "bespoke software generation"
> > will decline to the point where it will simply involve plugging a few
> > standard components from the Corporate component repository into
standard
> > desktop software.
>
> I remember an engineer tell me back in 1964 that this was going to happen,
except that he said it would be
> hardware-based. It never arrived, but I'm willing to concede that the
large ERP products are managing to
> sell their message to senior management more and more. The trouble is that
they require an awful lot of
> tailoring because every company works differently, and there could be a
reaction to the inordinate amount
> of learning and twiddling to get a package into a useful state. I don't
know - it could work, or there
> could be a reaction saying "dammit, I paid for all that functionality I
never needed, and never will
> need."
>

I am not suggesting this scenario will arrive without pain...<G>

What was said in 1964 was far-sighted. Your Engineer wasn't so wrong when
you look at what is on chips today.

However, the fact that something failed to materialize (in your view)
before, doesn't NOT mean that it can't happen EVER.

"Previous performance is no guarantee of future results. Consult your
Adviser." <G>

> But I don't think it will ever be a  case of plugging in software to a
base package. Businesses, even
> within the same industry, are too different. I've seen these packages be
adopted, and then quietly
> abandoned to be replaced by in-house developed stuff.
>

Maybe... it is early days yet for CBSE.

I have some personal experience of this which supports my contention.

> > (OO, which COBOL seems to have missed the boat on, is one
> > of the major facilitators of this capability.)
>
> Well, XML is a better contender for interoperability, and it doesn't
mandate OO.
>

I have yet to see a component written in XML. It is good for transporting
messages between OO interfaces.


> > When another report is required, most Businesses are not
> > going to accept that a COBOL programmer is required to write it.
>
> You're really going back into the ark with that one. We haven't used
programmers to prepare reports for
> years - we use a report program generator which allows users to select
fields from a data dictionary and
> report on them, with the reports automatically formatted.
>

Excellent! However the same is not true for the majority of  sites using
COBOL.

> > Because of tradition, these
> > sites will support COBOL, but as the pressure comes on from cheaper
> > alternatives, they will slowly disappear (or transmute into something
other
> > than what they are today...)
>
> I don't know what you mean by "cheaper alternatives", but I will agree
that Cobol is fighting a rearguard
> action which it could well lose, regardless of its merits.
>
> > (d) Many CEOs are wanting to get back to the Business they are in, and
> > resent the huge budgets we have seen for in-house IT departments. If
your
> > business is Insurance  (for instance...) you may resent spending 15% of
your
> > turnover on maintaining in house IT facilities
>
> Wow. 15% of their turnover! The IT department deserved to be sacked. Most
UK insurance companies spend
> between 3% and 7% of turnover on IT - and 7% was a waste.

I consulted to Norwich Union for several projects. An excellent Company. I
believe their IT budget (across ALL areas, General, Investment, Life and
Pensions, was around 10% of turnover, prior to their flotation. I am sure it
has come down since, as one of the things we needed to do for flotation was
combine data from many different systems, so we could calculate what each
Policyholder (soon to become Shareholder) was entitled to.

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-02T13:22:11+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003cc.00df07e3@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <VA.000003bf.006c5817@ieee.org> <3ff4c74a_5@news.athenanews.com>`

```
Peter,

> I have reason to believe that Batch Processing will be rendered redundant
> within 20 years. (See my post in this thread).

And see my counter-post :-)

> The die is now cast and distributed systems will win.

There will always be a need for centralised processing - prepare reports 
once and send them via the network; in particular, weekly/monthly 
statements will always be batch, and complex documents like insurance 
contracts will be the last to go electronic, I'd say. Having said that, I'm 
staggered that the Land Registry has gone web-based. We'll have to see how 
successful that is.

Come to think of it, the Land Registry isn't distributed. In fat, many of 
the web-based solutions aren't distributed. Again, the presentation layer 
may be distributed, but distributing the database processing is much more 
difficult.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 7)_

- **From:** "Howard Brazee" <howard@brazee.net>
- **Date:** 2004-01-02T16:06:08+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<bt44tg$mnm$1@peabody.colorado.edu>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com>`

```

On  1-Jan-2004, "Peter E.C. Dashwood" <dashwood@enternet.co.nz> wrote:

> 1. SOME businesses will continue to use COBOL (I believe it will be mainly
> for Batch processing.). I also believe that there will not ALWAYS be a need
…[4 more quoted lines elided]…
> Intranet will remove the need for Report runs off a central mainframe.

Is that what batch processing is used for?

I guess when we run a batch program to write bills, it does update the database
to indicated that a customer has been billed, but I wouldn't categorize this as
"overnight update".

Will payroll be replaced by individual on-line transactions?
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 8)_

- **From:** "Peter E.C. Dashwood" <dashwood@enternet.co.nz>
- **Date:** 2004-01-03T11:18:56+13:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<3ff5eec9_7@news.athenanews.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <bt44tg$mnm$1@peabody.colorado.edu>`

```

"Howard Brazee" <howard@brazee.net> wrote in message
news:bt44tg$mnm$1@peabody.colorado.edu...
>
>
> Will payroll be replaced by individual on-line transactions?

Not in the short term, I shouldn't think.

It certainly COULD be.

Data on hours worked can be collected directly and/or indirectly. A
"current" payslip with all deductions can be produced as an electronic image
at the same time. At a scheduled time, a transaction to "print", "post" or
otherwise bring this document from Virtual Reality into Real Reality could
be activated.

It just needs imagination.

Pete.
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 9)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-03T13:23:08+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003e6.00fe28c4@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <bt44tg$mnm$1@peabody.colorado.edu> <3ff5eec9_7@news.athenanews.com>`

```
Peter,

> It just needs imagination.

By its very nature, payroll is time-synchronised. Real time or 
interactive transactions are relevant where people work in different 
cost centres within a payroll period, so that part of it can be 
interactive. But the employee is paid weekly, or monthly or whatever. 
That then becomes a batch process, because no further human interaction 
is required to produce the results - just a tick of the clock.

Similarly, share dividends are declared and paid annually, quarterly or 
whatever time period they decide. Once the dividend allocation is 
declared (a single transaction), millions of payments can be 
originated. Doing that via a real-time interactive system would 
probably dim the lights, but have no other effect on the result. Do it 
in batch background, and let the users get better response times.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 10)_

- **From:** Pierra <pierra@sprynet.com>
- **Date:** 2004-01-03T19:44:15+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<jYEJb.22303$IM3.14902@newsread3.news.atl.earthlink.net>`
- **In-Reply-To:** `<VA.000003e6.00fe28c4@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <bt44tg$mnm$1@peabody.colorado.edu> <3ff5eec9_7@news.athenanews.com> <VA.000003e6.00fe28c4@ieee.org>`

```
Two things about the topic at hand.

1.  If all the payroll processing is done dynamically/real time - how do 
you balance it?  When I was doing payroll processing (tax changes and 
converting the print process from internal to external)  balancing was 
critical.  It was part of the process of generating checks and posting 
the fact that payments were made (as well as calculating and posting 
benefit information.)  Again, balancing was/is critical.  Balancing is 
kind of hard to do in an interactive environment.

2.   I've had this argument in the past (not payroll initiated.)  Batch 
processing (single program/process or multi programs) can happen either 
in a traditional batch environment (separate partition/region from the 
online processing region(s)) or the online environment 
(CICS/TSO/WINDOWS/etc.)  My favorite term for the online batch approach 
was OLB - On-Line-Batch!  It's the same thing.  The only difference is 
how it's initiated.

Traditional batch is initiated by a job scheduler, operator submission, 
or on-line user submission.

OLB is initiated by a trigger or on-line user submission.

During the last conversion project I worked on, the end users were 
furious that they now would have to remember to initiate their periodic 
processes because the traditional batch operator was gone.

Just because the tools change, does not mean the the functions go away.

Dick
Doug Scott wrote:
> Peter,
> 
…[24 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** Doug Scott <dwscott@ieee.org>
- **Date:** 2004-01-03T21:30:05+00:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<VA.000003e9.02bbf77d@ieee.org>`
- **References:** `<3FE0AC45.3070208@istar.ca> <brseln$6t5$1@peabody.colorado.edu> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <bt44tg$mnm$1@peabody.colorado.edu> <3ff5eec9_7@news.athenanews.com> <VA.000003e6.00fe28c4@ieee.org> <jYEJb.22303$IM3.14902@newsread3.news.atl.earthlink.net>`

```
Pierra,

> 1.  If all the payroll processing is done dynamically/real time - how do 
> you balance it?

Well you need to timestamp every transaction (to within a microsecond) and 
then any processing must declare the time limits within its processing 
boundary. It's theoretically possible, but we never implemented it. And the 
timestamp must be related to the time of data entry, not the logical date 
of the transaction (i.e. Corrections to earlier incorrect entries may well 
not be processed because the "batch" run had started, even though the 
system was aware of them).

> During the last conversion project I worked on, the end users were 
> furious that they now would have to remember to initiate their periodic 
> processes because the traditional batch operator was gone.

I should bloody well think so. It's not difficult to write a small 
scheduler such as provided by any diary alarm system. Your designers didn't 
do a complete job, that's all.

> Just because the tools change, does not mean the the functions go away.

Well, you've just shown that designers can design functionality out of the 
system, forcing it back onto the users. Sad times.

---

Doug

dwscott@ieee.org
```

###### ↳ ↳ ↳ Re: (not entirely...) OT: OPINION... chicken entrails, runic stones, and crystal balls... WAS CoBOL moved to OO

_(reply depth: 11)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2004-01-03T14:50:14-08:00
- **Newsgroups:** alt.cobol,comp.lang.cobol
- **Message-ID:** `<217e491a.0401031450.389ad2a7@posting.google.com>`
- **References:** `<3FE0AC45.3070208@istar.ca> <ABPEb.94739$ea%.27039@news01.bloor.is.net.cable.rogers.com> <KdmdnVz_0LQPxnmiRVn-iQ@giganews.com> <7rGFb.121094$ea%.103425@news01.bloor.is.net.cable.rogers.com> <zf4Gb.6598$IM3.2139@newsread3.news.atl.earthlink.net> <217e491a.0312311900.7e1c2e1d@posting.google.com> <3ff3daf0_2@news.athenanews.com> <bt44tg$mnm$1@peabody.colorado.edu> <3ff5eec9_7@news.athenanews.com> <VA.000003e6.00fe28c4@ieee.org> <jYEJb.22303$IM3.14902@newsread3.news.atl.earthlink.net>`

```
Pierra <pierra@sprynet.com> wrote

> Again, balancing was/is critical.  Balancing is 
> kind of hard to do in an interactive environment.
 
Time based balancing, such as is found in most accounting systems, has
many problems in interactive and/or real time environments.

One major issue is that transactions update master records and a
balance is required to a specific date and time but may need
adjustments to be entered.

This can be handled by complex systems procedures that keeps separate
figures for balance date and ongoing transactions.  These usually
require batch processes to set and clear these.

Often, however, they lead to duplication of data by users taking
samples into a spreadsheet or PC database and manipulating as they
require.  Their 'adjustments' may have to be replicated back into the
system and this can lead to errors or omissions, and of course these
may be completely invisible to the IT dept.
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
