[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)

# Database versus COBOL indexed files

_26 messages · 15 participants · 2002-08 → 2002-09_

**Topics:** [`Databases and SQL`](../topics.md#databases) · [`VSAM, files, sorting`](../topics.md#files)

---

### Database versus COBOL indexed files

- **From:** philhickling@compuserve.com (Phil Hickling)
- **Date:** 2002-08-29T06:23:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a371be2.0208290523.13ca39d9@posting.google.com>`

```
What are the relative advantages and disadvantages of an sql database
system as compared with COBOL indexed files?

I have a client using a networked system for 100+ users, developed
using MicroFocus NetExpress, accessing a database of 30 indexed files,
3 Gb in total size, 1Gb largest file (plus 5 Gb archived data), about
10 million live records.  About 80% of users connect via the local NT4
LAN, the remainder via a WAN using Citrix WinFrame.  It all works OK,
but we face a possible 10 times expansion, and are concerned that
performance may disintegrate.

Would an sql database system such as Oracle, Sybase, etc. be better? 
Are there other options for improving performance?  Can COBOL systems
and indexed files cope with 1000+ users, and 30Gb databases?
```

#### ↳ Re: Database versus COBOL indexed files

- **From:** Binyamin Dissen <postingid@dissensoftware.com>
- **Date:** 2002-08-29T10:15:22-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<nfesmu88bk74mvkhm3va1vvd6f1mbm2b6i@4ax.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com>`

```
On 29 Aug 2002 06:23:25 -0700 philhickling@compuserve.com (Phil Hickling)
wrote:

:>What are the relative advantages and disadvantages of an sql database
:>system as compared with COBOL indexed files?

SQL access.

Lot more storage and DASD use. Lot more maintenance.

:>I have a client using a networked system for 100+ users, developed
:>using MicroFocus NetExpress, accessing a database of 30 indexed files,
:>3 Gb in total size, 1Gb largest file (plus 5 Gb archived data), about
:>10 million live records.  About 80% of users connect via the local NT4
:>LAN, the remainder via a WAN using Citrix WinFrame.  It all works OK,
:>but we face a possible 10 times expansion, and are concerned that
:>performance may disintegrate.

:>Would an sql database system such as Oracle, Sybase, etc. be better? 
:>Are there other options for improving performance?  Can COBOL systems
:>and indexed files cope with 1000+ users, and 30Gb databases?

Depends on the implementation of COBOL, coding skills of developers, type of
access to the data, etc.
```

#### ↳ Re: Database versus COBOL indexed files

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-08-29T12:39:25-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0208291139.47a4f2be@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com>`

```
philhickling@compuserve.com (Phil Hickling) wrote 

> What are the relative advantages and disadvantages of an sql database
> system as compared with COBOL indexed files?

The major advantages that I see for SQL are that it can be accessed by
several different systems at one time independant of the computer
language and this includes direct client programs.

Indexed files are usually tied to the particular implementation of a
specific language.
 
> I have a client using a networked system for 100+ users, developed
> using MicroFocus NetExpress, accessing a database of 30 indexed files,
…[8 more quoted lines elided]…
> and indexed files cope with 1000+ users, and 30Gb databases?

Could Windows cope with 1000 users and 30Gb database ?  Could the LAN
cope with the traffic ?  There are far more fundemental problems with
scaling performance than worying about whether you should should
rewrite the programs.

In fact I would suggest that you need to avoid going to an SQL server
because it alone could take some time to design and tune.  You would
most likely find that just going to SQL would initially give severe
degradation in performance until you worked out how to tune and
optimise it.

Does MF have FileShare server running on a really grunty multiCPU
server ?  If so that could help in keeping the LAN traffic down (by
localising the index lookups) and would also help consistency and
recovery.
```

#### ↳ Re: Database versus COBOL indexed files

- **From:** "William M. Klein" <wmklein@nospam.ix.netcom.com>
- **Date:** 2002-08-29T14:43:31-05:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<akltha$nvm$1@slb7.atl.mindspring.net>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com>`

```
Some PROs and CONs of each.

Many COBOL implementations have "optimized" indexed file systems.  I believe
that NetExpress is one of those.  This MAY perform better than "generalized"
(even optimized) SQL systems.

Most SQL systems have BETTER "transaction processing" (checkpoint, rollback,
etc) features than "native COBOL".

If you know that your entire application will ALWAYS be written in COBOL,
then that MAY be the best fit for your "built-in" programmer knowledge base.
On the other hand, most SQL systems have built in "user inquiry" and "ad hoc
report" facilities.  Furthermore, it is easier to interface with OTHER
languages using SQL if you are running on a system where the compiler
vendor, not the operating system vendor provides the data access system.
(For example, on IBM mainframes, the indexed file system is "independent" of
COBOL while on Windows and Unix there are "some" independent systems such as
C-ISAM and Btrieve, but most compilers "default" to a proprietary system).

How many "search" fields do you think you will EVER need to use from your
data - and in what combinations?  Certainly COBOL "alternate indexes" work
in many applications - however, the more you have the more performance (and
data integrity) MAY suffer in certain cases.  SQL, on the other hand, is
DESIGNED for both optimized and occasional individual and multiple field
"searches".

I am certain that there are many, MANY, other things that might impact your
decision.  My "guess" is that for the long term, you would be better with a
"production quality" SQL than with a COBOL indexed file, but that will (of
course) add to the cost of your application - and its complexity if your
programmers are not used to SQL and COBOL applications.
```

#### ↳ Re: Database versus COBOL indexed files

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-08-29T22:34:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D6EA31E.B4EE4868@shaw.ca>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com>`

```
Come on guys, Phillip posted a similar message at M/F Answer Exchange. I
suggested he would probably get better coverage here, beyond what Bill and
Richard have already written. Come on you DB2 users - any comments ?

** see below

Phil Hickling wrote:

> What are the relative advantages and disadvantages of an sql database
> system as compared with COBOL indexed files?
…[11 more quoted lines elided]…
> and indexed files cope with 1000+ users, and 30Gb databases?

Philip, I wont touch this one with a barge pole - my particular volumes
are too small.
I checked back on Answer Exchange and see you are in Worcs. Boy ! Do a lot
of our American friends have trouble pronouncing that one. Knowing you are
in UK, following is relevant.

- Is the NCC still active in Manchester - they might have a list of DB
professionals/consultants you could converse with

- Any listings of firms that specialize in DBs/multi-user

- Third option. Sure worked for me over 30 years ago. Perhaps contact some
of the utility Electricity and Gas companies who have HUGE DBs, and are
using the software you want to use. (In our case at Debenhams we needed to
put in a new Food A/P (Bought Ledger). A few of us used our contacts and
although they were competitive retailers, managed to get visits to United
Dairies (small supermarkets in London area), MacFisheries, Tesco etc..
Surprisingly,  people were very 'open' - nothing secretive, and told us
what we wanted to know and gave us documentation. No - we didn't come out
with arms full of source code - but the verbal and documentary info we got
was relevant.

Jimmy, Calgary AB
```

##### ↳ ↳ Re: Database versus COBOL indexed files

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-30T00:06:05+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NFyb9.139400$eK6.4145663@twister.austin.rr.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <3D6EA31E.B4EE4868@shaw.ca>`

```
Sure, but there really isn't enough information there to make a judgment call.
Take for instance, the platform he is talking about. A 30gb filesystem running on a
Widows 2000 implementation? That is just plain silly- W2K would not be able to
reliably handle an indexed file that size. So if you want to run it on W2K, break the file
sizes down to split that 30G file into 10 3 Gig files or something like that.

If you are on a Mainframe, AS/400, or in some case, a RS/6000 machine or the equivalent,
a 30gb indexed file is doable, though backup will sure be a pain in the a**.  Still, it will be
doable, and run very fast, depending upon the number of indices you need to operate,
the transaction rate, how it is being access (i.e. terminal, JDBC, etc., etc.,etc.)

30gb for DB/2 on almost any platform, outside of OS/2 is quite doable, and the response from a well designed and tuned system will
be fast and reliable. But, you will probably wind up doing some data
redesign. If all you want to do is stick a 30gb indexed file into a DBMS, then don't both. Just use it as
an indexed file.

Now you see why the answers are not flowing as thick as you might wish? I didn't even touch the capabilities of things like
segregating the data in DB/2 so that single table has the data for each geographic location in separately defined areas, or the
capability to eliminate an outside transaction processing system, or federated databases, or cross platform,or how you use explains
to get subsecond response on *every* query or database pooling for Web Access from something like WebSphere or.....

Ask your friend to provide more detail and I am sure that there will be more targeted answers.

-Paul


"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:3D6EA31E.B4EE4868@shaw.ca...
> Come on guys, Phillip posted a similar message at M/F Answer Exchange. I
> suggested he would probably get better coverage here, beyond what Bill and
…[44 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

- **From:** "Alexys Flores" <arflores1@earthlink.net>
- **Date:** 2002-09-01T23:19:18+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Wfxc9.544$LI2.35804@newsread2.prod.itd.earthlink.net>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <3D6EA31E.B4EE4868@shaw.ca> <NFyb9.139400$eK6.4145663@twister.austin.rr.com>`

```
Windows is not gear for realtime networking and multi-tasking application,
it only run well in single user mode.

Paul Raulerson <praulerson@hot.NOSPAM.rr.com> wrote in message
news:NFyb9.139400$eK6.4145663@twister.austin.rr.com...
> Sure, but there really isn't enough information there to make a judgment
call.
> Take for instance, the platform he is talking about. A 30gb filesystem
running on a
> Widows 2000 implementation? That is just plain silly- W2K would not be
able to
> reliably handle an indexed file that size. So if you want to run it on
W2K, break the file
> sizes down to split that 30G file into 10 3 Gig files or something like
that.
>
 If you are on a Mainframe(IBM S 4300, 3890 ES 9000, S/390, Z series),
AS/400(Correction Minicomputer not Mainframe), or in some case, a RS/6000
machine or the equivalent,a 30gb indexed file is doable, though backup will
sure be a pain in the a**.  Still, it will be doable, and run very fast,
depending upon the number of indices you need to operate, the transaction
rate, how it is being access (i.e. terminal, JDBC, etc., etc.,etc.)
>
> 30gb for DB/2 on almost any platform, outside of OS/2 is quite doable, and
the response from a well designed and tuned system will
> be fast and reliable. But, you will probably wind up doing some data
> redesign. If all you want to do is stick a 30gb indexed file into a DBMS,
then don't both. Just use it as
> an indexed file.
>
> Now you see why the answers are not flowing as thick as you might wish? I
didn't even touch the capabilities of things like
> segregating the data in DB/2 so that single table has the data for each
geographic location in separately defined areas, or the
> capability to eliminate an outside transaction processing system, or
federated databases, or cross platform,or how you use explains
> to get subsecond response on *every* query or database pooling for Web
Access from something like WebSphere or.....
>
> Ask your friend to provide more detail and I am sure that there will be
more targeted answers.
>
> -Paul
>
>
> "James J. Gavan" <jjgavan@shaw.ca> wrote in message
news:3D6EA31E.B4EE4868@shaw.ca...
> > Come on guys, Phillip posted a similar message at M/F Answer Exchange. I
> > suggested he would probably get better coverage here, beyond what Bill
and
> > Richard have already written. Come on you DB2 users - any comments ?
> >
…[21 more quoted lines elided]…
> > I checked back on Answer Exchange and see you are in Worcs. Boy ! Do a
lot
> > of our American friends have trouble pronouncing that one. Knowing you
are
> > in UK, following is relevant.
> >
…[5 more quoted lines elided]…
> > - Third option. Sure worked for me over 30 years ago. Perhaps contact
some
> > of the utility Electricity and Gas companies who have HUGE DBs, and are
> > using the software you want to use. (In our case at Debenhams we needed
to
> > put in a new Food A/P (Bought Ledger). A few of us used our contacts and
> > although they were competitive retailers, managed to get visits to
United
> > Dairies (small supermarkets in London area), MacFisheries, Tesco etc..
> > Surprisingly,  people were very 'open' - nothing secretive, and told us
> > what we wanted to know and gave us documentation. No - we didn't come
out
> > with arms full of source code - but the verbal and documentary info we
got
> > was relevant.
> >
…[4 more quoted lines elided]…
>
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 4)_

- **From:** "JerryMouse" <nospam@bisusa.com>
- **Date:** 2002-09-02T02:57:49+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NsAc9.353166$m91.14064091@bin5.nnrp.aus1.giganews.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <3D6EA31E.B4EE4868@shaw.ca> <NFyb9.139400$eK6.4145663@twister.austin.rr.com> <Wfxc9.544$LI2.35804@newsread2.prod.itd.earthlink.net>`

```

"Alexys Flores" <arflores1@earthlink.net> wrote in message
news:Wfxc9.544$LI2.35804@newsread2.prod.itd.earthlink.net...

> Windows is not gear for realtime networking and multi-tasking application,
> it only run well in single user mode.
>

That doesn't pass the giggle test.
```

##### ↳ ↳ Re: Database versus COBOL indexed files

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-09-02T02:51:22-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0209020151.72df9af0@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <3D6EA31E.B4EE4868@shaw.ca>`

```
"James J. Gavan" <jjgavan@shaw.ca> wrote in message news:<3D6EA31E.B4EE4868@shaw.ca>...
> Come on guys, Phillip posted a similar message at M/F Answer Exchange. I
> suggested he would probably get better coverage here, beyond what Bill and
…[3 more quoted lines elided]…
> 
Jimmy,

I haven't had time to look at CLC for the past few weeks but if you
feel there haven't been enough responses why not suggest the
correspondent search Google archives? The subject has been thrashed to
death over years...

For the file sizes he is talking about, Database is the way to go, but
there is no easy solution.

There have been some very good posts in this thread noting some of the
pitfalls, either way.

I smiled at your suggestion for him to contact some large Electricity
Companies, especially as he is based in Worcester.

I am currently Managing the IT for a section of just such a Utility
that is based in Birmingham, about 20 minutes drive from Worcester.
(It is one of the largest in the UK and a household name...)

You may be surprised to find that things have changed a bit in the
last 30 years <G>. There is NO COBOL used on the site. And NO indexed
files (COBOL based or otherwise).

The company's multi-million user base resides on ORACLE and SQL Server
DBs and we are in the process of moving to Siebel CRM as the "New
World" solution.(This will utilise ORACLE 11 for the database).

Our existing "Legacy" systems are based around Client/Server and
utilise VB, XML, ASP, DTS, JavaScript, Components (DCOM, ActiveX, OLE,
and Web Services [XML/SOAP]), and Visual Studio as the IDE. Legacy
applications are all Web Based and would be considered "cutting edge"
by many organisations; here they are already obsolete...(although the
New World Solution will also be Web Based)

Fortress COBOL is dead here and so is Fortress PL/1. There is one old
mainframe that churns out bills for our residential customers using a
system written in PL/1 many years ago. It is due for decommissioning
in about 3 months.

We are replacing the Waterfall with RAD and it is very successful (but
then, I would say that <G>)

I have been staggered by the skill of the staff here and my own
education has progressed in leaps and bounds. The concept of
processing files in COBOL is about as relevant as spitting when you
come to crossroads, or turning widdershins when the moon is full...
Part of a bygone era.

Mr Hickling should utilise Database technology.

End of story <G>.

Pete.






> Phil Hickling wrote:
> 
…[37 more quoted lines elided]…
> Jimmy, Calgary AB
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

- **From:** spamdump@nospam.noway.nohow (Ed Stevens)
- **Date:** 2002-09-03T12:34:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d74ab39.2592247@ausnews.austin.ibm.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <3D6EA31E.B4EE4868@shaw.ca> <b3638c46.0209020151.72df9af0@posting.google.com>`

```
On 2 Sep 2002 02:51:22 -0700, dashwood@enternet.co.nz (Peter E. C. Dashwood)
wrote:

<snip>
>The company's multi-million user base resides on ORACLE and SQL Server
>DBs and we are in the process of moving to Siebel CRM as the "New
>World" solution.(This will utilise ORACLE 11 for the database).
>
<snip>

That must be a very long-range project, seeing as how the current version of
Oracle's database is Oracle 9.  I haven't even seen a date for Oracle 10, much
less Oracle 11.

Now, if you're talking about Oracle *applications*, yes they are at v11, but you
*did* say "ORACLE 11 for the database."
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 4)_

- **From:** dashwood@enternet.co.nz (Peter E. C. Dashwood)
- **Date:** 2002-09-04T07:41:51-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<b3638c46.0209040641.35dfaee1@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <3D6EA31E.B4EE4868@shaw.ca> <b3638c46.0209020151.72df9af0@posting.google.com> <3d74ab39.2592247@ausnews.austin.ibm.com>`

```
Quite right, Ed. We are using Version 8.0.4 for some areas and version
9 is being trialled for others. I was mistaking Application versions
for Database Versions as you pointed out.

Pete.

spamdump@nospam.noway.nohow (Ed Stevens) wrote in message news:<3d74ab39.2592247@ausnews.austin.ibm.com>...
> On 2 Sep 2002 02:51:22 -0700, dashwood@enternet.co.nz (Peter E. C. Dashwood)
> wrote:
…[13 more quoted lines elided]…
> *did* say "ORACLE 11 for the database."
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 5)_

