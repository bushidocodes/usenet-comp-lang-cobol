[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Visual Age COBOL and MS SQL Server

_17 messages · 9 participants · 2002-12_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Visual Age COBOL and MS SQL Server

- **From:** Al Rudderham <xal.rudderhamx@sympatico.ca>
- **Date:** 2002-12-20T00:12:00-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com>`

```
I'm looking at porting a small COBOL application to VA COBOL.  The
client is committed to VA COBOL specifically because it is being used
for another MUCH larger project.  The client also uses SQL Server
quite extensively.

The most desirable approach would be to use embedded SQL in the COBOL
code.  So far everything I've found in the VA COBOL docmentation only
points to using DB2 with VA COBOL.  Is there a preprocessor available
for VA COBOL that works with MS SQL Server, and if so where can I find
more info.

I've spent hours searching with Google, and on the IBM and Microsoft
web sites without any success so far.

Thanks!
```

#### ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2002-12-20T11:43:38
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atuv80$1m5$1@hyperion.microfocus.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com>`

```
You might want to look at an alternative, Net Express from Micro Focus for
example. Using embedded SQL it can access any SQL database that has ODBC
support.

www.microfocus.com

"Al Rudderham" <xal.rudderhamx@sympatico.ca> wrote in message
news:5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com...
> I'm looking at porting a small COBOL application to VA COBOL.  The
> client is committed to VA COBOL specifically because it is being used
…[16 more quoted lines elided]…
> (Sorry, but I'm SICK of spam...)
```

##### ↳ ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** Al Rudderham <xal.rudderhamx@sympatico.ca>
- **Date:** 2002-12-20T08:16:41-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<hs560voc1r38lljasi7g21b58dlqdvll4j@4ax.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <atuv80$1m5$1@hyperion.microfocus.com>`

```
On Fri, 20 Dec 2002 11:43:38 -0000, "Paul Barnett"
<paul.barnett@nospam.microfocus.com> wrote:

>You might want to look at an alternative, Net Express from Micro Focus for
>example. Using embedded SQL it can access any SQL database that has ODBC
>support.

I wish we could.  It's quickly becoming glaringly obvious that the
customer made a very poor choice in Visual Age COBOL.  However that
decision is made, and we're stuck with it.

What about any tools that simplify calling ODBC from COBOL?
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** "Paul Barnett" <paul.barnett@nospam.microfocus.com>
- **Date:** 2002-12-20T14:47:21
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<atva0m$2mt$1@hyperion.microfocus.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <atuv80$1m5$1@hyperion.microfocus.com> <hs560voc1r38lljasi7g21b58dlqdvll4j@4ax.com>`

```
You might look at Transoft - they can map flat files to ODBC - it may be
possible to do it the other way round. They can be found at www.transoft.com

Other than that it might well have to be direct calls to the ODBC API.

www.microfocus.com

"Al Rudderham" <xal.rudderhamx@sympatico.ca> wrote in message
news:hs560voc1r38lljasi7g21b58dlqdvll4j@4ax.com...
> On Fri, 20 Dec 2002 11:43:38 -0000, "Paul Barnett"
> <paul.barnett@nospam.microfocus.com> wrote:
>
> >You might want to look at an alternative, Net Express from Micro Focus
for
> >example. Using embedded SQL it can access any SQL database that has ODBC
> >support.
…[9 more quoted lines elided]…
> (Sorry, but I'm SICK of spam...)
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** Bob Wolfe <rtwolfe@flexus.com>
- **Date:** 2002-12-20T15:31:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<bqd60voieq801m6ojumkmtvap1bfnud25h@4ax.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <atuv80$1m5$1@hyperion.microfocus.com> <hs560voc1r38lljasi7g21b58dlqdvll4j@4ax.com>`

```
Al Rudderham <xal.rudderhamx@sympatico.ca> wrote:

>On Fri, 20 Dec 2002 11:43:38 -0000, "Paul Barnett"
><paul.barnett@nospam.microfocus.com> wrote:
…[9 more quoted lines elided]…
>What about any tools that simplify calling ODBC from COBOL?


Al:

I'm not sure if either one of these companies provides support for
Visual Age, but it's probably worth an e-mail to find out.

Data Direct Technologies (These guys used to be part of Merant and are
now independent.)

http://www.datadirect-technologies.com/products/odbc/odbcindex.asp

Parkway Systems

http://www.parkway-software.com/

Good luck!



Bob Wolfe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When replying by e-mail, make sure that you correct the e-mail address.
Check out The Flexus COBOL Page at http://www.flexus.com
```

#### ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-21T03:58:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NFRM9.22208$KW2.868799@twister.austin.rr.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com>`

```
Couldn't be much easier, though it is - ah - non intuitive.

First, no, the preprocessor that is included is for DB/2 only. But guess what? Microsoft has their own preprocessor for SQL server,
and you can use that. You would have to contact Microsoft's SQL group about it or find someone with a full MSDN subscription though.
I dropped all support for Microsoft about 2 years ago.

Or you can use ODBC, which is probably a whole lot easier. Just link to the OBDC libraries and make the appropriate calls. It looks
complex, but it really is simple.

By the way, if the big project is using VA COBOL, they are probably talking to DB/2 anyway. Why not just use DB/2 instead of SQL
Server, even under Windows?


-Paul

"Al Rudderham" <xal.rudderhamx@sympatico.ca> wrote in message news:5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com...
> I'm looking at porting a small COBOL application to VA COBOL.  The
> client is committed to VA COBOL specifically because it is being used
…[16 more quoted lines elided]…
> (Sorry, but I'm SICK of spam...)
```

##### ↳ ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-21T04:10:46+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-qT3g9mUgwPts@h24-82-204-17.wp.shawcable.net>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com>`

```
On Sat, 21 Dec 2002 03:58:37 UTC, "Paul Raulerson" 
<praulerson@hot.NOSPAM.rr.com> wrote:

> Couldn't be much easier, though it is - ah - non intuitive.
> 
…[10 more quoted lines elided]…
> 

Given that DB2 would be a better choice of database engine, I 
whole-heartedly agree

(someone who works with both SQL server and DB2 - both with COBOL)

And if you have stuff that resides in SQL server, use the federated 
database stuff in DB2 to present the tables to a DB2 client as if they
are present in DB2
```

##### ↳ ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** Al Rudderham <xal.rudderhamx@sympatico.ca>
- **Date:** 2002-12-22T21:59:34-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com>`

```
On Sat, 21 Dec 2002 03:58:37 GMT, "Paul Raulerson"
<praulerson@hot.NOSPAM.rr.com> wrote:

>Couldn't be much easier, though it is - ah - non intuitive.
>
…[4 more quoted lines elided]…
>I dropped all support for Microsoft about 2 years ago.

Thanks, I'll check that out.

>Or you can use ODBC, which is probably a whole lot easier. Just link 
>to the OBDC libraries and make the appropriate calls. It looks
>complex, but it really is simple.

That seems to be where I'm headed.

>By the way, if the big project is using VA COBOL, they are probably 
>talking to DB/2 anyway. Why not just use DB/2 instead of SQL
>Server, even under Windows?

There are a couple of reasons.  The primary reason is that an outside
vendor is driving the "big project" (and defined the toolset).  They
have control of the DBA function for DB2, whereas there are already
plenty of SQL Server databases in house.  It would not be permitted to
interfere in any way with the "big project", and use of DB2 would
probably wrest control of the DB2 admin function from them.  The small
project I'm interested in can only go ahead if it doesn't impact the
big one.  Using SQL Server keeps out of their way.

The second reason is the toolset.  I've worked with SQL Server
databases for the last 5 years, and the toolset (for developers and
for admin) is slick and well integrated with Windows.  DB2 reminds me
of Oracle - somebody did a quick port to Windows and to hell with
following Windows conventions.  Not to state a religious war - no
matter how good or bad the tools are, the real issue is not stepping
on the big project vendor's toes...
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-12-23T05:10:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<JUwN9.42374$Nz5.1076220@twister.austin.rr.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com>`

```

"Al Rudderham" <xal.rudderhamx@sympatico.ca> wrote in message news:29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com...
> On Sat, 21 Dec 2002 03:58:37 GMT, "Paul Raulerson"
> <praulerson@hot.NOSPAM.rr.com> wrote:
…[29 more quoted lines elided]…
>

There would only be anissue if you integrated the database with the "big project."
If in fact, they are totally separate databases, then I am unsure why there would be
any conflict. DB/2 under Windows does not have to have any interaction with
the mainframe or UNIX systems.


> The second reason is the toolset.  I've worked with SQL Server
> databases for the last 5 years, and the toolset (for developers and
…[5 more quoted lines elided]…
>

I'm not really clear on this one either, except on the differences between T-SQL and DB/2 SQL.
Hands down, DB./2 is much better. Other than that, DB/2 integrates a lot better with Java,
less well with ASP. (Well, what did you expect? You almost have to use ODBC to use ASP.)
It costs less, and outperforms SQL Server in almost every area. Development toolsets
include extremely good integration with more than one COBOL dialect, Java, C, C++,
ODBC, and XML, all of which are mature at this point, having been introduced at least
2 years ago.

Perhaps you should take another look at DB/2, without the Window's blinders on. :)

-Paul

> --
> Remove preceding and trailing X from username for replies
> (Sorry, but I'm SICK of spam...)
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 4)_

- **From:** Al Rudderham <xal.rudderhamx@sympatico.ca>
- **Date:** 2002-12-23T01:10:12-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com>`

```
On Mon, 23 Dec 2002 05:10:01 GMT, "Paul Raulerson"
<praulerson@hot.NOSPAM.rr.com> wrote:

>There would only be anissue if you integrated the database with the "big project."
>If in fact, they are totally separate databases, then I am unsure why there would be
>any conflict. DB/2 under Windows does not have to have any interaction with
>the mainframe or UNIX systems.

The big project is using DB/2 on Win2K Server.  The project I'm
interested in isn't big enough to justify any more hardware, or
software licences.  I just want to piggy-back on pre-existing
infrastructure.  What I'd like to prevent is the outsourcing of the
business function, which would mean a permanent loss of jobs.

While I'm sure you could *technically* do things so there were 2
independent DB/2 databases on the same server, *politically* it would
be a can of worms, and probably open up the opportunity for a lot of
finger pointing.  I don't believe they would buy the idea, and I don't
want to try to sell it.

>I'm not really clear on this one either, except on the differences between T-SQL and DB/2 SQL.
>Hands down, DB./2 is much better. Other than that, DB/2 integrates a lot better with Java,
…[6 more quoted lines elided]…
>Perhaps you should take another look at DB/2, without the Window's blinders on. :)

No blinders.  I don't get to pick the toolset - I get to write code.
My client is a large company with their own staff.  They made a
commitment to SQL Server several years ago (ripping out Oracle mid-way
through a large project when the vendor ran into problems making
Oracle work with MTS), and are using SQL Server everywhere.  They now
have one project that is more legacy based, which will use DB/2.

I'd just like to find a low cost and relatively painless way to port
an old COBOL application without incurring any software licencing
costs, and without jumping through too many hoops.
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 5)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-23T23:53:53
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e07a0e9_1@Usenet.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com> <119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com>`

```
Al,

I totally understand your reasoning and agree that SQL Server is the way to
go.

(I have a similar environment in some respects...)

You can use SQL Server from COBOL without problem. You need the ODBC driver
and away you go.

If ODBC doesn't appeal you can actually use OLE to SQL Server if you are
into OO COBOL (and you are using the Fujitsu toolset and compiler), and that
enables running stored procedures and triggers, or using ADO, but that's a
bit cutting edge for most people here.

Using SQL Server with ODBC and embedded SQL from COBOL is a doddle.

Pete.

Al Rudderham <xal.rudderhamx@sympatico.ca> wrote in message
news:119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com...
> On Mon, 23 Dec 2002 05:10:01 GMT, "Paul Raulerson"
> <praulerson@hot.NOSPAM.rr.com> wrote:
>
> >There would only be anissue if you integrated the database with the "big
project."
> >If in fact, they are totally separate databases, then I am unsure why
there would be
> >any conflict. DB/2 under Windows does not have to have any interaction
with
> >the mainframe or UNIX systems.
>
…[12 more quoted lines elided]…
> >I'm not really clear on this one either, except on the differences
between T-SQL and DB/2 SQL.
> >Hands down, DB./2 is much better. Other than that, DB/2 integrates a lot
better with Java,
> >less well with ASP. (Well, what did you expect? You almost have to use
ODBC to use ASP.)
> >It costs less, and outperforms SQL Server in almost every area.
Development toolsets
> >include extremely good integration with more than one COBOL dialect,
Java, C, C++,
> >ODBC, and XML, all of which are mature at this point, having been
introduced at least
> >2 years ago.
> >
> >Perhaps you should take another look at DB/2, without the Window's
blinders on. :)
>
> No blinders.  I don't get to pick the toolset - I get to write code.
…[12 more quoted lines elided]…
> (Sorry, but I'm SICK of spam...)



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 6)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2002-12-24T13:08:15+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3%YN9.3047$qU5.2273261@newssrv26.news.prodigy.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com> <119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com> <3e07a0e9_1@Usenet.com>`

```
"Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
news:3e07a0e9_1@Usenet.com...
> Using SQL Server with ODBC and embedded SQL from COBOL is a doddle.

Pray, what is a "doddle?"

In context, it seems to mean "a thing of little significance"  Close?

(Is "doddle" Kiwi-speak or has it its origins elsewhere?)

MCM
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 7)_

