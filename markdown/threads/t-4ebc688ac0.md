[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOl Files v. Databases

_17 messages · 14 participants · 2001-03 → 2001-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Re: COBOl Files v. Databases

- **From:** "charles" <fjlk@home.com>
- **Date:** 2001-03-18T22:14:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Lqat6.117205$t67.1708087@news1.rdc1.il.home.com>`
- **References:** `<3AB260A2.A708A555@home.com>`

```
I work for a community college and we have nothing but VSAM files on our IBM
Mainframe.  Some of our VSAM files are around 150,000 records or so.  In the
big scheme of things that isn much compared to a large corporation.

For many people that use smaller mainframe's it can be a major cost to
migrate to a database system.  Besides just changing the file structure you
would have to change hundreds of programs.  Also keep in mind that would
require changing about 200 online CICS programs all at once in our case.  In
other words, it would require a complete system redevelopment.  This would
be no easy task and would probably cost at least a few hundred thousand
dollars if not a million.  We priced possible replacement for a total system
replacement from people like People Soft and 1 million dollars was among the
bids.  We have just 3 mainframe programmers.  No job schedulers or system
developers or anything else.


"James J. Gavan" <jjgavan@home.com> wrote in message
news:3AB260A2.A708A555@home.com...
> I'm posting this seeking some clarification, hoping it doesn't start a
> religious war <G>
…[29 more quoted lines elided]…
> --------------------------------------------------------------------------
---------
>
> I understand that most "real-time" data processing today DOES use a
…[25 more quoted lines elided]…
> --------------------------------------------------------------------------
-----------
>
> I have only programmed for PCs - but Bill did program for mainframes -
…[43 more quoted lines elided]…
>
```

#### ↳ Re: COBOl Files v. Databases

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-03-19T17:36:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB645D8.BE209EFC@home.com>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com>`

```


charles wrote:

> I work for a community college and we have nothing but VSAM files on our IBM
> Mainframe.  Some of our VSAM files are around 150,000 records or so.  In the
…[11 more quoted lines elided]…
> developers or anything else.

To which I reply, quoting from my original message :-

> > So as the person asking the question, may I set some rules ? Ignore the
> > pros and cons insofar as it effects applications, the obvious cost there
> > would be switching from COBOL files to a DB - that is clearly
> > understood, and is not a topic to be taken lightly.

Specifically, you use 'flat-files' - in either the support/rejection of DBs have
you ever worked on or evaluated a DB ? I'm not making a point for DBs one way or
the other - but as a current 'flat-file' user myself, I am curious what the
attitude is of other 'flat-file' users - did they arrive at a reasonable
conclusion  to reject DBs - OR - is the rejection based on the fact that they
are unfamiliar with DB techniques ?.

Jimmy Calgary AB
```

##### ↳ ↳ Re: COBOl Files v. Databases

- **From:** "Calin Macrinici" <cmac@pathcom.com>
- **Date:** 2001-03-19T18:43:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<lrst6.488753$JT5.14056018@news20.bellglobal.com>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com> <3AB645D8.BE209EFC@home.com>`

```
I'm not sure if I should comment in here, as I've been working on PCs for
the last 7-8 years (although before that I programmed on a PDP-11 for about
the same amount of time), but here's my two cents anyway (like you can tell
me to shut up!)

We used ISAM files for a long period of time, mostly in DOS environments and
everything was peachy (some users had problems, some crashes would screw-up
your data, mostly fixable with a rebuild).  Never even wanted to check DBs
out because "it wasn't worth it", although now, looking back it probably was
because they weren't COBOL enough!  (does that makes sense?)

Then Windows came along, and with it our perennial printing problems.  We
first tried to use windows APIs and graphical printing (for accounting
reports!!!!!!!!!), and it was pretty much OK, until more and more people
asked about the nice Crystal reports.

So we had to byte the bullet and start using Crystal.  No easy feat here,
but we did it.  Well guess what?  Crystal is much better at handling
databases (for one thing if you call their tech support and tell them you do
anything with COBOL they kind of laugh at you), MicroFocus accepts btrieve
files using the same IO techniques (i.e. COBOL syntax) so of we went.

Then we started to introduce more and more OO in our code.  If the OO COBOL
starts making any headways and the vendors don't change their approach
(MicroFocus allows SQL statements embedded in their COBOL programs; also web
based data access, CGI, etc., but file IO in an OO program is not made any
easier), me thinks that ISAM / COBOL files are dead (let me spell that: d e
a d!)