- **From:** spamdump@nospam.noway.nohow (Ed Stevens)
- **Date:** 2002-09-05T12:49:33+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3d77526f.57565845@ausnews.austin.ibm.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <3D6EA31E.B4EE4868@shaw.ca> <b3638c46.0209020151.72df9af0@posting.google.com> <3d74ab39.2592247@ausnews.austin.ibm.com> <b3638c46.0209040641.35dfaee1@posting.google.com>`

```
And to make sure there's no other misunderstandings, I *did* forget to put a
'<grin>' at the end of that . . .

<grin>


On 4 Sep 2002 07:41:51 -0700, dashwood@enternet.co.nz (Peter E. C. Dashwood)
wrote:

>Quite right, Ed. We are using Version 8.0.4 for some areas and version
>9 is being trialled for others. I was mistaking Application versions
…[20 more quoted lines elided]…
>> *did* say "ORACLE 11 for the database."
```

#### ↳ Re: Database versus COBOL indexed files

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-08-30T04:29:37+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<RwCb9.42601$Ke2.2965549@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com>`

```

"Phil Hickling" <philhickling@compuserve.com> wrote in message
news:6a371be2.0208290523.13ca39d9@posting.google.com...
> What are the relative advantages and disadvantages of an sql database
> system as compared with COBOL indexed files?
…[11 more quoted lines elided]…
> and indexed files cope with 1000+ users, and 30Gb databases?

    I am a bit surprised that you are able to manage that many users with
vanilla Indexed files.  I have no experience with the sort of scale you are
talking about, although I have come somewhat close to your current scale.

    In my experience, Indexed files slow down and become corrupt more
often when you have too many concurrent users.  Of course, their are
many variables.  You could support many more users if most access
is read only.

    I am assuming that you are using standard file access over a network,
and am not using fileshare or Btrieve or whatever.
```