- **From:** "Hugh Candlin" <no@spam.com>
- **Date:** 2002-12-24T19:00:26+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<e92O9.77503$hK4.6341461@bgtnsc05-news.ops.worldnet.att.net>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com> <119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com> <3e07a0e9_1@Usenet.com> <3%YN9.3047$qU5.2273261@newssrv26.news.prodigy.com>`

```

Michael Mattias <michael.mattias@gte.net> wrote in message news:3%YN9.3047$qU5.2273261@newssrv26.news.prodigy.com...
> "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz> wrote in message
> news:3e07a0e9_1@Usenet.com...
…[4 more quoted lines elided]…
> In context, it seems to mean "a thing of little significance"  Close?

Yes, very.  A walk in the park.  An effortless stroll.  No bother at all.  Piece of cake.
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 7)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-12-24T13:03:19-08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0212241303.40748e25@posting.google.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com> <119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com> <3e07a0e9_1@Usenet.com> <3%YN9.3047$qU5.2273261@newssrv26.news.prodigy.com>`

```
"Michael Mattias" <michael.mattias@gte.net> wrote 

> Pray, what is a "doddle?"
> 
> In context, it seems to mean "a thing of little significance"  Close?

doddle[dCdl] n.ï¿½ï¿½ï¿½ï¿½×¾ï¿½Ö®ï¿½ï¿½ any activity that is easy to do.
 