Why, you're asking?  Well for one thing accessing a file from a COBOL
class/object is difficult!  You cannot use FC/FD in the instance (Jimmy, you
know too well what I'm talking about), so you're stuck with hoop-jumping at
its best!  COBOL programmers actually exchange ideas as how to access data
from OO code!

So, now we're btrieve, next comes (probably) SQL, although I would have
never thought...

Whoa, that was way longer than I intended, so I'll leave it here.

Again, I apologize for barging w/o any mainframe info, but anyway...


Calin, TORONTO
```

###### ↳ ↳ ↳ Re: COBOl Files v. Databases

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-03-19T12:37:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB66016.42EC07CF@brazee.net>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com> <3AB645D8.BE209EFC@home.com> <lrst6.488753$JT5.14056018@news20.bellglobal.com>`

```
Databases put the emphasis of the IS shop where it belongs, with the data.  Let
the IS shop handle issues of the data of record, security, data integrity, data
accuracy, data currency, and access within the database instead of within
programs.

If this is done, we can use tools of choice for various applications.  As
hardware gets cheaper, adding an extra layer becomes more cost effective.   This
layer functions in a similar way as TCP layers do - applications do not need to
have an intimate detail knowledge, and the IS shop can make changes which are
transparent to the applications.

Functions which need to be centralized can be centralized, while the users can
easily have control on their own side - do they want the data retrieved into a
spread sheet?  Printed in a report?  Doesn't matter to the IS shop.

If a DBA decides to add a key to a file, the applications don't care, they just
run faster (if the DBA was correct).

The biggest costs are opportunity cost in not having data available, and
maintenance.  Then comes design and programming, and finally operating and
hardware.  Concentrating on getting the data correct is cost effective.
```

###### ↳ ↳ ↳ Re: COBOl Files v. Databases

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-03-21T02:52:22+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB819AA.FE1FC1D1@home.com>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com> <3AB645D8.BE209EFC@home.com> <lrst6.488753$JT5.14056018@news20.bellglobal.com>`

```


Calin Macrinici wrote:

Calin,

Your observations are pertinent.

>
> Why, you're asking?  Well for one thing accessing a file from a COBOL
…[3 more quoted lines elided]…
> from OO code!

Well things do move on........<G>.  As you've got beyond COBOL files, you are
probably no longer interested - but if you are I can now give you file classes
for relative, sequential, line sequential. There's a model for indexed from Pete
Dashwood, which I haven't yet pursued. But for the first three, using just three
separate file classes, you can throw 5,000 + record formats at the file class
and the only thing the file class needs to know is the full pathname and record
size varying ...... If you have a business program that needs say 10
sequentials, you (invoke) load the one source and have 10 instances.

I'm hoping I can take a parallel approach using DB, keeping existing Business
Logic,  the intermediary DBI - the only changes being required at the file class
level, where for the moment at least, I would store SQL syntax..
```

##### ↳ ↳ Re: COBOl Files v. Databases

- **From:** Susan Allen <susan.a.allen@boeing.com>
- **Date:** 2001-03-19T21:53:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB67FC6.BBDD7DD7@boeing.com>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com> <3AB645D8.BE209EFC@home.com>`

```
"James J. Gavan" wrote:
> 
> Specifically, you use 'flat-files' - in either the support/rejection of DBs have
…[5 more quoted lines elided]…
> 

Well actually I use both flat files and Databases (since I load some
large flat files into databases).  I also wrote stored procedures,
tested on a flat file and then altered into embedded SQL calls and
finally direct stored procedures - as the records extracted needed to
jump through some elaborate hoops.

I do not see a need for an either or with COBOL and DB's (or rather flat
files and relational files) each have a purpose and need.

The DB's I designed (& load or cause to be loaded with production job
streams) are used for ad-hoc decision support requests.  Other
applications may need to add or update large volumes of data with
complex matching or complex selection, not a strong area for a database
- the data from these files (in general) produces fixed reports in fixed
formats.

It is a matter of the best application to meet the specific need in a
timely and cost effective fashion

		Susan A
```

###### ↳ ↳ ↳ Re: COBOl Files v. Databases

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2001-03-19T19:11:05-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<996722$74dc$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com> <3AB645D8.BE209EFC@home.com> <3AB67FC6.BBDD7DD7@boeing.com>`

```
"Susan A" wrote:

> It is a matter of the best application to meet the specific need in a
timely and cost effective fashion.

I'd have to agree with Susan on this one.  If I had the time, and the
knowledge, I'd test out the SQL capabilities of using the NX-5600 as an SQL
server, since we do get "occasional" requests to look up a specific
account's transactions for a particular day.  An ideal "query" application,
I must say.  The flat file (I use this term loosely) used for check capture
needs to stay more or less in a sequential mode, even though it is actually
defined as a "random access" file in the select statement.  If you ever
notice all the endorsement stuff on the back/front of your checks, the
document identification number (DIN) is how most any bank researches
questions on your account. This is exactly how the items passed through the
sorter, and this is how they were captured into the file for posting to your
account.  We can get the account information using a COBOL program to access
the captured file, but I have a hunch that the SQL approach would be
quicker.  Bottom line, though, is that we just don't get all that many
requests to do this.

However, the stats that I was talking about in the Access DB, are basically
volume/reject/operator stats.  The software we run puts out a total record
for every unit of work we process (about every 3000 checks, give or take),
so rather than read through the whole database, we just grab the total
record (randomly on the NX-5600), then move the content into the database,
using the Fujitsu COBOL PC program.  I don't want to go into a lot of
detail, but the way any rejected items are tied back to the original
captured items might be beyond any SQL structure at this stage of the game.
For us, the above approach is both timely and cost effective.

As Susan says, depends on what you need to do with the data.

Being the age that I am, I am still in awe that we can read checks at
upwards of 2000 checks per minute, endorse them, microfilm them, image them,
pocket them and capture them to the "flat file" without going nuclear.  But
I love that fact that we can use both PC's and the mainframe as a truly
"open" platform.  We won't even get into the FTP side of it!  That's even
more fun.  Can you tell that I enjoy my work???

Denny
```

###### ↳ ↳ ↳ Re: COBOl Files v. Databases

- **From:** "Peter E. C. Dashwood" <dashwood@enternet.co.nz.nospam>
- **Date:** 2001-03-20T15:00:47+12:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ab74b5e_1@news.newsfeeds.com>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com> <3AB645D8.BE209EFC@home.com> <3AB67FC6.BBDD7DD7@boeing.com>`

```

Susan Allen wrote in message <3AB67FC6.BBDD7DD7@boeing.com>...
>
>I do not see a need for an "either" "or" with COBOL and DB's (or rather
flat
>files and relational files) each have a purpose and need.
>

<snipped.>
>
>It is a matter of the best application to meet the specific need in a
>timely and cost effective fashion


Neither do I, Susan.

"The BEST tools for the Job"   every time....

I have deliberately refrained from entering this debate because the ground
rules are flawed...

Jimmy, please note Susan's response and measure it against the private mail
I sent you.

Pete.



-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----==  Over 80,000 Newsgroups - 16 Different Servers! =-----
```

##### ↳ ↳ Re: COBOl Files v. Databases

- **From:** sff5ky@aol.comxxx123 (Sff5ky)
- **Date:** 2001-03-20T04:31:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<20010319233114.11923.00000681@nso-fq.aol.com>`
- **References:** `<3AB645D8.BE209EFC@home.com>`

```
In article <3AB645D8.BE209EFC@home.com>, "James J. Gavan" <jjgavan@home.com>
writes:

>
>Specifically, you use 'flat-files' - in either the support/rejection of DBs
…[7 more quoted lines elided]…
>

I'll chime in here. Probably out of context and on the wrong tangent.
In my current work environment, we have a group that works to maintain
optimum performance of our Databases thru defining alternate 'sets/tables'
into the main data structure.  Even with the best 'tuned' access 'set', we have

found that our "batch" processing works best with an UNLOAD to flat file at
the beginning, do all our work on the flat files, and then RESTORE from the
flat files back to the database.   This is processing a volume of approximately
60 institutions with 1.5M accounts.  As we have somewhere around 8 such 
databases on 8 machines (64 total) to process each night,  this has proven
to make the difference of making delivery 'on time'.

Hope that this set of comments is not too far off-topic.  It does seem to fit
you discussion, in my mind.
```

###### ↳ ↳ ↳ Re: COBOL Files v. Databases

- **From:** Rob Lec <RobLec@cinci-rr.com>
- **Date:** 2001-03-22T00:46:28+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB94B56.FBA0E818@cinci-rr.com>`
- **References:** `<3AB645D8.BE209EFC@home.com> <20010319233114.11923.00000681@nso-fq.aol.com>`

```


Sff5ky wrote:
> "James J. Gavan" <jjgavan@home.com> writes:
> >
…[7 more quoted lines elided]…
> flat files back to the database. 

Likewise, I have in many cases found it much more efficient to extract a
chunk of data from the system stores and process it locally using native
ISAM files.  This not only provides the convenience of creating any
necessary indexes (which may not exist within the database, or even be
worthwhile maintaining once the update process has completed), but also
has several additional benefits such as a substantial reduction in
network traffic and reduced processing overhead, and also allows
concurrent maintainance or backup of the master database.

-------------------------------------------------
(To reply by email change dash to dot in address)
```

###### ↳ ↳ ↳ Re: COBOL Files v. Databases

_(reply depth: 4)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-03-22T02:45:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB9697A.7E890D26@home.com>`
- **References:** `<3AB645D8.BE209EFC@home.com> <20010319233114.11923.00000681@nso-fq.aol.com> <3AB94B56.FBA0E818@cinci-rr.com>`

```


Rob Lec wrote:

> Sff5ky wrote:
> > "James J. Gavan" <jjgavan@home.com> writes:
…[14 more quoted lines elided]…
> worthwhile maintaining........

Whoa!. Hold it right there and I'm ABSOLUTELY no DB expert. But as I understand if
EVERY field in a DB is in effect 'keyed'  - specifically if using SQL.
Now, 'worthwhile maintaining....', that's a different thing - a judgement call on
what you consider most effective .......

Jimmy, Calgary AB

> ..........once the update process has completed), but also
> has several additional benefits such as a substantial reduction in
> network traffic and reduced processing overhead, and also allows
> concurrent maintainance or backup of the master database.
```

###### ↳ ↳ ↳ Re: COBOL Files v. Databases

_(reply depth: 5)_

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-03-22T14:06:29+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<FFnu6.105760$p66.30092768@news3.rdc1.on.home.com>`
- **References:** `<3AB645D8.BE209EFC@home.com> <20010319233114.11923.00000681@nso-fq.aol.com> <3AB94B56.FBA0E818@cinci-rr.com> <3AB9697A.7E890D26@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message news:3AB9697A.7E890D26@home.com...
> 
> 
…[4 more quoted lines elided]…
> > > >

<< SNIP of an interesting performance tuning tip >>

> > worthwhile maintaining........
> 
…[3 more quoted lines elided]…
> what you consider most effective .......

Jimmy, you're getting mixed up in the jargon. While it is possible to seek out every "field", that doesn't mean there is an index that will get you to that field efficiently. Keys and indices in tables work pretty much as they do in an indexed file. The DB manager keeps track of some statistics which it uses to find it's way to the piece of data as efficiently as possible. Sometimes the DB is forced to do an exhaustive scan (think of it as doing a READ NEXT) of the table to find the row(s) you are after. 

- Karl

> 
> Jimmy, Calgary AB
>
```