#### ↳ Re: Database versus COBOL indexed files

- **From:** philhickling@compuserve.com (Phil Hickling)
- **Date:** 2002-08-30T03:23:29-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a371be2.0208300223.6646123d@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com>`

```
Thanks for all your helpful comments so far.  Please keep them rolling
in.

In response to what I have recieved so far:
-  Fileshare is not being used.  I tried it once, but had severe
degradation in performance, and a serious file corruption within an
hour.  Maybe I should try again?
-  Most users access files for I-O, even if only reading.  I have just
seen others suggesting this is probably good - they experience slowing
down when mixing I-O and INPUT.
-  I am interested to note that alternate indexes MAY reduce
performance.  When I originally designed the system I created the 2
main data files with only 1 and 2 keys, and put other search keys into
separate files, with the suspicion that this would be more secure and
quicker.
-  I am sure that there must be many things I can do to tune the
current system, including Fileshare, web-enabling to force all
processing onto beefy servers and reduce network transfers of data,
upgrading servers etc.  I would love a secondary discussion on all
these sorts of issues, but for now my primary question is:  which
would perform faster, database or indexed files?  DOES ANYONE HAVE
EXPERIENCE OF BOTH, PARTICULARLY SPEED MEASUREMENTS TO COMPARE BOTH?