> (Is "doddle" Kiwi-speak or has it its origins elsewhere?)

It's english.

"No doddle for Hoddle": BBC Sport Online columnist Derek 'Robbo'
Robson on Spurs' chances.
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 6)_

- **From:** Al Rudderham <xal.rudderhamx@sympatico.ca>
- **Date:** 2002-12-24T14:50:11-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<2geh0v02dr3d8002lsto0bn4gnc3neih1d@4ax.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com> <119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com> <3e07a0e9_1@Usenet.com>`

```
On Mon, 23 Dec 2002 23:53:53 -0000, "Peter E. C. Dashwood"
<dashwood@nospam.enternet.co.nz> wrote:

>You can use SQL Server from COBOL without problem. You need the ODBC driver
>and away you go.

So, who produces such a driver for SQL Server and VisualAge COBOL?  I
haven't been able to find one or reference to one on either IBM's or
Microsoft's web site...
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 7)_

- **From:** lsunley@mb.sympatico.ca
- **Date:** 2002-12-24T20:39:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<ZpzG4UNLyRNq-pn2-vRroumSep36z@h24-82-204-17.wp.shawcable.net>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com> <119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com> <3e07a0e9_1@Usenet.com> <2geh0v02dr3d8002lsto0bn4gnc3neih1d@4ax.com>`

```
On Tue, 24 Dec 2002 19:50:11 UTC, Al Rudderham 
<xal.rudderhamx@sympatico.ca> wrote:

> On Mon, 23 Dec 2002 23:53:53 -0000, "Peter E. C. Dashwood"
> <dashwood@nospam.enternet.co.nz> wrote:
…[7 more quoted lines elided]…
> 

The ODBC driver for SQL server is part of the MDAC package (Microsoft 
Data Access Component). Do a search at the microsoft website and you 
should turn up an installation package...

Visualage COBOL uses whatever ODBC drivers are present. The ODBC calls
are actually to the ODBC32.DLL and are forwarded from that DLL to the 
appropriate database specific driver that is tied to the DSN that you 
are attaching to.

When you link the program you have to link to the ODBC32.LIB.
```

###### ↳ ↳ ↳ Re: Visual Age COBOL and MS SQL Server

_(reply depth: 7)_

- **From:** "Peter E. C. Dashwood" <dashwood@nospam.enternet.co.nz>
- **Date:** 2002-12-26T12:33:24
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3e0af6c6_2@Usenet.com>`
- **References:** `<5a850vsupgebk7ph32aa0ftadjvcba8995@4ax.com> <NFRM9.22208$KW2.868799@twister.austin.rr.com> <29uc0vo5kmqtr81fc6n20i36u9t0ba5qug@4ax.com> <JUwN9.42374$Nz5.1076220@twister.austin.rr.com> <119d0v0naga144djib7b7d3n0aduu1uaru@4ax.com> <3e07a0e9_1@Usenet.com> <2geh0v02dr3d8002lsto0bn4gnc3neih1d@4ax.com>`

