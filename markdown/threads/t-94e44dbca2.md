[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# COBOl Files v. Databases

_7 messages · 6 participants · 2001-03 → 2001-04_

**Topics:** [`Databases and SQL`](../topics.md#databases)

---

### Re: COBOl Files v. Databases

- **From:** "Denny Brouse" <denden@prodigy.net>
- **Date:** 2001-03-19T00:10:55-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<99448d$3og2$1@newssvr05-en0.news.prodigy.com>`
- **References:** `<3AB260A2.A708A555@home.com> <98vdqk$c7n@netnews.hinet.net>`

```
Jason and Jimmy, Calgary AB

<snip from Jason>
Finally, for the portability of cobol programs, I  think each cobol vendor
should provide utility for converting their data files to  ascii files.
Ascii files means greater freedom even converting to DB.
I have converted my old MF cobol files to FJ cobol by writing programs
do the work.
<unsnip>

Although this group is predominately IBM oriented, I work for a major
Midwest bank that processes between 600,000 - 900,000 checks a day on a
Unisys NX-5600 open platform system.  We have an PC MS Access database for
our statistics, so that all the people that "number crunch" can  retrieve
them from the Access DB.  How do we feed the database?  Using Fujitsu Cobol,
we can actually map a Network drive to the NX-5600, and read the necessary
numbers from a flat sequential Mainframe file that is created as a byproduct
of the huge random access file of those 600,000-900,000 items created by 3
check sorters.  A portion of the NX-5600 operating system named NX-Services
handles the EBCDIC to ASCII conversion automatically.  And the Fujitsu
program reads the file exactly as defined on the mainframe as far as record
size, blocksize, filename, etc.

Also, this system is capable of being an SQL server on it's own, but there
simply is no need to create a database from items that come in directly from
these sorters.  We need to be able to see a transaction as it was
"captured", i.e. deposit of a check or two, maybe a utility and a loan
payment, etc.  To set up a database for this type on environment would not
be needed.  Plus, has anyone ever attempted to find info in a database this
size?  It certainly can be done, but in my opinion, it isn't pretty and it
certainly isn't speedy.  In this particular case, Mainframe COBOL file
structure rules!!!

Denny
```

#### ↳ Re: COBOl Files v. Databases

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-03-19T19:17:13+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB65D80.5582A1A@home.com>`
- **References:** `<3AB260A2.A708A555@home.com> <98vdqk$c7n@netnews.hinet.net> <99448d$3og2$1@newssvr05-en0.news.prodigy.com>`

```


Denny Brouse wrote:

> Jason and Jimmy, Calgary AB
>
…[6 more quoted lines elided]…
> <unsnip>

> Although this group is predominately IBM oriented, I work for a major
> Midwest bank that processes between 600,000 - 900,000 checks a day on a
…[20 more quoted lines elided]…
>

Denny,

Good ! I'm glad one of our 'banking boys' jumped in because of the obvious
volumes you handle.

Certainly there is a distinct difference between front-end input as you describe
(MICR for banks,  OCR for utilities(electrIcity, gas etc.), and from my own
experience, (design, not programming), using OCR to input payroll; add to that
list the front-end for POS systems.- set against that  the approach you might
take with a truly interactive system - which is mostly what new PC applications
are about.

POS crosses the line here. For the big retailers it's the front end approach
similar to what you are describing. In the case of the Mom and Pop store using a
PC as POS - then arguably having said, 'OK print sales slip' the transaction
could directly enter a DB system. To illustrate this point - we've gone private
on liquor stores here. The word 'private' is questionable since the provincial
government still does warehousing and controls distribution.

Now many of these small retailers are strapped for cash. Around a 'holiday'
period, they can't wait for the traditional approach of producing a sales
summary at the end of the day. Given a system which 'updates immediately' they
would see a benefit from an application which allows them to query sales at
11:45, 15.00 17.30 or whatever - and believe me they'll dash out the door to
pick up a couple of cases of whiskey, based on the cash currently sat in the
till.

I was curious about your comments about query the 'falt-file/DB' for
transactions, specifically where you have zillions of transactions, and this was
something mulling in the back of my mind.

Flat files - as a generalization postal/zip code is not usually considered a
'keyed' field.
(It is when part of your application is geared to customized mailing lists).It
makes sense to limit Alternate keys. Now the DB 'argument(?)' would be that
every field is 'keyed' and use SQL to get at a specific feature.

So taking the two, flat files or DB, and with LARGE volumes, do they come out
equal :-

(a) Flat files
- could add an Alternate Key if it becomes apparent this is going to be a
regular feature, or
- Sequentially read Customer/Consumer file picking up on postal/zip value, to
produce a specific listing.

(b) DBs
- use SQL syntax to 'search', (I'm not into SQL yet so I don't have the buzz
phrase on my lips) where the postal/zip fits the criteria.

Now taking those two options and a LARGE file - will one be more effective than
the other ?

Jimmy, Calgary AB
```

##### ↳ ↳ Re: COBOl Files v. Databases

- **From:** Howard Brazee <howard@brazee.net>
- **Date:** 2001-03-19T12:40:30-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB660AE.D70FEE4A@brazee.net>`
- **References:** `<3AB260A2.A708A555@home.com> <98vdqk$c7n@netnews.hinet.net> <99448d$3og2$1@newssvr05-en0.news.prodigy.com> <3AB65D80.5582A1A@home.com>`

```
"James J. Gavan" wrote:

> (a) Flat files
> - could add an Alternate Key if it becomes apparent this is going to be a
> regular feature, or
> - Sequentially read Customer/Consumer file picking up on postal/zip value, to
> produce a specific listing.

It still seems odd to me to see someone mentioning a keyed file as being flat.

One old file system which was very efficient, but which seems to have disappeared
was relative files.
```

##### ↳ ↳ Re: COBOl Files v. Databases

- **From:** "Oscar T. Grouch" <dustbin@home.com>
- **Date:** 2001-03-19T20:12:14+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<yKtt6.82752$p66.23724119@news3.rdc1.on.home.com>`
- **References:** `<3AB260A2.A708A555@home.com> <98vdqk$c7n@netnews.hinet.net> <99448d$3og2$1@newssvr05-en0.news.prodigy.com> <3AB65D80.5582A1A@home.com>`

```

"James J. Gavan" <jjgavan@home.com> wrote in message news:3AB65D80.5582A1A@home.com...

<<SNIP>> 

> So taking the two, flat files or DB, and with LARGE volumes, do they come out
> equal :-
…[15 more quoted lines elided]…
> 

It depends... :o). If you are processing the records sequentially, and all records will be accessed, then it's a close race between DB and indexed files. Sorted sequential files win that race because they don't have any overhead doing index lookup. In a fair comparison, sequential and indexed file processing and would be slowed a bit by checkpoint restart,  rollback recovery, and optional journalling that are usually handled by the database manager.

However, if you want to know all the unique postal codes in the database, or those postal codes that represent a certain minimum value of sales, or some such thing, then the SQL query will be easier to write/maintain, and there's a good chance that the DB will be able to retrieve the information faster, all things being equal. The DB is able to optimize the query based on all indices that may be referenced by the query, rather than having to sequentially process all those duplicate records looking for the ones of interest.


Karl
```

###### ↳ ↳ ↳ Re: COBOl Files v. Databases

- **From:** "James J. Gavan" <jjgavan@home.com>
- **Date:** 2001-03-19T21:22:02+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3AB67AB9.7F4643AC@home.com>`
- **References:** `<3AB260A2.A708A555@home.com> <98vdqk$c7n@netnews.hinet.net> <99448d$3og2$1@newssvr05-en0.news.prodigy.com> <3AB65D80.5582A1A@home.com> <yKtt6.82752$p66.23724119@news3.rdc1.on.home.com>`

```


"Oscar T. Grouch" wrote:

> "James J. Gavan" <jjgavan@home.com> wrote in message news:3AB65D80.5582A1A@home.com...
>
…[25 more quoted lines elided]…
> Karl

Yep, I buy that about DBs - if you are doing a multiple query as you suggest.

Jimmy
```

###### ↳ ↳ ↳ Re: COBOl Files v. Databases

- **From:** Joseph J Katnic <josephk@iinet.net.au>
- **Date:** 2001-03-20T22:37:16+08:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<josephk-8DB58A.22371620032001@news.m.iinet.net.au>`
- **References:** `<3AB260A2.A708A555@home.com> <98vdqk$c7n@netnews.hinet.net> <99448d$3og2$1@newssvr05-en0.news.prodigy.com> <3AB65D80.5582A1A@home.com> <yKtt6.82752$p66.23724119@news3.rdc1.on.home.com>`

```
In article <yKtt6.82752$p66.23724119@news3.rdc1.on.home.com>, "Oscar T. 
Grouch" <dustbin@home.com> wrote:

> It depends... :o). If you are processing the records sequentially, and 
> all records will be accessed, then it's a close race between DB and 
…[5 more quoted lines elided]…
> 
Ok if we are talking DB2 on MF, then you have to include the cost of the 
SORT before you run your cobol program. In which case you might just be 
supprised how quick that DB2 DB can perform. DB2 will sort the keys for 
you so that you can access the records "sequentially". It will then 
pre-load the data pages into memory such that the program will 
experience minimum I/O delays for the access.
```

##### ↳ ↳ Re: COBOl Files v. Databases

- **From:** G Moore <gvwmoore@spam.ix.netcom.com>
- **Date:** 2001-04-09T14:13:29-04:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<m36fau09cqq2639dtdg5ie4o8u8d4stsc8@4ax.com>`
- **References:** `<3AB260A2.A708A555@home.com> <98vdqk$c7n@netnews.hinet.net> <99448d$3og2$1@newssvr05-en0.news.prodigy.com> <3AB65D80.5582A1A@home.com>`

```
 In the case of the Mom and Pop store using a
>PC as POS - then arguably having said, 'OK print sales slip' the transaction
>could directly enter a DB system. To illustrate this point - we've gone private
…[3 more quoted lines elided]…
>Now many of these small retailers are strapped for cash. 

i dunno how many are strapped for cash. i do know that sometimes small
biz eats up big biz and vice versa. for computers, at least today,
small biz will eat up big biz in the service sector. the resume
hunters may get organized, but for something which changes daily, big
biz can't get a foothold. microsoft had a foothold from about win 3.0
to win 98se, but now it's lost it again. i think it started losing
about the time linux entered the scene and they offered internet
explorer for free. you can't compete with free.

now the inet is trying to swallow the education market. the prob is,
there was never any lack of geographically-isolated educators. and if
you get a classroom the size of ten, the price of webcams and
coursework is easily outdone by the price of a train and apartment
cost.




reply to email gvwmoore@spam.ix.netcom.com 
remove the spam

points in agreement snipped

spambots pick up these spambots addys

nonesofar
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