It is interesting that no-one has yet said in clear terms that, "other
things being equal, a database will outperform indexed files", or vice
versa!
```

##### ↳ ↳ Re: Database versus COBOL indexed files

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-30T12:29:56+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<8zJb9.169364$Yd.7417919@twister.austin.rr.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com>`

```
Jeesh - what does it take? Spell out your environment and then we can give you a clear answer.
The only possible answer right now is "sometimes a database is faster and sometimes indexed files
are faster."


"Phil Hickling" <philhickling@compuserve.com> wrote in message news:6a371be2.0208300223.6646123d@posting.google.com...
> Thanks for all your helpful comments so far.  Please keep them rolling
> in.
…[23 more quoted lines elided]…
> versa!
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

- **From:** "Tom Morrison" <t.morrison@liant.com>
- **Date:** 2002-08-30T18:28:30+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<iPOb9.7642$MF6.2880105676@newssvr11.news.prodigy.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <8zJb9.169364$Yd.7417919@twister.austin.rr.com>`

```
Phil,

I second the comment of my fellow Texan, Paul.  You have raised this
question in multiple venues, and gotten quite a bit of response.  Mine was
to your identical question in Tek-Tips COBOL forum.

Please be open to the possibility that:
1.  Indexed files are v-e-r-y good at what they do;
2.  Indexed files constitute a database; and
3.  It is possible to have SQL access to a database which uses indexed
files.

Please cooperate with all the folks here and provide more information.

Best regards,
Tom Morrison
Liant Software Corporation


"Paul Raulerson" <praulerson@hot.NOSPAM.rr.com> wrote in message
news:8zJb9.169364$Yd.7417919@twister.austin.rr.com...
> Jeesh - what does it take? Spell out your environment and then we can give
you a clear answer.
> The only possible answer right now is "sometimes a database is faster and
sometimes indexed files
> are faster."
>
>
> "Phil Hickling" <philhickling@compuserve.com> wrote in message
news:6a371be2.0208300223.6646123d@posting.google.com...
> > Thanks for all your helpful comments so far.  Please keep them rolling
> > in.
[snip]
```

