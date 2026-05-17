[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Using COBOL with Relational Databases

_13 messages · 3 participants · 2017-08 → 2017-09_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Using COBOL with Relational Databases

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-30T23:52:01+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<f0pfg3FaakrU1@mid.individual.net>`

```
I have been pressed to provide some "brain dumps" regarding my IT
philosophy. (I think it has to do with an approaching birthday... and
realization that I won't ALWAYS be here... :-))

After all these years, I'm more than happy to give back what I can, so
I'd like to think that somebody, somewhere, can benefit from what I've
written. (Or, at the very least, decide they strongly disagree and move
in a different direction...)

Anyway, I gave it some thought and, rather than write a "memoirs" type
of self-indulgent book, I decided to do some self-indulgent web pages... :-)

The trouble with writing web page content is that it is very difficult
to know how other people will view what you've written (both literally
and figuratively.) Not only that, but if you can't afford to employ a
professional web developer, don't like the idea of using a standard
template like Joomla or WordPress, so your site looks like dozens of
other people's, and really don't want to irritate your visitors with
annoying advertisements, then you have little recourse but to build it
yourself. (You can learn HTML easily in a (rainy) afternoon, and these
days there are superb tools to help you build your site. I'm using the
Web Version of Visual Studio Express 2012 - it's free and it supports
HTML5 and CSS. I'm using ASP.NET with C# code-behinds and it is all
loads of fun...)


The above topic is part of the refurbishment of the COBOL21 (COBOL in
the 21st century) web site which is currently being amalgamated with the
PRIMA web site. Various clients from time to time ask questions about
why I don't "like" certain things relating to data manipulation (like
hanging on to ISAM technology...) so I've taken this opportunity to
explain the reasoning behind some of the positions I take on using RDBMS
with COBOL.