###### ↳ ↳ ↳ Re: COBOL Files v. Databases

_(reply depth: 5)_

- **From:** "Michael Mattias" <michael.mattias@gte.net>
- **Date:** 2001-03-22T16:20:59+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<LDpu6.178$dx2.88153@paloalto-snr1.gtei.net>`
- **References:** `<3AB645D8.BE209EFC@home.com> <20010319233114.11923.00000681@nso-fq.aol.com> <3AB94B56.FBA0E818@cinci-rr.com> <3AB9697A.7E890D26@home.com>`

```
James J. Gavan <jjgavan@home.com> wrote in message
news:3AB9697A.7E890D26@home.com...
> Whoa!. Hold it right there and I'm ABSOLUTELY no DB expert. But as I
understand if
> EVERY field in a DB is in effect 'keyed'  - specifically if using SQL.

Well, no, that's not quite true.

It just 'seems' that each field (column) is keyed. The whole idea behind SQL
language was to create a method of data access independent of the specifics
of the datamanager - that is, the application can use the same commands if
the application is using Oracle, DB/2, dBase, Access or any other
SQL89/92/99 compliant datamanager."How" the datamanager does it is why some
databases sell more than others.

An SQL statement tells the datamanager to select records based on the value
of certain columns (fields). If those columns are defined as an index, the
datamanager uses (well, *should use*) that index for efficiency. If that
column is not defined as an index, the datamanager just reads everything and
selects qualifying records.