##### ↳ ↳ Re: Database versus COBOL indexed files

- **From:** Frederico Fonseca <frederico_fonseca@eudoramail.com>
- **Date:** 2002-08-30T19:07:33+01:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<0ibvmu42fqglk8tlupl47a5ns78110kp22@4ax.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com>`

```
On 30 Aug 2002 03:23:29 -0700, philhickling@compuserve.com (Phil
Hickling) wrote:

>Thanks for all your helpful comments so far.  Please keep them rolling
>in.
…[23 more quoted lines elided]…
>versa!
Taken in consideration this information, and the fact that you did
mention that the network was a citrix/NT4 mix, I assume that the
servers you are using are Windows based. this on it's own will degrade
performance.

I can not speak for other situation, but I had customers that had to
change from Indexed file to Oracle/Informix databases, and performance
did degrade up to a certain point.
Basically the bigger the COBOL file, the less would be the difference
in performance.

If we consider the fact that the COBOL files had at that time a limit
of 2GB, and my customers had files this size (some had to split the
file in two (not fun at all!!)) changing to a Database system was the
only solution(this was on the Unix world).

For the above change we used the product from www.rldt.fr, which
allowed us to convert almost every file into a database format.
This is normally done without any change to the COBOL programs,
depending on the database used, on how you have the information on the
COBOL files, and in how you require them to be in the database side.

In our case some of the files were converted as a BIG field in the
database side, as we did not intended then to use the information from
the database side and doing otherwise would mean changing some of the
programs.

The way the product is now, with it's client/server option, it may
just be what you need to solve your problem.

Contact them, ask for an evaluation/demo, and measure performances
with BIG files, in both a Unix server, and a Windows server. And then
decide if you go this way(with minimal changes at the beginning, and a
possibility to change the programs to optimize performance), if you
keep as you are (1Gb file is not a lot in the Unix world, and I have a
customer with 600 users and several files that size and they work
fine, but Windows is another story...), or if you go completelly to
database systems.


FF
```

##### ↳ ↳ Re: Database versus COBOL indexed files

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-08-30T14:38:32-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0208301338.799b27c5@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com>`

```
philhickling@compuserve.com (Phil Hickling) wrote 

> In response to what I have recieved so far:
> -  Fileshare is not being used.  I tried it once, but had severe
> degradation in performance, and a serious file corruption within an
> hour.  Maybe I should try again?

Fileshare should improve performance by reducing network traffic and
having just one task attempting to update the index rather than having
several competing by using locks.

OTOH if it has been set to cater for rollbacks then it will by
journalising the updates.

> -  Most users access files for I-O, even if only reading.  I have just
> seen others suggesting this is probably good - they experience slowing
> down when mixing I-O and INPUT.

It should be OK as long as it has READ .. WITH NO LOCK, otherwise
there will be locks left on which may affect other users.

> -  I am interested to note that alternate indexes MAY reduce
> performance.  When I originally designed the system I created the 2
> main data files with only 1 and 2 keys, and put other search keys into
> separate files, with the suspicion that this would be more secure and
> quicker.

Alternate keys with large numbers of duplicate keys can be slow. 
Non-duplicate, or with few duplicates, alternate keys should be faster
and more secure than creating a separate file.

> -  I am sure that there must be many things I can do to tune the
> current system, including Fileshare, web-enabling to force all
> processing onto beefy servers and reduce network transfers of data,
> upgrading servers etc. 

Many years ago, when using 386 machines with 80Mbyte drives, I did
some performance testing on Multiuser-DOS systems.  Using different
cluster sizes on FAT partitions (I had a nice fdisk that would do
this) gave a _3_fold_ difference in performance between 2Kb clusters
and 16Kb clusters on the same drive.  But then that is because FAT is
a useless disk system.

Also with MF Level II Cobol files, building the data file as a
multiple of 128 bytes (ie record size of 126, 254, 510 etc), rather
than other sizes, gave a 40% improvement in performance.

Of course this is all obsolete - as long as you are using NTFS and not
FAT32.

Using data compression on files with sparse data (lots of spaces or
zeros) can not only save disk space but also is much faster to read
sequentially due to savings in disk block transfers.

>  I would love a secondary discussion on all
> these sorts of issues, but for now my primary question is:  which
> would perform faster, database or indexed files?  DOES ANYONE HAVE
> EXPERIENCE OF BOTH, PARTICULARLY SPEED MEASUREMENTS TO COMPARE BOTH?

How long is a piece of string ?

Given that there are vast differences between performances of database
systems, even with the same data and on the same machine then you will
never get an answer, and even if someone says that they got a 10 fold
improvement on going from ISAM to Database X that will not indicate
that you would get that, and in fact you could get severve
degradation.

> It is interesting that no-one has yet said in clear terms that, "other
> things being equal, a database will outperform indexed files", or vice
> versa!

It won't, nor will vice versa.

If you are really going to have 10x users and thus 10x volume and
traffic then you need to make serious changes to your systems.  Start
by measuring actual traffic - LAN volumes, disk accesses, CPU usage,
delays, clashes, response times, in fact everything.  Then apply
queueing theory until you can build a model that gives the answers
that you have measured.
Next put in the expected volumes and transactions and be amazed at how
the response times with go expontial (which of course will bring down
the actual transactions per day to the achievable level).

Then you will have numbers that will indicate the type of resources
required in terms of LAN blocks per second, disk accesses per second,
server CPU power.

By knowing the actual resource usage for each type of file access (FAT
table reads, index block accesses, LAN traffic, data blocks) then you
can experiment with several different database systems such as DB/2,
Oracle, PostgreSQL, FileShare in order to measure those same factors.

Eventually you may be able to come up with an approximation of
requirements for _your_ pattern of data usage.
The other approarch is to keep fiddling until either you find ways of
improving the system or there is complete collapse on increasing
volumes.
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

- **From:** qcblsrc@worldnet.att.net (John)
- **Date:** 2002-08-31T11:00:59-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<a2cb1565.0208311000.71e36a18@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com>`