```

Al Rudderham <xal.rudderhamx@sympatico.ca> wrote in message
news:2geh0v02dr3d8002lsto0bn4gnc3neih1d@4ax.com...
> On Mon, 23 Dec 2002 23:53:53 -0000, "Peter E. C. Dashwood"
> <dashwood@nospam.enternet.co.nz> wrote:
>
> >You can use SQL Server from COBOL without problem. You need the ODBC
driver
> >and away you go.
>
…[3 more quoted lines elided]…
>
If you have SQL Server installed you will have automatically installed the
SQL Server ODBC driver. As Lorne pointed out, it is part of the MDAC package
that SQL Server requires in order to run.

I won't repeat Lorne's very apposite and accurate post (except to observe
that the VA environment should automatically include linking with ODBC32.LIB
when it encounters embedded SQL in the pre-compile.).

This post was simply to say that if you need help mail me privately. I have
a lot of stuff on using Relational Database from COBOL in a Client Server
environment.

I have been advocating this approach for years in the face of stiff
opposition from the ISAM/VSAM lovers who seem unable to grasp the fact that
the closed file system has been killing COBOL for a long time now.

I used to get abusive mail from people telling me that RDB was a fad and
that ISAM/VSAM was a proven and tested way to implement systems. (I never
disputed that it wasn't. Spent many years of my career (prior to 1983) using
VSAM/KSDS/RRDS/ESDS and ISAM in different flavours and developing Access
Methods and File system "layers" with these tools as they were all that was
available for random access from COBOL.) In those days hierarchic DB (IMS)
was King but it was unwieldy and had some serious limitations in that it
required traversal of the hierarchy, and for a long time it was necessary to
re-establish position by multiple calls after a dequeue boundary. By the
time they gave us the DL/1 call code that "remembered" current position so
you could pick up where you left off with a single call, it was too late...I
had already experimented with concatenating segment keys as the hierarchy
was traversed, but it was unwieldy and you had to store it somewhere across
a dequeue boundary...)

Currently, when I see my staff writing SQL server procedures and look at
what they write, it is a humbling experience. These are young people who
have never known any OTHER way than Relational Database and they manipulate
complex joins and selections with a facility born of years of experience in
doing just that.(I thought I was a pretty dab had at SQL until I saw what
these folks do...<G> However, my education is continuing...)

Nowadays I get private mail from people who can't understand why I still
make this point, as their installations automatically use RDB and the
message is clear. They can't imagine anyone clinging to the idea of serious
development WITHOUT using RDB.

I wish it had happened while there was still time to make COBOL part of it.

The fact is that embedded static SQL in COBOL programs is just not an option
for the new world. However, it serves nicely in the interim <G>.

Pete.



 Posted Via Usenet.com Premium Usenet Newsgroup Services
----------------------------------------------------------
    ** SPEED ** RETENTION ** COMPLETION ** ANONYMITY **
----------------------------------------------------------        
                http://www.usenet.com
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