MCM
```

###### ↳ ↳ ↳ Re: COBOL Files v. Databases

_(reply depth: 6)_

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-03-22T17:35:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3ABA3A18.27FAF96@home.com>`
- **References:** `<3AB645D8.BE209EFC@home.com> <20010319233114.11923.00000681@nso-fq.aol.com> <3AB94B56.FBA0E818@cinci-rr.com> <3AB9697A.7E890D26@home.com> <LDpu6.178$dx2.88153@paloalto-snr1.gtei.net>`

```


Michael Mattias wrote:

> James J. Gavan <jjgavan@home.com> wrote in message
> news:3AB9697A.7E890D26@home.com...
…[4 more quoted lines elided]…
> Well, no, that's not quite true.<snip>

Thanks to Karl and Michael for the clarification.

Phew ! I'm glad I indicated I was no expert on DB or SQL - I would've got
'floored' otherwise <G>

Jimmy
```

###### ↳ ↳ ↳ Re: COBOL Files v. Databases

_(reply depth: 6)_

- **From:** Jeff Baynard <jeffbaynard@home.com>
- **Date:** 2001-03-31T02:08:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<B6EAA661.4D9%jeffbaynard@home.com>`
- **References:** `<3AB645D8.BE209EFC@home.com> <20010319233114.11923.00000681@nso-fq.aol.com> <3AB94B56.FBA0E818@cinci-rr.com> <3AB9697A.7E890D26@home.com> <LDpu6.178$dx2.88153@paloalto-snr1.gtei.net>`

```
No, there are explicit keys on records in every database I've seen.  You
could technically create an index on each column of a record though.