```
I have tested a 10 million record file using Fujitsu COBOL for Windows
on an indexed file. I also tested accessing the same file using MS SQL
Server with a stored procedure running random SQL statements, both to
retrieve random records.  The COBOL indexed file outperformed the SQL
statements and SQL Server by about 100 to 1.  There is just no
comparison.  SQL Server in Windows requires intensive memory operation
which degraded performance.  This theme is common across all 4GL
languages from Microsoft.  Java suffers the same fate when running in
a MS environment.

I recommend sticking with COBOL indexed files in whichever platform
you run.
I'm going to be flamed for this !!

Regards,

QCBLSRC@wideopenwest.com









riplin@Azonic.co.nz (Richard) wrote in message news:<217e491a.0208301338.799b27c5@posting.google.com>...
> philhickling@compuserve.com (Phil Hickling) wrote 
> 
…[95 more quoted lines elided]…
> volumes.
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 4)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-08-31T22:18:11+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<Dgbc9.383203$q53.12650498@twister.austin.rr.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com> <a2cb1565.0208311000.71e36a18@posting.google.com>`

```

No flame - however, DB/2 under Windows does a much better job that SQL Server does
on a high transaction rate process. Especially if you do an explain on the query you are using and
tune for it. On my 13 million record test database (it is full of address records basically from the phone
book), on the PC, Microfocus tends to wipe up AcuCOBOL, IBM, and Fujitsu for indexed datafile
random retrievals. DB/2 wipes up Oracle, SQL Server 2000, MySQL, and Informix.

DB/2 is faster than Microfocus, albeit by only a few dozen seconds - about 212 seconds to be exact, that on a PIII 1.2Ghz machine
with a very fast SCSI disk. (The test is random retrieval of 1 million records.)

That would however, add up remarkably fast were that system in production and running 24X7. Since the
timing it is designed to test runs only once per week, the only reason I implemented it in DB/2 instead of
MicroFocus was for ease of access from the Web. Now I have another reason, which is the pesky
MicroFocus licensing, which I disagree with and will no longer support.

-Paul

"John" <qcblsrc@worldnet.att.net> wrote in message news:a2cb1565.0208311000.71e36a18@posting.google.com...
> I have tested a 10 million record file using Fujitsu COBOL for Windows
> on an indexed file. I also tested accessing the same file using MS SQL
…[122 more quoted lines elided]…
> > volumes.
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 5)_

- **From:** philhickling@compuserve.com (Phil Hickling)
- **Date:** 2002-09-04T03:37:58-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<6a371be2.0209040237.41303c2c@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com> <a2cb1565.0208311000.71e36a18@posting.google.com> <Dgbc9.383203$q53.12650498@twister.austin.rr.com>`

```
Thank you again everyone for your comments - it is all very
interesting and helpful.

Paul, and others, have asked for more information about the
environment:
The system runs on a single NT4 server, with dual processors and loads
of memory.  Approximately 80 workstations running NT4 Workstation
connect during the online day - these get reasonable performance. 
Also a further 20 thin clients in remote offices connect via Citrix to
one of two Citrix Winframe servers, and thus into the main system -
these get barely acceptable performance.

The data is basically 350,000 names and addresses in one indexed file:
 200 Mb, compressed, 1 main key (our reference), and notes or history
of each case in another file:  1 Gb compressed, with several different
redefinitions of records for different data contents, 1 main key (our
reference), and 1 alternate key (a composite key, used for accessing
records sequentially in a different order than the main key).  We
needed to be able to search the main name and address file on 10
different fields:  name, 1 of 2 addresses, client, client's reference,
etc.:  this data doesn't change very often, so rather than have the
main data file with 10 alternate keys I created 10 separate indexed
files for the searches, approximately 10 Mb each.  There are a further
15 files with ancilary information, accessed only occassionally.

All files have fixed lenght records.  The main file is over 1110 bytes
long, the larger history file is 131 bytes.

The system is accessed by the 100 users throughout the working day,
viewing cases and their history, responding to phone calls, adding
history, etc.  There are several 'end of day' routines that take about
4 hours in total to run, reading right the way through the database,
moving cases on to the next stage, producing letters, invoices, etc.

The system is developed entirely with MicroFocus NetExpress.  All
files are NetExpress indexed files, most with compression, and with
single keys, or only 1 alternate.

File system is NTFS.  Hard disks are Raided, moderately fast SCSI
disks.

All files are opened for I-O when a user first logs in, and remain
open until they logoff, usually.  Locking is manual, and only done
when a user wants to update a record - in which case the record is
read or re-read with lock, changed and then immediately re-written.

We don't use transaction processing or rollbacks.  We would like to,
but as I said, when we tried Fileshare we had big problems!

We cope with the current performance, but would like it improved - who
wouldn't!  But we are faced with a possible 10 fold growth - and
recognise the current setup probably wouldn't cope.

I am an independant contractor - I designed and built the original
system single handedly, and have been maintaining it ever since.  The
client now has another programmer to help.  The client has raised the
question:  'Would we be better with a database?', but I have never
used one - hence the original question.

From the feedback so far, I suspect more beneficial changes would be
Fileshare and Unix, and also suspect web-enabling the application to
force a thin-client/fat server and reduce network traffic would help? 
I am sure I should also be analysing Lan volumes, disk accesses,
delays, clashes etc - but I have no experience or knowledge of how.

Question:  can anyone confirm that record sizes as a multiple of 128
bytes are no longer an advantage - I have often wondered about this?

Thank you,
Phil Hickling.
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 6)_

- **From:** "Paul Raulerson" <praulerson@hot.NOSPAM.rr.com>
- **Date:** 2002-09-04T12:17:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<9Rmd9.198798$Yd.8581287@twister.austin.rr.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com> <a2cb1565.0208311000.71e36a18@posting.google.com> <Dgbc9.383203$q53.12650498@twister.austin.rr.com> <6a371be2.0209040237.41303c2c@posting.google.com>`