What I would really like is for people here (whose opinions I do
actually value, even if I don't always agree with them) to take a look
and criticize what is there. (Although this could be humiliating and
painful for me, there is no other way to improve and make what is there
useful to people...)

So, if you find yourself needing a coffee break, please go and look at:

http://primacomputing.co.nz/PRIMAmetro/RDBandSQL.aspx

The sort of feedback I'm looking for:

1. You can see the pages in various Browsers (and mobile devices...)
2. There are no broken links.
3. You found the content interesting (or not...)
4. You think the pages could be useful to COBOL people (or not)

Or, whatever comments you want to make.

Please post here, or privately to me.

The COBOL21 site is linked to this newsgroup and it is intended to be a
"COBOL place" just as this Newsgroup has always been. It is a huge
amount of work to implement everything I actually want there (some of
the tiles on the hub (http://primacomputing.co.nz) are currently being
worked on and others are having their existing content reviewed and
refurbished), and do real work as well, but I'm giving it a go...

I hope you'll mark the site and copy people you think would enjoy it. It
will evolve over the next few months (if I can still see and type... :-))

Cheers,

Pete.
I used to write COBOL; now I can do anything...
```

#### ↳ Re: Using COBOL with Relational Databases

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-08-31T02:34:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p2@usenetarchives.gap>`
- **In-Reply-To:** `<f0pfg3FaakrU1@mid.individual.net>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net>`

```
On 8/30/2017 10:52 PM, pete dashwood wrote:
› I have been pressed to provide some "brain dumps" regarding my IT 
› philosophy. (I think it has to do with an approaching birthday... and 
…[25 more quoted lines elided]…
› 

Pete,

I viewed those pages in Firefox and Chrome and they looked identical. I
didn't notice any problems with the formatting. All the links from the
"portal" link on page 2 seemed to work fine. I might not have followed
every link, but I never found a broken link. I enjoyed the old story of
disk drives (have you ever heard of IBM's "noodle-picker"?).

I found the contents interesting, and I think the pages would be very
useful to COBOL people. Now if only the managers could pay attention...

I do have some minor quibbles, probably not anything big enough to
require any changes on your part. You've simplified the differences
between ISAM and DBMS for the article and I've seen some exceptions in
the real world. That doesn't mean your explanation is "wrong".

You seemed to say that ISAM requires constant housekeeping and DBMS does
not. I would disagree. I've seen a large IBM DB2 system with over 100
tables, and for a major upgrade the database had to be taken down for
over 8 hours to rebuild data (new columns, new tables), convert existing
data, and reload it. I'm sure you would have similar problems with
Oracle or other DBMS systems.

I'm not denying that ISAM requires constant housekeeping, I'm arguing
DBMS can require some major housekeeping of its own, of a different
kind. But at the same time you get much more power and flexibility with
DBMS compared with ISAM.

In my experience there is NO performance advantage for ISAM (or IBM KSDS
VSAM) compared to IBM DB2, especially in those cases where you would
want to use alternate indexes with VSAM KSDS. Where performance is
measured for really large datasets with complex relationships, a modern
DBMS should be faster than ISAM.

They used to say nothing was faster on an IBM mainframe that BDAM.
Sure, if you want your COBOL program to read disk records by physical
address, and assuming you knew the address or could calculate it. With
modern systems the data should be indexed by key or pointer and cached
in memory. BDAM is no longer even orderable as a z/OS component because
it is just not fast enough any more. Today's data management technology
is more complex but also more powerful and flexible. You've made an
excellent case for that.

You also suggest that performance is not a problem with DBMS (on modern
devices with modern software). I would also disagree. There are always
cases where bad or incomplete design (or changing business rules) create
performance problems, but a good DBA should be able to tune the system
to solve most of those problems.

You also imply that DBMS does not have the space management problems
that ISAM does. In fact, it has different space problems. I've seen a
DB2 table with 400 million rows getting 25 to 50 million new rows per
day, and believe me, you will have space management problems. Even if
you don't run out of space your query time may increase intermittently.
Once users get used to sub-second response time they scream if it falls
to 5 seconds.

Where I had a problem with DB2 was that it was owned by the DBA's and
they were were a different department from application development.
Fortunately we had excellent relations with our DBA's, and they were
real wizards. In some corporate cultures the two groups might be at
each others throats like Operations versus Programming in the old days.

If I needed a TEST DB2 table, I could not create it for myself. The
DBA's had to do it for me, because they administered all the tables and
all the DB2 plans or schemas. We could write our own SQL, but it had to
be reviewed and approved by our DBA's. Quite often they would require
changes that improved it, but which we were not able to foresee. We
didn't have the DBMS skills that the DBA's had.

So for a small, simple application it might be quicker to develop a VSAM
KSDS file, since I didn't have to wait a week for another department to
create my test file. But I only did that if I could live with the
limitations of ISAM, including the maintenance issues. ISAM was still
"good enough" in some cases, especially if budget was an issue.

You've written on occasion about "fortress COBOL" and the data being
locked up in files and record layouts controlled by COBOL applications
development. The same problem also exists with DBMS, especially with
today's security and privacy concerns. The data is now owned by the
DBA's, but the tools to get at that data are better than for ISAM.

>From my point of view as a programmer, one huge advantage to DBMS
(which you also pointed out) is that the data definition (the "record
layout" in COBOL terms) is also stored in the DBMS. That means it can
be searched and manipulated much more easily by a programmer than COBOL
record layouts scattered in various libraries, programs, and copybooks.

Overall, I would say it's well-written and very informative. I saved
those pages because you made your case.

Kind regards,


http://www.arnoldtrembley.com/GnuCOBOL.htm
```

##### ↳ ↳ Re: Using COBOL with Relational Databases

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-08-31T02:41:03+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p3@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p2@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap>`

```
This showed up in bit.listserv.ibm-main recently. It does relate to the
issue:

===quote===

Subject: dumb VSAM KSDS & AIX question.
From: joh··n@GM··L.COM (John McKown)
Date: 8/30/2017 3:34 PM
Newsgroups: bit.listserv.ibm-main

A programmer came by with a question. He asked if, when you are reading
a VSAM KSDS via an alternate index (PATH), to have duplicates returned
in base key order. I don't think that is possible. From examining the
contents of the AIX records themselves, it appears to me that the base
key for a "new" base record with a given alternate key is just placed at
the end of the keys. Yes, I know, if this sort of thing is a
requirement, we need Db2 (or is it DB2), but that is _never_ going to
happen around here.

-- Caution! The OP is an hyperpolysyllabicsesquipedalianist and this
email may cause stress to those with
hippopotomonstrosesquipedaliophobia. Maranatha! <>< John McKown
----------------------------------------------------------------------
For IBM-MAIN subscribe / signoff / archive access instructions, send
email to lis··v@lis··a.edu with the message: INFO IBM-MAIN

===end quote===


http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: Using COBOL with Relational Databases

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-08-31T09:16:04+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p4@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p3@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap> <gap-ebed4892c1-p3@usenetarchives.gap>`

```
In article ,
Arnold Trembley wrote:
› This showed up in bit.listserv.ibm-main recently.  It does relate to the 
› issue:
…[10 more quoted lines elided]…
› in base key order. I don't think that is possible.

I know it *is* possible for batch processing but I'm not sure about
individual records.

DD
```

###### ↳ ↳ ↳ Re: Using COBOL with Relational Databases

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-31T20:50:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p5@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p3@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap> <gap-ebed4892c1-p3@usenetarchives.gap>`

```
On 31/08/2017 6:41 PM, Arnold Trembley wrote:
› This showed up in bit.listserv.ibm-main recently.  It does relate to the 
› issue:
…[26 more quoted lines elided]…
› 
The primary sequence of duplicate alternate keys is "indeterminate" but
there are programming devices that will let you do what he wants. It is
"possible".

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Using COBOL with Relational Databases

_(reply depth: 4)_

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-08-31T21:48:06+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p6@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p5@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap> <gap-ebed4892c1-p3@usenetarchives.gap> <gap-ebed4892c1-p5@usenetarchives.gap>`

```
On 8/31/2017 7:50 PM, pete dashwood wrote:
› On 31/08/2017 6:41 PM, Arnold Trembley wrote:
›› This showed up in bit.listserv.ibm-main recently.  It does relate to 
…[33 more quoted lines elided]…
› 

The few times I worked with IBM VSAM alternate indexes it always gave me
a headache.

I suspect the alternate keys would have to be redesigned to allow this,
and the problem could have been prevented. It would be difficult (or
even impossible) to solve it in VSAM/ISAM and without changing the
current alternate key structure.

But it should be trivial to solve in a relational DBMS. All ya gotta do
is add an "ORDER BY" clause correctly.

I'm just glad I don't need to work with VSAM AIX and PATH anymore.


http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: Using COBOL with Relational Databases

_(reply depth: 5)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-09-02T02:01:07+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p7@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p6@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap> <gap-ebed4892c1-p3@usenetarchives.gap> <gap-ebed4892c1-p5@usenetarchives.gap> <gap-ebed4892c1-p6@usenetarchives.gap>`

```
On 1/09/2017 1:48 PM, Arnold Trembley wrote:
› On 8/31/2017 7:50 PM, pete dashwood wrote:
›› On 31/08/2017 6:41 PM, Arnold Trembley wrote:
…[42 more quoted lines elided]…
› current alternate key structure.

No, it's not too hard at all.

You use skip sequential access on the alternate key and save the primary
keys you encounter for each secondary, until the secondary key changes.
(Because COBOL uses OCCURS and it has a limit for the table you are
storing the primary keys in, you might need to check if the limit was
blown and "page" the results...)

Sort the collection/table of primary keys in memory (or add them in the
correct sequence as you retrieve them) and you have a collection of
duplicate secondary keys, in primary key sequence...

No physical changes to key structure required.

In LINQ, you could treat the whole file as a collection of structures
(records) and use SORT, similarly to what you described for the RDBMS.
(It would be one statement... but you might need to implement the
IQueryable interface on the collection you loaded the file into...)



›
› But it should be trivial to solve in a relational DBMS.  All ya gotta do
…[4 more quoted lines elided]…
›

It's pretty obvious why the world uses databases... :-)

Pete.


I used to write COBOL; now I can do anything...
```

##### ↳ ↳ Re: Using COBOL with Relational Databases

- **From:** "docdwarf" <ua-author-6588713@usenetarchives.gap>
- **Date:** 2017-08-31T09:09:08+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p8@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p2@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap>`

```
In article <1JidnZAAbsRzMDrEnZ2dnUU7-VXN··d@gig··s.com>,
Arnold Trembley wrote:

[snip]


› I'm not denying that ISAM requires constant housekeeping, I'm arguing
› DBMS can require some major housekeeping of its own, of a different
› kind.

'Those old carpeted floors need too much vacuuming... let's install
linoleum and we won't need to clean them!'

'Sir, linoleum needs to be at least swept... sometimes polished.'

'Dare you question the wisdom of the Corner Office Idiot? I say they'll
need no vacuuming and they'll need none!'

[snip]

› You also imply that DBMS does not have the space management problems 
› that ISAM does.  In fact, it has different space problems.  I've seen a 
› DB2 table with 400 million rows getting 25 to 50 million new rows per 
› day, and believe me, you will have space management problems.

Mr Trembley, how can there be such volume when the entire country contains
but five million people?

(... and thanks for the reminder that Large Volume isn't 75,000 rows of
400 characters each)

[snip]

› If I needed a TEST DB2 table, I could not create it for myself.  The 
› DBA's had to do it for me, because they administered all the tables and 
…[3 more quoted lines elided]…
› didn't have the DBMS skills that the DBA's had.

You mean - gasp! - that They Did Their Jobs in order so that You Could Do
Yours? This sounds like a strategy for an organisation that will benefit
from both foxes and hedgehogs.

DD
```

##### ↳ ↳ Re: Using COBOL with Relational Databases

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-31T20:46:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p9@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p2@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap>`

```
On 31/08/2017 6:34 PM, Arnold Trembley wrote:

Wow!

This is brilliant!

Thanks SO much Arnold.

I've posted some responses below... hopefully to clarify some of the points.

› On 8/30/2017 10:52 PM, pete dashwood wrote:
›› I have been pressed to provide some "brain dumps" regarding my IT 
…[32 more quoted lines elided]…
› disk drives (have you ever heard of IBM's "noodle-picker"?).
 
› No, do tell... :-)
› 
› I found the contents interesting, and I think the pages would be very 
› useful to COBOL people.  Now if only the managers could pay attention...

Sadly, (uninformed) Management have been the bane of IT right throughout
my career.

› 
› I do have some minor quibbles, probably not anything big enough to 
…[4 more quoted lines elided]…
› Sure, I used "ISAM" very loosely...
 
› You seemed to say that ISAM requires constant housekeeping and DBMS does 
› not.  I would disagree.  I've seen a large IBM DB2 system with over 100 
…[3 more quoted lines elided]…
› Oracle or other DBMS systems.

That is certainly true, but the RDBMS maintenance is separate from the
application and it can be split into parts. Some clusters can be
"maintained" while others are still "working"; you can't do that with an
indexed file.
› 
› I'm not denying that ISAM requires constant housekeeping, I'm arguing 
…[3 more quoted lines elided]…
› Yep.
 
› 
› In my experience there is NO performance advantage for ISAM (or IBM KSDS 
…[3 more quoted lines elided]…
› DBMS should be faster than ISAM.

Your experience is probably mostly predicated on mainframes where the
actual execution times are pretty much unobservable by a human. (You can
only see response times at the terminal, or check logs to see how much
CPU and IO time was used.) On a PC it becomes painfully apparent if
something is not performing well because you are sitting there watching
it... :-)

› 
› They used to say nothing was faster on an IBM mainframe that BDAM. Sure, 
…[6 more quoted lines elided]…
› excellent case for that.
 
› Thanks. I agree with what you say abut BDAM and have used it many years ago.
 
› 
› You also suggest that performance is not a problem with DBMS (on modern 
…[3 more quoted lines elided]…
› to solve most of those problems.

THAT was the point. It can be fixed without impacting the applications.
(I was careful to qualify what I said with the fact that the DB design
has to be good.)
› 
› You also imply that DBMS does not have the space management problems 
…[5 more quoted lines elided]…
› to 5 seconds.

In a separate life where I was a DBA for a while, this is the kind of
thing I would love to address. I have never worked with such volumes but
I believe it is a challenge that any good DBA would be pleased to accept.

› 
› Where I had a problem with DB2 was that it was owned by the DBA's and 
…[3 more quoted lines elided]…
› each others throats like Operations versus Programming in the old days.

Yes, I have encountered this syndrome on a number of sites. It is one of
the reasons why people combine DBs and tables incorrectly (because it is
easier to use an existing DB that they DO have permission for than to
request permission for a NEW DB), or just use indexed files and avoid
the paperwork with the DBA...

› 
› If I needed a TEST DB2 table, I could not create it for myself.  The 
…[4 more quoted lines elided]…
› didn't have the DBMS skills that the DBA's had.

You can understand WHY companies do this; the data resource is the most
precious thing they have (next to their employees), but I agree that it
is counter productive. Good DBAs will allocate expendable TEST DBs and
give permissions on them that allow programmers to basically do what
they want. When the testing is done, the Test stuff can be reviewed by
the DBA and copied to the production system (or not).

I had occasion once in Spain where we (my team) were required to design
and develop a Major IMS DB system for a major Bank. We did this over 10
months and when we came to deliver it, the Bank's Chief DBA said:"No,
you can't implement that here because it violates our standards; we only
allow 3 levels of hierarchy and you have designed 4." (IBM actually
support 16 and we NEEDED 4...)

Eventually she was overridden and it went in. She never spoke to me
again. (Political decisions can be very hard on people.)

› 
› So for a small, simple application it might be quicker to develop a VSAM 
…[3 more quoted lines elided]…
› "good enough" in some cases, especially if budget was an issue.

What you say is sound common sense under the circumstances, but stand
back a bit... what has happened here? A technical decision has been
taken because of the political climate. It's no wonder so many sites
have problems with data handling.

› 
› You've written on occasion about "fortress COBOL" and the data being 
…[3 more quoted lines elided]…
› DBA's, but the tools to get at that data are better than for ISAM.

I disagree. Permissions must be managed but the difference is that
ANYONE can sit down and use the tools I mentioned (SQL, QBE... etc.) to
view data on the corporate DB. The DATA IS NOT OWNED BY THE DBA's! It is
a Corporate resource and for it to be useful, it needs to be shared by
the Corporation. I talk about exactly this on the video about salvaging
COBOL.

› 
›  From my point of view as a programmer, one huge advantage to DBMS 
…[6 more quoted lines elided]…
› those pages because you made your case.

Thanks very much for your feedback, Arnold.

Cheers,

Pete.
I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Using COBOL with Relational Databases

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-08-31T21:38:10+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p10@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p9@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap> <gap-ebed4892c1-p9@usenetarchives.gap>`

```
On 8/31/2017 7:46 PM, pete dashwood wrote:
› On 31/08/2017 6:34 PM, Arnold Trembley wrote:
› (snip) 
…[9 more quoted lines elided]…
› No, do tell... :-)

You can actually read about IBM's "noodle picker" in Wikipedia:

https://en.wikipedia.org/wiki/IBM_2321_Data_Cell

The article says it was a successful direct access storage device, but
that particular technological approach has long since been abandoned.
For the obvious reasons.

Kind regards,


http://www.arnoldtrembley.com/
```

###### ↳ ↳ ↳ Re: Using COBOL with Relational Databases

_(reply depth: 4)_

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-09-01T18:44:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p11@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p10@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap> <gap-ebed4892c1-p9@usenetarchives.gap> <gap-ebed4892c1-p10@usenetarchives.gap>`

```
On 1/09/2017 1:38 PM, Arnold Trembley wrote:
› On 8/31/2017 7:46 PM, pete dashwood wrote:
›› On 31/08/2017 6:34 PM, Arnold Trembley wrote:
…[22 more quoted lines elided]…
› 
Hi Arnold,

I remember someone talking about a new device from IBM called a "Data
Cell" but I don't think they were ever installed in New Zealand. I never
heard of the "noodle picker" but after reading the Wikipedia entry it
sounds apposite.

Thanks for the link. It SHOULD have been in my article (which was
originally published in an Australian computer magazine that I wrote a
regular column for, back in the '80s) the current link is to an NCR
historical website who picked up my article a few years back. I have no
control over the link but it has been up for some years now so I guess
it will be there as long as the site is there. The Internet is pretty
amazing... :-)

Thanks for the link.

Pete.

I used to write COBOL; now I can do anything...
```

###### ↳ ↳ ↳ Re: Using COBOL with Relational Databases

- **From:** "arnold.trembley" <ua-author-6588734@usenetarchives.gap>
- **Date:** 2017-08-31T22:38:12+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p12@usenetarchives.gap>`
- **In-Reply-To:** `<gap-ebed4892c1-p9@usenetarchives.gap>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net> <gap-ebed4892c1-p2@usenetarchives.gap> <gap-ebed4892c1-p9@usenetarchives.gap>`

```
Some additional comments...

On 8/31/2017 7:46 PM, pete dashwood wrote:
› On 31/08/2017 6:34 PM, Arnold Trembley wrote:
› 
…[4 more quoted lines elided]…
› Thanks SO much Arnold.
 
› You are most welcome!
 
› (snip) 
›› 
…[11 more quoted lines elided]…
› indexed file.

This is a good point that may be hard for managers to understand. You
can add a new column to a DBMS table, and only the COBOL programs that
need the new column are affected. Programs that use the same table but
don't need the new column do not even need to be recompiled. In DB2
they might need a bind to the new DB2 plan, but that's the DBA's
problem, not applications development.

Maintaining the data base separately from the applications programs has
real benefits, but the disadvantage is the addition coordination
required between applications development and DataBase administration
during large projects.


›› (snip) 
› 
…[8 more quoted lines elided]…
› has to be good.)

I experienced a specific example of this, where a CICS DB2 query that
required sub-second response time dragged into several minutes. It was
a major show-stopper. The problem was caused by poor design and not
found because testing did not include large volumes of insert data. But
our DBA wizards were able to work out a solution within the DBMS. As I
recall we also had a make a minor change to our SQL, but 5 minute
response time was reduced to sub-second response time.

So you may want to emphasize the benefits of the DBMS being maintained
separately from the applications programs.

›› (snip)
›› 
…[10 more quoted lines elided]…
› have problems with data handling.

I agree this is a bad situation. But I've seen this on numerous
occasions. A problem comes up, the implementation date is only a few
days away, there's no money left in the budget, and management says, "I
don't care what you have to do. It needs to be fixed NOW!".

So we get quick and dirty fixes that might cause problems in the future.

› (snip) 
› 
› Thanks very much for your feedback, Arnold.
 
› It was my pleasure.
 
› 
› Cheers,
› 
› Pete.


http://www.arnoldtrembley.com/
```

#### ↳ Re: Using COBOL with Relational Databases

- **From:** "dashwood" <ua-author-14501808@usenetarchives.gap>
- **Date:** 2017-08-31T19:35:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<gap-ebed4892c1-p13@usenetarchives.gap>`
- **In-Reply-To:** `<f0pfg3FaakrU1@mid.individual.net>`
- **References:** `<f0pfg3FaakrU1@mid.individual.net>`

```
On 31/08/2017 3:52 PM, pete dashwood wrote:
› I have been pressed to provide some "brain dumps" regarding my IT 
› philosophy. (I think it has to do with an approaching birthday... and 
…[66 more quoted lines elided]…
› Pete.
I have had a report that when using the Opera browser, the site is
marked as malicious by Yandex (a huge Russian company).

Obviously, it is not, and we go to great pains to ensure that visits and
downloads are safe.

I have written to Yandex and explained the problem, so hopefully, they
will remove us from their blacklist.

Apparently there is a "protect" module provided by them, that is a
browser plugin. It is possible that people who install Opera may also be
installing this module.

If you are in this category, please mark us as "safe". Here's their web
page on how to do it:

https://yandex.ru/support/browser-beta/security/hips.html#trusted

Thanks,

Pete.

I used to write COBOL; now I can do anything...
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