In Informix SQL, I can create and drop indices on the fly, on whatever
columns I want, on whatever tables I want.  That allows me to tune the SQL
procedure, and I have found this to really improve performance in certain
situations (large tables 1 million rows+).  It's all about overhead vs
latency...  Should you take the time to do some work now, at a set amount of
time, in order to maybe save time later.

I have seen routines not complete after 12 hours of processing, then after
putting the correct indices on, complete in 20 minutes.  SQL, Informix at
least, in really pretty dumb if you use it wrong.

I would imagine you can do indices in Oracle SQL+ also.

Jeff

in article LDpu6.178$dx2.88153@paloalto-snr1.gtei.net, Michael Mattias at
michael.mattias@gte.net wrote on 3/22/01 8:20 AM:

> James J. Gavan <jjgavan@home.com> wrote in message
> news:3AB9697A.7E890D26@home.com...
…[27 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: COBOL Files v. Databases

_(reply depth: 4)_

- **From:** thaneH@softwaresimple.com (Thane Hubbell)
- **Date:** 2001-03-24T15:57:51+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3abcc37e.299783387@news1.attglobal.net>`
- **References:** `<3AB645D8.BE209EFC@home.com> <20010319233114.11923.00000681@nso-fq.aol.com> <3AB94B56.FBA0E818@cinci-rr.com>`

```
I have a monthly process where I do the same thing.  When they were
trying to do the process with a Query they gave up after it ran for 30
hours.  It had to do subqueries for each row returned from the main
query.  It was creating a file of the last 6 months activity for any
account that had over 2000  any time in the last 6 months.  The query
was not hard to design, but even with re-indexing the table it was too
slow.  I extract the raw data to an indexed file and create the
resulting spreadsheet.  My process takes about 30 minutes - including
the extract.

On Thu, 22 Mar 2001 00:46:28 GMT, Rob Lec <RobLec@cinci-rr.com> wrote:

>
>
…[22 more quoted lines elided]…
>(To reply by email change dash to dot in address)
```

#### ↳ Re: COBOl Files v. Databases

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2001-04-09T14:13:30-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3g5fauki3moii18r267e2d0vss201vlljc@4ax.com>`
- **References:** `<3AB260A2.A708A555@home.com> <Lqat6.117205$t67.1708087@news1.rdc1.il.home.com>`

```
>For many people that use smaller mainframe's it can be a major cost to
>migrate to a database system.  Besides just changing the file structure you
>would have to change hundreds of programs.  Also keep in mind that would
>require changing about 200 online CICS programs all at once in our case.  In
>other words, it would require a complete system redevelopment.

the way i look at it, it's not the software cost that is the problem
(unless it's licensed). and even if it is, you are going to have to
port the hardware anyways.

reply to email gvwmoore@spam.ix.netcom.com 
remove the spam

points in agreement snipped

spambots pick up these spambots addys

nonesofar
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