```
Hey Phil - now the situation is a whole lot clearer. I'll tell you what I would do in this case,
which will probably be a bit different from what other people would do. <grin>

The main sticking point to your performance issue is a two fold issue; one is client access by Windows machines trying to drag that
file all over the network; two is simply that the Windows server is spending a lot of cycles running Windows.

Ultimately, you will want to go to a database, probably something like DB/2, but the reason won't be performance, it will be so that
you can deal with ad-hoc queries. You don't currently have that need, probably because you designed the system well in the first
place. The idea of using separate files and
just rebuilding them as necessary is, IMNSHO, a perfect fit for this kind of processing.

Now, some concrete recommendations:

Move the system over to a small UNIX system, I suggest an IBM pSeries B50 system, in a small rack. The base system with 18gigs of
disk is going to cost just over $3000, and will easily support the number of users  and the data size you predict. There is a single
assumption here, and that is the assumption that you do all the edits and such in a text mode, and do not utilize the GUI stuff.
(i.e. dialog or screen section stuff.)
For your users, get a copy of PuTTY (free terminal emulation) and work on the system till you have the emulation working exactly the
way you want it. You will probably need some UNIX help for this, but the task isn't hard. Takes a couple or three hours.

At this point, you run PuTTY from both your central NT fileserver and your Citrix clients. Since you have the thinnest of thin
clients here, everything will run fast. (We run about a 100 users from Citrix and they are fast fast fast... faster in fact, than
the non-Citrix Windows machines.)

You should not even have to recompile the source code for this, and the data files should FTP over from the NT machine to the UNIX
machine unchanged as well. All you will need is a MF runtime for the AIX machine.

Now that you have it moved and have accounted for the projected growth (and by the way, now have a server under 24X7 OnSite warranty
for at least the first year...) you can start working on moving it towards a database if you wish, say DB/2.

Now if you have a GUI interface, this won't work, and the best choice is to go ahead and move it to a database now. It will be
slower than the file access, but not because of the database. It will be the
ODBC  (or whatever way you integrate SQL) and the network that slow you down. Even in this case though, you should move the database
to a dedicated server, and preferably, a UNIX based server. The Linux version of DB/2 would serve in this instance.

I can probably make a AIX machine available for limited testing for you over the internet if you decide to explore that path.

Good luck.
-Paul




"Phil Hickling" <philhickling@compuserve.com> wrote in message news:6a371be2.0209040237.41303c2c@posting.google.com...
> Thank you again everyone for your comments - it is all very
> interesting and helpful.
…[67 more quoted lines elided]…
> Phil Hickling.
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 6)_

- **From:** riplin@Azonic.co.nz (Richard)
- **Date:** 2002-09-04T12:47:12-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<217e491a.0209041147.674c724c@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com> <a2cb1565.0208311000.71e36a18@posting.google.com> <Dgbc9.383203$q53.12650498@twister.austin.rr.com> <6a371be2.0209040237.41303c2c@posting.google.com>`

```
philhickling@compuserve.com (Phil Hickling) wrote 

> needed to be able to search the main name and address file on 10
> different fields:  name, 1 of 2 addresses, client, client's reference,
> etc.:  this data doesn't change very often, so rather than have the
> main data file with 10 alternate keys I created 10 separate indexed
> files for the searches, approximately 10 Mb each. 

I would probably have done a single seaparte search file (of 100Mb)
with each of the type+reference+main key as primary key and main key
as alternate.
 
> There are several 'end of day' routines that take about
> 4 hours in total to run, reading right the way through the database,
> moving cases on to the next stage, producing letters, invoices, etc.

If the end of day involves checking status etc which is changed during
the day and only finds a small proportion (5%-10%) to do things with
then I would probably build a small 'action' file during the day with
one record per main record and a series of 'process type' flags
(delete record when all processing done). This should be faster than
reading through the whole file.
 
> We cope with the current performance, but would like it improved - who
> wouldn't!  But we are faced with a possible 10 fold growth - and
> recognise the current setup probably wouldn't cope.

Taking for example the daily processing of 4 hours: multiply by 10 and
???
 
> The client has raised the
> question:  'Would we be better with a database?', but I have never
> used one - hence the original question.

In general the answer would be 'No', it would probably not be faster
on the existing hardware.  However if a grunty RS6000 was running,
say, Oracle using raw partitions then there would be potential for
performance improvement.

For example by just opening files across the network the traffic
between the client machine and the server includes all the necessary
index blocks to do each index look up and update.  Using fileshare or
DB should reduce the traffic to just the actual data records.

Given that you say the Citrix clients are not acceptable it may be
that the NT server is severely overloaded and is using 100% CPU and
disk access with most going to managing the disk cache leaving little
CPU for the programs running there.  If you had two machines with one
(the existing) running the citrix terminals and the new just running
the file system then you would probably get improvements to both - as
long as it didn't overload the LAN - use a separate 100Mb segment.
 
> From the feedback so far, I suspect more beneficial changes would be
> Fileshare and Unix, and also suspect web-enabling the application to
> force a thin-client/fat server and reduce network traffic would help? 

Citrix/TSE is a real resource hog.  If it is only being used to run a
'dumb terminal' emulation then get rid of it.  Web serving is only OK
as long as the loading and file opening of CGI doesn't kill the
system.  Each interaction loads a fresh copy of the program unless you
use ISAPI or NAPI or something or use a CGI feed program piping
requests into an application server type program (eg like CICS). 
Could be a job for SP/2 thin client.

> I am sure I should also be analysing Lan volumes, disk accesses,
> delays, clashes etc - but I have no experience or knowledge of how.

You need to quantify the actual problems.  A LAN analyser should be
able to tell you LAN utilisation very quickly. Can you get disk
statistics from the server ?
 
> Question:  can anyone confirm that record sizes as a multiple of 128
> bytes are no longer an advantage - I have often wondered about this?

The advantage of x128 was entirely that it reduced the average number
of block reads because the records did not cross block boundries. 
With C2 indexed files there is a file header and record headers so
there is no mechanism to ensure alignment, and in any case you are
using compression so you could never get this.

I have no idea whether aligning with blocks would make any difference
with modern caching systems anyway.
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 7)_

- **From:** "James J. Gavan" <jjgavan@shaw.ca>
- **Date:** 2002-09-04T21:26:36+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<3D767C5C.30C7EF6F@shaw.ca>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com> <a2cb1565.0208311000.71e36a18@posting.google.com> <Dgbc9.383203$q53.12650498@twister.austin.rr.com> <6a371be2.0209040237.41303c2c@posting.google.com> <217e491a.0209041147.674c724c@posting.google.com>`

```


Richard wrote:

> > There are several 'end of day' routines that take about
> > 4 hours in total to run, reading right the way through the database,
…[8 more quoted lines elided]…
>

I'm 'small league', but I concur with that design approach Richard. Even if
he moved to a DB, it would seem to be that it would be effective there too.

In COBOL terms that would be an ISAM file containing a record with only the
PrimeKey. (As you suggest the PrimeKey could be what we would normally term
the Alternate Key).  I currently do the same thing, but not on a daily
basis  - read the ISAM sequentially (1) No records - you are finished, or
(2) records found, do updating (calculations) on main file; close and
re-open the 'flag' file as input then close. Even switching to SQL,  I
*might* retain the ISAM flag file concept.

Jimmy
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 6)_

- **From:** "Russell Styles" <RWSTYLES@worldnet.att.net>
- **Date:** 2002-09-05T06:31:09+00:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<NSCd9.53059$Ke2.3723889@bgtnsc04-news.ops.worldnet.att.net>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com> <a2cb1565.0208311000.71e36a18@posting.google.com> <Dgbc9.383203$q53.12650498@twister.austin.rr.com> <6a371be2.0209040237.41303c2c@posting.google.com>`

```

"Phil Hickling" <philhickling@compuserve.com> wrote in message
news:6a371be2.0209040237.41303c2c@posting.google.com...
> Thank you again everyone for your comments - it is all very
> interesting and helpful.
…[67 more quoted lines elided]…
> Phil Hickling.

    Have you thought about trying Btrieve instead of Fileshare.  Netexpress
supports Btrieve with (almost) no changes to source.  It should cut down
on network traffic, just like Fileshare, and should (hopefully) be more
reliable.  I have no idea how fast it would be.
```

###### ↳ ↳ ↳ Re: Database versus COBOL indexed files

_(reply depth: 6)_

- **From:** dlittlesr@yahoo.com (Dennis Little)
- **Date:** 2002-09-17T09:09:55-07:00
- **Newsgroups:** comp.lang.cobol
- **Message-ID:** `<315d2f8c.0209170809.66bc3c82@posting.google.com>`
- **References:** `<6a371be2.0208290523.13ca39d9@posting.google.com> <6a371be2.0208300223.6646123d@posting.google.com> <217e491a.0208301338.799b27c5@posting.google.com> <a2cb1565.0208311000.71e36a18@posting.google.com> <Dgbc9.383203$q53.12650498@twister.austin.rr.com> <6a371be2.0209040237.41303c2c@posting.google.com>`

```
Phil,
    What you'e done with Net Express and NT is very similar to what we
have done. We are also pondering the indexed files vs SQL...and we
tried Fileshare with poor results and file corruption. Has anyone had
success using Fileshare on Windows NT/2000 and NetExpress?? It appears
that it just doesn't work.
Dennis Little
```

---

[← Index](../README.md) · [Topics](../topics.md) · [Years](../years.md) · [Subjects](../subjects.md) · [Authors](../authors.md)
